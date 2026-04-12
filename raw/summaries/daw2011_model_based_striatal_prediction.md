---
source_file: daw2011_model_based_striatal_prediction.md
paper_id: daw2011_model_based_striatal_prediction
title: "Model-Based Influences on Humans' Choices and Striatal Prediction Errors"
authors:
  - "Nathaniel D. Daw"
  - "Samuel J. Gershman"
  - "Ben Seymour"
  - "Peter Dayan"
  - "Raymond J. Dolan"
year: 2011
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - human
methods:
  - fmri
  - computational_modeling
  - behavioral_analysis
brain_regions:
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - ventromedial_prefrontal_cortex
  - striatum
  - ventral_striatum
  - nucleus_accumbens
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - temporal_difference_learning
keywords:
  - model_based_reinforcement_learning
  - model_free_reinforcement_learning
  - reward_prediction_error
  - ventral_striatum
  - mesostriatal_dopamine
  - temporal_difference_learning
  - hybrid_rl
  - two_step_decision_task
  - fmri_bold
  - goal_directed_behaviour
  - habitual_behaviour
  - dual_system_decision_making
  - model
  - based
  - influences
  - humans
  - choices
  - striatal
  - prediction
  - errors
key_citations:
  - daw2005_uncertainty_prefrontal_striatal
---

### One-line summary

Ventral striatal BOLD signals previously assumed to reflect purely model-free reward prediction errors in fact encode a mixture of model-free and model-based valuations, in proportions that match the mixture governing subjects' actual choice behaviour.

---

### Background & motivation

The mesostriatal dopamine system is widely held to implement model-free temporal-difference (TD) reinforcement learning, with ventral striatal BOLD signals closely tracking TD reward prediction errors (RPEs). In parallel, behavioural and lesion evidence shows that humans and animals also use a separate model-based planning system that evaluates actions by prospective simulation of a learned internal model. The two systems were assumed to operate independently, with striatal RPEs being a clean readout of the model-free controller alone. This paper addresses the untested assumption of isolation: whether the striatal BOLD signal is indeed a pure model-free signal when both controllers are simultaneously active and their relative contributions can be quantified.

---

### Methods

- **Subjects**: 17 healthy adult humans scanned with fMRI (1.5T) while performing a sequential decision task.
- **Task**: A two-stage Markov decision task. On each trial subjects made a first-stage choice between two options; this led probabilistically (70% common / 30% rare) to one of two second-stage states, each requiring another binary choice that yielded monetary reward with a slowly drifting probability (Gaussian random walk, reflecting boundaries at 0.25 and 0.75). 201 trials per subject.
- **Behavioural analysis 1**: Hierarchical logistic regression predicting first-stage stay/switch from the previous trial's reward outcome, transition type (common vs. rare), and their interaction. Under pure model-free (TD) learning only a main effect of reward is expected; a significant interaction signals model-based influence.
- **Behavioural analysis 2**: Fit of a hybrid RL algorithm that learns action values via both model-based RL (Bellman equation) and model-free SARSA(λ) TD; choices driven by a weighted sum with free parameter w (model-based weight). Model comparison against TD-only, model-based-only, and restricted-λ variants using classical (LRT) and Bayesian methods including random-effects model comparison (Stephan et al., 2009).
- **fMRI analysis**: Two parametric regressors entered into a GLM: (1) the model-free RPE time series; (2) the difference between the model-based and model-free RPEs, which tests whether the BOLD signal contains residual model-based information beyond the model-free RPE. Conjunction analysis of the two regressors identified voxels reflecting a weighted mixture. A second-level covariate (per-subject behavioural w) tested whether individual differences in striatal model-based weighting correlated with behavioural model-based weighting.
- **Factorial BOLD analysis**: Independent analysis of anticipatory activity at trial onset in right nucleus accumbens as a function of the previous trial's reward and transition type, mirroring the behavioural factorial analysis.

---

### Key findings

- Behaviour showed significant main effects of reward (p < 1e-8) and a reward × transition-type interaction (p < 5e-5), rejecting a pure model-free account at the population level; ~10/17 subjects showed a positive interaction.
- The hybrid model was strongly preferred over TD-only, model-based-only, and restricted-λ special cases (Bayesian exceedance probability 92% for hybrid). Median model-free weight w = 61%, model-based weight = 39%; both differed significantly from 0 and 100%.
- Ventral striatum (bilateral) showed significant BOLD correlations with the model-free RPE regressor (p < 0.001, cluster-corrected), and also with the model-based difference regressor (right p < 0.005, left p < 0.05, cluster-corrected), with the conjunction surviving whole-brain correction on the right and small-volume correction on the left.
- Similar but weaker effects were found in vmPFC (conjunction survived only at a relaxed threshold).
- Across subjects, the neural estimate of model-based weighting in right ventral striatum correlated significantly with the behavioural estimate (r² = 0.28, p = 0.027), indicating the mixture proportions were consistent across the two measurement modalities.
- The independent factorial analysis of anticipatory striatal BOLD replicated the link: the reward × transition-type interaction in BOLD (per subject) correlated with behavioural model-based weight w (r² = 0.32, p = 0.017). The two neural model-based indices themselves correlated (r² = 0.37, p < 0.01).

---

### Computational framework

The paper uses **model-free and model-based reinforcement learning** as its primary framework.

- **Model-free (SARSA(λ) TD)**: Action values are updated retrospectively via RPEs. The eligibility parameter λ controls whether the second-stage estimated value or only the final reward reinforces the first-stage choice. RPEs are defined as δ = r + γV(s') − Q(s, a).
- **Model-based RL**: A learned transition model T(s'|s,a) combined with learned second-stage reward probabilities allows direct computation of first-stage action values via Bellman's equation, without TD chaining.
- **Hybrid**: First-stage action values are a weighted combination Q_net = w·Q_MB + (1−w)·Q_MF, with w a free parameter. Choices are softmax over Q_net. The framework yields distinct trial-by-trial RPE predictions for each strategy, enabling dissociation in both behaviour and BOLD.
- Key assumption: the mixing weight w is constant across trials within a subject. Model-based RPEs are defined to generate the fMRI difference regressor but do not directly drive model-based learning (which instead updates the model itself).

---

### Prevailing model of the system under study

Before this paper, the dominant view was that the brain contains two largely separate RL systems: (1) a model-free habit system implemented by the mesostriatal dopamine circuit, in which RPEs broadcast by dopaminergic neurons reinforce actions via TD learning; (2) a model-based goal-directed system, associated with prefrontal and hippocampal circuits, that evaluates actions prospectively using an internal task model. These systems were thought to compete for behavioural control (Daw et al., 2005) but to operate independently in the sense that the dopaminergic RPE signal was considered a pure product of the model-free system — reflecting only past reinforcement history and ignorant of task structure. The strong association between ventral striatal BOLD, dopamine, and TD RPEs was the principal evidence for this view. Model-based influences had previously been demonstrated in vmPFC (Hampton et al., 2006, 2008) but not in the striatal RPE signal itself.

---

### What this paper contributes

The paper provides the first direct evidence that the striatal BOLD signal — long treated as a read-out of purely model-free TD computation — in fact encodes a mixture of model-free and model-based valuations. Crucially, the mixture proportions in the neural signal match those governing the same subject's choice behaviour, arguing against an incidental contamination and supporting the conclusion that striatal RPE computations are genuinely influenced by model-based predictions. This challenges the clean two-system modularity in which each system's valuation signals are kept separate. The authors propose a possible reconciliation: a "model-based critic" architecture in which model-based RPEs are used to train a model-free actor — conceptually related to the Dyna algorithm and prioritised sweeping — which would preserve the overall parallel structure while explaining why striatal RPEs are not purely model-free. The paper also provides and validates the two-step Markov decision task as a tractable within-session tool for separating the two controllers in humans.

---

### Brain regions & systems

- **Ventral striatum (bilateral; nucleus accumbens / ventral putamen)** — primary locus of interest; shows both model-free and model-based RPE correlates, and whose model-based weighting correlates with the behavioural mixing weight across subjects.
- **Ventromedial prefrontal cortex (vmPFC / mPFC)** — secondary finding; also shows both model-free and model-based RPE correlates, though more weakly (conjunction required relaxed threshold). Identified as a candidate for model-based value signalling on prior grounds.
- **Mesostriatal dopamine system** — implicated via the BOLD signal; the paper notes that striatal BOLD likely conflates dopaminergic and other input signals, so the direct attribution to dopamine remains open.

---

### Mechanistic insight

This paper meets the bar: it formalises two distinct RL algorithms with different RPE predictions and provides fMRI data that distinguish them in the same voxels and correlate individual differences in the neural mixture with those in behaviour.

- **Computational**: The brain is solving sequential reward prediction under an unknown transition structure. Model-free TD solves this retrospectively by chaining RPEs; model-based planning solves it prospectively by simulating the transition model. The finding is that both algorithms contribute to ventral striatal RPE computation, contradicting a purely model-free account.
- **Algorithmic**: The BOLD signal in ventral striatum is best characterised as a weighted mixture of model-free and model-based RPEs (δ_net = (1−w)·δ_MF + w·δ_MB), where w is consistent with the same weight governing choice. The two-step task's transition structure (common vs. rare) provides the empirical handle to dissociate the algorithms' predictions.
- **Implementational**: The neural substrate is the ventral striatum (nucleus accumbens / ventral putamen). The BOLD signal likely reflects a combination of dopaminergic input and corticostriatal afferents, meaning the model-based contribution may arrive from model-based regions (e.g., prefrontal cortex) rather than from local dopaminergic computation. The paper notes this ambiguity explicitly and calls for dopamine unit recordings or voltammetry in an analogous animal task to resolve it.

---

### Limitations & open questions

- fMRI BOLD cannot attribute the model-based component of the striatal signal to dopamine specifically; it may arise from cortical input to striatum, leaving the cellular mechanism unresolved.
- The study was not designed to track the dynamic tradeoff between model-based and model-free systems across time or with varying cognitive load; the mixing weight w was treated as constant.
- The striatal signal lacked the dorsal/ventral dissociation predicted by rodent lesion literature (dorsolateral for habits, dorsomedial for goal-directed), possibly due to limited spatial resolution or because the manipulation did not differentially engage subregions.
- vmPFC results were weaker and did not survive whole-brain correction without threshold relaxation, leaving the role of that region ambiguous.
- The paper proposes a "model-based critic" hybrid architecture as a post-hoc interpretive framework but does not test it against the standard parallel-competition model.
- Sample size is small (n = 17); individual variability in mixing weight was substantial, raising questions about what factors determine the tradeoff.
- Whether the findings generalise beyond the specific two-step task structure (sequential, Markov, with instructed transition knowledge) remains to be established.

---

### Connections & keywords

**Key citations**:
- Daw, Niv & Dayan (2005) — prior computational framework for uncertainty-based model-based/model-free competition
- Glascher, Daw, Dayan & O'Doherty (2010) — companion study using a similar task focused on transition learning
- Schultz, Dayan & Montague (1997) — foundational paper linking dopamine to TD RPEs
- Dickinson (1985) — behavioural framework for habit vs. goal-directed distinction
- Balleine & O'Doherty (2010) — corticostriatal determinants of goal-directed and habitual action
- Hampton, Bossaerts & O'Doherty (2006, 2008) — model-based signals in vmPFC
- Sutton (1990); Moore & Atkeson (1993) — Dyna and prioritised sweeping algorithms

**Named models or frameworks**:
- SARSA(λ) — model-free TD algorithm used to fit and simulate behaviour
- Hybrid RL algorithm — weighted combination of model-based and model-free action values (Glascher et al., 2010 variant)
- Actor-critic model — referenced as the canonical neural instantiation of model-free TD
- Dyna — Sutton's architecture for offline model-based training of a model-free system
- Two-step Markov decision task — the experimental paradigm introduced/validated here

**Brain regions**:
- Ventral striatum (nucleus accumbens, ventral putamen)
- Ventromedial prefrontal cortex (vmPFC / mPFC)

**Keywords**:
- model-based reinforcement learning
- model-free reinforcement learning
- reward prediction error
- ventral striatum
- mesostriatal dopamine
- temporal difference learning
- hybrid RL
- two-step decision task
- fMRI BOLD
- goal-directed behaviour
- habitual behaviour
- dual-system decision-making
