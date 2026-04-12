---
source_file: grillner2020_motor_control_locomotion.md
paper_id: grillner2020_motor_control_locomotion
title: "Current Principles of Motor Control, with Special Reference to Vertebrate Locomotion"
authors:
  - "Sten Grillner"
  - "Abdeljabbar El Manira"
year: 2020
journal: "Physiological Reviews"
paper_type: review
contribution_type: review
species:
  - mouse
methods:
  - optogenetics
  - computational_modeling
brain_regions:
  - striatum
  - nucleus_accumbens
  - ventral_tegmental_area
  - substantia_nigra
  - thalamus
  - zona_incerta
  - periaqueductal_gray
keywords:
  - central_pattern_generators
  - vertebrate_locomotion
  - basal_ganglia_disinhibition
  - mesencephalic_locomotor_region
  - reticulospinal_neurons
  - spinal_interneurons
  - v2a_interneurons
  - modular_cpg_organization
  - sensory_cpg_interaction
  - phase_dependent_reflex_reversal
  - spinocerebellar_tract
  - comparative_vertebrate_neuroscience
  - current
  - principles
  - motor
  - control
  - special
  - reference
  - vertebrate
  - locomotion
---

### One-line summary

A comprehensive review of vertebrate locomotor control spanning all levels from basal ganglia behavior selection, through brainstem command systems, to the cellular and synaptic organization of spinal central pattern generators (CPGs), synthesising insights from lamprey to humans.

---

### Background & motivation

Locomotion is the motor behaviour in which the most mechanistic knowledge has accumulated across vertebrates, yet no single synthesis had covered the entire hierarchy from forebrain selection to spinal microcircuitry. Prior reviews tended to focus on individual levels (spinal CPGs, brainstem commands, or basal ganglia) in isolation. This review aims to integrate all major subsystems — forebrain, brainstem, spinal cord, cerebellum, sensory feedback, postural control, and steering — into a unified account of how goal-directed locomotion is produced. It also exploits comparative data from lamprey, zebrafish, and rodents to argue that the basic vertebrate motor architecture is evolutionarily conserved across ~560 million years.

---

### Methods

This is a narrative review of primary literature covering:

- Electrophysiological, anatomical, pharmacological, genetic, and optogenetic studies across multiple model organisms (lamprey, Xenopus tadpole, zebrafish, mouse, cat, human).
- Coverage extends from in vitro isolated spinal cord preparations to behaving intact animals.
- Key experimental approaches synthesised include: fictive locomotion recordings, deafferentation, dorsal root transection, spinal cord transection and training, decerebrate preparations, MLR/DLR stimulation, viral tracing, optogenetic activation/silencing of molecularly defined interneuron classes (V0, V1, V2a, V2b, V3, dI6, Hb9, Shox2), large-scale computational modelling of spinal networks, and split-belt treadmill adaptation paradigms.
- Scope: all vertebrate classes from protochordate Ciona to primates; locomotion including swimming, walking, precision stepping, steering, and posture.

---

### Key findings

- The fundamental neural architecture for locomotion — basal ganglia, MLR/DLR command systems, reticulospinal pathways, spinal CPGs — is conserved from lamprey to mammals, having evolved before the lamprey–mammal split ~560 million years ago.
- The basal ganglia control behaviour selection via disinhibition: tonic GABAergic output from SNr/GPi suppresses brainstem motor centres at rest; striatal D1R direct-pathway activation removes this inhibition to initiate locomotion; D2R indirect-pathway activation reinforces inhibition to suppress movement.
- Optogenetic studies (Roseberry et al.) confirm that direct-pathway D1R striatal neuron activation drives MLR glutamatergic neurons and initiates locomotion; D2R pathway activation reduces locomotor activity.
- Within MLR, the cuneiform nucleus and PPN are functionally distinct: cuneiform mediates fast/escape locomotion, PPN glutamatergic neurons mediate slower exploratory locomotion; PPN cholinergic neurons facilitate but do not initiate locomotion.
- Glutamatergic reticulospinal neurons in LPGi (lateral paragigantocellular nucleus) are the main interface between MLR and spinal CPGs across a wide speed range; intermingled glycinergic LPGi neurons halt locomotion; pontine Chx10-expressing neurons produce a smooth sit-down stop.
- Locomotor CPGs can generate the full complex four-phase motor pattern (support, lift-up, swing, touch-down) independently of sensory feedback, demonstrated by persistence of the detailed EMG pattern after deafferentation (dorsal root transection) in cats.
- The half-centre hypothesis is insufficient: isolated hemi-segments can generate rhythmic activity; inhibitory blockade does not abolish rhythmicity but switches alternation to synchrony, confirming that burst generation precedes and is independent of reciprocal inhibition for rhythm per se.
- In zebrafish, V2a excitatory interneurons are both necessary and sufficient for rhythm generation; they are organised into three speed modules (slow, intermediate, fast) with correspondingly selective synaptic connectivity to slow, intermediate, and fast motoneurons — contradicting the single-network CPG view.
- Motoneurons are bona fide CPG members, not merely passive output: gap junction feedback from motoneurons to V2a interneurons (zebrafish) and ionotropic glutamate receptor-mediated feedback (neonatal mouse) modulate CPG frequency online.
- Sensory feedback is essential for adaptation, not rhythm generation: hip position signals regulate the stance-to-swing transition; load receptor signals (Golgi tendon organs, footpads) prevent premature flexion during stance; phase-dependent reflex reversals allow the same cutaneous stimulus to elicit either flexion (swing phase) or extension (stance phase).
- Vestibular stabilisation of body orientation operates via reticulospinal neurons that integrate vestibular input and set a bilateral activity equilibrium; asymmetric visual input (dorsal light response) shifts this equilibrium to stabilise a tilted body position.
- Cerebellum provides error-driven fine-tuning via climbing fibres; mossy fibre inputs (DSCT: limb state; VSCT/SRCP: efference copies of CPG flexor/extensor commands) enable rhythmic, step-cycle-locked modulation of vestibulo-, rubro-, and reticulospinal pathways; cerebellar learning (split-belt adaptation) depends on the paravermal anterior lobe and interpositus nucleus.
- Time-to-walking onset across all mammals correlates linearly with brain weight (log-log), suggesting locomotor maturation reflects brain assembly time rather than species-specific differences in circuit organisation.

---

### Computational framework

The paper draws on dynamical systems and network-level circuit theory rather than a single formal computational framework. The core formalisms are:

- **Recurrent excitatory network dynamics with burst-terminating mechanisms**: segmental CPG rhythm emerges from recurrent excitatory interneurons (E-neurons) whose bursting is terminated by Ca2+-activated K+ channels (KCa), Na+-activated K+ channels (KNa), and spike-frequency adaptation. Burst frequency is tunable by modulators (5-HT, dopamine, metabotropic glutamate receptors) acting on these intrinsic conductances.
- **Disinhibition logic**: basal ganglia output (SNr/GPi) is tonically inhibitory; behaviour selection is implemented as removal of inhibition from relevant motor centres, a winner-take-all mechanism mediated by striatal D1R vs. D2R pathway competition.
- **Unit burst generator (UBG) architecture**: each limb's CPG is proposed to consist of interacting unit generators controlling individual joint synergist groups; these can be recombined to produce different gaits and directions without requiring separate CPGs per gait.
- **Neuromechanical modelling**: large-scale simulations (up to 10,000 model neurons, 100 lamprey segments) replicate intersegmental phase coupling, forward/backward transitions, and actual swimming kinematics, providing quantitative validation of circuit hypotheses.
- **Sensory-CPG integration**: sensory entrainment is modelled as phase-resetting of the ongoing CPG oscillation by movement-related proprioceptive input; position-dependent reflex gating is framed as CPG state-dependent modulation of interneuronal transmission.

---

### Prevailing model of the system under study

The introduction and historical sections frame the field as having settled, by the 1970s–80s, on a hierarchical model with three functional levels: (1) a spinal CPG generating a basic locomotor rhythm, (2) brainstem command centres (MLR/DLR) that tonically drive CPG excitability and scale speed, and (3) forebrain structures providing goal-directed context. Within the spinal level, the dominant conceptual framework was the half-centre oscillator — two mutually inhibitory half-centres controlling flexors vs. extensors — supplemented by sensory reflex sculpting to explain the more complex four-phase pattern. The basal ganglia's role in locomotion was not appreciated in earlier frameworks; early accounts focused on cortex as the primary executive for voluntary movement, with CPGs viewed as relatively autonomous rhythm generators requiring only tonic drive from above. The interneuronal basis of CPG function was largely unknown as recently as the mid-1970s. Motoneurons were conceptualised as passive output elements. The modular, speed-specialised organisation of CPGs (multiple interacting unit generators) was not part of the prevailing view.

---

### What this paper contributes

This review synthesises three decades of findings to substantially update the prevailing model in the following ways:

1. **Basal ganglia as the central behaviour selector**: The disinhibition architecture of the basal ganglia — with tonically active SNr/GPi suppressing all motor centres and D1R/D2R pathway competition releasing specific programs — is now established as the primary mechanism for locomotion initiation and suppression, with optogenetic proof linking specific cell types to specific behavioural outcomes.
2. **MLR decomposition**: The monolithic MLR concept is resolved into cuneiform (escape/fast) and PPN glutamatergic (exploratory/slow) components, with the LPGi identified as the key relay to spinal CPGs.
3. **CPG cellular basis**: The interneuronal logic of vertebrate CPGs is now mapped at cellular resolution in lamprey, Xenopus, zebrafish, and partially in mouse, establishing that: rhythm arises from recurrent excitatory networks (not half-centres), alternation requires commissural inhibition, and these properties are distributed throughout the spinal cord.
4. **Modular speed control**: The zebrafish data demonstrate that CPGs are not single networks but modular assemblies of speed-specific microcircuits, each with distinct interneuron subtypes and synaptic properties — a conceptual advance beyond earlier UBG models.
5. **Motoneurons as CPG members**: Gap junction and ionotropic feedback from motoneurons to CPG interneurons establishes motoneurons as active participants in rhythm generation, contradicting the longstanding passive-output assumption.
6. **Key unresolved questions identified**: (a) The exact interneuronal identity of the rhythm generator in mouse (V2a, Shox2, Hb9, or others) remains unsettled, partly due to compensation effects in genetic ablation models. (b) Whether modular speed organisation found in zebrafish generalises to mammals. (c) The relative contribution of thalamic vs. cortical input to striatum for voluntary locomotion initiation. (d) The mechanisms of forward-backward locomotion switching. (e) Full circuit identification of postural control systems.

---

### Brain regions & systems

- **Striatum (dorsal and ventral)** — receives cortical, thalamic, and dopaminergic input; D1R direct-pathway neurons initiate locomotion via MLR disinhibition; D2R indirect-pathway neurons suppress locomotion.
- **SNr/GPi** — tonically active GABAergic output nuclei of basal ganglia; continuous inhibition of brainstem motor centres; removal of this inhibition = behaviour selection.
- **GPe / STN** — indirect pathway components; STN deep brain stimulation alleviates Parkinson's motor symptoms by an unclear mechanism.
- **SNc / VTA** — dopaminergic systems; SNc projects to dorsal striatum, VTA to nucleus accumbens; salient stimuli drive pre-locomotion dopamine bursts; SNc also projects directly to MLR with glutamate co-transmission.
- **Optic tectum / superior colliculus** — retinotopic map providing orienting and avoidance steering signals to reticulospinal neurons; also activates SNc dopamine neurons in response to salient visual stimuli.
- **MLR (cuneiform nucleus + PPN)** — mesencephalic locomotor region; cuneiform = fast/escape locomotion; PPN glutamatergic = slow/exploratory locomotion; PPN cholinergic = facilitation only.
- **DLR (zona incerta / ventral thalamus)** — diencephalic locomotor region; alternative/parallel command centre to MLR, possibly engaged preferentially by emotionally salient stimuli.
- **LPGi (lateral paragigantocellular nucleus)** — primary glutamatergic reticulospinal relay from MLR to spinal CPGs across full speed range; intermingled glycinergic neurons halt locomotion.
- **Raphe nuclei** — 5-HT descending modulation of spinal CPGs; fine-tunes burst stability via intrinsic conductances.
- **Locus coeruleus** — noradrenergic descending modulation; released by MLR activation; contributes to CPG excitability via alpha2/beta2 receptors.
- **Spinal cord (lumbar/lumbosacral for hindlimbs; cervical for forelimbs)** — contains the CPG interneurons responsible for generating and coordinating the locomotor motor pattern; distributed rhythmogenic capacity throughout.
- **Vestibular apparatus / Deiters nucleus** — detects head orientation; Deiters' monosynaptic excitation to extensor motoneurons; bilateral activity equilibrium controls body orientation during swimming; gated during locomotion.
- **Cerebellum (anterior lobe, paravermal)** — receives DSCT (limb state) and VSCT/SRCP (CPG efference copies) as mossy fibre inputs; climbing fibres (via spinoolivary tract) signal errors; output modulates vestibulo-, rubro-, and reticulospinal pathways in step-cycle synchrony; paravermal cortex + interpositus nucleus required for split-belt adaptation.
- **Motor cortex** — required for precision walking (accurate foot placement, obstacle avoidance) via corticospinal projections; not required for basic locomotion; same corticospinal neurons active during both precision walking and reaching.
- **Parietal cortex** — intermediary between visual input and motor cortex for visuomotor corrections during precision locomotion.
- **PAG (periaqueductal grey)** — mentioned in diagram context for fight/flight/freezing selection; receives basal ganglia output.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight in several subsystems:

**Spinal CPG rhythm generation (lamprey/Xenopus/zebrafish)**

- *Computational*: The spinal CPG must transform tonic excitatory drive from reticulospinal neurons into a rhythmic, bilaterally alternating, segmentally propagating motor pattern appropriate for propulsion.
- *Algorithmic*: Ipsilateral recurrent excitatory interneurons (E-neurons; V2a in zebrafish) generate bursts via NMDA/AMPA activation amplified by Ca2+-dependent and Na+-dependent K+ channel-mediated burst termination. Commissural glycinergic I-neurons couple the two sides into alternation. Intersegmental phase coupling emerges from the long rostrocaudal axonal extent of E- and I-neurons combined with a rostrocaudal excitability gradient. Modular speed control (zebrafish) arises from three anatomically distinct V2a modules with differential short-term synaptic plasticity (NMDA-dependent potentiation in slow module vs. convergence-dependent summation in fast module).
- *Implementational*: Specific cell types identified: V2a (Chx10+) excitatory interneurons (rhythm generation, necessary and sufficient); V0d inhibitory and V0v excitatory commissural interneurons (left-right coordination, speed-dependent); V1 inhibitory interneurons (burst termination, speed control); V2b inhibitory interneurons (flexor-extensor reciprocal inhibition); dI6/DMRT3 interneurons (gait flexibility); gap junctions between V2a interneurons and from motoneurons back to V2a (retrograde CPG modulation). Biophysical burst termination via KCa, KNa, and spike-frequency adaptation channels characterised.

**Basal ganglia disinhibition (lamprey + rodent)**

- *Computational*: Select which motor program to execute from among competing options (behaviour selection).
- *Algorithmic*: Disinhibition — tonically active SNr/GPi GABAergic neurons suppress all motor centres; striatal D1R neurons directly inhibit SNr/GPi releasing one motor centre; D2R neurons via GPe-STN enhance SNr/GPi inhibition of competing centres.
- *Implementational*: D1R vs. D2R striatal projection neurons defined by receptor expression, co-transmitters (substance P vs. enkephalin), and opposing Kir channel modulation by dopamine. MLR glutamatergic neurons identified as the disinhibited output target (optogenetic proof in mouse). This architecture is conserved to lamprey with identical molecular signatures.

**Bonus (implementational detail)**: The paper extensively documents cell-type-specific biophysical properties (Kir channels stabilising striatal neurons at rest; NMDA-mediated plateau potentials in reticulospinal neurons; Ca2+ channel subtypes mediating burst termination in CPG interneurons; gap junction mediation of motoneuron-to-CPG feedback), satisfying the implementational level with molecular and synaptic specificity.

---

### Limitations & open questions

- The identity of the rhythm-generating interneurons in the mouse spinal cord remains unresolved; genetic ablation experiments yield inconsistent results, possibly due to developmental compensation, and the neonatal in vitro preparation is not a fully mature locomotor system.
- The modular speed-specialised CPG organisation demonstrated in adult zebrafish has not yet been confirmed in mammals; the extent of homology is unknown.
- The relative weight of thalamic vs. cortical glutamatergic input to striatum for voluntary locomotion initiation in the intact behaving animal is unclear; the decorticate animal's preserved behaviour suggests thalamic input may suffice.
- The neural command for forward vs. backward locomotion switching, including which reticulospinal neurons provide the backward-locomotion command in mammals, is largely unknown.
- The circuits providing smooth transitions between standing and locomotion (muscle tone regulation integrated with CPG initiation) are incompletely characterised.
- Deep brain stimulation of STN alleviating Parkinson's symptoms is paradoxical within the canonical indirect-pathway model; the mechanism remains unclear.
- The neonatal rodent and larval zebrafish preparations, while extremely useful, represent immature circuit states — the adult four-phase locomotor pattern is not present — which may limit generalisability of interneuron-ablation conclusions.
- Biomechanical aspects and spinal cord injury regeneration are explicitly acknowledged as beyond the review's scope.

---

### Connections & keywords

**Key citations**:
- Graham Brown (1911) — half-centre hypothesis and dorsal root transection experiments
- Shik, Severin, Orlovskii (1966) — MLR discovery in decerebrate cat
- Grillner and Zangger — deafferentation preservation of complex motor pattern
- Roseberry et al. — optogenetic proof of D1R-striatum → MLR locomotion initiation
- Caggiano et al. and Josset et al. — cuneiform vs. PPN MLR decomposition
- Capelli et al. — LPGi as the primary reticulospinal relay
- Ampatzis, Song, El Manira — zebrafish modular CPG speed modules
- Garwicz et al. — brain weight vs. time-to-walking linear relationship
- Deliagina-Orlovski group — vestibular stabilisation circuits
- Arshavsky group — spinocerebellar tract physiology during locomotion
- Rossignol laboratory — spinal plasticity and split-belt locomotor adaptation

**Named models or frameworks**:
- Half-centre oscillator (Graham Brown)
- Unit burst generator (UBG) model (Grillner)
- Disinhibition model of basal ganglia (direct/indirect pathway)
- Neuromechanical lamprey simulation (Ekeberg, Grillner et al.)

**Brain regions**:
Striatum, SNr, GPi, GPe, STN, SNc, VTA, optic tectum/superior colliculus, MLR (cuneiform nucleus, PPN), DLR (zona incerta), LPGi, raphe nuclei, locus coeruleus, spinal cord (lumbar, cervical), vestibular nuclei/Deiters nucleus, cerebellum (anterior lobe, paravermal cortex, interpositus nucleus), motor cortex, parietal cortex, PAG

**Keywords**:
central pattern generators, vertebrate locomotion, basal ganglia disinhibition, mesencephalic locomotor region, reticulospinal neurons, spinal interneurons, V2a interneurons, modular CPG organization, sensory-CPG interaction, phase-dependent reflex reversal, spinocerebellar tract, comparative vertebrate neuroscience
