---
source_file: velasco2025_decision_precaching_planning.md
title: Expert navigators deploy rational complexity–based decision precaching for large-scale real-world planning
authors: Pablo Fernandez Velasco, Eva-Maria Griesbauer, Iva K. Brunec, Jeremy Morley, Ed Manley, Daniel C. McNamee, Hugo J. Spiers
year: 2025
journal: Proceedings of the National Academy of Sciences (PNAS)
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Expert London taxi drivers precache decisions at high-complexity street junctions during an early offline planning phase, with response time patterns revealing a nonsequential, globally prioritized access to remote states guided by successor representation and local transition entropy metrics.

---

### Background & motivation

Human planning research has primarily studied naive participants in simplified laboratory tasks, leaving open how experts plan in complex real-world environments. London taxi drivers provide a unique opportunity to study large-scale planning: they undergo extensive training ("The Knowledge") and navigate over 26,000 streets. This study investigates how expert planners dynamically organize their planning process across offline (pre-response) and online (during route reporting) phases, testing whether they deploy rational complexity-based decision precaching strategies.

---

### Methods

- **Participants**: 43 licensed London taxi drivers with extensive navigational expertise
- **Task**: Participants mentally planned routes between origin-destination pairs across London (26,000+ street segments) and verbally called out routes street-by-street
- **Response time measures**:
  - **OFF-TT (offline thinking time)**: Time from instruction to first street call-out (early planning phase)
  - **COT (call-out times)**: Pauses between consecutive street names (online planning phase)
  - **ON-TT (online thinking time)**: Sum of COTs for a route
- **Key predictor variables**:
  - **Successor Representation (SR)**: Measures state predictability/likelihood under random walk policy
  - **Local Transition Entropy (LTE)**: Measures decision complexity at a state (branching factor uncertainty)
  - **Environmental variables**: Euclidean distance, streetwise distance, segment length, angular deviations
- **Analysis**: Fixed-effects multivariate linear regression (GLM) with log-transformed, z-standardized COT as dependent variable; model comparison using AIC/BIC

---

### Key findings

- **Offline-online trade-off**: Strong negative correlation between OFF-TT and ON-TT (ρ = −0.348, p < 10⁻⁹) when normalized by streetwise distance; longer offline thinking reduced subsequent online planning burden
- **SR and LTE effects on response times**:
  - Significant negative main effect of SR on COT (β = −0.378, p = 0.001): more predictable states associated with faster call-outs
  - LTE trended toward slowing COTs (p = 0.066)
  - SR and LTE were relatively independent of environmental variables
- **Critical interaction effects**: The best-fitting model (GLM3) contained significant interactions between OFF-TT and both SR (β = 0.380, p = 0.002) and LTE (β = −0.048, p = 0.033), indicating that longer offline planning selectively reduced COT at high-SR and high-LTE states
- **Nonsequential prioritization**: No significant effect of planning step number (p = 0.16) and no interaction between step number and OFF-TT duration (p = 0.648), ruling out sequential tree-search-like processing; instead, results support spatially discontiguous, global prioritization of remote states
- **Environmental variables**: Only distance metrics measured along actual streets (not Euclidean distances) modulated COT, suggesting taxi drivers use embodied, street-based internal representations rather than abstract Euclidean metrics

---

### Computational framework

The study employs an **information-theoretic planning complexity framework** based on **path entropy** (also called planning description length). Key formal components:

- **Path entropy**: Quantifies the information cost of specifying a route from origin to destination under a stochastic search model; measures the uncertainty over possible trajectories in the state space
- **Successor Representation (SR)**: M(o,s) = Σₖ γᵏ Tᵏ(o,s) — captures the expected discounted number of visits to state s from origin o under a random walk policy; high SR indicates frequently visited, predictable states
- **Local Transition Entropy (LTE)**: H(s) = −Σₛ′ T(s,s′) log T(s,s′) — measures the uncertainty/decision complexity at a particular state based on its outgoing transition distribution; high LTE indicates complex branching points
- **Decomposition of path entropy**: The total path entropy can be expressed as the product of SR and LTE summed over states: H(τ|o) = Σₛ M(o,s) · H(s)

The framework predicts that rational planners should prioritize planning at states with high SR × LTE (high contribution to path entropy) to maximally reduce planning uncertainty. This yields a **nonsequential, global prioritization strategy** where remote critical junctions are precached during offline planning, rather than sequential rollout from the origin.

---

### Prevailing model of the system under study

The prevailing understanding of human planning, drawn from both cognitive science and AI, centers on **tree search algorithms** (forward planning, backward induction, or variants like MCTS). These models assume:

1. **Sequential state expansion**: States are processed in order of their spatial/temporal proximity to the origin (or goal), with trajectories built step-by-step
2. **Local computation**: Computational effort is concentrated on immediate next-step decisions, with planning depth modulated by resource constraints
3. **Depth-limited search**: Humans trade off accuracy against computational cost by pruning branches or limiting search depth

Recent theoretical work has proposed **hierarchical planning** as an efficiency enhancement, suggesting that humans exploit structural bottlenecks (cluster boundaries) to decompose problems. However, most empirical evidence for these frameworks comes from:
- Abstract games (chess, Go, Tower of Hanoi) with small, well-defined state spaces
- Virtual environments with explicitly designed hierarchical structure
- Naive participants rather than domain experts

The prevailing model thus lacks validation in **large-scale, real-world environments** with natural (not artificially imposed) structure, and in **expert populations** with extensive domain knowledge. Whether complexity-based prioritization and nonsequential access actually characterize human planning in such contexts remains an open question.

---

### What this paper contributes

This paper provides the first empirical evidence that expert human planners deploy **rational complexity-based decision precaching** in a large-scale real-world environment (London's 26,000+ street network). The key contributions are:

1. **Identification of nonsequential planning in experts**: Unlike sequential tree-search models, taxi drivers access states in a spatially discontiguous, globally prioritized manner based on SR and LTE metrics, not their order along the route.

2. **Evidence for decision precaching**: Longer offline planning periods (OFF-TT) selectively reduce online response times (COT) at high-SR and high-LTE states, consistent with pre-computing and caching decisions at critical junctions during the offline phase.

3. **Real-world validation of information-theoretic planning complexity**: The SR × LTE metric (path entropy decomposition) predicts planning behavior in a natural, uncontrolled environment, supporting the normative framework's ecological validity.

4. **Expert-specific planning strategies**: The trade-off between offline and online planning, and the global nonsequential access pattern, may reflect expertise-acquired strategies for managing complexity in very large state spaces—distinct from the sequential, depth-limited approaches observed in novices.

5. **Methodological contribution**: The study demonstrates that response time analysis in verbal route reporting can serve as a window into the computational structure of expert planning in real-world contexts.

Overall, the paper bridges the gap between theoretical proposals of efficient hierarchical planning and real-world expert cognition, showing that humans can indeed implement rational complexity-based precaching strategies in natural, large-scale environments.

---

### Brain regions & systems

Not applicable — this is a behavioral study with no neural measurements. However, the authors discuss theoretical implications for:

- **Hippocampus** — discussed as the likely substrate for the internal model of London's street network (building on prior work showing hippocampal structural changes in taxi drivers)
- **Prefrontal cortex** — implicated in hierarchical planning and control over memory retrieval
- **Entorhinal cortex/grid cells** — discussed in relation to vector-based navigation strategies

The paper suggests that the observed nonsequential state access patterns may reflect alternative forms of neural replay (different from sequential replay observed in rodent studies), which could be tested in future neurophysiological work.

---

### Mechanistic insight

This paper meets the mechanistic insight bar, though primarily at the **computational and algorithmic levels** with theoretical implications for implementation.

**Computational level**: The brain is solving the problem of efficient route planning in a very large state space (26,000+ streets) under constraints of limited working memory and time. The problem is formalized as minimizing path entropy (planning description length) — the information-theoretic cost of specifying a route.

**Algorithmic level**: The paper proposes and finds evidence for a **nonsequential, globally prioritized planning algorithm**:
- States are prioritized by their contribution to path entropy: SR × LTE
- High-SR states (frequently visited under random walk) and high-LTE states (complex decision points) are accessed during offline planning
- Decisions at these critical states are precached, enabling faster retrieval during online route reporting
- This contrasts with sequential tree search (forward simulation from origin) which would predict step-number effects

The SR and LTE metrics provide a formal way to identify bottleneck states and cluster boundaries without requiring explicit hierarchical decomposition. The algorithm is resource-rational: it allocates limited planning time to states that maximally reduce overall trajectory uncertainty.

**Implementational level**: No direct neural data, but the authors discuss possible substrates:
- Internal model of London likely stored in hippocampal-cortical networks (building on prior taxi driver studies showing posterior hippocampal expansion)
- Vector-based navigation may involve entorhinal grid cells
- Nonsequential state access may reflect alternative forms of hippocampal replay (not sequential forward/reverse replay as in rodent studies, but prioritized access based on SR/LTE)
- Prefrontal cortex may mediate hierarchical control and retrieval of cached decisions

The paper provides behavioral evidence consistent with a specific algorithmic architecture that could guide future neurophysiological investigations.

---

### Limitations & open questions

- **No neural data**: The study is purely behavioral; neural mechanisms are inferred from response time patterns and theoretical frameworks
- **Cross-sectional design**: Cannot distinguish expertise-acquired strategies from selection effects (whether taxi drivers develop these strategies through training or whether people with these abilities become taxi drivers)
- **Simplified route reporting**: While more natural than laboratory tasks, verbal call-outs may not capture all aspects of internal planning (e.g., visual imagery, simulation)
- **Static environment**: London's street network is fixed; unclear how strategies adapt to dynamic environments with traffic, construction, or changing conditions
- **Single expert population**: Findings may be specific to taxi drivers or London; generalization to other expert domains (e.g., chess, medicine) or other cities unknown
- **Descriptive not mechanistic**: The GLM approach identifies statistical relationships but does not provide a generative model of the planning process; the authors note future work should develop computational models that reproduce the observed dynamics

---

### Connections & keywords

**Key citations**:
- McNamee, Wolpert, Lengyel (2016) — foundational theory of planning description length and SR/LTE metrics
- Dayan (1993) — successor representation
- Botvinick & Niv (2009); Botvinick (2012) — hierarchical reinforcement learning
- Balaguer, Spiers, Hassabis, Summerfield (2016) — hierarchical planning in virtual subway network
- Mattar & Daw (2018) — prioritized memory access and hippocampal replay
- Griesbauer et al. (2022); Griesbauer et al. (2024) — prior work on London taxi driver navigation and hierarchical planning

**Named models or frameworks**:
- Planning description length / path entropy framework (McNamee et al.)
- Successor Representation (SR) — Dayan (1993)
- Local Transition Entropy (LTE)
- Hierarchical reinforcement learning / options framework
- Tree search algorithms (contrastive baseline)
- Vector-based navigation

**Brain regions**:
- Hippocampus (implied — structural changes in taxi drivers, internal model storage)
- Entorhinal cortex / grid cells (discussed in relation to vector navigation)
- Prefrontal cortex (hierarchical control)

**Keywords**:
- route planning
- spatial navigation
- successor representation
- local transition entropy
- decision precaching
- hierarchical planning
- expert cognition
- London taxi drivers
- planning description length
- path entropy
- offline planning
- online planning
- state-space complexity
- resource-rational analysis
- large-scale state space
