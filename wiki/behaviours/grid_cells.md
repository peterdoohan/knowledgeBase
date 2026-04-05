# Grid Cells

## Current understanding

Grid cells are a class of neurons primarily found in the medial entorhinal cortex (MEC) that exhibit striking regular hexagonal firing patterns tessellating the environment. Traditionally viewed as providing a universal invariant metric for spatial cognition, current understanding recognizes that grid cells participate in mnemonic coding beyond simple spatial metrics—their firing fields shift toward behaviorally relevant locations such as learned goals, causing dynamic deformations of the spatial map during learning.

---

## Key evidence

- Grid cells in the medial entorhinal cortex shift their firing fields toward learned goal locations during spatial learning, with 80-90% of grid cells showing significant field movement toward at least one goal (binomial test, P < 0.00001). This demonstrates that grid cells encode behaviorally relevant information beyond simple spatial position ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Grid scores (measuring hexagonal regularity) are significantly lower in environments containing learned reward locations compared to open field (P < 0.00001, one-way ANOVA), independent of spatial sampling, trajectories, speed, or heading. The number of fields at goals increased (Fisher exact test, P = 0.0145) and mean distance from field centers to closest reward decreased (KS test, P = 0.01472), demonstrating that goal learning deforms the regular hexagonal grid structure ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Field attraction strength in grid cells correlates with pre-probe distance to goal: fields within ~30 cm showed attraction, while fields beyond showed little detectable attraction (r = –0.192, P = 0.01225, Spearman). This distance-dependent attraction suggests an attractor-like mechanism where goal locations create basins of influence on nearby grid fields ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Grid cell field reorganization in MEC is retained overnight (using previous day's goal locations), while CA1 place cell changes are more transient. This indicates that grid cell plasticity has different timescales than hippocampal plasticity, with more stable memory traces in entorhinal cortex ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Grid cells exhibit local remapping (field-specific movement toward goals) in contrast to CA1 place cells which show global remapping (population-wide reorganization). This dissociation indicates that grid cells update spatial representations through localized field shifts while place cells recode the entire map ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Grid cells show "flickering" dynamics—rapid alternation between pre- and post-learning spatial representations during learning, with no intermediate representations (KS test, P < 0.00001). MEC flickering scores shifted toward more positive values during learning, suggesting dynamic competition between multiple coexisting spatial maps ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Grid cell population vector similarity in MEC is weaker around goals than away from them (P = 0.0003, t test) and positively correlates with distance from goals (P < 0.00001), indicating that grid representations are more variable near rewarded locations. Grid cell activity increase at goals correlates with memory retention (r = 0.77, P = 0.002), linking grid reorganization to behavioral performance ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Grid cells implement a residue number system (modulo code) for position that is combinatorially large in capacity, carry-free for arithmetic position updating, and vastly more efficient than place-cell-like representations ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

- With conservative parameters (N=12 lattices, periods 30-74cm, phase resolution δ_φ=0.2), the modulo code uniquely represents a ~2000m range with 6cm resolution per linear dimension, consistent with rat foraging ranges ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

- The modulo code requires only ~5×10^4 neurons to cover a (2000m)^2 area at 6cm resolution; an equivalent place-cell code would require ~10^10 neurons for the same range ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

- Position updating via path integration is carry-free: each lattice can independently and in parallel add velocity-derived displacement signals without inter-lattice communication, even when phases wrap around ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

- dMEC population vectors decorrelate non-monotonically with distance beyond ~one blob width, meaning metric distance cannot be linearly read out from the grid cell code at large scales ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

---

## History of ideas

Grid cells were discovered by Hafting et al. (2005) in the medial entorhinal cortex of rats. The striking regularity of their hexagonal firing patterns led to the hypothesis that they provide a universal invariant metric for spatial cognition—a rigid coordinate system that would support navigation across all environments. This view positioned grid cells as having a narrower role than hippocampal place cells, which were known to encode multimodal information beyond space. Early evidence that environmental geometry could distort grid structure (Stensola et al., 2015) suggested some flexibility, but the prevailing model held that grid cells were primarily spatial metric encoders. Boccara et al. (2019) fundamentally challenged this view by demonstrating that grid cells shift their firing fields toward learned goal locations, indicating that grid cells encode behaviorally relevant nonspatial information and that the entorhinal cognitive map is dynamically shaped by learning.

---

## Open questions

- What are the specific cellular or synaptic mechanisms underlying grid field attraction (e.g., synaptic plasticity, changes in local inhibition, or neuromodulatory influences)?
- Does grid field attraction generalize to other types of behaviorally relevant information beyond reward locations?
- What is the causal relationship between grid cell reorganization and behavioral performance during navigation?
- How do grid cells interact with other cell types in MEC (e.g., head direction cells, border cells) during goal learning?
- What are the computational implications of grid field flickering dynamics for learning and decision-making?

---

## Related pages

- [[medial_entorhinal_cortex]] (this page's parent region)
- [[hippocampus_ca1]]
- [[hippocampus]]
- [[place_cells]]
- [[cognitive_map]]
- [[spatial_navigation]]
- [[attractor_networks]]
- [[goal_directed_behaviour]]
- [[memory_consolidation]]

- A distinct population of MEC neurons, termed predictive grid cells, have grid firing fields shifted ahead of the animal's current position by ~22.5 cm (~0.27 of grid spacing), encoding future locations. These cells fire at the trough (~180°) of CA1 theta oscillations and are predominantly located in MEC layer 3 ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- Predictive grid cells, phase-precessing cells, and phase-locked cells together produce theta sequences sweeping from current to future positions across each theta cycle; removing predictive grid cell spikes significantly reduces future-position representation during descending theta phases ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- Disrupting spike synchronisation within theta cycles abolishes future-position representation, implicating coordinated assembly activity rather than single-cell coding for predictive spatial representation ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- Cross-correlogram analysis shows increased functional connectivity from predictive MEC grid cells to CA1 place cells when the grid field precedes the place field, suggesting directional spike transmission from entorhinal to hippocampal formation ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- Predictive coding properties of MEC cells are preserved across goal-directed and random-foraging tasks, with grid spacing rescaling but position-shift bias and phase preferences maintained ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- The medial entorhinal cortex encodes compositional predictive maps through Predictive Object Representations (PORs)—compact, translation- and rotation-invariant matrices representing objects as perturbations to open space ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- Object vector cells in MEC (~30% of spatially tuned cells) encode PORs, serving as compositional building blocks that are translation- and rotation-invariant, generalize across objects, and are experience-independent ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- Grid cells encode basis functions (eigenvectors) of the compositional predictive map, with POR perturbations projected onto this basis predicting local (not global) remapping when barriers or goals are introduced ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))
