---
source_file: barreto2017_successor_features_transfer_c.md
title: Successor Features for Transfer in Reinforcement Learning
authors: André Barreto, Will Dabney, Rémi Munos, Jonathan J. Hunt, Tom Schaul, Hado van Hasselt, David Silver
year: 2017
journal: Advances in Neural Information Processing Systems (NIPS 2017)
paper_type: computational
contribution_type: theoretical
---

### One-line summary

Successor features (SFs) combined with generalized policy improvement (GPI) provide a principled, theoretically grounded framework for transfer across reinforcement learning tasks that share dynamics but differ in reward function, with formal performance guarantees before any learning on a new task.

---

### Background & motivation

Transfer in RL — reusing knowledge from previously learned tasks to accelerate performance on new ones — is desirable but lacks a principled, general-purpose solution. Most prior approaches either impose rigid information-flow structures (e.g. strict hierarchies) or are not deeply integrated into the RL framework itself. A key bottleneck is that standard value functions entangle environmental dynamics and reward, so a change in reward invalidates everything learned. This paper addresses that entanglement directly, aiming for a transfer method that is both theoretically grounded and seamlessly compatible with existing RL algorithms.

---

### Methods

- **Setting**: Multi-task RL where the MDP dynamics are fixed but the reward function changes across tasks; rewards are assumed to decompose as an inner product r(s,a,s') = φ(s,a,s')⊤w, where φ are fixed features and w encodes task identity.
- **Successor features (SFs)**: Generalisation of Dayan's successor representation (SR) to continuous spaces and function approximation. SFs ψ^π(s,a) capture the expected discounted future occupancy of features φ under policy π, decoupling dynamics from rewards so that Q^π(s,a) = ψ^π(s,a)⊤w.
- **Generalized policy improvement (GPI)**: Extension of Bellman's policy improvement theorem from a single policy to a set of n policies; acting greedily with respect to max_i Q^π_i(s,a) yields a policy no worse than any individual π_i (Theorem 1).
- **Transfer mechanism**: When a new task w_{n+1} arrives, stored SFs {ψ^π_j} from past tasks immediately yield Q-function estimates Q^π_j_{n+1}(s,a) = ψ^π_j(s,a)⊤w_{n+1} via a simple dot product; GPI then selects the best composite policy. Learning w_{n+1} is reduced to supervised regression.
- **Theoretical guarantee (Theorem 2)**: The GPI policy's suboptimality is bounded by 2φ_max · min_j ||w_i − w_j|| / (1−γ) plus approximation error, formalising that performance improves the more similar the new task is to a previously seen one.
- **Experiments**:
  - *Four-room navigation*: 2D continuous environment, objects of 3 classes with rewards sampled from U[−1,1], sequence of 250 tasks changing every 20,000 transitions. Methods compared: Q-learning (QL), probabilistic policy reuse (PRQL), SFQL-φ (oracle features), SFQL-h (learned features of dimension h).
  - *Reacher domain (MuJoCo)*: Two-joint robotic arm, 12 target locations, agents trained on 4 tasks and tested on remaining 8; baseline DQN vs. SFDQN (SFs combined with DQN).

---

### Key findings

- All SFQL variants significantly outperformed QL and PRQL in the four-room domain; SFQL improved average return by >100% relative to PRQL, which itself improved ~100% over QL.
- SFQL-h (learned features) achieved good performance faster than SFQL-φ (oracle features), possibly because learned features φ̃ are dense across state space, providing a richer pseudo-reward signal.
- In the reacher domain, SFDQN achieved near-optimal performance on training tasks and simultaneously improved performance on unseen test tasks during training, demonstrating genuine generalisation across the task space.
- GPI enables performance on never-trained tasks through combinatorial reuse of stored SFs, illustrating that the library of SFs functions as a set of reusable skills covering the task space.
- The framework integrates naturally with deep RL (DQN), showing scalability beyond tabular or linear settings.

---

### Computational framework

**Reinforcement learning / dynamic programming**, with a linear value-function decomposition.

Core formalism: An MDP M = (S, A, p, R, γ) is embedded in a family M^φ of MDPs sharing dynamics p but parameterised by a reward weight vector w ∈ R^d via r(s,a,s') = φ(s,a,s')⊤w. The successor features ψ^π(s,a) ∈ R^d satisfy a vector-valued Bellman equation with φ in the role of rewards, allowing any RL method to learn them. The value function decomposes as Q^π(s,a) = ψ^π(s,a)⊤w. Key assumptions: (1) reward linearity in fixed features φ; (2) shared transition dynamics across tasks; (3) approximate computation of both ψ and w is permissible and handled by existing error bounds.

---

### Prevailing model of the system under study

Prior to this paper, transfer in RL was generally treated as a supplementary engineering problem rather than something derivable from the RL formalism itself. The dominant framing was task-similarity-based reuse: store old policies or value functions and re-deploy them via heuristic selection mechanisms (e.g. probabilistic policy reuse), or hand-design hierarchical structures. Dayan's (1993) successor representation was a known factorisation of the value function but had been applied only in tabular, discrete settings and was not connected to a multi-task transfer theory. The introduction lays out this landscape explicitly, noting that existing transfer methods lack tight performance guarantees and are not naturally integrated with RL's core policy-improvement machinery.

---

### What this paper contributes

The paper establishes that transfer across tasks sharing dynamics is not merely an engineering heuristic but follows directly from two theorems grounded in dynamic programming. Theorem 1 (GPI) extends policy improvement to multiple policies, giving a lower bound on the performance of the combined policy. Theorem 2 provides an explicit, quantitative bound on the loss incurred on a new task as a function of its distance in w-space to the nearest previously solved task — something previously only intuited. The SF representation makes Theorem 2 computationally practical: re-evaluating n stored policies under a new reward reduces to n dot products. Together, the contributions transform transfer from an ad hoc practice into a principled extension of DP, with provable guarantees and a concrete implementation pathway that scales to deep RL.

---

### Brain regions & systems

Not applicable. This is a purely computational paper with no anatomical or neural focus. The level of analysis is algorithmic: the paper characterises what computation an agent must perform to transfer knowledge across tasks with shared dynamics, without commitment to biological substrate.

---

### Mechanistic insight

The paper does not meet the bar. It proposes and formalises a transfer algorithm (SF + GPI) and validates it empirically in simulated environments, but provides no neural data (recordings, imaging, lesions, pharmacology, etc.) linking the algorithm's specific variables (successor features, GPI policy selection) to measured biological activity. The paper is relevant to the neuroscience of the hippocampal successor representation and prefrontal policy selection, but does not provide evidence at any of Marr's three levels from neural data.

---

### Limitations & open questions

- The reward linearity assumption (r = φ⊤w) is restrictive; the paper notes φ can in principle be expressive enough to approximate any reward, but learning a sufficiently expressive φ remains non-trivial.
- The paper does not address how to choose the feature representation φ optimally; the bound in Theorem 2 depends critically on φ, raising the question of what φ makes the task geometry in R^d most useful.
- Memory management for growing libraries of stored SFs is acknowledged but not fully solved; the paper discusses heuristics (distance-based eviction) without formal analysis.
- Transfer is limited to tasks within the same MDP dynamics; environments with changing transition functions are outside the scope.
- The framework does not yet handle non-stationary w (shifting task identity within an episode) in a principled way.
- The paper does not address exploration under the new framework — how the agent should explore a new task given its SF library.

---

### Connections & keywords

**Key citations**:
- Dayan (1993) — successor representation (SR), the direct precursor to SFs
- Bellman (1957) — policy improvement theorem, generalised by this paper
- Mehta et al. (2008) — closest prior transfer learning work; compared and contrasted
- Mnih et al. (2015) — DQN, used as the base algorithm for SFDQN
- Sutton et al. (1999) — options framework; SFs related to temporal abstraction
- Sutton et al. (2011) — general value functions (GVFs); technical overlap with SFs
- Schaul et al. (2015) — universal value function approximators (UVFAs); structural similarity
- Fernández et al. (2010) — probabilistic policy reuse (PRQL), used as a baseline
- Kulkarni et al. (2016); Zhang et al. (2016) — prior deep SR work

**Named models or frameworks**:
- Successor Features (SFs)
- Generalized Policy Improvement (GPI)
- Successor Representation (SR)
- SFQL (SF + Q-learning)
- SFDQN (SF + DQN)
- Probabilistic Policy Reuse (PRQL)
- Universal Value Function Approximators (UVFAs)
- General Value Functions (GVFs)
- Options framework

**Brain regions**: Not applicable.

**Keywords**: successor features, successor representation, transfer learning, reinforcement learning, generalized policy improvement, reward decomposition, task generalisation, multi-task RL, value function factorisation, deep reinforcement learning, policy reuse, performance guarantees
