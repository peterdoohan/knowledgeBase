# Reverse Replay

## Current understanding

Reverse replay is the time-compressed reactivation of place cell sequences in the opposite order to which they were experienced during behavior. It occurs during sharp-wave ripple (SWR) events primarily during awake pauses at reward locations. Reverse replay is uniquely modulated by reward magnitude—increasing at higher reward and decreasing at lower reward—suggesting it plays a specific role in temporal credit assignment during reinforcement learning.

---

## Key evidence

- Reverse hippocampal replay rates track changes in reward magnitude—increasing at higher reward and decreasing at lower reward—while forward replay rates remain unchanged ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Poisson GLMM analysis showed reverse replay increased at 4× reward end (z = 3.57, p = 3.60 × 10⁻⁴) and decreased when reward removed (z = −2.05, p = 0.041).

- Reverse hippocampal replay encodes relative (adaptive) reward magnitude rather than absolute reward levels, with rate changes reflecting reward value relative to the environment ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Increasing reward at one end simultaneously elevated reverse replay there and depressed it at the unchanged end; this adaptive coding matches the known adaptive range coding of reward by dopamine neurons.

- Reverse replay is elevated after reward reinstatement, consistent with sensitivity to reward prediction error-like signals ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). When baseline reward was restored at a previously unrewarded location, reverse (but not forward) replay was significantly elevated (z = 3.35, p = 0.0049), suggesting it signals reward prediction errors.

- Reverse replay can occur after a single traversal of a novel track, demonstrating that behavioral repetition is not strictly necessary for replay generation, though experience-dependent plasticity enhances replay expression ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Foster & Wilson (2006) discovered reverse replay after first experience; subsequent plasticity strengthens expression.

- The number of reverse replays correlates with reward magnitude, and dopaminergic activation enhances replay likelihood, suggesting salience signals bias reverse replay content toward important experiences ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Ambrose et al. (2016) established reward-replay correlation; McNamara et al. (2014) showed dopaminergic enhancement.

- Reverse replay appears suited for memory consolidation by linking outcomes to prior actions, while forward replay serves memory retrieval for planning ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). This functional dissociation suggests reverse replay solves temporal credit assignment by bringing reward information to preceding actions.

- Both forward and reverse replay are predominantly locally initiated, beginning at the animal's current position during awake stopping periods ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Approximately 86% of replays in Experiment 1 and 78% of Experiment 2 were locally initiated, supporting the credit assignment hypothesis where reverse replay propagates value information backward from the current reward location.

- In humans, reward-triggered reverse replay appears during value learning itself (b = −0.053 ± 0.016) and continues during subsequent decision-making (b = −0.055 ± 0.020). Only the rewarded sequence reversed; the neutral sequence remained forward. This demonstrates that reverse replay in humans is reward-modulated, matching the functional properties observed in rodents. ([Liu 2019](../../raw/summaries/liu2019_human_replay_reorganizes.md))

---

## History of ideas

Reverse replay was first reported by Foster and Wilson (2006) who discovered that place cells reactivate in reverse order during awake pauses at reward locations on a linear track. They proposed the temporal credit assignment hypothesis: reverse replay propagates reward information backward along the just-experienced trajectory, allowing place cells distant from reward to become associated with reward value. This was initially controversial because both forward and reverse replay had been observed, and their functional distinction was unclear. Ambrose et al. (2016) provided the critical test by manipulating reward magnitude and demonstrating that only reverse replay is reward-sensitive, establishing the functional dissociation predicted by the credit assignment hypothesis.

---

## Open questions

- What is the precise circuit mechanism linking VTA dopamine signals to the initiation of reverse replay?
- Is the rate of reverse replay itself functionally meaningful, or merely a byproduct of reward-triggered initiation?
- What is the role of remote reverse replay (of non-current locations) in credit assignment?
- Does the same reward sensitivity hold for reverse replay in 2D environments or during active decision-making?

---

## Related pages

- [[forward_replay]]
- [[hippocampal_replay]]
- [[place_cells]]
- [[sharp_wave_ripples]]
- [[hippocampus_ca1]]
- [[temporal_credit_assignment]]
- [[reward_processing]]
- [[ventral_tegmental_area]]
