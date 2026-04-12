---
source_file: sorscher2022_grid_cells_path_integration.md
paper_id: sorscher2022_grid_cells_path_integration
title: "When and why grid cells appear in trained path integrators"
authors:
  - "Ben Sorscher"
  - "Gabriel C. Mel"
  - "Aran Nayebi"
  - "Lisa Giocomo"
  - "Daniel Yamins"
  - "Surya Ganguli"
year: 2022
journal: bioRxiv
paper_type: computational
contribution_type: theoretical
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
keywords:
  - grid_cells
  - path_integration
  - pattern_formation
  - place_cells
  - neural_network_training
  - entorhinal_cortex
  - spatial_navigation
  - fourier_analysis
  - correlation_structure
  - computational_neuroscience
  - deep_learning
  - spectral_theory
  - receptive_fields
  - dorsoventral_organization
  - when
  - why
  - grid
  - cells
  - appear
  - trained
key_citations:
  - schaeffer2022_no_free_lunch_deep_learning_neuroscience
wiki_pages:
  - wiki/debates/grid_cells_as_a_mechanism_for_path_integration
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
---

### One-line summary

Grid cells robustly emerge from trained path-integrator circuits precisely when prior theory predicts they should, and claims of fragility result from failing to follow the theoretical conditions.

---

### Background & motivation

Recent work by Schaeffer et al. (2022) claimed that grid cell emergence in trained path-integrators is more fragile than previously reported, suggesting prior work involved non-transparent fine-tuning. This paper critically assesses those claims within the context of established theoretical frameworks, demonstrating that the apparent fragility reflects deviations from theoretically predicted necessary conditions rather than genuine instability in the phenomenon itself.

---

### Methods

- **Computational simulations**: Training of path-integrator neural networks to convert velocity inputs into place cell outputs through hidden units
- **Theoretical analysis**: Application of prior theory from Sorscher et al. (2019, 2020) linking place cell correlation structure to grid cell emergence
- **Replication studies**: Reproduction of key findings from Schaeffer et al. (2022) with corrected implementations
- **Parameter sweeps**: Systematic variation of place cell receptive field widths (0.11-0.13m range) to test robustness
- **Network architecture**: Single-layer hidden units with ReLU or tanh nonlinearities, trained on different place cell target structures

---

### Key findings

- **Robust emergence under correct conditions**: When two key conditions from prior theory are met (nonzero negativity cost in the nonlinearity, and narrow center-surround place cell correlation structure with large radius Fourier annulus), hexagonal grid cells emerge reliably in close to 100% of trained networks without fine-tuning
- **DoG structures work with proper normalization**: Difference of Gaussians (DoG) place cell structures can reliably generate hexagonal grids when properly normalized, contrary to claims in Schaeffer et al. (2022); the apparent failure in that work resulted from an improper normalization that removed the necessary Fourier annulus structure
- **Multiple field place cells can yield grids**: Place cells with multiple fields at a single scale can generate hexagonal grid cells, as the key determinant is the correlation structure (center-surround annulus in Fourier space) rather than unimodal place field structure
- **Robustness to scale changes**: Grid cell emergence is robust to small changes in place cell scale (e.g., 0.11-0.13m range); networks trained across this range all produced hexagonal grids with grid scores exceeding thresholds used in Schaeffer et al. (2022), and grid scale varied smoothly with place cell scale
- **Gaussian place cells can generate periodic patterns**: Contrary to a claimed proof in Schaeffer et al. (2022), Gaussian place cell targets can produce periodic patterns (stripes, squares) in trained networks; the proof's conclusion is inconsistent with simulation results and contains incompletenesses in its linear stability analysis
- **Reinterpretation of fragility claims**: The low grid cell rates reported in Schaeffer et al. (2022) (~10% of 11,000 networks) reflect that most of their parameter choices violated theoretical conditions for grid emergence; when conditioned on correct conditions, they actually obtained high rates, consistent with prior predictions

---

### Computational framework

**Pattern formation theory applied to neural network learning**

The paper employs a theoretical framework from pattern formation theory, adapted to analyze how grid cell representations emerge from training path-integrator networks. The core formalism involves:

- **Position encoding problem**: Converting velocity inputs to place cell outputs through hidden units, framed as an optimization problem where hidden unit firing rates g(x) must generate desired place cell input currents p_i(x)

- **Correlation structure (Σ matrix)**: The nx × nx matrix describing similarity in place cell input currents across spatial locations. The eigenstructure of this matrix determines the nature of solutions

- **Fourier decomposition**: Eigenvectors are approximated as Fourier plane waves indexed by spatial frequencies (kx, ky). The eigenvalues correspond to power in each Fourier mode

- **Annulus structure in Fourier space**: Center-surround place cell correlation structures produce maximal eigenvalues near an annulus in the (kx, ky) plane; the narrower the spatial correlation, the larger the annulus radius

- **Nonnegativity constraint**: The cost function includes a negativity cost σ(g) that promotes positive firing rates. This breaks the degeneracy among equally optimal Fourier combinations, favoring 3-fold combinations of eigenvectors whose frequencies form equilateral triangles (predicting hexagonal grids)

The framework assumes translation-invariant statistics and connects the spatial correlation structure of place cells to the geometric patterns learned by hidden units through spectral analysis of the optimization landscape.

---

### Prevailing model of the system under study

The paper addresses claims about the emergence of grid cells in trained path-integrator neural networks. The prevailing theoretical understanding, established by Sorscher et al. (2019, 2020), holds that:

1. Grid cells emerge from training path-integrators when specific conditions are met: the place cell targets must have narrow center-surround correlation structure (producing a large-radius annulus of high Fourier power), and the hidden units must be subject to a nonnegativity constraint

2. The nonnegativity constraint breaks the degeneracy among equally optimal Fourier mode combinations, specifically favoring 3-fold combinations forming equilateral triangles in frequency space, which produce hexagonal grid patterns

3. The geometric structure of learned grid cells (square, heterogeneous, or hexagonal) is determined by the spectral properties of the place cell correlation matrix and the presence/absence of constraints on hidden unit activity

This theoretical framework was claimed by Schaeffer et al. (2022) to be based on non-transparent fine-tuning and to predict fragile, rather than robust, grid cell emergence. The introduction signals this debate as the paper's central focus.

---

### What this paper contributes

This paper demonstrates that the apparent fragility of grid cell emergence claimed by Schaeffer et al. (2022) reflects methodological deviations from established theoretical conditions rather than genuine instability in the phenomenon. The work refines and defends the prevailing model by showing that:

1. **Grid cells emerge robustly when theory's conditions are met**: Contrary to claims of ~10% success rates, hexagonal grid cells emerge in close to 100% of trained networks when both key theoretical conditions are satisfied (proper place cell correlation structure and nonnegativity constraints)

2. **Prior theory correctly predicts when grids will and won't appear**: The specific combinations of parameters that failed to produce grids in Schaeffer et al. (2022) were precisely those that theory predicts should not produce grids, making the overall ~10% rate consistent with theoretical expectations

3. **DoG structures work with proper implementation**: The claim that Difference of Gaussians place cell structures cannot produce hexagonal grids is incorrect; with proper normalization, DoG produces identical grid score distributions to DoS structures

4. **Gaussian place cells can generate periodic patterns**: The claimed mathematical proof that Gaussian interactions cannot produce periodic patterns is both incomplete and inconsistent with simulation results

5. **Grid emergence is robust to scale variations**: Small changes in place cell scale (e.g., 10cm to 12cm) do not cause grid cells to disappear; instead, grid scale varies smoothly with place cell scale as theory predicts

The paper establishes that the field's theoretical understanding of grid cell emergence is more robust and predictively accurate than challenged by Schaeffer et al. (2022), provided the theoretical conditions are properly implemented.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — contains grid cells that exhibit spatially periodic firing patterns; the paper models how these representations might emerge through learning
- **Hippocampus** — contains place cells that serve as the target output for the modeled path-integrator circuits; the paper examines how place cell structure (single vs. multiple fields, correlation structure) influences grid cell emergence
- **Entorhinal-hippocampal circuit** — the paper models the transformation from velocity inputs to place cell outputs through hidden units (putative grid cells), addressing how grid cell representations emerge from training this circuit to perform path integration

The paper explicitly adopts a simplified single-scale modeling approach motivated by the topographic organization of grid scale along the dorsoventral axis of MEC, where grid cells at different scales are found at different anatomical locations.

---

### Mechanistic insight

This paper meets the high bar for mechanistic insight, presenting both a formal algorithm and neural data supporting that algorithm over alternatives. The work maps the evidence onto Marr's three levels:

**Computational level**: The brain solves a position encoding problem — converting velocity inputs into spatial representations. The problem is formalized as finding hidden unit firing rates g(x) that can generate desired place cell input currents p_i(x) through a linear transformation. The correlation structure of place cells (Σ matrix) determines the optimal solutions.

**Algorithmic level**: The solution emerges through spectral analysis of the place cell correlation matrix. The eigenvectors are Fourier plane waves indexed by spatial frequencies (kx, ky). The key algorithmic insight is that:
1. Center-surround place cell correlation structures produce maximal eigenvalues near an annulus in frequency space
2. The nonnegativity constraint on hidden units breaks the degeneracy among equally optimal Fourier combinations
3. Specifically, the nonnegativity constraint favors 3-fold combinations of eigenvectors whose frequencies form equilateral triangles in (kx, ky) space
4. These combinations predict hexagonal grid patterns

The paper provides neural network simulation data showing that when these algorithmic conditions are met, hexagonal grid cells emerge robustly in trained networks.

**Implementational level**: The implementation involves:
- Single-layer hidden units with ReLU or tanh nonlinearities (imposing nonnegativity or negativity costs)
- Learned weights connecting velocity inputs to hidden units and hidden units to place cell outputs
- Training via gradient descent on the position encoding objective
- The specific nonlinearity matters: ReLU and Sigmoid have nonzero negativity costs that favor hexagonal grids, while linear and tanh (without proper constraints) do not

The paper demonstrates that with proper implementation of the algorithmic constraints (correct normalization of place cell structures, appropriate nonlinearities), hexagonal grid cells emerge in close to 100% of trained networks, confirming the physical realizability of the computational and algorithmic framework.

---

### Limitations & open questions

- **Multiple grid scales**: The paper notes that questions regarding multiple grid scales were outside the scope of the prior theory [3, 4]. The biological reality that grid cells at different scales are found at different locations along the dorsoventral axis motivates the single-scale modeling approach, but a unified theory handling multiple scales simultaneously remains an open question.
- **Optimization details**: The paper acknowledges that their simulations used higher learning rates and shorter training times than prior work to speed up training of many networks, which led to "dead ReLUs" (hidden units that never fire) and lower absolute fractions of grid cells. The optimization dynamics of training path-integrators, especially the phenomenon of dead ReLUs at high learning rates, may affect grid cell emergence patterns.
- **Biological plausibility of DoG/DoS inputs**: While the paper argues that center-surround place cell input currents from grid cells are difficult to rule out experimentally, the actual biological mechanisms generating these input patterns remain to be determined. The relationship between subthreshold input currents and observed place cell firing rates requires further experimental investigation.
- **Temperature/finite energy effects**: The paper notes that the global minimum of the pattern formation problem does not uniquely specify what every learned grid cell will do, and suggests that "low energy configurations of the pattern formation problem at some finite temperature more correctly characterize the distribution of grid cells that appear in neural network training," though this was not explored in depth.

---

### Connections & keywords

**Key citations:**
- Cueva & Wei (2018) — Emergence of grid-like representations by training RNNs to perform spatial localization
- Banino et al. (2018) — Vector-based navigation using grid-like representations in artificial agents
- Sorscher et al. (2019) — A unified theory for the origin of grid cells through the lens of pattern formation
- Sorscher et al. (2020) — A unified theory for the computational and mechanistic origins of grid cells (Neuron)
- Hafting et al. (2005) — Microstructure of a spatial map in the entorhinal cortex (discovery of grid cells)
- Schaeffer et al. (2022) — No free lunch from deep learning in neuroscience (the work being critiqued)

**Named models or frameworks:**
- Path-integrator circuits / position encoding problem
- Pattern formation theory
- Difference of Softmaxes (DoS) place cell structure
- Difference of Gaussians (DoG) place cell structure
- Fourier/spectral analysis of place cell correlation matrices
- Nonnegative firing rate constraints

**Brain regions:**
- Medial entorhinal cortex (MEC)
- Hippocampus
- Entorhinal-hippocampal circuit

**Keywords:**
grid cells, path integration, pattern formation, place cells, neural network training, entorhinal cortex, spatial navigation, Fourier analysis, correlation structure, computational neuroscience, deep learning, spectral theory, receptive fields, dorsoventral organization

### Related wiki pages
- [[wiki/debates/grid_cells_as_a_mechanism_for_path_integration|Grid cells as a mechanism for path integration]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
