# PROJECT ELYSIAN: COMPREHENSIVE WORLD & SPECIES ARCHIVE
## Document ID: DOC-00I — Illustration: Pictures That Stay Beside the Text
**Classification:** Tool, not canon. Governs illustrations for the project's ebooks. DOC-00C governs what a Kin looks like; this document governs how a picture sits in a story.
**Status:** v0.1 DRAFT, 2026-09-25. Written from the owner's brief. **Nothing is generated yet**: generation waits for the owner's OpenRouter key (ROADMAP Step 13). Revise after the first owner's read of real pictures.

---

### 0. THE BRIEF, IN THE OWNER'S TERMS
Like the inline pictures in *The Chronicles of Narnia*: small reference images in the text that give the reader **something to visualise without trying to replace the text**. They supplement it.

### 1. WHAT A PICTURE IS HERE
- **Small and inline.** A spot illustration, set in the text next to the moment it shows, not a full-page plate. In the EPUB it is at most about 60% of the page width and 14 em high (`tools/build_ebook.py`, `figure.spot`).
- **One style.** Pen-and-ink line work with light hatching, black on white, no colour, and no painterly rendering. Every picture in a work looks like it came from the same hand.
- **A moment or a thing, rarely a portrait.** Haw's egg cracked one-handed on a knee; the tiller gatepost; the pegasus asleep on a cloud with an oat on her lip; the ledger. Faces are small or turned. **The prose owns the faces and the feelings.**
- **One to three per chapter**, placed where the reader would like to see something, not at the chapter's climax. **A picture never shows what hasn't happened yet on that page.**
- **Never explains.** If the prose leaves a thing unsaid (whose ribbon it is, what the sound was), the picture doesn't say it either.

### 2. WHAT MUST BE RIGHT
Image models get the Kin wrong in predictable ways. Every picture with a Kin in it is checked against DOC-00C before it goes in:
- **six limbs**: two slim human-pattern arms hanging from the yoke, **four hand-paws** with thumbs;
- a **horizontal body**, low (withers ~0.45 m), and the **tail about half the length** of the body (~1 m, thick at the root);
- ears **longer than the skull**; eyes large and forward;
- **60 kg**: not horse-sized, not cat-sized.

For a long work, keep a **reference sheet** (one small turnaround per recurring character, in the work's style) and give it to every generation call, so the same Haw is in every picture.

### 3. HOW IT IS MADE (once there is a key)
1. **An illustration brief per chapter**, written by the orchestrator after the owner passes the chapter: for each picture, the line it sits next to, what is in the frame, what must be anatomically right, and what must not be shown.
2. **Generate** with the style prompt, the reference sheet and the brief.
3. **Check** against §1 and §2. Reject and regenerate rather than patch.
4. **Place.** Add `![](images/chNN_mm.png)` on a line of its own in the chapter file (caption optional and short), and rebuild the EPUB.
5. **The owner reads the illustrated EPUB.** Their notes go into `research/OWNER_TASTE.md`, as for prose.

### 4. OPEN QUESTIONS (for the owner)
- Captions or none? Narnia mostly had none.
- Is a single frontispiece per book wanted, in addition to the spots?
- One style for every work, or one per work (a crossover might borrow its source's look)?
