---
source_file: dordek2016_grid_cells_nonnegative_pca.md
title: "Extracting grid cell characteristics from place cell inputs using non-negative principal component analysis"
authors: Yedidyah Dordek, Daniel Soudry, Ron Meir, Dori Derdikman
year: 2016
journal: eLife
paper_type: computational
contribution_type: theoretical
---

### One-line summary

A single-layer neural network with non-negative Hebbian (Oja rule) weights learning from place cell inputs implements non-negative PCA and spontaneously converges to hexagonal grid cell firing patterns, providing a mechanistic account of grid cell formation driven by hippocampal feedback.

---

### Background & motivation

Grid cells in the medial entorhinal cortex (MEC), presubiculum, and parasubiculum fire in spatially periodic hexagonal patterns and are widely assumed to receive input primarily from path integration (velocity-driven) mechanisms. However, experimental evidence challenges this downstream-only view: inactivating hippocampal place cells causes grid cells to disappear, and during development place cells emerge before grid cells. These data point to a functionally significant feedback projection from place cells to grid cells that most models had ignored. The paper asks whether hexagonal grid cell structure can emerge from place cell inputs alone, without any path integration signal, via a biologically plausible learning rule.

---

### Methods

- **Model architecture**: Single-layer feedforward neural network; place-cell-like inputs (2D Gaussian or difference-of-Gaussians firing fields uniformly covering a square arena) project to one or more grid-cell-like output units.
- **Learning rule**: Oja rule (self-normalizing Hebbian learning), which provably converges to the leading principal component of the input covariance. In the multi-output case, a Sanger/Gram-Schmidt hierarchical extension is used.
- **Non-negativity constraint**: Feedforward weights are rectified to zero when they become negative (reflecting the excitatory nature of hippocampal-to-MEC projections). For direct PCA, two numerical algorithms were used: NSPCA (coordinate-descent non-negative sparse PCA) and AMP (approximate message passing).
- **Zero-mean requirement**: Tested via (1) temporal differentiation of inputs, (2) adaptation variable (Kropff & Treves approach), (3) spatially zero-mean inputs (Laplacian/Mexican-hat or positive-negative disks).
- **Validation metrics**: Hexagonal gridness score (autocorrelogram rotations at 30°, 60°, 90°, 120°, 150°) and square gridness score (45° rotations). ~1500 simulations per condition. Grid spacing and orientation dependence on place field width analyzed using FISTA algorithm.
- **Analytical treatment**: Fourier-domain analysis showing that unconstrained PCA solutions lie on a square k-lattice, while non-negative PCA solutions lie on a hexagonal k-lattice.
- **Stability analysis**: ODE method (stochastic approximation theory) used to confirm asymptotic stability of hexagonal solutions.

---

### Key findings

- Unconstrained PCA/neural network: converges to square-periodic spatial patterns (gridness score 0.302 ± 0.003 for network; 0.27 ± 0.0023 for direct PCA).
- Non-negatively constrained network: converges robustly to hexagonal grid patterns (gridness score 1.07 ± 0.003 for network; 1.13 ± 0.0022 for direct PCA).
- Two necessary conditions for hexagonal outputs: (1) non-negative feedforward weights; (2) zero-mean input (in time or space).
- Simple 2D Gaussian inputs (which are not zero-mean) fail to produce grid-like outputs; zero-mean inputs (derivatives, Mexican hats, adaptation) all succeed.
- Grid spacing scales linearly with place field width: S = 7.5σ + 0.85 (periodic boundary conditions); grid scale primarily reflects the largest place cell fields.
- Grid orientation is approximately uniformly distributed in [0°, 15°] for large environments; Fourier analysis provides a lower bound on grid spacing equal to 4π/(√3 · k†).
- Hierarchical multi-output network produces two clusters of grid spacings with a ratio of ~√2 ≈ 1.4, consistent with the experimental value of 1.42 (Stensola et al., 2012). Only two modules are recovered, however, while experimental data show at least five.
- Hexagonal solutions are stable from random, stripe, square, rhomboid, and noisy-hexagon initializations.
- Fourier analysis proves that the hexagonal lattice in k-space achieves a higher objective value (0.2558) than any square or 1D lattice solution (bounded ≤ 0.25), formally explaining why non-negative PCA favors hexagons.

---

### Computational framework

The paper employs **non-negative Principal Component Analysis (nn-PCA)** implemented via a biologically plausible Hebbian network.

- **What is modelled**: the synaptic weights from a population of place cells to grid cell output units. Weight dynamics follow the Oja rule (which maximises output variance subject to unit-norm constraint).
- **Key variables**: weight vector J (place-to-grid connection strengths), place cell activity matrix X (Neuron × Time), covariance matrix Σ = E[X^T X], gridness score.
- **Key assumption**: excitatory-only (non-negative) weights, equivalent to a non-negativity constraint on the PCA eigenvector. This is NP-hard in general; solved numerically or via the neural network rectification rule.
- **Fourier analysis**: the covariance matrix has Toeplitz (spatially stationary) or circulant (periodic boundary) structure, so PCA eigenvectors are sinusoidal. The non-negativity constraint forces the optimal solution to occupy a hexagonal arrangement of Fourier components rather than a square one.
- **Modules**: a hierarchical Gram-Schmidt-like extension recovers higher principal components, producing grid modules at spacings related by √2.

---

### Prevailing model of the system under study

Before this paper, grid cell models fell predominantly into the **path integration** camp: velocity signals are integrated over time by attractor network dynamics (continuous attractor network models) or oscillatory interference mechanisms, generating periodic spatial firing without requiring any place cell input. The anatomical flow from MEC grid cells to hippocampal place cells (grid→place) had guided most modelling efforts. A notable exception was Kropff & Treves (2008), who showed grids could emerge from place cell inputs using an adaptation mechanism, but did not frame this as PCA and did not identify non-negativity as the critical factor controlling lattice geometry. The paper by Stachenfeld et al. (2014) noted a PCA-like relationship but, without a non-negativity constraint, obtained square rather than hexagonal grids. The paper therefore works against the dominant assumption that velocity/path integration is the primary determinant of grid cell structure, and extends the minority view (place→grid feedback) to provide a mathematically grounded explanation for hexagonality.

---

### What this paper contributes

This paper makes the following specific advances:

1. **Identifies non-negativity as the geometric switch**: the difference between square and hexagonal grid output is entirely explained by whether feedforward weights are constrained to be non-negative. This had not been noted in prior work.
2. **Formal explanation of hexagonality**: Fourier analysis of the non-negative PCA objective proves that hexagonal k-lattice solutions achieve strictly higher variance than square solutions (objective ≈ 0.2558 vs. ≤ 0.25), providing the first mathematically rigorous account of why grid cells are hexagonal in a learning model.
3. **Linear grid spacing law**: grid spacing is analytically and numerically shown to scale linearly with place field width, with a derivable lower bound. This predicts that large-field place cells drive wide-spacing grid cells.
4. **Modular spacing ratio**: the hierarchical network recovers two modules with spacing ratio ~√2, consistent with experimental measurements.
5. **Unification with PCA**: the place-to-grid transformation is formally equivalent to non-negative PCA, linking grid cell development to a well-understood dimensionality reduction algorithm.

What remains open: the model predicts only two modules (data show ≥ 5); grid orientation distribution is predicted to be uniform in [0°, 15°] whereas data show a peak near 7.5°; and the reciprocal grid-to-place projection is not modelled.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — site of grid cell output units in the model; the paper seeks to explain how hexagonal firing patterns are formed here.
- **Hippocampus (CA1, CA3)** — source of place cell inputs to the model; evidence that hippocampal inactivation destroys grid cells motivates the place→grid feedback direction.
- **Presubiculum / parasubiculum** — mentioned as additional regions containing grid cells, though not modelled separately.
- **Entorhinal-hippocampal circuit** — the paper focuses on the feedback (place→grid) limb of this circuit rather than the more commonly modelled grid→place limb.

---

### Mechanistic insight

The paper proposes an algorithm (non-negative PCA via Hebbian learning) and provides mathematical proof and simulation evidence that it produces hexagonal outputs, but it does not provide neural recordings or other empirical data linking the model's specific variables to measured neural activity. The model is fit to the statistical structure of place cell inputs, not to grid cell electrophysiology.

Therefore the paper does not meet the bar for mechanistic insight as defined: it presents a formal algorithm with strong theoretical support, but there are no neural data specifically supporting nn-PCA over alternative algorithms. The contribution is at the computational and algorithmic levels of Marr's hierarchy, without implementational grounding in measured cell types, connectivity, or physiology.

---

### Limitations & open questions

- **Only two modules recovered**: the hierarchical network produces only two grid spacing clusters, while experiments show at least five. The paper acknowledges this discrepancy.
- **Grid orientation distribution mismatch**: the model predicts a uniform distribution of orientations in [0°, 15°] for large environments; experiments find a peak at 7.5°. The authors suggest a bidirectional model (closing the loop between grid and place cells) may be needed.
- **Non-uniform place field widths ignored**: real hippocampus has a gradient of place field sizes along the dorsoventral axis, which is not incorporated.
- **No reciprocal grid-to-place projection**: the model is feedforward (place→grid only); the full circuit likely involves iterative, bidirectional interactions.
- **Non-negativity implementation is NP-hard**: the direct non-negative PCA problem is NP-hard; the neural network rectification heuristic converges to a local, not necessarily global, optimum.
- **Zero-mean requirement is biologically post-hoc**: the requirement for zero-mean input (via differentiation, Mexican hats, or adaptation) is necessary for PCA but the biological mechanism producing this in place cells is unspecified.
- **No developmental or temporal predictions**: the model learns in simulation but makes no specific predictions about the time course of grid cell development in young animals.

---

### Connections & keywords

**Key citations**:
- Hafting et al. (2005) — original grid cell discovery
- Stensola et al. (2012) — entorhinal grid map is discretized into modules; ratio ~√2
- Stensola et al. (2015) — grid orientation asymmetry
- Bonnevie et al. (2013) — hippocampal inactivation destroys grid cells
- Langston et al. (2010) / Wills et al. (2010) — place cells precede grid cells in development
- Oja (1982) — Oja learning rule / neural PCA
- Kropff & Treves (2008) — grid emergence from place cell inputs via adaptation
- Stachenfeld, Botvinick, Gershman (2014) — PCA relationship between place and grid cells (square result)
- Sanger (1989) — hierarchical multi-output PCA network
- Couey et al. (2013) — recurrent inhibitory circuitry in grid formation
- Mathis et al. (2014); Wei et al. (2013) — information-theoretic optimality of hexagonal grids

**Named models or frameworks**:
- Oja rule (self-normalizing Hebbian learning / PCA)
- Non-negative PCA (nn-PCA)
- NSPCA (Nonnegative Sparse PCA, Zass & Shashua 2006)
- AMP (Approximate Message Passing, Montanari & Richard 2014)
- FISTA (Fast Iterative Shrinkage-Thresholding Algorithm, Beck & Teboulle 2009)
- Sanger's hierarchical PCA network
- Stochastic approximation / ODE method (Hornik & Kuan 1992)

**Brain regions**:
- Medial entorhinal cortex (MEC)
- Hippocampus (CA1, CA3)
- Presubiculum, parasubiculum

**Keywords**:
- grid cells
- place cells
- non-negative principal component analysis
- Hebbian learning
- Oja rule
- hexagonal lattice
- place-to-grid feedback
- entorhinal cortex
- grid modules
- spatial navigation
- dimensionality reduction
- Fourier analysis of spatial coding
