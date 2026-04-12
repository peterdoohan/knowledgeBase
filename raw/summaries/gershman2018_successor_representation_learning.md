---
source_file: "gershman2018_successor_representation_learning.md"
paper_id: "gershman2018_successor_representation_learning"
title: "The Successor Representation: Its Computational Logic and Neural Substrates"
authors: "Samuel J. Gershman"
year: 2018
journal: "The Journal of Neuroscience"
paper_type: "review"
contribution_type: "theoretical"
brain_regions: ["hippocampus", "prefrontal_cortex", "striatum", "ventral_tegmental_area", "substantia_nigra"]
frameworks: ["reinforcement_learning", "model_based_rl", "model_free_rl", "successor_representation", "temporal_difference_learning"]
keywords: ["successor", "representation", "its", "computational", "logic", "neural", "substrates"]
key_citations: ["dayan1993_successor_representation", "momennejad2017_successor_representation_humans", "russek2017_model_based_reinforcement", "tolman1948_cognitive_maps_rats"]
---

### One-line summary

The successor representation (SR) — a predictive map encoding each state in terms of its expected future state occupancies — offers a principled account of how the brain balances computational efficiency and flexibility in reinforcement learning, with hippocampal place cells as its neural substrate and dopamine as a potential error signal for its learning.

---

### Background & motivation

Reinforcement learning requires value estimation over a large state space, and different algorithmic architectures make different tradeoffs between computational efficiency and flexibility. Model-based systems are flexible but computationally costly; model-free systems are cheap but inflexible to environmental change. The SR, originally proposed by Dayan (1993), occupies an intermediate position, but had not been systematically evaluated against behavioral and neural data. This review synthesises recent computational, behavioral, and neural work to assess whether the SR constitutes a distinct reinforcement learning system in the brain, and to clarify what representations the brain should maintain given architectural constraints.

---

### Methods

This is a theoretical review paper. It synthesises the following:

- Formal analysis of the efficiency-flexibility tradeoff across model-based, model-free (TD learning), and SR-based reinforcement learning architectures.
- Review of behavioral studies testing SR-specific predictions (primarily the differential revaluation paradigm of Momennejad et al., 2017, and latent learning findings from Tolman, 1948, and Russek et al., 2017).
- Review of neural studies examining the SR hypothesis in hippocampal place cells (Stachenfeld et al., 2017) and dopaminergic prediction error signals (Gardner et al., 2018).
- Discussion of biologically plausible learning mechanisms, including spike-timing-dependent plasticity as a route to SR learning (Brea et al., 2016).
- Identification of open questions and future directions for the SR research program.

---

### Key findings

- The SR is optimal for a linear function approximation architecture: if state features equal the SR, the value function can be represented exactly as a linear combination of those features.
- The SR predicts asymmetric revaluation: reward devaluation should cause rapid value updating (because the reward function is factored out of the SR), whereas transition devaluation should cause slow updating (because the SR encodes compiled transition statistics). Momennejad et al. (2017) confirmed this asymmetry in humans.
- Hippocampal place fields closely resemble columns of the SR matrix: radially symmetric in open fields, distorted around barriers, skewed in the direction of travel, and clustered near reward — all consistent with the SR model of Stachenfeld et al. (2017).
- Pre-exposure facilitation of contextual fear conditioning (Fanselow, 2010) is abolished by hippocampal lesions, consistent with the hippocampus encoding a predictive map that generalises conditioned fear across states.
- Dopamine neurons respond to sensory (not just reward) prediction errors, and dopamine transients are both necessary and sufficient for stimulus-stimulus learning — consistent with Gardner et al.'s (2018) proposal that phasic dopamine encodes a vector-valued temporal difference error for SR updating.
- Human revaluation behavior in Momennejad et al. (2017) was best explained by a mixture of SR-based and model-based strategies, with model-based computation incrementally refining SR-based value estimates.
- Spike-timing-dependent plasticity can implement SR learning via prospective coding (Brea et al., 2016), consistent with ramping activity in prefrontal neurons anticipating predictable stimuli.

---

### Computational framework

The paper uses reinforcement learning as its primary computational framework, specifically temporal difference (TD) learning with linear function approximation.

Core formalism:
- **Value function**: V(s) = E[sum over t of gamma^t * r_t | s_0 = s], the expected discounted future reward.
- **Successor representation**: M(s, s') = expected discounted future occupancy of state s' when starting from state s, learned by a vector-valued TD rule where the error is the discrepancy between observed and expected state occupancy.
- **Value decomposition**: V(s) = sum over s' of M(s, s') * R(s'), factoring value into a predictive (SR) component and a reward component.
- **Key assumptions**: Markov state transitions; linear function approximation architecture; reward function separable from state transition statistics.

The SR is positioned within a tradeoff space spanning from model-free TD learning (maximally efficient, minimally flexible) through the SR (intermediate) to model-based planning (maximally flexible, computationally costly).

---

### Prevailing model of the system under study

Prior to this paper's framing, the dominant view was that the brain implements two dissociable reinforcement learning systems: a model-free system (habitual, using cached TD values, supported by dorsal striatum) and a model-based system (goal-directed, using an internal world model, supported by prefrontal cortex). The hippocampus was understood primarily as a spatial and episodic memory structure, with its role in reinforcement learning less well characterised. Dopamine was interpreted as encoding a scalar reward prediction error (RPE) signal for model-free value updating, following Schultz, Dayan, and Montague (1997). The SR was known theoretically since Dayan (1993) but had not been widely considered as a biologically implemented third system.

---

### What this paper contributes

The review establishes the SR as a theoretically motivated and empirically supported third reinforcement learning system in the brain, distinct from both model-free and model-based systems. Concretely:

- It provides a principled account of why hippocampal place cells look the way they do: they encode the SR, not merely the animal's current location.
- It reinterprets classical behavioral phenomena (latent learning, fear pre-exposure, outcome devaluation asymmetries) as diagnostics of SR-based computation rather than model-based computation.
- It proposes a reinterpretation of dopamine signals as vector-valued state prediction errors rather than scalar reward prediction errors, linking dopamine to SR learning.
- It clarifies the specific circumstances under which SR-based and model-based systems cooperate: model-based computation refines SR estimates when the transition structure changes.
- It identifies six concrete open questions for future research, including the need for ensemble recordings of dopamine neurons, the nature of SR-model-based interactions, the linearity assumption, state uncertainty, hippocampal response patterns in revaluation experiments, and the relationship between SR-based reinforcement learning and episodic memory.

---

### Brain regions & systems

- **Hippocampus** — proposed neural substrate of the SR; place cell population activity across states encodes the SR matrix, with place fields corresponding to individual columns of that matrix. Hippocampal lesions abolish the fear pre-exposure effect, consistent with loss of predictive map.
- **Midbrain dopamine neurons (VTA/SNc)** — proposed source of vector-valued temporal difference error for SR learning; their responses to sensory (non-reward) prediction errors and necessity for stimulus-stimulus learning are cited as evidence.
- **Prefrontal cortex** — mentioned as a site of prospective coding (ramping activity anticipating predictable stimuli) consistent with SR-like representations; also discussed as potentially shaping dopamine RPEs under state uncertainty.
- **Dorsal striatum** — background role as locus of model-free (habitual) value learning in the broader multi-system framework.

---

### Mechanistic insight

The paper partially meets the bar. It reviews a formalised algorithm (SR with TD learning) and provides supporting neural data (hippocampal place field properties, dopamine response profiles, effects of hippocampal lesions), but the neural evidence is largely correlational or indirect — it is consistent with the SR algorithm but does not decisively dissociate SR-based mechanisms from alternatives at the neural level.

At the level of Marr's three levels:
- **Computational**: the brain solves the problem of value estimation under the constraint of a linear function approximation architecture, for which the SR is the optimal representation.
- **Algorithmic**: the SR is learned via a vector-valued temporal difference prediction error; value is computed as the dot product of the SR and the reward function, allowing rapid reward revaluation without relearning the SR.
- **Implementational**: hippocampal place cells encode the SR matrix (one cell per column); phasic dopamine neurons may convey the vector-valued TD error for SR updating; spike-timing-dependent plasticity can in principle implement SR learning via prospective somatic-dendritic coding.

The review does not provide direct recording evidence that dopamine signals are specifically vector-valued, and it acknowledges that the dopamine hypothesis (Gardner et al., 2018) is "completely speculative." The hippocampal evidence (Stachenfeld et al., 2017) is stronger but relies on model-fitting to existing place cell data rather than causal manipulation of SR-specific variables. Full mechanistic closure — linking the SR algorithm to specific cell types, connectivity, and biophysical mechanisms — is flagged as an open problem.

---

### Limitations & open questions

1. **Dopamine vector hypothesis untested**: No study has systematically tested whether dopamine population activity is vector-valued; ensemble recordings are needed.
2. **SR-model-based interactions**: The nature of cooperative computation between SR and model-based systems is unclear; the temporal ordering of SR-based versus model-based neural signals has not been measured.
3. **Linearity assumption**: Whether neural circuits implementing value approximation are well described by a linear architecture is unknown and difficult to test directly.
4. **State uncertainty**: The SR is defined over known states; how the brain computes an SR over a posterior distribution of hidden states is an open problem.
5. **Hippocampal predictions from revaluation studies**: The SR predicts specific patterns of hippocampal activity changes following reward versus transition devaluation; these have not been tested.
6. **SR and episodic memory**: Whether reinforcement learning and episodic memory share a common hippocampal SR substrate remains unclear.

---

### Connections & keywords

**Key citations**:
- Dayan (1993) — original formulation of the SR
- Stachenfeld, Botvinick, Gershman (2017) — hippocampus as predictive map
- Momennejad et al. (2017) — behavioral evidence for SR in human reinforcement learning
- Russek et al. (2017) — computational account of SR-based and model-based cooperation
- Gardner, Schoenbaum, Gershman (2018) — dopamine as SR prediction error
- Brea et al. (2016) — spike-timing-dependent plasticity and prospective coding
- Schultz, Dayan, Montague (1997) — dopamine as reward prediction error
- Sutton and Barto (1998) — reinforcement learning foundations
- Tolman (1948) — cognitive maps and latent learning
- Fanselow (2010) — fear pre-exposure effect and hippocampus

**Named models or frameworks**:
- Successor representation (SR)
- Temporal difference (TD) learning
- Linear function approximation
- Model-based reinforcement learning / value iteration
- Model-free reinforcement learning
- Efficiency-flexibility tradeoff framework
- Deep successor reinforcement learning (Kulkarni et al., 2016)

**Brain regions**:
- Hippocampus
- Midbrain dopamine neurons (VTA/SNc)
- Prefrontal cortex
- Dorsal striatum

**Keywords**:
- successor representation
- reinforcement learning
- predictive map
- hippocampal place cells
- temporal difference learning
- dopamine prediction error
- efficiency-flexibility tradeoff
- model-based vs model-free
- reward devaluation
- latent learning
- prospective coding
- linear function approximation
