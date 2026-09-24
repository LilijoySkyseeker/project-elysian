# R01 — What reads as machine, and what reads as a person
**Research dossier behind DOC-00G (the prose standard) and `tools/tells.py`.** Compiled 2026-09-24.
**Status:** Evidence file, not canon. When a rule in DOC-00G cites "R01 §n", this is the n.

## How this was gathered, and what that limits

Two research passes ran on 2026-09-24: one on the academic literature and one on craft and practitioner sources. **This environment's network policy blocked most primary sources**: arXiv, ACM DL, PNAS, Nature, ACL Anthology, Wikipedia, SFWA, Substack, the New Yorker and Project Gutenberg. The pages that could be opened directly were GitHub repositories, including the ones that publish the code and word lists behind several of the papers. Everything else below comes from **search-engine abstracts and snippets, not full text read on the page**.

Each claim is marked with its access status:
- **[read]**: the page itself was opened.
- **[abstract]**: from the search-result text of the paper's own page. Usually the abstract, and it may be paraphrased by the search engine.
- **[secondary]**: from someone else's summary of the source. Weakest; check before quoting.

**Before quoting any figure below in public, check it against the PDF.** Nothing here has been verified to that standard. That is why every rule in DOC-00G is written so that it still stands if one number turns out to be off.

A second limit is the models studied. Most papers test GPT-4-era models, and one of the older ones tests Claude v1.3. Only StoryScope (§3) looks at a current Claude. The collection in this repo is the best evidence available about current Claude on *this* material, which is why R02 (the diagnosis) matters as much as this file.

---

## 1. Within a text: the measured tells

| # | Finding | Source | Status | Used in |
| :-- | :-- | :-- | :-- | :-- |
| 1.1 | Professional writers edited 1,057 LLM paragraphs (8,000+ edits). Edit categories by share: awkward word choice/phrasing 28%, poor sentence structure 20%, **unnecessary/redundant exposition 18%**, cliché 17%; also purple prose, lack of specificity, tense inconsistency. No significant difference between GPT-4o, Claude 3.5 and Llama 3.1. | Chakrabarty et al., "Can AI writing be salvaged?", CHI 2025, arXiv 2409.14509 | [abstract] | DOC-00G §3 E, §7 cold-read categories |
| 1.2 | Instruction-tuned LLMs use **present participial clauses at 2–5× the human rate** and nominalisations at 1.5–2×, and the gap persists even when prompted to write informally. The gap is larger for instruction-tuned models than for base models. | Reinhart et al., "Do LLMs write like humans?", PNAS 122(8), 2025 | [abstract] | `tells.py` participle metric |
| 1.3 | Some "slop" patterns appear **over 1,000× more often** in LLM fiction than in human text. The published lists are model- and era-specific. | Paech et al., "Antislop", ICLR 2026, arXiv 2510.15061; lists in github.com/EQ-bench/creative-writing-bench and github.com/sam-paech/antislop-sampler | lists [read]; paper [abstract] | `tells_patterns.tsv` L01–L04 |
| 1.4 | **Negative parallelism** ("It's not X, it's Y"; "no…, no…, just…") is 25% of the Slop Score, detected with 10 regexes and 35 part-of-speech patterns, including forms that span two sentences. | github.com/sam-paech/slop-score README | [read] | R01–R06, the house tic |
| 1.5 | Models reuse part-of-speech templates (4–8 grams) at a higher rate than human text; 76% of model templates occur in pre-training data, against 35% of human text; templates survive RLHF. | Shaib et al., "Detection and Measurement of Syntactic Templates", EMNLP 2024 | [abstract] | DOC-00G §5 (why a scene can't be rescued by swapping words) |
| 1.6 | Against the 14-test Torrance Test of Creative Writing, New Yorker stories passed 84.7% of tests, GPT-4 27.9% and Claude v1.3 30.0%. LLM judges' ratings did not correlate positively with the experts'. | Chakrabarty et al., "Art or Artifice?", CHI 2024, arXiv 2309.14556 | [abstract] | DOC-00G §7: **a model is not the final reader** |
| 1.7 | LLM stories "struggle to adequately develop critical turning points… the major setback and climax"; human stories show higher suspense, "with the gap enlarging from the midpoint to the end"; LLM stories are "homogeneously positive and lack tension." | Tian et al., "Are LLMs capable of human-level narratives?", EMNLP 2024 | [abstract] | DOC-00G §2.4 (escalation) |
| 1.8 | The EQ-Bench creative-writing rubric scores against "Incongruent Ending Positivity", "Unearned Transformations", "Tell-Don't-Show", "Weak Dialogue", "Overwrought", "Purple Prose", "Meandering". | github.com/EQ-bench/creative-writing-bench | [read] | cold-read rubric |
| 1.9 | Wikipedia's editors catalogue "undue emphasis on symbolism, legacy and significance", rule of three, trailing participle analysis, elegant variation, false ranges and didactic closers, and warn that many of these also appear in human editorials, blogs and fan fiction. | Wikipedia: Signs of AI writing (WikiProject AI Cleanup) | a third-party copy [read]; the live page blocked | DOC-00G §3 |
| 1.10 | Em-dash overuse: only an independent preprint (GPT-4.1 at 3.28× in essays) and population-level trend preprints. Writers have pushed back hard, because the em dash is a human habit too. | Freeburg, arXiv 2603.27006; Washington Post Apr 2025, The Ringer Aug 2025 | [abstract]/[secondary] | **Not a rule.** Reported, never budgeted |

**What was looked for and not found:** no peer-reviewed study of "not X but Y" or of tricolons in *fiction*. Both are well attested in practitioner catalogues (1.4, 1.9) and Paech's detector, but not measured in a fiction study.

## 2. Across texts: sameness

| # | Finding | Source | Status |
| :-- | :-- | :-- | :-- |
| 2.1 | LLM stories "consist of plot elements that are echoed across a number of generations" and across different LLMs, "at all semantic levels and not necessarily in the same order"; human plots are rarely recreated. The **Sui Generis** score (resample continuations from each prefix, then check which segments recur) correlates with human judgements of surprise. | Xu et al., "Echoes in AI", PNAS 2025, arXiv 2501.00273; code github.com/microsoft/SuiGeneris | README [read]; paper [abstract] |
| 2.2 | Stories written with AI-generated ideas were rated more creative and better written individually, but were **more similar to each other**. | Doshi & Hauser, Science Advances 2024 | [abstract]; how similarity was measured is unverified |
| 2.3 | InstructGPT (but not base GPT-3) increased similarity between different authors' writing and reduced lexical and content diversity. | Padmakumar & He, ICLR 2024 | [abstract] |
| 2.4 | "LLM responses are much more similar to other LLM responses than human responses are to each other." Measured on creativity tests, not fiction. | Wenger & Kenett, arXiv 2501.19361 (preprint) | [abstract] |
| 2.5 | LLMs "struggle to match human stylistic variation": low variance across texts is itself a signal. | Reinhart et al. (1.2) | [abstract] |
| 2.6 | EQ-Bench's repetition metric counts words and n-grams that recur **across at least two different prompts** and ranks them against a human frequency profile. That cross-prompt filter is the collection-level check. | github.com/EQ-bench/creative-writing-bench `core/metrics.py` | [read] |

## 3. Narrative structure, and Claude specifically

**StoryScope: Investigating idiosyncrasies in AI fiction**: Jenna Russell, Rishanth Rajendhran, Chau Minh Pham, Mohit Iyyer and John Wieting (University of Maryland / Google DeepMind), arXiv 2604.03136, 2026. A preprint; no venue seen.
- **[read, GitHub README, github.com/jenna-russell/storyscope]** 61,608 stories of about 5,000 words from 10,272 prompts (one human and five LLMs per prompt), 304 features across 10 narrative dimensions. Narrative features *alone* separate human from AI at 93.2% macro-F1, and AI stories "cluster together in narrative space."
- **[secondary: several write-ups, one of them by a company that sells story software]** AI narrators state the theme outright about 77% of the time, against about 52% for humans. Dialogue is used for philosophical debate about 59% of the time, against about 34%. Plots are tidy and single-track. **Claude** shows "flatter event escalation and quieter endings", "event intensity escalates less than in any other source", and "narrative voice is the most uniform." Narrative features kept over 97% of the detection power of the style-plus-narrative model.
- **[abstract — search text of the paper page, confirmed a second time]** "AI stories over-explain themes and favor tidy, single-track plots while human stories frame protagonist choices as more morally ambiguous and have increased temporal complexity." "Claude produces notably flat event escalation"; Claude is "characterized by a uniform narrative voice, a restrained approach to event intensity, and **a preference for epilogues** while avoiding dream sequences." Which section of which version holds that wording is not confirmed.
- **Why it matters here:** it predicts, from outside, exactly what R02 measured inside this collection. The collection has quiet endings, stated meaning, gentle arcs and one narrator. It also shows that **scrubbing style cannot fix structure**, because structure alone gives the game away.

**Concreteness (not fiction-specific).** Wang et al., "Is Human-Like Text Liked by Humans? Multilingual Human Detection and Preference Against AI", ACL 2026 (arXiv 2502.11614) [abstract]: 19 expert annotators, 9 languages, 87.6% average detection. "The major gaps… lie in concreteness, cultural nuances, diversity in length, structure, style, and sentiment." Human text carries "concrete numbers, specific names… exact places or dates… while machine-generated text tends to provide generic information." Concreteness is listed first among the gaps; the abstract does not rank it first. **Note for this project:** our scenes are *not* generic. They are full of numbers. R02 §3 argues that the numbers have become a performance of concreteness. They are precise about the lore and vague about life.

## 4. What readers can and cannot tell: the counter-evidence

These are the reasons DOC-00G is a craft standard and not a detector-evasion checklist.
- **Readers often can't tell, and sometimes prefer the AI.** Porter & Machery, Scientific Reports 2024: 1,634 participants, 46.6% accuracy on poetry, AI poems rated more favourably [abstract]. Mark Lawrence's blind flash-fiction test, reported by PC Gamer in Aug 2025: 964 voters were at chance and preferred the AI stories [secondary]. Both involve *short* texts. Tells accumulate with length and across a collection, which is this project's exposure.
- **Heavy LLM users detect very well, mostly through vocabulary.** Russell, Karpinska & Iyyer, ACL 2025: five frequent-LLM-user annotators misclassified 1 of 300 articles (non-fiction) [abstract].
- **Folk heuristics are wrong.** Jakesch et al., PNAS 2023: people wrongly read first-person pronouns, "authentic" words and family topics as signs of a human [abstract]. Faking these doesn't work.
- **Tell-hunting misfires on plain human prose.** Liang et al., Patterns 2023: detectors flagged more than half of non-native TOEFL essays [abstract]. Wikipedia's own list warns that its tells also appear in human writing (1.9). **Budgets, not bans, for anything a good human writer also does.**
- **Anchoring to a real author closes the gap.** Chakrabarty, Ginsburg & Dhillon, arXiv 2510.13939 / CHI 2026: MFA readers strongly disfavoured *prompted* AI (quality OR 0.13) but favoured AI *fine-tuned on an author's work* (OR 1.87) [abstract]. We cannot fine-tune here. The nearest lever is real human exemplars in context, which DOC-00G §7 and the pipeline use.
- **Experts and lay readers read differently.** Marco et al., ACL Findings 2025 [abstract]. The owner of this project is the expert reader; the pipeline ends with them.

## 5. Craft sources: the positive standard

Mostly [secondary] or [abstract] (search snippets of well-known quotations). They are standard quotations, but none was checked against a primary text this session.
- **Saunders**: "Always be escalating… A swath of prose earns its place… to the extent that it contributes to our sense that the story is (still) escalating." Also: read a page at a time and track what the reader knows, wants and expects, then satisfy the expectation, but not too neatly. (*A Swim in a Pond in the Rain*, 2021.)
- **Hemingway**, *Death in the Afternoon* ch. 16, omission: the writer "may omit things that he knows and the reader… will have a feeling of those things as strongly as though the writer had stated them."
- **Gardner**, *The Art of Fiction*: the "vivid and continuous dream"; profluence as "a sequence of causally related events"; psychic distance as something the writer controls deliberately.
- **Chekhov**, letter to Alexander Chekhov, 10 May 1886: the broken bottle glinting on the mill dam. **Quote Investigator** shows the popular "Don't tell me the moon is shining…" is a later paraphrase and not Chekhov's line.
- **Orwell**, "Politics and the English Language": never use a figure of speech you are used to seeing in print.
- **Elmore Leonard**, NYT July 2001: use "said"; "leave out the part that readers tend to skip."
- **Le Guin**, *Steering the Craft*: exposition should be ground fine and made "into bricks to build the story with", not left in lumps. Writer and reader "collaborate in world-making."
- **Turkey City Lexicon** (ed. Shiner and Sterling, hosted by SFWA): *info-dump / expository lump*, *"As you know, Bob"*, *white-room syndrome*, *"call a rabbit a smeerp"*, *pushbutton words*, *eyeball kick*.
- **Jo Walton**, *incluing*: "scattering information seamlessly through the text, as opposed to stopping the story to impart the information."
- **Collections**: advice from collection-arrangement pieces is to vary length, POV, tone, the span of time covered and structure [secondary; attribution unclear]. **No reputable source was found on differentiating narrators' voices across a collection.** DOC-00G §5 is our own method there, and says so.

## 6. What this dossier does not support

- Any claim that a scene "passes as human" because a tool says so. No tool here or anywhere measures that reliably (§4).
- Banning the em dash, or any single word except the true stock phrases.
- Any specific human-baseline number for this project's metrics. No human corpus could be downloaded here (Gutenberg was blocked). `tells.py` reports relative figures and one in-house anchor (R02 §2).
