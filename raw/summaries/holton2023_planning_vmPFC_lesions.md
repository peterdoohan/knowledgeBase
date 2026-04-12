---
source_file: holton2023_planning_vmPFC_lesions.md
paper_id: holton2023_planning_vmPFC_lesions
title: "Disentangling the component processes in complex planning impairments following ventromedial prefrontal lesions"
authors:
  - "Eleanor Holton"
  - "Bas van Opheusden"
  - "Jan Grohn"
  - "Harry Ward"
  - "John Grogan"
  - "Patricia L Lockwood"
  - "Ili Ma"
  - "Wei Ji Ma"
  - "Sanjay G Manohar"
year: 2023
journal: "(preprint / eLife submission)"
paper_type: empirical
contribution_type: empirical
species:
  - human
tasks:
  - two_step_task
methods:
  - lesion
  - behavioral_analysis
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - orbitofrontal_cortex
  - ventromedial_prefrontal_cortex
  - striatum
  - ventral_striatum
frameworks:
  - reinforcement_learning
  - model_based_rl
keywords:
  - vmpfc_lesion
  - planning_depth
  - feature_drop_rate
  - heuristic_quality
  - four_in_a_row
  - two_step_task
  - model_based_planning
  - model_free_planning
  - tree_search
  - frontal_lobe_lesion
  - cognitive_components_of_planning
  - computational_lesion_study
  - disentangling
  - component
  - processes
  - complex
  - planning
  - impairments
  - following
  - ventromedial
key_citations:
  - vopheusden2023_expertise_planning_depth
  - daw2011_model_based_striatal_prediction
  - wilson2014_best_practices_scientific
  - schuck2016_orbitofrontal_cortex_state
wiki_pages:
  - wiki/topics/hippocampal_prefrontal_replay_in_planning
  - wiki/topics/medial_prefrontal_cortex_in_rat_goal_directed_vs_habitual_control
  - wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning
---

### One-line summary

vmPFC lesions impair complex planning by increasing the tendency to overlook task-relevant features and by reducing the depth of forward search, deficits that are detectable in a rich board-game task but not in the simpler Two-Step Task.

---

### Background & motivation

Damage to ventromedial prefrontal cortex (vmPFC) is well known to disrupt real-world planning and decision-making, yet the precise cognitive components responsible remain unclear. Prior work has proposed candidate deficits — impaired future simulation, impaired multi-attribute evaluation, or failure to select relevant information — but existing tasks lack the resolution to distinguish these. A further open question is whether vmPFC planning deficits depend on the complexity of the state space or reflect a more general impairment in model-based reasoning. This paper addresses both gaps using a recently validated computational framework for complex planning alongside an established simpler planning paradigm.

---

### Methods

- **Participants**: Three groups — vmPFC lesion patients (Study 1: N=10; Study 2: N=30), lesion control patients with damage outside vmPFC (Study 1: N=8; Study 2: N=19), and healthy age-matched controls (Study 1: N=30; Study 2: N=20). Lesion classification used the Harvard-Oxford Cortical Structural Atlas; vmPFC lesions were highly focal (median volume 8.5 cm³ in Study 1).
- **Study 1 — Four-in-a-Row Task**: Participants played a four-by-nine board game against computer opponents of graded difficulty, completing 40 games each. Performance was quantified as Elo rating. A computational process model (van Opheusden et al. 2023) decomposed behaviour into three summary parameters: planning depth (average forward-search length), heuristic quality (correlation between participant feature weights and optimal weights), and feature drop rate (probability of overlooking a board feature on a given move). Model fitting used inverse binomial sampling on a high-performance cluster; group differences tested with non-parametric Mann-Whitney U tests.
- **Study 2 — Two-Step Task**: A variant with stationary (abruptly shifting) rather than drifting reward probabilities, administered in person. Model-free vs model-based behaviour assessed via stay-probability logistic regression (transition × outcome interaction) and a Bayesian hierarchical SARSA(λ) reinforcement learning model with separate model-free and model-based value weights. Response time sensitivity to rare vs common transitions also analysed.
- **Controls**: Regression analyses verified that Elo deficits were predicted by vmPFC lesion volume rather than total lesion volume.

---

### Key findings

- **Four-in-a-Row performance**: vmPFC patients showed lower Elo ratings than both lesion controls (median −66.0 vs 33.5; U=14, p=0.021) and healthy controls (median HC=27.5; U=71, p=0.014). Elo rating was predicted by vmPFC lesion volume (β=−0.08, p=0.033) but not total lesion volume (p=0.664).
- **Feature drop**: vmPFC patients were significantly more likely to overlook game-relevant board features compared to lesion controls (U=72.0, p=0.002) and healthy controls (U=246.0, p=0.001).
- **Planning depth**: vmPFC patients planned to lower depth than lesion controls (U=15.0, p=0.013); the comparison with healthy controls alone did not reach significance (p=0.073), but depth was lower when both control groups were pooled (p=0.035).
- **Heuristic quality**: No significant group difference (vmPFC vs LCs: p=0.072; vmPFC vs HCs: p=0.078).
- **Two-Step Task**: All groups performed above chance but showed no significant group differences in accuracy (F(2,66)=0.71, p=0.495), stay-probability model-based index (H(2)=2.34, p=0.310), model-based RL weight (H(2)=5.19, p=0.075), or response time transition sensitivity (H(2)=2.35, p=0.309). Notably, model-based behaviour was attenuated across all groups, consistent with the older age of the sample (mean ~58–68 years).

---

### Computational framework

The paper applies two computational frameworks.

**Four-in-a-Row planning model** (van Opheusden et al. 2023): A best-first tree-search algorithm combined with a heuristic value function. The value function V(s) is a weighted sum of five board features (connected 2-in-a-row, unconnected 2-in-a-row, 3-in-a-row, 4-in-a-row, proximity to centre), with separate scaling constants for the active vs passive player and additive Gaussian noise. The tree-search performs iterative best-first expansion with minimax backpropagation and probabilistic stopping, plus a pruning threshold (θ) that eliminates branches below best-value minus θ. Individual parameters are aggregated into three interpretable summary statistics: depth, heuristic quality, and feature drop rate. The key assumption is that human planners deploy a resource-limited tree search guided by heuristic state evaluation and selective attention.

**Two-Step Task RL model** (Daw et al. 2011 variant): A hybrid SARSA(λ) model-free learner combined with a model-based learner using the Bellman equation over the known transition structure. Choice at Step 1 is governed by a softmax over a weighted combination of model-based value, model-free value, and a repetition bias, with separate inverse temperature parameters (β_mb, β_mf). Fitted using a Bayesian hierarchical framework in Stan.

---

### Prevailing model of the system under study

The introduction frames vmPFC as broadly necessary for planning and future-oriented decision-making, citing evidence from naturalistic tasks (Multiple Errands Task), standard laboratory paradigms (Tower of London), and neuroimaging showing OFC/vmPFC correlates of stepwise planning. Two competing accounts dominate: (1) vmPFC is specifically required for simulating or imagining future events (future episodic thinking, mental time travel), and (2) vmPFC is required for integrating multiple value attributes when evaluating options. The authors treat these as separable and prior work as unable to distinguish them. They also note that orbitofrontal cortex has been proposed to encode a cognitive map of task state space (Wilson et al. 2014; Schuck et al. 2016), which would support model-based forward planning. The implicit working model is thus that vmPFC/OFC supports one or more of: (a) mental simulation of future states, (b) evaluation/integration of multi-attribute value, and (c) selective allocation of attention to value-relevant features — and that damage to this region disrupts real-world planning through one or more of these routes.

---

### What this paper contributes

Using a computational process model with sufficient resolution to separate planning components, this paper shows that vmPFC lesions specifically impair (a) the tendency to attend to all relevant board features (feature drop) and (b) the depth of forward search, while leaving heuristic quality intact. This provides the first computational evidence that vmPFC patients plan less deeply into the future — consistent with qualitative accounts of impaired episodic future thinking — and implicates a selective attentional or information-integration deficit rather than a general failure of heuristic knowledge. The dissociation with heuristic quality argues against a pure evaluation account. The null result on the Two-Step Task further shows that vmPFC planning deficits are specific to complex, high-branching state spaces and are not detectable with simpler binary two-step paradigms, particularly in older cohorts where model-based behaviour is already attenuated.

---

### Brain regions & systems

- **Ventromedial prefrontal cortex (vmPFC)** — focal lesion site; the paper tests whether it is causally necessary for complex planning, and specifically for forward-search depth and selective feature attention during planning.
- **Orbitofrontal cortex (OFC)** — mentioned in the introduction as the region showing neural correlates of stepwise planning and state-space representations in neuroimaging; treated as overlapping with vmPFC in the broader literature the paper situates itself against.
- **Hippocampus** — discussed in the Discussion as a likely partner region for model-based simulation, citing evidence that hippocampal damage impairs model-based planning in rodents and humans, and that vmPFC–hippocampus coupling predicts structured inference.
- **Ventral striatum / dorsomedial PFC** — noted as additional damage sites in 3 vmPFC patients in Study 1, flagged as a potential confound.

---

### Mechanistic insight

The paper partially meets the bar. It presents a specific algorithm (best-first tree search with feature-weighted heuristics) and provides lesion data showing that vmPFC damage selectively disrupts the feature drop and depth parameters of that algorithm while sparing heuristic quality — a dissociation that has mechanistic specificity beyond a general performance deficit. However, the paper does not provide direct neural recordings or imaging data linking specific model variables (e.g., tree-search depth signals, feature saliency representations) to measured neural activity. The evidence is causal (lesions) but not mechanistically constraining at the algorithmic level beyond ruling out the heuristic quality account.

Mapping onto Marr's levels:
- **Computational**: The brain must plan through complex state spaces to maximise long-run reward; this requires forward simulation of possible futures and evaluation of candidate states using task-relevant features.
- **Algorithmic**: The process involves iterative best-first tree search guided by a heuristic feature-weighted value function, with a stochastic feature-attention mechanism (captured by feature drop rate) and a stopping/pruning process that determines depth. vmPFC lesions increase feature drop probability and reduce search depth without impairing feature weight calibration.
- **Implementational**: Not addressed by this paper. The authors speculate that vmPFC may coordinate simulation performed in hippocampal circuits and may support goal-directed attention toward value-relevant features, but no neural implementation data are provided.

---

### Limitations & open questions

- Small sample sizes, especially in Study 1 (N=10 vmPFC, N=8 LC), limit statistical power; the depth finding did not survive comparison with healthy controls alone.
- The mechanism underlying increased feature drop is ambiguous: it could reflect impaired integration of value-relevant attributes, impaired goal-directed attention, or other processes. Eye-tracking is noted as a future direction.
- The Two-Step Task null result is confounded by the age of the sample (mean ~58–68 years), which attenuates model-based behaviour regardless of lesion status; it is therefore not possible to conclude that vmPFC is truly uninvolved in simple two-step planning.
- Lesion heterogeneity: three vmPFC patients also had striatal or dorsomedial PFC damage; individual lesion maps are provided but co-lesion effects cannot be fully excluded.
- The paper cannot determine whether planning depth and feature drop deficits arise from the same or different underlying mechanisms.
- Whether the Four-in-a-Row deficits generalise beyond this specific game to naturalistic real-world planning contexts is not directly tested.
- Publication year is listed as 2023 in the filename, but the paper appears to be a preprint/submission and the precise publication record is not stated in the document.

---

### Connections & keywords

**Key citations**:
- van Opheusden et al. (2023) — Four-in-a-Row task and planning model
- Daw et al. (2011) — Two-Step Task and hybrid RL model
- Shallice & Burgess (1991); Tranel et al. (2007) — naturalistic vmPFC planning deficits
- Wilson et al. (2014); Schuck et al. (2016) — OFC as cognitive map of task space
- Bertossi et al. (2015, 2016, 2017) — vmPFC and episodic future thinking
- Vikbladh et al. (2019) — hippocampal contributions to model-based planning
- Huys et al. (2012, 2015) — decision-tree pruning in human planning
- Eppinger et al. (2013) — age-related reductions in model-based behaviour

**Named models or frameworks**:
- Four-in-a-Row planning model (best-first tree search + heuristic value function)
- Two-Step Task (Daw et al. 2011)
- SARSA(λ) hybrid model-free/model-based RL model
- Elo / Bayeselo rating system
- Harvard-Oxford Cortical Structural Atlas (lesion classification)

**Brain regions**:
- Ventromedial prefrontal cortex (vmPFC)
- Orbitofrontal cortex (OFC)
- Hippocampus
- Ventral striatum
- Dorsomedial PFC

**Keywords**:
- vmPFC lesion, planning depth, feature drop rate, heuristic quality, Four-in-a-Row, Two-Step Task, model-based planning, model-free planning, tree search, frontal lobe lesion, cognitive components of planning, computational lesion study

### Related wiki pages
- [[wiki/topics/hippocampal_prefrontal_replay_in_planning|Hippocampal–prefrontal replay in planning]]
- [[wiki/topics/medial_prefrontal_cortex_in_rat_goal_directed_vs_habitual_control|Medial prefrontal cortex in rat goal-directed vs habitual control]]
- [[wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning|Orbitofrontal cortex as a cognitive map of task state for model-based reinforcement learning]]
