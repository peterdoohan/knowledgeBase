---
source_file: butler2019_reward_locations_entorhinal_maps.md
paper_id: butler2019_reward_locations_entorhinal_maps
title: "Remembered reward locations restructure entorhinal spatial maps"
authors:
  - "William N. Butler"
  - "Kiah Hardcastle"
  - "Lisa M. Giocomo"
year: 2019
journal: Science
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - foraging_task
methods:
  - tetrode_recording
  - bayesian_decoding
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - mixed_selectivity
keywords:
  - grid_cells
  - entorhinal_cortex
  - spatial_remapping
  - reward_location
  - goal_directed_navigation
  - head_direction_cells
  - border_cells
  - bayesian_decoding
  - rate_remapping
  - spatial_memory
  - navigational_strategy
  - cognitive_map
  - remembered
  - reward
  - locations
  - restructure
  - entorhinal
  - spatial
  - maps
---

### One-line summary

Entorhinal spatial maps in rats restructure to incorporate a learned reward location during goal-directed navigation, improving positional decoding accuracy near that location.

---

### Background & motivation

The medial entorhinal cortex (MEC) contains neurons — grid cells, head direction cells, border cells, and other spatial cells — that provide maplike representations of space. Early work proposed that MEC codes were context-independent, in contrast to the context-sensitive hippocampal place cells. More recent work revealed that MEC spatial codes are flexible, but this flexibility had primarily been studied during random foraging. Whether ethologically relevant, goal-directed navigation — which requires recalling and navigating to a remembered reward location — also shapes MEC representations was unknown. This paper fills that gap by directly comparing MEC coding between free foraging and a spatial memory task in the same rats and environments.

---

### Methods

- **Subjects**: Seven rats implanted with tetrodes targeting MEC and surrounding areas.
- **Task design**: Rats explored two distinct arenas (1.5 m x 1.5 m) in the same session. ENV1 (black walls, lemon scent): free foraging for scattered food. ENV2 (white walls, vanilla scent): spatial memory task — rats navigated to a remembered, unmarked 20 cm x 20 cm reward zone upon an auditory cue; between trials, they also foraged freely. Control animals (n = 3 rats) performed free foraging in both environments.
- **Training**: Animals were trained to criterion (mean 15 sessions; range 8–24), taking rapid, direct paths to the reward zone after training. Reward trials occurred ≥10 times per session.
- **Neural recordings**: 778 cells were recorded in both environments. Cells were classified as encoding position (P), head direction (H), or running speed (S); P-encoding cells further classified as grid, border, or nongrid spatial cells.
- **Analyses**: Grid pattern orientation, spacing, ellipticity, and translation were quantified between environments. Firing rate as a function of distance from the reward zone was analysed for grid and nongrid cells. A Bayesian decoder estimated position from simultaneously recorded neurons across 43 sessions to assess whether reward-related remapping improved spatial decoding. Task-trajectory versus no-task-trajectory comparisons within ENV2 controlled for movement-related confounds. Data were downsampled to match speed and position occupancy between environments.

---

### Key findings

- Grid cells reorganized between ENV1 and ENV2: median orientation change 12.53° (P = 1.12 × 10^−12); small decrease in grid spacing (P = 0.015); reduced ellipticity (P = 0.006); grid pattern translation was also observed. Co-recorded grid cells changed coherently and maintained phase offsets.
- Control animals (same task in both environments) showed grid translation but not orientation, spacing, or ellipticity changes, confirming that task demands drive the reorganization.
- Head direction cells coherently rotated preferred directions between environments (70/132 cells significantly changed; P < 0.002), and HD rotations correlated with grid orientation rotations (r = 0.70, P = 0.02 when averaged within sessions).
- Border cells predominantly remapped (24/36) between environments, mainly through rotations.
- Nongrid spatial cells showed more remapping in task-trained animals versus controls (proportions test P = 3 × 10^−5).
- Grid and nongrid spatial cells showed increased relative firing rates near the reward zone in ENV2 versus ENV1 (signed-rank test: grid P = 0.0025; nongrid P = 5 × 10^−4). The grid field with the highest firing rate was closer to the reward zone in ENV2 (P = 0.01), and peak firing rate of fields near the reward zone was higher in ENV2 (P = 0.01).
- Nongrid spatial cells remapped heterogeneously into four functional groups: cells shifting fields toward the reward (group I), away from reward in ENV1 (group II), acquiring new fields near reward only in ENV2 (group III), and cells with unstructured spatial tuning that fired preferentially near the reward (group IV). 159/271 nongrid cells showed reward preference.
- Reward-related firing increases were present on both task and no-task trajectories within ENV2, indicating persistent long-term map restructuring rather than trajectory-specific coding.
- Bayesian decoding accuracy was significantly higher near the reward zone in ENV2 versus ENV1 (ENV2 slope > ENV1 slope in 27/43 sessions, median slope difference = 1 × 10^−3, signed-rank P = 0.042). Decoding error was lower within 30 cm of the reward-zone center (median difference = −4.3 cm, P = 0.028). Reward-related decoding improvement did not consistently covary with moment-to-moment task performance.

---

### Computational framework

The paper does not develop a formal computational model. However, it employs Bayesian decoding as an analysis tool: a Bayesian decoder uses the ensemble activity of simultaneously recorded MEC neurons to estimate the animal's position, quantifying how spatial coding quality varies as a function of distance from the reward zone.

The broader theoretical framing draws on the idea that grid cells provide unique combinations of spatial firing patterns that downstream neurons could use for vector navigation — computing the distance and direction between the animal's current position and a goal location. The paper's results are most directly relevant to reinforcement-learning and cognitive-map frameworks: they show that navigational experience (specifically, goal-directed spatial memory retrieval) reshapes the metric structure of MEC representations and concentrates representational precision at behaviourally important locations.

---

### Prevailing model of the system under study

The paper's introduction outlines two phases of thinking about MEC. The original view held a strong dissociation: hippocampal representations are sensitive to contextual features (and support remapping between environments), while MEC provides a context-independent, stable spatial scaffold — a universal metric for position, head direction, and running speed regardless of context. This model treated MEC as an allocentric coordinate system that the hippocampus reads out and contextualises.

Subsequent work (cited as references 6, 11–13) revised this view by demonstrating that MEC spatial codes can be flexible and adaptive (e.g., grid rescaling, rotation in response to environmental manipulations). However, even in the revised view, MEC flexibility had been characterised almost exclusively during random foraging. The degree to which goal-directed behaviour and remembered reward locations could reshape MEC representations remained an open question — the working assumption being that such influences, if present, would be modest or restricted to hippocampus.

---

### What this paper contributes

The paper demonstrates that remembered reward locations produce systematic, long-term restructuring of the entire MEC spatial map — not just in nongrid cells but in grid cells, head direction cells, and border cells as a coherent ensemble. This has two key implications:

1. MEC representations are not merely a context-free metric scaffold; they integrate task-relevant information (specifically, learned reward locations) to produce behaviourally specialised maps. Different navigational demands generate distinct long-term entorhinal map states.
2. This restructuring has functional consequences: Bayesian decoding of position is specifically improved near the reward zone in ENV2, implying that the representational changes enhance the precision of spatial information available to downstream regions precisely where accuracy matters most for goal-directed navigation.

Before this paper, it could only be speculated that MEC might incorporate reward-related information. The paper provides direct neural evidence that it does so, and that the effect is spatially localised, persistent (not trajectory-specific), and behaviourally consequential.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — primary recording site; shown to restructure its spatial map (grid, head direction, border, and nongrid spatial cells) in response to a learned reward location, improving positional decoding near the reward.
- **Surrounding cortical areas** — tetrodes also targeted regions adjacent to MEC; not separately analysed in the main text.
- **Hippocampus** — mentioned as a comparator system for contextual remapping, and as a downstream recipient of MEC spatial codes; not directly recorded.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight at the algorithmic and implementational levels, though the implementational level remains partial.

**Computational level**: The brain is solving the problem of constructing a goal-relevant spatial representation — one that allocates more representational precision near a remembered reward location. This serves goal-directed navigation by providing a sharper positional signal exactly where navigational accuracy matters.

**Algorithmic level**: The MEC achieves this by simultaneously executing two restructuring operations: (1) a global map reorganisation (grid rotation, rescaling, translation; coherent HD and border cell remapping) that distinguishes the task environment from the free-foraging environment as a discrete map state; and (2) a local rate-remapping that elevates firing rates near the reward zone within that map state. These two mechanisms together concentrate representational information at the reward location. The effect is persistent throughout ENV2 sessions (present on non-task as well as task trajectories), indicating that map restructuring is a long-term contextual memory rather than a transient task-execution signal. Bayesian decoding confirms that the restructuring translates into a functional precision gain.

**Implementational level**: The paper identifies that grid cells, head direction cells, border cells, and nongrid spatial cells all participate coherently — co-recorded grid cells maintain phase offsets while rotating and translating together, and HD cell rotations correlate with grid cell rotations. This coherence across cell types suggests a circuit-level mechanism (shared inputs or attractor dynamics) rather than independent cell-by-cell plasticity. However, the specific cell types, neuromodulators, or synaptic mechanisms underlying the restructuring are not addressed.

---

### Limitations & open questions

- The paper records during well-trained performance (post-criterion); how and when during learning the map restructuring emerges is unknown.
- The precise parameters of restructuring (magnitude of rotation, degree of reward-localized firing) may depend on task familiarity or experience history, as the authors acknowledge citing concurrent work (Boccara et al., 2019).
- The paper demonstrates that restructuring persists throughout ENV2 sessions (on non-task trajectories), but does not fully characterise how long this map state persists across days or after the task is extinguished.
- The circuit mechanism driving the reorganisation — which inputs to MEC carry reward or task-context signals, and which plasticity rules implement the map change — is not addressed.
- Whether the decoding improvement near the reward zone actually translates into improved navigational performance (e.g., faster or more accurate paths) is not directly shown; reward-related decoding did not consistently covary with moment-to-moment task performance.
- The study uses a single reward-zone location per animal; whether multiple reward locations would produce multiple local overrepresentations, or interact, is untested.

---

### Connections & keywords

**Key citations**:
- Hafting et al., Nature 2005 (original grid cell discovery)
- Sargolini et al., Science 2006 (conjunctive grid x HD cells in MEC)
- Solstad et al., Science 2008 (border cells in MEC)
- Kropff et al., Nature 2015 (speed cells in MEC)
- Diehl et al., Neuron 2017 (context-dependent MEC remapping)
- Hardcastle et al., Neuron 2017 (mixed selectivity in MEC)
- Krupic et al., Nature 2015 (environmental geometry shapes grid patterns)
- Stensola et al., Nature 2012 (grid cell modules)
- Stensola et al., Nature 2015 (self-organised limit-set grids)
- Fyhn et al., Nature 2007 (grid cell global remapping across environments)
- Boccara et al., Science 2019 (concurrent study on goal-directed MEC coding)
- Bush et al., Neuron 2015 (vector navigation model)

**Named models or frameworks**:
- Bayesian population decoding (used as analysis tool)
- Grid cell module framework (Stensola et al.)
- Vector navigation (theoretical framework motivating functional significance)

**Brain regions**:
- Medial entorhinal cortex (MEC)
- Hippocampus (comparator; not directly recorded)

**Keywords**:
- grid cells, entorhinal cortex, spatial remapping, reward location, goal-directed navigation, head direction cells, border cells, Bayesian decoding, rate remapping, spatial memory, navigational strategy, cognitive map
