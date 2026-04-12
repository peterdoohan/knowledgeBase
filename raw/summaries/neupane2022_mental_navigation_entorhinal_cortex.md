---
source_file: neupane2022_mental_navigation_entorhinal_cortex.md
paper_id: neupane2022_mental_navigation_entorhinal_cortex
title: "Vector production via mental navigation in the entorhinal cortex"
authors:
  - "Sujaya Neupane"
  - "Ila Fiete"
  - "Mehrdad Jazayeri"
year: 2022
journal: "bioRxiv (preprint, posted December 15, 2022)"
paper_type: empirical
contribution_type: empirical
species:
  - macaque
  - monkey
tasks:
  - navigation_task
methods:
  - electrophysiology
  - computational_modeling
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - attractor_networks
  - tolman_eichenbaum_machine
keywords:
  - cognitive_map
  - mental_navigation
  - entorhinal_cortex
  - grid_cells
  - continuous_attractor_network
  - path_integration
  - hebbian_learning
  - landmark_reconstruction
  - temporal_periodicity
  - internal_landmark_replay
  - scalar_property_of_interval_timing
  - vector_production
  - vector
  - production
  - via
  - mental
  - navigation
  - entorhinal
  - cortex
key_citations:
  - tolman1948_cognitive_maps_rats
  - constantinescu2016_gridlike_conceptual_knowledge
  - whittington2020_tolman_eichenbaum_machine
  - burak2009_path_integration_grid_cells
---

### One-line summary

Entorhinal cortex neurons in monkeys generate endogenous periodic activity locked to the temporal structure of memorised landmarks during purely mental navigation, and a continuous attractor network model explains how this internal reconstruction of landmarks reduces behavioural variability.

---

### Background & motivation

A foundational prediction of cognitive map theory (O'Keefe & Nadel, 1978; Tolman, 1948) is that the brain can exploit learned spatial structure in the absence of sensory input to perform mental computations such as planning novel routes. While grid cells and place cells are well-established as the neural substrate of cognitive maps during externally-driven navigation, direct evidence for the endogenous recruitment of these representations during purely internal, landmark-guided navigation has been lacking. This paper addresses that gap by designing a task that requires animals to navigate a memorised sequence of landmarks without any sensory feedback, enabling a test of whether entorhinal cortex encodes the internal temporal structure of those landmarks.

---

### Methods

- **Subject population**: Two male rhesus macaques (M. mulatta), head-restrained, performing a joystick-based task.
- **Task design**:
  - *Navigate-to-Sample (NTS)*: Animals used a joystick to move a visible sequence of six equidistant landmarks to align the correct landmark with a fixation point. This phase trained animals on landmark structure and joystick speed.
  - *Mental Navigation (MNAV)*: Identical contingency but all landmarks were invisible during joystick movement (and only a single landmark was visible before the go cue). Animals had to produce the correct displacement vector from memory.
  - Generalisation test: 30 possible landmark pairs were split into 15 training and 15 held-out pairs; immediate generalisation to held-out pairs was used to distinguish model-based (structured) from model-free (lookup table) strategies.
- **Electrophysiology**: Extracellular recordings from posterior entorhinal cortex (EC) using 32- and 64-channel laminar probes across 32 sessions (monkey A: 614 units; monkey M: 864 units). Task-modulated neurons identified by periodicity or temporal distance tuning.
- **Neural analyses**:
  - Autocorrelogram-based periodicity index (PI) to detect activity bumps at the 0.65 s inter-landmark interval.
  - Phase analysis of local firing rate peaks relative to joystick offset.
  - Targeted dimensionality reduction (regression-based) to quantify population-level distance coding at joystick onset and offset.
  - Pairwise cross-correlations between simultaneously recorded periodic neurons to test for grid-cell-like attractor signatures.
- **Computational modelling**:
  - Continuous attractor network (CAN) of grid cells (adapted from Burak & Fiete, 2009) with multiple modules of different periodicities and phases.
  - Hebbian plasticity at grid-cell-to-landmark-neuron synapses to enable internal reconstruction of external landmarks.
  - Two Bayesian observer models of behaviour (with and without internal landmark resets) fit to produced vector distributions via maximum likelihood estimation.

---

### Key findings

- Animals showed immediate generalisation to held-out landmark pairs, indicating use of a structured, model-based representation rather than stimulus-response memorisation.
- 16% (monkey A) and 8.5% (monkey M) of EC neurons had significant periodic activity at 0.65 s during mental navigation — matching the temporal spacing of memorised landmarks — despite no external sensory input.
- Periodicity was significantly stronger during the mental navigation epoch than during the inter-trial interval (paired t-tests, p << 0.0001 for both animals and both directions).
- Periodic neurons showed lower PI on error trials than correct trials (p << 0.0001), linking periodicity to behavioural accuracy.
- The phase of firing rate bumps was systematically distributed at multiples of 0.65 s before joystick offset (KS test, p << 0.0001), consistent with structured temporal representation across the navigation epoch.
- Population-level distance coding at joystick offset was significantly stronger than at onset (Wilcoxon rank sum, Z = -7.21, p << 0.0001 for monkey A; Z = -6.82, p << 0.0001 for monkey M).
- Pairwise cross-correlations between periodic EC neurons were conserved across mental navigation and ITI epochs (monkey A: r(188) = 0.84, p << 0.0001; monkey M: r(292) = 0.86, p << 0.0001), consistent with continuous attractor dynamics.
- The CAN model with internal landmark reconstruction predicted sublinear growth of variability with distance (exponent < 1; one-tailed t-test(999) = -39.32, p << 0.0001), whereas the path-integration-only model predicted linear (scalar) growth.
- The reset model provided a significantly better fit to animals' behaviour than the no-reset model (paired t-test, monkey A: t(78) = 7.89, p << 0.0001; monkey M: t(102) = 16.35, p << 0.0001).

---

### Computational framework

**Continuous attractor networks (CAN) and Hebbian associative learning.**

The paper adopts the continuous attractor network model of grid cells (Burak & Fiete, 2009) as its core framework. In this formalism, a population of neurons with difference-of-Gaussian lateral connectivity forms a stable activity bump that moves through neural state space in response to velocity input, thereby implementing path integration. The key variables are: (i) the phase and periodicity of the network's activity pattern, (ii) velocity input (here assumed to be efference copy or reafference from joystick deflection), and (iii) external or internal landmark inputs that can anchor or reset the bump.

The model is extended with Hebbian (Oja's rule) plasticity at synapses from grid cell modules to a hypothetical landmark neuron. During learning with visible landmarks (NTS), this plasticity selectively strengthens inputs from the subset of grid cells whose periodicity and phase match the external input. After learning, when landmarks are absent (MNAV), the grid cell drive alone can reconstruct the landmark neuron's activity, effectively inserting internally generated "resets" into the path integration dynamics at the correct temporal intervals. The assumption is that each internal landmark transiently stabilises the active bump, making it less responsive to velocity input, thereby dividing long navigation intervals into shorter, more precise segments and producing sublinear scaling of variability with distance.

---

### Prevailing model of the system under study

The paper's introduction situates itself within a long-standing framework in which the hippocampal-entorhinal system encodes cognitive maps of both spatial and non-spatial variables. The accepted view at the time of the study is that grid cells in medial entorhinal cortex implement path integration via continuous attractor dynamics, generating periodic spatial firing patterns driven by sensory velocity inputs during active or virtual navigation. There is also established evidence that the hippocampal-entorhinal system can encode non-spatial relational structures (temporal sequences, value spaces, abstract conceptual relationships). However, the prevailing view has been that these structured representations are evoked by exogenous sensory inputs; whether the same representations can be recruited entirely endogenously, without sensory scaffolding, during purely mental computation, had not been directly demonstrated in neural recordings. The introduction thus frames the paper as a test of the original cognitive map hypothesis (Tolman; O'Keefe & Nadel) in its strongest form: that maps are available for internal mental navigation.

---

### What this paper contributes

The central new contribution is direct neural evidence that entorhinal cortex can generate the temporal structure of a learned landmark sequence internally, without any external sensory input. Before this paper, the grid cell machinery had been documented to encode spatial and non-spatial variables when those variables were externally cued; this paper shows that the same system can endogenously reconstruct temporal landmarks during purely mental navigation, evidenced by periodic firing locked to the 0.65 s inter-landmark interval. The conservation of pairwise cross-correlations across navigation and ITI epochs provides evidence that this periodicity reflects the same continuous attractor dynamics seen in rodent grid cells, rather than a distinct mechanism. The modelling work adds a mechanistic account: Hebbian learning at grid-cell-to-landmark synapses can explain how the system learns to reconstruct landmark inputs, and the resulting landmark-induced resets make a specific, quantitatively testable prediction — sublinear variability scaling — that is confirmed in the animals' behaviour. This prediction is non-trivial because it distinguishes mental navigation (with structured internal landmarks) from pure temporal estimation (without them), and the Bayesian model comparison confirms this distinction. Collectively, the paper moves the cognitive map theory from a conceptual postulate to a neurally grounded, algorithmically specified mechanism for endogenous mental computation.

---

### Brain regions & systems

- **Entorhinal cortex (EC), posterior subdivision** — primary recording site; proposed locus of endogenous periodic activity corresponding to memorised landmark structure during mental navigation. Task-modulated neurons concentrated in a small posterior EC region in both animals.
- **Hippocampus** — referenced as part of the broader hippocampal-entorhinal circuit encoding cognitive maps; not directly recorded but implicated through its known connectivity with EC and its established role in encoding temporal sequences and relational structure.
- **Grid cell system (medial entorhinal cortex)** — the recorded EC neurons are argued to be functionally homologous to rodent grid cells, based on their periodic firing, conservation of pairwise correlations, and consistency with continuous attractor dynamics.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight: it formalises an algorithm (continuous attractor path integration with internal landmark resets via Hebbian learning) and provides neural data (periodic EC firing with conserved cross-correlation structure, linked to behaviour) that support that algorithm over alternatives.

**Computational level**: The brain solves the problem of producing accurate displacement vectors in the absence of sensory feedback by segmenting long intervals into shorter, more precisely timed sub-intervals bounded by internally reconstructed landmarks. This reduces cumulative timing variability below the scalar (Weber's law) prediction.

**Algorithmic level**: A continuous attractor network performs path integration by shifting an activity bump in proportion to velocity input. Hebbian plasticity at grid-cell-to-landmark-neuron synapses encodes the phase and periodicity of experienced landmarks. During subsequent mental navigation without external input, the learned grid cell drive reconstructs landmark neuron activity at the appropriate temporal phases, producing transient "resets" that stabilise the bump and reduce velocity-driven drift. Temporal distance is encoded both at navigation onset (weakly, in initial population state) and at offset (robustly, as a ramp signal), providing both initialisation and ongoing tracking signals.

**Implementational level**: Partially addressed. Recordings are from posterior entorhinal cortex in macaques; the periodic neurons show cross-correlation invariance consistent with continuous attractor dynamics known from rodent grid cells. The paper notes that velocity input is likely efference copy or reafference from joystick deflection (rather than external sensory flow), requiring gain calibration of the attractor landscape. Specific cell types, neuromodulators, and the anatomical source of the velocity signal are not directly identified; the paper discusses Hebbian (Oja's rule) plasticity as the assumed synaptic mechanism, while acknowledging that other plasticity mechanisms in EC-hippocampus (e.g., behavioural time-scale plasticity) might be better biological candidates.

---

### Limitations & open questions

- The velocity input driving path integration during MNAV is assumed to be efference copy or reafference from the joystick, but its neural source within or upstream of EC is not identified.
- Specific cell types mediating the periodic activity and the identity of putative "landmark neurons" are not characterised; the LM neuron in the model is hypothetical.
- The biological basis of the Hebbian plasticity between grid cells and landmark neurons remains untested; the paper flags this as an open experimental question.
- The model predicts that changed joystick speeds should require gain adjustment of the internal velocity input — testable but not done in the current design (no visual flow feedback was provided).
- The degree to which the recorded EC neurons are strictly homologous to rodent grid cells (vs. a functionally analogous but distinct population) is left unresolved; the paper notes there are differences, including the presence of ramping neurons and the internally generated nature of velocity input.
- The model predicts that irregular landmark spacings could be encoded by a weighted sum of multiple grid modules — untested.
- The experiment was conducted in macaques; generalisability to human mental navigation and to the role of the hippocampus (not recorded) in this process is speculative.
- The paper is a preprint (bioRxiv, 2022) and had not undergone peer review at the time of posting.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — *The Hippocampus as a Cognitive Map* (foundational cognitive map theory)
- Tolman (1948) — cognitive maps in rats and men (original postulate)
- Hafting et al. (2005) — discovery of grid cells in entorhinal cortex
- Burak & Fiete (2009) — continuous attractor network model of grid cells used directly for modelling
- Yoon et al. (2013); Trettel et al. (2019); Gardner et al. (2019) — conservation of pairwise correlations in grid cells as evidence of attractor dynamics
- Constantinescu et al. (2016) — grid-like codes for abstract conceptual spaces in humans
- Whittington et al. (2020) — Tolman-Eichenbaum Machine, unifying space and relational memory
- Killian et al. (2012) — grid-like spatial map in primate entorhinal cortex
- Jazayeri & Shadlen (2010) — Bayesian temporal calibration model used in behavioural fitting

**Named models or frameworks**:
- Mental Navigation task (MNAV) — custom task paradigm
- Navigate-to-Sample task (NTS) — training paradigm
- Continuous attractor network (CAN) model of grid cells (Burak & Fiete, 2009)
- Periodicity index (PI) — adapted from gridness score in spatial navigation
- Bayesian observer model of interval timing (reset vs. no-reset variants)
- Targeted dimensionality reduction (Mante et al., 2013)
- Oja's rule (Hebbian plasticity)

**Brain regions**:
- Entorhinal cortex (EC), posterior subdivision
- Hippocampus (referenced, not recorded)
- Medial entorhinal cortex (MEC) (in referenced rodent literature)

**Keywords**:
- cognitive map, mental navigation, entorhinal cortex, grid cells, continuous attractor network, path integration, Hebbian learning, landmark reconstruction, temporal periodicity, internal landmark replay, scalar property of interval timing, vector production
