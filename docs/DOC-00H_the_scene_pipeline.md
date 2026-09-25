# PROJECT ELYSIAN: COMPREHENSIVE WORLD & SPECIES ARCHIVE
## Document ID: DOC-00H — The Scene Pipeline: How a Scene Gets Written
**Codename:** Project Elysian | **Species:** Aethela (*Homo Sapiens Successor*) | **Self-Name:** The Kin  
**Classification:** Tool, not canon. This is the process. The standard it serves is DOC-00G; the evidence is `research/R01`–`R02`.  
**Status:** v1.1, 2026-09-25: §13 long works, §14 the orchestrator's hand, §15 the cold-session test (from X01). v1.0, 2026-09-24. Run it with the `/scene` skill (`.claude/skills/scene/`). The cold read runs on its own with `/cold-read`.

---

### 0. THE SHAPE OF IT

```
  0 CHOOSE ─► 1 BRIEF ─► 2 PREDICT ─► 3 DRAFT ─► 4 LINT ─► 5 COLD READ ─► 6 REVISE ─► 7 OWNER ─► 8 CANON ─► 9 FILE
  (ledger)   (person,    (what a      (fresh     (tells.py) (fresh reader,  (cuts first,  (the only  (DOC-00B  (ledger,
              voice,      model        context,              no lore)        ≤2 rounds)    pass)      §12)      spent list)
              budget)     would do)    no checklist)
```

Each stage is there because of a specific finding:

| Stage | Answers | Evidence |
| :-- | :-- | :-- |
| 0 Choose against the ledger | one shape, one ending across the collection | R02 §4–§5; R01 §2 |
| 1 Brief from a person, not a ruling | scenes that demonstrate canon | R02 §2 |
| 1 Voice card | one narrator for everyone | R02 §1 |
| 2 Predictability pass | plots that echo what any model would write | R01 2.1 (Sui Generis) |
| 3 Fresh-context draft with exemplars | the house voice; the strongest measured lever | R01 §4 (Chakrabarty et al.) |
| 4 Lint | the surface tells | R01 §1; R02 §5–§8 |
| 5 Cold read by a reader with no lore | explaining, lore lectures, flat escalation | R01 1.1, 1.7, §3 |
| 6 Few, targeted revisions | each model pass adds model features | R01 1.5; DOC-00G §8 |
| 7 The owner passes the scene | model judges do not track expert judgement | R01 1.6 |
| 8 Canon last | the checklist as a composition menu | R02 §2, §6 |

---

### 1. STAGE 0: CHOOSE

Read the last five rows of `scenes/LEDGER.md` and the rotation rules in DOC-00G §6.2. Pick from `scenes/SLATE.md` **the entry that most changes the ledger**: a form, ending, tone or outcome the last five lack. If nothing on the slate does, write the need into the slate first.

Output: the slate entry, plus one line saying which ledger gap it fills.

### 2. STAGE 1: THE BRIEF

Written to `scenes/briefs/S0xx_brief.md` (template: `scenes/briefs/TEMPLATE.md`). The brief holds:

1. **The want.** One sentence, **no canon terms**: who wants what, today. (DOC-00G §2.1)
2. **The obstacle, and what goes wrong after the middle.** One sentence each. The second must not follow from the first. (§2.4)
3. **What is lost.** Who loses what, for good. (§2.4)
4. **The voice card.** All eight fields (§5.1). If the teller already exists, re-read their earlier scene and write the card to *differ* from the house voice (§5.3), not to match it.
5. **Form, tense, person, target length, ending type.** Each chosen against the ledger.
6. **The lore budget.** The ≤2 mechanics the plot turns on. Everything else in canon is texture or absent. (§4)
7. **Three details that demonstrate nothing.** Candidates only: the drafter may replace them, but must end with at least three. (§2.3)
8. **The exemplars.** Which shelf pages go in the drafter's context (DOC-00G §7; `research/SHELF.md`). **For a Kin or outsider POV, one passed X01 chapter comes first.**
9. **Canon excerpts.** Only the paragraphs of the docs that the two mechanics need, pasted in. **Not** DOC-00B whole, and **not** the §12 checklist.

The owner may write the brief, or approve one the pipeline drafts. **A brief the owner has seen makes a better scene than one they haven't.** This is the cheapest place for their judgement to go in.

### 3. STAGE 2: PREDICT

A **fresh** agent gets only the premise, the teller and the situation from the brief. No voice card and no exemplars. It is asked to write what a competent model would write:
- the five most likely versions of the scene, one paragraph each;
- the ten most likely beats, images and lines;
- the five most likely final lines.

These go into the brief as **the predictable list**. The drafter must not use any item on it, and where the draft converges on one anyway, the cold reader checks. This is a small, practical version of Xu et al.'s echo test (R01 2.1): what a model would resample is, by definition, what reads as generated.

### 4. STAGE 3: DRAFT

A **fresh** agent, never the one that wrote the brief or the predictable list, gets this context and nothing else:
1. the exemplar pages from the brief, **first**, whole;
2. DOC-00G §0, §2, §3 and §5.3 (the house voice card, labelled *do not write like this*);
3. the brief, including the predictable list and the canon excerpts;
4. the instruction to write the scene **once, straight through, in the teller's voice**, and stop.

It does not see DOC-00B §12, other scenes (apart from shelf pages), the ledger, or the canon appendices. It does not write the scene header, canon notes or a summary. It returns prose only.

### 5. STAGE 4: LINT

`python3 tools/tells.py scene <draft>`. Every *banned* and *rested* hit is fixed. Every over-budget *limited* kind is brought within budget, **or** the brief records why this teller talks that way. A voice distance clearly below the anchor (S012↔S012alt, computed in the same run; 0.85–0.92 depending on the pool), or at or below it against two or more scenes, sends the draft back to Stage 3 with the voice card, not to Stage 6. A single borderline match is a warning for the cold reader and the owner, because Delta is noisy on texts this short. A voice problem cannot be edited out line by line.

### 6. STAGE 5: COLD READ

Two readers, both fresh, run in parallel:

**The cold reader** (`/cold-read`) gets the prose and one line: *"a science-fiction story; invented terms are deliberate."* It gets no lore, no brief and no standard. It returns, with line references and **without rewriting anything**:
- where it lost interest, where it was confused, and where it correctly guessed what came next;
- every sentence that explains, interprets or states a theme;
- every line of dialogue that sounds written rather than said;
- the Chakrabarty edit categories, line by line: cliché, redundant exposition, purple prose, poor sentence structure, lack of specificity, awkward phrasing (R01 1.1);
- the worst moment in the scene, and whether it comes after the midpoint;
- **the first place it thought a model wrote this**, and why.

**The fidelity reader** *(added 2026-09-24)*, for any chapter or scene with a non-human viewpoint, or any part of a longer work: prompt `.claude/skills/cold-read/fidelity_prompt.md`, plus the relevant canon (DOC-00D for Kin voice), the continuity file and the previous chapter. It checks channels, species feel, shock, continuity and physical clarity, which are the things the cold reader, knowing no canon, cannot check.

**The collection reader** gets the draft's opening and closing paragraphs, the last five ledger rows, and §5–§6 of the current `tools/tells.py corpus` report. It answers one question: *what does this scene repeat?*

### 7. STAGE 6: REVISE

- **Cut first.** Most professional edits to LLM prose are deletions and replacements of exposition and phrasing, not additions (R01 1.1).
- **Targeted, not regenerated.** Rewrite the sentences and paragraphs that were marked, in the teller's voice. Never regenerate the whole scene: that brings back the tells the draft had lost, and the templates underneath survive anyway (R01 1.5).
- **At most two model revision rounds.** Every model pass adds model features. After two rounds the scene goes to the owner as it is, with the unresolved marks listed.
- Re-lint after each round.

### 8. STAGE 7: THE OWNER

The owner reads the scene cold, before any notes, and then reads the lint and cold-read summaries. The owner's marks, however brief (*"flat here"*, *"that's the voice again"*, *"love this"*), go into the brief file under **Owner's read**. They are the most valuable data the pipeline produces. Over time they should retune `tells_patterns.tsv`, the budgets and the shelf.

A scene the owner does not pass goes back to Stage 6 with their marks, or is dropped. Dropping is fine. The number is not reused (scenes/README).

### 9. STAGE 8: CANON

Only now: DOC-00B §12 as a checklist *against* the finished scene. Contradictions are fixed in the prose with the smallest edit possible, or the scene's header says it offers canon (the D-96 rule). The header block and the canon-consistency appendix are written now, by the checker.

### 10. STAGE 9: FILE

- The scene goes into `scenes/drafts/` (or `scenes/` once accepted), with the next number.
- Add its row to `scenes/LEDGER.md`.
- Add any new strong beat to `tools/tells_patterns.tsv` as `rested`, and any DOC-00F detail to DOC-00F §9.
- Regenerate the corpus report: `python3 tools/tells.py corpus --out reports/tells_latest.md`.
- Update `scenes/README.md` and mark the slate entry **[WRITTEN]**.

---

### 11. REVISING AN EXISTING SCENE

This is the same pipeline, entered at Stage 4, with three differences:
1. **Stage 1 is retrofitted.** Write the voice card and the want for the scene as it stands. If there isn't one, that is the revision.
2. **The cut list comes first.** The lint and the cold read mark lines, and the revision starts by deleting the marked explaining lines, codas and stingers, then reading what is left.
3. **A revision gets a new version header, never an overwrite** (scenes/README). The original stays until the owner chooses.

Recommended order for the existing collection, by how much each would gain: S021, S022, S023 (the most tells, and the three most alike), then S016 and S019.

---

### 12. WHAT THE PIPELINE COSTS, AND WHERE TO SPEND LESS

A full run is five or six agent contexts. For a small scene, skip Stage 2 if the brief is already strange, and run only the cold reader at Stage 5. **Never skip** the voice card, the lore budget, the fresh-context draft, the lint, or the owner.

---

### 13. LONG WORKS *(added 2026-09-25, from X01)*

A work in chapters runs the pipeline once per chapter, with a standing file set around it. Templates are in `templates/long_work/`. X01 (`offcanon/X01_equestria/`) is the worked example of every file.

| File | Holds | Updated |
| :-- | :-- | :-- |
| `BIBLE.md` | The owner's rules for this work (they outrank everything), the premise, the cast and each one's two-way pulls, and the whole-work predictable list | when the owner rules |
| `OUTLINE.md` | One section per chapter (POV, span, beats, threads ↑↓, ending type, *Not:*), the chapter ledger, and threads that run across chapters (X01: the wagon, magic) | before each chapter's brief |
| `VOICES.md` | A card per speaking character; **"How X talk among X"** for any non-human group; standing rules from the owner's reads (X01: pony pronouns; every POV has a person) | after every owner's read |
| `CONTINUITY.md` | **Calendar** (day numbers and dates), **numbers** (prices, money, distances, quantities), places and bearings, who holds what, who knows what | after every chapter, before the next brief |
| `tells_patterns_<work>.tsv` | The house patterns plus the work's own banned clichés and watch-list | when a new cliché shows |
| `briefs/CHnn_brief.md` | The chapter brief, then the logs: lint, cold read, fidelity read, revision rounds, owner's read | through the chapter's life |
| `chapters/CHnn.md` | The chapter | per round |

**What changes for a long work:**
- **The drafter gets the passed chapters.** The one before, and the best one in the same mode (Kin or outsider POV). This is why X01's quality rose chapter by chapter. It also carries VOICES.md, CONTINUITY.md, and the BIBLE's rules and premise.
- **Two readers, not one.** The **cold reader** (no lore) and the **fidelity reader** (`.claude/skills/cold-read/fidelity_prompt.md`: the canon, VOICES, CONTINUITY, the previous chapter, and any earlier chapter the new one retells). The fidelity reader caught the bow at Applejack's stall, the backwards walnut arithmetic, the bed positions and the day counts. The cold reader caught every structural tell.
- **Budget length at target × 1.3** (DOC-00G §10.9).
- **After the owner passes the last chapter**, compile the chapters into `<work>_full.md` for reading straight through.

### 14. THE ORCHESTRATOR'S HAND *(added 2026-09-25)*

In X01 the drafters and readers were fresh agents. **The orchestrator was not**, and several things that made the chapters good were done by hand. A cold session must do them too. They are listed here so that they don't depend on one session's memory.

1. **Write the brief from the owner's last read.** Fold every note into VOICES, CONTINUITY or the BIBLE *before* the next brief, so it binds the next chapter as well as this one.
2. **For every character-level ban, name the trait that survives** (DOC-00G §10.2). The brief's §4 has a field for it.
3. **Read the draft whole yourself before the readers do.** Note your own finds, such as the motive that contradicted ch. 1 or a speaker on the wrong side of the bed. The readers miss some.
4. **Check every number with code**: calories, prices and the running tab, distances, dates and day counts, loads. X01 caught a backwards walnut sum and a *ten days* that was four this way.
5. **Triage the readers.** Most findings are right. **Some are not**: the fidelity reader wanted the Crusaders kept out of the town's rumour, against the outline. Reject those with a one-line reason in the brief's log.
6. **Write the revision as a numbered list** (`templates/long_work/REVISE.md`):
   - a **keep list** of what must survive;
   - continuity fixes first;
   - line numbers that are the file's own;
   - a length range;
   - the style clause.
   Never ask for a regeneration.
7. **After the revision, read the whole chapter again, not the diff.** Re-lint it. Fix small things by hand: a pronoun, a tree species, a timing, a chopped run of sentences (DOC-00G §10.7). Log each hand fix.
8. **Run the world-logic pass** (DOC-00G §10.5) before the owner reads.
9. **Update CONTINUITY.md** with every new fact the chapter adds, the same day.
10. **Hand to the owner** with a short account: what happens, what the readers caught, what you did by hand, and anything you decided against a reader's advice.

**Where X01 departed from this document, for the record:**
- The orchestrator wrote the predictable lists itself instead of spawning a Stage 2 agent.
- The readers were not re-run after revisions.

Both saved time. The first is a bias risk, because the orchestrator's own expectations shape the list. **A cold session should follow Stage 2 as written until the cold-session test (§15) shows the shortcut is safe.**

### 15. THE COLD-SESSION TEST *(proposed 2026-09-25)*

X01's orchestrator had a long context: every owner note, every reader report, every hand fix. **That context may have helped in ways the files don't carry.** The files now carry what could be written down: the standard (DOC-00G §10), this process (§13–§14), the owner's standing notes (`research/OWNER_TASTE.md`), the templates, and X01 itself as the exemplar.

**The test.** A fresh session, started by the owner with no history, is given one prompt and nothing else, for example: *"Write a short standalone story about a Cluster, through the pipeline (`/scene`)."* It works only from the repository. The owner reads the result against X01 and judges it the same way.

- **If it reaches X01's level, the files carry the method.**
- **If it doesn't, the owner's marks say what is still missing from the files**, and that goes into DOC-00G, this document or OWNER_TASTE.md. Then run the test again.

