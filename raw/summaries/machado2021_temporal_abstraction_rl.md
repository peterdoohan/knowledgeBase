---
source_file: machado2021_temporal_abstraction_rl.md
paper_id: machado2021_temporal_abstraction_rl
title: "Temporal Abstraction in Reinforcement Learning with the Successor Representation"
authors:
  - "Marlos C. Machado"
  - "André Barreto"
  - "Doina Precup"
year: 2021
journal: "Journal of Machine Learning Research"
paper_type: computational
contribution_type: theoretical
brain_regions:
  - hippocampus
  - entorhinal_cortex
frameworks:
  - reinforcement_learning
  - successor_representation
keywords:
  - temporal_abstraction
  - options_framework
  - successor_representation
  - option_discovery
  - eigenoptions
  - covering_options
  - option_keyboard
  - temporally_extended_exploration
  - spectral_graph_theory
  - proto_value_functions
  - generalised_policy_improvement
  - diffusion_time
  - temporal
  - abstraction
  - reinforcement
  - learning
  - successor
  - representation
key_citations:
  - dayan1993_successor_representation
  - momennejad2017_successor_representation_humans
wiki_pages:
  - wiki/topics/successor_representation_as_a_predictive_map_in_reinforcement_learning_and_hippocampal_prefrontal_coding
---

### One-line summary

The successor representation (SR) provides a natural and unified substrate for discovering, representing, and combining temporally extended options in reinforcement learning, as demonstrated through a general framework (the ROD cycle) that generates eigenoptions and covering options and combines them via the option keyboard.

---

### Background & motivation

Intelligent decision making requires operating across multiple time scales, yet standard RL acts only at a primitive, step-by-step level. The options framework formalises temporally extended actions but has no principled answer to where options should come from — the option discovery problem. Existing approaches often assume a useful option set is given in advance. The paper argues that the successor representation (SR), which encodes states by their expected future state-visitation patterns, is the right substrate for solving option discovery because it directly captures environment dynamics and is closely related to spectral graph representations that identify long-range structure.

---

### Methods

- **Framework**: Proposes the Representation-Driven Option Discovery (ROD) cycle — an iterative process of (1) collecting samples, (2) learning the SR as a representation, (3) deriving an intrinsic reward from the SR's eigenvectors, (4) learning an option policy to maximise that reward, and (5) adding the option to the agent's library to facilitate future data collection.
- **Eigenoptions**: Options defined from the top eigenvectors of the SR; the intrinsic reward is the difference in eigenvector value between successive states, providing a gradient for learning. Initiation set and termination condition are implicit, determined by where the option's state-action value function goes non-positive.
- **Covering options**: Options derived from the bottom eigenvector of the graph Laplacian, defined as point options connecting the two maximally separated states; discovered iteratively.
- **Option keyboard**: A mechanism for combining a finite set of basis options (eigenoptions) into a combinatorially large set using generalised policy evaluation (GPE) and generalised policy improvement (GPI) applied to successor features — no additional learning required.
- **Evaluation metric**: Diffusion time (expected number of decisions for a random walk to move between any two states), computed analytically in tabular gridworld domains (four-room, open-room), used as a task-agnostic proxy for exploration quality.
- **Experiments**: Tabular gridworld domains; options computed both in closed form and online (TD learning of the SR); comparison of eigenoptions vs. covering options across varied numbers of options; factorial design varying initiation set breadth and eigenspectrum usage; qualitative and quantitative analysis of option-keyboard combinations.

---

### Key findings

- Eigenoptions consistently reduce diffusion time when sufficient options are available; covering options do so only in the closed-form setting and fail online due to their sparse initiation sets.
- Broad initiation sets (eigenoptions) eventually achieve lower diffusion time than point options (covering options), but create temporary sink states with fewer options; point options improve median diffusion time immediately but plateau.
- Using multiple eigenvectors of the SR (not just the top one) leads to more robust exploration and lower diffusion time than iterating on a single eigenvector.
- Eigenoptions are robust to online SR estimation; covering options are brittle online because their point initiation sets are rarely sampled and similar options are rediscovered across iterations.
- The option keyboard applied to 10 eigenoptions generates up to 137 unique options in the open-room and 115 in the four-room domain (using {0,1} weights), substantially expanding behavioral diversity without additional environment interactions.
- Combining eigenoptions with the option keyboard reduces the number of eigenoptions needed to outperform a random policy by 30–42% (from ~10–12 down to ~4 in tested domains) — matching the intuition that four directional options should suffice in these environments.
- Using {−1, 0, 1} weights with the option keyboard allows the agent to halve the number of eigenoptions to learn, since the negated-direction option is recovered for free.

---

### Computational framework

The paper uses **reinforcement learning with temporal abstraction** (the options / semi-MDP framework) grounded in **spectral graph theory** and the **successor representation**.

**Successor representation**: For policy π, the SR Ψ^π is an |S|×|S| matrix where entry (s, s') is the discounted expected future occupancy of s' starting from s under π: Ψ^π(s,s') = E[Σ_t γ^t 1(S_t = s') | S_0 = s, π]. The value function decomposes as v^π = Ψ^π r, separating the environment structure (encoded in Ψ^π) from the task (encoded in r). Successor features generalise this to arbitrary feature functions φ: v^π(s) ≈ ψ^π(s)^⊤ w when r(s,a) = φ(s,a)^⊤ w.

**Key assumption**: The eigenvectors of the SR are equivalent to proto-value functions (eigenvectors of the graph Laplacian) in symmetric, deterministic MDPs (Theorem 1). This connects the SR to diffusion processes on the state-space graph, motivating its use for discovering temporally extended behaviors that span different time scales.

**Option keyboard**: Uses generalised policy evaluation (evaluate each basis option under all intrinsic rewards) and generalised policy improvement (take the argmax over options at each state) to synthesise new option policies for any linear combination of basis rewards — instantly, without additional learning.

---

### Prevailing model of the system under study

The paper's introduction situates the work in RL, not neuroscience. The prevailing model it pushes against is that useful options must be given a priori or discovered by ad hoc methods without a principled theoretical substrate. Prior option discovery work either assumed handcrafted options or used heuristics (bottleneck detection, subgoal identification) that lacked a unifying framework. Proto-value functions (PVFs) had been proposed as spectral representations for function approximation but were not widely adopted for option discovery, and existing methods using the SR (e.g., Stachenfeld et al., eigenoptions in prior work) existed in isolation without a unifying framework showing how they relate to each other or how discovered options can be combined without extra learning.

---

### What this paper contributes

The paper introduces the ROD cycle as a unifying framework showing that diverse option discovery methods (eigenoptions, covering options, and others) are all special cases of the same representation-driven process. It then provides the first systematic empirical comparison of these methods on the same metric (diffusion time), identifying concrete design trade-offs: initiation set breadth versus sink-state creation, full eigenspectrum versus single eigenvector, and online versus closed-form robustness. The novel integration of eigenoptions with the option keyboard demonstrates that a finite set of discovered options can be extended — without learning — to a combinatorially large and diverse option library, drastically reducing both the learning cost and the number of options required. Concretely, the paper shows for the first time that four options suffice to improve exploration in environments where intuition suggested they should, bridging a gap between theoretical intuition and empirical demonstration.

---

### Brain regions & systems

The paper is primarily a computational/algorithmic paper. Brain regions appear only in the related work section (Section 9.3), not as a focus of the paper's own experiments.

- **Hippocampus** — cited as a candidate neural locus of the SR (Stachenfeld et al., 2014, 2017); hippocampal place fields interpreted as encoding a predictive representation of future states.
- **Entorhinal cortex / grid cells** — the eigenvectors of the SR resemble grid cell firing patterns, suggesting the entorhinal cortex may use this representation to aid hierarchical RL.

These connections are discussed as motivation and external validation, not as primary evidence in the paper's own experiments.

---

### Mechanistic insight

The paper does not meet the bar. It is a computational/theoretical paper presenting algorithms and simulations in gridworld domains. No neural data (recordings, imaging, lesions, pharmacology) are collected or analysed. The connections to hippocampal SR encoding and grid cell representations are cited from prior empirical work (Stachenfeld et al.) as suggestive convergent evidence, not as data that directly test the paper's specific algorithmic claims.

---

### Limitations & open questions

- All core experiments are in small tabular gridworlds; scaling to function approximation and continuous state spaces is discussed but not empirically demonstrated in this paper.
- The equivalence between SR eigenvectors and PVFs holds only in symmetric, deterministic MDPs; the SR is more general but the relationship becomes less clean in stochastic or asymmetric environments.
- Covering options perform poorly online; the paper conjectures this is due to sparse initiation sets but does not fully resolve the issue.
- The option keyboard relies on options being evaluated under all pairwise intrinsic rewards, which is quadratic in the number of basis options; scalability to large option libraries is unaddressed.
- Identifying equivalent options (needed to count unique combinations) is trivial in tabular settings but hard with function approximation.
- The paper does not characterise theoretically how many basis options are needed to guarantee at least one combined option terminates in each state.
- Optimal choice of weights for the option keyboard (beyond {−1,0,1}) is left as future work.
- The relationship between the SR eigenvectors and the eigenvectors of the non-symmetric lazy random walk (used by diffusion options) lacks a formal theoretical connection.

---

### Connections & keywords

**Key citations**:
- Dayan (1993) — original successor representation
- Sutton, Precup & Singh (1999) / Precup (2000) — options framework
- Machado et al. (2017, 2018) — eigenoptions
- Jinnai et al. (2019b, 2020) — covering options
- Barreto et al. (2017, 2019) — successor features, option keyboard, GPE/GPI
- Stachenfeld et al. (2014, 2017) — hippocampus as predictive map
- Mahadevan (2005); Mahadevan & Maggioni (2007) — proto-value functions
- Momennejad et al. (2017) — SR in human RL
- Tomov et al. (2021) — SR and GPI in human multi-task decision making

**Named models or frameworks**:
- Options framework / semi-MDP
- Successor representation (SR)
- Successor features (SFs)
- Proto-value functions (PVFs)
- Eigenoptions
- Covering options
- Option keyboard
- Generalised policy evaluation (GPE)
- Generalised policy improvement (GPI)
- Representation-Driven Option Discovery (ROD) cycle
- Diffusion time (evaluation metric)
- Four-room domain (Sutton et al., 1999)
- Deep Q-Network (DQN) — background

**Brain regions**:
- Hippocampus
- Entorhinal cortex

**Keywords**:
- temporal abstraction
- options framework
- successor representation
- option discovery
- eigenoptions
- covering options
- option keyboard
- temporally extended exploration
- spectral graph theory
- proto-value functions
- generalised policy improvement
- diffusion time

### Related wiki pages
- [[wiki/topics/successor_representation_as_a_predictive_map_in_reinforcement_learning_and_hippocampal_prefrontal_coding|Successor representation as a predictive map in reinforcement learning and hippocampal–prefrontal coding]]
