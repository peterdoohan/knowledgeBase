---
source_file: spiers2015_detour_problem_navigation.md
paper_id: spiers2015_detour_problem_navigation
title: "Solving the detour problem in navigation: a model of prefrontal and hippocampal interactions"
authors:
  - "Hugo J. Spiers"
  - "Sam J. Gilbert"
year: 2015
journal: "Frontiers in Human Neuroscience"
paper_type: review
contribution_type: review
species:
  - human
tasks:
  - detour_task
methods:
  - electrophysiology
  - fmri
  - lesion
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - prefrontal_cortex
  - striatum
  - retrosplenial_cortex
frameworks:
  - reinforcement_learning
keywords:
  - detour_problem
  - spatial_navigation
  - prefrontal_cortex
  - hippocampus
  - cognitive_map
  - prediction_error
  - route_planning
  - model_based_control
  - reinforcement_learning
  - goal_directed_behavior
  - virtual_reality
  - place_cells
  - subgoal_processing
  - frontopolar_cortex
  - solving
  - detour
  - problem
  - navigation
  - model
  - prefrontal
key_citations:
  - tolman1948_cognitive_maps_rats
  - daw2011_model_based_striatal_prediction
wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation
  - wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory
  - wiki/topics/successor_representation_as_a_predictive_map_for_flexible_planning
---

### One-line summary

The prefrontal cortex, not the hippocampus, consistently responds to forced detours during navigation, with lateral PFC detecting prediction errors, frontopolar PFC supporting subgoal generation, and the hippocampus tracking path distance to goals.

### Background & motivation

Despite extensive research on spatial navigation and decision-making, surprisingly little is known about how the brain solves the detour problem—when a learned route is blocked and an alternative must be found. This review addresses the gap by synthesizing evidence from functional neuroimaging, single unit recording, and lesion studies to understand the neural mechanisms underlying flexible route replanning.

### Methods

- **Literature review**: Systematic review of 9 human neuroimaging studies (PET and fMRI) examining forced detours during navigation in virtual environments
- **Synthesis approach**: Integration of findings across neuroimaging, rodent single unit recording, and human/rodent lesion studies
- **Model development**: Conceptual model of prefrontal-hippocampal interactions based on empirical evidence and reinforcement learning theory
- **Comparative analysis**: Comparison of PFC responses across spatial and non-spatial tasks to identify domain-general processes

### Key findings

- **Consistent PFC activation**: All 9 neuroimaging studies reviewed reported increased prefrontal cortex activity during detour conditions compared to non-detour conditions
- **Frontopolar PFC (BA 10)**: Most consistently activated region across studies; implicated in subgoal generation and goal-subgoal integration during detour replanning
- **Lateral PFC**: Activated in response to unexpected environmental changes requiring route adjustment; proposed to signal model-based prediction errors about route expectations
- **Superior PFC (BA 6)**: Active during conflict between alternative route options; may support conflict resolution during multi-route planning
- **Hippocampal findings**: Contrary to predictions, the hippocampus did not show consistent increased activity during detours across the 9 studies; two studies showed decreased activity
- **Hippocampal path distance encoding**: Howard et al. (2014) found right posterior hippocampal activity correlated with the magnitude of change in path distance to the goal at detours, suggesting the hippocampus tracks path distance rather than detour detection per se
- **Rodent lesion evidence**: Hippocampal lesions in rats (Winocur et al., 2010) impaired optimal detour taking in a learned environment, but navigation was still possible, suggesting hippocampus supports optimal path selection rather than detour capability itself
- **Place cell remapping**: Alvernhe et al. (2011) found local remapping of place fields near barrier locations during detours, but this geometric response was not specific to detour processing

### Computational framework

The paper employs **reinforcement learning (RL) theory** to conceptualize navigation control systems:

- **Model-based control**: Uses a cognitive map representation of the environment to enable tree-search planning and flexible route selection; associated with hippocampal-parahippocampal systems
- **Model-free control**: Uses cached action-value associations (habits) learned through experience; less computationally demanding but less flexible; associated with striatal systems
- **Prediction error signals**: Model-based prediction errors (deviations from expected route outcomes) are proposed to trigger lateral PFC responses and initiate route replanning

The framework also incorporates **vector-based navigation** concepts, where the entorhinal/subicular region encodes the direction and Euclidean distance to goals, potentially guiding path selection during detours.

### Prevailing model of the system under study

Prior to this review, the dominant theoretical framework (stemming from O'Keefe and Nadel, 1978) held that the hippocampus was essential for flexible, map-based navigation. Given this perspective, one would predict that the hippocampus would be more active during detours, as these situations require memory retrieval, new learning, and flexible route replanning. The prefrontal cortex was known to support executive functions and flexible behavior, but its specific role in navigation and detour processing was less well characterized. The prevailing view also distinguished between hippocampal-dependent "locale" navigation (map-based) and striatal-dependent "taxon" navigation (response-based).

### What this paper contributes

This review challenges the expectation that the hippocampus would be more active during detours by showing that, contrary to predictions, none of the 9 neuroimaging studies reviewed found increased hippocampal activity during detours (and two found decreased activity). Instead, the prefrontal cortex emerges as the key region for detour processing. The paper synthesizes evidence to propose a novel conceptual model where:

1. **Lateral PFC** detects prediction errors when the expected route is blocked
2. **Frontopolar PFC** supports subgoal generation and route replanning
3. **Superior PFC** resolves conflict between alternative route options
4. **Hippocampus** tracks path distance to the goal and may simulate future paths

This model reframes the hippocampus as representing path distance information rather than primarily detecting detours, and establishes the PFC as central to flexible route replanning. The paper also bridges spatial navigation and non-spatial executive function literatures by showing how frontopolar PFC contributes to goal-subgoal integration across domains.

### Brain regions & systems

- **Prefrontal cortex (PFC)** — Core region for detour processing; multiple subregions play distinct roles:
  - **Frontopolar PFC (BA 10)** — Most consistently activated across studies; involved in subgoal generation, goal-subgoal integration, and route replanning
  - **Lateral PFC** — Responds to unexpected environmental changes; proposed to signal model-based prediction errors about route expectations; involved in detecting the need for route adjustment
  - **Superior PFC / superior frontal gyrus (BA 6)** — Active during conflict between alternative routes; may support conflict resolution and decision-making between path options
  - **Ventrolateral PFC** — Activated in some detour studies; role in route planning
  - **Medial PFC / ventromedial PFC** — Less consistently activated; may code reward value of goals and "regret" signals
  
- **Hippocampus / hippocampal-parahippocampal regions** — Contrary to predictions, not consistently more active during detours; proposed to track path distance to goals and simulate future paths; right posterior hippocampus specifically shows correlation with change in path distance at detours

- **Entorhinal cortex / subicular region** — Encodes Euclidean distance and allocentric direction to goals; may provide vector information for path planning

- **Striatum** — Associated with model-free (habit-based) navigation; less flexible but computationally efficient; tracks action value in reinforcement learning frameworks

- **Posterior parietal cortex** — Not discussed in detail in this review but noted to potentially play a role in route planning and spatial novelty detection

- **Retrosplenial cortex** — Part of the broader navigation network; not specifically discussed for detour processing

### Mechanistic insight

The paper does not meet the high bar for mechanistic insight as defined in the criteria. While it proposes a conceptual model of prefrontal-hippocampal interactions for detour navigation, it does not present or formalize a specific algorithm that could explain the phenomenon, nor does it provide new neural data that specifically supports such an algorithm over alternatives. Instead, this is a review paper that synthesizes existing evidence from multiple studies to propose a conceptual framework. The paper references computational models by Martinet et al. (2011) and Hirel et al. (2013) that formalize PFC-hippocampal interactions in rodent navigation, but these are cited as existing work rather than novel contributions of this review. The value of this paper lies in its synthesis of disparate literatures and its generation of testable hypotheses about regional specialization within the PFC for detour processing, rather than in providing mechanistic insight at the algorithmic or implementational level.

### Limitations & open questions

- **Limited animal data**: Prefrontal responses to detours have not been characterized in rodents or non-human primates; the imperfect homology between primate and rodent PFC precludes straightforward cross-species comparisons
- **Parietal cortex underexplored**: The role of posterior parietal cortex in detour processing is not discussed in detail due to lack of single unit, lesion, and neuropsychological evidence, and inconsistent neuroimaging findings
- **Lack of neuropsychological evidence**: No studies have specifically tested patients with frontal lobe damage on optimal detour taking in navigation tasks
- **Model-based vs. model-free dissociation**: Further studies needed to tease apart involvement of model-based and model-free systems during detours
- **Remote vs. recent memory**: Most studies examined recently learned environments; the model's applicability to remotely learned environments requires further investigation
- **Shortcut processing**: The model does not fully address how the system processes situations where a new shortcut becomes available (as opposed to forced detours)
- **Option processing**: How the system processes different route options and selects among them is not fully understood
- **PFC-hippocampus interaction dynamics**: The extent and timing of reciprocal interactions between PFC and hippocampus during detour planning remain to be characterized

### Connections & keywords

- **Key citations**:
  - Tolman (1948) - cognitive map theory and early behavioral studies of detours
  - O'Keefe and Nadel (1978) - hippocampus as cognitive map
  - Maguire et al. (1998) - first neuroimaging study of forced detours
  - Spiers and Maguire (2006) - event-related analysis of detours with taxi drivers
  - Howard et al. (2014) - hippocampal encoding of path distance during detours
  - Simon and Daw (2011) - model-based fMRI analysis of navigation
  - Winocur et al. (2010) - hippocampal lesion study of detours in rodents
  - Alvernhe et al. (2011) - place cell remapping during detours

- **Named models or frameworks**:
  - Cognitive map theory (Tolman; O'Keefe and Nadel)
  - Reinforcement learning framework (Sutton and Barto)
  - Model-based vs. model-free control systems
  - Vector-based navigation (Burgess and O'Keefe; Kubie and Fenton)
  - Goal-subgoal integration / cognitive branching (Koechlin et al.)
  - Gateway hypothesis of rostral PFC function (Burgess et al.)
  - Multiple-demand system (Duncan)

- **Brain regions**:
  - Prefrontal cortex (PFC) - frontopolar (BA 10), lateral, superior (BA 6), ventrolateral, medial, ventromedial
  - Hippocampus (posterior, right posterior)
  - Entorhinal cortex
  - Subiculum
  - Striatum
  - Posterior parietal cortex
  - Retrosplenial cortex

- **Keywords**: detour problem, spatial navigation, prefrontal cortex, hippocampus, cognitive map, prediction error, route planning, model-based control, reinforcement learning, goal-directed behavior, virtual reality, place cells, subgoal processing, frontopolar cortex

### Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]
- [[wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation|Hippocampal–prefrontal mechanisms of route planning and detour navigation]]
- [[wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory|Medial prefrontal cortex in goal-directed spatial navigation and spatial working memory]]
- [[wiki/topics/successor_representation_as_a_predictive_map_for_flexible_planning|Successor representation as a predictive map for flexible planning]]
