#!/usr/bin/env python3
"""tells.py — measure the machine-prose tells in Project Elysian scenes.

Standard library only. Three commands:

    python3 tools/tells.py scene  scenes/S021_coming_wait.md     # one scene, with line refs; exit 1 if over budget
    python3 tools/tells.py corpus [--out reports/corpus.md]       # the whole collection: recycling, sameness, endings
    python3 tools/tells.py ledger                                 # one row per scene, for scenes/LEDGER.md
    python3 tools/tells.py baseline private/<work>/text           # measure a human reference text against the collection

What this measures and what it cannot are both in docs/DOC-00G §8. In one line:
it finds surface patterns and cross-scene recycling. It cannot tell whether a scene is
any good. A scene that passes is not thereby human; a scene that fails is not thereby bad.
The pattern table is tools/tells_patterns.tsv; provenance is research/R01.
"""
from __future__ import annotations

import argparse
import math
import re
import statistics
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERNS = ROOT / "tools" / "tells_patterns.tsv"
SCENE_GLOBS = ["scenes/S[0-9]*.md", "scenes/drafts/S[0-9]*.md"]

# Headings that end the prose and begin the apparatus.
APPARATUS = re.compile(r"^##\s+(Canon|Offers|Notes|Drift|Revision)", re.I)

# Per-1000-word budgets for "limited" kinds, and scene-level structure limits. See DOC-00G §8.
BUDGET = {
    "reframe": 1.0,
    "gnomic": 1.0,
    "explain": 0.5,
    "hedge": 2.0,
    "lexicon": 0.5,
    "trope": 1.5,        # 'limited' tropes only; 'rested' ones have budget zero
}
LIMITS = {
    "stinger_ratio": None,   # reported, not failed: Estee ends 60% of sections on one (research/R03 §1)
    "number_word_repeat": 4, # the same number word (three..ninety) more than max(this, words/350) times
    "one_sentence_par_ratio": 0.45,
    # Flow (narration only; dialogue excluded). Calibrated on Estee's novel (research/R03 §1A): and-chains
    # 1.0 per 100 sentences, subordinators per "and" 1.11. The collection's house cadence strings clauses
    # with "and" instead of ordering them; the owner read it as "disjointed, not quite full prose".
    "and_chain_per_100": 6.0,     # narration sentences with three or more "and", per 100 narration sentences
    "sub_per_and_min": 0.5,       # subordinators per "and" in narration
    # Chopped prose: the overcorrection of the flow rule (X01 ch. 5 r1 went to CV 0.71). Warned, not failed.
    # Estee's 10th percentiles, per chapter (research/R03; X01 debrief 2026-09-25): narration mean 10.6, CV 0.73.
    "narr_mean_len_warn": 10.6,
    "cv_len_warn": 0.73,
}

SUBORDINATORS = re.compile(r"\b(because|when|while|although|though|since|until|unless|after|before|so\s+that|if|"
                           r"whether|which|who|whose|where|as\s+soon\s+as|once)\b", re.I)

NUMBER_WORDS = ("three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
                "sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty "
                "ninety").split()     # 'hundred'/'thousand' excluded: they are the tail of every Kin date

# ", leaning on his agility, dances" — Reinhart et al. (PNAS 2025) found instruction-tuned models use
# present participial clauses at 2-5x the human rate. Words that merely end in -ing are excluded.
PARTICIPLE = re.compile(r",\s+(?!(?:thing|nothing|something|anything|everything|morning|evening|ceiling|during|"
                        r"being|king|ring|string|wing|spring|bring|sing|swing|sting|ping|ling|ding|awning)\b)"
                        r"[a-z]+ing\b", re.I)

# Pronouns are fixed by the style sheet (hir/she by POV), so they are excluded from voice profiles.
PRONOUNS = set("i me my mine we us our you your he him his she her hers hir hirs it its they them their".split())


# ─────────────────────────────────────────────────────────────── parsing

@dataclass
class Paragraph:
    line: int
    text: str
    section: int


@dataclass
class Scene:
    path: Path
    sid: str
    title: str
    pov: str
    form: str
    paragraphs: list[Paragraph] = field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n\n".join(p.text for p in self.paragraphs)

    @property
    def words(self) -> list[str]:
        return WORD.findall(self.text.lower())

    def sections(self) -> list[list[Paragraph]]:
        out: dict[int, list[Paragraph]] = defaultdict(list)
        for p in self.paragraphs:
            out[p.section].append(p)
        return [out[k] for k in sorted(out)]


WORD = re.compile(r"[a-z]+(?:['’][a-z]+)?", re.I)
SENT_SPLIT = re.compile(r"(?<=[.!?])[\"'”’*\]⟩)]*\s+(?=[\"'“‘*\[⟨(]*[A-Z0-9])")


def parse_scene(path: Path) -> Scene:
    lines = path.read_text(encoding="utf-8").splitlines()
    title = lines[0].lstrip("# ").strip() if lines else path.stem
    sid = (re.match(r"S\d{3}", path.name) or [path.stem])[0]
    header = "\n".join(lines[:8])
    pov = _field(header, "POV")
    form = _field(header, "Form") or "Short story"

    # Skip the header block: title, then **Field:** lines and blanks, then an optional ---.
    i = 1
    while i < len(lines) and (not lines[i].strip() or lines[i].startswith("**")):
        i += 1
    if i < len(lines) and lines[i].strip() == "---":
        i += 1

    scene = Scene(path, sid, title, pov, form)
    section, buf, start = 0, [], None

    def flush():
        nonlocal buf, start
        if buf:
            scene.paragraphs.append(Paragraph(start, " ".join(s.strip() for s in buf), section))
        buf, start = [], None

    for n in range(i, len(lines)):
        ln = lines[n]
        if APPARATUS.match(ln):
            break
        if ln.strip() in ("---", "***", "* * *"):
            flush()
            section += 1
            continue
        if ln.startswith("#"):          # an in-prose section title (S019, S023)
            flush()
            if scene.paragraphs:
                section += 1
            continue
        if not ln.strip():
            flush()
            continue
        if start is None:
            start = n + 1
        buf.append(ln)
    flush()
    # Drop a trailing empty section left by a closing ---.
    return scene


def _field(header: str, name: str) -> str:
    m = re.search(r"\*\*" + name + r":\*\*\s*([^·\n*]+)", header)
    return m.group(1).strip() if m else ""


def sentences(text: str) -> list[str]:
    flat = re.sub(r"\s+", " ", text).strip()
    return [s for s in SENT_SPLIT.split(flat) if WORD.search(s)]


def scene_paths(args_paths: list[str] | None = None, globs: list[str] | None = None) -> list[Path]:
    if args_paths:
        return [Path(p) for p in args_paths]
    out: list[Path] = []
    for g in globs or SCENE_GLOBS:
        out.extend(sorted(ROOT.glob(g)))
    return out


# ─────────────────────────────────────────────────────────────── patterns

@dataclass
class Pattern:
    pid: str
    kind: str
    status: str
    rx: re.Pattern
    note: str


def load_patterns(path: Path | None = None) -> list[Pattern]:
    out = []
    for raw in (path or PATTERNS).read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.startswith("#"):
            continue
        cols = raw.split("\t")
        if len(cols) < 5:
            continue
        pid, kind, status, rx, note = cols[:5]
        out.append(Pattern(pid, kind, status, re.compile(rx, re.I | re.M), note))
    return out


@dataclass
class Hit:
    pat: Pattern
    line: int
    excerpt: str


def find_hits(scene: Scene, pats: list[Pattern]) -> list[Hit]:
    hits = []
    for p in scene.paragraphs:
        for pat in pats:
            for m in pat.rx.finditer(p.text):
                a, b = max(0, m.start() - 30), min(len(p.text), m.end() + 30)
                hits.append(Hit(pat, p.line, ("…" if a else "") + p.text[a:b].replace("\n", " ") + ("…" if b < len(p.text) else "")))
    return hits


# ─────────────────────────────────────────────────────────────── metrics

@dataclass
class Metrics:
    words: int
    sentences: int
    mean_len: float
    cv_len: float                 # sentence-length burstiness: stdev / mean
    one_sentence_pars: float
    stinger_ratio: float
    sections: int
    dialogue_share: float
    emdash_per_k: float
    and_chains: int               # sentences with four or more " and "
    participle_per_k: float       # ", verb-ing" clauses per 1000 words
    and_chain_per_100: float      # narration sentences with 3+ "and", per 100 narration sentences
    sub_per_and: float            # narration subordinators per "and"
    narr_mean_len: float          # mean narration sentence length (dialogue and Kin-code excluded)
    number_repeats: dict[str, int]
    opener_top: list[tuple[str, int]]
    ending: str


def measure(scene: Scene) -> Metrics:
    text = scene.text
    words = scene.words
    sents = sentences(text)
    lens = [len(WORD.findall(s)) for s in sents] or [0]
    mean = statistics.mean(lens)
    cv = (statistics.pstdev(lens) / mean) if mean else 0.0

    pars = scene.paragraphs
    one_sent = sum(1 for p in pars if len(sentences(p.text)) <= 1) / max(1, len(pars))

    secs = [s for s in scene.sections() if s]
    stingers = 0
    for s in secs:
        last = s[-1].text
        if len(WORD.findall(last)) <= 12 and len(sentences(last)) <= 2 and len(s) > 1:
            stingers += 1
    stinger_ratio = stingers / max(1, len(secs))

    quoted = sum(len(m) for m in re.findall(r"[\"“][^\"”]*[\"”]|\*\[[^\]]*\]\*?|⟨[^⟩]*⟩", text))
    dialogue = quoted / max(1, len(text))

    emd = text.count("—") + text.count(" -- ")
    and_chains = sum(1 for s in sents if len(re.findall(r"\band\b", s, re.I)) >= 4)
    participles = len(PARTICIPLE.findall(text))
    # Flow, narration only: paragraphs with no dialogue, Kin-code or ticket headers.
    narr = [p.text for p in pars if not re.search(r'["“”]', p.text) and not p.text.startswith(("*[", "—"))]
    nsents = [x for t in narr for x in sentences(t)]
    nchain = sum(1 for x in nsents if len(re.findall(r"\band\b", x, re.I)) >= 3)
    nands = sum(len(re.findall(r"\band\b", t, re.I)) for t in narr)
    nsubs = sum(len(SUBORDINATORS.findall(t)) for t in narr)
    and_chain = 100 * nchain / max(1, len(nsents))
    sub_per_and = nsubs / nands if nands else 9.99
    nlens = [len(WORD.findall(x)) for x in nsents] or [0]
    narr_mean = statistics.mean(nlens)

    wc = Counter(words)
    cap = max(LIMITS["number_word_repeat"], len(words) // 350)
    reps = {w: wc[w] for w in NUMBER_WORDS if wc[w] > cap}

    openers = Counter()
    for s in sents:
        m = WORD.search(s)
        if m:
            openers[m.group(0).lower()] += 1

    ending = pars[-1].text if pars else ""
    return Metrics(len(words), len(sents), mean, cv, one_sent, stinger_ratio, len(secs),
                   dialogue, 1000 * emd / max(1, len(words)), and_chains,
                   1000 * participles / max(1, len(words)), and_chain, sub_per_and, narr_mean, reps,
                   openers.most_common(4), ending)


# ─────────────────────────────────────────────────────────────── budgets

def warnings(m: Metrics, counting_pov: bool = False) -> list[str]:
    """Things a reader should look at that are not failures."""
    w = []
    if m.narr_mean_len < LIMITS["narr_mean_len_warn"] or m.cv_len < LIMITS["cv_len_warn"]:
        w.append(f"possibly chopped: narration mean {m.narr_mean_len:.1f} words, CV {m.cv_len:.2f} "
                 f"(Estee's 10th percentile {LIMITS['narr_mean_len_warn']} / {LIMITS['cv_len_warn']}); "
                 "a flow fix that shortens every sentence is the overcorrection (DOC-00G §2.7)")
    if counting_pov:
        for word, n in m.number_repeats.items():
            w.append(f"number words: '{word}' ×{n} (reported, not failed: --counting-pov)")
    return w


def judge(scene: Scene, hits: list[Hit], m: Metrics, counting_pov: bool = False) -> list[str]:
    """Return a list of budget failures (empty = within budget)."""
    fails = []
    per_k = 1000 / max(1, m.words)
    for h in hits:
        # A rested beat binds later scenes, not the one it came from: "origin S0xx" in the note exempts that scene.
        if h.pat.status == "rested" and f"origin {scene.sid}" in h.pat.note:
            continue
        if h.pat.status in ("banned", "rested"):
            fails.append(f"{h.pat.status.upper()} {h.pat.pid} ({h.pat.note}) at L{h.line}")
    by_kind = Counter(h.pat.kind for h in hits if h.pat.status == "limited")
    for kind, n in by_kind.items():
        rate = n * per_k
        if kind in BUDGET and rate > BUDGET[kind]:
            fails.append(f"{kind}: {n} hits = {rate:.1f}/1000 words (budget {BUDGET[kind]})")
    # Documents in the world (a letter, minutes, a song) end on sign-offs and short lines by their nature.
    documentary = re.search(r"letter|minutes|song|log|transcript", scene.form + " " + scene.title, re.I)
    if LIMITS["stinger_ratio"] and not documentary and m.sections >= 3 and m.stinger_ratio > LIMITS["stinger_ratio"]:
        fails.append(f"stingers: {m.stinger_ratio:.0%} of sections end on a short one-liner (limit {LIMITS['stinger_ratio']:.0%})")
    if not documentary and m.one_sentence_pars > LIMITS["one_sentence_par_ratio"]:
        fails.append(f"one-sentence paragraphs: {m.one_sentence_pars:.0%} (limit {LIMITS['one_sentence_par_ratio']:.0%})")
    if not counting_pov:     # a teller who counts for a living (a quartermaster) is exempt, and reported instead
        for w, n in m.number_repeats.items():
            fails.append(f"number tic: '{w}' ×{n}")
    if m.and_chain_per_100 > LIMITS["and_chain_per_100"]:
        fails.append(f"flow: {m.and_chain_per_100:.1f} and-chained narration sentences per 100 (limit {LIMITS['and_chain_per_100']}; "
                     "order the clauses: because / when / so / which)")
    if m.sub_per_and < LIMITS["sub_per_and_min"]:
        fails.append(f"flow: {m.sub_per_and:.2f} subordinators per 'and' in narration (min {LIMITS['sub_per_and_min']}; "
                     "the ideas are laid side by side instead of ordered)")
    return fails


# ─────────────────────────────────────────────────────────────── voice profile

def profile(words: list[str], vocab: list[str]) -> list[float]:
    c = Counter(words)
    n = max(1, len(words))
    return [c[w] / n for w in vocab]


def burrows_delta(profiles: dict[str, list[float]]) -> dict[tuple[str, str], float]:
    """Burrows's Delta over the most-frequent-word profiles: mean |z_a - z_b|. Lower = more alike."""
    keys = list(profiles)
    dims = len(next(iter(profiles.values())))
    mu = [statistics.mean(profiles[k][d] for k in keys) for d in range(dims)]
    sd = [statistics.pstdev([profiles[k][d] for k in keys]) or 1e-9 for d in range(dims)]
    z = {k: [(profiles[k][d] - mu[d]) / sd[d] for d in range(dims)] for k in keys}
    out = {}
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            out[(a, b)] = sum(abs(x - y) for x, y in zip(z[a], z[b])) / dims
    return out


# ─────────────────────────────────────────────────────────────── recycling

def ngrams(words: list[str], n: int) -> set[tuple[str, ...]]:
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def recycled(scenes: list[Scene], n: int, min_scenes: int) -> list[tuple[str, list[str]]]:
    where: dict[tuple[str, ...], set[str]] = defaultdict(set)
    for s in scenes:
        for g in ngrams(s.words, n):
            where[g].add(s.sid)          # drafts of one scene share a sid and so never count as recycling
    rows = [(" ".join(g), sorted(v)) for g, v in where.items() if len(v) >= min_scenes]
    # Drop n-grams wholly contained in a longer reported one would need another pass; keep it simple,
    # but drop rows that are all stopwords of length < 5, which are grammar, not voice.
    rows.sort(key=lambda r: (-len(r[1]), r[0]))
    return rows


# ─────────────────────────────────────────────────────────────── reports

def report_scene(path: Path, pats: list[Pattern], corpus: list[Scene] | None = None,
                 counting_pov: bool = False) -> tuple[str, bool]:
    s = parse_scene(path)
    hits = find_hits(s, pats)
    m = measure(s)
    fails = judge(s, hits, m, counting_pov)
    out = [f"# tells — {s.sid} {s.title}", "",
           f"POV: {s.pov or '?'} · Form: {s.form} · {m.words} words · {m.sentences} sentences · {m.sections} sections", ""]
    out += ["## Budget", ""]
    out += ([f"- ✗ {f}" for f in fails] or ["- ✓ within budget (this proves nothing about quality — DOC-00G §8)"])
    out += [f"- ⚠ {w}" for w in warnings(m, counting_pov)]
    out += ["", "## Shape", "",
            f"- sentence length: mean {m.mean_len:.1f} words (narration {m.narr_mean_len:.1f}), variation (CV) {m.cv_len:.2f} "
            "(Estee 13.3 / 13.8 / 0.80)",
            f"- one-sentence paragraphs: {m.one_sentence_pars:.0%}",
            f"- sections ending on a short one-liner: {m.stinger_ratio:.0%}",
            f"- dialogue share of characters: {m.dialogue_share:.0%}",
            f"- em dashes per 1000 words: {m.emdash_per_k:.1f}",
            f"- sentences with four or more 'and': {m.and_chains}",
            f"- participial clauses (', verb-ing') per 1000 words: {m.participle_per_k:.1f}",
            f"- flow (narration): and-chained sentences {m.and_chain_per_100:.1f}/100 · subordinators per 'and' {m.sub_per_and:.2f} "
            "(Estee 1.0 · 1.11)",
            f"- commonest sentence openers: {', '.join(f'{w} ×{n}' for w, n in m.opener_top)}",
            f"- final paragraph: “{m.ending[:220]}{'…' if len(m.ending) > 220 else ''}”", ""]
    out += ["## Hits", ""]
    by_kind: dict[str, list[Hit]] = defaultdict(list)
    for h in hits:
        by_kind[h.pat.kind].append(h)
    for kind in ("explain", "trope", "reframe", "gnomic", "lexicon", "hedge"):
        if not by_kind.get(kind):
            continue
        out.append(f"### {kind} ({len(by_kind[kind])})")
        for h in sorted(by_kind[kind], key=lambda h: h.line):
            out.append(f"- L{h.line} `{h.pat.pid}` {h.pat.status}: {h.excerpt}")
        out.append("")
    if corpus:
        others = [c for c in corpus if c.sid != s.sid]
        mine = {g for g in ngrams(s.words, 6)}
        shared = defaultdict(set)
        for o in others:
            for g in mine & ngrams(o.words, 6):
                shared[" ".join(g)].add(o.sid)
        if shared:
            out += ["## Recycled from other scenes (6-word runs)", ""]
            for g, ids in sorted(shared.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:25]:
                out.append(f"- “{g}” — also in {', '.join(sorted(ids))}")
            out.append("")
        # Voice distance: is this narrator distinguishable from the rest of the collection?
        pool = [c for c in corpus if len(c.words) > 600 and c.sid != s.sid] + [s]
        pool += [c for c in corpus if c.sid == "S012" and len(c.words) > 600 and s.sid != "S012"]
        vocab = [w for w, _ in Counter(w for c in pool for w in c.words if w not in PRONOUNS).most_common(150)]
        profs = {c.path.name: profile(c.words, vocab) for c in pool}
        d = burrows_delta(profs)
        key = s.path.name
        mine_d = sorted((v, (b if a == key else a)) for (a, b), v in d.items() if key in (a, b))
        mine_d = [(v, k) for v, k in mine_d if not k.startswith(s.sid)]
        s012 = [k for k in profs if k.startswith("S012")]
        anchor = d.get(tuple(s012)) or d.get(tuple(reversed(s012))) if len(s012) == 2 else None
        out += ["## Voice distance (Burrows's Delta, 150 most-frequent non-pronoun words)", "",
                f"- nearest: {', '.join(f'{k[:4]} {v:.2f}' for v, k in mine_d[:3])}",
                f"- anchor (S012 ↔ S012alt, one narrator, two drafts): {anchor:.2f}" if anchor else "- anchor unavailable",
                "- A different narrator at or below the anchor sounds like the same person (DOC-00H Stage 4).", ""]
        if anchor and s.form and len(s.words) > 600:
            # Delta is noisy on short texts, so: fail when clearly below the anchor, or at/below it against two
            # or more scenes; a single borderline match is a warning for the cold reader and the owner.
            close = [(v, k) for v, k in mine_d if v <= anchor]
            if close and (len(close) >= 2 or close[0][0] <= 0.9 * anchor):
                fails.append("voice: as close as one narrator's two drafts to " +
                             ", ".join(f"{k[:4]} ({v:.2f})" for v, k in close) + " — back to Stage 3 with the voice card")
            elif close:
                out.insert(out.index("## Voice distance (Burrows's Delta, 150 most-frequent non-pronoun words)") + 2,
                           f"- ⚠ borderline: {close[0][1][:4]} ({close[0][0]:.2f}) — have the cold reader and owner check the voice")
            # Rewrite the budget block now that voice has been judged.
            i = out.index("## Budget") + 2
            j = out.index("## Shape") - 1
            out[i:j] = [f"- ✗ {f}" for f in fails] or ["- ✓ within budget (this proves nothing about quality — DOC-00G §8)"]
    return "\n".join(out), not fails


def report_corpus(pats: list[Pattern]) -> str:
    scenes = [parse_scene(p) for p in scene_paths()]
    scenes = [s for s in scenes if s.paragraphs]
    out = ["# tells — collection report", "",
           f"{len(scenes)} scene files · {sum(len(s.words) for s in scenes):,} words of prose.",
           "Generated by `python3 tools/tells.py corpus`. Read with DOC-00G; the numbers point, they do not judge.", ""]

    # 1. Budget table
    out += ["## 1. Per-scene budget", "",
            "| Scene | POV | Words | Reframe /k | Gnomic /k | Explain | Rested tropes | Stingers | Sent. CV | Partic. /k | Number tics | Verdict |",
            "| :-- | :-- | --: | --: | --: | --: | --: | --: | --: | --: | :-- | :-- |"]
    trope_ledger: dict[str, list[str]] = defaultdict(list)
    endings, openings = [], []
    for s in scenes:
        hits = find_hits(s, pats)
        m = measure(s)
        k = 1000 / max(1, m.words)
        kinds = Counter(h.pat.kind for h in hits)
        rested = sum(1 for h in hits if h.pat.status == "rested" and f"origin {s.sid}" not in h.pat.note)
        fails = judge(s, hits, m)
        tag = s.sid + ("alt" if "ALT" in s.path.name else "")
        for h in hits:
            if h.pat.kind == "trope":
                trope_ledger[h.pat.pid].append(tag)
        nums = ", ".join(f"{w}×{n}" for w, n in m.number_repeats.items()) or "—"
        out.append(f"| {tag} | {(s.pov or '?')[:28]} | {m.words} | {kinds['reframe']*k:.1f} | {kinds['gnomic']*k:.1f} | "
                   f"{kinds['explain']} | {rested} | {m.stinger_ratio:.0%} | {m.cv_len:.2f} | {m.participle_per_k:.1f} | {nums} | {'✓' if not fails else f'✗ {len(fails)}'} |")
        endings.append((tag, m.ending))
        openings.append((tag, s.paragraphs[0].text if s.paragraphs else ""))

    # 2. Trope ledger
    out += ["", "## 2. Lore set-pieces across the collection", "",
            "How many scenes each stock beat appears in. A reader of the collection meets every one of these again.", "",
            "| ID | Beat | Status | Scenes |", "| :-- | :-- | :-- | :-- |"]
    for pat in pats:
        if pat.kind != "trope":
            continue
        ids = trope_ledger.get(pat.pid, [])
        uniq = sorted(set(ids))
        out.append(f"| {pat.pid} | {pat.note} | {pat.status} | {len(uniq)}: {' '.join(uniq) or '—'} |")

    # 3. Recycled phrasing
    out += ["", "## 3. Recycled phrasing", "",
            "### Seven-word runs shared by two or more scenes (near-verbatim reuse)", ""]
    r7 = recycled(scenes, 7, 2)
    out += [f"- “{g}” — {', '.join(ids)}" for g, ids in r7[:40]] or ["- none"]
    out += ["", "### Four-word runs found in five or more scenes (the house voice)", ""]
    r4 = [r for r in recycled(scenes, 4, 5)]
    out += [f"- “{g}” — {len(ids)} scenes" for g, ids in r4[:50]] or ["- none"]

    # 4. Number words
    out += ["", "## 4. Number words across the collection", ""]
    total = Counter()
    per = defaultdict(set)
    for s in scenes:
        c = Counter(s.words)
        for w in NUMBER_WORDS:
            if c[w]:
                total[w] += c[w]
                per[w].add(s.sid)
    out += [f"- {w}: {n} uses in {len(per[w])} scenes" for w, n in total.most_common(8)]

    # 5. Openings and endings side by side
    out += ["", "## 5. Every opening", ""]
    out += [f"- **{t}** — {o[:160]}{'…' if len(o) > 160 else ''}" for t, o in openings]
    out += ["", "## 6. Every ending", "",
            "Read these in a column. If they could be shuffled between scenes without anybody noticing, the collection has one ending.", ""]
    out += [f"- **{t}** — {e[:200]}{'…' if len(e) > 200 else ''}" for t, e in endings]

    # 7. Voice distance
    vocab = [w for w, _ in Counter(w for c in scenes for w in c.words if w not in PRONOUNS).most_common(150)]
    profs = {s.sid + ("alt" if "ALT" in s.path.name else ""): profile(s.words, vocab) for s in scenes if len(s.words) > 600}
    d = burrows_delta(profs)
    out += ["", "## 7. Voice distance between narrators", "",
            "Burrows's Delta on the 150 most frequent non-pronoun words (scenes over 600 words). Lower = more alike.",
            "No outside human baseline is in the repo, so read it *relatively*. The one in-house anchor is S012 ↔ S012alt:",
            "two drafts of one letter by one narrator. Any pair of *different* narrators at or below that figure is one voice.",
            "Delta is noisy on texts this short; treat single pairs as indicative, patterns as evidence.", ""]
    closest = sorted(d.items(), key=lambda kv: kv[1])[:10]
    out += [f"- {a} ↔ {b}: {v:.2f}" for (a, b), v in closest]
    anchor = d.get(("S012", "S012alt")) or d.get(("S012alt", "S012"))
    if anchor:
        below = [(a, b, v) for (a, b), v in d.items() if a[:4] != b[:4] and v <= anchor]
        out += [f"- anchor (same narrator, two drafts): {anchor:.2f}; different-narrator pairs at or below it: {len(below)}"]
    out += [f"- collection median: {statistics.median(d.values()):.2f}"]
    return "\n".join(out) + "\n"


def report_ledger(pats: list[Pattern]) -> str:
    out = ["| Scene | POV | Form | Words | Sections | Mean sent. | CV | Dialogue | Ending (first 60 chars) |",
           "| :-- | :-- | :-- | --: | --: | --: | --: | --: | :-- |"]
    for p in scene_paths():
        s = parse_scene(p)
        if not s.paragraphs:
            continue
        m = measure(s)
        out.append(f"| {s.sid} | {(s.pov or '?')[:24]} | {s.form[:14]} | {m.words} | {m.sections} | {m.mean_len:.1f} | "
                   f"{m.cv_len:.2f} | {m.dialogue_share:.0%} | {m.ending[:60].replace('|', '/')} |")
    return "\n".join(out) + "\n"


def text_as_scene(text: str, sid: str) -> Scene:
    """Wrap plain text (paragraphs split by blank lines, '* * *' section breaks) as a Scene."""
    sc = Scene(Path(sid + ".md"), sid, sid, "", "Short story")
    sec = 0
    for n, par in enumerate(text.split("\n\n"), 1):
        t = par.strip()
        if not t or t.startswith("#"):
            continue
        if re.fullmatch(r"[*\s~=-]+", t):
            sec += 1
            continue
        sc.paragraphs.append(Paragraph(n, t, sec))
    return sc


def report_baseline(folder: str, pats: list[Pattern]) -> str:
    """Compare a human reference text (a folder of chapter files) with the collection, rate for rate."""
    files = sorted(p for p in Path(folder).iterdir() if p.suffix in (".md", ".txt"))
    ref = [text_as_scene(p.read_text(encoding="utf-8"), p.stem) for p in files]
    ours = [s for s in (parse_scene(p) for p in scene_paths()) if len(s.words) > 900]

    def rates(scenes):
        kinds, words = Counter(), 0
        shape = defaultdict(list)
        for sc in scenes:
            m = measure(sc)
            words += m.words
            for h in find_hits(sc, pats):
                if h.pat.status != "watch":
                    kinds[h.pat.kind] += 1
            for k in ("mean_len", "narr_mean_len", "cv_len", "one_sentence_pars", "dialogue_share", "emdash_per_k", "participle_per_k"):
                shape[k].append(getattr(m, k))
            if m.sections >= 3:
                shape["stinger_ratio"].append(m.stinger_ratio)
        c = Counter(w for sc in scenes for w in sc.words)
        return kinds, words, {k: statistics.median(v) for k, v in shape.items()}, c

    rk, rw, rs, rc = rates(ref)
    ok, ow, os_, oc = rates(ours)
    out = [f"# baseline — {folder}", "", f"{len(ref)} files, {rw:,} words, against {len(ours)} scenes, {ow:,} words.", "",
           "| Measure | Reference | Collection | Ratio |", "| :-- | --: | --: | --: |"]
    for kind in ("reframe", "gnomic", "explain", "hedge", "lexicon"):   # tropes are Elysian-only beats
        a, b = 1000 * rk[kind] / rw, 1000 * ok[kind] / ow
        out.append(f"| {kind} per 1000 words | {a:.2f} | {b:.2f} | {b / a if a else float('inf'):.1f}× |")
    for k, fmt in (("mean_len", "{:.1f}"), ("narr_mean_len", "{:.1f}"), ("cv_len", "{:.2f}"), ("one_sentence_pars", "{:.0%}"), ("dialogue_share", "{:.0%}"),
                   ("emdash_per_k", "{:.1f}"), ("participle_per_k", "{:.1f}"), ("stinger_ratio", "{:.0%}")):
        out.append(f"| {k} (median) | {fmt.format(rs.get(k, 0))} | {fmt.format(os_.get(k, 0))} | |")
    for w in ("three", "four", "eleven"):
        out.append(f"| '{w}' per 10k words | {1e4 * rc[w] / rw:.2f} | {1e4 * oc[w] / ow:.2f} | |")
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("scene", help="report on one or more scenes; exit 1 if any is over budget")
    a.add_argument("paths", nargs="+")
    a.add_argument("--no-corpus", action="store_true", help="skip recycling and voice-distance checks")
    a.add_argument("--counting-pov", action="store_true",
                   help="the teller counts for a living (e.g. a quartermaster): report number words instead of failing them")
    a.add_argument("--patterns", help="pattern table to use instead of tools/tells_patterns.tsv (e.g. a side project's own)")
    a.add_argument("--corpus-glob", action="append", help="glob(s), relative to the repo root, for the comparison corpus "
                   "instead of the Elysian scenes; repeatable")
    b = sub.add_parser("corpus", help="collection-level report")
    b.add_argument("--out")
    sub.add_parser("ledger", help="one row per scene")
    c = sub.add_parser("baseline", help="measure a human reference text (folder of chapters) against the collection")
    c.add_argument("folder")
    args = ap.parse_args(argv)

    pats = load_patterns(Path(args.patterns) if getattr(args, "patterns", None) else None)
    if args.cmd == "scene":
        corpus = None if args.no_corpus else [c for c in (parse_scene(p) for p in scene_paths(globs=args.corpus_glob))
                                              if c.paragraphs]
        ok_all = True
        for p in args.paths:
            text, ok = report_scene(Path(p), pats, corpus, args.counting_pov)
            print(text)
            ok_all &= ok
        return 0 if ok_all else 1
    if args.cmd == "corpus":
        text = report_corpus(pats)
        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            Path(args.out).write_text(text, encoding="utf-8")
            print(f"wrote {args.out}")
        else:
            print(text)
        return 0
    if args.cmd == "baseline":
        print(report_baseline(args.folder, pats))
        return 0
    if args.cmd == "ledger":
        print(report_ledger(pats))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
