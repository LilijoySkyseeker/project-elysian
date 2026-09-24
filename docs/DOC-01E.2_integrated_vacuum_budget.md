# PROJECT ELYSIAN: COMPREHENSIVE WORLD & SPECIES ARCHIVE
## Document ID: DOC-01E.2 — Integrated Vacuum Budget: Coupled Thermal / Oxygen / Acidosis Model (State A → State B)
**Codename:** Project Elysian | **Species:** Aethela (*Homo Sapiens Successor*) | **Self-Name:** The Kin  
**Classification:** Subsystem Deep-Dive: Unified Vacuum Survival Envelope  
**Status:** LOCKED (v1.1) — D-68 scale pass 2026-09-20 — accepted 2026-09-19; supersedes DOC-01E §4 matrix and DOC-01E.1 §5 matrix  
**Model:** `models/vacuum_budget.awk` — every number below is reproducible from it.

---

### 1. WHY THIS DOCUMENT EXISTS

DOC-01E.1 computed thermal saturation, oxygen depletion and acidosis as three *independent* clocks and took the shortest. That is correct for State A but cannot describe State B, where the clocks interact: core temperature sets metabolic rate (Q₁₀), metabolic rate sets O₂ draw, ear perfusion sets heat loss, and heat loss sets core temperature. This document replaces the three clocks with one coupled model and applies the Step-1 rulings (CANON.md §11): the *vesica oxygenii*, exhale-and-seal, the myoglobin floor, Crawl-Home Mode, 3 W hypometabolic torpor with radiative cooling, and the albedo reflex.

The headline result is that **the pelt, not the ears, dominates vacuum heat loss** — and that this is good news in both directions.

---

### 2. MODEL ARCHITECTURE

```
                    INTEGRATED VACUUM BUDGET (single-node core)

   [ HEAT IN ]                                        [ HEAT OUT ]
   P_met(mode, T_core)  ──┐                     ┌──  P_ear(T_core, open/closed)
   P_solar,bare          ──┼──►  C·dT/dt  ◄──────┼──  P_pelt(T_core, shell state)
   P_solar,fur-inward    ──┘                     └──  (conductive dump: not modelled)

   [ OXYGEN ]                          [ ACID ]
   State-A pool ─► FULL (120 W)        1.2 mol H⁺ ≈ 37 kJ ─► CRAWL (25 W)
   State-B floor ─► TORPOR (Q₁₀)

   MODE MACHINE:  FULL ──(pool empty)──► CRAWL ──(buffer spent)──► TORPOR ──► rescue
                    │                       │                          │
                    └──── T_core ≥ +2.0 K ──┴──────────────────────────┘ (forced)
   TERMINATION:  T_core ≥ 42 °C · T_core ≤ 5 °C · State-B floor empty · 12 h desiccation (canon)
```

Time step 10 s. Single lumped thermal node ($C = 208{,}200\text{ J/K}$, the $60\text{ kg}$ reference individual). The peripheral shell is not a second node; its shunted state is represented by a reduced pelt conductance (§3B).

---

### 3. THERMAL TERMS

#### A. Ear Radiators — a throttle, not a constant
DOC-01E.1's $80\text{ W}$ is the *maximum* (both dishes perfused at $310\text{ K}$, $\epsilon = 0.97$, $0.16\text{ m}^2$, into $3\text{ K}$). The venous plexus exists so dish temperature can be modulated, and the pinnae swivel — folded flat and vasoconstricted they radiate $\sim 6\text{ W}$.

$$P_{ear} = \begin{cases} 80 \cdot \left(\dfrac{T_{core}}{310.15}\right)^4 & \text{open} \\[6pt] 6.0 & \text{folded} \end{cases}$$

**Controller:** State A holds $37.5^\circ\text{C}$ (open above setpoint, folded below). Crawl-Home opens the radiators unconditionally (pre-chill before torpor). State B keeps them open until the core reaches $27^\circ\text{C}$, then folds.

#### B. Pelt Radiation — the missing term
A $60\text{ kg}$ taurform has $\sim 1.36\text{ m}^2$ of furred surface. In vacuum the trapped air that normally carries most heat through fur is gone; what remains is fibre conduction plus radiative exchange between hair layers — the pelt becomes a crude multilayer insulation. Estimated vacuum fur resistance $R_{fur} \approx 2\text{ m}^2\text{K/W}$ (range $1$–$4$). Solving the fur-surface balance $(T_{skin} - T_{fs})/R = \epsilon\sigma T_{fs}^4$ gives a fur surface at $\sim 183\text{ K}$ radiating $\sim 60\text{ W/m}^2$:

$$P_{pelt} = k \cdot \frac{T_{core} - 183}{310.65 - 183}, \qquad k = \begin{cases} 79\text{ W} & \text{shell perfused (State A)} \\ 28\text{ W} & \text{shell shunted (State B)} \end{cases}$$

The shunted value reflects the Voiding Cascade's $>95\%$ peripheral perfusion cut: the limbs and skin cool toward fur temperature and the effective insulation rises.

**Consequence for shadow:** at $144\text{ W}$ with ears folded the net is $+59\text{ W}$; with ears open it is $-15\text{ W}$. **Thermal saturation is never the limit in shadow** — the individual sits between the two by ear control. DOC-01E.1's ear-only figure was a lower bound from a model without the pelt term. The margin narrows with mass (production scales $\propto M$, radiating surface $\propto M^{2/3}$); at the $60\text{ kg}$ reference it is still comfortably negative with the radiators open, and that shrinking margin is what sets the species ceiling near $80\text{ kg}$ (D-68).

#### C. Solar Load — fur shields as well as insulates
DOC-01E.1 assumed all $161\text{ W}$ of absorbed sunlight enters the body. It does not: the sunlit fur surface heats to whatever temperature re-radiates the absorbed flux ($\sim 365\text{ K}$ at the sub-solar point for $\alpha = 0.70$) and only the temperature difference across the fur conducts inward — of order $6$–$11\text{ W}$ total. Solar heat reaches the core mainly through **bare skin**: ear dishes ($\sim 37\text{ W}$ tumbling average if lit), ventral thermal windows ($\sim 27\text{ W}$), face.

| Configuration | Bare-skin gain | Fur-inward gain | Lit-side pelt loss |
| :--- | :--- | :--- | :--- |
| State A, oriented (dishes edge-on, belly to shadow) | $23\text{ W}$ | $6\text{ W}$ (albedo reflex) / $11\text{ W}$ | halved |
| State B, tumbling (uncontrolled) | $64\text{ W}$ | $6$ / $11\text{ W}$ | halved |
| DOC-01E.1 worst case (all absorbed, no pelt) | $161\text{ W}$ | — | — |

**Albedo reflex (D-8):** through $2\text{ cm}$ of fur, pelt albedo is a second-order thermal lever ($\sim 0.7\text{ h}$ on a 24 h drift). Its real job is holding the fur surface below $\sim 60^\circ\text{C}$ instead of $\sim 90^\circ\text{C}$, protecting hair and epidermis over long exposures. Keep it; do not oversell it.

---

### 4. OXYGEN PARTITION & MODE MACHINE

#### A. Reservoirs (post D-4/D-6/D-7)

| Compartment | O₂ (L STP) | Pool |
| :--- | :--- | :--- |
| Lungs, ordinary air, vented to $40\text{ kPa}$ before seal ($4.2\text{ L} \times 0.21 \times 40/101.3$) | $0.35$ | A |
| Vascular haemoglobin ($1{,}134\text{ g} \times 1.34\text{ mL/g}$) | $1.52$ | A |
| *Vesica oxygenii*, State-A fraction ($7.2 - 1.8$) | $5.40$ | A |
| **State-A pool** | **$7.27$** | |
| *Vesica oxygenii*, locked State-B fraction | $1.80$ | B |
| Muscle myoglobin ($1{,}188\text{ g} \times 1.34\text{ mL/g}$) | $1.60$ | B |
| **State-B floor** | **$3.40$** | |
| Total | $10.67$ | |

The bladder lock is enforced by a pressure-gated sphincter on the gas gland: below $\sim 100\text{ kPa}$ residual the bladder only discharges under torpor-state autonomic signalling. Myoglobin is self-locking — it unloads only at the very low $p\text{O}_2$ of shunted tissue.

#### B. Metabolic demand by mode

| Mode | $P_{met}$ | O₂ source | Duration driver |
| :--- | :--- | :--- | :--- |
| **FULL** — locomotion, tools, active RADAR, VHF | $144\text{ W}$ | State-A pool, $0.430\text{ L/min}$ | $7.27 / 0.430 = \mathbf{17.0\text{ min}}$ |
| **CRAWL-HOME** — rail locomotion + passive RADAR only | $30\text{ W}$ | anaerobic, $44\text{ kJ}$ buffer | $44{,}400 / 30 = \mathbf{24.7\text{ min}}$ |
| **TORPOR** — unconscious, Bio-Core clock + minimal cardiac | $3.44 \cdot 2.5^{(T_{core} - 310.65)/10}\text{ W}$ | State-B floor | coupled (§5) |

Torpor base $3.44\text{ W}$ at $37.5^\circ\text{C}$ falls to $1.3\text{ W}$ at $27^\circ\text{C}$ and $0.5\text{ W}$ at $17^\circ\text{C}$.

---

### 5. RESULTS — CANONICAL SCENARIOS

All runs: $60\text{ kg}$, $R_{fur} = 2$, albedo reflex on, $3.44\text{ W}$ torpor base, $1.8\text{ L}$ bladder lock. Reproduce with `awk -v SCEN=<name> -f models/vacuum_budget.awk`.

#### S1 · Shadow EVA (Full → Crawl → Torpor)
| $t$ | $T_{core}$ | Event |
| :--- | :--- | :--- |
| 17.0 min | 37.5 °C | State-A pool spent → Crawl-Home, radiators open |
| 41.7 min | 36.6 °C | Acid buffer spent → **State B** (unconscious) |
| 6.2 h | 27.0 °C | Cooled to torpor setpoint; ears fold; draw $1.3\text{ W}$ |
| 12.0 h | 24.0 °C | Canon desiccation ceiling (DOC-01E) |
| 12.8 h | 23.6 °C | State-B floor exhausted |

**Conscious window 42 min. Survivable drift after a full EVA ≈ 12 h**, desiccation- and O₂-limited within half an hour of each other.

#### S2 · Shadow Drift (straight to Torpor)
| $t$ | $T_{core}$ | Event |
| :--- | :--- | :--- |
| 6.1 h | 27.0 °C | Torpor setpoint reached |
| 12.0 h | 23.9 °C | Desiccation ceiling — $3.7\text{ L}$ still in State-A pool, floor untouched |
| 24 h | 17.8 °C | $2.1\text{ L}$ pool remaining |
| 48 h | 6.2 °C | Still viable, cold floor not yet reached; $0.6\text{ L}$ pool + full $3.40\text{ L}$ floor unused |

**Oxygen is not the limit in shadow drift.** The limit is desiccation (12 h canon) or, if the torpid-skin water-loss rate is lower than the active rate, slow hypothermia somewhat beyond 48 h. This is the "hibernating frog" regime: the Kin freeze slowly and revive on rescue.

#### S3 · Sun EVA, oriented (Full → Crawl → Torpor, tumbling after)
| $t$ | $T_{core}$ | Event |
| :--- | :--- | :--- |
| 17.0 min | 37.8 °C | State-A pool spent → Crawl-Home |
| 41.7 min | 37.3 °C | → State B, now tumbling |
| 6.9 h | 35.1 °C | State-B floor exhausted |

Thermally stable throughout with orientation discipline. **Conscious window 42 min; drift ≈ 6.9 h**, O₂-limited because the core cannot cool in sunlight and torpor runs at $\sim 2.8\text{ W}$ instead of $1.3\text{ W}$.

#### S4 · Sun Drift, tumbling (straight to Torpor)
| $t$ | $T_{core}$ | Event |
| :--- | :--- | :--- |
| 12.0 h | 33.4 °C | Desiccation ceiling |
| 24.7 h | 29.8 °C | State-B floor exhausted |

#### S5 · Sun EVA, DOC-01E.1 worst case (all 161 W absorbed, ear-only loss)
| $t$ | $T_{core}$ | Event |
| :--- | :--- | :--- |
| 17.0 min | 38.6 °C | Pool spent → Crawl |
| 41.7 min | 39.4 °C | → State B, **at the +2 K forced-torpor limit** |
| 2.5 h | 42.0 °C | Heat death |

Kept as the pessimistic bound. Truth lies between S3 and S5 depending on how much bare skin faces the sun; the operational rule that follows is in §7.

---

### 6. CONSOLIDATED OPERATIONAL ENVELOPE (replaces DOC-01E §4 and DOC-01E.1 §5)

| Phase | Shadow | Sunlight (oriented / tumbling) | Limiting factor |
| :--- | :--- | :--- | :--- |
| **FULL activity** | $17.0\text{ min}$ | $17.0\text{ min}$ | State-A O₂ pool ($7.27\text{ L}$) |
| **Crawl-Home** | $+24.7\text{ min}$ | $+24.7\text{ min}$ | Acid buffer ($1.44\text{ mol H}^+$) |
| **Conscious total (State A)** | **$\approx 42\text{ min}$** | **$\approx 42\text{ min}$** (worst case: forced to B at 42 min, +2 K) | — |
| **State B after full State A** | **$\approx 12\text{ h}$** | **$\approx 6.9\text{ h}$** (worst case $\approx 1.8\text{ h}$) | Shadow: desiccation ≈ O₂ · Sun: O₂ (no cooling) |
| **State B, immediate drift** | **$12\text{ h}$ canon / $\sim 48\text{ h}$ cold floor** | **$12\text{ h}$ canon / $\sim 25\text{ h}$ O₂** | Shadow: desiccation → hypothermia · Sun: desiccation → O₂ |
| Thermal saturation, shadow | never (ear throttle) | — | — |
| Thermal saturation, sun | — | never if oriented; $\sim 40\text{ min}$ worst case | bare-skin exposure |

**Canon statement:** *"An Aethela in hard vacuum has about forty minutes of agency — seventeen at full capacity, the rest a crawl — and then twelve hours of sleep in which to be found."*

---

### 7. SENSITIVITY — WHAT IS LOAD-BEARING

| Assumption | Varied | Effect on headline | Verdict |
| :--- | :--- | :--- | :--- |
| Torpor base $3.44\text{ W}$ + $1.8\text{ L}$ bladder lock | $5.7\text{ W}$, no lock | State B after EVA: $12\text{ h} \to \mathbf{2.7\text{ h}}$ | **Load-bearing.** Both are needed; neither alone suffices. |
| Fur resistance $R = 2$ | $R = 1$ (thin/compressed) | Shadow drift cold floor: $48\text{ h} \to 29\text{ h}$; EVA unchanged | Comfortable margin over 12 h. |
| Fur resistance $R = 2$ | $R = 4$ (winter coat) | Shadow drift: still viable at the $48\text{ h}$ cap, O₂ nearly spent | Also fine. |
| Albedo reflex | off | Sun drift: $24.7\text{ h} \to 22.0\text{ h}$ | Second-order thermally; keep for hair/skin protection. |
| Solar bare-skin model | 01E.1 worst case | Sun EVA: stable → forced B at 42 min, dead at 2.5 h | **Orientation discipline is the real solar survival mechanism** — a trained reflex worth writing into DOC-09. |
| Desiccation 12 h (DOC-01E, active skin) | torpid-skin rate unknown | Sets the shadow answer entirely | **Open item** — the only unmodelled term that changes the headline. |

---

### 8. NEW CANON VALUES & OPEN ITEMS

**Locked on acceptance (D-10):**
1. State-A O₂ pool $7.27\text{ L}$; State-B floor $3.40\text{ L}$ ($1.8\text{ L}$ bladder lock + $1.60\text{ L}$ Mb).
2. Torpor base $3.44\text{ W}$ at $37.5^\circ\text{C}$, $Q_{10} = 2.5$; torpor cooling setpoint $27^\circ\text{C}$; cold floor $5^\circ\text{C}$; heat death $42^\circ\text{C}$.
3. Vacuum pelt loss $79\text{ W}$ (perfused) / $28\text{ W}$ (shunted) at $37.5^\circ\text{C}$; ear radiator $6$–$80\text{ W}$ throttle.
4. Envelope matrix §6 replaces DOC-01E §4 column 2–3 and DOC-01E.1 §5.
5. Crawl-Home Mode opens the radiators (pre-chill).
6. Solar orientation reflex: dishes edge-on, ventral windows to shadow — add to DOC-09 §2 vacuum protocol.

**Open (for DOC-01E v2.0 or DOC-01A):**
- Torpid-skin water loss rate (sets whether shadow drift is 12 h or 48 h).
- Two-node thermal model (core/shell) to replace the $k = 70/25$ shortcut if a vignette ever needs limb temperatures.
- Conductive dump to a bulkhead (Voiding while clamped to a hull is common and would extend everything).
- Revival: rewarming a $10^\circ\text{C}$ core at rescue — what the Kin-Nest medical bay does, and how long it takes.
