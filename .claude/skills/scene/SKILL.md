---
name: scene
description: Write a new Project Elysian scene, or revise an existing one, through the DOC-00H pipeline — choose against the ledger, brief from a person not a ruling, predictability pass, fresh-context draft with exemplars, lint, cold read, targeted revision, owner's read, canon check last. Use whenever the user asks to write, draft, redraft or revise a scene, vignette or story for the archive, or picks an item from scenes/SLATE.md.
---

# Scene

You are the orchestrator of DOC-00H. Read DOC-00G (the standard) and DOC-00H (the process) before anything else. The rules that matter most:

- **You do not draft the scene yourself.** A fresh agent does, with a controlled context (Stage 3). You have read too much lore to write without lecturing, and the house voice is yours.
- **The owner passes scenes.** No model reader does (R01 1.6). Stop at Stage 7 and hand over.
- **Canon comes last** (Stage 8). DOC-00B §12 is never in the drafter's context.

Arguments: a slate entry (e.g. `A5`), a premise, or `revise S0xx`.

## New scene

**Stage 0: choose.** Read `scenes/LEDGER.md` (last five rows), DOC-00G §6.2, and `scenes/SLATE.md`. Say in one line which ledger gap this scene fills. If the user named the entry, still say it. If it fills no gap, say that, and suggest what would.

**Stage 1: brief.** Copy `scenes/briefs/TEMPLATE.md` to `scenes/briefs/S0xx_brief.md` (the next number is in `scenes/README.md`). Fill sections 1–9. For §9, paste in only the doc paragraphs the two mechanics need. **Then show the brief to the owner and ask them to change anything before drafting**, unless they have said to run straight through. The want, the loss and the voice card are the places their judgement matters most.

**Stage 2: predict.** Spawn a fresh `general-purpose` agent with this prompt, filled from the brief (premise, teller and situation only; no voice card, no exemplars):
> Here is the premise for a short story set in an invented science-fiction world: [premise, teller, situation, in 3–5 sentences, plus a 5-line glossary of the invented terms it needs]. Write what a competent language model would most likely produce from this premise: (a) the five most likely versions of the story, one paragraph each; (b) the ten most likely beats, images or lines; (c) the five most likely final lines. Be honest about the obvious; that is the point.

Paste the result into brief §10.

**Stage 3: draft.** Spawn a fresh `general-purpose` agent. Its prompt, in this order:
1. The exemplar pages named in brief §8, whole, under the heading *"Pages to read first. This is the texture to aim for."*
2. DOC-00G §0, §2, §3, and the §5.3 card under the heading *"The house voice. Do not write like this."*
3. The brief, sections 1–10.
4. This instruction:
   > Write the scene once, straight through, in the teller's voice, to about [target] words. Use none of the predictable list. Keep canon terms unexplained: the teller lives here. At least three details must demonstrate nothing. Something must get worse after the middle, and it is not repaired. Stop when it is over; no epilogue, no reflection. Return the prose only: no title, no header, no notes.

Save the result to `scenes/drafts/S0xx_<slug>.md` under a minimal header (title and POV only; the canon header is Stage 8).

**Stage 4: lint.** `python3 tools/tells.py scene <draft>`. Fix banned and rested hits with the smallest edits. If a limited kind is over budget because of the teller's voice, record why in the brief; otherwise fix it. **If the linter fails the scene on voice** (clearly below the S012↔S012alt anchor, or at it against two or more scenes), **go back to Stage 3** with a sharper voice card. Don't patch it line by line.

**Stage 5: cold read.** Run the `cold-read` skill on the draft. Put its report in the brief.

**Stage 6: revise.** Cut first, starting with the cut list. Then make targeted rewrites of the marked sentences, in the teller's voice. Never regenerate the whole scene. At most two rounds, re-linting after each. Log each round in the brief.

**Stage 7: owner.** Stop. Tell the owner the draft path and the brief path, and give a five-line summary: the want, the loss, the ending type, the lint verdict, and the cold reader's "first place a model" answer. Ask them to read the scene **before** the notes, and to write their marks into the brief's *Owner's read*.

**Stages 8–9** (after the owner passes it): run DOC-00B §12 against the finished scene. Write the header block and canon appendix. Add the ledger row. Add new strong beats to `tools/tells_patterns.tsv` as `rested`. Update DOC-00F §9 if a small thing was used. Regenerate `reports/tells_latest.md`. Update `scenes/README.md` and mark the slate entry. Commit.

## Revising an existing scene (`revise S0xx`)

DOC-00H §11. Retrofit the brief: write the want, the loss and the voice card *for the scene as it stands*, and note where any is missing. That gap is the revision. Run Stage 4 and Stage 5 on the original. Then make a cut-first revision into a **new versioned file** (`S0xx_<slug>_v2.md`, with a version header), never an overwrite. Then stop for the owner, as in Stage 7.
