---
source_file: vicente2020_cortico_basal_ganglia_motor.md
paper_id: vicente2020_cortico_basal_ganglia_motor
title: "Cortico-basal ganglia circuits underlying dysfunctional control of motor behaviors in neuropsychiatric disorders"
authors:
  - "Ana Mafalda Vicente"
  - "Gabriela J Martins"
  - "Rui M Costa"
year: 2020
journal: "Current Opinion in Genetics and Development"
paper_type: review
contribution_type: review
species:
  - mouse
methods:
  - optogenetics
brain_regions:
  - orbitofrontal_cortex
  - prelimbic_cortex
  - striatum
  - dorsomedial_striatum
  - dorsolateral_striatum
  - ventral_striatum
  - nucleus_accumbens
  - substantia_nigra
frameworks:
  - reinforcement_learning
  - model_free_rl
keywords:
  - cortico_basal_ganglia_circuits
  - restricted_repetitive_behaviors_rrbs
  - obsessive_compulsive_disorder
  - autism_spectrum_disorder
  - direct_pathway_spiny_projection_neurons_dspns
  - indirect_pathway_spiny_projection_neurons_ispns
  - goal_directed_behavior
  - habitual_behavior
  - metabotropic_glutamate_receptor_5_mglur5
  - striatal_synaptic_plasticity
  - cortico
  - basal
  - ganglia
  - circuits
  - underlying
  - dysfunctional
  - control
  - motor
  - behaviors
  - neuropsychiatric
---

### One-line summary

This review synthesizes evidence that distinct dysregulations in specific cortico-basal ganglia circuits underlie different aspects of repetitive motor behaviors in neuropsychiatric disorders, particularly OCD and ASD.

---

### Background & motivation

Neuropsychiatric disorders often manifest with abnormal control of motor behavior, particularly restricted and repetitive patterns of behavior (RRBs). While cortico-basal ganglia circuits have long been implicated in RRBs, the range of behaviors is vast—from simple explosive motor tics to complex ritualized compulsions. This review addresses the need to understand how specific circuit dysfunctions map onto distinct motor symptoms in neuropsychiatric disorders.

---

### Methods

- **Literature scope**: Comprehensive review of recent studies using genetic animal models of OCD and ASD
- **Model systems reviewed**: 
  - OCD: Sapap3-ko, Slitrk5, Hoxb8 mice
  - ASD: Shank3-ko, Del16p11.2, deer mice, BTBR T+tf/J, C58J, AC5-ko, D2-ko mice
- **Analysis approach**: Synthesis of findings across behavioral paradigms (grooming, reversal learning, goal-directed vs. habitual behavior) and circuit manipulation studies (optogenetics, chemogenetics, pharmacology)

---

### Key findings

- **OCD models (Sapap3-ko)**: Show increased grooming and anxiety phenotypes reversed by fluoxetine; exhibit cortico-striatal synaptic dysfunction specifically (thalamocortical pathway normal); show bimodal reversal learning patterns not due to perseveration but to reduced engagement with new actions.

- **Compulsions vs. habits**: OCD may involve deficits in shifting between goal-directed and habitual systems depending on context, rather than purely habitual behavior or purely goal-directed overactivation.

- **Circuit-specific effects in OCD**: Repeated optogenetic activation of ventromedial OFC→ventral striatum induces overgrooming; stimulation of dorsolateral OFC→dorsal striatum (via feedforward inhibition) attenuates compulsive grooming in Sapap3-ko mice.

- **ASD models converge on direct/indirect pathway imbalance**: Multiple ASD genetic models (Shank3, Del16p11.2, BTBR, C58J, deer mice, AC5-ko, D2-ko) show evidence of either increased dSPN activity/function or decreased iSPN activity/function.

- **Mechanistic evidence in ASD**: 
  - Shank3-ko: impaired striatal LTD, increased SPN excitability, rescued by iSPN (not dSPN) chemogenetic activation
  - Deer mice: decreased enkephalin (iSPN marker) in high-stereotypy animals
  - BTBR mice: reduced striatal A2a receptor function; A2a agonist reduces repetitive behaviors
  - D2-ko mice: increased p-ERK, CaMKIIa, p-GluN2B, mGluR5 in dorsal striatum; rescued by D1 antagonist

- **mGluR5 as therapeutic target**: Multiple ASD models (Shank3, Del16p11.2, BTBR, AC5-ko, D2-ko) show rescue of repetitive behaviors with mGluR5 antagonism; mGluR5 is a major modulator of LTD in striatum.

- **Tourette syndrome (TS)**: Involves sensorimotor loop dysfunction; focal disinhibition in DLS induces tics; postmortem studies show selective loss of GABAergic and cholinergic interneurons in striatum.

- **ADHD**: Characterized by increased motor activity without repetitive stereotypic actions; increased D2 receptor availability in children; increased behavioral switching (associated with iSPN activity); D1 agonist reduces hyperactivity in mouse models.

---

### Computational framework

The review employs a reinforcement learning (RL) framework to conceptualize the balance between goal-directed and habitual action control. The basal ganglia are understood as implementing action selection through opponent processing:

- **Direct pathway (dSPNs)**: Promote action performance and continuation/repetition of ongoing actions
- **Indirect pathway (iSPNs)**: Permit action switching by inhibiting competing actions

This framework conceptualizes repetitive behaviors as arising from an imbalance favoring the direct pathway (excessive action continuation) or impaired indirect pathway function (reduced action switching). The review also incorporates model-based vs. model-free RL distinctions to discuss OCD, where aberrant prediction error signaling and uncertainty processing may drive compulsive checking behavior.

---

### Prevailing model of the system under study

Prior to the reviewed work, the prevailing model of basal ganglia function in motor control was the "classic" direct/indirect pathway model where dSPNs promote movement and iSPNs suppress movement. This model was already being challenged by observations that both populations are active during movement. The review notes that accumulating evidence from optogenetic studies (particularly Tecuapetla et al. 2016) supports a revised model where both pathways are necessary for movement, with dSPNs supporting specific actions and iSPNs inhibiting competing actions. For neuropsychiatric disorders, there was a general understanding that cortico-striatal dysfunction underlies RRBs, but the specific circuit dysfunctions mapping to distinct behavioral phenotypes were not well characterized.

---

### What this paper contributes

This review advances understanding by:

1. **Mapping specific circuit dysfunctions to distinct RRB subtypes**: Demonstrating that different types of repetitive behaviors (compulsions vs. stereotypies) emerge from distinct dysregulations in specific cortico-basal ganglia circuits, rather than being undifferentiated manifestations of "basal ganglia dysfunction."

2. **Synthesizing a revised model of direct/indirect pathway imbalance for ASD**: Proposing that repetitive behaviors in ASD arise from an imbalance favoring the direct pathway over the indirect pathway in dorsal striatum, supported by converging evidence from multiple genetic models (Shank3, Del16p11.2, BTBR, D2-ko, etc.).

3. **Differentiating habitual vs. goal-directed contributions to OCD**: Clarifying that OCD may involve context-dependent deficits in shifting between goal-directed and habitual systems, rather than purely habitual or purely goal-directed dysfunction.

4. **Identifying therapeutic targets**: Highlighting mGluR5 antagonism and A2a receptor agonism as promising circuit-based interventions for ASD repetitive behaviors.

---

### Brain regions & systems

- **Dorsal striatum (dorsomedial striatum, DMS)**: Involved in early action learning and goal-directed behaviors; receives inputs from associative cortices (prelimbic cortex, orbitofrontal cortex); implicated in OCD compulsions and reversal learning deficits.

- **Dorsal striatum (dorsolateral striatum, DLS)**: Associated with late skill learning, sequence chunking, and habitual actions; receives sensorimotor cortical inputs; implicated in habit formation and Tourette syndrome tics.

- **Ventral striatum (nucleus accumbens)**: Involved in reinforcement and motivational processing; receives projections from ventromedial orbitofrontal cortex; stimulation of this pathway induces overgrooming.

- **Substantia nigra pars compacta (SNc)**: Source of dopaminergic projections to dorsal striatum; shows differential responses to aversive stimuli in DMS-projecting vs. DLS-projecting cells.

- **Subthalamic nucleus (STN)**: Part of the hyperdirect pathway; receives direct cortical projections.

- **Globus pallidus internal segment (GPi)**: Basal ganglia output nucleus; exerts inhibitory control over downstream areas.

- **Orbitofrontal cortex (OFC)**: Associative cortex projecting to striatum; ventromedial OFC→ventral striatum promotes grooming; dorsolateral OFC→dorsal striatum suppresses compulsive grooming.

- **Prelimbic cortex (PL)**: Projects predominantly to dSPNs in dorsal striatum; involved in goal-directed behavior.

- **Striatal interneurons**: Parvalbumin-positive GABAergic interneurons and cholinergic interneurons; loss in Tourette syndrome leads to enhanced stereotypies.

---

### Mechanistic insight

The review provides substantial mechanistic insight into the neural basis of repetitive behaviors, though it does not present novel experimental data but rather synthesizes existing findings. The mechanistic contributions are:

**Computational level**: The review frames repetitive behaviors within reinforcement learning theory, conceptualizing the problem as dysregulated action selection where the balance between continuing current actions (direct pathway) and switching to alternatives (indirect pathway) is disrupted.

**Algorithmic level**: The review identifies specific algorithmic implementations of action control:
- Direct pathway SPNs (dSPNs) support action performance and continuation
- Indirect pathway SPNs (iSPNs) enable action switching by suppressing competing actions
- Dopamine modulates both pathways differentially (D1 receptors on dSPNs, D2 receptors on iSPNs)
- mGluR5 signaling regulates synaptic plasticity at cortico-striatal synapses

**Implementational level**: The review maps these algorithms onto specific neural hardware:
- Distinct cortico-striatal circuits (OFC→ventral striatum vs. OFC→dorsal striatum) mediate different behavioral effects
- DMS-projecting vs. DLS-projecting SNc dopamine neurons show differential responses to aversive stimuli
- Specific cell types (parvalbumin interneurons, cholinergic interneurons) modulate striatal output
- Genetic mutations (Shank3, Sapap3, Del16p11.2) converge on common circuit-level pathophysiology

The review does not itself provide new neural data linking model variables to measured activity, but synthesizes extensive evidence from multiple studies that together establish these mechanistic links.

---

### Limitations & open questions

- **Heterogeneity of RRBs**: The diversity of repetitive behaviors (stereotypies, compulsions, tics, perseveration) is not always differentiated in animal models, making it difficult to map specific circuit dysfunctions to specific behavioral phenotypes.

- **Construct validity of animal models**: The review notes that animal models have "sometimes-limited construct or face validity" for neuropsychiatric disorders, though they remain useful for establishing circuit-behavior links.

- **Translational gaps**: While optogenetic and chemogenetic studies in animals reveal circuit mechanisms, translating these findings to human therapeutic interventions remains challenging.

- **Dissociating goal-directed vs. habitual systems**: The field lacks consensus on whether OCD compulsions stem from overactive habitual systems, overactive goal-directed systems, or deficits in switching between them.

- **Dopamine's role in ASD**: While there is evidence for dopamine dysfunction in ASD, the exact mechanisms and how they interact with other systems (e.g., mGluR5 signaling) remain incompletely understood.

- **Sex differences**: Most studies use male animals, and sex differences in circuit dysfunction and behavioral phenotypes are understudied.

---

### Connections & keywords

**Key citations**:
- Albin et al. 1989 (classic direct/indirect pathway model)
- Tecuapetla et al. 2016 (complementary contributions of striatal projection pathways)
- Ahmari et al. 2013 (repeated cortico-striatal stimulation generates OCD-like behavior)
- Burguière et al. 2013 (optogenetic stimulation of lateral orbitofrontostriatal pathway suppresses compulsions)
- Welch et al. 2007 (Sapap3-mutant mice OCD-like behaviors)
- Peça et al. 2011 (Shank3 mutant mice ASD behaviors)

**Named models or frameworks**:
- Direct and indirect pathway model of basal ganglia
- Goal-directed vs. habitual action control
- Reinforcement learning (RL) framework
- mGluR5-mediated synaptic plasticity
- Dopamine prediction error signaling

**Brain regions**:
- Dorsal striatum (dorsomedial and dorsolateral)
- Ventral striatum/nucleus accumbens
- Orbitofrontal cortex (ventromedial and dorsolateral)
- Prelimbic cortex
- Substantia nigra pars compacta
- Subthalamic nucleus
- Globus pallidus internal segment
- Striatal interneurons (parvalbumin-positive, cholinergic)

**Keywords**:
- cortico-basal ganglia circuits
- restricted repetitive behaviors (RRBs)
- obsessive-compulsive disorder
- autism spectrum disorder
- direct pathway spiny projection neurons (dSPNs)
- indirect pathway spiny projection neurons (iSPNs)
- goal-directed behavior
- habitual behavior
- metabotropic glutamate receptor 5 (mGluR5)
- striatal synaptic plasticity
