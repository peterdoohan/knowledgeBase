# Planning

Planning involves the prospective computation of action sequences using an internal model of the environment to achieve desired outcomes.

---

## Current understanding

*Placeholder: Awaiting synthesis of key evidence.*

---

## Key evidence

- The reward-as-cue strategy treats the combination of previous trial outcome and second-step state as a discriminative stimulus, learning a fixed stimulus-response mapping that produces a strong stay-probability transition-outcome interaction despite using no prospective planning. It can be distinguished from true model-based planning by lagged regression: only the immediately preceding trial is predictive of choice ([Akam 2015](../../raw/summaries/akam2015_two_step_task_simple_plans.md)).

- During goal-directed navigation, forward replay encodes paths from current location to goal, and replay content strongly correlates with subsequent behavior; replay can also encode paths to avoid, suggesting it provides outcome predictions to inform rather than dictate behavior ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Pfeiffer & Foster (2013) showed forward replay predicts behavior; Wu et al. (2017) demonstrated path avoidance encoding.

- Forward replay serves memory retrieval for planning, while reverse replay appears suited for memory consolidation by linking outcomes to prior actions; sleep and awake replay may have distinct functions, with forward replay during wakefulness supporting planning and working memory ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). This functional dissociation suggests forward replay implements model-based planning by simulating future trajectories.

- Replay can encode novel "shortcut" paths never actually taken, indicating replay represents learned spatial relationships rather than mere replication of prior activity, supporting its role in constructing possible future paths for planning ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Gupta et al. (2010) demonstrated never-experienced shortcut paths in replay.

- The latent-state strategy maintains a Bayesian belief over which latent reward state the world is in and maps this belief to choice deterministically, producing behaviour that mimics model-based planning on both one-trial-back and multi-lag analyses. Discrimination from true model-based planning requires explicit model comparison ([Akam 2015](../../raw/summaries/akam2015_two_step_task_simple_plans.md)).

- Right prefrontal cortex lesions specifically impair real-world planning by causing premature commitment to concrete solutions before adequate problem space exploration. RPFC patients produced significantly lower-quality plans than normal controls (F[3,16]=4.76, p=.015); LPFC and posterior groups did not differ from NC. RPFC patients had significantly higher concrete-to-abstract statement ratios (F[3,16]=3.90, p=.029). ([Goel 2013](../../raw/summaries/goel2013_prefrontal_planning_real_world.md))

- Right PFC specifically supports early planning phases requiring abstract representations, while left PFC is not required for real-world planning. The concrete-to-abstract ratio was significantly elevated for RPFC patients in the middle planning phase (F[3,15]=4.28, p=.023). LPFC patients showed no planning deficit, did not differ from NC in time-on-task or abstractness ratios, and were not significantly different from any group. ([Goel 2013](../../raw/summaries/goel2013_prefrontal_planning_real_world.md))

- The right PFC deficit is specific to representational abstractness, not to operator repertoire, episode structure, or planning phase allocation. No significant between-group differences were found in operator distributions, episode types, or allocation of time to problem-solving phases. The deficit was specific to the abstractness dimension - NC showed a 'judicious interplay' of concrete and abstract representations while RPFC patients locked into concrete detail prematurely. ([Goel 2013](../../raw/summaries/goel2013_prefrontal_planning_real_world.md))

- Right PFC patients spend less time on planning tasks but show no deficit in well-structured laboratory tasks like Tower of London. RPFC patients spent significantly less time on the Travel Planning Task than NC (RPFC M=28.75 min vs NC M=58.80 min; F[3,16]=4.31, p=.024). The deficit is specific to ill-structured real-world planning - standard well-structured tasks like Tower of London/Hanoi fail to detect right PFC contributions. ([Goel 2013](../../raw/summaries/goel2013_prefrontal_planning_real_world.md))

- mFC neurons form mnemonic fields at fixed task-space lags from specific goal-progress/place anchors, enabling distal behavioral prediction. Three convergent cross-validation analyses confirmed state-tuned neurons fire at fixed lags in task-space from specific anchors (t-tests against 0, all P<0.001), and neuronal activity at 'bump time' predicted the animal's choice to visit the anchor on the following trial (regression coefficient significantly positive, P=0.017). ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

- A recurrent meta-RL agent with imagined policy rollouts learns to plan when beneficial, matching human thinking-time variability and hippocampal replay statistics. The model's rollout probability correlates with human thinking time (r=0.186±0.007), and forcing more rollouts at trial start monotonically reduces steps-to-goal and decreases policy entropy ([Jensen 2024](../../raw/summaries/jensen2024_recurrent_planning_hippocampal_replay.md)).

- The meta-RL planning model unifies model-based and model-free control through a single policy refined by iterative rollouts. Model-based computation (rollout) directly updates the hidden state of the same network used for model-free decisions, explaining how hippocampal replay could influence behavior through fast recurrent dynamics rather than slow synaptic updates ([Jensen 2024](../../raw/summaries/jensen2024_recurrent_planning_hippocampal_replay.md)).

- Hippocampal activity patterns during the planning period significantly decode the future goal location before navigation begins; classifier accuracy 29.4% (t16=7.54, P=1.19e-6) for future goal decoding during pre-navigation planning period, demonstrating prospective goal-state coding in humans ([Brown 2016](../../raw/summaries/brown2016_prospective_goals_hippocampus.md))

- During planning, hippocampal representations show confusion between the true goal and intervening sub-goals along the optimal route, consistent with sequential trajectory simulation; MVPA confusion matrices show classifier errors reflect route waypoints and pattern reinstatement of intermediate locations, extending rodent forward-sweep concept to humans ([Brown 2016](../../raw/summaries/brown2016_prospective_goals_hippocampus.md))

- Trial-by-trial hippocampal goal evidence positively correlates with planning-period activity in lateral and medial frontopolar cortex, suggesting PFC-hippocampal coupling during prospective simulation; FPC activity tracked trial-by-trial goal coding strength in hippocampus, providing human evidence for PFC-hippocampal top-down control during planning ([Brown 2016](../../raw/summaries/brown2016_prospective_goals_hippocampus.md))