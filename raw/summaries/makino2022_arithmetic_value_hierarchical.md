---
source_file: makino2022_arithmetic_value_hierarchical.md
paper_id: makino2022_arithmetic_value_hierarchical
title: "Arithmetic value representation for hierarchical behavior composition"
authors:
  - "Hiroshi Makino"
year: 2022
journal: "Nature Neuroscience"
paper_type: computational
contribution_type: theoretical
species:
  - mouse
methods:
  - calcium_imaging
  - behavioral_analysis
brain_regions:
  - striatum
  - retrosplenial_cortex
frameworks:
  - reinforcement_learning
  - hierarchical_rl
  - neural_manifold
keywords:
  - hierarchical_reinforcement_learning
  - action_value_function_q_function
  - behavioral_composition
  - soft_actor_critic_sac
  - maximum_entropy_policy
  - two_photon_calcium_imaging
  - cortex_wide_mesoscale_imaging
  - intrinsic_neural_manifold
  - policy_transfer
  - policy_entropy
  - few_shot_learning
  - generalized_linear_model_glm
  - arithmetic
  - value
  - representation
  - hierarchical
  - behavior
  - composition
wiki_pages:
  - wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning
---

### One-line summary

Mice compose a novel hierarchical task by additively combining cortical action-value (Q) representations from previously learned subtasks, mirroring the arithmetic Q-averaging operation identified in deep reinforcement learning agents.

---

### Background & motivation

A hallmark of biological intelligence is the ability to recombine previously acquired skills to solve new, unseen tasks — yet the neural mechanism by which the brain achieves this "behavioral composition" is largely unknown. In the AI field, deep reinforcement learning (deep RL) has shown that independently learned Q-functions from subtasks can be linearly averaged to derive a near-optimal policy for a composite downstream task, a process that depends on maximum-entropy (stochastic) subpolicies. Whether the brain uses an analogous arithmetic operation on action-value representations had not been empirically tested. This paper asks whether mouse cortex encodes compositional Q functions in a way consistent with the averaging principle established computationally, and whether behavioral variability (policy entropy) similarly facilitates composition in biological agents.

---

### Methods

- **Model architecture**: Deep RL agents were trained using the Soft Actor-Critic (SAC) algorithm — a model-free, off-policy, maximum-entropy actor-critic algorithm — with a neural network of 3 hidden layers (256 units each) for both actor and critic.
- **Task design**: Mice and deep RL agents learned two subtasks (Task 1: joystick-driven object manipulation to a reward zone; Task 2: licking a water spout on a stationary LED-attached object) before being introduced to a composite task requiring both skills in sequence.
- **Behavioral variables**: Action-value functions Q(s,a) and state-value functions V(s) were estimated from behavior (trial duration, correct rate) using a temporal discounting model (γ = 0.99 for mice, 0.95 for agents).
- **Neural recordings**: Cortex-wide two-photon calcium imaging via a random-access mesoscope (2p-RAM) in transgenic mice (CaMKII-tTA × TRE-GCaMP6s) imaged thousands of layer 2/3 excitatory neurons across M1, M2, S1, RSC, and PPC simultaneously.
- **Neural analysis**: Generalized linear models (GLMs) were built for individual neurons to decode encoding of task variables (position, direction, lick). Q-function-representing neurons were identified by correlating neural tuning with the behaviorally estimated Q function. Population manifold structure was compared across tasks using KL-divergence estimation.
- **Policy entropy manipulation**: A separate cohort of mice was trained with a fixed initial object position to induce more deterministic policies, allowing comparison with standard (stochastic) policy mice in composite task learning.
- **Deep RL ablations**: Q-subtask-encoding neurons in the ANN were inactivated (50% or 100%) to test their causal role in composite task learning.

---

### Key findings

- Mice with subtask pretraining learned the composite task in approximately one session, whereas naive mice (trained from scratch) showed substantially slower acquisition (P < 0.001, n = 6–7 mice per group).
- In deep RL agents, initializing the composite Q function by **averaging** the two subtask Q functions (Q_Composite = (Q_Task1 + Q_Task2)/2) produced rapid learning; initializing by taking the **maximum** of Q_Subtask did not (P < 0.001 vs scratch for average; P = 0.89 vs scratch for maximum).
- Fractions of Q_Task1- and Q_Task2-encoding cortical neurons increased over subtask learning (Task 1: P = 0.004; Task 2: P = 0.04), with functionally segregated cortical distributions (Q_Task1 enriched in PPC; Q_Task2 enriched in M2).
- Q_Subtask representations were retained in individual cortical neurons during the early composite task phase (Q_Task1-encoding neurons: 8.3%, above chance of 5.3%, P < 0.001), with stable cortical distribution across subtasks and composite task (R² = 0.98 for Task 1, R² = 0.76 for Task 2).
- Mixed Q_Composite representations — single neurons spatially tuned to high-value states from both subtasks simultaneously — were observed in cortex at the early composite stage (20.7% of neurons, above chance of 16.1%, P = 0.006), consistent with averaging of Q_Subtask functions.
- Population manifold analysis showed that intrinsic neural population geometry was preserved between subtask expert stages and composite task early stage (KL divergence significantly lower than shuffled baseline, P < 0.001), while subtask learning itself caused major manifold restructuring.
- Over composite task learning, Q representations transitioned from dedicated (subtask-segregated) to distributed (cross-cortical) circuits; this redistribution in mice was predicted with R² = 1.0 by the redistribution observed in ANN subnetworks (P < 0.001).
- Ablating Q_Subtask-encoding neurons in the ANN decelerated composite task learning (full ablation: P < 0.001; 50% ablation: P = 0.006); control ablation did not (P = 0.83).
- Policy entropy during subtask pretraining predicted composite task performance across individual mice (R² = 0.57, P < 0.001, n = 15 mice). Mice trained with deterministic policies (fixed initial position) learned the composite task more slowly (P < 0.001).
- Neurons in mice and ANNs trained with higher-entropy policies showed broader directional tuning (P < 0.001 by KS test), providing a mechanistic link between policy stochasticity and compositional flexibility.

---

### Computational framework

**Framework**: Maximum-entropy deep reinforcement learning (Soft Actor-Critic, SAC); hierarchical policy composition via arithmetic Q-function averaging.

The paper formalises behavioral composition through the Q-averaging principle from the RL literature: given K independently trained maximum-entropy subpolicies, the composite Q function Q_Composite is approximated by:

Q_Sigma = (1/|C|) * sum_i Q*_i

This approximation is near-optimal when constituent subpolicies agree on an action or are indifferent to each other's actions. The SAC objective additionally maximises policy entropy H(pi), weighted by temperature alpha, encouraging broad, stochastic subpolicies that maintain exploratory capacity when transferred to novel composite tasks.

Key variables: state s (object position), action a (movement direction or lick), Q(s,a) (expected future reward for action a in state s under policy pi), V(s) (state-value function), pi (stochastic policy), H (policy entropy).

Key assumption: action spaces of constituent subtasks are independent, so averaging Q functions over the combined action space decomposes cleanly.

---

### Prevailing model of the system under study

The paper's introduction signals that the prevailing view in neuroscience is that behavioral composition — the ability to build new skills from preacquired primitives — is well-studied in AI but poorly understood mechanistically in the brain. The actor-critic framework (with basal ganglia, especially striatum, as the substrate for value-based learning) is the dominant model for reward-based action selection. The cortex is not traditionally the focus of action-value representation; instead, value signals are usually attributed to striatum and midbrain dopamine systems. The literature had not established whether the brain uses a linear arithmetic operation on prelearned action-value representations, nor had it tested the algorithmic parallel between maximum-entropy RL and behavioral variability in biological systems. The introduction thus establishes a gap: computational theory predicts Q-averaging and stochastic policies should enable composition, but no neural evidence had been provided.

---

### What this paper contributes

The paper provides the first empirical evidence that the mouse cortex encodes combinatorial action-value representations consistent with an arithmetic (averaging) operation on prelearned subtask Q functions. Specifically:

1. Cortical neurons retain subtask-specific Q representations when transferred to a composite task, and novel mixed-Q neurons emerge that are tuned to high-value states from both subtasks simultaneously — a signature predicted by Q-averaging but not Q-maximisation.
2. The geometric structure of population activity (intrinsic manifold) is preserved across subtask and composite task contexts, providing a mechanistic basis for sample-efficient transfer learning: the brain does not need to restructure its representational geometry, only fine-tune existing circuits.
3. The transition from dedicated to distributed Q representations over composite task learning closely mirrors what occurs in deep RL ANN subnetworks, strengthening the algorithmic analogy.
4. Policy stochasticity during pretraining causally improves composite task learning in mice (not just in agents), and this is mediated by broader directional tuning of individual cortical neurons — a formal account of why behavioral variability facilitates learning.
5. The paper implicates cortex (not only striatum/basal ganglia) as a site of action-value coding, with distinct functional parcellation (PPC for object-movement Q values, M2 for lick Q values).

---

### Brain regions & systems

- **Primary motor cortex (M1)** — imaged as part of cortex-wide mesoscale recording; contains Q_Task1- and Q_Task2-encoding neurons but not at the highest fractions.
- **Secondary motor cortex (M2)** — enriched in Q_Task2 (lick-related) encoding neurons; aligns with known role of anterior lateral motor cortex in licking behavior.
- **Primary somatosensory cortex (S1)** — imaged; contains Q-encoding neurons at intermediate fractions.
- **Retrosplenial cortex (RSC)** — imaged; enriched in Q_Task1-encoding neurons at expert stage.
- **Posterior parietal cortex (PPC)** — most enriched region for Q_Task1 (object manipulation) representations; consistent with the author's prior work showing PPC is critical for the object manipulation task.
- **Basal ganglia / striatum** — discussed in the context of the actor-critic model as the canonical locus of value learning; the paper argues cortical neurons play an additional role beyond classical striatal accounts.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight: it formalises an algorithm (Q-averaging) and provides neural data (calcium imaging) that specifically supports that algorithm over alternatives (Q-maximisation).

**Computational level**: The brain solves the problem of rapidly composing a new behavioural policy from previously learned subtask policies, without needing extensive re-training. The goal is near-optimal performance in the composite task with minimal additional experience (few-shot learning).

**Algorithmic level**: The solution is arithmetic averaging of prelearned action-value functions: Q_Composite(s,a) ≈ (Q_Task1(s,a) + Q_Task2(s,a)) / 2. This is instantiated in cortical circuits as follows: (1) individual neurons retain their subtask Q-tuning (dedicated phase), (2) a subset of neurons develops mixed representations correlated with both subtask Q functions simultaneously (Q-averaging signature), and (3) over fine-tuning, representations redistribute from dedicated subtask circuits to shared composite circuits. The preservation of intrinsic population manifolds across task contexts enables this reuse without costly representational restructuring. Maximum-entropy (stochastic) subpolicies are also required: they produce broadly tuned Q representations over actions, enabling flexible policy adjustment in the composite task.

**Implementational level**: Layer 2/3 excitatory cortical neurons (CaMKII-positive) across a distributed, functionally parcellated network implement this computation. Q_Task1 is preferentially encoded in PPC; Q_Task2 in M2; the composite Q redistributes across all imaged areas. The paper does not resolve specific cell types, connectivity, or neuromodulators beyond the excitatory L2/3 identification.

---

### Limitations & open questions

- The paper studied only a small number of cortical regions (M1, M2, S1, RSC, PPC) — contributions from striatum, prefrontal cortex, hippocampus, or subcortical structures were not examined and could also contribute to behavioral composition.
- The arithmetic averaging account is consistent with the data but not uniquely proven — the paper acknowledges that the brain might additionally construct dynamic models of the environment to further improve learning, as suggested by the MBPO result in agents.
- The mechanism by which the brain selects which prelearned policies to combine in a novel context is not addressed (the paper raises this as an open question, noting the prefrontal cortex and meta-learning may be relevant).
- Only layer 2/3 excitatory neurons were imaged; inhibitory interneurons and deeper layers were not examined, leaving the circuit-level implementation underspecified.
- Generalisation: the paradigm involves only two subtasks combined into one composite task. Whether the arithmetic principle scales to more subtasks, or to more complex skill hierarchies, remains untested.
- The manipulation to induce deterministic policies (fixed initial position) may have reduced statistical features of the environment beyond policy entropy, complicating causal interpretation.
- Imaging was performed under head-fixation; whether the same mechanism generalises to freely moving animals or more naturalistic behaviors is unknown.

---

### Connections & keywords

**Key citations**:
- Haarnoja et al. 2018 (arXiv:1803.06773) — composable deep RL for robotic manipulation; source of the Q-averaging principle and composability theory
- Haarnoja et al. 2018 (SAC algorithm, arXiv:1801.01290; arXiv:1812.05905) — Soft Actor-Critic algorithm
- Suhaimi et al. 2022 (Sci. Adv.) — prior work by same lab on representation learning in object manipulation task
- Botvinick, Niv & Barto 2009 (Cognition) — hierarchical RL and its neural foundations
- Sadtler et al. 2014 (Nature) — neural constraints on learning via intrinsic manifold structure
- Cross et al. 2021 (Neuron) — human PPC activity resembles deep Q-network representations
- Wu et al. 2014 (Nat. Neurosci.) — behavioral variability and motor learning in biological systems
- Janner et al. 2019 (NeurIPS) — model-based policy optimization (MBPO)

**Named models or frameworks**:
- Soft Actor-Critic (SAC)
- Model-Based Policy Optimization (MBPO)
- Maximum entropy reinforcement learning
- Q-averaging / hierarchical policy composition
- Actor-critic model

**Brain regions**:
- Primary motor cortex (M1)
- Secondary motor cortex (M2)
- Primary somatosensory cortex (S1)
- Retrosplenial cortex (RSC)
- Posterior parietal cortex (PPC)
- Basal ganglia / striatum (discussed, not recorded)

**Keywords**:
- hierarchical reinforcement learning
- action-value function (Q function)
- behavioral composition
- Soft Actor-Critic (SAC)
- maximum entropy policy
- two-photon calcium imaging
- cortex-wide mesoscale imaging
- intrinsic neural manifold
- policy transfer
- policy entropy
- few-shot learning
- generalized linear model (GLM)

### Related wiki pages
- [[wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning|Task-state representation and hidden-state inference in orbitofrontal–hippocampal reinforcement learning]]
