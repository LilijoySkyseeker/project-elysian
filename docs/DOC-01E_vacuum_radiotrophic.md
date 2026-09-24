# PROJECT ELYSIAN: COMPREHENSIVE WORLD & SPECIES ARCHIVE
## Document ID: DOC-01E — Vacuum Survival, Radiation Shielding & Integument Specification
**Codename:** Project Elysian | **Species:** Aethela (*Homo Sapiens Successor*) | **Self-Name:** The Kin  
**Classification:** Subsystem Deep-Dive: The Voiding Cascade, Radiation Defence, Eyes and Skin in Vacuum  
**Status:** LOCKED (v2.2) — errata folded 2026-09-19; D-68 scale pass 2026-09-20; D-75 fascia extended to the tail 2026-09-21. The radiotrophic *energy* pathway of v1.0 is struck (D-2); the survival envelope is given by DOC-01E.2.

---

### 1. VOIDING RESPONSE & STATE MANAGEMENT

When exposed to hard vacuum ($P < 6.3\text{ kPa}$, the Armstrong limit), the Aethela organism does not suffer explosive decompression or rapid asphyxiation. An autonomous reflex — the **Voiding Cascade**, run by the Lattice's flight controller (DOC-01C §2) — engages within $<50\text{ ms}$ of ambient pressure collapse and leaves the individual **conscious and working**. Torpor is not part of the cascade; it is a later, conditional state.

```
                    VOIDING CASCADE PHASING (<50 ms Trigger)

  [ Pressure Drop Detected ] (Baroreceptors < 6.3 kPa)
             │
             ▼
  [ Exhale-and-Seal ] ──> Lungs vent to ~40 kPa; laryngeal/nasal sphincters lock
             │
             ▼
  [ Fascial Turgor Compression ] ──> Subcutaneous muscle tenses (15 kPa counter-pressure)
             │
             ▼
  [ Storm Posture / Membranes ] ──> Anchors lock; dual nictitating membranes close
             │
             ▼
  [ STATE A — ACTIVE ] ──> Full activity on the State-A O₂ pool (~17 min), then Crawl-Home (~25 min)
             │
             ▼ (State-A pool spent, or ΔT_core ≥ +2 K, or voluntary)
  [ STATE B — TORPOR ] ──> Unconscious; peripheral shunt; ~3 W falling with core temperature
```

#### A. Airway & Cavity Isolation
* **Exhale-and-Seal:** The lungs vent to $\sim 40\text{ kPa}$ before the cartilaginous sphincter rings at the nasal turbinates and laryngeal glottis lock shut — cutting the chest-wall load from $\sim 23\text{ kN}$ to $\sim 9\text{ kN}$, which the interlocking double rib cage carries indefinitely. Lung gas contributes only $\sim 0.35\text{ L}$ of O₂; the reserve is carried by the ***vesica oxygenii*** (DOC-01B §1, DOC-01E.2 §4).
* **Ebullition Prevention:** Cutaneous ebullition is prevented by the elastomeric *fascia subcutanea compressa*, which contracts across all four limbs, the abdomen and the tail (D-75 — the tail's seal, and its anti-pooling under a burn) to apply $15\text{ kPa}$ of mechanical counter-pressure to sub-dermal capillary beds — a latch-state muscle costing $2.5$–$4\text{ W}$ (DOC-01E.1 §4).
* **Anosmia:** The sealed turbinates take smell with them; it is the first sense back on repressurisation (DOC-01F §4).

#### B. State B — Hypometabolic Torpor
State B engages when the State-A oxygen pool is exhausted, when core temperature has risen $2.0\text{ K}$, or on command. Peripheral perfusion drops by $>95\%$; oxygenated blood is shunted into a closed loop between the primary heart and the Neuro-Thoracic Vault; the Bio-Core drops to its heartbeat and clock. **The individual is unconscious.** Base draw is $3.4\text{ W}$ at $37.5^\circ\text{C}$, falling with core temperature ($Q_{10} \approx 2.5$) as the ear radiators deliberately cool the body toward $27^\circ\text{C}$ — the Kin freeze slowly and revive on rescue. The Hum continues throughout, at $0.01\text{ W}$, detectable by an ear array at $\sim 800\text{ km}$ (DOC-01C §4). Duration and limits: DOC-01E.2 §5–6.

---

### 2. RADIATION SHIELDING & REPAIR

Space presents high fluxes of ionizing radiation — galactic cosmic rays, solar particle events, hard X-rays. The Aethela defence is **shielding for what can be shielded and repair for what cannot.** Ambient radiation carries no harvestable energy (a $50\text{ kg}$ body at $15\text{ mSv/h}$ absorbs $\sim 0.2\text{ mW}$); no metabolic pathway uses it.

#### A. Melanin-Metal Micro-Matrix
* **Histological Composition:** The outer epidermis and fur hair shafts carry dense arrays of eumelanin polymers chelated with heavy-metal trace ions (Cu²⁺, Fe³⁺, Zn²⁺) — the same complexes that make the fur mildly conductive (DOC-01B §6).
* **What it stops:** Ultraviolet, soft X-rays, β particles and the low-energy protons and electrons that dominate trapped-belt dose — the bulk of routine exposure. It does *not* stop galactic cosmic rays; a millimetre of skin is nothing to a GeV proton.

#### B. Hyper-Active DNA Repair Pathways
For what penetrates, the Genomic Bio-Core's Sentinel Nucleus (DOC-01C §9) directs continuous genomic maintenance:
* **Enzymatic Cascade:** Constant expression of hyper-redundant **Ku70/80** complexes and **RAD51** analogs enables immediate Non-Homologous End Joining and Homologous Recombination of double-strand breaks.
* **Repair Threshold:** Sustained survival without oncogenic mutation or cellular breakdown at continuous exposure up to $5.0\text{ Gy/day}$. Past that threshold the deaths are slow — days — which is why storm deaths are the rare foreseeable kind (DOC-10 §4, the Shielded Storm).
* **Cost:** Repair is metabolic work; a Kin through a solar event eats for a week afterward.

---

### 3. OCULAR PROTECTION & THERMAL VACUUM INTEGUMENT

```
                        OCULAR VACUUM SHIELDING

  [ Outer Vacuum Environment ]
         │
  [ Outer Nictitating Membrane ] <── Gold/Melanin Electro-chromic Filter (UV/IR)
         │
  [ Inner Nictitating Membrane ] <── Fluorocarbon Liquid Barrier (Prevents Evaporation)
         │
  [ Cornea & Lens ]             <── High-Emissivity Fluid-Cooled Chamber
```

#### A. Dual Nictitating Membrane System
1. **Inner Moisture Barrier (Membrana Fluorocarbonea):** A clear, flexible inner membrane sliding horizontally across the eye, secreting a non-volatile fluorocarbon-rich lipid film that seals corneal moisture down to zero ambient pressure.
2. **Outer Radiation & Solar Filter (Membrana Aurum):** A structural outer membrane impregnated with bio-synthesised gold nanoparticle suspensions and dense melanin — an electro-chromic filter with optical density $\text{OD} > 6.0$ across UV ($200–400\text{ nm}$) and far-IR ($1{,}000–3{,}000\text{ nm}$), darkening automatically in unattenuated sunlight. Humans on a video feed call the filmed eye "silver"; it is gold.

#### B. Cutaneous Lipid Sealing (*Sebum Vacuum*)
* **Self-Healing Skin Seal:** Epidermal glands continuously produce a dense hydrophobic wax-ester compound. In low pressure it polymerises on contact with vacuum into a flexible, air-tight seal over pores and follicles. (In cabin the same secretion carries the individual's scent signature — DOC-01F §4.)
* **Desiccation Limits:** Unassisted cutaneous water loss in hard vacuum is held to $<25\text{ mL/hour}$ with active skin, giving the **12-hour canon ceiling** for State B (DOC-01E.2 §6). The torpid-skin rate is lower and unmodelled; it is the one term that could extend shadow drift toward the ~48 h cold floor.

---

### 4. OPERATIONAL STATE SUMMARY

| Operational Parameter | Terrestrial Baseline | State A (Active Vacuum) | State B (Torpor) |
| :--- | :--- | :--- | :--- |
| **Ambient** | $101.3\text{ kPa}$, $21\%\text{ O}_2$ | $<6.3\text{ kPa}$ | $<6.3\text{ kPa}$ |
| **Metabolic Draw** | $99–133\text{ W}$ ($\sim 2{,}500\text{ kcal/day}$) | $144\text{ W}$ full / $30\text{ W}$ Crawl-Home | $3.4\text{ W}$ at $37.5^\circ\text{C}$, $\sim 1.2\text{ W}$ at $27^\circ\text{C}$ |
| **Respiration** | $12–18\text{ breaths/min}$ | $0$ (sealed at $40\text{ kPa}$) | $0$ |
| **Peripheral Perfusion** | $100\%$ | Working limbs perfused; shell otherwise reduced | $<5\%$ (shunted to core) |
| **Consciousness** | Full | Full | **None** |
| **Ocular** | Open | Membranes closed; gold filter in sun | Membranes closed |
| **Duration** | Indefinite | $\sim 42\text{ min}$ | $\sim 12\text{ h}$ after a full State A (shadow); $\sim 7\text{ h}$ (sun); $12\text{ h}$ canon on immediate drift |

The full envelope, its derivation and its sensitivities are in DOC-01E.2.
