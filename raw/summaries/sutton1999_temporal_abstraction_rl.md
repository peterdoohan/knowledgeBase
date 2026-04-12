---
source_file: "sutton1999_temporal_abstraction_rl.md"
paper_id: "sutton1999_temporal_abstraction_rl"
title: "Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning"
authors: "Richard S. Sutton, Doina Precup, Satinder Singh"
year: 1999
journal: "Artificial Intelligence"
paper_type: "computational"
contribution_type: "theoretical"
frameworks: ["reinforcement_learning", "hierarchical_rl"]
keywords: ["bradtke_and_duff_1995_smdp_methods_for_continuous_time_mdps", "parr_1998_hierarchical_control_and_learning_for_mdps", "mahadevan_et_al_1997_continuous_time_average_reward_rl", "kaelbling_1993_hierarchical_learning_in_stochastic_domains", "dietterich_1998_maxq_method_for_hierarchical_rl", "dean_and_lin_1995_decomposition_techniques_for_planning_in_stochastic_domains", "singh_1992_abstract_models_and_variable_temporal_resolution_in_rl", "sutton_1995_td_models_at_multiple_time_scales", "hauskrecht_et_al_1998_hierarchical_solution_of_mdps_using_macro_actions", "named_models_or_frameworks", "options_framework", "semi_markov_decision_processes_smdps", "multi_time_models", "smdp_q_learning", "intra_option_q_learning", "intra_option_model_learning", "interruption_theorem", "rooms_example_gridworld_environment", "hallway_options", "brain_regions"]
---

### One-line summary

Introduces "options"—temporally extended actions consisting of policies, termination conditions, and initiation sets—enabling temporal abstraction within the reinforcement learning framework while maintaining theoretical foundations via semi-Markov decision process (SMDP) theory.

---

### Background & motivation

Reinforcement learning and Markov decision processes (MDPs) traditionally operate at a single discrete time step, with actions affecting only the immediate next state. This framework cannot naturally represent temporally extended behaviors like "go to lunch" or "pick up an object" that persist over variable durations. While temporal abstraction has been explored in AI planning since the 1970s, existing approaches lacked the ability to handle stochastic environments, closed-loop policies, and integrated learning and planning within a unified mathematical framework.

---

### Methods

- **Theoretical framework development**: Formal definitions of options, their value functions, and Bellman equations
- **Simulation experiments**: "Rooms example"—a gridworld with four rooms and stochastic cell-to-cell movements
  - 8 built-in "hallway options" (policies navigating from anywhere within a room to one of two hallway cells)
  - Two goal locations tested: G1 (hallway state) and G2 (middle of room)
  - Three option sets compared: primitive actions only (A), hallway options only (H), and both (A ∪ H)
- **Learning experiments**: SMDP Q-learning and intra-option Q-learning tested with ε-greedy exploration (ε = 0.1)
- **Model learning experiments**: Comparison of SMDP model-learning vs. intra-option model-learning

---

### Key findings

- **Options enable SMDP analysis**: Any MDP with a fixed set of options constitutes a semi-Markov decision process (SMDP), allowing existing SMDP theory to provide foundations for planning and learning with temporally abstract actions
- **Faster planning**: In the rooms example, synchronous value iteration with hallway options achieved accurate values room-by-room in 2 iterations versus cell-by-cell propagation requiring many more iterations with primitive actions alone
- **Interrupting options improves performance**: The interruption theorem proves that a policy can be improved by terminating options early when switching to a better-valued option, without requiring additional expensive planning—demonstrated with navigation tasks showing 474 steps (interrupted) vs. 600 steps (SMDP-optimal)
- **Intra-option learning is more efficient**: Learning about options from fragments of execution (intra-option methods) allows simultaneous learning about multiple options from the same experience—model learning experiments showed faster convergence than SMDP methods that only learn at option termination
- **Subgoals enable option learning**: Option policies can be learned by defining terminal subgoal values and applying standard RL methods within the option framework

---

### Computational framework

**Reinforcement learning with options as semi-Markov decision processes**

The paper extends the standard MDP framework to include temporally extended actions called "options." An option o = ⟨I, π, β⟩ consists of:
- **Initiation set I**: States where the option can be started
- **Policy π**: A mapping from states/histories to action probabilities that governs behavior while the option executes
- **Termination condition β**: The probability of terminating in each state

Options generalize primitive actions (which are options lasting exactly one step). When a set of options executes to termination, the resulting process is a semi-Markov decision process (SMDP), where transitions occur at irregular intervals.

The framework introduces **multi-time models** for options that predict:
- Expected cumulative discounted reward until termination
- Distribution over next states and transit times

These enable generalizations of Bellman equations for value functions over options:

Q^μ(s,o) = Σ p(s',k) [r + γ^k V^μ(s')]

where p(s',k) combines the probability of terminating in s' with a measure of delay relative to discount factor γ.

The paper also formalizes **intra-option learning**—updating option values from partial execution fragments using off-policy TD methods—and proves convergence for deterministic option policies.

---

### Prevailing model of the system under study

Before this paper, temporal abstraction in AI was primarily explored through:
1. **STRIPS-style planning** (1970s onwards): Macro-operators and hierarchical planning, but limited to deterministic environments without integrated learning
2. **Semi-Markov decision processes (SMDPs)**: Provided mathematical foundations for continuous-time, discrete-event systems with temporally extended actions, but treated actions as indivisible black boxes without internal structure
3. **Hierarchical reinforcement learning approaches**: Various ad hoc methods for temporal abstraction existed but lacked a unified, minimal theoretical framework

The prevailing view in reinforcement learning was that MDPs operated at a single time scale with primitive actions. While SMDP theory existed for temporally extended actions, there was no clean integration with MDPs that allowed examining and modifying the internal structure of temporally extended actions. The authors note that their work builds on and generalizes many co-temporaneous approaches to form a compact, unified framework.

---

### What this paper contributes

This paper establishes a minimal, mathematically rigorous extension of reinforcement learning that unifies primitive and temporally extended actions through the "options" framework. The key contributions are:

1. **Unified theoretical foundation**: Shows that any set of options defined over an MDP constitutes an SMDP, providing immediate theoretical foundations for planning and learning with temporal abstraction while treating primitive and extended actions uniformly

2. **Multi-time models**: Introduces models that predict option outcomes across variable time horizons, enabling dynamic programming and value iteration methods to work seamlessly with options

3. **Interruption theorem**: Proves that policies can be improved by interrupting options when switching to better-valued alternatives, providing a "nearly free" improvement over SMDP planning with minimal additional computation

4. **Intra-option learning methods**: Develops off-policy TD methods that learn about options from execution fragments without requiring the option to actually be selected or run to completion, enabling more efficient learning from shared experience

5. **Subgoal formulation for learning options**: Shows how option policies can be learned by defining terminal subgoal values and applying standard RL methods, providing a foundation for hierarchical skill acquisition

The paper demonstrates these contributions through the rooms example, showing that hallway options enable room-by-room planning versus cell-by-cell, and that intra-option methods learn option values without ever selecting those options.

---

### Brain regions & systems

Not applicable. This is a computational/algorithmic paper that does not involve neural data or biological brain systems. The framework is inspired by the need to model human-like flexible decision-making across multiple time scales, but no biological implementation is discussed.

---

### Mechanistic insight

The paper presents a formal framework for temporal abstraction in reinforcement learning, but does not provide neural data linking algorithmic components to measured neural activity. Therefore, it does not meet the bar for mechanistic insight as defined.

The paper proposes a computational framework where:
- **Computational level**: The problem is sequential decision-making with delayed rewards, where the agent must trade off exploration and exploitation while planning at multiple time scales
- **Algorithmic level**: Options (policies with termination conditions) enable temporal abstraction; SMDP theory provides planning and learning methods; intra-option learning enables off-policy updates from partial experience
- **Implementation level**: Not addressed—no mapping to neural circuits, cell types, or biophysical mechanisms

The paper notes that options may have implications for temporally extended perception, suggesting that learning models of options could correspond to learning action-oriented concepts (e.g., recognizing a battery charger by knowing how to dock with it). However, this remains speculative without empirical validation.

---

### Limitations & open questions

1. **Source of subgoals**: The paper assumes subgoals are given and does not address how appropriate subgoals are discovered or what principles should guide their selection

2. **State abstraction integration**: The framework focuses on temporal abstraction; integration with state abstraction (representing states at multiple levels of detail) remains incomplete

3. **Transfer between subtasks**: How knowledge transfers between related subtasks or options learned in different contexts is not fully addressed

4. **Option discovery**: The paper assumes options are given or learned from given subgoals; automatic discovery of useful options from experience remains an open problem

5. **Stochastic option policies**: The intra-option Q-learning convergence proof assumes deterministic option policies; extensions to stochastic policies are noted as a topic for current research

6. **Computational cost of many options**: The paper acknowledges that adding multi-step options may slow planning if the initial value function is optimistic (Hauskrecht et al. result), and that the "utility problem" of too many macros applies to temporal abstraction as well

7. **Nonstationary policies**: The paper distinguishes semi-Markov policies from nonstationary policies, noting that semi-Markov policies are more constrained; the full implications of this distinction are not explored

---

### Connections & keywords

**Key citations:**
- Bradtke & Duff (1995) — SMDP methods for continuous-time MDPs
- Parr (1998) — Hierarchical control and learning for MDPs
- Mahadevan et al. (1997) — Continuous-time average-reward RL
- Kaelbling (1993) — Hierarchical learning in stochastic domains
- Dietterich (1998) — MAXQ method for hierarchical RL
- Dean & Lin (1995) — Decomposition techniques for planning in stochastic domains
- Singh (1992) — Abstract models and variable temporal resolution in RL
- Sutton (1995) — TD models at multiple time scales
- Hauskrecht et al. (1998) — Hierarchical solution of MDPs using macro-actions

**Named models or frameworks:**
- Options framework
- Semi-Markov decision processes (SMDPs)
- Multi-time models
- SMDP Q-learning
- Intra-option Q-learning
- Intra-option model learning
- Interruption theorem
- Rooms example (gridworld environment)
- Hallway options

**Brain regions:**
Not applicable

**Keywords:**
temporal abstraction, reinforcement learning, options, semi-Markov decision processes, hierarchical reinforcement learning, macro-actions, intra-option learning, multi-time models, planning, SMDP Q-learning, subgoals, interruption
