---
source_file: bakermans2020_reinforcement_learning_dopamine.md
paper_id: bakermans2020_reinforcement_learning_dopamine
title: "Reinforcement Learning: Full Glass or Empty — Depends Who You Ask"
authors:
  - "Jacob J.W. Bakermans"
  - "Timothy H. Muller"
  - "Timothy E.J. Behrens"
year: 2020
journal: "Current Biology"
paper_type: review
contribution_type: review
species:
  - mouse
brain_regions:
  - ventral_tegmental_area
frameworks:
  - reinforcement_learning
  - temporal_difference_learning
keywords:
  - distributional_reinforcement_learning
  - temporal_difference_learning
  - reward_prediction_error
  - dopamine_neurons
  - ventral_tegmental_area
  - optimistic_pessimistic_neurons
  - quantile_coding
  - reward_distribution
  - rpe_asymmetry
  - reversal_point
  - risk_sensitive_decision_making
  - neuroscience_ai_interaction
  - reinforcement
  - learning
  - full
  - glass
  - empty
  - depends
  - who
  - you
key_citations:
  - schultz1997_neural_substrate_reward_pred
  - lammel2014_dopamine_reward_aversion_b
wiki_pages:
  - wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning
---

### One-line summary

A Current Biology Dispatch reviewing Dabney et al. (2020), arguing that the diversity of dopamine neuron responses reflects distributional reinforcement learning — the representation of a full probability distribution over future rewards — rather than classical temporal-difference tracking of average expected reward.

---

### Background & motivation

Classical temporal difference (TD) learning predicts that dopamine neurons signal a reward prediction error (RPE) based on the difference between received and expected average future reward. This model elegantly explained the phasic firing of dopamine neurons first observed by Schultz et al. (1997), but left two open problems: (1) TD learning tracks only the mean of the reward distribution, discarding information about the variance or shape of possible outcomes, which is necessary for certain decisions (e.g., risk-sensitive foraging); and (2) empirically, dopamine neurons show heterogeneous RPE responses — some exhibit stronger prediction errors than others to identical rewards — which is not predicted by classical TD. This dispatch contextualises Dabney et al.'s (2020) solution to both problems via distributional reinforcement learning.

---

### Methods

This is a commentary/dispatch piece, not a primary study. The authors summarise and interpret the methods and findings of Dabney et al. (2020):

- Dabney et al. re-analysed dopamine neuron recordings from the ventral tegmental area (VTA) of mice (originally from Eshel et al., 2015) during delivery of variable reward volumes (0.1, 0.3, 1.2, 2.5, 5, or 10 µl per trial).
- Key analysis: identification of each neuron's "reversal point" — the reward magnitude at which the RPE switches from negative to positive — as a proxy for each neuron's learned reward prediction.
- Asymmetries in positive vs. negative RPE scaling were used to classify neurons as optimistic or pessimistic.
- A decoding analysis reconstructed the full reward probability density function from the population of reversal points and scaling asymmetries.

---

### Key findings

- Dopamine neurons in mouse VTA show a range of reversal points across the population, consistent with distributional RL rather than classical TD (which predicts a single shared reversal point at the mean reward).
- Some neurons are "pessimistic" (reversal point below the mean; mostly positive RPEs), others are "optimistic" (reversal point above the mean; mostly negative RPEs).
- The asymmetry in positive vs. negative RPE scaling correlates with each neuron's reversal point — a specific prediction of distributional RL that is not expected from random neural diversity.
- The full reward probability distribution, including multimodal distributions, can be successfully decoded from the population of dopamine neurons using the reversal points and scaling asymmetries alone.
- The function of distributional RL may differ between brains and artificial agents: in machines, learning the distribution primarily improves internal representations; in biological systems, it may additionally support risk-sensitive decision-making.

---

### Computational framework

The paper centres on distributional reinforcement learning (distributional RL), an extension of classical temporal difference (TD) learning imported from machine learning (Bellemare et al., 2017; Dabney et al., 2018).

- In classical TD learning, a single value function V(s) estimates the expected cumulative future reward from state s. The TD RPE (δ) = r + γV(s') − V(s) drives value updates; all neurons converge to the same estimate.
- In distributional RL, rather than a single expectation, a population of value functions each tracks a different quantile of the reward distribution. Each neuron i has an asymmetric learning rate: it weights positive RPEs by α⁺ᵢ and negative RPEs by α⁻ᵢ. The equilibrium prediction of neuron i converges to the τᵢ-th quantile, where τᵢ = α⁺ᵢ / (α⁺ᵢ + α⁻ᵢ).
- Optimistic neurons (high τ) overweight positive RPEs and converge to high quantile predictions; pessimistic neurons (low τ) converge to low quantile predictions.
- Taken together, the population encodes the full cumulative distribution function of rewards, allowing reconstruction of multimodal distributions.

---

### Prevailing model of the system under study

Before Dabney et al. (2020), the dominant model of dopamine signalling was the TD prediction error hypothesis: dopamine neurons in the VTA and substantia nigra uniformly signal the scalar TD RPE — the difference between received and predicted average future reward (Schultz, Dayan & Montague, 1997). Under this account, all dopamine neurons should track the same quantity (mean expected value) and produce identical RPEs for the same reward, with positive errors for above-average rewards and negative errors for below-average rewards. The heterogeneity of dopamine neuron responses (differential response magnitudes and reversal points) was noted empirically (Fiorillo et al., 2003; Lammel et al., 2014) but lacked a mechanistic explanation within this framework.

---

### What this paper contributes

This dispatch synthesises and contextualises the finding that dopamine neuron diversity is not noise or incidental anatomical heterogeneity, but rather a functional signature of distributional RL: the population collectively encodes the full probability distribution over future rewards, not just the mean. This reframes the heterogeneity of dopamine responses from a puzzle into a computational necessity. The piece also raises the open question of whether the computational function of distributional RL in biological brains (potentially enabling risk-sensitive choice) differs from its function in artificial agents (primarily improving representational quality), noting this is not yet resolved.

---

### Brain regions & systems

- **Ventral tegmental area (VTA)** — primary locus of analysis; dopamine neurons recorded here exhibit the distributional RPE signatures described. The VTA is argued to implement distributional RL at the population level.

---

### Mechanistic insight

This paper meets both criteria for a mechanistic insight entry.

1. It formalises a specific algorithm (distributional RL with asymmetric RPE scaling) as the mechanism underlying dopamine population coding.
2. It cites neural recording data (Eshel et al., 2015, re-analysed by Dabney et al., 2020) that specifically support distributional RL over classical TD — in particular, the correlation between reversal points and RPE scaling asymmetries, and the successful reconstruction of the reward distribution from population activity.

**Bonus**: The paper addresses the implementational level by specifying the biophysical parameter (asymmetric positive/negative RPE learning rates) that determines each neuron's optimism/pessimism.

- **Computational level**: The brain must represent the full probability distribution over future rewards, not merely the mean, to support risk-sensitive decision-making (e.g., threshold-based survival decisions where mean reward is insufficient).
- **Algorithmic level**: A population of dopamine neurons each tracks a different quantile of the reward distribution via asymmetric TD learning — neurons with a higher ratio of positive-to-negative RPE sensitivity converge to higher quantile predictions (optimistic), and vice versa. The set of reversal points across the population encodes the cumulative distribution function.
- **Implementational level**: The asymmetry in RPE sensitivity (α⁺ vs. α⁻) across individual dopamine neurons in the VTA is the physical instantiation of the distributional code. Specific neurons are identified as optimistic or pessimistic based on the sign and magnitude of their scaling asymmetry, a property measurable from electrophysiological recordings.

---

### Limitations & open questions

- The paper (and Dabney et al.) uses previously collected data (Eshel et al., 2015) not originally designed to test distributional RL; future experiments designed specifically for this hypothesis would strengthen the evidence.
- It remains unclear why biological brains would implement distributional RL — is it for risk-sensitive choice (as the foraging example implies) or primarily for better sensory representation (as in artificial networks), or both?
- The dispatch does not address whether distributional RL signatures extend beyond VTA to other dopaminergic populations or other neuromodulatory systems.
- The relationship between the population-level distributional code and downstream read-out mechanisms (how the distribution is actually used by target regions) is not discussed.

---

### Connections & keywords

**Key citations**:
- Schultz, Dayan & Montague (1997) — original TD prediction error / dopamine correspondence
- Sutton & Barto (1998) — foundational TD learning framework
- Dabney et al. (2020, Nature) — primary paper being reviewed
- Bellemare, Dabney & Munos (2017) — distributional RL in machine learning
- Dabney et al. (2018, AAAI) — quantile regression distributional RL
- Eshel et al. (2015) — original mouse VTA dopamine recording dataset re-analysed by Dabney et al.
- Fiorillo, Tobler & Schultz (2003) — early evidence for heterogeneous dopamine responses
- Lammel, Lim & Malenka (2014) — heterogeneous midbrain dopamine system

**Named models or frameworks**:
- Temporal difference (TD) learning
- Distributional reinforcement learning
- Quantile regression RL
- TD reward prediction error (RPE)

**Brain regions**:
- Ventral tegmental area (VTA)

**Keywords**:
- distributional reinforcement learning, temporal difference learning, reward prediction error, dopamine neurons, ventral tegmental area, optimistic/pessimistic neurons, quantile coding, reward distribution, RPE asymmetry, reversal point, risk-sensitive decision-making, neuroscience-AI interaction

### Related wiki pages
- [[wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning|Dopamine reward prediction error and temporal-difference learning]]
