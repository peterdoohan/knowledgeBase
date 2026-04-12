---
source_file: schultz1997_neural_substrate_reward_pred.md
paper_id: schultz1997_neural_substrate_reward_pred
title: "A Neural Substrate of Prediction and Reward"
authors:
  - "Wolfram Schultz"
  - "Peter Dayan"
  - "P. Read Montague"
year: 1997
journal: Science
paper_type: review
contribution_type: theoretical
species:
  - monkey
methods:
  - computational_modeling
brain_regions:
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - striatum
  - nucleus_accumbens
  - ventral_tegmental_area
  - substantia_nigra
frameworks:
  - reinforcement_learning
  - temporal_difference_learning
keywords:
  - dopamine
  - prediction_error
  - temporal_difference_learning
  - reinforcement_learning
  - reward_prediction
  - ventral_tegmental_area
  - basal_ganglia
  - conditioning
  - blocking
  - computational_neuroscience
  - neuromodulation
  - actor_critic_model
  - neural
  - substrate
  - prediction
  - reward
wiki_pages:
  - wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning
  - wiki/topics/model_based_vs_model_free_reinforcement_learning_frameworks_in_anterior_cingulate_future_state_control
---

### One-line summary

Dopamine neurons in the primate midbrain encode a temporal difference (TD) prediction error signal that drives reinforcement learning, shifting from responding to primary rewards to reward-predicting cues as learning progresses.

---

### Background & motivation

The ability to predict future events is fundamental to adaptive behavior, allowing animals to prepare responses and make optimal choices. Behavioral studies suggested that learning is driven by changes in expectations about rewards, but the neural substrate remained unclear. Physiological work had identified dopaminergic neurons whose activity correlated with reward processing, but the precise computational nature of this signal was unknown. This paper bridges these experimental findings with reinforcement learning theory to propose that dopamine neurons encode a formal prediction error signal.

---

### Methods

This is a theoretical/review paper that synthesizes existing experimental and computational work:

- Reviews existing electrophysiological recordings from dopamine neurons in alert monkeys performing conditioning tasks
- Synthesizes findings from multiple prior studies by Schultz and colleagues showing dopamine responses to rewards and reward-predicting cues
- Formalizes the connection between observed neural activity and the temporal difference (TD) learning algorithm from reinforcement learning
- Uses computational modeling to demonstrate how TD error signals account for the observed patterns of dopamine activity
- Extends the framework to demonstrate how prediction errors could guide action selection through connection to dynamic programming

---

### Key findings

- Dopamine neurons show phasic activations to primary rewards (fruit juice) in naive animals, but after conditioning, these responses shift to the reward-predicting conditioned stimulus (CS)
- After learning, the primary reward no longer elicits a phasic response if it is fully predicted by the cue
- When an expected reward is omitted, dopamine neurons show a phasic depression below baseline firing rate at the precise time the reward should have occurred, indicating an internal representation of expected reward timing
- Dopamine neurons do not respond to aversive stimuli (air puffs, saline) or discriminate between different types of appetitive stimuli— they encode a scalar "goodness" signal rather than specific reward properties
- The pattern of dopamine activity matches the temporal difference (TD) prediction error: positive when outcomes are better than expected, zero when outcomes match expectations, and negative when outcomes are worse than expected
- The TD framework provides a quantitative account of blocking and secondary conditioning phenomena
- The prediction error signal can be used for both learning predictions (critic) and selecting actions (actor) through connection to dynamic programming

---

### Computational framework

The paper uses **temporal difference (TD) learning**, a reinforcement learning algorithm for learning predictions about future rewards.

**Core formalism:**
- The goal is to learn a value function V(t) that predicts the discounted sum of future rewards: V(t) = E[Σ γⁿ r(t+n)], where γ is a discount factor (0 ≤ γ ≤ 1) and r(t) is reward at time t
- The key insight is that V(t) satisfies a consistency condition: V(t) = E[r(t) + γV(t+1)]
- The TD error δ(t) = r(t) + γV̂(t+1) - V̂(t) provides an instantly available surrogate for the prediction error
- Weights are updated according to: Δwᵢ = αₓ Σₜ xᵢ(t)δ(t), where xᵢ(t) represents sensory cues at different time delays

**Key assumptions:**
- Markov property: future states depend only on current state, not history
- Complete serial-compound stimulus representation: each sensory cue is represented as a vector of signals at different time delays into the future
- Linear value function: V̂(t) = Σ wᵢxᵢ(t)

The framework connects to action selection through dynamic programming, where the TD error serves as an evaluation signal for choosing actions that maximize future rewards.

---

### Prevailing model of the system under study

Prior to this work, the prevailing understanding of dopamine function was primarily based on motivational and hedonic accounts:

- Dopamine neurons were thought to signal primary reward value or pleasure, consistent with their involvement in self-stimulation behavior and drug addiction
- The neurons were viewed as encoding the appetitive properties of stimuli that drive approach behavior
- Dopamine was conceptualized as a general arousal or motivation signal that facilitates motor responses
- The anatomical connectivity to striatum, nucleus accumbens, and frontal cortex was known, but the precise computational nature of the signal was not formalized
- Behavioral theories of reward learning (Rescorla-Wagner, blocking, secondary conditioning) existed but lacked a clear neural substrate

The paper notes that physiological studies had identified dopamine neurons responding to rewards, but the dynamic nature of these responses—shifting from rewards to predictive cues and showing depression at omitted rewards—required a new computational interpretation.

---

### What this paper contributes

This paper provides a formal computational framework that unifies diverse experimental observations about dopamine neuron activity:

- **Quantitative prediction error account**: Demonstrates that dopamine neurons encode a temporal difference (TD) prediction error signal, providing a mathematically precise characterization of what was previously described qualitatively as "reward expectation"

- **Unified explanation of diverse phenomena**: The TD framework explains multiple previously disparate findings: (1) the shift of dopamine responses from primary rewards to reward-predicting cues, (2) the depression of activity at omitted rewards, (3) the dependence on reward timing, and (4) the insensitivity to aversive stimuli

- **Link to reinforcement learning theory**: Connects neurophysiological data to a well-established computational framework (TD learning) that has been extensively studied in engineering and artificial intelligence, enabling cross-disciplinary insights

- **Extension to action selection**: Shows how the same prediction error signal can serve dual purposes—learning predictions (critic) and guiding action choices (actor)—through connection to dynamic programming principles

- **Testable predictions**: The model generates specific predictions about dopamine responses in more complex scenarios, including: (1) responses to multiple sequential cues, (2) depression at omitted intermediate cues, and (3) the re-emergence of reward responses when timing is changed

---

### Brain regions & systems

- **Ventral tegmental area (VTA)**: Primary source of dopamine neurons that encode prediction errors; receives convergent input from cortical regions and outputs a scalar prediction error signal δ(t)
- **Substantia nigra (pars compacta)**: Second major group of dopamine neurons with similar prediction error encoding properties; sends projections to dorsal striatum
- **Striatum (dorsal and ventral)**: Major target of dopamine projections; site where dopamine signals may modulate action selection and plasticity; dopamine synapses contact dendritic spines that also receive cortical excitatory input
- **Nucleus accumbens**: Ventral striatal target of VTA dopamine projections; implicated in motivation and attentional functions
- **Frontal cortex (prefrontal cortex, anterior cingulate cortex)**: Receives dopamine projections; dopamine modulates working memory and cognitive activation; proposed site where prediction errors should be preferentially delivered to regions making the predictions
- **Cortical input regions (M1, M2 in the model)**: Sensory cortical regions that provide input to VTA; modeled as providing temporal derivative signals V̇(t) measuring surprise or change in sensory state

---

### Mechanistic insight

This paper provides strong mechanistic insight by linking a formal computational algorithm to specific neural activity patterns, meeting both criteria for this section.

**Phenomenon**: The phasic responses of midbrain dopamine neurons to reward-related events, and their systematic changes with learning.

**Marr's three levels analysis:**

- **Computational level**: The brain must solve the problem of predicting future rewards to make optimal decisions. The computational goal is to learn a value function V(t) that estimates the discounted sum of future rewards, enabling the animal to evaluate states and choose actions that maximize long-term return. This is an adaptive optimizing control problem faced by any organism that must learn from delayed feedback.

- **Algorithmic level**: The TD learning algorithm implements this computation using (1) a complete serial-compound stimulus representation that tracks cues over time, (2) adaptable weights that store predictions, and (3) a prediction error signal δ(t) = r(t) + γV̂(t+1) - V̂(t) that drives learning. The algorithm uses local weight updates (Δwᵢ = α Σ xᵢ(t)δ(t)) that correlate sensory cues with prediction errors, allowing predictions to converge to true values without requiring storage of complete reward histories.

- **Implementational level**: Dopamine neurons in VTA and substantia nigra physically implement the TD error signal. The VTA receives convergent input from cortex (providing temporal derivative signals V̇(t)) and reward-related inputs (r(t)), and computes δ(t) = r(t) + V̇(t) - b(t) (where b(t) is baseline firing). The phasic dopamine signal is broadcast via widespread axonal projections to target structures (striatum, frontal cortex, nucleus accumbens), where it modulates synaptic plasticity at corticostriatal synapses and influences action selection. The anatomical arrangement of dopamine terminals contacting dendritic spines that also receive cortical input provides a physical substrate for the weight updates posited by the algorithm.

---

### Limitations & open questions

- **Temporal representation**: The model assumes a complete serial-compound stimulus representation (vectors tracking cues at multiple time delays), but the biological implementation of this representation is unknown. Where and how the brain constructs and maintains temporal labels for stimuli remains an open question.

- **Time scales of prediction**: It is unclear how far into the future dopamine-mediated predictions can extend. The time scales that are ethologically important to different species should constrain the search for neural mechanisms, but these limits are not well characterized.

- **Aversive processing**: The model primarily addresses appetitive stimuli. While dopamine neurons do not respond to aversive stimuli, the absence of expected reward may be interpreted as "punishment" by downstream structures. The relationship between dopamine signals and aversive processing, and the neural mechanisms for punishing outcomes, remain unclear.

- **Vector vs. scalar signals**: The model uses a scalar prediction error, but realistic behavior requires discriminating between different types of rewards and different sensory components of predictive stimuli. How the brain disambiguates which stimuli are responsible for fluctuations in the broadcast scalar error signal is unknown.

- **Attentional mechanisms**: The model does not address attentional functions of dopamine-innervated structures (nucleus accumbens, frontal cortex). How attentional mechanisms operate at the level of dopamine neurons, including response decrement to repeated stimuli and generalization to similar stimuli, requires further investigation.

- **Local cortical coupling**: The model suggests that local cortical activity should couple to enhanced sensitivity of nearby dopamine terminals, but the mechanisms underlying this spatial specificity (possibly involving nitric oxide) require further experimental validation.

---

### Connections & keywords

**Key citations:**
- Sutton & Barto (1981, 1987, 1988) - TD learning algorithm and psychological applications
- Rescorla & Wagner (1972) - Classical conditioning model
- Kamin (1969) - Blocking phenomenon
- Schultz et al. (1986, 1990, 1992, 1993, 1994, 1996) - Prior electrophysiological recordings from dopamine neurons
- Montague, Dayan & Sejnowski (1996) - Previous TD model of dopamine activity
- Bellman (1957) - Dynamic programming
- Gallistel (1990) - Organization of learning

**Named models or frameworks:**
- Temporal Difference (TD) learning algorithm
- Rescorla-Wagner rule
- Dynamic programming
- Complete serial-compound stimulus representation
- Actor-critic architecture (implied)
- Blocking paradigm
- Secondary conditioning

**Brain regions:**
- Ventral tegmental area (VTA)
- Substantia nigra (pars compacta)
- Striatum (dorsal and ventral)
- Nucleus accumbens
- Prefrontal cortex
- Anterior cingulate cortex
- Frontal cortex

**Keywords:**
- dopamine
- prediction error
- temporal difference learning
- reinforcement learning
- reward prediction
- ventral tegmental area
- basal ganglia
- conditioning
- blocking
- computational neuroscience
- neuromodulation
- actor-critic model

### Related wiki pages
- [[wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning|Dopamine reward prediction error and temporal-difference learning]]
- [[wiki/topics/model_based_vs_model_free_reinforcement_learning_frameworks_in_anterior_cingulate_future_state_control|Model-based vs model-free reinforcement learning frameworks in anterior cingulate future-state control]]
