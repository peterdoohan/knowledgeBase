---
source_file: stella2019_hippocampal_reactivation_brownian.md
title: Hippocampal Reactivation of Random Trajectories Resembling Brownian Diffusion
authors: Federico Stella, Peter Baracskay, Joseph O'Neill, Jozsef Csicsvari
year: 2019
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Hippocampal replay during rest reactivates random 2D trajectories that follow Brownian diffusion dynamics, rather than directly replaying the animal's actual behavioral trajectories.

### Background & motivation

Hippocampal place cell sequences encoding movement trajectories are reactivated during immobility and sleep, a process linked to memory consolidation and decision-making. It was thought that only fixed, behaviorally relevant patterns stored across synaptic connections could be reactivated. This paper tests whether generalized rules govern reactivation by examining trajectory reactivation following non-stereotypical exploration in open-field environments, where animals perform random pellet-chasing tasks rather than repeated stereotyped trajectories.

### Methods

- **Subjects**: Four adult male Long-Evans rats
- **Recording**: 128-channel (32 tetrodes) recordings from dorsal CA1 hippocampal region, yielding 383, 243, 206, and 100 putative pyramidal neurons and 31, 18, 30, and 24 putative interneurons per animal
- **Behavior**: Random foraging in 1.2m diameter circular open-field arena with scattered food pellets, followed by rest/sleep in a separate box without visual contact with the explored environment
- **SWR detection**: Sharp-wave ripple events detected during quiet immobility periods (excluding REM sleep) using wavelet analysis of LFP (150-250 Hz ripple band), with events classified at 5 SD threshold
- **Position decoding**: Bayesian reconstruction method using place cell firing rate maps to estimate encoded locations during SWR events
- **Analysis windows**: Fixed-spike windows (15 spikes) or fixed-time windows (8 ms); events required at least 5 prediction windows
- **Quality threshold**: SWR events admitted if average maximum posterior probability exceeded 0.1

### Key findings

- Reactivated 2D trajectories during SWRs exhibited Brownian diffusion dynamics with power law exponent a ≈ 0.5 (characteristic of Brownian motion), significantly different from the animal's actual behavioral trajectories (a ≈ 0.7)
- Reactivated trajectories covered wide ranges of spatiotemporal scales (varying lengths and speeds), with speeds following lognormal distributions
- Shuffled controls (spike jittering, identity shuffling, place field rotation) showed significantly different speed distributions and weaker encoding confidence, confirming that original trajectories were temporally organized and represented the actual environment
- Reactivation starting positions were distributed randomly across the environment (>90% of maximum entropy), uncorrelated with behavioral occupation patterns
- Trajectory starting directions were generally not directionally tuned for central locations, with some tuning observed near environmental boundaries
- Population Activity Distance (PAD, measuring assembly orthogonality) increased with reactivation time independently of encoded distance, suggesting separate coding of time and position
- Different oscillatory bands predicted distinct reactivation dynamics:
  - Ripple-band power (150-200 Hz) and interneuron firing correlated with PAD (assembly orthogonality)
  - Fast gamma power (≥80 Hz) correlated with reactivation speed
  - Slow gamma (~30 Hz) correlated with both reactivation speed and PAD
- No evidence of preplay (trajectory reactivation before novel environment experience) was found

### Computational framework

The paper conceptualizes hippocampal replay using a **Brownian diffusion / random walk framework**. The core formalism describes trajectory reactivation as a diffusion process where:
- Distance scales with time according to a power law: ⟨d²⟩ = G × t^(2a)
- For Brownian diffusion, the exponent a = 0.5
- The step length distribution follows a Rayleigh distribution in 2D
- The process can be modeled as sequential recruitment of place cell assemblies where activation of one assembly triggers the next in random spatial directions, with assembly transitions constrained to similar distances

This framework is related to attractor network models of hippocampal place cells, where sequential activation can be viewed as transitions between attractor states representing spatial locations.

### Prevailing model of the system under study

The prevailing model before this study held that hippocampal replay reactivates specific, behaviorally relevant trajectory patterns that were stored through experience-dependent synaptic plasticity during exploration. According to this view:
- Only fixed patterns experienced during behavior could be reactivated
- Replay served to consolidate these specific memories
- Replay during sleep reflected direct storage and retrieval of experienced sequences
- The content of replay was determined by what the animal actually did

This model was supported by findings showing that novel spatial maps and their replay require NMDA receptors (Kentros et al., 1998; Silva et al., 2015), and that sequences on linear tracks emerge after the first lap (Feng et al., 2015).

### What this paper contributes

This paper challenges the prevailing model by demonstrating that hippocampal replay can generate random trajectories that do not directly reflect the animal's behavioral experience:

1. **Replay is not a direct storage of experience**: The Brownian diffusion statistics of replayed trajectories (a ≈ 0.5) differ markedly from the statistics of actual behavioral trajectories (a ≈ 0.7), demonstrating that replay does not simply reactivate stored patterns of what the animal did.

2. **Generalized generation capability**: The hippocampus can generate random trajectories covering wide spatiotemporal scales without requiring prior experience of those specific paths. This suggests a generalized mechanism for trajectory generation rather than storage of specific behavioral episodes.

3. **Flexible time-position coding**: The independence of PAD (assembly orthogonality) from encoded distance suggests separate coding of temporal and spatial information during replay, enabling flexible representation of trajectories at different speeds.

4. **Oscillatory control mechanisms**: Different aspects of replay dynamics (speed vs. assembly orthogonality) are differentially controlled by distinct oscillatory bands (fast gamma vs. ripple), suggesting parallel mechanisms for regulating replay content.

This work suggests that hippocampal replay may serve broader cognitive functions beyond consolidation of specific experiences, including generalization, planning, and optimization of behavioral solutions through simulated random walks in neural space.

### Brain regions & systems

- **Hippocampus CA1**: Primary region of study; site of sharp-wave ripple (SWR) events and place cell recordings; locus of trajectory reactivation; local generation of ripple oscillations through pyramidal cell-interneuron interactions
- **Hippocampus CA2/CA3a**: Mentioned as triggering region for sharp waves and SWR emission that propagate to CA1
- **Medial entorhinal cortex (MEC)**: Implicated as potential source of speed-related inputs and fast gamma oscillations that may regulate reactivation dynamics; source of upstream spatial sensory inputs that may drive waking replay
- **Dentate gyrus**: Mentioned as region associated with fast gamma oscillations and interactions with CA1 during reactivation

### Mechanistic insight

This paper meets the mechanistic insight bar by providing both a computational algorithm (Brownian diffusion / random walk process) and neural data supporting it over alternatives.

**Computational level**: The brain generates random trajectories through previously experienced spatial maps to support flexible cognitive functions including memory consolidation, generalization, and planning. The problem is to generate diverse trajectory representations without storing every possible path.

**Algorithmic level**: Reactivated trajectories follow a Brownian diffusion process characterized by:
- Power law relationship between distance and time with exponent a ≈ 0.5
- Rayleigh distribution of step distances in 2D
- Sequential recruitment of place cell assemblies where activation of one assembly triggers the next in random directions
- Assembly transitions constrained to similar distances (consistent reactivation speed within events)
- Separate coding of time (via PAD/orthogonality) and position

**Implementational level**: 
- Local CA1 circuits generate sequences through pyramidal cell-interneuron interactions
- Ripple-band oscillations (150-200 Hz) modulate assembly orthogonality (PAD) via interneuron activity
- Fast gamma oscillations (≥80 Hz) regulate reactivation speed, potentially via entorhinal inputs
- Slow gamma (~30 Hz) relates to both speed and orthogonality, potentially coordinating information routing
- The network can autonomously generate sequences (as shown by optogenetic studies), with consistency dependent on interneuron firing

### Limitations & open questions

- The study focused on random foraging in open fields; whether similar Brownian diffusion dynamics occur during more structured behavioral tasks (e.g., goal-directed navigation, linear track running) remains to be determined
- The role of preplay (trajectory reactivation before experience) in the novel environment was not clearly established; the low proportion of preplay events and their lack of organized trajectory structure leaves open whether preplay serves a distinct function
- The exact biophysical mechanisms linking specific oscillatory bands to reactivation dynamics (speed vs. orthogonality) were not fully resolved; causal manipulations (e.g., optogenetic control of specific interneuron types) would be needed
- Whether the Brownian diffusion dynamics are a default mode of hippocampal operation or can be modulated by behavioral state, reward, or task demands was not addressed
- The functional consequences of the orthogonal assembly coding (PAD) for memory processes remain to be directly tested
- The relationship between these random trajectory reactivations and behavioral measures of memory consolidation or generalization was not established

### Connections & keywords

**Key citations**:
- O'Keefe and Dostrovsky (1971) - discovery of place cells
- O'Keefe and Nadel (1978) - cognitive map theory
- Lee and Wilson (2002) - discovery of replay during sleep
- Foster and Wilson (2006) - awake replay and reverse replay
- Pfeiffer and Foster (2013) - hippocampal place-cell sequences depicting future paths
- Gupta et al. (2010) - replay not a simple function of experience
- Dragoi and Tonegawa (2011) - preplay of future place cell sequences
- Csicsvari et al. (1999, 2000) - sharp waves and ripples
- Samsonovich and McNaughton (1997) - continuous attractor neural network model

**Named models or frameworks**:
- Brownian diffusion / random walk process
- Bayesian decoding framework for position reconstruction
- Attractor network models of hippocampal place cells
- Maximum entropy model (kinetic Ising model) for rate map generation
- Sharp-wave ripple (SWR) detection and analysis framework

**Brain regions**:
- Hippocampus CA1
- Hippocampus CA2/CA3a
- Medial entorhinal cortex (MEC)
- Dentate gyrus

**Keywords**:
hippocampal replay, sharp-wave ripples, place cells, Brownian diffusion, random walk, Bayesian decoding, trajectory reactivation, spatial memory, CA1, oscillations, gamma, ripples, assembly dynamics, population activity distance, attractor networks
