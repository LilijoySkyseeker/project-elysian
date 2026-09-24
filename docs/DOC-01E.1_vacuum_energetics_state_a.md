# PROJECT ELYSIAN: COMPREHENSIVE WORLD & SPECIES ARCHIVE
## Document ID: DOC-01E.1 — Hard Vacuum Operational Physics & State-A Derivation
**Codename:** Project Elysian | **Species:** Aethela (*Homo Sapiens Successor*) | **Self-Name:** The Kin  
**Classification:** Subsystem Deep-Dive: The Component Physics Behind the Vacuum Envelope  
**Status:** LOCKED (v2.2) — errata folded 2026-09-19; D-68 scale pass 2026-09-20; D-73 loin radius 2026-09-21. This document derives the *terms*; DOC-01E.2 couples them and owns the envelope.

---

### 1. DUAL-STATE VACUUM SURVIVAL ARCHITECTURE

Vacuum physiology is partitioned into **State A (Active EVA / Self-Rescue)** and **State B (Torpor / Drift)**. State A is the default on exposure and is itself two phases; State B is conditional.

```
                           VACUUM SURVIVAL DUAL-STATE

                       [ HARD VACUUM EXPOSURE TRIGGER ]
                                       │
                     ┌─────────────────┴──────────────────┐
                     ▼                                    ▼
        [ STATE A: ACTIVE / SELF-RESCUE ]        [ STATE B: TORPOR / DRIFT ]
        - FULL: ~17 min @ 120 W, all systems     - Unconscious; Bio-Core heartbeat + clock
        - CRAWL-HOME: ~25 min @ 25 W,            - 3 W @ 37.5 °C, ~1 W @ 27 °C (Q₁₀ 2.5)
          rails + passive RADAR only             - Ears cool the core deliberately
        - Conscious total ≈ 42 min               - ~12 h shadow / ~7 h sun after full State A
```

* **State A** sustains locomotion, navigation, tool work and active bio-RADAR without a pressure suit until the State-A oxygen pool is spent; then degrades to **Crawl-Home Mode** on the anaerobic buffer — rail locomotion and passive RADAR only, radiators open, no tools, no VHF.
* **State B** engages when the acid buffer is spent, when core temperature has risen $2.0\text{ K}$, or on command. Unconscious, hypometabolic, self-cooling; the Lattice runs it (DOC-01C §2).

---

### 2. THERMAL TERMS

#### A. Baseline Biophysical Parameters
* **Body Mass ($M$):** $60\text{ kg}$ (reference individual, D-68); **Specific Heat ($c_p$):** $3{,}470\text{ J/(kg·K)}$ → $C_{body} = 208{,}200\text{ J/K}$
* **Core Temperature:** $T_{baseline} = 37.5^\circ\text{C}$; forced-torpor ceiling $39.5^\circ\text{C}$ ($\Delta T_{max} = 2.0\text{ K}$, $Q_{max} = 416\text{ kJ}$); torpor cooling setpoint $27^\circ\text{C}$; cold floor $5^\circ\text{C}$; heat death $42^\circ\text{C}$.
* **Metabolic Draw:** FULL $144\text{ W}$; peak surge $180\text{ W}$; CRAWL-HOME $30\text{ W}$; TORPOR $3.44 \cdot 2.5^{(T - 310.65)/10}\text{ W}$.

#### B. Ear Radiators — maximum and throttle
Both pinnae fully perfused ($A = 0.16\text{ m}^2$, $\epsilon = 0.97$, $T_{skin} = 310.15\text{ K}$) into $3\text{ K}$:

$$P_{ear,max} = \epsilon \sigma A (T_{skin}^4 - T_{space}^4) \approx 80\text{ W}$$

Vasoconstricted and folded flat, $\sim 6\text{ W}$. The ears are a **6–80 W throttle** under Lattice control, not a constant.

#### C. Pelt Radiation — the dominant term
$\sim 1.36\text{ m}^2$ of fur; in vacuum the trapped air is gone and the pelt behaves as crude multilayer insulation, $R_{fur} \approx 2\text{ m}^2\text{K/W}$ (range $1$–$4$). The fur surface settles near $183\text{ K}$ and radiates $\sim 60\text{ W/m}^2$:

$$P_{pelt} \approx k \cdot \frac{T_{core} - 183}{310.65 - 183}, \quad k = 79\text{ W (shell perfused)} \;/\; 28\text{ W (shell shunted)}$$

**Consequence:** in shadow at $144\text{ W}$, ears folded gives $+59\text{ W}$ net, ears open $-15\text{ W}$ — the individual sits between them. Thermal saturation is never the limit in shadow; the v1.0 ear-only figure was a lower bound.

#### D. Solar Load — fur shields as well as insulates
Incident $q_{solar} = 1{,}361\text{ W/m}^2$ on a $0.17\text{ m}^2$ profile at $\alpha = 0.70$ is $161\text{ W}$ *absorbed at the fur surface* — which re-radiates most of it at $\sim 365\text{ K}$. Only $6$–$11\text{ W}$ conducts inward through the fur. Solar heat reaches the core mainly through **bare skin**: ear dishes ($\sim 37\text{ W}$ if lit), ventral windows ($\sim 27\text{ W}$), face. Orientation discipline (dishes edge-on, belly to shadow) reduces bare-skin gain to $\sim 23\text{ W}$; the albedo reflex ($\alpha \to 0.35$) mainly protects hair and skin. The v1.0 worst case (all $161\text{ W}$ into the body) is retained in DOC-01E.2 as a pessimistic bound.

---

### 3. OXYGEN TERMS

#### A. Metabolic Oxygen Demand
Aerobic yield $\approx 20.1\text{ kJ/L O}_2$. At $144\text{ W}$: $\dot V_{O_2} = 0.430\text{ L/min}$. At $3.44\text{ W}$: $0.010\text{ L/min}$; at $1.15\text{ W}$: $0.003\text{ L/min}$.

#### B. Reservoirs and the Partition Rule

| Compartment | O₂ (L STP) | Pool |
| :--- | :--- | :--- |
| Lungs — ordinary air, vented to $40\text{ kPa}$ before seal ($4.2\text{ L} \times 0.21 \times 40/101.3$) | $0.35$ | A |
| Haemoglobin — $5.4\text{ L}$ at $210\text{ g/L}$, $1.34\text{ mL/g}$ | $1.52$ | A |
| *Vesica oxygenii*, State-A fraction ($7.2 - 1.8$) | $5.40$ | A |
| **State-A pool** | **$7.27$** | |
| *Vesica oxygenii*, locked fraction | $1.80$ | B |
| Myoglobin — $26\text{ kg}$ muscle at $45\text{ g/kg}$, $1.34\text{ mL/g}$ | $1.60$ | B |
| **State-B floor** | **$3.40$** | |

The bladder lock is a pressure-gated sphincter that discharges only under torpor-state signalling; myoglobin self-locks by unloading only at the very low $p\text{O}_2$ of shunted tissue.

#### C. Aerobic Operational Limit
$$t_{FULL} = \frac{7.27\text{ L}}{0.430\text{ L/min}} = \mathbf{17.0\text{ minutes}}$$

#### D. Crawl-Home Mode — the anaerobic extension
$$\text{C}_6\text{H}_{12}\text{O}_6 \longrightarrow 2\text{ C}_3\text{H}_5\text{O}_3^- + 2\text{ H}^+ + 2\text{ ATP}$$

Splanchnic histidine/bicarbonate buffers neutralise $1.44\text{ mol H}^+$ before arterial pH falls below $7.15$ — $0.72\text{ mol}$ glucose, $\sim 44\text{ kJ}$ usable. That is **five minutes at $144\text{ W}$**; it is **$\sim 25\text{ minutes}$ at $30\text{ W}$**, which is why the anaerobic phase is a crawl: rail locomotion and passive RADAR, nothing else. At $30\text{ W}$ with radiators open the crawler is also *cooling*, pre-chilling for torpor.

---

### 4. FASCIAL COMPRESSION & MECHANICAL ENERGETICS

The *fascia subcutanea compressa* applies $P_{int} = 15\text{ kPa}$ ($0.148\text{ atm}$) to prevent ebullition. Laplace on the compressed compartments — the fascia acts across the limbs, abdomen and tail (D-75), not the rib-braced thorax, so the governing radius is the loin's, $r = 0.08\text{ m}$ (D-68, D-73):

$$T = P_{int} \cdot r = 15{,}000 \times 0.08 = \mathbf{1{,}200\text{ N/m}}$$

Latch-state cross-bridge kinetics hold tension at minimal detachment rates; cost $3.0$–$4.8\text{ W}$ ($<3\%$ of active draw). Non-limiting.

---

### 5. WHERE THE ENVELOPE IS

These terms are coupled — core temperature sets metabolic rate, metabolic rate sets oxygen draw, ear perfusion sets heat loss — in `models/vacuum_budget.awk`, and the resulting envelope (17 min + 25 min conscious; ~12 h shadow / ~7 h sun in torpor after a full State A; 12 h canon on immediate drift, ~48 h cold floor in shadow) is specified in **DOC-01E.2 §6**. This document does not carry a matrix of its own.
