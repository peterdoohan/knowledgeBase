---
source_file: "shamash2021_mice_multi_step_routes.md"
paper_id: "shamash2021_mice_multi_step_routes"
title: "Mice learn multi-step routes by memorizing subgoal locations"
authors: "Philip Shamash, Sarah F. Olesen, Panagiota Iordanidou, Dario Campagner, Nabhojit Banerjee, Tiago Branco"
year: 2021
journal: "Nature Neuroscience"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
tasks: ["navigation_task"]
brain_regions: ["hippocampus", "striatum"]
frameworks: ["reinforcement_learning", "model_free_rl", "hierarchical_rl"]
keywords: ["okeefe_and_nadel_1978_the_hippocampus_as_a_cognitive_map", "tolman_1948_cognitive_maps_in_rats_and_men", "morris_1981_spatial_localization_without_local_cues", "etienne_and_jeffery_2004_path_integration_in_mammals", "vale", "evans_and_branco_2017_rapid_spatial_learning_controls_instinctive_defensive_behavior_in_mice", "stachenfeld", "botvinick_and_gershman_2017_the_hippocampus_as_a_predictive_map", "named_models_or_frameworks", "cognitive_map_theory_okeefe_and_nadel", "taxon_strategies_okeefe_and_nadel", "hierarchical_reinforcement_learning_sutton", "precup_and_singh", "model_based_vs_model_free_reinforcement_learning", "path_integration", "subgoal_memorization_strategy_novel_contribution", "brain_regions", "hippocampus_hypothesized_for_allocentric_spatial_memory", "dorsal_striatum_hypothesized_for_inflexible_route_repetition", "entorhinal_cortex_mentioned_in_context_of_cognitive_maps"]
---

### One-line summary

Mice rapidly learn efficient multi-step escape routes by memorizing allocentric subgoal locations (obstacle edges) encountered during spontaneous exploratory "practice runs" rather than building cognitive maps or repeating habitual movements.

### Background & motivation

The behavioral strategies mammals use to learn multi-step routes in novel environments are unknown. While previous work identified cognitive map-based navigation and inflexible taxon strategies in constrained maze training, it remains unclear how animals spontaneously acquire spatial knowledge for efficient goal-directed navigation under natural time constraints. Escape behavior offers a powerful model for studying naturalistic navigation due to reliable stimulus-locked trajectories and rapid learning within single sessions.

### Methods

- **Subjects**: 158 male C57BL/6J mice (8–12 weeks old), singly housed
- **Behavioral platform**: Elevated circular platform (92 cm diameter) with shelter and removable white acrylic wall obstacle (50 cm long × 12.5 cm tall) positioned between threat zone and shelter
- **Escape task**: Loud crashing sound (87 dB) delivered when mouse in threat zone; analyzed first 3 escape trials per mouse
- **Food-seeking task**: Mice trained to approach reward port in response to 10-kHz tone; tested on platform with same geometry as escape task
- **Tracking**: DeepLabCut pose estimation (13 body parts) at 30 Hz, custom Python analysis
- **Key metrics**: 
  - Escape target score (0 = shelter-directed, 1.0 = obstacle edge-directed)
  - Spatial efficiency (ratio of shortest path to actual path)
  - Homing runs (spontaneous turn-and-run movements toward shelter/obstacle edges)

### Key findings

- **Rapid learning of efficient escape routes**: Mice progressed from inefficient homing-vector escapes (57% on trial 1) to efficient edge-vector escapes (90% by trial 3) within 20 min. Spatial efficiency improved from median 0.77 (trial 1) to 0.87 (trial 3; F(2,30) = 7.2, P = 0.003).

- **Spatial memory strategy**: After obstacle removal, mice continued running toward the former obstacle edge location (median target = 0.98), demonstrating memory-guided navigation. 44% of escapes 9±5 min after obstacle removal still targeted the former edge location (P = 0.02 vs. open field).

- **Visual cues required for naive but not experienced mice**: Naive mice in darkness performed fewer edge-vector escapes (33% vs. 74% with lights on; P = 0.002). After 20 min experience in light, mice could execute edge vectors in darkness (55% vs. 22% open field; P = 0.002).

- **Subgoal memorization not explained by habitual egocentric movements**: Repeating turn angles from previous homing runs did not explain variance in escape targets (R² = 0.0009 for most similar turn angle; R² = 0.97 in constrained corridor positive control).

- **Subgoals learned through practice homings, not cognitive map building**: 
  - 100% of edge-vector escapes after obstacle removal were preceded by at least one edge-vector homing during exploration (P = 0.02 vs. chance).
  - Edge-vector homings specifically to the same edge used in escape correlated with escape targets (r = 0.75, P = 5×10⁻⁵), but homings to opposite edge (r = 0.15, P = 0.5) or from shelter area (r = 0.30, P = 0.2) did not.
  - Mice without prior edge-vector homings showed no subgoal memory (13% edge vectors; P = 0.4 vs. open field).
  - Mice with threat side blocked during exploration (preventing long-range homings) showed no subgoal memory (20% edge vectors; P = 0.2 vs. open field).

- **Spontaneous edge-directed movements are instinctive**: Edge-directed movements occurred most in first few minutes, equally with/without shelter, but less with hole obstacle than wall obstacle (P = 0.0005). Hole obstacle learning took longer (20% edge vectors trials 2–3 vs. 67% trials 6–7).

- **Subgoal strategy generalizes to food-seeking**: In food-seeking task after obstacle removal, 53% of paths targeted former obstacle edge (vs. 12% open field; P = 0.006). Subgoal memory was not due to general increase in edge-directed exploratory movement (obstacle removed: median 3 edge-directed movements/15 min; obstacle present: 10; open field: 4; P = 0.9 for removed vs. open field).

### Computational framework

The paper frames navigation in terms of hierarchical reinforcement learning and hybrid model-based/model-free strategies. The subgoal memorization strategy combines elements of:
- **Model-based planning**: Allocentric spatial memory for subgoal locations enables flexible, efficient routes
- **Model-free habits**: Rapid all-or-none learning through practice movements; inflexible persistence of learned routes even after obstacle removal

The proposed algorithm: mice instinctively execute visually guided movements toward salient obstacle edges; if this movement provides direct access to a subsequent goal (shelter/reward), its target is memorized as a subgoal location. This differs from traditional cognitive map models (tree-search, map-partitioning) that require extensive environmental sampling to build internal maps before computing efficient routes.

### Prevailing model of the system under study

The field traditionally views rodent navigation through two dominant frameworks:
1. **Cognitive map-based navigation**: Hippocampus-dependent allocentric representation where animals build internal topological maps connecting locations, enabling computation of subgoal locations via tree-search or map-partitioning algorithms when new multi-step routes are required. Requires extensive environmental sampling to build the map.
2. **Taxon strategies**: Inflexible, stimulus-response behaviors learned through previous motivated actions—repeating egocentric movements at familiar junctions or using landmarks for visual guidance. These are model-free, rely on proximal cues, and do not involve allocentric spatial reasoning.

The prevailing assumption was that efficient multi-step route learning in novel environments requires cognitive map construction through environment investigation, or alternatively relies on habitual egocentric action repetition.

### What this paper contributes

The paper demonstrates that mice use a **hybrid subgoal memorization strategy** that does not fit cleanly into either traditional category:

1. **Subgoal learning is not cognitive map-based**: Standard cognitive map models predict that environmental sampling (exploring the obstacle and its edges) should correlate with subgoal formation. However, the amount of exploration near the obstacle or its edges did NOT correlate with subsequent escape targets (r = -0.09, P = 0.7; r = 0.06, P = 0.8). Investigating the formerly obstructed area after obstacle removal also did not suppress edge vector escapes. The key variable was not exploration quantity but specific "practice homings" targeting the obstacle edge.

2. **Subgoal learning is not habitual egocentric action repetition**: The memory-guided escapes could not be predicted from repeating turn angles from previous homing runs (R² = 0.0009), unlike in constrained environments where such prediction worked (R² = 0.97). Changing the starting conditions (blocking threat side during exploration) did not change escape angles, as would be expected if stereotyped egocentric responses were learned.

3. **Subgoal memorization is the key mechanism**: Mice memorize specific allocentric locations (obstacle edges) encountered during spontaneous "practice runs" that successfully lead to the goal. 100% of edge-vector escapes after obstacle removal were preceded by at least one prior edge-vector homing (P = 0.02). The correlation between edge-vector homings and escape targets was specific to the same edge (r = 0.75, P = 5×10⁻⁵) and direction (threat-to-shelter), not general exploration.

4. **The strategy is generalizable**: The same subgoal memorization strategy was observed in both escape (defensive) and food-seeking (appetitive) tasks, suggesting it is a fundamental building block for efficient goal-directed navigation.

### Brain regions & systems

Not applicable — this is a purely behavioral study with no neural recordings, lesions, or manipulations. The Discussion speculates about potential involvement of hippocampus (for allocentric spatial memory) and dorsal striatum (for inflexible route repetition) based on previous literature, but no neural data is presented.

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined in the template. While it proposes an algorithm (subgoal memorization through practice homings), it does not provide neural data supporting that algorithm over alternatives. The study is purely behavioral with no neural recordings, lesions, pharmacology, or imaging. The paper's contribution is at the level of identifying the behavioral strategy and learning rule, not at the neural implementation level.

### Limitations & open questions

- **Neural mechanisms unknown**: No neural data is presented; the hippocampus and striatum are hypothesized to be involved based on previous literature, but not tested.
- **Persistence of subgoal memory**: Edge vector escapes persisted over 20+ minutes and 7+ trials after obstacle removal; how mice eventually relearn direct routes remains unclear.
- **Spatial scale and generalization**: How subgoal memories transfer across days, obstacle types, and spatial scales was not tested.
- **Causal role of practice homings**: While correlational evidence strongly supports the practice homing hypothesis, experiments specifically manipulating the occurrence of edge-vector homings (e.g., by blocking them) were not performed.
- **All-or-none learning rule**: The paper hypothesizes a rapid learning moment when a successful practice homing is memorized as a subgoal, but the causal evidence for this specific learning rule is lacking.

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) — The Hippocampus as a Cognitive Map
- Tolman (1948) — Cognitive maps in rats and men
- Morris (1981) — Spatial localization without local cues
- Etienne & Jeffery (2004) — Path integration in mammals
- Vale, Evans & Branco (2017) — Rapid spatial learning controls instinctive defensive behavior in mice
- Stachenfeld, Botvinick & Gershman (2017) — The hippocampus as a predictive map

**Named models or frameworks:**
- Cognitive map theory (O'Keefe & Nadel)
- Taxon strategies (O'Keefe & Nadel)
- Hierarchical reinforcement learning (Sutton, Precup & Singh)
- Model-based vs. model-free reinforcement learning
- Path integration
- Subgoal memorization strategy (novel contribution)

**Brain regions:**
- Hippocampus (hypothesized for allocentric spatial memory)
- Dorsal striatum (hypothesized for inflexible route repetition)
- Entorhinal cortex (mentioned in context of cognitive maps)

**Keywords:**
spatial navigation, escape behavior, subgoal learning, multi-step routes, allocentric memory, obstacle avoidance, spatial memory, rodent behavior, cognitive map, defensive behavior, goal-directed navigation, practice homings, spontaneous exploration, threat response, behavioral strategy
