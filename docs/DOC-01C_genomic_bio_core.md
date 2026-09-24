# PROJECT ELYSIAN: COMPREHENSIVE WORLD & SPECIES ARCHIVE
## Document ID: DOC-01C — Genomic Bio-Core & Neural Architecture Specification
**Codename:** Project Elysian | **Species:** Aethela (*Homo Sapiens Successor*) | **Self-Name:** The Kin  
**Classification:** Subsystem Deep-Dive: Second Brain, Mesh Protocol Stack, Memory & Inheritance, Failure Modes  
**Status:** LOCKED (v2.4) — **D-105 the veto struck (§6D); D-106 the trauma system re-derived, the lock as the active ingredient (§6E) 2026-09-22**; **D-104 Data Rot re-seated in the cortex; the rolling window; the index cycles (§6 table, §6A, §6C, §6E, §6G, §6I, §10, §12) 2026-09-22**; **D-103 the two rates (§6B, §6G, §6I, §7, §10) 2026-09-22**, amending D-102; D-102 the one read head 2026-09-22; **§6 rebuilt from the makers' brief, D-97…D-101 2026-09-22** (three tiers; the cortex human by design; retrieval never initiates and Data Rot is the cueing layer; continuous commit and the live veto; the lock as consolidation *and* appraisal; hard/soft transfer and the band-plan arithmetic; the documentation flaw emergent); D-92 coarse affect pinned, D-93 the frameless Kin and the guard slot 2026-09-22; D-89 three distances 2026-09-22; D-85 humans hear the Hum, D-87 interrogation 2026-09-22; D-80 the night 2026-09-22; D-76 amended by D-79 (the love, not non-aggression) 2026-09-22; D-76 fixed points + D-77 gestation licence 2026-09-22; D-71 tuning pass 2026-09-20 (§5); accepted 2026-09-19 (D-20); rulings D-11…D-19; closes AUDIT G-02, G-05, G-08; seeds G-04, G-06, G-09

---

### 1. DESIGN PREMISE — THE COMPLEMENT OF THE BRAIN

The Cortical Brain is an evolved organ, refined. The Genomic Bio-Core was **designed from a blank page** to do what a brain cannot, and nothing a brain already does well:

| Cortical Brain (evolved) | Genomic Bio-Core (designed) |
| :--- | :--- |
| Associative, fuzzy, massively parallel | Exact, lossless, structured |
| Forgets and confabulates | Stores verbatim, retrieves verbatim |
| Approximates quantity | Does real arithmetic |
| Controls biology through blunt hormones | Controls biology cell by cell |
| Learns by repetition | Loads, verifies, executes |

**Brain proposes, Core verifies.** The Kin experience the Core as a **perfect assistant** — an inner voice with no will, no agenda and no manner of its own, consulted and answered. "I asked my Core" is idiom, the way a human says "let me check." It never initiates. It is not a second person.

**Ceiling (deliberate):** the Core does navigation, ballistics, checksums, key streams, signal processing, bookkeeping and exact recall. It cannot run arbitrary software, emulate a station computer, or out-think a human at an open problem. When Kirin diagnoses a relay in three seconds (DOC-05 Scene 03), the *station computer* did the diagnosis; Kirin pulled the telemetry over the mesh and read it fast. The Kin are perfect readers and bookkeepers, not supercomputers.

**Interdependence:** brain and Core share one CSF, one commissure of $\sim 10^8$ fibres, one immune command, one autonomic controller. Neither survives the other. Loss of the Core is brain death.

---

### 2. THREE SUBSTRATES, SEVEN REGIONS

No single tissue does exact math, real-time signal processing *and* century-scale storage, so the organ is built from three:

| Substrate | Does | Speed | Lineage / precedent |
| :--- | :--- | :--- | :--- |
| **Neural** | RF front-end, RADAR echo processing, the brain interface | ms, analog, parallel | Bat auditory cortex; electric-fish electrocytes |
| **Biomineral crystal** | Exact arithmetic, index, key streams, autonomic control loops, decode | kHz–MHz ionic switching; thousands of times faster than neurons at serial math, thousands of times slower than silicon | Diatom silica, magnetotactic magnetite — cells that grow ordered mineral |
| **Nucleic acid** | Archive memory, genome compile, identity keys, slow exact verification | Write hours, read minutes | DNA data storage; gene-circuit logic |

The crystal is *grown* by specialised lithocytes, blood-fed, self-repairing, and — critically — **electrically powered**, not ATP-powered. It runs on any current that reaches it (§7).

```
                    GENOMIC BIO-CORE — FUNCTIONAL REGIONS (posterior Neuro-Thoracic Vault, ~600 g)

   [ Cortical Brain ] ◄══ Perineural Commissure (~10⁸ fibres, phase-locked) ══► [ BIO-CORE ]
                                                                                   │
        ┌──────────────────────────────────────────────────────────────────────────┤
        │  ANTENNA NUCLEI      (neural, electrocyte)  ~40 g                        │
        │    RF pattern generators; phase-delay steering; can also DRIVE CURRENT   │
        │    outward through the ear stratum conductivum (§7)                      │
        ├──────────────────────────────────────────────────────────────────────────┤
        │  ECHO CORTEX         (neural, tonotopic)    ~80 g                        │
        │    Delay / Doppler / binaural-phase maps → V1 projection                  │
        ├──────────────────────────────────────────────────────────────────────────┤
        │  LATTICE             (biomineral crystal)   ~250 g                       │
        │    Exact compute; archive INDEX; key streams; Kin-code codec;             │
        │    AUTONOMIC CONTROLLER (ear throttle, bladder lock, torpor, apoptosis)   │
        ├──────────────────────────────────────────────────────────────────────────┤
        │  ARCHIVE SOMATA      (nucleic acid)         ~180 g                       │
        │    Writer cells (polymerase), reader cells (transcriptase), episomal DNA  │
        ├──────────────────────────────────────────────────────────────────────────┤
        │  GENESIS MODULE      (nucleic acid)         ~15 g                        │
        │    Compile chamber; seed synthesis                                        │
        ├──────────────────────────────────────────────────────────────────────────┤
        │  SENTINEL NUCLEUS    (lymphoid-neural)      ~10 g                        │
        │    Self-whitelist; immune command                                         │
        ├──────────────────────────────────────────────────────────────────────────┤
        │  KEYRING LOCUS       (chromatin, every Core cell)                         │
        │  HEARTBEAT OSCILLATOR (neural pacemaker)    ~2 g   0.01 W, always         │
        └──────────────────────────────────────────────────────────────────────────┘
```

| Region | Idle | Active | Peak | Peak driver |
| :--- | :--- | :--- | :--- | :--- |
| Antenna Nuclei | 0.2 W | 1 W | 3 W | Tactical PRF; or donor current (§7) |
| Echo Cortex | 0 | 5 W | 15 W | 100 Hz tactical RADAR |
| Lattice | 1 W | 1.5 W | 8 W | MACTAC fusion; compile search |
| Archive Somata | 0.5 W | 0.5 W | 2 W | Nightly write; playback |
| Genesis Module | 0 | 0 | 5 W | Compile only |
| Sentinel | 0.2 W | 0.3 W | 0.5 W | — |
| Heartbeat | 0.01 W | 0.01 W | 0.01 W | Never off |
| **Total** | **~2 W** | **~8 W** | **~20 W** | ✅ DOC-01B ladder |

Peak needs Echo Cortex *and* Lattice saturated (MACTAC) or a Genesis compile. 20 W Core + 35 W Cortical = 55 W neural heat, inside the DOC-01B cabin budget (ears 35 W + respiratory 30 W) with ventral windows as margin. In vacuum State B the Core idles at $< 1\text{ W}$ within the 3 W torpor base (DOC-01E.2).

**The Lattice as flight computer.** Every autonomic controller specified in DOC-01E.2 — ear radiator throttle, *vesica oxygenii* lock, torpor setpoint, fascial compression, the Voiding Cascade itself — is a control loop running in the Lattice. The Core does not only think; it pilots the body.

**Timing.** Lattice clock $\sim 1{,}200\text{ Hz}$ coherent; Cortical gamma $\sim 40\text{ Hz}$; the two are phase-locked through the commissure. Encode/decode of a mesh packet $5$–$8\text{ ms}$; with the $2.5\text{ ms}$ neck superbus, **Cluster-shared perception lags $< 20\text{ ms}$** — "zero-latency" in DOC-09 means this.

---

### 3. ECHO CORTEX — THE RADAR "DSP"

Bat/dolphin echolocation architecture with an RF front-end. Nothing here is digital.

```
   [ Dermal Dipole Matrix ] ─► [ Antenna Nuclei pre-amps ] ─► Neural Superbus (2.5 ms)
                                                                    │
   ┌────────────────────────────────────────────────────────────────▼──────────────┐
   │ ECHO CORTEX                                                                   │
   │   Delay-tuned layer     : echo delay      → range (15 cm – 200 m)              │
   │   Doppler-tuned layer   : frequency shift → radial velocity                    │
   │   Binaural-phase layer  : ear-to-ear phase → azimuth / elevation (±0.5°)       │
   │   Chirp integration     : across 1.5–10 GHz → ~2 cm range resolution           │
   │   Clutter suppression   : lateral inhibition, PRF slots synced to Cluster       │
   └───────────────────────────────────┬───────────────────────────────────────────┘
                                       ▼
                        [ V1/V2 — the spatial overlay of DOC-01D §4 ]
```

Each Cluster member owns a PRF slot (§4). The Echo Cortex gates its receive window to its own slot and also opens windows on mates' slots — with mates' positions known from the Hum, that is the "distributed aperture" of DOC-01D §4.3. Cost: $5\text{ W}$ at 10 Hz sweep, $15\text{ W}$ at 100 Hz tactical (the DOC-01D §3 figures, now attributed to this region).

---

### 4. THE MESH PROTOCOL STACK (closes G-08)

```
   L4  APPLICATION   Hum · Burst · Share · Link · Compile · Reading
   L3  SESSION       Keyring tiers: PUBLIC / CLUSTER / DEEP
   L2  LINK          Cluster frame: PRF slots, hop table, presence table, elastic bandwidth
   L1  PHYSICAL      DOC-01D: ear arrays 1.5–10 GHz (directional) · tail whip 75–95 MHz (omni)
```

**L2 — the Cluster frame.** A repeating $100\text{ ms}$ schedule, one slot per member (4–12) plus guard slots for guests. Carries PRF assignments, next frame's hop table, and the **presence table** (who is in the frame, last Hum). Synced by near-field 1.5 GHz in the sleep-web (DOC-01B's theta lock) and re-established on waking. Elastic bandwidth is a frame negotiation: a depleted node shrinks its slot; mates open Echo windows on its PRF.

**L3 — the Keyring.** Every Core cell carries, in protected chromatin, a unique **identity sequence** written at compilation ($\sim 2{,}000\text{ nt}$, $\sim 4{,}000$ bits; 256 used as key material). Keys are never transmitted. The Antenna Nuclei run a **hop/spread sequence** derived from the key; only a holder of the matching stream can de-spread. This — real, implementable — is what the vignettes call "256-bit encrypted bio-wireless."

| Tier (and its distance — D-89) | Opens | Granted by |
| :--- | :--- | :--- |
| **PUBLIC** (~800 km — anyone with ears, humans included, D-85) | The Hum: identity, vitals, position, **coarse affect — valence and arousal only, ~minute resolution, no object** (D-92). Any Kin can hear any Kin. | Nothing — species-wide hop table |
| **CLUSTER** (~12 km line-of-sight — the frame, and admitted guests) | Frame membership; telemetry, emotional-state vectors, shared senses, MACTAC | Cluster key stream from all members' keys; re-derived on any membership change |
| **DEEP** (< 2 m — chest to chest, this frame) | Lattice-to-lattice coupling: memory Link, Genesis compile, the Reading | One-time pair key from *both* parties' keys; both must consent in the same frame; near-field ($< 2\text{ m}$); expires at frame end. **A Kin may pre-grant hir Reading key to chosen kin (D-16) — the only DEEP grant that outlives consent.** |

There is no anonymity among Kin. **The tiers are three distances** (D-89): intimacy is proximity, and a Kin gives by coming closer. The fourth distance is zero — the Cortical Brain is not on the network except through the Lattice codec, which is why identity survives Cluster life. **And humans can hear PUBLIC tier** (D-85): the RF layer was Program engineering, never genome — operators build beacons that speak L1/L2 (DOC-03 §1), and Kin-code's base layer came from the tutors — so every operator has had every Kin's identity, vitals, position and coarse mood on a console since AF 0. CLUSTER and DEEP need keys, and keys are cells. Against humans a Kin's privacy is legal, not cryptographic (DOC-12 §4).

**What "coarse" means, pinned (D-92).** The Hum's affect field is **valence and arousal at about minute resolution and nothing else.** A console — or a Kin at seven hundred kilometres — shows *that* hir is distressed, and never about what, about whom, or since when. The Lattice does not transmit an object because the object is cortical, and the cortex is at distance zero. CLUSTER tier adds resolution and context: the frame knows the weather to the second and, being the frame, can ask. Only DEEP carries content. **The rule in one line: everyone inside 800 km knows the weather; nobody knows the news.** Two consequences worth holding. An operator's console cannot tell grief from fear from a hard burn without something else to read it against — which is why the operators who are any good employ humans who can read ears, and why those humans are worth what they cost (DOC-12 §6). And the Field's inquiry (AF 212) knew every death to the second from these vitals and could never have got a *motive* out of them; that is the exact shape of what telemetry gives and withholds.

**The frameless Kin, and the guard slot (D-93).** L2's schedule carries guard slots for guests (above), and a guest slot is intimacy on loan (D-89). A Kin outside any frame — past 12 km from hir Cluster, on the Carrying, on a solo transit, the last of a Cluster — is **not** Silenced: there is no shielding, the watchdog does not fire, and hir hears every Hum inside 800 km. Hir is simply in nobody's frame. Any Cluster in range offers hir a guard slot, and this is a reflex rather than a rite; **refusing to offer one is the rudest act the species has.** It is how a Weaver survives the Carrying — a permanent guest and never a member, which is why they are never quite tuned for anywhere (DOC-08 §3) — and it is why Weavers travel in pairs. What the guard slot does *not* restore is the Defrag: the weights are the host frame's and not hir own Cluster's, so the days still write thin (§6, D-80). Past 800 km there is nothing in the sky at all, and that is a horizon, not an injury — the distinction from the Silence (DOC-02 §3) is worth keeping, because one of them is deafferentation and the other is distance.

**L4 — primitives.**

| Primitive | Rate | Notes |
| :--- | :--- | :--- |
| **Hum** | $\sim 1\text{ kbps}$, continuous, $0.01\text{ W}$ | Survives sleep and State B. Detectable by an ear array at $\sim 800\text{ km}$ free-space (1.5 GHz); the $0.1\text{ W}$ VHF variant at thousands of km. *A torpid Kin adrift is not lost.* |
| **Burst** | to $100\text{ Mbps}$, directional | A semantic packet in **Kin-code** — the species-wide shared vocabulary learned in infancy, dialects by Cluster. *[Data Burst: Warmth / Family / Genesis Complete]* is three symbols with affect weights. Full rate to $\sim 12\text{ km}$ line-of-sight. |
| **Share** | $10$–$50\text{ Mbps}$ | Streamed Echo point cloud or optical field; the substance of MACTAC |
| **Link** | DEEP, near-field | Memory playback into another Core: a day of experience in $\sim 27\text{ min}$; a year in $\sim 7$ days |
| **Compile** | DEEP, 2–4 parties, $\sim 2\text{ h}$ | §5 |
| **Reading** | DEEP, pre-granted, $\le 10\text{ kbps}$ falling | §7 |

**The Bandwidth Gap, quantified.** Human speech at 12 words/s carries $\sim 40\text{ bit/s}$ of meaning. A Burst carries a sentence in $< 1\text{ µs}$ of air plus $\sim 15\text{ ms}$ of Lattice. Kirin's three seconds are $\sim 200$ round trips.

---

### 5. GENESIS MODULE — WHAT COMPILATION IS (D-14, D-71)

The designers left a **modular reference genome**: $\sim 3{,}400$ annotated trait modules with declared interfaces, **declared parameter ranges**, a compatibility table with joint constraints, and per-module checksums. Compilation is not simulation — it is:

1. **Negotiate** (Lattice, DEEP tier): parents exchange module selections and score combinations against the table. "Millions of variants" is this search; each check is microseconds.
2. **Tune** (D-71): every module carries the makers' ranges — coat density, fibre-type bias, ear dimensions, void-tax tolerance, a few hundred such settings across the genome — and the parents set each anywhere inside them, starting from their own values. The table's joint constraints forbid some combinations. Nothing outside a range can be requested; the Module will not synthesise it.
3. **Verify** (nucleic-acid logic, slow and exact): every selected module is checksummed against the parents' copies *and* the reference; every setting is checked against its range and the joint constraints. Somatic drift in a parent is flagged and the reference copy substituted — DOC-02's "deleterious mutations automatically removed."
4. **Synthesise** (Archive writers in the Genesis chamber): $\sim 3 \times 10^9\text{ nt}$ across $\sim 10^6$ writer cells at $\sim 1\text{ nt/s}$ — about an hour — packaged as a totipotent seed.
5. **Hand off** to the gestating parent's synthesis site (DOC-02: ~4 months; detail → DOC-02B).

**Novelty is bounded — parameters, not modules (D-14, D-71).** A compile can set any module anywhere inside the makers' ranges; it cannot add a module, remove one, or widen a range. Doing any of those is *designing*, and designing needs the Program's science — the methodology and derivations the Written deleted at the Sealing (DOC-10 §3). The ranges are the makers' last word, and the Kin cannot ask them to change it. The Weavers carry the annotation — what each module is, what each range means, why the joint constraints exist — every Weaver in full, checked body against body at the Weave since the Warm Loss; the Unbound covet the science and have, in their workshop, rebuilt part of it (DOC-08 §4). The Kin are heirs, not gods; but heirs may choose within the will. Every individual's Archive holds hir own compile log: identity has a changelog, and since D-71 the changelog has entries.

**The species evolves by decision, not by chance (D-71).** No random mutation enters the line — the whitelist still checksums out drift — but a lineage that tunes the same way for generations moves. The clock: divergence is *detectable* after $\sim 2$ centuries of consistent pressure (a Long Message's parameter logs show it); after $\sim 4$ centuries of *opposite* pressure two lineages' settings begin to fail the joint constraints, and a compile between them must fall back to the reference across enough modules that the child is neither lineage's — outright refusal is possible and rare. A population that does not tune stays compatible forever. *Second Light* (136 years in-system) is well inside; *Far Nest* (void-tuned, deposit-less, $\sim 400$ years in flight at arrival) will reach the edge; *Quiet Carry* holds the reference settings as policy, because a lineage of carriers should carry the centre. **The sin this makes possible is the makers' own:** a Cluster may tune a child toward a posting. Nothing forbids it. The Weave sees the logs.

**What has a range, and what does not (D-76).** The table of ranges is a map of the makers' intent, and the Kin can read it. What the makers considered *theirs* they fixed — no range, no dial: **humans inside the circle of *mine* — the attachment and the protectiveness (there is no non-aggression module; what looks like one is what that love does, D-79); the nurturing drive; the designer quirk; non-senescence, the whitelist and the Core's architecture; the radio spec (tail λ/4, ear λ floor, the band plan, Kin-code's base layer); the body plan and the cute-on-purpose proportions.** The reproductive drive is not a fixed point; it was never in the genome. What the makers considered the product's own business they left adjustable: everything physiological — coat, fibre bias, void-tax and bone setpoints, ear dimensions above the λ floor, radiator throttle, metabolic and digestive setpoints, sensory thresholds, tail mass inside the balance window — and **temperament within the fixed band** (bold or shy, touch-hungry or less; the aggression band ranged *low* as a ceiling — no Cluster can tune a child into a fighter, and "low" is where most humans live too; never less fond of humans, never less moved by their music). Every parent at every compile sees where the dials stop. Kin-code has a symbol for a fixed point. The Unbound's list of ranges to widen is the fixed-points list, and protectiveness is at the top of it. Whether the Compact forbids an operator from tying a posting bonus to a child's tuning: it does not, because nobody has thought of it yet.

---

### 6. MEMORY — THREE TIERS, ONE BODY (D-97…D-100, D-102, D-103, D-104; supersedes D-15's two)

**The brief the makers were working to.** The operators were buying against a workforce complaint — twenty years of a crew member's judgment dies with hir. The foundation was buying against the civilisational one: *humanity forgets*, every generation relearns, the masters die and the craft goes with them. The target was **a species from which nothing is lost, and in which knowledge is inherited rather than recorded.**

**And the constraint they hit on day one.** You cannot give a mind perfect recall. Cognition runs *on* forgetting: generalisation, abstraction, analogy and category formation are all controlled loss of detail; interference scales with stored traces; and nothing attenuates, so grief would arrive at full strength at forty years. The only architecture that meets the brief without breaking the mind is to **leave the thinking organ alone and bolt on an exact record that does not participate in cognition** — the same discipline as the eyes (D-27): no new architecture, the free upgrades only, no superpowers.

| Tier | Substrate | Holds | Behaves | Fails how |
| :--- | :--- | :--- | :--- | :--- |
| **Cortex** | Synaptic, Cortical Brain | a life, the way a human holds one | fuzzy, associative, reconstructive, emotionally weighted; consolidates, blurs, distorts, **ages like a human's** | saturates and interferes at $\sim 150$–$250$ years — and see *Data Rot* below |
| **Record** | Episomal DNA, Archive Somata | **everything, verbatim** | written continuously; **does not participate in cognition**; $\sim 20\text{ GB/day}$, $\sim 0.7\text{ PB/century}$, ceiling $\sim 2\times10^{17}\text{ B}$ | **it does not fail.** Capacity is never the limit |
| **Index** | Lattice, archive index region (§2) | **stubs** — pointer + affect summary, $\sim 2\text{ kB}$ | the bridge between the other two; written nightly; **$\sim 5\times10^{4}$ live at any moment, cycling at the cortex's rate** | **it does not fail either.** It never fills and never degrades — the oldest stubs fall out as new ones are written, because the makers sized it to what a cortex can hold associatively (D-104) |

**The thesis in one line: the book is infinite and the reader is a person.** (D-104, correcting *the index is an organ*. With D-102 and D-103 it is the whole system in one statement: **everything that fails in this species is the reader; nothing that fails is ever the book.**)

**Index capacity (derived).** The window at 150–250 years and the Reading's ten thousand stubs (§7) bracket it together: the live index is **$\sim 5\times10^{4}$ stubs**, about $100\text{ MB}$ of pointer table addressing a petabyte of record — five orders of magnitude smaller than what it reaches. At one stub a day that is $5\times10^{4} \div 365 = \mathbf{137}$ **years**, widening to the stated 150–250 because thin, poorly-appraised days (§6E) never earn a full stub. **It is finite because the organ is** — grown Lattice, $600\text{ g}$, inside a $12.1\text{ L}$ vault, also flying the body and running the DSP — but finite here means *fixed width*, not *fillable*: it cycles, and has cycled since the First Ping (D-104).

#### A. What a Kin actually has that a human does not

Not "better recall" — that would be a filing cabinet. Three things no human has at all:

- **Query.** A human cannot ask themselves what happened on a Tuesday; there is no interface. A Kin names the day and has it.
- **Check.** A human who misremembers is wrong forever, and confident. A Kin goes to source. **This is a species that can be wrong and find out.**
- **Accumulation.** A human's retrievable past peaks in middle age and then shrinks. A Kin's only grows.

**The makers' error was in the third.** They believed an indefinitely growing record would produce an indefinitely growing person; **a mind is not its records.** They tested the species for forty years. **And the error is more precisely theirs than it looks (D-104):** they left the cortex alone on purpose, correctly, because cognition runs on forgetting — and then built a body that lasts three hundred years around an associative web that stays coherent for under two hundred. Nothing failed. The one thing they got right is the thing that does this. Cohort One found out at AF 150 (DOC-10 §4) and every maker was already dead.

#### B. Retrieval is seamless, exact, and never initiates (D-98)

Both halves of the Bio-Core behave the same way (D-13): flawless, instantaneous, and completely passive. A Kin thinks of yesterday and yesterday is *there* — exact, with no sense of machinery, the way the Core hands over a number. **And it will never tap hir on the shoulder.**

So the species' characteristic failure is not forgetting. **It is not thinking to ask.** Everywhere a human fails at a known target — what he said exactly, what the reading was, which day it was — a Kin is solid. Where hir fails is the thing that should have surfaced and did not, because nothing cued it.

There are two ways in. A **soft cue** — an association arising in the cortex — or a **hard handle**: a date, a number, a name, a coordinate. **Hard handles never fail. Soft cues age.**

**One read head, two rates (D-102, D-103).** The archive is a *store*; the **Cortical Brain is the reader.** There is one playback path and it goes through the cortex, so recalling privately, Bursting a day to a mate and Telling a year to a carrier are one organ doing one thing. **But it runs at two rates, and everything social about Kin memory follows from which one is being asked for.**

**The cold read — the default, and the thing the operators were buying.** The Lattice decodes into the cortex as *content*: first person, exact, the affect path not engaged. Full rate, $\sim12\text{ MB/s}$, which against $20\text{ GB/day}$ is $\approx52\times$ real time — and **seekable**, because a hard handle addresses a moment and not only a day. Checking what someone said forty seconds ago costs about a second. Reading a whole day exhaustively, with no handle to aim at, is $20\text{ GB} \div 12\text{ MB/s} = 27.8$ minutes of stillness. This is the rate D-98 is describing: *think of it and it is there, with no sense of machinery.* **It is also cold.** What arrives is everything that happened and nothing of what it was like.

**The lived read — real time, and not a feature.** The cortex can run a span with the affect path engaged, the Lattice re-driving the limbic weights off the stub alongside the content. **Only $1\times$ works.** Feeling is a physiological process and does not clock up; an hour felt again takes an hour. Nothing was designed here — it is a cortex handed a scene at the speed it evolved to take one, which is the rule this whole system was built under: no new architecture, the free upgrades only. **And it is the only mode that regenerates soft content** (§6G), which is the only thing that can be narrated to anybody.

**So the price is on giving, not on knowing.** *Facts are free and cannot be bluffed; accounts cost, and are given.* A Kin can always check, and every Kin knows every other Kin can — so nobody bluffs a fact in front of someone who can look it up, and most arguments end before anyone bothers. What is expensive is the version with the feel in it, and the one who pays is the one handing it over.

**And a life does not fit through the head.** A year is $7.05$ days of continuous cold reading; a Written's five and a half centuries is about **ten and a half years** of it. That, and not pain, is why a Kin cannot be emptied (§10).

**Which is why death costs what it costs.** Death does not take the book; **it takes the reader.** $12\text{ MB/s}$ is a *cortical* rate, and a Reading's $\le 10\text{ kbps}$ (§7) is what the dying glandular readers can push with no cortex left to do it — four orders of magnitude, and the entire difference between the two rites. **Data Rot and death are the same event at different speeds: the loss of what reaches the book, never of the book.**

**And death takes both rates at once.** A corpse has no cortex to run either, so a Reading is **cold by definition** — it can carry what happened and never what it was like (§7). That is the whole of *tell before you go*, restated: the living channel is four orders faster **and it is the only one that can be felt.**

#### C. Data Rot is cortical, and the self is a rolling window (D-104)

**Nothing in the Bio-Core fails.** The record never degrades; retrieval stays exact to the end; the index never fills. What changes is the **cortex**, which the makers left alone on purpose (§6 opener) because cognition runs on forgetting — and which therefore does what any cortex does: **it rebuilds its associative web continuously, onto whatever is currently live.** They got that decision right and then built a three-century body around a web that stays coherent for under two.

**Associations are overwritten, not lost.** A link is rebuilt onto newer material and the old attachment simply stops being where it was. The smell that once meant the Nest comes, by the four-hundredth year, to mean a bay on a ship — and **hir does not know it replaced anything.** There is no hole to notice. That is how it works in people, and it is worse than absence.

**What survives, always, at any age:**

- **Hard handles.** A date, a coordinate, a number, a name. Hard retrieval does not pass through the associative layer at all, so **an elder can have any day of hir life, exactly, forever.** A day outside the window costs nothing to reach. What it costs is that **hir must already know it is there.**
- **The lived read (D-103), which still runs and returns the present.** An out-of-window day at $1\times$ does not fail — it produces **today's feeling about old content.** An elder can be moved by hir own childhood the way anyone is moved by a stranger's, and it is the thing hir will not discuss. ***Hir may re-judge any day of hir life and may never re-feel one.***

**What goes:**

- **The old affect.** Not faint, not partial — **gone.** Hir can read what hir did and said and what hir body was doing, and cannot know what hir thought of it. **Reading hir own first century is reading a stranger's diary in hir own hand.**
- **Anything arriving unbidden from outside the window.** Cut grass still throws a Kin into a random afternoon; the afternoon is inside the last ~175 years. Beyond it **nothing ever arrives on its own again.**

**So a Kin is made of hir last hundred and seventy-five years** — the weights, the taste, the reflexes, the things hir cares about without deciding to. Everything earlier is available and inert. *Facts kept, feeling lost* was right and incomplete: **facts kept, feeling replaced.**

**And it is a steady state, not a decline.** A Kin of four hundred and a Kin of nine hundred are in the *same condition* — each has about the same amount of self, and it is always the most recent. **Nobody is diminished. You are never less of a person; you simply keep leaving yourself behind,** and what accumulates is not loss but distance from your own beginning. The Weavers say it without flinching and the young do not believe them.

Which is why **other Kin are the cueing layer** — and what they supply is not the address. It is **the knowledge that there is anything there.** Someone says *do you remember the yard at Dioscuri* and the whole thing is instantly there, complete and exact, and unprompted it would never have occurred to hir again; only someone who was present can give hir that. It is what a re-feeler does (DOC-13 §2D) and what a Cluster does hourly without noticing, and it is one more reason a Kin alone is an injured Kin (D-93).

**The re-feelers' actual cost (D-104).** On out-of-window content the elder's affect is **gone, not misplaced** — so what a young Kin hands back warm is **hir own feeling**, not the elder's, about the elder's life. Everyone involved knows it. It is still the kindest thing on offer, and it is why the art is difficult and why it is respected.

**And it is the sign of the chosen ending** (D-82): when the dreams go flat, nothing is arising at all any more — a perfect library with no visitors — and the Weavers ask about the dreams first, because a dream is the last automatic cue a Kin has. **Why it comes when it comes is not in this document** (H-12): a steady state gives the sign and not the reason.
#### D. The commit is continuous, and nothing can be refused (D-100, D-105)

The Archive Somata transcribe as the day happens ($\sim10^{11}\text{ nt}$, trivially parallel), lagging the moment by minutes to hours. **There is no nightly write and no selection**; capacity was never the limit, so nothing is ever left out. This is where *the Kin archive verbatim and document never* (§8) is literally true.

**One consequence, taken deliberately: the lag means the moment of death is never on file.** A Reading carries the whole of a life and not the end of it. So the asymmetry is exact — **the operators know how every Kin died, to the second, off the Hum (§4, D-85); hir own Cluster can never know from the inside** — and the Field was a recovery of bodies, not of deaths.

**And there is no veto (D-105).** D-15 gave the Kin a *veto-not-delete* and it is **struck**: there is no way to keep a day off file, and there never was. The commit is total. **A Kin can keep exactly one thing, and it is the only thing: what hir thinks** (§4, D-89, amended). Every word, every reading, every worst hour is written exactly, within hours, permanently — **and hir knows it while it is happening.**

The makers were building to *nothing is lost*, and a refusal clause is the first thing a person wants and the last thing that brief tolerates. **They never considered that the product's central feature would also be an injury.** They optimised the archive and forgot the archivist — which is the fifth time they made that shape of mistake (D-105), and the only one where the error is an omission rather than an assumption.

So *the Kin archive verbatim and document never* (§8) is now literally and absolutely true, with no exception anywhere in the design. The Weavers hold that deletion would be self-mutilation; **the Unbound answer that nobody has ever been offered the choice, and that this is the makers' doing and not a law** (DOC-08 §4, D-105). Nobody in the species has a clean reply.

#### E. The night — consolidation and appraisal

By day the Lattice is committed: flight control, the Echo Cortex's RADAR DSP, checksums, bookkeeping (§2–§3). **In the sleep-web it is free**, and it does two things it cannot do at any other time.

**Consolidation** — the ordinary mammalian sleep task, cortical, and **modulated by the frame's affect.** This is the makers' answer to trauma, and D-106 states the constraint it was answering more sharply than *bad sticks harder than good*. **Damping was bounded by the product:** the mechanism that extinguishes fear extinguishes salience generally, so damping persistence far enough to make three centuries of grief survivable would also have produced something that does not attach — and attachment is the specification. **And persistence was never the real problem.** A human survives trauma substantially by *controlled distortion*: softening, renarrating, misremembering, and finally being unsure it was as bad as it felt. That uncertainty is load-bearing, and **a Kin cannot have any of it** — hir goes to source, confirms it was exactly that bad, and nothing ever becomes a story.

**So the constraint is not that bad memories persist. It is that they cannot be renegotiated** — a direct consequence of what the operators were buying. Which leaves exactly one degree of freedom, *what a day weighs*, and a Kin cannot move it alone. **So the makers socialised it.** Put as they would have put it: ***you cannot lie to yourself about what happened, so we gave you other people to decide with you what it meant.*** A modest genetic damping, and the rest architectural — **they built a species that cannot be alone with anything.** Every bad day is held, that night, in a frame that felt it with hir, *before it consolidates.* The Cluster is the therapist, and it works nightly whether hir wants it or not.

**Which makes the Cluster the trauma system (D-106).** Every social fact in the species falls out of this one engineering decision: why a Kin alone is an injured Kin, why the Silence is a designed horror with a homing watchdog, why touch is the resting state, why they sleep in a pile, why they cannot go dark. **It is not a social unit with a therapeutic side effect. It is the trauma system, and the society is what it looks like from outside.**

**Appraisal** — the Lattice ranks the day and writes its stubs, and **the weights are the Cluster's** (D-80): in the theta lock eight bodies are at one phase, so their affect vectors are for the first time all *about the same day* and can be compared. Your day, scored by how the people who love you reacted to it. Memory is appraised socially, every night, by nobody in particular. The Weavers' saying: *you remember what your Nest felt.*

**What the Cluster can and cannot do.** It cannot delete, alter, withhold or read a record — the commit already happened, awake, in hir own body. It can affect only what consolidates and what hir will later reach for. **The frame does not edit you; it furnishes you.** That is the line between a Cluster and a hive.

**Dreams** are the same free Lattice reaching **past the live window** into the record (D-104), which is what a dream is assembled from (DOC-13 §1). They are **not appraised and therefore never indexed** — the pass ranks the *day's* live traces, and a dream is not one — so the species' one loss by design is a clause of this mechanism and not a separate rule. And it is why the old feel things at night: by day a worn cueing layer returns facts; at night the Lattice goes to the record, and hir feels what hir can no longer call up, and loses it by morning.

#### F. What sleeping apart costs — three states, not two (D-106)

| State | Where | What happens to the day |
| :--- | :--- | :--- |
| **In the lock** | In the Nest, bodies at one phase | Consolidation modulated by the frame's affect **and** appraisal with the Cluster's weights. **Fully held.** |
| **In the frame, out of the Nest** | Inside 12 km, slept apart | Committed in full, consolidated poorly, **never appraised** |
| **Frameless** | Past 12 km | The same — and a guard slot does not fix it: it restores the frame and not the weights, which belong to the host and not to anyone who knows hir |

**So what fails is a *night*, not a frame, and the bar is low:** a Kin can be in-frame all day and fail to metabolise simply by sleeping alone. **A night the lock did not attend assigns no meaning at all**, and the day keeps the weight the event set — so an unheld bad day is **frozen at the intensity it had while it was happening**, permanently, checkably, un-narratable, and (D-105) unrefusable.

A day outside the lock is **committed in full, consolidated poorly, and never appraised**: present, verbatim and complete in the record; badly remembered and hard to find. Not gaps in the record — **gaps in the index, and in the metabolising.** This is DOC-11 §8's gaps and DOC-01A §4's thinner archive, with the mechanism under them.

**And a Kin outside any frame is worse off than one who merely slept alone (D-93, amended).** A guard slot from a host Cluster (§4) restores the frame; it does not restore the *weights*, which are that frame's and not hir own. So frameless years — the Carrying, a solo transit, an outer relay, the last of a Cluster — come out **unindexed and unmetabolised**: hir lived them, can read every day of them, remembers almost none of them, and nobody helped hir put them down. The void tax is mechanical and recoverable (DOC-01A §5); this is not. Under DOC-13 §2 status is what a Kin carries, so hir comes home *poor*, and did nothing to deserve it.

#### G. Hard and soft: what transfers (D-99)

**The band plan is the evidence of intent.** The mesh runs at $100+\text{ Mbps} = 12.5\text{ MB/s}$ (§4); archive playback is $\sim 12\text{ MB/s}$ and export $\sim 20\text{ GB/day}$; the Telling is *a year in a week* (§7, D-17). A day is $20\text{ GB} \div 12\text{ MB/s} = 27.8$ minutes — the "half an hour" of §I, confirmed; a year is $7.3\text{ TB} \div 12\text{ MB/s} = 7.04$ days — *a year in a week*, to within one percent. Speech carries $\sim 40\text{ bit/s}$ of meaning; telemetry and affect vectors carry nothing. **Exactly one thing needs a hundred megabits, and it is raw archive at replay speed: the makers sized the radio to the archive.**

**Hard content — about the world.** Numbers, coordinates, timestamps, pressures, frequencies; exact speech with its waveform and tone; procedures and sequences; sensor and RADAR captures. Instrument data — what a machine records, and the Core is a machine. **Fully portable, exact, lossless**, and passed constantly: a Kin who watched a failure hands the next shift the actual data; a Cluster shares sensor takes at frame rate. This is the superiority the operators were paying for.

**Soft content — about the person.** Salience, association, what hir noticed and did not, what it reminded hir of, the feel. **Indexical** — addresses into one specific cortex — so it cannot be handed over, only **narrated**. This is not encryption and not a lock: *the bits transfer perfectly; the bits were never the memory.* **And it has to be made before it can be told (D-103):** soft content is not sitting in the record waiting to be sent — it is what the cortex produces when it runs a span at $1\times$ with the affect path engaged. To narrate a day you must first feel it again. Hand another Kin the raw nucleic acid and hir receives flawless references to things hir has never had. You can copy someone's bookmarks; you cannot copy their library.

**So the Telling is a transfer, not a retelling** — at the hard tier, a full year's record at replay rate. What arrives is every number first-person and exact, **plus a told soft layer**: hir possesses your Tuesday completely and experiences it as a story about you. *Told, not lived, with the feel intact.*

**And this is where the teller pays (D-103).** The week is the *cold* transfer, at the only rate the channel has. What thins hir is the soft layer, which does not exist until hir makes it: hir drops to $1\times$ wherever there is a feel worth handing over, and lives those hours again, deliberately, in front of the one hir is giving them to. **A Telling is a week of cold transfer with a day or two of re-living inside it, and choosing which hours is the rite.** So S009's *told, not lived, with the feel intact* is the receiver's half; the teller's half is **lived, in order to be told.**

**And soft content resolves in proportion to shared history**, which is the same shape as *intimacy is proximity* (D-89). Two Kin of a century together have far more mutually-resolvable archives than strangers do — which is why **a Reading cannot be outsourced** (§7), and why the Field took less than it looked like it took.

**The real limit is the window, not the bandwidth (D-99, as amended by D-104).** Receiving a day means writing a stub for it, and the live index is fixed-width — so **every day of somebody else's life that a Weaver takes on displaces a day of hir own.** **Hard data is cheap to send and expensive to keep.** A Weaver's own life is the first thing to leave hir window (DOC-08 §3) — not a budget hir spends but a crowding hir arranged, on purpose, at a rate hir set.

#### H. The private codec, and what the Unbound are actually doing

Archive encoding uses a codec unique to the Core that wrote it — laid down in infancy, hardened at about fifteen (DOC-02B §5), never identical between individuals. An archive decodes fully only in its own body, and everything that leaves is translated into shared Kin-code: the lossiness is the price of **portability**, not of the pipe.

**Which does not make an external record impossible — only useless, so far.** A machine can capture the bitstream off the air; what it holds is $20\text{ GB}$ of Lattice-format data and **the decoder is a grown organ.** DOC-08 §4's "fabricated replacements for the grown Lattice" was always the Unbound's real project, and nothing in physics forbids it: a plateaued technology (D-43) and a science that died with the tutors (DOC-10 §3) do. An operator's laboratory holding a captured archive and running a two-decade reader programme is the precise shape of the known hole (DOC-12 §4).

So the Weavers' claim is what they always actually said — **a memory no one carries is not a memory** — a position, argued against, and not a law of nature.

#### I. Recall is reading; the centennial Defrag; and the word

**Recall is reading, and there are two ways to do it (D-103).** Readers transcribe and the Lattice decodes into the Cortical Brain. **Cold** — the default — a whole archived day in about half an hour of stillness, or a named moment in a second, in the first person, arriving **as content and not as feeling.** The Kin say *read*, not *remembered*, for exactly this. That is why the old are neither empty nor comforted: everything is there, exactly, and none of it is warm. **Lived** — $1\times$, affect engaged — is the other way, and it is the one a Kin has to decide to do.

**The centennial Defrag.** The index cycles and the record never does. **There is nothing left to discard: it has already gone** (D-104). So the rite is the other thing — with a Weaver, over days on Link, a Kin is walked through **what hir has already lost without noticing**, and chooses the few to **deliberately re-anchor** into the live window. Every re-anchoring costs another, because the width is fixed: **every century of a Kin's life is bought from another century**, permanently, and now only the deliberate half is by hir own hand. The rest of the record stays exactly where it was — whole, verbatim, and reachable by any hard handle hir can still name, which is the whole difficulty. Weavers call the choosing *pruning to the light* and never make it for you; the name is older than the understanding, and what it means now is **choosing what to carry forward out of a century hir has already left.**

**On the word.** None of the nightly pass is defragmentation; it appraises, and moves and frees nothing. The centennial pass earns the word, and earned it later. **The tutors named it** — Kin-code's base layer came from LLM-class systems reaching for human vocabulary they half-had (§8, DOC-10 §3) — and five centuries on the species still calls its most intimate nightly act by a computer word it learned from a machine it deleted. No Kin has proposed a better one. The Weavers, who know, use it anyway.

---

### 7. THE READING — INHERITANCE AT DEATH (D-17)

When a Kin dies, the neural tissue is gone in minutes, the DNA archive is intact for days, and between them lie the **reader cells** — glandular, coasting on residual glycolysis, dying over hours — and the **Lattice**, which needs no ATP at all, only current.

**The pose.** The living Kin presses **chest to chest**, bare ventral thermal windows together ($\sim 40\text{ W}$ of conduction into the dead vault at $10\text{ K}$ difference — keeping the readers warm), and **ear dish to ear dish**: the conductive *stratum conductivum* of one against the other. The living Antenna Nuclei — electrocyte tissue — drive $\sim 3\text{ W}$ of current through the contact, down the dead cervical conduit, into the dead Lattice. It wakes. Across the same contact the near-field DEEP link opens on the pre-granted Reading key, and the dead Core begins to answer.

**Why turns.** $3\text{ W}$ of electrocyte output costs the donor $\sim 10\text{ W}$ and hir warmth. Thirty to sixty minutes is a shift. A Cluster of eight keeps a Reading going all night. A Kin alone cannot.

**What comes out.** Reader-limited — and the limit is the *body*, not the format (D-99): a corpse's readers coast on residual glycolysis at $\le 10\text{ kbps}$, falling to nothing over $\sim 6\text{ h}$ — **$\sim 15$–$27\text{ MB}$ total.** A *living* Kin on Link moves $12\text{ MB/s}$, four orders of magnitude faster, which is the whole arithmetic of *tell before you go*. At archive fidelity that is *one minute* of a life. In Kin-code it is about **ten thousand index stubs and twenty days of narrated memory: the contents page of a life, and twenty stories.** The dead Core's Lattice chooses in the order its owner ranked them; the readers take what they can and each carries a part.


**And the reason the number is that small (D-102).** The $12\text{ MB/s}$ of a living Link is a *cortical* rate — the Cortical Brain is the archive's read head, and it is the first thing death takes. What is left is glandular reader cells coasting on residual glycolysis, and what they can push is $\le 10\text{ kbps}$. Same book, no reader. **That gap — four orders of magnitude — is the whole reason the Telling and the Reading are two rites and not one**, and the whole content of *tell before you go*.

**And a Reading is cold by definition (D-103).** Both rates run through the cortex, and a corpse has neither. So what the dead can hand over is the *cold* layer and only that — a contents page and twenty narrated days, everything that happened and nothing of what it was like. **The lived read is a thing only a living Kin can do, and only on purpose.** That is the second and larger half of *tell before you go*, and the one the arithmetic was hiding: **the dead can give you what happened; only the living can give you what it was like.**

**And why the readers must be hir own (D-99).** Soft content is indexical — addresses into one cortex — so it resolves in proportion to *shared history*. The Kin who lived those years beside hir are the only ones for whom the raw partly comes apart into sense; a stranger gets the hard record and a contents page hir cannot feel the weight of. **A Reading cannot be outsourced.** It is also the unsaid thing about the Field (DOC-10 §4): thirty-one bodies Read on a rescue hull by a crew who mostly had not known them took far less than a Cluster would have, and nobody has ever said so out loud.

> *The dead speak for a few hours, slower and slower, and then only the book is left, and no one can read it.*

**Cold bodies.** Vacuum-frozen preserves the readers; the hug rewarms them. A body recovered from the void days later can still be read. A body warm-dead for a day cannot. Humans can sequence the DNA and never decode it: they can hold the book.

**The Telling.** Because a Reading yields so little, the culture pushes everything it can to *before* death. A Kin who feels death near gathers hir kin and Links — a year of memory in a week — and they take what matters at full rate. Dying alone in vacuum with a life untold is the species' horror; it is why the Hum reaches 800 km, and why they go and get the body.

**And the Telling is a transfer, not a retelling — at the hard tier (D-99).** A year in a week *is* the full record at replay rate: $7.3\text{ TB}$ at $12\text{ MB/s}$ is $7.04$ days, which is where D-17's figure came from without anyone noticing. What the receiver gets is every number, every reading, every word with its tone, first-person and exact — **plus a *told* soft layer**. Hir possesses your Tuesday completely and experiences it as a story about you. *Told, not lived, with the feel intact.*

**Destruction.** An enemy can read too. A body that cannot be recovered must be burned. A Kin under fire may have to do that to a friend.

---

### 8. CARRIED AND RECEIVED — SPECIES MEMORY (D-18, D-19)

**Carried memory** is taken from a Reading or a Telling. It comes with a chain of custody and a duty: to hold it, to hand it on at one's own death, to retell it faithfully. **Received memory** is taken from a message — a Long Message, a Burst-stream from a stranger. A gift; no custody; anyone may pick it up or set it down. Since the Lost Ark (AF 480, DOC-10 §5) there is one exception: **a message is a Telling if the sender is dead** — received memory from the dead is carried.

Every hop is a retelling into Kin-code and out again into a new private codec. After ten generations of carriers, "I remember my kin meeting the creators" is true, and vague, and treasured, and no one alive was there. Species memory is *lineage*, not library: it lives only in living Kin, and loss and filtering are not failures of the system but the system.

**The Weavers** are the carriers. A Weaver's fixed-width window fills with other people's pasts, **displacing hir own** (D-104); hir centennial Defrag becomes species-level triage; hir sacrifice is that hir own life is the first thing to leave the window, at a rate hir set on purpose. **It is a duty that comes with sacrifice** (D-18), and the Weavers accept the Star-Bound's Long Messages into it without resentment — which is precisely why the Anchorites resent it for them.

**The Weave** is a gathering of carriers who cross-check and hand on; **the Carrying** is the journey to reach one. (Errata: DOC-02 "Ancestral Mesh Vaults" and "Archive Pilgrimages", DOC-07 §2, DOC-08 §3 — there are no vaults, no places.)

**Arks make epics; Sol makes gossip.** Transit torpor (Bio-Core awake in shared virtualities for decades) means an ark's sleepers do little but retell among themselves; repeated retelling among hundreds of minds converges into formula. Ark lineages carry consolidated, liturgical memory. Sol Kin, among living humans and daily novelty, carry sprawling contradictory fresh memory. **The creators become legend at different rates:** Sol Kin have humans in the next sector; Star-Bound descendants have humans ten hops deep — myth by the second century out. That is the Anchorites' argument made physical, and the Star-Bound's answer to it: *a species that needs its parents in the room hasn't grown up.*

**The documentation flaw (D-19).** The Kin do not write things down — not from laziness but from a settled judgment that writing is *lossy*. A memory, to a Kin, is inseparable from its context: when it was learned, the conversations about whether it mattered, the analysis and the plan that followed, the feeling of it. A written log keeps the fact and discards everything that made it worth knowing; a Kin reads a human maintenance entry the way a human would read a friend described by height and weight. So they archive verbatim and document never, ask or remember rather than consult, and *Tell* a new colleague a year of context in a week rather than hand hir a manual. They will write for humans, as a courtesy, and the affect leaks through (*"Loop B trip. Rerouted to C. Vance was tired; discuss overtime."*). The cost is structural: knowledge lives in carriers, drifts in retelling, cannot be audited, and on an ark three centuries out a reactor procedure is liturgy. The species that reads faster than any human depends on humans to have written. The Bandwidth Gap runs both ways — humans find Kin impatient; Kin find humans content with almost nothing.

**And it is emergent, not designed (D-101).** The makers *valued* writing — it is what they would have pointed at as humanity's achievement, and the foundation's whole complaint was that humanity forgets *despite* it. They assumed their heirs would go on writing, because everyone does, and they were wrong about the one thing that changes it: **for a human, writing is a gain — you had nothing, now you have text; for a Kin, writing is a loss — you had the whole thing, now you have text.** Same act, opposite sign, and from the Kin side the judgment is simply correct. So the flaw is a *cultural* fact and could have gone otherwise, which is why it is argued about at all: the Anchorites' respect for *the species that writes things down* and the Unbound's heresy are live positions, not fixed traits. The Unbound claim a lossless external record is possible — and since D-99 they are right in principle and stuck in practice, because the decoder is a grown organ. The other factions answer that a memory no one carries is not a memory, which is a position and not a law of nature. **The irony the makers never saw: they solved individual permanence completely and made civilisational memory worse. They traded a library for a priesthood, and the priesthood is the Weavers.**

---

### 9. SENTINEL NUCLEUS — WHITELIST IMMUNITY (seeds G-04)

Every somatic cell displays a surface marker hashing its Keyring Locus and a set of checksummed loci. The Sentinel does not learn pathogens; it maintains the **self-whitelist**, and anything failing it — mutated cell, bacterium, human virus — is marked for the phagocytic lymph grid. Hence "infectious disease eliminated," zero-latency tumour suppression, and the ability to carry human pathogens in fur and gut without infection. Costs (→ DOC-02B): transplants are rejected absolutely; the gut flora must be *licensed* (a curated, checksummed microbiome); and there is no immune memory to speak of — a novel self-mimicking agent would meet no defence at all. **The gestation licence (D-77):** the seed carries its own Keyring Locus, written at compile, so every fetal cell fails the gestating parent's self-checksum; the compile therefore issues a *licence* — the seed's identity hash whitelisted in the gestating parent's Sentinel for the term, the way the microbiome is licensed, and revoked at weaning. The hash is known only to the compile's parties, which is why **only a compile parent can gestate** (DOC-02B §3: "chosen, not determined" — chosen from among the parents). A licence that fails is the only miscarriage the Kin have, and it is named.

---

### 10. FAILURE MODES (closes G-09 in part)

| Condition | Mechanism | Presentation | Recovery |
| :--- | :--- | :--- | :--- |
| **The Silence** | Cluster presence is wired into the Cortical body-schema like proprioception (designed — it makes Clusters cohere), plus a designed homing watchdog. Total RF loss = deafferentation of the social sense. | 30 s unease → 5 min distress → 30 min panic, claustrophobia. | Any Hum ends it. Silence Chambers keep a $0.01\text{ W}$ beacon: L2 up, L4 quiet. |
| **Node death** | A mate's Hum stops; presence table times out in one frame; Cluster key must be re-derived without hir. | "Phantom node." Physiological grief; re-keying is felt as amputation. | Time; ritual re-keying; the Reading. |
| **Core loss** | Thoracic trauma to the posterior vault. | **Brain death** (D-13). No Deafened; no survivors of the Core. | None. The Reading, if the body is warm or frozen. |
| **The Stutter** | Cortical–Lattice phase-lock lost (fever, trauma, some Unbound implants). | Thought and mesh output desynchronise; Bursts garble; the Kin hears hirself late. | Sleep-web resync; sometimes permanent. |
| **Keyring compromise** | Copied key stream (tissue theft; an Unbound relay). | Impersonation on PUBLIC/CLUSTER; DEEP still safe. | Cluster re-keys; the individual cannot — hir key is hir cells. |
| **Over-clock** | Sustained $20\text{ W}$ beyond dissipation budget. | Core temperature rise; the DOC-01B tropical throttle is this loop. | Automatic throttle; ventral windows on a cold bulkhead. |
| **Data Rot** | §6C. **Cortical, not Lattice (D-104).** The associative web is rebuilt continuously onto live material; the record never degrades, retrieval stays exact, the index never fills. | The old answer anything precisely and volunteer nothing: **not forgetful, unprompted.** Hard handles work forever; nothing outside the last ~175 years ever arrives on its own; the old affect is **gone, not faint** — hir may re-judge any day and may never re-feel one. **A steady state, not a decline.** | None, and none is needed — nothing is broken. Other Kin supply *the knowledge that something is there*; a re-feeler supplies **hir own** feeling in place of one that is gone; the centennial Defrag buys re-anchoring, not feeling. |
| **Interrogation** (D-87) | The Silence (thirty minutes to panic) or a drug on the Cortical Brain — the whitelist clears cells, not molecules. | A Kin will say anything hir cortex can voice, and hir Core answers hir honestly; but **the cortex is the read head** (D-102), so archive content cannot be *dumped* — it must be **read, at $\approx52\times$ and no faster**: 27.8 min for a day with no handle to aim at. A life does not fit through the head — a year is 7.05 days of it, a Written's life about ten and a half years, so **a drugged Kin yields one day verbatim, not a life.** Nothing reaches DEEP. **And what hir yields comes out cold (D-103):** the lived read needs a willing cortex and a drug on the Cortical Brain is not one, so an operator takes the facts and can never take the person. **The cap is the mercy and the cruelty both: hir cannot be emptied, and hir cannot refuse to be read out loud, a day at a time, in front of the one doing it.** | The Cluster, an hour of tails — and the memory of it, verbatim, forever. The Compact court uses neither; operators have used both (DOC-12 §4). |

---

### 11. TERMINOLOGY & ERRATA RAISED BY THIS DOCUMENT

1. **Vacuum torpor** (State B, unconscious, 3 W — DOC-01E.2) ≠ **transit torpor** (DOC-07 arks: Cortical asleep, Core at 2–8 W in virtualities). DOC-07 → "transit torpor."
2. "Zero-latency" (DOC-09) → "sub-20 ms."
3. "256-bit encrypted" → "keyed spread-spectrum, 256-bit key entropy" in technical docs; vignettes may keep the shorthand.
4. "Simulate millions of genetic variants" (DOC-02) → "search millions of module combinations."
5. **DOC-02 §2, DOC-07 §2, DOC-08 §3:** strike "Ancestral Mesh Vaults" / "Archive Pilgrimage" / "curating the ship's Vault" → the Weave, the Carrying, carried memory. Weavers = carriers, not vault-keepers.
6. **DOC-08 §4:** the Unbound's defining heresy is externalised memory.
7. **DOC-07 §2:** the Anchor Cluster's duties include Readings for deaths in transit — five awake Kin carrying for a ship (flagged thin; see open items).
8. **DOC-06 §4:** "The Ancestral Vaults" anchor is closed by this document.

---

### 12. CANON VALUES TO LOCK & OPEN ITEMS

**Locked (D-20, §6 superseded by D-97…D-101, §6B/§6G/§6I/§7/§10 amended by D-103, §6 table/§6A/§6C/§6E/§6G/§6I/§10 amended by D-104; §6D struck and rewritten by D-105; §6E re-derived by D-106):** everything in §2's mass/power table; latencies (§2); keyring tiers and the pre-granted Reading key (§4); Hum/Burst/Link/Reading rates and ranges (§4, §7); modular genome $sim 3{,}400$ modules and the compile stages (§5; four at D-20, five since D-71 added *tune*); **three-tier memory — cortex / record / index — with the index at $\sim 5\times10^{4}$ stubs, continuous commit, the live veto, and Data Rot as cueing-layer decay (§6)**; Reading yield $\sim 15$–$27\text{ MB}$ ≈ 10,000 stubs + 20 narrated days, 6 h window, 3 W donor current, 30–60 min shifts, **reader-limited not format-limited** (§7); **hard/soft transfer, the Telling as a full-rate transfer of the hard tier, the index as the real limit** (§6G, §7); carried/received distinction, Weavers as carriers-with-sacrifice, the documentation flaw **as an emergent cultural fact** (§8); whitelist immunity (§9).

**The window, for quick reference (D-104):** the live index holds $\sim 5\times10^{4}$ stubs and **cycles**; the associative web is cortical and rebuilds onto live material; the result is a **rolling self of ~150–200 years**, always the most recent. Hard handles never fail at any age. The old affect is gone and not faint. Data Rot is a **steady state**, identical at four hundred and at nine hundred. **Everything that fails in this species is the reader; nothing that fails is ever the book.**

**The two rates, for quick reference (D-103):** *cold* — $\sim12\text{ MB/s}$, $\approx52\times$ real time, seekable, affect off, a whole day = 27.8 min, a year = 7.05 days, a Written's life ≈ 10.6 years; *lived* — $1\times$ only, affect on, the sole source of soft content, and the only rate a corpse cannot run at all.

**Open (→ DOC-02B, DOC-07 v2, DOC-08 v2):**
- ~~Who may edit the reference genome, and where its master copy lives~~ — resolved (D-70, D-71): no one may; the ranges are the limit; sequence in every Genesis Module, annotation in every Weaver.
- Infant boot: when the private codec and Kin-code are trained; what the First Ping contains; the age DEEP tier becomes possible.
- Is five awake Kin per ark enough to carry a ship's dead through a century? (Suggest: transit-torpor sleepers can be woken for a Reading — cost to be specified.)
- The ethics of *receiving* from a dead ship's last Long Message — who decides to take it on.
