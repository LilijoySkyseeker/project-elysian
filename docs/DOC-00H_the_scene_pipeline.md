# PROJECT ELYSIAN: COMPREHENSIVE WORLD & SPECIES ARCHIVE
## Document ID: DOC-00H — The Scene Pipeline: How a Scene Gets Written
**Codename:** Project Elysian | **Species:** Aethela (*Homo Sapiens Successor*) | **Self-Name:** The Kin  
**Classification:** Tool, not canon. This is the process. The standard it serves is DOC-00G; the evidence is `research/R01`–`R02`.  
**Status:** v1.0, 2026-09-24. Run it with the `/scene` skill (`.claude/skills/scene/`). The cold read runs on its own with `/cold-read`.

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
8. **The exemplars.** Which shelf pages go in the drafter's context (DOC-00G §7; `research/SHELF.md`).
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
