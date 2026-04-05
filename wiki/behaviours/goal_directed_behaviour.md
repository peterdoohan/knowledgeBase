# Goal-Directed Behaviour

Goal-directed behaviour involves actions performed to obtain specific outcomes, where the behaviour remains sensitive to the current value of the outcome and the contingency between action and outcome.

---

## Current understanding

*Placeholder: Awaiting synthesis of key evidence.*

---

## Key evidence

- ACC activity between trial outcome and subsequent choice is causally necessary for using state transition information to update behavior, but not for basic reward-driven reinforcement. Optogenetic inhibition of ACC from trial outcome to next choice selectively reduced the influence of state transitions on subsequent choice (p=0.007, Bonferroni corrected) without affecting direct reward reinforcement; effect size correlated with individual MB weight (R=-0.91, p=0.0001). ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- The ACC is causally necessary for model-based but not model-free reinforcement learning. Optogenetic inhibition selectively impaired model-based control (reduced influence of state transitions on choice) without affecting model-free reward-driven reinforcement; no significant effect in simpler reversal learning task where MB and MF agree. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- The model-based vs. model-free distinction represents a spectrum rather than a binary. Extended-state strategies demonstrate that intermediate forms of control exist: model-free RL algorithms applied to richer or inferred state representations can produce cached state-action mappings that approximate model-based goal-directed behaviour without prospective planning ([Akam 2015](../../raw/summaries/akam2015_two_step_task_simple_plans.md))

- A scalar dopaminergic surprise signal can upregulate learning rates in cortical and hippocampal predictive models, explaining stimulus-stimulus learning impairments and optogenetic unblocking without requiring vector-valued state prediction errors ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- Goal learning in spatial navigation tasks causes grid cells in the medial entorhinal cortex to shift their firing fields toward learned goal locations, demonstrating that spatial representations are dynamically updated to encode behaviorally relevant information. This field attraction is distance-dependent (stronger within ~30 cm of goals) and correlates with subsequent memory retention (r = 0.77, P = 0.002), linking neural reorganization directly to goal-directed behavioral performance ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- The hippocampal-entorhinal circuit supports goal-directed navigation through multiple coexisting spatial maps that alternate rapidly during learning ("flickering" dynamics), with both MEC and CA1 showing rapid switching between pre-learning and post-learning representations. CA1 reaches plateau faster than MEC in flickering dynamics, suggesting faster initial hippocampal reorganization that is more transient compared to stable entorhinal changes ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- During goal-directed navigation, forward replay encodes paths from current location to goal, and replay content strongly correlates with subsequent behavior; replay can also encode paths to avoid, suggesting it provides outcome predictions to inform rather than dictate behavior ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Pfeiffer & Foster (2013) showed forward replay predicts behavior during goal-directed navigation; Wu et al. (2017) demonstrated path avoidance encoding.

- Goal neglect — failure to act on a understood and remembered task requirement — is strongly correlated with Spearman's g in the normal population. Correlation between goal neglect and Culture Fair IQ was r = .41, rising to r = .52 in elderly and r = .55 under dual-task conditions; goal neglect showed higher correlation with g than comparably distributed items from the Culture Fair test itself. ([Duncan 1996](../../raw/summaries/duncan1996_intelligence_frontal_goal.md))

- Goal neglect is the predominant deficit following frontal lobe lesions, implicating frontal action-control functions in general intelligence. 7/10 frontal patients showed complete goal neglect vs. 1/10 matched controls; F(1,9) = 14.4, p < .005. Posterior lesion patients showed no deficit. Frontal patients also showed mean 9-point Culture Fair IQ deficit (F(1,9) = 14.8, p < .005). ([Duncan 1996](../../raw/summaries/duncan1996_intelligence_frontal_goal.md))

- Goal neglect reflects failure of goal activation — converting verbally understood requirements into active behavioral controllers — not working memory or verbal ability per se. Verbal prompts eliminated neglect in both normal and frontal subjects; once a subject first correctly used the requirement, performance was almost immediately and durably correct (~1-2% subsequent failures). Many subjects who neglected the requirement reported having seen the symbols, showing stimulus awareness and goal activation are dissociable. ([Duncan 1996](../../raw/summaries/duncan1996_intelligence_frontal_goal.md))

- Concurrent goal requirements increase goal neglect and strengthen its correlation with g, consistent with a limited-capacity goal-activation process. Adding a secondary task increased goal neglect and raised the g correlation; secondary task neglect was much greater and more closely tied to g (r = .66 vs. .19) when instructions were given last, confirming concurrent goal load as a key determinant. ([Duncan 1996](../../raw/summaries/duncan1996_intelligence_frontal_goal.md))

- Right prefrontal cortex lesions specifically impair real-world planning by causing premature commitment to concrete solutions before adequate problem space exploration. RPFC patients produced significantly lower-quality plans than normal controls (F[3,16]=4.76, p=.015); LPFC and posterior groups did not differ from NC. RPFC patients had significantly higher concrete-to-abstract statement ratios (F[3,16]=3.90, p=.029). ([Goel 2013](../../raw/summaries/goel2013_prefrontal_planning_real_world.md))

- Right PFC specifically supports early planning phases requiring abstract representations, while left PFC is not required for real-world planning. The concrete-to-abstract ratio was significantly elevated for RPFC patients in the middle planning phase (F[3,15]=4.28, p=.023). LPFC patients showed no planning deficit, did not differ from NC in time-on-task or abstractness ratios, and were not significantly different from any group. ([Goel 2013](../../raw/summaries/goel2013_prefrontal_planning_real_world.md))

- Goal-progress tuning is the dominant signal in mFC, with 80% of neurons tuned to fractional progress between consecutive goals independent of specific locations or trajectories. GLM analysis showed 80% of mFC neurons were significantly tuned to goal-progress (one-sample t-test vs. 0, N=1438, P=2.71×10⁻⁸²), with tuning independent of elapsed time, physical distance, speed, and acceleration. ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

---

- OFC neurons persistently encode the animal's future navigational destination throughout a journey ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals ([Basu2021](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

## History of ideas

---

## Open questions

---

## Related pages

- [Model-based RL](../computational_frameworks/model_based_rl.md)
- [Habits](habits.md)
- [Planning](planning.md)

- The hippocampal formation encodes goal-related information in multiple formats across all three phases of navigation: planning (replay), travel (theta sequences, goal-distance cells), and arrival (place-field overrepresentation) ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))

- Goal-distance cells in CA1 (~16% of principal cells in bats) encode path proximity to the goal, while goal-direction cells (~19%) encode egocentric angle to the goal; ~5% conjunctively encode both ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))

- Place-field overrepresentation at goal locations occurs in CA1 (but not CA3) when trajectories are repeated AND the goal location must be memorised, but not in flexible place-navigation tasks or when goals are visibly cued with no memory demand ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))

- mEC grid fields overrepresent goals more slowly than CA1 but more persistently, lasting to the next day; non-grid spatial cells in mEC form goal-proximal fields specifically in goal-directed contexts ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))

- A subset of CA1 place cells (31.1%, 142/456 cells) fire as egocentric vector fields oriented toward goal-proximal "convergence sinks" (ConSinks), with population vector fields converging to a population ConSink close to the goal ([Ormond 2022](../../raw/summaries/ormond2022_goal_oriented_vector_fields.md))

- ConSink positions redistribute from the original goal to a new goal after goal switching, with cells moving their ConSinks progressively closer to the goal with continued training ([Ormond 2022](../../raw/summaries/ormond2022_goal_oriented_vector_fields.md))

- Before error choices in CA1, goal-directed firing rates are significantly reduced and the fantail is rotated away from the goal, even before the animal knows which platforms will be offered, suggesting the firing predicts choice rather than merely accompanying movement ([Ormond 2022](../../raw/summaries/ormond2022_goal_oriented_vector_fields.md))

- RSC spatial representations develop progressively across learning stages, with position coding improving early, trajectory coding emerging mid-learning, and selective future-goal coding appearing only at asymptotic performance ([Miller 2019](../../raw/summaries/miller2019_retrosplenial_spatial_learning.md))

- RSC lesions have no effect during early learning but selectively impair asymptotic performance, with lesion size strongly correlated with impairment magnitude (r = -0.90, p < 0.01) ([Miller 2019](../../raw/summaries/miller2019_retrosplenial_spatial_learning.md))

- RSC selectively simulates upcoming correct reward locations at asymptotic performance, coinciding with when lesions produce deficits ([Miller 2019](../../raw/summaries/miller2019_retrosplenial_spatial_learning.md))
