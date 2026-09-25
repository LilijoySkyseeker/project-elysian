# PROJECT ELYSIAN — World & Species Archive
**Species:** Aethela (*Homo Sapiens Successor*) · **Self-Name:** The Kin

**What this repository is for** *(the owner, 2026-09-25)*. A world the owner builds, or has built, that pays them back in stories they enjoy. It combines canon, resources, tools, exemplars and a production process so that **agents can create media from it**: stories first, delivered as **ebooks**, with illustrations and other media to follow. The loop is: the world → agents → a work → **the owner's read** → the owner's notes back into the world and the tools. **The best stories are canon:** when a story is better for a change, canon changes, within the world's internal consistency (D-113).

The design phase (Steps 1–12 of `ROADMAP.md`) built the species; the production phase (Step 13) makes things from it.
Source material lives in the Obsidian vault (`~/Documents/Vault/Projects/Project Elysium/Aethela`); this directory is the organized, audited working copy. Vault originals are untouched.

## Start here
| File | What it is | Read when |
| :--- | :--- | :--- |
| **`AGENTS.md`** | Orientation for any agent: what to read before what, the big-file warnings, how writing is done here. (`CLAUDE.md` imports it.) | **Always, first.** |
| **`offcanon/X01_equestria/`** | X01, the eight-chapter crossover the owner passed chapter by chapter: **the project's best writing and its first exemplar**, and the worked example of a long work. | Before writing any fiction. |
| `references/` | Other writers' books, kept for study (**never read one whole**; see its README). | Pulling an exemplar passage; the linter's human baseline. |
| `templates/long_work/` | The file set for a work in chapters (bible, outline, voices, continuity, chapter brief, revision list). | Starting a long work. |
| `research/OWNER_TASTE.md` | The owner's standing notes: what they want, and what their reads caught. | Before any brief. |
| **`CANON.md`** | Every locked parameter in one ledger, by subsystem, with source doc and conflict flags. | You need *the* number for anything. |
| **`AUDIT.md`** | Six registers: conflicts (C), physics (P), gaps (G), editorial (E), **narrative findings (N)**, **mechanism re-derivations (M)** — and the **H-register**, holes kept on purpose, closable by a scene and never by a ruling. | Deciding what to fix, and what to leave alone. |
| **`ROADMAP.md`** | The eleven design steps (done) and **Step 12 — the standing writing phase**: the rule of order, the dramatisation test and the scene queue. | Deciding what to work on. |
| **`docs/DOC-00G`** | **The prose standard** — what good writing is here: six things a scene must have, the house tells, the lore economy, voice, and variety across the collection. | **Before writing or revising any scene.** |
| **`docs/DOC-00H`** | **The scene pipeline** — brief → predict → draft → lint → cold read → revise → owner → canon. Run it with `/scene`; the cold read alone with `/cold-read`. | Writing or revising a scene. |
| **`docs/DOC-00` + `DOC-00B`** | The style sheet and the writing primer (what a Kin is like; §12 is now the post-draft canon check). | Checking a scene against canon. |
| **`docs/DOC-00C`** | Visual reference — form, proportion, surfaces, postures, and image-generation prompts. | Drawing one, or commissioning art. |
| **`docs/DOC-00D`** | Voice — the six channels a Kin talks on, how each one goes on the page, and what can be concealed on which. | Writing Kin dialogue. |
| **`docs/DOC-00E`** | The outsider's primer — the hand-out version, for someone with no genre background. | Introducing the Kin to a newcomer. |
| **`docs/DOC-00F`** | The small things — a shuffle-deck of Kin–human social detail, tagged by register, with a spent list. | Writing any scene with a human in it. |
| `docs/` | The source documents, one file per DOC. | Reading the actual lore. |
| `scenes/` | The scene collection — every vignette with its canon-drift notes (`scenes/README.md`), and **`scenes/SLATE.md`, the standing queue** of what to write next. | Writing or revising fiction. |
| `tools/` | `tells.py` — the prose linter: house tells with line refs, recycled phrasing, number tics, voice distance between narrators (`python3 tools/tells.py scene <file>` · `corpus` · `ledger`). Patterns in `tells_patterns.tsv`. | Every draft (DOC-00H Stage 4). |
| `research/` | R01 — what the literature says reads as machine and as human, with sources and access status. R02 — the diagnosis of this collection. `SHELF.md` — exemplar pages for the drafter. | Changing the standard; filling the shelf. |
| `reports/` | Generated `tells.py corpus` reports; `tells_baseline_2026-09-24.md` is the before-picture. | Measuring whether the collection is improving. |
| `models/` | Reproducible calculations behind the deep-dives (`awk -v SCEN=shadow_eva -f models/vacuum_budget.awk`; `awk -f models/age_structure.awk`). | Re-running or changing a number. |
| `wargames/` | Wargame records — the species stress-tested from outside. `W03` tests it against its *job*: whether the Kin generate stories, and where story pressure will break the biology. | Before opening a new design pass. |

## Document registry
| ID | File | Scope | Version | Audit status |
| :--- | :--- | :--- | :--- | :--- |
| DOC-00 | `docs/DOC-00_usage_naming_style.md` | Names, pronouns, capitalisation, Kin-code on the page — the writing sheet | v1.2 | Canon (D-54…D-56; D-88, D-90) |
| DOC-00B | `docs/DOC-00B_writing_primer.md` | How to write a Kin — body, ears, the pause and **the override**, the Core, senses, **memory (human recall + the check + "don't make me read it")**, traps, **where an antagonist comes from**, scene checklist (§12 now draws from DOC-00F) | v1.9 | Tool, not canon |
| DOC-00C | `docs/DOC-00C_visual_reference.md` | Visual reference — silhouette, dimension sheet, head/ears/eyes/hand-paws/coat, postures, state changes, image-gen prompt kit | v1.4 | Tool, not canon |
| DOC-00D | `docs/DOC-00D_voice_how_the_kin_talk.md` | Voice — Kin-code and the affect rider, the whistle as the one private channel, human speech as the marked case, the Hum, the Core and the archive on the page, the switching table | v1.3 | Tool, not canon; **§9 open** |
| DOC-00E | `docs/DOC-00E_outsiders_primer.md` | The outsider's primer — one-sitting introduction for a reader with no science-fiction background; ground rules, body, mesh, memory, death and names, humans, factions, glossary, the five wrong assumptions | v1.2 | Tool, not canon |
| DOC-00G | `docs/DOC-00G_the_prose_standard.md` | The prose standard — the six requirements (a want, a teller, detail from a life, escalation and loss, meaning left with the reader, ending when it is over), the house tells, the lore economy (two mechanics a scene), voice cards and the house-voice card, collection rotation and the spent list, exemplars and readers, what the linter can't do, a worked revision, **§10 what X01 taught** (the Cluster as the unit; keep the trait; no evenly spaced echoes; a person and a lens; world logic) | v1.1 | Tool, not canon; governs drafting |
| DOC-00H | `docs/DOC-00H_the_scene_pipeline.md` | The scene pipeline — ten stages, each tied to a finding in `research/`; revising existing scenes; what can be skipped; **§13 long works, §14 the orchestrator's hand, §15 the cold-session test** | v1.1 | Tool, not canon |
| DOC-00F | `docs/DOC-00F_the_small_things.md` | The small things — the competence-marker deck: body, senses, mesh, memory, domestic, names, edges; register tags (W/C/P/E/R), derivation column, and a **spent list** so no detail is used twice | v1.0 | Tool, not canon |
| DOC-01 | `docs/DOC-01_anatomical_biological_specification.md` | Summary anatomy, senses, metabolism | v2.2 | Errata folded; canon |
| DOC-01A | `docs/DOC-01A_musculoskeletal_locomotion.md` | Skeleton, anchor budget, hand-paw, tail, void tax, void-/ground-build, gaits, two clocks, regeneration, yoke & bone box, dual-role limbs, the burn and after it, the frameless Kin | v1.7 | Canon (D-26; D-73…D-75, D-80, D-93, D-95, D-100) |
| DOC-01B | `docs/DOC-01B_macro_physiology.md` | Coelomic vaults, circulation, acceleration tolerance, digestion, energetics ladder, cabin thermal | v2.2 | Errata folded; canon |
| DOC-01C | `docs/DOC-01C_genomic_bio_core.md` | Three-substrate Core, mesh stack, **memory rebuilt (§6: cortex/record/index, retrieval, Data Rot, the night, hard vs soft transfer)**, the Reading, carried memory, tuning within the makers’ ranges, **the two rates — cold and lived (D-103); Data Rot cortical and the rolling window (D-104); **the veto struck (D-105)**; the Cluster as the trauma system (D-106)**, failure modes | v2.4 | Canon (D-20; D-71, D-76→D-79, D-77, D-80, D-85, D-87, D-89, D-92, D-93, **D-97…D-107**) |
| DOC-01D | `docs/DOC-01D_bio_radio_radar.md` | Ear phased arrays, VHF tail, DSP, sensor fusion | v2.1 | Errata folded; canon |
| DOC-01F | `docs/DOC-01F_sensory_systems.md` | Sight, near-field, smell, hearing/voice, touch, hull-hearing | v1.0 | Canon (D-31) |
| DOC-01E | `docs/DOC-01E_vacuum_radiotrophic.md` | Voiding cascade, shielding, eyes, skin | v2.2 | Errata folded; canon |
| DOC-01E.1 | `docs/DOC-01E.1_vacuum_energetics_state_a.md` | State A/B vacuum energetics, thermal + O₂ + acidosis math | v2.2 | Errata folded; canon |
| DOC-01E.2 | `docs/DOC-01E.2_integrated_vacuum_budget.md` | Coupled thermal/O₂/acid model, final vacuum envelope | v1.1 | Canon (D-10); model in `models/vacuum_budget.awk` |
| DOC-02 | `docs/DOC-02_psychology_genesis_social_structure.md` | Reproduction, Clusters, Bandwidth Gap, the three memory tiers, the override, the Kin alone | v2.8 | D-89, D-91, D-93, D-97…D-101 folded; canon |
| DOC-03 | `docs/DOC-03_architecture_tech_environmental_standards.md` | Kin-Nest ergonomics, burn webs, interfaces | v2.4 | D-84 folded; canon |
| DOC-04 | `docs/DOC-04_aesthetic_alignment_cultural_arts.md` | Designer quirk, arts; extended by DOC-13 | v2.1 | D-84 folded; canon |
| DOC-05 | `docs/DOC-05_narrative_vignettes_practical_lore.md` | Four vignettes | v2.0 | Errata folded; canon |
| DOC-06 | `docs/DOC-06_inspiration_influence_matrix.md` | Influences, thematic matrix | v2.1 | Errata folded; canon |
| DOC-07 | `docs/DOC-07_habitat_settings_spatial_environments.md` | Artemis-9, ark ships **and where they came from (§2A, D-108…D-110)**, Nest, virtualities as held dreams | v2.2 | D-81 folded; canon |
| DOC-08 | `docs/DOC-08_factions_philosophical_movements.md` | Four factions; Weavers travel in pairs; what the Unbound are actually building | v2.9 | D-76/D-79/D-80/D-93/D-99 folded; canon |
| DOC-09 | `docs/DOC-09_tactical_crisis_protocols.md` | MACTAC, vacuum tactics, the burn and the hour after it, ordnance as preference, the one Kin war | v2.4 | D-79/D-86/D-95 folded; canon |
| DOC-02B | `docs/DOC-02B_lifecycle_development.md` | Genesis, First Ping, the decade between, first Telling, death & lifespan, medicine | v1.8 | Canon (D-37; D-77, D-78, D-81…D-83, D-86, D-94, D-98) |
| DOC-10 | `docs/DOC-10_timeline_history.md` | AF reckoning, the Program, the Written, the Sealing (the tutors deleted), dated events, population now | v1.6 | Canon (D-50; D-70…D-72, D-78, D-79, D-85, D-87); placeholder names open; human calendar deliberately vague |
| DOC-11 | `docs/DOC-11_rites.md` | Every rite as it happens on the page — First Ping, first Telling, Telling before risk, the Reading, re-keying, joining, the Defrags (nightly = consolidation + appraisal; centennial = the index), the Weave and the Carrying in pairs, what a Telling costs the teller, the chosen ending | v1.9 | Canon (D-63…D-67; D-80, D-82, D-86, D-90, D-93, D-100, D-102) |
| DOC-12 | `docs/DOC-12_the_human_side.md` | Tech ceiling, lifespan asymmetry, Compact law, money, human currents, what a console shows | v1.8 | Canon (D-57…D-62; D-72, D-79, D-85, D-87, D-92, D-93) |
| DOC-13 | `docs/DOC-13_culture_daily_life.md` | The dreaming (weather not content; dreams unwritten; held dreams; virtualities), memory as currency and the grant-web, the argument with the quirk, the literate nose, athletics as Core-training, the arts in the bands, tails, three languages, places, funny/rude/sacred | v1.6 | Canon (D-80…D-84; D-88, D-90, D-93, D-94, D-100) |

## Canon precedence
As of v3.6 (2026-09-23, where the arks came from — D-108…D-110 — after the veto struck and the trauma system re-derived — D-105…D-107 — after Data Rot re-seated in the cortex — D-104 — after the two-rates correction — D-103, amending D-102 — after the memory re-derivation — D-97…D-102 — after the W03 story-engine pass — D-91…D-96 — after the D-89/D-90 distances-and-names pass after the D-85…D-88 keyring-and-body pass after the DOC-13 culture pass — D-80…D-84 — after the D-79 love-and-violence pass after the D-76…D-78 ranges-womb-age pass after the D-74/D-75 limbs-and-burn pass after the D-73 silhouette pass, after the D-70…D-72 Sealing pass and the D-68 scale and D-69 hand-paw passes) every document is folded and consistent. If a contradiction is ever found: deep-dive beats summary; a decision-log ruling in `CANON.md` §11–§29 beats any doc; a scene beats nothing (stories illustrate, docs decide).

**Order of work, since D-96.** The design is closed and the archive is in its writing phase: **a ruling is drafted only when a scene has demanded it, and is discharged by a scene before the next is made.** The queue is `ROADMAP.md` Step 12. Silences listed in the H-register are deliberate and are not gaps — a ruling that closes one is a bug.

## Conventions
- Pronouns, names and page conventions: **DOC-00**. Single-form *hir*; humans say *she* uncorrected; Vesper-7 = the seventh Vesper.
- Numbers are decimal SI. Markdown with LaTeX math, ASCII block diagrams, one `### N.` section per subsystem — match the existing docs when adding new ones.
- Header block on every doc: title line, Document ID line, Codename/Species/Self-Name line, Classification, Status.
