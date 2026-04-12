---
source_file: gillespie2021_replay_past_experiences.md
paper_id: gillespie2021_replay_past_experiences
title: "Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice"
authors:
  - "Anna K. Gillespie"
  - "Daniela A. Astudillo Maya"
  - "Eric L. Denovellis"
  - "Daniel F. Liu"
  - "David B. Kastner"
  - "Michael E. Coulter"
  - "Demetris K. Roumis"
  - "Uri T. Eden"
  - "Loren M. Frank"
year: 2021
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
  - prefrontal_cortex
  - striatum
  - ventral_striatum
  - nucleus_accumbens
  - ventral_tegmental_area
frameworks:
  - reinforcement_learning
keywords:
  - hippocampal_replay
  - sharp_wave_ripples_swrs
  - memory_storage_vs_planning
  - place_cells
  - spatial_memory
  - clusterless_decoding
  - reward_history
  - recency_suppression
  - awake_replay
  - memory_consolidation
  - deliberation
  - win_stay_lose_switch_task
  - hippocampal
  - replay
  - reflects
  - specific
  - past
  - experiences
  - rather
  - than
key_citations:
  - igata2021_prioritized_experience_replays
  - shin2019_hippocampal_prefrontal_replay_b
  - gupta2010_replay_not_simple_function
wiki_pages:
  - wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning
  - wiki/topics/sharp_wave_ripple_associated_hippocampal_replay
---

### One-line summary

Awake hippocampal replay during a dynamic spatial memory task is decoupled from subsequent behavioral choice, instead preferentially representing previously rewarded locations and non-recently visited places, supporting a memory storage rather than planning role.

---

### Background & motivation

Hippocampal replay — the time-compressed reactivation of place cell sequences during sharp-wave ripples (SWRs) — has been proposed to serve two distinct roles: storing past experiences (memory consolidation/maintenance) or guiding upcoming behavior (planning/deliberation). Prior studies were limited by simple, repetitive tasks that could not dissociate replay of recently rewarded locations from replay of possible future options. No previous study had systematically related replay content to behavior on a trial-by-trial basis in a task with dynamic, changing goal locations and a wide range of spatial options. This paper addresses this gap by deploying a dynamic win-stay/lose-switch task in rats with real-time, trial-resolved clusterless decoding of hippocampal ensemble activity.

---

### Methods

- **Subjects**: 4 adult male Long-Evans rats, well-trained on a novel task prior to recording.
- **Task**: An eight-arm radial maze with dynamic goal locations (win-stay, lose-switch). Each trial consisted of home port trigger → random center port delay (2–20 s) → arm choice → home port return. The goal arm changed after 4–15 rewards, requiring flexible spatial memory. Trials were classified as search phase (goal unknown) or repeat phase (goal known).
- **Neural recordings**: Bilateral 30-tetrode microdrive arrays targeting dorsal CA1; 24–33 sessions per subject.
- **SWR detection**: Permissive LFP-based threshold; verified against multiunit activity-based detection.
- **Spatial decoding**: Clusterless state-space decoding algorithm (Denovellis et al.) using a marked point process encoding model and a 2 ms time bin; linearized maze into 9 segments. Replay events classified as local (same maze segment as animal) or remote (different segment).
- **Analysis**: Replay content categorized per trial into four arm categories: past (just visited), future (about to be visited), current goal, and previous goal (prior trial block's reward location). Poisson GLMs estimated fold-change in replay rate per category. Binomial GLMs assessed whether replay content predicted correct vs. error trial outcome (cross-validated).

---

### Key findings

- **Remote replay was common**: 34–47% of spatially continuous SWRs represented remote locations, consistent with prior reports.
- **Replay was not enriched for the upcoming arm**: Only 2 of 4 subjects showed small, inconsistent enrichment for the future arm during search trials; no consistent enrichment during repeat trials.
- **Replay was strongly enriched for the previous goal arm**: ~20% of all pre-choice remote replay events during search trials represented the previous goal arm (the reward location from the prior trial block), despite it no longer being visited or rewarded. GLMs confirmed ~2-fold increase in replay rate for previous-goal arm category.
- **The immediate past arm was suppressed in replay**: Replay of the arm just visited occurred significantly below chance levels.
- **Replay of the current goal increased with reward experience**: Enrichment for the current goal arm emerged only in the late repeat phase (≥5 rewards received), likely explaining prior reports of future-trajectory replay in well-learned tasks.
- **Previous goal replay persisted for multiple trial blocks**: Elevated replay of a decommissioned goal arm continued for at least two full subsequent trial blocks, well after the animal's behavioral bias to that arm had returned to baseline within a few trials.
- **No trial-by-trial relationship between replay and choice**: Correct and error repeat trials showed no consistent difference in future arm or current goal replay rate. In fact, error trials showed higher overall remote replay rate. GLM classifiers predicting correct vs. error trials from replay content performed at or near chance.
- **Previous goal replay did not deter or encourage visits**: No correlation between previous-goal replay rate and subsequent visits to that arm.
- **Replay biased toward non-recently visited arms**: Among non-rewarded arms, replay rate was higher for arms not visited in the past 5 trials; visit recency was negatively correlated with replay rate.

---

### Computational framework

The paper does not develop or fit a formal computational model. It is primarily a neural recording and decoding study. However, it explicitly engages with two competing computational hypotheses for replay:

1. **Planning / deliberation hypothesis**: Replay implements a search through possible future trajectories, allowing an evaluative process to select the best action. Predicts replay content should predict upcoming choice.
2. **Memory storage / maintenance hypothesis**: Replay stabilises and consolidates representations of past experiences, biased toward salient and temporally remote events. Does not predict trial-by-trial correspondence with upcoming behaviour.

The paper's findings are inconsistent with the planning hypothesis and strongly support the storage hypothesis. The authors propose that replay strengthens distributed hippocampal-cortical representations of specific experiences (by stabilising local ensemble connectivity and facilitating plasticity in downstream networks), while planning may be implemented by a separate mechanism such as theta sequences.

The **Mattar & Daw (2018)** prioritised replay model (reinforcement learning / value update account) is also discussed; the authors argue their data are inconsistent with replay directly updating behavioural values on a trial-by-trial basis.

---

### Prevailing model of the system under study

Prior to this paper, the field held two competing views of awake hippocampal replay. The **planning hypothesis** — supported by studies showing increased replay of the about-to-be-chosen trajectory (Pfeiffer & Foster, 2013; Xu et al., 2019) and SWR disruption impairing learning (Jadhav et al., 2012) — held that pre-choice replay evaluates candidate future trajectories to inform behavioural decisions. The **storage hypothesis** — consistent with observations of replay of remote, unavailable, or inaccessible locations — held that replay serves to consolidate and maintain representations of past experience regardless of immediate behavioural relevance. Studies supporting planning typically used simple, well-learned tasks with few fixed reward locations, where future and past options were confounded with reward history, making it impossible to definitively attribute planning-related replay to deliberation rather than reward-biased storage.

---

### What this paper contributes

The paper provides the most direct test to date of the planning hypothesis under conditions designed to maximise its detectability (defined pre-choice period, dynamic goals, eight possible trajectories, trial-by-trial resolution). The key contribution is a definitive dissociation between replay content and upcoming behaviour: replay was not systematically enriched for the chosen arm, did not differ between correct and error trials, and did not predict choice even when tested with cross-validated classifiers.

The paper additionally identifies two specific principles governing what gets replayed: (1) reward history (previous goal status), with enrichment emerging gradually over multiple rewards and persisting long after goal change; and (2) recency suppression, with the most recently visited arm being actively under-represented. These two factors together provide a unified explanatory framework for the majority of prior replay findings, including apparent planning-related replay: previous reports of future-trajectory enrichment likely reflect reward-history bias at familiar, repeatedly rewarded locations rather than prospective deliberation.

The paper cannot rule out indirect or delayed influences of replay on behavior, and proposes that the behaviorally relevant planning signal may instead reside in theta sequences outside of SWRs.

---

### Brain regions & systems

- **Dorsal CA1** — primary recording site; hippocampal place cells and SWRs recorded here form the empirical basis of all findings. Replay events decoded from CA1 ensemble activity.
- **Hippocampus (general)** — the system under study; discussed as the locus of spatial map formation, memory storage, and the site of sharp-wave ripples mediating consolidation.
- **Prefrontal cortex (PFC)** — discussed in relation to Shin et al. (2019), which reported enhanced hippocampal-PFC coordination during replay of the upcoming trajectory; the current paper contextualises this as potentially reflecting task engagement rather than direct behavioural guidance.
- **Nucleus accumbens / ventral striatum / VTA** — mentioned in discussion as downstream regions that engage with replay of rewarded locations (Gomperts et al., 2015; Sosa et al., 2020), relevant to the role of replay in reinforcing reward associations.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight at the computational and algorithmic levels, but not at the implementational level.

- **Computational**: The brain is solving a memory maintenance problem — preserving accurate representations of locations and experiences to prevent forgetting and interference, prioritising salient (previously rewarded) and temporally remote experiences over recent ones.
- **Algorithmic**: Replay (SWR-associated ensemble reactivation) implements this storage function by selectively reactivating representations of previous goal locations and non-recently visited arms. The algorithm is not prospective planning but retrospective, experience-biased reactivation. Neural evidence (CA1 tetrode recordings across 4 rats, clusterless decoding, GLM analysis) directly demonstrates that replay content tracks reward history and recency rather than upcoming choice, and that this content is decoupled from trial-by-trial behaviour.
- **Implementational**: The paper does not address specific cell types, synaptic mechanisms, or neuromodulators. The authors cite other work (Roux et al., 2017) for the hypothesis that SWRs stabilise local ensemble connectivity, but this is not tested here.

**Bonus**: The paper does note that replay at outer arm ports also shows enhanced previous-goal arm representation, suggesting the storage-biased content is not specific to the pre-choice period.

---

### Limitations & open questions

- The study used only 4 rats; while results were consistent across subjects and sessions, the sample size is small.
- The task is well-learned prior to recording, so findings apply to the maintenance/performance phase; acquisition-phase replay (when SWR disruption impairs learning) may serve different functions.
- Forward vs. reverse directionality of replay was not analysed, leaving open whether directional content relates differentially to past or future trajectories.
- The study cannot rule out that some small subset of planning-related replay exists but is swamped by the dominant storage signal; the proposed deliberation-via-theta-sequences mechanism remains speculative.
- The paper does not assess sleep replay in the same animals/task, so a direct comparison of wake and sleep replay content relative to behaviour is absent.
- Mechanisms by which reward history and recency modulate replay probability are not addressed.
- How stored representations ultimately influence future planning (e.g., via theta sequences) remains an open question.

---

### Connections & keywords

**Key citations**:
- Pfeiffer & Foster (2013) — Hippocampal place-cell sequences depict future paths to remembered goals. *Nature*.
- Jadhav et al. (2012) — Awake hippocampal sharp-wave ripples support spatial memory. *Science*.
- Karlsson & Frank (2009) — Awake replay of remote experiences in the hippocampus. *Nat. Neurosci.*
- Mattar & Daw (2018) — Prioritized memory access explains planning and hippocampal replay. *Nat. Neurosci.*
- Carey et al. (2019) — Reward revaluation biases hippocampal replay content away from the preferred outcome. *Nat. Neurosci.*
- Igata et al. (2021) — Prioritized experience replays on a hippocampal predictive map for learning. *PNAS*.
- Shin et al. (2019) — Dynamics of awake hippocampal-prefrontal replay for spatial learning and memory-guided decision making. *Neuron*.
- Denovellis et al. (2020) — Hippocampal replay of experience at real-world speeds. *bioRxiv*.
- Roux et al. (2017) — Sharp wave ripples during learning stabilize the hippocampal spatial map. *Nat. Neurosci.*
- Gupta et al. (2010) — Hippocampal replay is not a simple function of experience. *Neuron*.

**Named models or frameworks**:
- Planning hypothesis (deliberation via replay)
- Memory storage/maintenance hypothesis
- Mattar & Daw prioritised replay model (RL-based)
- Clusterless state-space decoding (Denovellis et al.)
- Win-stay, lose-switch task (eight-arm spatial variant)
- Theta sequences (proposed alternative planning mechanism)

**Brain regions**:
- Dorsal CA1
- Hippocampus
- Prefrontal cortex
- Nucleus accumbens / ventral tegmental area (discussed)

**Keywords**:
- hippocampal replay
- sharp-wave ripples (SWRs)
- memory storage vs. planning
- place cells
- spatial memory
- clusterless decoding
- reward history
- recency suppression
- awake replay
- memory consolidation
- deliberation
- win-stay lose-switch task

### Related wiki pages
- [[wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning|Goal-directed vs habitual control in corticostriatal reinforcement learning]]
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
- [[wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning|Hippocampal sharp-wave ripple replay and prefrontal coordination during planning]]
- [[wiki/topics/sharp_wave_ripple_associated_hippocampal_replay|Sharp-wave ripple-associated hippocampal replay]]
