---
source_file: tacikowski2024_temporal_structure_hippocampal.md
title: Human hippocampal and entorhinal neurons encode the temporal structure of experience
authors: Pawel Tacikowski, Güldamla Kalender, Davide Ciliberti, Itzhak Fried
year: 2024
journal: Nature
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Human hippocampal and entorhinal neurons encode the temporal structure of experience by forming predictive successor representations that integrate 'what' and 'when' information, supported by time-compressed replay during offline periods.

### Background & motivation

Extracting temporal patterns from recurring events is fundamental for organizing memory, predicting future events, and guiding flexible behavior. While functional neuroimaging has suggested the hippocampal-entorhinal system supports this process, the actual neural computation at the single-neuron level in humans remained unknown. This study fills that gap by recording from single neurons during a structured temporal learning task.

### Methods

- **Participants**: 17 patients with epilepsy implanted with intracranial depth electrodes for clinical purposes (21 recording sessions total)
- **Task design**: Three-phase experiment with 6 images assigned to nodes of a pyramid graph:
  - **PRE (pre-exposure)**: Images presented in pseudo-random order (baseline)
  - **E1-E6 (exposure)**: Images presented following pyramid graph structure (only directly linked nodes shown sequentially)
  - **POST (post-exposure)**: Images presented in pseudo-random order (read-out phase)
- **Behavioral tasks**: Gender discrimination (PRE/POST) or mirror/normal judgment (E1-E6) — tasks unrelated to the hidden temporal structure
- **Recordings**: 1,456 single- and multi-units identified; 546 hippocampal-entorhinal neurons analyzed for main results
- **Key analyses**: 
  - Identification of "selective neurons" (preferential response to one stimulus) and "relational neurons" (increasing response to directly linked stimuli)
  - Bayesian naive classifier for population decoding of stimulus identity
  - Template matching (geodesic, Euclidean, successor representations) to neural distance matrices
  - Replay analysis: detection of time-compressed spike sequences during inter-phase breaks

### Key findings

- **Selective and relational neurons**: 45% of hippocampal, 53% of entorhinal, and 56% of parahippocampal neurons showed stimulus selectivity during PRE. Among these, 16% of hippocampal and 20% of entorhinal neurons became "relational" — increasing responses to stimuli directly linked to their preferred stimulus on the graph during exposure phases.

- **Gradual representational change**: Relational neurons showed progressively stronger responses to direct stimuli (E5-E6 vs PRE: P = 3.56 × 10⁻⁵) and diminished selectivity for their preferred stimulus (P = 9.69 × 10⁻⁹). These changes persisted during POST when the pyramid structure was no longer present (P = 0.018 for direct vs PRE).

- **Population-level representation**: The hippocampal-entorhinal population progressively encoded the pyramid structure. Classifier posterior probabilities for direct stimuli increased while probabilities for actual stimuli decreased. The difference between direct and indirect stimuli remained significant during POST (P = 8.61 × 10⁻⁵).

- **Successor representation**: The neural representation most closely matched the "successor representation" template (predictive, probability-weighted) rather than pure geodesic (shortest path) or Euclidean (physical distance) templates. The successor template significantly outperformed others (vs geodesic: P < 0.0001; vs Euclidean: P = 0.0094) and remained significant during POST (P = 0.0434).

- **Regional differences**: During exposure, hippocampal neurons represented the pyramid more accurately than entorhinal neurons (successor: P = 0.0429). During POST, the successor representation was more preserved in entorhinal cortex than hippocampus (P = 0.037), suggesting entorhinal cortex uses a more stable structural code while hippocampus uses a more dynamic object-related code.

- **Receptive field modulation**: Neurons selective to outer nodes (where the agent can only go back) showed elongated receptive fields — responding differently to indirect-inner vs indirect-outer nodes (P = 0.0151). Neurons selective to inner nodes (where the agent can go in multiple directions) showed symmetric receptive fields (P = 0.9825). This matches successor model predictions.

- **Neuronal replay**: Time-compressed replay of neuron sequences corresponding to graph trajectories was detected during breaks between phases. The proportion of pyramid-congruent replays (direct neuron fires before indirect neuron within 30 ms after seed neuron spike) increased significantly during learning (P < 0.001), while incongruent replays did not change (P = 0.195). This bridges behavioral and synaptic timescales.

- **Implicit learning**: None of the patients reported explicit awareness of the pyramid structure. Control studies with healthy participants confirmed lack of detailed explicit knowledge — performance on position reconstruction was at chance (P = 0.1584), though some link-level knowledge was above chance (P = 0.007). The successor representation strength correlated with behavioral indicators of implicit knowledge (reaction time conflict: ρ = 0.53, P = 0.0077).

### Computational framework

The paper employs the **successor representation (SR)** framework from reinforcement learning, which provides a predictive map of likely future states. The SR represents each state not just by its identity but by the expected discounted sum of future state occupancies, capturing the temporal structure of transitions.

Key formalism: The successor matrix is computed as the negative matrix exponential of the adjacency matrix (or via the discounted sum of path counts). This creates a representation where:
- Distances reflect temporal proximity and transition probabilities, not just graph topology
- Inner nodes (highly connected) have shorter distances to each other than outer nodes
- Receptive fields elongate predictably based on movement constraints

The SR can be learned through spike-timing dependent plasticity (STDP) and theta phase precession, connecting the computational framework to known neural mechanisms. The framework predicts that the hippocampal-entorhinal system builds predictive cognitive maps that support planning and generalization, not just memory storage.

### Prevailing model of the system under study

Before this study, the field understood that:
1. The hippocampal-entorhinal system supports spatial navigation through cognitive maps (place cells, grid cells)
2. Similar neural mechanisms represent non-spatial features (sound frequency, object characteristics, abstract space, time)
3. Functional neuroimaging in humans suggested the hippocampal-entorhinal system extracts temporal structure
4. The successor representation provided a computational account of how spatial representations might be predictive
5. Animal studies showed replay of place cell sequences during rest/sleep

However, a critical gap remained: **no study had shown how individual neurons in the human hippocampal-entorhinal system encode the temporal structure of non-spatial experience**, whether through predictive successor representations, whether this occurs without explicit awareness, or whether replay mechanisms support this encoding.

### What this paper contributes

This paper provides the first direct evidence that:
1. **Single neurons in human hippocampus and entorhinal cortex encode temporal structure** — neurons that initially responded to specific images gradually increased responses to temporally adjacent images, forming a relational code

2. **The representation is predictive (successor representation)** — the neural geometry matched the successor representation template better than geodesic or Euclidean alternatives, reflecting not just graph topology but transition probabilities

3. **Encoding occurs without explicit awareness** — patients showed no explicit knowledge of the pyramid structure, yet neurons encoded it and behavior was influenced by it

4. **The representation persists after experience ends** — the successor representation remained during POST when the temporal structure was no longer present, suggesting durable encoding

5. **Hippocampal and entorhinal codes differ** — hippocampus showed more accurate representation during learning; entorhinal cortex showed more stable representation during post-exposure, suggesting dynamic object-related coding in hippocampus versus stable structural coding in entorhinal cortex

6. **Replay bridges timescales** — time-compressed replay of graph-trajectories during rest periods increased with learning, providing a mechanism for how seconds-long temporal associations can be encoded via millisecond-scale synaptic plasticity

### Brain regions & systems

- **Hippocampus (H)**: Primary site of relational neurons showing dynamic changes in selectivity during learning; more accurate successor representation during exposure phases; more dynamic, object-related code
- **Entorhinal cortex (EC)**: Contained relational neurons with similar properties to hippocampus; more stable successor representation during POST; possibly serves as a structural scaffold
- **Parahippocampal gyrus (PH)**: Contained selective neurons but minimal relational coding
- **Amygdala, insula, orbitofrontal cortex, temporal cortex, parietal cortex**: Recorded from but did not show significant relational or structure-encoding properties

### Mechanistic insight

This paper meets the high bar for mechanistic insight by providing both an algorithmic account and neural data supporting it.

**Computational level**: The brain solves the problem of predicting future states from temporal experience by constructing a predictive map (successor representation) that encodes not just what was experienced but what is likely to be experienced next.

**Algorithmic level**: The successor representation is implemented through:
1. **Relational neurons** that scale firing rates to temporal distance (direct vs indirect links)
2. **Receptive field reorganization** that elongates predictably based on transition constraints (outer vs inner nodes)
3. **Population-level geometry** that warps Euclidean space to reflect transition probabilities

**Implementational level**: The encoding relies on:
1. **Spike-timing dependent plasticity (STDP)** — the paper discusses how synaptic modifications with ~30ms windows can encode seconds-long associations
2. **Time-compressed replay** — spontaneous reactivation of graph-trajectories during rest periods bridges the gap between behavioral and synaptic timescales
3. **Theta phase precession** — mentioned as a mechanism for learning successor representations

The paper provides direct neural evidence linking the computational framework (successor representation) to specific neural phenomena (relational neurons, replay, receptive field warping) through a combination of single-unit recording and computational modeling.

### Limitations & open questions

1. **Clinical population**: Participants were epilepsy patients with implanted electrodes, potentially limiting generalizability to healthy populations
2. **Spatial confounds**: The pyramid graph structure has spatial properties; fully disentangling spatial from temporal factors remains challenging despite control analyses
3. **Sample size for replay**: The replay analysis was limited to specific neuron triplets, and the overall number of detected replays was relatively small
4. **No causal manipulations**: The study is observational; causal roles of hippocampal vs entorhinal representations were inferred from correlational patterns rather than perturbations
5. **Limited explicit knowledge testing**: While patients reported no explicit awareness, formal testing of explicit knowledge was limited in the patient sample
6. **Stimulus familiarity**: Inner nodes were presented more frequently than outer nodes; though control analyses suggest this did not drive results, perfect balancing was not possible

### Connections & keywords

**Key citations**:
- Stachenfeld et al. 2017 (successor representation framework)
- Schapiro et al. 2013 (temporal community structure)
- Garvert et al. 2017 (abstract relational knowledge in hippocampal-entorhinal cortex)
- Bellmund et al. 2019 (sequence structure in entorhinal cortex)
- Whittington et al. 2022 (Tolman-Eichenbaum machine)

**Named models or frameworks**:
- Successor representation (SR)
- Cognitive map theory
- Spike-timing dependent plasticity (STDP)
- Theta phase precession
- Neuronal replay
- Place cells / grid cells (analogous concepts)

**Brain regions**:
- Hippocampus
- Entorhinal cortex
- Parahippocampal gyrus
- Amygdala
- Medial temporal lobe (MTL)

**Keywords**:
- temporal structure
- sequence learning
- statistical learning
- successor representation
- single-neuron recording
- human hippocampus
- entorhinal cortex
- neuronal replay
- cognitive map
- predictive coding
- relational memory
- implicit learning
- abstract representation
