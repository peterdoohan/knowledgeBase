---
source_file: "iyer2024_grid_cells_abstract_velocity.md"
paper_id: "iyer2024_grid_cells_abstract_velocity"
title: "Flexible mapping of abstract domains by grid cells via self-supervised extraction and projection of generalized velocity signals"
authors: "Abhiram Iyer, Sarthak Chandra, Sugandha Sharma, Ila Fiete"
year: 2024
journal: "NeurIPS 2024 (38th Conference on Neural Information Processing Systems)"
paper_type: "computational"
contribution_type: "theoretical"
brain_regions: ["entorhinal_cortex", "medial_entorhinal_cortex"]
frameworks: ["successor_representation", "attractor_networks", "tolman_eichenbaum_machine"]
keywords: ["grid_cells", "abstract_cognitive_maps", "self_supervised_learning", "velocity_extraction", "loop_closure_constraint", "continuous_attractor_networks", "path_integration", "cognitive_flexibility", "dimensionality_reduction", "non_spatial_representations", "transfer_learning", "manifold_learning", "flexible", "mapping", "abstract", "domains", "grid", "cells", "via", "self"]
key_citations: ["constantinescu2016_gridlike_conceptual_knowledge", "whittington2020_tolman_eichenbaum_machine", "stachenfeld2017_hippocampus_predictive_map"]
---

### One-line summary

A self-supervised neural network model shows how the brain can reuse grid cell circuits to map arbitrary abstract cognitive domains by first extracting a low-dimensional, state-independent velocity signal from high-dimensional sensory inputs.

---

### Background & motivation

Grid cells in the medial entorhinal cortex generate hexagonal spatial maps during navigation, but recent experiments show they also represent non-spatial abstract spaces (auditory frequency, visual features, conceptual dimensions). How the brain generalises its spatial mapping machinery to these heterogeneous abstract domains is unknown. Existing models (TEM, successor representation, CSCG) learn transition structures and state representations simultaneously, requiring expensive re-learning for each new domain and not guaranteeing preservation of cell-cell relationships across environments. This paper addresses the prerequisite computational challenge: extracting a self-consistent, low-dimensional velocity signal from high-dimensional, time-varying sensory inputs so that a pre-existing continuous attractor grid cell circuit can directly map any abstract domain.

---

### Methods

- **Model architecture**: Encoder-decoder network of multi-layer perceptrons (MLPs). The encoder maps pairs of consecutive high-dimensional input frames to a low-dimensional latent velocity; the decoder applies the estimated velocity to a state to predict the next unseen state.
- **Self-supervised loss functions**:
  - *Next-state prediction*: minimises MSE between predicted and true next frame, ensuring the velocity latent is decodable.
  - *Loop-closure*: requires estimated velocities along closed-loop trajectories to sum to zero; proven to constrain the encoder to be a linear function of true velocity, enforcing a global metric structure.
  - *Shortcut estimation* (auxiliary): tests generalisation by predicting states multiple steps ahead via velocity addition.
  - *Isotropy* (auxiliary): penalises variance in velocity norms for nearby states, promoting isotropic velocity representations.
- **Abstract cognitive domains tested**: 2D Stretchy Blob, 2D Stretchy Bird, 3D Stretchy Bird, 2D Moving Blobs, 1D Frequency Modulation — all procedurally generated with known ground-truth velocity distributions.
- **Validation**: (1) Mean squared error between model-inferred velocities and ground truth (after best-fit linear transformation); (2) velocity outputs fed into a synthetic continuous attractor grid cell model to assess whether hexagonal firing fields emerge; (3) comparisons against PCA, Isomap, UMAP, deep autoencoders, and MCNet.

---

### Key findings

- The model recovers low-dimensional velocity representations across all five abstract domains, with MSE errors of 0.02–0.07 (compared to 0.21–2.96 for all baselines), outperforming traditional dimensionality reduction and deep motion-prediction networks by 1–2 orders of magnitude.
- When the latent dimensionality exceeds the true data manifold dimensionality, the model automatically collapses its representations into a subspace matching the true dimensionality (>97% of variance in the correct number of PCs).
- Model-inferred velocities, when fed into a synthetic grid cell circuit, produce hexagonal tuning fields across all abstract domains, consistent with experimental observations of grid-like coding in non-spatial spaces.
- Ablation studies show that the loop-closure loss is essential for linear (metric) velocity representations and for hexagonal grid tuning; next-state prediction alone yields nonlinear representations and non-hexagonal fields.
- The model preserves cell-cell co-activity relationships across domains (a novel testable prediction), because the same continuous attractor network is reused with a shared velocity representation.
- Training does not require exclusively loop trajectories; 50% loops / 50% random walks yields comparable performance (error 0.035 vs 0.02 on loops only).

---

### Computational framework

**Self-supervised learning combined with continuous attractor dynamics.**

The core claim is that the brain can factor the cognitive mapping problem into two stages: (1) extract a state-independent, low-dimensional velocity from successive high-dimensional sensory inputs; (2) integrate that velocity using a pre-existing continuous attractor grid cell circuit to update grid phases and build a map.

Key variables: latent velocity vector v̂ (low-dimensional), input states i_t (high-dimensional images or signals), encoder f: (i_t, i_{t+1}) → v̂, decoder g: (i_t, v̂) → î_{t+1}.

Key constraints: (a) next-state decodability; (b) loop-closure — ∑v̂ = 0 along closed loops, proven to enforce linearity of the encoder with respect to true velocities, which is required for linear path integration by grid cells. The framework is entirely self-supervised — no labels, no assumed coordinate system, no known dimensionality.

The downstream integrator is modelled as a continuous attractor network (sum of three plane waves on a neuron lattice) whose state is updated by the incoming velocity estimates.

---

### Prevailing model of the system under study

Prior to this paper, the dominant framework for understanding how the brain maps abstract cognitive domains relied on models that *jointly* learn state representations and transition structures (TEM, successor representation, CSCG). These models treat each new environment as requiring fresh representation learning: the brain must build a dedicated set of stable states and transition operators for every explored domain. The introduction also assumes a baseline in which grid cells' spatial mapping role (via continuous attractor path integration) is understood as domain-specific — i.e., the same circuit would need to be re-adapted or replaced for non-spatial domains. The paper's framing takes as established background that (a) grid cells employ continuous attractor dynamics for path integration in space, and (b) grid cell co-activity patterns are preserved across different spatial environments and sleep states.

---

### What this paper contributes

The paper proposes a mechanistically distinct account: rather than re-learning state representations per domain, the brain extracts a universal, domain-agnostic velocity signal and projects it onto the *invariant, pre-structured* grid cell manifold. This allows the *same* continuous attractor circuit to map arbitrary abstract spaces without modification. Concretely:
- Establishes that self-supervised loop-closure is sufficient to enforce the metric linearity required by path integration, providing a plausible biological learning rule.
- Demonstrates computationally that a single architecture generalises across qualitatively different abstract domains (visual, auditory, featural) without retraining the grid cell circuit.
- Makes a novel, falsifiable prediction: grid cell co-activity patterns should be preserved *across* distinct abstract domains (not just across spatial environments), because the same attractor module performs integration in all of them.
- Identifies "abstract velocity extraction" as a prerequisite bottleneck that prior cognitive mapping models bypass through unrealistic assumptions (predefined discrete action spaces, domain-specific representation learning).

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — site of grid cells; the paper proposes MEC reuses its continuous attractor dynamics to map abstract domains by receiving low-dimensional velocity inputs extracted elsewhere.
- **Hippocampal-entorhinal circuit** — broader system implicated in cognitive mapping; referenced via experimental findings on non-spatial grid-like tuning (e.g., Aronov et al. 2017 on frequency space in rodents).
- The paper does not specify which brain region computes the upstream velocity extraction (the encoder); identifying this is listed as a future experimental challenge.

---

### Mechanistic insight

The paper does not meet the high bar: it proposes an algorithm (self-supervised velocity extraction + continuous attractor integration) and demonstrates that the algorithm works in simulation, but provides no neural data — no recordings, imaging, lesion, or pharmacology — specifically linking model variables to measured neural activity.

The paper is a computational modelling study. It makes testable predictions (preservation of cell-cell correlations across abstract domains; existence of a brain region generating abstract velocity signals) but does not yet validate these against neural data. The loop-closure loss is argued to be biologically plausible as a form of sensory prediction error combined with neural integration, but this alignment is speculative.

---

### Limitations & open questions

- **Auxiliary losses lack biological grounding**: the shortcut estimation and isotropy losses are computationally motivated but not well-supported by known neural mechanisms.
- **Euclidean velocity assumption**: the model assumes velocity vectors commute (Euclidean tangent space), preventing direct application to non-Euclidean spaces (e.g., hierarchical or spherical manifolds). The authors note these can be embedded in higher-dimensional Euclidean spaces as a workaround.
- **No identified neural substrate for velocity extraction**: the paper does not specify which brain region performs the encoder computation; this is flagged as a future experimental question.
- **Scaling to naturalistic environments**: all domains are procedurally generated with low-dimensional structure; whether the framework extends to high-dimensional naturalistic inputs remains untested.
- **Discrete or non-metric domains**: the model is restricted to continuously varying abstract spaces; discrete domains (like family trees) would require extension.
- **Cell-cell preservation prediction is untested**: the key novel empirical prediction (that grid cell co-activity is preserved across abstract domains) awaits experimental verification.

---

### Connections & keywords

- **Key citations**: Aronov, Nevers & Tank 2017 (grid cells in frequency space); Killian et al. 2012 (grid cells in visual space); Constantinescu et al. 2016 (gridlike conceptual knowledge in humans); Burak & Fiete 2009 (continuous attractor path integration); Whittington et al. 2020 (Tolman-Eichenbaum Machine); Stachenfeld et al. 2017 (hippocampus as predictive map); George et al. 2021 (clone-structured cognitive graphs); Dayan 1993 (successor representation); Klukas, Lewis & Fiete 2020 (grid cells for higher-dimensional variables); Gardner et al. 2021 (toroidal topology of grid cell population activity).
- **Named models or frameworks**: Tolman-Eichenbaum Machine (TEM); successor representation (SR); clone-structured cognitive graphs (CSCG); continuous attractor network model; MCNet (motion-content decomposition network); UMAP; Isomap; PCA.
- **Brain regions**: medial entorhinal cortex, hippocampal-entorhinal circuit.
- **Keywords**: grid cells, abstract cognitive maps, self-supervised learning, velocity extraction, loop-closure constraint, continuous attractor networks, path integration, cognitive flexibility, dimensionality reduction, non-spatial representations, transfer learning, manifold learning.
