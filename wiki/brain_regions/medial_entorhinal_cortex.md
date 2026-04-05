# Medial Entorhinal Cortex (MEC)

## Current understanding

The medial entorhinal cortex (MEC) is a key hub for spatial navigation and memory, containing grid cells that provide a regular hexagonal firing pattern across environments. Unlike the traditional view of grid cells as a rigid metric system, current understanding holds that the MEC cognitive map is dynamic and influenced by behaviorally relevant information such as reward locations.

---

## Key evidence

- Grid cells in MEC shift their firing fields toward learned goal locations, with 80-90% of cells showing significant field movement toward at least one goal (binomial test, P < 0.00001). Field attraction strength correlates with pre-probe distance to goal, with fields within ~30 cm showing attraction while fields beyond showed little detectable attraction (r = –0.192, P = 0.01225, Spearman). ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Grid scores in MEC are significantly lower in cheeseboard probes compared to open field (P < 0.00001, one-way ANOVA), independent of spatial sampling, trajectories, speed, or heading. The number of fields at goals increased (Fisher exact test, P = 0.0145) and mean distance from field centers to closest reward decreased (KS test, P = 0.01472), demonstrating that goal learning deforms the regular hexagonal grid structure. ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- MEC retains goal-related field reorganization overnight (using previous day's goal locations), while CA1 changes are more transient, suggesting different memory trace lability between entorhinal and hippocampal regions. MEC changes were more stable, indicating longer-lasting plasticity in the entorhinal cortex. ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- MEC exhibits local remapping (field-specific movement toward goals) while CA1 reorganizes through global remapping (population-wide reorganization). This dissociation reveals different computational strategies: MEC updates individual spatial representations locally while CA1 recodes the entire spatial map. ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- MEC shows "flickering" dynamics—rapid alternation between pre- and post-probe spatial representations during learning, with no intermediate representations (KS test, P < 0.00001). MEC flickering scores shifted toward more positive values during learning, suggesting dynamic competition between multiple coexisting spatial maps. ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- MEC population vector similarity is weaker around goals than away from them (P = 0.0003, t test) and positively correlated with distance from goals (P < 0.00001), while CA1 shows no such correlation (P = 1). This indicates that MEC spatial representations are more variable near rewarded locations. ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- MEC activity increase at goal locations correlates with subsequent memory retention (r = 0.77, P = 0.002), linking entorhinal reorganization directly to behavioral performance and demonstrating that goal-specific MEC activity supports memory formation. ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- A subset of MEC neurons — termed predictive grid cells — fire with grid fields shifted ahead of the animal's current position, encoding future locations. These cells had maximum gridness at a mean forward shift of 22.5 ± 10.2 cm (~0.27 of grid spacing) and fired at the trough (~180°) of CA1 theta oscillations ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- Predictive grid cells are predominantly located in MEC layer 3, while phase-precessing cells are in layer 2 and phase-locked cells are in layer 3 with opposite phase preference. The three cell types collectively produce within-theta-cycle sequences from current to future positions ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- Bayesian decoding using the three MEC cell types together reveals theta sequences sweeping from current to future positions; removing predictive grid cell spikes significantly reduces representation of future positions during descending theta phases. This establishes predictive grid cells as a key contributor to prospective spatial coding ([Ouchi 2024](../../raw/summaries/ouchi2024_predictive_grid_coding.md))

- The medial entorhinal cortex encodes compositional predictive maps through translation- and rotation-invariant object representations (Predictive Object Representations, PORs), reconciling flexibility and efficiency. Object vector cells (~30% of MEC cells) encode PORs as compositional building blocks, while grid cells encode basis functions (eigenvectors) of the open-space predictive map ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- The compositional cognitive map model predicts local (not global) remapping of grid cells when barriers/goals are introduced, consistent with empirical data from wall removal, home cage introduction, and goal learning experiments. This resolves a key puzzle that successor representation models could not explain ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- Grid cells in MEC implement a residue number system (modulo code) for position representation, with capacity to uniquely encode ~2000m range at 6cm resolution using only ~5×10^4 neurons ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

- Position updating via path integration is carry-free in the MEC: each grid lattice can independently add velocity-derived displacement signals without inter-lattice communication, even when phases wrap around ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

- Continuous attractor networks of ~10^4 neurons can accurately integrate velocity inputs with <0.1 cm/m error over 260m trajectories, producing stable grid responses over behaviorally relevant timescales of 1-10 minutes ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- Path integration accuracy in MEC scales with network size and is limited by diffusive noise: D_trans ∝ CV²/N. Sub-Poisson spiking (CV < 1) observed in real dMEC recordings extends coherent integration time quadratically ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- fMRI adaptation in human entorhinal cortex decreases monotonically with link distance on implicit graphs, recovering graph topology (r = 0.65, p = 0.003) even without explicit awareness of structure ([Garvert 2017](../../raw/summaries/garvert2017_relational_knowledge_maps.md))

- The neural metric for relational knowledge in entorhinal cortex follows successor representation/communicability rather than Euclidean or link distance, indicating the system warps relational space according to expected future visitation ([Garvert 2017](../../raw/summaries/garvert2017_relational_knowledge_maps.md))

- Both humans and rats navigate using successor representation strategies rather than pure model-based or model-free approaches, with SR agent providing best fit for both species (70% human trials, 60% rat trials) ([de Cothi 2022](../../raw/summaries/decothi2022_predictive_spatial_navigation.md))

- Grid cell modules in MEC implement a toroidal continuous attractor, forming a 2-dimensional torus invariant across environments, sleep/wake states, and time. Grid cell co-activity preserved across sleep while place cell co-activity is not validates continuous attractor models and rules out place-cell-primacy models. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

---

## History of ideas

Grid cells were discovered by Hafting et al. (2005) and initially hypothesized to provide a universal invariant metric for spatial cognition due to their regular hexagonal firing fields. This view held that grid cells served a narrower role than hippocampal place cells, providing rigid spatial coordinates resistant to nonspatial influences. However, Boccara et al. (2019) fundamentally challenged this view by demonstrating that grid cells shift their firing fields toward learned goals, indicating that the entorhinal cognitive map is dynamically shaped by behaviorally relevant information, not just environmental geometry.

---

## Open questions

- What are the specific cellular or synaptic mechanisms underlying grid field attraction (e.g., synaptic plasticity, changes in local inhibition, or neuromodulatory influences)?
- What is the causal relationship between MEC and CA1 reorganization during goal learning—which region drives the changes?
- Do grid field attraction effects generalize to other types of behaviorally relevant information beyond reward locations?
- What are the computational implications of flickering dynamics for learning and decision-making?

---

## Related pages

- [[hippocampus_ca1]]
- [[place_cells]]
- [[grid_cells]]
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

- The medial entorhinal cortex encodes compositional predictive maps through Predictive Object Representations (PORs)—compact, translation- and rotation-invariant matrices representing objects as perturbations to open space. Using the Woodbury matrix identity, compositional predictive maps are computed by adding low-rank POR correction terms to baseline open-space map; complexity scales with object size (O³) rather than environment size (S³) ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- Object vector cells in MEC (~30% of spatially tuned cells) encode PORs, serving as compositional building blocks that are translation- and rotation-invariant, generalize across objects, and are experience-independent ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- Grid cells encode basis functions (eigenvectors) of the compositional predictive map, with POR perturbations projected onto this basis predicting local (not global) remapping when barriers or goals are introduced ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- The compositional framework enables efficient planning via simple matrix-vector multiplication, performing comparably to complete ground-truth planners (relative path length 1.09 with updates) and substantially outperforming successor representation models ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- The learning algorithm for refining combined PORs operates in object-space rather than state-space, making it computationally tractable compared to temporal-difference learning of successor representations ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- The model predicts that grid cells should show local remapping near introduced barriers or goals, with preserved patterns in distal locations, consistent with empirical observations from wall removal, home cage introduction, and goal learning experiments ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- A single-layer neural network with non-negative Hebbian weights learning from place cell inputs spontaneously converges to hexagonal grid cell firing patterns, providing a mechanistic account of grid cell formation driven by hippocampal feedback ([Dordek 2016](../../raw/summaries/dordek2016_grid_cells_nonnegative_pca.md))

- Non-negativity and zero-mean input are necessary conditions for hexagonal grid formation; 2D Gaussian inputs (non-zero-mean) fail to produce grids while zero-mean inputs (derivatives, Mexican hats, adaptation) succeed ([Dordek 2016](../../raw/summaries/dordek2016_grid_cells_nonnegative_pca.md))

- Grid spacing scales linearly with place field width following S = 7.5σ + 0.85, predicting that large-field place cells drive wide-spacing grid cells ([Dordek 2016](../../raw/summaries/dordek2016_grid_cells_nonnegative_pca.md))

- Hierarchical multi-output network produces grid modules with spacing ratio ~√2, consistent with experimental observations from Stensola et al. 2012 ([Dordek 2016](../../raw/summaries/dordek2016_grid_cells_nonnegative_pca.md))

- Three minimal constraints — actionability, biological feasibility, and functional discriminability — uniquely produce multiple modules of hexagonal grid cells from first principles ([Dorrell 2023](../../raw/summaries/dorrell2023_actionable_grid_constraints.md))

- Non-negativity forces lattice tuning curves while occupancy/resolution constraints select hexagons from all lattices; Fourier analysis shows hexagonal k-lattice achieves higher objective value (0.2558) than square (≤0.25) ([Dorrell 2023](../../raw/summaries/dorrell2023_actionable_grid_constraints.md))

- Optimal inter-module angular offset is small (~4°) to minimize harmonic overlap between frequency lattices, matching observations from Stensola et al. 2012 ([Dorrell 2023](../../raw/summaries/dorrell2023_actionable_grid_constraints.md))

- Grid frequency structure adapts to environment geometry — rectangular rooms produce grids tiling along cardinal axes, matching stable/shifting cell observations from Stensola et al. 2012, 2015 ([Dorrell 2023](../../raw/summaries/dorrell2023_actionable_grid_constraints.md))

- A single-layer neural network with non-negative Hebbian weights learning from place cell inputs spontaneously converges to hexagonal grid cell firing patterns, providing a mechanistic account of grid cell formation driven by hippocampal feedback ([Dordek 2016](../../raw/summaries/dordek2016_grid_cells_nonnegative_pca.md))

- Non-negativity and zero-mean input are necessary conditions for hexagonal grid formation; 2D Gaussian inputs (non-zero-mean) fail to produce grids while zero-mean inputs (derivatives, Mexican hats, adaptation) succeed ([Dordek 2016](../../raw/summaries/dordek2016_grid_cells_nonnegative_pca.md))

- Grid spacing scales linearly with place field width following S = 7.5σ + 0.85, predicting that large-field place cells drive wide-spacing grid cells ([Dordek 2016](../../raw/summaries/dordek2016_grid_cells_nonnegative_pca.md))

- Three minimal constraints — actionability, biological feasibility, and functional discriminability — uniquely produce multiple modules of hexagonal grid cells from first principles ([Dorrell 2023](../../raw/summaries/dorrell2023_actionable_grid_constraints.md))

- Non-negativity forces lattice tuning curves while occupancy/resolution constraints select hexagons from all lattices; Fourier analysis shows hexagonal k-lattice achieves higher objective value (0.2558) than square (≤0.25) ([Dorrell 2023](../../raw/summaries/dorrell2023_actionable_grid_constraints.md))

- Optimal inter-module angular offset is small (~4°) to minimize harmonic overlap between frequency lattices, matching observations from Stensola et al. 2012 ([Dorrell 2023](../../raw/summaries/dorrell2023_actionable_grid_constraints.md))
