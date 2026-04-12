---
source_file: bogacz2020_dopamine_action_inference.md
paper_id: bogacz2020_dopamine_action_inference
title: "Dopamine role in learning and action inference"
authors:
  - "Rafal Bogacz"
year: 2020
journal: eLife
paper_type: computational
contribution_type: theoretical
tasks:
  - probabilistic_reversal_learning
brain_regions:
  - striatum
  - dorsomedial_striatum
  - dorsolateral_striatum
  - ventral_striatum
  - nucleus_accumbens
  - ventral_tegmental_area
  - substantia_nigra
  - thalamus
frameworks:
  - reinforcement_learning
  - active_inference
  - bayesian_inference
  - temporal_difference_learning
keywords:
  - dopamine_prediction_error_heterogeneity
  - goal_directed_vs_habitual_action_control
  - free_energy_minimisation
  - bayesian_action_inference
  - basal_ganglia_circuit_model
  - cortico_striatal_plasticity
  - action_planning_and_movement_initiation
  - habit_formation_mechanisms
  - reward_prediction_error
  - parkinsons_disease_dopamine_depletion
  - probabilistic_reversal_learning
  - uncertainty_based_arbitration
  - dopamine
  - role
  - learning
  - action
  - inference
key_citations:
  - schultz1997_neural_substrate_reward_pred
  - miller2019_retrosplenial_spatial_learning
  - haber2000_striatonigrostriatal_pathways
  - montague1996_predictive_hebbian_dopamine
  - daw2005_uncertainty_prefrontal_striatal
wiki_pages:
  - wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning
---

### One-line summary

A unified computational framework (DopAct) proposes that dopaminergic neurons in distinct striatal loops encode separate prediction errors — reward-based for goal-directed systems and action-deviation-based for the habit system — that simultaneously drive both learning and action planning via free-energy minimisation.

---

### Background & motivation

Dopamine's role in reward prediction error and reinforcement learning is well established, but this classical account cannot explain why dopamine depletion impairs voluntary movement initiation (as in Parkinson's disease) while leaving some habitual responses intact. Additionally, the observed diversity of dopaminergic responses — with some neurons responding to rewards and others to movements — is unexplained by a single uniform reward prediction error signal. This paper seeks a unified framework that reconciles dopamine's roles in learning, habit formation, and action planning within a single computational account grounded in known basal ganglia anatomy.

---

### Methods

- **Model architecture**: Three interacting systems — valuation, goal-directed, and habit — are mapped onto a spectrum of cortico-basal ganglia loops (ventral to dorsolateral striatum).
- **Computational framework**: Action selection is formalised as Bayesian inference: the goal-directed system provides a likelihood over actions given desired reward; the habit system provides a prior. The posterior is maximised via gradient ascent on a free-energy objective function F.
- **Algorithm derivation**: Differential equations for action planning and parameter learning are derived analytically as derivatives of F. Both processes are shown to minimise the same prediction-error-based objective.
- **Network implementation**: The algorithm is mapped onto anatomically plausible basal ganglia circuitry, using known connectivity (cortico-striatal weights, dopaminergic projections, ascending spiral structure of Haber et al. 2000, output nuclei, thalamus).
- **Simulations**: Two tasks are simulated: (1) selection of action intensity with Gaussian likelihood and prior, including devaluation and Pavlovian-instrumental transfer paradigms; (2) probabilistic reversal learning with binary choice between two actions.
- **Validation**: Simulation outputs are compared qualitatively and quantitatively to published experimental data (Dickinson et al. 1995, Estes 1943, Howe & Dombeck 2016, Choi et al. 2005, Jin & Costa 2010, Hardwick et al. 2019).

---

### Key findings

- Both learning and action planning can be described as minimisation of the same objective (negative free energy / sum of squared prediction errors), unifying them under a single computational principle.
- Dopaminergic neurons in the goal-directed system encode reward prediction errors; in the habit system they encode deviations of the chosen action from the habitual action — not reward errors. This predicts distinct dopaminergic subpopulations mapped onto VTA (reward prediction error) and SNc (movement/habit prediction error).
- Dopamine in the goal-directed system plays an active role in action planning by modulating striatal excitability until a motor plan sufficiently accounts for the available reward (prediction error reaches zero). Habit system execution does not require this dopaminergic facilitation.
- Simulations reproduce: (a) resistance to devaluation with extended training; (b) Pavlovian-instrumental transfer; (c) reversal-learning competition between goal-directed and habit systems; (d) impaired goal-directed but not habitual responding after simulated dopamine depletion.
- The model predicts that SNc dopaminergic neurons should show elevated activity for non-habitual movements (at task onset and after reversal), distinguishing the DopAct account from the Daw et al. 2005 model which expects reward prediction errors in dorsolateral striatal dopamine.
- Uncertainty (variance) in each system determines the relative weighting of goal-directed vs. habit contributions to action selection, with the habit system gaining control as its uncertainty decreases with extended training.

---

### Computational framework

**Active inference / free-energy minimisation combined with Bayesian action inference.**

The core formalism treats action selection as posterior inference: given a desired reward R (set by the valuation system based on physiological reserve levels) and a state s, the actor selects the action a that maximises P(a|R,s). This posterior is computed from a goal-directed likelihood P(R|a,s) and a habit prior P(a|s) via Bayes' theorem.

An objective function F = log[P(R|a,s) · P(a|s)] (equivalent to negative free energy / a lower bound on log P(R|s)) is defined. Action planning proceeds by gradient ascent on F over a (da/dt ∝ ∂F/∂a); learning proceeds by gradient ascent over synaptic weight parameters. Both processes thus minimise prediction errors in the goal-directed and habit systems simultaneously.

Key variables: action intensity a, desired reward R, state s, goal-directed parameters Q (reward-action mapping), habit parameters H (action-state mapping), variance parameters Σ_g and Σ_h (system uncertainties). Prediction errors δ_g (reward prediction error in goal-directed system) and δ_h (action prediction error in habit system) are computed locally by dopaminergic neurons and modulate plasticity and excitability of corresponding striatal populations.

Key assumptions: Gaussian probability densities; mean reward proportional to product of action intensity and stimulus intensity; cortico-striatal weights encode distribution parameters; dopaminergic neurons can compute prediction errors from locally available signals.

---

### Prevailing model of the system under study

The paper's introduction positions itself against the classical reinforcement learning account of dopamine (Schultz et al. 1997; Montague et al. 1996; Houk et al. 1995), in which all dopaminergic neurons uniformly encode a single reward prediction error (RPE) signal that drives striatal synaptic plasticity. In this classical view, dopamine is a teaching signal for learning expected reward values and action policies, but has no specific role in action planning or movement initiation — leaving the movement-related dopaminergic responses and the motor deficits of Parkinson's disease unexplained.

A competing account (Daw et al. 2005) proposes that goal-directed behaviour arises from a cortical model-based system and habitual behaviour from a model-free striatal system learning via standard reward RPEs, with uncertainty arbitrating between them. The paper also notes the active inference account (Friston 2010) as a high-level principle and a prior model of habit formation (Miller et al. 2019) as a partial predecessor that proposes action-based prediction errors in the habit system, though without network implementation or integration with dopamine.

---

### What this paper contributes

The DopAct framework makes three concrete advances over prevailing models:

1. **Unification of learning and action planning**: It shows, at the algorithmic level, that both processes are gradient steps on the same free-energy objective, providing a principled reason why dopaminergic RPE neurons should be involved in motor planning.

2. **Functional heterogeneity of dopaminergic populations**: It assigns distinct computational roles to dopaminergic neurons in different striatal loops — reward RPEs (VTA/ventral dopamine) for valuation and goal-directed systems, action prediction errors (SNc/dorsal dopamine) for the habit system. This directly contradicts the Daw et al. 2005 prediction that dorsolateral striatal dopamine should carry reward RPEs to support habit formation, and is consistent with empirical evidence that SNc neurons respond to movements rather than rewards.

3. **Network implementation of probabilistic action inference**: It translates the Bayesian action-selection framework of Solway & Botvinick 2012 into an anatomically specific basal ganglia circuit model, showing how cortico-striatal connections, dopaminergic modulation of excitability and plasticity, and the ascending spiral architecture can together implement posterior inference over actions.

We can now say that a single computational framework — free-energy minimisation with distinct prediction errors for goal-directed and habit systems — can account for dopaminergic diversity, the specific role of dopamine in goal-directed but not habitual movement initiation, reward-devaluation insensitivity, Pavlovian-instrumental transfer, and reversal-learning dynamics, none of which was accounted for jointly by prior models.

---

### Brain regions & systems

- **Ventral striatum (nucleus accumbens)** — locus of the valuation system; receives dopamine from VTA encoding reward prediction errors for value learning; maps reserve-level-dependent desired reward.
- **Dorsomedial striatum** — locus of the goal-directed system; encodes reward-action contingencies; receives dopamine modulating excitability during action planning and synaptic plasticity during learning.
- **Dorsolateral striatum** — locus of the habit system; encodes action-state mappings; receives dopamine from SNc encoding action (non-habitual movement) prediction errors, not reward RPEs.
- **Ventral tegmental area (VTA)** — proposed location of dopaminergic neurons encoding reward prediction errors for the valuation and goal-directed systems; maps onto δ_v and δ_g.
- **Substantia nigra pars compacta (SNc)** — proposed location of dopaminergic neurons encoding action (habit) prediction errors; maps onto δ_h; predicts responses preferentially to non-habitual movements.
- **Output nuclei of the basal ganglia (GPi/SNr)** — relay action intensity signals; integrate inputs from goal-directed and habit striatal populations to thalamus.
- **Thalamus** — represents planned action intensity; receives integrated output from basal ganglia; feeds back into cortex.
- **Cortex (sensorimotor/prefrontal)** — provides state representations to striatum via cortico-striatal connections; connection weights encode learned parameters Q and H.
- **Ascending spiral striato-dopaminergic projections** (Haber et al. 2000) — structural substrate for communication between valuation and goal-directed systems; ventral striatal neurons send value signal v to goal-directed dopaminergic neurons.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight at the computational and algorithmic levels, but provides limited direct implementational evidence from empirical neural data.

**Computational level**: The brain solves the problem of selecting actions that achieve a desired level of physiological reserves. Rather than always maximising reward, the animal infers which action is most likely to deliver the reward required to restore reserves to their set-point. This is formulated as posterior inference over actions given a desired outcome.

**Algorithmic level**: Both action planning (within-trial gradient ascent on F over a) and learning (across-trial gradient ascent on F over parameters) are instances of the same free-energy minimisation algorithm. Two distinct prediction errors are computed: δ_g (difference between obtained/expected reward and reward predicted by the goal-directed system's current action plan) and δ_h (difference between chosen and habitual action). δ_g drives action planning by modulating striatal excitability until the plan accounts for available reward; δ_h drives habit formation by updating the habit system's action-state mappings. Bayesian weighting by inverse variance means the habit system gradually dominates as its uncertainty decreases with training.

**Implementational level**: The paper proposes that δ_g is computed by dopaminergic neurons in VTA/goal-directed dopamine projections, and δ_h by dopaminergic neurons in SNc/habit system projections. Cortico-striatal weights encode the learned parameters Q and H; dopaminergic modulation of excitability implements the planning signal; dopaminergic modulation of plasticity implements three-factor Hebbian learning. These mappings are consistent with known anatomy (VTA-ventral striatum and SNc-dorsolateral striatum connectivity; ascending spiral; output nuclei; Watabe-Uchida et al. 2012) and with selective experimental observations (movement responses in SNc, reward responses in VTA; Howe & Dombeck 2016; Jin & Costa 2010; Choi et al. 2005; Faure et al. 2005). However, the neural data cited are largely existing observations used to motivate or validate the model, rather than new recordings specifically designed to test the model's unique predictions. The paper's two key predictions — (1) SNc neurons show elevated responses to non-habitual movements and (2) goal-directed dopaminergic responses are prolonged when motor planning is blocked — remain untested.

---

### Limitations & open questions

- The valuation system is not fully described: how the brain determines the desired reward level from physiological reserves is left to future work.
- The model does not explain how striatal neurons distinguish whether a dopaminergic signal should trigger plasticity vs. excitability changes, which the same phasic dopamine signal is proposed to do in different contexts.
- The paper models only D1-expressing direct pathway striatal neurons; the role of D2-expressing indirect pathway neurons (learning from negative feedback) is acknowledged but not incorporated.
- The subthalamic nucleus/hyperdirect pathway — potentially important for action gating and competition — is excluded from the implemented models.
- The models cannot reproduce dopamine ramping as animals approach reward (Howe et al. 2013); this is acknowledged as a direction for future work.
- Habit suppression (extinction) can sometimes fail in the related Miller et al. 2019 model; additional mechanisms for goal-directed re-engagement may be needed.
- The key experimental predictions of the framework (SNc responses to non-habitual movements; prolonged goal-directed dopamine responses when planning is blocked) are not tested in this paper.
- The model assumes Gaussian distributions and linear reward-action dependencies, which may not generalise to more naturalistic tasks.
- Dopaminergic projections to amygdala and cortex are noted as important extensions outside the scope of the current framework.

---

### Connections & keywords

**Key citations**:
- Schultz et al. 1997 — canonical reward prediction error in dopamine
- Daw, Niv & Dayan 2005 — uncertainty-based competition between goal-directed (prefrontal/model-based) and habit (striatal/model-free) systems
- Miller et al. 2019 — habit formation driven by action prediction errors, not reward RPEs
- Solway & Botvinick 2012 — planning as probabilistic inference over actions
- Friston 2010 — active inference framework; prediction errors minimised by both learning and action
- Haber et al. 2000 — ascending spiral striato-dopaminergic projections
- Howe & Dombeck 2016 — distinct VTA (reward) and SNc (movement) dopaminergic responses in mice
- Montague et al. 1996; Houk et al. 1995 — classical reinforcement learning / temporal difference model of dopamine
- Bogacz 2017 — free-energy/predictive coding tutorial

**Named models or frameworks**:
- DopAct framework (the framework introduced in this paper)
- Active inference (Friston)
- Temporal difference learning / model of Schultz et al. 1997
- Daw et al. 2005 model-based / model-free arbitration
- Miller et al. 2019 habit formation model
- Solway & Botvinick 2012 planning-as-inference
- Bayesian action inference

**Brain regions**:
- Ventral striatum / nucleus accumbens
- Dorsomedial striatum
- Dorsolateral striatum
- Ventral tegmental area (VTA)
- Substantia nigra pars compacta (SNc)
- Basal ganglia output nuclei (GPi/SNr)
- Thalamus
- Cortex (sensorimotor, prefrontal)

**Keywords**:
- dopamine prediction error heterogeneity
- goal-directed vs. habitual action control
- free-energy minimisation
- Bayesian action inference
- basal ganglia circuit model
- cortico-striatal plasticity
- action planning and movement initiation
- habit formation mechanisms
- reward prediction error
- Parkinson's disease dopamine depletion
- probabilistic reversal learning
- uncertainty-based arbitration

### Related wiki pages
- [[wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning|Dopamine reward prediction error and temporal-difference learning]]
