---
source_file: "zielinski2019_theta_hippocampus_prefrontal.md"
paper_id: "zielinski2019_theta_hippocampus_prefrontal"
title: "Coherent Coding of Spatial Position Mediated by Theta Oscillations in the Hippocampus and Prefrontal Cortex"
authors: "Mark C. Zielinski, Justin D. Shin, Shantanu P. Jadhav"
year: 2019
journal: "The Journal of Neuroscience"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
methods: ["bayesian_decoding"]
brain_regions: ["hippocampus", "hippocampus_ca1", "prefrontal_cortex", "medial_prefrontal_cortex"]
keywords: ["theta_oscillations", "hippocampal_prefrontal_synchrony", "spatial_coding", "phase_locking", "phase_precession", "bayesian_decoding", "ensemble_activity", "working_memory", "place_cells", "coherent_coding", "theta_phase", "spatial_memory", "w_track_task", "population_decoding", "coherent", "coding", "spatial", "position", "mediated", "theta"]
---

### One-line summary

Prefrontal cortex population activity encodes spatial position coherently with hippocampal CA1 populations on a theta-cycle timescale, and theta phase-associated spiking significantly improves spatial decoding accuracy in both regions.

### Background & motivation

Hippocampal-prefrontal interactions are critical for memory-guided behavior, with theta oscillations (~8 Hz) serving as a key physiological mechanism for coordinating these interactions. While hippocampal place cells encode spatial position via theta-mediated rate and temporal codes, it was unknown whether prefrontal cortex similarly encodes spatial information coherently with hippocampus or whether theta phase modulates prefrontal spatial representations.

### Methods

- **Subjects**: 5 adult male Long-Evans rats
- **Task**: Continuous W-track spatial alternation task requiring hippocampal-prefrontal interactions
- **Recordings**: Simultaneous multitetrode recordings from dorsal CA1 (hippocampus) and prelimbic (PrL) region of medial prefrontal cortex (PFC)
- **Neural populations**: 255 CA1 neurons and 111 PFC neurons (after excluding interneurons and low-firing units)
- **Analysis**: 
  - Bayesian decoding of spatial position using theta cycles as time bins
  - Theta phase binning (1-8 bins) to assess phase-specific spatial coding
  - Joint decoding error correlation analysis between CA1 and PFC
  - Phase-locking and phase precession quantification using Rayleigh tests and circular-linear regression

### Key findings

- Both CA1 and PFC population activity encoded the animal's current spatial position on a theta-cycle timescale during memory-guided behavior, with CA1 showing significantly higher spatial specificity (median spatial specificity: CA1 = 0.10, PFC = 0.37; p < 1e-99)
- Decoding accuracy was significantly better in CA1 than PFC (median decoding error: CA1 = 3.4 cm, PFC = 15.7 cm; p < 1e-99)
- CA1 and PFC position representations were coherent, with correlated decoding errors within theta cycles (r = 0.10, p = 0.001; significantly higher than shuffled controls, p = 0.01)
- Incorporating theta phase information significantly improved spatial decoding accuracy in both CA1 (~2-fold improvement with 7 phase bins, p < 0.02) and PFC (~4-fold improvement with 7 phase bins, p < 0.0013)
- Theta phase-associated spiking in PFC (phase-locking) rather than phase precession underlies improved spatial coding, unlike CA1 where phase precession dominates
- 83.5% of CA1 neurons and 51.4% of PFC neurons were significantly phase-locked to hippocampal theta oscillations
- Phase-locking strength was significantly higher in CA1 than PFC (p = 1.5e-08), and preferred phases differed between regions (p = 0.002)

### Computational framework

The study employs a **Bayesian decoding framework** for spatial position estimation from neural ensemble activity. The core formalism treats the probability of position given spike counts as a Poisson process:

P(pos|spikes) ∝ P(spikes|pos) = ∏ᵢ (fᵢ(pos) * t)^nᵢ / nᵢ! * exp(-fᵢ(pos) * t)

Where fᵢ(pos) is the occupancy-normalized firing rate map for unit i, nᵢ is spike count, and t is the time window (theta cycle). This framework incorporates theta phase by subdividing firing fields into phase-dependent templates, effectively testing whether spike timing relative to theta phase carries additional spatial information beyond rate coding alone.

### Prevailing model of the system under study

Prior to this study, the field understood that:
1. Hippocampal-prefrontal interactions are necessary for spatial working memory, supported by both anatomical connectivity and inactivation studies
2. Theta oscillations (~8 Hz) mediate physiological coupling between hippocampus and prefrontal cortex, manifesting as oscillatory coherence and phase-locked prefrontal spiking
3. Hippocampal CA1 place cells encode spatial position via both rate coding and theta phase precession (temporal coding), with phase precession significantly improving spatial decoding accuracy
4. Prefrontal neurons exhibit spatial selectivity and prominent phase-locking to hippocampal theta, but whether theta phase similarly modulates prefrontal spatial representations was unknown
5. Whether hippocampal and prefrontal populations coherently encode spatial position on a theta-cycle timescale was unexplored

### What this paper contributes

This paper establishes two key advances over the prevailing model:

1. **Coherent spatial coding across hippocampal-prefrontal networks**: The study demonstrates that prefrontal cortex population activity encodes the animal's current spatial position on a theta-cycle timescale, and importantly, this encoding is coherent with hippocampal CA1 representations. The correlated decoding errors between regions indicate shared processing of spatial information, suggesting that theta oscillations coordinate not just temporal synchrony but also content-specific information transfer between these memory-critical regions.

2. **Theta phase as a mechanism for improved spatial coding in prefrontal cortex**: The study reveals that theta phase-associated spiking (phase-locking) significantly improves prefrontal spatial decoding accuracy (~4-fold improvement), paralleling the improvement seen in CA1 (~2-fold improvement). This demonstrates that theta phase serves as a temporal coordination mechanism for spatial coding across both regions, even though the specific phase-space relationship differs (phase precession in CA1 vs. phase-locking in PFC). The finding extends the classical understanding of theta phase coding beyond the hippocampus to prefrontal networks.

### Brain regions & systems

- **Hippocampus (area CA1)**: Primary locus of spatial representation via place cells; exhibits high spatial specificity (median 0.10); strong theta phase-locking (83.5% of neurons) and phase precession (58.0% of neurons); serves as reference for theta phase measurements
- **Prefrontal cortex (medial PFC, prelimbic region)**: Shows coherent spatial coding with CA1 on theta-cycle timescale; lower spatial specificity (median 0.37) but significant position encoding; prominent theta phase-locking (51.4% of neurons) with phase-specific spatial firing that improves decoding accuracy; limited phase precession (6.3%, near chance levels)
- **Hippocampal-prefrontal circuit**: Theta oscillations (~8 Hz) mediate coherent interactions; high theta coherence across regions; correlated spatial decoding errors indicate shared information processing; theta phase serves as temporal coordination mechanism for spatial coding across the network

### Mechanistic insight

This paper provides strong mechanistic insight meeting both criteria: (1) it formalizes an algorithmic process (Bayesian decoding of position from population activity with theta phase modulation), and (2) it provides neural data showing that theta phase-associated spiking specifically improves spatial coding in both regions.

**Computational level**: The brain solves the problem of tracking current spatial position during memory-guided behavior by maintaining distributed representations across hippocampal-prefrontal networks. The coherent coding across regions suggests that position information is shared across nodes of a memory network, enabling flexible behavior that requires both hippocampal spatial memory and prefrontal executive control.

**Algorithmic level**: Position is encoded via a hybrid rate-phase code. Firing rates provide coarse position information, while spike timing relative to theta phase provides finer spatial resolution. In CA1, this manifests as phase precession (systematic phase advance across place fields). In PFC, it manifests as phase-locking to preferred phases within spatial fields. The Bayesian decoding framework formalizes how these complementary codes combine: P(pos|spikes) ∝ P(spikes|pos), with phase-binning effectively increasing the resolution of the firing rate templates.

**Implementational level**: Theta oscillations provide the biological implementation of this temporal coding scheme. The ~8 Hz rhythm creates discrete temporal windows (theta cycles, ~125-131 ms) that organize spiking across the hippocampal-prefrontal network. Phase-locking and coherence ensure that spikes occur at specific oscillatory phases, enabling phase-specific information transmission. The high theta coherence between regions and the correlated spatial decoding errors suggest that theta oscillations synchronize the network into coherent functional states for shared spatial processing.

### Limitations & open questions

- The study focused on dorsal CA1 and prelimbic PFC; whether ventral hippocampus (which projects directly to PFC) plays a specific role in the observed coherent coding remains to be investigated
- The specific anatomical pathways supporting coherent spatial coding (direct ventral CA1→PFC projections vs. indirect routes via nucleus reuniens) are not dissociated in this study
- The directionality of information flow during coherent coding (CA1→PFC vs. PFC→CA1 vs. bidirectional) was not explicitly tested, though prior work suggests CA1-leading-PFC directionality for theta-mediated interactions
- Whether the observed phase-locking in PFC improves spatial coding through enhanced signal-to-noise (phase-specific segregation of spikes) or through specific circuit mechanisms remains to be determined
- The relationship between coherent spatial coding and behavior (e.g., whether coherence varies with task demands or performance) was not explicitly tested
- Whether similar coherent coding extends to other cortical areas (e.g., visual cortex as suggested by prior work) and whether it generalizes beyond spatial representations to other mnemonic content remains open

### Connections & keywords

- **Key citations**: Jones and Wilson 2005a (theta coordination in spatial memory), Benchenane et al. 2010 (theta oscillations and spike timing), O'Keefe and Recce 1993 (phase precession), Jensen and Lisman 2000 (theta phase coding in position reconstruction), Haggerty and Ji 2015; Saleem et al. 2018 (coherent spatial representations in CA1 and visual cortex)
- **Named models or frameworks**: Bayesian decoding of position, theta phase precession, theta phase-locking, theta-gamma coupling (discussed as potential mechanism), theta sequences
- **Brain regions**: Hippocampus (area CA1, dorsal), Prefrontal cortex (medial PFC, prelimbic region), Nucleus reuniens (mentioned as indirect connection)
- **Keywords**: theta oscillations, hippocampal-prefrontal synchrony, spatial coding, phase-locking, phase precession, Bayesian decoding, ensemble activity, working memory, place cells, coherent coding, theta phase, spatial memory, W-track task, population decoding
