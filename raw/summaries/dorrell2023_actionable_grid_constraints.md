---
source_file: "dorrell2023_actionable_grid_constraints.md"
paper_id: "dorrell2023_actionable_grid_constraints"
title: "Actionable Neural Representations: Grid Cells from Minimal Constraints"
authors: "William Dorrell, Peter Latham, Timothy E.J. Behrens, James C.R. Whittington"
year: 2023
journal: "International Conference on Learning Representations (ICLR 2023)"
paper_type: "computational"
contribution_type: "theoretical"
brain_regions: ["entorhinal_cortex", "medial_entorhinal_cortex"]
frameworks: ["attractor_networks", "tolman_eichenbaum_machine"]
keywords: ["actionable", "neural", "representations", "grid", "cells", "minimal", "constraints"]
key_citations: ["whittington2020_tolman_eichenbaum_machine", "whittington2023_disentanglement_constraints", "burak2009_path_integration_grid_cells", "schaeffer2022_no_free_lunch_deep_learning_neuroscience"]
---

### One-line summary

By combining three minimal constraints — actionability (linear matrix updates for each action), biological feasibility (non-negative, bounded firing), and functional discriminability — the optimal neural representation of 2D space is provably multiple modules of hexagonal grid cells.

---

### Background & motivation

Grid cells in medial entorhinal cortex fire in hexagonal lattices and are organised into discrete modules differing in scale and orientation, but a principled normative explanation for why this particular structure is optimal has remained elusive. Previous theories either assumed hexagonal tuning and derived downstream properties, or derived grid-like responses from recurrent network training without explaining the multi-module hexagonal structure from first principles. The paper fills this gap by asking: what minimal representational constraints jointly necessitate the observed grid cell architecture?

---

### Methods

- **Framework**: Constrained optimisation over neural representations of 2D position.
- **Actionability constraint**: Each spatial translation must correspond to a matrix that linearly updates the population representation, regardless of starting position. Formalised using group and representation theory (Peter-Weyl theorem applied to the group of 2D translations); constrains the representation to be a linear mixture of sines and cosines at a set of 2D frequencies.
- **Functional constraint**: A loss function L minimises total representational similarity between positions, weighted by the agent's occupancy distribution p(x) and a pair-importance kernel χ that prioritises separating pairs within a resolution scale l. This biases frequencies to a Goldilocks annulus in frequency space (between 1/L and 1/l).
- **Biological constraints**: Non-negativity of all firing rates and bounded (energy-normalised) activity.
- **Analysis**: Analytic derivations supported by numerical optimisation using ADAM with GECO constraint enforcement; simulations vary neuron count, module number, environment geometry, and in ablation experiments remove individual constraints.
- **Validation**: Qualitative and rudimentary quantitative comparison to published experimental data (primarily Stensola et al., 2012, 2015).

---

### Key findings

- The three constraints jointly and uniquely produce multiple modules of hexagonal grid cells; removing any single constraint (ablations in Appendix I) prevents the full grid-cell structure from emerging.
- Non-negativity alone forces lattice tuning curves: satisfying non-negativity for a single neuron requires harmonically related frequencies, and the efficient way to achieve this across many neurons is to make them translated copies of one another — a module of lattice cells.
- The occupancy distribution p(x) and pair-importance kernel χ together break the degeneracy among all lattices, selecting a hexagonal frequency lattice (densest packing within the Goldilocks annulus) and thus hexagonal grid cells.
- A "harmonic tussle" between intra-module (harmonic frequency lattices required for non-negativity) and inter-module (non-harmonic frequencies required for population-level discriminability) constraints is resolved by multiple modules: harmonics within each module, non-harmonic relationships across modules.
- **Prediction 1**: Number of neurons in a module scales as N ∝ (ν/µ)², where ν is lattice lengthscale and µ is field width; consistent with data from Stensola et al. (2012).
- **Prediction 2**: The optimal inter-module angular offset is small (~4°), not 0° or 30°, because small offsets minimise harmonic overlap between module frequency lattices; matches observations in Stensola et al. (2012).
- **Prediction 3**: Grid frequency structure should adapt to environment geometry — in rectangular rooms, grids should tile along cardinal axes at intervals of 2π/L, with some cells stable across room reshaping and others shifting; matches the stable/shifting cell observations of Stensola et al. (2012) in square vs. rectangular rooms.

---

### Computational framework

The paper uses **group and representation theory** (specifically the Peter-Weyl theorem for compact topological groups) as its mathematical foundation, embedded within a **normative/constrained optimisation** framework.

- **What is modelled**: The optimal population-level neural code for representing 2D position given three biologically and functionally motivated constraints.
- **Key variables**: The neural representation g(x) ∈ R^N; the transformation matrix T(Δx) that updates the representation for any translation Δx; frequency vectors k_d parameterising the representation; coefficient vectors a_d, b_d mixing sinusoidal components.
- **Core formalisation**: Actionability requires g(x + Δx) = T(Δx) g(x) for all x. By Peter-Weyl, T must decompose into irreducible representations (irreps) of the 2D translation group — 2×2 rotation matrices at frequencies k_d. This constrains g(x) to be a linear combination of sines and cosines of k_d · x.
- **Key assumption**: 2D space is approximated by a large torus, making the group of translations compact and enabling application of Peter-Weyl. This approximation becomes exact as torus radius → ∞.

---

### Prevailing model of the system under study

The paper's introduction frames the field as having two main strands of normative grid cell theory. The **functional strand** (Mathis et al., 2012; Wei et al., 2015; Sreenivasan & Fiete, 2011) shows that hexagonal grids provide efficient position coding and predicts module scale ratios, but assumes hexagonal tuning rather than deriving it, and does not explain module multiplicity or inter-module angles. The **actionability/path-integration strand** (Burak & Fiete, 2009; Cueva & Wei, 2018; Banino et al., 2018; Sorscher et al., 2019) derives grid-like responses from recurrent networks trained to path-integrate, but has been questioned for parameter sensitivity (Schaeffer et al., 2022) and reliance on experimentally unobserved place-cell decoder shapes (Sorscher et al., 2019). Whittington et al. (2020) and Gao et al. (2021) learn actionable linear representations that produce hexagonal grids, but require hard-coded module structure. The prevailing view is therefore that grid cells are efficient, path-integrating position codes, but the precise reason for hexagonality and multi-module organisation from first principles is not fully settled.

---

### What this paper contributes

The paper provides the first fully derivational account of the multi-module hexagonal grid cell architecture from minimal first principles, without assuming hexagonal tuning or hard-coding the number of modules. It clarifies the functional role of each constraint: non-negativity produces lattice tuning and module structure; the occupancy/resolution tradeoff selects hexagons from among all lattices; the neural discrimination loss drives inter-module non-harmonicity. The paper also produces three novel quantitative predictions (module neuron-count scaling, inter-module angle, environment-geometry adaptation) that go beyond prior functional theories and receive preliminary empirical support. Conceptually, it proposes "actionability" — the requirement that action consequences be linearly predictable from the representation — as a general normative principle for flexible cognition, distinct from mere encoding efficiency.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — sole anatomical focus; the locus of grid cells whose hexagonal, multi-module organisation the paper normatively derives and makes predictions about.

The paper is otherwise entirely computational; no anatomical or circuit-level implementation is proposed, though continuous attractor networks (CANs) in MEC are acknowledged as a candidate implementational mechanism.

---

### Mechanistic insight

The paper does not meet the bar. It proposes a normative computational framework and validates it with simulations, and the predictions are compared to existing electrophysiology data (Stensola et al., 2012, 2015). However, the paper does not present new neural recordings, imaging, or other direct neural data linking the model's specific variables (e.g. frequency lattice structure, transformation matrices T(Δx)) to measured neural activity. The framework operates at the computational and algorithmic levels only; it does not provide neural evidence that specifically distinguishes the actionability account from alternative algorithms.

---

### Limitations & open questions

- The framework currently does not account for grid cell phenomena arising from sensory uncertainty or environment boundary effects, such as field-intensity variability (Dunn et al., 2017) or grid bending in trapezoidal environments (Krupic et al., 2015); the authors suggest incorporating spatial uncertainty (as in Ocko et al., 2018; Kang et al., 2023) may address these.
- The relationship between the linear actionability framework and continuous attractor network (CAN) implementations of path integration is left for future work; the two approaches imply different update equations.
- The torus approximation of flat 2D space excludes some formal representations of the infinite plane, though the authors argue these are biologically implausible.
- The prediction that 3D space should yield regular ordered representations is at odds with experimental findings of irregular 3D grid cells (Grieves et al., 2021; Ginosar et al., 2021), suggesting either the theory is incomplete for 3D navigation or animals navigate 3D space suboptimally.
- Quantitative comparison to experimental data (module neuron counts, inter-module angles) is described as "rudimentary"; rigorous statistical testing is deferred to future work.
- The framework assumes a separate neural population encodes each variable; the companion paper (Whittington et al., 2023) addresses how independent variables are routed to separate sub-populations.

---

### Connections & keywords

**Key citations**:
- Hafting et al. (2005) — original discovery of grid cells
- Stensola et al. (2012) — modular organisation and multi-scale structure of grid cells (primary empirical validation target)
- Stensola et al. (2015) — shearing of grid cells in square environments
- Whittington et al. (2020) — Tolman-Eichenbaum Machine; related linear actionable representation learning
- Gao et al. (2021) — path integration via group representation theory (most directly related prior work)
- Burak & Fiete (2009) — continuous attractor network model of path integration
- Sorscher et al. (2019) — pattern-formation theory of grid cell origin
- Wei et al. (2015) — functional efficiency theory of grid cell architecture
- Mathis et al. (2012a,b) — hexagonal grids as optimal population codes for space
- Whittington et al. (2023) — companion paper on disentanglement and sub-population structure

**Named models or frameworks**:
- Actionable representations
- Group and representation theory / Peter-Weyl theorem
- Tolman-Eichenbaum Machine (Whittington et al., 2020)
- Continuous attractor networks (CAN) — discussed but not adopted
- GECO (Rezende & Viola, 2018) — constraint-handling optimisation method

**Brain regions**:
- Medial entorhinal cortex (MEC)

**Keywords**:
- grid cells
- actionable representations
- group representation theory
- normative theory
- path integration
- non-negative firing rates
- hexagonal lattice
- multi-module organisation
- constrained optimisation
- cognitive map
- spatial coding
- zero-shot inference
