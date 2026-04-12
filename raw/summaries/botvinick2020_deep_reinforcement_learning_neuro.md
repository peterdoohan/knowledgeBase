---
source_file: botvinick2020_deep_reinforcement_learning_neuro.md
paper_id: botvinick2020_deep_reinforcement_learning_neuro
title: "Deep Reinforcement Learning and Its Neuroscientific Implications"
authors:
  - "Matthew Botvinick"
  - "Jane X. Wang"
  - "Will Dabney"
  - "Kevin J. Miller"
  - "Zeb Kurth-Nelson"
year: 2020
journal: Neuron
paper_type: review
contribution_type: review
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - prefrontal_cortex
  - orbitofrontal_cortex
  - dorsolateral_prefrontal_cortex
  - striatum
  - ventral_tegmental_area
  - visual_cortex
frameworks:
  - reinforcement_learning
  - model_based_rl
  - successor_representation
  - hierarchical_rl
keywords:
  - deep_reinforcement_learning
  - reward_prediction_error
  - distributional_dopamine
  - meta_reinforcement_learning
  - prefrontal_cortex_working_memory
  - experience_replay_hippocampal_consolidation
  - model_based_versus_model_free_learning
  - representation_learning_reward_shaping
  - hierarchical_reinforcement_learning_cognitive_control
  - explore_exploit_trade_off_intrinsic_motivation
  - successor_representation_navigation
  - temporal_difference_learning_dopamine
  - deep
  - reinforcement
  - learning
  - its
  - neuroscientific
  - implications
key_citations:
  - stachenfeld2017_hippocampus_predictive_map
  - behrens2018_cognitive_map_organizing_knowledge
  - botvinick2009_hierarchically_organized_behavior
---

### One-line summary

Deep reinforcement learning (deep RL) — the integration of deep neural networks with RL — constitutes a new and largely unexplored framework with wide-ranging implications for neuroscience, offering models of how representations are shaped by reward and how those representations in turn support learning and decision making.

---

### Background & motivation

Deep learning and RL have each independently transformed neuroscience: deep networks model neural representations, and RL provides a powerful theory of reward-based learning and dopamine signalling. However, these two frameworks have largely been applied in isolation, and neuroscience has benefited little from the novel computational phenomena that emerge when they are combined. The authors argue that deep RL — in which a deep neural network is trained end-to-end to maximise long-term reward — is genuinely more than the sum of its parts, giving rise to emergent phenomena (meta-learning, distributional coding, hierarchical control, etc.) that neither framework produces alone. A comprehensive neuroscientific engagement with deep RL has barely begun, and this review maps out the opportunities.

---

### Methods

This is a narrative review. It covers:

- A conceptual and historical introduction to RL, deep learning, and their integration into deep RL, including tabular RL, temporal-difference algorithms, the DQN breakthrough (Mnih et al., 2013/2015), and subsequent scaling.
- A survey of vanguard neuroscience studies that have already applied deep RL models (Song et al. 2017; Banino et al. 2018; Wang et al. 2018; Dabney et al. 2020).
- Six thematic sections on forward-looking research opportunities: representation learning, model-based RL, memory, exploration, cognitive control and action hierarchies, and social cognition.
- A final section on challenges and caveats, including sample efficiency, flexible generalisation, temporal credit assignment, biological plausibility of backpropagation, and the engineering–neuroscience mismatch.

The review does not apply systematic inclusion/exclusion criteria; it is a selective, expert-authored synthesis.

---

### Key findings

For a review, key conclusions across the literature:

- **Deep RL is genuinely novel**: integrating deep learning with RL produces emergent phenomena absent from either alone, including meta-RL (Wang et al. 2018) and performance gains from distributional reward coding (Bellemare et al. 2017; Dabney et al. 2020).
- **Meta-RL**: recurrent deep RL networks trained on families of related tasks develop an activity-based fast-learning algorithm spontaneously — slow weight-level RL shapes activation dynamics so that rapid in-context adaptation occurs without further weight changes. This provides a unifying account of puzzling findings in dopamine and prefrontal cortex research.
- **Distributional RL**: expanding the scalar RPE to a vector of pessimistic-to-optimistic channels dramatically improves AI performance and, critically, empirical mouse dopamine recordings are consistent with such a distributional code — individual dopamine neurons appear to carry RPE signals with different implicit reference points.
- **Representation learning**: deep RL systems learn task-relevant internal representations shaped by reward (not just sensory statistics), resonating with neuroscientific evidence that prefrontal representations depend on task and reward contingency.
- **Model-based RL**: deep RL clarifies the interaction between model-free and model-based systems; spontaneous model-based-like behaviour can emerge from model-free training, and the successor representation may be a mechanism for this.
- **Memory**: experience replay in deep RL parallels hippocampal replay; recurrent gating (LSTM/GRU) parallels working memory maintenance; episodic memory architectures support one-shot learning. Non-uniform replay in the brain and in prioritised experience replay serve analogous learning-efficiency functions.
- **Exploration**: deep RL research has produced intrinsic motivation algorithms (novelty, uncertainty, learned curiosity) and meta-RL-based structured exploration that parallel neuroscientific observations about strategic exploration.
- **Cognitive control and hierarchical RL**: multi-level RL architectures recapitulate frontal hierarchy, cost-of-control, automatic vs. controlled processing, and timescale gradients across cortex.
- **Key open questions identified**: sample efficiency vs. humans, flexible structured generalisation, long-term credit assignment, biological plausibility of backpropagation, and bidirectional influence (neuroscience informing AI).

---

### Computational framework

The paper is organised around **deep reinforcement learning** as a unifying framework. Core elements:

- **RL formalism**: an agent in an environment selects actions to maximise cumulative reward; the central quantities are state values V(s), action values Q(s,a), and reward-prediction errors (RPEs) δ = r + γV(s') − V(s).
- **Deep learning**: a deep neural network provides non-linear function approximation, learning representations from raw perceptual inputs via backpropagation.
- **Integration**: the RPE serves as the error signal for backpropagation, updating weights throughout the network. Key stabilisation mechanisms include experience replay and target networks.
- **Distributional RL**: the scalar RPE is replaced by a vector of RPE channels, each learning predictions from different implicit quantiles of the reward distribution, collectively representing the full return distribution.
- **Meta-RL**: a recurrent deep RL system trained on task families develops activation-level fast adaptation; the network's weights constitute a slow outer learner, while activation dynamics constitute a fast inner learner.
- The framework treats representation, learning, and decision making as mutually constitutive rather than independent problems.

---

### Prevailing model of the system under study

As framed in the paper's introduction, the prevailing approach before deep RL entered neuroscience was a **separation of concerns**: supervised deep learning modelled neural representations (largely in sensory cortex) while classical RL (particularly temporal-difference models) accounted for dopaminergic RPE signals and reward-based learning in basal ganglia and prefrontal circuits. Small handcrafted neural networks integrated RL with anatomically-constrained circuit models. The representation problem — how states come to be encoded in ways that support generalisation and task-adaptive behaviour — was largely left unaddressed by RL theory, and the learning problem was largely decoupled from representation in deep learning approaches.

The paper explicitly frames deep RL as filling this gap: neither deep learning alone (no RL) nor RL alone (no deep representation learning) offers models of the mutual shaping of representation and reward-based learning.

---

### What this paper contributes

The review establishes that deep RL offers neuroscience several things that existing frameworks cannot:

1. **A principled account of reward-shaped representation**: deep RL shows how internal representations can be progressively structured by reward signals, providing testable hypotheses about task- and reward-dependent neural coding.
2. **Meta-RL as a unifying account of prefrontal–dopamine interactions**: the meta-RL framework accounts for patterns in dopamine and PFC data that were previously puzzling under classical RL accounts.
3. **The distributional dopamine hypothesis**: deep RL's distributional RPE framework predicted a non-trivial structure in dopamine signals that was subsequently confirmed electrophysiologically.
4. **A taxonomy of open research opportunities**: the review identifies six specific domains (representation learning, model-based RL, memory, exploration, cognitive control, social cognition) where deep RL provides concrete translational leverage.
5. **A call for bidirectional exchange**: neuroscience should not just consume deep RL but actively inform its development, particularly regarding biological constraints that current deep RL violates (backpropagation, sample efficiency, heritability).

---

### Brain regions & systems

- **Ventral tegmental area (VTA) / dopamine neurons** — proposed to carry distributional RPEs rather than a single scalar RPE; central to the meta-RL and distributional RL sections.
- **Prefrontal cortex (PFC)** — proposed locus of meta-RL's fast inner learning algorithm; representations shaped by task and reward; also discussed in the context of cognitive control and hierarchical action organisation.
- **Orbitofrontal cortex (OFC)** — discussed in relation to value coding, specifically Song et al.'s (2017) recurrent deep RL model matching OFC neuron response profiles.
- **Dorsolateral prefrontal cortex** — mentioned in connection with Song et al. (2017) recurrent deep RL fits to neurophysiological data.
- **Hippocampus** — discussed in the memory section: experience replay in deep RL parallels hippocampal replay; episodic memory architectures model hippocampal-dependent rapid learning; successor representation linked to place/grid cells.
- **Entorhinal cortex** — grid-like representations emerging in deep RL navigation agents (Banino et al. 2018) modelled on grid cells.
- **Striatum / basal ganglia** — implicated in model-free RL, habit formation, and the model-free vs. model-based arbitration literature discussed throughout.
- **Primary visual cortex** — cited as evidence that reward contingency shapes even early sensory representations (Pakan et al. 2018).

---

### Mechanistic insight

The paper does not itself present neural data, so the bar for mechanistic insight is not met in the strict sense. However, it reviews two studies that partially meet it:

**Dabney et al. (2020)** — distributional dopamine:
- Computational: the brain represents the full distribution of expected future reward, not just its mean.
- Algorithmic: individual dopamine neurons carry RPE signals referenced to different implicit quantile predictions (pessimistic to optimistic), collectively encoding a distributional value code.
- Implementational: electrophysiological recordings from mouse dopamine neurons show heterogeneous RPE scaling consistent with distributional coding; the decoded reward distribution matches the actual reward distribution of the task.

This comes close to meeting both criteria (a specific algorithm formalised, neural data supporting it over the scalar alternative), but the paper treats it as a summary of one vanguard study rather than presenting primary data itself.

**Wang et al. (2018)** — meta-RL / prefrontal–dopamine:
- Proposes and validates an algorithm (meta-RL via recurrent deep RL) and connects it to dopamine and PFC data, but the neural evidence is correlational (matching patterns) rather than causally isolating the algorithm.

Overall, the review proposes mechanistic hypotheses at the computational and algorithmic levels but does not itself provide the neural data needed to satisfy the implementational level across all topics.

---

### Limitations & open questions

- **Sample efficiency**: deep RL systems require vastly more experience than humans to reach comparable performance, though meta-learning and episodic memory approaches partially close this gap.
- **Flexible structured generalisation**: current deep RL systems struggle to leverage background knowledge for systematic generalisation to genuinely novel situations; humans do this readily.
- **Long-term temporal credit assignment**: attributing current rewards to actions taken far in the past remains unsolved for deep RL.
- **Biological plausibility of backpropagation**: it is unclear how or whether backpropagation is implemented in biological circuits; weight transport, non-locality, and sign symmetry constraints are unresolved.
- **Catastrophic forgetting**: deep RL networks can lose old knowledge when learning new tasks; solutions exist but are imperfect.
- **Engineering–neuroscience mismatch**: most deep RL research is AI-driven and contains mechanisms with no plausible biological counterpart; energy efficiency, heritability, and developmental constraints are not addressed.
- **Causality vs. correlation**: most neuroscience-relevant deep RL studies demonstrate representational correspondence (matching activation patterns) rather than causal mechanistic identity.
- **Inductive biases and architecture choices**: the extent to which architectural biases in deep RL systems (convolution, LSTM gating) correspond to genuine biological inductive biases is an open question.

---

### Connections & keywords

**Key citations**:
- Mnih et al. (2013, 2015) — DQN, deep RL breakthrough
- Wang et al. (2018) — meta-RL and prefrontal–dopamine
- Dabney et al. (2020) — distributional dopamine
- Silver et al. (2016, 2017, 2018) — AlphaGo / AlphaZero, model-based deep RL
- Sutton & Barto (2018) — RL textbook
- Yamins & DiCarlo (2016) — supervised deep learning and ventral stream
- Niv (2009) — RL and dopamine review
- Banino et al. (2018) — grid-like representations in deep RL navigation
- Song et al. (2017) — recurrent deep RL and OFC/PFC unit responses
- Bellemare et al. (2017) — distributional RL framework
- Stachenfeld et al. (2017) — hippocampus as successor representation
- Behrens et al. (2018) — cognitive maps
- Botvinick et al. (2009) — hierarchical RL and PFC

**Named models or frameworks**:
- Deep Q-Network (DQN)
- AlphaGo / AlphaZero
- Meta-reinforcement learning (meta-RL)
- Distributional RL
- Temporal-difference (TD) learning
- Successor representation
- LSTM (long short-term memory)
- Experience replay
- Hierarchical RL / options framework
- Model-free vs. model-based RL dichotomy

**Brain regions**:
- Ventral tegmental area / dopamine neurons
- Prefrontal cortex (dorsolateral and orbitofrontal)
- Hippocampus
- Entorhinal cortex
- Striatum / basal ganglia
- Primary visual cortex

**Keywords**:
- deep reinforcement learning
- reward-prediction error
- distributional dopamine
- meta-reinforcement learning
- prefrontal cortex working memory
- experience replay hippocampal consolidation
- model-based versus model-free learning
- representation learning reward shaping
- hierarchical reinforcement learning cognitive control
- explore-exploit trade-off intrinsic motivation
- successor representation navigation
- temporal-difference learning dopamine
