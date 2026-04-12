---
source_file: machado2018_eigenoption_successor_representation.md
paper_id: machado2018_eigenoption_successor_representation
title: "Eigenoption Discovery Through the Deep Successor Representation"
authors:
  - "Marlos C. Machado"
  - "Clemens Rosenbaum"
  - "Xiaoxiao Guo"
  - "Miao Liu"
  - "Gerald Tesauro"
  - "Murray Campbell"
year: 2018
journal: "International Conference on Learning Representations (ICLR 2018)"
paper_type: computational
contribution_type: methodological
brain_regions:
  - hippocampus
  - entorhinal_cortex
frameworks:
  - reinforcement_learning
  - successor_representation
  - hierarchical_rl
keywords:
  - option_discovery
  - eigenoptions
  - successor_representation
  - proto_value_functions
  - spectral_graph_theory
  - hierarchical_reinforcement_learning
  - temporal_abstraction
  - intrinsic_motivation
  - deep_reinforcement_learning
  - representation_learning
  - atari_2600
  - diffusion_time
  - eigenoption
  - discovery
  - through
  - deep
  - successor
  - representation
key_citations:
  - dayan1993_successor_representation
  - barreto2017_successor_features_transfer_c
  - sutton1999_temporal_abstraction_rl
wiki_pages:
  - wiki/topics/successor_representation_as_a_predictive_map_in_reinforcement_learning_and_hippocampal_prefrontal_coding
---

### One-line summary

A new algorithm extends eigenoption discovery to stochastic, non-enumerated-state environments by exploiting the equivalence between proto-value functions and the successor representation, enabling options to be learned directly from raw pixels via a deep neural network.

---

### Background & motivation

Hierarchical reinforcement learning relies on options (temporally extended actions) to speed up learning and planning, but autonomously discovering a useful set of options remains an open problem. Prior work on eigenoptions — options derived from eigenvectors of a diffusive information flow (DIF) model encoded by the combinatorial graph Laplacian (proto-value functions, PVFs) — was limited to deterministic tabular settings or settings where a fixed linear feature representation was provided in advance. The paper addresses these limitations by leveraging the mathematical equivalence between PVFs and the successor representation (SR), which naturally handles stochastic transitions and does not require a prespecified feature map.

---

### Methods

- **Framework**: Reinforcement learning with the options framework (Sutton et al., 1999); Markov decision processes.
- **Core insight**: Proved (following Stachenfeld et al., 2014) that the eigenvectors of the normalised Laplacian (PVFs) are equivalent to the eigenvectors of the SR (scaled by γ⁻¹D^½), so the SR can directly replace the Laplacian for eigenoption discovery.
- **Tabular algorithm**: Estimated the SR online via temporal-difference updates under a uniform random policy (Algorithm 2). Eigendecomposition of the estimated SR matrix yields eigenpurposes (intrinsic reward functions); options are then learned by maximising these rewards (Algorithm 1).
- **Deep neural network (function approximation)**: A convolutional network receives raw pixels and learns a latent representation via two jointly trained losses: (1) next-state reconstruction loss (auxiliary task; Oh et al., 2015) to avoid the zero fixed-point and promote contingency-aware features; (2) SR estimation loss based on the TD error over successor features (Barreto et al., 2017). Gradients from the SR estimator are blocked from updating the representation layers.
- **Eigenoption learning in Atari**: Trained the network on 500,000 samples per game; stored SR outputs during 50,000 random-policy steps; extracted right eigenvectors of the resulting matrix; used one-step greedy lookahead (γ = 0) to approximate option policies.
- **Evaluation domains**: Four-rooms tabular domain and four Atari 2600 games (Bank Heist, Freeway, Montezuma's Revenge, Ms. Pac-Man) from the Arcade Learning Environment.
- **Metrics**: Diffusion time (expected steps under uniform random policy to traverse state space) in tabular domain; qualitative state-visitation density plots for Atari options.

---

### Key findings

- In the four-rooms domain, SR-estimated eigenvectors closely approximate the true PVFs even after only 100 episodes of data, though 500 episodes give near-perfect agreement.
- Eigenoptions derived from the SR significantly reduce diffusion time compared to primitive actions and to "random options" (which require hundreds of random options to match the effect of a handful of eigenoptions).
- SR-derived eigenoptions also improve reward accumulation in the tabular setting when used as behavioural options in an off-policy Q-learning setup; even rough SR estimates (100 episodes) are sufficient for a notable speedup.
- In Atari, the deep SR network discovers purposeful options: in three of four games (Bank Heist, Montezuma's Revenge, Ms. Pac-Man), discovered options drive the agent to corners and structurally meaningful locations (e.g., subgoals in Montezuma's Revenge match human-identified milestones).
- Options learned from raw pixels are comparable to those obtained with RAM-state features, demonstrating that the network implicitly identifies controllable, task-relevant screen regions.
- The auxiliary reconstruction task is sufficient to prevent the zero fixed-point collapse and yields useful representations even when next-state prediction quality is moderate.

---

### Computational framework

The paper operates within the **reinforcement learning** framework (MDPs, options, temporal-difference learning) combined with **spectral graph theory** and **deep learning**.

Key formalism:
- The **successor representation** Ψ^π(s, s') is defined as the expected discounted future occupancy of state s' starting from s under policy π; it converges to (I − γT_π)^{-1}.
- **Eigenpurposes** are intrinsic reward functions r_i^e(s_{t-1}, s_t) = φ(s_t)^T e − φ(s_{t-1})^T e, where e is an eigenvector of the SR encoding the DIF model at a specific timescale.
- **Eigenoptions** maximise eigenpurposes; an option terminates when all action-values for that eigenpurpose fall to ≤ 0.
- The key mathematical result: eigenvectors of the normalised Laplacian L = D^{-½}(D−W)D^{-½} and eigenvectors of the SR Ψ are related by e_{PVF,j} = γ^{-1} D^{½} e_{SR,i} (indices sorted in reverse order), ensuring interchangeability for eigenpurpose extraction.
- In the deep setting, **successor features** (Barreto et al., 2017) generalise the SR to continuous state spaces via a learned feature map φ(·).

---

### Prevailing model of the system under study

The paper studies option discovery in RL. The prevailing approach prior to this work was that eigenoptions (the most principled spectral approach) could only be computed in the tabular case (by explicitly constructing the graph Laplacian from the state-transition graph) or, in the function approximation case, by enumerating transitions over a fixed, hand-crafted linear feature space. This placed strong constraints on applicability: deterministic environments, symmetric transition matrices, and pre-specified representations were all assumed. The broader field used diverse alternative approaches (bottleneck-state methods, skill chaining, end-to-end hierarchical RL) without a unifying spectral grounding. The SR had been proposed (Dayan, 1993) and linked to place cells and hippocampal function (Stachenfeld et al., 2014, 2017), but had not been deployed as the backbone for option discovery in the non-tabular setting.

---

### What this paper contributes

The paper shows that switching from the Laplacian/PVF formulation to the SR for eigenoption discovery eliminates three key limitations simultaneously: stochastic transitions are handled naturally, no symmetric adjacency matrix is required, and memory cost is constant per update rather than scaling with sample count. Extending the SR to raw pixels via the proposed deep network further removes the requirement for handcrafted features. Empirically, this work demonstrates for the first time that principled, spectral-geometry-inspired options can be extracted from raw game pixels, producing behaviours comparable to those obtained with privileged state information (RAM states). The paper also provides explicit proof of the SR–PVF eigenvector equivalence, formalising a connection previously suggested without full rigour.

---

### Brain regions & systems

The paper is primarily a computational/algorithmic contribution to reinforcement learning and does not study brain regions empirically. However, it explicitly invokes neuroscience motivation:

- **Hippocampus** — cited (Stachenfeld et al., 2014, 2017) as a proposed neural substrate encoding the successor representation; relevant to spatial memory and navigation.
- **Entorhinal cortex** — cited as encoding a low-dimensional basis set of the SR (analogous to PVFs / grid cells); part of the same spatial memory system.

These regions are referenced as motivation and as evidence that the SR is a biologically plausible representational scheme, not as objects of study in the paper itself.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined here. It is a computational/algorithmic contribution that proposes and validates a new RL algorithm. It does not collect neural recordings, imaging data, lesion data, or any other neural measurements. The neuroscience references (hippocampus as SR substrate) are cited to motivate the use of the SR but are not tested or extended by new neural evidence.

---

### Limitations & open questions

- The Atari eigenoption policies were approximated using one-step greedy lookahead (γ = 0), which cannot deal with delayed rewards; this likely explains failure on Freeway and limits option quality generally.
- The approach was evaluated qualitatively in Atari (state-visitation plots) rather than quantitatively in terms of downstream task performance (reward accumulation), leaving the end-to-end RL benefit undemonstrated in the pixel-input setting.
- The paper does not evaluate compositionality or transferability of discovered eigenoptions across related environments or task variations, flagged as a direction for future work.
- The reconstruction module prediction quality was moderate; better representations are expected to yield better options, but the relationship is not systematically characterised.
- Sample complexity of the option-learning phase is not accounted for in the experimental analysis; the paper's justification (lifelong learning reuse) is not empirically tested.
- Scaling beyond four rooms and four Atari games, and to continuous action spaces, is unexplored.

---

### Connections & keywords

**Key citations**:
- Machado et al. (2017) — original eigenoptions and Laplacian framework (ICML)
- Dayan (1993) — successor representation
- Stachenfeld et al. (2014, 2017) — SR–PVF equivalence; hippocampus as predictive map
- Kulkarni et al. (2016b) — deep successor reinforcement learning (first deep SR network)
- Oh et al. (2015) — action-conditional next-state prediction module
- Barreto et al. (2017) — successor features for transfer
- Mnih et al. (2015) — DQN; target networks
- Sutton et al. (1999) — options framework
- Mahadevan (2005); Mahadevan & Maggioni (2007) — proto-value functions
- Bellemare et al. (2013) — Arcade Learning Environment

**Named models or frameworks**:
- Eigenoptions
- Proto-value functions (PVFs)
- Successor representation (SR)
- Successor features (Barreto et al.)
- Options / semi-MDP framework
- Deep Q-Network (DQN)
- Diffusive information flow (DIF) model
- Normalised graph Laplacian
- Slow feature analysis (noted as equivalent to PVFs under specific adjacency function)

**Brain regions**:
- Hippocampus (cited, not studied)
- Entorhinal cortex (cited, not studied)

**Keywords**:
- option discovery
- eigenoptions
- successor representation
- proto-value functions
- spectral graph theory
- hierarchical reinforcement learning
- temporal abstraction
- intrinsic motivation
- deep reinforcement learning
- representation learning
- Atari 2600
- diffusion time

### Related wiki pages
- [[wiki/topics/successor_representation_as_a_predictive_map_in_reinforcement_learning_and_hippocampal_prefrontal_coding|Successor representation as a predictive map in reinforcement learning and hippocampal–prefrontal coding]]
