---
title: "Medial prefrontal cortex in rat goal-directed vs habitual control"
subtopic_id: prefrontal_goal_representation_and_control__02
parent_topic_id: prefrontal_goal_representation_and_control
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:48:53.115398+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - russek2017_model_based_reinforcement
  - coutureau2003_infralimbic_prefrontal_goal
  - ostlund2005_prefrontal_cortex_habits
  - piray2020_linear_reinforcement_learning
  - corbit2018_goal_directed_habitual
core_papers:
  - anastasiades2021_circuit_medial_prefrontal
  - botvinick2009_hierarchically_organized_behavior
  - corbit2018_goal_directed_habitual
  - coutureau2003_infralimbic_prefrontal_goal
  - dolan2013_goals_habits_brain_b
  - gabriel2022_behaviordepot_detection
  - hok2005_goal_coding_prefrontal
  - holton2023_planning_vmPFC_lesions
---

# Medial prefrontal cortex in rat goal-directed vs habitual control

Rat medial prefrontal cortex (mPFC) is best understood here as a set of dissociable control nodes, not a single “planning” module. The strongest lesion/inactivation data support a functional split: dorsal mPFC/prelimbic-heavy lesions impair the acquisition of action–outcome control, while infralimbic (IL) activity promotes the expression of habits after overtraining and can suppress intact devaluation-sensitive responding. The core evidence comes from outcome devaluation assays, so claims should stay narrow: these studies bear directly on value-sensitive instrumental control, not on all forms of planning or model-based computation.

## Current view

The most defensible summary is:

- mPFC is involved in establishing goal-directed action control during learning, but is not the permanent storage site for action–outcome knowledge, based on the pretraining vs posttraining lesion dissociation in [[raw/summaries/ostlund2005_prefrontal_cortex_habits|Ostlund et al. 2005]].
- IL contributes to the expression of habits after extended training; silencing IL after habits are established can reinstate devaluation sensitivity, implying that goal-directed information can survive beneath habitual performance [[raw/summaries/coutureau2003_infralimbic_prefrontal_goal|Coutureau and Killcross 2003]].
- This supports a competitive or gating view rather than a simple memory-loss view of habit formation: overtraining does not necessarily erase action–outcome representations.
- At the circuit level, the field often aligns dorsal mPFC/prelimbic with goal-directed corticostriatal control and IL with habit-promoting circuitry, but the anatomical specificity is not fully clean in the classic lesion work [[raw/summaries/corbit2018_goal_directed_habitual|Corbit et al. 2018]].

A useful caution: outcome devaluation is a reward revaluation test. Computationally, success on such tasks is not uniquely diagnostic of full online model-based search; predictive representations such as the successor representation can also support reward revaluation sensitivity [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

## Strongest evidence

[[raw/summaries/ostlund2005_prefrontal_cortex_habits|Ostlund et al. 2005]] is the cleanest causal evidence for an acquisition role.

- Pretraining excitotoxic mPFC lesions abolished devaluation sensitivity.
- Posttraining lesions spared devaluation sensitivity.
- Therefore, mPFC was required to acquire goal-directed instrumental control, but not to store or later express it once learned.

This temporal dissociation is hard to reconcile with a simple “mPFC stores action–outcome memories” account.

[[raw/summaries/coutureau2003_infralimbic_prefrontal_goal|Coutureau and Killcross 2003]] is the strongest evidence for IL in habit expression.

- Overtrained control rats were insensitive to devaluation, consistent with habitual responding.
- Temporary IL inactivation with muscimol restored devaluation sensitivity.
- Consumption tests showed devaluation itself was intact across groups.
- Baseline response rates before test did not differ, arguing against a trivial motor/performance account.

The key inference is mechanistic: habitual performance can actively suppress goal-directed control rather than replace it.

[[raw/summaries/corbit2018_goal_directed_habitual|Corbit et al. 2018]] consolidates these findings within a broader corticostriatal framework.

- Dorsomedial striatum + medial prefrontal regions are linked to goal-directed control.
- Dorsolateral striatum + sensorimotor cortex, with IL often grouped on the habit side, are linked to habitual control.
- Post-training manipulations of habit circuitry can restore goal-directed responding, supporting competition rather than unidirectional transfer.

## Landmark papers

[[raw/summaries/coutureau2003_infralimbic_prefrontal_goal|Coutureau and Killcross 2003]]

- Classic demonstration that IL inactivation after overtraining reinstates devaluation-sensitive responding.
- Landmark because it shifted the interpretation of habit formation from loss of goal knowledge to suppression/gating of goal-directed control.

[[raw/summaries/ostlund2005_prefrontal_cortex_habits|Ostlund et al. 2005]]

- Established the acquisition vs expression dissociation for mPFC lesions.
- Landmark because it argues against mPFC as the long-term repository of action–outcome knowledge.

[[raw/summaries/corbit2018_goal_directed_habitual|Corbit et al. 2018]]

- Not primary evidence, but a useful synthesis of how mPFC findings fit with DMS/DLS competition, action sequencing, and pathological habits.

For computational framing rather than direct rat mPFC evidence:

- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] shows that reward revaluation sensitivity can arise from successor-like predictive representations, cautioning against equating devaluation effects with a single algorithmic process.
- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] extends the same caution: flexible revaluation behavior need not imply exhaustive tree search or a pure model-based/controller dichotomy.

## Boundaries and tensions

Subregion specificity is strong in the verbal consensus, less clean in the classic causal evidence.

- [[raw/summaries/coutureau2003_infralimbic_prefrontal_goal|Coutureau and Killcross 2003]] specifically targeted IL.
- [[raw/summaries/ostlund2005_prefrontal_cortex_habits|Ostlund et al. 2005]] used broader mPFC lesions with some spread beyond prelimbic territory.
- So the popular “PL for goal-directed, IL for habit” formulation is plausible, but not settled by perfectly selective lesion contrasts in these anchor studies alone.

The task assay is narrower than the conceptual claims often attached to it.

- Outcome devaluation tests value-sensitive instrumental control.
- It does not by itself show prospective planning over transition structure, detour behavior, or hierarchical action selection.
- Computationally, reward revaluation can be solved by several architectures besides full model-based search [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

“Habit” is also not a unitary construct.

- The strongest IL result is in overtrained free-operant behavior.
- It remains unclear how far the same mPFC dissociation generalizes across interval vs ratio schedules, contingency degradation, action sequences, stress- or drug-accelerated habits, or sex/strain differences [[raw/summaries/corbit2018_goal_directed_habitual|Corbit et al. 2018]].

Storage remains unresolved.

- If posttraining mPFC lesions spare devaluation sensitivity, the learned action–outcome information must be supported elsewhere.
- Candidate downstream loci are usually discussed in corticostriatal/amygdala terms, but these studies do not localize the storage site directly [[raw/summaries/ostlund2005_prefrontal_cortex_habits|Ostlund et al. 2005]].

## Open questions

- How selective is the dorsal mPFC/prelimbic vs IL division when tested with modern projection- and cell-type-specific tools?
- Does IL suppress goal-directed control directly, or bias action selection indirectly through striatal and accumbal circuits?
- In overtraining-induced habits, what survives: full action–outcome structure, only cached outcome values, or something closer to predictive state representations?
- Are devaluation-sensitive effects in these rat tasks better captured by model-based planning, successor representations, or hybrid reuse schemes [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]]?
- Where is action–outcome knowledge stored after acquisition if mPFC is dispensable for later expression [[raw/summaries/ostlund2005_prefrontal_cortex_habits|Ostlund et al. 2005]]?
- Do stress, drugs, and compulsive-like states recruit the same IL-centered suppression mechanism, or multiple distinct routes to habit dominance [[raw/summaries/corbit2018_goal_directed_habitual|Corbit et al. 2018]]?

## Key papers

- [[raw/summaries/coutureau2003_infralimbic_prefrontal_goal|Coutureau and Killcross 2003]] — IL inactivation after overtraining restores devaluation sensitivity.
- [[raw/summaries/ostlund2005_prefrontal_cortex_habits|Ostlund et al. 2005]] — mPFC lesions disrupt acquisition, not expression, of goal-directed action.
- [[raw/summaries/corbit2018_goal_directed_habitual|Corbit et al. 2018]] — circuit-level synthesis of goal-directed vs habitual control in rodents.
- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] — computational warning that reward revaluation is not uniquely diagnostic of full model-based planning.
- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] — broader computational account of flexible revaluation without a simple model-based/model-free split.

## Source papers
- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] | [[raw/mds/russek2017_model_based_reinforcement|source md]]: Predictive representations can link model-based reinforcement learning to model-free mechanisms
- [[raw/summaries/coutureau2003_infralimbic_prefrontal_goal|Coutureau and Killcross 2003]] | [[raw/mds/coutureau2003_infralimbic_prefrontal_goal|source md]]: Inactivation of the infralimbic prefrontal cortex reinstates goal-directed responding in overtrained rats
- [[raw/summaries/ostlund2005_prefrontal_cortex_habits|Ostlund and Balleine 2005]] | [[raw/mds/ostlund2005_prefrontal_cortex_habits|source md]]: Lesions of Medial Prefrontal Cortex Disrupt the Acquisition But Not the Expression of Goal-Directed Learning
- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray and Daw 2020]] | [[raw/mds/piray2020_linear_reinforcement_learning|source md]]: Linear reinforcement learning: Flexible reuse of computation in planning, grid fields, and cognitive control
- [[raw/summaries/corbit2018_goal_directed_habitual|Corbit 2018]] | [[raw/mds/corbit2018_goal_directed_habitual|source md]]: Understanding the balance between goal-directed and habitual behavioral control
- [[raw/summaries/anastasiades2021_circuit_medial_prefrontal|Anastasiades and Carter 2021]] | [[raw/mds/anastasiades2021_circuit_medial_prefrontal|source md]]: Circuit organization of the rodent medial prefrontal cortex
- [[raw/summaries/botvinick2009_hierarchically_organized_behavior|Botvinick et al. 2009]] | [[raw/mds/botvinick2009_hierarchically_organized_behavior|source md]]: Hierarchically organized behavior and its neural foundations: A reinforcement-learning perspective
- [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]] | [[raw/mds/dolan2013_goals_habits_brain_b|source md]]: Goals and Habits in the Brain
- [[raw/summaries/gabriel2022_behaviordepot_detection|Gabriel et al. 2022]] | [[raw/mds/gabriel2022_behaviordepot_detection|source md]]: BehaviorDEPOT is a simple, flexible tool for automated behavioral detection based on markerless pose tracking
- [[raw/summaries/hok2005_goal_coding_prefrontal|Hok et al. 2005]] | [[raw/mds/hok2005_goal_coding_prefrontal|source md]]: Coding for spatial goals in the prelimbic/infralimbic area of the rat frontal cortex
- [[raw/summaries/holton2023_planning_vmPFC_lesions|Holton et al. 2023]] | [[raw/mds/holton2023_planning_vmPFC_lesions|source md]]: Disentangling the component processes in complex planning impairments following ventromedial prefrontal lesions
