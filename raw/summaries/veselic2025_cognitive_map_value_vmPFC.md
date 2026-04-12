---
source_file: veselic2025_cognitive_map_value_vmPFC.md
paper_id: veselic2025_cognitive_map_value_vmPFC
title: "A cognitive map for value-guided choice in the ventromedial prefrontal cortex"
authors:
  - "Sebastijan Veselic"
  - "Timothy H. Muller"
  - "Elena Gutierrez"
  - "Timothy E.J. Behrens"
  - "Laurence T. Hunt"
  - "James L. Butler"
  - "Steven W. Kennerley"
year: 2025
journal: Cell
paper_type: empirical
contribution_type: empirical
species:
  - macaque
methods:
  - electrophysiology
brain_regions:
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - ventromedial_prefrontal_cortex
  - dorsolateral_prefrontal_cortex
  - medial_temporal_lobe
frameworks:
  - reinforcement_learning
  - tolman_eichenbaum_machine
keywords:
  - cognitive_map
  - grid_like_coding
  - hexadirectional_modulation
  - theta_oscillations
  - sharp_wave_ripples
  - value_guided_decision_making
  - ventromedial_prefrontal_cortex
  - vector_based_navigation
  - economic_choice
  - abstract_space
  - phase_dependent_coding
  - replay
  - non_human_primate
  - electrophysiology
  - local_field_potential
  - cognitive
  - map
  - value
  - guided
  - choice
key_citations:
  - bush2015_grid_cells_navigation_vector
  - bongioanni2021_novel_choice_neural
  - constantinescu2016_gridlike_conceptual_knowledge
  - behrens2018_cognitive_map_organizing_knowledge
  - fyhn2007_remapping_grid_realignment
wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
  - wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_hidden_task_state
---

### One-line summary

The vmPFC constructs cognitive maps of value space using grid-like codes and theta-dependent neural representations to support flexible value-guided decision-making.

### Background & motivation

Economic decision-making has traditionally been conceptualized as comparing values in a common currency format. However, this framework cannot explain how animals make novel choices that require inferring or constructing value from previous experience. The medial temporal lobe (MTL) builds cognitive maps that encode relationships between entities, supporting flexible behavior through grid-like codes and sharp-wave ripples (SWRs). Recent work found grid-like codes in vmPFC during passive navigation between trials, raising the question of whether these mechanisms are actively deployed during choice itself.

### Methods

- Two male rhesus macaques performed a two-alternative forced-choice task where options were constructed from two cues (reward magnitude × reward probability) that never formed an option during training
- Dataset 1: simultaneous option presentation; Dataset 2: sequential option presentation (independent replication)
- Single-unit recordings from ACC (n=198), dlPFC (n=156), OFC (n=195), and vmPFC (n=160)
- LFP recordings from 97 vmPFC channels (theta: 5-8 Hz; ripple: 80-180 Hz)
- Hexadirectional analysis to detect 6-fold periodic modulation (grid-like coding)
- Phase-aligned analyses to examine theta-dependency of neuronal firing
- Non-negative matrix factorization for ripple detection with SNR thresholding

### Key findings

- vmPFC LFP theta (5-8 Hz) showed significant hexadirectional modulation during choice (t(15)=3.20, pBonferroni=0.03, Cohen's d=0.79), with 6-fold periodicity, indicating grid-like coding of value space
- No significant grid-like code in ACC (t(40)=1.54, p=0.13), dlPFC (t(31)=0.12, p=0.182), or OFC (t(33)=1.73, p=0.09) during the same time window
- Grid orientations were stable within stimulus sets (t(8)=4.77, pBonferroni=0.007) but realigned across stimulus sets (t(15)=0.06, p=0.95), mirroring grid cell behavior in spatial environments
- vmPFC neurons showed theta-phase dependent firing, firing most at theta troughs (F(9,159)=8.87, p<0.001)
- Grid-like code in vmPFC neurons was theta-phase dependent, occurring at theta troughs (t(159)=3.08, pBonferroni=0.012)
- Chosen value code also emerged in vmPFC neurons at theta troughs but on separate theta cycles from the grid-like code, suggesting sequential construction of cognitive map followed by value readout
- Neurons with high grid-like coding exhibited patchy, irregular firing fields across value space and showed more periodic activation on trials with longer navigation trajectories (t(52)=3.97, p<0.001)
- Sharp-wave ripples (SWRs; 90-140 Hz) were detected in vmPFC (n=4,162 events, median duration=103 ms), occurring predominantly before and after choice and at feedback
- Ripple frequency in vmPFC predicted session-level choice accuracy, with higher ripple rates associated with better performance
- Ripple frequency increased after rewarded trials compared to unrewarded trials, suggesting involvement in consolidation
- Results replicated in an independent dataset (Dataset 2: t(10)=2.74, p=0.02, Cohen's d=0.83)

### Computational framework

Cognitive map theory and vector-based navigation from spatial cognition applied to economic decision-making. The framework treats value-guided choice as navigation through an abstract 2D value space (reward magnitude × reward probability), where options are locations and choices are trajectories. Grid-like coding provides a 6-fold symmetric representation supporting vector-based navigation and inference. Theta oscillations (5-8 Hz) provide a temporal framework for organizing sequential representations. Sharp-wave ripples (80-180 Hz) may support replay, consolidation, and model-based planning. The framework integrates reinforcement learning (value construction) with spatial navigation mechanisms (map-based inference).

### Prevailing model of the system under study

The prevailing model of economic decision-making in PFC posits that value is represented in a common currency format, facilitating efficient action selection through direct comparison. This model predicts strong chosen value signals in vmPFC neurons, consistent with fMRI findings but inconsistent with many electrophysiological studies. The model assumes value representations are stable and comparable across options, without requiring structured representations of task space. The paper notes that this framework cannot explain how animals make novel choices requiring inference or value construction from previous experience.

### What this paper contributes

This paper establishes that vmPFC utilizes cognitive map-based computations for value-guided choice, representing an alternative architecture to the common currency model. The key contributions are:

1. Demonstration that vmPFC constructs a cognitive map of value space using grid-like codes during choice itself, not just during passive navigation between trials
2. Evidence that grid-like coding in vmPFC shows environment-specific realignment (stable within stimulus sets, realigned across sets), mirroring spatial grid cells
3. Discovery that vmPFC neurons deploy theta-phase-dependent codes, with grid-like representations and chosen value signals occurring on separate theta cycles
4. First documentation of sharp-wave ripples in non-human primate vmPFC, showing they are modulated by choice accuracy and reward history
5. Evidence that the neural geometry of the cognitive map in vmPFC is better explained by objective (veridical) than subjective (distorted) representations, suggesting downstream regions may implement value distortions

These findings suggest that well-characterized MTL mechanisms for spatial navigation have been redeployed by vmPFC for abstract value-guided decision-making.

### Brain regions & systems

- **vmPFC (ventromedial prefrontal cortex)**: Primary focus; contains grid-like codes for value space, theta-modulated neuronal firing, and sharp-wave ripples; represents choices as locations in a 2D cognitive map; shows weak canonical chosen value signals without theta alignment
- **ACC (anterior cingulate cortex)**: Shows strong canonical chosen value and chosen value difference coding; no significant grid-like code
- **dlPFC (dorsolateral prefrontal cortex)**: Shows chosen value coding; no significant grid-like code; exploratory analyses suggest subjective (distorted) value coding
- **OFC (orbitofrontal cortex)**: Shows chosen value and chosen value difference coding; no significant grid-like code during choice window (earlier temporal window shows effect that doesn't survive cluster correction)
- **MTL (medial temporal lobe)**: Discussed as anatomically connected to vmPFC and source of cognitive map computations; not directly recorded

### Mechanistic insight

This paper provides strong mechanistic insight by linking algorithmic and implementational levels:

**Computational**: The brain solves value-guided choice by treating it as vector-based navigation through a cognitive map of value space. This allows inference and flexible choice by computing trajectories between option locations rather than simple value comparison.

**Algorithmic**: The implementation uses a grid-like code (6-fold periodic modulation) to represent the abstract 2D value space (reward magnitude × reward probability). Theta oscillations (5-8 Hz) organize sequential processing: grid-like representations occur at theta troughs on one set of cycles, followed by chosen value readout on subsequent theta cycles. Sharp-wave ripples (90-140 Hz) occur at choice and feedback, correlated with choice accuracy and reward history, suggesting consolidation and replay mechanisms.

**Implementational**: Grid-like coding is implemented in vmPFC LFP theta frequency and single neuron firing (patchy, irregular firing fields). Theta-phase modulation of firing is consistent across the vmPFC population (firing most at troughs). Grid orientations realign across stimulus sets (environments) but remain stable within sets, matching spatial grid cell properties. SWRs are localized to 90-140 Hz with sharp-wave components, indicating specialized circuit generation rather than noise.

The paper provides neural data (recordings from 724 neurons and 497 LFP channels across 4 PFC regions) that specifically support the grid-based navigation algorithm over alternative value comparison mechanisms.

### Limitations & open questions

- **Direct evidence for grid cells**: Could not provide direct evidence of grid cells in vmPFC using traditional spatial navigation approaches; relied on indirect measures (hexadirectional analysis) typical of LFP/MEG/fMRI studies
- **Sex limitation**: Only male subjects used; relationship between sex and results unknown
- **Origin of grid-like code**: Unclear whether grid-like code in vmPFC LFP originates in entorhinal cortex (via anatomical connectivity) or is generated by local vmPFC circuitry; observed grid-like code in vmPFC neurons suggests local generation
- **Origin of SWRs**: Unclear whether ripples originate in hippocampal formation or vmPFC itself
- **Anatomical specificity**: Grid-like coding in human fMRI found in both vmPFC and OFC; non-human primate fMRI reported in mPFC (closer to BA 10); need to dissociate contributions across PFC subregions
- **Precise role of ripples**: While ripples are modulated by task events, their precise role in value-based decision-making remains unclear (possible roles: retrieval/consolidation, replay of task states, model-based planning)
- **Theta-phase discrepancies**: Discrepancy between fMRI and electrophysiology findings for chosen value signals in vmPFC may relate to phase-dependent coding; longer averaging windows may obscure phase-dependent signals

### Connections & keywords

- **Key citations**: Padoa-Schioppa 2011 (neurobiology of economic choice), Bush et al. 2015 (grid cells for navigation), Bongioanni et al. 2021 (grid-like code in monkeys), Constantinescu et al. 2016 (grid-like code in humans), Maidenbaum et al. 2018 (hexadirectional modulation), Behrens et al. 2018 (What Is a Cognitive Map?), Foster 2017 (replay), Khodagholy et al. 2017 (ripple oscillations in cortex), Fyhn et al. 2007 (grid realignment)
- **Named models/frameworks**: Cognitive map theory, vector-based navigation, hexadirectional analysis, prospect theory, reinforcement learning, model-based planning, Tolman-Eichenbaum Machine
- **Brain regions**: vmPFC, ACC, dlPFC, OFC, MTL, hippocampus, entorhinal cortex
- **Keywords**: cognitive map, grid-like coding, hexadirectional modulation, theta oscillations, sharp-wave ripples, value-guided decision-making, ventromedial prefrontal cortex, vector-based navigation, economic choice, abstract space, phase-dependent coding, replay, non-human primate, electrophysiology, local field potential

### Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
- [[wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_hidden_task_state|Orbitofrontal cortex as a cognitive map of hidden task state]]
