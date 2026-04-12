---
source_file: "johnson2007_hippocampus_decision.md"
paper_id: "johnson2007_hippocampus_decision"
title: "Neural Ensembles in CA3 Transiently Encode Paths Forward of the Animal at a Decision Point"
authors: "Adam Johnson, A. David Redish"
year: 2007
journal: "The Journal of Neuroscience"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
tasks: ["t_maze"]
methods: ["electrophysiology", "tetrode_recording", "bayesian_decoding", "behavioral_analysis"]
brain_regions: ["hippocampus_ca3", "orbitofrontal_cortex", "striatum", "ventral_striatum", "nucleus_accumbens"]
keywords: ["neural", "ensembles", "ca3", "transiently", "encode", "paths", "forward", "animal", "decision", "point"]
key_citations: ["jackson2006_hippocampal_sharp_waves_reactivation", "daw2005_uncertainty_prefrontal_striatal"]
---

### One-line summary

CA3 hippocampal ensembles in rats transiently represent spatial locations ahead of the animal — sweeping forward along each potential path one at a time — during pauses at high-cost decision points, in a brain state characterised by theta and gamma oscillations rather than sharp-wave ripples.

---

### Background & motivation

The hippocampus is well established as a site for declarative and episodic memory, and place cells encode the animal's current location. However, declarative memory use — such as route planning — requires information to be retrieved and evaluated on timescales far shorter than minutes. Prior work had shown hippocampal replay during sharp-wave ripples (LIA state) and phase precession within theta cycles, but neither mechanism had been directly tied to prospective path planning at explicit choice points. The paper addresses whether hippocampal ensemble activity can represent potential future paths ahead of the animal during active decision-making, and whether this differs from known replay phenomena.

---

### Methods

- **Subjects**: Male Fisher–Brown–Norway hybrid rats (n = 3 animals for electrophysiology).
- **Tasks**: Two T-maze variants — (1) a multiple-T maze (four sequential choice points; reward side fixed within a session but changed daily) and (2) a cued-choice maze (single T; cue tone indicated rewarded arm each lap).
- **Recording**: 14-tetrode microdrives implanted targeting dorsal CA3 (AP −3.8 mm, ML 4.0 mm from bregma); 237 spike trains recorded across four sessions (33–72 cells per session). Spike sorting via MClust/KlustaKwik; LFPs sampled at 2 kHz.
- **Decoding**: Extended recursive Bayesian position decoding (Brown et al., 1998) with a spatiotemporal compression factor (4–8x) allowing the decoded representation to evolve faster than overt behaviour. No formal place field definition required; tuning curves estimated from full-session spiking.
- **Nonlocality measure**: Radial distance between decoded maximum a posteriori position and actual animal position.
- **Sweep identification**: Visual inspection of 20 ms reconstruction slices; sweeps defined as coherent non-local deviations >40 ms.
- **LFP analysis**: Cross-frequency correlation (Masimore et al., 2004) to detect theta, gamma, and sharp-wave ripple components; Watson's circular test for theta-phase relationships.
- **Behavioural analysis**: Linear velocity and angular orientation variability used to identify pausing and vicarious trial-and-error (VTE)-like behaviour.

---

### Key findings

- CA3 ensembles showed transient non-local representations ("forward sweeps") at the final choice point on both tasks, occurring at a rate of ~0.63 sweeps/s while at the choice point; sweeps lasted ~153 ms on average (close to one theta cycle at 7 Hz).
- Decoded representations swept preferentially **forward** of the animal (not behind); the probability mass in front significantly exceeded that behind in all sessions (sign-rank test, p < 10⁻¹⁰).
- Sweeps encoded each arm **separately** in sequence — the joint probability of representing both arms simultaneously was near zero, indicating the representation sampled one future path at a time.
- Similar forward sweeps were observed during **error correction** (when the rat reversed on the wrong arm), with the representation sweeping to the unchosen correct arm.
- LFPs at the choice point showed strong **theta (7 Hz) and gamma (30–80 Hz)** power but **no sharp-wave ripple** activity — contrasting with feeder sites, which showed replay during sharp-wave ripples.
- Sweep stop times aligned significantly to the rising phase of theta (Watson's U² = 0.52, p < 0.0001).
- On the **multiple-T task**, forward sweeps and time spent at the choice point decreased across laps as behaviour automated. On the **cued-choice task**, non-local activity was maintained throughout the session, consistent with continued moment-to-moment deliberation.
- Non-local representations were more prevalent during periods of high orientation variability (VTE-like behaviour) than during normal locomotion (Wilcoxon, p < 10⁻¹⁰).

---

### Computational framework

**Recursive Bayesian decoding / cognitive map framework.** The paper applies a Bayesian neural ensemble decoder to reconstruct the animal's represented position from instantaneous population activity. A key modification is the use of a spatiotemporal compression factor (n = 4–8×) applied to the transition kernel, allowing the decoded location to "move" much faster than the animal itself. This operationalises the idea that hippocampal representations can reflect cognitive states — possible future locations — rather than only tracking the animal's current physical position.

The broader theoretical framing is the **cognitive map / planning system** (O'Keefe & Nadel, 1978; Redish, 1999): the hippocampus is proposed to support flexible, model-based decision-making by representing prospective paths that downstream areas (e.g., orbitofrontal cortex, ventral striatum) can evaluate. The forward sweep is interpreted as the neural substrate of the planning computation — a sequential sampling of potential future trajectories for value assessment.

---

### Prevailing model of the system under study

At the time of publication, the dominant view was that hippocampal non-local representations occurred primarily during **sharp-wave ripples** in the LIA (non-theta) state, reflecting reactivation or reverse replay of recently experienced sequences (e.g., Foster & Wilson, 2006; Jackson et al., 2006). Place cells were understood to encode the animal's current position during active navigation (theta state), with phase precession providing a within-cycle forward shift from slightly behind to slightly ahead of the animal. Forward-looking activity had been proposed theoretically (Jensen & Lisman, 1998; Daw et al., 2005) and inferred from single-cell "prospective" firing, but direct ensemble-level evidence for discrete, path-selective prospective representations at choice points during active behaviour was lacking.

---

### What this paper contributes

The paper demonstrates that **forward sweeping representations exist as a distinct phenomenon from replay**: they occur during the theta/gamma state (not sharp-wave ripples), sweep selectively down each potential path in alternation, and are sensitive to task demands and learning. This shows that the hippocampus does not passively track position but engages an active prospective process specifically at high-cost decision moments. By showing that sweeps decrease as behaviour automates on the multiple-T task but persist on the cued-choice task, the paper links this mechanism to deliberative, flexible decision-making rather than habitual navigation. The results provide the first direct ensemble-level evidence linking hippocampal CA3 activity to a trajectory-planning process during ongoing behaviour, and distinguish this from both phase precession (smaller spatial extent, no discrete path selection) and LIA replay (different brain state).

---

### Brain regions & systems

- **Hippocampal CA3** — primary recording site; locus of non-local forward sweeps at decision points. The paper argues CA3 generates prospective representations that propagate downstream.
- **Hippocampal fissure** — reference electrode for theta LFP (7 Hz).
- **Orbitofrontal cortex** — discussed (not recorded) as a candidate downstream evaluator of hippocampal prospective signals, encoding value of potential choices.
- **Ventral striatum / nucleus accumbens** — discussed (not recorded) as a candidate downstream structure receiving hippocampal projections and encoding reward anticipation.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight. It presents an algorithm (forward sequential sweep of hippocampal spatial representations as a prospective planning mechanism) and provides neural data (ensemble recordings during specific behavioural states) that specifically support the forward-sweep algorithm over alternatives such as general phase precession or backward replay.

**Computational level**: The brain is solving a path-planning problem — evaluating the expected consequences of available choices before committing. This requires representing future states, not just the current state.

**Algorithmic level**: The hippocampal ensemble sequentially activates the spatial representation of each potential future path in alternation, each event lasting approximately one theta cycle (~150 ms). The representation is directionally coherent, forward-biased, and path-selective (one arm at a time, not both simultaneously). Decoding with a compressed temporal transition model reveals this sequence structure. The algorithm is proposed to feed prospective location estimates to downstream valuation circuits.

**Implementational level**: The sweeps occur in the **theta/gamma brain state** (not sharp-wave LIA), implicating theta-gamma coupling as the neural substrate. Sweep stop times phase-lock to the rising phase of theta. The data identify CA3 pyramidal ensembles as the cellular substrate. The paper notes that some sweeps outlast a single theta cycle, with theta appearing to transiently degrade during long sweeps, suggesting the sweep process and theta generation may share a common mechanism. **Bonus**: The paper explicitly links the cell-type/oscillation level (CA3 pyramidal cells firing extrafield during theta/gamma, not during sharp-wave ripples) to the computational function, providing implementation-level grounding.

---

### Limitations & open questions

- Ensembles were small (33–72 simultaneously recorded cells from 3 animals, 4 sessions); larger ensembles may reveal whether sweeps reach goal locations or terminate prematurely along the path.
- The paper cannot determine whether the hippocampal sweep drives choice behaviour or merely correlates with deliberation — downstream recording (orbitofrontal cortex, ventral striatum) during sweep events is needed.
- The relationship between the forward sweeps and phase precession is acknowledged but not fully resolved; the two phenomena may share a common theta-driven mechanism.
- The exact relationship between forward sweeps and overtly observable VTE behaviour was not formally quantified (VTE events were not explicitly scored, only approximated by angular orientation variability).
- Sweeps were identified by visual inspection, introducing potential observer bias, though sweep identification was stated to be blind to LFP data.
- It is unclear whether similar forward sweeps occur in CA1, subiculum, or entorhinal cortex, and how the signal propagates to downstream evaluative structures.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — cognitive map theory; hippocampus as spatial map
- Brown et al. (1998) — original recursive Bayesian decoding framework
- Foster & Wilson (2006) — reverse replay during awake sharp-wave ripples
- Jackson et al. (2006) — hippocampal sharp waves and reactivation
- Jensen & Lisman (1998, 2005) — theta-gamma model of hippocampal sequence encoding and planning
- Daw, Niv & Dayan (2005) — model-based vs. model-free competition; prefrontal role in planning
- Skaggs et al. (1996) — theta phase precession
- Redish (1999) — beyond the cognitive map; computational theory of hippocampal function
- Masimore et al. (2004) — cross-frequency correlation LFP method

**Named models or frameworks**:
- Recursive Bayesian decoding (with spatiotemporal compression)
- Cognitive map (O'Keefe & Nadel)
- Vicarious trial and error (VTE; Meunzinger, Tolman)
- Planning/prospective memory system (Daw et al.; Redish & Johnson)

**Brain regions**:
- Hippocampal CA3
- Orbitofrontal cortex (discussed)
- Ventral striatum / nucleus accumbens (discussed)

**Keywords**:
- hippocampal place cells
- forward sweep
- non-local representations
- Bayesian neural decoding
- CA3 ensemble activity
- vicarious trial and error
- theta oscillations
- gamma oscillations
- prospective memory
- spatial decision-making
- cognitive map
- trajectory planning
