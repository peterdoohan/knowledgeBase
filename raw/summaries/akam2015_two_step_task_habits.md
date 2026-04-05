---
source_file: akam2015_two_step_task_habits.md
title: Simple Plans or Sophisticated Habits? State, Transition and Learning Interactions in the Two-Step Task
authors: Thomas Akam, Rui Costa, Peter Dayan
year: 2015
journal: PLoS Computational Biology
paper_type: computational
contribution_type: methodological
---

### One-line summary

Model-free reinforcement learning agents using extended state representations can produce behaviour on the two-step task that is indistinguishable from model-based planning under standard analyses, challenging the task's ability to cleanly dissociate these strategies.

---

### Background & motivation

The two-step task was developed to dissociate model-based (planning) from model-free (habitual) reinforcement learning in behavioural experiments, including in humans and increasingly in animal subjects. The standard analysis — examining how transition type (common/rare) and reward interact to predict stay probability — was assumed to cleanly separate agents that use a predictive world model from those that do not. However, the authors noticed that modifications to the task structure required for animal work (increasing the contrast between good and bad options) might introduce statistical confounds. This paper formalises and analyses those confounds to determine what can and cannot be validly inferred from two-step task performance.

---

### Methods

- Simulation study — no animal or human subjects; all analyses conducted on simulated data in Python
- Compared five agent types: Q(1) model-free, Q(0) model-free, model-based, reward-as-cue, and latent-state
- Two task variants: original two-step task (70/30 common/rare transitions, drifting reward probabilities) and a reduced task (80/20 transitions, block-based reward probabilities, no second-step choice)
- Analyses: stay probability plots, logistic regression (standard and extended with 'correct' predictor), lagged logistic regression (multi-trial effects), and maximum likelihood model comparison
- 10 sessions × 10,000 trials per agent; parameters either optimised for reward or fitted to model-based agent behaviour for fair comparison

---

### Key findings

- On the **reduced task**, a pure Q(1) model-free agent showed a spurious transition-outcome interaction in stay probability — the classical signature of model-based behaviour — due to correlations between action values at trial onset and subsequent trial events
- This confound is absent in the original task because higher stochasticity decorrelates trial-start action values from subsequent events; the effect is very weak (P = 0.01) in the original task
- Including a 'correct' predictor in logistic regression (repeat the choice that was correct on the previous trial) eliminates the spurious interaction for Q(1) agents and is validated as an effective correction
- The **reward-as-cue** agent (model-free RL over 4 states defined by previous outcome × second-step state) learns a fixed stimulus-response mapping that produces a strong transition-outcome interaction — indistinguishable from model-based by one-trial-back analysis; detectable only by lagged regression showing no multi-trial integration
- The **latent-state** agent (Bayesian inference over two latent world states + fixed state-action mapping) produces behaviour qualitatively identical to a model-based agent on both stay probability and lagged logistic regression analyses
- Latent-state and model-based agents could only be discriminated by maximum likelihood model comparison on large datasets; differences are highly significant (P < 10⁻⁵) but small
- Both extended-state agents outperform classical model-free strategies in reward obtained, providing an incentive for their acquisition with extended training

---

### Computational framework

Reinforcement learning (RL), specifically the model-based vs. model-free distinction within the framework of Sutton & Barto-style temporal difference learning.

Key formalisms:
- **Q(λ) agents**: action value updated via prediction error weighted by eligibility trace λ; λ=1 gives Q(1) (outcome-driven), λ=0 gives Q(0) (second-step value propagation)
- **Model-based agent**: first-step action values computed prospectively as weighted sum of second-step state values using known transition probabilities P(sj|ai)
- **Latent-state agent**: Bayesian update over a discrete two-state world model; asymptotic fixed mapping from inferred latent state to action
- All agents use softmax decision rule with inverse temperature T
- The paper also connects to the **successor representation** as a related middle-ground between MB and MF strategies

---

### Prevailing model of the system under study

The introduction frames the field as operating under a two-system view: model-based RL (goal-directed, computationally costly, flexible) and model-free RL (habitual, computationally cheap, inflexible). These were assumed to be empirically dissociable using the two-step task's transition-outcome interaction on stay probability. The field further assumed that this interaction was a reliable indicator of prospective action evaluation — i.e., that subjects using transition information must be using a forward model. The task was being widely adopted in human neuroscience and was being adapted for animal use on the implicit assumption that the standard analysis remained valid across task variants.

---

### What this paper contributes

The paper shows that the two-system dissociation the two-step task was designed to provide is more fragile than assumed. Specifically:

1. The stay probability signature of model-based behaviour can arise from purely model-free agents when task structure induces correlations between trial-start action values and subsequent trial events — a statistical confound, not a strategic one. A corrected regression analysis is validated.

2. More fundamentally, agents that learn extended state representations (reward-as-cue, latent-state) can approximate or match model-based performance and produce model-based behavioural signatures without performing prospective planning. These strategies sit on a spectrum between MB and MF, rendering the binary classification inadequate.

The practical implication is that animal studies using modified task variants, and overtrained human subjects, may be misclassified. The paper repositions the MB/MF distinction as a spectrum rather than a binary, and foregrounds state representation learning as a key variable the task does not currently measure.

---

### Brain regions & systems

Not applicable in the direct sense — this is a purely computational/simulation study with no neural data. However, the discussion explicitly connects latent-state and reward-as-cue strategies to **cortico-basal ganglia loops**, particularly associative and limbic striatal sub-regions, as candidate implementations of model-free RL applied to higher-level state representations. The distinction between goal-directed and habitual control is linked throughout to prior lesion literature implicating **dorsomedial striatum** (model-based) and **dorsolateral striatum** (model-free), though this is background framing rather than a contribution of the paper.

---

### Mechanistic insight

Not applicable. The paper is a simulation study and presents no neural data. It proposes and analyses algorithms but does not provide empirical evidence linking any specific algorithm to neural activity. The paper explicitly acknowledges (Discussion) that neural data would be needed to disambiguate latent-state from model-based strategies in experimental subjects.

---

### Limitations & open questions

- All conclusions are based on simulated agents; no human or animal behavioural data are analysed
- The latent-state agent uses asymptotic fixed mappings — the learning process by which animals would acquire this strategy is not modelled
- Model comparison can discriminate latent-state from model-based agents but requires large datasets unlikely to be available in typical experiments
- The paper does not propose a modified task design that definitively rules out extended-state strategies (though transition matrix reversals are suggested as a partial solution)
- Whether extended-state strategies actually explain apparently model-based behaviour in published human or animal data remains an open empirical question

---

### Connections & keywords

**Key citations**: Daw et al. 2011 (original two-step task), Wunderlich et al., Otto et al. (human two-step literature), Killcross & Coutureau / Balleine & Dickinson (goal-directed vs. habitual lesion literature)

**Named models/frameworks**: Q(λ) temporal difference learning, model-based RL, model-free RL, successor representation, latent-state inference, hierarchical RL (options framework), softmax decision rule, logistic regression stay probability analysis

**Brain regions**: dorsomedial striatum, dorsolateral striatum, cortico-basal ganglia loops (background context only)

**Keywords**: two-step task, model-based reinforcement learning, model-free reinforcement learning, habitual control, goal-directed control, latent state inference, stay probability, extended state representation, reward-as-cue, behavioural dissociation, transition-outcome interaction, successor representation
