---
source_file: "wen2024_entorhinal_maps_flexible_navigation.md"
paper_id: "wen2024_entorhinal_maps_flexible_navigation"
title: "One-shot entorhinal maps enable flexible navigation in novel environments"
authors: "John H. Wen, Ben Sorscher, Emily A. Aery Jones, Surya Ganguli, Lisa M. Giocomo"
year: 2024
journal: "Nature"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
tasks: ["navigation_task"]
methods: ["neuropixels", "computational_modeling"]
brain_regions: ["hippocampus", "hippocampus_ca1", "entorhinal_cortex", "medial_entorhinal_cortex", "lateral_entorhinal_cortex", "visual_cortex"]
frameworks: ["attractor_networks"]
keywords: ["one", "shot", "entorhinal", "maps", "enable", "flexible", "navigation", "novel", "environments"]
key_citations: ["fyhn2007_remapping_grid_realignment"]
---

### One-line summary

Grid cells in the medial entorhinal cortex form stable spatial maps in novel environments after a single exposure through fixed landmark-to-attractor connectivity, while flexible navigation is enabled by rapid plasticity in downstream regions.

### Background & motivation

Animals must navigate changing environments to find resources, yet how the brain rapidly incorporates changing environmental features into neural spatial maps remains unknown. Previous solutions proposed include rigid path integration systems (prone to error accumulation) and slower Hebbian plasticity mechanisms (taking minutes to hours). Neither fully explains how mammals navigate novel or rapidly changing environments. This study investigates how grid cells in the medial entorhinal cortex (MEC) adapt to environmental changes on behaviorally relevant timescales.

### Methods

- **Subjects**: 19 female and 3 male C57BL/6 mice, 12-24 weeks of age
- **Recording**: Neuropixels 1.0 probes for acute recordings; Neuropixels 2.0 for chronic recordings
- **Virtual reality environments**: 
  - Build-up track (320 cm): systematic addition of visual landmarks
  - Random environment track (100 cm): 5 landmarks in random arrangements across 12 environments
  - Hidden reward track (200 cm): navigation task with unmarked reward zone
- **Analysis**: 
  - Grid cell identification via power spectral density analysis (three-peaked structure)
  - Activity bump tracking on 2D toroidal neural sheet via phase-based sorting
  - Computational model: continuous attractor network with fixed landmark pinning
- **Manipulation**: Bilateral muscimol inactivation of MEC during hidden reward task

### Key findings

- Grid cells exhibit low-dimensional continuous attractor dynamics in 1D virtual reality, with activity bumps that drift diffusively in darkness (D = 1.16 ± 0.07 deg²/m) but maintain stable grid scale (<5% drift over 100m)
- Visual landmarks induce one-shot remapping: grid cells develop new stable firing patterns after a single trial exposure to a new landmark configuration (average 1.29 ± 0.07 trials for remapping)
- Landmarks entrain grid cells to periodic trajectories on the toroidal attractor but cause distortions (anisometry and curvature) in the bump trajectory compared to darkness
- A computational model with fixed landmark-to-grid connectivity (weak pinning) and no plasticity accurately predicts grid cell firing patterns in novel environments (Pearson r > chance, p = 3.58 × 10⁻¹⁸)
- Model fits show best performance with learning rate η = 0, indicating fixed (non-plastic) landmark-grid connectivity explains the data better than Hebbian plasticity mechanisms
- In a hidden reward task, grid cell firing patterns remain distorted after landmark shifts (no recovery across blocks), yet animals adapt behaviorally within <10 trials
- MEC inactivation with muscimol significantly impairs behavioral performance (p = 0.0004, permutation test), confirming MEC's role in the task
- Grid cell stability correlates with behavioral performance (Pearson r = −0.20, p < 1 × 10⁻¹⁰ for licking error)
- A downstream decoder using behavioral timescale synaptic plasticity (BTSP) can adapt to distorted grid cell codes and predict reward location across environments, unlike a fixed decoder

### Computational framework

**Continuous attractor network (CAN)**: The paper models grid cells as a bump of activity moving on a 2D toroidal neural sheet. The bump's dynamics are governed by:
- Path integration: the bump moves in straight lines with velocity proportional to the animal's speed
- Landmark pinning: visual landmarks exert weak attractive forces (pinning) on the bump toward fixed locations on the neural sheet when the animal approaches within 50 cm
- The model uses hexagonal periodic boundary conditions (twisted torus topology) to account for grid cell geometry

**Key variables**: 
- θ₁, θ₂: 2D coordinates of the activity bump on the neural sheet
- ρᵢ: fixed pinning phase of landmark i on the neural sheet
- αᵢ: pinning strength of landmark i
- D: angular diffusion constant (drift in darkness)

### Prevailing model of the system under study

Before this study, the field understood that:
1. Grid cells in MEC construct a neural spatial map using idiothetic cues (path integration) and are sensitive to environmental features (boundaries, rewards)
2. Grid cell firing patterns can distort with environmental changes, but these distortions persist for days, suggesting slow plasticity mechanisms
3. Continuous attractor dynamics provide a computational framework for understanding grid cell responses
4. Hebbian plasticity (minutes to hours timescale) was considered a primary mechanism for integrating new landmarks into spatial maps, based on evidence from Drosophila and mammalian head direction cells

The paper notes that neither rigid path integration (prone to error accumulation) nor slow Hebbian plasticity (too slow for rapid navigation) fully explained how mammals navigate novel or rapidly changing environments.

### What this paper contributes

This paper reveals that:
1. **One-shot remapping**: Grid cells form stable firing patterns in novel environments after a single exposure, much faster than previously thought (not requiring days of plasticity)
2. **Fixed landmark architecture**: Visual landmarks provide fixed (non-plastic) inputs to the grid cell attractor network over short timescales (minutes to hours), causing predictable distortions in grid firing patterns
3. **Weak pinning mechanism**: Landmarks "tug" the activity bump via weak pinning to fixed points on the neural sheet, explaining both the rapid stability and the systematic distortions observed
4. **Separation of map stability and behavioral flexibility**: Grid cell representations remain distorted (fixed), but flexible behavior emerges from rapid plasticity (BTSP) in downstream regions (likely CA1 hippocampus)
5. **MEC necessity for navigation**: Inactivation of MEC impairs behavioral performance, confirming its role in supporting spatial navigation tasks

The paper reconciles rapid navigation in novel environments with fixed grid cell architecture by showing that behavioral flexibility relies on downstream plasticity rather than remapping of the grid cell code itself.

### Brain regions & systems

- **Medial entorhinal cortex (MEC)**: Primary region of study; contains grid cells that form the neural spatial map. Grid cells show rapid one-shot remapping and fixed landmark-induced distortions. Non-grid spatial cells in MEC also show landmark-driven responses.
- **Hippocampus (CA1)**: Proposed downstream region where behavioral timescale synaptic plasticity (BTSP) enables rapid adaptation to distorted grid cell codes. Not directly recorded in this study but modeled as the locus of flexible behavioral adaptation.
- **Lateral entorhinal cortex (LEC)**: Mentioned as potentially encoding information about rewarded locations that could support flexible behavior.
- **Parasubiculum**: Mentioned as having boundary vector and corner cells that could provide landmark input to grid cells.
- **Visual cortex (V1)**: Mentioned as containing neurons active near visual landmarks that could provide input to grid cells.

### Mechanistic insight

This paper meets the high bar for mechanistic insight by providing both an algorithm (continuous attractor network with fixed landmark pinning) and neural data supporting that algorithm over alternatives.

**Computational level**: The brain solves the problem of rapid spatial mapping in novel environments by using a fixed landmark-to-grid cell network architecture. This enables one-shot formation of stable spatial maps (rapidity) but at the cost of metric distortions (inaccuracy). The trade-off is resolved by delegating behavioral flexibility to downstream plastic mechanisms.

**Algorithmic level**: Grid cells implement a continuous attractor network where:
- An activity bump moves on a 2D toroidal neural sheet
- Path integration moves the bump in straight lines proportional to the animal's speed
- Visual landmarks provide fixed "pinning" inputs that tug the bump toward preferred locations on the neural sheet
- The bump trajectory results from the interplay of path integration and landmark pinning

**Implementational level**: 
- The MEC contains grid cells organized into modules with discrete grid scales (ratio ~1.4-1.7)
- Grid cells within a module maintain fixed phase relationships, supporting the attractor dynamics
- Visual landmarks provide inputs to fixed points on the neural sheet (no rapid plasticity observed)
- Downstream regions (likely CA1) use behavioral timescale synaptic plasticity (BTSP) to adapt to distorted grid codes

The paper explicitly tests and rejects alternative algorithmic implementations (Hebbian plasticity with various learning rates) in favor of the fixed pinning model.

### Limitations & open questions

- **Mechanistic details upstream**: The specific nature of landmark inputs to the grid cell network remains unknown. Candidates include MEC non-grid spatial cells, border cells, object vector cells, LEC neurons, V1 neurons, or subicular boundary vector/corner cells.
- **Mechanistic details downstream**: The exact plasticity mechanism enabling behavioral flexibility requires further investigation. BTSP is one candidate, but Hebbian learning in associative networks or LEC contributions are also possible.
- **Model limitations**: The study used a simplified model with point landmark inputs; broader connectivity patterns between landmarks and grid cells could be explored in future work.
- **Temporal dynamics**: The paper focuses on rapid one-shot remapping, but longer-term plasticity (days to weeks) that eventually restores grid regularity remains to be fully characterized.
- **Causality**: While MEC inactivation impaired behavior, the specific contribution of grid cells versus other MEC cell types to the observed effects was not directly dissociated.

### Connections & keywords

**Key citations**:
- Hafting et al. 2005 (grid cell discovery)
- Fyhn et al. 2007 (hippocampal remapping and grid realignment)
- Yoon et al. 2013 (continuous attractor dynamics in grid cells)
- Gardner et al. 2022 (toroidal topology of grid cell activity)
- Bittner et al. 2017 (BTSP in CA1 place fields)
- Grienberger & Magee 2022 (entorhinal cortex directs learning-related changes in CA1)
- Kim et al. 2019, Fisher et al. 2019 (landmark integration in Drosophila heading system)
- Barry et al. 2007, Stensola et al. 2012 (experience-dependent grid rescaling and discretization)

**Named models or frameworks**:
- Continuous attractor networks (CAN)
- Path integration
- Toroidal attractor dynamics
- Weak pinning model
- Behavioral timescale synaptic plasticity (BTSP)
- Hebbian learning

**Brain regions**:
- Medial entorhinal cortex (MEC)
- Hippocampus (CA1)
- Lateral entorhinal cortex (LEC)
- Parasubiculum
- Visual cortex (V1)
- Subiculum

**Keywords**:
- grid cells
- entorhinal cortex
- spatial navigation
- continuous attractor networks
- landmark pinning
- remapping
- toroidal attractor
- virtual reality
- one-shot learning
- behavioral timescale synaptic plasticity (BTSP)
- path integration
- neural coding
- spatial memory
