---
source_file: keramati2016_plan_until_habit.md
paper_id: keramati2016_plan_until_habit
title: "Adaptive integration of habits into depth-limited planning defines a habitual-goal directed spectrum"
authors:
  - "Mehdi Keramati"
  - "Peter Smittenaar"
  - "Raymond J. Dolan"
  - "Peter Dayan"
year: 2016
journal: "Proceedings of the National Academy of Sciences (PNAS)"
paper_type: empirical
contribution_type: theoretical
species:
  - human
tasks:
  - two_step_task
methods:
  - behavioral_analysis
brain_regions:
  - prefrontal_cortex
  - striatum
  - dorsomedial_striatum
  - amygdala
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
keywords:
  - plan_until_habit
  - depth_limited_planning
  - model_based_reinforcement_learning
  - model_free_reinforcement_learning
  - habitual_decision_making
  - goal_directed_decision_making
  - speed_accuracy_trade_off
  - cognitive_resource_constraints
  - stay_probability_analysis
  - markov_decision_process
  - hybrid_rl_models
  - decision_making_spectrum
  - adaptive
  - integration
  - habits
  - depth
  - limited
  - planning
  - defines
  - habitual
key_citations:
  - daw2011_model_based_striatal_prediction
---

### One-line summary

Humans integrate cached habitual values directly into forward planning at variable depths, forming a "plan-until-habit" spectrum between purely habitual and purely goal-directed control that is modulated by available cognitive resources (time pressure).

---

### Background & motivation

Behavioral and neural research has established two broad decision-making systems: a goal-directed system that simulates future consequences via a mental model, and a habitual system that caches previously experienced values. Prior accounts mostly framed these systems as competing for control, with the more competent system winning in a given context. This paper fills the gap by asking whether individuals can normatively integrate the two systems — using forward planning up to some depth k, then switching to habitual values for the remainder of the tree — and whether this depth is modulated by available cognitive resources such as time.

---

### Methods

- **Task design**: A novel three-stage Markov decision task adapted from the Daw et al. (2011) two-step paradigm but extended to three decision stages, allowing depths of planning k = 0 (pure habitual), k = 1 (plan-until-habit), or k = 2 (pure planning). Reward was located deterministically in one of four terminal states at any given time and hopped randomly across states according to a discretised normal distribution.
- **Subject population**: 30 human subjects (17 female, 13 male), London-based university students aged 20–30 years, randomly split into two groups of 15.
- **Manipulation**: High-resource group had 2,000 ms per decision stage; low-resource group had 700 ms per stage (time pressure).
- **Key measurements**: Stay-probability profiles across 8 trial categories (defined by common/rare first- and second-stage transitions crossed with reward/no-reward outcome) as a model-agnostic behavioural signature distinguishing the three strategies.
- **Analysis approach**: (1) Nonparametric Wilcoxon signed-rank tests on model-agnostic stay-probability contrasts; (2) Mann-Whitney U tests for between-group comparisons; (3) Mixed-effect lagged logistic regression; (4) Hierarchical Bayesian model fitting with expectation-maximisation to fit hybrid models combining the three strategies, using integrated Bayesian information criterion (iBIC) for model selection.

---

### Key findings

- Both high- and low-resource groups showed significant pure planning effects after rewarded and unrewarded trials (P < 0.001).
- The plan-until-habit strategy was significantly stronger in the low-resource group than in the high-resource group after rewarded trials (P = 0.034), consistent with time pressure reducing planning depth.
- Model fitting confirmed that both groups were best described by a mixture of pure planning and plan-until-habit strategies (not pure habitual); the weight of the plan-until-habit component was significantly larger in the low-resource group (permutation test, P < 0.01).
- Within subjects, reliance on plan-until-habit at stage 1 correlated strongly with reliance on pure habit at stage 2 across both groups, indicating a stable individual trait in planning depth.
- The habitual weight at the second stage was 0.37 ± 0.18 (high-resource) vs 0.59 ± 0.23 (low-resource), replicating the resource-dependent shift.

---

### Computational framework

The paper uses a **reinforcement learning / Markov decision process (MDP)** framework, specifically a hybrid of model-free (MF) and model-based (MB) RL.

- **MF (habitual) system**: Q-learning with temporal difference updates; Q-values cache prior experience via reward prediction errors. Does not build a model of state transitions.
- **MB (planning) system**: Learns the reward and transition functions of the MDP and uses recursive value iteration (tree expansion) to compute Q-values.
- **Plan-until-habit**: A novel integrative algorithm that performs depth-k forward simulation using the MB system, then substitutes MF cached values Q_habit(s', a') at depth k rather than continuing the tree. Depth k is a free parameter representing cognitive resource use. Formally: Q(s, a) = sum of first-k discounted MB rewards + gamma^k * Q_habit(s_k, a_k).
- Key assumption: the depth k is a covert internal decision influenced by resource availability (time, working memory). Changing k interpolates continuously between pure habitual (k=0) and pure planning (k→∞).

---

### Prevailing model of the system under study

Prior to this paper, the field conceptualised habitual and goal-directed control as two competing systems, with arbitration mechanisms determining which system gains behavioural control based on their relative competencies (uncertainty, stress, working memory load, etc.). The dominant framework (Daw, Niv & Dayan 2005; Daw et al. 2011) modelled the two systems as running in parallel, with a weighted average or a winner-takes-more competition at the output stage. This implied a discrete or smoothly weighted blend, but not a principled integration of one system's outputs into the other's computations. The paper's introduction explicitly positions this "competition" framing as the baseline it is moving beyond.

---

### What this paper contributes

The paper shows that rather than simply blending or competing, the two systems are integrated structurally: habitual values are inserted as leaf-node estimates within forward planning trees, enabling a normatively rational depth-of-planning strategy. This reframes the habitual/goal-directed distinction from a binary or continuous weight into a spectrum parameterised by planning depth. The finding that time pressure shifts depth (not just the competition weight) gives a mechanistic account of how resource constraints alter decision strategy. The correlation between planning depth across task stages within individuals points to a stable cognitive trait. Clinically, the framework suggests that psychiatric conditions involving habit/goal-directed imbalances (addiction, OCD) may be better characterised by planning depth profiles than binary system dominance.

---

### Brain regions & systems

The paper is primarily a computational/behavioural study; it does not collect neural data. Brain regions are mentioned in the Discussion as targets for future investigation:

- **Cortico-amygdala-striatal circuits** — referenced as the likely neural substrate of the interplay between habitual and goal-directed control of external actions, and as a candidate system for investigating the "metacontrolling" operations described by the plan-until-habit model.
- **Prefrontal cortex** — implicated by prior literature (Smittenaar et al. 2013) in model-based planning; referenced as a potential site modulated by time pressure.
- **Dorsolateral and dorsomedial striatum** — referenced from prior work (Yin et al. 2004, 2005) as substrates of habitual vs. goal-directed control.

The paper itself does not map its novel algorithmic construct onto specific brain regions.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined here. It proposes a novel RL algorithm (plan-until-habit) and provides human behavioural data that fit the model, including model comparison across competing hybrid strategies. However, it does not present neural data (recordings, imaging, lesion, pharmacology) linking the model's specific variables (depth parameter k, the point at which habitual Q-values are substituted, or associated prediction error signals) to measured neural activity. The paper is best characterised as establishing a behavioural and computational signature of an intermediate planning strategy, leaving neural implementation as explicitly stated future work.

---

### Limitations & open questions

- The study uses only 15 subjects per group, limiting statistical power for detecting fine-grained individual differences and between-group effects (the plan-until-habit effect after unrewarded trials did not significantly differ between groups, P = 0.9).
- The task constrains planning depth to integer values 0, 1, or 2 by design; this does not rule out richer, non-integer or tree-heterogeneous depth strategies in more complex environments.
- No neural data: the mapping of the plan-until-habit algorithm onto specific brain circuits (cortico-striatal, prefrontal, amygdala) is speculative.
- The model assumes habitual values are computed by standard Q-learning; more exotic forms of habit (e.g. chunked action sequences, Dezfouli & Balleine 2012) are not tested.
- Depth is modelled as uniform across all branches of the tree; depth could in principle vary across branches (e.g. pruning as in Huys et al. 2012).
- Generalisability of the 700 ms vs. 2000 ms manipulation to naturalistic time pressure is unclear.
- The paper raises but does not address the neural substrates of "metacontrol" — i.e. how the brain selects depth k.

---

### Connections & keywords

**Key citations**:
- Daw, Niv & Dayan (2005) — uncertainty-based arbitration between prefrontal and striatal systems
- Daw, Gershman, Seymour, Dayan & Dolan (2011) — model-based influences on choices and striatal prediction errors (two-step task)
- Sutton & Barto (1998) — Reinforcement Learning: An Introduction
- Keramati, Dezfouli & Piray (2011) — speed/accuracy trade-off between habitual and goal-directed processes
- Huys et al. (2012) — tree pruning by Pavlovian system (bonsai trees)
- Cushman & Morris (2015) — habitual control of goal selection

**Named models or frameworks**:
- Plan-until-habit model (novel, introduced here)
- Model-based reinforcement learning (MB-RL)
- Model-free reinforcement learning (MF-RL / Q-learning)
- Two-step task (Daw et al. 2011 paradigm, extended to three stages)
- Hierarchical Bayesian model fitting with expectation-maximisation

**Brain regions**:
- Prefrontal cortex (mentioned from prior literature)
- Dorsolateral striatum (referenced)
- Dorsomedial striatum (referenced)
- Cortico-amygdala-striatal circuits (referenced as future target)

**Keywords**:
- plan-until-habit
- depth-limited planning
- model-based reinforcement learning
- model-free reinforcement learning
- habitual decision-making
- goal-directed decision-making
- speed-accuracy trade-off
- cognitive resource constraints
- stay-probability analysis
- Markov decision process
- hybrid RL models
- decision-making spectrum
