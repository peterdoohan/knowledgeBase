---
source_file: nardin2023_theta_oscillations_prefrontal_hippocampal.md
paper_id: nardin2023_theta_oscillations_prefrontal_hippocampal
title: "Theta oscillations as a substrate for medial prefrontal-hippocampal assembly interactions"
authors:
  - "Michele Nardin"
  - "Karola Kaefer"
  - "Federico Stella"
  - "Jozsef Csicsvari"
year: 2023
journal: "Cell Reports"
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - tetrode_recording
  - behavioral_analysis
brain_regions:
  - hippocampus_ca1
  - entorhinal_cortex
  - prefrontal_cortex
  - medial_prefrontal_cortex
keywords:
  - theta_oscillations
  - hippocampal_prefrontal_interactions
  - cell_assemblies
  - neural_synchronization
  - phase_locking
  - spatial_navigation
  - cross_correlation
  - generalized_linear_model
  - graph_clustering
  - sequence_coding
  - rule_switching
  - working_memory
  - oscillatory_coupling
  - information_transfer
  - place_cells
  - prefrontal_cortex
  - ca1
  - rats
  - theta
  - oscillations
key_citations:
  - kaefer2020_replay_prefrontal_rule_switching
  - zielinski2019_theta_hippocampus_prefrontal
  - jones2005_theta_hippocampal_prefrontal
---

### One-line summary

Theta oscillations provide a temporal reference frame for transient functional coupling between hippocampal CA1 and medial prefrontal cortex (mPFC) assemblies, where mPFC cells enhance their theta phase locking during synchronized firing with specific CA1 partners.

---

### Background & motivation

Coordinated activity across brain regions is essential for cognitive functions, but the mechanisms by which neuronal assemblies in different areas interact remain unclear. While theta oscillations are known to synchronize hippocampal and prefrontal populations, it is unknown whether and how specific assemblies coordinate their activity beyond general oscillatory coupling. This study investigates the circuit mechanism behind CA1-mPFC assembly interactions during behavior.

---

### Methods

- **Subjects**: Four male Long-Evans rats (300-350g, 2-4 months old)
- **Task**: Rule-switching task on a plus maze requiring switching between spatial and cue-guided (light) rules
- **Recording**: Simultaneous extracellular recordings from dorsal hippocampal CA1 (16 tetrodes) and prelimbic mPFC (8 tetrodes per hemisphere) using tetrodes
- **Analysis approach**:
  - Generalized linear models (GLM) to account for spatial position, trajectory, speed, theta phase, spiking history, and within-area activity
  - Functional correlation analysis comparing real cross-correlograms to 10,000 GLM-simulated surrogates (Z > 4.5 threshold, Bonferroni corrected)
  - Bipartite spectral graph clustering to identify interregional assemblies
  - Theta phase locking analysis (mean vector length) and temporal bias detection

---

### Key findings

- **Delayed mPFC spatial coding**: mPFC spatial representations lag behind CA1 by ~114 ms for position correlation and ~150 ms for decoding error correlation, suggesting hippocampal information influences mPFC representations.

- **Functionally coupled (FnC) cell pairs**: 23,482 CA1-mPFC cell pairs analyzed; significant functional correlations (Z > 4.5) were most frequent at ~50 ms mPFC delay, occurring within a 125 ms window. These correlations persisted after accounting for spatial coding, theta oscillations, speed, and other confounds via GLM.

- **Enhanced theta phase locking during coupling**: When FnC mPFC cells fired synchronously with their CA1 partners, they showed significantly stronger theta phase locking compared to independent firing (binomial test, p < 0.001). Non-FnC pairs showed no such difference (Mann-Whitney U test, all p < 0.0003).

- **Fixed mPFC theta phase during co-firing**: During synchronized firing, mPFC cells maintained consistent theta phases even when CA1 cells exhibited theta phase precession; the phase difference compensated for CA1 phase changes, indicating mPFC cells did not mirror CA1 theta timing.

- **Interregional assemblies**: Bipartite spectral clustering revealed graph assemblies (clusters) of interconnected CA1-mPFC cells. During assembly activation, mPFC cells exhibited stronger theta phase locking and showed theta-phase biases relative to each other, forming theta sequences independent of spatial trajectory coding.

- **Behavioral modulation**: Assembly synchronization increased during error trials (particularly on goal arms) and during rule-switching periods, suggesting these assemblies signal cognitive demands or conflict requiring behavioral strategy changes.

- **No global oscillatory changes**: Paired firing of FnC cells was not accompanied by changes in theta, gamma, or ripple power or coherence, indicating functional coupling is a transient, cell-specific phenomenon rather than a global network state change.

---

### Computational framework

The study employs a **dynamical systems and network neuroscience framework** conceptualizing brain function as coordinated activity of neuronal assemblies across regions. Key computational elements include:

- **Generalized Linear Models (GLM)**: Poisson GLMs with L2 regularization are used to construct null models of neuronal firing, accounting for spatial position, trajectory, speed, theta phase, spiking history, and within-area network activity. These serve as statistical baselines to identify excess correlations (functional coupling) beyond explained variance.

- **Graph theory and spectral clustering**: A bipartite spectral graph clustering algorithm (based on modularity optimization) is applied to the functional correlation graph to identify interregional assemblies. The modularity matrix eigendecomposition reveals community structure, with cluster "cleanliness" (within vs. between-cluster connectivity) quantifying assembly boundaries.

- **Information theory**: Transfer entropy is used to quantify directed information flow between CA1 and mPFC, complementing the correlation-based analyses.

- **Normative modeling**: A restricted Boltzmann machine-inspired model formalizes optimal spatial information transfer from CA1 to mPFC, predicting connectivity patterns that maximize mutual information between mPFC population activity and spatial position.

The framework assumes that cognitive functions emerge from transient synchronization of distributed assemblies, with theta oscillations providing a temporal reference frame for coordinating multi-regional activity.

---

### Prevailing model of the system under study

The field has established several key frameworks for understanding hippocampal-prefrontal interactions:

1. **Theta-mediated synchronization**: The prevailing view holds that theta oscillations (5-10 Hz) provide a global coupling mechanism between hippocampus and prefrontal cortex, with the strength of theta coherence varying with cognitive demands. This oscillatory coupling is thought to facilitate information transfer across regions by aligning excitability windows.

2. **Cell assemblies and Hebbian plasticity**: Following Hebb's postulate, correlated activity is believed to establish functional associations between neurons, forming cell assemblies. Recent multi-neuronal recording studies have provided evidence for assemblies within brain regions, with reactivation during sleep and behavior suggesting their role in memory and cognition.

3. **Synfire chain propagation**: The synfire chain theory proposes that synchronized activity propagates sequentially across brain regions, with assemblies in one region activating connected assemblies in downstream areas. This provides a mechanism for cross-regional information flow.

4. **Hippocampal-prefrontal reactivation**: During sharp wave-ripple events (SWRs), hippocampal place cell sequences are reactivated, and this reactivation can recruit mPFC cells. However, the coordination between regions during these events is variable—sometimes coherent, sometimes independent.

5. **Hippocampal influence on prefrontal coding**: Prior work suggests that accurate spatial coding requires intact hippocampal-prefrontal circuits. Inactivation studies indicate mutual influence, with hippocampal spatial representations preceding and potentially shaping prefrontal representations. The mPFC is thought to transform hippocampal spatial codes into more abstract representations (e.g., distance-to-goal coding) for decision-making.

The current paper challenges and extends this framework by demonstrating that CA1-mPFC interactions can occur through transient, cell-specific theta phase locking enhancements rather than only through global oscillatory coherence or SWR-mediated reactivation.

---

### What this paper contributes

This paper provides several key advances to the understanding of hippocampal-prefrontal interactions:

1. **Transient assembly coupling mechanism**: The study identifies a novel mechanism for interregional assembly interactions—transient enhancement of theta phase locking in mPFC cells when they synchronize firing with specific CA1 partners. This extends beyond the prevailing model of global theta coherence by showing that phase locking can be dynamically modulated at the cell-pair level to signal functional interactions.

2. **Independence from common coding and oscillations**: The paper demonstrates that functionally coupled (FnC) CA1-mPFC pairs synchronize independently of common spatial coding, trajectory, speed, or oscillatory firing. This addresses a fundamental challenge in identifying true interregional assemblies—distinguishing coordinated activity from correlations driven by shared inputs or common behavioral covariates.

3. **Fixed theta phase during co-firing**: A striking finding is that mPFC cells maintain consistent theta phases during synchronized firing with CA1 partners, even when CA1 cells exhibit theta phase precession. This indicates that mPFC cells do not simply mirror hippocampal theta timing but maintain their own temporal reference frame, suggesting independent temporal coding schemes across regions during interactions.

4. **Graph-assembly organization**: Using bipartite spectral clustering, the study reveals that FnC cells form organized interregional assemblies (graph assemblies) with distinct spatial firing properties. During assembly activation, mPFC cells exhibit unique theta sequences that are independent of spatial trajectory representations, suggesting that different temporal coding schemes can operate simultaneously in the mPFC without interference.

5. **Behavioral relevance**: Assembly synchronization is modulated by cognitive demands—increasing during error trials and rule-switching periods. This suggests that CA1-mPFC assemblies may signal conflict or the need for behavioral strategy changes, providing a potential neural substrate for cognitive flexibility.

6. **Directional influence**: Multiple converging lines of evidence (delayed mPFC coding, transfer entropy, optimal theta locking delays, functional correlation timing) consistently suggest stronger hippocampal-to-mPFC than mPFC-to-hippocampal influence during the task. This supports a model where the hippocampus provides spatial information that the mPFC transforms into more abstract representations for decision-making.

7. **No global network state changes**: Unlike previous frameworks emphasizing global oscillatory coherence or SWR-mediated reactivation, this study shows that CA1-mPFC functional coupling does not involve changes in theta, gamma, or ripple power/coherence. This supports a model of transient, cell-specific interactions rather than global network state changes.

---

### Brain regions & systems

- **Hippocampal CA1 (dorsal)**: Primary source of spatial representations; shows earlier spatial coding than mPFC, with place cells exhibiting theta phase precession. CA1 cells form the "upstream" partners in functionally coupled pairs, with their activity preceding mPFC responses.

- **Medial prefrontal cortex (mPFC, prelimbic area)**: Shows delayed spatial coding relative to CA1 (~114-150 ms lag), encoding relative maze distance rather than absolute 2D position. mPFC cells exhibit enhanced theta phase locking to CA1 theta oscillations specifically during synchronized firing with functionally coupled CA1 partners, maintaining consistent theta phases independent of CA1 phase precession.

- **Thalamic nucleus reuniens**: Mentioned as a potential indirect pathway for hippocampal-prefrontal communication, bidirectionally connecting with mPFC and receiving hippocampal input via subiculum.

- **Entorhinal cortex / perirhinal cortex**: Mentioned as indirect pathways for hippocampal-prefrontal information transfer.

---

### Mechanistic insight

This paper provides substantial mechanistic insight into hippocampal-prefrontal interactions through a combination of empirical data and computational modeling. The findings map onto Marr's three levels as follows:

**Computational level**: The brain solves the problem of coordinating distributed cognitive computations across the hippocampus and prefrontal cortex during spatial navigation and decision-making. The specific computational goal is to enable transient, selective communication between specific cell assemblies in CA1 and mPFC to support flexible behavior (e.g., rule switching).

**Algorithmic level**: The algorithm implementing this coordination involves:
1. **Theta oscillations as a reference frame**: A 5-10 Hz theta rhythm provides a temporal scaffold for coordinating spike timing across regions.
2. **Transient phase locking enhancement**: When an mPFC cell needs to communicate with its CA1 partner, it transiently enhances its theta phase locking (quantified by mean vector length). This enhancement is specific to co-firing events, not a global state change.
3. **Fixed theta phase maintenance**: During interaction, mPFC cells maintain consistent theta phases even as CA1 cells exhibit phase precession. This allows mPFC cells to preserve their own temporal coding scheme while still receiving information from CA1.
4. **Assembly organization**: Functionally coupled cells form organized assemblies (identified via bipartite spectral clustering) with distinct spatial representations. Assembly activation is signaled by theta sequences in mPFC that are independent of spatial trajectory representations.

**Implementational level**: 
- **Neural hardware**: The mechanism involves dorsal CA1 pyramidal cells and prelimbic mPFC principal neurons.
- **Connectivity**: Direct projections from ventral hippocampus to mPFC, indirect pathways via entorhinal/perirhinal cortices, and thalamic nucleus reuniens (bidirectional with mPFC, receives hippocampal input via subiculum).
- **Oscillatory substrate**: Theta oscillations (5-10 Hz) recorded in CA1 LFP provide the reference frame. mPFC cells exhibit stronger phase locking to time-delayed CA1 theta (optimal delays: 23 ms start arm, 47 ms goal arm).
- **Physiological mechanism**: The transient enhancement of theta phase locking during co-firing requires precise spike timing within theta cycles. Randomizing theta spike timing (even within-cycle) abolishes ~75% of functional correlations, demonstrating that sub-theta-cycle precision is critical for the coupling mechanism.

---

### Limitations & open questions

- **Common factors not accounted for**: The GLM-based approach could not account for unknown common factors that might cause correlated firing; only demonstrated factors were controlled.

- **Physiological mechanism unclear**: The specific biophysical mechanism underlying synchronization-dependent phase-locking enhancement remains unspecified. Whether this involves specific synaptic mechanisms, neuromodulatory effects, or network dynamics is unknown.

- **Anatomical pathways speculative**: The specific anatomical routes (direct vs. indirect) mediating the observed functional coupling could not be definitively identified.

- **Limited behavioral data**: The behavioral role of CA1-mPFC assembly activity was investigated only in limited contexts (error trials, rule switching). The precise computational function of these assemblies in decision-making remains unclear.

- **Causality not established**: The directional influence analyses (transfer entropy, delays) are correlational; causal manipulation of CA1-mPFC pathways would be needed to confirm the hippocampal-to-mPFC directionality.

- **Generality to other tasks**: The findings were obtained during a specific rule-switching spatial task; whether similar mechanisms operate during other cognitive demands or in non-spatial contexts is unknown.

---

### Connections & keywords

**Key citations**:
- Hebb (1949) - The Organization of Behavior (cell assembly hypothesis)
- Buzsaki (2010) - Neural syntax: cell assemblies, synapsembles, and readers
- Jones & Wilson (2005) - Theta Rhythms Coordinate Hippocampal-Prefrontal Interactions
- Kaefer et al. (2020) - Replay of Behavioral Sequences in the Medial Prefrontal Cortex during Rule Switching
- Siapas et al. (2005) - Prefrontal Phase Locking to Hippocampal Theta Oscillations
- Dragoi & Buzsaki (2006) - Temporal encoding of place sequences by hippocampal cell assemblies
- Zielinski et al. (2019) - Coherent coding of spatial position mediated by theta oscillations in the hippocampus and prefrontal cortex

**Named models or frameworks**:
- Hebbian cell assembly hypothesis
- Synfire chain theory
- Generalized Linear Model (GLM) for neuronal firing
- Bipartite spectral graph clustering (Newman 2006, Barber 2007)
- Mutual information maximization model for spatial information transfer
- Restricted Boltzmann machine-inspired connectivity model
- Transfer entropy for directed information flow

**Brain regions**:
- Hippocampal CA1 (dorsal)
- Medial prefrontal cortex (mPFC, prelimbic area)
- Thalamic nucleus reuniens
- Entorhinal cortex
- Perirhinal cortex
- Subiculum

**Keywords**:
theta oscillations, hippocampal-prefrontal interactions, cell assemblies, neural synchronization, phase locking, spatial navigation, cross-correlation, generalized linear model, graph clustering, sequence coding, rule switching, working memory, oscillatory coupling, information transfer, place cells, prefrontal cortex, CA1, rats
