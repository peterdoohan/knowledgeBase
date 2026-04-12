---
source_file: "piray2025_compositional_cognitive_map.md"
paper_id: "piray2025_compositional_cognitive_map"
title: "Reconciling flexibility and efficiency: medial entorhinal cortex represents a compositional cognitive map"
authors: "Payam Piray, Nathaniel D. Daw"
year: 2025
journal: "Nature Communications"
paper_type: "computational"
contribution_type: "theoretical"
tasks: ["navigation_task"]
methods: ["computational_modeling"]
brain_regions: ["hippocampus", "entorhinal_cortex", "medial_entorhinal_cortex", "prefrontal_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl", "successor_representation", "attractor_networks", "tolman_eichenbaum_machine", "compositionality"]
keywords: ["reconciling", "flexibility", "efficiency", "medial", "entorhinal", "cortex", "represents", "compositional", "cognitive", "map"]
key_citations: ["stachenfeld2017_hippocampus_predictive_map", "whittington2020_tolman_eichenbaum_machine", "dordek2016_grid_cells_pca", "piray2021_linear_reinforcement_planning"]
---

### One-line summary

A computational model proposes that the medial entorhinal cortex encodes compositional predictive maps through translation- and rotation-invariant object representations, reconciling flexibility and efficiency in cognitive map construction and planning.

### Background & motivation

Cognitive maps enable flexible goal-directed behavior such as planning novel routes and taking shortcuts. A key feature of flexible representations is compositionality—the ability to build complex structures by recombining simpler components. However, compositionality has been difficult to reconcile with efficient planning, as reusing components may limit efficiency. Previous models of cognitive maps based on reinforcement learning (e.g., successor representations) require recomputing the entire map when environments change, and predict global remapping of grid cells inconsistent with empirical data.

### Methods

- **Computational framework**: Extended linear RL theory (Default Representation; DR) to incorporate compositionality
- **Key innovation**: Predictive Object Representations (PORs)—compact, translation- and rotation-invariant matrices representing objects as perturbations to open space
- **Mathematical approach**: Used Woodbury matrix identity to efficiently compute compositional predictive maps by adding low-rank correction terms to baseline open-space map
- **Learning algorithm**: Developed iterative update rule for learning combined PORs for multiple objects, operating in object-space rather than full state-space
- **Neural simulations**: 
  - Simulated object vector cells as rows of projected POR matrices
  - Simulated grid cells using non-negative PCA of open-space DR (Dordek et al. framework), with perturbations from PORs projected onto eigenbasis
- **Planning simulations**: Compared compositional model against random walk, successor representation (SR), and complete (converged) models in multi-object navigation tasks

### Key findings

- **Compositional map construction**: The model enables efficient construction of predictive maps by combining PORs for individual objects, with complexity scaling with object size (O³) rather than environment size (S³)
- **Planning performance**: The compositional model performed comparably to the complete (ground-truth) planner (relative path length 1.09 with updates, 1.76 without) and substantially outperformed random walk and SR models
- **Object vector cell properties**: The model successfully accounts for:
  - Translation invariance: PORs maintain consistent response when objects are moved
  - Rotation invariance: PORs maintain consistent response across object orientations
  - Field size dependence on object diameter
  - Generalization across different objects with similar geometry
  - Generalization to multi-object environments
  - Emergence without experience (experience-independent)
- **Grid cell predictions**: The model predicts local (not global) remapping when barriers/objects are introduced, consistent with empirical data:
  - Wall removal (Wernle et al.): Local reorganization near former partition, preserved patterns near distal walls
  - Home cage introduction (Sanguinetti-Scheck & Brecht): Local shift near home, global stability elsewhere
  - Goals (Boccara et al.): Grid fields move closer to goals, reduced hexagonal pattern locally
  - Hairpin maze (Derdikman et al.): Alternating patterns across arms, fragmentation at turning points
- **Efficiency**: The learning algorithm operates in object-space (not state-space), making it computationally tractable compared to SR learning

### Computational framework

**Linear Reinforcement Learning (Linear RL) / Default Representation (DR)**

The paper extends the linear RL framework (also known as the Default Representation), which provides a closed-form solution for optimal value computation by introducing a default policy and control costs. The key mathematical object is the DR matrix D, defined as D = (diag(exp(c)) - T)⁻¹, where T is the one-step transition matrix under a uniform random walk policy and c is a per-state cost vector.

The DR captures, for each state, which other states will be visited in the long run under the default policy, discounted by cumulative costs. This enables efficient planning via simple matrix-vector multiplication rather than iterative computation.

**Predictive Object Representations (PORs)**

The paper's key innovation is the Predictive Object Representation (POR), a compact matrix Aₒ that captures how an object perturbs the baseline open-space predictive map. Using the Woodbury matrix identity, the DR for an environment containing an object can be computed as:

D = Dₒₛ + DₒₛCₒAₒRₒDₒₛ

where Dₒₛ is the open-space DR, and Cₒ and Rₒ are simple lookup matrices encoding states adjacent to the object. The POR Aₒ is translation- and rotation-invariant, depending only on the object's geometry, not its position or orientation.

**Compositional construction**

For multiple objects, the DR can be approximated by summing projected PORs:

D ≈ Dₒₛ + Dₒₛ[C₁ C₂][A₁ ⊕ A₂][R₁ R₂]ᵀDₒₛ

This provides a first-order approximation that improves as object separation increases, and can be refined via an efficient learning algorithm operating in object-space rather than state-space.

### Prevailing model of the system under study

The prevailing understanding of cognitive maps in the medial entorhinal cortex (MEC) includes several key theoretical proposals:

1. **Successor Representation (SR) account**: Stachenfeld et al. proposed that grid cells encode eigenvectors of the Successor Representation, a predictive map of expected state occupancy under a given policy. This provided a computational interpretation of grid cells as basis functions for spatial prediction.

2. **Tolman-Eichenbaum Machine (TEM)**: Whittington et al. proposed that MEC represents abstract relational structure through generalization of graph connectivity motifs, learned via backpropagation across environments.

3. **Metric theories**: Traditional accounts view grid cells as encoding metric spatial information through continuous attractor networks, providing a distance metric for path integration.

However, these models face significant challenges. The SR model predicts global remapping of grid cells when barriers or goals are introduced (since eigenvectors change dramatically with map modifications), which contradicts empirical data showing local remapping. The SR also scales poorly computationally, requiring repeated eigendecomposition of large matrices. The TEM captures relational structure but learns compositionality implicitly through black-box neural network training, limiting functional interpretation. Metric theories struggle to explain how grid cells accommodate barriers and non-uniform environments.

### What this paper contributes

This paper introduces a unifying computational framework that reconciles compositionality with efficient planning in cognitive maps, and provides a principled account of diverse MEC cell types:

1. **Compositional predictive maps**: The paper extends linear RL with Predictive Object Representations (PORs)—compact, translation- and rotation-invariant matrices that capture how objects perturb baseline open-space predictive maps. This enables efficient construction of predictive maps by combining precomputed object representations, with computational complexity scaling with object size rather than environment size.

2. **Unified account of MEC cell types**: 
   - **Object vector cells**: The model identifies these as encoding PORs—the building blocks of compositionality. The paper shows that PORs capture key properties of object vector cells: translation and rotation invariance, field size dependence on object diameter, generalization across objects and environments, and experience-independent emergence.
   - **Grid cells**: The model proposes grid cells encode basis functions (eigenvectors) of the compositional predictive map. Unlike previous SR-based accounts, this predicts local (not global) remapping when barriers/goals are introduced, consistent with empirical data from wall removal, home cage introduction, and goal learning experiments.

3. **Efficient planning and learning**: The framework enables efficient planning via simple matrix-vector multiplication without iterative search. It also provides a biologically plausible learning algorithm for refining combined PORs for multiple objects, operating in object-space rather than state-space—dramatically more efficient than temporal-difference learning of successor representations.

4. **Resolution of puzzles**: The model resolves key empirical puzzles that challenged previous theories: why grid cells show local rather than global remapping, why object vector cells are so abundant (~30% of MEC cells), why grid cells are stable across behavioral policies but sensitive to physical barriers, and how goals subtly modulate grid fields.

### Brain regions & systems

**Medial entorhinal cortex (MEC)** — The primary focus of the paper. The model proposes a computational interpretation of MEC's role in cognitive mapping:
- **Object vector cells** (~30% of spatially tuned MEC cells): Encode Predictive Object Representations (PORs)—the compositional building blocks that capture how objects perturb baseline predictive maps. These cells are translation- and rotation-invariant, generalize across objects and environments, and are experience-independent.
- **Grid cells**: Encode basis functions (eigenvectors) of the open-space predictive map, onto which POR perturbations are projected. Provide a low-dimensional, efficient code for the compositional cognitive map. The model predicts local remapping of grid fields near introduced barriers/goals, with global stability elsewhere.
- **Border cells**: Distinguished from object vector cells; encode barriers already integrated into the current cognitive map (unlike object vector cells which maintain latent compositional representations)

**Hippocampus** — Mentioned in the context of place cells and replay. The paper discusses hippocampal replay (awake replay) as a potential neural mechanism for the learning algorithm that updates PORs for multiple objects.

**Prefrontal cortex** — Mentioned briefly in the context of representation learning and cognitive maps of task space.

### Mechanistic insight

The paper meets the bar for mechanistic insight by presenting a formal algorithm (compositional predictive maps with PORs) and connecting it to neural data (object vector cells and grid cells in MEC). However, the neural implementation is proposed rather than directly verified—the paper shows that the model's predictions match empirical data, but does not provide new neural recordings demonstrating that MEC cells actually encode the proposed representations.

**Computational level**: The brain solves the problem of efficiently constructing predictive cognitive maps for flexible planning by representing objects as perturbations to a baseline open-space map. This enables compositionality—complex maps can be built by combining precomputed object representations—while maintaining efficient planning through long-range predictive dependencies encoded in the Default Representation (DR).

**Algorithmic level**: The computation is implemented through:
1. **Predictive Object Representations (PORs)**: Compact matrices (size O×O where O is object size, not environment size S) that capture how objects alter state transitions. Computed using the Woodbury matrix identity for efficient updating of the DR.
2. **Basis function representation**: Grid cells encode eigenvectors of the open-space DR (matrix Uos), with PORs projected onto this basis (matrix G = Uos + UosC·A·R·Uos)
3. **Learning algorithm**: Iterative update rule A_new = A_old + α(I - Z·A_old) that refines combined PORs for multiple objects, operating in object-space rather than state-space

**Implementational level**: The paper proposes but does not directly verify the neural implementation:
- **Object vector cells**: Encode PORs (specifically, projected rows of the POR matrix). These cells are proposed to serve as the compositional building blocks.
- **Grid cells**: Encode the basis functions (eigenvectors) of the compositional predictive map. The model predicts that grid fields should show local remapping near barriers/goals due to local perturbations projected onto the stable eigenbasis.
- **Neural circuitry**: The model suggests grid cells might receive inputs from object vector cells (consistent with known MEC connectivity), implementing the projection of PORs onto the basis functions via simple neural network computations with fixed weights.

### Limitations & open questions

1. **Suspended objects**: The model's interpretation of why object vector cells fire for suspended objects (which don't block movement) remains debatable—the model suggests these are latent representations that could be integrated if needed, but this requires further investigation.

2. **Dynamic environments**: The model does not fully address navigation in dynamically changing environments where visual occlusion and object permanence pose challenges. The current framework can build maps gradually by adding barriers as observed, but tracking occluded or movable objects remains for future work.

3. **Continuous state spaces**: The current framework primarily addresses discrete state spaces, limiting direct applicability to classical continuous RL problems like motor control. However, the linear RL framework theoretically extends to continuous domains, offering a promising avenue for future work.

4. **Joint selectivity**: The model does not currently address how entorhinal cells often exhibit joint selectivity to multiple behavioral variables—a straightforward potential extension but one not pursued here.

5. **Boundary vector cells**: While the model primarily focuses on object vector cells, it could in principle be extended to boundary vector cells, which exhibit similar vectorial tuning. This extension remains for future work.

6. **Path integration**: The model does not explicitly incorporate velocity and path integration, though recent graph-based extensions could potentially be combined with the compositional framework.

7. **Neural implementation**: While the model proposes specific neural implementations (object vector cells encoding PORs, grid cells encoding basis functions), direct empirical verification of these mappings through simultaneous recordings of different MEC cell types during navigation remains for future work.

### Connections & keywords

**Key citations**:
- Stachenfeld et al. (2017): Proposed SR account of grid cells (contrast paper)
- Whittington et al. (2020): Tolman-Eichenbaum Machine (TEM) for relational memory
- Dordek et al. (2016): Non-negative PCA for grid cell learning (basis for open-space grid simulation)
- Høydal et al. (2019): Discovery of object vector cells in MEC (empirical foundation)
- Piray & Daw (2021): Linear RL / Default Representation (DR) foundation
- Todorov (2007, 2009): Linearly-solvable MDPs (theoretical foundation)

**Named models or frameworks**:
- Linear Reinforcement Learning (Linear RL)
- Default Representation (DR)
- Predictive Object Representation (POR)
- Successor Representation (SR) - contrast model
- Tolman-Eichenbaum Machine (TEM) - contrast model
- Woodbury matrix identity (mathematical tool)

**Brain regions**:
- Medial entorhinal cortex (MEC) - primary focus
  - Object vector cells (compositional building blocks)
  - Grid cells (basis functions)
  - Border cells (integrated barriers)
- Hippocampus (place cells, replay)
- Prefrontal cortex (cognitive maps of task space)

**Keywords**:
- Cognitive map
- Compositionality
- Reinforcement learning
- Predictive representation
- Default Representation (DR)
- Successor Representation (SR)
- Medial entorhinal cortex
- Grid cells
- Object vector cells
- Linear RL
- Planning
- Model-based RL
- Spatial navigation
- Basis functions
- Eigenvectors
- Woodbury identity
