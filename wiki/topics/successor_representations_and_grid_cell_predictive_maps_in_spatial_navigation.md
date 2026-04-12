---
title: "Successor representations and grid-cell predictive maps in spatial navigation"
subtopic_id: behavioral_paradigms_and_navigation_tasks__02
parent_topic_id: behavioral_paradigms_and_navigation_tasks
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:48:01.213935+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - momennejad2017_successor_representation_humans
  - russek2017_model_based_reinforcement
  - piray2021_linear_reinforcement_planning
  - piray2020_linear_reinforcement_learning
  - decothi2022_predictive_spatial_navigation
core_papers:
  - decothi2022_predictive_spatial_navigation
  - eldar2020_replay_planning
  - huang2024_hippocampal_theta_goal_distance
  - martinet2011_spatial_learning_action_planning
  - momennejad2017_successor_representation_humans
  - neupane2022_mental_navigation_entorhinal_cortex
  - piray2020_linear_reinforcement_learning
  - piray2021_linear_reinforcement_planning
---

# Successor representations and grid-cell predictive maps in spatial navigation

The strongest convergence is on a constrained claim: spatial behavior often looks as if animals and humans use cached predictions about future state occupancy, and such predictive maps offer a plausible bridge from reinforcement-learning theory to entorhinal-hippocampal navigation codes. The case is strongest for behavior and computation, not for a literal neural identification of grid cells with the classic successor representation (SR). Pure SR explains reward revaluation and some navigation regularities, but its policy dependence and weak handling of transition/policy change sit uneasily with geometry-anchored, often rapidly established entorhinal maps. That tension has pushed the field toward hybrid accounts: SR plus model-based computation or replay, and more policy-stable predictive maps such as linear RL’s Default Representation (DR).

## Current view

A predictive-map account is now a serious middle ground between model-free habits and full online planning. In this view, cached multi-step state predictions support fast value recomputation when rewards change, yielding flexible behavior without requiring exhaustive tree search on every choice [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

For navigation, the behavioral case is fairly strong. Humans in sequential decision tasks show the hallmark SR asymmetry: better adaptation to reward revaluation than to transition or policy revaluation, with slower responding when transition structure must be updated [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]]. In dynamic spatial mazes, both rats and humans are better described by SR-like agents than by pure model-free or pure model-based agents, although humans show more model-based signatures early in learning [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]].

For grid cells, the live debate is not whether predictive coding matters, but which predictive map is neurally plausible. Classic SR is attractive because its eigenvectors can generate grid-like bases, but it is policy-dependent. That is a problem if entorhinal grid fields are relatively stable across policy changes and more sensitive to environmental geometry or barriers. Linear RL’s DR was proposed partly to solve this mismatch by providing a policy-independent map that still supports replanning and yields grid- and border-like basis functions [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] [[raw/summaries/piray2021_linear_reinforcement_planning|Piray et al. 2021]].

Overall, the field is past the simple “grid cells = Euclidean metric” view, but it is not yet at a consensus “grid cells = SR” view either. The more defensible position is that entorhinal codes participate in predictive spatial representations, with the exact computational form still unsettled.

## Strongest evidence

- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]]
  - Cleanest behavioral signature of SR-like decision-making in humans.
  - Reward revaluation exceeded transition revaluation in experiment 1 (mean revaluation scores 0.52 vs 0.45; reward > transition, t₅₇ = 2.89, P = 0.016).
  - In experiment 2, switching was higher for reward revaluation (0.66) than for transition (0.47) or policy revaluation (0.50), with transition and policy revaluation not differing.
  - Transition revaluation was slower, and better transition performance correlated with longer response times, consistent with extra computation beyond cached SR.
  - A hybrid SR–model-based account fit the asymmetry better than pure SR, pure model-based, or pure model-free accounts.

- [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]]
  - Strong cross-species navigation evidence in a shared open-field modular maze.
  - Human and rat occupancy patterns correlated strongly overall (r = 0.67).
  - Across likelihood, difficulty-ranking, and trajectory-shape analyses, SR agents best matched both species.
  - SR was the maximum-likelihood model on 70% of human trials and 60% of rat trials.
  - Important nuance: humans showed more model-based behavior early in trials/configurations, so the result is not “navigation is purely SR.”

- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]]
  - The key computational decomposition.
  - SR-TD explains reward revaluation but fails on transition revaluation.
  - SR-MB handles reward and transition revaluation by recomputing from a one-step model, but fails on policy revaluation.
  - SR-Dyna can recover all three with enough replay.
  - This paper matters because it turns vague “model-based/model-free” mixtures into testable predictive-map variants.

- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] [[raw/summaries/piray2021_linear_reinforcement_planning|Piray et al. 2021]]
  - Strongest theoretical attempt to reconcile predictive maps with grid-field phenomenology.
  - DR supports one-shot reward revaluation, policy revaluation, and efficient detour updates.
  - Eigenvectors of DR produce periodic multiscale patterns resembling grid fields.
  - Barrier effects are handled by low-rank updates, yielding border-like correction terms.
  - The central claim is that a policy-stable predictive map fits entorhinal phenomena better than classic policy-bound SR.

- [[raw/summaries/whitlock2012_functional_parietal_entorhinal|Whitlock et al. 2012]]
  - Useful physiological constraint on theory.
  - Posterior parietal cortex tracked self-motion/action states, whereas medial entorhinal grid cells maintained spatial maps determined by environmental cues.
  - This supports the idea that entorhinal maps are not just action-policy summaries.

## Landmark papers

- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]]
  - Established the modern predictive-representation framework and the critical distinction between reward, transition, and policy revaluation.

- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]]
  - First strong human behavioral evidence that SR-like representations contribute to choice.

- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] / [[raw/summaries/piray2021_linear_reinforcement_planning|Piray et al. 2021]]
  - Reframed the grid-cell link: from classic SR to a more policy-invariant predictive map compatible with flexible replanning.

- [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]]
  - Showed that SR-like structure scales from abstract sequential tasks to naturalistic spatial navigation in both humans and rats.

## Boundaries and tensions

Pure SR is too weak for the full navigation problem. It naturally explains reward revaluation, but by construction it struggles when transition structure or the policy itself changes unless replay or extra model-based computation is added [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]].

That matters for detours and shortcuts. Real navigation often requires exactly the sort of transition updating that classic SR misses. de Cothi et al. still found SR-like behavior in dynamic mazes, but humans retained an early model-based component, which is what one would expect if SR is only part of the solution [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]].

The grid-cell link is suggestive rather than settled. The appeal of SR-based grid theories is mathematical: predictive-map eigenvectors can look grid-like. But the main objection is conceptual and empirical: grid fields often appear more tied to environmental geometry than to the animal’s currently optimized policy. That is exactly why DR/linear RL was introduced as a better candidate than classic SR for entorhinal maps [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] [[raw/summaries/piray2021_linear_reinforcement_planning|Piray et al. 2021]].

There is also tension between learned predictive-map theories and fast map formation. [[raw/summaries/wen2024_entorhinal_maps_flexible_navigation|Wen et al. 2024]] argues that grid-cell maps in novel environments can stabilize after a single exposure through fixed landmark-to-attractor connectivity, with flexibility delegated downstream. If that result generalizes, it weakens any account in which entorhinal predictive maps require slow SR-like learning alone.

Relatedly, entorhinal activity can support endogenous, non-perceptual spatial reconstruction. [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]] found periodic entorhinal activity during mental navigation in monkeys. This supports internal map dynamics, but it does not discriminate cleanly between SR, DR, and attractor accounts.

Finally, the neural locus of predictive maps is unresolved. The provided literature implicates hippocampus, prefrontal cortex, orbitofrontal/vmPFC, striatum, and entorhinal cortex. Current evidence supports a distributed system more than a single-site implementation.

## Open questions

- Do medial entorhinal grid cells encode a classic SR, a DR-like map, an attractor-based geometry map, or a mixture that depends on task demands?

- How are predictive maps updated in practice?
  - online temporal-difference learning,
  - offline replay,
  - one-shot landmark anchoring,
  - or some combination?

- When humans face detours or changing policies, what determines the shift between cached predictive maps and explicit model-based planning? The early-versus-late dissociation in [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]] suggests resource-sensitive arbitration, but the mechanism is not settled.

- Can the same framework explain both stable spatial codes and flexible goal coding? [[raw/summaries/huang2024_hippocampal_theta_goal_distance|Huang et al. 2024]] shows hippocampal theta tracks goal distance during planning and navigation, which is clearly relevant to predictive navigation, but not specifically diagnostic of SR versus DR.

- How well do current predictive-map theories handle stochastic, partially observable, and continuous environments? This remains a major limitation for both classic SR and current linear-RL formulations [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]].

- What is replay doing computationally in navigation? [[raw/summaries/eldar2020_replay_planning|Eldar et al. 2020]] links online replay to model-based flexibility and offline replay to more rigid policies, which is relevant to SR-Dyna-style accounts, but the mapping to spatial predictive maps is still indirect.

## Key papers

- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]] — strongest human behavioral evidence for SR-like revaluation asymmetries.

- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] — core computational framework linking SR, model-based behavior, replay, and diagnostic task signatures.

- [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]] — cross-species navigation study showing SR-like behavior in humans and rats.

- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] — introduces DR/linear RL as a policy-stable predictive map with grid and border field implications.

- [[raw/summaries/piray2021_linear_reinforcement_planning|Piray et al. 2021]] — expanded formulation emphasizing planning, cognitive control, and grid-field consequences.

- [[raw/summaries/whitlock2012_functional_parietal_entorhinal|Whitlock et al. 2012]] — physiological evidence that entorhinal maps are more environment-anchored than action-organized.

- [[raw/summaries/wen2024_entorhinal_maps_flexible_navigation|Wen et al. 2024]] — important challenge to slow-learning-only accounts: one-shot stable entorhinal maps in novel environments.

- [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]] — entorhinal periodic activity during mental navigation, supporting endogenous map dynamics without resolving the exact computational form.

## Source papers
- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]] | [[raw/mds/momennejad2017_successor_representation_humans|source md]]: The successor representation in human reinforcement learning
- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] | [[raw/mds/russek2017_model_based_reinforcement|source md]]: Predictive representations can link model-based reinforcement learning to model-free mechanisms
- [[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]] | [[raw/mds/piray2021_linear_reinforcement_planning|source md]]: Linear reinforcement learning in planning, grid fields, and cognitive control
- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray and Daw 2020]] | [[raw/mds/piray2020_linear_reinforcement_learning|source md]]: Linear reinforcement learning: Flexible reuse of computation in planning, grid fields, and cognitive control
- [[raw/summaries/decothi2022_predictive_spatial_navigation|Cothi et al. 2022]] | [[raw/mds/decothi2022_predictive_spatial_navigation|source md]]: Predictive maps in rats and humans for spatial navigation
- [[raw/summaries/eldar2020_replay_planning|Eldar et al. 2020]] | [[raw/mds/eldar2020_replay_planning|source md]]: The roles of online and offline replay in planning
- [[raw/summaries/huang2024_hippocampal_theta_goal_distance|Huang et al. 2024]] | [[raw/mds/huang2024_hippocampal_theta_goal_distance|source md]]: Human Hippocampal Theta Oscillations Organise Distance to Goal Coding
- [[raw/summaries/martinet2011_spatial_learning_action_planning|Martinet et al. 2011]] | [[raw/mds/martinet2011_spatial_learning_action_planning|source md]]: Spatial Learning and Action Planning in a Prefrontal Cortical Network Model
- [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]] | [[raw/mds/neupane2022_mental_navigation_entorhinal_cortex|source md]]: Vector production via mental navigation in the entorhinal cortex
