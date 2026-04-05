# Hippocampus CA1

## Current understanding

CA1 is the primary output region of the hippocampus, receiving input from CA3 via the Schaffer collaterals and from entorhinal cortex. It is the site where place cells show strong spatially-tuned firing and where sharp-wave ripple (SWR) events contain compressed sequential reactivation of place cell sequences.

---

## Key evidence

- Reverse hippocampal replay rates in CA1 track changes in reward magnitude—increasing at higher reward and decreasing at lower reward—while forward replay rates remain unchanged ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). This functional dissociation supports distinct roles: reverse replay for reward-based learning and forward replay for planning or memory retrieval.

- Forward and reverse hippocampal replay in CA1 are functionally dissociable, with reverse replay mediating reward-based learning while forward replay supports planning or memory retrieval independent of reward ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). The bidirectional control within same stopping periods shows forward replay unaffected by reward manipulation while reverse replay is strongly modulated.

- Reverse hippocampal replay in CA1 encodes relative (adaptive) reward magnitude rather than absolute reward levels, with rate changes reflecting reward value relative to the environment ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Increasing reward at one end simultaneously elevated reverse replay there and depressed it at the unchanged end.

- Reverse replay in CA1 is elevated after reward reinstatement, consistent with sensitivity to reward prediction error-like signals ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). When baseline reward was restored at a previously unrewarded location, reverse (but not forward) replay was significantly elevated (z = 3.35, p = 0.0049).

- Both forward and reverse replay in CA1 are predominantly locally initiated, beginning at the animal's current position during awake stopping periods ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Approximately 86% of replays in Experiment 1 and 78% in Experiment 2 were locally initiated.

- Sharp-wave ripple (SWR) rates in CA1 track reward magnitude changes, serving as a nonspecific marker of reward-related hippocampal activation ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). SWR rate increased significantly at 4× reward end (z = 5.24, p = 1.61 × 10⁻⁷) and decreased when reward removed (z = −6.66, p = 2.67 × 10⁻¹¹).

- CA1 place cells shift firing fields toward learned goal locations during spatial learning, with 79% of cells showing significant field movement toward at least one goal (similar to MEC grid cells). However, CA1 changes are more transient than MEC changes, suggesting higher lability of hippocampal memory traces compared to entorhinal cortex ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md)).

- CA1 exhibits global remapping (population-wide reorganization) during goal learning, in contrast to MEC which shows local remapping (field-specific changes). This reveals different computational strategies between hippocampus and entorhinal cortex for updating spatial representations when behaviorally relevant information changes ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md)).

- CA1 shows "flickering" dynamics—rapid alternation between pre-learning and post-learning spatial representations during goal learning, with no intermediate representations (KS test, P < 0.00001). CA1 reached plateau faster than MEC in goal flickering dynamics, suggesting faster initial reorganization in hippocampus despite more transient changes ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md)).

- CA1 population vector similarity shows no correlation with distance from goals (P = 1), unlike MEC where similarity is weaker around goals and positively correlates with distance. This indicates that CA1 spatial representations maintain consistent variability regardless of reward location, while MEC representations are more variable near rewarded locations ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md)).

---

## History of ideas

The discovery of reverse replay in CA1 by Foster and Wilson (2006) proposed it as a mechanism for temporal credit assignment—propagating reward information backward along trajectories. However, the functional relationship between forward and reverse replay remained unclear until Ambrose et al. (2016) demonstrated that only reverse replay is reward-sensitive, establishing a functional dissociation that supports distinct computational roles.

---

## Open questions

- What is the precise circuit mechanism linking VTA dopamine signals to the initiation of reverse replay?
- Do the same dissociations between forward and reverse replay hold in 2D environments or during active decision-making tasks?
- Is the rate of reverse replay itself functionally meaningful, or merely a byproduct of reward-triggered initiation?

---

## Related pages

- [[hippocampus]]
- [[hippocampal_replay]]
- [[place_cells]]
- [[sharp_wave_ripples]]
- [[reverse_replay]]
- [[forward_replay]]
- [[ventral_tegmental_area]]

- Goal-distance cells in CA1 (~16% of principal cells in bats) encode path proximity to the goal, while goal-direction cells (~19%) encode egocentric angle to the goal; ~5% conjunctively encode both ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))

- A subset of CA1 place cells (31.1%, 142/456 cells) fire as egocentric vector fields oriented toward goal-proximal "convergence sinks" (ConSinks), with population vector fields converging to a population ConSink close to the goal ([Ormond 2022](../../raw/summaries/ormond2022_goal_oriented_vector_fields.md))

- ConSink positions redistribute from the original goal to a new goal after goal switching, with cells moving their ConSinks significantly toward the new goal (Wilcoxon signed-rank, z = -2.48, p = 0.013); ConSinks move progressively closer to the goal with continued training ([Ormond 2022](../../raw/summaries/ormond2022_goal_oriented_vector_fields.md))

- 86.6% of ConSink cells (123/142) significantly encode at least one of relative direction, distance, or allocentric direction to the sink; 57% encode combinations sufficient to calculate the full goal direction vector ([Ormond 2022](../../raw/summaries/ormond2022_goal_oriented_vector_fields.md))

- Population firing rate in CA1 varies monotonically with angular deviation from the goal direction, forming a "fantail" pattern that provides sufficient information to choose between any available pair of platforms ([Ormond 2022](../../raw/summaries/ormond2022_goal_oriented_vector_fields.md))

- Before error choices in CA1, goal-directed firing rates are significantly reduced (z = 5.61, p = 1.97 × 10⁻⁸) and the fantail is rotated away from the goal, even before the animal knows which platforms will be offered, suggesting the firing predicts choice rather than merely accompanying movement ([Ormond 2022](../../raw/summaries/ormond2022_goal_oriented_vector_fields.md))

- ConSink tuning in CA1 is task-specific: only 13% of place cells show ConSink tuning during open-field foraging versus 31% during goal-directed navigation, and foraging ConSinks are not clustered around the navigation goal ([Ormond 2022](../../raw/summaries/ormond2022_goal_oriented_vector_fields.md))

- Dopamine (VTA→CA1 and LC→CA1) is required for place fields to shift toward goal locations; LC manipulation that induces goal overrepresentation does not affect task performance, dissociating map reorganization from overt behaviour ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))

- Place-field overrepresentation at goal locations occurs in CA1 (but not CA3) when trajectories are repeated AND the goal location must be memorised, but not in flexible place-navigation tasks or when goals are visibly cued with no memory demand ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))

- Predictive grid cells in MEC fire at the trough (~180°) of CA1 theta oscillations and contribute to theta sequences sweeping from current to future positions; removing predictive grid cell spikes significantly reduces future-position representation during descending theta phases ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- Disrupting spike synchronisation within theta cycles abolishes future-position representation in CA1, implicating coordinated assembly activity rather than single-cell coding for predictive spatial representation ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- Cross-correlogram analysis shows increased functional connectivity from predictive MEC grid cells to CA1 place cells when the grid field precedes the place field, suggesting directional spike transmission from entorhinal to hippocampal formation ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- Splitter cells in CA1, CA3, mEC, and SUB encode current route identity rather than goal identity per se; only ~0.5% of place cells show goal-specific (route-independent) firing ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))
