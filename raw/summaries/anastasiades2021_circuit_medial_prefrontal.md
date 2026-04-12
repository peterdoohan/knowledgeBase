---
source_file: anastasiades2021_circuit_medial_prefrontal.md
paper_id: anastasiades2021_circuit_medial_prefrontal
title: "Circuit organization of the rodent medial prefrontal cortex"
authors:
  - "Paul G. Anastasiades"
  - "Adam G. Carter"
year: 2021
journal: "Trends in Neurosciences"
paper_type: review
contribution_type: review
species:
  - mouse
methods:
  - optogenetics
  - electrophysiology
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - anterior_cingulate_cortex
  - prelimbic_cortex
  - infralimbic_cortex
  - striatum
  - ventral_tegmental_area
  - thalamus
  - mediodorsal_thalamus
  - amygdala
  - basolateral_amygdala
  - periaqueductal_gray
  - ventral_hippocampus
keywords:
  - medial_prefrontal_cortex
  - agranular_cortex
  - projection_neuron_diversity
  - intratelencephalic_neurons
  - pyramidal_tract_neurons
  - corticothalamic_neurons
  - long_range_afferent_specificity
  - laminar_targeting
  - feedforward_inhibition
  - disinhibitory_circuits
  - parvalbumin_interneurons
  - somatostatin_interneurons
  - cck_interneurons
  - ndnf_interneurons
  - vip_interneurons
  - reciprocal_loops
  - dendritic_computation
  - endocannabinoid_modulation
  - cell_type_specific_wiring
  - rodent_prefrontal_cortex
---

### One-line summary

This review synthesises emerging cell- and synapse-specific wiring rules in the rodent medial prefrontal cortex (mPFC), showing how its agranular architecture, diverse projection neurons, and layer-specific long-range inputs together produce a circuit organisation fundamentally distinct from sensory cortex.

---

### Background & motivation

The prefrontal cortex supports cognition, motivation, reward, and emotion, and is implicated in schizophrenia, ADHD, addiction, and depression. Yet our mechanistic understanding of cortical circuitry has been built almost entirely on primary sensory cortices, which differ substantially from the agranular mPFC in laminar structure, cell-type composition, and connectivity. The field lacked a synthesis of how the mPFC's unique architecture — its projection neuron diversity, the targeting rules of its long-range afferents, and its local excitatory and inhibitory microcircuits — collectively departs from the canonical cortical model and may support the mPFC's specialised functional roles.

---

### Methods

- **Scope**: Rodent (primarily mouse) mPFC, focusing on the prelimbic cortex (PL), with comparisons to anterior cingulate (ACC) and infralimbic (IL) cortices.
- **Synthesis method**: Narrative review integrating anatomical tracing studies, slice electrophysiology, optogenetics, in vivo recording, and imaging.
- **Topics covered**: (i) Projection neuron diversity and intrinsic properties; (ii) laminar and cell-type specificity of long-range excitatory afferents (contralateral PFC, mediodorsal thalamus, ventromedial thalamus, BLA, ventral hippocampus); (iii) local excitatory microcircuit organisation across layers; (iv) GABAergic interneuron subtypes and their inhibitory connectivity; (v) activation of inhibitory circuits by long-range inputs; (vi) functional implications and outstanding questions.

---

### Key findings

- The mPFC is agranular — it lacks a canonical L4 — so thalamic and other long-range inputs are distributed across L1–L6, unlike sensory cortex where primary thalamic input targets L4.
- Projection neurons span L2–L6 and fall into three major classes (intratelencephalic/IT, pyramidal tract/PT, corticothalamic/CT), each with distinct morphology, intrinsic physiology, and subcellular properties; the mPFC has more broadly distributed corticostriatal and corticoclaustral neurons than sensory cortex.
- Long-range inputs are laminar- and cell-type-specific: BLA preferentially targets L2 cortico-amygdalar neurons; mediodorsal (MD) thalamus strongly drives L3 IT cells; ventromedial (VM) thalamus enriches inputs at the distal apical dendrites of L5 PT cells (a motif not seen in sensory cortex); ventral hippocampus (vHPC) preferentially targets L5 IT cells.
- Many long-range inputs preferentially contact neurons that project back to the input region, providing a synaptic basis for strong reciprocal loops (e.g. BLA↔mPFC, mPFC↔thalamus).
- In local excitatory circuits, IT cells strongly innervate PT cells (but not vice versa), imposing a directional flow that ensures local computations are funnelled into output pathways.
- mPFC has fewer PV+ interneurons but more SOM+ and CCK+ cells than sensory cortex; PV+, SOM+, CCK+, and NDNF+ interneurons all show biased inhibitory connectivity, preferentially targeting L5 PT cells over IT cells.
- Long-range inputs recruit distinct interneuron populations: cPFC targets PV+ basket and chandelier cells; MD drives PV+ and SOM+ cells in L3 and VIP+ cells in L1b; VM drives NDNF+ cells in L1a; vHPC activates CCK+ interneurons that show endocannabinoid-mediated presynaptic modulation specifically at IT cell synapses.
- Disinhibitory circuits exist in the mPFC: VIP+ cells target SOM+ cells; NDNF+ cells in L1 target PV+ cells in L2/3; these allow long-range inputs to gate inhibitory tone in a pathway-specific manner.
- Wiring rules differ along the dorsoventral axis: BLA and vHPC show graded innervation across ACC, PL, and IL, with distinct laminar and cell-type targeting in each subregion.

---

### Computational framework

Not applicable as a standalone formalism — no quantitative model is built or simulated. However, the review is organised around a circuit-level understanding of signal routing and integration, drawing implicitly on the following computational ideas:

- **Reverberant/attractor dynamics**: connections between pyramidal cells within the same class (especially IT–IT and PT–PT) display facilitating short-term dynamics predicted to sustain persistent, delay-period activity, relevant to working memory attractor models (citing Wang 2001).
- **Hierarchical feedforward processing**: the laminar flow from L2/3 IT → L5 PT mirrors the canonical cortical hierarchy, now mapped onto a cell-type-specific substrate.
- **Dendritic computation**: VM thalamic inputs to PT apical tufts can evoke dendritic Ca²⁺ spikes, analogous to perforant path gating in hippocampal CA1 — a mechanism for multiplicative gating or coincidence detection at the single-cell level.
- **Feedforward vs. feedback inhibition**: PV+ cells (fast, depressing synapses) dominate feedforward inhibition on initial input; SOM+ cells (facilitating synapses) take over during repeated activation, shifting inhibition from soma to dendrites.

---

### Prevailing model of the system under study

Before the wave of cell-type-specific studies reviewed here, the dominant framework for cortical circuitry was derived almost entirely from primary sensory cortices, particularly barrel cortex and visual cortex. In that canonical model: thalamic inputs drive L4 (a prominent granular layer) → L4 excites L2/3 → L2/3 projects to L5 output neurons → L5 PT cells send subcortical commands. Interneurons were largely treated as providing a "blanket" of inhibition relatively indiscriminately onto local pyramidal cells. The mPFC was known to be agranular and to receive diverse inputs related to cognition, motivation, and emotion, and its broad behavioural roles had been studied for decades; but the cell-type- and synapse-level specificity of its circuitry — which inputs target which projection neurons, how interneurons are selectively recruited, how local connections are directionally organised — remained largely unknown. The default assumption was that mPFC circuits would broadly resemble sensory cortex, modified only by the absence of L4.

---

### What this paper contributes

This review establishes that the mPFC is not simply a sensory cortex without L4. Instead, it is organised by a set of cell- and synapse-specific wiring rules that are qualitatively different:

1. **Input specificity**: Each major long-range input preferentially engages a distinct combination of projection neurons and interneurons across layers, rather than converging uniformly. This cell-type specificity gives each pathway a unique functional fingerprint.
2. **Reciprocal loop architecture**: Multiple inputs (BLA, thalamus, contralateral PFC) preferentially contact neurons that project back to the input source, constituting dedicated reciprocal loops — a more closed, loop-based architecture than the largely feedforward sensory hierarchy.
3. **Dendritic gating by VM thalamus**: The enrichment of VM inputs at PT apical tufts, capable of driving dendritic Ca²⁺ spikes, is a feature not found in sensory cortex and points to a distinct mechanism for modulating mPFC output.
4. **Biased inhibition**: Interneurons in mPFC are not indiscriminate — they preferentially target specific projection neuron subtypes (PT over IT, cortico-amygdalar over corticocortical), meaning inhibition is organised to selectively gate output pathways rather than globally suppress activity.
5. **Endocannabinoid-modulated feedforward inhibition**: The CCK+ circuit recruited by vHPC provides an inhibitory pathway that is selectively sensitive to endocannabinoids at IT cell synapses, adding a neuromodulatory layer of pathway specificity not previously appreciated.

These findings collectively allow the field to reason about which specific circuit elements support functions like working memory (sustained IT–IT reverberant activity), emotional memory (BLA↔L2 cortico-amygdalar loop), and output gating (VM→PT apical dendrites), and to identify exactly which elements may be disrupted in psychiatric disease.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)** — primary subject; encompasses ACC, PL, and IL; focus of all circuit analysis.
  - **Anterior cingulate cortex (ACC)** — dorsal mPFC; roles in decision making and action; distinct input/output profile from PL and IL.
  - **Prelimbic cortex (PL)** — primary focus for cell-type-specific circuit mapping; role in cognitive control and fear expression.
  - **Infralimbic cortex (IL)** — ventral mPFC; roles in motivation, emotion, extinction; distinct vHPC and BLA connectivity compared to PL.
- **Mediodorsal thalamus (MD)** — provides prominent L1/L3 input to mPFC; strongly drives L3 IT cells; key role in working memory and attention.
- **Ventromedial thalamus (VM)** — provides dense L1a input; selectively targets PT apical dendrites; distinct from MD in target and function; role in arousal and cortical state regulation.
- **Basolateral amygdala (BLA)** — provides L2-enriched input in PL; selectively targets cortico-amygdalar neurons; critical for emotional encoding, expression, and extinction.
- **Ventral hippocampus (vHPC)** — primarily targets L5 of IL, with weaker input to PL; preferentially contacts IT cells; role in contextual/mnemonic and emotional control signals.
- **Contralateral PFC (cPFC)** — distributed input across all layers; relatively egalitarian targeting of projection neurons; shares information across hemispheres.
- **Striatum** — major target of IT and PT efferents; receives mPFC corticostriatal projections.
- **Claustrum** — both a target and a source of mPFC projections; sends inhibitory input activating NPY+ interneurons in deeper layers; bilateral projections appear unique to frontal cortex.
- **Periaqueductal gray (PAG)**, **VTA**, **pons** — subcortical targets of mPFC PT efferents; relevant to autonomic, neuromodulatory, and aversive processing.

---

### Mechanistic insight

The paper does not present novel primary data — it is a review — so it cannot meet the dual bar of presenting a formalised algorithm AND providing neural data supporting that algorithm over alternatives. However, it synthesises mechanistic insight at the circuit level that partially maps onto Marr's levels:

- **Computational**: The mPFC must integrate heterogeneous inputs conveying cognitive, motivational, and emotional signals and route the appropriate signals to diverse subcortical and cortical outputs in a context- and task-dependent manner.
- **Algorithmic**: The reviewed evidence points toward a routing architecture in which (i) specific projection neuron classes serve as labelled lines to specific output structures; (ii) long-range afferents selectively engage the appropriate output neurons and their associated inhibitory circuits; and (iii) reciprocal loops sustain activity over delays. The IT→PT directionality in local excitation formalises a processing stage between input and output.
- **Implementational**: Cell-type-specific connectivity is realised via identifiable morphological and physiological cell classes (PV+, SOM+, CCK+, NDNF+, VIP+ interneurons; IT/PT/CT pyramidal cells), specific synaptic loci (soma vs. dendrite), and synapse-specific short-term dynamics (facilitating vs. depressing), with neuromodulation (endocannabinoids at CCK+ terminals, dopamine broadly) adding a regulatory layer.

The review synthesises enough mechanistic detail across primary studies to constitute a coherent, implementationally grounded circuit account, even though no single empirical test of the full scheme is presented here.

---

### Limitations & open questions

- The review focuses almost exclusively on the mouse PL; whether findings generalise to IL, ACC, other rodents, or primates is explicitly noted as unresolved.
- The exact number and identity of cell types in mPFC remains unclear; the IT/PT/CT taxonomy is acknowledged as an oversimplification.
- Ipsilateral cortical inputs (other than cPFC callosal) and claustral inputs are poorly characterised.
- How subregions of mPFC (ACC, PL, IL) communicate with each other via local cortical connections is largely unknown.
- The relative functional dominance of feedforward excitation, feedforward inhibition, feedback inhibition, and disinhibition in vivo — and how they combine during behaviour — is unresolved.
- Neuromodulatory regulation of specific circuit elements (dopamine, noradrenaline, acetylcholine, endocannabinoids) is noted as important but incompletely understood.
- How mPFC circuits are disrupted in psychiatric disorders (schizophrenia, depression, ADHD, addiction) remains a major open question.
- The functional implications of VM input to PT apical dendrites — particularly for synaptic plasticity — are not yet established.

---

### Connections & keywords

**Key citations**:
- Harris & Shepherd (2015, Nat. Neurosci.) — canonical neocortical circuit framework used as the primary point of comparison throughout.
- Collins et al. (2018, Neuron) — reciprocal prefrontal–thalamic circuits; primary empirical basis for MD/VM targeting rules.
- Anastasiades et al. (2021, Neuron) — MD and VM thalamus engage distinct L1 circuits (NDNF+ vs. VIP+ cells).
- Little & Carter (2013, J. Neurosci.) — synaptic basis for mPFC–BLA reciprocal connectivity.
- Liu & Carter (2018, J. Neurosci.) — vHPC inputs preferentially target IT cells in IL.
- Liu et al. (2020, eLife) — CCK+ interneurons and endocannabinoid-modulated feedforward inhibition.
- Anastasiades et al. (2018, Cell Reports) — callosal excitation and feedforward inhibition specificity.
- Anastasiades et al. (2019, Cereb. Cortex) — D1 dopamine receptor modulation of projection neurons and interneurons.
- Wang (2001, Trends Neurosci.) — synaptic reverberation and persistent activity.
- Tremblay et al. (2016, Neuron) — GABAergic interneurons in the neocortex; canonical interneuron framework.

**Named models or frameworks**:
- IT/PT/CT projection neuron classification
- Feedforward vs. feedback inhibition framework
- Marr's levels (implicitly invoked in the mechanistic discussion)
- Driver/modulator classification for thalamic inputs
- Attractor/reverberant activity model for working memory (Wang 2001)

**Brain regions**:
- Medial prefrontal cortex (mPFC): anterior cingulate cortex (ACC), prelimbic cortex (PL), infralimbic cortex (IL)
- Mediodorsal thalamus (MD)
- Ventromedial thalamus (VM)
- Basolateral amygdala (BLA)
- Ventral hippocampus (vHPC)
- Contralateral PFC
- Striatum
- Claustrum
- Periaqueductal gray (PAG)
- VTA

**Keywords**: medial prefrontal cortex, agranular cortex, projection neuron diversity, intratelencephalic neurons, pyramidal tract neurons, corticothalamic neurons, long-range afferent specificity, laminar targeting, feedforward inhibition, disinhibitory circuits, parvalbumin interneurons, somatostatin interneurons, CCK interneurons, NDNF interneurons, VIP interneurons, reciprocal loops, dendritic computation, endocannabinoid modulation, cell-type-specific wiring, rodent prefrontal cortex
