# R03 — Style study: Estee, *Daily Equestria Life With Monster Girl*
**The first human reference on the shelf.** Chosen by the owner as a favourite for following a non-human mind and for its prose. Studied 2026-09-24.
**Status:** Evidence file, not canon. It is our analysis, in our words. Quotations are kept to a few words each, for illustration. **The text itself is never committed.** A private copy can live in `private/` (git-ignored), and the owner re-supplies it when a session needs it (research/SHELF.md).

**The work.** A *My Little Pony* × *Monster Musume* crossover by Estee (fimfiction.net, story 432523). 100 chapters, 714,524 words. Cerea, a centaur knight, arrives in Equestria and is taken for a monster. It is serial fiction, long-form and in close third, with rotating viewpoints.

**How it was read.** It is too long to read whole in a session, so the study has two halves. The whole text was measured with `tools/tells.py baseline`. Then samples were read: the opening 1,500 words, the openings of chapters 2, 10, 30 and 60, the endings of eight chapters (3, 10, 25, 40, 55, 70, 85, 99), and the densest dialogue passage in chapter 30. **Everything below rests on those samples plus the numbers.** A claim about the whole book beyond the numbers is an inference from about 6,000 words.

---

## 1. The numbers: the collection's first human baseline

`python3 tools/tells.py baseline private/delwmg/text`, against the 16 Elysian scenes over 900 words:

| Per 1,000 words | Estee | Elysian | Elysian ÷ Estee |
| :-- | --: | --: | --: |
| Negation-reframe | 0.76 | 1.92 | 2.5× |
| Gnomic aside | 0.15 | 1.89 | 12.5× |
| Explaining line | 0.03 | 0.77 | 26× |
| Hedged number | 0.25 | 1.39 | 5.5× |

| Shape (median) | Estee | Elysian |
| :-- | --: | --: |
| Mean sentence length | 13.3 | 13.5 |
| Sentence-length variation (CV) | 0.80 | 0.99 |
| One-sentence paragraphs | 38% | 35% |
| **Dialogue share** | **22%** | **8%** |
| Em dashes per 1,000 words (Estee types `--`) | 3.6 | 8.0 |
| Participial clauses per 1,000 words | 1.6 | 1.7 |
| **Sections ending on a short line** | **60%** | 40% |
| "four" / "eleven" per 10,000 words | 2.9 / 0.01 | 38.5 / 18.1 |

**What the numbers confirm.**
- R02's diagnosis holds against a real human writer. Explaining is about 26× Estee's rate, the gnomic aside about 12×, and the hedged number 5.5×.
- The house numbers are an artefact. Estee uses "eleven" once in 715,000 words.
- The collection talks much less. Dialogue is 8% of the characters, against Estee's 22%.

**What the numbers correct.**
- **Stingers are not a tell.** Estee ends 60% of sections on a short line. The limit in `tells.py` was wrong and has been removed (now reported only). The problem in the collection is that every closer is the *same kind* of closer (§4).
- **"Vary your sentence length" is not the fix.** The collection already varies more than Estee does (CV 0.99 against 0.80). The staged long-long-short rhythm is its own tell.
- **Sentence length, one-line paragraphs and participles are the same.** These surface stats do not separate the two. The difference is in what the sentences *do*.

**Voice distance, calibrated.** In one pooled Burrows's Delta run, sixteen 1,800-word windows from Estee's chapters sit a median **0.90** apart (range 0.71–1.07), and the Elysian scenes by different narrators sit a median **1.07** apart. Overall, then, the collection varies more than one human novel does, as it should. But its closest pairs (0.69–0.83: S017–S023) fall inside the range of chapters of a single novel. R02 §1 is amended to say exactly this.

### 1A. Flow: the measure the first study missed *(added 2026-09-24)*
After the owner found X01 ch. 1 "disjointed… not quite full prose" in its narration, the narration alone (dialogue excluded) was measured across 34 of Estee's chapters:
| Narration | Estee | X01 ch. 1 | S024 | S012alt | S025 |
| :-- | --: | --: | --: | --: | --: |
| Sentences with 3+ *and*, per 100 | 1.0 | 15.1 | 18.5 | 5.0 | 5.9 |
| *and* per 1,000 words | 26 | 57 | 54 | 44 | — |
| Subordinators per 1,000 words | 29 | 14 | 18 | 28 | — |
| Subordinators per *and* | 1.11 | 0.24 | 0.34 | 0.65 | 1.17 |
Fragments (18.7 per 100 sentences) and short paragraphs were *not* the difference. Estee orders ideas; the house cadence strings them. It is now in DOC-00G §2.7 and the linter.

---

## 2. The non-human mind: how it is done

This is why the owner chose the book. Seven techniques, each with where it was seen.

**2.1 The narration takes on the mind's habits, not just its thoughts.** Cerea is compulsively polite, and in chapter 2 the narration itself censors a word about a housemate the way her mind would: a parenthesis in which a mind "trained towards politeness" edits the term out. The prose *behaves* like her. That goes beyond reporting her.
*For the Kin:* a Kin narration could do what a Kin mind does. It could check a fact mid-sentence and move on, having it exactly and not caring. Or it could stop to hold an answer while a human's mouth finishes. That means doing it in the syntax, not describing it.

**2.2 Thoughts break in, in italics, mid-sentence, and are often wrong.** Short italic interior lines cut across the narration, like her name in her own voice, or a knightly rule she then fails to keep. The narrator then quietly corrects her in the next line ("Strictly speaking, this wasn't true," ch. 10). The narrator comments on the *character's belief*, never on the world's meaning.
*Contrast:* Elysian's narrator comments on what things mean (R02 §2). Estee's comments on what a person has got wrong about themselves.

**2.3 The comparisons come from the character's life, not from the author's notes.** Cerea's analogies are her own: life in a particular noisy household, a sliding-block puzzle (ch. 30), smells she knows and smells that are missing. In the chapter 10 prison she registers bleach and old feathers, and notices the *absence* of detergent. What is missing tells her where she is.
*For the Kin:* the scent, the Hum and the frame should be compared to things *this* Kin has lived through, not glossed from DOC-01F.

**2.4 The alien is seen first from outside, by people who get it wrong.** Chapter 1 is told from the pony townsfolk, collectively. They catalogue the centaur with their own biology as the measure: eyes set forward mean "predator"; the nose is "a tiny afterthought". The narration states their certainties flatly and lets the reader see past them. Nobody in the chapter is corrected.
*For the Kin:* this is DOC-00G §4.4 ("wrong is allowed") at full strength. S006 and S020 do a gentle version. Estee lets the wrong reading be *dangerous*: they nearly kill her.

**2.5 The world is never explained to the reader.** Unicorns, pegasi and earth ponies are "those with horns", "the ones with wings" and "the ones who lacked both" (ch. 1). The terms of Cerea's own world arrive as unexplained proper nouns. Customs are learned by a character, in a scene, at a cost.

**2.6 Other species' minds get rules, but from inside a character, with a joke attached.** Chapter 60 opens with a general account of how panicked pony minds rebuild memory as a group, which technically is a gnomic passage. But it is Luna's weary view. It is concrete, and it ends on a named idiot whose brilliant plan is still unknown to himself. **Lesson for DOC-00G §3.2:** the aside is fine when it belongs to someone and pays off. What fails is the narrator's own wisdom, unowned.

**2.7 Feeling is not rationed.** Cerea sobs into a pillow in chapter 10, the chapter's emotional centre, rendered physically: the folded legs, the compressed torso, the fingernails. The Elysian register is understatement throughout (R02 §4). Estee's restraint is situational. The prose is sometimes loud.

---

## 3. Dialogue

The densest exchange sampled (ch. 30) shows four things the collection almost never does (R02 §7):
- **People talk past each other.** A pegasus answers a question about the weather when asked something else, and keeps going.
- **Interruptions cut both ways**, both speakers breaking in with `--`, neither finishing.
- **The hard thing is said sideways,** through an extended metaphor from the speaker's own trade (weather scheduling, lightning, standing near the tallest thing), and **the listener doesn't get it**, or not yet.
- **Tags carry manner.** Estee uses said-bookisms and adverbs ("evenly stated", "prettily smiled"). Elmore Leonard's rule (R01 §5) says don't, and Estee does anyway, consistently, as part of the voice. **Rules like Leonard's describe *a* voice, not *the* human voice.**

---

## 4. Endings

Across the eight chapter endings sampled, the ending *type* keeps changing:
- a line of command dialogue;
- a proleptic hook (*it would also be the moment it ended*);
- a seduction interrupted by a question;
- an italic passage from a different mind;
- a run of parenthetical fragments into a breakdown;
- a one-word paragraph and a single italic thought;
- a direct address to the reader to *watch*;
- a comic button about elephants.

Several are short one-liners. Several are cliffhangers, which fit serial fiction. **Not one is a quiet reflection on what the chapter meant.** That is the correction to DOC-00G §3.4: vary the *kind* of ending, and let short closers be as common as they want to be.

---

## 5. What not to take

- **Length and pace.** A 7,000-word mean chapter in a 715,000-word serial allows digressions that a 2,000-word scene cannot carry.
- **Genre furniture.** Proleptic cliffhangers suit serial fiction. In a collection they should be rare.
- **The borrowed world.** The crossover leans on reader familiarity with two franchises. The Kin have no such cushion, so incluing (§2.5) has to be even more careful here, not less.
- **Any specific sentence.** The shelf is for the texture in the drafter's context, not for imitation.

## 6. How the pipeline uses this

- **Shelf** (research/SHELF.md): chapter 10, the first ~1,500 words, as the exemplar for a non-human close third in distress. Chapter 1, the first ~1,500 words, for an alien seen wrongly from outside. Chapter 30, the bath dialogue, for dialogue. Passages go into the **drafter's prompt only**, from the private copy, and are never pasted into a committed brief.
- **Linter:** stingers are reported, not failed. `tells.py baseline` is the standard way to measure any future shelf text.
- **DOC-00G:** §3.2 (an aside belongs to someone), §3.4 (stingers), §3.5 (dialogue talks past itself) and §5.1 (the voice card's "Syntax" can include how the mind shows in the syntax) take these amendments.
