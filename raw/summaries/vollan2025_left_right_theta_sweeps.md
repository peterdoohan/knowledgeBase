---
source_file: "vollan2025_left_right_theta_sweeps.md"
paper_id: "vollan2025_left_right_theta_sweeps"
title: "Left\u2013right-alternating theta sweeps in entorhinal\u2013hippocampal maps of space"
authors: "Abraham Z. Vollan, Richard J. Gardner, May-Britt Moser, Edvard I. Moser"
year: 2025
journal: "Nature"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
tasks: ["open_field", "linear_track", "foraging_task", "navigation_task"]
methods: ["neuropixels", "bayesian_decoding"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "medial_entorhinal_cortex"]
frameworks: ["attractor_networks"]
keywords: ["leftright", "alternating", "theta", "sweeps", "entorhinalhippocampal", "maps", "space"]
key_citations: ["burak2009_path_integration_grid_cells"]
---

### One-line summary

Grid cells and place cells encode left–right-alternating theta sweeps that sample ambient space, including never-visited locations, driven by an internal direction signal from parasubiculum cells that maximizes spatial coverage through an efficient algorithm.

### Background & motivation

Place cells and grid cells form a neural map of self-position, but how these cells dynamically sample surrounding locations beyond the animal's current path remains unclear. Previous studies showed forward theta sequences in hippocampal place cells during maze navigation, but these were constrained to travelled paths. The authors hypothesized that a general mechanism for sampling ambient space—potentially including never-visited locations—might exist within the entorhinal-hippocampal circuit.

### Methods

- **Subjects**: 19 Long-Evans rats (recordings from 16 rats with MEC-parasubiculum implants, 8 with hippocampal implants)
- **Recording**: High-site-count Neuropixels probes (384–1,522 cells per session) targeting MEC, parasubiculum, and hippocampus
- **Tasks**: Open-field foraging (1.5 m × 1.5 m), linear track (2.0 m), wagon-wheel maze, m-shaped maze, and sleep sessions
- **Decoding**: Population vector (PV) correlation decoding, Bayesian decoding, and latent manifold tuning (LMT) model to extract sweeps and internal direction signals
- **Sweep detection**: Sequence-detection algorithm identifying linear trajectories spanning ≥4 time bins within theta cycles
- **Functional connectivity**: Cross-correlogram analysis to identify putative monosynaptic connections between cell pairs
- **Agent simulation**: Artificial agent choosing sweep directions to minimize overlap with previous coverage traces

### Key findings

- **Left–right-alternating sweeps**: In individual theta cycles, grid cell and place cell ensembles encode position sweeps that sweep linearly outward from the animal's location, with direction alternating stereotypically between left and right across successive theta cycles (79.8% of triplets showed alternation vs. 61.1% for shuffled data)
- **Sweep geometry**: Sweeps directed forwards at 23.9° to either side of head axis; average length 22.5 cm (19.7% of grid module spacing); sweep length scaled with grid spacing (r = 0.95)
- **Coordination across modules**: Co-recorded grid modules showed mutually aligned sweep directions (70.3% pointing to same side; circular correlation r = 0.60)
- **Internal direction signal**: A population of theta-rhythmic direction-tuned cells in parasubiculum (85.6% of internal direction cells) encoded an alternating internal direction signal (86.1% alternation in triplets) that was aligned with sweep directions (circular correlation r = 0.66; 72.5% same side alignment)
- **Cell-type specificity**: Bursty grid cells (MEC layer II and parasubiculum) were stronger carriers of sweep signals than non-bursty grid cells (MEC layer III); theta cycle skipping was present in 53.7% of theta-modulated grid cells and 73.9% of theta-modulated direction-tuned cells
- **Functional circuit**: Putative monosynaptic connections identified: internal direction cells → conjunctive grid cells (0.11% of pairs; aligned directional tuning, r = 0.41) and conjunctive grid cells → pure grid cells (0.38% of pairs; grid phase offset aligned to conjunctive cell preferred direction, r = 0.62)
- **Extension to unvisited space**: Sweeps extended into never-visited locations along elevated tracks and beyond arena walls; individual grid cells showed tuning to unvisited locations; hippocampal sweeps also extended to unvisited locations (17.6% of sweeps terminated outside arena)
- **Persistence during sleep**: Left–right-alternating sweeps and internal direction signals persisted during REM sleep (70.1% alternation in triplets; sweep alignment with internal direction: 18.4° mean angle); during SWS, sweep-like trajectories occurred during up states but without rhythmic alternation (52.4% alternation)
- **Optimal coverage algorithm**: An artificial agent maximizing spatial coverage by choosing sweep directions that minimize overlap with previous sweeps spontaneously generated alternating sweeps (97% alternation score after convergence; 33° to either side of movement direction); agent's predicted directions aligned with empirical sweeps (r = 0.36, P < 0.001 in all 13 animals tested); alternation increased with running speed and path straightness

### Computational framework

The paper employs **continuous attractor network models** of grid cells, where position is represented as an activity bump on a toroidal manifold. The framework assumes that:
- Grid cells implement a vector-based navigation system where position offsets are expressed as vectors on the toroidal manifold
- Directional inputs translate the activity bump across the attractor via conjunctive grid × direction cells
- Theta oscillations discretize population activity into sequential packets that enable sweep trajectories

The paper also introduces an **optimal spatial sampling framework**, where an artificial agent chooses sweep directions to maximize coverage of ambient space. This algorithmic approach demonstrates that alternating left–right sweeps emerge naturally from a coverage-maximization objective without explicit alternation mechanisms.

### Prevailing model of the system under study

Prior to this study, the field understood that:
- Grid cells form a spatial coordinate system via periodic firing patterns organized in modules with different spatial scales
- Hippocampal place cells exhibit theta phase precession and forward sweeps during navigation, particularly at decision points
- Grid cells are thought to update position via path integration using speed and direction inputs
- Theta oscillations organize sequential neural activity, but the spatial extent and algorithmic purpose of theta sequences were unclear
- The mechanism generating theta phase precession and sequential firing remained debated (intrinsic vs. network mechanisms)

The prevailing view held that forward sweeps in place cells primarily serve navigational planning or deliberation over upcoming choices, extending along travelled or upcoming paths but not necessarily sampling unvisited ambient space systematically.

### What this paper contributes

This paper fundamentally transforms understanding of entorhinal-hippocampal spatial coding by demonstrating:

1. **A universal sampling mechanism**: Grid cells and place cells generate left–right-alternating sweeps that systematically sample ambient space, including never-visited locations, rather than just encoding the animal's current position or immediate path.

2. **Experience-independent mapping**: Sweeps extend into never-visited locations and persist during sleep, indicating they are generated by intrinsic circuit mechanisms rather than being tied to sensory experience or navigational goals.

3. **A circuit mechanism for sweep generation**: The paper identifies a functional microcircuit where internal direction cells in parasubiculum → conjunctive grid cells → pure grid cells in MEC, with asymmetric projections that translate activity bumps in the direction of the internal direction signal.

4. **An algorithmic explanation**: An artificial agent maximizing spatial coverage spontaneously generates alternating sweeps, suggesting that the entorhinal circuit implements an efficient coverage algorithm rather than goal-directed planning.

5. **Reconciliation of theta phenomena**: The findings provide a unified framework for understanding theta phase precession, theta cycle skipping, and forward sweeps as manifestations of the same underlying sweep mechanism.

### Brain regions & systems

- **Medial entorhinal cortex (MEC)**: Contains grid cells that are the primary carriers of the sweep signal, particularly bursty grid cells in layer II. Grid cells are organized into modules with different spatial scales. Sweeps in MEC are the source of sweeps in downstream hippocampus.

- **Parasubiculum**: Contains a discrete population of theta-rhythmic direction-tuned cells ("internal direction cells") that encode the alternating direction signal driving sweeps. These cells are anatomically segregated from pure grid cells, with 85.6% of internal direction cells located in parasubiculum. They show broad head-direction tuning but sharp tuning to the internal direction signal.

- **Hippocampus (CA1/CA3)**: Contains place cells that inherit sweeps from entorhinal cortex. Hippocampal sweeps are delayed by ~19 ms relative to MEC sweeps, suggesting propagation from entorhinal cortex. Place cells show tuning to never-visited locations beyond the arena boundaries.

- **Hippocampal-entorhinal circuit**: The functional connectivity analysis reveals a microcircuit: internal direction cells (parasubiculum) → conjunctive grid cells (MEC layer II/parasubiculum) → pure grid cells (MEC layer II/III).

### Mechanistic insight

This paper provides strong mechanistic insight by combining neural data, functional connectivity, and computational modeling:

**Computational level**: The brain solves the problem of efficiently mapping ambient space without requiring physical traversal of all locations. The solution is to generate internal sweeps that sample surrounding locations algorithmically.

**Algorithmic level**: The mechanism involves:
1. An internal direction signal that alternates between left and right on successive theta cycles (encoded by parasubiculum cells)
2. Translation of this directional signal into position sweeps via a vector-integration mechanism in grid cells
3. Conjunctive grid cells (encoding both position and direction) serve as the intermediate layer that converts directional inputs into position offsets

**Implementational level**: 
- Internal direction cells in parasubiculum project to conjunctive grid cells with aligned directional tuning (144 connected pairs, circular correlation r = 0.41 between tuning directions)
- Conjunctive grid cells project asymmetrically to pure grid cells, with grid phase offsets aligned to the conjunctive cell's preferred direction (85 connected pairs, correlation r = 0.62 between phase offset direction and preferred direction)
- Bursty grid cells in MEC layer II receive stronger projections from internal direction/conjunctive cells than non-bursty layer III grid cells (0.32% vs 0.007% connection rates, P = 3.0 × 10⁻⁷³)

The paper also demonstrates that an artificial agent maximizing spatial coverage spontaneously generates alternating sweeps, showing that the observed neural dynamics can emerge from a simple optimization principle without requiring explicit alternation mechanisms.

### Limitations & open questions

- The scalar component of the vector computation (what determines sweep length) remains unidentified; sweep length is not directly tied to running speed but may reflect intensity/duration of internal direction input
- The mechanism of directional alternation is not fully resolved—it could involve hardwired central pattern generator circuitry or emerge spontaneously from firing-rate adaptation mechanisms
- Whether sweeps can be flexibly aligned to goal locations with training remains unclear; the rigid sweep geometry suggests hardwired patterns, but previous studies show goal-directed sweeps in structured environments
- The causal role of the identified microcircuit (internal direction → conjunctive grid → pure grid) in generating sweeps was not tested with perturbations
- The relationship between sweep dynamics and navigation behavior remains largely correlational

### Connections & keywords

**Key citations**: O'Keefe & Dostrovsky (1971); Hafting et al. (2005); McNaughton et al. (2006); Skaggs et al. (1996); Kay et al. (2020); Gardner et al. (2022); Burak & Fiete (2009); Fuhs & Touretzky (2006)

**Named models or frameworks**: Continuous attractor network models; Latent manifold tuning (LMT) model; Vector-based navigation; Path integration; Theta phase precession; Theta cycle skipping

**Brain regions**: Medial entorhinal cortex (MEC); Parasubiculum; Hippocampus (CA1, CA3); Grid cells; Place cells; Head-direction cells

**Keywords**: theta oscillations, grid cells, place cells, spatial navigation, entorhinal cortex, hippocampus, theta sequences, internal direction, continuous attractor networks, vector integration, sleep, REM, spatial sampling, neural manifolds, Neuropixels
