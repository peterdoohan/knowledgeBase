---
source_file: sorscher2023_grid_cells_unified_theory.md
paper_id: sorscher2023_grid_cells_unified_theory
title: "A unified theory for the computational and mechanistic origins of grid cells"
authors:
  - "Ben Sorscher"
  - "Gabriel C. Mel"
  - "Samuel A. Ocko"
  - "Lisa M. Giocomo"
  - "Surya Ganguli"
year: 2023
journal: Neuron
paper_type: computational
contribution_type: theoretical
species:
  - rat
methods:
  - electrophysiology
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - grid_cells
  - path_integration
  - recurrent_neural_networks
  - pattern_formation
  - attractor_dynamics
  - toroidal_manifold
  - hexagonal_lattice
  - spatial_navigation
  - entorhinal_cortex
  - place_cells
  - nonnegative_firing_rates
  - continuous_attractor_networks
  - fourier_analysis
  - eigenvalue_decomposition
  - neural_manifolds
  - computational_neuroscience
  - representation_learning
  - unified
  - theory
  - computational
key_citations:
  - dordek2016_grid_cells_pca
  - stachenfeld2017_hippocampus_predictive_map
wiki_pages:
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
---

### One-line summary

Recurrent neural networks trained to path integrate with nonnegative firing rate constraints and center-surround place cell outputs develop hexagonal grid cells, with pattern formation theory providing a unifying explanation for when and why different grid lattice structures emerge.

---

### Background & motivation

Entorhinal grid cells exhibit striking hexagonal firing patterns, yet two fundamental questions remain unanswered: (1) what generic circuit mechanisms give rise to grid cells, and (2) what computational reasons explain their pervasive existence across species? Prior hand-tuned attractor models can generate grid patterns but require many specific connectivity choices and do not demonstrate that hexagonal patterns arise as optimal solutions to computational problems. Meanwhile, normative models show grid-like representations can emerge from optimization but do not address how neural circuits actually perform path integration. This paper bridges these approaches by training RNNs to path integrate and using pattern formation theory to explain the emergent grid structures.

---

### Methods

- **Task design**: Simulated animal exploring a 2.2m x 2.2m square environment following a smooth random walk; network receives 2D body velocity input and must output place cell code representing current position
- **Network architecture**: "Vanilla" RNN with 4096 recurrently connected hidden units (ReLU or tanh nonlinearity), velocity input weights, and linear readout to 512 place cells
- **Training procedure**: Trained via RMSProp (learning rate 1e-4, batch size 200, 10,000 batches) with cross-entropy loss on place cell reconstruction; L2 regularization (1e-4) on recurrent weights to encourage generalization
- **Key constraints**: (1) Nonnegative firing rates (ReLU nonlinearity) to promote hexagonal grids; (2) Center-surround place cell receptive fields (difference of Gaussians with σ1=20cm, σ2=40cm)
- **Comparison architectures**: Also trained feedforward networks (Dordek et al. 2016), LSTM networks (Banino et al. 2018), and 1D head direction networks
- **Neural data comparison**: Compared model predictions to electrophysiology recordings from 778 MEC neurons in awake, behaving rats (Butler et al. 2019; Gardner et al. 2022)

---

### Key findings

- **Hexagonal grids emerge with nonnegative constraints**: RNNs trained with ReLU nonlinearity (nonnegative firing) and center-surround place cell outputs develop regular hexagonal grid cells matching biological grid cells; tanh networks develop heterogeneous or square grids
- **Pattern formation theory unifies grid emergence**: The optimal position encoding map corresponds to the top eigenvector of the place cell spatial correlation matrix; with nonnegative constraints, hexagonal grids emerge from cooperative interaction of frequency triples forming equilateral triangles in Fourier space
- **Generalization beyond training environment**: Unlike prior trained networks (Banino et al. 2018), models with weight decay regularization continue to path integrate and maintain grid patterns when the animal moves outside the training arena boundaries, matching biological grid cell behavior
- **Emergent toroidal attractor manifold**: Trained networks develop a 2D toroidal manifold of stable activity patterns (confirmed by persistent homology analysis), with neural trajectories wrapping around the torus as the animal moves in physical space, matching the topology found in actual MEC grid cells (Gardner et al. 2022)
- **Mechanistic similarity to hand-designed models**: At the population level, trained networks exhibit similar dynamics to hand-tuned continuous attractor models: center-surround connectivity on an emergent neural sheet, low-frequency Fourier mode amplification, and velocity-coupled bump movement; however, these mechanisms are only apparent at the collective level, not at the level of individual synapses
- **Functional role of heterogeneous cells**: Ablating high grid-score cells severely degrades path integration performance, while ablating low grid-score (heterogeneous) cells has minimal effect; however, heterogeneous cells significantly improve the network's ability to read out spatial information into place cell codes, suggesting grid cells form the core path integrator while heterogeneous cells facilitate downstream readout
- **Superior fit to neural data**: Trained RNNs predict actual MEC neural response maps significantly better than hand-designed continuous attractor models (cross-validated Pearson correlation), nearly saturating the ceiling set by brain-to-brain prediction; maximum entropy models with matched first- and second-order statistics perform similarly well, suggesting MEC heterogeneity may be characterized by second-order statistics alone

---

### Computational framework

**Pattern formation theory** provides the core theoretical framework. The position encoding problem is formalized as finding optimal hidden representations that generate place cell activity patterns through a single synaptic transformation while minimizing neural activity costs. Mathematically, this corresponds to extracting the top principal component of the place cell spatial correlation matrix S, with eigenvectors representing Fourier plane waves. The lattice structure of emergent grids (square, heterogeneous, or hexagonal) depends on: (1) the width of place cell similarity structure (determining which Fourier modes have maximal eigenvalues), and (2) nonnegativity constraints on firing rates (favoring hexagonal patterns through cooperative interactions of frequency triples forming equilateral triangles in Fourier space). This connects to **continuous attractor network** dynamics for path integration, where stable activity patterns form a toroidal manifold and velocity inputs push activity bumps along the manifold.

---

### Prevailing model of the system under study

Before this work, two largely separate approaches existed for understanding grid cells. **Hand-tuned continuous attractor models** (Fuhs & Touretzky 2006; Burak & Fiete 2009) proposed that grid cells are arranged on a 2D neural sheet with center-surround connectivity, creating stable hexagonal bump patterns. These models could path integrate by shifting activity bumps via velocity-coupled connectivity but required many specific hand-tuned choices and did not explain why hexagonal patterns should be optimal. **Normative models** (Dordek et al. 2016; Stachenfeld et al. 2017) showed that grid-like representations can emerge from optimization principles (efficient coding, predictive maps) but did not address how circuits actually perform path integration. **Trained path integrator networks** (Cueva & Wei 2018; Banino et al. 2018) represented an important step but produced either square grids (Cueva & Wei) or heterogeneous, non-generalizing grids (Banino et al.) that did not match biological hexagonal grid cells. The prevailing view was that these approaches addressed different aspects of grid cells without a unifying theoretical framework.

---

### What this paper contributes

This paper provides a **unified theory** connecting path integration to hexagonal grid emergence through pattern formation theory, demonstrating that: (1) RNNs trained to path integrate with nonnegative firing rates and center-surround place cell outputs develop **biologically realistic hexagonal grid cells** that generalize beyond the training environment; (2) **Pattern formation theory** explains why different grid lattice structures (square, heterogeneous, hexagonal) emerge based on place cell similarity structure width and nonnegativity constraints; (3) The **emergent toroidal attractor manifold** in trained networks matches the topology found in actual MEC recordings (Gardner et al. 2022); (4) At the **population level**, trained networks employ similar mechanisms to hand-designed models (center-surround connectivity, low-frequency mode amplification, velocity-coupled bump movement), but these mechanisms only emerge at the collective level, not at individual synapses; (5) A **functional dichotomy** exists between grid cells (core path integration) and heterogeneous cells (facilitating downstream readout); (6) Trained models **fit actual MEC neural data** significantly better than hand-designed continuous attractor models. The paper establishes a principled bridge between normative and mechanistic approaches to grid cells.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — primary focus; contains grid cells that path integrate; the paper demonstrates that trained RNNs develop representations matching MEC grid cells and heterogeneous cells
- **Hippocampus** — place cells serve as the target output representation that the network learns to generate; the grid cell-to-place cell organization mirrors the MEC-hippocampus connectivity

---

### Mechanistic insight

This paper achieves a high bar for mechanistic insight by presenting both a computational algorithm and connecting it to neural data.

**Computational level**: The brain must solve path integration—maintaining an estimate of current position by integrating velocity signals over time—while efficiently encoding spatial information with minimal neural activity.

**Algorithmic level**: Pattern formation theory formalizes the optimal encoding problem as extracting principal components of the place cell spatial correlation matrix. With nonnegative firing constraints, hexagonal grids emerge from cooperative interactions of Fourier frequency triples forming equilateral triangles. Path integration is implemented via a toroidal attractor manifold where velocity inputs push activity bumps along the manifold.

**Implementational level**: The trained RNN develops center-surround effective connectivity on an emergent 2D neural sheet (obtained by sorting neurons by their spatial phases). The connectivity amplifies low-frequency Fourier modes while preserving frequency and orientation. Individual synapses show little discernible structure, but population-level analysis reveals the emergent attractor dynamics. The network contains both regular hexagonal grid cells (forming the core path integrator) and heterogeneous cells (facilitating downstream readout), matching the diversity found in actual MEC recordings.

---

### Limitations & open questions

- **Training procedure**: The network is trained using backpropagation with a place cell teaching signal, which is a method for exploring path-integrator models rather than a biologically plausible developmental mechanism; how grid cells actually develop remains unclear
- **Velocity signal**: The model assumes body velocity input is available, though recent work shows head direction is primarily represented in MEC; the model is agnostic about whether this signal would be found in MEC neurons themselves
- **Biological details**: The model does not capture specific biological features like purely inhibitory recurrent connectivity found in MEC (Couey et al. 2013); the attractor framework alone cannot predict synapse polarity
- **Landmark integration**: The current model does not incorporate landmarks or other directional signals; extending the model to include landmark-velocity fusion could explain grid cell deformations in irregular environments and remapping in virtual reality
- **Reward and spatial coding**: The model does not address how changes in rewarded location affect grid-cell firing properties; training networks to forage with changing reward locations could yield hypotheses about reward-spatial interactions
- **Beyond path integration**: The functional role of grid cells in more general cognitive processes (episodic memory, abstract reasoning, planning, imagination) remains to be explored; whether ancient path integration mechanisms were co-opted for general reasoning is an open question

---

### Connections & keywords

**Key citations**: Dordek et al. 2016 (normative grid models), Cueva & Wei 2018 (square grids in trained networks), Banino et al. 2018 (vector-based navigation with grid-like representations), Burak & Fiete 2009 (continuous attractor models), Gardner et al. 2022 (toroidal topology in grid cells), Stachenfeld et al. 2017 (predictive map hypothesis), Fuhs & Touretzky 2006 (hand-tuned grid models)

**Named models or frameworks**: Pattern formation theory, continuous attractor networks, path integration, toroidal attractor manifold, principal component analysis (PCA), nonnegative matrix factorization, Fourier analysis

**Brain regions**: Medial entorhinal cortex (MEC), hippocampus, place cells, grid cells, head direction cells

**Keywords**: grid cells, path integration, recurrent neural networks, pattern formation, attractor dynamics, toroidal manifold, hexagonal lattice, spatial navigation, entorhinal cortex, place cells, nonnegative firing rates, continuous attractor networks, Fourier analysis, eigenvalue decomposition, neural manifolds, computational neuroscience, representation learning

### Related wiki pages
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
