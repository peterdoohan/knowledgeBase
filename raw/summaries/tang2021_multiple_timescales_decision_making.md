---
source_file: tang2021_multiple_timescales_decision_making.md
paper_id: tang2021_multiple_timescales_decision_making
title: "Multiple time-scales of decision-making in the hippocampus and prefrontal cortex"
authors:
  - "Wenbo Tang"
  - "Justin D Shin"
  - "Shantanu P Jadhav"
year: 2021
journal: eLife
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - tetrode_recording
  - bayesian_decoding
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
frameworks:
  - reinforcement_learning
  - model_based_rl
  - bayesian_inference
keywords:
  - theta_oscillations
  - theta_sequences
  - prefrontal_cortex
  - hippocampus
  - sharp_wave_ripples
  - replay
  - decision_making
  - working_memory
  - spatial_navigation
  - ensemble_dynamics
  - population_coding
  - sequence_coding
  - cycle_skipping
  - vicarious_memory_recall
  - multi_timescale_dynamics
  - bayesian_decoding
  - theta_phase_precession
  - attractor_dynamics
  - memory_guided_behavior
  - multiple
key_citations:
  - shin2019_hippocampal_prefrontal_replay_b
  - johnson2007_hippocampus_decision
wiki_pages:
  - wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning
  - wiki/topics/sharp_wave_ripple_associated_hippocampal_replay
---

### One-line summary

Hippocampal theta sequences encode alternative choices for deliberation and are coordinated with prefrontal theta sequences that predict upcoming choices, establishing cooperative multi-timescale interactions between hippocampus and prefrontal cortex for memory-guided decision-making.

### Background & motivation

The prefrontal cortex (PFC) and hippocampus are crucial for memory-guided decision-making. While neural activity at behavioral timescales (seconds) has been extensively studied in decision circuits, fast cognitive-timescale activity patterns (100-200 ms) such as hippocampal theta sequences may also underlie decision processes. However, whether theta sequences exist in PFC and how hippocampal and prefrontal sequences interact across multiple timescales to support decision-making was unknown.

### Methods

- **Subjects**: Nine adult male Long-Evans rats
- **Task**: Spatial working-memory delayed alternation task on a W-maze (inbound reference-memory and outbound working-memory trials). Animals learned the task over eight 15-20 min sessions in a single day
- **Recordings**: Simultaneous multi-tetrode recordings from dorsal CA1 hippocampus and PFC (mean ± SEM = 43.9 ± 7.6 CA1 place cells, 29.8 ± 5.6 PFC cells per session)
- **Analysis**: Memoryless Bayesian decoding to identify behavioral sequences (120 ms bins) and theta sequences (20 ms bins); theta sequence detection using weighted correlation and goodness-of-fit measures with shuffling procedures; SVM classifiers for trial-by-trial choice prediction

### Key findings

- **Behavioral sequences**: Both CA1 and PFC exhibited slow behavioral sequences (spanning ~8 seconds) that maintained representations of current choices during navigation. Decoding accuracy for choice on the center stem increased over learning in CA1 but remained stable in PFC
- **Theta sequences in PFC**: First demonstration of theta sequences in PFC, nested within behavioral sequences. Prevalence was similar to CA1 (~70% of CA1 and ~60% of PFC theta sequences were forward sequences). Sequence scores and slopes increased over learning in both regions
- **Look-ahead differences**: During working-memory-guided outbound navigation, theta sequences in both regions showed greater "look-ahead" (extended future representation) compared to reference-memory-guided inbound navigation. This was associated with more asymmetric spatial fields (extended initial tails) on outbound trajectories
- **Choice representations**: Before the choice point, CA1 theta sequences encoded both actual and alternative choices equivalently (vicarious memory recall), whereas PFC theta sequences preferentially encoded the upcoming actual choice. After the choice point, both regions encoded the current choice
- **CA1-PFC coordination**: When CA1 and PFC theta sequences occurred simultaneously, they showed coherent choice representations when CA1 represented the actual choice, but not when CA1 represented alternatives
- **Error trials**: Behavioral and theta sequences were preserved during incorrect trials, but CA1-PFC replay sequences during inter-trial periods were impaired prior to incorrect navigation, suggesting replay primes initial decisions while theta sequences maintain working memory during navigation

### Computational framework

The paper employs a **dynamical systems and probabilistic decoding framework** for analyzing neural population activity. The core methodology uses Bayesian inference to decode spatial position and trajectory choice from population spike trains, treating the posterior probability matrix as a representation of the animal's internal state. The framework distinguishes between:
- **Behavioral timescale mechanisms**: Sequential activation patterns that span seconds, maintaining working memory through persistent or sequential activity
- **Cognitive/compressed timescale mechanisms**: Theta sequences (100-200 ms) that enable rapid vicarious memory recall and deliberation; replay sequences during SWRs that prime future decisions

The paper also uses concepts from reinforcement learning and model-based planning, noting that internally generated sequences simulating future scenarios are key features of model-based computation.

### Prevailing model of the system under study

The prevailing model before this study held that:
1. Hippocampal and prefrontal circuits support memory-guided decision-making through behavioral-timescale activity patterns (persistent activity or slow sequences spanning seconds)
2. Hippocampal theta sequences during navigation represent upcoming spatial paths ("look-ahead"), potentially supporting planning
3. Hippocampal replay sequences during sharp-wave ripples (SWRs) reactivate past and future trajectories and interact with PFC during memory-guided decisions
4. Theta sequences in PFC had not been demonstrated, and the specific roles of fast-timescale sequences in hippocampal-prefrontal coordination for decision-making were unknown

### What this paper contributes

This paper makes several key contributions that refine and extend the prevailing model:

1. **Discovery of PFC theta sequences**: First demonstration that PFC exhibits theta sequences similar to hippocampus, nested within behavioral sequences. This establishes that fast-timescale sequential dynamics are not unique to hippocampus but are a shared feature of hippocampal-prefrontal circuits.

2. **Multi-timescale framework**: Provides a unified framework integrating behavioral-timescale sequences (maintenance of current choice) with cognitive-timescale sequences (theta sequences for deliberation, replay sequences for decision priming). Shows these mechanisms operate in parallel but serve distinct computational functions.

3. **Dissociable roles of CA1 and PFC theta sequences**: Reveals that before the choice point, CA1 theta sequences encode both actual and alternative choices (vicarious memory recall), while PFC theta sequences preferentially predict the upcoming choice. This suggests complementary roles: hippocampus for deliberating over options, PFC for selecting actions.

4. **Mechanism of look-ahead modulation**: Shows that theta sequence "look-ahead" (how far ahead of current position sequences represent) is modulated by memory demands—greater look-ahead during working-memory-guided outbound navigation. This is linked to asymmetric spatial field properties rather than phase precession speed.

5. **Error analysis revealing sequence contributions**: Demonstrates that behavioral and theta sequences are preserved during error trials, but replay sequences are impaired before incorrect navigation. This dissociates the roles: replay primes the initial decision, while theta sequences maintain working memory during navigation.

### Brain regions & systems

- **Hippocampus (dorsal CA1)**: Contains place cells organized into behavioral sequences at the timescale of seconds and theta sequences at compressed timescales (100-200 ms). Exhibits theta cycle skipping in subsets of neurons. Theta sequences encode both actual and alternative choices before the decision point, supporting vicarious memory recall. Replay sequences during SWRs at reward wells reactivate past and future trajectories.

- **Prefrontal cortex (PFC)**: Contains neurons with trajectory-selective firing organized into behavioral sequences and, for the first time demonstrated here, theta sequences nested within behavioral sequences. PFC theta sequences preferentially encode the upcoming actual choice rather than alternatives, predicting decisions before the choice point. Shows coordinated theta sequence activity with hippocampus when representing actual choices.

- **Hippocampal-prefrontal circuit**: The two regions interact through theta-frequency synchrony and coherent spatial coding during memory-guided navigation. Coordinated theta sequences and replay sequences (SWR reactivation) support different phases of decision-making.

### Mechanistic insight

This paper provides mechanistic insight at the intersection of algorithmic and implementational levels:

**Computational**: The brain solves the problem of memory-guided decision-making by using internally generated sequences to simulate future scenarios. This is a hallmark of model-based computation, where the agent uses a learned model of the environment (spatial map) to evaluate potential future actions.

**Algorithmic**: The paper reveals a multi-timescale algorithm involving three distinct sequential mechanisms:
1. **Behavioral sequences** (seconds): Maintain current choice information through sequential activation of trajectory-selective neurons during navigation
2. **Theta sequences** (100-200 ms): Enable rapid vicarious memory recall—hippocampal sequences alternate between representing actual and alternative choices, while prefrontal sequences preferentially represent the selected choice
3. **Replay sequences** (SWRs, 100-200 ms): Prime upcoming decisions by reactivating future trajectories during inter-trial periods at reward wells

The algorithm involves coordination between hippocampus and PFC: when both regions show theta sequences simultaneously, their representations are coherent for actual choices but not for alternatives, suggesting PFC reads out hippocampal deliberation to select actions.

**Implementational**: The implementation relies on specific neural hardware properties:
- **Theta oscillations** (6-12 Hz) provide a temporal framework for organizing cell assemblies into sequences within single cycles
- **Theta cycle skipping**: Subsets of neurons fire on alternate theta cycles, potentially enabling segregation of different representations (actual vs. alternative) into different cycles
- **Asymmetric spatial fields**: Extended initial tails of place fields contribute to greater "look-ahead" during working memory navigation, with different asymmetry properties in outbound vs. inbound trajectories
- **Phase precession**: Individual neurons show theta phase precession to hippocampal theta, but this alone cannot account for the full extent of theta sequences
- **Sharp-wave ripples (SWRs)**: Brief high-frequency oscillations (150-250 Hz) during immobility provide windows for replay sequences that reactivate hippocampal-prefrontal ensembles

The paper thus meets the bar for mechanistic insight by providing both a formal algorithmic description (multi-timescale sequential computation) and linking it to specific neural implementations (theta oscillations, cycle skipping, SWRs, hippocampal-prefrontal coordination).

### Limitations & open questions

- The exact mechanism underlying hippocampal-prefrontal theta sequence coordination remains unclear; potential mediators include entorhinal cortex, nucleus reuniens, or other regions, but their specific roles need further investigation
- The network mechanisms that enable expression of sequences at distinct timescales (behavioral vs. theta vs. replay) in multiple circuits remain unknown
- The causal contribution of theta sequences versus behavioral sequences to decision-making was not directly tested through perturbation experiments
- Whether theta sequences in PFC are independent of hippocampal theta sequences or require hippocampal input was not determined
- The computational role of theta cycle skipping in segregating representations of alternatives requires further investigation
- The relationship between sequence degradation and memory impairment in this task needs direct causal testing

### Connections & keywords

- **Key citations**: Fuster (2015); Goldman-Rakic (1995); Miller et al. (2018); Johnson and Redish (2007); Kay et al. (2020); Shin et al. (2019); Jadhav et al. (2012); Fernández-Ruiz et al. (2019); Benchenane et al. (2010)
- **Named models or frameworks**: Bayesian decoding, dynamical systems, theta sequences, sharp-wave ripples (SWRs), replay sequences, cycle skipping, model-based reinforcement learning, working memory, vicarious trial and error
- **Brain regions**: hippocampus (dorsal CA1), prefrontal cortex (PFC), nucleus reuniens, entorhinal cortex
- **Keywords**: theta oscillations, theta sequences, prefrontal cortex, hippocampus, sharp-wave ripples, replay, decision-making, working memory, spatial navigation, ensemble dynamics, population coding, sequence coding, cycle skipping, vicarious memory recall, multi-timescale dynamics, Bayesian decoding, theta-phase precession, attractor dynamics, memory-guided behavior

### Related wiki pages
- [[wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning|Hippocampal sharp-wave ripple replay and prefrontal coordination during planning]]
- [[wiki/topics/sharp_wave_ripple_associated_hippocampal_replay|Sharp-wave ripple-associated hippocampal replay]]
