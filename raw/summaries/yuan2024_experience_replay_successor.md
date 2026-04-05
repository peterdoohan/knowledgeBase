---
source_file: yuan2024_experience_replay_successor.md
title: Improving Experience Replay with Successor Representation
authors: Yizhi Yuan, Marcelo G. Mattar
year: 2024
journal: Not specified (conference paper)
paper_type: computational
contribution_type: methodological
---

### One-line summary

A novel prioritization scheme for experience replay that combines TD-error with a "need term" derived from successor representation, showing improved performance in Dyna-Q maze and Atari games.

---

### Background & motivation

Experience replay improves sample efficiency in reinforcement learning by reusing past experiences. Prioritized experience replay (PER) prioritizes experiences based on TD-error (prediction error), assuming that experiences with large prediction errors provide more learning signal. However, recent neuroscience research suggests that biological organisms prioritize memory replay based on both "gain" (prediction error) and "need"—the expected relevance of each experience to the current situation. Current algorithms like PER only consider gain, not need. This paper aims to incorporate the need term into computational RL algorithms to improve sample efficiency.

---

### Methods

- **Successor Representation (SR)**: Used to compute the "need term"—the expected discounted future occupancy of states. The SR estimates how often the agent expects to visit each state in the future from the current state.
- **Tabular Implementation**: PS-SR (Prioritized Sweeping with SR) for the Dyna-Q maze; used TD(λ) to learn the SR matrix M with λ = 0.5.
- **Non-tabular Implementation**: PER-SR (Prioritized Experience Replay with SR) for Atari games; used deep successor representation network (DSR) with vector projection to estimate need terms.
- **Vanilla PER-SR**: Simplified PER with one-hot state representation (no neural networks) tested on Blind Cliffwalk environment.
- **Sampling Strategy**: Instead of modulating sampling probability (which would require computing need terms for all transitions), the need term modulates the magnitude of Q-updates directly.
- **Baselines**: Prioritized Sweeping (PS), Prioritized Experience Replay (PER), uniform sampling, oracle (hindsight-optimal).

---

### Key findings

- **Dyna-Q Maze**: PS-SR converged to the optimal policy faster than PS. While PS took ~50 episodes to converge, PS-SR reached optimal policy in fewer steps (significant improvement in steps per episode).
- **Blind Cliffwalk**: PER with need term required fewer Q-updates to converge than vanilla PER. Even random need terms outperformed vanilla PER, and optimal need terms approached the oracle lower bound.
- **Atari Games**: PER-SR achieved better performance than PER in most games tested. Significant performance increases in Berzerk (~1500% improvement), Qbert (~1000% improvement), and Robotank (~500% improvement).
- **Learning Dynamics**: PER-SR showed slower early learning but better long-term performance compared to PER. This is attributed to the time needed to learn accurate SR representations.
- **Overfitting Mitigation**: PER showed performance drops after initial rapid learning (e.g., in Boxing, score dropped from 50 to -40), likely due to overfitting to high TD-error transitions. PER-SR mitigated this effect by rescaling Q-updates with need terms, continuing to improve without catastrophic drops.

---

### Computational framework

- **Reinforcement Learning**: Q-learning, Deep Q-Networks (DQN), tabular and function approximation settings
- **Successor Representation (SR)**: A predictive representation that encodes the expected discounted future occupancy of states. The SR decomposes value functions into expected state occupancies and immediate rewards, allowing for efficient transfer and generalization.
- **Prioritized Experience Replay**: Standard approach uses TD-error to prioritize experiences. This paper augments it with the "need term" from SR.
- **Key variables**: TD-error (prediction error), need term (expected future state occupancy from SR), Q-values (action values), SR matrix M (tabular) or SR vectors m_s,a (deep)

---

### Prevailing model of the system under study

The prevailing model for experience replay prioritization, established by Prioritized Experience Replay (PER, Schaul et al., 2016), holds that experiences should be prioritized based on their TD-error (prediction error). The underlying assumption is that experiences with larger prediction errors provide more learning signal and should be replayed more frequently. This approach has been widely adopted in both tabular RL (Prioritized Sweeping) and deep RL (PER in DQN). The model does not consider the expected utility or relevance of learning about particular states to the agent's current situation—only the magnitude of the prediction error matters.

---

### What this paper contributes

This paper introduces the "need term"—derived from successor representation and inspired by biological memory replay—into computational experience replay algorithms. The key contributions are:

1. **Normative justification**: The paper provides a principled argument for why experiences should be prioritized based on both gain (TD-error) and need (expected future relevance), grounded in the successor representation framework.

2. **Algorithmic extensions**: Developed PS-SR (Prioritized Sweeping with SR) and PER-SR (Prioritized Experience Replay with SR) that incorporate the need term into tabular and deep RL settings respectively.

3. **Empirical validation**: Demonstrated that adding the need term significantly improves performance across multiple benchmarks—Dyna-Q maze, Blind Cliffwalk, and Atari games—compared to TD-error-only prioritization.

4. **Practical implementation**: Addressed computational challenges by using need terms to modulate Q-update magnitudes rather than sampling probabilities, making the approach feasible for large replay buffers.

5. **Overfitting mitigation**: Showed that the need term helps mitigate overfitting to high TD-error transitions, a problem observed in standard PER.

---

### Brain regions & systems

Not applicable. This is a purely computational paper. However, the work draws inspiration from neuroscience research on hippocampal replay, particularly work by Mattar & Daw (2018) showing that biological replay prioritizes memories based on both prediction error and expected future relevance (need).

---

### Mechanistic insight

The paper does not meet the high bar for mechanistic insight because it is purely computational—no neural data is provided that specifically supports the proposed algorithm over alternatives. The paper proposes an algorithmic framework (combining successor representation with experience replay) and validates it through behavioral performance metrics in simulated environments.

However, the successor representation itself has been linked to biological neural systems in prior work. The hippocampus and prefrontal cortex have been proposed as neural substrates for SR-like representations (Gershman et al., 2012; Stachenfeld et al., 2017). The paper cites Mattar & Daw (2018) showing that hippocampal replay in biological organisms follows similar prioritization principles (gain + need). Thus, while this paper does not provide new mechanistic insights, it connects computational RL to existing neurobiological findings about replay prioritization.

The paper's contribution is at the algorithmic level (Marr's level 2): it specifies the representations (SR, need terms, Q-values) and processes (TD-learning for SR, need-modulated Q-updates) that implement prioritized experience replay. The computational level (Marr's level 1) is the normative argument for why prioritizing by both gain and need is optimal for sample efficiency.

---

### Limitations & open questions

- **Limited game selection**: Only tested on a subset of Atari games (not the full 49 games used in the original PER paper), limiting generalization claims.
- **Slower early learning**: PER-SR learned slower initially compared to PER, likely because the SR network needs time to learn accurate representations before need terms become useful.
- **Computational cost**: Calculating need terms for all transitions in the replay buffer would be prohibitively expensive for large buffers; the paper addressed this by modulating Q-update magnitudes instead of sampling probabilities, but this is a compromise.
- **Negative need values**: Early in training, the SR network produced inaccurate estimates, sometimes resulting in negative need values that required mitigation (subtracting minimum need value).
- **Backward relevance unexplored**: The paper only considered forward relevance (future states), but backward relevance (states leading to current state) might also be beneficial, as suggested by Prioritized Sweeping's backward sweep mechanism.
- **Game-specific performance**: Performance improvements were larger in games with recurring similar states; games without these traits may benefit less from SR-based prioritization.

---

### Connections & keywords

**Key citations**: Schaul et al. (2016) [PER], Mattar & Daw (2018) [neuroscience of replay], Dayan (1993) [successor representation], Barreto et al. (2018) [successor features], Kulkarni et al. (2016) [deep successor reinforcement learning], Sutton & Barto (2014) [RL textbook], Mnih et al. (2015) [DQN], Brittain et al. (2020) [PSER], Gershman et al. (2012) [successor representation and temporal context]

**Named models or frameworks**: Prioritized Experience Replay (PER), Prioritized Sweeping (PS), Successor Representation (SR), Deep Successor Representation (DSR), Successor Features (SF), Dyna-Q, Deep Q-Network (DQN), Double DQN

**Brain regions**: Not applicable (computational paper)

**Keywords**: experience replay, successor representation, prioritized experience replay, prioritized sweeping, reinforcement learning, TD-error, need term, sample efficiency, deep reinforcement learning, Q-learning, Atari games, Dyna maze, function approximation, transfer learning, replay prioritization
