---
source_file: schaeffer_grid_cell_pathintegration.md
paper_id: schaeffer_grid_cell_pathintegration
title: "Disentangling Fact from Grid Cell Fiction in Trained Deep Path Integrators"
authors:
  - "Rylan Schaeffer"
  - "Mikail Khona"
  - "Sanmi Koyejo"
  - "Ila Rani Fiete"
year: 2023
journal: "arXiv (response paper, original NFL in NeurIPS 2022)"
paper_type: computational
contribution_type: theoretical
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - grid_cells
  - path_integration
  - deep_recurrent_neural_networks
  - entorhinal_cortex
  - spatial_navigation
  - continuous_attractor_networks
  - fourier_analysis
  - supervised_learning
  - neural_predictivity
  - emergence
  - optimization
  - representation_learning
  - disentangling
  - fact
  - grid
  - cell
  - fiction
  - trained
  - deep
  - path
key_citations:
  - schaeffer2022_no_free_lunch_deep_learning_neuroscience
  - sorscher2022_neural_geometry_few_shot
wiki_pages:
  - wiki/debates/grid_cells_as_a_mechanism_for_path_integration
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
---

### One-line summary

Grid cells do not emerge naturally from path integration in deep neural networks; they only appear when researchers explicitly design supervised targets to produce grid-like tuning, challenging the "path integration hypothesis."

### Background & motivation

Several high-profile papers (Nature, Neuron, NeurIPS) claimed that grid cells emerge generically and robustly when recurrent neural networks are trained to path integrate. This "path integration hypothesis" suggests that simply optimizing networks to track spatial position from velocity inputs naturally produces grid-like representations. However, this claim contradicts prior numerical results and theoretical work suggesting grid codes have special coding-theoretic properties beyond path integration. The authors previously challenged this hypothesis in their "No Free Lunch" (NFL) paper, showing that grid cells do not emerge naturally from path integration. This paper restates that evidence and addresses a response from proponents of the path integration hypothesis.

### Methods

- **Large-scale hyperparameter sweeps**: Trained over 11,000 deep recurrent neural networks to path integrate with different architectures, supervised targets, and hyperparameters
- **Multiple supervised target types**: Compared Cartesian, Polar, Gaussian, Difference-of-Gaussians (DoG), and Difference-of-Softmaxes (DoS) supervised targets
- **Grid scoring**: Used standard 60° and 90° grid scores to quantify hexagonal and square lattice-like tuning
- **Architecture variations**: Compared ReLU vs Tanh nonlinearities, different dropout rates, learning rates, optimizers, and network sizes (1024 vs 4096 units)
- **Null distribution comparisons**: Compared network grid scores against filtered-and-thresholded noise to determine statistical significance
- **Theory reproduction**: Reproduced and analyzed the "Unified Theory" of grid cell emergence from Sorscher et al.

### Key findings

- **Path integration does not produce grid cells**: Most networks (regardless of supervised target) successfully learned to path integrate, but very few developed grid-like tuning
- **DoS targets are required for grid cells**: Grid-like tuning only appeared when researchers used specifically designed Difference-of-Softmaxes (DoS) supervised targets that embed grid-like tuning into the target function itself
- **DoS is not functionally or biologically motivated**: The DoS target does not improve path integration performance and has no biological justification
- **Gaussian targets do not produce grids**: Extensive sweeps over Gaussian receptive field widths with both ReLU and Tanh nonlinearities failed to produce grid-like tuning
- **The "Unified Theory" is insufficient**: The Unified Theory's predicted conditions for grid emergence (Fourier power on an annulus of appropriate radius) are necessary but not sufficient
- **Narrow hyperparameter sensitivity**: Even within the theoretically predicted parameter range, grid-like tuning only occasionally emerged and was highly seed-dependent
- **Non-negativity produces both hexagonal and square lattices**: Contrary to the Unified Theory's prediction that non-negativity favors hexagonal lattices, ReLU networks consistently produced both hexagonal (60°) and square (90°) lattices simultaneously
- **Neural regression methodology is flawed**: Neural predictivity scores in regression analyses correlate with effective dimensionality rather than biological plausibility, allowing high-dimensional models to achieve better scores without being better biological models

### Computational framework

The paper operates within the framework of **deep recurrent neural networks (RNNs) trained for path integration**. The core computational problem is: given velocity inputs over time, integrate to estimate current position. The networks are trained with supervised learning to predict target position representations (various schemes: Cartesian coordinates, polar coordinates, Gaussian place fields, DoG, DoS).

The paper extensively engages with the **"Unified Theory" of Sorscher et al.**, which frames grid cell emergence as a problem of Fourier structure in supervised targets. This theory treats the problem as static function approximation (readout reconstruction) rather than dynamic path integration. The theory uses a Lagrangian formulation with assumptions about orthonormality of hidden representations and translational invariance of readouts.

The paper also references **continuous attractor network theory**, which explains grid cells through pattern formation in neural sheets with translation-invariant connectivity (Mexican-hat connectivity profiles). This is contrasted with the supervised learning approach.

### Prevailing model of the system under study

The prevailing model (the "path integration hypothesis") asserts that grid cells emerge generically and robustly when recurrent neural networks are trained to path integrate. This claim, advanced in multiple high-profile publications (Nature, Neuron, NeurIPS), suggests that:

1. Simply optimizing networks to track spatial position from velocity inputs naturally produces grid-like representations
2. Grid cells are a surprising, emergent consequence of path integration optimization
3. Non-negativity constraints (e.g., ReLU) favor hexagonal grid patterns over square lattices
4. The "Unified Theory" provides a complete theoretical account of grid cell emergence in trained path integrators

This prevailing model treats grid cells as functionally motivated by path integration, implying that the grid code is simply what optimal path integration looks like in neural networks.

### What this paper contributes

This paper fundamentally challenges the path integration hypothesis and demonstrates that:

1. **Grid cells are not emergent from path integration**: Deep networks trained to path integrate almost always learn to path integrate successfully, but almost never learn grid-like tuning unless researchers explicitly insert it via specially designed supervised targets (DoS).

2. **DoS targets "bake in" grid cells**: The Difference-of-Softmaxes (DoS) supervised target, which is required for grid-like tuning, is explicitly designed to place Fourier power on an annulus of a specific radius. This embeds grid-like tuning into the target function itself, making grid cell emergence a researcher's design choice rather than an emergent property.

3. **The "Unified Theory" is incomplete**: The Unified Theory is not a theory of path integration or deep RNN learning dynamics—it's a theory of Fourier structure in supervised targets. Its predictions are at best "occasionally suggestive," not exact or comprehensive. Even within theoretically predicted parameter ranges, grid-like tuning only occasionally emerges and is highly seed-dependent.

4. **Non-negativity does not exclusively favor hexagons**: Contrary to the Unified Theory's prediction, ReLU networks (with non-negativity) consistently produce both hexagonal (60°) and square (90°) lattices simultaneously, not just hexagonal patterns.

5. **Neural regression methodology is flawed**: The paper demonstrates that neural predictivity scores in regression analyses correlate with effective dimensionality rather than biological plausibility. This allows high-dimensional models to achieve better predictivity scores without being better biological models, calling into question a widely-used methodology in computational neuroscience.

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — the brain region containing grid cells; the paper focuses on evaluating whether trained deep path integrators are valid models of MEC grid cells
- **Hippocampus** — mentioned in the context of the entorhinal-hippocampal circuit

The paper is primarily computational, using deep RNNs as models of MEC. The neural systems focus is on evaluating whether these artificial networks capture the actual biological properties of MEC grid cells.

### Mechanistic insight

The paper does **not** meet the high bar for mechanistic insight because it does not present a specific algorithm supported by neural data that explains grid cell formation. Instead, it is a critique of existing models. However, the paper does provide important conceptual insights:

**Computational level**: The paper argues that path integration alone is insufficient to explain grid cell emergence. The actual computational problem being solved by biological grid cells may involve coding-theoretic optimization (error correction, spatial code packing) rather than just position tracking.

**Algorithmic level**: The paper critiques the "Unified Theory" as being a theory of supervised target Fourier structure rather than a theory of how RNNs learn to path integrate. The actual learning dynamics of gradient descent in RNNs are not captured by the static optimization framework of the Unified Theory.

**Implementational level**: The paper does not address specific biological implementation details (cell types, connectivity, neuromodulators). It does note that the Unified Theory's assumptions (orthonormal ratemaps, translational invariance of readouts) are biologically implausible.

The paper's main contribution is negative—showing what does NOT explain grid cells—rather than proposing a positive mechanistic account.

### Limitations & open questions

- **Limited biological constraints**: The deep RNN models used in this study and the ones it critiques use simplified architectures that may not capture key biological constraints (e.g., specific cell types, Dale's principle, realistic synaptic dynamics).
- **Alternative training objectives**: The paper notes that self-supervised learning combining path integration with coding-theoretic objectives can produce multi-modular grid cells without supervised targets, but this direction requires further investigation.
- **Neural regression methodology**: The paper identifies problems with using neural regression to validate models but does not provide a complete alternative validation framework.
- **What is sufficient for grid cells?**: The paper establishes that path integration is insufficient but does not fully resolve what combination of computational objectives and biological constraints would be sufficient for grid cell emergence.
- **Multiple grid modules**: The paper notes that multiple grid modules (a key biological property) do not emerge from the Unified Theory framework, and their artificial networks do not reproduce biological grid module ratios.

### Connections & keywords

**Key citations**: 
- Hafting et al. 2005 (original grid cell discovery)
- Sorscher et al. 2019, 2020, 2022 (Unified Theory papers, Neuron)
- Banino et al. 2018 (Nature grid cell paper)
- Cueva & Wei 2018 (ICLR grid cell paper)
- Nayebi et al. 2021 (NeurIPS, neural predictivity)
- Schaeffer et al. 2022 (NFL paper, NeurIPS)
- Sorscher et al. 2022 (Response to NFL)
- Khona & Fiete 2022 (attractor networks review)
- Burak & Fiete 2009 (continuous attractor models)

**Named models or frameworks**:
- Path Integration Hypothesis
- Unified Theory of grid cell emergence (Sorscher et al.)
- Difference-of-Softmaxes (DoS) supervised targets
- Difference-of-Gaussians (DoG) supervised targets
- Continuous attractor network theory
- Neural regression methodology

**Brain regions**:
- Medial entorhinal cortex (MEC)
- Hippocampus

**Keywords**:
- grid cells
- path integration
- deep recurrent neural networks
- entorhinal cortex
- spatial navigation
- continuous attractor networks
- Fourier analysis
- supervised learning
- neural predictivity
- emergence
- optimization
- representation learning

### Related wiki pages
- [[wiki/debates/grid_cells_as_a_mechanism_for_path_integration|Grid cells as a mechanism for path integration]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
