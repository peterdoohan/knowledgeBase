---
source_file: davis2013_homeostatic_signaling_neural_stabilization.md
paper_id: davis2013_homeostatic_signaling_neural_stabilization
title: "Homeostatic Signaling and the Stabilization of Neural Function"
authors:
  - "Graeme W. Davis"
year: 2013
journal: Neuron
paper_type: review
contribution_type: review
species:
  - human
methods:
  - calcium_imaging
  - optogenetics
  - electrophysiology
  - computational_modeling
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - visual_cortex
keywords:
  - homeostatic_plasticity
  - synaptic_scaling
  - presynaptic_homeostasis
  - intrinsic_excitability
  - readily_releasable_pool
  - cav2_1_calcium_channel
  - deg_enac_sodium_channel
  - rim_rab3_interacting_molecule
  - set_point_stabilisation
  - ion_channel_rebalancing
  - bmp_permissive_signalling
  - tor_s6k_synaptic_maintenance
  - homeostatic
  - signaling
  - stabilization
  - neural
  - function
---

### One-line summary

Homeostatic plasticity mechanisms — including intrinsic excitability control, synaptic scaling, and presynaptic homeostasis — stabilize neural activity at cell-type-specific set points and are emerging as central to neural function, development, and disease.

---

### Background & motivation

Neural circuits must remain stable and reproducible despite constant experiential change and genetic variation, yet also retain the capacity for learning-related plasticity. The coexistence of Hebbian (destabilising) and homeostatic (stabilising) plasticity presents a fundamental tension. This perspective addresses the gap by surveying the rapidly growing field of homeostatic signalling: how individual neurons and circuits detect deviations from a set point and deploy compensatory mechanisms to restore baseline activity. Understanding these mechanisms is essential because their failure may underlie neurological and psychiatric diseases including autism spectrum disorders and schizophrenia.

---

### Methods

This is a narrative review. It synthesises experimental findings across:

- Multiple model systems: Drosophila neuromuscular junction (NMJ), Aplysia, crustacean stomatogastric ganglion, mammalian cultured neurons, and in vivo rodent cortex
- Three major homeostatic effector domains: (1) intrinsic excitability, (2) postsynaptic synaptic scaling, (3) presynaptic neurotransmitter release
- Experimental approaches surveyed include: chronic activity blockade (TTX, pharmacological), genetic ion channel knockouts, optogenetic stimulation, forward genetic screens in Drosophila, calcium imaging, variance-mean analysis, in vivo electrophysiology
- No formal inclusion criteria or meta-analytic methods; synthesis is narrative and organised thematically

---

### Key findings

- Neurons homeostatically rebalance ion channel expression to restore cell-type-specific firing properties after channel gene deletion or chronic activity disruption; this is quantitatively accurate but can be compartment-specific (e.g., somatic but not dendritic restoration in Kv4.2 knockouts).
- Synaptic scaling bidirectionally adjusts neurotransmitter receptor abundance in a multiplicative, cell-wide fashion in response to chronic activity changes; it can also be synapse-specific and input-specific.
- Presynaptic homeostasis at the Drosophila NMJ precisely compensates for postsynaptic receptor impairment via two parallel mechanisms: increased presynaptic calcium influx (through CaV2.1, gated by DEG/ENaC sodium leak channels) and expansion of the readily releasable pool of vesicles (requiring RIM and Rab3-GAP).
- RIM mutations block RRP modulation but not calcium influx changes, and are sufficient to abolish presynaptic homeostasis, establishing RRP regulation as the obligate convergence point.
- Permissive signals (BMP at the Drosophila NMJ; TNF-α at mammalian synapses) gate whether homeostatic plasticity can be expressed without instructing its timing or magnitude.
- Presynaptic homeostasis is developmentally uncoupled from NMJ growth: acute blockade of ENaC channels erases compensation without affecting synapse anatomy.
- Forward genetic screening implicates the schizophrenia-associated gene dysbindin in presynaptic homeostasis; fragile X and autism-related genes (Homer, mGluR, retinoic acid pathway) implicate synaptic scaling in neurodevelopmental disease.
- TOR/S6K signalling is required for the sustained maintenance (but not rapid induction) of presynaptic homeostasis, linking metabolic sensing to homeostatic effector expression.

---

### Computational framework

The paper does not develop a formal computational model, but it repeatedly invokes control-theoretic language as a conceptual scaffold:

- **Set point**: the cell-type-specific activity level that homeostatic systems defend.
- **Error signal**: the difference between actual and set-point activity, sensed via calcium-dependent pathways (CamKK/CamKIV) and potentially metabolic sensors (eEF2, TOR).
- **Feedback control**: effectors (ion channel rebalancing, receptor trafficking, presynaptic release) are deployed to null the error signal.
- **Quantitative accuracy**: compensation is graded and matches perturbation magnitude over wide parameter ranges, analogous to integral feedback control in engineering.

The review references theoretical/computational work from the stomatogastric system (Marder, Prinz) showing that multiple combinations of ion channel densities can generate the same target firing pattern — framing the set-point problem as one of navigating a high-dimensional solution space under homeostatic feedback.

---

### Prevailing model of the system under study

Prior to and surrounding this review, the dominant framework in synaptic plasticity was Hebbian: activity-dependent changes in synaptic strength (LTP/LDP) were seen as the primary substrate for learning and memory. The problem of stability — why runaway excitation or silencing does not result from unconstrained Hebbian plasticity — was recognised but underappreciated mechanistically. The paper is written against the backdrop of an emerging consensus that dedicated homeostatic mechanisms exist and are as fundamental as Hebbian plasticity. The prior understanding included isolated demonstrations of synaptic scaling (Turrigiano 1998) and presynaptic homeostasis (Davis & Goodman 1998), but no unified mechanistic account. The introduction of this Perspective signals that the field is shifting from phenomenology toward molecular mechanism, and from in vitro demonstration toward in vivo relevance.

---

### What this paper contributes

This review synthesises a field that had reached sufficient mechanistic depth to begin cross-system comparison and disease application. Key contributions as a review:

1. **Mechanistic consolidation**: establishes the two-component model of presynaptic homeostasis (calcium influx + RRP) as a field consensus, grounded in Drosophila genetics.
2. **Cross-system generalisation**: draws explicit parallels between invertebrate and mammalian homeostatic mechanisms, arguing for evolutionary conservation.
3. **Disease relevance**: articulates how homeostatic plasticity genes (dysbindin, Homer, mGluR) connect to schizophrenia, fragile X, and ASD — reframing these as homeostatic disorders.
4. **Open problems**: identifies that the molecular basis of the set point, the sensor mechanisms, and the coordination of multiple homeostatic effectors remain unknown, framing the research agenda.

---

### Brain regions & systems

- **Drosophila neuromuscular junction (NMJ)** — primary model system for presynaptic homeostasis; provides genetic tractability for forward screening.
- **Mammalian hippocampus (CA1, cultured neurons)** — main model for synaptic scaling (postsynaptic receptor trafficking); also implicated in presynaptic homeostasis via CDK5/calcineurin.
- **Visual cortex** — cited for in vivo evidence of firing rate homeostasis and interaction with ocular dominance plasticity.
- **Crustacean stomatogastric ganglion** — model for intrinsic excitability homeostasis and computational modelling of set-point maintenance.
- **Xenopus optic tectum** — cited for sensory modality-specific homeostatic plasticity.
- **Developing vertebrate spinal cord** — cited for circuit-level homeostatic control of spontaneous network activity.

---

### Mechanistic insight

The paper meets the bar for the presynaptic homeostasis component:

**Phenomenon**: At the Drosophila NMJ, pharmacological or genetic reduction of postsynaptic glutamate receptor sensitivity is precisely compensated by a graded increase in presynaptic neurotransmitter release, restoring set-point muscle depolarisation.

- **Computational level**: The brain (motoneuron) solves the problem of maintaining constant postsynaptic depolarisation in the face of unpredictable variation in receptor function; this is a feedback control problem requiring detection of an error signal proportional to receptor efficacy.
- **Algorithmic level**: Two parallel processes implement the solution: (1) ENaC sodium-leak channel insertion near the nerve terminal causes a modest depolarisation of resting potential, increasing CaV2.1-mediated calcium influx; (2) RIM-dependent expansion of the readily releasable pool of vesicles. Both are necessary; neither is sufficient alone. The RRP pathway is the obligate convergence point (blocked by RIM loss-of-function, which abolishes compensation even when calcium influx is intact).
- **Implementational level**: Presynaptic DEG/ENaC channels (pickpocket11/16 subunits) are transcriptionally upregulated after persistent receptor perturbation; RIM and RIM-binding protein scaffold vesicles at the active zone; Rab3/Rab3-GAP bridge calcium channels to vesicles. Permissive BMP retrograde signalling from muscle to motoneuron soma is required for homeostatic competence. TOR/S6K is required for sustained (not rapid) expression.

**Bonus**: The review identifies specific molecular players at the implementational level (ENaC subunits, RIM, RBP, Rab3, CDK5, calcineurin, CaV2.1/2.2), although causal evidence for the complete pathway is distributed across multiple cited studies rather than being fully established in a single experiment.

For synaptic scaling in mammals, the evidence meets the algorithmic level (receptor trafficking machinery, immediate early genes) but lacks single-paper mechanistic closure linking sensors to effectors in vivo.

---

### Limitations & open questions

- The molecular identity of the activity sensor(s) — what precisely detects the error between actual and set-point activity — remains unknown; calcium signalling is implicated but insufficient as a complete account.
- How multiple homeostatic effectors (intrinsic excitability, scaling, presynaptic homeostasis) are coordinated within a single neuron is unresolved.
- How the genomic set point is specified — the link between terminal selector transcription factors, ion channel expression, and homeostatic feedback — is not molecularly defined.
- Whether homeostatic plasticity participates in normal development (as opposed to correcting perturbations) is unclear; data from Drosophila suggest it is uncoupled from normal NMJ growth, but the mammalian case is unresolved.
- The in vivo relevance of synaptic scaling and presynaptic homeostasis for behaviour and learning is not established at the time of writing.
- Whether compensation is perfectly accurate or systematically imperfect in specific compartments (e.g., dendrites) has disease-relevant implications that are unexplored.

---

### Connections & keywords

**Key citations**:
- Turrigiano et al. (1998) — synaptic scaling discovery
- Davis & Goodman (1998a, 1998b) — presynaptic homeostasis at Drosophila NMJ
- Frank et al. (2006) — rapid induction and sustained expression of presynaptic homeostasis
- Muller et al. (2012) — RIM and RRP modulation in presynaptic homeostasis
- Younger et al. (2013) — ENaC channels as presynaptic homeostasis effectors
- Prinz et al. (2004); Marder (2011) — computational modelling of set-point degeneracy in stomatogastric ganglion
- Dickman & Davis (2009) — dysbindin/schizophrenia link via homeostatic screen
- Keck et al. (2013); Hengen et al. (2013) — in vivo firing rate homeostasis in visual cortex
- Nerbonne et al. (2008) — Kv4.2 knockout homeostatic rebalancing

**Named models or frameworks**:
- Synaptic homeostasis / presynaptic homeostasis
- Synaptic scaling
- Terminal selector transcription factors (Hobert, C. elegans)
- Homeostatic set point model
- Variance-mean analysis (for RRP estimation)

**Brain regions**:
- Drosophila neuromuscular junction
- Hippocampus (CA1)
- Visual cortex
- Crustacean stomatogastric ganglion
- Xenopus optic tectum
- Vertebrate spinal cord

**Keywords**:
- homeostatic plasticity
- synaptic scaling
- presynaptic homeostasis
- intrinsic excitability
- readily releasable pool
- CaV2.1 calcium channel
- DEG/ENaC sodium channel
- RIM (Rab3 Interacting Molecule)
- set point stabilisation
- ion channel rebalancing
- BMP permissive signalling
- TOR/S6K synaptic maintenance
