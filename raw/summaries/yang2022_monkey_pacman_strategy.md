---
source_file: "yang2022_monkey_pacman_strategy.md"
paper_id: "yang2022_monkey_pacman_strategy"
title: "Monkey plays Pac-Man with compositional strategies and hierarchical decision-making"
authors: "Qianli Yang, Zhongqiao Lin, Wenyi Zhang, Jianshu Li, Xiyuan Chen, Jiaqi Zhang, Tianming Yang"
year: 2022
journal: "eLife"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human", "macaque", "monkey"]
methods: ["computational_modeling"]
brain_regions: ["prefrontal_cortex", "orbitofrontal_cortex", "dorsolateral_prefrontal_cortex"]
frameworks: ["reinforcement_learning", "hierarchical_rl"]
keywords: ["botvinick_et_al_2009", "botvinick_and_weinstein_2014_hierarchical_rl_and_human_action_control", "sutton_et_al_1999_temporal_abstraction_in_rl", "dezfouli_and_balleine_2013", "ostlund_et_al_2009_hierarchical_organization_of_behavior", "mnih_et_al_2015_deep_q_network_flat_rl_comparison", "van_seijen_et_al_2017_multi_agent_hierarchical_rl_for_pac_man", "nassar_et_al_2012", "urai_et_al_2017_pupil_linked_arousal_and_decision_making", "leong_et_al_2017", "wilson_and_niv_2011_selective_attention_in_decision_making", "named_models_or_frameworks", "dynamic_compositional_strategy_model_the_papers_main_model", "take_the_best_ttb_heuristic", "six_basis_strategies_local", "global", "evade_blinky", "evade_clyde", "approach", "energizer"]
---

### One-line summary

Macaque monkeys trained to play Pac-Man use compositional strategies and hierarchical decision-making with a "take-the-best" heuristic, achieving over 90% prediction accuracy with a dynamic strategy model.

### Background & motivation

Complex decision-making in humans often relies on heuristic strategies that decompose difficult problems into manageable sub-goals. While animals demonstrate complex behaviors in nature, quantitative studies of strategic decision-making in non-human animals have been limited by insufficiently complex behavioral paradigms. The gap in understanding how animals manage multiple strategies to solve sophisticated tasks motivated development of a quantifiable yet complex behavior paradigm.

### Methods

- **Subjects**: Two male rhesus macaques (Macaca mulatta), named O and P
- **Task**: Adapted Pac-Man video game where monkeys used a joystick to navigate Pac-Man through a maze to collect pellets and energizers while avoiding or chasing two ghosts (Blinky and Clyde)
- **Training**: Three-stage progressive training over 392 sessions (Monkey O) and 412 sessions (Monkey P)
- **Data collection**: 74 testing sessions with 3,217 games, 15,772 rounds, and 899,381 joystick movements; eye movements and pupil sizes recorded at 500-1000 Hz
- **Modeling**: Dynamic compositional strategy model with six basis strategies (local, global, evade-Blinky, evade-Clyde, approach, energizer) combined via softmax policy with time-varying weights estimated via maximum likelihood with change-point detection
- **Comparison models**: Static strategy model, linear approximate RL (LARL), and linear perceptron

### Key findings

- The dynamic compositional strategy model achieved 90.4% overall prediction accuracy (Monkey O: 90.7%, Monkey P: 90.0%), significantly outperforming static (81.6%), LARL (66.9%), and perceptron (62.4%) models
- Monkeys adopted a "take-the-best" (TTB) heuristic: the dominant strategy weight (0.907 ± 0.117) was significantly larger than secondary (0.273 ± 0.233) and tertiary (0.087 ± 0.137) strategies
- In over 90% of time points, the weight difference between first and second strategies exceeded 0.1; in 33% of cases it exceeded 0.9
- Strategy usage was context-dependent: _local_ strategy dominated early game (abundant pellets), _global_ strategy became prominent in late game (scarce local pellets), _approach_ strategy activated when ghosts were scared and nearby
- Monkeys formed compound strategies: _planned attack_ (energizer consumption followed by ghost chasing) and _suicide_ (deliberate death to reset game when pellet distribution was unfavorable)
- Eye movements validated strategy labels: fixation patterns shifted to match strategy-relevant game elements (ghosts during _approach_, pellets during _local_, energizers during _energizer_ strategy)
- Pupil dilation increased transiently around strategy transitions (p<0.01), consistent with hierarchical decision-making requiring additional cognitive processing at strategy switches
- Monkeys demonstrated sophisticated understanding of ghost "personalities": more likely to evade aggressive Blinky but could safely follow Clyde when nearby due to Clyde's avoidance behavior at close range

### Computational framework

The study employs a **hierarchical reinforcement learning framework** with **compositional strategies**. The core computational ideas are:

- **Hierarchical decision-making**: Three-level hierarchy with (1) action selection (joystick movements), (2) basis strategy selection, and (3) optional compound strategy assembly
- **Take-the-best heuristic**: Rather than averaging multiple strategies, the brain selects a single dominant strategy at each time point, reducing computational complexity
- **Softmax policy**: Actions chosen probabilistically based on weighted combination of strategy utilities: π(d|w) = exp(Q_d) / Σ exp(Q_d')
- **Dynamic strategy weights**: Strategy weights change over time via change-point detection, allowing flexible adaptation to game state changes
- **Basis strategy decomposition**: Complex decision-making decomposed into six simple, interpretable strategies (local, global, evade, approach, energizer), each focusing on a subset of game features

The framework contrasts with flat RL models (e.g., DQN, LARL) that evaluate all actions directly using all features, which are computationally expensive and less interpretable.

### Prevailing model of the system under study

Prior to this study, the prevailing understanding of animal decision-making in complex tasks was limited by the availability of sufficiently complex behavioral paradigms. Existing studies typically:
- Used simple rule-based tasks where strategies were mutually exclusive and cued explicitly
- Equated strategies with simple stimulus-response associations
- Focused on flat decision-making models where actions are computed directly from sensory features
- Lacked quantitative frameworks for studying how animals manage multiple strategies dynamically

The paper's introduction notes that while animals exhibit complex strategy-like behaviors in nature, "quantitative studies are lacking" and "the level of complexity of the existing animal behavioral paradigms is insufficient for studying how animals manage strategies to simplify a sophisticated task."

### What this paper contributes

This paper establishes that non-human primates can employ compositional strategies and hierarchical decision-making to solve complex tasks, demonstrating:

1. **Strategic competence in monkeys**: Macaques can learn and flexibly deploy multiple strategies in a dynamic, complex task without explicit instruction or cuing, challenging the view that strategic decision-making is uniquely human or requires linguistic capacities.

2. **Take-the-best heuristic**: Rather than averaging across multiple strategies, monkeys predominantly use a single dominant strategy at each decision point, simplifying computational demands. This provides empirical evidence for heuristic decision-making in non-human animals.

3. **Compound strategy formation**: Monkeys can assemble basis strategies into higher-level compound strategies (e.g., planned attacks combining energizer collection with ghost hunting), demonstrating compositional cognitive abilities previously difficult to quantify in animals.

4. **Hierarchical solution to complex problems**: The superiority of the hierarchical model over flat RL models suggests monkeys organize behavior hierarchically, matching the most successful AI approaches to the same task.

5. **Physiological markers of strategy**: Pupil dilation and eye movements provide independent validation of strategy labels and reveal cognitive costs associated with strategy transitions.

### Brain regions & systems

Not applicable — this study is purely behavioral and computational, with no neural recordings or manipulations. However, the authors discuss that future work should investigate the neural mechanisms underlying strategy-based decision-making, suggesting the prefrontal network (dorsolateral prefrontal cortex, orbitofrontal cortex, polar cortex) as likely candidates given its role in rule use and rule switching documented in prior studies.

### Mechanistic insight

This paper does not meet the bar for mechanistic insight because it does not provide neural data supporting the algorithmic model. The study provides behavioral and computational evidence for hierarchical strategy-based decision-making in monkeys, but lacks neural recordings or manipulations that would link the model's variables to specific neural activity patterns.

The paper proposes a hierarchical RL algorithm and validates it behaviorally through model fitting, eye movements, and pupil dilation. However, without neural data showing that brain activity tracks strategy weights, transitions, or the hierarchical structure posited by the model, the mechanistic claims remain at the computational and algorithmic levels without implementational grounding. Future work combining this paradigm with neural recordings would be needed to establish mechanistic insight.

### Limitations & open questions

- The particular set of basis strategies was hand-crafted by the researchers; it remains unknown whether monkeys naturally develop these specific strategies or whether alternative decompositions would be equally valid
- The study does not investigate the neural mechanisms underlying strategy selection and transitions; future work combining this paradigm with neural recordings is needed
- Only two monkeys were tested, limiting generalizability to the broader macaque population
- The training period was extensive (hundreds of sessions), raising questions about the scalability of this approach for studying advanced cognition in animals
- The model assumes stable strategy weights within time windows, but the dynamics of how strategy transitions occur in real-time remain poorly understood
- It is unclear whether the take-the-best heuristic reflects a capacity limitation or an optimal computational strategy

### Connections & keywords

**Key citations:**
- Botvinick et al. (2009); Botvinick & Weinstein (2014) — hierarchical RL and human action control
- Sutton et al. (1999) — temporal abstraction in RL
- Dezfouli & Balleine (2013); Ostlund et al. (2009) — hierarchical organization of behavior
- Mnih et al. (2015) — Deep Q-Network (flat RL comparison)
- Van Seijen et al. (2017) — multi-agent hierarchical RL for Pac-Man
- Nassar et al. (2012); Urai et al. (2017) — pupil-linked arousal and decision-making
- Leong et al. (2017); Wilson & Niv (2011) — selective attention in decision-making

**Named models or frameworks:**
- Dynamic compositional strategy model (the paper's main model)
- Take-the-best (TTB) heuristic
- Six basis strategies: local, global, evade(Blinky), evade(Clyde), approach, energizer
- Two compound strategies: planned attack, suicide
- Linear approximate reinforcement learning (LARL) model
- Static strategy model
- Linear perceptron model
- Softmax policy

**Brain regions:**
- Dorsolateral prefrontal cortex (discussed as future research direction)
- Orbitofrontal cortex (discussed as future research direction)
- Polar cortex (discussed as future research direction)
- Prefrontal network (hypothesized to underlie strategy-based decision-making)

**Keywords:**
- Hierarchical decision-making
- Compositional strategies
- Take-the-best heuristic
- Strategy switching
- Reinforcement learning
- Complex behavior paradigm
- Non-human primate cognition
- Eye movements
- Pupil dilation
- Computational modeling
- Pac-Man game
- Macaque monkeys
