---
title: "Successor representation and hierarchical planning in navigation"
subtopic_id: behavioral_paradigms_and_navigation_tasks__04
parent_topic_id: behavioral_paradigms_and_navigation_tasks
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:47:34.899195+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - dayan1993_successor_representation
  - wientjes2024_successor_representation
  - tomov2020_hierarchical_planning_representation
  - brunec2022_predictive_representations_hierarchies
  - alonso2021_hexmaze_cognitive_map
core_papers:
  - alonso2021_hexmaze_cognitive_map
  - balaguer2016_hierarchical_planning_subway
  - brunec2022_predictive_representations_hierarchies
  - coutrot2022_entropy_street_navigation
  - dayan1993_successor_representation
  - jensen2024_recurrent_planning_hippocampal_replay
  - kim2026_hippocampus_smallworld
  - olson2020_secondary_motor_cortex_navigation
---

# Successor representation and hierarchical planning in navigation

A working synthesis is that successor-like predictive maps can compress navigation problems into multiscale expectations over future states, and this compression may be one route to hierarchical planning. The strongest case is not that SR alone explains hierarchy, but that SR-like predictive structure, Bayesian/graph-based hierarchy discovery, and prefrontal control signals are partially complementary. Human behavior and fMRI support a predictive-map hierarchy spanning hippocampus and prefrontal cortex, but direct causal evidence that these signals implement SR-based hierarchical planning in navigation remains limited.

## Current view

The successor representation (SR) provides an attractive middle ground between model-free caching and full model-based search: it stores discounted future occupancy under a policy, so values can be recomputed quickly when rewards change without relearning the entire transition structure [[raw/summaries/dayan1993_successor_representation|Dayan 1993]].

For navigation, the key hierarchical idea is multiscale prediction. Short-horizon predictive structure can support local action choice, while longer-horizon predictive structure can expose bottlenecks, communities, or subgoals that are useful for coarse planning. This view is broadly consistent with predictive-horizon gradients across hippocampus and prefrontal cortex during naturalistic navigation [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]].

Behaviorally, the cleanest recent claim is that humans appear to use both a detailed predictive representation and a coarser hierarchical abstraction in the same task. In that account, SR-like structure tracks fine-grained state predictions, while choices can follow a simpler community- or wing-level policy [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]].

But the field should stay careful. Evidence for hierarchy discovery in navigation does not uniquely implicate SR. Bayesian structure-learning accounts can derive similar cluster, bottleneck, and subgoal phenomena without committing to SR as the algorithmic substrate [[raw/summaries/tomov2020_hierarchical_planning_representation|Tomov et al. 2020]]. Likewise, dmPFC signals during virtual subway planning clearly track hierarchical plan cost, but they do not by themselves identify SR-based computation [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]].

## Strongest evidence

[[raw/summaries/dayan1993_successor_representation|Dayan 1993]] is still foundational because it formalizes why SR is useful in navigation-like tasks. It generalizes across states that share future trajectories rather than mere spatial proximity, and it respects barriers in a way naive spatial generalization does not. That is directly relevant to maze navigation, where Euclidean closeness can be misleading.

[[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] provides the strongest behavioral bridge from SR to hierarchical abstraction. Their main dissociation matters:
- explicit hierarchical models fit choice best
- SR-based models fit response times best
- individual differences in SR modularity predict better hierarchical choices, reward, and memory for task layout

That pattern supports a hybrid view: predictive structure may be the substrate from which hierarchical abstractions are extracted, even if overt decisions are made over a coarser representation.

[[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] gives the best neural evidence for multiscale predictive representations during navigation. Representational similarity scaled with future-state occupancy over multiple horizons, with short horizons in posterior hippocampus and much longer horizons in anterior PFC. This is highly compatible with multiscale SR accounts and with the idea that hierarchical planning relies on progressively larger predictive scales.

[[raw/summaries/tomov2020_hierarchical_planning_representation|Tomov et al. 2020]] is strong on the computational side. It shows that hierarchy can be inferred from topology, task distribution, and reward structure, and that such learned clusters bias planning in ways seen in human navigation tasks. This does not prove SR, but it clarifies what any SR-based account must explain: hierarchy is shaped not just by graph topology, but by what goals and rewards the agent repeatedly encounters.

Two additional papers sharpen the boundaries of the claim. [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]] shows that dmPFC/premotor cortex track hierarchical planning cost in a virtual navigation setting, supporting prefrontal involvement in abstract route control. [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]] shows that navigation behavior in mice becomes progressively more schema-like and rapidly updateable over weeks, consistent with the idea that reusable structured maps emerge over time, though SR itself was not tested.

## Landmark papers

[[raw/summaries/dayan1993_successor_representation|Dayan 1993]]
- Introduced SR as discounted future occupancy.
- Established the central computational tradeoff: efficient transfer across reward changes, but policy dependence under transition/policy change.

[[raw/summaries/tomov2020_hierarchical_planning_representation|Tomov et al. 2020]]
- Reframed hierarchy discovery as Bayesian structure learning over graphs, tasks, and rewards.
- Important because it offers a serious alternative/complement to SR-only stories.

[[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]]
- Put multiscale predictive representations onto an anatomical gradient from hippocampus to anterior PFC in real-world virtual navigation.
- Strongest current neural evidence for a predictive hierarchy relevant to navigation planning.

[[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]]
- Most direct empirical argument that SR supports hierarchical abstraction in humans.
- Especially important for the dual-process claim: detailed predictive representation plus coarse hierarchical control.

[[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]]
- Landmark for hierarchical planning in a navigation task, even though it is not an SR paper.
- Shows that abstract route decomposition has measurable prefrontal costs/signals.

## Boundaries and tensions

SR is policy-dependent. That is its classic strength/weakness tradeoff: it transfers well when rewards move over a stable transition graph, but can become maladaptive when the policy or transition structure changes substantially [[raw/summaries/dayan1993_successor_representation|Dayan 1993]]. Hierarchical navigation often requires exactly those changes.

Neural “SR-like” findings are not unique identification. The fMRI similarity results in [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] are strongly consistent with predictive maps, but RSA over future-weighted similarity cannot by itself rule out other sequence-learning or latent-state models.

Hierarchy may not come from SR alone. [[raw/summaries/tomov2020_hierarchical_planning_representation|Tomov et al. 2020]] shows that topology, task frequencies, and rewards can induce clusters and subgoals through Bayesian inference. In practice, hierarchy discovery may require structure learning over and above predictive occupancy coding.

Choice and latency can dissociate. In [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]], hierarchical models best explain choices, whereas SR explains response times. That argues against a simple one-level mapping from SR to decision policy. Predictive maps may support deliberation, segmentation, or state access without being the sole driver of final choice.

Prefrontal hierarchy signals do not specify algorithm. dmPFC signals for line changes or context transitions in subway navigation show abstract planning costs [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]], but they are compatible with multiple computational accounts: options, latent-state inference, graph search over clusters, or SR-derived abstractions.

Animal navigation paradigms show structured map learning, but mechanistic resolution is still weak. The HexMaze results imply gradual formation of reusable knowledge and rapid barrier updating [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]], yet without neural recordings or model comparison they do not adjudicate between SR, schema, model-based graph search, or replay-based consolidation accounts.

## Open questions

How is hierarchical abstraction extracted from predictive maps?
- Is hierarchy read out from SR modularity/community structure, or inferred by a separate clustering process?
- [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] supports the first idea; [[raw/summaries/tomov2020_hierarchical_planning_representation|Tomov et al. 2020]] suggests the second may be necessary.

What neural circuit implements multiscale predictive planning?
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] supports a hippocampal-to-anterior PFC gradient, but causal perturbation evidence is missing.
- It remains unclear whether hippocampus computes SR-like predictions, PFC extracts hierarchical chunks, or both jointly maintain different planning scales.

How robust is SR under navigation-relevant transition changes?
- Barriers, detours, and shortcut discovery are central to real navigation.
- SR predicts partial flexibility, but strong policy/transition changes should expose its limits [[raw/summaries/dayan1993_successor_representation|Dayan 1993]].
- The field still lacks decisive experiments pitting SR against full graph-model and latent-state hierarchy accounts under systematic transition manipulations.

What is the relation between offline consolidation and hierarchical map formation?
- The time-dependent map improvement in [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]] suggests offline processes matter.
- A plausible but still unproven link is that replay/consolidation builds long-horizon predictive structure that later supports abstraction and subgoal selection.

Do planning-time dynamics require explicit search beyond SR?
- Multiscale predictive representations may reduce the search space, but difficult navigation likely still requires rollout or recurrent deliberation.
- This is where replay/planning models may complement SR rather than compete with it, though the direct evidence here is not yet specific to hierarchical navigation [[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]].

## Key papers

- [[raw/summaries/dayan1993_successor_representation|Dayan 1993]] — canonical SR theory; still the core computational reference.
- [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] — strongest direct behavioral evidence linking SR structure to hierarchical abstraction.
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] — best neural evidence for multiscale predictive horizons across hippocampus and PFC during navigation.
- [[raw/summaries/tomov2020_hierarchical_planning_representation|Tomov et al. 2020]] — essential alternative/complement: hierarchy as learned latent graph structure from topology, tasks, and rewards.
- [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]] — key navigation evidence that prefrontal cortex tracks hierarchical plan structure.
- [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]] — useful animal paradigm showing gradual emergence and rapid updating of structured spatial knowledge, but not yet a direct SR test.

## Source papers
- [[raw/summaries/dayan1993_successor_representation|Dayan 1993]] | [[raw/mds/dayan1993_successor_representation|source md]]: Improving Generalisation for Temporal Difference Learning: The Successor Representation
- [[raw/summaries/wientjes2024_successor_representation|Wientjes and Holroyd 2024]] | [[raw/mds/wientjes2024_successor_representation|source md]]: The successor representation subserves hierarchical abstraction for goal-directed behavior
- [[raw/summaries/tomov2020_hierarchical_planning_representation|Tomov et al. 2020]] | [[raw/mds/tomov2020_hierarchical_planning_representation|source md]]: Discovery of hierarchical representations for efficient planning
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec and Momennejad 2022]] | [[raw/mds/brunec2022_predictive_representations_hierarchies|source md]]: Predictive Representations in Hippocampal and Prefrontal Hierarchies
- [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]] | [[raw/mds/alonso2021_hexmaze_cognitive_map|source md]]: The HexMaze: A Previous Knowledge Task on Map Learning for Mice
- [[raw/summaries/balaguer2016_hierarchical_planning_subway|Balaguer et al. 2016]] | [[raw/mds/balaguer2016_hierarchical_planning_subway|source md]]: Neural Mechanisms of Hierarchical Planning in a Virtual Subway Network
- [[raw/summaries/coutrot2022_entropy_street_navigation|Coutrot et al. 2022]] | [[raw/mds/coutrot2022_entropy_street_navigation|source md]]: Entropy of city street networks linked to future spatial navigation ability
- [[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]] | [[raw/mds/jensen2024_recurrent_planning_hippocampal_replay|source md]]: A recurrent network model of planning explains hippocampal replay and human behavior
- [[raw/summaries/kim2026_hippocampus_smallworld|Kim et al. 2026]] | [[raw/mds/kim2026_hippocampus_smallworld|source md]]: The hippocampus as a small-world cognitive map
- [[raw/summaries/olson2020_secondary_motor_cortex_navigation|Olson et al. 2020]] | [[raw/mds/olson2020_secondary_motor_cortex_navigation|source md]]: Secondary Motor Cortex Transforms Spatial Information into Planned Action during Navigation
