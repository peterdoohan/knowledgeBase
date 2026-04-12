---
title: "Hippocampal–prefrontal replay in planning"
subtopic_id: hippocampal_prefrontal_coordination_and_planning__01
parent_topic_id: hippocampal_prefrontal_coordination_and_planning
page_type: topic
page_worthiness: 3
status: draft_llm
generated_at: "2026-04-12T19:50:45.307523+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - wikenheiser2016_cognitive_maps_hippocampus
  - piray2021_linear_reinforcement_planning
  - patai2021_versatile_wayfinder_prefrontal
  - piray2025_compositional_cognitive_map
  - momennejad2018_offline_replay_planning
core_papers:
  - balaguer2016_hierarchical_planning_subway
  - barron2020_neuronal_computation_inferential
  - comrie2024_hippocampal_representations
  - corbit2018_goal_directed_habitual
  - eichenbaum2017_prefrontal_hippocampal_episodic
  - holton2023_planning_vmPFC_lesions
  - huang2023_hierarchical_replay_working_memory
  - kurth2023_replay_compositional_computation
---

# Hippocampal–prefrontal replay in planning

The clearest synthesis is that planning-relevant replay is probably not a purely hippocampal phenomenon. Across navigation, revaluation, and inference tasks, the hippocampus is repeatedly implicated in generating nonlocal or prospective state sequences, while prefrontal regions—especially OFC, mPFC/vmPFC, ACC, and dmPFC—carry task-state, goal, outcome, and control variables needed to use those sequences for choice. What is much less settled is whether hippocampus and PFC jointly replay the same content during planning, in a content-specific and causally necessary way. The literature is stronger on complementary representations and co-recruitment than on direct proof of coordinated cross-area replay during planning [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]] [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]].

## Current view

A cautious current view is a division of labor.

Hippocampus contributes sequential, relational, and often prospective representations of nonlocal possibilities. These can appear during choice, deliberation, or offline periods, and are well positioned to supply candidate trajectories or latent links needed for inference and replanning [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]] [[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]] [[raw/summaries/comrie2024_hippocampal_representations|Comrie et al. 2024]].

Prefrontal regions appear to provide the planning context that makes those sequences useful: hidden-state inference and outcome expectations in OFC, control and reconfiguration signals in ACC/dmPFC, goal/value maintenance in vmPFC, and route adaptation or hierarchical choice variables in lateral/dorsomedial PFC [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]] [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]] [[raw/summaries/holton2023_planning_vmPFC_lesions|Holton et al. 2023]].

Replay fits this picture as a candidate coordination mechanism, but the strongest evidence is indirect. Human fMRI shows replay-like reinstatement during rest that predicts later replanning, with hippocampal and ACC/vmPFC engagement under revaluation demands [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]]. Multi-region physiology shows that hippocampal–prefrontal sequential motifs can be replayed spontaneously and modulated by task demands, though not yet in a clean planning task [[raw/summaries/huang2023_hierarchical_replay_working_memory|Huang et al. 2023]].

Computationally, replay is often treated as a way to update or exploit predictive maps. Successor-representation accounts capture some generalization and replay phenomena, but more flexible frameworks such as linear RL and compositional predictive maps were proposed partly because standard SR struggles with detours and policy revaluation [[raw/summaries/momennejad2020_successor_representations_replay|Momennejad et al. 2020]] [[raw/summaries/piray2021_linear_reinforcement_planning|Piray et al. 2021]] [[raw/summaries/piray2025_compositional_cognitive_map|Piray et al. 2025]].

## Strongest evidence

- **Offline replay predicts later replanning in humans.** In a reward revaluation task, rest-period replay evidence for a distal task state predicted subsequent replanning, and this relationship was selective for the revaluation condition. Hippocampus and ACC showed stronger rest-period activity when replanning was required. This is strong functional evidence for replay in planning, but it remains correlational and temporally coarse; it does not directly show hippocampal–prefrontal sequence coordination [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]].

- **Hippocampus and OFC/PFC carry complementary map-like representations suited for planning.** Reviews converging across lesions, electrophysiology, and human imaging argue that hippocampus represents spatial-temporal and relational structure, whereas OFC/PFC emphasizes biologically relevant task states, hidden variables, and expected outcomes. This framework explains why replay-driven planning would likely require both systems, even if direct cross-area replay measurements are sparse [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]].

- **Multi-regional replay across hippocampal and prefrontal circuits is physiologically plausible.** Brain-wide Neuropixels data show hierarchical replay of sequential spiking motifs spanning hippocampal and prefrontal circuits, replayed outside the task delay and modulated on demand. This is among the strongest direct evidence for cross-area replay structure, but the task was working memory rather than explicit planning or navigation [[raw/summaries/huang2023_hierarchical_replay_working_memory|Huang et al. 2023]].

- **Hippocampal prospective/inferential codes can construct nonexperienced relations relevant to planning.** During choice, hippocampus expresses prospective codes; during rest, SWR-related activity can link reward relationships that were never directly experienced together. This strongly supports constructive, model-based use of memory, though it does not by itself establish prefrontal replay coupling [[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]].

- **Prefrontal planning signals are robust even when replay is not measured directly.** dmPFC tracks hierarchical plan cost and context in a virtual subway task, and vmPFC lesions impair forward search depth and feature selection in richer planning tasks. These findings matter because they constrain what a coordinated hippocampal–prefrontal planning system must explain [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]] [[raw/summaries/holton2023_planning_vmPFC_lesions|Holton et al. 2023]].

## Landmark papers

- [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]]  
  Established the influential “parallel cognitive maps” framing: hippocampus and OFC both represent task structure, but in different formats that are naturally complementary for planning.

- [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]]  
  First strong human evidence that offline replay-like activity predicts subsequent replanning behavior.

- [[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]]  
  Showed that hippocampal activity can prospectively encode inferred relationships and that rest-period SWR activity can bind nonexperienced reward associations.

- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]]  
  Repositioned PFC from “executive add-on” to core navigation/planning machinery, sharpening the case that replay-based planning must be understood as hippocampal–prefrontal coordination.

- [[raw/summaries/huang2023_hierarchical_replay_working_memory|Huang et al. 2023]]  
  Provided rare direct multi-regional evidence that hippocampal and prefrontal sequential activity can be replayed in coordinated hierarchical patterns.

## Boundaries and tensions

The main tension is between **functional plausibility** and **direct proof**. Many data fit the idea that hippocampal replay feeds prefrontal planning, but direct content-specific demonstrations of joint replay during planning are still limited.

A second tension is definitional. Human fMRI “replay” studies often measure reinstatement or category evidence across rest, not millisecond-scale sequences. Those results are important, but they are not equivalent to rodent sharp-wave ripple replay [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]].

There is also a task-generalization problem. Multi-regional replay has been observed in working-memory settings, while planning findings often come from navigation, revaluation, or hierarchical choice tasks. It is not yet clear how much these phenomena share a common mechanism [[raw/summaries/huang2023_hierarchical_replay_working_memory|Huang et al. 2023]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]].

“PFC” is too coarse a label. OFC, vmPFC, ACC, and dmPFC likely contribute different computations. OFC is especially implicated in hidden-state and outcome maps; ACC in error/control and replay prioritization; dmPFC in hierarchical plan structure; vmPFC in value and forward search. Many studies do not distinguish these roles cleanly enough for mechanistic claims about replay coordination [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]] [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]] [[raw/summaries/holton2023_planning_vmPFC_lesions|Holton et al. 2023]].

Computational interpretations are unsettled. SR-based accounts explain some replay-linked generalization, but they are weaker on policy revaluation and detours; linear RL and compositional map models are more flexible in principle, yet neural evidence distinguishing these algorithms is thin [[raw/summaries/momennejad2020_successor_representations_replay|Momennejad et al. 2020]] [[raw/summaries/piray2021_linear_reinforcement_planning|Piray et al. 2021]] [[raw/summaries/piray2025_compositional_cognitive_map|Piray et al. 2025]].

Finally, causal evidence remains the major gap. The provided literature strongly supports coordinated hippocampal and prefrontal contributions to planning, but only weakly supports the specific claim that disrupting cross-area replay disrupts planning.

## Open questions

- Does PFC replay the same content as hippocampus, or does it mainly evaluate/select hippocampal candidate sequences?

- Which prefrontal subregions couple to hippocampal replay for which planning demands: OFC for hidden state, ACC for prioritization and conflict, dmPFC for hierarchy, vmPFC for value integration?

- How do online prospective representations during navigation relate to offline rest replay? Are they two modes of one mechanism or partially distinct processes [[raw/summaries/comrie2024_hippocampal_representations|Comrie et al. 2024]] [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]]?

- What neural signal prioritizes replay for planning—unsigned prediction error, uncertainty, goal change, or novelty—and where is that prioritization implemented [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]]?

- Can experiments cleanly dissociate SR-like cached predictive maps from more flexible linear-RL or compositional planning schemes in hippocampal–prefrontal circuits [[raw/summaries/momennejad2020_successor_representations_replay|Momennejad et al. 2020]] [[raw/summaries/piray2021_linear_reinforcement_planning|Piray et al. 2021]] [[raw/summaries/piray2025_compositional_cognitive_map|Piray et al. 2025]]?

- What anatomical pathways actually mediate replay coordination during planning, and when do they operate? Bidirectional hippocampal–mPFC interactions are often proposed, but stage-specific circuit tests remain limited [[raw/summaries/eichenbaum2017_prefrontal_hippocampal_episodic|Eichenbaum 2017]].

## Key papers

- [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]] — parallel hippocampal/OFC cognitive maps for flexible decision making.
- [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]] — offline replay evidence predicts human replanning.
- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]] — PFC as a core navigation and planning system.
- [[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]] — hippocampal prospective and inferential coding across choice and rest.
- [[raw/summaries/huang2023_hierarchical_replay_working_memory|Huang et al. 2023]] — direct multi-regional hippocampal–prefrontal replay structure.
- [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]] — dmPFC representations of hierarchical planning cost.
- [[raw/summaries/holton2023_planning_vmPFC_lesions|Holton et al. 2023]] — vmPFC lesions impair key component processes of complex planning.
- [[raw/summaries/momennejad2020_successor_representations_replay|Momennejad et al. 2020]] — SR/replay framework for predictive planning.
- [[raw/summaries/piray2021_linear_reinforcement_planning|Piray et al. 2021]] — linear RL as a more flexible alternative to standard SR.
- [[raw/summaries/piray2025_compositional_cognitive_map|Piray et al. 2025]] — compositional predictive maps as a scalable planning account.

## Source papers
- [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser and Schoenbaum 2016]] | [[raw/mds/wikenheiser2016_cognitive_maps_hippocampus|source md]]: Over the river, through the woods: cognitive maps in the hippocampus and orbitofrontal cortex
- [[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]] | [[raw/mds/piray2021_linear_reinforcement_planning|source md]]: Linear reinforcement learning in planning, grid fields, and cognitive control
- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]] | [[raw/mds/patai2021_versatile_wayfinder_prefrontal|source md]]: The Versatile Wayfinder: Prefrontal Contributions to Spatial Navigation
- [[raw/summaries/piray2025_compositional_cognitive_map|Piray and Daw 2025]] | [[raw/mds/piray2025_compositional_cognitive_map|source md]]: Reconciling flexibility and efficiency: medial entorhinal cortex represents a compositional cognitive map
- [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]]: Offline replay supports planning in human reinforcement learning
- [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]] | [[raw/mds/balaguer2016_hierarchical_planning_subway|source md]]: Neural Mechanisms of Hierarchical Planning in a Virtual Subway Network
- [[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]] | [[raw/mds/barron2020_neuronal_computation_inferential|source md]]: Neuronal Computation Underlying Inferential Reasoning in Humans and Mice
- [[raw/summaries/comrie2024_hippocampal_representations|Comrie et al. 2024]] | [[raw/mds/comrie2024_hippocampal_representations|source md]]: Hippocampal representations of alternative possibilities are flexibly generated to meet cognitive demands
- [[raw/summaries/corbit2018_goal_directed_habitual|Corbit 2018]] | [[raw/mds/corbit2018_goal_directed_habitual|source md]]: Understanding the balance between goal-directed and habitual behavioral control
- [[raw/summaries/eichenbaum2017_prefrontal_hippocampal_episodic|Eichenbaum 2017]] | [[raw/mds/eichenbaum2017_prefrontal_hippocampal_episodic|source md]]: Prefrontal–hippocampal interactions in episodic memory
- [[raw/summaries/holton2023_planning_vmPFC_lesions|Holton et al. 2023]] | [[raw/mds/holton2023_planning_vmPFC_lesions|source md]]: Disentangling the component processes in complex planning impairments following ventromedial prefrontal lesions
- [[raw/summaries/huang2023_hierarchical_replay_working_memory|Huang et al. 2023]] | [[raw/mds/huang2023_hierarchical_replay_working_memory|source md]]: Hierarchical replay of multi-regional sequential spiking associated with working memory
- [[raw/summaries/kurth2023_replay_compositional_computation|Kurth-Nelson et al. 2023]] | [[raw/mds/kurth2023_replay_compositional_computation|source md]]: Replay and compositional computation
