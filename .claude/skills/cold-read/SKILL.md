---
name: cold-read
description: Cold-read a Project Elysian scene the way a stranger would — a fresh reader with no lore, no brief and no standard marks every line that explains, lectures, sounds written, or feels generated, and names the first place it thought a model wrote it. Use on any scene draft or existing scene before revising it (DOC-00H Stage 5), or when the user asks to "cold read", "critique", "review the prose of", or "find what feels AI" in a scene.
---

# Cold read

Stage 5 of DOC-00H. The reader must be **fresh**: it has not seen the brief, DOC-00B, DOC-00G, the canon docs, or other scenes, because a reader who knows the lore forgives the lore lectures. You are the orchestrator; you do not do the reading yourself.

## Steps

1. **Extract the prose.** Take the scene file's prose only: after the header block, stopping at `## Canon` / `## Offers`. Write it to the scratchpad with line numbers (`nl -ba`). Do not include the header, since it names the canon rulings.

2. **Run two agents in parallel**, both `general-purpose`, in one message:

   **a. The cold reader.** Prompt = the full text of `reader_prompt.md` in this folder, followed by the numbered prose. Nothing else. No title, no header, no lore.

   **b. The collection reader.** Prompt:
   > You are checking whether a new story in a collection repeats the collection. Below are (1) the new story's first and last paragraphs, (2) the last five rows of the collection's ledger, and (3) every opening and every ending in the collection so far. Answer one question, concretely, in at most 250 words: what does the new story repeat, in shape, move, image, phrasing, ending or tone? Name the earlier story each time. If it repeats nothing, say so.

   Attach: the first and last paragraph of the scene; the last five rows of `scenes/LEDGER.md`; sections 5–6 of the output of `python3 tools/tells.py corpus` (run it to a scratchpad file).

3. **Also run the linter** yourself: `python3 tools/tells.py scene <file>`. Keep the Budget block.

4. **Report** to the user, or into the brief's *Cold read* section when running inside `/scene`:
   - the cold reader's **"first place a model"** answer, verbatim, at the top;
   - the explaining sentences and written-sounding dialogue, with line numbers;
   - the worst moment and whether it is after the midpoint;
   - the collection reader's repeats;
   - the lint budget block;
   - a **cut list**: the lines that all three sources (reader, collection, lint) point at. Those are the first to go.

Do not rewrite the scene in this skill. Revision is DOC-00H Stage 6, and it starts from this report.
