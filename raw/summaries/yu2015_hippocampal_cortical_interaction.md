---
source_file: yu2015_hippocampal_cortical_interaction.md
paper_id: yu2015_hippocampal_cortical_interaction
title: "Hippocampal–cortical interaction in decision making"
authors:
  - "Jai Y. Yu"
  - "Loren M. Frank"
year: 2015
journal: "Neurobiology of Learning and Memory"
paper_type: review
contribution_type: review
species:
  - rat
tasks:
  - open_field
  - foraging_task
methods:
  - electrophysiology
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - prefrontal_cortex
  - prelimbic_cortex
  - striatum
  - ventral_striatum
  - thalamus
frameworks:
  - reinforcement_learning
keywords:
  - sharp_wave_ripples
  - theta_oscillations
  - vicarious_trial_and_error
  - memory_replay
  - prefrontal_cortex
  - hippocampus
  - deliberation
  - decision_making
  - spatial_navigation
  - working_memory
  - place_cells
  - trajectory_encoding
  - w_track_alternation_task
  - awake_replay
  - swr_disruption
  - hippocampal_cortical_coherence
  - hippocampalcortical
  - interaction
  - decision
  - making
key_citations:
  - singer2013_hippocampal_swr_decisions
  - gupta2010_replay_not_simple_function
  - johnson2007_hippocampus_decision
wiki_pages:
  - wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation
  - wiki/topics/sharp_wave_ripple_associated_hippocampal_replay
  - wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning
---

### One-line summary

Hippocampal sharp-wave ripples (SWRs) reactivate memory sequences that serve as choice options during deliberative decision making, with the prefrontal cortex evaluating these options against task rules and previous experience.

### Background & motivation

When making decisions, animals must often consider available alternatives to choose the most appropriate option—a process called deliberation that relies on memories of past actions and outcomes. While the hippocampus and prefrontal cortex (PFC) are required for memory encoding, retrieval, and decision making, the specific neural mechanisms supporting deliberation remain unclear. This review examines how hippocampal-cortical interactions in the rat could provide a neural substrate for deliberative decision making.

### Methods

- Review of empirical literature on hippocampal-prefrontal interactions during decision making
- Focus on rodent (primarily rat) electrophysiology studies using spatial navigation tasks
- Analysis of two major network states: theta oscillations (active exploration) and sharp-wave ripples (SWRs, quiescence/immobility)
- Discussion of behavioral correlates including vicarious trial and error (VTE) behavior
- Integration of findings from W-track alternation task, open field foraging, and other spatial memory paradigms
- Synthesis of anatomical connectivity data between hippocampus and PFC

### Key findings

- Sharp-wave ripples (SWRs) satisfy key criteria for a neural signature of deliberation: they are more frequent during learning, occur at choice points and decision-relevant locations, encode trajectories relevant to the current decision, and are required for memory-guided decisions
- SWR interruption during learning impairs performance on outbound decisions (which require memory of the previous trial) but not inbound decisions (which follow a simple place-response rule), demonstrating that SWRs specifically support deliberation requiring memory retrieval
- Replayed trajectories during SWRs include both chosen and unchosen paths, suggesting they provide potential choice options rather than simply predicting the animal's future path
- Replay can include trajectories from remote or even novel environments, suggesting hippocampal replay supports imagination and flexible exploration of possibilities beyond immediate experience
- Theta oscillations during exploration show increased hippocampal-PFC coherence at choice points, particularly after learning, and may support execution of well-learned rules rather than deliberation per se
- Non-local place cell activity during theta at choice points (during vicarious trial and error) may represent another mechanism for exploring future trajectories, but its influence on PFC remains unclear
- The PFC receives hippocampal input during SWRs and could maintain working memory representations of previous choices and task rules to evaluate replayed options

### Computational framework

The paper proposes a sequential evaluation model of deliberation grounded in reinforcement learning and working memory frameworks. In this model, hippocampal replay during SWRs provides potential trajectories (choice options) that are serially transmitted to the PFC. The PFC maintains two critical working memory buffers: (1) a representation of the previous trajectory/choice, and (2) the task rule (e.g., "choose the arm not visited in the previous trial"). Each replayed option is compared against these maintained representations to evaluate whether it satisfies the task rule. This framework draws on: (1) Reinforcement learning models of sequential decision making where options are evaluated based on expected outcomes; (2) Working memory models of PFC function where persistent activity maintains task-relevant information; and (3) The constructive episodic simulation hypothesis where hippocampal mechanisms support imagination and exploration of possibilities. The paper also discusses an alternative parallel evaluation model where multiple options are simultaneously maintained and compared, but notes that the available evidence (individual trajectories per SWR rather than mixtures) favors the serial model.

### Prevailing model of the system under study

Prior to the work reviewed here, the field understood the hippocampus as critical for encoding and storing episodic memories, with sharp-wave ripples (SWRs) serving primarily as a mechanism for memory consolidation during sleep and quiet rest. The prefrontal cortex was understood to support working memory and executive functions necessary for decision making, but the specific mechanisms by which these two regions interact during active deliberation were not well characterized. The relationship between hippocampal replay and decision making was underexplored, with replay primarily viewed as a consolidation phenomenon rather than a mechanism for actively exploring choice options during behavior.

### What this paper contributes

This review synthesizes evidence that hippocampal SWR replay serves as a mechanism for deliberation—not just consolidation. It establishes that: (1) SWRs meet the criteria expected of a deliberative process (more frequent during learning, at choice points, encoding relevant trajectories, required for memory-guided decisions); (2) SWR interruption specifically impairs deliberation requiring memory retrieval (outbound decisions) but not simple place-response decisions (inbound decisions); (3) replayed trajectories include both chosen and unchosen options, suggesting they provide choice alternatives rather than predicting behavior; (4) replay can access remote or even novel trajectories, supporting flexible exploration beyond immediate experience; and (5) the PFC likely evaluates these replayed options against task rules and previous experience maintained in working memory. The paper proposes a specific mechanistic model where hippocampal replay serially provides choice options to the PFC for evaluation.

### Brain regions & systems

- **Hippocampus (CA1, CA3)** — source of replayed memory sequences during SWRs; encodes spatial trajectories through place cell sequences; transmits trajectory information to PFC via direct projections from CA1/subiculum to prelimbic cortex and indirect connections via anterior thalamic nuclei
- **Prefrontal cortex (PFC)** — evaluates replayed trajectories against task rules and previous experience; maintains working memory representations of previous choices; includes prelimbic, infralimbic, and anterior cingulate regions; receives hippocampal input during SWRs and shows time-locked LFP changes
- **Ventral striatum** — involved in action-outcome evaluation; receives SWR-triggered reactivation of reward-associated firing; reciprocally connected with PFC
- **Entorhinal cortex** — receives direct projections from PFC (potential feedback pathway to hippocampus)
- **Nucleus reuniens (thalamus)** — indirect pathway from PFC to hippocampus; situated in midline thalamus

### Mechanistic insight

This review does not meet the high bar for mechanistic insight as defined in the guidelines. While the paper proposes a specific algorithmic model (serial evaluation of replayed trajectories by the PFC), it does not provide direct neural data showing that the PFC specifically implements this evaluation algorithm over hippocampal inputs. The evidence presented is correlational (SWRs occur during deliberation, SWR disruption impairs performance) or anatomical (connectivity between regions). The review discusses mechanisms that *could* support deliberation (working memory maintenance in PFC, replay in hippocampus, theta coherence for information transfer), but these are proposed mechanisms rather than empirically validated ones. The paper proposes that replayed trajectories are evaluated serially against task rules maintained in PFC working memory, but does not provide direct evidence of this evaluation process occurring in the PFC during awake SWRs. The model is a theoretical synthesis rather than a mechanistically validated account.

### Limitations & open questions

- The specific mechanism by which sequential activation of hippocampal cells engages PFC cells remains unclear; whether trajectories are represented as distributed non-sequential PFC patterns or sequential ones is unknown
- Whether options are evaluated in series (one per SWR) or in parallel (multiple options maintained simultaneously) is unresolved; both models have theoretical merits but direct evidence is lacking
- The role of PFC feedback to hippocampus during deliberation is poorly understood; while anatomical pathways exist (via entorhinal cortex and nucleus reuniens), their functional role in deliberation is unknown
- Whether SWRs contribute to deliberation during active locomotion (when SWRs are less frequent) remains unclear; alternative mechanisms may exist for deliberation during movement
- The specific neural signatures of PFC evaluation during awake SWRs have not been directly characterized; most evidence comes from sleep studies
- How the PFC compares replayed trajectories against task rules and previous experience at the neural level is not well understood
- The role of ventral striatum and other subcortical structures in evaluating replayed options needs further characterization
- Whether replayed trajectories from remote or novel environments are actually used for decision making (as opposed to simply being present) requires further investigation

### Connections & keywords

- **Key citations**: Johnson & Redish (2007) — vicarious trial and error; Jadhav et al. (2012) — SWR disruption impairs memory; Singer et al. (2013) — SWR activity predicts correct decisions; Pfeiffer & Foster (2013) — place-cell sequences depict future paths; Carr et al. (2011) — hippocampal replay in awake state; Jones & Wilson (2005b) — theta rhythms coordinate hippocampal-prefrontal interactions; Benchenane et al. (2010) — coherent theta oscillations and reorganization of spike timing; Gupta et al. (2010) — hippocampal replay is not a simple function of experience; Siapas & Wilson (1998) — coordinated interactions between hippocampal ripples and cortical spindles
- **Named models or frameworks**: Cognitive map (Tolman); Constructive episodic simulation hypothesis (Schacter & Addis); Working memory model (Goldman-Rakic); Reinforcement learning framework; Serial evaluation model of deliberation
- **Brain regions**: Hippocampus (CA1, CA3), prefrontal cortex (prelimbic, infralimbic, anterior cingulate), ventral striatum, entorhinal cortex, nucleus reuniens (thalamus), anterior thalamic nuclei
- **Keywords**: sharp-wave ripples, theta oscillations, vicarious trial and error, memory replay, prefrontal cortex, hippocampus, deliberation, decision making, spatial navigation, working memory, place cells, trajectory encoding, W-track alternation task, awake replay, SWR disruption, hippocampal-cortical coherence

### Related wiki pages
- [[wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning|Hippocampal sharp-wave ripple replay and prefrontal coordination during planning]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]
- [[wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation|Hippocampal–prefrontal mechanisms of route planning and detour navigation]]
- [[wiki/topics/sharp_wave_ripple_associated_hippocampal_replay|Sharp-wave ripple-associated hippocampal replay]]
- [[wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning|Task-state representation and hidden-state inference in orbitofrontal–hippocampal reinforcement learning]]
