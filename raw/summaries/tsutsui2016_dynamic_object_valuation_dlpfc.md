---
source_file: tsutsui2016_dynamic_object_valuation_dlpfc.md
title: A dynamic code for economic object valuation in prefrontal cortex neurons
authors: Ken-Ichiro Tsutsui, Fabian Grabenhorst, Shunsuke Kobayashi, Wolfram Schultz
year: 2016
journal: Nature Communications
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Single dorsolateral prefrontal cortex (DLPFC) neurons encode dynamic object-specific value signals constructed from recent reward experience, serving as decision variables that convert to choice signals during economic decision-making.

### Background & motivation

Economic decisions require converting neuronal reward valuations into choices, but how this conversion occurs remains unclear. While previous studies found experience-based value signals in parietal cortex and striatum, these were action-referenced and time-locked to sensory or motor events. The critical open questions were: (1) whether individual neurons encode object-specific values suitable for competitive choice mechanisms, and (2) whether such neurons participate in the dynamic construction of values from experience and their conversion to choices.

### Methods

- **Task design**: Two macaque monkeys performed an object-based foraging task with two visual objects (A and B) as choice targets. Base reward probabilities varied in unsignalled blocks (50-150 trials). Instantaneous reward probability increased with consecutive unchosen trials. Task followed Herrnstein's matching law.
- **Behavioural analysis**: Logistic regression estimated subjective "object values" from weighted reward and choice histories. Filter weights derived from half the data; model validated via out-of-sample prediction on remaining half.
- **Neuronal recordings**: Single-unit extracellular recordings from 205 DLPFC neurons (principal sulcus, upper and lower banks) in two monkeys.
- **Analysis**: Multiple linear regression tested for object value coding (value A, value B) controlling for choice, cue position, and action. Sliding window regression (200 ms, 25 ms steps) identified coding latencies. Population decoding used linear SVM and nearest-neighbour classifiers on unselected neurons.

### Key findings

- **Object value coding in single neurons**: 58% (119/205) of DLPFC neurons showed value-related activity. 85.8% of value responses were object-specific (coding value A or B, not both), satisfying criteria for a decision variable: object-specific, distinct from sensory/motor signals, timed before choice, and independent of current-trial choice.
- **Dynamic value construction**: 37% of neurons encoded both last-trial information (reward/choice history) and current-trial object value. These neurons showed temporal transitions: early in trials they encoded history variables, later they encoded scalar object values. Last-trial choice coefficients correlated positively with current-trial value coefficients for the same object (R=0.938, P=2.7×10⁻²³).
- **Value-to-choice conversion**: 46% of value-coding neurons showed dynamic transitions from object value to object choice. Value signals appeared significantly earlier than choice signals (Fig. 5d). Some neurons converted value → choice → action/spatial position, suggesting a processing cascade consistent with attractor-based decision models.
- **Population decoding**: Linear SVM decoded object value from unselected populations with 79.1% accuracy in pre-cue period. Decoding accuracy increased linearly with neuron number, suggesting distributed representation. Population decoding also revealed value-derived variables not emphasized by single neurons: value sum (motivational variable, best decoded in fixation period) and value difference (decision variable).
- **Behavioural relevance**: Neuronal value coding strength correlated with behavioural valuation accuracy (R=0.913, P=8.5×10⁻⁵). Stronger neuronal value coding predicted better choices. Value coding transiently declined before error trials and recovered post-error.

### Computational framework

The paper employs **reinforcement learning (RL)** and **economic decision theory** frameworks. Object values are constructed through exponential discounting of past rewards and choices, formalized as:

Object Value = Σ (weighted reward history) + Σ (weighted choice history)

The framework treats object values as decision variables input to competitive choice mechanisms (winner-take-all attractor dynamics). The computational architecture assumes:
- **Credit assignment**: Object-specific values enable selective updating for chosen vs. unchosen options
- **Decision-making**: Value-to-choice conversion via mutual inhibition between competing alternatives
- **Motivation**: Value sum (net expected return) energizes performance vigour

The study also uses **population coding theory** and **support vector machine classification** to demonstrate distributed representation and flexible readout of decision variables.

### Prevailing model of the system under study

Before this study, the field understood that:
- Experience-based value signals exist in parietal cortex (area LIP) and striatum during matching behaviour
- These value signals were action-referenced (left/right) and time-locked to sensory targets or movement onset
- LIP and striatum neurons encode spatially-referenced values rather than abstract object values
- OFC neurons encode offer values during economic choice with explicit cues, but without the dynamic construction from experience seen in matching tasks
- DLPFC neurons encode various decision variables including reward probability, magnitude, effort, and history, but object value coding had not been established

The introduction framed the question as whether neurons encode object-specific values (computationally advantageous for credit assignment) or relative values (observed in human imaging), and whether such values are constructed dynamically from experience.

### What this paper contributes

This paper establishes that:

1. **Single DLPFC neurons encode object-specific values**: Unlike the prevailing action-referenced value signals in LIP and striatum, DLPFC neurons encode abstract, action-independent object values suitable as inputs to competitive choice mechanisms. This provides a neural basis for the credit assignment problem in RL.

2. **Dynamic value construction in single neurons**: DLPFC neurons show temporal transitions from encoding reward/choice history (value precursors) to encoding current-trial object values. This demonstrates a single-neuron mechanism for constructing values from experience, not previously observed in OFC or striatum.

3. **Single-neuron value-to-choice conversion**: Many DLPFC neurons dynamically convert from value coding to choice coding within trials, consistent with attractor-based decision models. This contrasts with OFC where value and choice are encoded by separate neurons.

4. **Population-level flexibility**: Unselected DLPFC populations encode value-derived variables (value sum, value difference) not emphasized by single neurons, enabling flexible readout for different behavioural functions (motivation vs. decision-making).

5. **Behavioural relevance**: Neuronal value coding strength predicts behavioural valuation accuracy and choice quality, establishing a functional link between DLPFC activity and economic decision performance.

### Brain regions & systems

- **Dorsolateral prefrontal cortex (DLPFC)**: Principal sulcus (upper and lower banks). Primary focus of the study. Encodes object-specific values, value construction from history, and value-to-choice conversion. Hypothesized to implement dynamic value code for economic decision-making.

- **Parietal cortex (area LIP)**: Mentioned as comparison region. Encodes spatially-referenced action values during matching behaviour, contrasted with DLPFC's object-referenced values.

- **Striatum (dorsal/ventral)**: Mentioned as comparison region. Encodes action values and value sum. Contrast with DLPFC object value coding suggests different functional roles.

- **Orbitofrontal cortex (OFC)**: Mentioned as comparison region. Encodes offer values with explicit cues. Contrast with DLPFC's dynamic value construction from experience.

- **Anterior cingulate cortex (ACC)**: Mentioned as comparison region. Lesions impair performance based on reward experience.

### Mechanistic insight

This paper provides **strong mechanistic insight** by presenting both an algorithmic framework and neural data supporting it.

**Computational level**: The paper frames economic decision-making as a reinforcement learning problem requiring: (1) construction of object values from experienced rewards (credit assignment), (2) comparison of values to select choices, and (3) motivation scaling via value sum. The DLPFC is hypothesized to implement this computational architecture.

**Algorithmic level**: The proposed algorithm involves:
- **Value construction**: Exponential weighting of reward/choice history to form scalar object values (equation 2)
- **Value representation**: Object-specific (not relative) value coding enabling selective credit assignment
- **Decision-making**: Attractor dynamics with mutual inhibition converting values to choices
- **Population readout**: Linear combinations of object value neurons compute value sum and difference

**Implementational level**: Single-neuron recordings reveal:
- 58% of DLPFC neurons encode object-specific values (not action values)
- Temporal dynamics show history → value → choice transitions in single neurons
- Population decoding demonstrates distributed representation with ~linear scaling
- Value sum (motivation) and value difference (decision) decoded from same population
- Physical implementation: Principal sulcus neurons with projections to striatum, parietal cortex hypothesized

The paper meets the mechanistic insight bar by linking Marr's three levels: computational (RL-based decision-making), algorithmic (object value construction and comparison), and implementational (single-neuron dynamics in DLPFC circuits).

### Limitations & open questions

- **Correlational nature**: The study cannot establish causal necessity of DLPFC object value coding for decision-making; lesions or inactivation would be needed
- **Simultaneous recording limitation**: Neurons were recorded sequentially, not simultaneously; cross-correlations and true population dynamics could not be assessed
- **Two-choice limitation**: Only two objects were used; whether object value coding scales to multi-option choices remains untested
- **Origin of value signals**: Whether DLPFC constructs values de novo or receives them from other regions (OFC, striatum) could not be determined
- **Causality of coding transitions**: Whether value-to-choice transitions reflect computation in DLPFC or inputs from other areas remains unresolved
- **Species generality**: Findings in macaque may not directly translate to human DLPFC function
- **Task specificity**: Whether results generalize to other decision paradigms (intertemporal choice, risky choice) is unknown

### Connections & keywords

**Key citations**:
- Herrnstein (1961) - Matching law
- Sugrue, Corrado & Newsome (2004) - Matching behaviour in parietal cortex
- Lau & Glimcher (2005, 2008) - Striatal value representations during matching
- Padoa-Schioppa & Assad (2006) - OFC offer value neurons
- Schultz (2015) - Neuronal reward and decision signals review
- Wang (2002), Soltani & Wang (2006), Deco et al. (2013) - Attractor models of decision-making

**Named models or frameworks**:
- Herrnstein's matching law
- Reinforcement learning (RL) models
- Linear-nonlinear-Poisson models of choice dynamics
- Attractor network models of decision-making
- Support vector machine (SVM) decoding
- Winner-take-all competitive choice mechanisms

**Brain regions**:
- Dorsolateral prefrontal cortex (DLPFC) - principal sulcus
- Parietal cortex (area LIP)
- Striatum (dorsal and ventral)
- Orbitofrontal cortex (OFC)
- Anterior cingulate cortex (ACC)

**Keywords**:
- object value
- economic decision-making
- dorsolateral prefrontal cortex
- matching law
- reinforcement learning
- single-neuron recording
- population decoding
- value construction
- credit assignment
- attractor dynamics
- decision variable
- foraging behaviour
- macaque monkey
- principal sulcus
