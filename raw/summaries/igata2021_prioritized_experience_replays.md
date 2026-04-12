---
source_file: igata2021_prioritized_experience_replays.md
paper_id: igata2021_prioritized_experience_replays
title: "Prioritized experience replays on a hippocampal predictive map for learning"
authors:
  - "Hideyoshi Igata"
  - "Yuji Ikegaya"
  - "Takuya Sasaki"
year: 2021
journal: "PNAS (Proceedings of the National Academy of Sciences)"
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - navigation_task
methods:
  - tetrode_recording
  - bayesian_decoding
brain_regions:
  - hippocampus_ca1
frameworks:
  - reinforcement_learning
keywords:
  - prioritized_experience_replay
  - sharp_wave_ripples
  - place_cells
  - hippocampal_replay
  - spatial_learning
  - predictive_map
  - theta_sequences
  - forward_replay
  - reverse_replay
  - bayesian_decoding
  - closed_loop_swr_disruption
  - reinforcement_learning
  - prioritized
  - experience
  - replays
  - hippocampal
  - predictive
  - map
  - learning
key_citations:
  - stachenfeld2017_hippocampus_predictive_map
wiki_pages:
  - wiki/topics/sharp_wave_ripple_associated_hippocampal_replay
---

### One-line summary

During spatial learning in rats, hippocampal place cells generate prioritized experience replays that preferentially represent novel, reward-related, and future-efficient trajectories — including paths never yet taken — and these replays are causally required to stabilise the learned behaviour.

---

### Background & motivation

Hippocampal place cells are known to replay past trajectories during sharp-wave ripples (SWRs), and these replays are thought to support reinforcement learning by helping to assign value to spatial experiences. However, it remained unclear how the content and directionality of replays dynamically change as animals actively update their behavioural strategies in response to environmental change. A key theoretical idea — "prioritized experience replay" from machine learning — proposes that selectively rehearsing high-value or surprising experiences improves learning efficiency; whether biological hippocampal circuits implement an analogous mechanism had not been directly demonstrated. This study fills that gap by combining within-session learning, multi-tetrode CA1 recording, Bayesian decoding of replay content, and closed-loop SWR disruption.

---

### Methods

- **Species and task**: 17 male Long Evans rats performed a two-checkpoint spatial navigation task in which the rewarded checkpoint was relocated mid-session, requiring new trajectory learning within a single recording session (~2 h).
- **Neural recordings**: 355 CA1 neurons recorded with 16 independently movable tetrodes from 5 rats during the full pre-learning, learning, and post-learning phases.
- **Replay analysis**: Bayesian decoding of population activity during SWR-associated synchronous events to estimate which path segment was replayed; weighted correlation (r) and sequence score (rZ) computed to classify forward vs. reverse replay events; representation rates (reprates) computed for each path.
- **Theta-sequence analysis**: Quadrant scores computed across learning phases to quantify within-theta-cycle sequential organisation.
- **Causal manipulation**: Closed-loop real-time electrical stimulation of the ventral hippocampal commissure (vHC) upon online SWR detection (140–180 µA, 100 µs pulse) to disrupt SWRs during the learning phase; delayed (250 ms) and non-learning controls included.
- **Statistical approach**: Hierarchical Bayesian modelling with Markov chain Monte Carlo (MCMC) to account for differences in trial and event counts across individual animals.

---

### Key findings

- Hippocampal cells showed two major firing types: spatially stable place fields (~47%) and context-dependent fields that generalised across equivalent behavioural steps toward checkpoints (~49%).
- During the learning phase, theta-sequence strength (quadrant scores) increased significantly not only on novel paths but also on previously learned and familiar paths, suggesting broad circuit plasticity signals.
- SWR-associated synchronous event frequencies increased significantly in the open field and goal area during learning; on the following day, after learning was complete, event rates returned to pre-learning baseline.
- Replay content shifted dynamically with learning: during the final third of the learning phase — before rats had physically adopted the optimal path S-C2 — the largest fraction of synchronous events already represented path S-C2, the future-efficient trajectory.
- The lag between onset of S-C2 replay dominance and the behavioural learning point was 16.4 ± 19.5 trials, indicating that replay changes preceded behavioural changes.
- Novel reward-associated paths (G-C2, S-C2) were replayed more frequently than a familiar high-reward path (C2-G, 200 µL reward), suggesting that novelty of the reward-related action policy, rather than reward magnitude, determines replay priority.
- During the learning phase, reverse replays increased significantly in the open field, particularly for path G-C2; the directionality then shifted as the postlearning phase was established.
- Online SWR disruption (real-time closed-loop stimulation) resulted in unstable trajectories across trials and significantly increased the probability of behavioural reversals after rats first adopted the optimal path, without affecting the number of trials to initially discover path S-C2. Delayed-control and non-learning-control stimulation had no such effect.

---

### Computational framework

The paper is framed within **reinforcement learning** and specifically the concept of **prioritized experience replay** (Schaul et al., 2015; Mattar & Daw, 2018). The key question is whether biological hippocampal circuits implement an analogue of the prioritized memory access algorithm used in deep RL.

The implicit formal structure: the hippocampus maintains a predictive map of task states (following Stachenfeld et al., 2017); SWR-associated replays implement something like memory sampling for value updating; the priority of which episodes get replayed is weighted by novelty and prediction error (rather than random or recency-based access). The paper does not formalise a full computational model but grounds each empirical observation in this RL framework, using the observation of predictive (future-path) replays to argue for a model-based planning account.

---

### Prevailing model of the system under study

The baseline understanding the paper works within holds that hippocampal place cells form a cognitive map of space (O'Keefe & Nadel, 1978) that has more recently been extended to a predictive map encoding expected future states (Stachenfeld et al., 2017). SWR-associated replay events are understood to represent recently experienced trajectories and are thought to promote learning and synaptic plasticity. Prior empirical work had shown that reward increases replay rates, that reverse replays follow novel reward encounters, and that SWR disruption impairs spatial memory consolidation. However, the prevailing view had not established that replay content is dynamically prioritised in a task-state-value-dependent manner within a single learning episode, nor that replays can anticipate behavioural strategies not yet physically executed.

---

### What this paper contributes

This paper provides direct evidence that hippocampal replay implements a biologically instantiated version of prioritized experience replay: the hippocampus selectively amplifies representations of novel, reward-relevant, and prospectively valuable experiences rather than simply replaying recent or high-reward experiences uniformly. Crucially, replays of the optimal path (S-C2) emerged before that path was behaviourally adopted, demonstrating that internal simulation — not just experience replay — contributes to hippocampal replay content. The causal SWR disruption experiment moves beyond correlation to show that learning-phase replays are necessary specifically for behavioural stabilisation after discovery of the optimal trajectory (rather than for initial discovery). Together, this establishes that the hippocampal predictive map is dynamically reorganised by learning-related replay that anticipates, rather than merely records, efficient future strategies.

---

### Brain regions & systems

- **Hippocampal CA1** — primary recording site; locus of place cell and context-dependent firing, SWR-associated synchronous events, and sequential replay events that encode and prioritise reward-related trajectories.
- **Ventral hippocampal commissure (vHC)** — stimulation target for closed-loop SWR disruption; used to test causal role of SWRs in learning stabilisation.

---

### Mechanistic insight

The paper meets both criteria for this section. It presents a specific algorithm (prioritized experience replay, weighted by novelty/prediction error) and provides neural data (multi-tetrode CA1 recordings + Bayesian decoding + causal SWR disruption) that link that algorithm to measured hippocampal activity.

- **Computational**: The brain solves the temporal credit assignment problem during spatial learning — it must assign value to earlier states in a trajectory given delayed reward. Prioritised replay of novel reward-related episodes (over familiar high-reward episodes) is the proposed solution, enabling efficient policy updating.
- **Algorithmic**: Hippocampal CA1 cell ensembles — combining stable place cells and context-dependent cells — are recruited into SWR-associated synchronous events in a priority order determined by novelty and prediction error. Replay content tracks the animal's internal model of valuable trajectories, including paths not yet physically taken. Theta-sequences encode prospective/retrospective positions within-trial; SWR replays encode multi-step trajectories offline (at rest/stops). The directionality of replay (forward vs. reverse) changes systematically across learning phases.
- **Implementational**: SWR-associated population synchrony is the neural vehicle for replay. The paper does not identify specific cell types, neuromodulators, or synaptic mechanisms beyond referencing that cholinergic signals likely drive theta-sequence increases and that dopaminergic signals during reward interact with Hebbian plasticity. Causal evidence is at the circuit level (SWR disruption via vHC stimulation).

---

### Limitations & open questions

- Small sample (n = 5 rats for recording; n = 12 for stimulation experiments); results flagged as potentially driven by Rat 1 (largest cell count), though key findings survived that animal's exclusion.
- The study does not identify the mechanism by which the hippocampus selects which episodes to prioritise — i.e., how prediction error signals reach CA1 to modulate replay content.
- It remains unclear whether the prospective replays of path S-C2 are truly "planning" (internal simulation from stored map) or arise from partial physical experience with segments of that path.
- The paper does not address how replay priority is computed or where the "salience signal" originates (e.g., from VTA dopamine, from prefrontal inputs, or from within the hippocampal-entorhinal circuit).
- The generalization to non-spatial or abstract domains is discussed speculatively; the paper does not test whether these replay dynamics extend beyond spatial navigation.
- SWR disruption affected behavioural stabilisation but not the number of trials to first discover the optimal path, leaving open what process supports initial discovery.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — hippocampus as cognitive map
- Stachenfeld, Botvinick & Gershman (2017) — hippocampus as predictive map
- Mattar & Daw (2018) — prioritized memory access explains planning and hippocampal replay
- Schaul et al. (2015) — prioritized experience replay in deep RL
- Foster & Wilson (2006) — reverse replay in awake hippocampus
- Pfeiffer & Foster (2013) — hippocampal place-cell sequences depict future paths
- Jadhav et al. (2012) — awake SWRs support spatial memory
- Roux et al. (2017) — SWRs during learning stabilise hippocampal spatial map
- Aronov, Nevers & Tank (2017) — hippocampal-entorhinal mapping of non-spatial dimensions
- Buzsáki (2015) — hippocampal sharp wave-ripple as cognitive biomarker

**Named models or frameworks**:
- Prioritized experience replay (PER)
- Hippocampal predictive map
- Cognitive map (O'Keefe & Nadel)
- Temporal difference reinforcement learning (TD-RL)

**Brain regions**:
- Hippocampal CA1
- Ventral hippocampal commissure (vHC)

**Keywords**: prioritized experience replay, sharp-wave ripples, place cells, hippocampal replay, spatial learning, predictive map, theta-sequences, forward replay, reverse replay, Bayesian decoding, closed-loop SWR disruption, reinforcement learning

### Related wiki pages
- [[wiki/topics/sharp_wave_ripple_associated_hippocampal_replay|Sharp-wave ripple-associated hippocampal replay]]
