---
source_file: daw2005_uncertainty_prefrontal_striatal.md
paper_id: daw2005_uncertainty_prefrontal_striatal
title: "Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control"
authors:
  - "Nathaniel D Daw"
  - "Yael Niv"
  - "Peter Dayan"
year: 2005
journal: "Nature Neuroscience"
paper_type: computational
contribution_type: theoretical
species:
  - rat
methods:
  - lesion
brain_regions:
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - infralimbic_cortex
  - striatum
  - dorsomedial_striatum
  - dorsolateral_striatum
  - amygdala
  - basolateral_amygdala
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - temporal_difference_learning
keywords:
  - model_based_reinforcement_learning
  - model_free_reinforcement_learning
  - habitual_control
  - goal_directed_control
  - outcome_devaluation
  - bayesian_arbitration
  - uncertainty_based_competition
  - dual_controller_architecture
  - corticostriatal_systems
  - temporal_difference_learning
  - prefrontal_striatal_competition
  - instrumental_conditioning
  - uncertainty
  - based
  - competition
  - between
  - prefrontal
  - dorsolateral
  - striatal
  - systems
key_citations:
  - coutureau2003_infralimbic_prefrontal_goal
---

### One-line summary

A normative Bayesian reinforcement learning framework proposes that the brain arbitrates between a model-based (prefrontal) tree-search controller and a model-free (dorsolateral striatal) caching controller according to the relative uncertainty of each system's value estimates.

---

### Background & motivation

The brain is thought to contain at least two parallel action-selection systems: one associated with prefrontal cortex (flexible, "goal-directed") and one with dorsolateral striatum (habitual, inflexible). Behavioral evidence from outcome devaluation experiments demonstrates that neither system always dominates — control shifts depending on factors like amount of training, task complexity, and action-reward proximity. Prior to this paper, there was no principled account of *why* the brain uses multiple controllers or *how* it should arbitrate between them when they disagree. This paper fills that normative gap by framing the competition in terms of reinforcement learning theory and Bayesian uncertainty.

---

### Methods

- **Model architecture**: two parallel reinforcement learning systems, each computing state-action value functions Q(s,a) in a Markov decision process (MDP) framework.
  - *Cache system* (dorsolateral striatum): Bayesian Q-learning — stores scalar value distributions and updates via temporal-difference bootstrapping; computationally cheap but inflexible to outcome changes.
  - *Tree-search system* (prefrontal cortex): Bayesian model-based value iteration — estimates transition and reward functions and derives values by iterating over the estimated tree; flexible but subject to computational noise accumulating with tree depth.
- **Uncertainty tracking**: each system maintains posterior variance over its Q-estimates; the system with lower variance controls action selection at each state-action pair.
- **Action selection**: softmax over the winning system's mean Q-estimate.
- **Devaluation modelling**: outcome devaluation implemented by replacing the terminal-state reward distribution; affects the tree system's computed values immediately but not the cache's stored scalars absent new direct experience.
- **Simulations**: run on stylised MDPs matching rat instrumental conditioning tasks (one action/one outcome, two actions/two outcomes); 250–1,000 simulation runs per condition.
- **Validation approach**: qualitative match to published rodent devaluation datasets (Adams 1982; Colwill & Rescorla 1985; Holland 2004; Killcross & Coutureau 2003), not quantitative curve-fitting.

---

### Key findings

- The tree-search (prefrontal/model-based) system is more data-efficient early in training: each experience immediately propagates to update value estimates across all states, so it achieves lower uncertainty first.
- With extended training, the caching system asymptotically wins for actions *distal* from reward (e.g., lever press in a two-step chain), because each additional tree-search step incurs computational noise that accumulates; the cache suffers no such cost.
- For actions *proximal* to reward (magazine entry), the tree system retains its uncertainty advantage even asymptotically, predicting persistent devaluation sensitivity — consistent with experimental data.
- With *two* actions and *two* outcomes, experience is spread over more state-action pairs, keeping data scarce; this preserves the tree system's early advantage even for distal actions, predicting sustained goal-directed control — consistent with Colwill & Rescorla (1985).
- The framework thus unifies the following empirical observations under a single principle (lowest uncertainty controls): (i) over-training produces habitual control, (ii) task complexity restores goal-directed control, (iii) proximity to reward preserves goal-directed control.
- Lesion patterns (dorsolateral striatum impairs habitisation; prelimbic cortex, dorsomedial striatum, basolateral amygdala, insular cortex impair goal-directed control) are consistent with the two-system architecture assumed.

---

### Computational framework

**Bayesian reinforcement learning / model-based vs. model-free RL**.

- *What is being modelled*: value learning in a discrete-state, discrete-action, absorbing Markov decision process; the agent must learn state-action values Q(s,a) (expected probability of eventual reward) from noisy experience in a potentially non-stationary environment.
- *Key variables*: posterior distributions over Q(s,a) for both systems (parameterised as beta distributions); posterior distributions over transition function T(s,a,s') and reward function R(s) for the tree system (Dirichlet and beta respectively); variance (posterior uncertainty) as the arbitration signal.
- *Cache system*: Bayesian Q-learning (Dearden et al. 1998) with bootstrapped mean-variance updates; nonstationarity handled by exponential decay of sufficient statistics toward prior.
- *Tree system*: Bayesian value iteration — iterates moment equations forward through the tree; each depth step adds a fixed computational noise variance ν × P(successor is nonterminal).
- *Arbitration rule*: hard winner-take-all on posterior variance; the system with smaller variance provides the Q-estimate used for softmax action selection.
- *Key assumption*: the two systems use matched priors and matched forgetting rates, so relative uncertainty differences reflect genuine differences in data efficiency and computational cost rather than parametric advantages.

---

### Prevailing model of the system under study

The introduction frames the prior understanding as follows: (i) dorsolateral striatum and its dopaminergic afferents support *habitual* (stimulus-response, outcome-insensitive) control; (ii) prefrontal cortex (and associated medial striatal areas) supports *cognitive*, *goal-directed* (outcome-sensitive) control. This dissociation was supported by electrophysiology, fMRI, and lesion studies, and had been elaborated descriptively in animal-conditioning theory (Dickinson & Balleine's dual-process account). However, the field lacked a normative explanation for why this division of labour exists and how arbitration should work — existing theories either replaced one system with the other or blended them without principled competition.

---

### What this paper contributes

The paper provides the first normative, computational account of why two controllers coexist and how they compete. Specifically:
- It identifies a fundamental trade-off: model-free caching is computationally cheap but data-inefficient and inflexible; model-based tree search is data-efficient but computationally costly for deep trees.
- It proposes a Bayesian principle — arbitrate by uncertainty — that predicts which system dominates under which conditions, deriving the known empirical regularities (training, complexity, proximity) as consequences of a single mechanism.
- It recasts habitual control not as irrational or impulsive interference with rational goal-directed control, but as a rational approximation strategy well-suited to specific task conditions.
- It predicts that dorsomedial striatum may be part of the tree-search circuit (not purely prefrontal), and that the competition is better framed as dorsomedial vs. dorsolateral corticostriatal loops.
- It generates novel experimental predictions: e.g., the need for "incentive learning" (re-exposure to devalued outcome) should disappear in animals with caching-system lesions, because the tree system will then dominate regardless.

---

### Brain regions & systems

- **Dorsolateral striatum** — proposed substrate for the caching (model-free, habitual) controller; lesions disrupt habit formation and prevent the over-training transition to habitual control.
- **Prefrontal cortex (prelimbic area in rat)** — proposed substrate for the tree-search (model-based, goal-directed) controller; lesions eliminate devaluation sensitivity even for moderately trained behaviours.
- **Dorsomedial striatum** — implicated as part of the tree-search (prefrontal-associated) circuit, not the habit system; lesions impair goal-directed control.
- **Basolateral amygdala** — lesions eliminate devaluation sensitivity, implicating it in the tree-search network.
- **Gustatory insular cortex** — similarly implicated in goal-directed control via lesion evidence.
- **Orbitofrontal cortex** (monkey) — lesions disrupt outcome-sensitive choice, consistent with tree-search involvement.
- **Infralimbic cortex (IL)** — proposed as a candidate arbitration region; lesions of IL reinstate goal-directed from previously habitual control.
- **Anterior cingulate cortex (ACC)** — proposed candidate for arbitration via error/conflict monitoring.
- **Dopaminergic afferents to striatum** — hypothesised to support caching-system learning (TD-like prediction errors); role in tree-search system unresolved.

---

### Mechanistic insight

The paper meets criterion 1 (formalises an algorithm) but not criterion 2 (does not present new neural recordings or direct neural measurements linking the model's arbitration variable — relative uncertainty — to measured neural activity). The study is a purely computational/theoretical one validated against published behavioural lesion data. It therefore does not meet the bar for a full Marr-level mechanistic account.

The model articulates a computational-level problem (efficient value learning in non-stationary MDPs) and an algorithmic-level solution (Bayesian uncertainty-based arbitration between model-free and model-based RL), but the implementational level — how posterior variance is computed and compared in neural circuits, and which specific cell types or neuromodulators carry the arbitration signal — is not resolved. The paper speculatively names cholinergic/noradrenergic neuromodulation and the IL/ACC as candidates, but without supporting neural data.

---

### Limitations & open questions

- The model uses hard winner-take-all arbitration; the paper notes that softer certainty-weighted averaging is also possible but is not explored.
- Uncertainty estimates rely on matched approximations across both systems — the absolute numerical values of uncertainty are likely inaccurate; the authors rely on relative comparisons being informative.
- The computational noise parameter ν (penalising tree depth) is chosen arbitrarily; it represents a real cost but is not independently motivated or measured.
- Nonstationarity is modelled via exponential forgetting toward priors, which is a heuristic rather than a principled generative model of change.
- The account is qualitative: simulations reproduce directional effects without quantitative fitting to data.
- The neural substrate for uncertainty-based arbitration is entirely speculative; no neural recordings test the specific prediction that arbitration tracks relative posterior variance.
- The paper assumes strict separation between systems for tractability, explicitly acknowledging that their neural substrates are intertwined (corticostriatal loops) and that learning interactions between systems are important but not modelled.
- The framework does not address Pavlovian influences, temporal discounting, or risk, all of which modulate habitual/goal-directed balance.
- Predictions about incentive learning and lesion interactions remain untested at the time of publication.

---

### Connections & keywords

**Key citations**:
- Dickinson & Balleine (2002) — dual-process animal learning theory foundational to the behavioural framing
- Sutton & Barto (1998) — RL: An Introduction; formal RL framework
- Schultz, Dayan & Montague (1997) — dopamine and TD learning
- Dearden, Friedman & Russell (1998) — Bayesian Q-learning (cache system implementation)
- Mannor et al. (2004) — Bayesian value iteration (tree-search implementation)
- Yin, Knowlton & Balleine (2004, 2005) — dorsolateral and dorsomedial striatum lesion studies
- Killcross & Coutureau (2003); Coutureau & Killcross (2003) — prelimbic cortex lesions and goal-directed control
- Colwill & Rescorla (1985) — task complexity and devaluation sensitivity
- Adams (1982) — over-training and devaluation insensitivity
- Pasupathy & Miller (2005) — striatal/prefrontal recordings during reversal learning

**Named models or frameworks**:
- Model-free / model-based reinforcement learning (Daw et al. dual-controller framework)
- Bayesian Q-learning (Dearden et al.)
- Bayesian value iteration / tree search
- Absorbing Markov decision process (MDP)
- Outcome devaluation / reinforcer devaluation paradigm
- Habitual vs. goal-directed control (dual-process conditioning theory)

**Brain regions**:
- Dorsolateral striatum
- Prefrontal cortex (prelimbic area)
- Dorsomedial striatum
- Basolateral amygdala
- Gustatory insular cortex
- Orbitofrontal cortex
- Infralimbic cortex
- Anterior cingulate cortex
- Dopaminergic afferents / nigrostriatal pathway

**Keywords**:
- model-based reinforcement learning
- model-free reinforcement learning
- habitual control
- goal-directed control
- outcome devaluation
- Bayesian arbitration
- uncertainty-based competition
- dual-controller architecture
- corticostriatal systems
- temporal-difference learning
- prefrontal-striatal competition
- instrumental conditioning
