# PROJECT ELYSIAN — DESIGN ROADMAP

## ▶ Where the project is (2026-09-25): the production phase
**What this repository is for** *(the owner, 2026-09-25)*. A world the owner builds, or has built, that pays them back in stories they enjoy. It combines canon, resources, tools, exemplars and a production process so that **agents can create media from it**: stories first, delivered as **ebooks**, with illustrations and other media to follow. The loop is: the world → agents → a work → **the owner's read** → the owner's notes back into the world and the tools. **The best stories are canon:** when a story is better for a change, canon changes, within the world's internal consistency (D-113).

**Step 13, the production loop (standing).** On branch `claude/production-loop`, in order:
1. **Purpose and canon policy.** This header, README, AGENTS.md; **D-113**, stories lead canon. ✅
2. **Ebooks.** `tools/build_ebook.py` plus a `book.json` per work, building to `library/<work>.epub` and validated with epubcheck. X01 first.
3. **Illustrations** (DOC-00I, drafted): Narnia-style inline spot illustrations. Generation waits for the owner's OpenRouter key.
4. **The cold-session test** (DOC-00H §15), run by the owner on the whole loop: request → brief → story → EPUB.
5. **Tooling** is managed with Nix flakes (`flake.nix`). ✅

The design history (Steps 1–12) follows unchanged.

---
**Where the design is (2026-09-22):** CLOSED at v3.2. Twenty-six documents, one hundred and two rulings, sixteen scenes (S013–S015 retired; numbers not reused). **The order of work has inverted (D-96):** from here a ruling is drafted only when a scene has demanded it, and is discharged by a scene before the next is made. Steps 1–11 are the record of the design phase; **Step 12 is the standing work.**

**Where to go next, in order.** Each step is scoped so it can be done in one working session and unblocks the ones after it.

---

## Step 1 — Rule on the audit — ✅ DONE 2026-09-19 (all nine, recommended options; CANON.md §11)
Nine decisions gate everything else. Suggested answers are in `AUDIT.md`; you only need to say yes/no/other for each:

| # | Decision | Suggested |
| :--- | :--- | :--- |
| 1 | VHF band (C-01) | 75–95 MHz λ/4 monopole |
| 2 | Radiotrophic pathway (P-01) | Demote to shielding + repair; strike 36 h mode |
| 3 | State B is unconscious (C-06) | Yes |
| 4 | Torpor draw & O₂ partition (P-02) | ~2 W, cooled core, Mb reserved for State B |
| 5 | Anaerobic = Crawl-Home Mode ≤30 W (P-04) | Yes |
| 6 | Add an O₂ bladder organ (P-04/C-05/P-07) | Yes — *vesica oxygenii*, ~1.5 L @ 400 kPa |
| 7 | Exhale-and-seal to ~40 kPa (P-07) | Yes |
| 8 | Albedo reflex for solar exposure (P-03) | Yes (cheap, no new organs) |
| 9 | Adopt `data storage spec.md` vault schema (G-10) | Defer until biology is locked |

Output: a short decision log appended to `CANON.md` §10. Then bump the affected docs to v1.1 with errata notes rather than rewriting them.

## Step 2 — DOC-01E.2: Integrated Vacuum Budget — ✅ LOCKED v1.0 (D-10, 2026-09-19)
The direct continuation of the work you just did. One coupled model instead of four separate calculations:
- State variables: core temperature, O₂ remaining by compartment (lung / bladder / Hb / Mb), H⁺ load.
- Loss terms: ear radiator *as a controllable 15–71 W throttle*, pelt radiation with fur insulation, solar load × albedo state, conductive dump when touching a bulkhead.
- Metabolic demand as a function of mode (Full / Crawl / Torpor) *and* core temperature (Q₁₀).
- Outputs: survival curves for the four canonical scenarios (shadow drift, shadow EVA, sun drift, sun EVA), plus the "go-straight-to-drift" case, and the crossover point where torpor beats action.
This produces the final "Operational Envelope Matrix" that 01E.1 §5 was reaching for, and it replaces the tables in 01E §4 and 01E.1 §5. It can be done as a short spreadsheet or a 40-line script; the doc then reports the curves.

## Step 3 — DOC-01C: Genomic Bio-Core & Neural Architecture — ✅ LOCKED v1.0 (D-20, 2026-09-19)
The keystone. Every social and tactical system in DOC-02/07/08/09 is a *consumer* of this organ, and it currently has no interior. Needs at minimum:
- Substrate: what tissue does DSP? (Options: engineered electrocyte stacks à la electric fish for the analog front-end; a dense, myelin-free "crystalline cortex" for the digital layer; or an admitted synthetic-biological hybrid — which is what The Unbound would be extending.)
- Memory: where long-term memory physically lives, what "Defrag" removes, what a Vault export *is* (→ closes G-05).
- The mesh protocol stack in one page (→ closes G-08): physical (01D) → link (Cluster handshake, PRF sync) → session (privacy firewalls, 256-bit auth) → application (telemetry hums, data bursts, MACTAC, genome compilation).
- Bandwidth and latency numbers consistent with 100 Mbps / <2.5 ms / 20 W peak.
- Failure modes: what The Silence *does* to the organ; what happens when a Cluster node dies mid-loop (→ seeds G-09).

## Step 4 — DOC-01A: Musculoskeletal, Locomotion & Microgravity Maintenance — ✅ LOCKED v1.0 (D-26, 2026-09-19)
- The immortal-in-0-G problem: what keeps bone density and muscle mass over centuries without gravity. (Candidates: Bio-Core-driven osteoblast signalling replacing mechanical load sensing; mandatory 1 G duty rotations into human sectors — which would give the Anchorites a physiological *reason* to stay near humans; or sleep-web isometric loading.)
- Gait catalogue: 0-G rail locomotion, 1-G quadrupedal sprint, transition-lock manoeuvre, tail-anchor mechanics.
- Grip and claw loads on carbon webbing; why the rails are cylindrical.
- Sprint power (150+ W) reconciled with 01B's ladder.

## Step 5 — DOC-01F: Sensory Systems — ✅ LOCKED v1.0 (D-31, 2026-09-19)
Short doc. Optical vision spec for a species that lives in the dark (likely tapetum, near-IR sensitivity, low acuity in colour); pit-node physical principle (recommend near-field capacitive/RF, which works in vacuum and explains the "pleasant buzz" in Scene 01); hearing to 22 kHz+ to match the whistle-choral; olfaction for a metal-hungry diet.

## Step 6 — DOC-02B: Lifecycle & Development — ✅ LOCKED v1.0 (D-37, 2026-09-19)
Birth → First Ping → Bio-Core boot → mesh-education → maturity → the first Defrag → injury/death/mourning in a Cluster. Immune model and human cross-infection go here. This is where the species stops being a spec and becomes people.

## Step 7 — DOC-10: Timeline & History — ✅ LOCKED v1.0 (D-50, 2026-09-19)
Only after biology is locked, because history explains *why* the biology is the way it is: who built them, when, for what contract, how many exist, what "now" is, what the first Cluster was. Establishes the era of the vignettes and gives the factions their origin events.

## Step 8 — Errata sweep — ✅ DONE 2026-09-19 (all v1.1 errata folded in place; vault schema deferred, D-9)
Fold every v1.1 errata into clean v2.0 docs; fix E-01/E-02; if Decision 9 is "yes", add frontmatter to every DOC and set up the folder layout from `data storage spec.md`.

---

## Step 9 — Scale, mass distribution & the extremities — ✅ LOCKED (D-68, D-69; 2026-09-20)

Triggered by a character-design question, then by a failed image generation. Two independent gaps surfaced: the 50 kg reference and the 1.4–1.6 m trunk had been set independently and never checked against each other, and the paws had no digit count, thumb or pad layout at all. Both re-derived from first principles.

| | Was | Is |
| :--- | :--- | :--- |
| Reference mass | 50 kg (45–65) | **60 kg (50–70)** |
| Trunk, chest → tail root | 1.4–1.6 m | **1.00–1.15 m** (ref 1.10) |
| Chest → tail tip | — | **1.90–2.05 m** |
| Standing heights | "~60 cm at the shoulder" | **withers 0.45 · shoulder 0.80 · head 1.15 · ears 1.28 m** |
| Tail | 0.8–1.0 m, mass unstated | **0.88 m, ~7 kg = 12 % of body** |
| Paws | "opposable digits", nothing else | **5 digits; D1 opposable ~100°, flat nail, no claw; D5 semi-divergent; three-jaw chuck** (D-69) |
| Hand vs paw | undifferentiated | **structurally distinct and always legible** (D-69) |
| Fascia radius (01E.1 §4) | 0.18 m → 2,700 N/m | **0.07 m → 1,050 N/m** |
| Vacuum envelope | 17 min / 42 min / 12 h | **unchanged — now provably mass-invariant** |

New results: a **12.1 L thoracic vault floor** sets a species mass floor at ~42 kg; grip-to-weight and State-A thermal margin set a ceiling near 80 kg; the tail's 12 % is forced independently by load split, vector-flip authority and the 450 N anchor rating; the paw's architecture is forced by having to clamp, run and ground all at once. `models/vacuum_budget.awk` is now parametrised by `M`, and the vacuum envelope is unchanged. Full rulings: `CANON.md` §20 and §21; derivations in `docs/DOC-01A` §3A and §3B; visual consequences in `docs/DOC-00C`.

---

## Step 10 — Silhouette-first packaging — ✅ LOCKED (D-73; 2026-09-21)

Triggered by rendering the D-68 geometry faithfully and getting a fat animal on a meerkat's torso. The 12.1 L vault floor had been stood up as a vertical thorax; laid along the body it is a fox's chest-to-loin taper on the same trunk, and the "upright humanoid torso" resolves into a *yoke* (arms at the shoulders, almost above the fore limbs) plus a *posture* (rearing by lumbar flexion). The stacked girdles become the bone box around the brain and Core.

| | Was | Is |
| :--- | :--- | :--- |
| Thorax | vertical 0.42 m column, 0.21 × 0.25 m | **horizontal 0.45 m, 0.21 × 0.23 m** |
| Loin | 0.85 m × 0.13 × 0.14 m | **0.65 m × 0.15 × 0.16 m** |
| Chest : loin girth | 1.7 (1.5 furred) | **1.4 (1.35 furred)** |
| Torso | "short upright humanoid torso" | **none — yoke + rearing** |
| Arm station | unspecified | **~10 cm ahead of, ~15 cm above the fore-leg joint** |
| Heights | 0.80 / 1.15 / 1.28 m "standing" | **those are reared; on all six: yoke 0.50, head ~0.70 m** |
| Legs | undifferentiated | **fore short/thick (load pair, 56 %), hind long/muscled (engine pair)** |
| Load split | 73/27 → 60/40 | **67/33 → 56/44** |
| Fascia radius | 0.07 m | **0.08 m** |
| Mass, trunk, tail, ears, vacuum envelope | — | **unchanged** |

Reference silhouette, now stated: *a fox's outline on a corgi's legs, drawn out to a marten's length.* DOC-00C rebuilt on it (v1.3); §14 keeps the prompt nouns that produced the right head and body, §15 item 0 records the failure.

---

## Step 11 — The six limbs as dual-role organs; the burn — ✅ LOCKED (D-74, D-75; 2026-09-21)

Triggered by preparing an artist's brief: every question an artist asks about a limb is a question about what the limb does, and the archive had described the limbs for 1 G only. Worked through as decisions, then derived.

| | Was | Is |
| :--- | :--- | :--- |
| Arm length | unspecified | **~0.50 m — reach parity with the forepaws** |
| Arm carriage at 1 G | unspecified | **loose at the walk, folded to the sternum at trot and bound** |
| Arm shoulder | unspecified | **primate-grade, full circumduction, elbows aft** |
| Yoke profile | unspecified | **~5 cm rise, hyena-grade** |
| Ventral windows | unspecified on all six | **hidden; revealed by rearing and splooting** |
| Fore-leg joint | unspecified | **hip-type socket, human-hip range; bends the arm way (elbow aft)** |
| Joint range | fixed | **build-tuned** (void looser, ground stiffer) |
| Anchoring | muscular endurance | **passive tendon lock in paws and tail** |
| Micro-G grab preference | unspecified | **forepaws by default; hands for precision** |
| Acceleration tolerance | asserted in DOC-01B §1, never computed | **never neurological; ~15–20 g seconds / ~8–10 g minutes, head tucked; burn posture; burn webs; hard-burn doctrine** |
| Fascia coverage | limbs + abdomen | **+ tail** |

**Next (not started):** `models/burn_budget.awk` — the fascia and the *vesica* each set a *time* under g, not a g-limit; the D-75 envelope is an estimate until that is coupled the way `vacuum_budget.awk` couples State A. Also still open from the artist brief: the reference individual's markings and iris colour (DOC-00C §16 leaves them open by design; the brief needs one answer).

---


---

## Step 12 — The writing phase — ▶ STANDING (D-96; 2026-09-22)

Triggered by `wargames/W03_the_kin_as_a_story_engine.md`, which tested the species against its *job* rather than its mechanisms and found the design sound and the ratio wrong: **ninety-six rulings, sixteen scenes,** in an archive whose stated purpose is stories and whose roadmap has said *the design is closed; the world is open* through three successive passes that each produced more rulings.

### The rule of order
1. **A ruling is drafted only when a scene has demanded it.** Not when an audit finds a silence — silences are now a legitimate state (see the H-register).
2. **Each new ruling is discharged by a scene before the next is made.** One in, one out.
3. **An H-item is closed by a scene or not at all.** A ruling that closes one is a bug, and the H-register in `AUDIT.md` exists to make that checkable.

### The dramatisation test — for triaging the existing ninety-six
Every ruling sorts into one of three, and the sort is maybe an hour's work over `CANON.md` §11–§28:
- **Infrastructure** — invisible by design, no debt. D-10 (the vacuum budget), D-68 (the mass floor), D-1 (the band plan), the whole physics spine. These are load-bearing and should never appear on a page as themselves.
- **Discharged** — a scene already carries it. D-79/S016, D-70/S007, D-34/S008, D-19/S011.
- **Undramatised** — a claim about *people* that has never once shown. This is the writing queue, not a defect list.

**See also `scenes/SLATE.md`** — the standing scene slate, written from the story side rather than the ruling side, with a stated *moment* for each. Where the two disagree, the slate usually has the better angle.

### The undramatised queue, best first
Each of these is a ruling the archive leans on and has never put on a page.

| Ruling | What has never been shown | Shape |
| :--- | :--- | :--- |
| **D-83** | The grant-web — whose Reading key you hold, who holds yours. *Removal from a grant is the breakup with no other name.* The kinship map the species actually runs on. | The removal, from either side |
| **D-90** | Two claimants at a Reading for one name; custom settles it *in the frame — the one who took the most of hir*. | The loser's story |
| **D-76** | A Cluster tuning a child toward a posting, and an operator's bonus behind it. The ruling itself says *the first case is a scene*. | The compile log at a Weave |
| **D-77** | The gestation licence failing — the only miscarriage the Kin have, and currently a table row | Quiet, two parents |
| **D-82** | The night the dreams go flat; the Weaver who presides asks about the dreams first | The chosen ending, from the Weaver's side |
| **D-87** | An interrogation — a day verbatim per half hour, and the Cluster afterwards | An operator's dispute, not a court |
| **D-85** | The console: a human reading a Kin's mood off a screen and never off hir face | Human POV, ordinary day |
| **D-88** | The Alder piece — *[Off / by / one]* — played at a human funeral while the Kin stand with nothing to do | Either POV |

### The memory re-derivation (D-97…D-101, 2026-09-22)

Not a new pass under the rule of order — a **re-derivation**, on the D-73 precedent: the nightly Defrag failed on reading, and the audit trail showed it had never been derived at all (`AUDIT` M-01). Rebuilt from the makers' brief. The result changed the shape of the species' central mechanism and cost five documents a rewrite, and it is the last thing done before the writing phase resumes.

| | Was | Is |
| :--- | :--- | :--- |
| Tiers | two (live / archive) | **three — cortex / record / index** (D-97) |
| The cortex | emptied to a stub over weeks | **human, unmodified, lifelong** — where they live |
| The record | written nightly, selected | **continuous, verbatim, nothing omitted**; does not participate in cognition |
| The index | implicit | a fixed-width table of ~5×10⁴ stubs that **cycles** and never fills (D-104) |
| The superiority | "perfect recall" | **query, check, accumulation** |
| Retrieval | unspecified | seamless and exact; **never initiates** (D-98) |
| Data Rot | "facts kept, feeling lost" | **cortical, and a rolling ~175-year self** (D-104) — *not forgetful, unprompted*, and a **steady state, not a decline** |
| The night | the write | **consolidation + appraisal**; the trauma answer (D-100) |
| The veto | at the Defrag | **struck entirely (D-105)** — there is no veto and there never was; nothing a Kin lives can be kept off file |
| Sharing | "private codec", read as encryption | **hard transfers perfectly, soft is indexical** (D-99) |
| The Telling | a retelling | **a transfer at the hard tier** — a year in a week = 7.3 TB at 12 MB/s ✅ |
| External store | impossible | **capturable, undecodable** — the decoder is a grown organ (→ H-04) |
| Documentation flaw | designed | **emergent** (D-101) |
| Reading vs sending | unspecified | **one act — the cortex is the read head** (D-102), at **two rates** (D-103): cold (≈52×, seekable, free, and what §6I always described) and lived (1×, affect on, the only source of soft content) |
| What costs | *(implied: every use of the archive)* | **giving, not knowing** (D-103) — a checked fact is a second; an account has to be felt again to exist |
| Why a Reading is slow | asserted | **death takes the reader, not the book** — 12 MB/s is cortical; ≤10 kbps is what is left without one |

**Scene debt (as amended by D-103).** *The account asked for* — someone wanting not the fact but what it was like, and the Kin deciding whether to go back to 1× for hir. *The cheap check* — a fact settled in a second, mid-argument, and nobody remarking on it, because that is the ordinary case and no scene has shown it. *The unprompted elder* — someone else being the cue. *The reach for a thing that is not there* — a Kin in the worst hour of hir life knowing, exactly, that this is going on file and cannot be stopped (D-105). *The lag* — a Cluster realising they will never know how hir died. *The Weaver's index* — what it costs to take a stranger's year. *A Telling from the teller's side* — the week, and the hours hir chooses to live again inside it (D-102, D-103). *The Defrag* — an elder choosing which century hir keeps the feel of.

`models/` owes nothing; no physics number moved.

### Scene debt from D-91…D-95 (drafted the old way; owed under the new rule)

| Ruling | The scene it owes |
| :--- | :--- |
| **D-91** the override | Not H-01 — that stays open. The *affordable* version: a Kin overriding the ranking in a small way, in a frame, and the Cluster feeling the weather turn and not asking. |
| **D-92** coarse affect | A console and a human who cannot tell grief from fear, and a human beside him who can read ears and can. |
| **D-93** the Kin alone | Two: the guard slot offered to a stranger on a relay; and a Kin home from a long lone posting, reciting a decade hir cannot feel. |
| **D-94** the child's envelope | The fourteen-year-old at the airlock, written as the thing hir *could* do. (The archive has wanted this since DOC-02B; S008 approaches it from the other side.) |
| **D-95** after the burn | The first hour after a hard burn, worked in the dark; the human being told where to put his hands. |

### And choose the fuses (N-09 → H-10)
AF 550 currently has no live fuse — every dated event is history and *it has not yet mattered enough* describes a quiet now. Pick **two or three** from: the first posting-bonus tuning case (D-76); a Kin over a human crew (DOC-10 §6, *not yet common*); the extent of the Unbound's reconstruction (H-03); *Last Light* reaching Barnard's in AF 619 with Written aboard (D-52); the next Written's Reading (forty left); the operator's laboratory the Kin are watching (H-04). **Register them as lit, and resolve them only in scenes.**

### Still open as rulings (not blocking)
- **N-05** the perfect witness's blind spot — a restatement of D-80 as a rule about evidence. Draft it when a scene needs a Kin to *not* remember something.
- **N-06** the name-pool across light-years — D-90 against D-52. Draft it when an ark scene needs a name.
- `models/burn_budget.awk` — still unwritten (Step 11), and now owes a retinal recovery curve alongside the fascia and *vesica* times (D-95).
- The reference individual's markings and iris colour (Step 11, from the artist brief).
## Why this order
- **1 before 2**: you cannot build the integrated budget on inputs that are still disputed.
- **2 before 3**: the vacuum budget is nearly done and closing it clears your head for the hard one.
- **3 before 4–7**: the Bio-Core is the dependency of *everything* social; once it has an interior, the lifecycle, history, and factions can be written against real constraints instead of vibes.
- **7 last among content**: history written before the biology is locked will be rewritten.

## What NOT to do next
- Don't write more vignettes yet — three of the four existing ones already lean on Bio-Core behaviours that have no mechanism (Scene 02 especially).
- Don't expand factions or tactics — DOC-08/09 are adequate for their current depth and would just inherit the G-02 hole.
- Don't lock DOC-01E.1 at v1.0 as written; it is the best doc in the set *and* the one whose inputs need the most change.

---

## What comes next (not yet chosen)
The design is closed; the world is open. Candidates, in no order:
- **DOC-07 v2 / DOC-08 v2 depth** — the six arks (targets, dates, which still transmit), named habitats, the Belt.
- **Placeholder names** in DOC-10 (the foundation, Ilex, Sable, Spire Meridian, the tether works, *Long Reach*).
- ~~Writing primer~~ — done (DOC-00B).
- ~~Visual reference & image-gen kit~~ — done (DOC-00C).
- **Scenes the design asks for** (`scenes/README.md`): a Telling before transit torpor; the auditor who wants a PDF; the fourteen-year-old at the airlock; a Written speaking at a Weave; the Storm from inside a shelter.
- **Kin-code and the whistle channel** — does the private acoustic channel have its own grammar (DOC-04 open item).
- ~~Human-side outline~~ — done (DOC-12).
- **Vault schema** (D-9, deferred) if the Obsidian tooling is ever wanted.

### Scene debt from D-104 (Data Rot re-seated in the cortex)

| The scene it owes | Shape |
| :--- | :--- |
| **The overwriting** | A Kin notices a smell now means the wrong decade, works out by hard handle what it used to mean, gets the answer exactly, and feels nothing. |
| **The re-anchor** | A centennial Defrag from inside: being shown what already went, and choosing the few to carry forward at the cost of others. |
| **The elder moved by a stranger** | A Written runs hir own first year at 1×, is moved by it the way anyone is moved by someone else's life, and does not say so. |

### Scene debt from D-108…D-110 (where the arks came from)

| The scene it owes | Shape |
| :--- | :--- |
| **The eighty-year build** | One Cluster, one job, four generations of human supervisors who each believed they were dealing with a new crew. |
| **The file** | A Compact clerk opening a docket on a ship already at 3 % of lightspeed. Comic and then not. |
| **The Weavers at the Schism** | The argument they lost, from the losing side (D-110). |
| **H-13** | An operator moving to stop a yard. Closes a hole or is never written — the setting's only untold action. |
