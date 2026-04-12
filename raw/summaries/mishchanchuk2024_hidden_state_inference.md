---
source_file: mishchanchuk2024_hidden_state_inference.md
paper_id: mishchanchuk2024_hidden_state_inference
title: "Hidden state inference requires abstract contextual representations in ventral hippocampus"
authors:
  - "Karyna Mishchanchuk"
  - "Gabrielle Gregoriou"
  - "Albert Qu"
  - "Alizée Kastler"
  - "Quentin Huys"
  - "Linda Wilbrecht"
  - "Andrew F. MacAskill"
year: 2024
journal: "bioRxiv (preprint, posted May 2024)"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
tasks:
  - probabilistic_reversal_learning
methods:
  - calcium_imaging
  - computational_modeling
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - orbitofrontal_cortex
  - nucleus_accumbens
  - ventral_hippocampus
frameworks:
  - reinforcement_learning
  - bayesian_inference
keywords:
  - hidden_state_inference
  - latent_context_representation
  - ventral_hippocampus_ca1
  - probabilistic_reversal_learning
  - 2_armed_bandit
  - bayesian_belief_updating
  - reward_prediction_error
  - dopamine_photometry
  - calcium_imaging
  - state_inference_vs_q_learning
  - abstract_context_coding
  - hippocampal_remapping
  - hidden
  - state
  - inference
  - requires
  - abstract
  - contextual
  - representations
  - ventral
key_citations:
  - wikenheiser2016_cognitive_maps_hippocampus
wiki_pages:
  - wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning
  - wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning
---

### One-line summary

Ventral CA1 hippocampal neurons are causally necessary for hidden state inference in a probabilistic reversal learning task, and robustly represent the two abstract latent task contexts in a manner analogous to spatial context coding.

---

### Background & motivation

Many behavioral settings require inferring unobservable latent contexts from sequences of stochastic outcomes — a process called hidden state inference (SI) — rather than incrementally updating action values trial by trial (Q-learning). While the hippocampus is well known for organizing sensory inputs into discrete spatial and contextual representations, its direct role in representing and utilizing non-spatial, abstract latent contexts to guide decision-making had not been demonstrated at the neural level. Deficits in hidden state inference are a core feature of psychiatric disorders including schizophrenia, depression, and anxiety, making this question clinically important.

---

### Methods

- **Task**: Operant 2-armed bandit (probabilistic serial reversal learning) in adult male C57BL/6 mice. Two levers had 70%/10% reward probability; contingencies reversed after 10–32 high-probability choices, unsignalled.
- **Behavioral modelling**: Comprehensive model comparison across Q-learning variants (with bias, perseverance, reward/punishment sensitivity, forgetting, Pearce-Hall dynamics) and state inference (SI) variants. Model fits evaluated by BIC and relative likelihood; model recovery (confusion/inversion matrices) used for validation.
- **Dopamine imaging**: Fiber photometry of dLight1.1 in nucleus accumbens core (NAc) during task performance (n = 5 mice). SI vs Q RPE predictions compared via trial-history sorting and time-lagged ridge regression (coefficient of partial determination).
- **Causal lesions**: Bilateral caspase (taCasp3) ablation of CaMKII+ vCA1 pyramidal neurons (n = 5 lesion, 3 sham); unilateral lesions used for dopamine photometry experiments (n = 5 per group) to isolate vCA1 contribution to NAc dopamine without confounding behavior.
- **Calcium imaging**: Miniscope (UCLA Miniscope V4) recording of GCaMP7f-expressing vCA1 pyramidal neurons during task (592 neurons, 9 sessions, 3 mice). Analysis included single-neuron selectivity indices, PCA of population trajectories, linear SVM decoding of choice/expected outcome/latent context, and cross-condition generalization decoding.

---

### Key findings

- All 10 mice were best fit by SI models over Q-learning models across multiple metrics: BIC (t(9) = 8.76, p = 0.000011), relative likelihood (t(9) = 12.7, p = 4.7 × 10⁻⁹), switch-behavior pattern matching (t(9) = 9.73, p = 0.000005), and trial-to-trial choice consistency (t(9) = 3.55, p = 0.006).
- NAc dopamine (dLight) reflected SI-based reward prediction errors: dopamine on CS+ differed significantly based on past opposite-lever outcome (O+ vs O-, t(66.4) = 3.62, p = 0.000574), consistent with SI-RPE predictions but not Q-RPE. SI-RPE explained more variance in dLight activity than Q-RPE (paired t, p = 0.034 for R² comparison; p = 0.012 for single-predictor R²).
- Bilateral vCA1 lesions impaired overall task performance (t(42) = 3.55, p = 0.001) and specifically reduced SI-consistent choices (t(48) = 3.75, p = 0.0005) without equivalently reducing Q-consistent choices, indicating selective loss of the SI strategy.
- Unilateral vCA1 lesions abolished SI signatures in ipsilateral NAc dopamine: the interaction between past choice outcome and lesion condition was significant (t(137.8) = 2.53, p = 0.01), and SI-RPE no longer outperformed Q-RPE in regression (sham: p = 0.047; lesion: p = 0.12; interaction F(1,8) = 8.55, p = 0.01).
- vCA1 population activity separated into three orthogonal principal components representing choice (PC1), expected outcome (PC2), and latent context (PC3). Choice, expected outcome, and context could each be decoded significantly above chance (all p < 0.001), and decoding was stable across trial periods including the ITI.
- Latent context representations were generalized and abstract: a decoder trained on one trial type within a context (e.g. RH) generalized to the other trial type in that context (e.g. LL), significantly above chance in both pseudo-population and single-session analyses (individual sessions: t(3) = 3.49, p = 0.03).
- Approximately 40% of recorded vCA1 neurons were selective for choice, ~20% for expected outcome, and ~30% for latent context.

---

### Computational framework

The paper employs **Bayesian hidden state inference** (also framed as partially observable Markov decision process inference) as its primary computational lens, contrasted with standard **Q-learning / reinforcement learning**.

In the SI framework, the agent maintains a belief state b(s) — the posterior probability of being in each latent task state (e.g. "right lever high", "left lever high") — updated via Bayes' rule from the sequence of past choices and their probabilistic outcomes. The key variables are: the belief b_t, a reward matrix R_m encoding the task's conditional reward probabilities, and a state transition probability γ governing how likely a block switch is on each trial. Action probabilities are derived via a softmax over belief-weighted expected values. This is contrasted with Q-learning, where only the value of the chosen action is updated on each trial and no inference over hidden states occurs. RPEs derived from each framework have distinct signatures: SI-RPE is sensitive to outcomes from both the chosen and unchosen lever (because both update the belief state), while Q-RPE is not.

---

### Prevailing model of the system under study

The hippocampus, and particularly CA1, is canonically understood as forming spatial context representations — "place cells" that fire at specific locations and undergo remapping between distinct spatial environments. This spatial context function has been extended theoretically to non-spatial latent contexts, with proposals that hippocampal circuitry may support hidden state inference through the creation and utilization of abstract subjective contexts. However, as the authors emphasize, direct investigation of hippocampal representations of non-spatial, latent (entirely abstract) contexts — defined solely by past probabilistic outcomes rather than by physical cues — had not been demonstrated prior to this study. The prevailing view implicated frontal cortex (OFC, mPFC) as the locus of latent state representations and SI, with the hippocampus presumed to supply contextual information to frontal regions, but the nature and necessity of hippocampal representations for this process remained untested.

---

### What this paper contributes

This study provides the first direct causal and neural-representational demonstration that ventral CA1 is necessary for hidden state inference over abstract, non-spatial latent contexts. Specifically:

- It shows that mice use SI (not Q-learning) to solve a probabilistic reversal task, and that NAc dopamine reflects SI-based RPEs — establishing the task as a valid SI paradigm.
- Causal lesion of vCA1 selectively abolishes SI-consistent behavior and removes SI signatures from NAc dopamine, without equivalently impairing Q-consistent choices, demonstrating that vCA1 is specifically required for the SI component of behavior.
- Population recordings reveal that vCA1 neurons represent the two abstract latent contexts with the same organizational logic (PC separation, remapping-like differentiation) as spatial context coding — extending the hippocampal context-coding framework to entirely abstract, outcome-defined states.
- The generalization decoding result is particularly important: context representations are not merely conjunctions of choice × outcome features but are genuinely abstracted over these features, consistent with the kind of stable "state" representation posited by SI theory.

---

### Brain regions & systems

- **Ventral CA1 (vCA1)** — primary region of interest; necessary for the behavioral use of hidden state inference and for SI signatures in NAc dopamine; vCA1 neurons represent latent task context in an abstract, generalized manner.
- **Nucleus accumbens core (NAc)** — used as a readout of dopamine-based RPE signals; dopamine release (via dLight) reflects SI-RPE rather than Q-RPE, and this signature depends on intact vCA1.
- **Medial prefrontal cortex (mPFC) / orbitofrontal cortex (OFC)** — discussed in context (not directly manipulated); proposed downstream recipients of vCA1 contextual signals; prior work shows frontal cortex lesions also disrupt SI dopamine signatures.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight.

**The phenomenon**: Mice use hidden state inference — Bayesian belief updating over two abstract task contexts — to optimally solve a probabilistic reversal learning task. This strategy requires an internal representation of which latent context is currently active, updated by both same-lever and opposite-lever outcomes.

**Computational level**: The brain is solving the problem of inferring which of two latent, unobservable task states is currently active from a noisy, stochastic sequence of outcomes, in order to identify the optimal action. This is a partially observable decision problem requiring probabilistic inference rather than simple value caching.

**Algorithmic level**: vCA1 maintains an abstract, generalized representation of the two latent task contexts — analogous to spatial context maps — that is updated by past probabilistic outcomes. This representation is read out by downstream structures (NAc dopamine system, and presumably frontal cortex) to compute SI-based reward prediction errors and guide choice. The population code is orthogonally organized: PC1 encodes choice, PC2 encodes expected outcome, and PC3 encodes latent context independently of choice and expected outcome.

**Implementational level**: Pyramidal neurons (CaMKII+) in the ventral two-thirds of CA1 are the cellular substrate. Approximately 30% of recorded neurons are selectively tuned to latent context. Some neurons fire for only one of four trial types (conjunctive), while others generalize across the two trial types within a context (abstract state cells). The paper does not resolve the specific connectivity or biophysical mechanisms by which vCA1 context signals are transmitted to NAc or frontal cortex.

**Bonus**: The study uses cell-type-specific caspase lesioning (CaMKII-Cre + flex-taCasp3), confirming that the causal role of vCA1 is mediated by excitatory pyramidal neurons specifically.

---

### Limitations & open questions

- Small sample sizes for neural recordings (3 mice, 592 neurons, 9 sessions) and lesion groups (5 mice per group), typical of the field but limiting statistical power and generalizability.
- The study does not identify the downstream pathway by which vCA1 context representations influence NAc dopamine — direct vCA1→NAc projections, indirect vCA1→mPFC→NAc routes, or other circuits remain unresolved.
- The mechanism by which vCA1 updates the context representation from past outcomes is not characterized — how does vCA1 compute belief state updates? What inputs drive this?
- Latent context representations are inferred from population activity in a small behavioral box; it is not clear whether similar activity confounds with spatial position were fully excluded, though the task was designed to minimize spatial variation.
- The model comparison is comprehensive but not exhaustive; alternative accounts (e.g. structured Q-learning with long history windows) are partially addressed by supplementary comparisons but not all variants are included.
- The study uses only male mice and one strain (C57BL/6); generalizability across sex and strain is untested.
- How hippocampal dysfunction associated with psychiatric disorders (schizophrenia, depression, anxiety) disrupts this specific SI mechanism is raised as a key open question but not investigated here.

---

### Connections & keywords

**Key citations**:
- Babayan et al. (2018) Nat Commun — belief state representation in dopamine system
- Starkweather et al. (2017) Nat Neurosci — dopamine RPEs reflect hidden-state inference
- Qu et al. (2023) bioRxiv — NAc dopamine reflects Bayesian inference during instrumental learning
- Schlagenhauf et al. (2014) Neuroimage — striatal dysfunction during reversal learning in schizophrenia
- Sanders, Wilson & Gershman (2020) eLife — hippocampal remapping as hidden state inference
- Wikenheiser & Schoenbaum (2016) Nat Rev Neurosci — cognitive maps in hippocampus and OFC
- Gershman & Uchida (2019) Nat Rev Neurosci — believing in dopamine
- Vertechi et al. (2020) Neuron — inference-based decisions in prefrontal cortex
- Komorowski et al. (2013) J Neurosci — ventral hippocampal neurons represent behaviorally relevant contexts
- Adams et al. (2015) J Neurology Neurosurg Psychiatry — computational psychiatry review

**Named models or frameworks**:
- State inference (SI) model / hidden state inference
- Q-learning (value updating / reinforcement learning)
- Bayesian hidden state inference / POMDP
- 2-armed bandit task (probabilistic serial reversal learning)
- dLight1.1 (dopamine sensor)
- GCaMP7f / Miniscope calcium imaging
- taCasp3 (caspase-based cell ablation)
- Cross-condition generalization performance (CCGP)

**Brain regions**:
- Ventral CA1 (vCA1)
- Nucleus accumbens core (NAc)
- Medial prefrontal cortex (mPFC)
- Orbitofrontal cortex (OFC)

**Keywords**: hidden state inference, latent context representation, ventral hippocampus CA1, probabilistic reversal learning, 2-armed bandit, Bayesian belief updating, reward prediction error, dopamine photometry, calcium imaging, state inference vs Q-learning, abstract context coding, hippocampal remapping

### Related wiki pages
- [[wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning|Orbitofrontal cortex as a cognitive map of task state for model-based reinforcement learning]]
- [[wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning|Task-state representation and hidden-state inference in orbitofrontal–hippocampal reinforcement learning]]
