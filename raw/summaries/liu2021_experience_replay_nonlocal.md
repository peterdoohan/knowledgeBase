---
source_file: "liu2021_experience_replay_nonlocal.md"
paper_id: "liu2021_experience_replay_nonlocal"
title: "Experience replay is associated with efficient nonlocal learning"
authors: "Yunzhe Liu, Marcelo G. Mattar, Timothy E. J. Behrens, Nathaniel D. Daw, Raymond J. Dolan"
year: 2021
journal: "Science"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
methods: ["computational_modeling"]
brain_regions: ["hippocampus", "ventral_tegmental_area", "medial_temporal_lobe", "visual_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl", "temporal_difference_learning"]
keywords: ["mattar_and_daw_2018_nat_neurosci_normative_theory_of_prioritised_replay_need_gain_utility", "liu_et_al_2019_cell_prior_human_meg_replay_study_3050_ms_lag", "post_task_rest", "wimmer_et_al_2020_nat_neurosci_episodic_memory_replay_at_similar_160_ms_speed", "foster_and_wilson_2006_nature_reverse_replay_of_hippocampal_place_cells_in_rodents", "ambrose_et_al_2016_neuron_reverse_replay_modulated_by_changing_reward_in_rodents", "barron_et_al_2020_cell_inferential_reasoning_and_replay_in_humans_and_mice", "daw_et_al_2011_neuron_model_based_influences_on_striatal_prediction_errors_in_humans", "schuck_and_niv_2019_science_sequential_replay_of_nonspatial_task_states_in_human_hippocampus", "gomperts_et_al_2015_elife_vta_co_activation_during_hippocampal_swr", "liu_et_al_2022", "biorxiv_tdlm_method_for_measuring_sequences_in_meg", "named_models_or_frameworks", "temporally_delayed_linear_modelling_tdlm_meg_replay_detection_method", "modified_q_learning_model_with_separate_local_nonlocal_learning_rates_and_replay_regressor", "prioritised_memory_access_mattar_and_daw", "2018_normative_framework_for_replay_priority", "brain_regions", "hippocampus_medial_temporal_lobe", "visual_cortex"]
---

### One-line summary

Backward neural replay of nonlocal experiences at 160 ms state-to-state lag, measured via MEG in humans, directly supports model-based reinforcement learning by propagating reward credit to unchosen actions, and is prioritised according to the utility (need × gain) of those actions.

---

### Background & motivation

Adaptive decision-making often requires linking outcomes to actions that are separated in time and space — a problem known as nonlocal credit assignment. Reinforcement learning theory proposes that model-based inference, implemented neurally via hippocampal replay, can solve this by simulating counterfactual trajectories. While rodent studies have established that hippocampal replay is associated with learning, a direct causal link between sequential neural replay and nonlocal (model-based) reinforcement learning had not been demonstrated in humans. This paper fills that gap by providing simultaneous neural and behavioural evidence in a task that cleanly dissociates local from nonlocal learning.

---

### Methods

- **Subjects**: 29 healthy adults (mean age 23 years; 17 female) recorded with whole-brain MEG (275-channel axial gradiometer, 1200 Hz).
- **Task design**: A three-arm decision task in which each arm offered two paths (each a sequence of three visual stimuli) converging on one of two shared end states. This structure allowed reward feedback at an end state to update value for both the chosen (local) path and the two unchosen (nonlocal) paths leading to the same end state. Need was manipulated by varying arm encounter probability (17%, 33%, 50%); gain was created by drifting reward probabilities (Gaussian random walk, bounded 25–75%) for the two end states.
- **Neural decoding**: A functional localizer phase trained multivariate classifiers (whole-brain MEG sensor patterns at 200 ms post-onset) for all 18 path stimuli. Classifiers were blind to task structure and arm probabilities.
- **Replay detection**: Temporally Delayed Linear Modelling (TDLM) measured pairwise state-to-state sequential reactivation at all possible time lags during the reward-receipt window, yielding sequence strength for forward and backward directions.
- **Computational modelling**: Modified Q-learning models with separate learning rates for local and nonlocal paths, and extensions incorporating replay presence (binary) as a trial-by-trial regressor on learning rate, and priority (need, gain, need × gain) as modulators of differential nonlocal learning.

---

### Key findings

- **Behavioural nonlocal learning**: Subjects reliably updated choices at unchosen arms after reward at a shared end state (P = 9.5 × 10⁻²³), confirming model-based learning. Computational modelling showed similar learning rates for local (αd = 0.64) and nonlocal (αn = 0.60) paths; the difference was not significant (P = 0.61).
- **Two distinct replay types**: At reward receipt, forward replay peaked at 30-ms state-to-state lag and backward replay peaked at 160-ms lag; these were physiologically dissociable.
- **Representational content**: The 160-ms backward replay encoded nonlocal paths significantly (t(28) = 2.92, P = 0.007) and to a greater degree than the local path (t(28) = 2.21, P = 0.03). The 30-ms forward replay showed the opposite pattern — encoding local but not nonlocal experience.
- **Physiological distinction**: The 30-ms forward replay was associated with a ripple-frequency (80–180 Hz) power increase (t(28) = 3.98, P = 4.3 × 10⁻⁴); the 160-ms backward replay was not (P = 0.53). Exploratory beamforming suggested higher hippocampal and VTA activation for 30-ms replay; higher cortical engagement for 160-ms replay.
- **Replay linked to trial-by-trial learning**: Trials with significant 160-ms backward replay showed higher nonlocal learning rates (αreplay = 0.70) than trials without (αno-replay = 0.61; difference = 0.09, P = 0.023). The 30-ms replay was not linked to nonlocal learning (P = 0.457), and neither replay type predicted local learning.
- **Priority (utility) determines replay content**: 160-ms backward replay was stronger for the higher-utility (need × gain) nonlocal path versus the lower-utility one (t(28) = 3.30, P = 0.003). This prioritisation was absent for 30-ms replay (P = 0.74) and was not explained by path encounter frequency.
- **Between-subject correlation**: Stronger average 160-ms backward replay correlated with higher average reward earned per trial across subjects (robust r = 0.41, P = 0.03); 30-ms replay did not (r = –0.29, P = 0.13).
- **Gain but not need significant behaviourally**: For behavioural learning rate differences, higher-gain nonlocal paths showed significantly larger learning rates (P = 0.020), whereas higher-need paths did not reach significance (P = 0.16).

---

### Computational framework

**Reinforcement learning — model-based Q-learning with prioritised replay.**

The paper frames nonlocal value propagation as the credit assignment problem in RL: reward received at an end state must be assigned not only to the chosen path (local) but also to unchosen paths leading to the same end state (nonlocal). This is solved by model-based methods that use a learned transition map to simulate (or retrieve) counterfactual trajectories.

The normative theory of prioritised replay (Mattar & Daw, 2018) decomposes replay priority into two factors: *need* (probability of encountering the starting state in the future) and *gain* (expected improvement in reward from updating the action value). The product, *utility* (need × gain), determines which experiences should be replayed. The paper tests whether measured human replay tracks this normative priority.

Computationally, a modified Q-learning model assigns separate learning rates to local and nonlocal paths and includes a binary replay indicator per trial as a modulator of the nonlocal learning rate. Key variables: Q-values per path, per-trial binary replay indicator, separate learning rates αd (local), αn (nonlocal), αreplay, αno-replay, and priority-split learning rates for high vs. low need/gain/utility paths.

---

### Prevailing model of the system under study

The introduction positions this work against two background frameworks. First, in RL theory, model-based inference was recognised as a mechanism for nonlocal value propagation, but how the brain implements this in real time — and whether replay specifically mediates it — was unknown. Second, in systems neuroscience, hippocampal replay in rodents had been linked to learning in spatial tasks (via SWR disruption studies and co-occurrence analyses), and fast replay had been detected in humans during rest with MEG. However, the functional link between human sequential replay and trial-by-trial, nonlocal learning had not been established: replay was observed, but whether it actually caused or accompanied nonlocal credit assignment was an open question. The prevailing view was thus that replay likely serves memory consolidation and model-based planning, based largely on indirect evidence from rodents and correlation-level data in humans.

---

### What this paper contributes

The paper provides the first direct, trial-by-trial evidence in humans linking sequential neural replay to nonlocal (model-based) reinforcement learning:

1. It isolates two functionally and physiologically distinct replay types: a fast (30-ms) forward replay associated with ripple power and local path encoding; and a slow (160-ms) backward replay without ripple association that encodes nonlocal paths.
2. It shows that 160-ms backward replay tracks the normative utility (need × gain) priority predicted by Mattar & Daw (2018), with stronger replay for the more useful nonlocal path on each trial.
3. It demonstrates that the presence of 160-ms backward replay on a given trial predicts enhanced learning rates for the replayed nonlocal path on that trial, providing within-subject, trial-by-trial evidence for a functional role of replay in credit assignment.
4. It links individual differences in 160-ms replay strength to overall task performance (reward earned), establishing a between-subjects behavioural correlate.

Together, these findings support a specific, normative account of replay: it is not merely incidental reactivation but a prioritised process that solves credit assignment by backward propagation of reward to nonlocal actions.

---

### Brain regions & systems

- **Hippocampus / medial temporal lobe** — identified via beamforming source localisation as associated with both replay types; primary candidate for generating the sequential replay events. The 30-ms forward replay showed higher hippocampal activation relative to 160-ms backward replay.
- **Visual cortex** — activation present for both replay types, consistent with replay reactivating visual stimulus representations.
- **Ventral tegmental area (VTA)** — exploratory beamforming found higher VTA activation for 30-ms forward replay, consistent with prior reports that hippocampal SWR co-occur with dopaminergic midbrain activity (Gomperts et al., 2015).
- **Cortex (broadly)** — 160-ms backward replay displayed greater cortical engagement than the 30-ms forward replay, potentially reflecting a more distributed, consciously accessible computation.

Note: MEG source localisation is limited (standard caveats apply); all anatomical claims are exploratory.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Phenomenon**: The brain solves nonlocal credit assignment — assigning reward value to unchosen actions sharing an outcome — through backward sequential replay of nonlocal paths at the time of reward receipt.

**Marr's levels:**

- **Computational**: The problem is nonlocal credit assignment in a partially observable environment. The brain must propagate reward received at an end state backwards through unchosen action sequences, to update the Q-values of those paths. This is the core problem that model-based RL addresses; the normative solution is to replay the highest-utility experiences (Mattar & Daw, 2018).
- **Algorithmic**: The brain represents path states as distinct neural patterns (decodable from MEG). During reward receipt, these representations are reactivated sequentially in reverse order at a 160-ms state-to-state lag. The reverse order is mechanistically appropriate: it propagates reward backward along the path, from end state toward starting state, implementing backward temporal difference learning. The strength of replay on each trial predicts the magnitude of the nonlocal learning rate update (αreplay = 0.70 vs. αno-replay = 0.61). Replay prioritisation follows the utility metric (need × gain), not raw frequency of occurrence.
- **Implementational**: Exploratory beamforming suggests medial temporal lobe involvement. The 160-ms backward replay is physiologically distinct from the 30-ms forward replay: it lacks ripple-band (80–180 Hz) power increases and shows greater cortical engagement. This dissociation implies a different neural mechanism — possibly theta-cycle-based (~6 Hz) rather than sharp-wave ripple-based replay. Cell-type or circuit-level data are not available in this study (MEG does not afford that resolution).

**Bonus**: The paper explicitly notes the 30-ms forward replay co-occurs with ripple power increases and higher hippocampal/VTA activity, paralleling rodent SWR mechanisms; the 160-ms backward replay does not, suggesting a distinct circuit. This is a step toward identifying differential implementational substrates.

---

### Limitations & open questions

- **Causal direction**: The trial-by-trial correlation between replay and learning is correlational; replay and learning might both be driven by a third variable (e.g., prediction error magnitude or attentional engagement).
- **MEG source localisation**: Beamforming is acknowledged as exploratory; reliable anatomical assignment of replay sources is not possible with MEG.
- **Gain not independently manipulated**: Gain was derived from subjects' own reward history rather than being orthogonally controlled, though empirically need and gain were uncorrelated (r = –0.004, P = 0.61). Behavioural learning-rate differences for need did not reach significance (P = 0.16), leaving it unclear whether need independently modulates replay.
- **Mechanism of 160-ms replay**: The authors speculate this may reflect theta-sequence-like processing (~6 Hz state cycling), but the relationship to rodent theta sequences (which are forward and occur during ongoing behaviour) is not fully resolved.
- **Forward replay at choice time**: The paper reports no significant relationship between forward replay at choice time and credit assignment, but does not rule out a role for forward (planning) replay in different task contexts.
- **No sleep or offline replay**: The study focuses on awake, task-time replay; the interaction with sleep replay and long-term consolidation is not addressed.
- **Why backward?**: The backward direction is theoretically motivated for credit assignment, but the mechanism by which the brain generates reverse-order replay at reward receipt (rather than forward) is not explained.

---

### Connections & keywords

**Key citations:**
- Mattar & Daw (2018) — Nat. Neurosci. — normative theory of prioritised replay (need × gain = utility)
- Liu et al. (2019) — Cell — prior human MEG replay study (30–50 ms lag, post-task rest)
- Wimmer et al. (2020) — Nat. Neurosci. — episodic memory replay at similar 160-ms speed
- Foster & Wilson (2006) — Nature — reverse replay of hippocampal place cells in rodents
- Ambrose et al. (2016) — Neuron — reverse replay modulated by changing reward in rodents
- Barron et al. (2020) — Cell — inferential reasoning and replay in humans and mice
- Daw et al. (2011) — Neuron — model-based influences on striatal prediction errors in humans
- Schuck & Niv (2019) — Science — sequential replay of nonspatial task states in human hippocampus
- Gomperts et al. (2015) — eLife — VTA co-activation during hippocampal SWR
- Liu et al. (2022, bioRxiv) — TDLM method for measuring sequences in MEG

**Named models or frameworks:**
- Temporally Delayed Linear Modelling (TDLM) — MEG replay detection method
- Modified Q-learning model — with separate local/nonlocal learning rates and replay regressor
- Prioritised memory access (Mattar & Daw, 2018) — normative framework for replay priority

**Brain regions:**
- Hippocampus / medial temporal lobe
- Visual cortex
- Ventral tegmental area (VTA)

**Keywords:**
- experience replay, nonlocal learning, model-based reinforcement learning, credit assignment, backward replay, hippocampal replay, MEG decoding, prioritised replay, need-gain utility, Q-learning, sequential reactivation, temporal difference learning
