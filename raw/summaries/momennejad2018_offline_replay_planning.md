---
source_file: "momennejad2018_offline_replay_planning.md"
paper_id: "momennejad2018_offline_replay_planning"
title: "Offline replay supports planning in human reinforcement learning"
authors: "Ida Momennejad, A Ross Otto, Nathaniel D Daw, Kenneth A Norman"
year: 2018
journal: "eLife"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
methods: ["fmri", "behavioral_analysis"]
brain_regions: ["hippocampus", "prefrontal_cortex", "anterior_cingulate_cortex", "ventromedial_prefrontal_cortex", "striatum", "medial_temporal_lobe"]
frameworks: ["reinforcement_learning", "model_free_rl", "successor_representation"]
keywords: ["offline", "replay", "supports", "planning", "human", "reinforcement", "learning"]
key_citations: ["momennejad2017_successor_representation_humans", "russek2017_model_based_reinforcement", "tolman1948_cognitive_maps_rats"]
---

### One-line summary

MVPA evidence from fMRI shows that offline neural replay of a distal task state during rest periods predicts subsequent replanning behaviour, and that neural sensitivity to unsigned prediction errors during learning forecasts both replay and replanning.

---

### Background & motivation

Planning in sequential environments requires integrating information acquired across separate, temporally distal learning episodes. Prior accounts assumed integration occurs online — either at encoding or at decision time — but the computational cost of online integration is high, especially in complex environments. A key unresolved question was whether offline replay during rest periods (analogous to the Dyna algorithm in machine learning) contributes to this integration, and if so, what determines which memories get replayed. This paper provides the first human neural evidence linking offline replay directly to a change in choice behaviour.

---

### Methods

- **Participants**: 24 human participants (2 excluded for incomplete data) underwent fMRI.
- **Task**: A 2-stage reward revaluation paradigm inspired by Tolman latent learning tasks. Each block had three phases — Learning (full 2-step decision tree), Relearning (Stage II only; rewards changed in revaluation blocks but not control blocks), and Test (Stage I choice). Four blocks total per participant (2 revaluation, 2 control), crossed with a noise manipulation (noisy vs. noiseless rewards), yielding a 2×2 factorial design.
- **Replay measure**: Stage I stimuli (faces or scenes) were always a different visual category from Stage II stimuli. An L2-regularised logistic regression classifier was trained on a separate functional localiser run and applied TR-by-TR during three 30-second rest periods embedded in the Relearning phase. Classifier evidence for Stage I category in category-selective ROIs (fusiform for faces, parahippocampal for scenes) served as the neural replay index.
- **Prediction error analysis**: Unsigned reward prediction errors (|RPE|) were estimated using a Temporal Difference learning model (learning rate = 0.7, fixed across participants). Model-based fMRI parametric modulation identified regions where PE response correlated with subsequent replay and replanning score across blocks and subjects.
- **Univariate analysis**: GLM contrasting rest-period BOLD signal during revaluation vs. control blocks.
- **Key measure of behaviour**: Replanning magnitude = proportion of optimal Stage I choices at Test minus proportion of same-direction choices at end of Learning phase.

---

### Key findings

- **Replay predicts replanning**: MVPA evidence for Stage I replay during rest correlated significantly with subsequent replanning magnitude in revaluation blocks (Spearman rho = 0.54, p = 0.0068) but not control blocks (rho = −0.13, p = 0.55); the difference between conditions was significant (p = 0.023, bootstrap).
- **Specificity**: Stage II replay did not correlate with replanning in either condition, ruling out nonspecific engagement as the driver.
- **Unsigned PE predicts replay and replanning**: Conjunction analysis identified regions (ACC, mid-cingulate, posterior medial cortex/precuneus, basal ganglia/putamen) where neural sensitivity to unsigned PE during Relearning predicted both subsequent replay and subsequent replanning magnitude (p < 0.005 extent threshold, cluster FWE corrected p < 0.05).
- **Elevated rest-period activity**: Hippocampus and anterior cingulate (extending to vmPFC at relaxed threshold) showed greater activity during rest in revaluation than control blocks (p < 0.005, cluster FWE corrected).
- **Within-block dynamics**: Replay evidence decreased across the three rest periods in revaluation blocks (Rest 1 > Rest 3, t(23) = 2.9, p = 0.007), tracking the decrease in unsigned PE as participants learned new Stage II rewards; no such pattern appeared in control blocks.
- **Behavioural confirmation**: Participants showed significant revaluation behaviour in revaluation blocks (t(23) = 4.89, p < 0.0001) but not control blocks (t(23) = −0.10, p = 0.92); the difference was significant (t(23) = 4.33, p = 0.0002).

---

### Computational framework

**Reinforcement learning — Dyna architecture and prioritized sweeping.**

The paper is explicitly framed around two machine learning algorithms:

1. **Dyna (Sutton, 1991)**: An RL architecture in which an agent learns both online (from direct experience) and offline (by replaying stored experience to update value estimates). The key idea applied here is that offline replay of past trajectories can integrate distal state-action-reward associations and update planning policies without requiring new online experience.

2. **Prioritized sweeping (Moore & Atkeson, 1993; Peng & Williams, 1993)**: An extension of Dyna that selects which memories to replay by prioritising states with large prediction errors — unsigned PE signals surprise/uncertainty and marks related predecessor states for preferential replay, since surprising outcomes may imply that distal states also need updating.

Key variables: state-action value Q(s,a), reward prediction error δ = r + γ·max Q(s',a') − Q(s,a) (with γ=1 for the 2-step MDP), learning rate α = 0.7. Neural replay is operationalised as MVPA classifier evidence for a specific stimulus category in sensory cortical ROIs during off-task rest.

---

### Prevailing model of the system under study

The introduction situates the work against a longstanding assumption — traceable to Tolman (1948) — that integration of distal episodes for planning occurs online: either during encoding (when newly learned rewards are immediately propagated to distal state values, e.g. Wimmer & Shohamy, 2012; Shohamy & Daw, 2015) or at decision time (via mental simulation of candidate trajectories, e.g. Doll et al., 2015). The dominant human fMRI literature at the time of writing had demonstrated benefits of online neural reinstatement on decision-making but had not tested whether integration occurring during offline rest could specifically drive changes in choice behaviour. The rodent literature showed that hippocampal replay is correlated with task performance, but without isolating offline integrative replay as the mechanism. In short, the working model was that planning is an online process, and offline replay was at best a consolidation mechanism, not a direct driver of policy updating.

---

### What this paper contributes

The paper provides the first human neural evidence that offline replay — not merely correlated with, but predictive of, subsequent behavioural replanning — plays a functional role in integrating distal memories to update planning policies. Key advances:

- Establishes a selective, category-specific link between rest-period MVPA replay evidence and replanning (Stage I replay predicts replanning; Stage II replay does not), ruling out generic attentional or motivational confounds.
- Shows that the brain's response to unsigned prediction error during Relearning tags memories for prioritised offline replay, linking the prioritized sweeping algorithm to specific neural substrates (ACC, basal ganglia, posterior medial cortex).
- Demonstrates that hippocampus and ACC are more active during rest in conditions that require integrative replanning, consistent with a memory consolidation/integration role for these regions in goal-directed behaviour.
- Provides a two-function account of replay: (1) initial replay triggered by PE searches the memory graph for states to tag with priority; (2) subsequent replay simulates and integrates those tagged trajectories to update policies.

---

### Brain regions & systems

- **Hippocampus / medial temporal lobe** — elevated univariate activity during rest in revaluation vs. control blocks; proposed locus of episodic memory storage and integrative replay.
- **Anterior cingulate cortex (ACC)** — elevated activity during revaluation rest; PE sensitivity predicts both replay and replanning; proposed role in conflict detection, signalling need for controlled memory retrieval.
- **Mid-cingulate cortex** — elevated activity during revaluation rest; PE sensitivity conjunction.
- **Posterior medial cortex (PMC) / precuneus** — PE sensitivity predicts both replay and replanning; associated with recall and integration of memories over long time-scales.
- **Basal ganglia / putamen** — PE sensitivity predicts both replay and replanning; consistent with a role in signalling reward prediction errors.
- **Ventromedial prefrontal cortex (vmPFC)** — elevated activity during revaluation rest at relaxed threshold; implicated in memory retrieval of relevant information and value representation.
- **Fusiform gyrus / parahippocampal gyrus** — category-selective sensory cortical ROIs used as MVPA targets for measuring face and scene replay respectively.

---

### Mechanistic insight

This paper meets both criteria for the high bar.

**Criterion 1 — Algorithm**: The paper formalises an algorithm (Dyna + prioritized sweeping): unsigned PE tags states for replay; replay integrates distal episodes; integration updates the policy. This is a process account capable of explaining the phenomenon.

**Criterion 2 — Neural data**: fMRI data (MVPA replay index, model-based PE parametric modulation, univariate rest contrasts) specifically support the algorithm: the PE-sensitive regions predicted replay, and replay predicted replanning — forming a chain of evidence linking the model's computational constructs to measured neural signals.

Mapped to Marr's levels:

- **Computational**: The brain must integrate temporally distal state-reward associations to update its policy before facing a choice. The problem is efficient policy updating under uncertainty with limited online processing time.
- **Algorithmic**: Unsigned prediction errors flag episodes for prioritised offline replay during rest. Replay reinstates sensory representations of distal states (measurable via MVPA in category-selective cortex), enabling the brain to simulate and integrate multi-step trajectories and propagate value updates backward through the decision graph.
- **Implementational**: Hippocampus and ACC show elevated BOLD during revaluation rest, and ACC/basal ganglia/PMC respond to unsigned PE and predict both replay and replanning. The paper does not resolve specific cell types or connectivity mechanisms, but identifies a hippocampal-prefrontal network as the substrate. No pharmacological or single-unit data are provided; temporal resolution of fMRI precludes direct observation of sub-second sequential replay.

---

### Limitations & open questions

- Results are correlational; causal role of offline replay in replanning cannot be definitively established.
- Temporal resolution of fMRI precludes direct measurement of sequential (sub-second) replay, unlike rodent electrophysiology; whether human rest-period replay is truly sequential (forward or reverse) remains untested.
- The signed vs. unsigned PE distinction could not be dissociated because most PEs were positive given the task incentives.
- The noise manipulation (noisy vs. noiseless rewards) showed only trend-level differences between conditions, limiting conclusions about how reward volatility modulates replay.
- The replay-replanning correlation was mainly significant in the noisy (not noiseless) reward condition, suggesting a possible ceiling effect for online integration in simpler reward structures — but the study lacked power to test this definitively.
- The tagging mechanism (PE tags memories at encoding vs. unbiased retrieval searching for high-PE memories offline) cannot be dissociated with the current design.
- The paper uses a fixed group-level learning rate rather than individually estimated parameters, which may obscure individual differences in PE magnitude and their neural correlates.
- Future work needed: larger decision trees, MEG or intracranial recordings for sequential replay characterisation, parametric manipulation of volatility, and exploration of how offline replay contributes to generalisation and the successor representation.

---

### Connections & keywords

**Key citations**:
- Sutton (1991) — Dyna architecture
- Moore & Atkeson (1993); Peng & Williams (1993) — prioritized sweeping
- Gershman, Markman & Otto (2014) — behavioural reward revaluation paradigm
- Momennejad et al. (2017) — successor representation in human RL
- Russek et al. (2017) — successor representation and model-based/model-free RL
- Tolman (1948) — cognitive maps, latent learning, revaluation tasks
- Wimmer & Shohamy (2012) — hippocampal-dependent encoding-time integration
- Doll et al. (2015) — online prospective reinstatement during model-based choice
- Pfeiffer & Foster (2013) — hippocampal place-cell sequential replay
- Ambrose, Pfeiffer & Foster (2016) — reverse replay modulated by changing reward
- Polyn et al. (2005) — category-specific cortical activity as replay index
- Gruber et al. (2016) — post-learning hippocampal dynamics and reward memory

**Named models or frameworks**:
- Dyna (Sutton 1991)
- Prioritized sweeping (Moore & Atkeson 1993; Peng & Williams 1993)
- Temporal Difference (TD) learning
- Successor representation (Momennejad et al. 2017; Russek et al. 2017)
- Reward revaluation paradigm (Gershman et al. 2014)

**Brain regions**:
- Hippocampus / medial temporal lobe
- Anterior cingulate cortex (ACC)
- Mid-cingulate cortex
- Posterior medial cortex (PMC) / precuneus
- Basal ganglia / putamen
- Ventromedial prefrontal cortex (vmPFC)
- Fusiform gyrus
- Parahippocampal gyrus

**Keywords**:
- offline replay
- hippocampal replay
- reward revaluation
- reinforcement learning
- Dyna architecture
- prioritized sweeping
- unsigned prediction error
- MVPA
- fMRI
- sequential decision-making
- memory integration
- goal-directed behaviour
