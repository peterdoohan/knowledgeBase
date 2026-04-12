---
source_file: drew2015_cortical_locomotion_control.md
paper_id: drew2015_cortical_locomotion_control
title: "Taking the next step: cortical contributions to the control of locomotion"
authors:
  - "Trevor Drew"
  - "Daniel S Marigold"
year: 2015
journal: "Current Opinion in Neurobiology"
paper_type: review
contribution_type: review
species:
  - human
methods:
  - fmri
  - lesion
brain_regions:
  - striatum
  - retrosplenial_cortex
keywords:
  - visually_guided_locomotion
  - posterior_parietal_cortex
  - motor_cortex
  - pyramidal_tract_neurons
  - muscle_synergies
  - state_estimation
  - motor_planning_vs_execution
  - obstacle_avoidance
  - egocentric_spatial_representation
  - working_memory_for_obstacle_properties
  - forelimb_hindlimb_coordination
  - corticospinal_control_of_gait
  - taking
  - next
  - step
  - cortical
  - contributions
  - control
  - locomotion
---

### One-line summary

The posterior parietal cortex (PPC) and motor cortex make dissociable contributions to visually guided locomotion: PPC supports motor planning via dynamic state estimation of body-object relationships, while motor cortex executes gait modifications by modulating muscle synergy patterns through pyramidal tract neurons.

---

### Background & motivation

Navigating complex environments requires both planning gait modifications and executing them precisely — a distinction that maps onto separable neural systems. Although the cortical control of discrete voluntary movements (reaching, grasping) is well characterised at the single-cell level, the cortical basis of locomotion has been far less studied. This review fills that gap by synthesising a body of single-unit recording, lesion, and human neuroimaging work on two cortical regions — PPC and motor cortex — during visually guided precision walking, primarily in cats stepping over obstacles.

---

### Methods

- **Scope**: Narrative review focused on PPC (area 5b) and motor cortex contributions to visually guided locomotion, principally in the cat model; human evidence reviewed where available.
- **Animal studies covered**: Single-unit recordings from behaving cats on treadmills with moving obstacles; lesion studies (unilateral PPC inactivation/ablation); transient visual occlusion paradigms; hindlimb working-memory tasks (obstacle straddling with delayed removal).
- **Human studies covered**: fMRI during imagined walking; high-density EEG during treadmill locomotion; TMS inactivation of motor cortex; corticospinal tract integrity and locomotor deficits in spinal cord injury; virtual reality walking with EEG.
- **Synthesis approach**: Narrative, organised around planning (PPC) versus execution (motor cortex) with a broader network perspective introduced in the final section.

---

### Key findings

- PPC (area 5b) neurons increase discharge 2–3 steps before an obstacle is stepped over, well in advance of the movement; this activity is largely limb-independent (72% of cells respond similarly whether the contralateral or ipsilateral limb leads).
- PPC discharge persists during brief visual occlusion, indicating it encodes a motor plan or state estimate rather than direct visual processing of obstacle features.
- PPC neurons also discharge between forelimb and hindlimb passage over an obstacle, with discharge duration scaling to the inter-limb interval; this supports flexible forelimb–hindlimb coordination.
- Unilateral PPC lesions produce errors in paw placement consistent with planning failure rather than perceptual or execution deficits; lesioned cats lose working memory for obstacle height within ~5 s (intact cats retain it for up to 10 min).
- Motor cortex neurons discharge primarily during the step over the obstacle (execution phase), and their activity modulates the phase and magnitude of muscle synergies rather than high-level endpoint parameters.
- Pyramidal tract neurons (PTNs) show phase and magnitude changes during gait modifications that mirror the Gaussian-shaped synergy activation profiles of synergistic muscle groups.
- TMS and coherence studies in humans confirm motor cortex drives leg muscles (24–40 Hz coupling in swing phase) and that motor cortex inactivation impairs locomotor adaptation.

---

### Computational framework

The paper invokes **state estimation** as the core computational framework for PPC function. Specifically, the PPC is proposed to compute a dynamic estimate of the relative position of the body and limbs with respect to objects in the environment — integrating visual input, proprioceptive/cutaneous feedback, efference copy, and temporal information (time-to-contact) — in order to plan paw placement and initiate gait modifications.

For motor cortex, the framework is **muscle synergy control**: the cortex is not computing endpoint kinematics directly, but instead modulating the phase and magnitude of a small set of Gaussian-shaped muscle synergy activations (indexed to the gait cycle). PTN populations are proposed to map onto synergy populations, giving flexible trajectory control through a compact parametric code.

Key variables:
- In PPC: body/limb state estimate, obstacle distance/time-to-contact, egocentric spatial representation.
- In motor cortex: phase offset and amplitude of muscle synergy Gaussians; PTN discharge patterns.

---

### Prevailing model of the system under study

The introduction signals that locomotion was predominantly viewed as a subcortically organised behaviour, with the spinal central pattern generator (CPG) providing rhythmicity and basic muscle patterning, and supraspinal (brainstem and cortical) structures modulating this baseline only during demanding or visually guided conditions. The literature on PPC and motor cortex contributions to locomotion was sparse compared to that on discrete voluntary movements; the field lacked single-cell-level accounts of how these cortical regions contribute specifically to gait planning versus execution. There was a broadly held view that motor cortex might control high-level parameters like limb endpoint trajectory rather than muscle-level detail, a view the Drew lab explicitly contests.

---

### What this paper contributes

This review establishes a clear functional dissociation:
- **PPC = planning**: provides a continuously updated, visually informed, limb-independent estimate of self-object spatial relationships, stored even in the absence of visual feedback, used to plan paw placement and coordinate forelimb–hindlimb sequencing.
- **Motor cortex = execution**: specifies muscle synergy modulation (phase and amplitude) required to produce the appropriate limb trajectory, acting via PTNs onto spinal CPG interneuronal networks.

This moves beyond the generic claim that "cortex is involved in gait" to assign specific computational roles at the planning/execution boundary. It also challenges endpoint-control accounts of motor cortex by providing evidence that PTN activity tracks muscle-level synergy parameters. The working-memory aspect of PPC (sustained discharge bridging forelimb and hindlimb events, sensitive to lesion) is a concrete new contribution not previously established for locomotion.

---

### Brain regions & systems

- **Posterior parietal cortex (PPC), area 5b** — motor planning; dynamic state estimation of body-limb position relative to obstacles; working memory for obstacle properties; forelimb–hindlimb coordination.
- **Motor cortex (M1), primarily layer V PTNs** — execution of gait modifications; modulation of muscle synergy phase and magnitude via corticospinal tract onto spinal CPGs.
- **Spinal CPG** — provides baseline rhythmicity and muscle patterning; receives PTN modulation through spinal interneuronal networks.
- **Premotor cortex** — identified as part of the broader planning network; contribution to locomotion noted as poorly understood.
- **Basal ganglia** — embedded in the motor planning/execution network (Figure 4); contribution to locomotion described as understudied.
- **Cerebellum** — provides state estimation inputs and locomotor adaptation; limited information available.
- **Retrosplenial cortex and entorhinal/hippocampal system** — involved in translating between allocentric and egocentric reference frames; feed into PPC.
- **Somatosensory cortex** — provides proprioceptive/cutaneous feedback to both PPC and motor cortex.
- **Visual extrastriate areas** — provide object attribute information to PPC.

---

### Mechanistic insight

The paper partially meets the bar. It proposes an algorithm (state-estimation-driven planning in PPC; synergy-phase modulation in motor cortex) and supports it with neural recording and lesion data. However, it is a review, so the mechanistic claims are assembled from multiple studies rather than a single integrated experiment.

**Computational (what problem is the brain solving):**
- PPC: estimate the current and future state of the body relative to environmental objects, to determine when and how to modify gait.
- Motor cortex: translate the planned gait modification into the specific muscle activation pattern (synergy phase/amplitude code) needed to achieve the desired trajectory.

**Algorithmic (representations and processes):**
- PPC computes a limb-independent, visually and proprioceptively informed state estimate that persists across visual occlusion and is retained in working memory; cell discharge encodes time-to-contact/distance with the obstacle.
- Motor cortex PTN populations each modulate a muscle synergy, characterised by a Gaussian activation profile (phase, amplitude) over the gait cycle; stepping over obstacles is achieved by shifting these Gaussians.

**Implementational (neural hardware):**
- PPC area 5b (cat lateral ansate sulcus); lesions specifically impair planning, not perception.
- Layer V PTNs projecting via corticospinal/pyramidal tract; activity modulated relative to specific muscle synergy onsets.
- PTNs act through spinal CPG interneuronal networks, integrating cortical commands into the locomotor rhythm.

**Bonus**: The cell-type resolution (PTNs vs. other layer V neurons) and the CPG interneuron pathway provide partial implementational grounding, though the specific interneuron classes are not identified.

---

### Limitations & open questions

- The vast majority of single-unit data comes from cat; the extent to which findings generalise to primates (including humans) is inferred largely from imaging and TMS, which lack the spatial and temporal resolution of single-unit recording.
- The contributions of premotor cortex and basal ganglia to visually guided locomotion remain poorly characterised at the single-cell level.
- The exact computational role of the early PPC discharge (motor plan vs. state estimate vs. sensory prediction) is not fully resolved; the review acknowledges the limb-independence could reflect either a high-level motor intention signal or an object-centred spatial signal.
- The specific spinal interneuron populations through which PTNs implement synergy modulation are not identified.
- Whether PPC working memory for obstacle properties involves the same mechanisms as standard prefrontal working memory is unaddressed.
- Human studies remain limited by indirect methods (EEG spectral power, TMS) that cannot resolve single-cell firing patterns or reliably target specific cortical layers.

---

### Connections & keywords

**Key citations:**
- Beloozerova & Sirota (2003) — PPC area 5 during cat locomotion
- Andujar, Lajoie & Drew (2010) — limb-independent PPC cells
- Lajoie & Drew (2007) — PPC lesion effects on paw placement
- Marigold & Drew (2011) — PPC during visual occlusion
- McVea & Pearson (2006); McVea, Taylor & Pearson (2009) — long-lasting obstacle working memory and PPC lesion
- Krouchev & Drew (2013) — muscle synergies and PTN control framework
- Krouchev, Kalaska & Drew (2006) — synergy identification in cat locomotion
- Petersen et al. (2012) — motor cortex drives leg muscles in humans (corticomuscular coherence)

**Named models or frameworks:**
- Muscle synergy framework (Gaussian synergy representation)
- State estimation / forward model (Shadmehr & Krakauer, 2008; Mulliken et al., 2008)
- Central pattern generator (CPG) for locomotion

**Brain regions:**
- Posterior parietal cortex (area 5b)
- Motor cortex / M1
- Pyramidal tract / corticospinal tract
- Spinal CPG interneurons
- Premotor cortex
- Basal ganglia
- Cerebellum
- Retrosplenial cortex
- Entorhinal cortex / hippocampus
- Visual extrastriate areas

**Keywords:**
- visually guided locomotion
- posterior parietal cortex
- motor cortex
- pyramidal tract neurons
- muscle synergies
- state estimation
- motor planning vs. execution
- obstacle avoidance
- egocentric spatial representation
- working memory for obstacle properties
- forelimb-hindlimb coordination
- corticospinal control of gait
