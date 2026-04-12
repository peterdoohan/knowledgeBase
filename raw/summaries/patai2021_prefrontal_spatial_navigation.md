---
source_file: "patai2021_prefrontal_spatial_navigation.md"
paper_id: "patai2021_prefrontal_spatial_navigation"
title: "The Versatile Wayfinder: Prefrontal Contributions to Spatial Navigation"
authors: "Eva Zita Patai, Hugo J. Spiers"
year: 2021
journal: "Trends in Cognitive Sciences"
paper_type: "review"
contribution_type: "review"
species: ["human"]
tasks: ["virtual_navigation", "navigation_task"]
methods: ["fmri", "lesion"]
brain_regions: ["hippocampus", "entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "anterior_cingulate_cortex", "orbitofrontal_cortex", "ventromedial_prefrontal_cortex", "dorsolateral_prefrontal_cortex", "posterior_cingulate_cortex"]
frameworks: ["reinforcement_learning"]
keywords: ["maguire_et_al_1998_earliest_study_showing_pfc_activation_during_virtual_navigation", "ekstrom_et_al_2003_seminal_human_intracranial_recording_study_showing_goal_selective_frontal_neurons", "spiers_and_maguire_2006", "2007_real_world_navigation_studies", "tolman_1948_cognitive_map_theory", "miller_and_cohen_2001_integrative_theory_of_pfc_function", "redish_2016_vte_and_hippocampal_function", "named_models_or_frameworks", "cognitive_map_theory_tolman", "core_navigation_network_hippocampus", "parahippocampus", "retrosplenial_cortex", "posterior_parietal_cortex", "hierarchical_planning_framework", "reinforcement_learning_model_based_and_model_free", "predictive_coding", "default_mode_network", "vicarious_trial_and_error_vte", "hippocampal_replay_and_preplay", "state_space_representation"]
---

### One-line summary

The prefrontal cortex plays a pivotal role in spatial navigation through goal selection, planning, adaptation to environmental changes, and value-based decision-making, operating in concert with the hippocampal formation and other core navigation regions.

### Background & motivation

Traditional models of spatial navigation have focused on a "core navigation network" comprising the hippocampus, parahippocampus, retrosplenial cortex, and posterior parietal cortex, with the striatum supporting stimulus-response navigation. The prefrontal cortex (PFC) has been largely overlooked in navigation theories despite its well-established roles in planning, decision-making, and goal maintenance. This review synthesizes recent evidence from humans, non-human primates, and rodents to establish the PFC as a crucial component of the mammalian navigation system.

### Methods

This is a narrative review that synthesizes findings across multiple species and methodologies:
- Human functional neuroimaging studies (fMRI, MEG) examining PFC activity during virtual navigation tasks
- Human intracranial recordings from presurgical epileptic patients
- Patient lesion studies (e.g., vmPFC damage)
- Non-human primate single-unit recordings during maze navigation
- Rodent lesion studies, immediate early gene expression, and electrophysiological recordings
- Cross-species anatomical comparisons of PFC regions

### Key findings

- **Route planning**: Multiple PFC regions are engaged during planning, including dorsomedial PFC (dmPFC), rostrodorsal medial PFC (rdmPFC), and lateral PFC (lPFC). Activity scales with planning complexity and route difficulty.

- **Goal representation and maintenance**: Medial PFC (mPFC) neurons show goal-selective activity that persists during travel. Ventromedial PFC (vmPFC) is critical for maintaining the current goal in mind during wayfinding; patients with vmPFC damage require reminders to navigate successfully.

- **Handling detours and environmental changes**: Superior frontal gyrus (SFG) and right lateral PFC (rlPFC) are specifically activated by detours requiring significant rerouting, but not by shortcuts. These regions detect prediction errors and initiate replanning.

- **Vicarious trial and error (VTE)**: At decision points, rodents exhibit VTE behavior (back-and-forth looking) that is hippocampal-dependent and disrupted by dmPFC lesions, pointing to a role in planning during memory-guided behavior.

- **PFC-hippocampus interactions**: Coordinated replay between CA1 and PFC is higher for trajectories that are subsequently taken. mPFC-hippocampal synchrony in theta band supports spatial memory retrieval and planning. The PFC may drive hippocampal activity during goal retrieval and facilitate rule switching.

- **Default-mode network (DMN) during navigation**: Core DMN regions including vmPFC are more active during ongoing travel compared to decision events, suggesting a role in internally-guided navigation when no immediate updates are needed.

- **Strategy switching**: Rodent medial PFC is necessary for switching between place and response strategies at maze junctions.

- **Value-based decision-making**: Orbitofrontal cortex (OFC) integrates environmental representations with action values, operating as a cognitive map of state space for value-based decisions. OFC is involved in updating and learning path values, not directly in choice behavior itself.

### Computational framework

The review adopts a Marr's three-level perspective implicitly, discussing:

- **Computational level**: Navigation requires solving problems of goal selection, path planning, progress monitoring, and value-based decision-making. The PFC contributes to these high-level computational demands that go beyond simple spatial localization.

- **Algorithmic level**: The PFC implements various algorithms including hierarchical planning (dmPFC/dACC), breadth-first search through possible paths (lPFC), prediction error detection (SFG/rlPFC), goal maintenance (vmPFC), and value-based state space mapping (OFC). The review discusses theta-band synchronization and replay events as neural mechanisms supporting these algorithms.

- **Implementational level**: The review discusses specific anatomical implementations across species (human dlPFC/vlPFC, rodent PL/IL, ACC/MCC) and their differential engagement during navigation stages. It emphasizes that PFC operates through functional networks interacting on local and global hierarchical architectures rather than as separate modules.

### Prevailing model of the system under study

Prior to recent advances, the prevailing model of spatial navigation focused on a "core navigation network" comprising the hippocampus (place cells), entorhinal cortex (grid cells), retrosplenial cortex, and posterior parietal cortex. These regions were thought to support place learning, path integration, and flexible navigation requiring self-localization. The striatum was recognized for supporting stimulus-response (habit-based) navigation. The prefrontal cortex was largely excluded from navigation theories, with any navigation impairments in frontal patients attributed to general executive dysfunction rather than specific navigational mechanisms. This neglect was reinforced by the absence of clear spatial coding in PFC neurons until recently, and reports that rodent medial PFC lesions had little impact on Morris water maze performance.

### What this paper contributes

This review establishes the PFC as a crucial component of the mammalian navigation system, synthesizing evidence across species to show that:

1. **PFC supports navigation-specific functions** beyond general executive dysfunction: goal selection and maintenance, planning, adaptation to environmental changes, and value-based decision-making are all specifically impaired by PFC damage during navigation.

2. **Different PFC subregions have distinct navigational roles**: dlPFC/vlPFC for inhibition and replanning; dACC for planning and internally-generated route changes; OFC for value integration; mPFC for goal maintenance and distance coding; SFG/rdmPFC for detecting changes and prediction errors.

3. **PFC-hippocampus interactions are critical for navigation**: Coordinated replay, theta-band synchrony, and goal-directed information flow between PFC and hippocampus support planning, memory-guided decisions, and strategy switching.

4. **Spatial coding exists in PFC**: Evidence of grid-like coding, goal-selective neurons, and path distance coding in human and rodent PFC challenges the historical view that spatial representations are confined to the hippocampal formation.

5. **Navigation engages the default-mode network**: DMN activity during travel periods suggests internal guidance and memory-based navigation when no immediate planning is required.

The review provides a framework for understanding how different PFC regions contribute to different stages of navigation, from goal selection through planning, travel, adaptation, and consolidation.

### Brain regions & systems

- **Dorsolateral prefrontal cortex (dlPFC)**: Inhibition and replanning during detours; active during active choice at junctions; involved in hierarchical planning and sequencing behavior.

- **Ventrolateral prefrontal cortex (vlPFC)**: Inhibition and replanning; activity increases with difficulty of future choice; involved in detecting environmental changes leading to replanning.

- **Dorsal anterior cingulate cortex (dACC) / Midcingulate cortex (MCC)**: Planning and spontaneous internally-generated changes of route (backtracking); hierarchical coding; predictive monitoring of environment; foraging/counterfactual processing; effort-based valuation.

- **Orbitofrontal cortex (OFC)**: Integrates environmental representations with value of actions; provides a 'cognitive map' of possible decisions; involved in updating and learning path values; represents state space for value-based decision-making.

- **Medial prefrontal cortex (mPFC)**: Goal maintenance during travel; codes path distance to goal; interacts with hippocampus during spatial decisions and replay; involved in scene construction and memory retrieval.

- **Superior frontal gyrus (SFG) / Rostrodorsal medial PFC (rdmPFC)**: Novelty detection and environmental changes leading to replanning; interacts with hippocampus during sequential planning; path integration.

- **Right lateral PFC (rlPFC)**: Novelty detection and replanning; specifically activated by detours and false shortcuts; involved in initiating stop signals for replanning.

- **Frontopolar cortex (BA10)**: Future choice processing; searching possible paths in the future.

- **Hippocampus**: Core navigation region providing spatial representations (place cells); interacts with PFC via replay and theta synchrony; provides goal distance and trajectory information.

- **Entorhinal cortex**: Grid cell representations; provides spatial metric for navigation.

- **Default-mode network (DMN)**: Active during travel periods when no immediate planning is required; includes vmPFC, hippocampus, and precuneus/posterior cingulate cortex.

### Mechanistic insight

This review does not meet the bar for mechanistic insight as defined in the skill instructions. While it synthesizes extensive evidence for PFC involvement in navigation and discusses PFC-hippocampus interactions, it does not present or formalize a specific algorithm that explains navigational decision-making, nor does it provide neural data specifically supporting one algorithmic implementation over alternatives. The review discusses multiple frameworks (hierarchical planning, reinforcement learning, predictive coding) but remains at a descriptive level regarding how PFC regions mechanistically implement navigation functions. The paper does propose that PFC-hippocampus interactions support planning via coordinated replay and theta synchronization, but this is presented as an empirical observation rather than a formalized algorithm with specific predictions tested against alternatives.

### Limitations & open questions

- **Cross-species integration challenges**: Differences in PFC neuroanatomy between species, varying navigation tasks, and different neural recording methods make direct comparisons difficult.
- **Limited research on PFC in navigation**: Despite recent advances, there is still surprisingly little research specifically examining PFC contributions to navigation compared to hippocampal studies.
- **Familiarity and strategy interactions**: Unclear how PFC engagement varies with environmental familiarity and how this relates to different navigation strategies.
- **Natural behavior dynamics**: Most studies are optimized for navigational processing time, potentially missing spontaneous behaviors and mind-wandering during navigation.
- **PFC-hippocampus interaction mechanisms**: While coordinated activity is observed, the precise mechanisms and directionality of information flow remain unclear.
- **Social navigation**: Limited understanding of how PFC processes social information during navigation (e.g., inferring popular routes from others' presence).
- **Computational models**: Need for future computational models that predict engagement of specific PFC subregions during different navigation events.

### Connections & keywords

**Key citations:**
- Maguire et al. (1998) - earliest study showing PFC activation during virtual navigation
- Ekstrom et al. (2003) - seminal human intracranial recording study showing goal-selective frontal neurons
- Spiers & Maguire (2006, 2007) - real-world navigation studies
- Tolman (1948) - cognitive map theory
- Miller & Cohen (2001) - integrative theory of PFC function
- Redish (2016) - VTE and hippocampal function

**Named models or frameworks:**
- Cognitive map theory (Tolman)
- Core navigation network (hippocampus, parahippocampus, retrosplenial cortex, posterior parietal cortex)
- Hierarchical planning framework
- Reinforcement learning (model-based and model-free)
- Predictive coding
- Default-mode network
- Vicarious trial and error (VTE)
- Hippocampal replay and preplay
- State space representation

**Brain regions:**
Prefrontal cortex (dlPFC, vlPFC, dACC, ACC, OFC, mPFC, vmPFC, SFG, rdmPFC, rlPFC, frontopolar cortex, prelimbic cortex, infralimbic cortex), hippocampus, entorhinal cortex, retrosplenial cortex, posterior parietal cortex, striatum, default-mode network

**Keywords:**
spatial navigation, prefrontal cortex, goal-directed behavior, route planning, cognitive map, hippocampal-prefrontal interactions, detours, wayfinding, replay, theta oscillations, decision-making, default-mode network, vicarious trial and error, state space representation
