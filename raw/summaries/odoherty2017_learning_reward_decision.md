---
source_file: odoherty2017_learning_reward_decision.md
paper_id: odoherty2017_learning_reward_decision
title: "Learning, Reward, and Decision Making"
authors:
  - "John P. O'Doherty"
  - "Jeffrey Cockburn"
  - "Wolfgang M. Pauli"
year: 2017
journal: "Annual Review of Psychology"
paper_type: review
contribution_type: review
species:
  - human
methods:
  - electrophysiology
  - fmri
  - computational_modeling
  - lesion
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - orbitofrontal_cortex
  - ventromedial_prefrontal_cortex
  - dorsolateral_prefrontal_cortex
  - prelimbic_cortex
  - striatum
  - ventral_striatum
  - nucleus_accumbens
  - ventral_tegmental_area
  - substantia_nigra
  - amygdala
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - hierarchical_rl
keywords:
  - model_based_reinforcement_learning
  - model_free_reinforcement_learning
  - reward_prediction_error
  - state_prediction_error
  - goal_directed_behaviour
  - habitual_behaviour
  - pavlovian_conditioning
  - arbitration_between_control_systems
  - cognitive_map
  - neurocomputational_substrates
  - dopamine_striatum_plasticity
  - social_learning_theory_of_mind
  - learning
  - reward
  - decision
  - making
key_citations:
  - daw2005_uncertainty_prefrontal_striatal
  - schultz1997_neural_substrate_reward_pred
  - tolman1948_cognitive_maps_rats
  - wilson2014_best_practices_scientific
---

### One-line summary

This review synthesises evidence for multiple coexisting behavioural control systems in the brain — model-free (habitual), model-based (goal-directed), and Pavlovian — and maps their computational algorithms onto distinct neurocomputational substrates, covering their interactions, arbitration, and extension to social learning contexts.

---

### Background & motivation

Organisms must navigate an environment that demands behavioural flexibility (to adapt to changing contingencies) and efficiency (to act quickly with limited cognitive resources). Longstanding debate contrasted habitual, stimulus-driven behaviour with deliberative, goal-directed behaviour, but accumulating evidence shows these are not alternatives but coexisting systems. The review synthesises how formal reinforcement learning (RL) theory, which distinguished model-free from model-based algorithms, has clarified what computations these brain systems implement and where those computations are realised in neural circuitry.

---

### Methods

This is a narrative review synthesising animal (rodent and primate) electrophysiology, human fMRI, lesion, pharmacological, and computational modelling studies. The authors do not report original data or apply formal meta-analytic inclusion criteria; coverage is broad across species and methods. Synthesis is organised by computational framework (model-free RL, model-based RL, Pavlovian conditioning) with explicit mapping to neuroanatomy.

---

### Key findings

- Evidence from devaluation paradigms and overtraining manipulations supports distinct habitual (model-free) and goal-directed (model-based) instrumental control systems in both rodents and humans.
- A similar model-free/model-based distinction applies to Pavlovian conditioning: some conditioned responses are devaluation-sensitive (model-based), others are not (model-free, linked to phasic dopamine / nucleus accumbens sign tracking).
- Phasic dopamine activity encodes reward prediction errors (RPEs) consistent with model-free TD learning; RPE signals are found in striatum and midbrain in both rodents and humans.
- State prediction errors (SPEs), distinct from RPEs, are found in posterior parietal cortex and dorsolateral prefrontal cortex and are candidates for learning the state-transition model underlying model-based control.
- A cognitive map supporting model-based control is distributed across multiple regions: hippocampus (spatial/relational maps), OFC (current state in abstract task space; outcome identity), posterior parietal cortex (action–state transitions), and dorsolateral PFC (working memory for planning).
- Outcome valuation is encoded in OFC, vmPFC, and amygdala; vmPFC encodes a common currency for goods of different categories.
- Goal-directed action selection recruits prelimbic/vmPFC and dorsomedial striatum/caudate; habitual control recruits posterior dorsolateral striatum, modulated by dopamine.
- An arbitration mechanism in ventrolateral PFC and frontopolar cortex assigns control to model-based versus model-free systems as a function of their relative reliability.
- Social learning recruits similar RL-like computations but additionally engages mentalising circuitry (posterior STS, dorsomedial PFC, temporoparietal junction) for theory-of-mind inference.
- Individual differences in corticostriatal connectivity (vmPFC–dorsomedial striatum; posterolateral striatum–premotor cortex) predict the degree of goal-directed versus habitual expression.

---

### Computational framework

The paper is organised around reinforcement learning (RL), specifically the model-free / model-based dichotomy introduced by Daw et al. (2005).

**Model-free RL**: value is learned incrementally from reward prediction errors (RPEs; temporal-difference learning). Values reflect cached stimulus–response associations and are insensitive to immediate changes in outcome value. Key variable: RPE = received reward − expected reward, implemented by phasic dopamine.

**Model-based RL**: an agent maintains an internal model of the environment (state-transition function T(s, a, s') and reward function R(s)). Value is computed online by planning (e.g., tree search / dynamic programming), making it immediately sensitive to outcome revaluation. Key variables: state prediction errors (SPEs) for learning T; outcome identity representations for R.

**Pavlovian conditioning**: covered under both frameworks. Model-free Pavlovian learning uses RPE-driven stimulus–outcome associations (Rescorla–Wagner); model-based Pavlovian learning uses stimulus–stimulus association maps (hippocampus, OFC) enabling sensory preconditioning and devaluation sensitivity.

**Arbitration**: a meta-controller weights control between systems based on relative predictive accuracy; formalised as uncertainty-based competition (Daw et al. 2005).

---

### Prevailing model of the system under study

The field's baseline, as framed in the paper's introduction, contrasts two long-standing theoretical positions: (1) habitual/stimulus–response control, in which behaviour is retrospectively shaped by past reinforcement (Thorndike), and (2) goal-directed/cognitive-map control, in which behaviour is prospectively guided by an internal model of the environment (Tolman). The introduction presents an emerging consensus — supported by devaluation experiments in rodents (Dickinson, Balleine) and parallel RL theory (Daw et al.) — that both systems coexist and compete for behavioural control. The baseline neurocomputational model, against which the review builds, holds that model-free control is implemented by dopamine-modulated striatal learning and that goal-directed control requires prefrontal and hippocampal circuitry encoding a cognitive map, but the precise boundaries, interactions, and neural substrates of arbitration remained uncertain.

---

### What this paper contributes

The review consolidates a decade of empirical and computational work into a unified neurocomputational framework with the following advances over baseline understanding:

1. **Multiple Pavlovian systems**: extends the model-free/model-based distinction from instrumental to Pavlovian conditioning, providing a framework for understanding devaluation-sensitive Pavlovian responses.
2. **Distributed cognitive map**: clarifies that the cognitive model supporting goal-directed control is distributed (hippocampus for relational/spatial maps, OFC for abstract state identity, posterior parietal cortex for action–state transitions, dlPFC for online planning), rather than localised.
3. **State prediction errors as a learning signal**: identifies SPEs in parietal and dlPFC as the mechanism for acquiring the transition model, separate from RPEs for value.
4. **Arbitration circuitry**: provides preliminary neural evidence for an explicit arbitration mechanism (ventrolateral PFC / frontopolar cortex) that monitors system reliability and shifts control accordingly.
5. **Social learning extension**: situates theory-of-mind computations as a potential fourth system, or module providing input into model-based RL, with distinct but overlapping circuitry.
6. **Open questions established**: clearly delineates what remains unresolved — mechanisms of arbitration between Pavlovian and instrumental systems, the role of multiple systems in exploration (not just exploitation), and how model-based and model-free systems interact during learning (tutoring hypothesis).

---

### Brain regions & systems

- **Striatum (posterior dorsolateral / posterior putamen)** — locus of model-free value learning; RPE-driven dopaminergic plasticity; habitual control expression.
- **Striatum (dorsomedial / caudate)** — goal-directed action acquisition and expression; model-based control.
- **Ventral striatum / nucleus accumbens** — Pavlovian conditioned responses; RPE signals for appetitive Pavlovian conditioning; sign-tracking behaviour.
- **Midbrain dopamine neurons (VTA / SNc)** — encode RPEs; provide teaching signal for model-free learning via projections to striatum.
- **Orbitofrontal cortex (OFC)** — outcome identity representation; current state encoding in abstract task space; model-based Pavlovian stimulus–stimulus associations.
- **Ventromedial prefrontal cortex (vmPFC)** — common currency outcome valuation; instrumental contingency tracking; devaluation-sensitive action values; homologue of rodent prelimbic cortex for goal-directed acquisition.
- **Dorsolateral prefrontal cortex (dlPFC)** — working memory for model-based planning; state prediction error signals.
- **Posterior parietal cortex (including lateral IPS, inferior parietal lobule)** — state-transition encoding; action-value representations; SPE signals; action planning.
- **Hippocampus** — spatial and relational cognitive map; model-based planning; sensory preconditioning; trajectory/future state representation.
- **Amygdala (basolateral complex / central nucleus)** — outcome value encoding; conditioned responses to aversive and appetitive stimuli; model-based expected value signals in Pavlovian conditioning.
- **Anterior cingulate / dorsomedial PFC** — effort representation; integrated action value; hierarchical control; social inference updating.
- **Ventrolateral PFC / frontopolar cortex** — arbitration between model-based and model-free systems; estimation uncertainty / exploration.
- **Posterior superior temporal sulcus / temporoparietal junction** — social inference; belief updating about other agents.

---

### Mechanistic insight

The paper meets a partial bar. It reviews neural data (fMRI, electrophysiology, lesion, pharmacology) that link specific computational variables (RPEs, SPEs, outcome value, action value, arbitration signals) to identified brain regions. In several cases — particularly the RPE/dopamine/striatum link and the SPE/parietal-dlPFC link — the mapping is specific enough to distinguish between algorithms. However, as a review, it does not present new original neural data, and many of the links it reports leave algorithmic alternatives open.

The clearest Marr-level mapping the paper supports is for **model-free RL via dopaminergic RPEs**:

- **Computational**: the brain must learn to predict future reward from past experience, minimising prediction error to cache value in stable stimulus–response associations.
- **Algorithmic**: temporal-difference learning with an RPE signal (received − expected reward); cached values update associative weights incrementally; value is not recomputed online but retrieved.
- **Implementational**: phasic activity of midbrain dopamine neurons encodes RPE; dopamine projections to dorsolateral striatum modulate synaptic plasticity (dopamine-gated STDP); posterior putamen stores stimulus–response values; dopaminergic drugs (L-DOPA, antagonists) modulate learning rate as predicted.

For **model-based control**, the computational and algorithmic levels are well articulated but the implementational level remains incompletely specified — the precise circuitry by which hippocampal maps, OFC state representations, and parietal transition estimates are integrated for online planning is not yet known.

---

### Limitations & open questions

- **Arbitration mechanism**: neural evidence for arbitration is preliminary; the computations mediating Pavlovian–instrumental arbitration are largely unknown.
- **Exploration vs. exploitation**: almost nothing is known about how the multiple control systems contribute to exploration; the review identifies this as a significant gap.
- **Model-based/model-free interaction during learning**: whether the model-based system actively tutors the model-free system (or vice versa) is unresolved.
- **Pavlovian system status**: it remains unclear whether goal-directed Pavlovian conditioning constitutes a genuinely distinct third control system or is subsumed by model-based instrumental computations.
- **Social learning system**: whether mentalising computations represent a fourth RL system or merely an input module to model-based RL is unresolved.
- **Individual differences**: sources of variability in habitual vs. goal-directed expression (genetics, training history, psychiatric risk) are noted but not deeply explained.
- **Common-currency debate**: the claim that vmPFC encodes a common currency for goods of different categories remains methodologically contested.
- **Species translation**: many lesion and electrophysiology findings are from rodents; homologues of prelimbic cortex and dorsomedial striatum in primates are assumed rather than demonstrated.

---

### Connections & keywords

**Key citations**:
- Daw et al. (2005) — model-free/model-based RL and uncertainty-based competition
- Schultz et al. (1997) — dopamine RPE
- Dickinson (1985); Balleine & Dickinson (1994) — habits vs. goal-directed control; devaluation paradigm
- Tolman (1948) — cognitive maps
- Glascher et al. (2010) — state prediction errors in parietal/dlPFC
- Lee et al. (2014) — arbitration in ventrolateral PFC
- Wilson et al. (2014) — OFC state encoding
- Dayan & Berridge (2014) — model-based Pavlovian conditioning
- Rescorla & Wagner (1972) — model-free Pavlovian learning

**Named models or frameworks**:
- Model-free reinforcement learning (temporal-difference learning)
- Model-based reinforcement learning
- Pavlovian-to-instrumental transfer (PIT)
- Uncertainty-based arbitration (Daw et al. 2005)
- Hierarchical reinforcement learning
- Reward prediction error (RPE)
- State prediction error (SPE)
- Outcome devaluation paradigm

**Brain regions**:
- Striatum (dorsolateral posterior, dorsomedial, ventral / nucleus accumbens)
- Midbrain dopamine neurons (VTA, SNc)
- Orbitofrontal cortex (OFC)
- Ventromedial prefrontal cortex (vmPFC)
- Dorsolateral prefrontal cortex (dlPFC)
- Posterior parietal cortex
- Hippocampus
- Amygdala (basolateral, central nucleus)
- Anterior cingulate / dorsomedial PFC
- Ventrolateral PFC / frontopolar cortex
- Posterior superior temporal sulcus / temporoparietal junction

**Keywords**:
- model-based reinforcement learning
- model-free reinforcement learning
- reward prediction error
- state prediction error
- goal-directed behaviour
- habitual behaviour
- Pavlovian conditioning
- arbitration between control systems
- cognitive map
- neurocomputational substrates
- dopamine striatum plasticity
- social learning theory of mind
