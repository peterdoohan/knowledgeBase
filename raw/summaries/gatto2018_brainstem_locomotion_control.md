---
source_file: "gatto2018_brainstem_locomotion_control.md"
paper_id: "gatto2018_brainstem_locomotion_control"
title: "Locomotion Control: Brainstem Circuits Satisfy the Need for Speed"
authors: "Graziana Gatto, Martyn Goulding"
year: 2018
journal: "Current Biology"
paper_type: "review"
contribution_type: "review"
species: ["mouse"]
methods: ["optogenetics"]
brain_regions: ["striatum", "periaqueductal_gray"]
keywords: ["locomotion", "control", "brainstem", "circuits", "satisfy", "need", "speed"]
key_citations: ["roseberry2016_basal_ganglia_motor"]
---

### One-line summary

Three complementary optogenetic and viral-tracing studies establish a bimodal brainstem circuit for locomotor speed control, with glutamatergic cuneiform nucleus neurons driving fast escape locomotion and pedunculopontine nucleus neurons supporting slow exploratory behavior.

---

### Background & motivation

The mesencephalic locomotor region (MLR) — encompassing the pedunculopontine nucleus (PPN) and cuneiform nucleus (CnF) — was identified 50 years ago as a site whose electrical stimulation initiates locomotion and modulates speed. However, the cellular identity of MLR neurons, their upstream inputs, and the downstream relay circuits through which they control the spinal cord remained poorly characterized. Novel viral and genetic tools have enabled dissection of genetically defined neuronal populations, filling this gap and allowing a mechanistic account of how locomotor speed and gait are selected.

---

### Methods

This is a review/dispatch article synthesizing findings from three closely related primary research papers:

- Capelli et al. (2017, Nature): mouse genetics, viral tools, optogenetics, and monosynaptic rabies viral tracing to characterize medullary nuclei (lateral paragigantocellular nucleus, LPGi; magnocellular and gigantocellular nuclei) downstream of the MLR.
- Caggiano et al. (2018, Nature): optogenetic activation and extracellular recordings of glutamatergic CnF and PPN neurons at different locomotor speeds; monosynaptic rabies tracing of presynaptic inputs to CnF vs. PPN.
- Josset et al. (2018, Current Biology): optogenetic stimulation of CnF and PPN excitatory/cholinergic neurons in resting and freely walking mice; electromyography (EMG) of flexor and extensor muscles; analysis of state-dependence, step-cycle phase gating, and stimulation duration effects.

Synthesis method: narrative review of converging results across all three studies.

---

### Key findings

- Glutamatergic CnF neurons drive the full range of locomotor gaits (walk, trot, bound, gallop) and speed; glutamatergic PPN neurons only trigger low-speed locomotion at high stimulation intensity; cholinergic PPN neurons cannot initiate locomotion.
- CnF neurons are most active during fast locomotion; PPN neurons are preferentially active at lower speeds (extracellular recordings, Caggiano et al.).
- CnF receives strong inputs from the periaqueductal grey (PAG) and inferior colliculus; PPN glutamatergic neurons receive input mainly from basal ganglia, other midbrain structures, and several medullary nuclei.
- Glutamatergic LPGi neurons are sufficient to initiate locomotion when optogenetically activated; ablation of LPGi glutamatergic neurons dampens MLR-induced locomotion speed. Inhibitory neurons in magnocellular/gigantocellular nuclei halt locomotion (producing either spasms or atonia depending on nucleus).
- LPGi glutamatergic neurons receive input from both CnF and PPN, with a stronger bias from CnF.
- Muscle recruitment patterns are state-dependent (rest vs. walking), gated by step-cycle phase, and strongly influenced by stimulation duration: prolonged CnF activation promotes transition to faster gaits (shortens extensor burst, anticipates flexor onset); prolonged PPN activation favors slower gaits (prolongs extensor contraction, delays flexion onset).
- A dedicated glutamatergic CnF–LPGi pathway mediates escape responses; PPN pathways (likely via LPGi and other medullary/spinal nuclei) mediate basal ganglia–initiated exploratory locomotion.

---

### Computational framework

Not applicable in a strict sense. The paper does not employ a formal computational framework. The results are interpreted within a circuit-level functional architecture: a bimodal control system where two parallel descending pathways (CnF-escape and PPN-exploratory) select locomotor speed and gait based on context. This could be viewed through a dynamical systems lens — the MLR as a state-selector that routes motor commands through distinct downstream effectors — but this framing is implicit rather than formalised.

---

### Prevailing model of the system under study

The baseline understanding, as stated in the paper's introduction, was that the MLR (PPN + CnF) is a conserved midbrain structure that, when electrically stimulated, initiates locomotion and scales its speed. Prior work (Roseberry et al., 2016) had established that glutamatergic MLR neurons were necessary and sufficient for locomotion initiation and that basal ganglia structures provided strong presynaptic drive to MLR glutamatergic neurons. The MLR was known to be neurochemically heterogeneous (glutamatergic, GABAergic, and cholinergic cell types), but the functional roles of distinct subpopulations — and the specific downstream medullary relay circuits — remained largely uncharacterized. The medullary reticular formation was known to relay MLR commands to spinal cord interneurons and motor neurons via the ventral funiculus, but the cellular identity of the key relay neurons had not been established.

---

### What this paper contributes

The three synthesised studies together establish that the MLR has a bimodal functional organisation:

1. A fast-escape pathway: glutamatergic CnF neurons, driven by PAG and inferior colliculus, relay via the LPGi to produce rapid, high-speed locomotion across all gaits.
2. A slow-exploratory pathway: glutamatergic PPN neurons, driven by basal ganglia, support low-speed goal-directed exploration.

This refines the prior view of the MLR as a single speed-modulating center into a circuit with two distinct functional streams defined by neurochemistry and anatomical location. The identification of LPGi glutamatergic neurons as the critical medullary relay for MLR-initiated locomotion, and inhibitory medullary neurons as a brake, provides a cellular-level account of how brainstem circuits implement speed and gait selection. The state-dependence and temporal-dynamics findings further show that locomotor context and timing of input recruitment are as important as which neurons are active.

---

### Brain regions & systems

- Mesencephalic locomotor region (MLR) — overarching midbrain locomotor control center; the paper's primary focus
- Cuneiform nucleus (CnF) — glutamatergic neurons drive fast locomotion / escape responses; receives input from PAG and inferior colliculus
- Pedunculopontine nucleus (PPN) — glutamatergic neurons support slow exploratory locomotion; receives basal ganglia input; contains cholinergic and GABAergic populations
- Lateral paragigantocellular nucleus (LPGi) — medullary relay; glutamatergic neurons initiate locomotion; receives biased input from CnF; required for full-speed MLR-induced locomotion
- Magnocellular nucleus — medullary; inhibitory neurons halt locomotion (atonia)
- Gigantocellular nucleus — medullary; inhibitory neurons halt locomotion (spasms)
- Periaqueductal grey (PAG) — provides strong excitatory input to CnF, linking threat/escape circuits to fast locomotion
- Inferior colliculus — provides input to CnF, part of escape-response recruitment
- Basal ganglia — primary upstream driver of PPN glutamatergic neurons; mediates goal-directed, exploratory locomotion
- Spinal cord (central pattern generator, ventral laminae, motor neurons) — ultimate effectors receiving descending commands from medullary nuclei

---

### Mechanistic insight

This paper meets both criteria for the mechanistic insight section.

**Phenomenon**: The brain selects between fast escape locomotion and slow exploratory locomotion based on behavioural context.

**Computational (what problem is being solved)**: The motor system must translate high-level behavioural goals (flee vs. explore) into appropriate locomotor speed and gait, routing commands through distinct circuits depending on context.

**Algorithmic (representations and processes)**: Two parallel descending pathways implement this:
- CnF pathway: activated by threat-related midbrain structures (PAG, inferior colliculus) → relays via LPGi glutamatergic neurons → drives fast, high-frequency stepping across all gaits.
- PPN pathway: gated by basal ganglia (direct/indirect striatal pathways) → supports low-speed, goal-directed movement; cholinergic PPN neurons preferentially recruit extensors on a slower timescale.
Muscle recruitment is further shaped by spinal gating (step-cycle phase) and temporal dynamics of recruitment (short vs. prolonged stimulation determines whether individual muscle activations or full gait transitions are triggered).

**Implementational**: Specific cell types identified include VGluT2+ (glutamatergic) and ChAT+ (cholinergic) PPN neurons, VGluT2+ CnF neurons, VGluT2+ LPGi neurons (locomotion-initiating), and glycinergic/GABAergic medullary inhibitory neurons (locomotion-halting). Medullary glycinergic neurons directly contact spinal motor neurons, whereas medullary glutamatergic synapses avoid motor neuron cell bodies and concentrate in ventral central grey matter (CPG circuitry). Evidence rests on optogenetics, monosynaptic rabies tracing, extracellular recordings, EMG, and cell-type-selective ablation.

**Bonus**: The paper explicitly addresses cell-type identity, connectivity, and synaptic targets at the level of neuromodulator phenotype (glutamatergic, glycinergic, cholinergic), providing a reasonably complete implementational account.

---

### Limitations & open questions

- The relationship between optogenetic stimulation dynamics and the physiological temporal dynamics of MLR recruitment during natural escape vs. exploratory behaviour has not been established.
- Whether the bimodal organisation (CnF vs. PPN) reflects fully segregated subpopulations or overlapping ensembles with population-level dynamics remains unclear; further molecular heterogeneity within each nucleus may reveal more dedicated pathways.
- The greater number of postsynaptic targets of PPN vs. CnF neurons raises the question of whether different spatial and temporal patterns of PPN recruitment encode distinct slow-locomotion contexts — this has not been tested.
- The Chx10+ medullary stop-locomotion subpopulation (Bouvier et al., 2015) has not been placed within the MLR–LPGi circuit, leaving open how "stop-and-explore" behaviour is orchestrated.
- Whether ascending MLR projections (to basal forebrain, modulating visual cortex gain) interact with the descending locomotor control pathway is unknown.

---

### Connections & keywords

**Key citations**:
- Capelli et al. (2017, Nature) — medullary locomotor relay circuits
- Caggiano et al. (2018, Nature) — MLR heterogeneity and speed/gait control
- Josset et al. (2018, Current Biology) — CnF vs. PPN muscle recruitment and gait transitions
- Roseberry et al. (2016, Cell) — basal ganglia–MLR connectivity; glutamatergic vs. cholinergic MLR neurons
- Shik, Severin, Orlovsky (1966) — original MLR identification
- Bouvier et al. (2015, Cell) — Chx10+ brainstem neurons that halt locomotion

**Named models or frameworks**:
- Mesencephalic locomotor region (MLR) — the core concept under investigation
- Central pattern generator (CPG) — spinal locomotor network receiving descending commands
- Bimodal escape/explore circuit model — proposed by Caggiano et al. and synthesised here

**Brain regions**: Cuneiform nucleus (CnF), pedunculopontine nucleus (PPN), lateral paragigantocellular nucleus (LPGi), magnocellular nucleus, gigantocellular nucleus, periaqueductal grey (PAG), inferior colliculus, basal ganglia, spinal cord

**Keywords**: mesencephalic locomotor region, brainstem locomotor control, descending motor pathways, locomotor speed control, gait selection, optogenetics, glutamatergic neurons, pedunculopontine nucleus, cuneiform nucleus, lateral paragigantocellular nucleus, escape vs. exploratory locomotion, reticulospinal tract
