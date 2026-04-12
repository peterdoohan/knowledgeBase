---
source_file: wikenheiser2016_cognitive_maps_hippocampus.md
paper_id: wikenheiser2016_cognitive_maps_hippocampus
title: "Over the river, through the woods: cognitive maps in the hippocampus and orbitofrontal cortex"
authors:
  - "Andrew M. Wikenheiser"
  - "Geoffrey Schoenbaum"
year: 2016
journal: "Nature Reviews Neuroscience"
paper_type: review
contribution_type: review
species:
  - rat
tasks:
  - t_maze
methods:
  - representational_similarity_analysis
  - computational_modeling
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - entorhinal_cortex
  - prefrontal_cortex
  - orbitofrontal_cortex
  - striatum
  - ventral_striatum
  - ventral_tegmental_area
  - retrosplenial_cortex
  - amygdala
frameworks:
  - reinforcement_learning
  - model_free_rl
keywords:
  - cognitive_map
  - hippocampus
  - orbitofrontal_cortex
  - reinforcement_learning
  - model_based_learning
  - task_state_representation
  - place_cells
  - vicarious_trial_and_error
  - prospective_coding
  - decision_making
  - goal_directed_behavior
  - neural_ensemble_coding
  - theta_oscillations
  - sensory_preconditioning
  - value_inference
  - state_space
  - navigation
  - associative_learning
  - cross_structural_interaction
  - over
key_citations:
  - tolman1948_cognitive_maps_rats
  - wilson2014_best_practices_scientific
  - johnson2007_hippocampus_decision
wiki_pages:
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/hippocampal_prefrontal_replay_in_planning
  - wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning
---

### One-line summary

The hippocampus and orbitofrontal cortex (OFC) encode parallel but interactive cognitive "maps" that capture complex relationships between cues, actions, outcomes, and environmental features to support flexible, goal-directed decision making.

### Background & motivation

Research on the hippocampus and OFC has proceeded largely independently, yet both structures are implicated in forming predictions about the future to support flexible behavior. This review synthesizes evidence that both regions encode cognitive maps—structured representations of causal relationships in the world—and examines how interactions between these structures contribute to adaptive decision making.

### Methods

This is a narrative review that synthesizes:
- Electrophysiological recordings from hippocampal and OFC ensembles in behaving rodents
- Lesion and inactivation studies in rats and primates
- Human neuroimaging studies
- Computational modeling approaches, particularly reinforcement learning models
- Anatomical tracing studies of hippocampal-OFC connectivity

Key paradigms reviewed include:
- T-maze decision-making tasks with vicarious trial and error (VTE)
- Plus-maze place/response tasks with contingency reversals
- Sensory preconditioning tasks
- Outcome devaluation paradigms

### Key findings

- **Parallel cognitive maps**: Both hippocampus and OFC encode cognitive maps, but with different emphases. The hippocampus provides a flexible system for rapidly encoding complex features of the world, organizing experience along spatial and temporal axes. The OFC emphasizes biological relevance, encoding task states colored by expected outcomes and current motivational states.

- **Hippocampal spatial and non-spatial coding**: Beyond place cells, hippocampal neurons encode non-spatial factors including objects, attention, conditioned stimuli, novelty, and motivational states. Hippocampal ensembles show prospective coding during deliberation, simulating future paths to goals.

- **OFC state representation**: OFC neurons encode task states, particularly when states are abstract or unobservable and must be inferred from experience. OFC activity tracks expected outcomes, counterfactual outcomes, and rule cues that define correct task performance.

- **Complementary representational formats**: In a plus-maze task, hippocampal neurons showed discrete place fields modulated by journey context, while OFC neurons fired evenly along entire paths, integrating prospective and retrospective information. Hippocampal representations fractionated primarily by spatial location; OFC representations fractionated primarily by reward contingency.

- **Dynamic cross-structural coupling**: Local field potentials in OFC and hippocampus showed coherent theta oscillations during stable task performance that transiently decoupled following contingency reversals or task switches, then re-established as new behaviors were learned.

- **Sensory preconditioning**: Hippocampal function is required during the initial learning phase to establish associative scaffolding between neutral stimuli, while OFC function is required during the test phase to access this information and support inferred value responding.

- **Functional dissociations**: Hippocampal and OFC lesions produce different patterns of impairment on delayed versus probabilistic outcomes and on specific satiety versus other devaluation manipulations, suggesting partially non-overlapping contributions to decision making.

### Computational framework

The paper applies a **reinforcement learning (RL) framework** with particular emphasis on the distinction between **model-free** and **model-based** learning algorithms.

**Core formalism**:
- **Model-free algorithms** learn cached values of actions without representing specific information about sensory properties or identities of outcomes.
- **Model-based systems** store richer associations and capitalize on a world model that tracks how different states are linked together and the specific identity of outcomes those states contain.

**Key assumptions**:
- The cognitive map can be defined as an associative structure that facilitates model-based learning and behavior.
- Cognitive maps require components for: (1) recognizing and categorizing world states, (2) learning relationships between states, (3) encoding rich outcome representations, and (4) prospectively using this information for planning.
- The neural instantiation of cognitive maps is distributed across structures supporting model-based behavior, including OFC and hippocampus.

**Model predictions**:
- RL models with impaired capacity to represent task states behave like animals with OFC lesions.
- The OFC represents task states, particularly abstract or unobservable states that must be inferred.
- Hippocampal ensembles encode environmental state spaces, with place cells representing individual states and their connectivity.

### Prevailing model of the system under study

Before this review's synthesis, the hippocampus and OFC were largely studied independently with distinct theoretical frameworks:

- **Hippocampus**: Dominated by the cognitive map theory (O'Keefe & Nadel, 1978), which focused on spatial mapping via place cells. However, this spatial view was being expanded to incorporate Tolman's original concept of cognitive maps as abstract representations of causal relationships, not merely spatial layouts.

- **OFC**: Historically associated with reward- and value-based behavior, including encoding economic value, suppressing inappropriate responses, and representing incentive value. Early theories centered on response inhibition, but contemporary thinking had shifted toward associative learning and decision-making frameworks.

The emerging consensus, which this review builds upon, was that both structures contribute to flexible, goal-directed behavior but through potentially different mechanisms. The prevailing view recognized that both regions form predictions about future events, but the specific nature of these predictions and how they interact remained underspecified.

### What this paper contributes

This review contributes an integrative theoretical framework that:

1. **Proposes parallel cognitive maps**: Both hippocampus and OFC encode cognitive maps, but with different representational formats and emphases. The hippocampus emphasizes spatial-temporal organization, while the OFC emphasizes biological relevance and outcome value.

2. **Formalizes the cognitive map in RL terms**: Updates Tolman's cognitive map concept using modern computational models, defining it as an associative structure that facilitates model-based reinforcement learning. This provides a precise, testable framework for understanding cognitive map function.

3. **Synthesizes cross-structural interactions**: Proposes specific mechanisms by which hippocampal and OFC cognitive maps interact, including: (a) hippocampal trajectory simulation evaluated by OFC outcome predictions, (b) dynamic theta coherence reflecting communication between structures, and (c) complementary roles in sensory preconditioning (hippocampus for encoding associations, OFC for accessing them).

4. **Identifies representational differences**: Demonstrates that hippocampal representations fractionate primarily by spatial location while OFC representations fractionate primarily by reward contingency, suggesting distinct but complementary representational hierarchies.

5. **Proposes distributed cognitive map architecture**: Suggests that cognitive maps are not localized to a single structure but are distributed across multiple brain regions, with different modules representing different informational layers of a global cognitive map.

### Brain regions & systems

- **Hippocampus (dorsal)**: Encodes spatial and non-spatial cognitive maps; place cells represent positions in environmental state space; ensembles simulate future trajectories during deliberation (vicarious trial and error); involved in sensory preconditioning (encoding phase); shows prospective coding; critical for organizing experience along spatial and temporal axes; enables flexible and inferential cognitive processes.

- **Orbitofrontal cortex (OFC, lateral)**: Encodes cognitive maps of task state; represents current task states, particularly abstract or unobservable states that must be inferred; tracks expected outcomes and their specific sensory features; encodes counterfactual outcomes; involved in outcome devaluation; necessary for sensory preconditioning (test phase); represents reward contingency as primary dimension; integrates information about responses and reward expectation; encodes biological significance and value.

- **Orbitofrontal complex**: Broader region including OFC with related functions in cognitive mapping and decision making.

- **Prefrontal cortex (other parts)**: Associated with working memory, representation of task rules, and top-down control of behavior; related to cognitive map function but potentially dissociable.

- **Ventral striatum**: Receives convergent input from hippocampus and OFC; encodes reward proximity; potential site for integration of hippocampal and OFC information; theta phase precession links place and reward information.

- **Ventral tegmental area (VTA)**: Receives indirect input from both hippocampus and OFC; dopamine neurons signal reward prediction errors; OFC lesions alter prediction error encoding in VTA; hippocampal outflow to VTA important for context-induced reinstatement.

- **Thalamic nucleus reuniens**: Receives projections from and sends projections to both OFC and hippocampus; important for coordinating bidirectional interactions between frontal cortex and hippocampal nuclei; potential role in spatial working memory.

- **Entorhinal cortex**: Part of hippocampal network; parahippocampal structure receiving OFC projections; pathway linking OFC and hippocampal processing streams.

- **Perirhinal cortex**: Parahippocampal structure; lesions abolish sensory preconditioning; involved in forming associations between multiple sensory stimuli.

- **Retrosplenial cortex**: Lesions abolish sensory preconditioning; chemogenetic silencing during preconditioning phase prevents value inference at test; involved in establishing associative scaffolding.

- **Subiculum**: Receives strong projection from CA1; projects to frontal cortex including OFC; part of extended hippocampal system.

- **Amygdala**: Mentioned in context of outcome devaluation and social behavior; interacts with OFC.

- **Dorsal striatum**: Mentioned in context of model-free vs model-free learning; part of multiple memory systems framework.

- **Postrhinal cortex**: Parahippocampal structure; part of pathway linking OFC and hippocampal processing streams.

### Mechanistic insight

This paper is a review and does not provide new primary mechanistic data. However, it synthesizes a mechanistic framework from existing literature:

The review proposes that both the hippocampus and OFC instantiate cognitive maps that enable model-based reinforcement learning. The hippocampus provides a flexible, promiscuous processor of abstract associations, particularly adept at linking information into temporally patterned sequences and organizing experience along spatial and temporal axes. This allows the hippocampus to encode, retrieve, and explore mental models of state spaces, including simulating future trajectories during deliberation (vicarious trial and error).

The OFC, by contrast, represents similar information but with a focus on biological relevance. It encodes task states colored by expected outcomes and current motivational states, with reward contingency as a primary organizing dimension. The OFC is particularly important for tracking unobservable states that must be inferred from experience.

Cross-structural interactions may involve: (1) hippocampal trajectory simulation evaluated by OFC outcome prediction, (2) dynamic theta coherence mediating communication, and (3) complementary roles in inference tasks (hippocampus encoding associations, OFC accessing them for decision-making).

However, the review does not provide direct neural evidence linking specific algorithmic variables to measured neural activity in a way that would fully satisfy the mechanistic insight criteria. The evidence is largely correlational (neural activity patterns during behavior) rather than causal (perturbation of specific algorithmic components).

### Limitations & open questions

- **Anatomical diversity**: The discussion focuses on rodent dorsal hippocampus and lateral OFC, but both regions show anatomical diversity that may have functional implications. Cross-species differences in OFC organization are also important considerations.

- **Under-constrained tasks**: Even well-controlled behavioral tasks can be solved in different ways by individual subjects, making it challenging to match neural activity to specific state space representations. Better paradigms are needed that provide behavioral readouts of the state spaces subjects are using.

- **Causal evidence gaps**: Much of the evidence for cross-structural interactions is correlational (e.g., LFP coherence). More work is needed using projection-specific and cell-type-specific manipulations to establish causal roles in cognitive map-dependent behavior.

- **Other frontal regions**: Parts of frontal cortex beyond OFC (working memory, task rules, top-down control) also contribute to cognitive mapping. More work is needed to determine how each region fits within the framework.

- **Mechanism of interaction**: The precise form of cross-structural dialogue remains unclear. Does OFC input modulate hippocampal spatial representations? Does hippocampal input provide spatial/relational context to OFC outcome predictions? How is information integrated?

- **Multiple map layers**: How are multiple informational layers of the global cognitive map coordinated across structures? What determines which layers are active or accessible at different times?

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) — The Hippocampus as a Cognitive Map (foundational cognitive map theory)
- Tolman (1948) — Cognitive maps in rats and men (original cognitive map concept)
- Wilson et al. (2014) — Orbitofrontal cortex as a cognitive map of task space (OFC state space theory)
- Johnson & Redish (2007) — Neural ensembles in CA3 transiently encode paths forward (hippocampal prospective coding)
- Steiner & Redish (2012, 2014) — OFC reward activity during deliberation and regret
- Jones et al. (2012) — OFC supports behavior using inferred but not cached values
- Pfeiffer & Foster (2013) — Hippocampal place-cell sequences depict future paths
- Sutton & Barto (1998) — Reinforcement Learning: An Introduction (RL framework)
- Daw, Niv & Dayan (2005) — Uncertainty-based competition between prefrontal and striatal systems

**Named models or frameworks:**
- Cognitive map theory (Tolman; O'Keefe & Nadel)
- Reinforcement learning (RL) models
- Model-based vs. model-free reinforcement learning
- Task state representation framework (Wilson et al. 2014)
- Vicarious trial and error (VTE) behavior
- Representational similarity analysis (RSA)
- Sensory preconditioning paradigm

**Brain regions:**
- Hippocampus (dorsal, ventral, CA1, CA3, subiculum)
- Orbitofrontal cortex (OFC, lateral OFC, medial OFC)
- Ventral striatum
- Ventral tegmental area (VTA)
- Thalamic nucleus reuniens
- Entorhinal cortex
- Perirhinal cortex
- Postrhinal cortex
- Retrosplenial cortex
- Prefrontal cortex

**Keywords:**
cognitive map, hippocampus, orbitofrontal cortex, reinforcement learning, model-based learning, task state representation, place cells, vicarious trial and error, prospective coding, decision making, goal-directed behavior, neural ensemble coding, theta oscillations, sensory preconditioning, value inference, state space, navigation, associative learning, cross-structural interaction

### Related wiki pages
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]
- [[wiki/topics/hippocampal_prefrontal_replay_in_planning|Hippocampal–prefrontal replay in planning]]
- [[wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning|Task-state representation and hidden-state inference in orbitofrontal–hippocampal reinforcement learning]]
