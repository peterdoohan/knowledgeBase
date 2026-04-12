---
source_file: decothi2022_predictive_spatial_navigation.md
paper_id: decothi2022_predictive_spatial_navigation
title: "Predictive maps in rats and humans for spatial navigation"
authors:
  - "William de Cothi"
  - "Nils Nyberg"
  - "Eva-Maria Griesbauer"
  - "Lydia Fletcher"
  - "Coco Newton"
  - "Sophie Renaudineau"
  - "Daniel Bendor"
  - "Carole Ghanam"
  - "Roddy Grieves"
  - "Fiona Zisch"
  - "Éléonore Duvelle"
  - "Julie M. Lefort"
  - "Caswell Barry"
  - "Hugo J. Spiers"
year: 2022
journal: "Current Biology"
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - open_field
  - virtual_navigation
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - striatum
frameworks:
  - reinforcement_learning
  - successor_representation
  - temporal_difference_learning
keywords:
  - successor_representation
  - spatial_navigation
  - reinforcement_learning
  - predictive_map
  - cognitive_map
  - cross_species_comparison
  - model_based_vs_model_free
  - trajectory_analysis
  - open_field_maze
  - virtual_reality_navigation
  - hippocampus
  - diffusivity_analysis
  - predictive
  - maps
  - rats
  - humans
  - spatial
  - navigation
key_citations:
  - dayan1993_successor_representation
  - momennejad2017_successor_representation_humans
  - tolman1948_cognitive_maps_rats
  - widloski2022_hippocampal_replay_barriers
  - stachenfeld2017_hippocampus_predictive_map
wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/successor_representation_in_striatal_and_dopaminergic_reinforcement_learning
---

### One-line summary

Using a novel open-field modular maze tested on humans, rats, and simulated reinforcement learning agents, this study shows that both species navigate most similarly to agents using a successor representation (SR) that builds a predictive map, with humans also displaying signatures of model-based planning in early trials.

---

### Background & motivation

Understanding how mammals navigate flexibly — taking shortcuts and detours when familiar paths are blocked — is a central question in cognitive and systems neuroscience. Most research has studied individual species with species-specific tasks, limiting direct cross-species comparison and the integration of human neuroimaging with rodent single-unit recordings. A key open question is whether humans and rats share a common computational strategy, and which class of reinforcement learning (RL) algorithm — model-free (MF), model-based (MB), or successor representation (SR) — best captures that strategy in a complex, dynamic spatial environment. Prior cross-species comparisons of navigation with RL agents had focused on small state spaces with shallow transition structures and typically did not include the SR as a candidate.

---

### Methods

- **Task (Tartarus maze)**: A configurable 10×10 modular open-field maze with barriers that reconfigure every 10 trials, requiring detours and shortcuts to reach a fixed hidden goal.
- **Subjects**: 18 healthy humans (9 female, mean age 24.6 ± 5.9) navigating via immersive VR (HTC Vive headset); 9 adult male Lister Hooded rats navigating a physical 2×2 m maze.
- **RL agents**: Three classic algorithms — model-free Q-learning (MF), model-based A* tree search (MB), and successor representation (SR) — each with eligibility traces; agent parameters (learning rate, discount factor) fit by maximum likelihood to individual biological trajectories.
- **Procedure**: All subjects completed the same sequence of 25 maze configurations × 10 trials per configuration (250 trials total), with identical starting locations across species.
- **Analyses**:
  - Action likelihood: RL agents constrained to follow biological trajectories; softmax value distributions used to compute log-likelihood ratios (SR vs. MF, SR vs. MB).
  - Performance comparison: proportion of trials reaching goal, deviation from optimal path.
  - Trajectory diffusivity: linear and angular diffusivity measures used to characterise trajectory shape; Mahalanobis distance used to quantify species–agent dissimilarity.
  - Minimum path distance: physical closeness between biological and simulated agent trajectories across trials.

---

### Key findings

- Humans and rats showed a strong occupancy correlation (r = 0.67 overall; r higher during later trials of each configuration), indicating remarkably similar spatial behaviour across species.
- In likelihood analysis, the SR agent provided the best fit for both humans and rats across all three analyses: SR was the maximum likelihood model on 70% of human trials and 60% of rat trials; SR vs. MF log-likelihood ratio = 1911.1 (humans) and 842.0 (rats); SR vs. MB = 538.2 (humans) and 225.2 (rats).
- Difficulty rankings across maze configurations correlated significantly more between humans and the SR agent than either MF or MB (SR vs. MB: t(17) = 4.57, p < 0.001; SR vs. MF: t(17) = 3.27, p = 0.004); rat difficulty rankings were significantly lower for MF than MB or SR.
- Diffusivity-based trajectory clustering (t-SNE) showed distinct agent clusters; both human and rat behaviour fell closest to the SR cluster (humans: SR vs. MF t(17) = −55.7, p < 0.001; SR vs. MB t(17) = −4.21, p < 0.001; rats: SR vs. MF t(8) = −11.1, p < 0.001; SR vs. MB t(8) = −12.7, p < 0.001).
- Humans additionally showed MB-like trajectories on the first 5 trials of a new maze configuration (MB vs. SR: t(17) = 3.30, p = 0.004), shifting to SR-like trajectories in the second half of trials (last 5 trials SR vs. MB: t(17) = 8.95, p < 0.001); this pattern was not observed in rats.
- The MB agent consistently outperformed biological subjects in goal-reaching, especially early in a new configuration, indicating it is not the best behavioural match despite superior performance.
- MF agents performed progressively worse over trials (performance declined as maze complexity increased), and were the worst fit to biological behaviour throughout.

---

### Computational framework

The paper uses **reinforcement learning (RL)** as its primary computational lens, comparing three algorithms:

1. **Model-free (MF) Q-learning with eligibility traces**: Learns cached state-action values (Q) via temporal-difference updates. Inflexible to environmental change; associated with habit formation. Key variables: Q(s,a), eligibility trace e, learning rate α, discount γ.

2. **Model-based (MB) with A* tree search**: Maintains a binary grid model of which modules are traversable, updated incrementally from experience. Plans the shortest route to goal via A* at each decision point. Optimal but computationally expensive and slow to recover a correct model after structural changes.

3. **Successor representation (SR)**: Learns a predictive map M where each entry M(s, s') encodes the discounted expected future occupancy of state s' from state s — i.e., M = (I − γT)⁻¹ for one-step transition matrix T. Value is computed as V(s) = M(s,·)·R, where R is separately learned state reward. M is updated via TD learning with eligibility traces. SR is intermediate between MF and MB: it lacks a full transition model but encodes transition structure in a way that supports flexible, map-like navigation without expensive tree search.

The framework assumes agents operate over discrete states in a grid world; biological trajectories are discretised onto the 10×10 grid for comparison.

---

### Prevailing model of the system under study

The introduction frames the field as implicitly assuming that rodents and humans share fundamentally similar navigation mechanisms grounded in a hippocampal cognitive map (O'Keefe & Nadel 1978), with place cells providing a spatial representation that supports flexible inference. However, the dominant computational debate has centred on a dichotomy between model-free (habit-based, striatal) and model-based (planning-based, hippocampal/prefrontal) control, with most human studies finding evidence for MB planning in small-step conceptual state spaces. The SR had been proposed as a neural candidate for hippocampal function (Stachenfeld et al. 2017; de Cothi & Barry 2020), but had not been tested against biological navigation behaviour in a large, dynamic, open-field spatial environment directly comparable across species. The field lacked experiments where humans and rodents performed a directly homologous task, limiting the translational integration of human neuroimaging with rodent recordings.

---

### What this paper contributes

The paper provides the first direct cross-species behavioural comparison of humans and rats on an identical spatial navigation task in a large, dynamic environment, and systematically evaluates MF, MB, and SR agents against the resulting data. The main contribution is strong convergent evidence — from three independent analysis approaches (likelihood, performance, trajectory shape) — that both species behave most consistently with a SR agent rather than either the habit-based (MF) or planning-based (MB) extremes. This cannot simply be explained by SR being the best-performing algorithm (MB performs better by goal-reaching metrics); the SR provides a better description of the qualitative trajectory patterns. The paper also documents a dissociation within humans: early trials show MB-like features, later trials revert to SR-like behaviour, consistent with a resource-allocation account where expensive planning gives way to cached map-based navigation once the environment is partially familiar. The strong cross-species occupancy correlation additionally demonstrates that the Tartarus maze is a viable homologous assay, opening the door to integrating human neuroimaging with rodent electrophysiology within a shared computational framework.

---

### Brain regions & systems

The paper is primarily behavioural and computational; it does not collect neural data. Brain regions are discussed in the context of prior literature and as directions for future work:

- **Hippocampus** — proposed locus of the SR / predictive map implementation; discussed as encoding transition structure via place-cell activity in CA1. Prior evidence (Stachenfeld et al. 2017; de Cothi & Barry 2020) and hippocampal replay (Widloski & Foster 2022) are cited as supporting the hippocampus-as-SR-map hypothesis.
- **Dorsal CA1** — specifically cited as a candidate for SR implementation in rodents, based on asymmetric place-field expansion consistent with SR predictions.
- **Prefrontal cortex** — noted as supporting route planning and detour-taking in humans; differences between rodent and primate prefrontal regions acknowledged as a potential source of species differences.
- **Dorsal striatum** — mentioned as a candidate for MF/habit-based learning, in contrast to hippocampal map-based control.

No neural recordings, imaging, lesion, or pharmacology data were collected in this study.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined. It proposes an algorithm — the SR — and provides strong behavioural evidence that both rats and humans act consistently with it. However, no neural data (recordings, imaging, lesion, pharmacology) were collected; the claims remain at the behavioural/computational level. The paper explicitly positions neural recordings and disruption studies as essential future steps.

The paper proposes the SR as a computational solution (what problem is the brain solving: flexible navigation with manageable computational cost) and specifies the algorithmic level (SR matrix M learned via TD, combined with separately learned reward signals to compute value). The implementational level — how the SR matrix is encoded in specific cell types, circuits, or neuromodulators — is not addressed by this study's data, though prior work linking CA1 place-cell asymmetry to SR predictions is cited.

---

### Limitations & open questions

- No neural data were collected; the match to SR behaviour is consistent with but does not causally implicate the hippocampus or any other structure.
- The physical apparatus differed between species (real maze vs. VR), and species differ in sensory ecology (vision, olfaction, whiskers, predator avoidance), complicating direct interpretation of behavioural differences.
- The fog manipulation in VR was intended to equalise visible range across species, but rats may still have had greater effective visual access to the maze, potentially biasing their strategy toward SR (consistent with Zhu et al. 2021).
- RL agents were given perfect state knowledge (one-hot state vector), whereas biological subjects must self-localise from sensory cues — a substantial computational burden not modelled.
- Agents did not include replay/offline learning; adding prioritised replay could improve MB and SR agent performance and alter the comparative fit.
- The epsilon-greedy exploration policy may not capture the curiosity-driven or uncertainty-guided exploration observed in rats and humans.
- The task tested only one goal location per maze configuration; manipulating distal cues, maze complexity, fog levels, and reconfiguration frequency would test the generality of the SR account.
- The study does not dissociate path distance from Euclidean distance as potential coding dimensions.
- Extending the paradigm to other species (ants, bats, birds, primates) and incorporating eye-tracking (for humans) and single-unit recordings (for rodents) are highlighted as priority future directions.

---

### Connections & keywords

**Key citations**:
- Stachenfeld, Botvinick & Gershman (2017) — hippocampus as a predictive map (Nature Neuroscience)
- Dayan (1993) — original SR paper
- Russek, Momennejad et al. (2017) — SR in human RL (PLoS Comp Biol)
- Momennejad et al. (2017) — SR in human reinforcement learning (Nature Human Behaviour)
- de Cothi & Barry (2020) — neurobiological successor features for spatial navigation (Hippocampus)
- Geerts, Chersi, Stachenfeld & Burgess (2020) — general model of hippocampal and dorsal striatal learning (PNAS)
- Widloski & Foster (2022) — flexible rerouting of hippocampal replay around barriers (Neuron)
- Daw, Gershman et al. (2011) — model-based influences on human choices (Neuron)
- O'Keefe & Nadel (1978) — hippocampus as cognitive map
- Tolman (1948) — cognitive maps in rats and men

**Named models or frameworks**:
- Successor Representation (SR)
- Model-free Q-learning (MF-RL)
- Model-based A* tree search (MB-RL)
- Tartarus maze (novel task paradigm)

**Brain regions**:
- Hippocampus (CA1)
- Prefrontal cortex
- Dorsal striatum

**Keywords**:
- successor representation
- spatial navigation
- reinforcement learning
- predictive map
- cognitive map
- cross-species comparison
- model-based vs. model-free
- trajectory analysis
- open-field maze
- virtual reality navigation
- hippocampus
- diffusivity analysis

### Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]
- [[wiki/topics/successor_representation_in_striatal_and_dopaminergic_reinforcement_learning|Successor representation in striatal and dopaminergic reinforcement learning]]
