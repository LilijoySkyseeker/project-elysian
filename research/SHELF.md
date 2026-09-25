# SHELF — exemplars for the drafter's context
**What this is.** The pages the drafter reads *before* writing (DOC-00H §4). The single strongest measured lever against generated-sounding fiction is real prose from a real writer in the room (R01 §4). This file says which pages, and why.

## In-house (usable now)
| Page | Why it is here | Use for |
| :-- | :-- | :-- |
| **`offcanon/X01_equestria/chapters/`** (one chapter, whole) | **The best writing the project has made** (the owner, 2026-09-25); every chapter passed the owner's read. Kin POV: ch. 2, 4, 6, 8. Outsider POV: ch. 3, 5, 7. Off-canon: take its texture, never its facts. | **first choice** for any Kin or outsider POV; group Kin-code (ch. 6, 8) |
| `scenes/S012_a_letterALT.md` (whole) | The most human page in the collection: a teller with a reason, digressions that belong to him, repetition as character, detail that demonstrates nothing, the unsaid left unsaid. | any human teller; any document form |
| `scenes/S006_the_flat_country.md`, first two sections | Physical comedy, an opening in motion, a human's wrong reading left in place for a while. | human POV; bodies; comedy |
| `scenes/S017_the_short_end.md`, the game (to "Ten all.") | Momentum, a set-piece that isn't a lesson, Kin-to-Kin talk that doesn't explain itself. | Kin POV; action; group scenes |
| `scenes/S010_minutes_of_the_safety_review.md` | A form that forces a voice that isn't the narrator's. | document forms |

**Caution:** these share the collection's tics in places (S006 has the ears/heat beat, S017 has *eleven*). Give the drafter the page, and give it DOC-00G §3 alongside.

## The owner's shelf
| Passage | Author, work, where | What it's for | Added |
| :-- | :-- | :-- | :-- |
| Chapter 10, first ~1,500 words | Estee, *Daily Equestria Life With Monster Girl* (fimfiction 432523) | A non-human mind in close third, in distress; the narration behaving like the mind (R03 §2.1–2.3, §2.7) | 2026-09-24 |
| Chapter 1, first ~1,500 words | same | An alien seen wrongly from outside by people who are sure; the world never explained (R03 §2.4–2.5) | 2026-09-24 |
| Chapter 30, the bath dialogue | same | Dialogue that talks past itself; the hard thing said sideways (R03 §3) | 2026-09-24 |

**Where the text lives.** *(Changed 2026-09-25 at the owner's request.)* Other writers' books are kept in `references/<work>/` in this **private** repository, with a warning README: **never read a book whole**, one chapter at a time. Estee is `references/estee_daily_equestria_life_with_monster_girl/text/chNNN.md`. Passages go into the **drafter's prompt only**, never into a committed brief; the brief records the chapter reference. Measure any new shelf text with `python3 tools/tells.py baseline references/<work>/text`. `private/` (git-ignored) is still there for anything the owner does not want committed.

## Still wanted
The pipeline gets much better with pages from writers whose voice the owner wants in the room, and with any of the owner's own writing. Suggested contents:
- **The owner's own prose**, any genre: a letter, notes, an old story. This is the most valuable item on the shelf.
- **More writers whose sentences the owner wants near the Kin.** Record them in the table above. The texts go in `references/` (or `private/` if the owner prefers them uncommitted).
- **One writer per register the collection lacks**: someone funny, someone unkind, someone who writes documents, someone who writes children.

