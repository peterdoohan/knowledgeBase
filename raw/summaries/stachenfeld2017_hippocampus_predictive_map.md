---
source_file: "stachenfeld2017_hippocampus_predictive_map.md"
paper_id: "stachenfeld2017_hippocampus_predictive_map"
title: "The hippocampus as a predictive map"
authors: "Kimberly L Stachenfeld, Matthew M Botvinick, Samuel J Gershman"
year: 2017
journal: "Nature Neuroscience"
paper_type: "computational"
contribution_type: "theoretical"
tasks: ["morris_water_maze"]
methods: ["fmri"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "medial_entorhinal_cortex", "medial_temporal_lobe"]
frameworks: ["reinforcement_learning", "model_free_rl", "successor_representation", "temporal_difference_learning"]
keywords: ["successor_representation", "place_cells", "grid_cells", "hippocampus", "entorhinal_cortex", "reinforcement_learning", "cognitive_map", "predictive_coding", "temporal_difference_learning", "model_based_vs_model_free", "spectral_graph_theory", "eigendecomposition", "hierarchical_planning", "subgoal_discovery", "reward_sensitivity", "remapping", "policy_dependence", "backward_skewing", "community_structure", "spatiotemporal_coding"]
---

### One-line summary
The hippocampus encodes a successor representation (SR) — a predictive map of future state occupancy — that unifies place cell response properties under a reinforcement learning framework, while entorhinal grid cells encode a low-dimensional eigendecomposition of that representation.

### Background & motivation
Hippocampal place cells have classically been interpreted as encoding a geometric cognitive map of space. However, several empirical phenomena are difficult to reconcile with a purely spatial, Euclidean account: place fields skew with directional travel, distort around barriers, cluster near reward locations, and show policy dependence. A principled computational account of why the hippocampus represents space the way it does — one that also explains nonspatial and entorhinal grid cell phenomena — was lacking.

### Methods
This is a theoretical/computational paper. The authors formalize the successor representation (SR) from reinforcement learning theory and apply it to hippocampal and entorhinal data. Simulations were run by discretizing spatial environments into triangular lattices and computing SR matrices analytically or via TD-learning updates. SR eigenvectors were derived and compared to recorded grid cell firing fields. The model was validated against multiple published experimental datasets covering: directed linear tracks (Mehta et al., 2000), Tolman detour maze remapping (Alvernhe et al., 2011), annular water maze reward clustering (Hollup et al., 2001), nonspatial community structure in fMRI (Schapiro et al., 2016), spatiotemporal navigation with teleportation (Deuker et al., 2016), geometric effects on grid fields (Krupic et al., 2015), hairpin maze grid fragmentation (Derdikman et al., 2009), and multi-compartment grid evolution (Carpenter et al., 2015).

### Key findings
1. SR place fields naturally reproduce backward skewing on directed linear tracks, obstacle-respecting distortion in barrier mazes, and clustering near reward locations — without ad hoc assumptions.
2. The SR applied to nonspatial graph-structured stimuli reproduces the community-structure similarity effect observed in human hippocampal fMRI.
3. Eigenvectors of the SR matrix simulate entorhinal grid cell firing fields in multiple geometric environments (square, trapezoid, hexagon, circle, hairpin, multi-compartment), matching boundary-dependent orientation effects and field fragmentation.
4. A gradient of discount factors along the hippocampal longitudinal axis provides a multi-timescale predictive representation, consistent with known place field scale gradients.
5. SR eigenvectors support subgoal discovery by identifying topological bottleneck states near doorways and decision points, relevant to hierarchical planning.
6. Low-dimensional spectral reconstruction of the SR (via grid cell eigenvectors) acts as regularization, stabilizing noisy SR updates during learning.

### Computational framework
The core construct is the successor representation M(s, s'), defined as the expected discounted future occupancy of state s' when starting from state s under a given policy: M(s, s') = E[sum_t gamma^t * I(s_t = s') | s_0 = s]. Value is then V(s) = M(s,:) * R, decomposing expected reward into a predictive state component and a reward component. The SR can be incrementally learned via temporal difference updates. Grid cells are modeled as the eigenvectors of M; the eigendecomposition provides a low-dimensional basis set enabling spectral regularization and subgoal discovery via graph spectral theory.

### Prevailing model of the system under study
The dominant prior view held that hippocampal place cells encode a geometric (Euclidean or geodesic) map of spatial location, serving as input to model-based or model-free RL systems. Grid cells were thought to implement a Euclidean metric for dead reckoning. These accounts struggled to explain policy dependence, directional skewing, and reward sensitivity of place fields, and the boundary-dependence of grid fields.

### What this paper contributes
The paper proposes and formalizes the predictive map theory: place cells encode the SR (predictions of discounted future state occupancy), not current location per se. This is a theoretical unification that explains a large and diverse body of empirical findings under a single framework. The novel contribution is applying SR theory comprehensively to hippocampus and entorhinal cortex, and specifically proposing that grid cells encode eigenvectors of the SR matrix — providing a normative account of why grid cells exist and why they take the form they do.

### Brain regions & systems
- Hippocampus (CA1, CA3): encodes the successor representation as a population rate code; place cells are SR-encoding neurons
- Medial entorhinal cortex (MEC): encodes eigenvectors of the SR matrix; grid cells are low-dimensional bases for the predictive map
- Hippocampal longitudinal axis: gradient of discount factor gamma, corresponding to multi-scale temporal prediction
- Medial temporal lobe broadly: connected to episodic memory via the temporal context model

### Mechanistic insight
Place field skewing emerges because the SR captures discounted future occupancy: states preceding an encoded location (predicting it) also activate the corresponding SR cell, producing backward-skewed fields. Barrier-induced remapping is local and policy-dependent because the SR respects transitions — states on opposite sides of a barrier are temporally distant regardless of Euclidean proximity. Reward sensitivity arises from lingering near reward, increasing expected occupancy of nearby and preceding states. Grid cell boundary sensitivity arises because environmental geometry shapes the underlying transition structure, which shapes the eigenvectors of the SR.

### Limitations & open questions
- The SR predicts larger place fields near reward, but Hollup et al. found field sizes approximately equal at reward vs. non-reward locations — the SR is an incomplete account of reward-dependent place fields.
- SR eigenvectors in rectangular environments tend to produce non-isotropic grid scales (different horizontal/vertical); biological grid cells are approximately isotropic. Additional constraints (e.g., non-negativity, orthogonality relaxation as in Dordek et al.) are likely needed.
- The model is trained on the current policy; when reward changes, the value function requires refinement as the agent adapts. Policy-independence of value recomputation is only partial.
- The SR cannot fully replace model-based forward planning (theta sweeps, sharp-wave ripples); it is offered as a complementary mechanism.
- The account of multi-compartment grid evolution involves assumptions about how the SR is initialized and how eigenvectors converge with experience.

### Connections & keywords
successor representation; place cells; grid cells; hippocampus; entorhinal cortex; reinforcement learning; cognitive map; predictive coding; temporal difference learning; model-based vs model-free; spectral graph theory; eigendecomposition; hierarchical planning; subgoal discovery; reward sensitivity; remapping; policy dependence; backward skewing; community structure; spatiotemporal coding; context pre-exposure; Dayan 1993; Tolman; O'Keefe
