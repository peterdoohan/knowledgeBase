---
source_file: deska_gauthier2019_spinal_interneurons_locomotor.md
paper_id: deska_gauthier2019_spinal_interneurons_locomotor
title: "The functional diversity of spinal interneurons and locomotor control"
authors:
  - "Dylan Deska-Gauthier"
  - "Ying Zhang"
year: 2019
journal: "Current Opinion in Physiology"
paper_type: review
contribution_type: review
species:
  - mouse
methods:
  - optogenetics
  - electrophysiology
  - computational_modeling
keywords:
  - spinal_interneuron_diversity
  - central_pattern_generator
  - locomotor_rhythm_generation
  - locomotor_pattern_formation
  - speed_dependent_gait_transitions
  - cardinal_interneuron_classes
  - v0_v1_v2a_v2b_v3_di6_interneurons
  - flexorextensor_alternation
  - leftright_coordination
  - motor_neuron_gain_control
  - recurrent_spinal_feedback_circuits
  - fictive_locomotion
  - functional
  - diversity
  - spinal
  - interneurons
  - locomotor
  - control
---

### One-line summary

Molecularly distinct spinal interneuron subpopulations assemble into hierarchically organised rhythm-generating and pattern-forming circuit modules that collectively produce the full repertoire of vertebrate locomotor behaviours.

---

### Background & motivation

Locomotion requires precise spatiotemporal coordination of muscle contractions mediated by spinal interneuron (IN) circuits. The spinal central pattern generator (CPG) can produce basic rhythmic and patterned motor outputs in the absence of supraspinal or sensory input, but the cellular and circuit basis of this capacity remained unclear. Genetic tools enabling the identification of molecularly distinct IN populations have enabled systematic functional dissection of CPG architecture. A key gap this review addresses is the newly appreciated heterogeneity within each cardinal IN class — subpopulations with distinct molecular, anatomical, and physiological profiles that underlie task-specific locomotor functions not ascribable to the cardinal class as a whole.

---

### Methods

- Scope: select recent studies (primarily mouse and zebrafish, with reference to horses) investigating ventral spinal IN subpopulations within rhythm-generating and pattern-forming circuit layers.
- Literature covered: genetic deletion/silencing experiments, fictive locomotor preparations (isolated neonatal spinal cord), in vivo gait analysis, single-cell electrophysiology, optogenetics, holographic glutamate uncaging, and computational modelling studies.
- Synthesis method: narrative review, organised thematically by circuit function (rhythm generation, left–right coordination, flexor–extensor alternation, motor output gain control, MN-IN reciprocal loops).
- The review explicitly limits itself to ventral IN populations contributing to core CPG circuits and briefly acknowledges the separate domain of dorsal INs integrating sensory and descending inputs.

---

### Key findings

- **Rhythm generation is distributed**: No single IN population is sufficient for rhythm generation. Glutamatergic Shox2+ non-V2a INs and HB9+ INs each contribute to locomotor frequency, as do dI6 (DMRT3+, Wt1+), V1, and excitatory V3 INs, but none is strictly necessary alone.
- **Speed-dependent left–right coordination is modular**: V0d INs secure left–right alternation at low (walking) speeds; V0v INs at intermediate (trotting) speeds; V2a INs (driving commissural V0v INs) are recruited with increasing frequency, enabling the walk-to-trot transition. Galloping/bounding circuits remain unidentified.
- **dI6 subpopulations are speed-sensitive**: DMRT3+ dI6 deletion in horses converts galloping to a pacing gait at high speeds; Wt1+ dI6 deletion disrupts fictive left–right alternation in mice.
- **Flexor–extensor alternation requires both V1 and V2b**: Each class alone is insufficient; their combined output is necessary. V1 INs are biased towards flexor MN inhibition and V2b towards extensor MN inhibition, and ~50 distinct V1 subsets (defined by combinatorial transcription factor expression) connect to joint-specific (hip, knee, ankle) microcircuits.
- **Motor output gain is regulated by V0c INs**: Cholinergic Pitx2+ V0c INs (<5% of V0 INs) form C-boutons on MNs, increase MN firing gain, and are necessary for high-amplitude ankle extensor bursting during swimming.
- **V3v INs form recurrent excitatory MN feedback**: Single-cell patch-clamp with holographic uncaging revealed a layered ipsilateral microcircuit in which medial V3vm INs synapse onto lateral V3vl INs, which innervate local MNs, which in turn synapse back onto V3v INs — a positive feedback loop. V3 deletion produces unstable, imbalanced gaits.
- **MNs are active CPG participants**: In zebrafish, V2a–MN gap junctions allow MN voltage changes to retrogradely control V2a firing thresholds and locomotor recruitment. Optogenetic MN silencing in mice reduces fictive locomotor frequency, confirming MNs as active CPG components rather than purely downstream executors.

---

### Computational framework

Not applicable in the strict sense — the paper is a narrative review and does not present or develop a computational model. However, the organisational logic it reviews is consistent with a **modular hierarchical CPG framework**: rhythm generation and pattern formation are treated as functionally separable layers, and within the pattern-forming layer, distinct circuit modules are recruited in a speed-dependent, task-specific manner. This maps loosely onto a two-level (rhythm generator / pattern formation network) CPG architecture as described in McCrea & Rybak (2007, 2008) and Danner et al. (2017), both cited in the paper.

Key variables in this implicit framework: locomotor frequency, left–right phase coordination, flexor–extensor phase, motor burst amplitude. IN subpopulations are identified as the circuit elements controlling each variable, with speed-dependent recruitment thresholds constituting a form of gain scheduling.

---

### Prevailing model of the system under study

The baseline model at the time of this review is a **two-layer spinal CPG**. A rhythm-generating layer (RG) produces the basic timing signal; a separate pattern-formation network (PF) distributes this signal to appropriate MN pools to generate coordinated flexor–extensor and left–right patterns. This half-centre oscillator concept originates with T. Graham Brown (1911) and was elaborated computationally by McCrea and Rybak. The paper's introduction also reflects an established view that molecularly distinct cardinal IN classes (V0–V3, dI1–dI6) each play broadly defined roles in this architecture, but the prevailing assumption being challenged is that these cardinal classes act as homogeneous units. The review argues that functionally relevant diversity operates at the level of molecularly defined subpopulations within each cardinal class, and that task-specific locomotor functions cannot be understood without this finer resolution.

---

### What this paper contributes

This review consolidates evidence that cardinal spinal IN classes are not functionally homogeneous — each contains molecularly and functionally distinct subpopulations with separable circuit roles. Key contributions:

1. **Speed-dependent gait transitions are implemented by distinct IN circuit modules**: V0d → walking, V0v/dI6 → trotting, with V2a INs gating the transition. This resolves how a single CPG produces qualitatively different gaits without requiring wholesale circuit reconfiguration.
2. **Recurrent MN–IN loops are architecturally diverse and functionally significant**: V3v INs form positive MN feedback loops while V1 Renshaw cells form negative feedback, and MNs themselves retrograde-regulate CPG dynamics — challenging the view of MNs as passive output elements.
3. **Task-specific recruitment of subpopulations** (e.g., V0c for high-amplitude swimming bursts) suggests that the same CPG architecture supports a wide behavioural repertoire through selective subpopulation engagement rather than circuit switching.
4. **Key open questions** identified: molecular characterisation of remaining subpopulations (e.g., V3v subtypes), circuit mechanisms for galloping/bounding, integration of dorsal INs and descending commands, and functional roles of V1 subpopulations in joint-specific reflex circuits.

---

### Brain regions & systems

- **Ventral spinal cord (lumbar segments)** — primary focus; site of the CPG networks generating locomotor rhythm and pattern.
- **Dorsal spinal cord** — briefly noted as the source of dI6 INs (which migrate ventrally) and as the site of sensory integration circuits; not the paper's main focus.
- **Central pattern generator (CPG)** — the spinal circuit system generating rhythmic locomotor output independently of supraspinal input; the paper reviews its modular organisation into rhythm-generating and pattern-forming layers.
- **Brainstem / supraspinal centres** — mentioned only peripherally as sources of descending commands that modulate spinal IN circuits.
- The paper is focused at the level of spinal circuits; no brain imaging or cortical/subcortical regions are discussed as primary subjects.

---

### Mechanistic insight

This review partially meets the bar. It synthesises studies that present circuit algorithms (e.g., speed-dependent modular recruitment, recurrent MN–IN feedback loops) and, in some cited cases, provides optogenetic, genetic deletion, and electrophysiological data supporting those specific algorithms over alternatives. However, as a review it does not present original data.

The strongest mechanistic case is for **speed-dependent left–right coordination**:

- **Computational**: The locomotor system must produce stable alternation at low speeds and synchrony at high speeds, requiring speed-dependent switching of inter-limb phase relationships.
- **Algorithmic**: Distinct V0d, V0v/dI6, and V2a IN subpopulations are sequentially recruited as speed increases. V0d provides alternation at walking; V0v (driven by V2a) extends alternation to trotting; DMRT3+ dI6 INs are required for galloping gait transitions. Each subpopulation represents a distinct circuit module with a defined speed range of operation.
- **Implementational**: Molecular identity is specified embryonically (Dbx1+ progenitors → V0d/V0v; Lbx1+ progenitors → dI6; Chx10+ postmitotic marker → V2a). Neurochemical profiles (inhibitory V0d, excitatory V0v, mainly inhibitory dI6) and axon projection patterns (commissural vs. ipsilateral) are documented.

The MN-as-active-CPG-component finding is also mechanistically grounded: gap junction recordings and optogenetic MN suppression (Song et al. 2016; Falgairolle et al. 2017) directly demonstrate retrograde MN-to-CPG signalling at the implementational level.

---

### Limitations & open questions

- The molecular characterisation of many subpopulations (particularly V3v subtypes and multiple dI6 subsets) remains incomplete, limiting selective functional manipulation.
- Circuit mechanisms enabling galloping/bounding gaits are entirely unknown.
- Whether IN subpopulations identified in neonatal fictive preparations have the same roles in adult in vivo locomotion is often untested.
- MN-to-CPG retrograde influence has been demonstrated in neonatal mice and adult zebrafish, but the generality across locomotor tasks and species remains to be established.
- The review focuses on ventral CPG INs; how dorsal INs and descending supraspinal commands are integrated into this circuit framework is acknowledged but not covered.
- The paper notes (for V3 INs) that unpublished in vivo data suggest V3 deletion prevents animals from increasing muscle strength for various locomotor tasks — this key claim is not peer-reviewed at time of publication.
- The review does not cover task-specific behaviours beyond locomotion (e.g., reaching, grasping), so generalisation of the subpopulation-diversity framework beyond locomotion remains an open question.

---

### Connections & keywords

**Key citations**:
- Grillner 2003 (Nat Rev Neurosci) — motor infrastructure
- Goulding 2009 (Nat Rev Neurosci) — vertebrate locomotor circuits
- Kiehn 2016 (Nat Rev Neurosci) — spinal locomotor circuit organisation
- McCrea & Rybak 2007, 2008 — two-layer CPG model
- Danner et al. 2017 (eLife) — computational model of gait-associated CPG circuits
- Bellardita & Kiehn 2015 (Curr Biol) — speed-associated gait characterisation in mice
- Talpalar et al. 2013 (Nature) — dual-mode V0 IN operation
- Zhang et al. 2014 (Neuron) — V1/V2b in flexor–extensor alternation
- Bikoff et al. 2016 (Cell) — V1 subpopulation diversity and motor microcircuits
- Chopek et al. 2018 (Cell Reports) — V3v layered microcircuits
- Song et al. 2016 (Nature) — MN–V2a gap junctions and retrograde CPG control
- Falgairolle et al. 2017 (eLife) — MN optogenetic control of fictive locomotion
- Andersson et al. 2012 (Nature) — DMRT3 mutations and gait in horses/mice

**Named models or frameworks**:
- Two-layer CPG model (rhythm generator / pattern formation network)
- Half-centre oscillator
- Fictive locomotion preparation
- Speed-dependent modular IN recruitment

**Brain regions**:
- Ventral spinal cord (lumbar)
- Dorsal spinal cord
- Central pattern generator (spinal)

**Keywords**:
- spinal interneuron diversity
- central pattern generator
- locomotor rhythm generation
- locomotor pattern formation
- speed-dependent gait transitions
- cardinal interneuron classes
- V0 V1 V2a V2b V3 dI6 interneurons
- flexor–extensor alternation
- left–right coordination
- motor neuron gain control
- recurrent spinal feedback circuits
- fictive locomotion
