---
source_file: demartino2023_value_based_goals_abstraction.md
title: "Goals, usefulness and abstraction in value-based choice"
authors: Benedetto De Martino, Aurelio Cortese
year: 2023
journal: Trends in Cognitive Sciences
paper_type: review
contribution_type: theoretical
---

### One-line summary

Value is a functional, goal-dependent construct — not simply hedonic reward — and the brain computes it through abstraction: building compact, low-dimensional representations that select goal-relevant information via attention, memory, and prefrontal mixed selectivity, and monitors and updates them via metacognitive mechanisms.

---

### Background & motivation

Neuroeconomics and decision-making research have largely equated value with hedonic reward, focusing on automatic valuation processes. This framing neglects the fact that the usefulness of an option is inherently goal-dependent: an object's value can change instantly when behavioural goals shift (e.g., a table becoming shelter during an earthquake). The paper addresses the gap between reward-centric accounts of value and the flexible, functional way humans actually assign value to options in dynamic real-world environments. It argues that understanding how the brain constructs abstract, goal-directed value representations is essential for bridging cognitive neuroscience, neuroeconomics, and artificial intelligence research on multi-goal learning.

---

### Methods

This is a narrative review synthesising empirical, computational, and theoretical work across cognitive neuroscience, neuroeconomics, reinforcement learning, and AI.

- Scope: human and animal studies on value-based choice, goal-directed behaviour, cognitive control, memory, attention, metacognition, and prefrontal cortex function; AI/RL algorithms (model-free, model-based, hierarchical, multi-objective, mixture-of-experts, meta-learning).
- Key empirical work cited: fMRI studies on goal-dependent representational geometry (representational similarity analysis), neurofeedback-guided abstraction learning, eye-tracking studies of attention in value-based choice, confidence and metacognitive monitoring studies, and single-unit recordings in non-human primates.
- Synthesis method: narrative, organised around three core computational problems — (1) how abstractions are formed (dimensionality reduction, mixed selectivity); (2) how goal-relevant information is selected (attention, memory); (3) how representations are monitored and updated (metacognition, algorithmic switching mechanisms).

---

### Key findings

- Value and reward are computationally distinct: value is goal-dependent and functional ("usefulness"), whereas reward is hedonic. Experimental designs that conflate the two (single-goal, maximise-reward paradigms) obscure this distinction.
- Abstraction — the construction of low-dimensional representations retaining only goal-relevant information — is proposed as the core computational operation linking goals to value. Humans who use abstraction-based strategies in learning tasks show faster learning and higher confidence (Cortese et al., 2021, eLife).
- Neural mixed selectivity in the prefrontal cortex (PFC) is identified as the key coding principle enabling the trade-off between generalisation (low-dimensional) and discrimination (high-dimensional). High-dimensional neural representations support effective learning and better episodic memory.
- Goal manipulations instantaneously rearrange representational geometry: in occipital and PFC regions, items cluster by goal-relevant features rather than perceptual similarity (Castegnetti et al., 2021, Science Advances).
- The ventromedial PFC (vmPFC) is a convergence zone linking value computation, schema-based memory, working memory prioritisation, and cognitive map formation — functions previously seen as distinct but here argued to reflect a common computational role in abstract goal-value representation.
- Attention and memory act as information-selection mechanisms feeding into abstract value representations: vmPFC-occipital coupling during reward predicts abstraction efficiency; attention modulates goal-relevant evidence integration rather than raw reward magnitude.
- Metacognition (confidence) provides a monitoring signal over value representations; reliability/confidence is treated as an intrinsic feature of value that drives switching when a representation ceases to be useful.
- Four candidate algorithmic architectures for monitoring and updating representations are discussed: hierarchical switch-evidence accumulation, concurrent behavioural strategy selection, meta-learning, and mixture-of-experts.

---

### Computational framework

**Reinforcement learning (RL) and its extensions**, including model-free RL, model-based RL, hierarchical RL, multi-objective RL (MORL), successor representation RL, meta-learning, and mixture-of-experts architectures.

The paper uses RL as its primary formal language. The core problem is state representation: RL requires the agent to define a state that captures goal-relevant environmental features, discarding irrelevant ones (the "curse of dimensionality"). Key variables include: value/utility (subjective expected reward), policy (action-selection mapping), reward prediction errors, and — centrally — abstract state representations that compress high-dimensional sensory inputs according to the current goal. The framework assumes that goal-dependent value is computed by first abstracting a low-dimensional representation from perception and memory, then evaluating that representation with standard RL-like value signals. Reliability or confidence is treated as a metacognitive variable that gates switching between competing representations.

Mixed selectivity in PFC populations is proposed as the neural implementation of high-dimensional latent representations that permit flexible linear readout for diverse downstream computations.

---

### Prevailing model of the system under study

The review identifies the prevailing model as **hedonic-reward-centric neuroeconomics**: the brain computes subjective expected utility by assigning scalar value signals to options (or actions) through dopaminergic prediction-error learning in midbrain-striatal circuits, with vmPFC as the locus of a common value currency. In this framework, value ≈ reward, goal manipulation is typically absent from experimental designs, and value is treated as a relatively stable property of stimuli updated by experience. Cognitive control and memory are treated as separate systems from value computation. The paper positions itself against this siloed, reward-as-value assumption, arguing that the field has underweighted the functional and context-dependent nature of value.

---

### What this paper contributes

The review advances a unified computational account in which vmPFC (and interconnected regions) performs a domain-general function: constructing, maintaining, monitoring, and updating abstract goal-value mappings. This reconciles previously disparate literatures on economic value, memory schemas, cognitive control, and cognitive maps under a single framework. Concretely:

- It reframes value as "usefulness" — a functional quantity that depends on goals and requires active abstraction, not just hedonic registration.
- It identifies mixed selectivity as the algorithmic mechanism enabling abstract, flexible representations without information loss.
- It positions metacognition/confidence as a computational ingredient in value (not merely a readout), serving the monitoring and switching of representations.
- It draws substantive parallels between human goal-directed valuation and AI advances in hierarchical RL, MORL, and mixture-of-experts, pointing towards a cross-disciplinary research program.
- Key unresolved questions identified: how hedonic and goal-directed value interact; how the brain endogenously sets and arbitrates among competing goals; how to distinguish goals, rules, and contexts algorithmically and neurally.

---

### Brain regions & systems

- **Ventromedial prefrontal cortex (vmPFC)** — proposed hub for abstract goal-value representations; encodes value strength, confidence, and schemas; functionally coupled with occipital cortex during reward-guided abstraction learning; lesions impair both schema-based memory and value-based choice.
- **Prefrontal cortex (PFC) broadly** — locus of mixed selectivity; generates separable, orthogonal representations via recurrent dynamics; domain-general controller for working memory and attention.
- **Orbitofrontal cortex (OFC)** — exerts top-down control over sensory cortices; encodes confidence; linked to arbitration between learning strategies (cited work on Knudsen & Wallis 2022).
- **Frontopolar cortex** — monitoring quality of value representations during metacognitive judgements; arbitration between learning strategies and competing goals.
- **Dorsomedial frontal cortex / dorsal anterior cingulate cortex (dACC)** — accumulates switch evidence and determines behaviour course in hierarchical control tasks (Sarafyazd & Jazayeri 2019).
- **Hippocampus (HPC)** — central to constructing goal-dependent value representations from memory; interacts with vmPFC in a recurrent loop for retrieving and amplifying goal-relevant memories; cited for successor representation and sequential replay.
- **Occipital / visual cortex** — modulated by goal and reward via top-down PFC signals; activity patterns reflect goal-relevant object clustering even in early visual areas.
- **Striatum / midbrain dopamine system** — substrate for reward prediction signals in model-free RL; interaction with PFC in meta-learning via cortico-thalamic-basal ganglia loops.
- **Cortico-thalamic loops (PFC–basal ganglia–thalamus)** — neural substrate for meta-learning and hierarchical control of representations.

---

### Mechanistic insight

The paper does not meet the bar for this section in full. It proposes a rich algorithmic framework (abstract value via mixed selectivity, metacognitive monitoring, mixture-of-experts switching) and cites supporting neural evidence, but it is a review synthesising others' findings rather than presenting primary neural data linking a specific algorithm's variables to measured neural activity. Individual cited studies provide partial mechanistic evidence (e.g., vmPFC-occipital coupling during abstraction learning with fMRI and neurofeedback; PFC single-unit mixed selectivity recordings in primates), but no single study in the review simultaneously formalises an algorithm and provides neural data uniquely supporting it over alternatives. The review's own empirical contributions (Cortese et al., 2021; Castegnetti et al., 2021) support specific aspects of the framework (value-guided abstraction; goal-dependent representational geometry) but do not constitute a full algorithmic-to-implementational mapping.

---

### Limitations & open questions

- The distinction between goal, context, and rule is acknowledged as conceptually blurry and lacking algorithmic precision; most experimental paradigms use externally set goals, leaving endogenous goal-setting largely unaddressed.
- The computational relationship between hedonic reward and goal-directed ("usefulness") value remains unspecified; it is unclear how dopaminergic prediction errors and the opioid/hedonic system interact.
- Most RL frameworks assume a single goal and scalar reward; how the brain arbitrates among competing goals simultaneously is unsolved.
- Whether the brain maps externally imposed rules and contexts onto an internal goal representation (enabling a unified mechanism) is an open question.
- Aesthetic values are discussed speculatively as extreme high-level abstractions; their relationship to functional goal-dependent value is "still opaque."
- The trade-off between low- and high-dimensional representations and how the brain determines the appropriate abstraction level remains poorly understood.
- Homeostatic RL (value depending on physiological state) is noted as a promising but nascent direction.

---

### Connections & keywords

**Key citations:**
- Cortese, A. et al. (2021). Value signals guide abstraction during learning. *eLife*, 10, e68943.
- Castegnetti, G. et al. (2021). How usefulness shapes neural representations during goal-directed behavior. *Science Advances*, 7, eabd5363.
- Frömer, R. & Shenhav, A. (2022). Filling the gaps: cognitive control as a critical lens for understanding mechanisms of value-based decision-making. *Neurosci. Biobehav. Rev.*
- Niv, Y. (2019). Learning task-state representations. *Nature Neuroscience*, 22, 1544–1553.
- Rigotti, M. et al. (2013). The importance of mixed selectivity in complex cognitive tasks. *Nature*, 497, 585–590.
- Fusi, S. et al. (2016). Why neurons mix: high dimensionality for higher cognition. *Current Opinion in Neurobiology*, 37, 66–74.
- Behrens, T.E.J. et al. (2018). What is a cognitive map? Organizing knowledge for flexible behavior. *Neuron*, 100, 490–509.
- Mante, V. et al. (2013). Context-dependent computation by recurrent dynamics in prefrontal cortex. *Nature*, 503, 78–84.
- De Martino, B. et al. (2012). Confidence in value-based choice. *Nature Neuroscience*, 16, 105–110.
- Sarafyazd, M. & Jazayeri, M. (2019). Hierarchical reasoning by neural circuits in the frontal cortex. *Science*, 364, eaav8911.
- Gilboa, A. & Marlatte, H. (2017). Neurobiology of schemas and schema-mediated memory. *Trends in Cognitive Sciences*, 21, 618–631.
- Sutton, R.S. & Barto, A.G. (1998). *Reinforcement Learning: An Introduction*. MIT Press.

**Named models or frameworks:**
- Reinforcement learning (model-free, model-based)
- Hierarchical reinforcement learning
- Multi-objective reinforcement learning (MORL)
- Successor representation RL
- Meta-learning
- Mixture-of-experts architecture
- Drift-diffusion / attentional drift-diffusion model (cited indirectly via Krajbich et al.)
- Representational similarity analysis (RSA)
- Hierarchical switch-evidence variable (Sarafyazd & Jazayeri)
- Concurrent behavioural strategies selection (Collins & Koechlin; Donoso et al.)

**Brain regions:**
- Ventromedial prefrontal cortex (vmPFC)
- Prefrontal cortex (PFC)
- Orbitofrontal cortex (OFC)
- Frontopolar cortex
- Dorsomedial frontal cortex
- Dorsal anterior cingulate cortex (dACC)
- Hippocampus (HPC)
- Occipital / visual cortex
- Striatum
- Midbrain dopamine system
- Cortico-thalamic-basal ganglia loops

**Keywords:**
- goal-dependent value representation
- usefulness vs. reward
- abstraction and dimensionality reduction
- mixed selectivity
- ventromedial prefrontal cortex
- cognitive maps and schemas
- metacognition and confidence in value
- attention-value interaction
- hierarchical reinforcement learning
- multi-objective reinforcement learning
- representational geometry
- information selection in decision-making
