---
source_file: wikenheiser2015_theta_sequences_goals.md
paper_id: wikenheiser2015_theta_sequences_goals
title: "Hippocampal theta sequences reflect current goals"
authors:
  - "Andrew M Wikenheiser"
  - "A David Redish"
year: 2015
journal: "Nature Neuroscience"
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
  - striatum
  - ventral_striatum
keywords:
  - hippocampus
  - theta_oscillations
  - theta_sequences
  - place_cells
  - phase_precession
  - goal_directed_behavior
  - spatial_navigation
  - prospective_coding
  - decision_making
  - volitional_behavior
  - ensemble_activity
  - cognitive_map
  - foraging
  - ca1
  - spatial_planning
  - hippocampal
  - theta
  - sequences
  - reflect
  - current
key_citations:
  - gupta2012_theta_sequences_experience
  - johnson2007_hippocampus_decision
wiki_pages:
  - wiki/topics/hippocampal_replay_and_schema_guided_generalization
  - wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation
---

### One-line summary

Hippocampal theta sequences show goal-dependent modulation, with look-ahead distance varying according to the distance to the rat's intended destination, providing evidence that theta sequences contain information about current spatial goals.

### Background & motivation

The hippocampus is critical for simulating future possibilities and goal-directed decision-making. While theta sequences (time-compressed trajectories through space organized by theta cycles) are a promising candidate mechanism for prospective planning, their connection to goal-directed behavior was unclear. This study tested whether theta sequences contain information about currently active goals rather than merely reflecting sensory-cued recall processes.

### Methods

- **Task**: Value-guided decision-making task on a circular track with three food dispensers, each with unique delays (1–32 s). Rats chose whether to wait for delayed reward or skip to the next site.
- **Subjects**: Four male Fisher-Brown Norway hybrid rats, implanted with tetrode arrays targeting dorsal CA1 hippocampus.
- **Recordings**: 1,263 cells recorded across 26 sessions; ensemble sizes 25–62 neurons. Local field potentials recorded from hippocampal fissure.
- **Analysis**: Theta sequence look-ahead measured as average position of spikes in final quarter of theta cycle relative to rat's current location. Trajectory types: one-segment (next site), two-segment (skip one), three-segment (complete lap).

### Key findings

- Theta sequence look-ahead distance varied with goal distance: longest for three-segment trajectories, intermediate for two-segment, shortest for one-segment (F₂,₂₀₂₆₈ = 172.09, P < 0.001; all pairwise comparisons P < 0.001).
- Look-ahead did not depend on how far rats had traveled: on arrival at goals, look-ahead was constant regardless of trajectory type (F₂,₂₀₇₈₉ = 0.56, P = 0.57).
- Multinomial logistic regression showed theta look-ahead predicted goal location at above-chance levels at trajectory initiation (z₂₉₉ = 17.03, P < 0.001; sign test) but not at goal arrival (z₂₉₉ = 0.28, P = 0.77).
- Place field size was modulated by trajectory type: fields on three-segment trajectories were ~20% (10 cm) larger than on one-segment trajectories (F₂,₂₅₅ = 5.53, P = 0.0044).
- Trial-by-trial analysis showed initial spike location varied with goal destination (F₂,₁₀₆₅₆ = 122.02, P < 0.001), confirming modulation occurred on single trials, separable from place field expansion phenomena.
- Control analyses: surrogate data models using speed, acceleration, or speed × acceleration could not reproduce goal-dependent look-ahead effects (all P > 0.5).

### Computational framework

The paper conceptualizes hippocampal theta sequences as implementing a prospective spatial computation—moment-by-moment prediction of upcoming positions during active behavior. This aligns with dynamical systems and predictive coding frameworks, where neural sequences serve to simulate future trajectories for planning. The work suggests theta sequences operate as an online planning mechanism, maintaining spatial goals throughout journey execution.

### Prevailing model of the system under study

Prior to this study, theta sequences were understood as time-compressed trajectory representations organized by theta cycles, beginning slightly behind the animal's position and projecting forward. While considered candidates for prospective planning, the prevailing view held that forward-shifted representations might reflect sensory-cued recall processes driven by landmark-place associations rather than goal-directed computation. The relationship between theta sequences and volitional decision-making remained unclear.

### What this paper contributes

This paper establishes that hippocampal theta sequences encode information about current spatial goals, not merely sensory features of the environment. The extent of theta sequence look-ahead varies moment-by-moment with the animal's intended destination, providing evidence that theta sequences participate in goal-directed planning rather than passive predictive recall. This reveals a mechanism by which the hippocampus could use spatial representations to support decision-making, maintaining prospective plans online during behavior execution.

### Brain regions & systems

- **Hippocampus CA1 (dorsal)**: Primary recording site; theta sequences showed goal-dependent modulation; proposed locus of prospective spatial planning signals.
- **Ventral striatum**: Referenced as receiving hippocampal inputs; ramp cells phase precess to hippocampal theta, potentially imbuing spatial paths with reward information.
- **Prefrontal cortex (PFC)**: Discussed as interacting with hippocampus during decision-making; theta coherence increases between structures during decisions; theta entrainment of PFC spiking predicts accurate performance.

### Mechanistic insight

The paper provides neural evidence linking theta sequence dynamics to goal-directed behavior, though it does not present a formal algorithmic model. The core mechanistic claim is that hippocampal ensembles perform moment-by-moment prediction of upcoming spatial positions, with the extent of prediction modulated by current goals. At Marr's levels:

- **Computational**: The brain solves the problem of planning future trajectories to valued goals during ongoing navigation.
- **Algorithmic**: Theta sequences implement time-compressed trajectory representations where look-ahead distance encodes goal distance; single-trial modulation of place cell activation timing achieves this flexibility.
- **Implementational**: The mechanism is realized through theta-paced ensemble spiking in CA1, coordinated by gamma oscillations, with phase precession governing the temporal organization of place cell firing within cycles.

### Limitations & open questions

- Causal relationship between theta sequences and decision-making not established; sequences could reflect rather than drive behavior.
- Relationship between theta- and sharp-wave ripple (SWR)-associated planning signals remains untested.
- Whether theta sequence modulation is specific to spatial goals or generalizes to other cognitive variables is unclear.
- The mechanism by which goal information modulates theta sequence extent is not specified.
- Interactions with downstream structures (ventral striatum, PFC) during theta-modulated planning are hypothesized but not directly tested.

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) - The Hippocampus as a Cognitive Map
- Skaggs et al. (1996) - Theta phase precession and sequence compression
- Dragoi & Buzsaki (2006) - Temporal encoding of place sequences
- Gupta et al. (2012) - Segmentation of spatial experience by theta sequences
- Johnson & Redish (2007) - CA3 ensemble representations of forward paths
- Pfeiffer & Foster (2013) - Hippocampal place-cell sequences depict future paths to goals
- Jadhav et al. (2012) - Awake hippocampal sharp-wave ripples support spatial memory

**Named models or frameworks:**
- Theta sequences / phase precession
- Cognitive map theory
- Prospective coding / planning
- Value-guided decision-making

**Brain regions:**
- Hippocampus CA1 (dorsal)
- Hippocampus CA3
- Ventral striatum
- Prefrontal cortex (PFC)

**Keywords:**
hippocampus, theta oscillations, theta sequences, place cells, phase precession, goal-directed behavior, spatial navigation, prospective coding, decision-making, volitional behavior, ensemble activity, cognitive map, foraging, CA1, spatial planning

### Related wiki pages
- [[wiki/topics/hippocampal_replay_and_schema_guided_generalization|Hippocampal replay and schema-guided generalization]]
- [[wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning|Hippocampal sharp-wave ripple replay and prefrontal coordination during planning]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]
- [[wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation|Hippocampal–prefrontal mechanisms of route planning and detour navigation]]
