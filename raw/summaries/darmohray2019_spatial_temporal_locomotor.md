---
source_file: "darmohray2019_spatial_temporal_locomotor.md"
paper_id: "darmohray2019_spatial_temporal_locomotor"
title: "Spatial and Temporal Locomotor Learning in Mouse Cerebellum"
authors: "Dana M. Darmohray, Jovin R. Jacobs, Hugo G. Marques, Megan R. Carey"
year: 2019
journal: "Neuron"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse", "human"]
methods: ["optogenetics"]
keywords: ["spatial", "temporal", "locomotor", "learning", "mouse", "cerebellum"]
---

### One-line summary

Split-belt treadmill locomotor adaptation in mice is cerebellum-dependent (specifically requiring paravermal Purkinje cells projecting to the interposed nucleus), and its spatial and temporal components are dissociable at the circuit level.

---

### Background & motivation

Stable locomotion requires precise coordination of movement across all four limbs, and the cerebellum is critical for this via error-driven motor adaptation. The split-belt treadmill — which imposes different speeds under each side of the body — has been used in humans and cats to study locomotor adaptation, but had not been established in mice, preventing investigation of the underlying neural circuit mechanisms with genetic tools. Human locomotor adaptation has separable spatial and temporal components that adapt at different rates, but the circuit-level basis for this dissociation was unknown. This paper establishes a mouse model of split-belt adaptation and uses cell-type-specific chemogenetics to begin to resolve the cerebellar circuits involved.

---

### Methods

- **Subjects**: Adult wild-type mice; cerebellar mutant lines (reeler, Purkinje cell degeneration/pcd); somatomotor cortex-lesioned mice; L7-Cre mice for Purkinje cell targeting.
- **Task**: Custom transparent split-belt treadmill with high-speed camera and LocoMouse tracking algorithm (nose, tail, four paws); baseline/split/washout protocol with ~2:1 belt speed ratio; single and multi-session (up to 30 min total) protocols.
- **Key measurements**: Stride length (individual limb), step length and step-length asymmetry (interlimb), center of oscillation (spatial component), double support asymmetry (temporal component), stance phasing for individual limbs.
- **Cerebellar manipulations**: Ataxic mutants (reeler, pcd) vs. littermate controls; bilateral aspiration of forelimb somatomotor cortex; cell-type-specific chemogenetics (retrograde AAV in L7-Cre mice) to express inhibitory DREADD hM4Di in Purkinje cells projecting to medial, interposed, or lateral cerebellar nuclei; CNO vs. saline intra-animal comparisons.
- **Analysis**: Exponential decay fitting to adaptation/washout curves; simulation model mapping spatiotemporal contributions to step-length asymmetry; analytical model (Finley et al., 2015) for spatial/temporal contributions in mm.

---

### Key findings

- Mouse split-belt adaptation shows the hallmarks of human locomotor adaptation: gradual change in interlimb (step length) symmetry during the split phase, prominent aftereffects upon return to tied belts, and no adaptation of individual limb parameters (stride length).
- Adaptation is context-specific: aftereffects do not transfer from treadmill to overground walking.
- No evidence of savings (faster relearning) upon re-exposure to the split-belt perturbation.
- Spatial adaptation (center of oscillation) and temporal adaptation (double support) proceed at different rates; temporal adaptation is faster (tau ~494 strides) than spatial adaptation (tau ~590 strides).
- Both reeler and pcd cerebellar mutants showed a complete absence of step-length adaptation despite normal reactive stride-length scaling, establishing a specific cerebellar requirement.
- Large bilateral lesions of forelimb primary motor and somatosensory cortex left adaptation fully intact.
- Chemogenetic inhibition (CNO) of Purkinje cells projecting to the interposed nucleus significantly impaired step-length adaptation; targeting the medial or lateral nucleus had no effect (step-length aftereffect, interposed CNO vs. saline: t(9) = 3.24, p = 0.01).
- All four limbs contribute to spatial adaptation; temporal adaptation is driven specifically by adjustment of the front fast limb's timing relative to the other three.
- Spatial adaptation was impaired by interposed-nucleus DREADD activation regardless of fast-belt laterality; temporal adaptation was impaired only when the injection was ipsilateral to the fast belt — consistent with predominantly ipsilateral cerebellar control and the fact that only the fast front limb drives temporal adaptation.
- When spatial adaptation was selectively blocked (contra-fast condition), no compensatory over-adaptation of temporal parameters was observed, supporting the independence of the two learning processes.

---

### Computational framework

The paper uses a **motor adaptation / internal model** framework, conceptualising locomotor learning as error-driven calibration: when a predictable perturbation is applied, the motor system gradually adjusts to minimise error. This is the standard cerebellar motor-adaptation framework (cf. Marr-Albus-Ito; Raymond and Medina, 2018).

A custom simulation model was built to map the full space of spatiotemporal combinations onto predicted step-length asymmetry. By treating strides as fixed triangle waveforms and shifting one limb's waveform relative to another in space and/or time, the authors generated a predictive mapping of step-length error across the adaptation trajectory (R² = 0.83). This is used descriptively to decompose observed adaptation into spatial and temporal contributions rather than as a mechanistic learning model. The specific error signals that drive locomotor adaptation are explicitly noted as unknown.

---

### Prevailing model of the system under study

The background model is that locomotion is a multi-level control hierarchy: the spinal cord generates basic rhythmic patterns via central pattern generators, brainstem/midbrain structures modulate speed and initiation, and the cerebellum is specifically required for coordinating movements across joints and limbs. The cerebellum was already known to be critical for split-belt adaptation in humans (Morton and Bastian, 2006) and decerebrate cats (Yanagihara and Kondo, 1996), and for motor adaptation more generally via error-driven learning. Human split-belt adaptation was known to have dissociable spatial and temporal components at the behavioural level, with different rates and developmental onsets. However, the paper notes that insights into cerebellar circuit mechanisms for learning had come almost exclusively from simpler reflexive behaviours (VOR, eyeblink conditioning), and that it was unknown which cerebellar sub-regions or circuit elements underlie the spatial/temporal dissociation observed behaviourally in locomotor adaptation. The assumption was that the intermediate cerebellum (paravermal cortex / interposed nucleus) would be relevant given its known role in precise limb placement and interlimb coordination, but this had not been directly tested.

---

### What this paper contributes

This paper establishes the first validated mouse model of split-belt locomotor adaptation, demonstrating that the key features of human locomotor adaptation (interlimb specificity, spatiotemporal dissociation, context specificity, no savings, cerebellar dependence, cortical independence) are conserved in mice. This makes the task amenable to genetic dissection.

The central new finding is that a relatively restricted population of paravermal Purkinje cells projecting to the interposed cerebellar nucleus is necessary for split-belt adaptation, while the medial and lateral cerebellar nuclei are not. This localises the locus of plasticity far more specifically than prior lesion work.

Beyond localisation, the paper reveals that spatial and temporal components of locomotor adaptation have distinct circuit implementations within this same cerebellar sub-region: spatial adaptation requires bilateral interposed Purkinje cell activity (consistent with the bilateral limb changes), whereas temporal adaptation requires ipsilateral activity (consistent with the unilateral fast-limb timing adjustment). This is the first direct circuit-level evidence for the long-inferred dissociation of spatial and temporal locomotor learning, and it constrains mechanistic accounts: the two components are not merely different timescales of a single learning process but depend on at least partially separate circuit implementations.

---

### Brain regions & systems

- **Intermediate cerebellum (paravermal cortex / interposed nucleus)**: Required for split-belt locomotor adaptation; Purkinje cells in this zone are the locus at which spatial and temporal learning are dissociable.
- **Medial cerebellum (vermis / fastigial nucleus)**: Not required for split-belt adaptation; associated with balance and posture via vestibular connectivity.
- **Lateral cerebellum (hemispheres / dentate nucleus)**: Not required for split-belt adaptation; associated with thalamocortical pathways and voluntary motor planning.
- **Somatomotor cerebral cortex (forelimb M1 and S1)**: Bilateral aspiration leaves adaptation intact; ruled out as necessary locus.
- **Spinal cord / CPGs**: Generate basic rhythmic locomotion; reactive stride-length scaling to belt-speed changes is preserved in all lesion conditions, implying these operate independently of cerebellar learning.

---

### Mechanistic insight

The paper meets both criteria for this section. It proposes a functional algorithm — error-driven calibration of interlimb coordination via paravermal Purkinje cells — and provides neural perturbation data (cell-type-specific chemogenetics) that support this algorithm's localisation and that specifically distinguish spatial and temporal circuit contributions.

- **Computational level**: The brain must maintain symmetric interlimb coordination during locomotion despite external perturbations. When perturbation is predictable and persistent, the motor system forms an internal model to compensate prospectively rather than reactively.
- **Algorithmic level**: Spatial adaptation involves adjusting the center of oscillation of all four limbs bilaterally; temporal adaptation involves adjusting the relative timing of the single fast front limb against the other three. These two adjustments draw on at least partially separate neural substrates within the paravermal cerebellum / interposed nucleus circuit and proceed at different rates (temporal faster than spatial).
- **Implementational level**: The critical neurons are Purkinje cells in paravermal cerebellar cortex (around the primary fissure) whose axons terminate in the interposed nucleus. Chemogenetic silencing of this specific population (via retrograde viral DREADD targeting in L7-Cre mice) selectively impairs adaptation without disrupting baseline gait or reactive stride adjustments. The lateralisation data further suggest that ipsilateral Purkinje cell activity is uniquely required for temporal adaptation, reflecting the predominantly ipsilateral cerebellar output to spinal/brainstem motor circuits.

**Bonus**: The paper does not resolve which specific cell types within the interposed nucleus (e.g., nucleo-olivary projection neurons versus tecto- or rubrospinal targets) carry the learned signal downstream, and notes that some retrograde labelling appeared in nucleo-olivary neurons; this is flagged as a limitation. The identity of the climbing fibre error signals is also unspecified.

---

### Limitations & open questions

- The chemogenetic approach produces sustained (~hours) suppression; it cannot resolve when during learning the interposed nucleus activity is required (acquisition vs. storage vs. expression).
- The retrograde virus also labelled a subset of nucleo-olivary projection neurons in the DCN, meaning the DREADD effect cannot be attributed exclusively to Purkinje cell input without additional controls.
- Cerebral cortex lesions were made post-training; compensatory mechanisms during recovery cannot be ruled out, though this is partially addressed by noting the lack of compensation in chronic cerebellar mutants.
- The paper cannot identify the specific error signals (climbing fibre inputs) that drive spatial vs. temporal adaptation.
- Hindlimb adaptation is weaker, slower, and purely spatial compared to forelimbs; whether this reflects secondary adjustments to front-limb learning or independent cerebellar learning is unresolved.
- The absence of savings in mice (unlike humans) raises the question of whether savings in humans reflects a cortical contribution that is absent in mice, but this remains speculative.
- Downstream connectivity from interposed nucleus to spinal/brainstem locomotor circuits mediating spatial vs. temporal learning is not mapped.

---

### Connections & keywords

**Key citations**:
- Reisman et al. (2005) — foundational human split-belt adaptation study
- Morton and Bastian (2006) — cerebellar patients and split-belt adaptation
- Malone et al. (2011, 2012) — spatial/temporal dissociation in human locomotor adaptation
- Machado et al. (2015) — LocoMouse tracking; pcd gait ataxia characterisation
- Yanagihara and Kondo (1996) — cerebellar requirement in cat split-belt adaptation
- Finley et al. (2015) — analytical model for spatial/temporal contributions to step length
- Torres-Oviedo and Bastian (2010) — context specificity of locomotor adaptation
- Raymond and Medina (2018) — cerebellar motor adaptation review

**Named models or frameworks**:
- LocoMouse (tracking algorithm for mouse whole-body locomotion)
- Split-belt treadmill paradigm
- DREADD chemogenetics (hM4Di, L7-Cre retrograde AAV targeting)
- Finley et al. (2015) analytical spatiotemporal decomposition model

**Brain regions**:
- Intermediate cerebellum / paravermal cortex
- Interposed cerebellar nucleus
- Medial cerebellum / fastigial nucleus
- Lateral cerebellum / dentate nucleus
- Forelimb primary motor cortex (M1)
- Forelimb somatosensory cortex (S1)

**Keywords**:
- split-belt treadmill adaptation
- locomotor learning
- interlimb coordination
- spatial vs. temporal adaptation
- intermediate cerebellum
- interposed nucleus
- Purkinje cells
- chemogenetics / DREADD
- motor adaptation
- center of oscillation
- double support asymmetry
- cerebellar circuit dissociation
