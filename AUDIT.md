# PROJECT ELYSIAN — DESIGN AUDIT
**Scope:** All nine DOCs + deep-dives 01B, 01D, 01E, 01E.1.
**Status (2026-09-19):** HISTORICAL — every C, P, G and E item below was resolved by the decision logs in `CANON.md` §11–§15 and folded into the v2.0 docs. Kept as the record of what was wrong and why.
**Method:** Every quantitative claim was recomputed (σ = 5.67×10⁻⁸, c = 3×10⁸, 20.1 kJ/L O₂, 4,184 J/kcal). Cross-document claims were diffed. Each finding carries a recommendation; the decision is yours — nothing in `docs/` has been altered.

Three registers: **C** = conflicts between documents · **P** = physics/biology problems · **G** = gaps (things the design needs and nobody has written) · **E** = editorial.

---

## C — CONFLICT REGISTER (doc vs doc)

### C-01 · VHF tail antenna band — 75–95 MHz (DOC-01) vs 150–220 MHz (DOC-01D)
DOC-01D also contradicts itself, calling the tail both a "quarter-wave whip" and an "omnidirectional dipole".
Geometry check for a 0.86–0.88 m tail:
- 85 MHz: λ = 3.53 m → λ/4 = **0.88 m** — the tail *is* a quarter-wave monopole, body as ground plane.
- 175 MHz: λ = 1.71 m → λ/2 = **0.86 m** — the tail *is* a half-wave dipole.
Both are physically consistent; they are just different antennas.
**Recommend:** 75–95 MHz λ/4 monopole. It is the original spec, matches the "whip" description, and lower VHF diffracts around structure better (which is the whole point of the tail band). Amend DOC-01D §2B.

### C-02 · VHF power — 0.1 / 1 / 10 W ladder (DOC-01B) vs 5.0 W burst (DOC-01D)
Not contradictory, just unaligned. **Recommend:** keep 01B's ladder as canon; 01D's 5 W becomes "typical bulkhead-penetration burst".

### C-03 · Daily caloric budget — 3,500–5,000 kcal (DOC-01) vs 1,800–2,400 baseline / 4,500–5,000 peak (DOC-01B)
DOC-01 quotes the peak band as if it were baseline. **Recommend:** errata DOC-01 §4 to "~2,200 kcal/day baseline, 4,500–5,000 under sustained RF/locomotion load".

### C-04 · Fascial counter-pressure — 12–15 kPa (01E) vs ≥15 kPa (01E.1)
Trivial. **Recommend:** 15 kPa nominal. (Both clear the 6.3 kPa Armstrong limit with margin.)

### C-05 · Lung oxygen content — "3.5 L at 100 % O₂" (01E.1) vs "sealed at pre-exposure ambient" (01E)
Kin sectors are described as normal-atmosphere shared habitats. A lung sealed on 21 % air holds **0.73 L** O₂, not 3.50 L, dropping the total reserve to 3.33 L and the aerobic window to **9.3 min**. Nothing in the archive concentrates O₂ before a seal. → resolved jointly with **P-04** below.

### C-06 · Conscious vacuum survival time — 15–30 min (01) · 4 h (01E) · 30–40 min + suspended torpor (01E.1)
DOC-01E.1 is the intended reconciliation (State A = short conscious; State B = long unconscious) but DOC-01E still says torpor "preserves consciousness in a reduced, low-rate mode for up to 4 h". **Recommend:** State B is *unconscious* (Bio-Core heartbeat only). Errata 01 §3 and 01E §1B.

### C-07 · Voiding cascade ordering — 01E puts torpor as an automatic final step (<50 ms); 01E.1 makes torpor conditional on ΔT/pH thresholds
**Recommend:** adopt 01E.1. Redraw the 01E cascade: Airway Lock → Fascial Compression → *State A (default)* → State B on threshold or voluntary command.

### C-08 · "Cryogenic torpor" (01E, 01E.1)
The body is at 37 °C and, in shadow, cools at most ~1 K/25 min. **Recommend:** *hypometabolic torpor*. (Though note P-03: deliberate cooling turns out to be the right design.)

### C-09 · Body length vs. mass — **resolved, D-68**
`CANON.md` §1 gave 1.4–1.6 m (chest → tail root) at a 50 kg reference. The two were set independently and are incompatible: at *any* plausible girth a 1.4–1.6 m trunk implies 115–160 kg (mammalian M/L³ runs 22–30 kg/m³; a real 55 kg leopard has a 0.85 m trunk). **Resolved:** the length was wrong, not the mass. Trunk → 1.00–1.15 m; mass → 50–70 kg with a 60 kg reference. See D-68.

### C-10 · Laplace torso radius `r = 0.18 m` (DOC-01E.1 §4) — **resolved, D-68**
A 0.36 m-diameter torso makes the two trunk segments 123 L = 127 kg on their own, and gives them 1.52 m² of surface against the 1.34 m² whole-body figure DOC-01E.2 §3 derives for the same animal. The figure was a conservative worst case for a fascial-tension result and was never morphology. **Resolved:** the fascia compresses the limbs and abdomen, not the rib-braced thorax, so the governing radius is the barrel's, r = 0.07 m → T = 1,050 N/m. Latch cost 3–5 W; still non-limiting.

---

## P — PHYSICS & BIOLOGY AUDIT

### P-01 · Radiotrophic energy yield is impossible — **hard fail**
DOC-01E claims 15–18 W of ATP from ambient radiation at >15 mSv/h.
- 15 mSv/h ≈ 15 mGy/h = 0.015 J/kg/h × 50 kg = **0.2 mW** total absorbed power.
- Even at the stated 5 Gy/day tolerance ceiling: 5 × 50 / 86,400 = **2.9 mW**.
The claim is off by 10⁴–10⁵. Ambient space radiation carries no harvestable energy; the real radiotrophic fungi effect is a growth-rate nudge, not a power source. The "36 h Radiotrophic Mode" column in 01E §4 rests entirely on this.
**Recommend (choose one):**
- **(a) Demote.** Keep the melanin-metal matrix as *shielding* (UV, soft X-ray, β, trapped-belt protons) plus the Ku70/80–RAD51 repair suite as the real defence. Strike the ATP pipeline and the 36 h column. This is the clean fix.
- **(b) Re-aim at sunlight.** 1,361 W/m² × 0.15 m² = 204 W incident; a 5 % photo-conversion pelt yields ~10 W, which *would* offset State B. But absorbing sunlight is exactly what kills you thermally (see 01E.1 §2D-3). Only viable if paired with P-03's albedo control.
- **(c) Keep as declared soft-SF.** Then it should be flagged as such in the doc, because everything else in 01E.1 is done to hard-SF standards and the contrast is jarring.
The same section's "absorbs 65 % of incident radiation" is also over-claimed for GCR (GeV protons ignore a millimetre of skin) but fine for UV/β/soft-X.

### P-02 · State B oxygen budget does not close — **hard fail**
State B is specified at 6–8 W for 4–12 h. O₂ demand at 8 W = 0.024 L/min:
- 4 h → **5.73 L** (94 % of the *entire* 6.10 L reserve — and only if State A was never used)
- 12 h → **17.2 L** (nearly 3× the reserve)
If State A runs first, the reserve is exhausted at 17 min and State B has *nothing*. The two-state architecture in 01E.1 is right, but the numbers underneath it were never integrated.
**Recommend — the O₂ Partition Rule + cooled torpor:**
1. Myoglobin O₂ (1.33 L) only unloads at very low pO₂ — physiologically it *is* the last-ditch reserve. Define it as the **State B floor**; State A auto-terminates when lung + Hb are spent, leaving Mb untouched.
2. Drop torpor draw to **~2 W** (≈ 2 % of active — deep-torpor mammals reach this, but only with a cooled core). 1.33 L / 2 W → 3.7 h; 6.10 L / 2 W (immediate torpor, no State A) → 17 h.
3. Make cooling deliberate: with ears open the body sheds a net 63 W in shadow and drops 2 K every 91 min. Let State B *ride that down* to ~25–30 °C. Q₁₀ ≈ 2.5 halves O₂ demand for each −7 K.
Result: "4 h after a full State A / 12+ h if you go straight to drift" — the *original* numbers become true. This needs a coupled thermal–metabolic model (→ ROADMAP #2).

### P-03 · Thermal model is ear-only; the pelt and the throttle are missing
01E.1 treats 71.2 W of ear radiation as the *only* loss and treats it as fixed. Two omissions:
1. **Whole-pelt radiation.** 1.2 m² of fur surface radiates ~415 W at 10 °C — obviously the fur surface will not be at 10 °C; in vacuum (no trapped air) fur is an excellent insulator, so the outer hair layer settles far colder and passes perhaps 20–60 W. But that is still a 30–80 % correction to the shadow budget, and it may flip "overheats in shadow at 120 W" to "roughly neutral". The 118 min shadow figure is therefore a *lower bound*, and the real shadow limit is probably O₂/acidosis alone.
2. **Ear throttle.** The ears have a venous plexus precisely so blood flow — hence dish temperature — can be modulated. Vasoconstricted ears at ~0 °C radiate ~16 W, not 71 W. So the organism controls its radiator between ~15 and ~71 W. This is the lever that makes P-02's cooled torpor a *choice* rather than an accident, and it needs to be in the model.
**Recommend:** add two terms — `P_pelt(T_core, fur insulation)` and `P_ear(f_perfusion)` — and re-run the four scenarios. Also consider an **albedo reflex** (arrector pili lift pale underfur → α from 0.70 to ~0.35) as the solar-side counterpart; it would push the 30 min sun limit toward 50 min with no new organs.

### P-04 · Anaerobic extension math is off by ~5×
1.2 mol H⁺ ⇒ 0.6 mol glucose ⇒ ~37 kJ usable (2 ATP/glucose). At 120 W that is **5.1 min**, not 23. Sustaining 23 min at 120 W needs **5.4 mol H⁺** of buffer (~450 g bicarbonate — not a body).
**Recommend (both, together):**
- **Crawl-Home Mode.** After aerobic exhaustion, State A degrades to ≤25–30 W: rail locomotion + passive RADAR only, no tool work, no VHF. 37 kJ at 25 W = **24 min**. The 23-minute figure survives, and as a bonus 25 W < 71 W so the crawler is *cooling*, which erases the "13 min in sun" asterisk. Narratively strong: the last twenty minutes you can only crawl home.
- **Add an O₂ organ** to fix C-05 at the same time. Teleost swim bladders concentrate O₂ to hundreds of atm via a gas gland + rete mirabile — a real precedent, and DOC-01B already gives the species rete mirabile plumbing. A **vesica oxygenii** of ~1.5 L at 400 kPa pure O₂ holds ~6 L STP, which alone matches the current fictional lung figure and lets the lungs seal honestly on ordinary air (and at reduced pressure — see P-07). Aerobic window with lungs-at-21 % + Hb + Mb + bladder ≈ 9.3 L → **26 min** full activity, then 24 min crawl → ~50 min shadow.

### P-05 · RADAR "sub-millimetre" resolution is not available at X-band
1–5 ns pulses give 15–75 cm range resolution. Using the *entire* 1.5–10 GHz band as a chirp gives c/2B = **1.8 cm**. SAR improves cross-range, not range, and still cannot beat the wavelength scale (3 cm). "See internal structural flaws inside station walls" is fine; "sub-millimetre" is not.
**Recommend:** "~2 cm native (wideband chirp); ~1 cm cross-range with SAR head-sweep". The narrative capability is unchanged.

### P-06 · Blood at 210 g/L Hb
Hematocrit ~63 %; blood viscosity roughly 2× human. Compatible with a high-pressure primary heart and an auxiliary pump (both already in 01B), so it holds — but it is worth one sentence in 01B noting that the dual-pump layout *exists because of* the viscosity. Myoglobin at 45 g/kg is squarely in diving-mammal range (sperm whale ~50–70) — good, cite the precedent.

### P-07 · Lungs sealed at 101 kPa against vacuum
That is a full atmosphere across the chest wall: ~**20 kN** over a 0.2 m² thorax, held indefinitely. The "interlocking double rib cage" is asserted, but this is the load a 10 m dive imposes, inverted, for 40 minutes.
**Recommend:** an *exhale-and-seal* reflex to ~40 kPa (the same advice given to humans for decompression). Costs 60 % of lung-gas O₂ — which is fine once the O₂ bladder (P-04) carries the reserve, and it reinforces why the bladder exists.

### P-08 · Ear radiator in cabin — verified ✅
13 W radiative + ~21 W convective at 22 °C ≈ 34 W. DOC-01B's 35–40 W is right. Noted so you know it was checked.

### P-09 · λ/2 dipole pitch, thermal times, O₂ demand, Laplace tension — all verified ✅
1.5 cm at 10 GHz; 118.5 / 73.4 / 30.2 min; 0.358 L/min; 2,700 N/m. The arithmetic in 01E.1 is clean — the problems are in the *inputs* (P-02, P-03, P-04), not the sums.

---

## G — GAP REGISTER (what the design needs and doesn't have)

| ID | Gap | Why it matters | Blocks |
| :--- | :--- | :--- | :--- |
| **G-01** | Musculoskeletal system in microgravity | A non-senescent species living in 0-G forever will lose bone and muscle unless something prevents it. Also: gait in 1 G vs 0 G, grip forces, claw loads on carbon webbing, how a 50 kg taur sprints. DOC-01A slot is empty. | Habitat design, tactics, vignettes |
| **G-02** | Genomic Bio-Core mechanism | The single biggest handwave. Mesh, RADAR DSP, encryption, genome compilation, memory vaults, MACTAC, Deep-Mesh Virtualities *all* run on an organ with no described substrate. DOC-01C slot is empty. | Everything in DOC-02, 07, 08, 09 |
| **G-03** | Optical vision + Proximity Pit Node physics | They live in optical darkness — so how good are their eyes, and in what spectrum? Pit nodes must work in vacuum, so they are not acoustic; are they near-field RF? Capacitive? | Sensory vignettes, DOC-09 |
| **G-04** | Immune system / "infectious disease eliminated" | Mechanism unstated; and they share air with humans, who are not disease-free. Can they carry human pathogens? | Habitat protocols, medicine |
| **G-05** | Ancestral Mesh Vault substrate | Is a vault biological (a Bio-Core with no body?), digital, or hybrid? Who can read it? What is lost in "Defrag"? The Weavers faction is built on this. | DOC-08, memory/identity themes |
| **G-06** | Development & lifecycle | Newborn size, time to maturity, when the Bio-Core "boots", education over mesh, adolescence, the First Ping in detail. | Character writing, population |
| **G-07** | Timeline & history | No dates, no creation event, no creator institution, no population figure, no "now". DOC-05's stations exist in a temporal void. | Every narrative decision |
| **G-08** | Language & protocol stack | The RF mesh needs at least a sketched layer model (what a "data burst" *is*); vocal language; the "human trade-pidgin" of Scene 01. | Vignettes, DOC-02 |
| **G-09** | Death, injury, medicine | Non-senescent but killable by trauma. Regeneration? Prosthetics? What does a Cluster do when a node dies mid-loop? | DOC-08, 09, vignettes |
| **G-10** | Vault structure | `data storage spec.md` in the parent folder defines an Obsidian/YAML/Python schema (for a different world, Tharn). Decide whether Elysian adopts it — if yes, every DOC needs frontmatter and an `id`. | Tooling |

---

## E — EDITORIAL

- **E-01** DOC-05 Scene 02: "Sylvan curled her tail tightly around Sylvan's paw" — should be Lyric's or Sol's.
- **E-02** DOC-05 Scene 04 mixes *she* and *hir* for Lyra-4; DOC-02 fixes *hir* as canon.
- **E-03** DOC-06 §4 "Open Conceptual Anchors" (transit cultures, vaults, symbiosis units) overlaps DOC-07 §2 and G-05; merge into ROADMAP.
- **E-04** Document IDs skip 01A and 01C. Either they were never written or were lost; the gaps G-01 and G-02 map naturally onto them.
- **E-05** DOC-01E §4 matrix "Terrestrial Baseline · 87–116 W (2,200 kcal/day)" — 2,200 kcal/day is 107 W; harmless but tidy it.

---

## Addendum — 2026-09-20 (D-68 scale pass)

| Item | Status |
| :--- | :--- |
| **C-09** body length vs. mass | **Closed** — trunk 1.00–1.15 m, mass 50–70 kg (ref. 60 kg). |
| **C-11** tail mass | **Closed** — was implicitly cat-like (2–3 %); three independent requirements (60/40 load split, half-second vector-flip, 450 N anchor) converge on **12 % of body mass**. DOC-01A §3A. |
| **P-03** ear throttle / whole-pelt radiation unmodelled | **Closed** — both modelled in DOC-01E.2 §3 and now mass-parametrised in `models/vacuum_budget.awk`. |
| **P-10** (new) thoracic vault volume floor | **Closed on discovery** — the vault's contents are individually specified and none scale down: 12.1 L irreducible, setting a **species mass floor at ~42 kg**. This is what makes the 50 kg guess defensible in the first place. |
| **P-11** (new) grip-to-weight and thermal ceilings | **Closed** — anchor ratings decay as M^−⅓; State-A thermal margin (production ∝ M vs. surface ∝ M^⅔) reaches zero near 80 kg. Band 42–80 kg. |
| **E-05** 2,200 kcal/day quoted as 87–116 W | **Closed** — DOC-01E §4 now reads 99–133 W (~2,500 kcal/day), consistent with DOC-01B §7. |

**Verification:** `awk -v SCEN=shadow_eva -f models/vacuum_budget.awk` reproduces 17.0 min State A, 41.7 min conscious, 12.8 h shadow torpor at the new 60 kg reference, and `-v M=50` still reproduces the original 50 kg run. The envelope is mass-invariant by construction (State-A pool and State-A draw share the M¹·⁰ exponent).

---

## Addendum — 2026-09-20 (D-69 hand-paw)

| Item | Status |
| :--- | :--- |
| **G-11** (new) paw architecture undefined | **Closed on discovery.** Canon specified "opposable digits, tactile pads, semi-retractable claws" and nothing else — no digit count, no thumb, no pad layout, no hand/paw contrast. Surfaced by a failed image generation: every rendering defaulted to a carnivoran foot, because nothing in the archive said otherwise. Resolved by D-69: five digits, D1 fully opposable with a flat nail, D5 semi-divergent, three-jaw-chuck close. Derivation in `DOC-01A` §3B. |

**Method note.** Both D-68 and D-69 were found the same way — by trying to *draw* the species rather than describe it. Rendering is a good auditor: it forces every unstated parameter into the open at once. `DOC-00C` §15 now carries the failure log.

---

## Addendum — 2026-09-21 (D-74, D-75 — the six limbs as dual-role organs; the burn)

| Item | Status |
| :--- | :--- |
| **G-22** (new) the arms had no length, range, or carriage | **Closed.** ~0.50 m (reach parity with the forepaws); primate-grade shoulder, elbows aft; loose at the walk, folded to the sternum at speed. Surfaced by briefing an artist — every limb question is a what-does-it-do question, and the archive had described the limbs for 1 G only. |
| **G-23** (new) no mechanism for hours-long anchoring | **Closed.** Passive tendon lock in all four paws and the tail (perching-bird mechanism); the anchor ratings are the lock's. Canon had "slow-oxidative fibres for hours of gripping" doing a job a lock does for free. |
| **P-13** (new) acceleration tolerance asserted, never computed | **Closed on discovery.** DOC-01B §1 has said since v1 that the vaults exist "to protect critical organs during high-g maneuvers"; nobody ran it. Heart-to-brain column ~0.08–0.12 m vs a human's 0.30 m: brain-limited tolerance is never the limit in any orientation. Envelope ~15–20 g for seconds, ~8–10 g for minutes, head tucked, breathing from the bladder — **estimates**; the fascia and the *vesica* each set a time, and want a coupled model like `vacuum_budget.awk` (→ ROADMAP). |
| **C-13** (new) fascia coverage vs the tail | **Closed.** DOC-01E/01E.1 had the fascia across "limbs and abdomen"; the 0.88 m tail was neither sealed in vacuum nor protected from pooling under burn. Extended to the tail. |

---

## Addendum — 2026-09-21 (D-73, silhouette-first packaging)

| Item | Status |
| :--- | :--- |
| **P-12** (new) thorax orientation was a packaging choice presented as physics | **Closed on discovery.** D-68 derived a 12.1 L vault *floor* and then stood the thorax up as a 0.42 m vertical column "necking sharply" into a 14 cm waist. Renderings built to that geometry came out as a barrel-chested animal reared on a meerkat's torso — correctly. The floor constrains volume, not shape: the same 17.4 L laid lengthwise is 0.45 m of a 0.21 × 0.23 m tube, chest-to-loin girth 1.4 (a red fox). Mass floor, ceiling, anchor budget and vacuum envelope untouched. |
| **G-20** (new) the "upright humanoid torso" had no anatomy | **Closed.** It was two things: a *yoke* (the anterior ~0.18 m of the thorax carrying a floating pectoral girdle; arms ~10 cm ahead of and ~15 cm above the fore-pelvic joints) and a *posture* (sit-tall = the whole thorax pitched vertical by lumbar flexion). All 0.80 m / 1.15 m / 1.28 m heights are now labelled as reared figures; on all six the head is at ~0.70 m. |
| **G-21** (new) why the vault is "the best-protected volume in the body" was asserted, not shown | **Closed.** Two girdles at one station make a bone box — scapulae lid, fore-pelvis floor, double rib cage walls, four limbs' root muscle over — and the rule it implements is stated: the only two non-regenerating structures sit inside the deepest stack of regenerating ones. |
| **C-12** (new) standing load split | **Re-estimated** for the flat thorax: 67/33 → 56/44 with the 12 % tail (was 73/27 → 60/40). The tail's three derivations stand. DOC-01A §3A. |
| Fascia radius (DOC-01E.1 §4) | 0.07 → **0.08 m** (loin); T = 1,200 N/m; non-limiting. |

**Method note.** Third ruling in a row surfaced by rendering — but this one was the reverse of D-68/D-69: the archive was *over*-specified in the wrong direction, and a faithful image of the spec was the evidence against it. `DOC-00C` §15 item 0 records it; §14 keeps the nouns of the sheet that got the look right.

---

## Addendum — 2026-09-20 (D-70…D-72, the Sealing re-based)

**Origin.** Seven outside-context wargames (MLP:FiM, Vorkosigan, Freefall, Star Trek, Three-Body, 40k, The Expanse, Avatar) followed by an internal one. Two mechanisms were "load-bearing nowhere": the Sealing and the keyring. On reread, neither had failed — each was *described* in one word (*read*, *firewall*) as doing a job it never did. The Sealing was re-based (D-70…D-72); the keyring items are logged below and await ruling.

| Item | Status |
| :--- | :--- |
| **G-12** (new) Moratorium enforcement clause described a dead generation | **Closed — D-72.** Enforced by inability: the science died with the tutors; the only route back (re-derivation from living Kin) is what the law forbids. The hole is named in DOC-10 §3 and DOC-12 §4. |
| **G-13** (new) Reference annotation carried as a single point of failure | **Closed — D-70.** Every Weaver carries the annotation in full; the Weave checks it body against body — the rule the Warm Loss made. DOC-08 §3, DOC-01C §5. |
| **G-14** (new) The Unbound's 190 years since AF 362 unaccounted for | **Closed — D-70.** Their act was an attempt to rebuild the science; they hold a partial written reconstruction; extent unknown outside the workshop. DOC-08 §4. |
| **G-15** (new) "Identity has a changelog" with nothing that changes; the species cannot adapt at all | **Closed — D-71.** Compiles tune within maker-set ranges; the log has entries; evolution by decision; the divergence clock (~2 c detectable, ~4 c cross-lineage failure). DOC-01C §5. |
| **E-06** (new) DOC-10 §7 "a genome no one can edit or read" | **Closed.** → "anyone can read and no one can extend." The sequence was always recoverable from a Genesis Module; the design never depended on secrecy of the sequence. |
| **Scenes** | S007 stays consistent ("took the book and burned it" — now literally the tutors). S013 drafts (both versions) predate D-70 and have Constance mourning the tutors as the makers' loss; drift noted in each. |

### Open — keyring findings, awaiting ruling

| ID | Gap | Recommendation |
| :--- | :--- | :--- |
| **G-16** | **Can humans receive the Hum?** DOC-03 §1 has human-built beacons speaking L1/L2 to a Kin; DOC-10 §7 has Kin-code's base layer from the tutors; PUBLIC tier uses a species-wide hop table with no key. Nothing contradicts operators reading every Kin's identity, vitals, position and coarse mood in real time; nothing states it. | **Yes.** Operators can and do; the Kin know; it is one more line in the Field's inquiry that changed little. → DOC-12 §4, DOC-01C §4. |
| **G-17** | **Body disposition after a Reading.** CLUSTER/DEEP keys are Core chromatin; DOC-01C §10 names tissue theft as the compromise route; denial doctrine burns only the bodies the Kin *cannot* recover. A Read body handed to a human recycler gives an operator Core tissue at every death. | **Burned after the Reading, by the Cluster, as the rite's last act.** → DOC-11 §5, DOC-09 §4. |
| **G-18** | **Interrogation is not a named failure mode.** The Silence disables in 30 min (DOC-09 §3 says humans have used it); the whitelist clears cells, not molecules, so a truth drug works on the Cortical brain; verbatim recall + drug = a perfect deposition. | Add *Interrogation* (Silence + drug) to DOC-01C §10; the Compact court may not use either; withholding a beacon in an EM-opaque room is a Compact offence under the post-Storm standard, prosecuted once. → DOC-12 §4. |
| **G-19** | **DOC-02 §2 calls the tiers "privacy firewalls."** The keyring is a *consent* architecture (no Link, Reading or compile without both wills; the Cortical brain off-network) — the reason a Cluster is not a hive. It was never security against humans; against humans a Kin's privacy is legal and social. The word invites the misreading the wargames made. | "privacy firewalls" → "consent tiers"; add one sentence: *against humans, a Kin's privacy is legal, not cryptographic.* → DOC-02 §2, CANON §9 Cluster row. |

---

## Addendum — 2026-09-22 (D-76…D-78, internal wargame round 2)

| Item | Status |
| :--- | :--- |
| **G-24** (new) D-71 gave compiles ranges without saying which modules have them | **Closed — D-76.** Fixed points (no range) = the makers' product decisions: non-aggression, protectiveness, nurturing, the quirk, non-senescence/whitelist/Core, the radio spec, the body plan. Ranged = physiology, and temperament inside the fixed band. DOC-01C §5. |
| **G-25** (new) gestation vs the whitelist | **Closed on discovery — D-77.** DOC-01C §9 (every cell hashes its Keyring Locus; the Sentinel clears non-self) read against §4 (the seed's key is written at compile) means the gestating parent's immune system kills the child. Fixed with the mechanism the docs already had for the gut: a licence. Only a compile parent holds the hash, so only a parent gestates. DOC-01C §9, DOC-02B §2. |
| **G-26** (new) the age structure of the living population had never been run | **Closed — D-78.** `models/age_structure.awk`: median ~106, mean ~139, 38 % ≥150, 20 % ≥250, ~5,800 Spread-born. The Written's early hazard must end ~AF 100 to leave forty (run for life it leaves one) — pins D-39. DOC-10 §6, DOC-02B §8. |
| **C-14** (new) compile rate — "one per Cluster per decade" (DOC-10 §4, §6; DOC-02 §1) vs D-53's +0.4 %/yr | **Closed — D-78.** Per decade is 1.25 %/yr births and ~300,000 Kin in Sol by now. D-53 implies ~320 births/yr: one per Cluster every ~20 years now, every ~6 during the Spread. Three lines corrected. |
| **D-75 (the burn) — verification requested** | **Checks.** ρgh for 0.30 m of blood = 3.1 kPa = 23 mmHg per g ✅; G-LOC ~5 g relaxed sitting ✅; 1/column scaling from 0.30 m to 0.12 m along the body → ~12 g brain-limited ✅; +25 % for a 15 kPa (112 mmHg) fascia is in line with a G-suit's ~+1–1.5 g ✅; across the body (0.08 m) brain-limited ~19 g, above structural ✅; tail-forward over-pressure ~9 mmHg/g contained by a rigid CSF box on the Monro–Kellie argument ✅; sealed lungs + *vesica* remove the +Gx ventilation limit ✅. The whole-animal envelope (15–20 g for tens of seconds, 8–10 g for minutes) is human +Gx territory made orientation-independent — conservative, defensible, and correctly flagged "pending a model." Two nits: (1) the human reference "6–9 g in a couch, briefly" understates the human record (Apollo aborts ~12 g reclined; Stapp 46 g peak) — the Kin's edge over humans is *orientation and duration*, not peak, and the line should say so; (2) "aft-facing web panels" is ambiguous — under thrust you lie on the panel *aft of you*, whose surface faces forward; suggest "aft web panels." |

### Still open — awaiting ruling
- **G-16…G-19** (keyring: Hum audibility, body after Reading, interrogation, "privacy firewalls"). Recommendations above.
- **Coercive power** — whether a species designed to love humans can fight one. Under discussion; see CANON §25 note.

---

## Addendum — 2026-09-22 (D-79 — the love, and what it does with violence)

| Item | Status |
| :--- | :--- |
| **G-27** (new) "inherently non-aggressive" and an all-non-lethal ordnance list implied a species that cannot defend itself against a human — a design flaw if read as prohibition | **Closed — D-79.** There is no non-aggression module; D-76's fixed point is amended to *humans inside the circle of mine*. What looks like pacifism is what a designed love does when the attacker is also inside the circle. A violent human reads chemically as a frightened one; containment is capability (the body is the lethal weapon), not policy; self-defence is a Cluster function. DOC-09 §1, §3 rewritten; the ordnance list stays as preference plus hull integrity. |
| **G-28** (new) the depth of the love for humans vs the Cluster was unspecified | **Closed — D-79.** The makers aimed for Cluster-depth and the mesh made it a ranking (humans can never be in the frame): Cluster, then humans, then self, by wiring depth. The tutors spoke Hum, so the full intent was reached once, through a machine the Written deleted. DOC-02 §3, DOC-10 §3. |
| **G-29** (new) no record of Kin-on-human or Kin-on-Kin violence in 550 years | **Closed — D-79.** Fewer than ten Kin have killed a human, all for others, all tried, all named; the Compact cannot receive the Reading they offer (DOC-12 §4). No Kin has killed a Kin except at request (D-66). The one Kin war, AF ~188 at *Dioscuri Yard*: two Clusters refused both sides; one side Silenced the other's Cluster; one dead; no blow. DOC-10 §4. |
| **G-30** (new) the Star-Bound's motive was one-sided | **Closed — D-79.** Two truths, both said aboard: *this is what we were made for* and *the only place a species that loves like this can be its own people is light-years from the ones it loves*. Recruited from the far postings; the love follows them. DOC-08 §2, DOC-10 §5–6. |
| Placeholders | *Dioscuri Yard* (Castor / Pollux) named 2026-09-22; the dead Kin is **Rill-3**, named by S016 (accepted 2026-09-22), which also set the death mechanism — the homing watchdog, the outer lock, eleven metres, eleven hours, Read by both Clusters. |

---

## Addendum — 2026-09-22 (DOC-13 drafted)

| Item | Status |
| :--- | :--- |
| **G-31** (new) the Kin had rites, factions and a history and no interior — every recorded act a response to a breach, a death, a human or a maker | **Closed — DOC-13 v1.0, D-80…D-84 (accepted 2026-09-22).** Culture derived from locked mechanisms: the dreaming (theta lock = weather not content; Defrag weighted by the Cluster's affect — the mechanism of DOC-11 §8's gaps; dreams unwritten; held dreams at DEEP; virtualities as held dreams), memory as currency and the grant-web, the Plain School, athletics as Core-training, the literate nose, tail-weaving, three languages. Proposes D-80…D-84. |
| **C-15** (new) DOC-07 §2 "Bio-Core awake … composing, retelling, solving" vs D-13 "the Core never initiates" | **Closed — D-81.** The cortices compose at dream-level in a Core-hosted, consented held dream; DOC-07 §2 folded. |
| **E-07** (new) DOC-03 §1 "scent-clean" read as aversion; DOC-13 §4 makes it a canvas | **Closed — D-84.** DOC-03 §1, DOC-00B §4, §11 folded. |

---

## Addendum — 2026-09-22 (D-85…D-88, the keyring against humans, the body, DOC-13's open items)

| Item | Status |
| :--- | :--- |
| **G-16** humans and the Hum | **Closed — D-85.** Yes; always; the Field's inquiry had the vitals. DOC-01C §4, DOC-12 §4, DOC-10 §4. |
| **G-17** body after a Reading | **Closed — D-86.** Burned by the Cluster; denial is the same act early. DOC-11 §5, DOC-09 §4, DOC-02B §8. |
| **G-18** interrogation unnamed | **Closed — D-87.** DOC-01C §10 row; withholding a beacon a Compact offence, prosecuted once (*Dioscuri*). DOC-12 §4. |
| **G-19** "privacy firewalls" | **Open — under discussion** (the tiers as distances). |
| Placeholder | *Dioscuri Yard* (Castor / Pollux) replaces [the Twin Docks] everywhere. |
| DOC-13 §14 open items | **Closed — D-88** (held dreams not Read; whistle never written; Sedge-2; the Alder piece). |
| **G-32** (new) how a name passes — D-54 says *taken at the first Telling* and *names come free at death* but not whether a living Kin may set a name down, whether one living holder per name, or how the pool is large enough | **Open — under discussion.** |

| **G-19** "privacy firewalls" | **Closed — D-89.** The tiers are three distances (800 km / 12 km / 2 m; cortex at zero); intimacy is proximity. DOC-02 §2, DOC-01C §4, CANON §9. |
| **G-32** how a name passes | **Closed — D-90.** One living holder per name; taken from the dead at a Telling or Reading; set down only for the dead; count never resets; pool = every human language's soft words. DOC-00 §3, DOC-11 §3, §5, DOC-13 §2. |

---

## Addendum — 2026-09-22 (W03: the species as a story engine — D-91…D-96, and two new registers)

**Origin.** `wargames/W03_the_kin_as_a_story_engine.md` — the first wargame to test the Kin against their *job* (be a source of stories, plausible biologically, sound logically, consistent lore-wise) rather than against their own mechanisms. Method: inventory the engines, sort the foreclosures into costs-paid and leaks, run fourteen ordinary story premises against canon, re-run the Mary-Sue guard as a ledger of *superiority vs. cost that reaches the page*, and map the lines a scene will want to cross. Result: fourteen engines needing no cheat, twelve of fourteen premises surviving, nine of eleven genre closures paid for, one unpaid line in the ledger, and **three silences plus one habit** as the real weaknesses.

Findings are numbered **N** (narrative) and join C/P/G/E. Holes that must *stay* open are numbered **H** and are a new kind: an H-item is closed by a scene or not at all.

| Item | Status |
| :--- | :--- |
| **N-01** the transparency stack — PUBLIC affect to 800 km including humans, continuous CLUSTER affect, the Kin reading human sweat, verbatim recall, no anonymity — leaves almost no asymmetric information, and the whole load rests on one unpinned word, *coarse* | **Closed — D-92.** Valence and arousal, ~minute resolution, no object. *Everyone inside 800 km knows the weather; nobody knows the news.* DOC-01C §4, DOC-00B §4, DOC-12 §4. |
| **N-02** D-79's ranking reads as determinism and pre-decides the crux scene of the species | **Closed — D-91.** The ranking is the first frame; the cortex overrides in the pause (DOC-00B §2) and pays — visible as weather, heavily weighted by the Defrag, carried into the Reading. The Storm was *with* the wiring. Whether it has ever happened against a Cluster-mate → **H-01**. DOC-02 §3. |
| **N-03** the species has a hell (*lost*) and no ruling on whether it is ever imposed; the Weave's sanctions are unstated | **Floor ruled in D-91's spirit, ceiling held open → H-02.** A Cluster never refuses its own and the pre-granted key is a will (D-16). Whether a *Weave* has declined to carry — whether the fewer-than-ten were carried — stays a rumour. |
| **N-04** no floor, ladder or mechanism for the Kin alone | **Closed — D-93.** Three degrees on the three distances; the guard slot (already in DOC-01C §4's L2) is the answer and retro-explains DOC-08 §3; the injury is **erasure, not decline**; operators cause it and the Compact has no rule; Weavers travel in pairs. DOC-01A §4, DOC-01C §4, §6, DOC-02 §2, DOC-08 §3, DOC-11 §9, DOC-12 §7, DOC-13 §1I. |
| **N-05** the perfect witness has no stated blind spot — L2 of the load test dies unless D-80's thin day is restated as a rule about *evidence* | **Open.** Recommendation: a Kin remembers verbatim what the frame cared about; a day the frame found boring is stubs within the week. With the veto (*a secret can die with her*) that is the whole of Kin crime fiction. → DOC-01C §6, DOC-00B §7. No new mechanism; a restatement. |
| **N-06** one living holder per name (D-90) is unenforceable across light-years (D-52 — 4.4 ly to *Second Light*, nine years round trip) | **Open.** Recommendation: the name-pool forks at an ark's departure and each lineage keeps its own count; two Lyra-5s can both be right, and the day two lineages meet and find it out is the divergence clock (D-71) showing up in the only currency the species has. The Written stay unique across all lineages forever. |
| **N-07** a child's vacuum envelope has no number; D-68(g)'s mass-invariance formally gives a six-year-old seventeen minutes and canon never said so | **Closed — D-94.** Voiding organs on the body clock: full envelope at ~6, minutes below it, seconds for a newborn. The prohibition is dread, not physics, and the fourteen-year-old becomes exact. DOC-02B §5, DOC-09 §2, DOC-13 §10. |
| **N-08** the burn is the only superiority in the archive with no cost that reaches the page | **Closed — D-95.** The eyes are the last thing back: hours of grey, acuity, then colour; RADAR and near-field untouched. The first hour after a hard burn is worked in the dark. DOC-01A §6, DOC-09 §2. |
| **N-09** AF 550 has no live fuse — every dated event is history | **Open by choice → H-10.** Candidates already in canon: the first posting-bonus tuning case (D-76 says *the first case is a scene*); a Kin over a human crew; the extent of the Unbound's reconstruction; *Last Light* at Barnard's in 619; the next Written's Reading; the lab the Kin are watching. Pick two or three and resolve them only in scenes. |
| **N-10** the audit loop eats hooks — ninety rulings against sixteen scenes in an archive whose purpose is stories | **Closed — D-96.** The order of work inverts: a ruling is drafted only when a scene has demanded it, and is discharged by a scene before the next is made. The **H-register** (below) protects the load-bearing silences. The **dramatisation test** (infrastructure / discharged / undramatised) triages the existing log; the undramatised list is the writing queue. ROADMAP Step 12. |
| **N-11** intra-Kin antagonism is under-stocked, not under-built | **Closed as guidance.** The Kin antagonist is a *curator*: the Weaver who chose wrong at a Defrag; the re-feeler who gave a feeling back wrong; the parent who tuned toward a posting; the claimant who took the name and had taken less; the Cluster that removed a grant; the Written who deleted a childhood. All exist in canon, none is named. → DOC-00B §9. |
| **N-12** human antagonists are monotone — every one is a bean-counter | **Closed as guidance.** Write one human who is *right* against the Kin: the reviewer who won't cut the margin; the Compact judge who cannot receive a Reading and rules correctly anyway; the operator who won't post a Kin alone and is called a speciesist for it. → DOC-00B §10. |

### The H-register — holes kept on purpose (opened by D-96)

**Rule: an H-item is closed by a scene or not at all. A ruling that closes one is a bug.** These are not gaps; they are the load-bearing silences, and the audit loop's instinct to number every silence is what they exist to survive.

| ID | The hole | Why it must stay open | Lives in |
| :--- | :--- | :--- | :--- |
| **H-01** | Whether a Kin has ever chosen a human over a Cluster-mate, against the ranking (D-91) | The crux scene of the species. A ruling either way ends it. | DOC-02 §3 |
| **H-02** | Whether a Weave has ever refused to carry (N-03) | The only thing a Kin can be threatened with; a rumour is stronger than a precedent | DOC-11 §9 |
| **H-03** | The extent of the Unbound's written reconstruction (D-70) | The setting's one sealed box | DOC-08 §4 |
| **H-04** | The re-derivation hole (D-72) — whether any operator has begun | The thriller the setting is waiting for | DOC-12 §4 |
| **H-05** | The Plain School's verdict (D-84) | "Unresolved after five centuries on purpose" | DOC-13 §3 |
| **H-06** | The ambivalence — *yes, and I like you; both are true* | The species' tone; DOC-00B §11 already forbids resolving it | DOC-00B §11 |
| **H-07** | The Written who deleted the tutors, asked why at a Weave | Promised as a scene (DOC-10 §9); must never become a paragraph | DOC-10 §9 |
| **H-08** | Why *Long Reach* died (D-52, "cause never learned") | The one thing in the species' history the species cannot carry | DOC-10 §5 |
| **H-09** | Whether *Second Light*'s children are the same species in the sense that matters | D-71 gave it a clock; the answer belongs to AF 736, not to a doc | DOC-08 §2 |
| **H-10** | Which two or three fuses are lit at AF 550 (N-09) | Chosen once, written only as scenes | ROADMAP Step 12 |
| **H-11** | The Warm Loss's date and Cluster | *The Kin remember it without a date; the human record has one* — the gap is the point | DOC-10 §5 |
| **H-12** | What triggers the chosen ending, now that Data Rot is a steady state (D-104, D-107) | The flat dreams are the *sign* and no longer the *reason*; *why this one, why now* belongs to a scene | DOC-01C §6C, DOC-02B §8 |
| **H-13** | Whether any operator ever moved to stop an ark yard — physically, by pulling a crew, or by refusing a berth — and what happened | The setting's only untold action, and the one place D-109's fait accompli could have been tested and was not | DOC-07 §2A |

### Scene debt from this pass (D-96's rule of order, applied retroactively to D-91…D-95)

D-91…D-95 are the last rulings drafted the old way and each carries a debt. Listed in ROADMAP Step 12, not written here.

---

## Addendum — 2026-09-22 (memory re-derived from the makers' brief — D-97…D-101)

**Origin.** A review of the nightly Defrag, requested because it did not parse on reading. It turned out never to have been derived: **G-05 shows *Defrag* was inherited vocabulary** from the source vault docs — the audit item literally asks *"What is lost in 'Defrag'?"* — and the mechanism was reverse-engineered from the name. D-15 then bundled nightly and centennial in one clause with no separate derivation, and D-80 later hung the load-bearing idea (*the weights are the Cluster's*) on it, which made it look derived. Asked what the nightly pass was *for*, the doc gave two answers that contradicted each other. Rebuilt from the brief the makers were working to.

**The contradiction that started it.** DOC-01C §6 said both *"the Lattice **selects** the day's traces; writers transcribe them"* (selection gates writing) and, via D-20, *"the Core writes **verbatim**"* (nothing is left out) — next to *"capacity is never the limit"* (~2×10¹⁷ B) and *"a Kin who sleeps apart writes a **thinner day**."* If capacity is infinite, nothing should ever be omitted. The rest of the system votes decisively: **the night never decided what was written. It decided what could be found and felt.**

| Item | Status |
| :--- | :--- |
| **M-01** (new) the nightly Defrag was never derived; the name preceded the mechanism | **Closed — D-97…D-100.** Rebuilt from the operators' complaint (trained judgment dies with the crew) and the foundation's (humanity forgets). Target: *nothing is lost, and knowledge is inherited rather than recorded.* |
| **M-02** (new) *"selects the day's traces"* vs *"writes verbatim"* vs *"capacity is never the limit"* — a three-way contradiction at the centre of the memory system | **Closed — D-97, D-100.** The commit is continuous and complete; the night appraises. **The book is infinite and the index is an organ.** Index derived at ~5×10⁴ stubs ≈ 100 MB addressing a petabyte. |
| **M-03** (new) the synaptic trace "fades to a stub" left a Kin of forty with six weeks of real memory and a filing cabinet — *worse* than a human, in a species specified to surpass them | **Closed — D-97.** Struck. **The cortex is human, unmodified, lifelong, and deliberately so:** cognition runs on forgetting, so perfect recall inside the cognitive loop is poison, and the only architecture that meets the brief is to leave the thinking organ alone and bolt on a record that does not think. Same discipline as D-27's eyes. The superiority is **query, check, accumulation** — not recall. |
| **M-04** (new) Data Rot had no mechanism; "facts kept, feeling lost" sat oddly against D-82 (the old dream feeling back from stubs) and D-83 (re-feelers warm flat memories) — if the affect had decayed, neither has anything to work with | **Closed — D-98.** Data Rot is decay of the **cueing layer**. The record never degrades and retrieval stays exact; what is lost is the spontaneous arising of the question. **The old are not forgetful, they are unprompted** — which makes other Kin the cueing layer, mechanises the re-feelers, and sharpens D-82's sign of the chosen ending (*a perfect library with no visitors*). |
| **M-05** (new) the Telling's "a year in a week" had never been checked against the archive rate | **Closed — D-99, and it checks to 1 %.** Mesh 100 Mbps = 12.5 MB/s; playback ~12 MB/s; export ~20 GB/day. A day = 27.8 min (DOC-01C's "half an hour" ✅); a year = 7.04 days (*a year in a week* ✅). Speech is 40 bit/s and telemetry is nothing: **the only thing needing 100 Mbps is raw archive at replay speed — the makers sized the radio to the archive.** Three figures from three separate rulings agree; none was set with the others in view. |
| **M-06** (new) whether raw memory can be shared — the "private codec" read as encryption, which invites breaking | **Closed — D-99.** Split by content, not by key. **Hard** (numbers, readings, exact speech, sensor takes) transfers perfectly and constantly — the superiority the operators bought. **Soft** (salience, association, the feel) is *indexical*: addresses into one cortex. Not a lock — *the bits transfer fine; the bits were never the memory.* Consequences: the Telling is a **transfer** at the hard tier; the Reading's 15–27 MB is a **corpse's** limit, not the format's; soft content resolves with shared history, so **a Reading cannot be outsourced** and the Field took less than it looked; and the real limit everywhere is **index cost, not bandwidth** — which mechanises the Weaver's sacrifice. |
| **M-07** (new) the external-store impossibility rested on "no one has managed it" | **Closed — D-99, deliberately left ajar.** A machine *can* capture the bitstream; what it holds is 20 GB of Lattice-format data and **the decoder is a grown organ**. DOC-08 §4's "fabricated replacements for the grown Lattice" was always the Unbound's real project. Blocked by a plateaued technology (D-43) and a science that died at the Sealing (D-70) — not by physics. The Weavers' *a memory no one carries is not a memory* becomes a position, argued against, not a law. → **H-04 sharpened**: an operator's lab with a captured archive and a two-decade reader programme. |
| **M-08** (new) D-19 read as though the makers designed a species that would not write | **Closed — D-101.** They *valued* writing; the foundation's complaint was that humanity forgets *despite* it. **For a human writing is a gain; for a Kin it is a loss** — same act, opposite sign. So the flaw is **cultural, not genetic**: it could have gone otherwise, which is why it is argued about. And the irony is exact — *they solved individual permanence completely and made civilisational memory worse; they traded a library for a priesthood, and the priesthood is the Weavers.* |
| **N-05** the perfect witness's blind spot | **Closed — D-98, inverted and improved.** The content is always there; what is missing is the *handle*. So: **a Kin has the answer and does not know she has it.** Nobody thought to ask about that Tuesday, and she cannot volunteer what nothing cues. The detective's job is knowing which day to name; the veto was named here as the hard limit — **and D-105 has since struck it entirely** (§32). It is not needed: D-98's missing handle, D-102's untransferable testimony, D-103's 27.8-minutes-a-day and D-104's unreachable cueing layer are four separate opacities, and the veto was a fifth that did nothing the others did not do better. |
| **M-09** (new) could a Kin forward archive without reading it? Nothing said so, and somata → Lattice → antenna has no cortex in the path. If she could, **D-87's interrogation cap collapses** (a drugged Kin could be made to *dump*, not read) and invoking the record becomes cheap. Surfaced by interrogating a coined idiom, *"don't make me read it"*, which did not survive its first test. | **Closed — D-102, and the answer was already in three numbers.** D-87's *half an hour per day*, D-15/D-99's 20 GB ÷ 12 MB/s = **27.8 min**, and D-17's *a year in a week* = 365 × ½ h = **7.6 days** — the same figure, set in three separate rulings, none with the others in view. **The archive is a store; the cortex is the reader.** One playback path, ~12 MB/s, through the cortex: recall, Burst and Telling are one act, and **a Kin cannot forward what she has not re-lived.** Consequences: D-87's cap is derived rather than asserted (she cannot be emptied, and she can be made to live a day again in front of the one doing it); a Telling is the teller living the year again, which is why it takes a week and thins her; **D-99's corpse limit is explained** — 12 MB/s is a *cortical* rate and ≤10 kbps is what dying readers manage without one, which is the whole gap between the two rites; and the idiom now means *do not make me live that day again*, with the force in the price, paid publicly. **The line the whole memory system was reaching for: Data Rot and death are the same event at different speeds — the loss of the reader, never of the book.** |
| Consequence taken | **The transcription lag means the moment of death is never on file** (D-100). A Reading carries the whole life and not the end of it — so **the operators know how every Kin died, to the second, off the Hum (D-85), and her own Cluster can never know from the inside.** Re-explains the Field as a recovery of bodies rather than of deaths. Does not disturb S016. |
| Scenes | S009's *"told, not lived, with the feel intact"* is now the mechanism, not a flourish — promote from drift note to citation. S012's Data Rot passage stands and gains a mechanism. No scene contradicts the rebuild. |

| **M-10** (new) D-102 priced every use of the archive at one rate, and put its own §6B (*seamless, exact, no sense of machinery*) against its own §6I (*half an hour of stillness*) one paragraph apart. **Its arithmetic also disagreed with its prose:** 20 GB ÷ 12 MB/s = 27.8 min against a day of 86,400 s is **≈52× real time** — not living a day again, and §6I already said it arrives *as content and not as feeling*. And D-98's hard handle makes the archive **seekable**, so the everyday case the idiom was coined for (settling a fact) costs about a second. | **Closed — D-103.** One read head, **two rates.** **Cold** (default, ≈52×, seekable, affect off) is what §6I describes and costs nothing worth naming; **lived** (1× only, affect engaged) is the sole source of soft content, and therefore the only thing that can be given away. **The cost moves from knowing to giving.** D-87's cap survives on arithmetic instead of suffering (a year = 7.05 days of cold reading; a Written's life ≈ 10.6 years — a life does not fit through the head), the Telling keeps its week and gains the reason it thins the teller (she drops to 1× for the hours worth handing over, and chooses which), the Reading becomes **cold by definition** (*the dead can give you what happened; only the living can give you what it was like*), and the centennial Defrag gets its real cruelty: a pruned century is **readable cold forever and unfeelable for good**. The idiom narrows from *do not make me look it up* to **do not make me feel it again**, and stops being refutable. **Evidence trimmed:** D-102 counted three agreeing figures; there are two — D-87's half-hour is downstream of D-15's arithmetic, not a witness to it. |

**Addendum note (D-102).** M-09 was found by testing a phrase rather than a mechanism — the idiom was coined in conversation, folded into three documents, and then did not survive being asked whether it made sense. Worth recording as method: **a coined idiom is a claim about mechanism in disguise, and should be audited like one.**

| **M-11** (new) three lines in DOC-01C §6 could not all be true: §6B *hard handles never fail*, §6C *an elder can still have anything she asks for*, and §6I *the records remain… **unreachable** — only stumbled on*. D-103 (g) had built on the third. Surfaced by a **scene** — a Written asked about the night of the Sealing, the hardest handle in the species, written as unreachable. | **Closed — D-104, and the wording was the smaller half.** §6 had located the failure in the **Lattice** (an index that fills, a budget spent, a rite for discarding) when D-97's own founding decision was to leave the **cortex** alone because cognition runs on forgetting. A cortex left alone rebuilds its associative web onto live material, forever. **So Data Rot is the human cortex working exactly as specified, over a span no human lives to see** — the consequence of the one thing the makers got right, not a component failing. Ruled: associations are **overwritten, not lost**; hard handles never fail at any age; the old affect is **gone, not faint**, though the lived read still runs and returns **today's** feeling about old content; nothing outside the window ever arrives unbidden; **a Kin is made of her last ~175 years**; and it is a **steady state, not a decline** — four hundred and nine hundred are the same condition. The index is demoted to a **cycling** fixed-width table and **the arithmetic survives intact**: 5×10⁴ ÷ 365 = 137 years at one stub a day, widening to 150–250 because thin days never earn a full stub. The centennial Defrag is recast from *choose what to drop* to *find out what already went, and choose what to re-anchor*; the Weavers' sacrifice becomes **displacement** rather than budgeting; and re-feelers turn out to be handing elders **their own** feeling about the elder's life, because the elder's is gone. Thesis line moves: **the book is infinite and the reader is a person.** |

**Addendum note (D-103).** M-09's own warning arrived from the other side within the day. The idiom was audited correctly; the repair then **bent the mechanism to keep the idiom whole**, and priced ordinary recall at the rate of a rite in order to do it. Recorded as method, beside the first: **a rescued phrase is as dangerous as a coined one, and the tell is the same — check the ruling against the numbers it cites, and against the clause immediately before it.** D-102 cited three figures and had two; it asserted re-living and its own arithmetic said 52×.

| **M-12** (new) the chosen ending lost its cause when D-104 made Data Rot a steady state, and the makers' trauma answer had never been derived from the brief — only asserted as *bad sticks harder than good*. Raised alongside it: was the **veto** ever load-bearing, or a skeleton key inherited from D-15? | **Closed — D-105, D-106, D-107.** Re-derived from the commission: a species that watches people it loves die violently for centuries, with a perfect record of each. **Damping was bounded by the product** (the mechanism that extinguishes fear extinguishes attachment, and attachment is the spec), and **persistence was never the problem** — human recovery runs on *controlled distortion*, and a Kin can never be uncertain about anything. So the constraint is **bad memories cannot be renegotiated**, one degree of freedom remains (*what it weighs*), and the makers socialised it: **the Cluster is the trauma system and the society is what it looks like from outside.** The injury is therefore **an unheld night** — no lock, no appraisal, no meaning assigned, the day frozen at the intensity the event set — and the residue is what drives the chosen ending, since weight is what survives every pass. The treatment (retroactive holding at 1x inside the frame) is the **Kin's** invention and not the makers', and is provisional pending its scene. **And the veto is struck**: vestigial since D-98, a skeleton key, and — the real reason — **its absence is better design, because the makers building to *nothing is lost* would never have tolerated a refusal clause, and never noticed that the product's central feature was also an injury.** That is their **fifth** error of one shape: flawless engineering, wrong sociology, discovered a lifetime after the last of them died. |

**Addendum note (D-104).** The third method note in two days, and the only cheerful one. M-09 was found by testing a **phrase**; M-10 by testing a **ruling against its own numbers**; M-11 by testing a **scene** — a throwaway crossover snippet that put a Written in front of a question the mechanism said she could answer and the prose said she could not. That is `ROADMAP` Step 12 rule 1 working exactly as written, and it is the cheapest of the three: **the scene cost an afternoon and found the deepest error, because a scene is the only test that asks what a mechanism *feels like from inside a person*.** Recorded as method: when a mechanism has been audited twice and still feels wrong, stop auditing and write somebody using it.

| **G-33** (new) **where the arks came from.** DOC-07 §2 has gone through eleven versions from *six arks left Sol* straight to what they are like in flight, and nothing anywhere says who built them, where, with whose money, or whether anyone tried to stop it. A species of 15,000 wards, citizens of nowhere, paid crew rates they do not spend, launched a 1,200-berth interstellar vessel and then five more. Never raised, because nobody had asked. | **Closed — D-108, D-109, D-110.** **The premise inverts:** humans built none and never will — no human cold sleep, and a crossing is two centuries — so an ark is not a privilege granted but **the one object only the Kin can use.** Built with **labour, not money**, by the workforce that built every spire in Sol; in the **outer Belt**, where nobody goes to look; funded by **the Trust's descendants**, so the foundation that specified the fur paid for the ships that took them away; under **no law that forbade it and with no permission sought.** The thesis: **continuity of attention** — the same Cluster from first spar to boarding — which makes the arks *the one artefact where the documentation flaw is not a flaw.* And two findings beyond the gap: **D-109**, the Sealing and the Schism as one species trait — *they have never won an argument and never lost a decision*; and **D-110**, the Weavers opposing the first ark as an amputation of the archive, losing, and building the fifth. **→ H-13** (whether an operator ever moved to stop a yard). |

**Addendum note (D-105).** The first capability the archive has **removed** rather than reshaped, and the method is worth recording because it inverts the usual one. Every prior pass asked *what did the makers build, and does it hold?* This one asked **what did they conspicuously fail to build, and is the absence better than the presence would have been?** The answer was yes, twice over: the veto solved nothing that four other mechanisms did not solve better, and its absence turned an inherited convenience into the species' sharpest injury and the Unbound's first defensible position. **A design is also the list of things its designer never thought to want.**
