---
source_file: "roscow2021_memory_replay_learning.md"
paper_id: "roscow2021_memory_replay_learning"
title: "Learning offline: memory replay in biological and artificial reinforcement learning"
authors: "Emma L. Roscow, Raymond Chua, Rui Ponte Costa, Matt W. Jones, Nathan Lepora"
year: 2021
journal: "Trends in Neurosciences"
paper_type: "review"
contribution_type: "review"
species: ["human"]
methods: ["computational_modeling"]
brain_regions: ["hippocampus", "prefrontal_cortex", "striatum", "ventral_tegmental_area", "amygdala", "visual_cortex"]
frameworks: ["reinforcement_learning"]
keywords: ["mnih_et_al_2015_dqn_atari", "silver_et_al_2016_alphago", "mcclelland_et_al_1995_complementary_learning_systems", "wilson_and_mcnaughton_1994_hippocampal_replay_discovery", "lin_1992_experience_replay_in_ai", "schaul_et_al_2016_prioritised_experience_replay", "lee_et_al_2017_generative_replay", "named_models_or_frameworks", "deep_q_network_dqn", "complementary_learning_systems_theory", "reinforcement_learning_rl", "q_learning", "temporal_difference_learning", "experience_replay_prioritised_experience_replay", "generative_replay", "elastic_weight_consolidation", "successor_representations", "predictive_coding", "catastrophic_interference", "brain_regions"]
---

### One-line summary

Replay of past experiences supports learning in both biological brains and artificial neural networks, with complementary progress in neuroscience and AI revealing how replay enables memory consolidation, generalisation, and continual learning.

### Background & motivation

Reinforcement learning (RL) has been studied in both biological and artificial systems, with remarkable success in deep RL for complex tasks. A key technique in both domains is the reactivation of previously experienced episodes, known as replay. In biological systems, replay is important for memory consolidation; in artificial systems, experience replay stabilises learning in deep neural networks. This review explores recent developments in both fields to understand how replay supports learning processes and how insights can be transferred between neuroscience and AI.

### Methods

This is a review article synthesising literature from:
- Neuroscience studies on hippocampal replay in rodents and humans
- Artificial intelligence research on experience replay in deep reinforcement learning
- Computational modelling studies of replay mechanisms
- Comparative analysis of biological and artificial replay implementations

Key experimental approaches reviewed include:
- Electrophysiological recordings of place cells and sharp-wave ripples in rodents
- Human neuroimaging studies of replay during rest and sleep
- Deep Q-networks (DQN) with experience replay buffers
- Generative adversarial networks and autoencoders for generative replay

### Key findings

- Replay is crucial for stabilising learning in deep Q-networks; without experience replay, temporal correlations in training data cause catastrophic forgetting.
- Biological replay occurs during sharp-wave ripples in the hippocampus, typically during rest and non-REM sleep, and often at faster timescales than the original experience.
- Disrupting sharp-wave ripples or replay events impairs spatial memory consolidation on timescales from minutes to days.
- Prioritised experience replay in AI, which samples experiences based on temporal-difference error magnitude, accelerates learning by focusing on surprising or unexpected information.
- Biological replay is biased toward high-reward and high-prediction-error episodes, suggesting similar prioritisation mechanisms exist in the brain, potentially mediated by dopaminergic signals encoding reward-prediction errors.
- Standard experience replay in AI stores exact copies of past experiences in a fixed-capacity buffer, which differs from biological replay where activity patterns are never exactly repeated due to neural stochasticity.
- Generative replay in AI, where networks generate their own training samples rather than storing exact copies, more closely resembles biological replay and shows promise for continual learning without catastrophic forgetting.
- Hippocampal replay can reflect paths never taken by the animal, including shortcuts and reverse trajectories, suggesting the hippocampus generates samples from a learned model rather than simply repeating stored experiences.
- Replay extends beyond the hippocampus to cortical and limbic areas, suggesting a brain-wide phenomenon for reactivating multiple facets of experience including sensory and reward-related information.

### Computational framework

The paper integrates several computational frameworks:

**Reinforcement Learning (RL)**: The paper extensively uses RL as a unifying framework. In RL, agents learn policies for action selection to maximise cumulative reward. Key algorithms discussed include Q-learning, where the Q-value function estimates expected future rewards for state-action pairs, and temporal-difference learning, which updates value estimates based on the difference between successive predictions.

**Experience Replay in Deep Q-Networks (DQN)**: The paper describes how DQN uses a replay buffer to store experience tuples (state, action, reward, next state). During learning, mini-batches are sampled from this buffer to break temporal correlations in training data, preventing catastrophic forgetting and stabilising learning. The Q-value update rule uses the temporal-difference error to adjust the network weights via backpropagation.

**Prioritised Experience Replay**: The paper discusses how sampling experiences based on the magnitude of temporal-difference errors (surprising outcomes) can accelerate learning. This prioritisation focuses computational resources on experiences where the model's predictions are most wrong, analogous to how biological systems may prioritise high-prediction-error episodes.

**Complementary Learning Systems Theory**: This theory proposes that the hippocampus provides fast, pattern-separated learning of individual episodes, while the cortex provides slow, interleaved learning that extracts statistical regularities across episodes. Replay serves as a mechanism for training the cortex on individual episodes from the hippocampus, enabling generalisation and preventing catastrophic interference.

**Generative Models and Generative Replay**: The paper discusses how generative models (e.g., generative adversarial networks, autoencoders) can learn to generate synthetic training data rather than storing exact copies of past experiences. This approach, termed generative replay, more closely resembles biological replay where activity patterns are never exactly repeated due to neural stochasticity. The generator learns the data distribution and produces samples that can be used for continual learning without requiring large memory buffers.

**Predictive Coding and Successor Representations**: The paper mentions predictive coding as a feature of hippocampal activity, where neural representations encode predictions about future states. Successor representations, which encode expected future state occupancies, are proposed as a computational structure that could be replayed to support efficient learning and generalisation in multi-task settings.

### Prevailing model of the system under study

Before this review, the prevailing understanding was that replay serves two primary functions: (1) memory consolidation through Hebbian plasticity between co-reactivated neurons, strengthening synaptic connections formed during recent experiences, and (2) preventing catastrophic interference by interleaving new and old experiences during offline periods. The complementary learning systems theory provided a framework where the fast-learning hippocampus gradually trains the slow-learning cortex through replay, allowing statistical regularities to be extracted while maintaining stable representations.

In the context of reinforcement learning, the prevailing model held that replay supports learning by reactivating state-action-reward associations, allowing value updates to propagate through the neural network. The success of deep Q-networks with experience replay demonstrated that storing exact copies of past experiences and uniformly sampling from a fixed-capacity buffer could effectively stabilise learning in artificial systems.

The review also notes that biological replay was primarily understood as a hippocampal phenomenon occurring during sharp-wave ripples, with the leading hypothesis being that replay induces spike-timing-dependent plasticity at compressed timescales to strengthen recently formed synapses. The causal role of replay in memory consolidation was supported by studies showing that disrupting sharp-wave ripples impairs spatial learning.

### What this paper contributes

This review synthesises recent developments across neuroscience and AI to advance the understanding of replay beyond the prevailing models. Key contributions include:

1. **Bridging biological and artificial replay**: The review establishes that replay is a convergent mechanism across biological and artificial intelligent systems, with complementary progress in both fields offering opportunities for cross-fertilisation. Deep neural networks serve as testable models for replay mechanisms that are difficult to manipulate biologically.

2. **Prioritised replay as a shared principle**: The review highlights that both biological and artificial systems benefit from prioritising certain experiences for replay. In AI, prioritised experience replay based on temporal-difference errors accelerates learning. In biology, replay is biased toward high-reward and high-prediction-error episodes, with dopaminergic signals providing a plausible mechanism for this prioritisation.

3. **Generative replay as a biologically-inspired solution**: The review proposes that generative replay—where networks generate their own training samples rather than storing exact copies—better reflects biological replay and offers solutions to limitations of standard experience replay. Biological replay never exactly repeats past patterns due to neural stochasticity, and can generate novel trajectories (shortcuts, reverse paths) not experienced directly.

4. **Memory buffer limitations and continual learning**: The review identifies key limitations of fixed-capacity memory buffers in AI: (1) inability to represent large state spaces, (2) privacy concerns from storing raw data, and (3) poor performance on continual learning with many sequential tasks. It highlights how neuroscience-inspired approaches (elastic weight consolidation, context-dependent gating, generative replay) offer alternative solutions.

5. **Interleaving and replay statistics**: The review synthesises quantitative findings on replay frequency and content, noting that biological replay shows 0.4–9 replays per online trial depending on reward and prediction error magnitude, with proportions changing over learning. It raises questions about whether biological replay is truly interleaved or consists of massed repetitions, and how interleaving may occur at cortical rather than hippocampal levels.

6. **Future directions and outstanding questions**: The review identifies critical open questions, including: the extent to which replay reflects individual episodes versus aggregated statistics; how replay propagates through cortical-subcortical networks; how replay of newer versus older information supports learning; and how replay can support transfer learning and hierarchical RL.

### Brain regions & systems

- **Hippocampus** — primary locus of replay events; contains place cells that encode spatial locations and are reactivated during sharp-wave ripples during rest and sleep; serves as fast learner for episodic memories in complementary learning systems theory.
- **Prefrontal cortex** — involved in encoding task states and cognitive maps; exhibits replay of rule-learning related neural patterns; receives replayed information from hippocampus and may participate in bidirectional replay interactions.
- **Visual cortex** — shows coordinated memory replay with hippocampus during sleep; involved in processing visual components of reactivated experiences.
- **Striatum (ventral)** — involved in representing action-specific reward values; shows preferential reactivation of motivationally relevant information; proposed site for updating stored action values during replay.
- **Ventral tegmental area (VTA)** — source of dopaminergic reward-prediction error signals; coordinates with hippocampal reactivation of spatial experience; proposed to modulate replay via dopaminergic influences on plasticity.
- **Amygdala** — involved in emotional memory reactivation during sleep; part of the broader limbic system showing replay-related activity.
- **Cortical networks (general)** — slow learner in complementary learning systems theory; destination for hippocampal replay that enables extraction of statistical regularities and generalisation across episodes.

### Mechanistic insight

This review does not present new mechanistic insights with accompanying neural data; rather, it synthesises existing evidence for mechanisms proposed across the literature. The paper meets the criteria for mechanistic insight at the level of reviewing and integrating proposed mechanisms, though it does not provide new experimental data testing specific algorithms against neural data.

**Computational level**: The review articulates that the brain solves the problem of learning stable representations from limited, correlated experiences while avoiding catastrophic interference. Replay serves to interleave experiences that would otherwise be temporally correlated, allowing the system to learn from a more representative distribution of state-action-reward transitions. The problem is framed within reinforcement learning, where the goal is to maximise cumulative reward through optimal action selection.

**Algorithmic level**: The review describes several algorithmic implementations of replay:

1. **Experience replay in Deep Q-Networks (DQN)**: Experiences (state, action, reward, next state) are stored in a fixed-capacity buffer and sampled uniformly for training. The Q-value update rule is: Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)], where the temporal-difference error drives weight updates via backpropagation.

2. **Prioritised experience replay**: Samples are drawn from the buffer with probability proportional to the magnitude of their temporal-difference error, focusing learning on surprising or unexpected transitions.

3. **Generative replay**: A generative model (e.g., GAN, autoencoder) learns the data distribution and generates synthetic samples for replay, rather than storing exact copies of past experiences. This more closely resembles biological replay where patterns are never exactly repeated.

4. **Hippocampal replay**: Sequential reactivation of place cells during sharp-wave ripples, potentially implementing a form of prioritized or generative replay biased by reward and prediction error signals.

**Implementational level**: The review discusses biological implementation through:
- Sharp-wave ripples in the hippocampus that synchronously excite large neuronal populations
- Spike-timing-dependent plasticity during replay that strengthens synaptic connections
- Dopaminergic modulation from VTA that may bias replay toward high-reward or high-error episodes
- Bidirectional interactions between hippocampus and cortex during replay events

For AI systems, implementation involves:
- Memory buffers storing experience tuples
- Sampling algorithms (uniform or prioritized)
- Backpropagation for weight updates
- Generative models for synthetic data generation

The review does not provide new neural data testing specific algorithmic predictions, but synthesises existing evidence for these mechanisms across both fields.

### Limitations & open questions

- Most biological replay studies focus on single tasks/environments; multi-task continual learning experiments are needed to test predictions about interleaving and catastrophic interference.
- Disruption studies in biology have largely used broad ripple disruption rather than selective manipulation of specific replay content; definitive evidence would require inducing specific replay events from scratch.
- Quantifying replay remains inconsistent across studies; lack of standardised definitions and measurement methods limits comparability.
- The extent to which biological replay reflects individual episodes versus aggregated statistics is unclear.
- How replay propagates through cortical and subcortical networks and how different brain areas interact during replay events remains poorly understood.
- Whether replay can originate in sensory cortices, higher-order areas (hippocampus, prefrontal cortex), or output areas (striatum) and how this influences learning is unknown.
- Whether update rules differ for online versus replayed experiences, and for wake versus sleep replay, is unresolved.
- How generative replay can be scaled to support continual learning of complex, sequential tasks in AI remains an open challenge.
- Privacy and ethical concerns with explicit storage of training data in AI replay buffers need addressing.
- Most continual learning approaches assume discrete, well-defined tasks; autonomous agents facing continuous unsupervised learning in the real world present unsolved challenges.

### Connections & keywords

**Key citations:**
- Mnih et al. 2015 (DQN/Atari)
- Silver et al. 2016 (AlphaGo)
- McClelland et al. 1995 (complementary learning systems)
- Wilson & McNaughton 1994 (hippocampal replay discovery)
- Lin 1992 (experience replay in AI)
- Schaul et al. 2016 (prioritised experience replay)
- Lee et al. 2017 (generative replay)

**Named models or frameworks:**
- Deep Q-Network (DQN)
- Complementary learning systems theory
- Reinforcement learning (RL)
- Q-learning
- Temporal-difference learning
- Experience replay / Prioritised experience replay
- Generative replay
- Elastic weight consolidation
- Successor representations
- Predictive coding
- Catastrophic interference

**Brain regions:**
- Hippocampus
- Prefrontal cortex
- Visual cortex
- Striatum (ventral)
- Ventral tegmental area (VTA)
- Amygdala
- Cortex (general)

**Keywords:**
- memory replay
- experience replay
- reinforcement learning
- deep reinforcement learning
- hippocampus
- place cells
- sharp-wave ripples
- memory consolidation
- catastrophic forgetting
- continual learning
- generative replay
- complementary learning systems
- temporal-difference error
- Q-learning
- dopamine
- reward-prediction error
