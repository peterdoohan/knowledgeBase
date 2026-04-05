---
source_file: dayan1993_successor_representation.md
title: "Improving Generalisation for Temporal Difference Learning: The Successor Representation"
authors: Peter Dayan
year: 1993
journal: Neural Computation
paper_type: computational
contribution_type: theoretical
---

### One-line summary

Dayan introduces the successor representation (SR) — a state representation defined as the expected discounted future occupancy of all states — and shows it can be learned via TD machinery itself, producing better generalisation for temporal difference learning.

---

### Background & motivation

Temporal difference (TD) methods for estimating future returns depend critically on the quality of the state representation used for function approximation. Standard approaches borrowed from static tasks generalise between states that are spatially nearby, but this can be inappropriate for dynamic tasks where states close in space may be far apart in terms of the behavioural trajectory (e.g., on opposite sides of a barrier). The paper addresses the question of what representation is _intrinsically_ appropriate for TD learning, arguing that states should be represented similarly when they share similar successors, not merely similar positions.

---

### Methods

- **Model architecture**: The SR of state $i$ is the vector of expected discounted future occupancies $\tilde{x}_i = (I - Q)^{-1}$, where $Q$ is the transition matrix. States are represented by this vector rather than by punctate (one-hot) or spatial (CMAC) encodings.
- **Learning mechanism**: The SR is itself learned using a TD algorithm applied to the prediction of future state occupancies, requiring no machinery beyond standard TD.
- **Validation task**: A grid-world navigation task with a central barrier, comparing four conditions: punctate representation, CMAC squares, SR without latent learning, and SR with a prior latent learning phase (exploration before reward is introduced).
- **Key measurement**: Learning curves expressed as average excess steps to goal after a fixed number of learning iterations.

---

### Key findings

- The SR produces a spatially distributed representation that decays exponentially from the starting state but respects the barrier — states on the far side of the barrier receive near-zero predicted occupancy, unlike CMAC squares which erroneously generalise across it.
- A punctate representation augmented with the SR learned during latent exploration outperforms both punctate-only and CMAC representations on the navigation task (Figure 3).
- SR with latent learning converges fastest; SR without latent learning also outperforms CMAC, demonstrating benefit even without pre-training.
- The SR factors out the temporal component of the value estimation problem: with the SR as basis, the optimal weights reduce to simply the expected immediate return $h$, eliminating the need for iterative TD computation in the limit.
- After policy improvement, the SR degrades in a principled way: predictions converge toward the optimal path, which would hinder transfer to new goals — a noted limitation.

---

### Computational framework

**Reinforcement learning / temporal difference learning.**

The paper works within the framework of TD learning applied to finite absorbing Markov chains. The core formalism:

- **State**: non-absorbing state $i \in N$; absorbing states $k \in T$.
- **Value**: overall expected return $\tilde{r}_i = h(I-Q)^{-1}$, where $h_i$ is the expected immediate return.
- **SR**: $[\tilde{x}_i]_j = [(I-Q)^{-1}]_{ij}$, the expected discounted number of future visits to state $j$ starting from state $i$.
- **Key assumption**: the SR can itself be learned by TD, treating future occupancy as the prediction target rather than future reward.
- The framework assumes stationarity of transition probabilities and returns; the paper notes this is violated during policy improvement.

---

### Prevailing model of the system under study

As framed by the paper, the prevailing approach to function approximation in TD learning was to use representations adapted from static supervised learning — either punctate (one-hot) or spatially local representations such as CMAC squares. These representations encode proximity in an a priori metric space (Euclidean or Manhattan distance on the grid). The paper treats this as the baseline to surpass: good representations should encode temporal-successor similarity, not spatial similarity, but no principled method for constructing or learning such representations had been proposed. The theoretical gap was the absence of a framework that tied the structure of the representation explicitly to the Markov dynamics of the task.

---

### What this paper contributes

The paper provides the first principled derivation of what the optimal representation for linear TD function approximation should look like: it should equal the matrix $(I - Q)^{-1}$, the discounted future state occupancy. This is not merely a theoretical observation — the paper shows the SR can be learned online via TD itself (no extra machinery) and demonstrates empirically that it outperforms CMAC on a canonical navigation task where spatial proximity is misleading. The key conceptual contribution is redefining "similarity" for temporal tasks: two states are similar if they tend to visit the same future states, regardless of their position in the input space. The paper also identifies the SR's Achilles heel: it is policy-dependent and must be relearned when the policy changes substantially.

---

### Brain regions & systems

Not applicable. This is a purely computational paper with no anatomical or neural system focus. The level of analysis is algorithmic: it concerns the appropriate mathematical structure for state representations in TD learning. The results are relevant to theories of hippocampal place cell coding and striatal value representations (the SR has subsequently been proposed as a model of hippocampal representations), but the paper itself makes no neuroscientific claims.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight in the neuroscientific sense. It proposes a new representational algorithm (the SR) and validates it computationally in a simulated maze, but provides no neural data (recordings, imaging, lesion, or pharmacology) linking the SR to measured neural activity. The paper is a purely computational contribution; any neural implementation claims would belong to later work.

---

### Limitations & open questions

- The SR is policy-dependent: as the agent's policy improves, the SR degrades (predictions collapse onto the optimal path), potentially hindering generalisation to new goals. This is acknowledged as a fundamental tension between estimation and control.
- Stationarity is violated in control settings — the transition matrix changes as the policy changes — invalidating the theoretical guarantees derived under fixed $Q$.
- Learning the full SR for large state spaces is computationally expensive: it converts one temporal prediction problem into $|N|$ temporal prediction problems (one per state). The paper acknowledges this objection.
- Convergence proofs for TD learning with non-punctate, non-linearly-independent function approximators were limited at the time of writing; the paper notes this as a concern.
- The SR provides less than a full world model: unlike learning the transition matrix $Q$ directly (Sutton, 1990), the SR is goal- and policy-sensitive, meaning that environmental changes require full relearning of affected predictions.

---

### Connections & keywords

**Key citations**:
- Sutton (1988) — TD($\lambda$) learning; convergence proofs for batch TD
- Watkins (1989) — Q-learning; navigation with CMAC
- Barto, Sutton & Watkins (1989/1990) — TD-based control; asynchronous dynamic programming
- Dayan (1992) — convergence of TD($\lambda$) for general $\lambda$
- Sutton & Pinette (1985) — related recurrent network approach to predicting future returns
- Sutton (1990) — integrated architectures; learning transition models

**Named models or frameworks**:
- Successor Representation (SR)
- Temporal Difference (TD) learning / TD($\lambda$)
- Q-learning
- CMAC (Cerebellar Model Articulation Controller) — Albus, 1975
- Asynchronous dynamic programming

**Brain regions**: Not applicable (no neural regions discussed)

**Keywords**: successor representation, temporal difference learning, function approximation, state representation, Markov chain, future state occupancy, latent learning, generalisation, distributed representations, reinforcement learning, navigation, policy-dependent representation
