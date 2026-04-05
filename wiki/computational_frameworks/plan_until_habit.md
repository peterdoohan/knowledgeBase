# Plan-Until-Habit Model

## Current understanding

The plan-until-habit model proposes that humans integrate cached habitual values directly into forward planning at variable depths, forming a spectrum between purely habitual and purely goal-directed control. Rather than treating habitual and goal-directed systems as competing for behavioral control, this framework suggests they are normatively integrated: forward planning proceeds to some depth k, then switches to habitual values for the remainder of the decision tree. The depth parameter k is modulated by available cognitive resources such as time pressure, with reduced planning depth under time constraints.

## Key evidence

- Both high- and low-resource groups showed significant pure planning effects after rewarded and unrewarded trials, confirming model-based control is engaged regardless of time pressure ([Keramati 2016](../../raw/summaries/keramati2016_plan_until_habit.md))

- The plan-until-habit strategy was significantly stronger in the low-resource group (700 ms per decision) than in the high-resource group (2000 ms) after rewarded trials (P = 0.034), consistent with time pressure reducing planning depth ([Keramati 2016](../../raw/summaries/keramati2016_plan_until_habit.md))

- Model fitting confirmed both groups were best described by a mixture of pure planning and plan-until-habit strategies (not pure habitual); the weight of the plan-until-habit component was significantly larger in the low-resource group (permutation test, P < 0.01) ([Keramati 2016](../../raw/summaries/keramati2016_plan_until_habit.md))

- Within subjects, reliance on plan-until-habit at stage 1 correlated strongly with reliance on pure habit at stage 2 across both groups, indicating a stable individual trait in planning depth ([Keramati 2016](../../raw/summaries/keramati2016_plan_until_habit.md))

- The habitual weight at the second stage was 0.37 ± 0.18 (high-resource) vs 0.59 ± 0.23 (low-resource), replicating the resource-dependent shift toward more habitual control under time pressure ([Keramati 2016](../../raw/summaries/keramati2016_plan_until_habit.md))

## History of ideas

Prior to this paper, the field conceptualized habitual and goal-directed control as two competing systems, with arbitration mechanisms determining which system gains behavioral control based on their relative competencies (uncertainty, stress, working memory load). The dominant framework (Daw, Niv & Dayan 2005; Daw et al. 2011) modeled the two systems as running in parallel, with a weighted average or winner-takes-more competition at the output stage. This implied a discrete or smoothly weighted blend, but not a principled integration of one system's outputs into the other's computations. The plan-until-habit model reframes the habitual/goal-directed distinction from a binary or continuous weight into a spectrum parameterized by planning depth, with habitual values inserted as leaf-node estimates within forward planning trees.

## Open questions

- What are the neural substrates of "metacontrol" — i.e., how does the brain select the planning depth parameter k?
- How does the plan-until-habit framework map onto specific brain circuits (cortico-striatal, prefrontal, amygdala)?
- Can the model be extended to allow non-integer or tree-heterogeneous depth strategies?
- How does the framework apply to psychiatric conditions involving habit/goal-directed imbalances (addiction, OCD)?

## Related pages

- [Model-based RL](model_based_rl.md)
- [Model-free RL](model_free_rl.md)
- [Hierarchical RL](hierarchical_rl.md)
- [Goal-directed behaviour](../behaviours/goal_directed_behaviour.md)
- [Habits](../behaviours/habits.md)
