# AGENTS.md — read this first
Instructions for any agent (Claude Code or otherwise) working in this repository. `CLAUDE.md` points here.

## What this is
**Project Elysian** is a world-and-species archive for the **Kin** (*Aethela*), a human-engineered successor species. Most of it is **fiction**: canon documents, a collection of scenes, and the tools and research for writing them well. The owner reads everything that is written. `README.md` has the full map.

## Before you do anything
| If you are… | Read first |
| :-- | :-- |
| writing or revising **any fiction** | `docs/DOC-00G` (the standard, **§10: what X01 taught**), `docs/DOC-00H` (the pipeline, **§13–§15**), `research/OWNER_TASTE.md` (the owner's standing notes). Then run `/scene`. |
| writing a **work in chapters** | the above, then `templates/long_work/README.md`, and the worked example `offcanon/X01_equestria/` |
| writing **Kin dialogue** | `docs/DOC-00D` (the six channels); the X01 card "How Kin talk among Kin" in `offcanon/X01_equestria/VOICES.md` |
| checking or changing **canon** | `CANON.md` (the numbers and the decision log) and `AUDIT.md`. **The design is closed (D-96):** a ruling is drafted only when a scene demands it, and only the owner rules. |
| using the **linter** | `python3 tools/tells.py scene <file>` (see `--help`; `--counting-pov` for a teller who counts for a living) |

## The exemplar
**`offcanon/X01_equestria/`** is the best writing the project has made, in the owner's judgement. It is an eight-chapter off-canon crossover, and every chapter passed the owner's read. Give a drafter **one passed chapter** as the first exemplar: Kin POV ch. 2, 4, 6, 8; outsider POV ch. 3, 5, 7. Take its texture, never its facts. The full text is `offcanon/X01_equestria/X01_full.md` (~35,000 words): **don't read it whole unless you need to.**

## ⚠ Big files: never read these whole
- **`references/`**: other writers' books. `references/estee_daily_equestria_life_with_monster_girl/` is **~720,000 words in 100 chapters**, and one chapter can be 18,000 words. Read **one chapter** at a time (`text/chNNN.md`), or the first ~1,500 words of one. Find chapters in `chapters.tsv`. **Never load a whole book into your context or a subagent's.** These are other people's work, kept in this private repo for study: quote a few words at most in anything committed, and use passages only in a drafter's prompt. Delete `references/` before any public release. See `references/README.md`.
- **`CANON.md`** and some **`docs/`** files are long. `grep` for what you need, or read by section.
- **Session transcripts and task output files** can be enormous. Don't `cat` them.

## How writing is done here (the short version)
1. **You don't draft the fiction yourself.** A fresh agent does, with a controlled context (DOC-00H Stage 3). You orchestrate: brief, predictability pass, draft, lint, cold read, fidelity read (for Kin or long works), revise (at most two model rounds), **the owner's read**, canon check last.
2. **The orchestrator's hand** (DOC-00H §14) is not optional:
   - read every draft whole yourself;
   - check every number with code;
   - triage the readers (some findings are wrong);
   - write revisions as numbered lists with a keep list;
   - re-read after each revision;
   - run the world-logic pass;
   - update the continuity file.
3. **The default Kin cast is a Cluster** (DOC-00G §10.1).
4. **The owner passes work. No model reader does.** Short praise from the owner is a normal pass (`research/OWNER_TASTE.md`).

## Repository habits
- **Log decisions where they live.** Owner's notes go into the brief's *Owner's read* and into `research/OWNER_TASTE.md`. New facts go into the work's `CONTINUITY.md`. Rulings go into `CANON.md` (owner only).
- **Revisions get a new version, never an overwrite** of an accepted scene (`scenes/README.md`).
- **Scratch work** goes in your session scratchpad, not the repo. Commit what's worth keeping, with a clear message.
- **Units:** metric for the Kin; the owner prefers metric generally.
- **Be honest about what you checked.** Say when a reader was not re-run, when a number is assumed, or when you departed from the pipeline.
