---
source_file: momennejad2020_successor_representations_replay.md
title: "Learning Structures: Predictive Representations, Replay, and Generalization"
authors: Ida Momennejad
year: 2020
journal: Current Opinion in Behavioral Sciences
paper_type: review
contribution_type: review
---

### One-line summary

This review argues that the successor representation (SR) — a count-based, predictive RL algorithm updated through offline replay — provides a neurally plausible and computationally efficient account of how the brain learns, generalises, and plans using cognitive maps.

---

### Background & motivation

A century of research on cognitive maps has established that the brain encodes rich relational structures of environments, but classical spatial theories (Euclidean, hippocampus-centric) fail to explain non-spatial place fields, path-dependent representations, or the flexible generalization seen in mammals. Model-free RL is too rigid and model-based RL is computationally intractable at realistic scales. The paper asks: what representational and learning mechanism can be both biologically plausible and computationally efficient enough to underpin flexible cognition?

---

### Methods

This is a narrative review covering computational theory and empirical evidence across the following areas:

- Successor representation (SR) theory: mathematical formulation, comparison to model-free and model-based RL, and its equivalence to the inverse graph Laplacian
- Empirical studies testing SR predictions in human behaviour (retrospective revaluation tasks) and neural data (rodent electrophysiology, human fMRI)
- Replay-based learning algorithms: Dyna-Q, Dyna-Q+, prioritized sweeping, and SR-Dyna
- Extensions: multi-scale SR, successor features, options/eigen-options, and intrinsic motivation
- Computational psychiatry applications

---

### Key findings

- SR outperforms model-free, model-based, Dyna-Q, and hybrid algorithms in capturing human retrospective revaluation behaviour (both reward and transition revaluation).
- SR columns simulate hippocampal place fields; eigendecomposition of the SR matrix simulates entorhinal grid fields (Stachenfeld et al., 2017).
- Multi-scale SR (with varying discount parameters) accounts for the anterior-posterior gradient of predictive horizon along the hippocampal long axis and into prefrontal cortex (PFC).
- Policy-dependent SR — learned via TD during goal-directed experience — over-represents states on reward trajectories, explaining goal-skewed place fields and the attraction of grid fields to reward locations.
- Prioritized replay (by unsigned prediction errors) drives revaluation behaviour: larger prediction errors are followed by more offline hippocampal replay of predecessor states, which in turn predicts future revaluation (human fMRI).
- Eigendecomposition of SR yields basis sets (eigen-options, proto-value functions) that support hierarchical planning, option discovery, and intrinsic motivation without extrinsic rewards.
- SR-Dyna accounts for latent learning and inference of unseen state relationships via offline stitching of distal experiences.

---

### Computational framework

The paper's central framework is the **successor representation** (SR) within **reinforcement learning**.

- **Core formalism**: SR is an n×n matrix M where entry M(s, s') encodes the expected discounted future number of visits to state s' when starting from state s. It is learned via temporal difference (TD) updates using successor prediction errors (analogous to reward prediction errors in model-free RL, but tracking visitation counts). The discount parameter γ (0 < γ < 1) determines the predictive horizon.
- **Key variables**: M (SR matrix), γ (discount/scale), α (learning rate), successor prediction error (onehot(s_new) + γM(s_new) − M(s)).
- **Mathematical properties**: SR approximates the inverse of the graph Laplacian; its eigenvectors tile state spaces and enable spectral clustering, subgoal discovery, and abstraction. Multi-scale ensembles are mathematically equivalent to Laplace transforms of future trajectories.
- **Core assumption**: The brain encodes not one-step transitions but expected multi-step visitation counts, updated both online during experience and offline via replay (SR-Dyna).
- Related frameworks discussed: Dyna architectures, hierarchical RL (options, eigen-options), successor features for transfer, and intrinsic motivation via Laplacian eigenmaps/proto-value functions.

---

### Prevailing model of the system under study

The paper pushes against two prior frameworks: (1) early cognitive map theory (O'Keefe & Nadel, 1978) positing that hippocampal maps are spatial, allocentric, and Euclidean; and (2) the standard model-free/model-based RL dichotomy. The prevailing view assumed place cells encode current location in a metric spatial map, grid cells provide a Euclidean coordinate system, and offline replay passively replays recent experience. Cognitive flexibility was attributed to model-based RL at high computational cost.

---

### What this paper contributes

The review consolidates and organises a body of computational and empirical evidence around a single principled account: SR as the brain's representational currency for cognitive maps. It establishes that:

1. SR resolves the MF/MB tradeoff by providing MB-level flexibility at near-MF computational cost.
2. SR predicts and explains non-Euclidean, path-dependent, policy-dependent, and goal-skewed neural representations that contradict classical spatial map theory.
3. SR updated via prioritized replay explains inference of unseen relations and revaluation behaviour, with direct fMRI support.
4. Eigendecomposition of SR unifies place fields (SR columns), grid fields (SR eigenvectors), and hierarchical planning (eigen-options) under one mathematical framework.

Key unresolved questions: how SR handles causal inference; which structures or graphs are learnable by current SR algorithms and how these compare to human structure learning limits; and how hippocampal and cortical replay interact mechanistically.

---

### Brain regions & systems

- **Hippocampus (posterior/dorsal)** — proposed locus of fine-grained, short-horizon SR; place cell firing simulated by SR columns; sharp-wave ripples as the neural substrate of replay
- **Hippocampus (anterior/ventral)** — proposed locus of longer predictive horizons in multi-scale SR; larger place fields consistent with larger discount γ
- **Entorhinal cortex** — grid fields proposed to encode eigendecomposition of SR, providing a low-dimensional basis set for the state space; grid fields attracted to reward locations consistent with policy-dependent SR
- **Prefrontal cortex (PFC, including OFC/Brodmann areas 10/11)** — proposed to represent the largest predictive horizons and generalised schema; engaged during offline replay correlated with revaluation behaviour
- **Medial temporal lobe (general)** — pattern similarity in fMRI shown to match SR-predicted similarity structure across statistical learning and relational concept tasks

---

### Mechanistic insight

The paper does not meet the full bar: it synthesises existing work rather than presenting a single new empirical dataset, and thus does not provide new neural recordings that directly pit SR against alternative algorithms at the level of neural mechanisms.

However, the review assembles compelling circumstantial evidence across Marr's levels:

- **Computational**: The brain solves the problem of flexible, efficient planning by precomputing multi-step state relationships as discounted visitation expectations, enabling rapid value computation at decision time.
- **Algorithmic**: SR is learned via TD-based successor prediction errors, updated both online and via prioritized offline replay; eigendecomposition yields basis sets for abstraction and transfer.
- **Implementational**: Place cells are proposed to encode SR columns (current state's row of M), grid cells to encode SR eigenvectors, sharp-wave ripples to implement replay updates, and the hippocampal anterior-posterior axis to represent the scale gradient of SR. The review does not address specific cell types, neuromodulators, or biophysical mechanisms for SR learning.

---

### Limitations & open questions

- SR as classically formulated assumes discrete states; extension to continuous feature spaces requires successor features, which introduce additional complexity.
- Policy-dependence predictions (e.g., differences between random-walk and goal-directed grid fields) remain incompletely tested experimentally.
- The relationship between SR and causal inference is unresolved.
- Limits of human structure learning relative to SR algorithm capacity are unknown.
- Interaction between hippocampal and cortical replay, and the role of neural oscillations (ripples, theta) in prioritization, remains to be mechanistically specified.
- Computational psychiatry applications (e.g., anxiety modelled as maladaptive replay prioritization) are speculative and require empirical validation.
- Replay modelling choices (memory buffer length, sequential vs. random order) are underspecified relative to biological constraints.

---

### Connections & keywords

**Key citations**:
- Dayan (1993) — original successor representation proposal
- Stachenfeld, Botvinick, Gershman (2017) — hippocampus as a predictive map
- Momennejad, Russek et al. (2017, Nat Hum Behav) — SR in human RL behaviour
- Russek, Momennejad et al. (2017, PLoS Comput Biol) — SR-Dyna: predictive representations link MB to MF
- Momennejad, Otto, Daw, Norman (2018, eLife) — offline replay and planning in human fMRI
- Momennejad & Howard (2018, bioRxiv) — multi-scale SR and Laplace transform equivalence
- Brunec & Momennejad (2019, bioRxiv) — predictive horizons along hippocampal-PFC hierarchy
- Sutton & Barto (2018) — RL: An Introduction (Dyna framework)
- Machado et al. (2017) — eigen-options via deep SR

**Named models or frameworks**:
- Successor Representation (SR)
- SR-Dyna
- Dyna-Q / Dyna-Q+
- Prioritized sweeping
- Multi-scale Successor Representations (MSR)
- Successor features
- Options framework / Hierarchical RL
- Eigen-options
- Proto-value functions
- Laplacian eigenmaps

**Brain regions**:
- Hippocampus (posterior and anterior)
- Entorhinal cortex
- Prefrontal cortex (including orbitofrontal cortex, Brodmann areas 10/11)
- Medial temporal lobe

**Keywords**:
- successor representation
- cognitive maps
- reinforcement learning
- hippocampal replay
- prioritized sweeping
- multi-scale predictive representations
- policy-dependent place fields
- grid cells eigendecomposition
- temporal difference learning
- hierarchical reinforcement learning
- eigen-options
- structure learning
