---
title: "Hippocampal replay and schema-guided generalization"
subtopic_id: schemas_and_generalization__02
parent_topic_id: schemas_and_generalization
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:26:40.647114+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - whittington2020_tolman_eichenbaum_machine
  - gupta2010_replay_not_simple_function
  - foster2017_replay_memory_consolidation
  - widloski2022_hippocampal_replay_barriers
  - baram2021_entorhinal_ventromedial_rl
core_papers:
  - alonso2021_hexmaze_cognitive_map
  - baram2021_entorhinal_ventromedial_rl
  - basu2023_goal_pointer_cognitive_map_ofc
  - duvelle2023_temporal_hippocampal_inference
  - elgaby2023_behavioral_structure_mapping
  - findlay2021_replay_wake_sleep
  - foster2017_replay_memory_consolidation
  - gupta2010_replay_not_simple_function
related_wiki_pages:
  - wiki/topics/entorhinal_grid_cells_and_continuous_attractor_models_of_cognitive_maps
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/hippocampal_prefrontal_replay_in_planning
  - wiki/topics/reward_modulated_hippocampal_replay_in_spatial_reinforcement_learning
---

# Hippocampal replay and schema-guided generalization

The best-supported view is that hippocampal replay is not a passive recap of recent episodes but a generative sampling process over a learned relational model of the environment. In spatial tasks, replay can depict nonlocal paths, novel shortcuts, and rapid rerouting around new barriers, implying access to structured knowledge that goes beyond direct recent experience [[raw/summaries/gupta2010_replay_not_simple_function|Gupta et al. 2010]] [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]]. The broader “schema-guided” claim is plausible but unevenly evidenced: direct replay evidence is strongest in navigation, whereas non-spatial generalization is supported more by entorhinal/prefrontal structure coding and computational models than by direct replay measurements [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]].

## Current view

Replay is now better treated as model-based sequence generation than as memory trace recapitulation.

In awake sharp-wave ripple periods, hippocampal sequences can represent trajectories that are:
- not the most recent,
- not the most frequent,
- sometimes never directly experienced as such,
- and behaviorally relevant to upcoming navigation [[raw/summaries/gupta2010_replay_not_simple_function|Gupta et al. 2010]] [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]].

This makes replay a candidate mechanism for schema-guided generalization: once relational structure is learned, sequence generation can fill in missing transitions, evaluate alternatives, and adapt to local task changes without rebuilding the entire map.

A useful working synthesis is:
- hippocampus supplies conjunctive state sequences,
- entorhinal cortex supplies reusable structural scaffolds,
- prefrontal/striatal systems bias replay toward goals, task demands, and learning needs [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai 2021]].

But this is still a synthesis, not a settled mechanism. Several frameworks remain viable:
- successor-like predictive maps,
- attractor-plus-sequence dynamics,
- prioritized memory access in reinforcement learning,
- latent-state / schema factorization accounts such as TEM [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] [[raw/summaries/whittington2022_cognitive_map_b|Whittington et al. 2022]].

## Strongest evidence

The strongest direct evidence comes from rodent spatial replay.

[[raw/summaries/gupta2010_replay_not_simple_function|Gupta et al. 2010]] showed that awake replay is not well explained by recency or accumulated experience. Replay sampled nonlocal trajectories and could include shortcut sequences not directly traversed. That is hard to reconcile with a pure “recent memory replay” account and strongly supports sequence generation from map structure.

[[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] sharpened the generalization claim. Replay rapidly conformed to new barrier layouts even though most place fields stayed stable. This dissociates flexible path computation from wholesale remapping and suggests that replay can recompute valid routes using stable spatial representations plus updated transition constraints.

[[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] synthesized the broader shift in the field: replay occurs during wake, can reverse order, can depict remote or novel trajectories, and often aligns with future behavior rather than merely rehearsing the past. As a review, it is not primary evidence, but it accurately summarizes why the old consolidation-only view became inadequate.

For schema-like transfer beyond spatial navigation, the strongest relevant empirical evidence is not replay itself but abstract structure coding. [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] showed that entorhinal cortex generalized relational structure across different sensory instantiations of a non-spatial reinforcement learning problem, with vmPFC/ventral striatal prediction-error patterns also depending on structure. This supports the idea that reusable task structure exists in the same broader circuit, but it does not directly show hippocampal replay driving non-spatial generalization.

Behavioral evidence for schema-like map accumulation over long timescales also matters, though indirectly. [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]] found accelerated learning after prior knowledge had built up in the HexMaze, consistent with schema formation. However, replay was not measured, so any link to replay remains inferential.

## Landmark papers

- [[raw/summaries/gupta2010_replay_not_simple_function|Gupta et al. 2010]]  
  Key empirical break from the “replay = recent experience” view. Important because it demonstrated nonlocal and shortcut-like replay content.

- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]]  
  Consolidated the modern interpretation of replay as an internally generated model-sampling process relevant to planning and learning, not just offline consolidation.

- [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]]  
  Major theoretical bridge between spatial and relational memory. TEM formalized how structural knowledge could generalize across environments and tasks while hippocampal representations remap.

- [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]]  
  Landmark for extending cognitive-map ideas to non-spatial RL structure in humans. Important for the “schema-guided” side of this topic, though not a replay study.

- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]]  
  Strong evidence that replay can update quickly to altered topology without global place-field remapping, directly linking replay to flexible rerouting.

## Boundaries and tensions

The replay evidence is strongest for spatial navigation. Claims that replay supports abstract relational generalization in non-spatial tasks are still mostly extrapolated from:
- entorhinal/prefrontal structure coding,
- computational models,
- and conceptual unification frameworks [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]].

Causality remains limited. Replay often predicts subsequent behavior, but many key studies are correlational. Stronger claims that replay is necessary for flexible generalization, shortcut construction, or schema transfer require targeted disruption during the relevant computation, not just replay-behavior correlations [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]].

“Schema-guided” can mean at least three different things, which are often conflated:
- retrieval of old structure,
- online inference over latent transitions,
- or reward/goal-biased route sampling.  
Goal-directed replay is not automatically evidence of abstract schema use.

Place-field stability alongside replay flexibility is important but mechanistically underconstrained. [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] implies that sequence content can update faster than the underlying place code. That is a real constraint on models, but it does not yet tell us whether the update comes from CA3 recurrent dynamics, entorhinal input, PFC biasing, or some combination.

Multiple computational accounts can explain parts of the data:
- successor representations explain predictive structure,
- attractor/heteroassociative models explain sequence dynamics,
- prioritized replay explains selective sampling,
- TEM explains factorized structural generalization [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]].  
At present, empirical discriminations between these accounts are weak.

The sleep vs wake issue is also unresolved. The strongest “generalization/planning” evidence comes from awake replay. Sleep replay may share mechanisms or may serve partly different functions; the field does not yet have a clean unifying account [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]].

## Open questions

- What circuit component performs the fast topology update seen in rerouting replay: CA3 recurrence, entorhinal structural input, medial PFC control, or dopaminergic/striatal biasing?

- Does selective disruption of awake SWRs impair zero-shot detours, shortcuts, or transfer to novel-but-structurally-familiar tasks more than it impairs simple memory retrieval?

- Is there direct non-spatial replay evidence for schema-guided inference, rather than only abstract structure coding in EC/vmPFC [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]]?

- How does long-timescale schema formation alter replay statistics? The HexMaze results imply accumulating prior knowledge [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]], but the neural mechanism is not yet pinned to replay.

- How should replay relate to latent-state inference and splitter signals? The latent-state literature suggests context segmentation may be necessary for flexible generalization, but the interface with replay remains underdeveloped [[raw/summaries/duvelle2023_temporal_hippocampal_inference|Duvelle et al. 2023]].

- Can human single-neuron and intracranial studies show replay-like sequence generation over abstract task structure, not just temporal predictive coding [[raw/summaries/tacikowski2024_temporal_structure_hippocampal|Tacikowski et al. 2024]]?

- How are explicit goal representations outside hippocampus integrated with replay? OFC “goal pointer” signals are a plausible biasing source, but direct coordination with replay remains to be established [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu et al. 2023]].

## Key papers

- [[raw/summaries/gupta2010_replay_not_simple_function|Gupta et al. 2010]] — direct evidence that replay is not a simple recency/frequency function and can generate shortcut-like sequences.
- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] — field-defining synthesis of replay as generative, wake-active, and planning-relevant.
- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] — replay reroutes around new barriers while place fields remain largely stable.
- [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] — core theoretical account of factorized structural knowledge and relational generalization in hippocampal-entorhinal circuits.
- [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] — strong non-spatial evidence that EC/vmPFC encode reusable relational task structure.
- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] — useful synthesis linking replay findings to reinforcement-learning-style prioritized sampling.
- [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]] — behavioral evidence for schema-like spatial knowledge accumulation, relevant but mechanistically indirect.
- [[raw/summaries/whittington2022_cognitive_map_b|Whittington et al. 2022]] — broad formal framework connecting cognitive maps, sequence learning, and latent-state structure across domains.

## Related wiki pages
- [[wiki/topics/entorhinal_grid_cells_and_continuous_attractor_models_of_cognitive_maps|Entorhinal grid cells and continuous attractor models of cognitive maps]]: Crosslink around the idea that entorhinal map-like state codes may provide structured inputs or latent geometry that hippocampal replay samples, reads out, or recombines during flexible planning and generalization.
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]: Crosslink via a shared 'replay' section: from Page A to Page B for replay as a generalization/inference mechanism, and from Page B to Page A for the hippocampal-entorhinal map codes and navigation framework that replay operates over.
- [[wiki/topics/hippocampal_prefrontal_replay_in_planning|Hippocampal–prefrontal replay in planning]]: Crosslink on replay as structured prospective simulation: Page B explains the relational/schema content replay may generate, while Page A explains how that content may be integrated with prefrontal task-state and control signals for planning.
- [[wiki/topics/reward_modulated_hippocampal_replay_in_spatial_reinforcement_learning|Reward-modulated hippocampal replay in spatial reinforcement learning]]: Crosslink around 'functional roles of hippocampal replay': Page A can point to reward modulation as a policy/value-related constraint on generative replay, while Page B can point to schema/generalization work as the broader model-based structure that replay may operate over.

## Source papers
- [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] | [[raw/mds/whittington2020_tolman_eichenbaum_machine|source md]]: The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation
- [[raw/summaries/gupta2010_replay_not_simple_function|Gupta et al. 2010]] | [[raw/mds/gupta2010_replay_not_simple_function|source md]]: Hippocampal Replay Is Not a Simple Function of Experience
- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] | [[raw/mds/foster2017_replay_memory_consolidation|source md]]: Replay Comes of Age
- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski and Foster 2022]] | [[raw/mds/widloski2022_hippocampal_replay_barriers|source md]]: Flexible rerouting of hippocampal replay sequences around changing barriers in the absence of global place field remapping
- [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] | [[raw/mds/baram2021_entorhinal_ventromedial_rl|source md]]: Entorhinal and ventromedial prefrontal cortices abstract and generalize the structure of reinforcement learning problems
- [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]] | [[raw/mds/alonso2021_hexmaze_cognitive_map|source md]]: The HexMaze: A Previous Knowledge Task on Map Learning for Mice
- [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu and Ito 2023]] | [[raw/mds/basu2023_goal_pointer_cognitive_map_ofc|source md]]: A goal pointer for a cognitive map in the orbitofrontal cortex
- [[raw/summaries/duvelle2023_temporal_hippocampal_inference|Duvelle et al. 2023]] | [[raw/mds/duvelle2023_temporal_hippocampal_inference|source md]]: Temporal context and latent state inference in the hippocampal splitter signal
- [[raw/summaries/elgaby2023_behavioral_structure_mapping|El-Gaby et al. 2023]] | [[raw/mds/elgaby2023_behavioral_structure_mapping|source md]]: A Cellular Basis for Mapping Behavioural Structure
- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] | [[raw/mds/findlay2021_replay_wake_sleep|source md]]: The evolving view of replay and its functions in wake and sleep
