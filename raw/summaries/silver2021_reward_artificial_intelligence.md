---
source_file: silver2021_reward_artificial_intelligence.md
paper_id: silver2021_reward_artificial_intelligence
title: "Reward is enough"
authors:
  - "David Silver"
  - "Satinder Singh"
  - "Doina Precup"
  - "Richard S. Sutton"
year: 2021
journal: "Artificial Intelligence"
paper_type: review
contribution_type: theoretical
frameworks:
  - reinforcement_learning
keywords:
  - artificial_general_intelligence
  - reinforcement_learning
  - reward_maximisation
  - reward_hypothesis
  - agent_environment_framework
  - computational_rationality
  - multi_agent_systems
  - transfer_learning
  - observational_learning
  - language_emergence
  - generalisation
  - knowledge_representation
  - alphazero
  - bounded_rationality
  - content
  - reward
  - enough
---

### One-line summary

Intelligence and its associated abilities can be understood as subserving the maximisation of reward by an agent acting in its environment.

---

### Background & motivation

The paper addresses the fundamental question of what drives intelligent behavior in natural and artificial agents. Traditional approaches often treat each ability associated with intelligence (perception, language, social intelligence, motor control) as requiring its own specialized problem formulation and objective. The authors propose an alternative hypothesis: that a singular objective of reward maximisation may be sufficient to drive behavior exhibiting most if not all abilities studied in natural and artificial intelligence.

---

### Methods

This is a conceptual/theoretical paper that:

- Formalises intelligence as the computational part of the ability to achieve goals in the world (following McCarthy)
- Adopts the reinforcement learning framework: an agent interacts with an environment, receiving observations and rewards
- Defines the reward-is-enough hypothesis: intelligence and associated abilities can be understood as subserving reward maximisation
- Examines specific abilities (knowledge, learning, perception, social intelligence, language, generalisation, imitation, general intelligence) through the lens of reward maximisation
- Discusses reinforcement learning agents as a practical implementation pathway

---

### Key findings

- **Knowledge and learning**: Both innate and learned knowledge can be understood as serving reward maximisation. Rich environments demand learned knowledge because the space of potential knowledge exceeds agent capacity, requiring adaptation to specific circumstances.

- **Perception**: Perceptual abilities (object recognition, scene parsing, speech recognition) can arise implicitly from reward maximisation rather than requiring separate supervised learning objectives. The utility of perception is context-dependent and intertwined with action.

- **Social intelligence**: Rather than requiring game-theoretic equilibrium concepts, social intelligence can emerge from a single agent maximising reward in an environment containing other agents. The agent learns to anticipate and influence others' behavior to maximise its own cumulative reward.

- **Language**: Full linguistic abilities (beyond just statistical language modelling) can emerge from reward maximisation, as language serves practical purposes: influencing others' mental states and behavior, predicting future rewards, and enabling cooperation.

- **Generalisation**: Rather than requiring explicit transfer learning mechanisms, generalisation can emerge naturally from maximising reward in a continuing stream of experience within a single complex environment where the agent encounters varied situations over time.

- **Imitation**: Observational learning (broader than behavioural cloning) can emerge from reward maximisation as the agent observes other agents as part of its environment and learns associations between its own states/actions and those of others.

- **General intelligence**: The ability to flexibly achieve varied goals in different contexts can emerge from maximising a singular reward in a sufficiently rich environment, as the environment demands diverse subgoals in service of the main objective.

---

### Computational framework

**Reinforcement learning (RL)**

The paper adopts the reinforcement learning framework as the formalism for understanding intelligence:

- **Agent**: A system that receives observations and outputs actions based on its history of experience
- **Environment**: A system that receives actions and responds with observations and rewards
- **Reward**: A scalar feedback signal that provides instantaneous measurement of progress toward a goal
- **Objective**: Maximise cumulative reward (sum, discounted sum, or average)

The key insight is that this framework is both general (can represent diverse goals and environments) and practical (can be solved through learning algorithms). The paper conjectures that agents that learn to maximise reward through trial-and-error experience can acquire sophisticated intelligence.

---

### Prevailing model of the system under study

The prevailing approach in AI research has been to treat different abilities associated with intelligence as requiring separate problem formulations and specialised objectives:

- **Perception**: Historically formulated as separate problems (object recognition, segmentation, speech recognition), more recently unified under supervised learning (minimising classification error)
- **Language**: Studied through separate subproblems (parsing, part-of-speech tagging, sentiment analysis, machine translation)
- **Social intelligence**: Formalised using game theory as Nash equilibrium of multi-agent systems
- **Generalisation**: Studied as transfer learning between distinct tasks or environments
- **Imitation**: Formalised as behavioural cloning from demonstration data

This prevailing view treats each ability as the solution to its own specialised goal, rather than understanding how diverse abilities might arise from a singular objective.

---

### What this paper contributes

This paper challenges the prevailing view by proposing that a singular objective—reward maximisation—may be sufficient to give rise to most if not all abilities associated with intelligence:

1. **Unifying hypothesis**: Intelligence and its associated abilities can be understood as subserving the maximisation of reward by an agent acting in its environment. This provides a singular foundation for understanding diverse cognitive abilities.

2. **Explanation of "why"**: Unlike specialised formulations that focus on what each ability does, reward maximisation explains why abilities arise—they serve pragmatic goals in specific environments.

3. **Integration mechanism**: A singular objective naturally addresses how diverse abilities are integrated— they all serve the same overarching goal.

4. **Pathway to AGI**: The paper conjectures that powerful reinforcement learning agents learning to maximise reward could constitute a solution to artificial general intelligence. This provides a concrete research direction.

5. **Reinterpretation of specific abilities**: The paper demonstrates how knowledge, perception, social intelligence, language, generalisation, imitation, and general intelligence can each be understood through the lens of reward maximisation.

---

### Brain regions & systems

Not applicable. This is a theoretical/artificial intelligence paper focused on computational principles rather than biological neural systems. The paper discusses natural intelligence as an existence proof that reward maximisation can produce sophisticated abilities, but does not focus on specific brain regions or neural circuits.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined in the summary template. It is a theoretical/conceptual paper that proposes a unifying framework rather than presenting a specific algorithm with neural data supporting it over alternatives.

The paper proposes that reward maximisation could explain intelligence at Marr's computational level (what problem is being solved and why), but does not specify the algorithmic level (what representations and processes implement the solution) or the implementational level (how this is realised in neural hardware) for natural intelligence. For artificial intelligence, the paper points to reinforcement learning as a general algorithmic approach but does not commit to specific implementations.

---

### Limitations & open questions

1. **Sample efficiency**: The paper explicitly notes it does not offer theoretical guarantees on sample efficiency. The rate and degree to which abilities emerge will depend on environment, learning algorithm, and inductive biases.

2. **Learning mechanism**: The paper does not specify how to learn to maximise reward effectively in practice. It notes this is the central question of the reinforcement learning field but does not resolve it.

3. **Environment specificity**: The specific abilities that emerge depend on the environment. The paper conjectures that general intelligence can emerge from maximising reward in sufficiently rich environments, but does not specify what "sufficiently rich" means.

4. **Counterexamples**: The paper acknowledges one can construct artificial environments where learning will fail, but argues that in complex, realistic environments, reward maximisation will give rise to intelligence.

5. **Alternative formulations**: The paper discusses and dismisses several alternatives (unsupervised learning, supervised learning, evolution, offline learning) but acknowledges these may have value in specific contexts.

---

### Connections & keywords

**Key citations:**
- Sutton & Barto (2018) - Reinforcement Learning: An Introduction (foundational RL text)
- Silver et al. (2017) - AlphaGo/Mastering Go without human knowledge
- Silver et al. (2018) - AlphaZero/mastering chess and shogi
- Nash (1950) - Equilibrium points in n-person games (game theory)
- McCarthy (1998) - Definition of intelligence
- Simon (1955) - Bounded rationality
- Hutter (2005) - Universal Artificial Intelligence
- Chomsky (2002) - Syntactic Structures (language)
- Mnih et al. (2015) - DQN/Human-level control through deep RL

**Named models or frameworks:**
- Reinforcement learning (RL) framework
- Agent-environment protocol
- Reward-is-enough hypothesis
- AlphaZero/AlphaGo (as practical examples)
- Nash equilibrium (contrasted approach)
- Behavioural cloning (contrasted approach)
- Computational/bounded rationality (related framework)

**Brain regions:**
- Not applicable (theoretical AI paper)

**Keywords:**
- artificial general intelligence
- reinforcement learning
- reward maximisation
- reward hypothesis
- agent-environment framework
- computational rationality
- multi-agent systems
- transfer learning
- observational learning
- language emergence
- generalisation
- knowledge representation
- AlphaZero
- bounded rationality
</content>