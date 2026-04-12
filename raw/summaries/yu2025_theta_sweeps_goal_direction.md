---
source_file: "yu2025_theta_sweeps_goal_direction.md"
paper_id: "yu2025_theta_sweeps_goal_direction"
title: "Hippocampal theta sweeps indicate goal direction"
authors: "Changmin Yu, Zilong Ji, Jake Ormond, John O'Keefe, Neil Burgess"
year: 2025
journal: "bioRxiv"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
tasks: ["open_field", "navigation_task"]
methods: ["tetrode_recording", "bayesian_decoding"]
brain_regions: ["hippocampus", "hippocampus_ca1", "entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "retrosplenial_cortex"]
frameworks: ["attractor_networks"]
keywords: ["okeefe_and_nadel_1978_the_hippocampus_as_a_cognitive_map_foundational_theory", "skaggs_et_al_1996", "foster_and_wilson_2007_theta_sequences_and_phase_precession", "johnson_and_redish_2007", "gupta_et_al_2012", "kay_et_al_2020_path_sampling_and_future_encoding", "wikenheiser_and_redish_2015_hippocampal_theta_sequences_reflect_current_goals", "pfeiffer_and_foster_2013_replay_depicts_future_paths_to_remembered_goals", "chu_et_al_2024", "ji_et_al_2025_continuous_attractor_network_models_of_theta_sweeps", "ormond_and_okeefe_2022_place_cells_have_goal_oriented_vector_fields", "named_models_or_frameworks", "cognitive_map_theory_okeefe_and_nadel", "continuous_attractor_network_can_model", "hierarchical_attractor_network_model_dc_conjunctive_gc_gc_pc", "theta_phase_precession_procession_framework", "firing_rate_adaptation_model", "brain_regions", "hippocampal_ca1_place_cells", "theta_sweeps"]
---

### One-line summary

Hippocampal theta sweeps exhibit robust goal-oriented directional biases independent of movement or head direction, providing a neural substrate for online goal-directed spatial planning.

### Background & motivation

Theta sweeps are sequential activations of place cells within individual theta cycles that exhibit predictive dynamics, potentially supporting rapid evaluation of future trajectories during navigation. However, it remained unresolved whether these sequences simply reflect movement-related variables or afford more cognitive goal-directed planning. Previous studies were hampered by experimental limitations where movement, head, and goal directions were typically aligned.

### Methods

- **Task**: Honeycomb maze navigation task allowing dissociation of head-, movement-, and goal-direction through a hexagonal platform design with indirect trajectories to the goal
- **Subjects**: 5 male Lister hooded rats trained to navigate to an unmarked goal location from different start platforms
- **Recordings**: Tetrode recordings from dorsal CA1 hippocampal region (105.2 ± 7.5 place cells per rat)
- **Decoding**: Bayesian maximum-a-posteriori (MAP) decoding of spatial location using phase-rolling temporal binning (60° phase windows, 15° increments)
- **Analysis**: Rayleigh vector length (MRL) analysis of circular distributions to quantify directional alignment; validation in open-field cheeseboard arena with 4 rats
- **Modeling**: Hierarchical continuous attractor network (CAN) with goal-directed top-down input to directional cells, projecting through conjunctive grid cells to place cells

### Key findings

- Theta sweeps exhibit robust goal-oriented directional bias, with sweep directions significantly more aligned to goal direction than movement or head direction (p = 0.0004 for SD vs GD vs MD; p = 0.0005 for MD vs HD)
- Initial offset directions (IOD) also show significant alignment to goal direction with no modulation by movement or head direction (p = 0.0078 for IOD vs GD vs MD; p = 0.9449 for MD vs HD)
- Goal-modulation strengthens with experience within recording sessions (p = 0.0269 for first vs second half of trials)
- Goal-modulation is stronger before correct compared to incorrect choices even after controlling for distance to goal (p = 0.0136), suggesting behavioral relevance
- In goal-switching sessions, sweeps align more strongly with current than alternative goal (p = 0.0220 for SD; p = 0.0060 for IOD)
- Theta sweep length increases with distance to goal and movement speed, and with theta power
- The continuous attractor network model with goal-directed input successfully reproduces goal-oriented theta sweeps and predicts goal-oriented theta phase precession (toward goal) and procession (away from goal), both confirmed empirically
- Replay events during sharp wave/ripples also show goal-directed bias, supporting that replay reflects composition of theta sweeps rather than direct experience

### Computational framework

The paper employs a **continuous attractor network (CAN)** framework with hierarchical structure:
- **Directional cells (DCs)**: Ring attractor representing head direction, receiving top-down goal-oriented allocentric directional input that biases activity toward goal direction
- **Conjunctive grid cells**: Bridge between directional and spatial representations, activated by DCs with shared preferred directions
- **Grid cells (GCs)**: 2D attractor receiving phase-shifted input from conjunctive cells, driving activity bumps along goal direction
- **Place cells (PCs)**: 2D attractor receiving feedforward projection from GCs, exhibiting goal-directed theta sweeps

Key mechanisms include theta-modulated oscillatory input, firing rate adaptation (enabling sequential activation), and speed-dependent modulation. The framework connects to broader computational principles of predictive coding, sequence generation, and cognitive map theory.

### Prevailing model of the system under study

Prior to this work, theta sweeps were understood as sequential activations of place cells within theta cycles that sweep forward from the animal's current location. Several models proposed that theta sweeps emerge from intrinsic network dynamics, particularly firing rate adaptation within attractor networks (Tsodyks et al., 1996; Chu et al., 2024), or from oscillatory interference mechanisms. The field recognized that theta sweeps could sample potential paths ahead of the animal, sometimes alternating to both sides of choice points or the forward direction in open fields, and that sweep length correlated with speed, distance to goals, and learning. However, it remained unresolved whether theta sweeps simply reflect movement-related dynamics or encode more abstract cognitive vectors toward goals. The prevailing view held that theta sweeps might reflect possible future movement trajectories rather than encoding a location-independent "sense of direction" toward goal locations.

### What this paper contributes

This paper establishes that hippocampal theta sweeps encode a goal-oriented cognitive vector that transcends immediate movement and sensory constraints. The key advances are:

1. **Demonstration of goal-directed theta sweeps**: Using a task that dissociates movement, head, and goal directions, the paper shows theta sweeps are robustly aligned to goal direction, with significantly weaker modulation by movement direction and little modulation by head direction.

2. **Behavioral relevance**: Stronger goal-modulation predicts subsequent correct choices and increases with experience, indicating theta sweeps actively contribute to navigation rather than merely reflecting motor output.

3. **Mechanistic model**: A hierarchical continuous attractor network with goal-directed input to directional cells successfully reproduces the empirical findings and makes testable predictions about theta phase precession/procession that are confirmed in the data.

4. **Unified framework for theta sweeps and replay**: The demonstration that replay events are also goal-directed and likely reflect composition of theta sweeps provides a coherent account of how online planning and offline consolidation may share common neural mechanisms.

These findings update the prevailing model by showing theta sweeps encode abstract cognitive vectors toward goals, not just possible movement trajectories, positioning them as a neural substrate for flexible online spatial planning within the cognitive map framework.

### Brain regions & systems

- **Hippocampal CA1**: Primary region of study; locus of place cell recordings and theta sweep generation; exhibits goal-oriented sequential activation during navigation
- **Entorhinal cortex**: Source of grid cell input to hippocampus; modeled as providing spatial input via conjunctive grid cells in the CAN model
- **Parasubiculum**: Location of directional cells (head direction cells) in the model; ring attractor network receiving top-down goal-oriented input
- **Retrosplenial cortex (RSC)**: Hypothesized source of top-down goal-oriented directional input; proposed to encode prospective goalward trajectories in allocentric and egocentric reference frames
- **Medial prefrontal cortex**: Alternative proposed source of goal information via projections to hippocampus through thalamic nucleus reuniens

### Mechanistic insight

This paper provides strong mechanistic insight that maps onto Marr's three levels:

**Computational level**: The brain solves the problem of rapid evaluation of potential future trajectories during spatial navigation. Theta sweeps provide a mechanism for online planning by encoding cognitive vectors toward goal locations, transcending immediate sensory inputs and motor outputs. This supports flexible navigation toward desired future states irrespective of current movement constraints.

**Algorithmic level**: The paper proposes and validates a hierarchical continuous attractor network (CAN) algorithm:
- Directional cells (ring attractor) receive top-down goal-oriented input, biasing activity toward goal direction
- This drives conjunctive grid cells, which provide phase-shifted input to grid cells
- Grid cell activity propagates to place cells via feedforward projection
- Firing rate adaptation within each network enables sequential activation (sweeps) within theta cycles
- Speed-regulated theta modulation paces the sequential dynamics

The model predicts and the data confirm that this algorithm produces goal-oriented theta phase precession when moving toward the goal and phase procession when moving away.

**Implementational level**: The neural implementation involves:
- **Hippocampal CA1 place cells**: Exhibit goal-directed sequential activation within theta cycles
- **Theta rhythm (6-12 Hz)**: Provides the temporal framework for organizing sequential sweeps
- **Firing rate adaptation**: Cellular mechanism enabling sequential activation within attractor networks
- **Entorhinal-hippocampal circuitry**: Directional cells (likely parasubiculum), conjunctive grid cells, and grid cells (entorhinal cortex) provide the circuit substrate
- **Top-down inputs**: Retrosplenial cortex or medial prefrontal cortex via thalamus provides goal-direction signals

The paper meets the high bar for mechanistic insight by providing a formalized algorithm (CAN model) with specific neural data supporting each level of analysis, from computational problem to biophysical implementation.

### Limitations & open questions

- **Source of goal-directed input**: The top-down goal-oriented input to directional cells is hypothesized to originate from retrosplenial cortex or medial prefrontal cortex via thalamus, but this remains to be empirically validated
- **Causal role of theta sweeps**: While the paper shows correlations between theta sweep quality and navigation performance, causal manipulations (e.g., phase-specific interventions) are needed to establish necessity and sufficiency
- **Generalization to other species**: The conservation of theta rhythms suggests similar mechanisms across mammals, but direct evidence in humans or non-rodent species is limited
- **Relationship to other cognitive functions**: The extent to which goal-directed theta sweeps support non-spatial planning or abstract reasoning remains unexplored
- **Replay composition**: The hypothesis that replay reflects composition of theta sweeps rather than experience requires further testing with manipulations that dissociate these possibilities
- **Network implementation details**: The model simplifies grid cell organization and omits some biophysical details; how the full entorhinal-hippocampal circuit implements these dynamics remains to be fully characterized

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) - The Hippocampus as a Cognitive Map (foundational theory)
- Skaggs et al. (1996); Foster & Wilson (2007) - Theta sequences and phase precession
- Johnson & Redish (2007); Gupta et al. (2012); Kay et al. (2020) - Path sampling and future encoding
- Wikenheiser & Redish (2015) - Hippocampal theta sequences reflect current goals
- Pfeiffer & Foster (2013) - Replay depicts future paths to remembered goals
- Chu et al. (2024); Ji et al. (2025) - Continuous attractor network models of theta sweeps
- Ormond & O'Keefe (2022) - Place cells have goal-oriented vector fields

**Named models or frameworks:**
- Cognitive map theory (O'Keefe & Nadel)
- Continuous attractor network (CAN) model
- Hierarchical attractor network model (DC → conjunctive GC → GC → PC)
- Theta phase precession/procession framework
- Firing rate adaptation model

**Brain regions:**
- Hippocampal CA1 (place cells, theta sweeps)
- Entorhinal cortex (grid cells, conjunctive cells)
- Parasubiculum (directional cells/head direction cells)
- Retrosplenial cortex (hypothesized source of goal-directed input)
- Medial prefrontal cortex (alternative source of goal information)
- Thalamic nucleus reuniens (projection pathway)

**Keywords:**
- theta sweeps
- hippocampal place cells
- goal-directed navigation
- spatial planning
- continuous attractor networks
- theta phase precession
- replay sequences
- Honeycomb maze
- cognitive map
- directional cells
- firing rate adaptation
- Bayesian decoding
- sharp wave ripples
- allocentric navigation
- prospective coding
