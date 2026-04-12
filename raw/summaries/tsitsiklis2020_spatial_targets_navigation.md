---
source_file: tsitsiklis2020_spatial_targets_navigation.md
paper_id: tsitsiklis2020_spatial_targets_navigation
title: "Single-Neuron Representations of Spatial Targets in Humans"
authors:
  - "Melina Tsitsiklis"
  - "Jonathan Miller"
  - "Salman E. Qasim"
  - "Cory S. Inman"
  - "Robert E. Gross"
  - "Jon T. Willie"
  - "Elliot H. Smith"
  - "Sameer A. Sheth"
  - "Catherine A. Schevon"
  - "Michael R. Sperling"
  - "Ashwini Sharan"
  - "Joel M. Stein"
  - "Joshua Jacobs"
year: 2020
journal: "Current Biology"
paper_type: empirical
contribution_type: empirical
species:
  - human
methods:
  - electrophysiology
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_temporal_lobe
keywords:
  - spatial_target_cells
  - head_direction_cells
  - serial_position_cells
  - place_cells
  - medial_temporal_lobe
  - hippocampus
  - entorhinal_cortex
  - spatial_navigation
  - goal_directed_behavior
  - single_neuron_recording
  - virtual_reality
  - episodic_memory
  - electrophysiology
  - human_neuroscience
  - single
  - neuron
  - representations
  - spatial
  - targets
  - humans
key_citations:
  - ekstrom2003_spatial_navigation
wiki_pages:
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
---

### One-line summary

Human medial temporal lobe neurons represent remote spatial target locations during navigation, distinct from place cells that encode current position.

### Background & motivation

The medial temporal lobe (MTL) is critical for memory and spatial navigation, with extensive research on neurons that encode an animal's current spatial location (place cells) and heading direction (head-direction cells). However, everyday navigation frequently requires representing and navigating to remote destinations, yet the neural representations of these remote spatial targets remain less well understood. This study investigates whether human MTL neurons encode remote spatial target locations during goal-directed navigation.

### Methods

- **Participants**: 15 neurosurgical epilepsy patients (10 male, mean age 32) with implanted Behnke-Fried microelectrodes in the MTL
- **Task**: Virtual reality "Treasure Hunt" spatial memory task where subjects navigated to chests, encoded object locations, and later recalled them
  - Two versions: object-cued (19 sessions) and location-cued (4 sessions)
  - Each trial: subjects navigated to 2-4 chests in sequence, each revealing an object to remember
- **Recordings**: 131 neurons total from hippocampal formation (HF: n=45), entorhinal cortex (EC: n=71), and parahippocampal/perirhinal cortex (PC: n=15)
- **Analysis**: ANOVA with permutation testing to identify neurons modulated by spatial target position, subject position, heading direction, serial position, and subsequent memory

### Key findings

- **Spatial-target cells**: 20% of MTL neurons (26/131) showed firing rates significantly modulated by the location of the upcoming spatial target, independent of the subject's current position
  - Found in all MTL regions: HF (9/45), EC (12/71), PC (5/15)
  - Present in 11 of 15 subjects
  - Activity was sustained throughout navigation, not transient at start/end
  - Only 6/26 showed distance-related activity (not significant overlap)
- **Place-like cells**: Only 6% (8/131) showed modulation by subject's current position, not significantly above chance (5%)
- **Heading-modulated cells**: 12% (16/131) showed firing rates modulated by heading direction
  - First evidence of head-direction cells in humans
  - Some cells showed bidirectional responses (similar to rodent findings)
  - No preferred direction across population (Rayleigh test p=0.97)
  - No significant overlap with spatial-target cells (p=0.9)
- **Serial-position cells**: 15% (20/131) showed firing rates modulated by serial position within the trial
  - Particularly prominent in EC (23% of EC cells, p=1.05×10⁻⁶)
  - Most cells preferred initial list positions (primacy effect)
  - No significant overlap with spatial-target cells (p=0.55)
  - May relate to EC time cells found in other studies
- **Memory-related cells**: 8% (11/131) showed firing rates modulated by subsequent memory, not significantly above chance (p=0.081)

### Computational framework

Not applicable. This is a purely empirical study without an explicit computational model. The findings constrain models of spatial navigation and memory by demonstrating that the human MTL employs multiple coding schemes (spatial target, heading direction, serial position) to support goal-directed behavior, suggesting distributed representations of task-relevant information rather than a single dominant code.

### Prevailing model of the system under study

The prevailing model of MTL spatial coding, based primarily on rodent and some human studies, emphasized:
1. **Place cells**: Neurons that fire when an animal is at a specific location (self-position coding)
2. **Head-direction cells**: Neurons that fire when facing a specific direction
3. **Grid cells**: Neurons with periodic spatial firing patterns

This framework focused on neurons representing the animal's current spatial context. While there was emerging evidence that MTL neurons could represent remote locations (e.g., goal cells, spatial view cells), this was less established, particularly in humans. The dominant assumption was that spatial navigation relies primarily on representations of current position and heading.

### What this paper contributes

This paper substantially extends the prevailing model by demonstrating that:

1. **Spatial-target cells represent remote goals**: A significant population (20%) of human MTL neurons encode the location of remote spatial targets during navigation, distinct from the subject's current position. This suggests the MTL maintains representations of future goals, not just current state.

2. **First evidence of human head-direction cells**: The identification of heading-modulated cells provides the first evidence of head-direction representations in humans, showing conserved mechanisms across species.

3. **Serial-position coding in EC**: The finding of serial-position cells, particularly prominent in entorhinal cortex, links human MTL coding to temporal sequence representations observed in rodents and suggests the EC plays a role in tracking event order.

4. **Task-dependent coding**: The relative absence of traditional place cells (6%, not significant) compared to spatial-target cells suggests that MTL coding schemes are flexibly deployed according to task demands—when the task requires encoding remote locations, the MTL prioritizes goal representations over self-position coding.

5. **Multiple parallel coding schemes**: The coexistence of spatial-target, heading-modulated, and serial-position cells (with minimal overlap between populations) suggests the MTL employs distributed, parallel representations to support complex spatial navigation and memory.

### Brain regions & systems

- **Medial temporal lobe (MTL)**: The overarching region studied, critical for memory and spatial navigation
- **Hippocampal formation (HF)**: 45 neurons recorded; contained spatial-target cells (9/45), heading-modulated cells (3/45), serial-position cells (3/45), and place-like cells (3/45)
- **Entorhinal cortex (EC)**: 71 neurons recorded; prominent location for spatial-target cells (12/71), heading-modulated cells (7/71), and particularly enriched for serial-position cells (16/71 = 23%)
- **Parahippocampal/perirhinal cortex (PC)**: 15 neurons recorded; contained spatial-target cells (5/15), heading-modulated cells (3/15), and serial-position cells (1/15)

### Mechanistic insight

This paper does not meet the high bar for mechanistic insight. While it identifies neural correlates of spatial target representation, heading direction, and serial position, it does not present or formalize a specific algorithm for how these representations are computed or used. The study provides descriptive electrophysiology showing that MTL neurons carry specific information, but does not specify the computational process by which spatial targets are encoded, how these representations guide navigation, or how the different cell types (spatial-target, heading, serial-position) interact to support behavior. The findings constrain future computational models by showing what variables must be represented, but do not themselves constitute a mechanistic account.

### Limitations & open questions

- **Small sample sizes per region**: Only 15 neurons recorded from parahippocampal/perirhinal cortex, limiting power to detect effects in this region
- **Clinical recording constraints**: Recordings were from epilepsy patients with electrodes placed for clinical purposes, not optimized for research questions; may not sample all relevant MTL subregions equally
- **No subicular recordings**: No heading-modulated cells were found in the subiculum, unlike rodent studies; this may reflect sampling limitations
- **Limited place cell observation**: Traditional place cells were rare (6%, not significant), which may reflect task demands rather than absence; task encouraged attention to remote targets rather than current position
- **Memory cells not significant**: Only 8% of cells showed subsequent memory effects, not significantly above chance; different from fMRI findings
- **Causal mechanisms unclear**: Correlational study cannot establish whether spatial-target cell activity causes or merely reflects navigation to targets
- **No eye tracking**: Cannot rule out that spatial-target cells encode gaze direction or attention rather than spatial location per se
- **Single environment**: All recordings from one virtual environment; unclear if coding generalizes across contexts

### Connections & keywords

**Key citations**:
- Ekstrom et al. (2003) — foundational human single-neuron navigation study that identified goal cells and view cells
- Miller et al. (2013) — prior work on hippocampal formation spatial context and memory retrieval
- O'Keefe & Dostrovsky (1971) — seminal place cell discovery
- Taube et al. (1990) — foundational head-direction cell work in rodents
- Tsao et al. (2018) — time cells in lateral entorhinal cortex (discussed in relation to serial-position cells)
- Aronov et al. (2017) — discussed regarding task-dependent coding in hippocampus

**Named models or frameworks**:
- Treasure Hunt task — virtual reality spatial memory paradigm
- Spatial-target cells — novel cell type identified in this paper
- Head-direction cells — first identification in humans
- Serial-position cells — neurons coding for temporal order within trials
- Place cells — traditional spatial coding (rare in this task)

**Brain regions**:
- Medial temporal lobe (MTL)
- Hippocampal formation (HF)
- Entorhinal cortex (EC)
- Parahippocampal cortex (PC)
- Perirhinal cortex (PC)
- Subiculum (mentioned but no recordings)

**Keywords**:
- spatial-target cells
- head-direction cells
- serial-position cells
- place cells
- medial temporal lobe
- hippocampus
- entorhinal cortex
- spatial navigation
- goal-directed behavior
- single-neuron recording
- virtual reality
- episodic memory
- electrophysiology
- human neuroscience

### Related wiki pages
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
