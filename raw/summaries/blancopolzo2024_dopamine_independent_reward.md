---
source_file: blancopolzo2024_dopamine_independent_reward.md
paper_id: blancopolzo2024_dopamine_independent_reward
title: "Dopamine-independent effect of rewards on choices through hidden-state inference"
authors:
  - "Marta Blanco-Pozo"
  - "Thomas Akam"
  - "Mark E. Walton"
year: 2024
journal: "Nature Neuroscience"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
tasks:
  - two_step_task
methods:
  - calcium_imaging
  - optogenetics
  - computational_modeling
brain_regions:
  - prefrontal_cortex
  - striatum
  - dorsomedial_striatum
  - nucleus_accumbens
  - ventral_tegmental_area
  - retrosplenial_cortex
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - bayesian_inference
keywords:
  - reward_prediction_error
  - hidden_state_inference
  - partially_observable_markov_decision_process_pomdp
  - dopamine_optogenetics
  - fiber_photometry_gcamp
  - dlight
  - two_step_decision_task
  - model_based_reinforcement_learning
  - bayesian_belief_updating
  - mesolimbic_dopamine
  - cortex_basal_ganglia_interaction
  - reward_rate_coding
  - nonlocal_value_update
  - dopamine
  - independent
  - effect
  - rewards
  - choices
  - through
  - hidden
key_citations:
  - montague1996_predictive_hebbian_dopamine
  - schultz1997_neural_substrate_reward_pred
wiki_pages:
  - wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning
---

### One-line summary

In a two-step decision task, rewards strongly shaped dopamine activity and choices via hidden-state inference tracked by cortex, but direct optogenetic activation or inhibition of dopamine neurons at outcome time had no effect on subsequent choices.

---

### Background & motivation

Reinforcement learning (RL) accounts of adaptive behavior assign dopamine a central role: dopamine reports reward prediction errors (RPEs) that update value estimates to drive choices. A separate body of work shows that animals in structured environments use inference over hidden states to guide behavior flexibly — for example, understanding that anticorrelated reward probabilities signal a single latent state. The two accounts have been largely treated independently. It is unclear whether the flexible behavior attributed to hidden-state inference is actually mediated by dopaminergic RPEs, or whether state inference and dopaminergic RL are dissociable mechanisms. This paper directly confronts that question using combined measurement and causal manipulation.

---

### Methods

- **Subjects**: DAT-Cre mice (n = 18 for behavior; additional cohorts for photometry and optogenetics).
- **Task**: Two-step sequential decision task. Each trial: first-step choice (left/right) → probabilistic transition (80/20) to one of two second-step states (up/down port) → probabilistic reward. Reward probabilities at second-step ports were anticorrelated (0.8/0.2, 0.5/0.5, or 0.2/0.8), reversing in blocks — constituting a binary hidden state (up_good vs down_good). Total: 181,323 trials across 520 sessions (behavior cohort).
- **Behavioral modeling**: Fitted model-free RL, model-based RL, Bayesian inference (standard and asymmetric variants), and mixture-of-strategies models to choices; model comparison via BIC and cross-validated log likelihood.
- **Fiber photometry**: GCaMP6f in DAT-Cre mice (VTA cell bodies, NAc axons, DMS axons) and dLight1.1 in wild-type mice (NAc, DMS) to measure dopamine activity and release concurrently with behavior.
- **Dopamine regression**: Lasso linear regression predicting trial-by-trial dopamine activity at each timepoint; key predictors included previous trial outcome when current second-step state was the same vs. different from previous — a signature distinguishing inference from model-based RL.
- **Optogenetic activation**: ChR2 (n = 7) vs. YFP control (n = 5) in VTA dopamine neurons; stimulation either 200 ms after first-step choice or at outcome-cue onset (25% of trials, counterbalanced). Intracranial self-stimulation as positive control.
- **Optogenetic inhibition**: GtACR2 (n = 7) vs. tdTomato control (n = 5) in VTA dopamine neurons; inhibition at same two timepoints. Two-alternative forced-choice bias assay as positive control.
- **Network model**: PFC modeled as gated recurrent units trained via gradient descent to predict next observations; basal ganglia modeled as feedforward rectified linear units trained via actor-critic RL. Optogenetic stimulation modeled as a positive RPE-equivalent weight update in basal ganglia.

---

### Key findings

- **Behavior consistent with hidden-state inference**: Mice repeated choices following rewarded common transitions and switched after rewarded rare transitions, indicating they tracked the single hidden variable controlling both reward probabilities. Behavioral model comparison could not distinguish asymmetric model-based RL from asymmetric Bayesian inference.
- **Dopamine carries inferred value signals**: When a mouse reached the same second-step state as the previous trial, prior reward positively influenced dopamine at state revelation — consistent with both model-based RL and inference. Critically, when the current second-step state was *different* from the previous trial, prior reward *negatively* influenced dopamine — a nonlocal value update consistent only with inference (reward in one state decreasing the inferred value of the other).
- **Biphasic RPE signature**: In NAc (GCaMP and dLight), second-step state values produced a positive dopamine response at state entry followed by a negative response at outcome — the canonical RPE signature. This was less prominent in VTA and DMS.
- **Parallel dopamine signals**: Dopamine simultaneously encoded (i) RPE-consistent action and state values, (ii) lateralized movement (DMS contralateral to choice; VTA/NAc contralateral to second movement), and (iii) sustained reward rate with distinct spatiotemporal profiles.
- **Dopamine activation does not recapitulate reward**: Stimulating dopamine neurons at outcome (when dopamine responses were maximal) had no effect on next trial choice (β = 0.041, p = 0.168; Bayes factor B = 0.048, strong evidence against the null). By contrast, stimulation after first-step choice significantly increased choice repetition (β = 0.091, p = 0.008).
- **Dopamine inhibition does not block reward effects**: Inhibiting dopamine neurons at outcome had no effect on subsequent choice (all p > 0.283; B = 0.062, strong evidence for null). Inhibition at outcome reduced trial-initiation latency, indicating the manipulation was physiologically effective.
- **Network model reproduces all key results**: A PFC (recurrent) + basal ganglia (feedforward) model in which PFC infers hidden states via observation prediction, and basal ganglia learns values via RPEs, reproduced: (i) inference-consistent behavior, (ii) nonlocal value updates in dopamine, (iii) choice sensitivity to stimulation after action but not after outcome.

---

### Computational framework

The paper integrates two frameworks:

1. **Bayesian hidden-state inference**: A partially observable Markov decision process (POMDP) formulation in which the agent maintains a belief state P(up_good) — the posterior probability that the hidden state is "up is better" — updated via Bayes rule after each observation. Values of second-step states and first-step actions are computed from this belief. Key assumption: the hidden state jointly determines both reward probabilities, so reward at one port is informative about value at the other.

2. **Temporal-difference reinforcement learning (actor-critic)**: RPEs (δ = r + γV(new state) − V(old state)) drive weight updates in a basal ganglia network. Key variables: state/action values V and Q, RPE δ, discount factor γ.

These are instantiated in a cortex-basal ganglia network model. PFC (gated recurrent units) is trained by gradient descent on observation prediction — an unsupervised, slow-timescale process over task acquisition. Basal ganglia (feedforward rectified linear units) receives PFC activity as input and learns via actor-critic RL. At test time, fast behavioral adaptation is driven by changes in PFC recurrent activity (tracking hidden state), not by weight updates. The model is related to meta-RL (Wang et al. 2018) and machine learning work on predictive state representations for POMDPs.

---

### Prevailing model of the system under study

The field's dominant account at the time of this paper is that dopamine neurons report RPEs, and these RPEs update cached or model-based value estimates that then drive choices (Montague et al. 1996; Schultz et al. 1997). Causal evidence that dopamine activation reinforces or suppresses behavior (Steinberg et al. 2013; Hamid et al. 2016; Parker et al. 2016) was taken to support dopamine as a functional RPE signal driving credit assignment. In parallel, an emerging literature documented that behavior and dopamine activity can reflect hidden-state inference rather than simple RPE (Starkweather et al. 2017; Babayan et al. 2018; Bromberg-Martin et al. 2010), but it was unclear whether this meant inference was actually driving choices or merely coloring an RPE signal that was still causally responsible. The paper's introduction frames the open question as: if inference regulates behavior, why does dopamine look like an RPE, and if dopaminergic RPEs drive choices, how are inference signatures generated?

---

### What this paper contributes

The paper dissociates the *informational content* of dopamine signals from their *causal role* in updating choices. Before this work, the inference-consistent signatures in dopamine could have been explained by inference simply shaping the inputs to an RPE mechanism that remained causally responsible for credit assignment. The optogenetic results rule this out: despite robust RPE-like dopamine signals at outcome, neither enhancing nor suppressing dopamine at that time affected subsequent choice. The paper thus establishes that:

1. Dopaminergic RPEs are not causally necessary for the trial-by-trial influence of rewards on choices in a structured environment.
2. The causal influence of rewards on choices is mediated instead by the information rewards provide about the hidden state of the world — a process the model attributes to changes in PFC recurrent dynamics, not dopamine-gated synaptic plasticity.
3. Dopaminergic RPEs appear to serve a different function: updating basal ganglia action weights over the slow timescale of task acquisition, not driving rapid credit assignment during task performance by experienced subjects.

This reframes what dopamine is doing in model-based/inference-based behavior: dopamine remains an RPE signal, but its RPEs are computed using inference-derived values, and the fast behavioral consequences of those RPEs (in expert animals) are mediated upstream in cortex rather than downstream via striatal weight changes.

---

### Brain regions & systems

- **Ventral tegmental area (VTA)**: Dopamine neuron cell bodies; site of GCaMP recordings and optogenetic stimulation/inhibition. Shows RPE-like and inference-consistent value modulation, reward rate, and movement signals. Stimulation here at outcome time fails to influence choice.
- **Nucleus accumbens (NAc)**: Mesolimbic dopamine target; GCaMP axon recordings and dLight release measurements. Shows the clearest biphasic RPE signature (positive at state entry, negative at outcome). Also reflects reward rate.
- **Dorsomedial striatum (DMS)**: Dorsal striatum dopamine target; GCaMP axon recordings and dLight. Shows lateralized movement signal (contralateral to initial choice, not return movement). RPE signature less prominent than NAc; mediolateral gradient in reward response.
- **Prefrontal cortex (PFC)**: Not directly recorded but explicitly modeled as the site of hidden-state inference via recurrent dynamics; referenced via prior literature on medial frontal and retrosplenial cortex tracking reward probabilities throughout ITI.
- **Basal ganglia**: Modeled as the site of actor-critic RL receiving PFC input; proposed locus of slow acquisition-timescale weight updates but not rapid trial-by-trial credit assignment in expert subjects.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Phenomenon**: Experienced mice adapt choices to reflect hidden-state inference (nonlocal reward updating), and dopamine carries RPE-like signals encoding these inferred values — yet dopamine is not causally responsible for reward-driven choice updating.

**Computational level**: The brain must solve a partially observable decision problem in a structured environment. The optimal strategy tracks a hidden state that jointly determines reward probabilities at both ports and maps this to the high-value action.

**Algorithmic level**: Two parallel processes: (i) a recurrent network (PFC) maintains a running estimate of the hidden state by predicting future observations — this estimate is updated within a trial through recurrent activity dynamics, not synaptic weight changes; (ii) a feedforward network (basal ganglia) uses temporal-difference RL with dopaminergic RPEs to learn values and action policies over task acquisition. On individual trials in an expert animal, choice updating is driven by PFC recurrent activity changes, not basal ganglia weight updates.

**Implementational level**: VTA dopamine neurons are the source of the RPE signal (supported by GCaMP recordings showing RPE-like biphasic responses and inference-consistent nonlocal updates). Optogenetic activation and inhibition of VTA dopamine neurons (ChR2, GtACR2) at outcome time causally dissociates dopamine from the behavioral consequences of reward. Local modulation of dopamine terminal activity (e.g., by cholinergic interneurons in striatum) is noted as a possible explanation for VTA vs. NAc signal differences. The paper does not directly record from PFC, but the network model and prior literature (cited) support cortical recurrent activity as the implementational locus of fast hidden-state inference.

---

### Limitations & open questions

- Behavior-only model comparison could not distinguish asymmetric model-based RL from asymmetric Bayesian inference; the dopamine signatures provide evidence for inference but do not definitively rule out model-based RL.
- The PFC-basal ganglia network model is highly simplified (no spiking, no detailed anatomy); the claim that PFC recurrent dynamics drive fast choice updating is supported by the model and prior literature but is not directly tested with PFC recordings or manipulation in this study.
- The null effect of dopamine at outcome time may be specific to well-trained ("expert") animals performing structured tasks; dopamine may still causally drive credit assignment during initial task acquisition when the PFC recurrent representation is not yet established.
- The mechanism by which PFC recurrent representations are read out by basal ganglia to select actions (and how this read-out is learned) is not fully specified.
- What function the ongoing RPE-like dopamine signals serve in the expert animal (beyond shaping basal ganglia weights slowly) remains an open question — reward rate signaling and motivational gating are proposed but not tested.
- Differences between VTA, NAc, and DMS dopamine signals (e.g., absent biphasic signature in VTA for single-trial history, but present for extended history) are not fully explained; local terminal modulation is suggested but not tested.

---

### Connections & keywords

**Key citations**:
- Montague, Dayan & Sejnowski 1996 — dopamine as predictive Hebbian learning/RPE
- Schultz, Dayan & Montague 1997 — dopamine RPE framework
- Akam, Costa & Dayan 2015 — two-step task analysis (model-free vs. model-based)
- Daw, Gershman, Seymour, Dayan & Dolan 2011 — model-based influences and striatal prediction errors
- Starkweather, Babayan, Uchida & Gershman 2017 — dopamine RPEs reflect hidden-state inference
- Babayan, Uchida & Gershman 2018 — belief state representation in dopamine
- Hamid et al. 2016 — mesolimbic dopamine signals value of work
- Parker et al. 2016 — reward/choice encoding in dopamine terminals by striatal target
- Steinberg et al. 2013 — causal link between prediction errors, dopamine and learning
- Mohebi et al. 2019 — dissociable dopamine dynamics for learning and motivation
- Wang et al. 2018 — prefrontal cortex as meta-reinforcement learning system
- Akam & Walton 2021 — what is dopamine doing in model-based RL?

**Named models or frameworks**:
- Two-step task (Daw/Akam variant for rodents)
- Model-free RL (temporal difference with eligibility trace)
- Model-based RL
- Asymmetric Bayesian inference / hidden-state inference
- Actor-critic reinforcement learning
- PFC-basal ganglia cortex-basal ganglia network model
- Meta-RL (Wang et al. 2018; related framework)
- Predictive state representations (Littman & Sutton 2001; machine learning analogue)

**Brain regions**:
- Ventral tegmental area (VTA)
- Nucleus accumbens (NAc)
- Dorsomedial striatum (DMS)
- Prefrontal cortex (PFC) — modeled, not directly recorded
- Basal ganglia — modeled

**Keywords**:
- reward prediction error
- hidden-state inference
- partially observable Markov decision process (POMDP)
- dopamine optogenetics
- fiber photometry (GCaMP, dLight)
- two-step decision task
- model-based reinforcement learning
- Bayesian belief updating
- mesolimbic dopamine
- cortex-basal ganglia interaction
- reward rate coding
- nonlocal value update

### Related wiki pages
- [[wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning|Goal-directed vs habitual control in corticostriatal reinforcement learning]]
