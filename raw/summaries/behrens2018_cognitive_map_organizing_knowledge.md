---
source_file: behrens2018_cognitive_map_organizing_knowledge.md
paper_id: behrens2018_cognitive_map_organizing_knowledge
title: "What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior"
authors:
  - "Timothy E.J. Behrens"
  - "Timothy H. Muller"
  - "James C.R. Whittington"
  - "Shirley Mark"
  - "Alon B. Baram"
  - "Kimberly L. Stachenfeld"
  - "Zeb Kurth-Nelson"
year: 2018
journal: Neuron
paper_type: review
contribution_type: theoretical
species:
  - human
methods:
  - fmri
  - lesion
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - lateral_entorhinal_cortex
  - prefrontal_cortex
  - orbitofrontal_cortex
frameworks:
  - reinforcement_learning
  - model_based_rl
  - successor_representation
keywords:
  - cognitive_map
  - place_cells
  - grid_cells
  - successor_representation
  - transition_structure
  - factorised_representations
  - meta_reinforcement_learning
  - structural_abstraction
  - transitive_inference
  - relational_knowledge
  - entorhinal_cortex
  - flexible_generalisation
  - what
  - cognitive
  - map
  - organizing
  - knowledge
  - flexible
  - behavior
key_citations:
  - tolman1948_cognitive_maps_rats
  - stachenfeld2017_hippocampus_predictive_map
  - dordek2016_grid_cells_pca
  - constantinescu2016_gridlike_conceptual_knowledge
  - garvert2017_relational_knowledge_maps
  - wilson2014_best_practices_scientific
  - dayan1993_successor_representation
wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
  - wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_hidden_task_state
---

### One-line summary

Spatial representations in the hippocampal-entorhinal system (place cells, grid cells) are instances of general-purpose coding mechanisms that organise abstract relational knowledge across all domains by learning and storing the transition structure of task state spaces.

---

### Background & motivation

Tolman originally conceived the cognitive map as a domain-general organisation of knowledge that supports flexible inference, but the concept has been dominated by spatial neuroscience ever since O'Keefe and Nadel localised it to the hippocampal-entorhinal system. Meanwhile, computational accounts of behaviour (reinforcement learning, decision-making) successfully model narrow, repetitive tasks but cannot account for the rapid generalisation, transitive inference, and imagination that characterise human cognition. Recent discoveries of grid-like coding for non-spatial conceptual dimensions and parallels between OFC/vPFC lesion effects and RL state-space deficits have reopened the question of whether spatial representations are special or are instances of something more general. This review synthesises these threads to propose a unified framework.

---

### Methods

This is a narrative review and theoretical perspective.

- Scope covers spatial navigation neuroscience (place cells, grid cells, boundary vector cells, object vector cells), reinforcement learning theory (successor representation, eigenvector decomposition, model-based RL), prefrontal lesion studies, non-spatial analogues of hippocampal/entorhinal coding, meta-learning in artificial neural networks, and implications for flexible human cognition.
- Synthesis method is theoretical and narrative: empirical findings are organised around the RL framework (states, transitions, successor representations) and used to motivate a unified computational account of cognitive maps across spatial and non-spatial domains.
- Key computational constructs introduced or reviewed: transition matrix T and its eigenvectors, successor representation (SR), factorised vs. conjunctive codes, meta-reinforcement learning (meta-RL), basis set representations of transition structure.

---

### Key findings

- OFC/vPFC lesions impair credit assignment and the use of latent state structure (learning set), paralleling the computational role of state-space representations in RL — providing empirical grounding for the analogy between OFC and entorhinal function.
- Grid cells can be derived as the eigenvectors of the transition matrix T of 2D space, or equivalently as the principal components of place cell activity; this makes them an efficient basis for representing all future state distributions from any current location, enabling vector navigation without step-by-step simulation.
- The successor representation (SR) of place cells — predicting expected future state occupancy rather than current location — accounts for policy-dependent place-field distortions (field stretching toward track start on 1-way tracks; clustering near reward).
- Grid-like (hexagonally symmetric) fMRI activity is observed in entorhinal cortex and ventral frontal cortex during navigation through a 2D *conceptual* space defined by bird morphology dimensions (Constantinescu et al., 2016), not just physical space.
- Hippocampal cells exhibit place-field-like activity for sound frequencies in a non-spatial task (Aronov et al., 2017); entorhinal cells show multi-field, grid-like firing across the frequency dimension.
- fMRI similarity structure in hippocampus and entorhinal cortex respects the statistical transition graph of discrete, non-spatial state spaces even when subjects are unaware of the structure (Garvert et al., 2017).
- A factorised neural network trained to predict sensory events during 2D random walks develops periodic (grid-like) structural units and conjunctive (place-like, remapping) units, reproducing key properties of the entorhinal-hippocampal system from first principles (Whittington et al., 2018).
- Meta-RL (Wang et al., 2018) proposes that dopamine-driven weight updates implement slow meta-learning of task structure across episodes, while fast within-episode learning is handled by RNN activation dynamics — explaining how PFC units acquire task-variable tuning matching macaque PFC recordings.
- Transitive inference and sensory preconditioning both require hippocampus, entorhinal cortex, and vPFC, consistent with these regions providing explicit structural representations that generalise across sensory contexts.

---

### Computational framework

**Reinforcement learning / successor representation / eigenvector basis**

The paper's central organising framework is reinforcement learning cast in terms of state spaces and transition structure. The key quantities are:

- **States** s and a transition matrix T (or T(s'|s,a)), encoding the topology of the problem.
- **Successor representation** SR = (I − γT)⁻¹: the expected discounted future state occupancy given a starting state under the current policy. Place cells are proposed to encode SR rather than current location.
- **Eigenvectors of T**: for a 2D continuous space these are periodic and grid-like, providing a compact basis from which all n-step transition distributions T^n·s can be computed by linear combination, enabling efficient distance estimation without step-by-step planning.
- **Factorised representations**: P(r_sensory, r_structure) = P(r_sensory)·P(r_structure). Separating structural (relational) from sensory representations allows structural knowledge to generalise to entirely new sensory instantiations of a task.
- **Meta-RL**: a recurrent neural network whose synaptic weights are trained slowly by dopamine-driven RPE to encode common task structure across episodes; within-episode learning exploits activation dynamics rather than weight change.

The framework assumes that the brain is fundamentally solving a generalised RL problem across spatial and non-spatial domains, and that the hippocampal-entorhinal system implements efficient basis representations of transition structure while vPFC maintains latent state identity and multi-step plans.

---

### Prevailing model of the system under study

The paper frames the prevailing view as a two-part tension. On one side: the hippocampal-entorhinal system houses spatially specific representations (place cells, grid cells, head-direction cells, boundary vector cells) whose functional roles are largely understood within the 2D navigation problem. Grid cells specifically encode Euclidean metric structure and enable vector navigation; place cells provide location signals. On the other side: these same structures are implicated in generalisation, inference, imagination, social cognition, and memory — none of which are obviously spatial. The field lacked a unifying computational account that could explain why spatially structured representations appear during non-spatial tasks and why hippocampal/OFC lesions impair abstract relational inference. The OFC/vPFC was separately understood as representing latent task states and supporting credit assignment, but the deep connection between entorhinal grid coding and RL transition structure was not yet a consensus view.

---

### What this paper contributes

The review's core contribution is a unified theoretical framework linking spatial navigation, reinforcement learning, and flexible cognition through the concept of **transition structure representation**. Specifically, it establishes or consolidates:

1. **Spatial codes as special cases of general structural codes**: grid cells and place cells are not unique to space — they reflect the topology of whatever state space the animal is navigating, spatial or otherwise. The eigenvector/SR derivation makes this mathematically precise.
2. **A computational account of vPFC/OFC function**: OFC lesion deficits in credit assignment and learning set are predicted by removing explicit latent-state representations from an RL agent — connecting spatial navigation theory to prefrontal cognitive flexibility.
3. **Factorisation as the key property enabling generalisation**: separating structural from sensory representations in the entorhinal-hippocampal circuit (medial vs. lateral entorhinal cortex → hippocampus) is proposed as the mechanism by which structural knowledge transfers across tasks.
4. **A path to understanding human cognitive flexibility**: the framework extends to transitive inference, sensory preconditioning, imagination, and long-range planning as structural inference over explicitly represented relational bases, suggesting a research programme for non-spatial cognitive neuroscience.

---

### Brain regions & systems

- **Hippocampus** — encodes conjunctive representations of object-in-structure (place cells as SR); required for transitive inference, sensory preconditioning, imagination, relational memory; remaps between environments.
- **Medial entorhinal cortex (MEC)** — encodes structural/spatial representation independently of sensory content (grid cells, band cells, boundary vector cells, object vector cells); proposed to implement the basis set of transition structure; does not remap between environments (grid phases preserved).
- **Lateral entorhinal cortex (LEC)** — encodes sensory/object information devoid of structural context; factorised from MEC input before conjunction in hippocampus.
- **Ventral prefrontal cortex (vPFC) / orbitofrontal cortex (OFC)** — represents latent task states and causal structure; required for credit assignment and learning set; treated computationally as analogous to entorhinal cortex but for multi-step, goal-dependent, and latent-state problems; connected to hippocampus via fornix.
- **Perirhinal cortex (PER) / postrhinal/parahippocampal cortex (POR)** — mentioned as providing sensory and spatial context inputs to hippocampus in the factorised circuit framework.

---

### Mechanistic insight

The paper does not itself present new neural recordings or imaging data. However, it synthesises neural evidence (place cell SR distortions, grid-like fMRI in conceptual space, OFC lesion effects, transitive inference hippocampal dependence) and links each to a specific algorithmic claim (SR encoding, eigenvector basis, latent-state RL, factorised code). This approaches but does not fully meet the bar:

The paper proposes a specific algorithm (SR/eigenvector basis in entorhinal cortex; factorised structural code; meta-RL in PFC) and marshals neural data — including place-field skewing consistent with SR predictions (Stachenfeld et al., 2017), non-spatial grid-like fMRI (Constantinescu et al., 2016; Aronov et al., 2017; Garvert et al., 2017), OFC lesion pattern fitting RL state-space deficits (Wilson et al., 2014), and PFC unit tuning matching meta-RL predictions (Wang et al., 2018) — that support these algorithms over simpler alternatives (pure current-location coding, associative chaining). At Marr's levels:

- **Computational**: the brain solves a generalised problem of predicting future state distributions across spatial and non-spatial domains; it must do so efficiently and in a manner that generalises to new tasks.
- **Algorithmic**: MEC encodes the eigenvectors (or SR basis) of transition structure in a factorised code separated from sensory content; hippocampus forms conjunctive codes binding structure to sensory events; vPFC maintains latent state and multi-step structural plans; meta-RL in PFC/dopamine circuitry implements slow learning of cross-task structure.
- **Implementational**: partial — grid cell attractor dynamics (Burak and Fiete, 2009), dorsoventral gradient of grid scale (Brun et al., 2008), and medial vs. lateral entorhinal anatomical segregation are noted as implementational signatures, but a detailed circuit-level account is not provided.

The review does not meet the full "mechanistic insight" bar because the neural evidence is drawn from many different studies with different paradigms, and no single study simultaneously presents the algorithm and neural data specifically supporting it over alternatives within the same experiment.

---

### Limitations & open questions

- The framework is largely theoretical/speculative in its extension beyond 2D spatial coding; direct experimental evidence for grid-like coding of abstract non-spatial relational structures beyond 2D continuous conceptual spaces remains sparse.
- The paper treats vPFC and entorhinal representations as computationally interchangeable for expository convenience, but important differences (latent state specificity, multi-step planning, goal-dependent representations) are acknowledged and not fully resolved.
- How much of the structural bias (e.g., preference for 2D, ordinal, or hierarchical structure) is hard-coded by evolution versus learned through early experience is explicitly left open.
- The eigenvector/SR framework handles continuous and discrete spaces of moderate scale, but its scaling to the high-dimensional, compositional nature of human conceptual knowledge is speculative.
- The link between meta-RL and biological dopaminergic learning is suggestive but the timescale mismatch between dopamine-driven synaptic plasticity and rapid within-task learning is acknowledged without full resolution.
- The paper raises but does not resolve how structural bases are selected or weighted when encountering genuinely novel task domains with no obvious analogue in prior experience.

---

### Connections & keywords

**Key citations**:
- Tolman (1948) — original cognitive map concept
- O'Keefe and Nadel (1978) — hippocampal spatial mapping
- Hafting et al. (2005) — discovery of grid cells
- Stachenfeld et al. (2017) — hippocampus as successor representation
- Dordek et al. (2016) — grid cells as eigenvectors of place cell covariance
- Banino et al. (2018) — grid-like units in deep RL agent for vector navigation
- Constantinescu et al. (2016) — grid-like coding for conceptual space in humans (fMRI)
- Aronov et al. (2017) — place/grid coding for sound frequency in rodents
- Garvert et al. (2017) — map of abstract relational knowledge in human hippocampal-entorhinal cortex
- Wang et al. (2018) — meta-reinforcement learning in prefrontal RNN
- Wilson et al. (2014) — OFC lesions as latent-state RL deficit
- Walton et al. (2010) — OFC lesion credit assignment deficit in macaques
- Harlow (1949) — learning set in primates
- Dusek and Eichenbaum (1997) — hippocampal dependence of transitive inference
- Whittington et al. (2018) — factorised neural network producing grid and place cell properties
- Dayan (1993) — successor representation

**Named models or frameworks**:
- Successor representation (SR)
- Eigenvector basis of transition matrix
- Meta-reinforcement learning (meta-RL)
- Factorised representations (structural vs. sensory)
- Cognitive map (Tolman)
- Learning set (Harlow)
- Model-based reinforcement learning

**Brain regions**:
- Hippocampus
- Medial entorhinal cortex (MEC)
- Lateral entorhinal cortex (LEC)
- Ventral prefrontal cortex (vPFC) / orbitofrontal cortex (OFC)
- Perirhinal cortex (PER)
- Postrhinal/parahippocampal cortex (POR)

**Keywords**: cognitive map, place cells, grid cells, successor representation, transition structure, factorised representations, meta-reinforcement learning, structural abstraction, transitive inference, relational knowledge, entorhinal cortex, flexible generalisation

### Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
- [[wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_hidden_task_state|Orbitofrontal cortex as a cognitive map of hidden task state]]
