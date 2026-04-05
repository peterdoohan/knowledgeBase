---
source_file: boccara2019_grid_goal_attractor.md
title: The entorhinal cognitive map is attracted to goals
authors: Charlotte N. Boccara, Michele Nardin, Federico Stella, Joseph O'Neill, Jozsef Csicsvari
year: 2019
journal: Science
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Grid cells in the medial entorhinal cortex shift their firing fields toward learned goal locations, causing long-lasting deformations of the spatial map and demonstrating that grid cells participate in mnemonic coding beyond providing a simple spatial metric.

### Background & motivation

Grid cells have been hypothesized to provide a universal invariant metric for spatial cognition due to their regular hexagonal firing fields. However, recent evidence suggests the grid structure can be distorted by environmental geometry. Given that the hippocampus encodes multimodal information beyond space, this study tested whether behaviorally relevant nonspatial information (reward locations) influences the organization of grid cells and how such information is encoded in the entorhinal-hippocampal circuit during learning.

### Methods

- **Task**: Rats trained daily to learn three new hidden reward locations on a cheeseboard maze (hippocampus-dependent spatial memory task)
- **Recording**: Simultaneous extracellular recordings from medial entorhinal cortex (MEC) and hippocampal CA1 region using tetrodes
- **Design**: Pre-probe (baseline), rest, learning, rest, post-probe (memory test) phases; open field control sessions in three animals
- **Analysis**: 
  - Grid score calculation from spatial autocorrelograms
  - Laplacian of Gaussian (LoG) filter for field detection
  - Linear-nonlinear Poisson (LNP) spiking model to control for behavioral confounds
  - Population vector correlation analysis (Fisher z-scored)
  - Flickering analysis (rapid alternation between pre/post representations)

### Key findings

- 80-90% of grid cells had at least one firing field significantly moving toward a goal (binomial test, P < 0.00001)
- Similar field movement observed in MEC nonperiodic spatial cells (84%) and CA1 place cells (79%)
- Grid scores were significantly lower in cheeseboard probes compared to open field (P < 0.00001, one-way ANOVA), independent of spatial sampling, trajectories, speed, or heading
- Field attraction strength correlated with pre-probe distance to goal: fields within ~30 cm showed attraction, fields beyond showed little detectable attraction (r = –0.192, P = 0.01225, Spearman)
- Number of fields at goals increased (Fisher exact test, P = 0.0145) and mean distance from field centers to closest reward decreased (KS test, P = 0.01472)
- MEC retained field reorganization overnight (using previous day's goal locations), while CA1 changes were more transient, suggesting different memory trace lability between regions
- MEC showed local remapping (field-specific movement), while CA1 reorganized through global remapping
- Both MEC and CA1 showed "flickering" — rapid alternation between pre- and post-probe representations during learning, with no intermediate representations (KS test, P < 0.00001)
- MEC flickering scores shifted toward more positive values during learning, and CA1 reached plateau faster than MEC in goal flickering dynamics
- Population vector similarity in MEC was weaker around goals than away from them (P = 0.0003, t test) and positively correlated with distance from goals (P < 0.00001), while CA1 showed no such correlation (P = 1)
- Activity increase at goals correlated with memory retention (r = 0.77, P = 0.002)

### Computational framework

The study is primarily empirical but engages with computational frameworks of spatial cognition and attractor network models. The findings are discussed in relation to:
- Attractor network models of grid cells and place cells
- Models of goal-directed navigation that assign specific roles to CA1 and MEC
- Theoretical frameworks distinguishing between local remapping (field-specific changes) and global remapping (population-wide reorganization)

The results suggest that the hippocampal-entorhinal circuit stores multiple spatial maps that can coexist and alternate rapidly (flickering), with implications for how new maps are dynamically encoded and reorganized during learning.

### Prevailing model of the system under study

The prevailing model before this study held that grid cells provide a universal invariant metric for spatial cognition due to their regular hexagonal firing fields that tessellate all environments. Under this view, grid cells were considered to have a narrower role than hippocampal place cells, which code for multimodal information beyond simple spatial representations. The grid structure was thought to be rigid and resistant to nonspatial influences, with any distortions being primarily driven by environmental geometry rather than behaviorally relevant information.

### What this paper contributes

This paper fundamentally challenges the view that grid cells provide a rigid, invariant spatial metric. The results demonstrate that:

1. Grid cells participate in mnemonic coding: Individual grid fields move toward learned goal locations, indicating that grid cells encode behaviorally relevant information, not just spatial position.

2. The grid map is deformable: The regular hexagonal structure is locally distorted by goal learning, with grid scores decreasing significantly in environments containing learned rewards.

3. Different mechanisms in MEC vs CA1: While both regions show goal-related field movement, MEC exhibits local remapping (field-specific changes) while CA1 shows global remapping. MEC changes are more stable overnight compared to CA1.

4. Flickering dynamics: Both regions show rapid alternation between pre- and post-learning representations during learning, suggesting multiple maps can coexist and be dynamically accessed.

These findings support emerging hypotheses that the grid pattern carries a broader organizational role for both spatial and nonspatial information in naturalistic behaviors, and require updates to computational models of goal-directed navigation that assign specific roles to CA1 and MEC.

### Brain regions & systems

- **Medial entorhinal cortex (MEC)**: Primary region of interest. Grid cells and nonperiodic spatial cells recorded here. Showed local remapping with field-specific movement toward goals. Changes were stable overnight.
- **Hippocampal CA1**: Simultaneously recorded with MEC. Place cells showed similar field movement toward goals but through global remapping. Changes were more transient than MEC, suggesting higher lability of CA1 memory traces.
- **MEC-CA1 circuit**: The study examines the interaction between these regions during goal learning, revealing different dynamics of map reorganization (local vs global remapping, different timescales of stability).

### Mechanistic insight

This paper provides strong mechanistic insight by linking behavioral performance to specific neural reorganization patterns. The study meets both criteria for mechanistic insight:

1. **Algorithm**: The paper characterizes the reorganization process as "field attraction" where grid and place fields move toward goal locations with a strength inversely proportional to initial distance. This describes a learning algorithm where spatial representations are dynamically updated based on reward locations.

2. **Neural data**: The paper provides extensive neural recordings showing that this attraction is reflected in both single-unit firing fields and population-level dynamics (flickering between representations).

**Marr's three levels analysis**:

- **Computational**: The brain must solve the problem of encoding behaviorally relevant locations (goals) within a metric spatial framework to support navigation and memory.

- **Algorithmic**: Grid and place fields move toward goal locations with attraction strength proportional to initial distance. Multiple maps (pre- and post-learning) coexist and alternate rapidly (flickering). MEC uses local remapping (field-specific changes) while CA1 uses global remapping.

- **Implementational**: The study identifies differences between MEC and CA1 in terms of plasticity timescales (MEC changes more stable overnight) and remapping mechanisms. However, specific cellular or synaptic mechanisms are not directly investigated.

### Limitations & open questions

- The study does not identify the specific cellular or synaptic mechanisms underlying field attraction (e.g., whether it involves synaptic plasticity, changes in local inhibition, or neuromodulatory influences)
- The difference in timescales between MEC and CA1 plasticity (faster in CA1) is observed but the underlying circuit mechanisms are not fully explained
- The causal relationship between MEC and CA1 reorganization is not established (which region drives the changes)
- The computational implications of flickering dynamics for learning and decision-making remain to be fully explored
- Whether grid field attraction generalizes to other types of behaviorally relevant information beyond reward locations is unknown

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — The Hippocampus as a Cognitive Map (foundational theory)
- Hafting et al. (2005) — Grid cell discovery
- Stensola et al. (2015) — Grid cell geometry and environmental influences
- Dupret et al. (2010, 2013) — Goal remapping and flickering in CA1
- Jezek et al. (2011) — CA1 flickering between representations

**Named models or frameworks**:
- Cognitive map theory (O'Keefe & Nadel)
- Attractor network models of grid cells
- Goal remapping framework
- Flickering dynamics (rapid alternation between representations)
- Local vs global remapping distinction

**Brain regions**:
- Medial entorhinal cortex (MEC)
- Hippocampal CA1
- MEC-CA1 circuit

**Keywords**:
grid cells, place cells, entorhinal cortex, hippocampus, goal learning, spatial memory, cognitive map, remapping, flickering, reward encoding, navigation, electrophysiology, cheeseboard maze, field attraction
