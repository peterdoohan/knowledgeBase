---
source_file: singer2009_reward_reactivation_hippocampus.md
paper_id: singer2009_reward_reactivation_hippocampus
title: "Rewarded Outcomes Enhance Reactivation of Experience in the Hippocampus"
authors:
  - "Annabelle C. Singer"
  - "Loren M. Frank"
year: 2009
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - tetrode_recording
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - prefrontal_cortex
  - striatum
  - ventral_striatum
frameworks:
  - reinforcement_learning
  - attractor_networks
keywords:
  - hippocampus
  - sharp_wave_ripples
  - swr
  - replay
  - reactivation
  - reward
  - place_cells
  - ca3
  - memory_consolidation
  - spatial_navigation
  - sequence_learning
  - awake_replay
  - neural_oscillations
  - credit_assignment
  - reinforcement_learning
  - rewarded
  - outcomes
  - enhance
  - experience
---

### One-line summary

Reward enhances sharp wave ripple (SWR) reactivation of hippocampal place cells, suggesting a mechanism to bind rewarding outcomes to the experiences that precede them.

### Background & motivation

Remembering experiences that lead to reward is essential for survival, yet the mechanisms that associate specific experiences with rewarding outcomes remain poorly understood. The hippocampus is required for forming and storing memories of events and places, and memory storage is thought to depend on reactivation of previous experiences during hippocampal sharp wave ripples (SWRs). This study investigates whether reward modulates SWR reactivation to bind outcomes to preceding experiences.

### Methods

- **Task**: Sequence switching task on a 6-arm maze where rats learned to switch between two spatial sequences (S1 and S2) based on changing reward contingencies
- **Subjects**: 3 male Long-Evans rats, food deprived to 85-90% baseline weight
- **Recordings**: Single-unit recordings from hippocampal CA3 principal neurons (n = 270 cells) using independently movable tetrode arrays
- **SWR detection**: LFP filtered 150-250 Hz, envelope via Hilbert transform, threshold at mean + 3 SD for at least 15 ms
- **Place field identification**: Occupancy-normalized firing rate maps, cells with mean rate > 0.1 Hz and peak spatial rate > 3 Hz
- **Analysis**: Compared SWR activity at the well (wSWRs) between rewarded and unrewarded trials; examined reactivation of place cells during SWRs; analyzed coactivation of cell pairs and sequence replay

### Key findings

- **Enhanced SWR activity after reward**: CA3 principal cells were significantly more active during wSWRs following reward compared to unrewarded trials (p < 10^-10)
- **Higher wSWR rate**: More wSWRs per unit time on rewarded trials (p < 10^-10)
- **Increased activation probability per wSWR**: Place cells were more likely to be active in any given wSWR on rewarded trials (p < 10^-10)
- **Effects persist with time control**: Differences remained significant when rewarded trial duration was truncated to match unrewarded trials
- **Learning enhances reactivation further**: wSWR rate, activation probability, and proportion of cells active per wSWR were higher when learning new reward associations (first day of S2) compared to familiar sequences (S1 or day 3 of S2)
- **Structured reactivation**: SWR activity reactivated coherent elements of paths associated with reward locations; cells with place fields on the track were much more likely to be reactivated than cells without place fields
- **Coactivation of cell pairs**: Pairs of place cells were more than twice as likely to fire together during wSWRs on rewarded than unrewarded trials (p < 10^-10)
- **Ordered replay**: Intercell interspike intervals during wSWRs were significantly related to distance between place field peaks, consistent with ordered replay (R^2 = 0.0913, p < 10^-10)
- **Reverse replay predominance**: In 68.1% of cases where two cells were active in a wSWR, the order was opposite to that seen during the run
- **Reward history effects**: SWR activity was higher on unexpectedly rewarded trials than unrewarded trials, indicating the presence of reward rather than reward expectation drives enhanced reactivation

### Computational framework

Not applicable. This is an empirical study recording neural activity in behaving animals. However, the findings constrain models of hippocampal function and memory consolidation. The results suggest that reward acts as a modulatory signal that gates or amplifies hippocampal reactivation, consistent with reinforcement learning frameworks where outcomes strengthen associations between states and actions. The observation of ordered replay is consistent with dynamical systems models of sequence reactivation in recurrent networks.

### Prevailing model of the system under study

Prior to this study, the prevailing model held that hippocampal reactivation during SWRs merely reflects recent activity within the hippocampal network—a simple Hebbian trace of what was recently experienced. Reactivation during sleep was known to reflect the structure of previous awake experience, and the amount that cells fire together during SWRs depends on their prior co-activation. Studies showed that repeated traversals of the same path lead to increases in SWR rate and reactivation in familiar environments. The introduction notes that while reward was known to modulate place field firing rates and locations, it was unclear how this would help animals learn to navigate from distant locations to rewards.

### What this paper contributes

This paper demonstrates that the simple "reactivation reflects recent activity" model is insufficient. The key contributions are:

1. **Reward modulates reactivation independently of recent activity**: SWR reactivation increases following reward even when there is no increase in activity during the preceding run period. This shows that reactivation is not simply a reflection of recent activity but is gated by behavioral outcomes.

2. **Outcome-specific enhancement**: Enhanced reactivation is specific to cells with place fields on the paths associated with the reward location, and these cells show increased coactivation during SWRs following reward. This demonstrates that reward enhances the reactivation of specific, relevant experiences rather than indiscriminately boosting all recent activity.

3. **Learning-dependent amplification**: The effect is further enhanced when animals must learn new path-reward associations, suggesting that reward-enhanced reactivation contributes to learning.

4. **Mechanistic insight**: The findings support a model where the spatial sequence an animal traverses determines which cells will be active during SWRs, while the presence or absence of reward modulates the amount and strength of reactivation. This provides a mechanism for binding rewarding outcomes to the experiences that precede them.

### Brain regions & systems

- **Hippocampus CA3**: Primary recording site; principal neurons showed enhanced SWR reactivation following reward. CA3 is the origin of SWR events and shows sparse, structured reactivation during SWRs.
- **Hippocampus CA1**: Mentioned as downstream target of CA3 SWRs; SWRs detected in CA3 propagate to CA1. Not directly recorded in this study but discussed in relation to previous replay studies.
- **Corpus callosum**: Reference electrode location.
- **Ventral striatum**: Mentioned as receiving coherent reactivation from hippocampus during SWRs (cited from other studies).
- **Prefrontal cortex**: Mentioned as showing coherent activity with hippocampus during SWRs (cited from other studies).

### Mechanistic insight

This paper provides strong mechanistic insight that maps onto Marr's three levels:

**Computational level**: The brain must solve the problem of associating specific experiences (spatial trajectories) with their outcomes (reward) to guide future behavior. This is essentially a credit assignment problem in reinforcement learning—determining which actions led to positive outcomes.

**Algorithmic level**: The paper proposes that SWR reactivation serves as the algorithmic mechanism for this association. After an animal completes a trajectory and receives an outcome, SWRs reactivate the cells that were active during that trajectory. The key finding is that reward modulates this reactivation: on rewarded trials, CA3 cells with place fields on the trajectory show (1) higher SWR rates, (2) higher per-SWR activation probability, (3) increased coactivation of cell pairs, and (4) structured sequential replay consistent with the spatial trajectory. This provides an algorithmic mechanism where reward acts as a gain control on hippocampal reactivation, strengthening the memory trace specifically for rewarded experiences.

**Implementational level**: The implementation involves specific neural hardware in hippocampal area CA3. SWRs are high-frequency network oscillations (150-250 Hz) that originate in CA3 and propagate to CA1 and other regions. The paper demonstrates that CA3 principal neurons (pyramidal cells) show sparse, structured reactivation during these events. The findings suggest that reward-related signals from other brain regions (potentially dopaminergic or other neuromodulatory inputs) modulate CA3 network dynamics during SWRs, amplifying reactivation of recently active cell assemblies. The specific biophysical mechanisms (e.g., which neuromodulators, receptor types, or synaptic plasticity rules) are not identified in this study, but the paper establishes the network-level phenomenon that future work must explain mechanistically.

### Limitations & open questions

- **Neuromodulatory mechanisms**: The study does not identify the specific neuromodulatory signals (e.g., dopamine, acetylcholine) that mediate reward-enhanced reactivation. The source of reward-related modulation remains unknown.
- **SWR criteria controversy**: The authors acknowledge controversy over SWR detection criteria in CA3, including potential differences from CA1 SWRs and possible contamination from gamma oscillations or reference electrode artifacts. They address this with cross-validation but note limitations.
- **Recording duration**: The study did not maximize the number of simultaneously recorded cells on a single day, instead prioritizing recording across many days. This limits the ability to analyze larger cell assemblies.
- **Causal manipulation**: The study is correlational; it does not demonstrate that enhanced SWR reactivation is necessary or sufficient for learning. Direct manipulation of SWR activity during reward would be needed to establish causality.
- **Generalization to other tasks**: The findings are from a specific sequence-switching task. Whether reward enhances reactivation similarly in other behavioral contexts (e.g., single-path tasks, non-spatial tasks) remains to be determined.
- **Timescale of plasticity**: The study does not directly address what synaptic plasticity mechanisms operate during reward-enhanced reactivation or how long-lasting the effects are.

### Connections & keywords

**Key citations:**
- Foster and Wilson (2006) — reverse replay in hippocampal place cells
- Diba and Buzsaki (2007) — forward and reverse replay sequences
- Karlsson and Frank (2009) — awake replay of remote experiences
- Csicsvari et al. (2000) — CA3 origin of SWRs
- Wilson and McNaughton (1994) — memory reactivation during sleep
- Cheng and Frank (2008) — coordinated neural activity in novel environments

**Named models or frameworks:**
- Sharp wave ripples (SWRs) as memory reactivation mechanism
- Hippocampal replay/reactivation
- Attractor network dynamics (referenced in discussion)
- Reinforcement learning (credit assignment problem)

**Brain regions:**
- Hippocampus CA3 (primary recording site)
- Hippocampus CA1 (downstream target)
- Corpus callosum (reference electrode)
- Ventral striatum (coherent reactivation)
- Prefrontal cortex (coherent activity)

**Keywords:**
hippocampus, sharp wave ripples, SWR, replay, reactivation, reward, place cells, CA3, memory consolidation, spatial navigation, sequence learning, awake replay, neural oscillations, credit assignment, reinforcement learning
