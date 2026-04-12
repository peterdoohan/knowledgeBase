---
source_file: vollan2024_theta_sweeps_entorhinal.md
paper_id: vollan2024_theta_sweeps_entorhinal
title: "Left–right-alternating theta sweeps in entorhinal–hippocampal maps of space"
authors:
  - "Abraham Z. Vollan"
  - "Richard J. Gardner"
  - "May-Britt Moser"
  - "Edvard I. Moser"
year: 2024
journal: Nature
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - open_field
  - linear_track
  - t_maze
  - foraging_task
methods:
  - neuropixels
  - bayesian_decoding
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - grid_cells
  - place_cells
  - theta_oscillations
  - theta_sweeps
  - theta_sequences
  - internal_direction_cells
  - head_direction_cells
  - conjunctive_cells
  - continuous_attractor_networks
  - path_integration
  - spatial_navigation
  - toroidal_topology
  - population_coding
  - neuropixels
  - rem_sleep
  - slow_wave_sleep
  - latent_manifold_tuning
  - spatial_sampling
  - vector_navigation
  - theta_phase_precession
key_citations:
  - burak2009_path_integration_grid_cells
  - johnson2007_hippocampus_decision
wiki_pages:
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
  - wiki/topics/sharp_wave_ripple_associated_place_cell_replay_in_spatial_memory_consolidation
---

### One-line summary

Grid cells and place cells encode left–right-alternating theta sweeps that sample the surrounding environment, including never-visited locations, through a coordinated circuit involving parasubiculum direction cells and continuous attractor network dynamics.

### Background & motivation

Place cells in the hippocampus and grid cells in the entorhinal cortex form a neural map of self-position essential for navigation. For these cells to support navigation, their representations must be dynamically related to surrounding locations. Previous studies demonstrated that hippocampal place cells exhibit theta-paced "forward sweeps" encoding trajectories from the animal's current location toward upcoming locations, particularly on linear tracks and mazes. However, these sweeps were constrained to previously visited or navigable paths. The question remained whether a more general mechanism exists for sampling the ambient environment, including never-visited locations, beyond the constraints of the animal's physical trajectory.

### Methods

- **Subjects**: 19 Long-Evans rats (18 male, 1 female) with Neuropixels probes targeting MEC–parasubiculum (16 rats), hippocampus (9 rats), or both (7 rats)
- **Recording**: Neuropixels 3A single-shank (8 rats) and 2.0 multi-shank probes (11 rats); 384–1,522 cells per session
- **Tasks**: Open-field foraging (1.5 m × 1.5 m arena), linear track (2.0 m), wagon-wheel track (circular with cross-bridges), m-shaped T-maze, and natural sleep recordings
- **Decoding**: Population vector (PV) correlation decoding, Bayesian decoding, and latent manifold tuning (LMT) model to extract position and direction signals
- **Sweep detection**: Sequence detection algorithm identifying near-linear trajectories spanning ≥4 time bins within theta cycles during locomotion (>15 cm/s)
- **Functional connectivity**: Cross-correlogram analysis to identify putative monosynaptic connections (0.7–4.7 ms peak latency, >5 SD baseline, P < 0.001)
- **Artificial agent simulation**: Self-driving and empirically-driven agents using overlap-minimization algorithms to predict sweep directions

### Key findings

- **Left–right-alternating sweeps**: In individual theta cycles, ensembles of grid cells and place cells encode position signals that sweep linearly outward from the animal's location, with sweep directions alternating stereotypically between left (~24°) and right (~24°) across successive theta cycles (79.8% of sweep triplets showed alternation vs. 61.1% shuffled)
- **Grid cell involvement**: Sweeps were stronger in grid cells than non-grid cells (28.5% vs. 13.4% of theta cycles, P = 0.001), with burst-firing grid cells (MEC layer II and parasubiculum) being the strongest carriers
- **Cross-module coordination**: Sweeps in different grid modules were mutually aligned (circular correlation r = 0.60, P < 0.001), pointing to the same side in 70.3% of theta cycles; sweep lengths scaled with grid module spacing (r = 0.95, P = 2.9 × 10⁻¹⁶), spanning ~20% of module spacing
- **Hippocampal sweeps**: Place cells also exhibited sweeps (43.7% of theta cycles), which were delayed relative to MEC sweeps by ~19 ms, suggesting propagation from entorhinal to hippocampal circuits
- **Internal direction signal**: A discrete population of parasubiculum cells (primarily theta-rhythmic, 34.9% of parasubiculum cells) encoded an "internal direction" signal that alternated left–right across theta cycles (86.1% alternation) and was aligned with sweep directions (circular correlation r = 0.66, absolute mean angle 4.4°)
- **Microcircuit for sweep generation**: Putative monosynaptic connections were identified from internal direction cells to conjunctive grid cells (0.11% of pairs) and from conjunctive grid cells to pure grid cells (0.38% of pairs); connected pairs showed aligned directional tuning and grid phase offsets matching the preferred direction of presynaptic conjunctive cells
- **Sweeps in never-visited space**: Sweeps extended into inaccessible locations beyond the animal's path (e.g., off elevated tracks, beyond arena walls), demonstrating experience-independent spatial sampling; individual grid cells showed tuning to unvisited locations
- **Sweeps during sleep**: Left–right-alternating sweeps and internal direction signals persisted during REM sleep (70.1% alternation), nested on longer behavioral timescale trajectories; during SWS, non-rhythmic sweep-like trajectories aligned with direction signals were observed
- **Optimal coverage algorithm**: An artificial agent selecting sweep directions to minimize overlap with previous coverage spontaneously generated left–right-alternating sweeps (alternation score 0.97 after convergence); the agent's predictions aligned with empirical sweep directions (correlation r = 0.36, P < 0.001 in all animals), and alternation increased with running speed and path straightness

### Computational framework

Continuous attractor network (CAN) models of grid cells, in which an activity bump is translated across an internally generated toroidal continuous attractor manifold based on external speed and direction inputs. The paper specifically references vector-based mechanisms where grid-cell position signals are translated by directional input causing phase shifts through layers of conjunctive grid cells. The findings support a model where internal direction cells (in parasubiculum) drive conjunctive grid cells, which in turn project asymmetrically to pure grid cells with appropriate grid phase offsets to generate sweep trajectories. The computational problem being solved is efficient coverage of surrounding space to build and maintain a continuous neural map independent of physical traversal.

### Prevailing model of the system under study

Prior to this work, the field understood that: (1) Grid cells generate a spatial coordinate system through continuous attractor dynamics on a toroidal manifold, with position updated by path integration; (2) Hippocampal place cells exhibit theta-phase precession and forward sweeps that encode trajectories along the animal's path; (3) In maze tasks, these sweeps alternately traversed upcoming arms at choice points, suggesting they might reflect deliberation over behavioral options based on previous experience; (4) Theta cycling between representations was observed in hippocampus during decision-making. The prevailing assumption was that sweeps were primarily involved in trajectory planning and were constrained to navigable, previously visited paths.

### What this paper contributes

This paper fundamentally reframes the function of theta sweeps in the entorhinal-hippocampal system:

1. **Generalized sampling mechanism**: Shows that sweeps are not limited to previously visited paths but extend into never-visited locations, including physically inaccessible spaces beyond arena walls or off elevated tracks. This demonstrates an experience-independent "look around" mechanism for spatial sampling.

2. **Left–right alternation as a default mode**: Establishes that sweeps stereotypically alternate between left and right (~24° from head axis) across successive theta cycles, rather than projecting forward along the path. This alternation is not goal-directed but instead follows an algorithm for optimal spatial coverage.

3. **Circuit mechanism**: Identifies the complete microcircuit generating sweeps: parasubiculum internal direction cells → conjunctive grid cells → pure grid cells, with functional connectivity showing aligned directional tuning and appropriate grid phase offsets.

4. **State-independence**: Shows that the sweep mechanism persists during REM sleep and darkness, decoupled from sensory input and locomotion, indicating it is a fundamental intrinsic property of the grid-cell system.

5. **Computational function**: Demonstrates that an artificial agent minimizing overlap with previous sweeps spontaneously generates left–right-alternating patterns, suggesting this alternation is an efficient algorithm for building continuous spatial maps without requiring physical traversal of all locations.

### Brain regions & systems

- **Medial entorhinal cortex (MEC)**: Contains grid cells organized in modules with distinct spatial scales; layer II contains bursty grid cells that are strongest carriers of sweep signals; layer III contains non-bursty grid cells with weaker sweep involvement
- **Parasubiculum**: Contains the internal direction cell population (85.6% of theta-rhythmic direction cells); these cells show broad head-direction tuning but sharp tuning to decoded internal direction; anatomically segregated from pure grid cells in MEC
- **Hippocampus (CA1/CA3)**: Contains place cells that exhibit sweeps delayed relative to MEC sweeps (~19 ms); sweeps extend into never-visited locations; likely inherit sweep signals from entorhinal inputs
- **Conjunctive grid × direction cells**: Primarily located in parasubiculum; serve as intermediate layer in sweep microcircuit, receiving internal direction input and projecting to pure grid cells

### Mechanistic insight

This paper provides strong mechanistic insight by identifying both the algorithm and neural circuit implementing theta sweeps.

**Computational level**: The brain solves the problem of building a continuous spatial map of the surrounding environment without requiring physical traversal of all locations. The solution is an efficient coverage algorithm that directs neural sampling (sweeps) to minimize overlap with previously sampled regions, which spontaneously produces left–right alternation as an optimal strategy.

**Algorithmic level**: The sweep mechanism is implemented through a three-stage circuit: (1) internal direction cells in parasubiculum generate an alternating directional signal (~20° left or right of head axis) that switches on each theta cycle; (2) these cells project to conjunctive grid cells with aligned directional tuning; (3) conjunctive cells project asymmetrically to pure grid cells, exciting cells with grid phases offset in the direction of the internal direction signal. This vector-integration mechanism translates the position representation across the grid-cell manifold to generate sweeps.

**Implementational level**: The circuit is anatomically segregated: internal direction cells and conjunctive cells are concentrated in parasubiculum (projecting to MEC layer II), while pure grid cells are found in both MEC layers II and III. Burst-firing grid cells (layer II) are the primary carriers of sweep signals. The theta rhythm provides the temporal framework for alternating activation, with individual cells showing theta-cycle skipping (firing on alternate cycles) as a consequence of the alternating sweep/direction signals.

### Limitations & open questions

- The mechanism generating the rigid left–right alternation remains unclear—whether it emerges from a hardwired central pattern generator circuit (as in spinal locomotor circuits or respiratory rhythms) or spontaneously from overlap-minimization via firing-rate adaptation
- The scalar component of the vector computation determining sweep length is unidentified—sweep length is not directly determined by running speed (sweeps persist during sleep), suggesting factors like internal direction input intensity or duration may be involved
- Whether sweeps can be volitionally controlled or flexibly aligned to goal locations with training remains unclear—the rigid alternation pattern suggests default spatial sampling, but goal-directed modulation may be possible
- The exact biophysical mechanisms implementing the attractor dynamics and phase shifts in the grid-cell network remain to be fully characterized
- Whether similar sweep mechanisms exist in other species or brain regions is unknown

### Connections & keywords

**Key citations**: O'Keefe & Dostrovsky (1971); O'Keefe & Nadel (1978); Hafting et al. (2005, 2008); Fuhs & Touretzky (2006); Burak & Fiete (2009); Stensola et al. (2012); Gardner et al. (2022); Kay et al. (2020); Johnson & Redish (2007); Skaggs et al. (1996); Buzsáki (1983); McNaughton et al. (2006); Sanders et al. (2015); Navratilova et al. (2012)

**Named models/frameworks**: Continuous attractor network (CAN) models; latent manifold tuning (LMT) model; vector-based navigation models; path integration; theta phase precession; theta sequences; toroidal manifold

**Brain regions**: Medial entorhinal cortex (MEC); parasubiculum; hippocampus (CA1, CA3); prefrontal cortex (mentioned); anterior thalamus (mentioned); postsubiculum (mentioned)

**Keywords**: grid cells; place cells; theta oscillations; theta sweeps; theta sequences; internal direction cells; head direction cells; conjunctive cells; continuous attractor networks; path integration; spatial navigation; toroidal topology; population coding; Neuropixels; REM sleep; slow-wave sleep; latent manifold tuning; spatial sampling; vector navigation; theta phase precession; theta cycle skipping; burst firing

### Related wiki pages
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
- [[wiki/topics/sharp_wave_ripple_associated_place_cell_replay_in_spatial_memory_consolidation|Sharp-wave ripple-associated place-cell replay in spatial memory consolidation]]
