---
source_file: yu2018_hippocampal_cortical_memory.md
paper_id: yu2018_hippocampal_cortical_memory
title: "Specific hippocampal representations are linked to generalized cortical representations in memory"
authors:
  - "Jai Y. Yu"
  - "Daniel F. Liu"
  - "Adrianna Loback"
  - "Irene Grossrubatscher"
  - "Loren M. Frank"
year: 2018
journal: "Nature Communications"
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - foraging_task
methods:
  - tetrode_recording
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - prelimbic_cortex
frameworks:
  - attractor_networks
keywords:
  - sharp_wave_ripples
  - memory_reactivation
  - place_cells
  - prefrontal_cortex
  - hippocampus
  - generalization
  - abstraction
  - schema
  - consolidation
  - spatial_memory
  - many_to_one_mapping
  - complementary_learning_systems
  - awake_replay
  - task_structure
  - ensemble_coding
  - learning_systems
  - specific
  - hippocampal
  - representations
  - linked
key_citations:
  - jadhav2016_hippocampal_prefrontal_swr
wiki_pages:
  - wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation
  - wiki/topics/sharp_wave_ripple_associated_place_cell_replay_in_spatial_memory_consolidation
---

### One-line summary

Specific hippocampal place representations are preferentially reactivated with generalized prefrontal cortical task representations during awake memory reactivation events, suggesting a mechanism linking specific experiences to general knowledge.

### Background & motivation

The hippocampus and prefrontal cortex (PFC) are thought to play complementary roles in memory, with the hippocampus supporting specific episodic memories and the PFC supporting generalized knowledge that abstracts across experiences. While hippocampal-cortical coactivity patterns are reinstated during sharp-wave ripple (SWR) memory reactivation events, it was unknown whether both specific and general features of experience are simultaneously reactivated. This paper investigates how the brain maintains links between specific and general memory representations.

### Methods

- **Subjects**: 6 male Long-Evans rats (500-700g, 4-9 months old)
- **Task**: Well-learned spatial foraging task with multiple paths; rats traveled between 4 potential reward wells (2 active at a time) via different trajectories
- **Recordings**: Simultaneous extracellular recordings from dorsal CA1 (234 cells) and dorsal PFC (578 cells, anterior cingulate and dorsal prelimbic cortex) using tetrodes
- **SWR detection**: Filtered LFP (150-250 Hz), Hilbert transform, Gaussian smoothing; events detected at speed <4 cm/s at reward wells
- **Analysis**: Trial-normalized firing rate maps, Pearson correlation for firing similarity measures (Rmedian = all-trial similarity; Rmax = maximum within-trajectory similarity), Generalized Linear Models (GLMs) to predict SWR participation

### Key findings

- CA1 cells showed location-specific firing with low all-trial similarity (Rmedian) but high within-trajectory reliability (Rmax), consistent with specific spatial representations
- PFC cells showed heterogeneous activity patterns, with a subset showing high all-trial similarity (Rmedian > 0.5) representing general task features across trajectories
- PFC cells with high all-trial similarity were significantly enriched in SWR reactivation events compared to non-reactivated PFC cells (Kolmogorov-Smirnov test: p < 10^-3)
- Trial similarity measures (Rmedian, Rmax, Intertraj. Rmedian) were better predictors of SWR reactivation than firing rate, speed correlation, or trial coverage variables (GLM: 7.4-10.8% variance explained vs. 3.8%)
- Reactivated PFC cells showed a "many-to-one" mapping: different hippocampal path location reactivations engaged similar PFC firing patterns, whereas hippocampal path vs. well location reactivations engaged different PFC patterns
- Pairwise CA1-PFC coactivity during ongoing experience was a poor predictor of reactivation, consistent with learned transformations in hippocampal-cortical associations

### Computational framework

The paper operates within the framework of **complementary learning systems**, where the hippocampus and neocortex play distinct but interacting roles in memory. The hippocampus is conceptualized as storing specific episodic representations (attractor states for particular spatial locations), while the prefrontal cortex gradually abstracts generalizable task structure through repeated experiences. The paper formalizes this through a **many-to-one mapping** between hippocampal and cortical representations: multiple specific hippocampal location representations can converge onto single generalized PFC task representations during memory reactivation. This framework suggests that memory consolidation involves not just transfer of information from hippocampus to cortex, but the formation of structured associations between specific and general representations that could support abstraction and schema formation.

### Prevailing model of the system under study

Prior to this study, the prevailing understanding was that the hippocampus and prefrontal cortex maintain stored associations that are transiently reinstated during hippocampal sharp-wave ripple (SWR) events. Earlier work established that early in learning, the degree of hippocampal-PFC co-firing during ongoing experience predicts their coactivity during SWRs. However, once the environment and task become familiar, hippocampal-PFC coactivity during ongoing experience is no longer predictive of SWR coactivity. This raised the question of what determines which PFC representations are reactivated with hippocampal representations in familiar settings, and whether these associations could reflect links between specific hippocampal representations and potentially more general PFC task representations.

### What this paper contributes

This paper demonstrates that in a familiar task, specific hippocampal place representations are preferentially reactivated with a subset of prefrontal cortical representations that generalize across different spatial trajectories (high all-trial similarity), rather than with PFC representations that are specific to individual trajectories. This reveals a "many-to-one" mapping where multiple hippocampal location representations can link to a single generalized PFC task representation during memory reactivation. The findings extend the complementary learning systems framework by showing that hippocampal-cortical networks maintain structured links between specific and general representations, which could support memory abstraction and the embedding of individual experiences in broader knowledge structures. The results also explain why pairwise coactivity during ongoing experience becomes uncorrelated with reactivation after learning: the network transforms to favor associations between specific hippocampal and general cortical representations that may not have been strongly coactive during behavior.

### Brain regions & systems

- **Hippocampus (dorsal CA1)**: Encodes specific spatial locations via place cells; shows location-specific firing with low all-trial similarity (Rmedian) but high within-trajectory reliability (Rmax); reactivated during SWRs
- **Prefrontal cortex (dorsal PFC, including anterior cingulate and dorsal prelimbic cortex)**: Shows heterogeneous activity patterns; subset encodes general task features with high all-trial similarity (Rmedian > 0.5) across different trajectories; preferentially reactivated with hippocampal representations during SWRs

### Mechanistic insight

This paper provides evidence for a **mechanism of memory consolidation and abstraction** that meets the high bar for mechanistic insight. The paper identifies an algorithmic process—selective reactivation of generalized cortical representations alongside specific hippocampal representations during SWR events—and provides neural data showing that this many-to-one mapping is specifically implemented in the hippocampal-prefrontal circuit.

**Computational level**: The brain solves the problem of linking specific episodic memories to generalizable knowledge structures (schemas), enabling appropriate generalization while preserving memory specificity. This addresses how individual experiences become embedded in broader knowledge frameworks.

**Algorithmic level**: The mechanism involves a learned many-to-one mapping where multiple specific hippocampal location representations can converge onto single generalized PFC task representations during memory reactivation. The selection is based on all-trial similarity (Rmedian), with PFC cells showing high generalization across trajectories preferentially reactivated. This mapping is task-relevant: different hippocampal path location reactivations engage similar PFC patterns, but path vs. well location reactivations engage different PFC patterns.

**Implementational level**: The mechanism is implemented through coordinated spiking activity in hippocampal CA1 place cells and prefrontal cortical neurons during sharp-wave ripple (SWR) events. The physical implementation involves specific patterns of reactivation during awake rest periods at reward locations, distinct from ongoing behavioral coactivity. The transformation from experience-specific to generalized associations emerges through learning, as the network enriches links between frequently co-occurring features across multiple experiences.

### Limitations & open questions

- The study was conducted in well-trained animals with at least 5 days of task exposure; the transformation of hippocampal-cortical associations with learning was inferred by comparing to prior studies rather than tracked longitudinally within the same animals
- The mechanism by which coordinated hippocampal-cortical communication during sleep drives changes in hippocampal-cortical associations remains unknown
- Whether the content of hippocampal-cortical memory reactivation during sleep SWRs reflects the same specific-to-general associations as awake SWRs is not directly tested
- The specific cellular and circuit mechanisms (e.g., specific cell types, neuromodulators) that enable selective reactivation of generalized PFC representations are not identified
- The computational principles governing how the network learns to map specific hippocampal representations to general cortical representations remain to be formalized

### Connections & keywords

**Key citations**: Preston & Eichenbaum (2013), Blumenfeld & Ranganath (2007), Moscovitch et al. (2016), Miller & Cohen (2001), O'Reilly & Rudy (2001), McClelland et al. (1995), Jadhav et al. (2016), Tang et al. (2017), Yu et al. (2017), Morrissey et al. (2017)

**Named models or frameworks**: Complementary learning systems theory, attractor networks, schema theory, sharp-wave ripple (SWR) reactivation, many-to-one mapping

**Brain regions**: Hippocampus (dorsal CA1), prefrontal cortex (PFC, anterior cingulate cortex, dorsal prelimbic cortex), corpus callosum

**Keywords**: sharp-wave ripples, memory reactivation, place cells, prefrontal cortex, hippocampus, generalization, abstraction, schema, consolidation, spatial memory, many-to-one mapping, complementary learning systems, awake replay, task structure, ensemble coding, learning systems

### Related wiki pages
- [[wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation|Hippocampal–prefrontal mechanisms of route planning and detour navigation]]
- [[wiki/topics/sharp_wave_ripple_associated_place_cell_replay_in_spatial_memory_consolidation|Sharp-wave ripple-associated place-cell replay in spatial memory consolidation]]
