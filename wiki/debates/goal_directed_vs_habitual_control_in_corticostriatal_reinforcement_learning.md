---
title: "Goal-directed vs habitual control in corticostriatal reinforcement learning"
subtopic_id: striatal_and_dopaminergic_reinforcement_learning__01
parent_topic_id: striatal_and_dopaminergic_reinforcement_learning
page_type: debate
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:49:28.932433+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - daw2005_uncertainty_prefrontal_striatal
  - balleine1998_goal_directed_instrumental_action
  - dolan2013_goals_habits_brain_b
  - mattar2022_planning_brain
  - corbit2018_goal_directed_habitual
core_papers:
  - akam2015_two_step_task_habits
  - akam2015_two_step_task_simple_plans
  - akam2021_dopamine_model_based_rl
  - balleine1998_goal_directed_instrumental_action
  - blancopolzo2024_dopamine_independent_reward
  - botvinick2009_hierarchical_behavior_reinforcement
  - botvinick2009_hierarchically_organized_behavior
  - chandra2024_visual_cortex_development
related_wiki_pages:
  - wiki/topics/medial_prefrontal_cortex_in_rat_goal_directed_vs_habitual_control
  - wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning
---

# Goal-directed vs habitual control in corticostriatal reinforcement learning

The cleanest account is that goal-directed action depends on action–outcome evaluation in medial prefrontal/dorsomedial striatal circuits, whereas habits depend on cached stimulus–response control in dorsolateral striatum. That account is strongly supported by rodent outcome-devaluation and contingency-degradation work, and it is computationally sharpened by model-based versus model-free reinforcement learning. But the mapping is not exact. Human two-step evidence is vulnerable to alternative strategies, neural signals are often mixed rather than anatomically clean, and habit-like behavior may reflect chunked action sequences or other compressed policies rather than simple scalar value caching [[raw/summaries/balleine1998_goal_directed_instrumental_action|Balleine et al. 1998]] [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]] [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]] [[raw/summaries/corbit2018_goal_directed_habitual|Corbit and Balleine 2018]].

## Central question

Is goal-directed versus habitual control best understood as a corticostriatal implementation of model-based versus model-free RL?

More specifically:

- Do prelimbic/OFC/dorsomedial striatal circuits compute and use action–outcome structure in a way that justifies calling them model-based?
- Do infralimbic/sensorimotor/dorsolateral striatal circuits support genuine model-free S–R habits?
- Or are these only partial correspondences, with hybrid representations, action chunking, inference, and task-specific heuristics accounting for much of the apparent dissociation?

## Strongest case for the main mechanism or position

The strongest evidence starts with behavior, not computation. Goal-directed control is operationally defined by sensitivity to both action–outcome contingency and current outcome value. In rats, limited-training instrumental responding shows both properties, and prelimbic lesions abolish contingency sensitivity and devaluation sensitivity in extinction, while insular lesions spare basic performance but disrupt incentive-value retrieval in extinction. This is hard to explain with a unitary S–R account [[raw/summaries/balleine1998_goal_directed_instrumental_action|Balleine et al. 1998]].

The broader lesion and inactivation literature supports a parallel-circuit view. Across studies synthesized in review, dorsomedial striatum plus medial prefrontal regions support goal-directed control, whereas dorsolateral striatum plus infralimbic/sensorimotor circuits support habits. Extended interval-schedule training biases behavior toward devaluation-insensitive responding, and inactivation of DLS after habits are established can restore goal-directed control, implying competition between controllers rather than irreversible replacement [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]] [[raw/summaries/corbit2018_goal_directed_habitual|Corbit and Balleine 2018]].

The model-based/model-free framework gives these behavioral facts a principled explanation. In the uncertainty-based arbitration model, a tree-search controller is initially favored because it generalizes each new experience through the transition model, making it more data-efficient early in learning. With overtraining, a cached controller can dominate for actions distal from reward because deep tree search accumulates computational noise, whereas cached action values do not. The framework also predicts that task structure matters: when experience is spread across more action–outcome pairs, goal-directed control should persist longer. Those predictions line up with classic devaluation data better than a simple “habits just emerge with time” story [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]].

Human work broadly fits the same picture, though less cleanly. fMRI studies reviewed by Dolan and Dayan associate goal-directed valuation with vmPFC/OFC and habit-promoting training with posterior putamen/globus pallidus, while two-step behavior varies continuously across individuals rather than splitting into pure types. That is at least consistent with weighted or competing model-based and model-free control in corticostriatal circuits [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]].

## Strongest alternatives or challenges

The biggest challenge is that goal-directed/habitual and model-based/model-free are not interchangeable labels. Outcome devaluation and contingency degradation measure whether behavior uses outcome identity and current value; they do not by themselves reveal the exact algorithm used. A system can be flexible without performing full prospective tree search.

The standard human assay is also less diagnostic than often claimed. In the two-step task, model-free agents with richer state representations can mimic the canonical model-based choice signature under standard analyses. So some “model-based” estimates from this task may instead reflect sophisticated habits or learned latent-state structure [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]].

Neural segregation is incomplete. Reviews emphasize that vmPFC and ventral striatum often contain both model-based and model-free related signals. That weakens any strict cortex-for-model-based / striatum-for-model-free mapping, and suggests substantial integration or shared downstream value coding [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]].

A second challenge is that “habit” may often mean chunked sequential control rather than elemental S–R learning. DLS neurons develop task-bracketing activity during overtraining, and this has been interpreted as sequence chunking. Hierarchical RL offers a formal version of that idea: behavior may become automatic because temporally extended options are selected and then run off, not because each individual movement is chosen from a cached scalar action value [[raw/summaries/corbit2018_goal_directed_habitual|Corbit and Balleine 2018]] [[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]].

A third challenge is that biological planning looks computationally constrained. Evidence reviewed by Mattar and Daw suggests planning is focused, depth-limited, and serial, not exhaustive tree search. That makes the classical model-based controller a useful idealization, but probably not a literal neural implementation [[raw/summaries/mattar2022_planning_brain|Mattar and Daw 2022]].

Finally, dopamine does not map neatly onto “model-free teaching.” A recent two-step study found that rewards strongly shaped dopamine activity and subsequent choices through hidden-state inference, yet direct optogenetic activation or inhibition of dopamine neurons at outcome time did not alter later choices. Related review arguments favor dopamine as a scalar RPE plus separate surprise/inference-related signals, rather than a direct successor-representation error. This does not refute corticostriatal dual-control accounts, but it does challenge overly simple dopamine=model-free equations [[raw/summaries/blancopolzo2024_dopamine_independent_reward|Blanco-Pozo et al. 2024]] [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Dayan 2021]].

## What the literature currently supports

The behavioral distinction between goal-directed and habitual control is real and well supported. Outcome devaluation and contingency degradation remain the strongest assays, and rodent lesion work gives a credible causal basis for dissociable circuits supporting these modes of control [[raw/summaries/balleine1998_goal_directed_instrumental_action|Balleine et al. 1998]] [[raw/summaries/corbit2018_goal_directed_habitual|Corbit and Balleine 2018]].

A corticostriatal division of labor is also well supported, but only at a coarse level. DMS/medial prefrontal/OFC-linked circuits are more necessary for goal-directed behavior; DLS/infralimbic/sensorimotor-linked circuits are more necessary for habits. The evidence is strongest for partial specialization and competition, not for strict anatomical exclusivity [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]] [[raw/summaries/corbit2018_goal_directed_habitual|Corbit and Balleine 2018]].

Model-based versus model-free RL is currently the most useful computational language for organizing this literature, especially for explaining effects of training history, task complexity, and reward proximity. But the literature does not support a strict one-to-one translation between psychological categories, algorithms, and brain regions [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]].

Human evidence supports mixed control more than clean dissociation. Two-step and related tasks show graded individual differences, but those tasks need careful analysis because apparent planning can arise from alternative learned-state strategies. Claims about pure model-based versus pure model-free control in humans should therefore be treated cautiously [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]] [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]].

## Open questions

- Is devaluation-insensitive behavior usually driven by genuine S–R associations, or by chunked action sequences/options that are simply insulated from outcome re-evaluation?
- What neural variable actually arbitrates control: relative uncertainty, computational cost, opportunity cost, reliability, or some combination [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]]?
- How do OFC, hippocampus, and ventral striatum contribute to model-based control when neural signals in these regions are mixed rather than segregated [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]]?
- Are hybrid representations such as successor-like predictive maps necessary to explain flexibility without full tree search, or can inference plus cached scalar values suffice [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Dayan 2021]]?
- How much of apparent human “planning” in two-step tasks survives when analyses explicitly control for extended-state model-free strategies [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]]?
- What is dopamine causally doing during goal-directed/model-based choice, if outcome-time manipulations can fail to influence later choices despite strong reward-evoked dopamine signals [[raw/summaries/blancopolzo2024_dopamine_independent_reward|Blanco-Pozo et al. 2024]]?
- Do replay and offline planning train habitual policies, support online goal-directed search, or both [[raw/summaries/mattar2022_planning_brain|Mattar and Daw 2022]]?

## Key papers

- [[raw/summaries/balleine1998_goal_directed_instrumental_action|Balleine et al. 1998]] — Foundational behavioral and lesion evidence separating contingency learning, incentive learning, and habit.
- [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] — Classic normative account of arbitration between model-based and model-free corticostriatal control.
- [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]] — Best compact synthesis of behavioral, neural, and computational evidence, including important caveats.
- [[raw/summaries/corbit2018_goal_directed_habitual|Corbit and Balleine 2018]] — Strong animal-focused review of DMS/DLS circuitry, overtraining effects, and action-chunking ideas.
- [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]] — Essential methodological challenge to interpreting two-step behavior as clean model-based control.
- [[raw/summaries/mattar2022_planning_brain|Mattar and Daw 2022]] — Useful corrective against overly literal tree-search interpretations of “model-based” control.
- [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Dayan 2021]] — Focused review on dopamine’s role in model-based RL and the limits of SR-style interpretations.
- [[raw/summaries/blancopolzo2024_dopamine_independent_reward|Blanco-Pozo et al. 2024]] — Recent causal evidence that reward-driven choice updating in a two-step task may depend more on inference than on outcome-time dopamine teaching.

## Related wiki pages
- [[wiki/topics/medial_prefrontal_cortex_in_rat_goal_directed_vs_habitual_control|Medial prefrontal cortex in rat goal-directed vs habitual control]]: Crosslink A -> B as the broader systems/computational framework for goal-directed vs habitual control; crosslink B -> A as a key rat mPFC case study showing how specific prefrontal nodes fit into, and complicate, the broader corticostriatal RL account.
- [[wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning|Orbitofrontal cortex as a cognitive map of task state for model-based reinforcement learning]]: Link Page B's goal-directed/model-based section to Page A as a candidate representational mechanism for state inference in flexible control; link Page A back to Page B for the broader debate on how such state representations relate to goal-directed versus habitual behavior.

## Source papers
- [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] | [[raw/mds/daw2005_uncertainty_prefrontal_striatal|source md]]: Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control
- [[raw/summaries/balleine1998_goal_directed_instrumental_action|Balleine and Dickinson 1998]] | [[raw/mds/balleine1998_goal_directed_instrumental_action|source md]]: Goal-directed instrumental action: contingency and incentive learning and their cortical substrates
- [[raw/summaries/dolan2013_goals_habits_brain_b|Dolan and Dayan 2013]] | [[raw/mds/dolan2013_goals_habits_brain_b|source md]]: Goals and Habits in the Brain
- [[raw/summaries/mattar2022_planning_brain|Mattar and Lengyel 2022]] | [[raw/mds/mattar2022_planning_brain|source md]]: Planning in the brain
- [[raw/summaries/corbit2018_goal_directed_habitual|Corbit 2018]] | [[raw/mds/corbit2018_goal_directed_habitual|source md]]: Understanding the balance between goal-directed and habitual behavioral control
- [[raw/summaries/akam2015_two_step_task_habits|Akam et al. 2015]] | [[raw/mds/akam2015_two_step_task_habits|source md]]: Simple Plans or Sophisticated Habits? State, Transition and Learning Interactions in the Two-Step Task
- [[raw/summaries/akam2015_two_step_task_simple_plans|Akam et al. 2015]] | [[raw/mds/akam2015_two_step_task_simple_plans|source md]]: Simple Plans or Sophisticated Habits? State, Transition and Learning Interactions in the Two-Step Task
- [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Walton 2021]] | [[raw/mds/akam2021_dopamine_model_based_rl|source md]]: What is dopamine doing in model-based reinforcement learning?
- [[raw/summaries/blancopolzo2024_dopamine_independent_reward|Blanco-Pozo et al. 2024]] | [[raw/mds/blancopolzo2024_dopamine_independent_reward|source md]]: Dopamine-independent effect of rewards on choices through hidden-state inference
- [[raw/summaries/botvinick2009_hierarchical_behavior_reinforcement|Botvinick et al. 2009]] | [[raw/mds/botvinick2009_hierarchical_behavior_reinforcement|source md]]: Hierarchically organized behavior and its neural foundations: A reinforcement-learning perspective
- [[raw/summaries/botvinick2009_hierarchically_organized_behavior|Botvinick et al. 2009]] | [[raw/mds/botvinick2009_hierarchically_organized_behavior|source md]]: Hierarchically organized behavior and its neural foundations: A reinforcement-learning perspective
- [[raw/summaries/chandra2024_visual_cortex_development|Chandra et al. 2024]] | [[raw/mds/chandra2024_visual_cortex_development|source md]]: Self-organized emergence of modularity, hierarchy, and mirror reversals from competitive synaptic growth in a developmental model of the visual pathway
