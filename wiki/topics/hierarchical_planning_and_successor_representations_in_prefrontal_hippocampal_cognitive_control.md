---
title: "Hierarchical planning and successor representations in prefrontal–hippocampal cognitive control"
subtopic_id: prefrontal_goal_representation_and_control__03
parent_topic_id: prefrontal_goal_representation_and_control
page_type: topic
page_worthiness: 3
status: draft_llm
generated_at: "2026-04-12T19:50:24.338917+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - botvinick2009_hierarchical_behavior_reinforcement
  - wientjes2024_successor_representation
  - piray2021_linear_reinforcement_planning
  - brunec2022_predictive_representations_hierarchies
  - jensen2024_recurrent_planning_hippocampal_replay
core_papers:
  - badre2019_hierarchical_cognitive_control_lobes
  - botvinick2009_hierarchical_behavior_reinforcement
  - brunec2022_predictive_representations_hierarchies
  - ho2022_mental_representations_planning
  - janssen2022_hierarchical_rl_motor_sequences
  - jensen2024_recurrent_planning_hippocampal_replay
  - kaplan2018_active_inference_navigation
  - kim2026_hippocampus_smallworld
---

# Hierarchical planning and successor representations in prefrontal–hippocampal cognitive control

Current work converges on a limited but useful picture: goal-directed control often looks hierarchical, and the underlying representations appear multiscale rather than flat. The best-supported account is that hippocampal and prefrontal systems encode predictive structure at different temporal/spatial horizons, which can support subgoal-based planning and abstraction. But the literature does not support a single settled mechanism. Successor-representation (SR) models explain several behavioral and neural signatures of predictive mapping, while hierarchical RL explains temporally abstract action structure, and newer alternatives such as linear RL and rollout-based recurrent planning highlight important failure modes of vanilla SR and strict option hierarchies.

## Current view

Planning in this domain is increasingly framed as an interaction between:

- predictive maps of future states, often formalized as SR-like representations
- hierarchical abstractions that compress action and state spaces
- control policies that can be refined online by simulation or replay

A plausible synthesis is that hippocampus provides shorter-horizon predictive structure and prefrontal cortex provides progressively more abstract, longer-horizon control representations. Naturalistic navigation fMRI is broadly consistent with such a gradient, from posterior hippocampus to anterior hippocampus to medial/anterior PFC [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]].

Behaviorally, people do not appear to rely on a single representation. In a task with community structure, hierarchical abstraction best explained choices, while SR-derived variables better explained response times and memory-linked structure learning [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]]. That is a useful result because it argues against an overly simple “SR explains planning” claim.

At the algorithmic level, hierarchical RL remains the clearest formalization of temporally extended control, especially via options/subgoals [[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]]. But pure SR has known limits under policy revaluation and some environmental changes, motivating alternatives such as linear RL’s goal-independent default representation [[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]].

The neural story is suggestive, not complete. There is evidence for frontal hierarchical control organization more generally [[raw/summaries/badre2019_hierarchical_cognitive_control_lobes|Badre 2019]], and for abstract goal/action coding in lateral PFC [[raw/summaries/tanji2007_behavioral_planning_prefrontal|Tanji and Hoshi 2007]], but direct causal evidence tying specific PFC subregions to SRs, options, or rollout control remains thin.

## Strongest evidence

[[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] provides the strongest direct neural evidence for multiscale predictive coding in a prefrontal–hippocampal hierarchy.

- During virtual navigation in a real city, representational similarity tracked predictive horizons across regions.
- Horizon length increased roughly from posterior hippocampus to anterior hippocampus to medial/orbitofrontal/anterior PFC.
- Goal-directed navigation increased predictive similarity relative to GPS-guided traversal, especially at longer horizons.
- The result is consistent with SR-like predictive maps, though the authors do not uniquely identify SR over other predictive sequence models.

[[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] is the clearest behavioral evidence linking predictive structure learning to hierarchical abstraction.

- Hierarchical choice models best captured overt decisions.
- SR-based variables best captured response-time fluctuations.
- Individual differences in SR modularity predicted better hierarchical choice, better reward, and better memory for task structure.
- The key implication is coexistence of fine-grained predictive and coarse hierarchical representations, not replacement of one by the other.

[[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]] remains foundational for the mechanistic argument that hierarchical control should be understood in RL terms.

- In four-rooms simulations, useful options reduced effective search depth and accelerated learning.
- Poorly chosen options produced negative transfer and inflexibility.
- The paper mapped option maintenance, policy selection, and extended prediction errors onto prefrontal, striatal, and orbitofrontal circuitry.
- This mapping is still influential, but mostly theoretical rather than directly verified.

[[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]] supplies the strongest computational challenge to interpreting planning solely through standard SR.

- Their linear RL model reuses a default representation that is stable across goals.
- It handles reward revaluation, policy revaluation, and detour tasks that defeat vanilla SR.
- This matters because many “hierarchical planning” problems require exactly these forms of flexible replanning.

[[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]] strengthens the link between online planning and hippocampal-like simulation.

- Human thinking times increased when farther from the goal and early in trials.
- A recurrent agent with imagined rollouts learned to deploy rollouts in the same conditions.
- Rollout statistics matched key features of rodent forward replay.
- This supports the idea that hippocampal sequences can contribute directly to planning, though the biological causal chain remains unresolved.

## Landmark papers

[[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]]  
The canonical theoretical statement of hierarchical RL as a neural framework for temporally abstract cognitive control.

[[raw/summaries/badre2019_hierarchical_cognitive_control_lobes|Badre 2019]]  
Important for situating hierarchical planning within a broader frontal-lobe control architecture, especially lateral PFC hierarchy.

[[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]]  
The strongest fMRI evidence that predictive horizons are organized across hippocampal and prefrontal gradients.

[[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]]  
A major correction to naive SR-centric accounts by showing how flexible replanning can arise from a different reusable predictive representation.

[[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]]  
The clearest evidence that hierarchical abstraction in behavior is related to learned predictive structure, while also dissociating choices from RT signatures.

[[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]]  
Important for linking hippocampal replay-like dynamics to online planning rather than treating replay as purely offline learning.

## Boundaries and tensions

The main computational tension is not “hierarchical vs non-hierarchical,” but which reusable representation supports flexible planning.

- SR captures predictive occupancy under a policy.
- Options/HRL capture temporally abstract action structure.
- Linear RL captures efficient replanning under changing rewards or policies.
- These are overlapping, not interchangeable, frameworks.

Vanilla SR is not sufficient for all forms of flexibility. [[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]] explicitly show failure on policy revaluation and some detour-like changes. So claims that hippocampal-prefrontal planning simply implements SR should be treated cautiously.

The evidence is task-skewed toward navigation-like settings. The strongest neural evidence comes from spatial navigation [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]], and the strongest behavioral SR-abstraction evidence also uses structured state spaces resembling navigation graphs [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]]. Generalization to abstract cognitive control tasks is plausible, but not yet tightly established.

Neural localization remains underdetermined. HRL theory points to DLPFC, striatum, and OFC for option representations and values [[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]], while predictive-horizon results emphasize anterior PFC, mPFC, OFC, and hippocampus [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]]. These accounts may be compatible, but they are not yet integrated at the level of direct neural tests.

Strict hierarchies can help and hurt. Useful subgoals speed learning, but mis-specified options produce negative transfer and shortcut insensitivity [[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]]. This is a real constraint on claims that hierarchical abstraction is simply adaptive.

The interpretation of fMRI predictive similarity is not unique. [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] is consistent with SR-like predictive maps, but does not rule out other predictive coding or sequence-learning schemes. [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] makes the same point behaviorally: alternative models with equivalent discounting structure could mimic SR.

Replay-based planning also complicates classical dual-system stories. [[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]] argues for iterative improvement of a single policy through rollouts, rather than arbitration between separate model-based and model-free controllers. That proposal is appealing, but still mainly model-driven.

## Open questions

How are useful subgoals discovered?  
This remains a central unresolved issue in HRL accounts [[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]]. Current evidence shows that people exploit structure, but not how the brain identifies the right decomposition online.

What exactly is stored in hippocampus versus PFC?  
Shorter versus longer predictive horizons are a robust working idea [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]], but this does not yet tell us whether regions encode SRs, option models, abstract schemas, uncertainty, or mixtures that depend on task demands.

When does behavior rely on coarse hierarchy versus detailed predictive maps?  
[[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] suggests choices and RTs may read out different representational levels. The control policy for switching between those levels is still unclear.

Can SR-like maps and replay-based planning be unified?  
One possibility is that stable predictive maps support fast evaluation while hippocampal replay refines choices online [[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]]. But direct evidence linking replay events to changes in PFC goal representations is still missing.

Is linear RL a better neural-level account than standard SR?  
[[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]] solves several problems that standard SR cannot. Whether the brain uses something closer to a default representation than a policy-bound SR is an open empirical question.

Do these principles extend beyond spatial domains?  
Frontal hierarchy and abstract action coding suggest yes [[raw/summaries/badre2019_hierarchical_cognitive_control_lobes|Badre 2019]] [[raw/summaries/tanji2007_behavioral_planning_prefrontal|Tanji and Hoshi 2007]], but direct prefrontal–hippocampal evidence in nonspatial cognitive control remains comparatively sparse.

## Key papers

- [[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]] — foundational hierarchical RL framework and neural mapping for temporally abstract control.
- [[raw/summaries/badre2019_hierarchical_cognitive_control_lobes|Badre 2019]] — review of frontal-lobe hierarchical control architecture relevant to abstract goal structure.
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] — fMRI evidence for multiscale predictive representations across hippocampal and prefrontal gradients.
- [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] — behavioral evidence that SR-like predictive structure supports hierarchical abstraction, with dissociable choice and RT signatures.
- [[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]] — alternative to vanilla SR that better handles flexible replanning and detours.
- [[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]] — recurrent rollout model connecting planning behavior to hippocampal replay.
- [[raw/summaries/tanji2007_behavioral_planning_prefrontal|Tanji and Hoshi 2007]] — evidence that lateral PFC represents abstract action categories and behavioral goals during planning.
- [[raw/summaries/ho2022_mental_representations_planning|Ho et al. 2022]] — complementary account in which people construct simplified task representations for planning, relevant to abstraction beyond classic SR/HRL.

## Source papers
- [[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]] | [[raw/mds/botvinick2009_hierarchical_behavior_reinforcement|source md]]: Hierarchically organized behavior and its neural foundations: A reinforcement-learning perspective
- [[raw/summaries/wientjes2024_successor_representation|Wientjes and Holroyd 2024]] | [[raw/mds/wientjes2024_successor_representation|source md]]: The successor representation subserves hierarchical abstraction for goal-directed behavior
- [[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]] | [[raw/mds/piray2021_linear_reinforcement_planning|source md]]: Linear reinforcement learning in planning, grid fields, and cognitive control
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec and Momennejad 2022]] | [[raw/mds/brunec2022_predictive_representations_hierarchies|source md]]: Predictive Representations in Hippocampal and Prefrontal Hierarchies
- [[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]] | [[raw/mds/jensen2024_recurrent_planning_hippocampal_replay|source md]]: A recurrent network model of planning explains hippocampal replay and human behavior
- [[raw/summaries/badre2019_hierarchical_cognitive_control_lobes|Badre and Desrochers 2019]] | [[raw/mds/badre2019_hierarchical_cognitive_control_lobes|source md]]: Hierarchical cognitive control and the frontal lobes
- [[raw/summaries/ho2022_mental_representations_planning|Ho et al. 2022]] | [[raw/mds/ho2022_mental_representations_planning|source md]]: People construct simplified mental representations to plan
- [[raw/summaries/janssen2022_hierarchical_rl_motor_sequences|Janssen et al. 2022]] | [[raw/mds/janssen2022_hierarchical_rl_motor_sequences|source md]]: Hierarchical Reinforcement Learning, Sequential Behavior, and the Dorsal Frontostriatal System
- [[raw/summaries/kaplan2018_active_inference_navigation|Kaplan and Friston 2018]] | [[raw/mds/kaplan2018_active_inference_navigation|source md]]: Planning and navigation as active inference
- [[raw/summaries/kim2026_hippocampus_smallworld|Kim et al. 2026]] | [[raw/mds/kim2026_hippocampus_smallworld|source md]]: The hippocampus as a small-world cognitive map
