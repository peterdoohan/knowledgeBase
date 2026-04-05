# Reward Processing

## Current understanding

Reward processing in the hippocampus involves the modulation of neural activity by reward magnitude, relative value, and prediction errors. The hippocampus does not simply encode reward as a scalar value but integrates reward information with spatial memory through specific mechanisms. Reverse replay of place cell sequences is uniquely sensitive to reward changes, encoding relative reward magnitude through an adaptive coding scheme similar to dopamine neurons. This reward-modulated replay provides a mechanism for associating spatial locations with reward value, enabling temporal credit assignment.

---

## Key evidence

- Reverse hippocampal replay encodes relative (adaptive) reward magnitude rather than absolute reward levels, with rate changes reflecting reward value relative to the environment ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Increasing reward at one end simultaneously elevated reverse replay there and depressed it at the unchanged end; this adaptive coding matches the adaptive range coding of reward by dopamine neurons (Tobler et al., 2005).

- Reverse replay is elevated after reward reinstatement, consistent with sensitivity to reward prediction error-like signals ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). When baseline reward was restored at a previously unrewarded location, reverse (but not forward) replay was significantly elevated (z = 3.35, p = 0.0049), suggesting it signals positive reward prediction errors.

- Sharp-wave ripple (SWR) rates track reward magnitude changes, serving as a nonspecific marker of reward-related hippocampal activation ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). SWR rate increased significantly at 4× reward end (z = 5.24, p = 1.61 × 10⁻⁷) and decreased when reward removed (z = −6.66, p = 2.67 × 10⁻¹¹).

- The number of reverse replays correlates with reward magnitude, and dopaminergic activation enhances replay likelihood, suggesting salience signals bias replay content toward important experiences ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Ambrose et al. (2016) established reward-replay correlation; McNamara et al. (2014) showed dopaminergic enhancement.

- Reverse hippocampal replay rates track changes in reward magnitude—increasing at higher reward and decreasing at lower reward—while forward replay rates remain unchanged, establishing that reward processing in the hippocampus is specifically implemented through reverse replay ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)).

- Dopamine neurons encode a scalar reward prediction error rather than specific reward properties; they do not discriminate between different types of appetitive stimuli and do not respond to aversive stimuli, encoding a general "goodness" signal that drives reinforcement learning ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- With learning, dopamine neuron responses shift from primary rewards to reward-predicting conditioned stimuli; after conditioning, fully-predicted primary rewards no longer elicit phasic dopamine responses, demonstrating that dopamine encodes prediction errors rather than reward value per se ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- When an expected reward is omitted, dopamine neurons show a phasic depression below baseline firing rate at the precise time the reward should have occurred, indicating an internal representation of expected reward timing and confirming the prediction error nature of the signal ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

---

## History of ideas

The idea that reward modulates hippocampal activity emerged from studies showing that the presence versus absence of reward affects sharp-wave ripple (SWR) rate (Singer and Frank, 2009). However, the specific mechanism by which reward information was integrated with spatial memory remained unclear. The temporal credit assignment hypothesis proposed by Foster and Wilson (2006) suggested that reverse replay could propagate reward information backward along trajectories, but this remained untested. Ambrose et al. (2016) established that reverse replay specifically encodes relative reward magnitude through adaptive coding, matching the properties of dopamine neurons and providing a mechanism for reward-modulated credit assignment.

---

## Open questions

- What is the precise circuit mechanism linking VTA dopamine signals to the reward modulation of reverse replay?
- Does the adaptive coding of reward in reverse replay generalize to 2D environments and more complex tasks?
- Is the reward sensitivity of reverse replay specifically tied to dopamine, or can other neuromodulators also modulate it?
- How does the hippocampus integrate reward prediction error signals with spatial information during replay?

---

## Related pages

- [[reverse_replay]]
- [[hippocampal_replay]]
- [[temporal_credit_assignment]]
- [[ventral_tegmental_area]]
- [[dopamine]]
- [[memory_consolidation]]
- [[sharp_wave_ripples]]
