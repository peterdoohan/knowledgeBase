---
source_file: chang2020_cuneiform_nucleus_locomotor_dbs.md
title: "Dissecting Brainstem Locomotor Circuits: Converging Evidence for Cuneiform Nucleus Stimulation"
authors: Stephano J. Chang, Iahn Cajigas, Ioan Opris, James D. Guest, Brian R. Noga
year: 2020
journal: Frontiers in Systems Neuroscience
paper_type: review
contribution_type: review
---

### One-line summary

Converging preclinical optogenetic evidence and clinical DBS outcome data argue that the cuneiform nucleus (CnF), not the pedunculopontine nucleus (PPN), is the superior brainstem target for treating freezing of gait and other neurological gait disorders.

---

### Background & motivation

Gait disturbances — including freezing of gait (FOG) in Parkinson's disease and progressive supranuclear palsy — affect more than 20% of adults over 60 and are refractory to dopaminergic therapies. Deep brain stimulation (DBS) of the pedunculopontine nucleus (PPN), chosen as the presumed neuroanatomical substrate of the mesencephalic locomotor region (MLR), was trialled in humans but produced disappointing and variable results. The paper argues that this failure reflects suboptimal targeting: the PPN is functionally heterogeneous and may not be the primary locomotor node of the MLR, whereas the adjacent cuneiform nucleus (CnF) has a clearer and more focused role in locomotor initiation and control.

---

### Methods

This is a perspective/review article synthesising preclinical and clinical literature. Key elements of the synthesis:

- Narrative review of electrical mapping, lesion, pharmacological, and optogenetic studies across species (mice, rats, cats, non-human primates, humans) addressing the functional organisation of the MLR.
- Summary and comparison of two major optogenetic studies (Caggiano et al., 2018; Josset et al., 2018) that selectively activated glutamatergic CnF vs. PPN neurons.
- Connectome-based review of cell-type-specific projection-terminal activation studies (Roseberry et al., 2016; Kroeger et al., 2017; Yoo et al., 2017; Assous et al., 2019; Dautan et al., 2016, 2020) dissecting PPN output pathways.
- Re-analysis and 3D reconstruction of clinical DBS electrode locations from Goetz et al. (2019) using Lead-DBS and MNI-space atlases to correlate electrode position with FOG outcome.
- No original data are collected; the paper relies entirely on reinterpretation of published datasets.

---

### Key findings

- Optogenetic photoactivation of glutamatergic CnF neurons robustly and consistently initiates locomotion at short latency across multiple independent studies (Roseberry et al., 2016; Caggiano et al., 2018; Josset et al., 2018; Dautan et al., 2020); photoinhibition arrests ongoing locomotion.
- Glutamatergic PPN neurons produce inconsistent locomotor results across studies — sometimes initiating low-speed locomotion with longer latency, sometimes decelerating locomotion or producing anxiety-like behavior — consistent with a functionally heterogeneous population.
- Cholinergic PPN neurons cannot initiate locomotion in any of three independent optogenetic studies; they may modulate speed during ongoing locomotion only.
- GABAergic MLR neurons stop locomotion, at least partly via local inhibition.
- Glutamatergic CnF neurons have focused connectivity: sparse inputs (mainly inferior colliculus and PAG) and focused descending output to reticulospinal neurons in the ventrocaudal medulla and monoaminergic nuclei (locus coeruleus, raphe).
- Glutamatergic PPN neurons receive inputs from numerous brain regions (basal ganglia, hypothalamus, frontal cortex, many brainstem nuclei) and project broadly, explaining their behavioral heterogeneity and unsuitability as a DBS target for a specific function.
- In the Goetz et al. (2019) clinical dataset, all "good responder" patients (34.1 ± 14% time in FOG with DBS off → 2.7 ± 2.6% with DBS on) had active electrode contacts in or bordering the CnF, not the PPN.
- Computer modelling of DBS in this region shows that lead shifts of as little as 1 mm significantly decrease target activation selectivity, highlighting the importance of precise CnF targeting.

---

### Computational framework

Not applicable in the formal modelling sense. The paper does not develop or apply a computational model. The mechanistic argument is circuit-level and connectomic: it maps cell-type-specific inputs, outputs, and electrophysiological properties onto locomotor behaviour to infer which nucleus instantiates the MLR's locomotor initiation function. The closest computational lens is a network/circuit account in which descending glutamatergic drive from CnF → reticulospinal neurons → spinal central pattern generators constitutes the functional pathway for gait control.

The results constrain future models of supraspinal locomotor control, particularly reinforcement learning or optimal control models that require a clear descending drive signal, and dynamical systems models of gait initiation that need an identified input node.

---

### Prevailing model of the system under study

The pre-existing consensus held that the MLR was functionally synonymous with — or at least centered on — the PPN, a cholinergic nucleus in the ventral mesopontine tegmentum. This view rested on: (1) histopathological findings of cholinergic PPN neurodegeneration in PD and PSP patients with dopamine-resistant FOG; (2) the hypothesis that hyperactive globus pallidus interna output excessively inhibits the PPN in PD, producing akinesia; (3) early NHP lesion studies showing akinesia after PPN lesions; and (4) the clinical translation into PPN DBS trials. The adjacent CnF was noted in the older electrical mapping literature as a locomotor-promoting site, but this evidence was overshadowed by the cholinergic-degeneration narrative linking PPN to Parkinsonian gait failure. The PPN was therefore treated as the primary therapeutic target.

---

### What this paper contributes

The review reframes the MLR debate by synthesising post-2016 optogenetic and connectomic evidence to make the following contributions:

1. Displaces cholinergic PPN neurons from the centre of the locomotor story: three independent optogenetic studies show they cannot initiate locomotion.
2. Separates CnF glutamatergic neurons — which have consistent, focused, short-latency locomotor initiation function — from PPN glutamatergic neurons, which are functionally heterogeneous and likely serve non-locomotor roles (reinforcement, arousal, striatal gating).
3. Provides an anatomical rationale for why PPN DBS trials yielded variable outcomes: the PPN's broad connectivity means stimulation recruits functionally diverse circuits.
4. Links these preclinical findings to clinical outcome data: the electrode-position analysis from Goetz et al. (2019) suggests that good FOG responders were those stimulating dorsal (CnF-bordering) contacts, not PPN.
5. Proposes a specific mechanistic hypothesis for DBS action: orthodromic activation of glutamatergic CnF efferents → reticulospinal neurons → spinal central pattern generators.

Before this synthesis, it was possible to argue that PPN cholinergic neurons were the key locomotor cells and that DBS failures were attributable to disease state or species differences. This review makes that position difficult to sustain, redirecting the field toward CnF as the therapeutic target.

---

### Brain regions & systems

- **Cuneiform nucleus (CnF)** — dorsal MLR; primary focus as the proposed superior DBS target; site of glutamatergic neurons that initiate and control locomotion; projects mainly to reticulospinal neurons in the ventrocaudal medulla.
- **Pedunculopontine nucleus (PPN)** — ventral MLR; historically targeted for DBS; cholinergic, glutamatergic, and GABAergic subpopulations with heterogeneous functions; cholinergic neurons degenerate in PD/PSP.
- **Mesencephalic locomotor region (MLR)** — physiologically defined midbrain area encompassing CnF and PPN; conserved across vertebrates; initiates locomotion when electrically stimulated at low threshold.
- **Periaqueductal gray (PAG)** — major input to glutamatergic CnF neurons; implicated in integrating sensorimotor and limbic signals upstream of locomotion.
- **Inferior colliculus (IC)** — provides monosynaptic input to glutamatergic CnF neurons.
- **Medullary reticular formation (ventrocaudal)** — downstream target of CnF glutamatergic efferents; contains reticulospinal neurons necessary and sufficient for MLR-evoked locomotion in mice.
- **Locus coeruleus (LC) and raphe nuclei** — receive CnF output; form monoaminergic descending pathways to spinal locomotor networks.
- **Globus pallidus interna** — sends dense inhibitory output to PPN area; hyperactivity in PD proposed to suppress PPN and cause akinesia (historical rationale for PPN DBS).
- **Subthalamic nucleus / substantia nigra** — mentioned as potential indirect targets modulated by MLR DBS.
- **Spinal central pattern generators** — ultimate downstream effectors for gait; activated via reticulospinal pathway from CnF.

---

### Mechanistic insight

The paper partially meets the bar. It synthesises optogenetic studies that formalise an algorithm (glutamatergic CnF neurons initiate locomotion by driving reticulospinal neurons, which activate spinal CPGs) and references neural data (optogenetics, tracing, electrophysiology) that support this algorithm over alternatives (cholinergic PPN, glutamatergic PPN). However, because the paper is a perspective review rather than a primary study, it does not itself provide neural recordings or stimulation data linking the specific circuit variables (e.g., CnF firing rates, reticulospinal discharge) to locomotor kinematics — it synthesises others' evidence.

Mapping onto Marr's levels using the cited evidence:

- **Computational**: the brain must generate a locomotor command signal with sufficient speed, focality, and amplitude to initiate gait and modulate its speed. The CnF provides this signal; the PPN's functional heterogeneity makes it unsuitable for this role.
- **Algorithmic**: glutamatergic CnF neurons integrate inputs from PAG and IC, and emit focused descending glutamatergic drive to reticulospinal neurons (and via LC/raphe, monoaminergic drive) that activate spinal CPGs; GABAergic MLR neurons locally suppress this signal to stop locomotion.
- **Implementational**: rapidly adapting, accommodating glutamatergic CnF neurons (distinct intrinsic membrane properties from heterogeneous PPN glutamatergic neurons; Dautan et al., 2020) project via vesicular glutamate transporter 2 (vGlut2)-expressing axons to the ventrocaudal medullary reticular formation. Monoaminergic pathways from LC and raphe provide spinal modulatory tone. Cholinergic PPN neurons are a distinct population that modulates but does not initiate locomotion.

The implementational level is the least complete: human CnF topography and the distribution of glutamatergic projection neurons in the human MLR remain unmapped, which limits translation.

---

### Limitations & open questions

- The paper is a perspective review; it draws conclusions from studies conducted in different species (mice, rats, cats, NHP, humans) under different conditions, and the degree to which mouse optogenetics translates to human gait control is uncertain.
- The distribution and topography of glutamatergic neurons in the human CnF and MLR have not been systematically mapped, limiting DBS targeting guidance.
- Mechanisms of DBS remain incompletely understood — it is unclear whether therapeutic benefit arises from orthodromic efferent activation, antidromic afferent effects, or network-level modulation.
- The clinical evidence (Goetz et al., 2019) is from a small, retrospective electrode-position analysis, not a prospective CnF-targeted trial.
- Neurodegeneration of non-cholinergic (including glutamatergic) neurons in CnF in PD/PSP patients raises the question of whether the CnF retains sufficient cellular integrity to respond to DBS.
- Species differences in MLR organisation (e.g., reverse cholinergic topography in humans vs. rats) mean preclinical findings may not translate directly.
- The functional role of glutamatergic PPN neurons in locomotion is not fully resolved — discrepancy between Caggiano et al. (2018) and Josset et al. (2018) due to methodological differences is acknowledged but not definitively settled.
- Optimal stimulation parameters, electrode geometry, and patient selection criteria for CnF DBS remain undefined.

---

### Connections & keywords

**Key citations:**
- Shik et al. (1966) — original MLR discovery in cats
- Caggiano et al. (2018), Nature — optogenetic dissection of CnF vs. PPN glutamatergic neurons and locomotor speed
- Josset et al. (2018), Current Biology — distinct contributions of CnF and PPN to locomotion in freely behaving mice
- Roseberry et al. (2016), Cell — cell-type-specific basal ganglia control of brainstem locomotor circuits
- Goetz et al. (2019), Neurosurgery — clinical DBS electrode-position analysis correlating CnF location with good FOG outcomes
- Dautan et al. (2020), BioRxiv — membrane properties and connectivity distinguishing CnF from PPN glutamatergic neurons
- Capelli et al. (2017), Nature — reticulospinal neurons necessary and sufficient for MLR-evoked locomotion
- Thevathasan et al. (2018), Movement Disorders — clinical review of PPN DBS in Parkinson's disease
- Karachi et al. (2010), JCI — cholinergic PPN lesions and gait/balance in macaques

**Named models or frameworks:**
- Mesencephalic locomotor region (MLR) — physiologically defined supraspinal locomotor node
- Lead-DBS — toolbox for DBS electrode localisation and visualisation used for clinical re-analysis
- Spinal central pattern generators (CPGs)

**Brain regions:**
- Cuneiform nucleus (CnF)
- Pedunculopontine nucleus (PPN)
- Periaqueductal gray (PAG)
- Inferior colliculus (IC)
- Medullary reticular formation / reticulospinal neurons
- Locus coeruleus (LC)
- Raphe nuclei
- Globus pallidus interna
- Subthalamic nucleus

**Keywords:**
- mesencephalic locomotor region (MLR)
- cuneiform nucleus DBS
- pedunculopontine nucleus
- freezing of gait
- Parkinson's disease
- glutamatergic locomotor neurons
- optogenetics brainstem locomotion
- reticulospinal pathway
- deep brain stimulation target selection
- brainstem locomotor circuits
- cell-type-specific circuit dissection
- gait disorder neuromodulation
