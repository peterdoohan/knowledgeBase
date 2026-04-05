# Forward Replay

## Current understanding

Forward replay is the time-compressed reactivation of place cell sequences in the same order as they were experienced during behavior. It occurs during sharp-wave ripple (SWR) events during both sleep and awake pauses. Unlike reverse replay, forward replay is reward-insensitive—its rate does not change with reward magnitude manipulation—suggesting it serves functions in memory retrieval and prospective planning rather than in reward-based credit assignment.

---

## Key evidence

- Forward hippocampal replay rates remain unchanged despite manipulation of reward magnitude, while reverse replay rates track reward changes ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Poisson GLMM analysis showed no effect of reward manipulation on forward replay in either experiment (Exp. 1: z = 0.305, p = 0.76; Exp. 2: z = −1.83, p = 0.068).

- Forward and reverse hippocampal replay are functionally dissociable, with forward replay supporting planning or memory retrieval independent of reward, while reverse replay mediates reward-based learning ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). The bidirectional control within same stopping periods shows forward replay unaffected by reward manipulation while reverse replay is strongly modulated, ruling out trivial behavioral confounds.

- Forward replay is elevated after reward reinstatement at the same magnitude as reverse replay, but shows no differential sensitivity to the reinstatement event itself ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). When baseline reward was restored at a previously unrewarded location, forward replay showed no significant elevation (unlike reverse replay which was significantly elevated, z = 3.35, p = 0.0049).

- Replay can encode novel "shortcut" paths never actually taken and trajectories in physically separate environments, indicating forward replay represents learned spatial relationships rather than mere replication of prior activity ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Gupta et al. (2010) demonstrated never-experienced shortcut paths in replay; Karlsson & Frank (2009) showed remote environment replay.

- During goal-directed navigation, forward replay encodes paths from current location to goal, and replay content strongly correlates with subsequent behavior; replay can also encode paths to avoid, suggesting it provides outcome predictions to inform rather than dictate behavior ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Pfeiffer & Foster (2013) showed forward replay predicts behavior; Wu et al. (2017) demonstrated path avoidance encoding.

- Forward replay serves memory retrieval for planning, while reverse replay appears suited for memory consolidation by linking outcomes to prior actions; sleep and awake replay may have distinct functions, with forward replay during wakefulness supporting planning and working memory ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). This functional dissociation suggests distinct computational roles for forward versus reverse replay.

- Both forward and reverse replay are predominantly locally initiated, beginning at the animal's current position during awake stopping periods ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Approximately 86% of replays in Experiment 1 and 78% in Experiment 2 were locally initiated, suggesting both replay types propagate from current location regardless of direction.

- Online (on-task) forward replay correlates with model-based planning flexibility and predicts policy re-evaluation; forward sequenceness positively correlated with Index of Flexibility (mean β = 0.17, 95% CI = 0.13–0.20) and with outcome surprise (β = 0.06), with significant interaction (β = 0.19) ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

- Hippocampal forward replay matches the spatiotemporal statistics of imagined policy rollouts in a recurrent meta-RL agent, avoiding walls more than chance (P<0.001), over-representing goal locations (P<0.001), and predicting subsequent physical actions more accurately when successful than unsuccessful (P<0.001) ([Jensen 2024](../../raw/summaries/jensen2024_recurrent_planning_hippocampal_replay.md)).

- Consecutive forward replays become increasingly goal-directed, mirroring iterative policy refinement in a planning agent. In trials with ≥3 replays, goal over-representation increased with replay number (2nd replay P=0.068, 3rd replay P=0.009), an effect absent in away trials and paralleled in the meta-RL agent with rollouts ([Jensen 2024](../../raw/summaries/jensen2024_recurrent_planning_hippocampal_replay.md)).

- The medial prefrontal cortex generates independent awake forward replay during rule-switching tasks, with mPFC replay temporally uncorrelated with hippocampal replay (~5% co-occurrence) despite co-occurring with hippocampal SWRs at above-chance rates (40%) ([Kaefer 2020](../../raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md)).

- On-task forward sequenceness predicts subsequent policy change: moves preceded by high sequenceness were less likely to be re-chosen; this re-evaluation increased reward by +11.1% (SEM 1.5%, p = 0.001) ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

- Advance planning is evident in neural representations before choice and outcome; chosen second moves were decodeable during first-move choices and prior to first-outcome onset; early decodability correlated with Index of Flexibility (β = 0.29, 95% CI = 0.24–0.34) ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

- In humans, forward replay of a rewarded sequence switched to reverse replay after value learning (b = −0.028 ± 0.010), while the neutral sequence remained forward. This reward-triggered direction reversal demonstrates that replay direction is dynamically modulated by reward outcomes in humans, matching rodent findings. ([Liu 2019](../../raw/summaries/liu2019_human_replay_reorganizes.md))

---

## History of ideas

Forward replay was first reported alongside reverse replay by Diba and Buzsáki (2007), who observed both directions of sequence reactivation during awake periods on a linear track. While reverse replay was immediately hypothesized to serve temporal credit assignment (Foster and Wilson, 2006), forward replay was associated with memory retrieval and prospective planning. Pfeiffer and Foster (2013) demonstrated that forward replay could predict upcoming behavioral choices, supporting its role in planning. However, the functional dissociation between forward and reverse replay remained unclear until Ambrose et al. (2016) showed that only reverse replay is reward-sensitive, establishing forward replay's role in reward-independent processes like planning and memory retrieval.

---

## Open questions

- Does forward replay in more complex 2D environments or active decision-making tasks show different reward sensitivity?
- What is the relationship between forward replay content and subsequent behavioral choices in tasks with multiple possible paths?
- How does the initiation of forward replay differ from reverse replay at the circuit level?

---

## Related pages

- [[reverse_replay]]
- [[hippocampal_replay]]
- [[place_cells]]
- [[sharp_wave_ripples]]
- [[hippocampus_ca1]]
- [[planning]]
- [[memory_retrieval]]
