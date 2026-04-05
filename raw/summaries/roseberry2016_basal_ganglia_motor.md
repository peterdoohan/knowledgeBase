---
source_file: roseberry2016_basal_ganglia_motor.md
title: Cell-Type-Specific Control of Brainstem Locomotor Circuits by Basal Ganglia
authors: Thomas K. Roseberry, A. Moses Lee, Arnaud L. Lalive, Linda Wilbrecht, Antonello Bonci, Anatol C. Kreitzer
year: 2016
journal: Cell
paper_type: empirical
contribution_type: empirical
---

### One-line summary

The basal ganglia bi-directionally control locomotion through cell-type-specific modulation of glutamatergic neurons in the mesencephalic locomotor region (MLR).

### Background & motivation

The basal ganglia (BG) are essential for adaptive motor control, but the specific circuit mechanisms underlying pathway-specific modulation of target regions remain poorly understood. The canonical model proposes that direct pathway MSNs (dMSNs) facilitate movement and indirect pathway MSNs (iMSNs) suppress it, but how these pathways influence downstream motor circuits is unclear. The MLR is a key brainstem target of BG output, but the functional roles of its distinct cell types and their selective regulation by BG pathways were unknown.

### Methods

- Head-fixed spherical treadmill preparation to study locomotion in mice
- Optogenetic activation/inhibition using Cre-driver lines:
  - D1-Cre mice for dMSNs; A2a-Cre mice for iMSNs
  - vGLUT2-Cre for glutamatergic neurons; vGAT-Cre for GABAergic neurons
  - ChAT-ChR2 transgenic mice for cholinergic neurons
  - CaMKIIa promoter for targeting MLR glutamatergic neurons
- In vivo single-unit recordings combined with optogenetic identification (optotagging)
- Cell-type-specific G-deleted rabies virus tracing to map monosynaptic inputs
- ROC analysis to quantify locomotor state encoding
- Linear regression to identify speed-correlated neurons

### Key findings

- Electrical stimulation of MLR (overlapping Cun, PPTg, MRN) induced locomotion with short latencies (<2 s), confirming functional MLR location in mice.
- dMSN activation increased locomotion and excited 25 of 26 identified MLR glutamatergic neurons; excitation preceded movement onset (mean latency 176 ± 18 ms).
- iMSN activation suppressed locomotion and inhibited 25 of 27 identified MLR glutamatergic neurons; inhibition preceded deceleration (mean latency 460 ± 48 ms).
- Only MLR glutamatergic neurons were sufficient to elicit locomotion at short latencies (mean 211 ± 22 ms); stimulation produced graded speed responses based on frequency.
- MLR GABAergic neuron activation caused deceleration during running but no effect when stationary; these neurons locally inhibited other MLR neurons.
- MLR cholinergic neuron activation modulated locomotion speed only when mice were already running but was insufficient to initiate locomotion.
- MLR glutamatergic neuron firing highly predicted locomotor state (high ROC AUCs); firing rate during stationary state correlated with probability of subsequent locomotion onset.
- Photo-inhibition of MLR glutamatergic neurons rapidly stopped running animals (mean deceleration onset 835 ± 103 ms), demonstrating necessity for spontaneous locomotion.
- Rabies tracing revealed BG nuclei (SNr, EP, GPe, STN) densely innervate MLR glutamatergic neurons but project minimally to MLR GABAergic neurons.
- Inhibition of MLR glutamatergic neurons during dMSN stimulation abolished locomotion despite continued dMSN activation.
- Activation of MLR glutamatergic neurons during iMSN stimulation completely reversed locomotor suppression.
- Bidirectional control of locomotion by BG circuitry requires modulation of MLR glutamatergic neurons specifically.

### Computational framework

Not applicable. This is an empirical circuit mapping study. However, the results constrain models of basal ganglia action selection, supporting a model where the balance of direct and indirect pathway activity is read out at the level of MLR glutamatergic neuron firing rates to determine locomotor probability.

### Prevailing model of the system under study

The basal ganglia were understood to control locomotion through two pathways: direct pathway MSNs (dMSNs) facilitating movement and indirect pathway MSNs (iMSNs) suppressing movement. These pathways converge in the substantia nigra pars reticulata (SNr), which provides tonic inhibition of downstream motor structures. The MLR was known as a brainstem target of BG that could drive locomotion when stimulated, but the specific cell types involved and their selective regulation by BG pathways were unknown. The field assumed BG output modulated the MLR, but whether through disinhibition of excitatory neurons, inhibition of inhibitory neurons, or both, remained unclear.

### What this paper contributes

This paper establishes that MLR glutamatergic neurons are the specific cell type both necessary and sufficient for locomotion, and that these neurons are selectively targeted by basal ganglia output. The paper demonstrates that: (1) BG direct pathway activation excites MLR glutamatergic neurons and initiates locomotion; (2) BG indirect pathway activation inhibits MLR glutamatergic neurons and stops locomotion; (3) MLR glutamatergic neuron firing encodes locomotor state and speed; (4) bidirectional control of locomotion by BG circuitry requires modulation of MLR glutamatergic neurons specifically. This refines the canonical BG model by identifying the specific cell type (MLR glutamatergic neurons) that serves as the BG-to-locomotion interface and showing that BG control is mediated through excitation of these neurons by the direct pathway and inhibition by the indirect pathway.

### Brain regions & systems

- Basal ganglia — source of locomotor command; direct pathway (dMSNs) facilitates movement, indirect pathway (iMSNs) suppresses movement; outputs via SNr
- Striatum — input nucleus of BG; contains dMSNs (D1 receptor) and iMSNs (D2/A2a receptors)
- Substantia nigra pars reticulata (SNr) — primary output nucleus of BG in rodents; provides tonic inhibition of downstream structures
- Mesencephalic locomotor region (MLR) — brainstem target of BG; overlaps with cuneiform nucleus (Cun), pedunculopontine tegmental nucleus (PPTg), and mesencephalic reticular nucleus (MRN)
- MLR glutamatergic neurons — necessary and sufficient for locomotion; encode locomotor state and speed; selectively targeted by BG output
- MLR GABAergic neurons — suppress locomotion via local inhibition; receive limbic inputs (amygdala, PAG, BNST)
- MLR cholinergic neurons — modulate locomotion but insufficient to initiate it; may regulate brain state
- Spinal cord — final output for locomotion via reticulospinal tracts
- Central amygdala and oval BNST — provide dense projections to MLR glutamatergic neurons; GABAergic nuclei potentially involved in fear/anxiety behaviors
- Superior colliculus — connects to MLR; involved in orienting behavior

### Mechanistic insight

This paper provides strong mechanistic insight by identifying a specific neural circuit mechanism for basal ganglia control of locomotion. The evidence supports a model where:

- **Computational level:** The brain must decide when to initiate or suppress locomotion based on internal state and environmental demands.
- **Algorithmic level:** The basal ganglia compute this decision through the balance of direct and indirect pathway activity, which is read out as the firing rate of MLR glutamatergic neurons. Higher firing rates increase the probability of locomotion initiation; lower firing rates suppress it.
- **Implementational level:** Direct pathway MSNs (dMSNs) in the striatum project through the SNr to excite MLR glutamatergic neurons, while indirect pathway MSNs (iMSNs) project through the SNr to inhibit these same neurons. The MLR glutamatergic neurons then project to reticulospinal systems to drive locomotion. This represents a cell-type-specific disynaptic circuit from cortex/striatum to brainstem locomotor centers.

### Limitations & open questions

- The study was conducted in head-fixed mice on a spherical treadmill, which may not capture all aspects of natural locomotion.
- The study focused on running locomotion; whether similar mechanisms apply to other types of motor behavior (e.g., turning, postural adjustments) is unclear.
- The specific biophysical mechanisms by which BG inputs excite or inhibit MLR glutamatergic neurons (e.g., disynaptic disinhibition vs. direct excitation) are not fully characterized.
- The role of the small subset of MLR glutamatergic neurons that are most active during stationary states remains unclear.
- The potential role of cholinergic neurons in gating brain state versus locomotion specifically warrants further investigation.
- Whether the observed circuit mechanisms generalize to other species or to pathological conditions (e.g., Parkinson's disease) requires further study.

### Connections & keywords

- **Key citations:** Kravitz et al. 2010 (BG pathways and locomotion), Lee et al. 2014 (MLR and cortical state), Shik et al. 1966 (MLR discovery), Hikosaka et al. 2000 (BG and saccades), Grillner et al. 2005, 2008 (locomotor control), Albin et al. 1989, DeLong 1990 (canonical BG model)
- **Named models or frameworks:** Canonical BG direct/indirect pathway model, MLR (mesencephalic locomotor region), disynaptic disinhibition, cell-type-specific optogenetics
- **Brain regions:** Basal ganglia, striatum, substantia nigra pars reticulata (SNr), mesencephalic locomotor region (MLR), cuneiform nucleus (Cun), pedunculopontine tegmental nucleus (PPTg), mesencephalic reticular nucleus (MRN), spinal cord, central amygdala, bed nucleus of the stria terminalis (BNST), superior colliculus
- **Keywords:** basal ganglia, mesencephalic locomotor region, MLR, direct pathway, indirect pathway, dMSN, iMSN, optogenetics, cell-type-specific, glutamatergic neurons, GABAergic neurons, cholinergic neurons, locomotion, motor control, brainstem, SNr, striatum, rabies tracing, electrophysiology, action selection
