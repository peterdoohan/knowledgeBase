---
source_file: "patai2021_versatile_wayfinder_prefrontal.md"
paper_id: "patai2021_versatile_wayfinder_prefrontal"
title: "The Versatile Wayfinder: Prefrontal Contributions to Spatial Navigation"
authors: "Eva Zita Patai, Hugo J. Spiers"
year: 2021
journal: "Trends in Cognitive Sciences"
paper_type: "review"
contribution_type: "review"
species: ["human"]
tasks: ["virtual_navigation", "detour_task", "navigation_task"]
methods: ["electrophysiology", "fmri", "lesion"]
brain_regions: ["hippocampus", "hippocampus_ca1", "entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "anterior_cingulate_cortex", "orbitofrontal_cortex", "ventromedial_prefrontal_cortex", "dorsolateral_prefrontal_cortex", "striatum", "retrosplenial_cortex"]
frameworks: ["reinforcement_learning", "model_free_rl", "attractor_networks"]
keywords: ["tolman_1948_cognitive_map_theory", "miller_and_cohen_2001_integrative_theory_of_pfc_function", "maguire_et_al_1998_human_navigation_network_discovery", "ekstrom_et_al_2003_first_human_intracranial_recordings_of_navigation", "hartley_et_al_2003_route_following_vs_wayfinding_neural_bases", "spiers_and_maguire_2006_real_world_navigation_dynamics", "spiers_and_gilbert_2015_detour_problem_model_of_pfc_hippocampal_interactions", "foster_2017_review_of_hippocampal_replay", "redish_2016_vicarious_trial_and_error_review", "wikenheiser_and_schoenbaum_2016_cognitive_maps_in_hippocampus_and_ofc", "badre_and_nee_2018_hierarchical_control_of_behavior_by_frontal_cortex", "named_models_or_frameworks", "cognitive_map_theory_tolman", "hierarchical_planning_framework", "pfc_hippocampal_interaction_model_for_navigation", "state_space_representation_framework_ofc", "default_mode_network_dmn_in_navigation", "model_based_vs_model_free_reinforcement_learning", "vicarious_trial_and_error_vte_behavior", "attractor_network_models_mentioned"]
---

### One-line summary

The prefrontal cortex (PFC) is a critical but historically overlooked component of the navigation system, supporting goal selection, planning, route adaptation, and value-based decision-making during spatial navigation across species.

---

### Background & motivation

Spatial navigation has traditionally been understood through the lens of the hippocampal formation and core navigation network (hippocampus, parahippocampus, retrosplenial cortex, posterior parietal cortex, and striatum). However, real-world navigation requires executive functions—planning, decision-making, goal maintenance, and adaptive behavior—traditionally associated with prefrontal cortex (PFC). Despite early neuroimaging studies showing PFC activation during navigation, the region has been largely neglected in navigation theories due to: (1) navigation impairments in frontal patients being attributed to general executive dysfunction rather than specific spatial deficits; (2) the relatively recent discovery of spatial coding in PFC neurons compared to hippocampal place/grid cells; and (3) rodent lesion studies showing minimal effects of medial PFC lesions on Morris water maze performance. This review synthesizes recent evidence across humans, non-human primates, and rodents to establish PFC as a key node in the navigation network.

---

### Methods

This is a narrative review paper that synthesizes findings from:
- Human functional neuroimaging studies (fMRI, MEG) examining PFC activity during virtual navigation tasks, route planning, detours, and shortcuts
- Human intracranial recording studies in presurgical epilepsy patients
- Non-human primate single-unit recording studies during maze navigation tasks
- Rodent lesion, electrophysiology, and immediate early gene studies examining medial PFC contributions to spatial navigation
- Neuropsychological case studies of patients with focal PFC damage navigating real-world environments

The review integrates findings across species while acknowledging anatomical differences in PFC organization between rodents and primates, and proposes a functional framework for how different PFC subregions contribute to navigation.

---

### Key findings

**Prefrontal subregions and their navigation-related functions:**

- **Dorsolateral PFC (dlPFC) and ventrolateral PFC (vlPFC)**: Active during detours and environmental changes requiring inhibition and replanning. Activity increases when choosing between paths with similar distances to goals, and when processing false shortcuts. dlPFC shows increased activity during active route choice compared to guided navigation.

- **Dorsal anterior cingulate cortex (dACC)**: Implicated in planning, hierarchical coding of navigation decisions, and spontaneous internally-generated route changes (backtracking). Active when choices are difficult and when tracking path distance to goals during travel. Shows activity during foraging and counterfactual processing.

- **Orbitofrontal cortex (OFC)**: Integrates environmental representations with action values, providing a 'cognitive map' of possible decisions. Supports inference about hidden states and value-based decision-making at choice points. In rodents, OFC inactivation abolishes inference-based foraging while preserving stimulus-bound behavior.

- **Ventromedial PFC (vmPFC)**: Critical for maintaining current goals during navigation. Patients with vmPFC damage can navigate familiar routes but frequently forget their destination goal; performance improves with external reminders. Involved in scene construction and integrating new spatial information with existing schemas. Active during travel periods in familiar environments.

- **Medial PFC (mPFC)**: Codes path distance to goals during initial planning and travel. Shows goal-selective activity and increased theta coherence with hippocampus during spatial memory retrieval. In rodents, mPFC activity precedes CA1 activity during rule learning and strategy switching.

- **Frontopolar cortex (BA10)**: Responds to future choice difficulty and may support searching possible future paths.

- **Superior frontal gyrus (SFG)/rostrodorsal medial PFC (rdmPFC)**: Active during novelty detection and environmental changes requiring replanning. Shows increased coupling with hippocampus during sequential planning and when correct choices are made.

**Cross-species findings:**

- In rodents, medial frontal areas (prelimbic, infralimbic) interact with hippocampus during spatial decisions and strategy switching between place-based and response-based navigation.
- Coordinated replay between hippocampus and PFC is higher for subsequently taken paths and predicts spatial memory performance.
- Theta-band coherence between PFC and hippocampus increases during planning and spatial memory retrieval.

**Default-mode network (DMN) involvement:**

- Core DMN regions including vmPFC are active during travel periods when no immediate navigational decisions are required.
- DMN activity is suppressed during backtracking and route changes, suggesting a shift from internal to external attention.

---

### Computational framework

The paper proposes a functional framework organizing PFC contributions around hierarchical control and reinforcement learning principles. The framework conceptualizes navigation as requiring:

1. **Hierarchical planning**: Different PFC regions encode information at different hierarchical levels—dACC and dmPFC process higher-level route decisions and path integration, while lPFC regions handle sequential action planning and subgoal management. Frontopolar cortex (BA10) may represent future choice demands at the highest level of the hierarchy.

2. **Model-based decision-making**: The OFC is proposed to maintain a cognitive map of the state space for value-based decisions, enabling inference about hidden states and counterfactual processing. This aligns with reinforcement learning models that distinguish between model-based (OFC-supported) and model-free (striatal) control.

3. **Prediction error signaling**: SFG and rlPFC are proposed to encode prediction errors when environmental changes require replanning, with activity scaling to the magnitude of the required behavioral adjustment.

4. **Goal maintenance and value comparison**: vmPFC and ACC are proposed to track goal proximity and compare the value of default versus non-default navigation options, consistent with foraging theory and sequential decision models.

The framework also incorporates dynamical systems concepts—prefrontal-hippocampal theta coherence and coordinated replay events are proposed as mechanisms for transferring information between planning (PFC) and spatial memory (hippocampal) systems during navigation.

---

### Prevailing model of the system under study

Before this review, the prevailing model of spatial navigation focused on a "core navigation network" consisting of the hippocampus, parahippocampus, retrosplenial cortex, and posterior parietal cortex, with the striatum supporting stimulus-response navigation. This model emphasized:

1. **Hippocampal-centric spatial coding**: The hippocampus and entorhinal cortex (with grid cells, place cells, and head direction cells) were viewed as the primary neural substrate for cognitive maps and flexible navigation.

2. **PFC as executive but not specifically spatial**: While PFC was acknowledged to support general executive functions that might aid navigation, it was not considered a specialized component of the navigation system. Frontal lobe damage was assumed to cause navigation deficits only indirectly through general executive dysfunction.

3. **Rodent medial PFC as non-essential for basic navigation**: Lesions of rodent medial PFC were reported to have minimal effects on standard navigation tasks like the Morris water maze, reinforcing the view that PFC was not critical for spatial navigation per se.

4. **Default-mode network as task-negative**: The DMN was understood as a system active during rest and internally-directed thought, but its specific role during navigation (particularly during travel periods) was not well articulated.

---

### What this paper contributes

This review substantially reframes the prevailing model by establishing the PFC as a critical, specialized component of the mammalian navigation system, not merely a general executive support system. The key contributions include:

1. **Functional mapping of PFC subregions to navigation processes**: The review provides a detailed functional taxonomy linking specific PFC regions to distinct navigation computations—dlPFC/vlPFC for inhibition and replanning, dACC for hierarchical planning and backtracking, OFC for state-space representation and value-based decisions, vmPFC for goal maintenance, and mPFC for goal-distance coding.

2. **Cross-species integration**: By synthesizing evidence from humans (fMRI, MEG, intracranial recordings, neuropsychology), non-human primates (single-unit recordings), and rodents (lesions, electrophysiology, IEGs), the review establishes conserved PFC contributions to navigation across mammals despite anatomical differences.

3. **Evidence for spatial coding in PFC**: The review highlights recent findings of spatially-selective PFC neurons (goal cells, grid-like coding) that challenge the view that PFC lacks spatial representations, demonstrating that PFC neurons encode navigation-relevant information with spatial specificity.

4. **Dynamic framework for PFC-hippocampus interactions**: The review articulates how PFC and hippocampus interact during navigation—PFC drives hippocampal activity during goal retrieval, theta coherence supports planning, and coordinated replay consolidates successful routes—positioning PFC-hippocampal interactions as central to flexible navigation.

5. **Role of default-mode network during navigation**: The review establishes that DMN activity (including vmPFC) during navigation is not merely task-negative but reflects a functional state during travel periods when route plans are retrieved from memory, with suppression during route changes indicating a shift to externally-directed attention.

6. **Integration of navigation with social cognition and foraging**: The review extends the navigation framework to include PFC contributions to social navigation (tracking others, inferring routes) and foraging-like decision-making, broadening the scope beyond purely spatial processing.

---

### Brain regions & systems

**Prefrontal cortex (PFC) subregions:**

- **Dorsolateral PFC (dlPFC)**: Supports route planning, sequential action planning, and inhibitory control during detours. Active during active route choice, detour detection, and when selecting between paths with similar goal distances. Interacts with posterior parietal cortex for planning routes and handling subgoals.

- **Ventrolateral PFC (vlPFC)**: Involved in inhibition and replanning. Active during detours and environmental changes requiring plan updates. Right vlPFC specifically engaged during novelty detection and detecting false shortcuts.

- **Dorsal anterior cingulate cortex (dACC) / Midcingulate cortex (MCC)**: Critical for hierarchical planning, tracking choice difficulty, and internally-generated route changes. Active during backtracking, foraging decisions, and predictive monitoring of the environment. Shows activity when processing new information linked to uncertainty and belief updating. Involved in effort-based cost-benefit valuation.

- **Rostrodorsal medial PFC (rdmPFC) / Superior frontal gyrus (SFG)**: Engaged during sequential planning and novelty detection. Shows increased coupling with hippocampus during planning and when correct choices are made. Active during environmental changes leading to replanning (e.g., long detours).

- **Ventromedial PFC (vmPFC)**: Essential for maintaining current goals during navigation. Patients with vmPFC damage can store spatial memories but fail to maintain goal representations during travel. Involved in scene construction, integrating new information with existing spatial schemas, and optimizing search paths. Active during travel periods in familiar environments (part of DMN).

- **Medial PFC (mPFC)**: Codes path distance to goals during planning and travel. Shows goal-selective activity and theta coherence with hippocampus during spatial memory retrieval. In rodents, interacts with hippocampus during spatial decisions and strategy switching.

- **Orbitofrontal cortex (OFC)**: Represents a cognitive map of the state space for value-based decision-making. Supports inference about hidden states and counterfactual processing. Updates representations of path usefulness based on outcomes. In rodents, necessary for inference-based foraging but not stimulus-bound behavior.

- **Frontopolar cortex (BA10)**: Responds to future choice difficulty and may support searching possible future paths during navigation planning.

**Other brain regions mentioned:**

- **Hippocampus**: Core navigation network component supporting place learning, spatial memory, and replay events. Interacts with PFC during planning and consolidation.
- **Entorhinal cortex**: Contains grid cells supporting spatial metric coding.
- **Retrosplenial cortex**: Core navigation network component supporting spatial orientation.
- **Posterior parietal cortex**: Core navigation network component supporting spatial processing; interacts with lPFC during route planning.
- **Striatum**: Supports stimulus-response navigation strategies.
- **Default-mode network (DMN)**: Includes vmPFC, hippocampus, and precuneus/posterior cingulate; active during internally-directed thought and travel periods in familiar environments.
- **Nucleus reuniens (NR)**: Thalamic nucleus conveying goal trajectory information from mPFC to hippocampal CA1.

---

### Mechanistic insight

This review does not meet the high bar for mechanistic insight as defined in the criteria. While the paper synthesizes substantial evidence for PFC involvement in navigation and proposes functional frameworks, it does not present a formal algorithmic model nor provide specific neural data that directly tests such a model's variables against alternatives. The review proposes that:

1. PFC-hippocampus interactions support navigation through coordinated theta oscillations and replay events, but these mechanisms are described at a correlational rather than causal or computational level.
2. Different PFC subregions implement hierarchical control processes during navigation, but no explicit algorithm or formal model is specified.
3. The OFC maintains a cognitive map of state space for decision-making, but this is conceptual rather than a formal computational implementation.

The review calls for future computational models that predict PFC engagement during navigation, acknowledging that such models do not yet exist. The mechanistic insights are primarily descriptive and functional rather than formal or algorithmic.

---

### Limitations & open questions

**Acknowledged limitations of the reviewed literature:**

- Cross-species integration is challenging due to differences in PFC neuroanatomy, navigation tasks used, and recording methods between rodents, primates, and humans.
- Most studies are optimized for navigational processing time, leaving gaps in understanding PFC dynamics during spontaneous, naturalistic behaviors.
- Limited research has directly compared navigation in familiar versus novel environments within the same study.
- The precise mechanisms of how PFC-hippocampal interactions support navigation remain underspecified.

**Open questions identified by the authors:**

- How do different PFC regions interact with each other and posterior regions to support navigation? Need for models predicting when different PFC-linked networks are engaged.
- To what extent does PFC role during navigation depend on environmental context (familiar vs. novel) and/or navigation strategy adopted?
- How can results be better integrated across species given anatomical and methodological differences? Need for cross-species studies using identical virtual reality paradigms.
- How can knowledge of PFC function during natural navigation inform understanding of healthy aging and cognitive decline?
- What are the specific neural mechanisms the PFC uses to plan and select navigational goals?
- How does the PFC track information for successful navigation?

---

### Connections & keywords

**Key citations:**
- Tolman (1948) - Cognitive map theory
- Miller & Cohen (2001) - Integrative theory of PFC function
- Maguire et al. (1998) - Human navigation network discovery
- Ekstrom et al. (2003) - First human intracranial recordings of navigation
- Hartley et al. (2003) - Route following vs. wayfinding neural bases
- Spiers & Maguire (2006) - Real-world navigation dynamics
- Spiers & Gilbert (2015) - Detour problem model of PFC-hippocampal interactions
- Foster (2017) - Review of hippocampal replay
- Redish (2016) - Vicarious trial and error review
- Wikenheiser & Schoenbaum (2016) - Cognitive maps in hippocampus and OFC
- Badre & Nee (2018) - Hierarchical control of behavior by frontal cortex

**Named models or frameworks:**
- Cognitive map theory (Tolman)
- Hierarchical planning framework
- PFC-hippocampal interaction model for navigation
- State-space representation framework (OFC)
- Default-mode network (DMN) in navigation
- Model-based vs. model-free reinforcement learning
- Vicarious trial and error (VTE) behavior
- Attractor network models (mentioned)

**Brain regions:**
- Dorsolateral prefrontal cortex (dlPFC)
- Ventrolateral prefrontal cortex (vlPFC)
- Dorsal anterior cingulate cortex (dACC)
- Midcingulate cortex (MCC)
- Rostrodorsal medial prefrontal cortex (rdmPFC)
- Superior frontal gyrus (SFG)
- Ventromedial prefrontal cortex (vmPFC)
- Medial prefrontal cortex (mPFC)
- Orbitofrontal cortex (OFC)
- Frontopolar cortex (BA10)
- Lateral prefrontal cortex (lPFC)
- Prelimbic cortex (PrL)
- Infralimbic cortex (IL)
- Hippocampus
- Entorhinal cortex
- Retrosplenial cortex
- Posterior parietal cortex
- Striatum
- Nucleus reuniens (NR)
- Default-mode network (DMN)

**Keywords:**
- Spatial navigation
- Prefrontal cortex (PFC)
- Wayfinding
- Cognitive map
- Route planning
- Detours
- Hippocampal-prefrontal interactions
- Vicarious trial and error (VTE)
- Replay
- Theta oscillations
- Goal coding
- Cross-species integration
- Default-mode network
- State-space representation
- Reinforcement learning
