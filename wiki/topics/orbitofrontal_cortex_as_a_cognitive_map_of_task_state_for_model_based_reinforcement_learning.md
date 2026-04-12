---
title: "Orbitofrontal cortex as a cognitive map of task state for model-based reinforcement learning"
subtopic_id: ofc_task_state_and_value_maps__01
parent_topic_id: ofc_task_state_and_value_maps
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:48:10.915631+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - daw2005_uncertainty_prefrontal_striatal
  - wilson2013_ofc_cognitive_map
  - daw2011_model_based_striatal_prediction
  - momennejad2017_successor_representation_humans
  - niv2019_representation_learning_task_states
core_papers:
  - bein2024_schemas_reinforcement_learning_pfc
  - botvinick2009_hierarchical_behavior_reinforcement
  - botvinick2009_hierarchically_organized_behavior
  - brown2016_prospective_goals_hippocampus
  - corbit2018_goal_directed_habitual
  - dahmani2015_prefrontal_navigation_strategies
  - daw2005_uncertainty_prefrontal_striatal
  - daw2011_model_based_striatal_prediction
---

# Orbitofrontal cortex as a cognitive map of task state for model-based reinforcement learning

A strong but still incomplete account is that orbitofrontal cortex (OFC) helps represent the current latent task state when stimuli alone do not specify what situation the agent is in. On this view, OFC is not the whole model-based controller and not just a generic value area; it supplies a compact state code that supports flexible valuation, devaluation-sensitive choice, reversal, and planning in a broader hippocampal-prefrontal-striatal circuit. The main support is convergent rather than decisive: computational unification of lesion findings, causal necessity for some flexible learning, and evidence that model-based information reaches striatal/vmPFC valuation systems. Direct proof that OFC uniquely implements a task-state map, as opposed to mixed state/value coding, remains limited.

## Current view

The most defensible version of the hypothesis is narrower than “OFC does model-based RL.”

OFC is proposed to represent task states that are partially observable, memory-dependent, or inferred from latent causes, allowing the same sensory input to map onto different actions or outcomes depending on recent history or context [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] [[raw/summaries/niv2019_representation_learning_task_states|Niv et al. 2019]].

This state-representation role can support both model-based and model-free learning. Model-based algorithms need state identity and transition structure explicitly, but even cached reinforcement-learning systems fail if the state space is wrongly specified [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]]. So OFC’s contribution may be upstream of the model-based/model-free divide.

The account is now usually framed as distributed. Hippocampus is a plausible source of relational or transition structure; OFC may provide a task-relevant “pointer” to the current latent state; striatum and vmPFC/medial prefrontal cortex use these representations for prediction-error learning and valuation [[raw/summaries/daw2011_model_based_striatal_prediction|Daw et al. 2011]] [[raw/summaries/niv2019_representation_learning_task_states|Niv et al. 2019]] [[raw/summaries/knudsen2022_ofc_cognitive_map|Knudsen et al. 2022]].

A key shift is that the old value-vs-map debate has softened. A plausible reconciliation is that OFC carries value signals because value is attached to positions in an internal task graph, not because OFC is only a scalar value comparator [[raw/summaries/knudsen2022_ofc_cognitive_map|Knudsen et al. 2022]].

## Strongest evidence

- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] is the core synthesis. Its two-state vs single-state models reproduce several classic OFC lesion effects:
  - rapid vs slowed reversal learning,
  - successful vs chance delayed alternation,
  - faster vs slower extinction,
  - preserved vs impaired devaluation sensitivity.
  
  The critical move is not altered reward learning per se, but loss of the hidden-state representation that distinguishes superficially similar situations.

- [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] provides the normative reinforcement-learning backdrop. It formalizes why a prefrontal “tree-search” controller should dominate early or when action-outcome structure matters, while a striatal cache wins with extensive training and shallow demands. This paper does not localize the function to OFC, but it makes clear why prefrontal state/model representations should matter for goal-directed control.

- [[raw/summaries/daw2011_model_based_striatal_prediction|Daw et al. 2011]] shows that in humans, choices in the two-step task are best fit by a hybrid model-based/model-free strategy, and ventral striatal prediction-error signals contain a model-based component that tracks behavior. This is not OFC-specific evidence, but it strongly implies that model-based state/transition information reaches downstream valuation machinery rather than remaining isolated in cortex.

- [[raw/summaries/niv2019_representation_learning_task_states|Niv et al. 2019]] sharpens the computational problem: the brain must learn task states by selective attention and latent-cause inference. The paper places OFC as a candidate locus for these abstract task-state representations, which is a better-specified claim than “OFC encodes value.”

- [[raw/summaries/knudsen2020_ofc_theta_learning|Knudsen et al. 2020]] adds causal circuit evidence. Disrupting OFC theta in macaques impairs reward-based learning, and the oscillation is driven by hippocampal input. This supports an OFC–hippocampal interaction relevant to flexible learning, though it does not by itself prove latent-state coding.

Taken together, the best-supported claim is that OFC is important when behavior depends on representing hidden or abstract task states, especially under revaluation, reversal, and partial observability. The weaker claim is that OFC alone computes full-blown model-based planning.

## Landmark papers

- [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]]  
  Established the modern arbitration framework between model-based prefrontal control and model-free striatal caching.

- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]]  
  Canonical statement of the OFC “cognitive map of task space” hypothesis, with lesion-grounded simulations across multiple paradigms.

- [[raw/summaries/daw2011_model_based_striatal_prediction|Daw et al. 2011]]  
  Made the two-step task a major assay of model-based choice and showed that striatal prediction errors already incorporate model-based information.

- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]]  
  Important corrective: flexible behavior in sequential tasks is not well captured by a pure online-planning account; a hybrid successor-representation/model-based algorithm fits better.

- [[raw/summaries/niv2019_representation_learning_task_states|Niv et al. 2019]]  
  Reframed the problem from “which RL controller?” to “how are task states learned at all?”

## Boundaries and tensions

The strongest tension is between state-map and value accounts of OFC. The literature does not cleanly support either extreme. OFC often carries value-related signals, but value coding alone does not explain hidden-state-dependent deficits; conversely, a pure state-map account may underplay robust value correlates. A mixed state-with-value-on-graph view is currently the least forced synthesis [[raw/summaries/knudsen2022_ofc_cognitive_map|Knudsen et al. 2022]].

“Model-based” is also too coarse. Human revaluation behavior is often asymmetric: people are more sensitive to reward revaluation than transition revaluation, consistent with a hybrid successor representation (SR) plus model-based computation rather than pure tree search [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]]. If OFC supports predictive maps, those maps may sometimes be cached multi-step expectations rather than explicit online search.

Task sensitivity is another problem. Simple two-step paradigms may underdetect ventromedial/orbitofrontal contributions. vmPFC lesions can spare performance on the standard two-step task while impairing richer planning tasks that require deeper search and better feature selection [[raw/summaries/holton2023_planning_vmPFC_lesions|Holton et al. 2023]]. Negative findings in stripped-down tasks should therefore be interpreted cautiously.

Localization remains unsettled. The original cognitive-map account is often thought to fit lateral OFC better than medial OFC/vmPFC, but many human studies blur these regions anatomically and functionally [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] [[raw/summaries/knudsen2022_ofc_cognitive_map|Knudsen et al. 2022]].

Finally, the network is broader than OFC. Meta-analytic and task-fMRI work implicates ventral striatum, vmPFC/anterior cingulate, and hippocampus alongside OFC [[raw/summaries/daw2011_model_based_striatal_prediction|Daw et al. 2011]] [[raw/summaries/huang2020_model_based_model_free_neural|Huang et al. 2020]]. An OFC-centered story is useful, but an OFC-exclusive story is not.

## Open questions

- What exactly is coded in OFC: current latent state, state value, transition structure, policy, or a multiplexed combination?
- How are task-state representations learned online, not just expressed after learning? Selective attention and latent-cause inference are plausible algorithms, but the neural mechanism is unclear [[raw/summaries/niv2019_representation_learning_task_states|Niv et al. 2019]].
- How is labor divided between hippocampus and OFC? One plausible split is relational graph structure in hippocampus and current state identity/value readout in OFC, but direct evidence is still thin.
- When is OFC necessary for flexible choice? Reversal, devaluation, delayed alternation, and some planning tasks point to partial observability and hidden-state demands, but boundary conditions are not sharply mapped.
- Are apparent model-based signals in OFC truly planning-related, or do they reflect SR-like predictive maps?
- How different are lateral OFC, medial OFC, and vmPFC in these computations?
- Can causal perturbation isolate state inference from value updating and search depth in the same task?

## Key papers

- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] — Core OFC-as-task-state-map theory; explains classic lesion effects via hidden-state loss.
- [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] — Normative framework for arbitration between model-based prefrontal and model-free striatal control.
- [[raw/summaries/daw2011_model_based_striatal_prediction|Daw et al. 2011]] — Human behavioral and striatal evidence that model-based information enters prediction-error computations.
- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]] — Strong evidence that flexible sequential choice is often SR–MB hybrid, not pure model-based planning.
- [[raw/summaries/niv2019_representation_learning_task_states|Niv et al. 2019]] — Best computational framing of how abstract task states may be learned and why OFC is a candidate substrate.
- [[raw/summaries/knudsen2022_ofc_cognitive_map|Knudsen et al. 2022]] — Useful critical review reconciling value and cognitive-map accounts of OFC.
- [[raw/summaries/knudsen2020_ofc_theta_learning|Knudsen et al. 2020]] — Causal evidence that OFC, in interaction with hippocampal input, is necessary for reward-based learning.
- [[raw/summaries/holton2023_planning_vmPFC_lesions|Holton et al. 2023]] — Important caution that simple laboratory assays may miss prefrontal contributions to richer planning.

## Source papers
- [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] | [[raw/mds/daw2005_uncertainty_prefrontal_striatal|source md]]: Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control
- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] | [[raw/mds/wilson2013_ofc_cognitive_map|source md]]: Orbitofrontal Cortex as a Cognitive Map of Task Space
- [[raw/summaries/daw2011_model_based_striatal_prediction|Daw et al. 2011]] | [[raw/mds/daw2011_model_based_striatal_prediction|source md]]: Model-Based Influences on Humans' Choices and Striatal Prediction Errors
- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]] | [[raw/mds/momennejad2017_successor_representation_humans|source md]]: The successor representation in human reinforcement learning
- [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]] | [[raw/mds/niv2019_representation_learning_task_states|source md]]: Learning task-state representations
- [[raw/summaries/bein2024_schemas_reinforcement_learning_pfc|Bein and Niv 2024]] | [[raw/mds/bein2024_schemas_reinforcement_learning_pfc|source md]]: Schemas, reinforcement learning, and the medial prefrontal cortex
- [[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]] | [[raw/mds/botvinick2009_hierarchical_behavior_reinforcement|source md]]: Hierarchically organized behavior and its neural foundations: A reinforcement-learning perspective
- [[raw/summaries/botvinick2009_hierarchically_organized_behavior|Botvinick et al. 2009]] | [[raw/mds/botvinick2009_hierarchically_organized_behavior|source md]]: Hierarchically organized behavior and its neural foundations: A reinforcement-learning perspective
- [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] | [[raw/mds/brown2016_prospective_goals_hippocampus|source md]]: Prospective representation of navigational goals in the human hippocampus
- [[raw/summaries/corbit2018_goal_directed_habitual|Corbit 2018]] | [[raw/mds/corbit2018_goal_directed_habitual|source md]]: Understanding the balance between goal-directed and habitual behavioral control
- [[raw/summaries/dahmani2015_prefrontal_navigation_strategies|Dahmani and Bohbot 2015]] | [[raw/mds/dahmani2015_prefrontal_navigation_strategies|source md]]: Dissociable contributions of the prefrontal cortex to hippocampus- and caudate nucleus-dependent virtual navigation strategies
