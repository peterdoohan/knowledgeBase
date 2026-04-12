---
source_file: basu2021_ofc_navigation_goals.md
paper_id: basu2021_ofc_navigation_goals
title: "The orbitofrontal cortex maps future navigational goals"
authors:
  - "Raunak Basu"
  - "Robert Gebauer"
  - "Tim Herfurth"
  - "Simon Kolb"
  - "Zahra Golipour"
  - "Tatjana Tchumatchenko"
  - "Hiroshi T. Ito"
year: 2021
journal: Nature
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - optogenetics
  - tetrode_recording
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - orbitofrontal_cortex
keywords:
  - orbitofrontal_cortex
  - navigational_goal_coding
  - persistent_goal_representation
  - dynamic_population_coding
  - orthogonal_subspace
  - lda_decoding
  - linear_dynamic_model
  - goal_directed_navigation
  - optogenetic_perturbation
  - spatial_working_memory
  - destination_specific_ensemble_dynamics
  - tetrode_recording
  - orbitofrontal
  - cortex
  - maps
  - future
  - navigational
  - goals
key_citations:
  - brown2016_prospective_goals_hippocampus
---

### One-line summary

Neurons in the rat orbitofrontal cortex (OFC) persistently encode the animal's future navigational destination throughout a journey, forming an internal goal map that is causally necessary for accurate navigation.

---

### Background & motivation

Accurate navigation to a goal requires the brain to maintain a representation of the target destination throughout the journey, not just the current position. While hippocampal place cells and grid cells represent current position and nearby trajectories, their role in encoding the specific future destination has been questioned — hippocampal sequential activity encodes nearby positions rather than a precise distal goal. It was therefore unclear which brain region, if any, maintains an accurate, persistent representation of a chosen navigational target. This paper addresses the gap by asking whether the OFC — a region implicated in goal-directed choice and spatial impairments upon lesion — provides such a goal map.

---

### Methods

- **Subjects**: 4 male Long-Evans rats implanted with tetrodes in ventral/lateral OFC; 18 recording sessions; 68–328 simultaneously recorded OFC neurons per session.
- **Task**: 2-m linear maze with 10 water-delivery wells; rats alternated between two active wells to obtain reward (requiring licking above a threshold duration); after six consecutive correct trials, the rewarded well pair changed, enforcing goal updating.
- **Neural recordings**: Tetrode recordings sorted with Kilosort; single units with firing rate ≥ 0.5 Hz retained.
- **Decoding analyses**: Linear discriminant analysis (LDA) decoders trained to classify current well (from licking epoch) and goal well (from combined motion-onset and lick-onset epochs); leave-two-out cross-validation; chance levels assessed against five null hypotheses (shuffled labels, running direction, speed, acceleration, trajectory distance).
- **Dimensionality reduction**: PCA for visualising population trajectories; LDA-based dimensionality reduction at individual time points to extract goal-selective axes; Isomap for visualising goal separation.
- **Linear dynamic model**: First-order regularised linear model fitted to neural trajectories from motion onset; used to simulate trajectories and test whether goal identity is encoded orthogonally to dynamics.
- **Causal perturbation**: Pharmacogenetic silencing (DREADD) and optogenetic activation (bReaCh-ES) of bilateral OFC in separate cohorts; 40-s or 6-s laser pulses timed to motion onset or lick onset; error rates measured before, during, and after perturbation.

---

### Key findings

- 80.8% of OFC neurons (2,366/2,927) showed spatial tuning on the maze; of these, 86.9% showed conjunctive coding of position and navigation phase, with firing predominantly near the goal well.
- An LDA decoder trained on licking-epoch activity successfully decoded the current (goal) well from 1.7 s before to 6 s after lick onset; decoding of run-over (non-goal) wells was significantly lower (P = 1.96 × 10⁻⁴, Wilcoxon).
- Goal well representation emerged ~1.1 s before motion onset and was maintained throughout the entire journey; current well representation decayed ~0.7 s before motion onset.
- Goal coding was viewpoint-invariant: well identity was decoded regardless of approach direction or starting well.
- In error trials, OFC population activity decoded the animal's incorrect destination as accurately as the correct goal in correct trials, indicating the OFC represents the animal's chosen (not correct) goal.
- The axis of maximal goal-well separability (LDA dimension) was nearly orthogonal to the direction of neural trajectory evolution, indicating goal identity is encoded independently of dynamic evolution.
- A regularised first-order linear dynamic model seeded at motion onset reproduced both correct and error trial trajectories and their associated goal decoding, supporting deterministic dynamics from motion onset.
- Optogenetic perturbation at motion onset (6-s pulses) increased navigational errors significantly (P = 0.020); perturbation at lick onset produced smaller, less significant effects (P = 0.008), with errors recovering in the immediately following trial.
- Pharmacogenetic OFC silencing also significantly increased error rates.

---

### Computational framework

The paper uses a **population coding / dynamical systems** framework. The key insight is that goal identity is encoded in a subspace of the high-dimensional neural state space that is orthogonal to the subspace in which trajectory dynamics evolve. This is formalised by:

1. **LDA-based dimensionality reduction**: at each time point of navigation, LDA identifies the low-dimensional axis that maximally separates goal-well-specific population activity. The angular difference between this axis and the instantaneous velocity vector of neural trajectories is measured to quantify orthogonality.
2. **Linear dynamic model**: A regularised first-order model of the form X_dot = AX (with regularised A obtained by least-squares) captures the global structure of neural trajectories. The model is seeded with the population state at motion onset and propagates forward, reproducing goal-selective dynamics — implying that the goal code is set at journey onset and the dynamics then unfold deterministically.

Key variables: neural population activity vector, goal well identity (class label), navigation phase (positional fraction of journey). Key assumption: goal identity is a stable, low-dimensional attribute of the population state that does not require continuous sensory feedback.

---

### Prevailing model of the system under study

Prior to this paper, the hippocampal formation was the dominant candidate for goal-directed spatial coding. Place cells encode current position; hippocampal theta sequences and sharp-wave ripple replay encode nearby past and future trajectories. Some studies suggested hippocampal activity is modulated by instructed future destinations in humans, but this was confounded with cue encoding. The OFC was known to contribute to goal-directed behaviour through value and choice history coding, and lesions of ventromedial prefrontal cortex (including OFC) impair accurate spatial targeting in humans and rodents. The OFC was also known to show activity modulation during goal-directed motion and navigational planning. However, no study had shown that OFC neurons form spatially precise, persistent representations of a chosen distal goal throughout a self-initiated journey — independent of ongoing sensory input — or that this representation is causally necessary for navigation.

---

### What this paper contributes

This paper establishes the OFC as a component of the brain's internal goal map. It demonstrates that OFC neurons encode the precise spatial identity of the animal's chosen destination (not just a non-specific goal signal or value signal) from before motion onset through the entire journey, without representing intermediate positions along the route. This updates the field by: (1) distinguishing OFC goal coding from hippocampal trajectory coding — the OFC encodes the endpoint, not the path; (2) showing the goal representation is causal, not merely correlated, since brief perturbation at navigation onset produces errors; (3) providing a mechanistic account — orthogonal coding — of how a stable goal identity can be maintained despite changing neural dynamics during navigation; (4) demonstrating that the goal code tracks the animal's chosen (including incorrect) destination, linking it to decision rather than reward history.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC), ventral and lateral parts** — primary focus; shown to encode the spatial identity of the navigational goal persistently throughout navigation; causal perturbation confirms a necessary role in accurate destination selection.
- **Hippocampus (CA1)** — used as a comparison region; OFC neurons conveyed significantly lower spatial information than CA1 neurons in an open-field random foraging task, confirming OFC is not a general spatial map but specifically activated in goal-directed contexts.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight.

**Phenomenon**: The brain maintains a persistent, accurate representation of a chosen distal navigational goal throughout a journey, in the absence of direct sensory access to that goal.

**Computational level**: The brain must solve the problem of goal-directed navigation — selecting a destination and holding it in mind across a variable-duration journey despite ongoing sensory input about current position. The OFC implements this by maintaining a stable goal identity signal that is resistant to sensory updating.

**Algorithmic level**: Goal identity is encoded in the neural population state as a low-dimensional attribute (a direction in activity space) that is orthogonal to the axis along which trajectory dynamics evolve. This orthogonal coding allows the goal signal to persist stably while the population trajectory evolves (reflecting position, navigation phase, and other covariates). A linear dynamic model seeded at motion onset propagates the state forward, implying the goal representation is set at journey onset and the dynamics encode the trajectory from start to goal. Decoding shows the transition from current-well to goal-well representation occurs ~1.1 s before motion onset, consistent with prospective goal selection.

**Implementational level**: The paper identifies the ventral and lateral OFC as the neural substrate (tetrode recordings, stereotaxically verified). Optogenetic activation of CamKII-positive neurons (excitatory, predominantly pyramidal) with bReaCh-ES disrupts goal coding; DREADD silencing of OFC produces similar errors. The paper does not resolve specific cell types, layer organisation, or input/output circuit mechanisms within OFC, nor the precise source of the goal signal (e.g., hippocampal or prefrontal inputs).

---

### Limitations & open questions

- The study uses a restricted 1D linear maze; it is unclear how OFC goal representations scale to 2D environments with more complex trajectories or multiple possible routes.
- The mechanism by which the goal representation is initially set at motion onset is unknown — what upstream circuit conveys the chosen destination to OFC?
- The paper does not address the relationship between OFC goal coding and value coding: does the same population encode both the identity and the value of the goal, and are these orthogonal?
- OFC recordings are unilateral; bilateral perturbation was used for causal experiments, leaving open whether lateralisation matters.
- The open-field foraging experiment suggests OFC does not function as a general spatial map, but the comparison is limited to a small number of CA1 neurons from one rat; the boundary between position coding and goal coding in OFC is not fully characterised.
- The paper does not resolve how goal representations are updated when the goal changes (transition between blocks), or what drives the abrupt transition from current-well to goal-well coding at motion onset.
- Only male rats were used.

---

### Connections & keywords

**Key citations**:
- Pfeiffer & Foster 2013 (Nature) — hippocampal place-cell sequences depict future paths
- Wikenheiser & Redish 2015 (Nat. Neurosci.) — hippocampal theta sequences reflect current goals
- Kay et al. 2020 (Cell) — questioning hippocampal goal destination coding
- Carey et al. 2019 (Nat. Neurosci.) — reward revaluation biases hippocampal replay
- Feierstein et al. 2006 (Neuron) — spatial goals in rat OFC (prior work)
- Wikenheiser et al. 2017 (Neuron) — ventral hippocampus and OFC encoding of task structure
- Ballesta et al. 2020 (Nature) — OFC value codes causally related to economic choices
- Machens et al. 2010 (J. Neurosci.) — orthogonal subspaces for 'what' and 'when' in PFC
- Elsayed et al. 2016 (Nat. Commun.) — reorganisation between preparatory and movement states in motor cortex
- Brown et al. 2016 (Science) — prospective representation of navigational goals in human hippocampus

**Named models or frameworks**:
- LDA-based goal decoder
- Orthogonal subspace coding (dynamic coding)
- Regularised first-order linear dynamic model
- bReaCh-ES optogenetic perturbation
- DREADD pharmacogenetic silencing

**Brain regions**:
- Orbitofrontal cortex (OFC), ventral and lateral
- Hippocampus CA1

**Keywords**:
- orbitofrontal cortex, navigational goal coding, persistent goal representation, dynamic population coding, orthogonal subspace, LDA decoding, linear dynamic model, goal-directed navigation, optogenetic perturbation, spatial working memory, destination-specific ensemble dynamics, tetrode recording
