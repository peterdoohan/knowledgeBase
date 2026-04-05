# Place Cells

## Current understanding

Place cells are pyramidal neurons in the hippocampus (primarily CA1 and CA3) that fire selectively when an animal occupies specific locations in space, called place fields. During behavior, place cells fire in sequences that encode trajectories through space. During sharp-wave ripple (SWR) events, these sequences are reactivated in time-compressed form as replay, which can occur in the same order as experienced (forward replay) or in reverse order (reverse replay). Place cell sequences serve as the substrate for both memory consolidation and planning.

---

## Key evidence

- Both forward and reverse replay are predominantly locally initiated, beginning at the animal's current position during awake stopping periods ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Approximately 86% of replays in Experiment 1 and 78% in Experiment 2 were locally initiated, suggesting place cell sequences propagate from the current location regardless of replay direction.

- Reverse replay of hippocampal place cells is uniquely modulated by changing reward magnitude, establishing a functional dissociation between the two directions of awake replay during sharp-wave ripples ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). This modulation suggests that place cell sequences are not simply reactivated uniformly but are selectively engaged depending on computational demands.

- Place cells encode the successor representation matrix, with individual place fields corresponding to columns of the SR matrix; this predictive map framework explains key place field properties: radial symmetry in open fields, geometric distortion around barriers, skew in the direction of travel, and reward-proximal clustering — all consistent with the SR model of Stachenfeld et al. (2017) that reframes place cells from simple location encoders to predictive state representations ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- The "preplay" phenomenon—where ripple sequences before novel experience match subsequent place cell firing order—remains controversial; while Dragoi & Tonegawa (2011) reported preplay suggesting pre-configured maps, subsequent studies found no evidence when controlling for experience-dependent plasticity, leading Grosmark & Buzsáki (2016) to propose a hybrid model with "rigid" pre-configured cells and "plastic" experience-dependent cells ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)).

- Hippocampal place cells may implement a non-metric place-label readout of the grid cell code, acting as sparse combinatorial labels derived from grid cell phase inputs rather than direct metric encoders ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

- An equivalent place-cell code covering a (2000m)^2 area at 6cm resolution would require ~10^10 neurons, compared to only ~5×10^4 grid cells in the MEC, demonstrating that place cells cannot be the primary high-capacity spatial representation for ecologically relevant scales ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

---

## History of ideas

Place cells were discovered by John O'Keefe in the 1970s, revealing that the hippocampus contains a cognitive map of space. The discovery that place cell sequences are reactivated during sleep and awake pauses (replay) came later, suggesting a mechanism for memory consolidation. The existence of both forward and reverse replay was demonstrated by Diba and Buzsáki (2007), and Foster and Wilson (2006) proposed that reverse replay specifically serves temporal credit assignment. Ambrose et al. (2016) confirmed this functional distinction by showing that reverse replay is selectively modulated by reward, while forward replay is reward-insensitive.

---

## Open questions

- How are place cell sequences organized to support both forward and reverse replay from the same starting position?
- What determines whether a given SWR event will contain forward vs. reverse replay?
- Do place cells in other hippocampal subregions (CA3, DG) show the same directional replay properties?

---

## Related pages

- [[hippocampal_replay]]
- [[reverse_replay]]
- [[forward_replay]]
- [[sharp_wave_ripples]]
- [[hippocampus_ca1]]
- [[hippocampus]]

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
