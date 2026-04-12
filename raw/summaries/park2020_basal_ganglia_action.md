---
source_file: park2020_basal_ganglia_action.md
paper_id: park2020_basal_ganglia_action
title: "Basal Ganglia Circuits for Action Specification"
authors:
  - "Junchol Park"
  - "Luke T. Coddington"
  - "Joshua T. Dudman"
year: 2020
journal: "Annual Review of Neuroscience"
paper_type: review
contribution_type: review
species:
  - monkey
methods:
  - calcium_imaging
  - optogenetics
  - electrophysiology
  - computational_modeling
  - lesion
brain_regions:
  - striatum
  - ventral_striatum
  - ventral_tegmental_area
  - substantia_nigra
  - thalamus
frameworks:
  - reinforcement_learning
keywords:
  - basal_ganglia
  - dopamine
  - reinforcement_learning
  - motor_control
  - action_selection
  - action_specification
  - gain_modulation
  - movement_vigor
  - movement_kinematics
  - superior_colliculus
  - striatum
  - direct_pathway
  - indirect_pathway
  - medium_spiny_neurons
  - thalamocortical_circuits
  - motor_thalamus
  - feedforward_inhibition
  - continuous_control
  - movement_execution
  - basal
wiki_pages:
  - wiki/topics/successor_representation_in_striatal_and_dopaminergic_reinforcement_learning
---

### One-line summary

The basal ganglia provide continuous, action-specific gain modulation of movement kinematics (vigor/speed) through feedforward inhibition of premotor structures, rather than acting as a categorical action selection switch.

### Background & motivation

Traditional models of basal ganglia (BG) function have emphasized categorical action selection—deciding which action to initiate. However, this review argues that BG are primarily involved in the continuous specification of movement parameters (particularly speed/vigor) during action execution. The authors synthesize evidence from physiological recordings, perturbation studies, and circuit anatomy to propose that BG act like a "graphic equalizer"—providing selective, continuous gain modulation of distinct action channels rather than binary selection.

### Methods

This is a comprehensive review article that synthesizes:
- Historical physiological studies (single-unit recordings in behaving monkeys and rodents)
- Modern large-scale imaging and electrophysiology (calcium imaging, fiber photometry, multi-electrode recordings)
- Cell-type-specific studies (dMSN vs iMSN recordings, FSI interneuron studies)
- Perturbation experiments (optogenetics, chemogenetics, lesions, inactivations)
- Circuit tracing and anatomical studies
- Computational modeling literature

### Key findings

- **Continuous encoding of kinematics**: BG neurons encode continuous movement parameters (speed, amplitude, velocity) during action execution, not just action initiation or selection.

- **Action-specific ensembles**: Distinct populations of striatal neurons are active during different actions (e.g., joystick movement vs. licking), with orthogonal population dynamics for different actions.

- **Gain modulation framework**: The ratio of dMSN to iMSN activity correlates with movement speed; this opponent pathway activity provides continuous gain control over movement vigor.

- **Inhibition for gain control, not competition**: Local inhibitory microcircuits in BG (collateral inhibition between MSNs, FSI-mediated feedforward inhibition) implement divisive gain control rather than winner-take-all selection.

- **Feedforward control of premotor areas**: BG output (via SNr/GPi) provides continuous inhibitory modulation of premotor structures (superior colliculus, brainstem), with BG-recipient thalamus primarily driven by cortical input rather than gated by BG.

- **Integration with other motor pathways**: BG and cerebellar output converge on common targets (motor thalamus, SC), with BG regulating open-loop movement vigor and cerebellum regulating closed-loop accuracy.

### Computational framework

The paper employs **gain modulation** as the central computational framework. Gain modulation refers to multiplicative scaling of neural responses that preserves selectivity while changing response magnitude. Key aspects:

- **Multiplicative control**: BG output scales the gain of premotor activity (e.g., SC firing rate determines saccade velocity) without changing the spatial pattern of activity.

- **Opponent process**: The difference between dMSN and iMSN activity (D-I balance) provides a signed signal for bidirectional control of movement velocity.

- **Divisive normalization**: Inhibitory microcircuits in BG output nuclei (SNr) implement divisive gain control through feedback inhibition.

- **Reinforcement learning connection**: The framework suggests how value signals (dopamine) could modulate vigor via gain control rather than just action selection.

### Prevailing model of the system under study

The prevailing model before this review conceptualized BG as an action selection circuit—a "switchboard" that decides which action to initiate (Mink 1996, Redgrave et al. 2010). This model emphasized:
- Categorical selection of discrete actions
- Initiation deficits as primary in Parkinson's disease
- Disinhibition as the mechanism for action release
- Competition between actions via lateral inhibition in striatum

The authors note this view emerged from early lesion studies showing initiation deficits, but argue it was reinforced by reinforcement learning models and focus on dopamine reward signals, shifting attention away from movement execution kinematics.

### What this paper contributes

This review reframes BG function from action selection to **continuous action specification**:

- **Kinematics over initiation**: BG primarily regulate movement vigor/speed during execution, not just action initiation. This is supported by: (a) most BG neurons modulate during movement execution, (b) perturbations affect kinematics without preventing initiation, (c) Parkinson's disease shows continuous slowing not just initiation failure.

- **Gain modulation mechanism**: The dMSN/iMSN opponent circuitry provides continuous gain control, not binary selection. The ratio of pathway activity predicts movement speed bidirectionally.

- **Anatomical integration**: BG output targets premotor areas (SC, brainstem) where it modulates gain of descending commands. BG-recipient thalamus is cortically driven, not gated by BG.

- **Complementary roles**: BG and cerebellum have distinct but complementary roles—BG regulate open-loop vigor, cerebellum regulates closed-loop accuracy.

- **Computational implications**: Reinforcement learning models of BG need to incorporate continuous vigor control, not just discrete action selection.

### Brain regions & systems

- **Striatum** — Primary BG input structure; contains dMSNs and iMSNs that show action-specific encoding of movement kinematics; source of continuous gain modulation signals
- **Globus pallidus externus (GPe)** — Part of indirect pathway; receives iMSN input
- **Subthalamic nucleus (STN)** — Part of indirect pathway; receives cortical input
- **Substantia nigra pars reticulata (SNr)** — Major BG output nucleus; provides inhibitory feedforward control of superior colliculus and other premotor areas; implements divisive gain control via local collateral inhibition
- **Internal globus pallidus (GPi)** — BG output nucleus (primates); functionally equivalent to SNr
- **Substantia nigra pars compacta (SNc)** — Source of dopaminergic input to striatum; modulates plasticity and vigor
- **Ventral tegmental area (VTA)** — Source of dopaminergic input to ventral striatum
- **Superior colliculus (SC)** — Midbrain premotor area; major target of BG output; BG modulation of SC firing rate controls saccade/limb movement velocity
- **Motor thalamus** — Receives BG output; provides feedback to motor cortex; primarily driven by cortical input rather than gated by BG
- **Cerebellum** — Complementary motor structure; provides excitatory input to same premotor targets as BG; regulates closed-loop accuracy vs. BG's open-loop vigor
- **Motor cortex** — Source of corticostriatal and corticofugal inputs to BG and premotor areas

### Mechanistic insight

This paper meets the mechanistic insight bar by providing a circuit-level account of how BG compute continuous movement specification, grounded in both anatomical and physiological evidence.

**Computational level**: The brain must solve the problem of continuously specifying movement parameters (speed, vigor) across diverse actions to achieve stable, goal-directed behavior. This requires action-specific gain modulation rather than generalized arousal.

**Algorithmic level**: The BG implement gain modulation through:
- Opponent pathway computation: The ratio of dMSN to iMSN activity provides a signed signal for bidirectional control of movement velocity
- Divisive gain control: Local inhibitory microcircuits in SNr implement feedback gain control via collateral inhibition between projection neurons
- Action-specific ensembles: Distinct striatal populations encode different actions with orthogonal dynamics, allowing independent gain control

**Implementational level**: The circuitry is implemented through:
- Feedforward inhibition: BG output nuclei (SNr/GPi) provide continuous inhibitory modulation of premotor structures (SC, brainstem)
- Lack of recurrent excitation: Unlike cortex, BG circuits lack recurrent excitation, making them ideal for gain modulation without unwanted dynamics
- Dopaminergic modulation: SNc/VTA dopamine modulates striatal plasticity and gain, linking reinforcement signals to vigor control

The paper also notes that the SC provides an ideal model system for understanding BG-premotor integration, with BG inhibition modulating SC firing rate to control movement velocity, while cerebellar excitation converges on the same target to regulate accuracy.

### Limitations & open questions

The authors explicitly identify several unresolved questions:

1. **Topography of BG output integration**: How does the topography of BG output relate to the topography of other descending pathways (e.g., corticofugal projections)? Understanding this requires synapse-level resolution mapping at mesoscale—a daunting technical challenge.

2. **Sufficiency of rate models**: Whether rate models describing average modulation of output are sufficient, or whether spike-timing codes are critical. Evidence suggests BG output may play critical roles in modulating precise timing of activity, which requires deeper appreciation of spike timing in premotor areas and thalamus.

3. **Incorporating continuous specification into RL models**: Reinforcement learning algorithms that have largely described behavior at the level of action selection need to incorporate the critical role for continuous specification of movement execution. Some progress exists but much work remains.

4. **Integration with cerebellar circuits**: The detailed mechanisms by which BG and cerebellar outputs converge and interact at shared targets (motor thalamus, SC) remain to be fully characterized.

### Connections & keywords

**Key citations**:
- Mink (1996) — previous selection-focused model of BG function
- DeLong et al. (1984) — early physiological work suggesting execution rather than initiation role
- Dudman & Krakauer (2016) — previous work on vigor control by BG
- Yttri & Dudman (2016) — opponent control of movement velocity
- Kornhuber (1971) — early proposal of BG as "ramp generator" for continuous control
- Hikosaka & Wurtz (1980s) — seminal work on SNr-SC interactions
- Salinas & Thier (2000) — gain modulation as computational principle

**Named models or frameworks**:
- Graphic equalizer model of BG function
- Opponent actor learning (OpAL) framework
- Reinforcement learning models of BG
- Action selection vs. action specification models
- Marr's three levels of analysis (referenced implicitly)

**Brain regions**:
- Striatum (dorsomedial, dorsolateral)
- Globus pallidus externus (GPe) and internus (GPi)
- Subthalamic nucleus (STN)
- Substantia nigra pars reticulata (SNr) and pars compacta (SNc)
- Ventral tegmental area (VTA)
- Superior colliculus (SC)
- Motor thalamus (ventroanterior, ventromedial, ventrolateral, intralaminar)
- Cerebellum
- Motor cortex

**Keywords**:
basal ganglia, dopamine, reinforcement learning, motor control, action selection, action specification, gain modulation, movement vigor, movement kinematics, superior colliculus, striatum, direct pathway, indirect pathway, medium spiny neurons, thalamocortical circuits, motor thalamus, feedforward inhibition, continuous control, movement execution

### Related wiki pages
- [[wiki/topics/successor_representation_in_striatal_and_dopaminergic_reinforcement_learning|Successor representation in striatal and dopaminergic reinforcement learning]]
