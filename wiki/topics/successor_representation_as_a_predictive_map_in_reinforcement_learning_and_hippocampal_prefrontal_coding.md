---
title: "Successor representation as a predictive map in reinforcement learning and hippocampal–prefrontal coding"
subtopic_id: predictive_maps_and_successor_representation__01
parent_topic_id: predictive_maps_and_successor_representation
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:25:04.528172+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - dayan1993_successor_representation
  - barreto2017_successor_features_transfer_c
  - brunec2022_predictive_representations_hierarchies
  - machado2018_eigenoption_successor_representation
  - momennejad2018_offline_replay_planning
core_papers:
  - akam2015_two_step_task_habits
  - akam2021_dopamine_model_based_rl
  - barreto2017_successor_features_transfer_c
  - botvinick2020_deep_reinforcement_learning_neuro
  - brown2016_prospective_goals_hippocampus
  - brunec2022_predictive_representations_hierarchies
  - dayan1993_successor_representation
  - dolan2013_goals_habits_brain_b
---

# Successor representation as a predictive map in reinforcement learning and hippocampal–prefrontal coding

The successor representation (SR) is best viewed as a middle-ground solution to reinforcement learning’s planning problem: it caches expected future state occupancy under a policy, so values can be recomputed quickly when rewards change, but not when transition structure changes. In neuroscience, this makes SR attractive as a bridge between model-free temporal-difference learning and map-like predictive coding in hippocampus and prefrontal cortex. The strongest case is computational and behavioral-neural convergence, not a clean one-to-one neural identification: SR explains generalization and reward revaluation well, successor features extend this to transfer under shared dynamics, and human fMRI/navigation work shows multiscale predictive coding gradients in hippocampus–PFC that are SR-like. But the literature does not support a simple conclusion that “the brain uses SR” full stop; policy dependence, task confounds, and weak dissociation from other predictive/map-based accounts remain central.

## Current view

SR formalizes state similarity by shared futures, not shared sensory features. In Dayan’s original formulation, the representation of state \(s\) is the expected discounted future occupancy of all states under the current policy [[raw/summaries/dayan1993_successor_representation|Dayan 1993]].

This matters because it factorizes value learning into:
- predictive dynamics captured by the SR
- immediate reward weights layered on top

That gives SR a characteristic computational profile:
- faster adaptation than cached model-free values when rewards change
- worse flexibility than full model-based planning when transitions or policies change substantially

Current neuroscience interest comes from that in-between status. SR offers a concrete way to interpret hippocampal and prefrontal codes as predictive maps over multiple horizons, rather than as purely spatial maps or purely value codes [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]].

The field’s present stance is therefore fairly specific:
- SR is a strong normative and algorithmic candidate for predictive state coding.
- Successor features (SFs) make the framework useful for transfer and hierarchical RL under shared dynamics [[raw/summaries/barreto2017_successor_features_transfer_c|Barreto et al. 2017]].
- Neural data are consistent with SR-like coding, especially in navigation and replay/planning tasks, but are not uniquely diagnostic of SR over other predictive or latent-state accounts [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]].

## Strongest evidence

The cleanest evidence is still computational.

[[raw/summaries/dayan1993_successor_representation|Dayan 1993]] showed that SR can itself be learned by TD methods and improves generalization in navigation problems where Euclidean proximity is misleading. Critically, the representation respects barriers: states separated by a wall are not treated as similar just because they are spatially near. That is the core conceptual win of SR over naive spatial generalization.

[[raw/summaries/barreto2017_successor_features_transfer_c|Barreto et al. 2017]] is the strongest transfer result. Successor features plus generalized policy improvement give formal guarantees and strong empirical performance when tasks share dynamics but differ in reward. This is the most rigorous statement of what SR-like predictive representations buy you: cheap reward revaluation and policy reuse, not arbitrary replanning.

On the neuroscience side, [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] is the strongest direct “predictive map” evidence. During naturalistic virtual navigation, representational similarity tracked predictive horizons across a hierarchy:
- posterior hippocampus: shortest horizons
- anterior hippocampus: longer horizons
- mPFC/OFC/ACC: intermediate to long horizons
- anterior PFC: longest horizons

That gradient is exactly the kind of multiscale predictive organization SR-inspired theories would expect. The effect was stronger in goal-directed than GPS-guided navigation, which argues against a purely perceptual account.

Two additional findings strengthen the broader interpretation without being SR-specific:
- [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] found hippocampal patterns prospectively code navigational goals and subgoals during planning.
- [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]] showed offline replay during rest predicts later replanning, consistent with replay updating predictive task structure.

Together, these papers support a synthesis: hippocampal–prefrontal systems carry predictive information at multiple scales, and SR is one of the best-specified RL formalisms for that computation.

## Landmark papers

- [[raw/summaries/dayan1993_successor_representation|Dayan 1993]]: foundational SR paper; defines value as expected future occupancy times immediate reward.
- [[raw/summaries/barreto2017_successor_features_transfer_c|Barreto et al. 2017]]: successor features and generalized policy improvement; makes SR useful for principled transfer.
- [[raw/summaries/machado2018_eigenoption_successor_representation|Machado et al. 2018]]: links SR to spectral structure and option discovery, extending predictive maps into hierarchical RL.
- [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]]: human replay evidence tied to replanning, relevant to how predictive maps may be updated offline.
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]]: strongest hippocampal–PFC multiscale predictive map result in naturalistic navigation.

## Boundaries and tensions

SR is policy-dependent. That is a feature for efficient prediction and a liability for flexible control. If the policy changes a lot, the stored predictive map becomes wrong or at least less useful [[raw/summaries/dayan1993_successor_representation|Dayan 1993]].

This creates the classic boundary:
- reward revaluation: SR should handle relatively well
- transition revaluation or detours: SR should struggle unless updated or augmented with model-based computation

That boundary is theoretically sharp, but many behavioral tasks do not isolate it cleanly. In particular, the two-step task is not a secure assay of model-based planning versus cached predictive structure, because sophisticated model-free agents with expanded state representations can mimic model-based signatures under standard analyses [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]]. So behavioral evidence often under-identifies SR.

Neural “predictive similarity” is also not uniquely SR. Multiscale future coding in hippocampus and PFC could reflect:
- SR-like discounted occupancy
- explicit model-based rollouts
- latent-state or task-schema coding
- prospective goal/subgoal representations without full SR structure

That is why [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] is important but not decisive: the data fit SR-like horizons, yet the design does not fully recover the graph-theoretic structure needed to distinguish SR from other predictive accounts.

Replay findings face the same issue. [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]] show replay predicts replanning, but fMRI cannot resolve sequential replay with enough precision to establish the exact update rule. The result is highly compatible with SR updating, not proof of it.

Successor features widen SR’s scope but also reveal its assumptions. Transfer guarantees rely on shared dynamics and approximately linear reward decompositions [[raw/summaries/barreto2017_successor_features_transfer_c|Barreto et al. 2017]]. That is powerful, but narrower than many real-world transfer problems.

There is also an unresolved neurobiological tension around dopamine. The idea that dopamine might carry an SR prediction error is appealing, but [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Walton 2021]] argue the evidence better supports a scalar reward prediction error plus additional surprise-like signals, rather than a specifically successor-based error.

## Open questions

How often does behavior genuinely require SR, rather than full model-based planning or simpler state-abstraction heuristics? Current task designs often do not cleanly separate these possibilities [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]].

What exactly is represented along the hippocampal–PFC hierarchy?
- discounted occupancy over states
- subgoal structure
- latent task states
- compressed predictive abstractions

The hierarchy is clear enough to be interesting, but not yet mechanistically pinned down [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]].

How are predictive maps updated?
- online TD-like learning
- offline replay
- explicit simulation
- mixtures that depend on uncertainty or surprise

[[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]] supports a role for offline replay, but the update algorithm remains inferential.

What is the right feature basis for successor features in brains or deep agents? The transfer guarantees are only as good as the feature decomposition of reward and state [[raw/summaries/barreto2017_successor_features_transfer_c|Barreto et al. 2017]].

Can SR-scale ideas explain abstraction beyond space? Human cognitive map theories increasingly extend to conceptual, social, and temporal structure [[raw/summaries/epstein2017_cognitive_maps_humans|Epstein et al. 2017]]. But direct evidence that hippocampal–prefrontal predictive maps in those domains are specifically successor-like is still limited.

How should SR relate to hierarchical option discovery? [[raw/summaries/machado2018_eigenoption_successor_representation|Machado et al. 2018]] shows a principled link between SR geometry and options, but downstream neural predictions remain underdeveloped.

## Key papers

- [[raw/summaries/dayan1993_successor_representation|Dayan 1993]] — original SR theory; still the clearest statement of the representation’s computational tradeoff.
- [[raw/summaries/barreto2017_successor_features_transfer_c|Barreto et al. 2017]] — successor features + generalized policy improvement; strongest transfer framework built from SR.
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] — best direct evidence for multiscale predictive coding across hippocampus and PFC in navigation.
- [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]] — replay predicts replanning; relevant for how predictive maps may be updated.
- [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] — prospective hippocampal coding of goals and subgoals during route planning.
- [[raw/summaries/machado2018_eigenoption_successor_representation|Machado et al. 2018]] — extends SR into hierarchical RL and option discovery.
- [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]] — important caution that common behavioral assays do not cleanly identify SR/model-based computation.
- [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Walton 2021]] — skeptical review of dopamine-as-SR-error interpretations.

## Source papers
- [[raw/summaries/dayan1993_successor_representation|Dayan 1993]] | [[raw/mds/dayan1993_successor_representation|source md]]: Improving Generalisation for Temporal Difference Learning: The Successor Representation
- [[raw/summaries/barreto2017_successor_features_transfer_c|Barreto et al. 2017]] | [[raw/mds/barreto2017_successor_features_transfer_c|source md]]: Successor Features for Transfer in Reinforcement Learning
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec and Momennejad 2022]] | [[raw/mds/brunec2022_predictive_representations_hierarchies|source md]]: Predictive Representations in Hippocampal and Prefrontal Hierarchies
- [[raw/summaries/machado2018_eigenoption_successor_representation|Machado et al. 2018]] | [[raw/mds/machado2018_eigenoption_successor_representation|source md]]: Eigenoption Discovery Through the Deep Successor Representation
- [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]]: Offline replay supports planning in human reinforcement learning
- [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]] | [[raw/mds/akam2015_two_step_task_habits|source md]]: Simple Plans or Sophisticated Habits? State, Transition and Learning Interactions in the Two-Step Task
- [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Walton 2021]] | [[raw/mds/akam2021_dopamine_model_based_rl|source md]]: What is dopamine doing in model-based reinforcement learning?
- [[raw/summaries/botvinick2020_deep_reinforcement_learning_neuro|Botvinick et al. 2020]] | [[raw/mds/botvinick2020_deep_reinforcement_learning_neuro|source md]]: Deep Reinforcement Learning and Its Neuroscientific Implications
- [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] | [[raw/mds/brown2016_prospective_goals_hippocampus|source md]]: Prospective representation of navigational goals in the human hippocampus
- [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]] | [[raw/mds/dolan2013_goals_habits_brain_b|source md]]: Goals and Habits in the Brain
