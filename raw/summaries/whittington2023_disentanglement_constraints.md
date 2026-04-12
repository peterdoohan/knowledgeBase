---
source_file: whittington2023_disentanglement_constraints.md
paper_id: whittington2023_disentanglement_constraints
title: "Disentanglement with Biological Constraints: A Theory of Functional Cell Types"
authors:
  - "James C.R. Whittington"
  - "William Dorrell"
  - "Surya Ganguli"
  - "Timothy E.J. Behrens"
year: 2023
journal: "ICLR (International Conference on Learning Representations)"
paper_type: computational
contribution_type: theoretical
species:
  - human
tasks:
  - navigation_task
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - prefrontal_cortex
  - visual_cortex
keywords:
  - disentanglement
  - nonnegativity
  - energy_efficiency
  - biological_constraints
  - functional_cell_types
  - grid_cells
  - object_vector_cells
  - independent_component_analysis
  - neural_representation
  - variational_autoencoder
  - mixed_selectivity
  - factorised_representations
  - neural_manifolds
  - path_integration
  - pattern_formation
  - hebbian_learning
  - interpretability
  - compositional_generalization
  - biological
  - constraints
key_citations:
  - boccara2019_grid_goal_attractor
  - butler2019_reward_locations_entorhinal_maps
---

### One-line summary
Simple biological constraints of nonnegativity and energy efficiency mathematically enforce disentangled neural representations where single neurons become selective for single task factors.

### Background & motivation
Neural representations in the brain often exhibit disentanglement (single neurons tuned to single interpretable factors), yet standard neural network theory suggests representations should be distributed and hard to interpret. Machine learning has long sought disentangled representations for better interpretability and compositional generalization, but this typically requires explicit inductive biases. The authors address the gap: why do biological neurons often represent single human-interpretable factors, and can biological constraints explain this?

### Methods
- **Theoretical approach**: Mathematical proof (two theorems) showing that nonnegativity and energy efficiency constraints on linear neural representations lead to disentanglement
- **Simulation studies**: 
  - Shallow and deep supervised neural networks on linear and nonlinear synthetic data
  - Linear and nonlinear autoencoders
  - Variational autoencoders (VAEs) on standard disentanglement benchmarks (Shapes3D, dSprites)
  - Spatial navigation task with grid cell and object-vector cell-like representations
- **Metrics**: Custom mutual information ratio (MIR) metric that scores highly when each neuron cares about only one factor (vs. MIG which requires each factor in only one neuron)

### Key findings
- **Theorem 1**: With independent task factors, nonnegativity constraint, and constant population variance, minimum activity energy representations are disentangled (each neuron selective for at most one task factor)
- **Theorem 2**: Even when network only receives entangled observations (linear mixtures of hidden factors), minimum energy nonnegative representations that accurately predict observations are disentangled
- **Empirical validation**: 
  - Linear networks without constraints learn entangled representations; with constraints learn disentangled (Fig. 2)
  - Deep nonlinear networks on linear data disentangle at all layers; on nonlinear data, early layers are mixed-selective, later layers disentangle (Fig. 3)
  - Autoencoders (linear and nonlinear) learn disentangled generative factors with constraints (Fig. 4)
  - VAEs with ReLU and weight regularization achieve competitive MIG scores (comparable to β-VAE) with better reconstruction (Fig. 5)
- **Neuroscience applications**:
  - Factorised tasks (objects anywhere in space) lead to distinct modules: grid cells (space) and object-vector cells (objects) (Fig. 6)
  - Entangled tasks (objects fixed in space) lead to warped grid cells that entangle space and object locations (Fig. 7), explaining experimental observations (Boccara et al., 2019; Butler et al., 2019)
  - Sparsity constraints alone do NOT promote disentanglement (Fig. 8, Fig. 9)
  - Categorical representations (one-hot) also disentangle under same constraints (Fig. 11)

### Computational framework
**Nonnegative Independent Component Analysis (ICA) with Energy Efficiency Constraints**

The paper frames disentanglement as a form of nonlinear ICA where biological constraints serve as the inductive bias. The core formalism involves:

- **Task factors**: Independent random variables e ∈ R^k representing ground truth factors of variation
- **Neural representation**: z ∈ R^n where z = Me + b_z (linear case) or nonlinear transformations thereof
- **Nonnegativity constraint**: z_i ≥ 0 for all neurons (enforced via ReLU or soft regularization)
- **Energy efficiency**: Minimizing E[||z||²] (activity energy) and/or ||W||²_F (weight energy)
- **Variance constraint**: Maintaining constant population variance to prevent representational collapse

The framework assumes that to satisfy nonnegativity with minimal energy, each neuron must be selective for at most one task factor, as mixing factors requires larger bias terms to ensure nonnegativity across all combinations of factor values.

### Prevailing model of the system under study
Before this work, the field understood that:
1. Disentangled representations exist in the brain (grid cells, object-vector cells, axis-aligned IT neurons) but there was no theory explaining why they emerge
2. Mixed-selectivity is prevalent in some brain regions (PFC, hippocampus) and serves computational purposes (dimensionality expansion for linear readout)
3. Machine learning disentanglement requires explicit inductive biases (β-VAEs, etc.) and is challenging without specific data biases
4. Grid cell warping to rewards was observed but unexplained (sometimes warps, sometimes doesn't)

The prevailing view was that disentanglement in the brain was a mysterious emergent property, while mixed-selectivity was the norm for flexible computation.

### What this paper contributes
This paper provides a unified theoretical framework showing that:

1. **Mathematical proof**: Simple biological constraints (nonnegativity + energy efficiency) are sufficient for disentanglement in linear networks—no explicit disentanglement objective needed

2. **Generalization to nonlinear settings**: Empirically demonstrates the same constraints induce disentanglement in deep nonlinear networks, autoencoders, and VAEs

3. **Theory of cell types**: Explains why the brain partitions neurons into distinct functional cell types (grid cells, object-vector cells, border cells)—because space, objects, and boundaries are independent task factors that should be represented in separate populations under biological constraints

4. **Explanation of grid cell warping**: Explains when and why grid cells warp to rewards—warping occurs when space becomes entangled with other factors (e.g., fixed reward locations), not when space and objects are factorised

5. **Resolution of disentanglement vs. mixed-selectivity debate**: Shows both can coexist—early layers in nonlinear tasks show mixed-selectivity (needed for computation), later layers disentangle (needed for readout)

6. **New disentanglement metric**: Introduces Mutual Information Ratio (MIR) that scores representations where each neuron cares about only one factor (different from MIG which requires each factor in only one neuron)

### Brain regions & systems
- **Medial entorhinal cortex**: Contains grid cells (GCs; hexagonal firing patterns for allocentric space) and object-vector cells (OVCs; firing at specific distances/orientations from objects). The paper shows these emerge as distinct modules under biological constraints when space and objects are factorised task variables
- **Hippocampal formation**: Including subiculum (border vector cells), CA regions (place cells). The paper explains why hippocampal cells sometimes encode conjunctions (entangled factors) and sometimes separate factors
- **Inferior temporal (IT) cortex**: Neurons axis-aligned to data generative factors (face identity axes). The paper's theory explains this as disentanglement under biological constraints
- **Prefrontal cortex (PFC)**: Shows both mixed-selectivity (Rigotti et al., 2013) and task-specific separation (Lee et al., 2022). The paper suggests this reflects different task demands (entangled vs. factorised)
- **Parietal cortex**: Task-specific neurons (Lee et al., 2022) explained by factorised task representations
- **Visual cortex (V1)**: Decorrelated firing (Ecker et al., 2010) consistent with energy efficiency constraints
- **Drosophila mushroom body**: Kenyon cells with random projections for dimensionality expansion (mixed-selectivity example)

### Mechanistic insight
This paper provides strong mechanistic insight by meeting both criteria: presenting a formal algorithm and providing neural data support.

**Algorithm**: The paper presents a formal computational framework where nonnegative, energy-efficient linear representations that predict observations from hidden task factors will necessarily disentangle. The algorithm involves:
- Representing task factors e through a linear generative model z = Me + b_z
- Enforcing nonnegativity (z_i ≥ 0) via ReLU or soft constraints
- Minimizing activity energy E[||z||²] and weight energy ||W||²_F
- Under constant variance constraint to prevent collapse

**Neural Evidence**: The theory explains diverse neuroscience observations:
- Grid cells and object-vector cells as distinct modules for factorised spatial variables
- Grid cell warping to rewards when space becomes entangled with reward locations
- Axis-aligned IT neurons for face identity factors
- Decorrelated V1 firing patterns
- Task-specific PFC/parietal neurons

**Marr's Levels Analysis**:
- **Computational**: The brain solves tasks by representing independent factors of variation; when factors are independent (factorised tasks), optimal representations under biological constraints are disentangled
- **Algorithmic**: Nonnegative, energy-efficient linear networks naturally implement independent component analysis (ICA), where each neuron becomes selective for at most one hidden factor
- **Implementational**: Biological neurons have firing rates (nonnegative), metabolic costs (energy efficiency), and must accurately predict sensory/behavioral outputs—these physical constraints naturally lead to disentangled, interpretable representations

The paper thus bridges all three levels of analysis, providing a mechanistic understanding of why single neurons in the brain often represent single human-interpretable factors.

### Limitations & open questions
- **Linearity assumption**: Theorems apply to linear networks; empirical results show extension to nonlinear networks but without formal proof
- **Independent factors assumption**: Theory assumes task factors are independent; extension to correlated factors is not fully formalized
- **Orthonormal columns assumption**: Theorem 2 requires (scaled) orthonormal columns in the data generation matrix D; authors note this approximately holds for random matrices with many observations and few factors
- **Does not explain specific representational forms**: While the theory explains why different factors are in different neurons (disentanglement), it does not explain why grid cells have hexagonal firing patterns or why specific cell types have their particular response properties (this is addressed in a companion paper by Dorrell et al., 2023)
- **Sparsity vs. nonnegativity**: Authors show sparsity alone does not promote disentanglement, but do not fully explore interactions between sparsity and other constraints
- **Limited to feedforward and simple recurrent architectures**: Theory does not fully address complex recurrent dynamics or multi-area interactions

### Connections & keywords
- **Key citations**: Hafting et al. (2005) grid cells; Høydal et al. (2019) object-vector cells; Higgins et al. (2017a) β-VAE; Locatello et al. (2019) disentanglement challenges; Rigotti et al. (2013) mixed-selectivity; Comon (1994) ICA; Lee & Seung (2000) nonnegative matrix factorization; Sorscher et al. (2019, 2020) grid cell emergence theory; Boccara et al. (2019) and Butler et al. (2019) grid cell warping studies
- **Named models/frameworks**: β-VAE, Variational Autoencoder (VAE), Independent Component Analysis (ICA), Nonnegative Matrix Factorization (NMF), Hebbian/anti-Hebbian learning, Pattern formation dynamics, Path integration, Cellular automata, Mutual Information Ratio (MIR) metric
- **Brain regions**: Medial entorhinal cortex, hippocampal formation, subiculum, prefrontal cortex (PFC), inferior temporal (IT) cortex, parietal cortex, visual cortex (V1), Drosophila mushroom body
- **Keywords**: disentanglement, nonnegativity, energy efficiency, biological constraints, functional cell types, grid cells, object-vector cells, independent component analysis, neural representation, variational autoencoder, mixed-selectivity, factorised representations, neural manifolds, path integration, pattern formation, Hebbian learning, interpretability, compositional generalization
