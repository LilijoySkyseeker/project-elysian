# PROJECT ELYSIAN: COMPREHENSIVE WORLD & SPECIES ARCHIVE
## Document ID: DOC-00G — The Prose Standard: What Good Writing Is Here
**Codename:** Project Elysian | **Species:** Aethela (*Homo Sapiens Successor*) | **Self-Name:** The Kin  
**Classification:** Tool, not canon. It governs *how* a scene is written. DOC-00B governs what a Kin is like on the page, and the docs govern what is true. Where DOC-00B's §12 checklist and this document disagree about **drafting**, this document wins; DOC-00B still governs **canon checking**.  
**Status:** v1.1, 2026-09-25: §10 added, the lessons of X01 (an eight-chapter crossover the owner passed chapter by chapter; now the first exemplar, §7). v1.0, 2026-09-24. Evidence: `research/R01` (what the literature says) and `research/R02` (what the collection does). Tooling: `tools/tells.py`. Process: DOC-00H.

---

### 0. THE STANDARD IN ONE PARAGRAPH

A scene is good when a particular person seems to have told it, for a reason, and you could not have predicted it from its premise. Somebody on the page wants something, and it gets harder. The world is taken for granted by the people in it, so the reader learns it the way a visitor learns a house: by what nobody explains. The detail belongs to a life, not to a design document. Nobody tells the reader what anything meant. It ends when it is over. **And across the collection, no two scenes are told by the same voice, built on the same shape, or ended the same way.**

"Human" in this document never means *free of tells*. A scene can pass every check in `tools/tells.py` and still be generic, and a good human writer breaks half of §3 on purpose. The tells are symptoms. §2 is the standard.

---

### 1. WHY THIS DOCUMENT EXISTS

`research/R02` read the whole collection. The short version: the scenes escaped the obvious machine prose early (S001–S004 still have it), and settled into a second, subtler register. It is restrained, wry and literary, and it has a small, fixed set of moves. It uses one narrator for everyone: five pairs of different narrators measure closer together than two drafts of the same letter (R02 §1). It stops to explain what things mean (R02 §2). It uses numbers as a performance of concreteness (R02 §3). Everyone is kind and everything comes round (R02 §4). And it ends on a quiet coda (R02 §5). The best outside study of AI fiction (StoryScope, R01 §3) describes Claude's fiction the same way, without having seen any of these scenes: flat escalation, uniform voice, restrained intensity, a preference for epilogues.

None of this is fixed by a better word list. Structure alone gives AI fiction away (R01 §3). The fix is upstream: what a scene is for, who is telling it, and what the writer is handed before drafting.

---

### 2. WHAT A SCENE MUST HAVE

These six are the standard. Each can be checked by a reader who has not seen the brief.

#### 2.1 Somebody wants something, now
A scene starts from **a person and a want**, not from a ruling. *"Dramatise D-88"* is a topic. *"Idris has spent eight months learning a phrase and today he's going to say it"* is a scene. The want belongs to a character on the page. It can be small (to win a point, to get out of a meeting, to be left alone), but it is *theirs*, and it is live in the first page.

**Check:** can you say, in a sentence with no canon term in it, who wants what?

#### 2.2 A teller, with a voice that is only theirs
Every scene has a **voice card** (§5) before the first word. The teller is a specific person, or a specific narrating stance, with a vocabulary, a sentence habit, a blind spot, a thing they are wrong about, and a reason for telling. A human hull tech in her third week does not generalise about Kin like an anthropologist. A fourteen-year-old does not have an elder's cadence. A Kin talking to Kin does not explain Kin things.

**Check:** cover the names. Could this paragraph have come from any other scene in the collection? If yes, the voice is the house voice (§5.3).

#### 2.3 Detail from a life, not from the docs
Concreteness is the gap expert readers name first (R01 §3, Wang et al.). This collection is concrete about **lore**: metres, minutes, kilos, catches. It needs to be concrete about **life**: what is in the mug, who left it there, what the song on the loop is, the stupid joke, the smell that isn't a plot point, the object that means nothing.

**Rule:** every scene carries at least **three details that demonstrate nothing**. They serve no canon, set up no payoff, and illustrate no ruling. They are there because the teller noticed them. S012alt is the model: the clothes brush, the chocolate lost at cards, the second pack of cards "somewhere in the rest".

**Rule:** numbers are budgeted. A number goes on the page when the *teller* would say it, which is less often than a narrator performing precision would (§3.6).

#### 2.4 It gets worse, and something is lost
LLM stories are "homogeneously positive and lack tension" (R01 1.7). Claude's escalation is the flattest measured (R01 §3). So:
- **After the midpoint, something goes wrong that the first half did not predict.** It is a real setback, not a misunderstanding that resolves into tenderness.
- **Someone loses something they do not get back:** an argument, a friend, face, a chance, the reader's good opinion.
- **Not everyone comes round.** Some people stay wrong, some stay unkind, and some Kin are the ones who are wrong (DOC-00B §9–§10).

**Check:** name the worst moment in the scene. Is it after the middle? Does the ending repair it? (It usually should not.)

#### 2.5 The meaning stays with the reader
No sentence tells the reader what a moment meant, what a custom is *for*, or what a character learned. The iceberg (R01 §5, Hemingway): the writer knows it; the reader feels it; nobody says it. If a scene needs a line explaining its own point, the scene has not earned the point. Cut the line and fix the scene.

**Check:** delete every sentence that interprets. Does the reader still get it? Then those sentences were redundant exposition, the third-largest edit category professional writers make to LLM prose (R01 1.1). If the reader doesn't get it, the scene was missing a beat, not an explanation.

#### 2.6 It ends when it is over
The default ending is **the last thing that happens**, not a reflection on it. No time-jump coda (*"He still does it. Eleven years became nineteen."*), no epilogue, no summary, no final line whose job is to sound final. A coda is allowed when the collection has not had one lately (§6), when the jump *changes* what the reader knows rather than confirming it, and when the ledger records it.

**Check:** cover the last paragraph. Is the scene worse without it? If not, it goes.

#### 2.7 The prose connects *(added 2026-09-24, after the owner's read of X01 ch. 1)*
The owner read a chapter that was funny, gripping and free of tells as *"a bit hard to follow… disjointed… not quite written like full prose"*, and specifically the narration, not the dialogue. Measured against Estee (R03 §1A), the cause is **parataxis**: clauses laid side by side with *and*, instead of ordered. Ch. 1's narration used *and* at 57 per 1,000 words against Estee's 26, and subordinators (*because, when, while, which, until, before*) at 14 against Estee's 29. The reader has to work out what caused what and which idea is the main one. The collection's house cadence has the same habit (S024: 0.34 subordinators per *and*); S012alt (0.65) and S025 (1.17) do not.
- **Each sentence has a main idea**, and the others hang off it: *because*, *when*, *so*, *which*, *until*, *before*, *while*. Cause and sequence are written in (the human-prose rule: people connect thoughts with *so*, *then*, *because*).
- **A paragraph is one movement**: one action, one thought, one look. It picks up what the last one left and hands something to the next. A backstory paragraph is bridged in and out; it is not dropped mid-action.
- **"And… and… and" is a tool, not a cadence.** Use it for momentum (a chase, a panic, a pile-up) and nowhere else.
- **Colons and parentheses are allowed**, and Estee uses both.
**Budgets** (`tools/tells.py`, narration only): no more than 6 sentences with three or more *and* per 100 narration sentences (Estee: 1.0); at least 0.5 subordinators per *and* (Estee: 1.11).
**Not a licence to explain.** A subordinate clause orders *events* ("she stopped because the wheel had caught"). It does not interpret them ("she stopped, which was the whole point").
**The overcorrection, seen in X01 ch. 2:** told to order clauses, a drafter reaches for *because* and *since* as **glosses**: *"because a load that wide doesn't go over"*, *"since breathing was work here too"*, *"because watching the watch was something to do"*. The cold reader counted about a dozen. Cutting them left the flow on target (1.2 chains per 100, 0.96 subordinators per *and*), because the ordering that mattered was of events. **Rule of thumb: if the *because* clause could be deleted and the reader would still know why, delete it.**

---

### 3. THE HOUSE TELLS

These are the specific habits of *this* collection's writer, with a fix for each. `tools/tells.py` finds most of them. The pattern IDs are in `tools/tells_patterns.tsv`.

**3.1 The negation-reframe** (R01–R06). *"It was not that a human made the sound. The sound was fine."* / *"That is the sport. Not the falling. The letting go of it."* It is the most heavily weighted pattern in Paech's Slop Score (R01 1.4). **Fix:** say the second half. If the first half was worth saying, it was worth saying on its own.
**Budget:** one per 1,000 words, in narration. A character may say one if that character talks that way.

**3.2 The gnomic aside** (G01–G09). *"which is how Fern says things"*, *"Margit sat down, which humans do"*, *"You do not think about it. You would not think about breathing."*, *"The thing about the whistle is…"* The narrator stops the story to state a rule of life. **Fix:** cut it, or give it to a character as an opinion they could be wrong about. An aside that *belongs to someone* and pays off is fine. Estee opens a chapter with a general account of panicking pony minds, and it works because it is Luna's weary view and ends on a named fool (R03 §2.6). What fails is the narrator's own unowned wisdom.
**Budget:** one per 1,000 words.

**3.3 The explaining line** (E01–E06). *"which is the whole of what it is for"*, *"and that is correct"*, *"That is the part Rowan turns over"*, *"Both are true."* **Budget: zero.** See §2.5.

**3.4 The ending that is always the same kind.** *(Amended 2026-09-24 after R03.)* Short one-line closers are **not** a tell: Estee ends 60% of sections on one, and the collection 40%. What is a tell is that the collection's closers are all one *kind*, the quiet line that lands the meaning. Estee's are commands, hooks, jokes, fragments, a thought from another mind, a question. **Rule:** no two consecutive sections end the same kind of way, and none ends on the narrator's reflection. `tells.py` reports the stinger ratio but no longer fails a scene on it.

**3.5 The epigram.** Every Kin line lands: *"Everyone who has asked."*, *"You will be very slow about it."* Careful speech (DOC-00B §5) is not the same as aphoristic speech. The collection's dialogue share is 8% of the text; Estee's is 22% (R03 §1). **Fix:** more talk, and worse at communicating. In any exchange longer than four lines, at least one line misfires. Someone misunderstands, answers a different question, says something dull that turns out to matter, trails off, or is interrupted. Nobody's dialogue is a closing line more than once a scene.

**3.6 Precision theatre** (H01, number tics). *"about four metres"*, *"about nine times"*, *"the better part of a second"*; "eleven" 47 times in 11 scenes, "four" 104 times (R02 §3). **Fix:** keep the numbers the teller would actually say, and replace the rest with the thing itself. **The collection's house numbers, *eleven* and *four*, are rested.** Use another number, or none.

**3.7 The lore lecture.** *"Because that is the rule, and it is not a rule anyone made, it is just what a record is when nobody writes anything down."* This is the Turkey City *expository lump* (R01 §5), delivered as wisdom. **Fix:** §4.

**3.8 The stock beat.** The fan, the very good assistant, the hand flat on the chest, the dog whistle, *"I am hot"*, the tail round the ankle, *"for as long as hir has anything"*, the number-two pump. **Each is rested** (§6.3). A rested beat may come back only if the scene is *about* it, and then it is new.

**3.9 The coda.** See §2.6.

**3.10 The general machine vocabulary** (L01–L04): tapestry, testament, delve, barely above a whisper, something shifted, the weight of, unspoken, palpable. Mostly absent since S005; kept at zero. *Bioluminescent*, *thrummed* and *hum* are near-defaults in SF and are especially exposed here, because the Hum is canon. Use the canon noun, and do not let it spread into the verbs.

**3.11 What is *not* a tell here.** Em dashes (R01 1.10: weak evidence, and human writers use them heavily; the tool reports them and never fails a scene on them). Short sentences. British spelling. *Hir*. Understatement as such. A human writer uses all of these. The problem is having nothing else.

---

### 4. THE LORE ECONOMY

The world is the project's great strength, and on the page it has been a liability. Every scene has been asked to show every system (R02 §2). From now on:

1. **Canon is assumed.** The people in the scene live in this world and do not notice it. A Kin does not explain the Hum to a Kin, and the narrator does not explain it to the reader. The reader works it out, as a visitor does. This is Jo Walton's *incluing* (R01 §5): the information is scattered through the story, and the story never stops to deliver it.
**Native channels are not lore** *(added 2026-09-24 after X01 ch. 2)*. When the viewpoint belongs to a Kin, hir own ways of talking and sensing (Kin-code, the frame's weather, the body, the Core) are **the medium, not mechanics**, and are **never rationed** by the budget below. Rationing them turns Kin into humans in Kin bodies. X01 ch. 2's first draft did exactly that, because its brief said "Kin-code, sparingly". The budget limits what a scene *demonstrates*. It never limits how a character *lives*.
2. **Budget: two mechanics.** At most **two** canon mechanics may matter to the plot of one scene. Everything else that appears is texture: named, used and never explained. Or it is absent. A scene about the whistle does not also demonstrate the pause, the Core, the ears, the frame, the Reading and the Nest.
3. **The Kin test.** For any sentence that explains lore, ask whether this teller would say it to this listener. A Kin telling another Kin would not. A human in week three would say it wrong. A letter-writer would assume it. If nobody would say it, cut it.
4. **Wrong is allowed.** Human tellers are wrong about Kin in ways the docs make clear (DOC-00B §10). Let the error stand uncorrected when the scene doesn't need the correction. The reader who knows the docs gets a second pleasure. The reader who doesn't gets a person.
5. **The checklist moves.** DOC-00B §12 is now a **canon check run after the draft**, not a list of things to put in. A scene that answers four of its twelve questions is normal.
6. **The header comes last.** A scene's *Canon status* line and consistency appendix are written after the prose is finished, by someone checking it. They are never the brief.

---

### 5. VOICE

No reputable source was found on differentiating narrators across a collection (R01 §5), so this section is the project's own method. It is measured by `tells.py`'s voice distance, whose one anchor is S012↔S012alt (0.85 in the corpus run; the figure moves with the comparison pool, so it is always recomputed), and judged by the owner. The measure is crude on texts this short. It flags S006 as borderline-close to S020, for instance, so it fails a scene only when the match is clear.

#### 5.1 The voice card
Written before drafting and kept in the scene's brief (DOC-00H). Eight lines:

| Field | Question |
| :-- | :-- |
| **Who** | The teller, specifically. Age, job, how long here, mood today. |
| **To whom, why now** | Who is this told to (a granddaughter, a review board, nobody, the Cluster at night), and what prompted it? |
| **Distance** | Gardner's psychic distance (R01 §5): how close are we to the teller's head, and does it move? |
| **Syntax** | Sentence habit: long and run-on, clipped, formal, listy, full of parentheticals, fond of questions. Pick one and let it be a little too much. For a non-human teller, also decide **how the mind shows in the syntax**: what it interrupts itself with, what it checks mid-sentence, what it censors (R03 §2.1). |
| **Vocabulary** | Five words this teller uses that the others don't, and five they never would. Trade words, slang, the words of their generation or job. |
| **Notices** | What this person looks at first in a room. A rigger sees load paths, a cook sees mess, a child sees who is watching. |
| **Wrong about** | One thing the teller believes that the docs say is false, or one blind spot. It stays on the page. |
| **Humour** | Dry, crude, none, cruel, silly, oblivious. Not "wry", which is the house default. |

#### 5.2 Rotation
The collection rotates **form** as well as teller. The in-world document forms are the strongest voices it has: the letter (S012), the minutes (S010), the song (S007). Candidates not yet used: a transcript, a log with marginal notes, a complaint, a eulogy given by a human who gets the rites wrong, a child's account, a set of instructions, a sales pitch, a court record. At least one scene in every five is a document or an unusual form (§6).

#### 5.3 The house voice, as a card, so that it can be avoided
It is written down here because it is the default a model falls into.

> **Who:** an omniscient-leaning, wise, amused observer, fond of everyone. **Syntax:** long "and…and…and" runs, broken by a short sentence that lands a point. **Vocabulary:** *which is how, the way you, the thing about, the whole of, entirely, exactly, simply, genuinely, about (+ number)*. **Notices:** precise quantities, the lore mechanism, the kindness nobody mentions. **Wrong about:** nothing. **Humour:** wry. **Ends:** quietly, on a withheld truth, a year later.

If a draft's narrator matches this card, the draft is in the house voice, whoever the POV character is.

---

### 6. ACROSS THE COLLECTION

The collection is read as a whole. Twenty scenes that are each fine and all the same read as one machine (R01 §2).

#### 6.1 The ledger
`scenes/LEDGER.md` carries one row per scene: teller, form, tense and person, length, time span, the two mechanics, escalation (does it get worse after the midpoint?), outcome (who lost what), ending type, and tone. Before choosing the next scene, read the last five rows.

#### 6.2 Rotation rules
- **Ending types:** *cut mid-action*, *line of dialogue*, *image with no comment*, *reversal*, *unresolved*, *document ends* (a signature or a stamp), *coda*. No type twice in a row. *Coda* and *quiet withheld truth* at most once in every five scenes.
- **In every five scenes, at least one of each:**
  - a scene where someone is petty, cruel or wrong and is not redeemed;
  - a Kin who is wrong, and loses (to a human, ideally one who deserved to win: DOC-00B §10);
  - a document or unusual form (§5.2);
  - a scene with no human in it at all, or no Kin;
  - a comedy.
- **Length varies.** The collection has sat at 1,400–2,200 words. Some scenes should be 400 and some 5,000.
- **Tense and person vary.** Past-tense close third dominates. Present tense has appeared once (S008). Second person has not appeared.

#### 6.3 The spent list
A beat used in the collection is **spent**. DOC-00F §9 already does this for social details. `tools/tells_patterns.tsv` extends it to the stock beats in §3.8 and marks each **rested**. A new scene that reaches for a rested beat fails the linter. When a scene introduces a strong new beat, add it to the table as `rested` after the scene is accepted.

#### 6.4 Names
The name pool is small and shared (R02 §8). New characters draw from outside the recurring set (Sable, Sorrel, Sedge, Ilex, Ashe, Kirin, Lyric, Fern, Kaelen, Rowan). Canon lets names pass down, so reuse must be a *choice the scene uses*, never a default. Human names avoid the model defaults (Elara, Marcus, Sarah, Elena, Kael, Lyra: R01 §1, the "promptonym" lists).

---

### 7. EXEMPLARS AND READERS

**Exemplars are the strongest lever there is.** AI fine-tuned on an author's work flipped expert readers' preference (R01 §4, Chakrabarty et al.). We cannot fine-tune here. The nearest thing is real prose, in the writer's context, before drafting.
- **X01 first** *(2026-09-25)*: `offcanon/X01_equestria/chapters/` is the best writing the project has made, by the owner's judgement, and every chapter passed the owner's read. For a Kin POV give the drafter a Kin chapter (ch. 2, 4, 6 or 8); for a human or outsider POV, an outsider chapter (ch. 3, 5 or 7). It is off-canon: take its texture, never its facts.
- **In-house shelf:** S012alt (whole), S006 §1–§2, S017's game, S010's minutes. These are the most human pages in the collection.
- **Estee**, *Daily Equestria Life With Monster Girl* (R03): the owner's chosen model for a non-human mind. Chapters 1, 10 and 30 are on the shelf.
- **Owner's shelf:** passages the owner chooses from writers whose voice they want in the room, and any of the owner's own writing. **This is the missing piece.** It should be filled before the next scene (`research/SHELF.md`).
- **Readers.** A model is not the final reader: LLM judges did not correlate positively with expert judgements of story quality (R01 1.6). The pipeline uses model readers to *find* things (a cold read, a predictability pass) and never to *pass* a scene. The owner passes scenes.

---

### 8. WHAT THE TOOL CAN AND CANNOT DO

`python3 tools/tells.py scene <file>` reports the house tells with line numbers, the scene's shape (sentence-length variation, one-line paragraphs, stingers, dialogue share, participial clauses), phrasing recycled from other scenes, and how close the narrator sits to the rest of the collection. It exits 1 if the scene is over budget.

**It can find:** every pattern in §3, the rested beats, recycled phrasing, number tics, and a narrator who measures as the house voice.
**It cannot find:** whether anybody wants anything (§2.1), whether it escalates (§2.4), whether the detail is alive (§2.3), or whether the scene is any good. **A scene that passes is not thereby human.** A scene that fails a *limited* budget because a character talks that way can stand, if a note in the brief says why.
**Its numbers now have one human baseline.** `python3 tools/tells.py baseline <folder>` measures a reference text against the collection. The first is Estee's 715,000-word novel (R03 §1): explaining at 0.03 per 1,000 words against the collection's 0.77, the gnomic aside at 0.15 against 1.89, and dialogue at 22% against 8%. One author in one genre is a reference point, not a target. Tune them in `tools/tells.py` (`BUDGET`, `LIMITS`) as the owner's judgements accumulate.

---

### 9. A WORKED REVISION

**S021, the opening, as written** (tells marked):

> The thing about the whistle is that nobody thinks about it *[G09]*, which is the whole of what it is for *[E01]*.
>
> Rowan had been on the transfer deck since the shift turned, up in the rails where the light was bad, running a hand along a conduit that had been making a noise for three days and had stopped making it the moment anyone came to look. Sable was forty metres down-deck with the other end of the same problem. Fern was somewhere below, doing something to a cable run and complaining about it in short flat Bursts that Rowan was only half taking.
>
> Every so often one of them whistled. Not for anything. *[R02]* ⟨*left of you*⟩, ⟨*done*⟩, ⟨*are you going to be much longer*⟩, and once, from Fern, a rude one about the cable run.
>
> You do not think about it. You would not think about breathing. *[G05 ×2; stinger]*
>
> The humans moved around underneath all of this, six of them on the day crew, and the whistle went over their heads the way weather goes over a house. *[G02-shaped simile; lore stated]*

The middle is good: the conduit that goes quiet when someone looks at it, the rude whistle. The frame is the house voice explaining D-88.

**Revised to the standard.** The frame is cut, the whistle's privacy is shown rather than stated, and there is one detail that demonstrates nothing:

> The conduit had been ticking for three days and it stopped the second Rowan put a hand on it, which was the third time it had done that, and hir was starting to take it personally.
>
> ⟨*anything?*⟩ Sable, from the far end of the run.
>
> ⟨*it knows*⟩
>
> Fern was under the grating with a cable tray, and had been whistling the same two notes about it for an hour. In Fern's mouth those two notes covered the tray, the tray's installer, the installer's Cluster and, some way back, their lineage.
>
> Down on the deck the day crew went about their business, six of them, and not one looked up. Idris's mug was still on the rail by the lift. It had been there since Tuesday.

**The ending, as written:** after *"That's it," said Rowan.* come two more sections. One is on how the story spread to an ark. The other is a coda eight years on that explains the secret and closes on *"Rowan is not going to be the one."*

**Revised, option A:** stop at *"That's it," said Rowan.* The reader already knows what Idris has just said and that nobody corrected him. Explaining it takes that away from them, and so does the time-jump confirming it.

**Option B, from the cold reader** (`scenes/briefs/S021_coldread_2026-09-24.md`): keep the coda's one image, *Eleven years became nineteen*, and the Cluster going still for a quarter of a second every morning. Cut everything that explains it. The reader called that stillness the best image in the story. Where the pipeline's readers disagree like this, the owner decides (DOC-00H Stage 7).

Find the person, cut the explaining, add a detail that belongs to somebody, and stop when it is over.

---

### 10. WHAT X01 TAUGHT *(added 2026-09-25, the owner's and the orchestrator's debrief)*

X01 (`offcanon/X01_equestria/`) is eight chapters, about 35,000 words, written through DOC-00H and passed by the owner one chapter at a time. These are the lessons that generalise. Each is tied to the chapter that taught it.

#### 10.1 The Cluster is the unit *(the owner)*
**The default Kin cast is a Cluster, not a Kin.** X01's five played off each other and worked as parts of one whole. The scenes only Kin can have need several of them at once:
- the noon argument over the cloud (ch. 6);
- Madder's forty-one seconds of silence (ch. 6);
- the barn silent to the fillies while the radio was loud (ch. 8).

Kin-code on the page needs several people on it. A lone Kin talking to a human (S024) has to carry everything through speech, the channel Kin like least.
- **Cast by role**, so the voices differ by function as well as by card: the one in charge (Madder), the face (Sloe), the hands (Yarrow), the wild one (Haw), the young one who is hiding something (Teasel). Four to six is the working range; five was right.
- **Loud radio, silent room.** When outsiders are present, the Cluster's argument happens in code while the room goes still. Outsiders see only stillness. The POV Kin hears everything. This is the Kin's own dramatic device, and no human cast can do it.
- **One Kin alone** is still allowed. It is a choice with a cost to state in the brief (a frameless Kin, an envoy), not a default.

#### 10.2 Ban the surface, keep the trait
The predictability pass bans tropes. **A trope ban can strip out the trait under it.**
- Banning Twilight's *"Fascinating!"* produced an incurious Twilight (ch. 5, caught by the owner).
- *"Kin-code, sparingly"* produced Kin who talked aloud (ch. 2).

**Rule:** for every character-level ban in the predictable list, the brief names **the trait that must survive it**. Example: *Not* "Fascinating!", *not* a scan spell; **but** burning to know, and holding it back.

#### 10.3 No evenly spaced echoes
The cold reader's most reliable "a model wrote this" came from structure, not sentences:
- a detail lingered on so that it can pay off (ch. 6: the stake's *tick*);
- callbacks spaced to be collected (ch. 7: Thursday, the hem, the carried foal and the carried Kin);
- a closing image mirrored from an opening one (ch. 8: the hands);
- S025's tidy plant and payoff.

A callback is fine. **A pattern of callbacks is the tell.**
- Plant without lingering.
- Let at most one echo per chapter land.
- Never explain the rhyme: cut the line that says *it was the same sound as…*

`tells.py` cannot see this. The cold reader can (question 9), and the predictability pass should list the likely echo.

#### 10.4 Every point of view has a person and a lens
- **A person** *(the owner, after ch. 3)*: the teller mutters, reacts, and has thoughts of hir own that have nothing to do with the plot. Fluttershy's jackdaw, Twilight's *Winter Orchard*, Rarity's christening hem. A few, lightly. The work still carries the chapter.
- **A lens.** Each teller orders the world by one habit of attention: Fluttershy's animals, Sloe's counts, Yarrow's loads, Twilight's lists, Rarity's workmanship, Teasel's *what everyone is eating*. The lens did more to make the chapters distinct than the voice cards did. **It goes in the voice card's *Notices* field as one sentence, and the drafter is told to run the chapter through it.**

#### 10.5 World logic and period
The owner caught what no model reader did:
- a town clock that the Mayor could not have known was fast (ch. 4);
- a rubber band in a world without them (ch. 5);
- sleeping Kin who would breathe, rarely and together (ch. 5);
- the Kin seeing the weather team and saying nothing (ch. 4).

**Before the owner's read, the orchestrator runs a world-logic pass:**
- Who could know this?
- Does this object exist here?
- What would these people have seen and not remarked on?
- Does the physiology do what canon says?

#### 10.6 Canon is the engine, not the decoration
The best chapters put a canon mechanic under pressure:
- the account (D-103) drove ch. 8's confrontation;
- the theta lock drove ch. 5's terror;
- regrowth costing calories drove Teasel's hunger;
- the Core's numbers drove the pegasi (ch. 4) and the cloud (ch. 6).

None of them explained the mechanic. This is §4's lore budget working as intended: two mechanics, **used**, not shown.

#### 10.7 Revisions overcorrect, in both directions
Told to order clauses, a reviser wrote *because*-glosses (ch. 2). Told to cut and-chains, a reviser chopped every sentence short (ch. 5, narration mean 12.2, CV 0.71). `tells.py` now warns on chopped prose as well as strung prose (Estee's 10th percentile: narration mean 10.6, CV 0.73). **After every model revision, the orchestrator reads the whole chapter**, not the diff, and hand-rejoins anything chopped.

#### 10.8 What only the owner catches
In X01 the model readers caught continuity, arithmetic, positions and tells, and never once *"this character is wrong"* or *"this doesn't fit the world"*. Every chapter's largest single improvement came from the owner's read. **A cold session gets the owner's standing notes from `research/OWNER_TASTE.md`**, and the owner still reads every chapter.

#### 10.9 Length
Chapters ran about 30% over target. Most of the overrun was the owner's notes adding what was missing (chatter, interiority, a section on magic). **Budget a long work at target × 1.3**, and don't cut to hit a number the owner didn't ask for.

