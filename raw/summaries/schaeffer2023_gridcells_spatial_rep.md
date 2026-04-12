---
source_file: schaeffer2023_gridcells_spatial_rep.md
paper_id: schaeffer2023_gridcells_spatial_rep
title: "Self-Supervised Learning of Representations for Space Generates Multi-Modular Grid Cells"
authors:
  - "Rylan Schaeffer"
  - "Mikail Khona"
  - "Tzuhsuan Ma"
  - "Cristóbal Eyzaguirre"
  - "Sanmi Koyejo"
  - "Ila Rani Fiete"
year: 2023
journal: "NeurIPS 2023"
paper_type: computational
contribution_type: theoretical
brain_regions:
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - grid_cells
  - self_supervised_learning
  - spatial_representation
  - path_integration
  - continuous_attractor
  - recurrent_neural_network
  - medial_entorhinal_cortex
  - multi_modular_coding
  - separation_invariance_capacity
  - contrastive_learning
  - spatial_navigation
  - toroidal_manifold
  - hexagonal_lattice
  - self
  - supervised
  - learning
  - representations
  - space
  - generates
  - multi
key_citations:
  - fiete2008_grid_cells_position
  - sorscher2023_grid_cells_unified_theory
---

### One-line summary

Multi-modular grid cells emerge as optimal solutions to a self-supervised learning (SSL) framework that optimizes separation, path invariance, and capacity losses, without requiring supervised position information or hand-engineered readout representations.

### Background & motivation

Grid cells in the mammalian medial entorhinal cortex represent spatial position using periodic, multi-scale firing patterns organized into discrete modules. While mathematical analysis has revealed the grid code's excellent properties (high capacity, error correction, algebraic structure), previous deep learning approaches required hand-engineered supervised targets or specific readout representations to generate grid cells. This paper addresses the gap by asking: can grid cells emerge from first principles through self-supervised learning without supervised position targets?

### Methods

- **Network architecture**: Recurrent neural network (RNN) with 128 hidden units, using velocity inputs (2D Cartesian) and Norm-ReLU nonlinearity (unit-norm, non-negative representations). No positional readout or supervised spatial targets.
- **Training data**: Sequences of 60 timesteps with i.i.d. sampled velocities from uniform distribution. Data augmentation via random permutations of velocity sequences to create trajectory intersections.
- **Loss functions** (SIC framework): 
  - Separation loss: encourages different spatial locations to have well-separated neural representations
  - Path Invariance loss: encourages same spatial locations (regardless of path) to have identical representations
  - Capacity loss: maximizes number of unique positions encodable within finite representation space (pushes embeddings together)
  - Conformal Isometry loss: ensures consistent neural distance scaling for same velocity magnitudes regardless of direction
- **Training**: 2 million gradient steps with AdamW optimizer, learning rate 2e-5.

### Key findings

- **Multi-modular grid emergence**: Networks trained with the full SIC framework develop multiple discrete modules of grid cells (typically 3 modules) with different spatial periods, matching the biological organization where cells within a module share period and orientation while covering all phases uniformly.
- **Hexagonal lattice structure**: Emergent grid cells exhibit hexagonal firing patterns with clear six-fold symmetry in Fourier power spectral density, consistent with biological grid cells.
- **Toroidal manifold structure**: State space analysis using spectral embedding revealed that population activity lies on a 2D toroidal manifold, with projections onto phase axes showing 3 ring structures characteristic of twisted torus topology.
- **Generalization**: Networks generalize to arenas much larger than training environments (tested up to 4m boxes vs. <1.2m training trajectories) and to different velocity statistics (smooth trajectories vs. i.i.d. uniform training velocities).
- **Ablation results**: 
  - Removing capacity loss → single module instead of multiple modules
  - Reducing σg (neural length scale) → place cell-like representations
  - Removing trajectory permutations → loss of spatial tuning
  - Removing path invariance or separation loss → loss of grid structure

### Computational framework

**Self-Supervised Learning (SSL) with Separation-Invariance-Capacity (SIC)**: The paper frames spatial representation learning as a SSL problem where the learning target is constructed from the data itself rather than external supervision. The SIC framework combines three principles:

1. **Separation**: Neural representations of different positions should be distinguishable (contrastive learning principle)
2. **Invariance**: Neural representations of the same position reached by different paths should be identical (path integration / continuous attractor requirement)
3. **Capacity**: The representation should encode as many unique positions as possible within its finite coding volume (efficient coding principle)

The framework sits at the intersection of coding theory (efficient algebraic codes), dynamical systems (continuous attractors, path invariance), and modern machine learning (self-supervised learning, contrastive methods).

### Prevailing model of the system under study

Prior to this work, the field understood grid cells through two main perspectives: (1) mathematical analysis showing grid cells form high-capacity, error-correcting algebraic codes with exponential coding capacity and path-independent displacement encoding; and (2) deep learning models that could generate grid-like responses but required hand-engineered supervised spatial targets or specific readout representations. Recent critiques (including by these authors) showed that supervised approaches put grid cells in by hand through their target functions and failed to generalize beyond training distributions. The prevailing challenge was identifying an optimization problem where grid cells would emerge naturally without supervised position information.

### What this paper contributes

This paper demonstrates that multi-modular grid cells emerge as optimal solutions to a purely self-supervised learning problem, without requiring: (1) supervised position targets, (2) hand-engineered readout representations, or (3) specific statistics in target functions. The SIC framework provides a normative, developmentally plausible account of how grid cells could arise from first principles—combining insights from coding theory (capacity, separation), dynamical systems (path invariance, continuous attractors), and function optimization. The trained networks generalize to novel environments and velocity statistics, addressing a key limitation of prior supervised approaches. The work establishes a bridge between mathematical theories of grid cell function and mechanistic models of their development.

### Brain regions & systems

- **Medial entorhinal cortex (MEC)**: The primary brain region containing grid cells; the paper focuses on modeling grid cell representations found in this region. The emergent representations in the trained RNNs are compared to biological grid cells in MEC.

### Mechanistic insight

This paper does **not** meet the high bar for mechanistic insight as defined in the template. While the paper demonstrates that grid cells emerge from self-supervised learning, it does not provide neural data (from biological recordings) that would specifically support the SIC algorithm over alternatives. The paper is purely computational, using artificial RNNs to demonstrate emergence. However, the paper does propose a clear algorithmic-level model (SIC framework with separation, invariance, and capacity losses) that could in principle explain grid cell development. The authors explicitly acknowledge this limitation and suggest future work to "reverse-engineer the learnt mechanisms" and connect them back to biological grid cells.

### Limitations & open questions

1. The specific factors controlling the number of modules, distribution of periods, period ratios, and lattice structure (hexagonal vs. square) remain to be fully characterized.
2. The underlying connectivity patterns that lead to discrete modular responses in the trained networks are not yet understood.
3. How the learned representations would respond to experimental manipulations (environmental deformations, rewards) is untested.
4. The relationship between the SIC framework and other SSL frameworks (InfoNCE, SimCLR, BYOL, etc.) remains to be mathematically characterized.
5. The apparent contradiction between capacity loss (minimizing entropy of representations) and standard information-theoretic intuitions (maximizing entropy) requires resolution.
6. Computational constraints prevented broader hyperparameter sweeps; broader exploration may reveal additional emergent properties.

### Connections & keywords

**Key citations:**
- Hafting et al. 2005 (discovery of grid cells)
- Fiete et al. 2008 (coding theory of grid cells)
- Banino et al. 2018 (supervised deep learning of grid cells)
- Sorscher et al. 2023 (unified theory of grid cells)
- Cueva & Wei 2018 (emergence of grid-like representations in RNNs)
- Sreenivasan & Fiete 2011 (error-correcting codes)

**Named models or frameworks:**
- Self-Supervised Learning (SSL)
- Separation-Invariance-Capacity (SIC) framework
- Continuous attractor networks
- Path integration
- Contrastive learning
- Deep metric learning

**Brain regions:**
- Medial entorhinal cortex (MEC)

**Keywords:**
grid cells, self-supervised learning, spatial representation, path integration, continuous attractor, recurrent neural network, medial entorhinal cortex, multi-modular coding, separation-invariance-capacity, contrastive learning, spatial navigation, toroidal manifold, hexagonal lattice
