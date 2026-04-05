# Temporal Credit Assignment

## Current understanding

Temporal credit assignment is the problem of associating distal events with outcomes that occur later in time—a fundamental challenge in reinforcement learning. In the hippocampus, temporal credit assignment is proposed to be solved through reverse replay: during sharp-wave ripple (SWR) events at reward locations, place cell sequences representing the preceding trajectory are reactivated in reverse order. This reverse reactivation, combined with dopamine signals at the reward location, allows value information to propagate backward along the trajectory, enabling place cells with fields distal from reward to become associated with reward value.

---

## Key evidence

- Reverse hippocampal replay rates track changes in reward magnitude—increasing at higher reward and decreasing at lower reward—while forward replay rates remain unchanged, supporting reverse replay's role in temporal credit assignment ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). This establishes the core prediction of the credit assignment hypothesis: that reverse replay specifically propagates reward information backward along trajectories.

- Forward and reverse hippocampal replay are functionally dissociable, with reverse replay mediating reward-based learning (temporal credit assignment) while forward replay supports planning or memory retrieval independent of reward ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). The bidirectional control within same stopping periods rules out behavioral confounds and establishes distinct computational roles.

- Reverse hippocampal replay encodes relative (adaptive) reward magnitude rather than absolute reward levels, matching the adaptive range coding of VTA dopamine neurons that would provide the reward signal for credit assignment ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). The correspondence between reverse replay and dopamine coding properties supports the proposed dopamine-replay interaction for credit assignment.

- Reverse replay can occur after a single traversal of a novel track, demonstrating that behavioral repetition is not strictly necessary for credit assignment-related replay, though experience-dependent plasticity enhances subsequent replay expression ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Foster & Wilson (2006) showed reverse replay after first experience; this supports credit assignment even with minimal experience.

- The number of reverse replays correlates with reward magnitude, suggesting salience signals bias replay content toward important experiences for credit assignment ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Ambrose et al. (2016) established reward-replay correlation; dopaminergic activation enhances replay likelihood (McNamara et al., 2014).

- Both forward and reverse replay are predominantly locally initiated, beginning at the animal's current position during awake stopping periods, supporting the hypothesis that reverse replay from reward locations propagates value information backward along the just-experienced trajectory ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Approximately 86% of replays in Experiment 1 and 78% in Experiment 2 were locally initiated.

---

## History of ideas

The temporal credit assignment problem was formally articulated in reinforcement learning theory (Sutton and Barto, 1998) as the challenge of attributing outcomes to preceding events when they are separated in time. In neuroscience, Foster and Wilson (2006) proposed that reverse replay in the hippocampus could solve this problem: by reactivating place cell sequences in reverse order at reward locations, value information could propagate backward along trajectories, allowing place cells distant from reward to become associated with reward value. This hypothesis was initially supported by the observation that reverse replay occurs at reward locations and propagates backward from the current position. However, direct evidence that reverse replay specifically (and not forward replay) is reward-sensitive was lacking until Ambrose et al. (2016) demonstrated that only reverse replay tracks reward magnitude changes, providing strong support for the temporal credit assignment hypothesis.

---

## Open questions

- What is the precise synaptic mechanism by which reverse replay pairs with dopamine signals to strengthen place-reward associations?
- Does spike-timing-dependent plasticity (STDP) modified by dopamine at CA3-CA1 synapses underlie the credit assignment mechanism?
- Can the temporal credit assignment mechanism account for learning over longer timescales beyond the immediately preceding trajectory?
- How does the brain handle credit assignment when multiple potential causes precede an outcome?

---

## Related pages

- [[reverse_replay]]
- [[forward_replay]]
- [[hippocampal_replay]]
- [[reinforcement_learning]]
- [[reward_processing]]
- [[ventral_tegmental_area]]
- [[memory_consolidation]]
