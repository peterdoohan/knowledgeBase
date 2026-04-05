---
source_file: dorrell2022_actionable_grid_cells.md
title: Actionable Neural Representations: Grid Cells from Minimal Constraints
authors: William Dorrell, Peter E. Latham, Timothy E.J. Behrens, James C.R. Whittington
year: 2022
journal: Preprint (under review)
paper_type: computational
contribution_type: theoretical
---

### One-line summary
Grid cells emerge as the optimal representation of 2D space when neural codes are constrained to be actionable (supporting linear transformation by actions), functional (maximally discriminating), and biological (non-negative, bounded firing rates).

### Background & motivation
The paper addresses how the brain builds internal representations that support flexible behaviors like zero-shot inference and shortcut planning. It introduces "actionable representations" — representations that encode not just variables of interest but also how those variables transform under actions. The framework is applied to explain why entorhinal grid cells have their characteristic hexagonal firing patterns and modular organization.

### Methods
- **Theoretical framework**: Formulated using group and representation theory to define actionable representations as those where each action has a corresponding linear transformation matrix
- **Constrained optimization**: Combined three constraints:
  - *Functional*: Minimize representational similarity between different positions (maximize discriminability)
  - *Biological*: Non-negative firing rates and bounded activity (L2 norm constraint)
  - *Actionable*: Linear update of representation via transformation matrices for each action
- **Numerical optimization**: Used gradient descent (ADAM) with GECO algorithm to enforce constraints, for both infinite spaces (line, plane) and finite spaces (circle, torus, sphere)
- **Analytical derivations**: Perturbation analysis of loss functions to understand frequency selection

### Key findings
- **Single module formation**: Non-negativity constraint drives neurons to share harmonically related frequencies, forming lattice-like (grid) tuning curves rather than random combinations of sines and cosines
- **Hexagonal preference**: The functional objective's tension between low-frequency bias (from distance-dependent similarity weighting χ) and high-frequency bias (from position occupancy distribution p) selects hexagonal lattices as optimal — hexagons pack most frequencies within the preferred annulus in frequency space
- **Multiple modules**: The neural lengthscale σ (minimum discriminable distance) creates a "harmonic tussle" — single neurons want harmonically related frequencies for non-negativity, but the population wants non-harmonically related frequencies for discriminability. Multiple modules resolve this: harmonically related frequencies within modules, non-harmonic relationships between modules
- **Testable predictions**:
  - Lattice size to field width ratio scales with square of number of neurons in module (N ∝ (ν/μ)²)
  - Optimal angular offset between modules is small (~4°, varying 3-8° depending on parameters)
  - Grid cells should morph to match room geometry: optimal frequencies align with integer multiples of π/L in square/rectangular rooms, Bessel function zeros in circular rooms

### Computational framework
- **Group and Representation Theory**: Actions on variables (like 2D translations) form mathematical groups. Actionable representations require transformation matrices that are representations of these groups. Representation theory constrains the neural code to be linear combinations of sines and cosines at specific frequencies.
- **Constrained Optimization**: The optimal code minimizes representational similarity loss subject to biological (non-negativity, boundedness) and actionable (frequency sparsity) constraints.
- **Normative Modeling**: Derives grid cells from first principles rather than hand-tuning network parameters.

### Prevailing model of the system under study
Before this work, grid cells were understood through several theoretical lenses: (1) Continuous attractor network models that hand-tuned connectivity to produce hexagonal patterns and path integration; (2) Supervised learning approaches that trained RNNs to path integrate, which produced grid-like responses but required specific training curricula and were criticized for parameter dependence; (3) Normative models based on efficient coding that explained hexagons as optimal for spatial representation but assumed grid-like tuning rather than deriving it. The functional (efficient coding) approaches generally predicted place cells rather than grid cells for 2D space, and none of the approaches fully explained the modular organization of grid cells.

### What this paper contributes
This paper provides a mathematical derivation showing that grid cells are the optimal representation of 2D space under three fundamental constraints: actionability (supporting linear transformation by actions), biological plausibility (non-negative, bounded firing), and functional efficiency (maximally discriminating representations). Unlike prior normative theories, it explains why grid cells (not place cells) emerge for 2D space, why they have hexagonal symmetry, and why they are organized into multiple modules with non-harmonically related scales. The framework makes novel, testable predictions about: (1) the scaling relationship between module size and grid field properties, (2) small optimal angular offsets between modules (~4°), and (3) how grid representations should adapt to room geometry (square vs. circular vs. rectangular environments). The theory generalizes beyond grid cells to any variables whose transformations form a group, providing a principled framework for understanding how the brain builds representations that support flexible behavior.

### Brain regions & systems
- **Medial entorhinal cortex (MEC)**: Contains grid cells that represent 2D space in hexagonal lattices; the paper proposes this organization emerges from the constraints of actionability, biological plausibility, and functional efficiency
- **Hippocampus**: Receives grid cell input; mentioned in context of place cells and the broader spatial representation system
- **Head direction system**: Used as comparison for theoretical predictions — the paper predicts place-cell-like tuning for circular variables (like heading direction) under their framework

### Mechanistic insight
The paper provides a strong mechanistic account at the computational and algorithmic levels, though implementation-level details are abstracted.

**Computational level**: The brain must solve the problem of representing variables in a way that supports flexible behavior (zero-shot inference, planning). The computational problem is to build an actionable representation — one where transformations of the input variable can be implemented as linear transformations in neural space. For 2D space, this means representing position such that translation actions (stepping north, south, etc.) have corresponding transformation matrices that update the representation predictably.

**Algorithmic level**: The representation is constructed as a linear combination of sinusoidal basis functions (sines and cosines at specific frequencies), with coefficients optimized to satisfy three constraints: (1) Actionability requires frequency sparsity — only D < N/2 frequencies can be used; (2) Biological constraints require non-negative firing rates (achieved by choosing appropriate frequency combinations and constant offsets) and bounded activity (L2 norm constraint); (3) Functional objectives require maximizing discriminability (minimizing representational similarity between different positions). The optimal algorithm produces multiple modules of hexagonal grid cells: within each module, neurons share harmonically related frequencies (enabling non-negativity), while between modules, frequencies are non-harmonically related (enabling discriminability).

**Implementational level**: The paper explicitly abstracts away from implementation, noting that continuous attractor networks (CANs) are thought to implement path integration circuits, but actionability and CANs imply seemingly different update equations. The theory does not specify particular cell types, synaptic connectivity, or biophysical mechanisms, though it constrains the space of possible implementations (e.g., requiring neural populations that can implement linear transformations via matrix multiplication).

The paper meets the high bar for mechanistic insight: it formalizes an algorithm (actionable representations via group/representation theory) and provides neural data constraints (grid cell properties match predictions), though it does not directly test whether the specific neural implementation follows the derived algorithmic principles.

### Limitations & open questions
- **Implementation gap**: The theory is normative and abstracted from implementation. While continuous attractor networks (CANs) are thought to implement path integration, the relationship between actionability (linear matrix updates) and CAN dynamics (attractor dynamics) is not fully resolved.
- **3D representations**: The theory predicts regular, densely packed 3D grid structures, but actual recordings in bats and mice show irregular, unstructured 3D firing patterns. The authors suggest this may reflect suboptimal coding in 3D where animals sacrifice actionability for efficient encoding.
- **Sensory integration**: The theory does not incorporate sensory information, which may explain phenomena like grid intensity variations and lattice bending in trapezoidal environments that the current theory cannot predict.
- **Multiple variables**: The current theory assumes separate populations for each variable; a companion paper (Whittington et al., 2022) extends this to show how biological and functional constraints encourage independent variables to be encoded in separate sub-populations.
- **Generality vs. specificity**: The framework applies to any group-structured variables, but the specific predictions have been primarily tested (and match) for 2D space. Further work is needed to validate predictions for other variables (heading direction, object orientation, 3D space, etc.).

### Connections & keywords
- **Key citations**: Tolman (1948) — cognitive maps; Hafting et al. (2005) — grid cell discovery; Stensola et al. (2012) — grid cell modularity; Burak & Fiete (2009) — continuous attractor models; Cueva & Wei (2018), Banino et al. (2018), Sorscher et al. (2019) — RNN models of grid cells; Whittington et al. (2020) — Tolman-Eichenbaum machine; Gao et al. (2021) — linear path integration models; Sengupta et al. (2018) — non-negative similarity matching; Stensola et al. (2015) — grid alignment to room geometry; Krupic et al. (2015) — grid bending in trapezoids; Dunn et al. (2017) — grid field intensity variations; Mathis et al. (2012a,b) — efficient coding of space; Wei et al. (2015) — grid scale predictions; Stemmler et al. (2015) — grid decoding; Issa & Zhang (2012) — path integration theory; Paccanaro & Hinton (2001) — linear relational embedding; Attneave (1954), Barlow et al. (1961) — efficient coding; Olshausen & Field (1996) — sparse coding; Hyvärinen (2010) — independent component analysis; Bronstein et al. (2021) — geometric deep learning
- **Named models/frameworks**: Actionable representations; Group and representation theory framework; Constrained optimization approach; GECO (Generalized EVB Constrained Optimization) algorithm; Continuous attractor networks (CANs) — mentioned as comparison; Tolman-Eichenbaum Machine — related work; Non-negative similarity matching — related framework
- **Brain regions**: Medial entorhinal cortex (MEC) — primary focus, contains grid cells; Hippocampus — mentioned in context of place cells and spatial memory; Head direction system — used as theoretical comparison
- **Keywords**: grid cells, actionable representations, group theory, representation theory, path integration, spatial navigation, hexagonal tuning, modularity, continuous attractor networks, efficient coding, non-negative firing rates, constrained optimization, neural coding, cognitive maps, toroidal topology, zero-shot inference, Fourier analysis, harmonic tussle, place cells, head direction cells, 3D spatial representation, normative modeling, biological constraints, functional constraints, generalization, neural representations, spatial memory, entorhinal cortex, hippocampal formation