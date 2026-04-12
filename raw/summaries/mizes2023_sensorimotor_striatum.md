---
source_file: mizes2023_sensorimotor_striatum.md
paper_id: mizes2023_sensorimotor_striatum
title: "Dissociating the contributions of sensorimotor striatum to automatic and visually guided motor sequences"
authors:
  - "Kevin G. C. Mizes"
  - "Jack Lindsey"
  - "G. Sean Escola"
  - "Bence P. Ölveczky"
year: 2023
journal: "Nature Neuroscience"
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - electrophysiology
  - tetrode_recording
  - lesion
brain_regions:
  - striatum
  - dorsomedial_striatum
  - dorsolateral_striatum
  - thalamus
frameworks:
  - reinforcement_learning
keywords:
  - motor_sequence_learning
  - sensorimotor_striatum
  - basal_ganglia
  - motor_automaticity
  - movement_kinematics
  - chunking
  - discrete_sequence_production_task
  - dorsolateral_striatum_lesion
  - action_selection
  - neural_population_coding
  - motor_vigor
  - internally_generated_sequences
  - dissociating
  - contributions
  - sensorimotor
  - striatum
  - automatic
  - visually
  - guided
  - motor
wiki_pages:
  - wiki/topics/successor_representation_in_striatal_and_dopaminergic_reinforcement_learning
---

### One-line summary

The sensorimotor striatum (DLS) encodes task-invariant kinematic features of learned motor sequences but is selectively essential for high-level sequence structure in automatic and working-memory-guided — but not visually cued — conditions.

---

### Background & motivation

The basal ganglia (BG) are implicated in both flexible (externally cued or working-memory-guided) and automatic (overtrained) motor sequence execution, yet whether and how their contributions differ across these conditions is unclear. Prior studies used different tasks and animals to examine each mode, confounding the task structure with the execution mode. This paper directly compares striatal contributions to the same motor sequence performed under three conditions in the same animals. The gap being filled is the lack of a controlled within-animal comparison of neural coding and causal contribution of the BG across distinct modes of motor sequence generation.

---

### Methods

- **Task**: Rats were trained on a discrete sequence production ("piano") task requiring three-element lever-press sequences. The same sequence was performed under three conditions: visually cued (CUE), working-memory-guided (WM), and automatic/overtrained (AUTO).
- **Animals**: Female Long Evans rats (n = 23 total); n = 12 for behavioral characterisation; n = 4 for electrophysiology; n = 7 for DLS lesions; n = 6 for DMS lesions.
- **Electrophysiology**: 64-channel tetrode drives implanted in dorsolateral striatum (DLS) of expert rats (n = 4); 579 neurons analysed from 2,468 sorted units. Firing rates compared across CUE, WM, and AUTO conditions for the same sequences.
- **Decoding**: Feed-forward neural network trained to predict instantaneous forelimb and nose velocity from DLS population activity; also tested for sequence phase decoding.
- **Lesions**: Bilateral excitotoxic (quinolinic acid) lesions of DLS (n = 7 rats) or DMS (n = 6 rats) in expert animals; performance re-assessed post-recovery.
- **Kinematic tracking**: DeepLabCut-based markerless pose estimation from multi-camera video (side and top views); smoothness quantified using spectral arc length.
- **Neural network model**: Two-population (DLS + downstream recurrent motor circuits) artificial neural network, pretrained on cued movements, then trained with DLS input weights on both CUE and AUTO conditions. DLS removal simulated computationally to compare with lesion data.

---

### Key findings

- DLS neural activity was highly similar across CUE, WM, and AUTO conditions for the same motor sequence (mean cross-condition correlation ~0.83); no significant difference in average firing rates or peak modulation (p > 0.05 all pairings).
- DLS neurons encoded low-level egocentric kinematics (direction and speed of orienting and lever-press movements) in a manner invariant to sequential context (ordinal position, lever identity, sequence identity).
- Phase of the sequence could not be decoded from DLS activity when kinematics and phase were dissociated (flexible task), but could be decoded for stereotyped single sequences — indicating DLS tracks kinematics rather than sequence phase per se.
- DLS lesions severely impaired sequencing in AUTO (performance dropped to near chance, ~8.33%) and WM conditions chronically, while CUE sequencing recovered rapidly and remained largely intact post-lesion.
- DLS lesions affected movement kinematics similarly across all three conditions: decreased speed/vigor and increased trial-to-trial variability and roughness; post-lesion kinematics reverted to early-learning levels.
- DMS lesions had no lasting effect on sequencing or kinematics in any condition.
- Neural network model reproduced all key experimental findings: task-invariant DLS representations, selective disruption of AUTO sequencing on DLS removal, and kinematic degradation across conditions.
- Alternative models (scalar DLS output, boundary-only signals, no pretraining of downstream circuits) each failed to replicate the experimental data, supporting the full-kinematics, pretrained-downstream-circuit architecture.

---

### Computational framework

**Reinforcement learning / motor control with hierarchical circuit architecture.**

The paper uses a two-population neural network model in which a DLS-like feedforward network (trained via backpropagation with an RL-style trial loss) interacts with a pretrained recurrent downstream motor circuit. Key variables: DLS input/output weights (learned), downstream recurrent weights (pretrained on cued movements), velocity output (the quantity being controlled). The core assumption is that cortico-striatal and thalamo-striatal plasticity shapes DLS input weights on top of already-competent downstream motor circuits — a separation-of-timescales architecture that naturally explains both the task-invariance of DLS representations and the condition-specific dependence of sequencing on DLS.

---

### Prevailing model of the system under study

The introduction frames the basal ganglia as serving multiple potentially distinct roles in motor sequence execution depending on condition: (1) serial action selection for externally cued sequences; (2) internally generated execution drawing on working memory or long-term sensorimotor representations; (3) chunking — the conversion of discrete sequences into unified, automatically executed actions after extensive overtraining. The sensorimotor striatum (DLS/putamen in rodents) was widely associated with motor automaticity and with encoding sequential context (start/stop "chunking" signals, ordinal position, lever identity). The associative striatum (DMS/caudate) was associated with flexible, goal-directed behaviour. A prevailing expectation was that the neural implementation in DLS would differ across conditions — in particular that automatic execution would engage DLS differently from cued execution, consistent with the "chunking" hypothesis (sparsification of striatal activity at sequence boundaries after overtraining).

---

### What this paper contributes

The results challenge the chunking hypothesis: DLS does not show start/stop activity specific to automatic sequences, and its representations are not organised by ordinal position, sequential context, or lever identity. Instead, DLS encodes continuous kinematics uniformly across all task conditions. The causal lesion data then reveal a condition-specific role: DLS is necessary for the high-level sequential organisation of internally generated (AUTO and WM) sequences, but is dispensable for sequencing when visual cues are available. The paper reframes the BG's role in motor chunking: rather than selecting a pre-formed chunk from downstream circuits, the BG may *constitute* the chunk by providing the continuous kinematic specification that defines overtrained behavior. The finding that post-lesion kinematics revert to early-learning patterns also supports the specific role of DLS in adding learned task-specific kinematic refinements to species-typical motor programs. DMS is shown to be dispensable for both sequencing and kinematics in well-trained animals.

---

### Brain regions & systems

- **Dorsolateral striatum (DLS)** — sensorimotor arm of the basal ganglia; primary focus. Encodes egocentric movement kinematics in a task-condition-invariant way; causally required for high-level sequence organisation in internally generated (AUTO and WM) but not visually cued conditions; required for task-specific kinematic refinement across all conditions.
- **Dorsomedial striatum (DMS)** — associative arm of the basal ganglia; lesioned as comparison. Not required for sequencing or kinematics in any well-trained condition.
- **Brainstem / spinal cord** — proposed locus of species-typical motor programs that are modulated but not replaced by the BG; post-lesion kinematics revert to patterns consistent with brainstem-controlled movement.
- **Motor cortex** — mentioned as a circuit that may control cued sequencing post-DLS lesion; not directly investigated in this study.
- **Thalamus** — noted as part of the cortico-BG-thalamo-cortical loop; not directly investigated.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight.

1. It formalises an algorithm: DLS learns to produce continuous, time-varying kinematic control signals (rather than discrete chunk-selection signals) that are fed to pretrained downstream motor circuits. For internally generated sequences, these kinematic signals implicitly define the sequential structure; for cued sequences, downstream circuits can independently use sensory input.

2. It provides neural data (electrophysiology) that support this algorithm over alternatives: population recordings confirm kinematic-invariant coding inconsistent with sequential-context or chunking accounts, and lesion data dissociate conditions as predicted.

**Marr's levels:**

- **Computational**: The brain must efficiently execute learned motor sequences with adapted kinematics. For internally generated sequences (AUTO, WM), external cues cannot scaffold sequencing, so it must be internally represented. The BG provides a continuous kinematic specification that simultaneously implements fine-grained movement adaptation and encodes the sequential order implicitly.
- **Algorithmic**: DLS learns input-output mappings (via cortico-striatal plasticity) that transform task inputs into continuous, egocentric-kinematic population activity patterns. This activity modulates downstream recurrent motor circuits — which are already competent to respond to cues — to produce task-adapted kinematics. Sequential structure for AUTO sequences is not represented explicitly but emerges from the learned kinematic trajectory.
- **Implementational**: DLS (medium spiny neurons and fast-spiking interneurons, no meaningful coding differences between subtypes identified) encodes kinematics via a high-dimensional, time-varying population code. Downstream targets are likely brainstem circuits. Specific cell types, neuromodulators, and synaptic biophysics are not addressed. The model captures the BG's feedforward-to-recurrent circuit motif.

**Bonus**: The paper notes that DMS lesions leave kinematics unchanged, providing a dissociation between the two striatal regions at the implementational level.

---

### Limitations & open questions

- Only one overtrained sequence was used per rat in the AUTO condition; it is unknown whether results generalise to other repertoire sizes or sequence lengths.
- Small recording cohort (n = 4 rats for electrophysiology; 579 of 2,468 units analysed), limiting statistical power for within-unit comparisons.
- The neural network model uses backpropagation and Adam optimisation, which are biologically unrealistic learning rules; the model is intended as a computational-level account rather than a biologically faithful algorithm.
- The circuit(s) that support cued sequencing after DLS/DMS lesions remain unknown; motor cortex is suggested as a candidate but not tested.
- DMS's potential role in early motor sequence learning (as opposed to expert execution) remains an open question.
- Working memory trials (WM) showed intermediate lesion effects compared to AUTO and CUE, and the mechanism by which DLS supports WM-guided sequencing is not fully explained.
- Distinction between automaticity and habit formation was carefully designed against but not fully validated with devaluation tests in this cohort.
- Whether the kinematic-code view generalises to non-rat species or to motor sequences with more complex inter-element transitions is unknown.

---

### Connections & keywords

**Key citations:**
- Dhawale et al. 2021 (Nat. Neurosci.) — prior work from same lab establishing DLS role in kinematic specification
- Kawai et al. 2015 (Neuron) — motor cortex not required for execution of overtrained motor skills in rodents
- Jin & Costa 2010 (Nature) — start/stop signals in nigrostriatal circuits; chunking hypothesis
- Barnes et al. 2005 (Nature) — dynamic encoding and recoding of procedural memories in striatum
- Graybiel 1998 — BG and chunking of action repertoires
- Rueda-Orozco & Robbe 2015 (Nat. Neurosci.) — striatum multiplexes contextual and kinematic information
- Desmurget & Turner 2010 — motor sequences and the BG: kinematics, not habits
- Redgrave et al. 2010 — goal-directed and habitual control in BG; Parkinson's disease
- Mazzoni et al. 2007 — movement vigor and Parkinson's disease
- Dudman & Krakauer 2016 — BG and control of vigor

**Named models or frameworks:**
- Discrete sequence production (DSP) task / "piano" task
- Chunking hypothesis (BG as chunk selector)
- Kinematic specification hypothesis (BG as kinematic controller)
- Two-population neural network model (DLS + downstream recurrent motor circuits)

**Brain regions:**
- Dorsolateral striatum (DLS)
- Dorsomedial striatum (DMS)
- Brainstem / spinal cord
- Motor cortex (discussed)
- Thalamus (circuit context)

**Keywords:**
- motor sequence learning
- sensorimotor striatum
- basal ganglia
- motor automaticity
- movement kinematics
- chunking
- discrete sequence production task
- dorsolateral striatum lesion
- action selection
- neural population coding
- motor vigor
- internally generated sequences

### Related wiki pages
- [[wiki/topics/successor_representation_in_striatal_and_dopaminergic_reinforcement_learning|Successor representation in striatal and dopaminergic reinforcement learning]]
