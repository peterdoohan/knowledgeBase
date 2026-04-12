---
source_file: pettersen2024_self_supervised_grid_cells.md
paper_id: pettersen2024_self_supervised_grid_cells
title: "Self-Supervised Grid Cells Without Path Integration"
authors:
  - "Markus Pettersen"
  - "Vemund Sigmundson Schøyen"
  - "Mattis Dalsætra Østby"
  - "Anders Malthe-Sørenssen"
  - "Mikkel Elle Lepperød"
year: 2024
journal: "bioRxiv preprint"
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
  - band_cells
  - path_integration
  - self_supervised_learning
  - distance_preservation
  - capacity_constraints
  - recurrent_neural_networks
  - feedforward_networks
  - spatial_navigation
  - toroidal_topology
  - persistent_homology
  - normative_models
  - entorhinal_cortex
  - metric_learning
  - self
  - supervised
  - grid
  - cells
  - without
  - path
key_citations:
  - sorscher2022_neural_geometry_few_shot
  - schaeffer_grid_cell_pathintegration
  - moser2008_place_cells_grid_cells
  - burak2009_path_integration_grid_cells
wiki_pages:
  - wiki/debates/grid_cells_as_a_mechanism_for_path_integration
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
---

### One-line summary

Grid cells emerge in neural networks trained solely on distance preservation under capacity constraints, without requiring path integration, and band cells (not grid cells) are primarily responsible for path integration in recurrent networks.

---

### Background & motivation

Grid cells in the medial entorhinal cortex display regular hexagonal firing patterns and have been hypothesized to support path integration, spatial metric formation, vector navigation, and memory. However, the exact function of grid cells remains debated. While many computational models assume grid cells are path integrators, recent evidence suggests grid cells may not be necessary for path integration. This paper investigates whether grid cells emerge from simpler objectives than path integration, and whether they are actually required for path integration in artificial neural networks.

---

### Methods

- **Task design**: Two neural network models trained on spatial encoding tasks:
  - **Feedforward network (FF)**: 2 hidden layers (64, 128 units) → 256 output units; receives 2D Cartesian coordinates directly
  - **Recurrent network (RNN)**: 256 recurrent units; receives initial position + velocity inputs; must learn path integration implicitly
- **Training regime**: 
  - FF: 100,000 steps; RNN: 50,000 steps; batch size 64
  - Adam optimizer (lr=1e-3)
  - Training data: random trajectories in 4π × 4π square arena (bouncing boundary conditions)
- **Objective function**: Two-term loss combining:
  - **Distance preservation**: Gaussian-weighted penalty on differences between neural and physical Euclidean distances over small spatial scales (σ = 1.2)
  - **Capacity constraint**: L1 norm penalty encouraging distributed, high-capacity representations (α = 0.54)
- **Output constraint**: normReLU activation ensuring non-negative, unit L2-norm representations
- **Velocity pruning analysis**: Systematic ablation of velocity inputs to subpopulations to assess path integration contribution
- **Analysis methods**: Grid score computation, persistent homology (Ripser), UMAP visualization, connectivity analysis

---

### Key findings

- Both FF and RNN models develop highly grid-like representations (hexagonal firing patterns) when trained on distance preservation with capacity constraints, despite the FF network having no path integration mechanism
- Grid score distributions are similar between FF and RNN models, with unimodal spacing distributions and uniform phase distributions
- The RNN exhibits a small subpopulation of band-like cells (low grid score, ~29 units with grid score < 0.15) not seen in the FF model
- **Velocity pruning reveals**: Path integration error is strongly negatively correlated with grid score—pruning band cells severely impairs path integration, while pruning high grid-score cells has minimal effect
- Persistent homology and UMAP projections show both models learn toroidal manifold structures (one 0D, two 1D, one 2D persistent cocycles)
- The RNN shows short-range excitation/long-range inhibition connectivity patterns between units with neighboring grid phases, consistent with continuous attractor models; band cells show phase-shifted connectivity profiles
- FF networks fail to generalize grid patterns outside training domain (non-periodic basis functions); RNNs generalize when initialized inside training domain but path integrate outward, but fail when initialized outside

---

### Computational framework

**Normative/self-supervised learning with geometric constraints**

The paper proposes a minimal normative framework where grid cells emerge from two computational principles:

1. **Distance preservation (computational level)**: The network must solve the problem of preserving local spatial distances in its neural representation—nearby locations in physical space should map to nearby points in the neural state space. This is formalized as minimizing the difference between Euclidean distances in the neural representation and physical Cartesian distances, weighted by a Gaussian envelope.

2. **Capacity maximization (algorithmic level)**: Under the constraint of fixed output dimensionality and normalization, the network must maximize representational capacity. This is achieved through an L1 capacity term that encourages distributed, correlated activity where the population vector occupies minimal state space volume—ideally clustering near the diagonal (all units coactive).

The framework suggests grid cells form a **high-capacity, distance-preserving metric for space** rather than being specialized for path integration per se. The hexagonal periodicity emerges as the optimal solution to these competing constraints, with the grid pattern's translational symmetry enabling efficient distance preservation while maintaining distributed, high-fidelity representations.

---

### Prevailing model of the system under study

The prevailing view in the literature, as described in the paper's introduction, holds that:

1. **Grid cells are path integrators**: Grid cells are widely believed to be the neural substrate for path integration—the ability to update one's position based on self-motion cues. This view is supported by continuous attractor network models (e.g., Burak & Fiete 2009) showing grid cells can theoretically perform path integration, and by the observation that grid-like representations emerge in RNNs trained to path integrate.

2. **Grid cells support multiple navigational functions**: Beyond path integration, grid cells are thought to provide a neural metric for space, enable vector navigation, and support memory and inference through their periodic, spatially organized firing patterns.

3. **Emergence of grid cells implies path integration function**: The correlation between grid-like representation emergence and path integration training has been interpreted as evidence that grid cells evolved/developed specifically for path integration.

The authors note that this prevailing model has been challenged by recent interventional studies (e.g., Nayebi et al. 2021; Schøyen et al. 2023) showing that grid cell ablation does not impair path integration, while band cell ablation does.

---

### What this paper contributes

This paper makes several key contributions that challenge and refine the prevailing model:

1. **Grid cells can emerge without path integration**: The authors demonstrate that highly grid-like representations emerge in a feedforward network trained solely on distance preservation with capacity constraints—no path integration mechanism, no recurrent connections, and no velocity inputs. This dissociates grid cell emergence from the path integration task, showing that grid cells are not defined by or exclusive to path integration.

2. **Grid cells are not necessary for path integration in RNNs**: In the recurrent network trained to path integrate, the authors find that ablating grid cells (by pruning velocity inputs to high grid-score units) has minimal impact on path integration performance. Conversely, ablating band cells severely impairs path integration. This provides causal evidence that band cells, not grid cells, are the primary neural substrate for path integration in their model.

3. **A minimal normative model**: The paper provides a parsimonious explanation for grid cell emergence based on just two principles: local distance preservation and capacity maximization. This is simpler than previous models requiring path integration objectives, multiple cell types, complex regularization schemes, or additional constraints like path invariance or conformal isometry.

4. **Unified computational framework**: The work reframes grid cells as a high-capacity, distance-preserving metric for space rather than specialized path integrators. This suggests their primary function may be spatial encoding and metric formation, with path integration being a separable computation potentially implemented by other cell types (like band cells).

5. **Toroidal manifold structure**: Both models learn representations with toroidal topology (one 0D, two 1D, one 2D persistent cocycles), consistent with biological grid cell population activity (Gardner et al. 2022), suggesting the model captures fundamental organizational principles of spatial representations.

---

### Brain regions & systems

- **Medial Entorhinal Cortex (mEC)** — primary brain region where grid cells are found; the paper focuses on modeling grid cell representations found in this region
- **Hippocampal formation** — referenced as part of the broader navigation circuit that includes grid cells; paper discusses connections to place cells and spatial memory

The paper is primarily computational and does not focus on specific anatomical circuits. Instead, it models the functional properties of mEC grid cells using artificial neural networks.

---

### Mechanistic insight

This paper partially meets the bar for mechanistic insight. It presents an **algorithm** (distance preservation + capacity constraint) and provides **neural data** from artificial neural networks, but not biological neural data. However, the paper's findings align with and help interpret existing biological observations.

**Phenomenon**: Grid cells in the medial entorhinal cortex exhibit hexagonal spatial firing patterns. The prevailing theory holds that grid cells function as neural path integrators, updating position estimates based on self-motion cues.

**Marr's levels analysis**:

- **Computational**: The brain (or artificial networks) must solve the problem of representing spatial locations such that nearby locations have similar neural representations (distance preservation) while maximizing the capacity to represent distinct locations (high-fidelity, distributed coding).

- **Algorithmic**: The solution involves learning a periodic, hexagonal representation through optimization of two objectives: (1) a Gaussian-weighted distance preservation loss that enforces local distance fidelity, and (2) an L1 capacity constraint that promotes distributed, correlated activity across the population. The hexagonal pattern emerges as the optimal trade-off between these constraints.

- **Implementational**: In the artificial networks, this is implemented through feedforward or recurrent neural networks with ReLU activations and normalized outputs. The RNN additionally implements path integration through recurrent connections that integrate velocity inputs. The paper does not provide biological implementation details, but notes that the RNN's connectivity follows short-range excitation/long-range inhibition patterns similar to biological continuous attractor models.

**Why partial mechanistic insight**: The paper provides a clear algorithmic-level account of how grid cells could emerge from simple optimization principles, and demonstrates this in artificial neural networks. However, it does not provide direct biological neural data (e.g., recordings, manipulations) that would conclusively establish this mechanism in biological systems. The findings do align with recent biological evidence that grid cells may not be necessary for path integration (Nayebi et al. 2021, Schøyen et al. 2023), supporting the paper's dissociation of grid cells from path integration.

---

### Limitations & open questions

**Acknowledged limitations**:

- Simplified domain using Cartesian coordinate inputs rather than biologically realistic sensory inputs (e.g., head direction cells, visual features)
- Use of labeled distances during training (Euclidean distance labels) which is biologically implausible; the authors note they are exploring sampling-based alternatives more transferable to biological learning
- Euclidean distance function may be insufficient for naturalistic environments with interior walls or exotic geometries where grid patterns deform
- Using Euclidean distance between state vectors may lead to inaccuracies; metric induced by the neural network could be more appropriate
- The model is trained on a simple open arena, not complex naturalistic environments

**Open questions raised**:

- How do the findings generalize to more biologically realistic input modalities (e.g., head direction cells, visual cues)?
- Can the distance preservation objective be learned through biologically plausible sampling-based methods without explicit distance labels?
- How do grid cells and band cells interact in biological systems during navigation?
- What is the precise circuit mechanism by which band cells implement path integration in the RNN model, and does this apply to biological systems?
- How do the findings apply to environments with complex geometries, boundaries, and obstacles?
- What is the evolutionary relationship between grid cells and band cells—did one evolve before the other?

---

### Connections & keywords

**Key citations**:
- Hafting et al. (2005) — Discovery of grid cells
- Burak & Fiete (2009) — Continuous attractor network models of grid cells and path integration
- Cueva & Wei (2018), Banino et al. (2018), Sorscher et al. (2022) — Grid cells emerging in RNNs trained to path integrate
- Nayebi et al. (2021) — Grid cells not necessary for path integration (interventional study)
- Schøyen et al. (2023) — Band cells responsible for path integration, not grid cells
- Gardner et al. (2022) — Toroidal topology of grid cell population activity
- Schaeffer et al. (2023), Xu et al. (2022) — Normative models with capacity constraints and path invariance/conformal isometry
- Moser & Moser (2008) — Grid cells as a metric for space
- Krupic et al. (2012) — Discovery of band cells

**Named models or frameworks**:
- Continuous attractor network models (Burak & Fiete 2009)
- Self-supervised learning with distance preservation + capacity constraints
- Feedforward network model (FF)
- Recurrent neural network model (RNN)
- Persistent homology analysis (topological data analysis)
- UMAP dimensionality reduction

**Brain regions**:
- Medial Entorhinal Cortex (mEC)
- Hippocampal formation (referenced)

**Keywords**:
grid cells, band cells, path integration, self-supervised learning, distance preservation, capacity constraints, recurrent neural networks, feedforward networks, spatial navigation, toroidal topology, persistent homology, normative models, entorhinal cortex, metric learning

### Related wiki pages
- [[wiki/debates/grid_cells_as_a_mechanism_for_path_integration|Grid cells as a mechanism for path integration]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
