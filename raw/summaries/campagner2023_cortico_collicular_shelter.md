---
source_file: campagner2023_cortico_collicular_shelter.md
paper_id: campagner2023_cortico_collicular_shelter
title: "A cortico-collicular circuit for orienting to shelter during escape"
authors:
  - "Dario Campagner"
  - "Ruben Vale"
  - "Yu Lin Tan"
  - "Panagiota Iordanidou"
  - "Oriol Pavón Arocas"
  - "Federico Claudi"
  - "A. Vanessa Stempel"
  - "Sepiedeh Keshavarzi"
  - "Rasmus S. Petersen"
  - "Troy W. Margrie"
  - "Tiago Branco"
year: 2023
journal: Nature
paper_type: empirical
contribution_type: empirical
species:
  - mouse
tasks:
  - navigation_task
methods:
  - optogenetics
  - neuropixels
  - computational_modeling
brain_regions:
  - anterior_cingulate_cortex
  - retrosplenial_cortex
frameworks:
  - attractor_networks
keywords:
  - egocentric_shelter_direction_encoding
  - cortico_collicular_circuit
  - escape_behaviour
  - memory_guided_orienting
  - feedforward_lateral_inhibition
  - superior_colliculus_cell_types_vglut2
  - vgat
  - retrosplenial_cortex_spatial_coding
  - defensive_navigation
  - goal_direction_vector
  - chemogenetic_projection_specific_inactivation
  - opto_tagging
  - spiking_ring_attractor_network
  - cortico
  - collicular
  - circuit
  - orienting
  - shelter
  - during
  - escape
---

### One-line summary

The mouse retrosplenial cortex (RSP) and superior colliculus (SC) form a feedforward lateral inhibition circuit that encodes egocentric shelter direction and is specifically required for accurate orienting to shelter during escape, but not for general spatial navigation or sensory-guided orientation.

---

### Background & motivation

When threatened, mice execute rapid, accurate shelter-directed escapes that rely on memory of the shelter's spatial location rather than live sensory cues. Prior work had identified neural mechanisms for escape initiation, but it was unknown how the escape circuit accesses spatial information to orient toward shelter along the most efficient route. The retrosplenial cortex (RSP) was a plausible hub given its established roles in encoding head direction, goal locations, and spatial features; the superior colliculus (SC) was implicated in escape initiation and orienting motor commands and receives input from the RSP. This paper addresses the gap by asking how these two regions jointly compute and transmit shelter-direction information to guide action.

---

### Methods

- **Subjects**: Adult male C57BL/6J mice; additional transgenic lines (VGluT2-ires-cre, VGAT-cre) for cell-type-specific experiments.
- **Behavioural paradigm**: Circular arena with a shelter; innately threatening auditory upsweep (17–20 kHz) elicited shelter-directed escapes. Shelter position was rotated between sessions to dissociate shelter encoding from allocentric landmarks. Controls included a second closed shelter and a bright LED landmark to assess behavioural selectivity.
- **Neural recordings**: Simultaneous silicon-probe (Neuropixels) single-unit recordings in RSP and SC during free exploration (836 RSP units, 683 SC units; 4 mice). Cell-type identification via opto-tagging of vGluT2+ and vGAT+ SC neurons.
- **Circuit inactivation**: Projection-specific chemogenetic silencing (hM4Di DREADD via retrograde AAV strategy) of SC-projecting RSP neurons, both systemically (CNO i.p.) and locally (cannula infusion over SC or ACC). Global RSP inactivation via chemogenetics and muscimol. Controls: posterior parietal cortex (PPC) and anterior motor areas (AMA) inactivated as comparison.
- **Anatomy**: Monosynaptic retrograde rabies tracing from vGluT2+ or vGAT+ SC starter cells to quantify convergence of RSP input onto excitatory vs. inhibitory SC populations.
- **Circuit physiology**: In vivo dual-opsin opto-tagging during RSP axon stimulation (20 Hz ChrimsonR); in vitro whole-cell recordings (ChR2 optogenetic stimulation of RSP axons onto identified SC cell types) to measure synaptic summation. Anterograde transsynaptic dual-opsin strategy to confirm feedforward lateral inhibition motif.
- **Computational model**: Conductance-based leaky integrate-and-fire spiking network model of RSP ring → vGluT2+/vGAT+ SC populations, constrained by anatomical and electrophysiological data; compared against a standard ring attractor model.
- **Specificity controls**: Sound-orienting assay (SC-dependent sensory orienting); goal-directed food-seeking navigation task (lick port reached via a slow, curved trajectory).
- **Analysis**: Generalized linear models for firing rate decomposition; linear discriminant analysis (LDA) population decoder for shelter direction; Rayleigh vector statistics for tuning breadth.

---

### Key findings

- A subset of RSP neurons (3.5%) and SC neurons (up to 9.2%) are tuned to egocentric shelter direction (head–shelter angle); firing fields rotated with shelter location (RSP median rotation = 113°, SC = 99°) and were independent of allocentric head direction.
- SC neurons were preferentially tuned to the behaviourally relevant open shelter vs. the closed shelter or LED; RSP was less discriminating (equal fractions tuned to open and closed shelters), suggesting the SC acts as a salience filter on RSP-encoded locations.
- Removing shelter-direction from a GLM dropped firing rate prediction accuracy by ~30% (RSP: −24 ± 3.67%, SC: −31 ± 3.6%); LDA population decoding accuracy: SC = 0.73, RSP = 0.83 (chance = 0.19).
- Chemogenetic silencing of SC-projecting RSP neurons reduced SC shelter-direction neuron fraction by 33% (P = 0.01) and SC population decoding accuracy by a median of 18.76%, confirming RSP drives SC shelter-direction tuning.
- Behavioural inactivation: systemic CNO increased escape orientation error (CNO median = 23°, saline = 5°; P = 0.0153); flight termination outside shelter was 7.4× more likely; time to shelter increased 50%. Local infusion of CNO over SC (targeting RSP terminals) replicated the error; infusion over ACC did not. PPC and AMA inactivation had no effect.
- Escape orientation errors did not generalise: RSP–SC inactivation left sound-orienting accuracy intact (P = 0.929), did not affect exploration navigation, and did not impair slow goal-directed navigation to a food lick port.
- Anatomically, inhibitory SC cells received 1.8× more convergent RSP input than excitatory cells (convergence index: vGAT+ = 0.83, vGluT2+ = 0.47; P = 0.035). RSP convergence onto SC was higher overall than AMA or PPC.
- In vitro, temporal summation of RSP synaptic input was significantly greater in vGAT+ than vGluT2+ SC neurons (fifth-pulse peak voltage: 154% vs. 79%; P = 2.53 × 10−4), due to intrinsic excitability differences and short-term plasticity.
- In vivo, 20 Hz RSP axon stimulation initially excited both SC populations, but over ~100 ms vGluT2+ firing fell below baseline while vGAT+ firing increased progressively — consistent with feedforward lateral inhibition.
- 26.3% of excitatory SC neurons received both monosynaptic RSP input and direct inhibition from RSP-recipient vGAT+ SC interneurons, directly demonstrating the feedforward lateral inhibition motif.
- Spiking network model with feedforward lateral inhibition fit the in vivo dynamics significantly better than a standard ring attractor model (sum of squared errors: 1.68 vs. 4.19; P = 8.97 × 10−40). The model predicted sharper tuning in vGluT2+ than vGAT+ SC neurons, confirmed experimentally (Rayleigh vector: vGAT+ = 0.09, vGluT2+ = 0.22; P = 0.0054).

---

### Computational framework

The paper uses a **spiking ring-attractor network with feedforward lateral inhibition** as its computational framework.

- **What is modelled**: Transfer and sharpening of a circular variable (egocentric shelter direction) from RSP to SC.
- **Key variables**: RSP ring network (neurons organised by shelter-direction preference); vGluT2+ SC excitatory neurons (inherit RSP tuning); vGAT+ SC inhibitory neurons (broad tuning from pooled RSP input); connectivity kernels (diagonal RSP→vGluT2+, inverted-diagonal RSP→vGAT+); local recurrent excitation and lateral inhibition within SC.
- **Core assumption**: RSP generates a continuous egocentric representation of shelter direction; the RSP–SC synapse exploits differential convergence and synaptic integration efficiency in inhibitory vs. excitatory SC neurons to implement a feedforward lateral inhibition computation that sharpens excitatory SC tuning while broadly activating the inhibitory network.
- The framework is biologically constrained: network parameters were fit to empirically measured in vivo and in vitro dynamics.

---

### Prevailing model of the system under study

Prior to this paper, the prevailing understanding was that escape initiation involves the medial SC responding to threatening stimuli, while spatial navigation to goals depends on hippocampal and entorhinal systems encoding allocentric space (place cells, grid cells, head-direction cells). The RSP was understood as a hub that encodes head direction, angular velocity, and spatial landmarks, and integrates multiple streams of spatial information, but its role in immediate defensive behaviour was not established. The SC was known to generate orienting motor commands and escape initiation signals, and to receive projections from the RSP, but the functional significance of the RSP→SC pathway was uncharacterised in the context of goal-directed escape. How memory of shelter location is translated into rapid, accurate orienting actions — specifically how the escape circuit accesses memorised spatial goals and converts them into egocentric motor commands — was an open question.

---

### What this paper contributes

This paper establishes that the RSP and SC jointly and continuously encode the egocentric shelter-direction vector, and that the RSP–SC projection is causally required for accurate shelter orientation specifically during escape (or other time-critical navigation), not for general navigation or sensory-guided orienting. This distinguishes a dedicated memory-guided escape orientation circuit from both the general SC orienting system and from hippocampal-dependent spatial navigation.

At the mechanistic level, the paper moves beyond showing that a pathway is necessary to characterising the circuit architecture that implements the information transfer: a feedforward lateral inhibition motif in which differential RSP convergence and synaptic integration efficiency drive the inhibitory SC network more strongly than the excitatory one, producing a clean mapping of shelter direction with sharpened excitatory tuning. The biologically constrained spiking model provides a quantitative account of these dynamics and outperforms alternative ring-attractor models.

The finding that SC neurons specifically encode the most behaviourally relevant shelter (open > closed > LED) — while RSP encodes multiple familiar locations — suggests a division of labour in which the RSP forms a general egocentric map of salient locations and the SC selects the most escape-relevant target.

---

### Brain regions & systems

- **Retrosplenial cortex (RSP)** — continuously encodes egocentric shelter direction during exploration; all three subdivisions (RSPv, RSPd, RSPa) project to SC; proposed source of the shelter-direction signal relayed to SC; encodes a broader set of familiar locations (both open and closed shelters); loss of function disrupts escape orientation.
- **Superior colliculus (SC), centromedial and centrolateral** — receives and inherits RSP shelter-direction signal; preferentially encodes the most behaviourally salient escape target (open shelter > closed shelter); contains excitatory (vGluT2+) and inhibitory (vGAT+) shelter-direction neurons with sharp and broad tuning, respectively; generates orienting motor commands; proposed locus where RSP-derived spatial goal representation is made accessible to the motor system.
- **Posterior parietal cortex (PPC) and anterior motor areas (AMA)** — also project to SC; inactivation does not affect escape orientation, establishing that the RSP–SC pathway is uniquely required.
- **Anterior cingulate cortex (ACC)** — receives collateral projections from SC-projecting RSP neurons; local inactivation of RSP terminals in ACC does not impair escape, confirming specificity to RSP–SC synapses.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Criterion 1 (algorithm)**: The paper formalises a feedforward lateral inhibition circuit algorithm in which RSP neurons encoding a particular shelter direction activate SC inhibitory neurons with inverted-diagonal connectivity, which then silence excitatory SC neurons tuned to other directions. This sharpens SC excitatory tuning and generates a clean directional map. The algorithm is instantiated in a conductance-based spiking network model.

**Criterion 2 (neural data supporting the algorithm)**: In vivo recordings, in vitro physiology, anatomical tracing, and optogenetic circuit dissection all converge on the same algorithm. Specifically: (a) in vivo dual-opsin experiments show the divergent firing dynamics of vGluT2+ and vGAT+ SC populations during RSP stimulation, (b) in vitro whole-cell recordings quantify the differential synaptic summation underlying this divergence, (c) rabies tracing quantifies the anatomical convergence bias, (d) transsynaptic dual-opsin experiments directly demonstrate that RSP-recipient vGAT+ SC neurons inhibit vGluT2+ SC neurons that also receive RSP input, and (e) tuning breadth of opto-tagged vGAT+ vs. vGluT2+ shelter-direction neurons in freely behaving mice matches the model prediction.

**Marr's three levels:**

- **Computational**: The brain must rapidly orient the body toward a memorised safe location when threatened, minimising time to shelter and exposure to the predator. The computation is to continuously represent the egocentric direction to shelter and make this immediately available to the motor system.
- **Algorithmic**: RSP neurons organised in a ring by shelter-direction preference project with diagonal connectivity to excitatory SC neurons (direct tuning transfer) and with inverted-diagonal connectivity to inhibitory SC neurons (which pool across RSP tuning preferences). The inhibitory SC neurons suppress excitatory SC neurons at orthogonal shelter directions, sharpening the population response. The result is a clean egocentric shelter-direction map in excitatory SC neurons.
- **Implementational**: The asymmetry in RSP convergence onto vGAT+ vs. vGluT2+ SC neurons (1.8× greater onto inhibitory cells) and the greater temporal summation efficiency in vGAT+ neurons (due to intrinsic excitability and short-term plasticity differences) are the identified biophysical mechanisms that bias the circuit toward stronger inhibitory drive. Cell types are molecularly defined (vGluT2+ excitatory, vGAT+ inhibitory), monosynaptic connectivity is confirmed by rabies tracing, and feedforward lateral inhibition is confirmed by transsynaptic circuit mapping and patch-clamp electrophysiology.

**Bonus**: The implementational level is addressed in detail — specific cell types (vGluT2+ vs. vGAT+ SC neurons), convergence of a specific cortical projection (RSP layer 5), and synaptic biophysics (short-term plasticity, intrinsic excitability) are all characterised.

---

### Limitations & open questions

- The chemogenetic inactivation approach (systemic CNO) may have off-target effects through collateral projections of SC-projecting RSP neurons beyond the SC, although local SC cannula experiments partially address this.
- It remains unclear how the escape circuit integrates threat detection (medial SC) with the shelter-orientation signal (RSP–SC pathway) to initiate directed flight; future work is needed on the interface between these systems.
- The food-seeking navigation task control used a slow, curved trajectory, leaving open whether the RSP–SC pathway is specifically for escape or more broadly for any time-critical goal-directed navigation.
- The model is constrained by measured circuit properties but the ring-attractor organisation of RSP and its connectivity kernels onto SC cell types are inferred from the model fit rather than directly verified anatomically.
- How shelter-direction information is initially computed in the RSP, and how RSP integrates self-motion and spatial memory signals to maintain a continuously updated egocentric shelter vector, is not addressed.
- Experiments used male mice only; sex differences in escape behaviour or circuit organisation are unknown.

---

### Connections & keywords

**Key citations**:
- Vale et al. (2017) *Curr. Biol.* — shelter-directed escape and spatial memory in mice (foundational behavioural work)
- Evans et al. (2018) *Nature* — synaptic threshold mechanism for escape decisions in SC
- Mitchell et al. (2018) *Brain Neurosci. Adv.* — RSP role in spatial cognition
- Sarel et al. (2017) *Science* — goal-vector cells in bat hippocampus
- Laurens & Angelaki (2018) *Neuron* — ring attractor and head direction
- Basso & May (2017) *Annu. Rev. Vis. Sci.* — SC circuits for action and cognition
- Keshavarzi et al. (2022) *Neuron* — multisensory coding of angular head velocity in RSP
- Zingg et al. (2017) *Neuron* — AAV anterograde transsynaptic tagging for defence behaviour circuits

**Named models or frameworks**:
- Feedforward lateral inhibition model (this paper)
- Ring attractor model (comparison model; Ben-Yishai et al. 1995; Zhang 1996)
- Spiking network model (conductance-based leaky integrate-and-fire)

**Brain regions**:
- Retrosplenial cortex (RSP)
- Superior colliculus (SC)
- Posterior parietal cortex (PPC)
- Anterior motor areas (AMA)
- Anterior cingulate cortex (ACC)
- Medial superior colliculus

**Keywords**:
- Egocentric shelter direction encoding
- Cortico-collicular circuit
- Escape behaviour
- Memory-guided orienting
- Feedforward lateral inhibition
- Superior colliculus cell types (vGluT2+, vGAT+)
- Retrosplenial cortex spatial coding
- Defensive navigation
- Goal-direction vector
- Chemogenetic projection-specific inactivation
- Opto-tagging
- Spiking ring-attractor network
