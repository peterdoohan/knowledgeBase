---
title: "Successor representation as a predictive map for flexible planning"
subtopic_id: predictive_maps_and_successor_representation__02
parent_topic_id: predictive_maps_and_successor_representation
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:26:20.718687+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - russek2017_model_based_reinforcement
  - piray2021_linear_reinforcement_planning
  - wientjes2024_successor_representation
  - piray2020_linear_reinforcement_learning
  - piray2025_compositional_cognitive_map
core_papers:
  - adams_delusions_inference_attractors
  - akam2015_two_step_task_simple_plans
  - piray2020_linear_reinforcement_learning
  - piray2021_linear_reinforcement_planning
  - piray2025_compositional_cognitive_map
  - raju2022_space_sequence
  - russek2017_model_based_reinforcement
  - sagiv_experience_replay_prioritization
related_wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_prefrontal_replay_in_planning
---

# Successor representation as a predictive map for flexible planning

This page is about SR as an algorithmic account of flexible planning, not about hippocampal map physiology per se. The central claim is that SR caches predictive structure so reward changes can be handled cheaply, but that benefit comes with a real cost: vanilla SR is policy-dependent and breaks on many transition or policy changes unless it is supplemented by replay, one-step models, or alternative predictive objects such as the Default Representation in linear RL. So the strongest current view is not "SR solves planning," but "SR captures one important reuse-of-structure trick inside a broader family of planning algorithms" [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/piray2020_linear_reinforcement_learning|Piray 2020]] [[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]].

## Current view

- SR is best viewed as an intermediate algorithmic family between model-free TD learning and full model-based search, not as a clean member of either class [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

- Its key advantage is factorization: learn predictive structure once, then combine it with current rewards. This explains immediate reward revaluation without replaying the full decision tree [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

- Its key limitation is equally central: the SR is learned under a policy. Change rewards enough to alter the optimal intermediate policy, or change transitions via barriers/detours, and vanilla SR becomes wrong unless it is updated through new experience or replay [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

- Current extensions split along two routes:
  - recompute predictive structure from a learned one-step model at choice time (SR-MB) [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]];
  - or cache a different object, such as the DR in linear RL, that is less tightly coupled to the optimized policy and supports cheap replanning [[raw/summaries/piray2020_linear_reinforcement_learning|Piray 2020]], [[raw/summaries/piray2021_linear_reinforcement_planning|Piray 2021]].

- On the empirical side, the cleanest support here is behavioral: human response times and individual differences can reflect SR-like predictive structure and its induced hierarchical abstraction [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]]. But direct neural evidence that a specific region literally stores the SR remains incomplete.

## Strongest evidence

- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] provides the clearest computational dissociation.
  - SR-TD solves reward revaluation tasks, including latent learning, reward devaluation, and sensory preconditioning, without further direct experience.
  - The same algorithm fails transition revaluation/detour tasks because cached occupancies are obsolete.
  - SR-MB solves reward and transition revaluation by rebuilding the SR from a one-step model, but still fails a policy revaluation task because the SR remains policy-specific.
  - SR-Dyna can solve reward, transition, and policy revaluation if replay is sufficient; with little replay it collapses back toward SR-TD behavior.

- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray 2020]] and [[raw/summaries/piray2021_linear_reinforcement_planning|Piray 2021]] show why many “SR successes” do not amount to general flexible planning.
  - The DR is designed to be reusable across goals and less entangled with the optimized policy.
  - In simulations it handles reward revaluation, policy revaluation, and detour tasks that defeat vanilla SR.
  - It also gives explicit update rules for local transition changes, rather than requiring full recomputation.
  - This is strong as a normative/computational argument, but it is still not direct neural evidence.

- [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] supplies the strongest empirical support in this set.
  - Choice behavior was best captured by an explicit hierarchical model, but response times were best captured by an SR model.
  - Individual differences in SR modularity predicted better hierarchical choice, greater reward, and better memory for task structure.
  - The implication is not “SR explains all planning,” but that SR-like predictive structure may support abstraction that planning then exploits.

- [[raw/summaries/akam2015_two_step_task_simple_plans|Akam et al. 2015]] is important negative evidence.
  - On the two-step task, model-free strategies can mimic model-based signatures.
  - So apparent flexibility in standard sequential choice tasks is not strong evidence for SR or model-based planning by itself.
  - Revaluation tasks remain more diagnostic than generic two-step analyses.

## Landmark papers

- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]]  
  Established the modern SR taxonomy: reward revaluation as an SR strength, transition and policy revaluation as critical failure modes, and replay/model-based recomputation as possible fixes.

- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray 2020]]  
  Reframed the problem by replacing the SR with a Default Representation that is more reusable across goals and better suited to flexible replanning.

- [[raw/summaries/piray2021_linear_reinforcement_planning|Piray 2021]]  
  Consolidated the linear RL account and extended its links to grid fields, border-like corrections, and cognitive control costs.

- [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]]  
  Provided direct human behavioral evidence that SR-like predictive structure is linked to hierarchical abstraction during goal-directed behavior.

- [[raw/summaries/akam2015_two_step_task_simple_plans|Akam et al. 2015]]  
  Not an SR paper per se, but a landmark caution: standard task signatures can overstate “model-based” control and therefore overstate evidence for predictive-map accounts.

## Boundaries and tensions

- Policy dependence is not a side issue; it is the core limitation of vanilla SR.
  - Reward changes are easy when the policy can stay fixed.
  - Reward changes that should induce different intermediate choices are not easy, because the SR was learned under the old policy [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

- Transition flexibility is mixed.
  - Vanilla SR fails detours.
  - SR-MB and SR-Dyna can recover flexibility, but only by importing additional machinery: explicit one-step models or sufficient replay [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].
  - Linear RL offers a more elegant update rule, but under stronger assumptions about controllability and often deterministic structure [[raw/summaries/piray2020_linear_reinforcement_learning|Piray 2020]], [[raw/summaries/piray2021_linear_reinforcement_planning|Piray 2021]].

- “Predictive map” is not uniquely diagnostic of SR.
  - Alternative sequence-learning accounts can generate spatially organized predictive structure without positing an SR in the strict RL sense [[raw/summaries/raju2022_space_sequence|Raju et al. 2022]].
  - [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] explicitly notes that hidden Markov or related sequence-learning models could be functionally isomorphic in some settings.

- The neural division of labor remains unresolved.
  - [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] argues SR-like predictive inputs could arise from hippocampus or prefrontal cortex and be learned by dopaminergic-striatal TD mechanisms.
  - [[raw/summaries/spiers2015_detour_problem_navigation|Spiers et al. 2015]] found prefrontal responses during forced detours, with hippocampus tracking path distance rather than showing the strongest detour signal.
  - This is consistent with, but does not prove, a division where hippocampal maps are insufficient for transition revaluation without prefrontal control computations.

- Grid-cell interpretations are theoretically split.
  - SR-based accounts naturally tie map structure to policy.
  - Linear RL predicts a more policy-stable entorhinal code because the DR is not the optimized-policy SR [[raw/summaries/piray2020_linear_reinforcement_learning|Piray 2020]], [[raw/summaries/piray2021_linear_reinforcement_planning|Piray 2021]].
  - In this evidence set, that remains a modeling argument more than a settled empirical result.

- Hierarchy and compositionality look promising but are not yet settled.
  - [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] suggests SR modularity supports hierarchical abstraction.
  - [[raw/summaries/piray2025_compositional_cognitive_map|Piray 2025]] extends predictive maps compositionally and outperforms plain SR in planning simulations.
  - But these are not yet decisive evidence that biological planning uses these exact representations.

## Open questions

- When does the brain use cached SR-like predictions, when does it rebuild from a one-step model, and when does it rely on replay-mediated updates?

- How is replay prioritized when future goals are unknown? This is central if replay is what turns SR from reward-revaluation competence into broader planning competence [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

- Can SR-like accounts handle hidden states, partial observability, and latent causes without collapsing into broader latent-state inference frameworks?

- Are hippocampal and entorhinal population codes closer to a policy-dependent SR, a default-policy DR, or a more general sequence model [[raw/summaries/raju2022_space_sequence|Raju et al. 2022]], [[raw/summaries/piray2020_linear_reinforcement_learning|Piray 2020]]?

- What are the best behavioral assays for SR specifically? Two-step tasks are often underconstrained [[raw/summaries/akam2015_two_step_task_simple_plans|Akam et al. 2015]]; revaluation tasks are better, but more real-world tests are needed.

- How does predictive structure become hierarchical or compositional?
  - Human behavior suggests a link between SR modularity and abstraction [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]].
  - Compositional extensions are promising but mostly theoretical so far [[raw/summaries/piray2025_compositional_cognitive_map|Piray 2025]].

- Which brain regions implement which parts of the computation: predictive map storage, TD-style learning, replay, subgoal generation, and detour-specific replanning?

## Key papers

- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] — Core statement of SR as a bridge from model-free TD mechanisms to model-like flexibility; defines the reward/transition/policy revaluation dissociations.

- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray 2020]] — Introduces linear RL and the Default Representation as a policy-relaxed alternative to SR for flexible replanning.

- [[raw/summaries/piray2021_linear_reinforcement_planning|Piray 2021]] — Expanded linear RL account linking planning, grid-like codes, border-like corrections, and control costs.

- [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] — Human behavioral evidence that SR-like predictive structure supports hierarchical abstraction in goal-directed behavior.

- [[raw/summaries/akam2015_two_step_task_simple_plans|Akam et al. 2015]] — Essential caution that apparent model-based signatures on the two-step task need not reflect genuine model-based or SR-based planning.

- [[raw/summaries/spiers2015_detour_problem_navigation|Spiers et al. 2015]] — Convergent evidence that detour behavior recruits prefrontal computations, relevant to SR’s weakness on transition revaluation.

- [[raw/summaries/piray2025_compositional_cognitive_map|Piray 2025]] — Speculative but important extension of predictive-map planning toward compositional object- and barrier-sensitive maps.

## Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]: Crosslink on 'successor representation as the computational formalism behind hippocampal predictive-map hypotheses' and on 'replay/one-step model mechanisms that address vanilla SR limits in planning and neural implementation.'
- [[wiki/topics/hippocampal_prefrontal_replay_in_planning|Hippocampal–prefrontal replay in planning]]: Crosslink on replay as a possible implementation or complement to SR/predictive maps: Page A can point to SR/linear-RL as theories of what replay may compute, while Page B can point to hippocampal–prefrontal replay as candidate neural circuitry for predictive-map-based planning.

## Source papers
- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] | [[raw/mds/russek2017_model_based_reinforcement|source md]]: Predictive representations can link model-based reinforcement learning to model-free mechanisms
- [[raw/summaries/piray2021_linear_reinforcement_planning|Piray and Daw 2021]] | [[raw/mds/piray2021_linear_reinforcement_planning|source md]]: Linear reinforcement learning in planning, grid fields, and cognitive control
- [[raw/summaries/wientjes2024_successor_representation|Wientjes and Holroyd 2024]] | [[raw/mds/wientjes2024_successor_representation|source md]]: The successor representation subserves hierarchical abstraction for goal-directed behavior
- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray and Daw 2020]] | [[raw/mds/piray2020_linear_reinforcement_learning|source md]]: Linear reinforcement learning: Flexible reuse of computation in planning, grid fields, and cognitive control
- [[raw/summaries/piray2025_compositional_cognitive_map|Piray and Daw 2025]] | [[raw/mds/piray2025_compositional_cognitive_map|source md]]: Reconciling flexibility and efficiency: medial entorhinal cortex represents a compositional cognitive map
- [[raw/summaries/adams_delusions_inference_attractors|Adams et al. 2021]] | [[raw/mds/adams_delusions_inference_attractors|source md]]: Everything is connected: Inference and attractors in delusions
- [[raw/summaries/akam2015_two_step_task_simple_plans|Akam et al. 2015]] | [[raw/mds/akam2015_two_step_task_simple_plans|source md]]: Simple Plans or Sophisticated Habits? State, Transition and Learning Interactions in the Two-Step Task
- [[raw/summaries/raju2022_space_sequence|Raju et al. 2022]] | [[raw/mds/raju2022_space_sequence|source md]]: Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus
- [[raw/summaries/sagiv_experience_replay_prioritization|Sagiv et al. unknown]] | [[raw/mds/sagiv_experience_replay_prioritization|source md]]: Prioritizing experience replay when future goals are unknown
