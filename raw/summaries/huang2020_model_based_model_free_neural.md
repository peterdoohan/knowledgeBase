---
source_file: huang2020_model_based_model_free_neural.md
paper_id: huang2020_model_based_model_free_neural
title: "Goal-oriented and habitual decisions: Neural signatures of model-based and model-free learning"
authors:
  - "Yi Huang"
  - "Zachary A. Yaple"
  - "Rongjun Yu"
year: 2020
journal: NeuroImage
paper_type: review
contribution_type: review
species:
  - human
tasks:
  - two_step_task
methods:
  - fmri
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - ventromedial_prefrontal_cortex
  - striatum
  - ventral_striatum
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
keywords:
  - model_based_reinforcement_learning
  - model_free_reinforcement_learning
  - neuroimaging_meta_analysis
  - activation_likelihood_estimation
  - ventral_striatum
  - reward_prediction_error
  - goal_directed_behaviour
  - habitual_behaviour
  - basal_ganglia
  - prefrontal_cortex
  - fmri
  - computational_psychiatry
  - goal
  - oriented
  - habitual
  - decisions
  - neural
  - signatures
  - model
  - based
key_citations:
  - russek2017_model_based_reinforcement
wiki_pages:
  - wiki/topics/model_based_vs_model_free_reinforcement_learning_frameworks_in_anterior_cingulate_future_state_control
  - wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning
---

### One-line summary

A coordinate-based neuroimaging meta-analysis reveals that both model-based and model-free reinforcement learning engage the ventral striatum, while model-based learning additionally recruits vmPFC/anterior cingulate and model-free learning specifically activates globus pallidus and caudate head.

---

### Background & motivation

Human decision-making is characterised by two dissociable learning systems: a slow, deliberative model-based system that builds internal representations of state-action-outcome contingencies, and a fast, habitual model-free system that updates cached action values via trial-and-error. Although individual fMRI studies have mapped neural correlates to each system, findings have been inconsistent — particularly regarding whether the ventral striatum is exclusive to model-free learning and whether the hippocampus reliably supports model-based processing. A quantitative meta-analysis was needed to identify regions of robust concordance across studies and resolve these contradictions.

---

### Methods

- **Literature search**: PubMed and Web of Science searched for "model-free" AND "model-based" AND "fMRI" (March 2019); supplemented by reference lists and Google Scholar.
- **Inclusion criteria**: whole-brain fMRI with random-effects analysis; coordinates reported in Talairach or MNI space for model-free and/or model-based signals separately or in conjunction; human participants.
- **Final dataset**: 21 eligible articles, 22 experiments, 868 participants, 332 foci.
- **Analysis tool**: GingerALE v3.0 using the Activation Likelihood Estimation (ALE) algorithm.
- **Statistical threshold**: cluster-level FWE correction p < 0.05 (5000 permutations), cluster-forming threshold p < 0.001.
- **Contrasts**: separate ALE maps for model-free and model-based; conjunction analysis (voxel minimum); contrast analyses (ALE map subtraction), thresholded at uncorrected p < 0.05.
- **Post-hoc analyses**: restricted to healthy young drug-free adults; restricted to sequential decision (two-step/maze) tasks.

---

### Key findings

- **Conjunction (both systems)**: Bilateral ventral striatum showed concordant activation across both model-free and model-based studies, challenging the view that the ventral striatum is a dedicated model-free substrate.
- **Model-free ALE map**: Bilateral ventral striatum and bilateral globus pallidus (left cluster: 3032 mm³, peak left globus pallidus; right cluster: 2680 mm³, peak right caudate head).
- **Model-based ALE map**: Bilateral ventral striatum/caudate head (4640 mm³), dorsal and ventral anterior cingulate (1144 mm³), anterior prefrontal cortex/medial frontal gyrus (1088 mm³), and medial frontal cortex (760 mm³).
- **Model-free > model-based contrast**: Left lateral globus pallidus, medial globus pallidus, right superior temporal gyrus, and caudate head.
- **Model-based > model-free contrast**: Medial frontal gyrus (BA 9) and anterior cingulate (BA 25).
- **Hippocampus**: No concordant activation was found for model-based learning across studies, despite individual studies reporting hippocampal involvement.
- **Post-hoc robustness**: Results were consistent in the healthy young drug-free subsample and in the sequential-task subsample (14 studies).

---

### Computational framework

The paper is framed around **reinforcement learning (RL)**, specifically the distinction between model-free (MF) and model-based (MB) RL:

- **Model-free RL**: Stores cached action values updated via temporal-difference prediction errors (RPE); computationally cheap but inflexible.
- **Model-based RL**: Maintains a forward model of state transitions and expected outcomes; computationally demanding but flexible.

The neuroimaging literature is interpreted through this dichotomy, using parametric contrasts of MF vs. MB prediction error signals as the primary experimental manipulation. The paper does not itself introduce a new computational model but uses ALE meta-analysis as its formal method to aggregate spatial activation coordinates across studies.

---

### Prevailing model of the system under study

Prior to this meta-analysis, the standard view held a clean dissociation: the **dopamine-rich striatum** (particularly ventral striatum) was considered the dedicated neural substrate for model-free learning, encoding reward prediction errors in a TD-learning framework. Model-based learning was thought to rely on **vmPFC/OFC** for value representation and **hippocampus** for forward planning and state-transition memory. The field had accumulated inconsistent findings — some studies showing ventral striatal signals during model-based computations, others not — without a systematic synthesis. The hippocampus was a particularly contested candidate for model-based processing, as individual studies showed its involvement but the broader pattern was unclear.

---

### What this paper contributes

The meta-analysis establishes that **ventral striatum is not selective for model-free learning** but is engaged by both learning systems, providing the strongest quantitative evidence to date against a strict striatum-as-model-free-only view. It confirms that **vmPFC and anterior cingulate are specifically associated with model-based processing**, consistent with their proposed role in goal-directed behaviour. It further specifies that model-free processing extends beyond ventral striatum to include **globus pallidus and caudate head** — regions associated with basal ganglia TD-learning circuitry. Notably, the meta-analysis finds **no concordant hippocampal activation** for model-based learning, suggesting hippocampal involvement may be task-dependent (e.g. requiring explicit spatial structure) rather than a general feature of model-based computation.

---

### Brain regions & systems

- **Ventral striatum (bilateral)** — engaged by both model-free and model-based learning; proposed to encode reward prediction errors and possibly arbitrate between the two systems.
- **Globus pallidus (left lateral and medial)** — selectively concordant for model-free learning; part of the dorsal striatal/basal ganglia circuitry for TD prediction errors.
- **Caudate head (right, model-free; bilateral, model-based)** — implicated in both systems with differential lateralisation; associated with prediction error signalling in basal ganglia.
- **Ventromedial prefrontal cortex (vmPFC) / anterior prefrontal cortex (BA 9)** — specifically concordant for model-based learning; consistent with role in goal-directed value representation.
- **Anterior cingulate cortex (dorsal and ventral, BA 24/25/32)** — specifically concordant for model-based learning; proposed role in executive control and flexible decision-making.
- **Hippocampus** — expected candidate for model-based learning based on prior individual studies, but no concordant activation found across the meta-analysis.

---

### Mechanistic insight

This paper does not meet the bar for mechanistic insight as defined here. It is a meta-analysis that aggregates activation coordinates across studies; it does not itself present a novel algorithm or provide new neural recordings to test a specific computational mechanism. The ALE method identifies spatial concordance across studies but cannot adjudicate between competing algorithmic accounts (e.g., whether ventral striatal activity during model-based tasks reflects genuine MB computation, arbitration between systems, or a common currency signal). The paper provides spatial constraints on where MB and MF computations occur, which could inform but does not constitute a mechanistic account at Marr's algorithmic or implementational levels.

---

### Limitations & open questions

- The conjunction/contrast analyses used uncorrected thresholds (p < 0.05), making those specific comparisons exploratory.
- Hippocampal absence may reflect task design (most studies used abstract two-step tasks without explicit spatial structure), not genuine lack of hippocampal involvement in model-based learning.
- Model-based and model-free taxonomy overlaps with other dichotomies (explicit/implicit, episodic/habit, goal-directed/habitual) but the analysis was restricted to studies using the MB/MF computational framing; it is unclear how well findings generalise across equivalent paradigms.
- The two systems interact (model-free signals can be informed by task structure; meta-RL frameworks propose the PFC learns to act as a standalone RL system trained by dopaminergic striatum), and the meta-analysis cannot capture these interactions.
- Clinical implications for OCD, addiction, and depression are discussed but not directly tested; the stereotaxic maps provide a reference rather than causal evidence.
- Relatively small final dataset (22 experiments), limiting power for subgroup and contrast analyses.

---

### Connections & keywords

- **Key citations**: Daw et al. (2005, 2011); Glascher et al. (2010); Balleine & O'Doherty (2010); Deserno et al. (2015a); Bornstein & Daw (2012, 2013); Russek et al. (2017); Yaple & Yu (2019); Turkeltaub et al. (2002); Eickhoff et al. (2017); Wang et al. (2018 — meta-RL).
- **Named models or frameworks**: Model-free RL (temporal-difference learning); Model-based RL (forward model / decision-tree planning); Activation Likelihood Estimation (ALE); Actor-critic framework; Meta-reinforcement learning (meta-RL); Two-step task (Daw et al., 2011).
- **Brain regions**: Ventral striatum, globus pallidus, caudate head, vmPFC, orbitofrontal cortex, anterior cingulate cortex, medial prefrontal cortex, hippocampus.
- **Keywords**: model-based reinforcement learning, model-free reinforcement learning, neuroimaging meta-analysis, activation likelihood estimation, ventral striatum, reward prediction error, goal-directed behaviour, habitual behaviour, basal ganglia, prefrontal cortex, fMRI, computational psychiatry.

### Related wiki pages
- [[wiki/topics/model_based_vs_model_free_reinforcement_learning_frameworks_in_anterior_cingulate_future_state_control|Model-based vs model-free reinforcement learning frameworks in anterior cingulate future-state control]]
- [[wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning|Orbitofrontal cortex as a cognitive map of task state for model-based reinforcement learning]]
