---
source_file: "rosenberg2021_learning_maze_navigation.md"
paper_id: "rosenberg2021_learning_maze_navigation"
title: "Mice in a labyrinth show rapid learning, sudden insight, and efficient exploration"
authors: "Matthew Rosenberg, Tony Zhang, Pietro Perona, Markus Meister"
year: 2021
journal: "eLife"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse", "human"]
brain_regions: ["hippocampus", "prefrontal_cortex"]
frameworks: ["reinforcement_learning"]
keywords: ["tolman_ec_1948_cognitive_maps", "gallistel_et_al_2004_discontinuous_learning_curves", "carandini_and_churchland_2013_2afc_task_limitations", "bruce_1959_rapid_olfactory_learning_bruce_effect", "fanselow_and_bolles_1979_fear_conditioning", "fonio_et_al_2009_free_exploration_in_rodents", "wood_et_al_2018_honeycomb_maze", "behrens_et_al_2018_cognitive_maps_and_flexible_behavior", "named_models_or_frameworks", "cognitive_map_tolman", "biased_random_walk_model", "markov_chain_models_fixed_depth_and_variable_depth", "two_alternative_forced_choice_2afc_paradigm", "ariadnes_thread_theseus_strategy", "brain_regions", "hippocampus_implied", "for_cognitive_maps_and_path_integration", "prefrontal_cortex_implied", "for_behavioral_strategy_switching", "dopaminergic_systems_implied"]
---

### One-line summary

Mice navigating a complex 6-level binary tree maze exhibit rapid few-shot learning (perfect navigation after ~10 rewards), discontinuous "insight" moments, and efficient exploration driven by local turning biases rather than global memory.

### Background & motivation

Most laboratory learning studies use simple two-alternative-forced-choice (2AFC) tasks that animals learn slowly (weeks to months, thousands of trials). This contrasts with natural behaviors like language acquisition or learning to balance a bicycle, where rapid learning occurs after few experiences. The authors sought to study complex decision-making in a more naturalistic setting where mice can exhibit rapid, flexible learning without extensive human intervention or shaping.

### Methods

- **Task**: Unconstrained exploration of a 6-level binary tree maze (63 T-junctions, 64 end nodes) with one water port at a deep end node
- **Subjects**: 20 C57BL/6J mice (10 water-deprived/rewarded, 10 sated/unrewarded), ages 45-98 days, both sexes
- **Procedure**: Single 7-hour recording session during dark phase; no handling or training; free movement between home cage and maze
- **Tracking**: DeepLabCut for pose estimation (nose, mid-body, tail base, four feet) from infrared video recorded below transparent maze floor
- **Analysis**: Node sequence extraction (127 nodes), Markov chain models of decision-making, efficiency metrics for exploration

### Key findings

- **Rapid learning**: All 10 water-deprived mice discovered the water port within 2000 seconds and <17 bouts; perfect navigation (6 correct decisions) achieved after ~10 reward experiences
- **Discontinuous insight**: At least 5 of 10 rewarded mice showed sudden, step-like improvements in navigation efficiency localized to ~200 second precision; separate "insights" for reward collection vs. direct path planning
- **One-shot homing**: On first exit from the maze, mice performed perfect home runs from end nodes (6 correct decisions) without prior practice; home paths had minimal overlap with entry paths
- **Exploration dominance**: Mice spent 84-95% of maze time in exploration (not direct to goals); exploration persisted even after task mastery and in unrewarded animals
- **Local turning biases**: Four consistent biases explained ~87% of exploration efficiency: (1) forward bias from stem (PSF ~0.83), (2) forward bias from branch (PBF ~0.83), (3) alternation bias (PSA ~0.63), (4) stem-preference from branch (PBS ~0.57)
- **Maze rotation robustness**: After 180-degree rotation of maze (disrupting external cues), 3/4 mice navigated correctly to water port on first entry; brief disruptions in performance resolved within an hour
- **Prediction limits**: Best Markov models left ~1.24 bits uncertainty per decision (from 1.585 bits prior), suggesting substantial but not complete predictability

### Computational framework

The paper employs a **Markov decision process** framework to model mouse navigation. The animal's trajectory is treated as a sequence of states (nodes) and actions (transitions between nodes). The authors formalize exploration efficiency as E = 32/N32, where N32 is the number of visits needed to discover half the 64 end nodes. They compare observed behavior against:

1. **Unbiased random walk**: baseline with no memory or biases (E ≈ 0.23)
2. **Biased random walk**: 4-parameter model using local turning biases (E ≈ 0.42, explaining ~87% of observed efficiency)
3. **Fixed-depth Markov chains**: history-dependent models with k preceding states
4. **Variable-depth Markov chains**: pruned history trees with average depth ~4, achieving best predictions

The framework treats navigation as a stochastic process where recent history (last ~4 locations) constrains but does not fully determine future actions. The remaining ~1.24 bits/action uncertainty is interpreted as potentially irreducible behavioral variability.

### Prevailing model of the system under study

Before this study, the field's understanding of rodent spatial learning was shaped by two contrasting paradigms:

1. **Rapid specialized learning**: One-shot learning systems like the Bruce effect (olfactory memory of mate) and fear conditioning establish simple 1-bit associations after single experiences. These are implemented by specialized circuits (accessory olfactory bulb, amygdala) but are limited to specific, evolutionarily important associations.

2. **Slow general learning**: Complex tasks in conventional 2AFC boxes (steering wheels, lever presses) require thousands of trials (weeks to months) to learn even simple 1-bit discriminations. The prevailing assumption was that complex multi-step navigation would similarly require extensive training and gradual improvement.

For navigation specifically, the field assumed that efficient exploration requires global memory of visited places (often called "cognitive maps"). The prevailing view held that animals gradually build up spatial representations through experience, practicing short routes before long ones, and using external cues (visual, olfactory) to guide navigation.

### What this paper contributes

This paper challenges the prevailing model in several key ways:

1. **Rapid learning of complex tasks**: Unlike 2AFC tasks that require thousands of trials for 1-bit learning, mice learned a ~10-bit task (6 correct decisions among 3 options each) in ~10 trials — a learning rate 1000-fold higher than 2AFC experiments. This bridges the gap between specialized one-shot learning systems and slow general learning.

2. **Discontinuous insight moments**: Learning is not always gradual. At least half the animals showed sudden, step-like improvements in performance localized to ~200 seconds. These "insights" occurred separately for different behavioral components (reward collection vs. direct path planning), suggesting distinct knowledge acquisition events rather than incremental parameter updates.

3. **One-shot homing without practice**: Contrary to expectations of gradual route learning, mice executed perfect 6-decision home runs on their very first attempt from deep in the maze, with no prior practice of shorter routes. This suggests an innate "Ariadne's thread" capability for path integration or egress planning.

4. **Local rules explain global efficiency**: Efficient exploration does not require global memory of visited places. Simple local turning biases (four parameters) explain ~87% of observed exploration efficiency. The remaining variability can be captured by Markov models using only the last ~4 locations, not long-term place memory.

5. **Navigation without external cues**: Maze rotation experiments showed that mice do not depend on external cues (visual, olfactory marks) attached to the maze for navigation. They navigated correctly immediately after 180-degree rotation, suggesting use of internal representations ("cognitive maps") rather than external gradients.

### Brain regions & systems

Not applicable — this is a purely behavioral study with no neural recordings or manipulations. However, the findings constrain possible neural mechanisms:

- **Hippocampal formation**: The one-shot homing and rapid learning of complex spatial sequences suggests involvement of hippocampal or hippocampal-cortical circuits for sequence learning and path integration
- **Prefrontal cortex**: The "insight" moments and switching between behavioral strategies (exploration vs. exploitation) may involve prefrontal circuits for cognitive control
- **Dopaminergic systems**: Reward learning and the shift from exploration to exploitation likely involve dopaminergic reinforcement learning signals, though the discontinuous nature of learning challenges conventional RPE-based models

### Mechanistic insight

This paper does **not** meet the bar for mechanistic insight because it provides no neural data linking proposed algorithms to biological implementation. However, it provides strong behavioral constraints on possible algorithms:

The paper establishes that efficient exploration can be achieved through purely **local turning rules** without global memory. The four biases (forward preferences from stem and branch, alternation preference, stem preference from branch) constitute an algorithmic-level description of exploration behavior. The authors formalize this as a biased random walk and show it explains ~87% of observed efficiency.

However, the paper lacks neural evidence that would distinguish this algorithm from alternatives. No recordings, lesions, pharmacological manipulations, or genetic tools are used to link the behavioral algorithm to specific neural circuits. The authors speculate about hippocampal involvement in path integration and cognitive maps, but these remain untested hypotheses.

Thus, while the paper provides a clear algorithmic-level description (local turning rules), it does not bridge to the implementational level (neural circuits) or provide neural evidence favoring this algorithm over alternatives.

### Limitations & open questions

1. **No neural data**: The study is purely behavioral; neural mechanisms remain speculative
2. **Single session**: Each animal was observed for only one night; long-term learning and memory retention were not studied
3. **Single maze geometry**: Only a symmetric binary tree was tested; generalization to other maze types unknown
4. **Water reward only**: Only water deprivation was used as motivation; other reward types or aversive learning not tested
5. **C57BL/6J only**: Only one strain was tested; genetic variation in strategies unknown
6. **Discontinuity mechanism unclear**: While sudden insights were observed, their neural or algorithmic basis remains unexplained
7. **Path integration unproven**: One-shot homing suggests path integration, but alternative explanations (e.g., odor trails) cannot be fully excluded

### Connections & keywords

**Key citations:**
- Tolman EC (1948) - cognitive maps
- Gallistel et al. (2004) - discontinuous learning curves
- Carandini & Churchland (2013) - 2AFC task limitations
- Bruce (1959) - rapid olfactory learning (Bruce effect)
- Fanselow & Bolles (1979) - fear conditioning
- Fonio et al. (2009) - free exploration in rodents
- Wood et al. (2018) - honeycomb maze
- Behrens et al. (2018) - cognitive maps and flexible behavior

**Named models or frameworks:**
- Cognitive map (Tolman)
- Biased random walk model
- Markov chain models (fixed-depth and variable-depth)
- Two-alternative-forced-choice (2AFC) paradigm
- Ariadne's thread / Theseus strategy

**Brain regions:**
- Hippocampus (implied, for cognitive maps and path integration)
- Prefrontal cortex (implied, for behavioral strategy switching)
- Dopaminergic systems (implied, for reinforcement learning)

**Keywords:**
maze navigation, spatial learning, few-shot learning, insight learning, exploration behavior, turning biases, Markov models, cognitive maps, path integration, binary tree maze, decision making, behavioral states, home run navigation, rapid learning, discontinuous learning curves, egocentric navigation, allocentric navigation