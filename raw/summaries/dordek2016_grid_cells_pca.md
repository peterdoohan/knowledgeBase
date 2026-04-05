---
source_file: dordek2016_grid_cells_pca.md
title: "Extracting grid cell characteristics from place cell inputs using non-negative principal component analysis"
authors: Yedidyah Dordek, Daniel Soudry, Ron Meir, Dori Derdikman
year: 2016
journal: eLife
paper_type: computational
contribution_type: theoretical
---

### One-line summary

A single-layer neural network with non-negative feedforward weights, performing a biologically constrained variant of PCA on place cell inputs, spontaneously develops hexagonal grid cell firing patterns consistent with experimental observations.

---

### Background & motivation

Dominant models of grid cell formation assume velocity-based path integration as the primary input. However, experimental findings — including evidence that hippocampal place cells precede grid cells developmentally and that inactivating place cells abolishes grid cell patterns — suggest that feedback from place cells to grid cells may play a fundamental role in grid cell formation. The paper addresses the question of how this place-to-grid feedback projection could, in principle, generate hexagonally periodic grid cell firing. A key prior computational result (Stachenfeld et al., 2014) showed that unconstrained PCA on place cell inputs yields square-like, not hexagonal, patterns, leaving the mechanism for hexagonality unexplained.

---

### Methods

- **Model architecture**: Single-layer feedforward neural network with place-cell-like inputs (2D Gaussians on a virtual arena) projecting to a single grid cell output.
- **Learning rule**: Oja's self-normalising Hebbian rule, which causes weights to converge to the principal eigenvector of the input covariance matrix — implementing online PCA.
- **Non-negativity constraint**: Feedforward weights constrained to be non-negative (rectification), motivated by the known anatomy of excitatory hippocampus-to-entorhinal projections.
- **Zero-mean inputs**: Required for PCA; achieved via (a) time-differentiation of place cell activity, (b) Mexican-hat / Laplacian spatial input profiles, (c) positive-negative disk inputs, or (d) an adaptation variable subtracting a running mean of output activity.
- **Direct non-negative PCA**: Three numerical algorithms (NSPCA, AMP, FISTA) applied to the input covariance matrix for comparison with the network results.
- **Validation metrics**: Hexagonal Gridness score (rotational autocorrelation at 60° intervals) and Square Gridness score (45° intervals), over ~1500 simulations per condition.
- **Modules**: Hierarchical multi-output network (Sanger, 1989 rule) to extract successive non-negative principal components and examine discrete grid spacing modules.
- **Stability**: ODE analysis (stochastic approximation framework) to characterise asymptotic equilibria.
- **Fourier analysis**: Analytical treatment to explain why non-negativity selects hexagonal over square solutions in terms of k-space structure.

---

### Key findings

- Without the non-negativity constraint, both the neural network and direct PCA converge to square-like periodic solutions (hexagonal Gridness = 0.302 ± 0.003 for network; 0.27 ± 0.0023 for PCA).
- With non-negative weights and zero-mean input, both methods robustly converge to hexagonal grid cell patterns (hexagonal Gridness = 1.07 ± 0.003 for network; 1.13 ± 0.0022 for PCA); square Gridness simultaneously drops (0.073 ± 0.006 and 0.1 ± 0.006 respectively).
- The hexagonal solution is stable across diverse initial conditions (random, stripe, square, rhomboidal, noisy hexagonal initialisation) and across novel trajectory realisations.
- Grid spacing scales linearly with place cell field width: S = 7.5σ + 0.85 (periodic boundary conditions), consistent with dimensional analysis predictions.
- In the large-environment limit, grid orientation approaches a uniform distribution over 0–15°; grid orientation is not a function of Gridness score.
- A hierarchical multi-output network produces two discrete modules of grid spacing, with inter-module ratio ≈ √2 ≈ 1.4, consistent with Stensola et al. (2012).
- Fourier analysis shows that the non-negativity constraint forces a hexagonal set of strong Fourier components near the peak of the place cell tuning curve transform, with a positive DC component to maintain non-negativity; the hexagonal arrangement is the unique way to pack six vectors of equal magnitude with equal angles.

---

### Computational framework

**Non-negative Principal Component Analysis (Non-negative PCA) / Oja Hebbian learning rule.**

The model formalises the place-to-grid projection as a variance-maximisation problem. The network learns the feedforward weight vector J that maximises output variance (i.e. the leading eigenvector of the place cell covariance matrix S), subject to J ≥ 0. This is the non-negative PCA problem. Key variables: J (weight vector / grid cell spatial representation), r(t) (place cell activity at time t), ε[t] (learning rate), Gridness score (hexagonality measure of the converged weights projected to arena space). Core assumptions: (1) place cell inputs have zero temporal mean; (2) feedforward weights are non-negative (excitatory synapses); (3) place cells tile the environment with overlapping Gaussian (or Mexican-hat) tuning curves; (4) the animal's trajectory is ergodic. The framework provides both a mechanistic (neural network) and a mathematical (direct non-negative PCA) account of the same solution.

---

### Prevailing model of the system under study

The dominant framework before and around this paper held that grid cells in medial entorhinal cortex are generated by path integration: velocity inputs are integrated over time to produce a periodic spatial representation, with grid cells sitting upstream of hippocampal place cells and providing positional information to them. Most computational models of grid cell formation (attractor-based, oscillatory interference) used velocity as the primary input and treated the grid-to-place direction as the functionally important projection. The existence of the anatomically documented feedback from place cells to grid cells was known but largely ignored in modelling. The paper by Stachenfeld et al. (2014) had noted the conceptual link between PCA and the place-to-grid transformation but found only square-like solutions because the non-negativity constraint was not applied.

---

### What this paper contributes

The paper demonstrates that a biologically motivated constraint — non-negativity of place-to-grid synaptic weights, corresponding to the known excitatory anatomy — is both necessary and sufficient to explain why grid cells have hexagonal rather than square symmetry when derived from place cell inputs via a Hebbian/PCA mechanism. This resolves the puzzle left open by Stachenfeld et al. (2014). More broadly, it establishes a fully place-cell-driven, path-integration-free developmental mechanism for grid cell formation. The model also makes quantitative predictions: linear scaling of grid spacing with place field size, uniform orientation distribution (0–15°) for large arenas, and a two-module structure with ratio ≈ √2 — the last being consistent with experimental data. The paper thus positions place-to-grid feedback as a viable primary mechanism for grid cell formation, challenging the path-integration-first orthodoxy.

---

### Brain regions & systems

- **Hippocampus (CA1/CA3)** — source of place cell inputs to the model; place cells provide the spatially localised, Gaussian-shaped input that drives grid cell learning.
- **Medial entorhinal cortex (MEC)** — location of grid cells in vivo; the model's output layer represents MEC grid cell outputs.
- **Hippocampus-to-MEC feedback projection** — the anatomically identified excitatory projection from hippocampus to MEC is the central biological motivation for the non-negativity constraint.

---

### Mechanistic insight

The paper meets criterion 1 (it formalises an algorithm — non-negative PCA via Oja's rule) but does not meet criterion 2 (it provides no neural recording, imaging, lesion, or pharmacological data). All evidence for the model is computational (simulation) and analytical (Fourier/ODE analysis). The paper does not provide neural data specifically linking the non-negative PCA algorithm's variables (e.g. the learned weight vector, the eigenvalue structure of place cell covariance) to measured neural activity in entorhinal cortex. It thus does not meet the bar for a full mechanistic insight entry.

---

### Limitations & open questions

- The model predicts only two grid modules, whereas experimental data (Stensola et al., 2012) show at least five; the discrepancy is acknowledged but unresolved.
- The model predicts a uniform grid orientation distribution over 0–15° in large arenas, but experimental data show a peak at 7.5° (Stensola et al., 2015) — a mismatch the authors attribute to the absence of bidirectional (grid-to-place) coupling in the current model.
- The place cells used as inputs have homogeneous field widths; incorporating the known non-uniform distribution of hippocampal place field sizes (Kjelstrup et al., 2008) is left as future work.
- The model treats the place-to-grid projection in isolation; a "closed-loop" model incorporating simultaneous grid-to-place and place-to-grid interactions remains to be built.
- How zero-mean input is biologically implemented in place cells (via interneurons, adaptation, or Mexican-hat-like lateral inhibition) is speculative.
- The non-negative PCA problem is NP-hard; the model relies on numerical algorithms whose convergence to global optima is not guaranteed in general.

---

### Connections & keywords

**Key citations**:
- Oja (1982) — Oja's self-normalising Hebbian learning rule
- Sanger (1989) — hierarchical multi-output PCA network
- Stachenfeld, Botvinick & Gershman (2014) — predecessor linking place cells, grid cells, and PCA (without non-negativity)
- Kropff & Treves (2008) — place-cell-driven grid cell model using firing-rate adaptation
- Bonnevie et al. (2013) — inactivation of hippocampus abolishes grid cell patterns
- Langston et al. (2010) / Wills et al. (2010) — place cells precede grid cells developmentally
- Stensola et al. (2012) — discrete grid spacing modules and √2 ratio
- Stensola et al. (2015) — grid orientation at 7.5°
- Witter & Amaral (2004) — anatomy of hippocampal-entorhinal projections
- Mathis et al. (2015) / Wei et al. (2013) — information-theoretic optimality of hexagonal grids
- Beck & Teboulle (2009) — FISTA algorithm

**Named models or frameworks**:
- Non-negative Principal Component Analysis (Non-negative PCA)
- Oja learning rule
- Sanger hierarchical network
- Generalized Hebbian algorithm
- NSPCA (Nonnegative Sparse PCA)
- Approximate Message Passing (AMP)
- FISTA (Fast Iterative Shrinkage-Thresholding Algorithm)
- Gridness score (Sargolini et al., 2006)

**Brain regions**:
- Hippocampus (CA1, CA3) — place cells
- Medial entorhinal cortex (MEC) — grid cells

**Keywords**:
- grid cells
- place cells
- non-negative PCA
- Hebbian learning
- Oja rule
- hexagonal firing patterns
- place-to-grid projection
- spatial navigation
- grid spacing modules
- path integration alternatives
- entorhinal cortex
- feedforward excitatory connectivity
