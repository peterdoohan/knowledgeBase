---
source_file: nyberg2022_spatial_goal_coding.md
title: "Spatial goal coding in the hippocampal formation"
authors: Nils Nyberg, Éléonore Duvelle, Caswell Barry, Hugo J. Spiers
year: 2022
journal: Neuron
paper_type: review
contribution_type: review
---

### One-line summary

A comprehensive review of how the mammalian hippocampal formation represents goal locations across three phases of navigation — planning, travel, and arrival — integrating evidence from rodents, bats, and humans against predictions from computational models.

---

### Background & motivation

Goal-directed navigation requires not only a representation of current self-location but also internal representations of goal locations that can guide route planning and execution. While place cells, grid cells, head-direction cells, and boundary cells in the hippocampal formation (HF) are well-studied as substrates of cognitive maps, how goals themselves are encoded had remained underspecified. Multiple computational modelling traditions — model-free reinforcement learning, topological/successor-representation models, and vector-based grid-cell models — make distinct predictions about what goal codes should look like and where they should reside. The review fills the gap of synthesising a rapidly growing body of empirical evidence against these predictions and across navigation phases.

---

### Methods

This is a narrative review of the primary empirical and computational literature, structured around three functional phases of navigation:

- **Phase I (planning/initiation):** Evidence from hippocampal replay (rodent electrophysiology, human fMRI/single units) and allocentric goal-direction codes in EC/SUB.
- **Phase II (travel):** Theta sequences, splitter cells, goal-distance cells, goal-direction cells; rodent tetrode and calcium imaging studies, bat CA1 recordings (Sarel et al., 2017), and human fMRI studies.
- **Phase III (arrival):** Place-cell overrepresentation of goals; mEC grid-cell and non-grid-cell reorganisation; reverse replay; dopaminergic modulation via VTA and LC.
- Computational models reviewed include: goal-cell models, model-free RL/TD learning, successor representation (SR), and vector-based grid-cell frameworks.
- No formal inclusion/exclusion criteria are stated; coverage is representative rather than systematic.

---

### Key findings

- **Hippocampal replay** during rest/pauses can represent future goal-directed routes but does so reliably only under high mnemonic demand (e.g., freely navigating to a remembered goal, not on stereotyped tracks).
- **Non-preferred route replay** (replaying routes to be avoided, or previously rewarded but currently less-visited routes) also occurs, possibly supporting maintenance of flexible successor representations.
- **Theta sequences** in CA1/CA3 alternate between prospective route options during deliberation and preferentially represent the future correct route once the goal is well-learned; look-ahead distance scales with goal distance.
- **Splitter cells** in CA1, CA3, mEC, and SUB encode the current route identity rather than the goal identity per se; only a very small fraction (~0.5% of place cells) showed goal-specific (route-independent) firing.
- **Goal-distance cells** (~16% of CA1 principal cells in bats) encode path proximity to the goal; **goal-direction cells** (~19%) encode egocentric angle to the goal; ~5% conjunctively encode both.
- **Place-field overrepresentation** at goal locations occurs in CA1 (but not CA3) when trajectories are repeated AND the goal location must be memorised; it does not occur in flexible place-navigation tasks or when goals are visibly cued with no memory demand.
- **mEC grid fields** also overrepresent goals (more slowly than CA1 but more persistently, lasting to the next day); non-grid spatial cells in mEC form goal-proximal fields specifically in goal-directed contexts.
- Human fMRI: right EC/SUB activity decreases with Euclidean proximity to goal during travel; EC shows grid-like coding during imagined navigation; anterior SUB and anterior EC signal allocentric goal direction during planning.
- **Dopamine** (VTA→CA1 and LC→CA1) is required for place fields to shift toward goal locations; LC manipulation that induces/suppresses goal overrepresentation does not affect task performance, dissociating the map reorganisation from overt behaviour.

---

### Computational framework

The review evaluates three broad classes of computational model:

1. **Model-free / goal-cell models** (Burgess et al. 1994; Foster et al. 2000; Dayan 1991): place cells define states; TD learning assigns value (proportional to proximity to reward) across states. Predicts ramp-like firing approaching goals and gradient activity across the environment.

2. **Topological / successor representation (SR)** (Stachenfeld et al. 2017; Dayan 1993): the HPC encodes expected future state occupancy as the SR matrix. Place fields represent predictive maps, are distorted by environmental geometry, and cluster around frequently visited (including goal) locations. Replay in a Dyna-SR framework maintains policy-independent estimates of transitions.

3. **Vector-based / grid-cell models** (Bush et al. 2015; Banino et al. 2018; Erdem & Hasselmo 2012): grid cell modules provide a spatial metric enabling computation of Euclidean goal vectors. Deep-RL agents endowed with grid-like representations exhibit flexible navigation including novel shortcuts. Predicts cells tuned to allocentric goal direction and Euclidean goal distance.

Key model parameters across frameworks: current state (place/grid cell activity), goal state (stored via Hebbian learning or grid-phase comparison), value or SR vector, and a policy or action-selection mechanism (typically in striatum). Models differ on whether goal vectors are precomputed, searched sequentially (resembling replay), or read out from population activity.

---

### Prevailing model of the system under study

Before the findings reviewed here, the hippocampal formation was primarily understood as a system for representing current self-location via place cells (CA1, CA3, DG), grid cells (mEC), head-direction cells (PrS, PaS, mEC), and boundary cells (SUB, mEC). O'Keefe and Nadel's cognitive map theory held that these representations collectively form an allocentric map from which routes can be read out. The dominant view was that goal information entered this system mainly from outside (prefrontal cortex, striatum) and that the spatial cells themselves were principally place-coding devices. Computational models had long predicted that goal codes should exist within the HF, but the empirical evidence was sparse and fragmentary. The introduction makes clear that a working assumption was that HPC provides a map that is "read out" for downstream goal coding rather than itself representing goals dynamically.

---

### What this paper contributes

The review establishes that the HF is not a passive map but actively encodes goal-related information in multiple formats and at every phase of navigation:

- **Planning phase:** Replay can represent prospective goal-directed routes (not just past experience), and EC/SUB activity signals allocentric goal direction.
- **Travel phase:** A distributed population of HF neurons — goal-distance cells, goal-direction cells, splitter cells, theta-sequence look-ahead — continuously encodes goal-related spatial parameters; these are not merely artefacts of oversampled trajectories.
- **Arrival phase:** Goal-field overrepresentation in CA1 and grid-cell reorganisation in mEC reflect a learning signal tied to memory formation (not just reward), dissociable from overt behaviour.

The review clarifies that goal overrepresentation is neither universal nor functionally sufficient for performance; it depends on repeated trajectories AND memory demand, and causal manipulations of it do not change task performance. This narrows the plausible computational role to learning/memory consolidation rather than online guidance. The review also identifies that different navigation strategies (place, response, sequential-egocentric) and phases of navigation invoke different goal codes, which had not previously been synthesised into a coherent framework.

---

### Brain regions & systems

- **CA1 (dorsal)** — primary locus of place-cell overrepresentation of goals, goal-distance and goal-direction cells (bat), splitter cells, theta sequences, reverse replay; main region reviewed.
- **CA3** — provides input for replay via recurrent connectivity and sharp-wave generation; does not overrepresent goals in most tasks.
- **CA2** — provides input to replay fidelity; goal coding unknown.
- **Medial entorhinal cortex (mEC)** — grid cell and non-grid spatial cell reorganisation around goals; slower but more persistent than CA1; splitter cells; grid-cell replay coordinated with CA1.
- **Subiculum (SUB)** — goal proximity code (predicted by Redish & Touretzky 1998); allocentric goal direction coding in human anterior SUB; splitter cells; goal overrepresentation in some studies.
- **Presubiculum (PrS) / Parasubiculum (PaS)** — head-direction cell origin; not strongly implicated in goal coding here.
- **Dentate gyrus (DG)** — spatial cells present; limited direct evidence for goal coding.
- **Medial prefrontal cortex (mPFC)** — goal-field coding (Hok et al. 2005); top-down control of splitter cells and theta sequences; coordinates replay with HPC; final route decision locus.
- **Orbitofrontal cortex (OFC)** — proposed cognitive map of task space; goal-location representation.
- **Dorsolateral striatum (DLS)** — response/habitual navigation; actor in model-free RL.
- **Dorsomedial striatum (DMS)** — place navigation and SR-based learning; policy flexibility.
- **Ventral tegmental area (VTA)** — dopaminergic modulation of place-field plasticity and goal-related reactivation; part of HPC-VTA loop.
- **Locus coeruleus (LC)** — dopaminergic LC→CA1 projection induces goal-directed place-field shift; manipulation dissociates map reorganisation from behaviour.
- **Nucleus reuniens (NR)** — relay between mPFC and CA1; required for splitter activity.
- **Posterior parietal cortex (PPC)** — egocentric goal direction during planning and travel.

---

### Mechanistic insight

The paper meets the bar for a partial mechanistic account in some areas but not a complete one.

**Does it present an algorithm?** Yes — multiple computational frameworks are reviewed (SR, vector-based grid computation, TD/replay-based credit assignment) and mapped to empirical findings.

**Does it provide neural data specifically supporting an algorithm over alternatives?** Partially. The most mechanistically grounded case is goal-overrepresentation learning: (1) increased SWR/replay rate at rewarded goals correlates with STDP-mediated place-field shift toward goals (Dupret et al. 2010; Ambrose et al. 2016); (2) NMDA receptor blockade prevents post-learning persistence of overrepresentation but not its initial emergence; (3) LC→CA1 dopamine is necessary and sufficient for place-field shift toward goals, but not for task performance. This combination supports an algorithm in which dopaminergic neuromodulation gates STDP-driven plasticity of place cells encoding the goal location, implementing a form of temporal credit assignment.

Mapped to Marr's levels:
- **Computational:** The brain must assign credit to spatial representations near the goal to support future navigation efficiency; goals must be distinguishable from mere locations.
- **Algorithmic:** STDP between sequentially activated place/grid cells during replay propagates reward-predictive value backward along recent trajectories (reverse replay = eligibility trace); SR-like predictive coding may maintain a goal-influenced map.
- **Implementational:** SWR-triggered NMDA-dependent LTP between CA1/CA3 place cells; dopaminergic modulation via LC→CA1 (and VTA→CA1) controls the magnitude and direction of place-field plasticity; goal overrepresentation is CA1-specific (not CA3), implicating differences in intrinsic or afferent circuitry.

The mechanistic account is incomplete: the precise circuit for computing goal-distance and goal-direction codes (particularly in the bat and human) is not resolved, and the mechanism by which mEC grid fields reorganise more persistently than CA1 place fields remains speculative.

---

### Limitations & open questions

- **Strategy confounds:** Most animal studies do not fully control navigation strategy; goal codes may differ depending on whether animals use place, response, or sequential-egocentric strategies.
- **Trajectory overlap as a confound:** Goal overrepresentation correlates with repeated trajectories; it is unclear whether overrepresentation is driven by the goal per se or by path repetition triggering STDP.
- **Goal vs. reward dissociation:** Very few studies separate the goal location from the reward site; the extent to which findings reflect goal coding versus reward-related processes (value, expectation, receipt) is underspecified.
- **Species and recording differences:** Goal-distance and goal-direction cells described in bats (Sarel et al. 2017) have not been replicated in rodents performing equivalent tasks; VR head-fixed mice may show different HPC correlates than freely moving animals.
- **Anterior vs. posterior HPC:** Conflicting reports of whether fMRI activity in human HPC increases or decreases with goal proximity; likely task-dependent but the driving factors are not understood.
- **Multi-region dynamics:** Most recordings are single-region; the circuit mechanisms by which goal codes are transformed across EC→HPC→SUB→mPFC remain largely unknown.
- **Scale of representation:** Goal codes may be distributed across ensemble patterns not captured by single-unit tuning curves; population-level representations may have been missed.
- **Non-goal-overrepresentation in place navigation:** Why place cells do not overrepresent goals in flexible place-navigation tasks (continuous novel route finding) while they do in repeated-route tasks is not fully resolved.
- **mEC grid persistence:** The mechanism by which mEC grid-field overrepresentation outlasts CA1 overrepresentation by at least one day is unknown.

---

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) — cognitive map theory
- Hafting et al. (2005) — grid cells in mEC
- Dupret et al. (2010) — place-field accumulation at goals; NMDA-dependent memory
- Pfeiffer & Foster (2013) — goal-directed replay in open field
- Stachenfeld et al. (2017) — hippocampus as predictive map / successor representation
- Banino et al. (2018) — deep RL with grid-like representations for navigation
- Sarel et al. (2017) — goal-distance and goal-direction cells in bat CA1
- Boccara et al. (2019) — mEC grid-cell goal overrepresentation
- Butler et al. (2019) — non-grid mEC spatial cells at goals
- Kaufman et al. (2020) — LC→CA1 dopamine controls place-field shift, not performance
- Bush et al. (2015) — grid-cell vector computation for goal navigation

**Named models or frameworks:**
- Cognitive map (O'Keefe & Nadel)
- Successor representation (SR; Dayan 1993; Stachenfeld et al. 2017)
- Temporal difference (TD) learning
- Dyna architecture (Sutton 1991)
- Goal-cell model (Burgess et al. 1994)
- Vector-based grid-cell navigation (Bush et al. 2015; Erdem & Hasselmo 2012)
- Deep reinforcement learning navigation agent (Banino et al. 2018)
- Morris water maze; open-field goal navigation; W-maze alternation; VR navigation tasks

**Brain regions:**
CA1, CA3, CA2, dentate gyrus, medial entorhinal cortex (mEC), lateral entorhinal cortex (lEC), subiculum (SUB), presubiculum (PrS), parasubiculum (PaS), medial prefrontal cortex (mPFC), orbitofrontal cortex (OFC), dorsolateral striatum (DLS), dorsomedial striatum (DMS), ventral tegmental area (VTA), locus coeruleus (LC), nucleus reuniens (NR), posterior parietal cortex (PPC), lateral septum (LS)

**Keywords:**
- spatial goal coding
- hippocampal formation
- place cells
- grid cells
- hippocampal replay
- successor representation
- goal-directed navigation
- theta sequences
- goal-distance cells
- goal-direction cells
- place-field overrepresentation
- cognitive map
