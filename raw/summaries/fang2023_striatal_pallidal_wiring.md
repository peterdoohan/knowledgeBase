---
source_file: "fang2023_striatal_pallidal_wiring.md"
paper_id: "fang2023_striatal_pallidal_wiring"
title: "Updating the striatal\u2013pallidal wiring diagram"
authors: "Lisa Z. Fang, Meaghan C. Creed"
year: 2023
journal: "Nature Neuroscience"
paper_type: "review"
contribution_type: "review"
species: ["mouse"]
methods: ["calcium_imaging", "optogenetics", "electrophysiology"]
brain_regions: ["hippocampus", "orbitofrontal_cortex", "infralimbic_cortex", "striatum", "ventral_striatum", "nucleus_accumbens", "ventral_tegmental_area", "substantia_nigra", "thalamus", "basolateral_amygdala", "ventral_hippocampus"]
frameworks: ["reinforcement_learning"]
keywords: ["updating", "striatalpallidal", "wiring", "diagram"]
key_citations: ["kravitz2010_basal_ganglia_optogenetic"]
---

### One-line summary

This review synthesises contemporary rodent circuit-mapping studies to propose an updated wiring diagram of the striatal and pallidal complexes, highlighting molecularly defined neuronal subpopulations whose heterogeneity challenges and extends the classical direct/indirect pathway model of basal ganglia function.

---

### Background & motivation

The classical box-and-arrow model of the basal ganglia posits that direct-pathway spiny projection neurons (dSPNs/D1-SPNs) promote movement by inhibiting GPi/SNr, while indirect-pathway neurons (iSPNs/D2-SPNs) suppress movement by inhibiting the GPe, which leads to disinhibition of the STN and subsequent activation of GPi/SNr. Although highly influential — informing computational models of action selection and clinical neuromodulation therapies — this model assumes substantial homogeneity in striatal and pallidal cell types and has long been acknowledged as an oversimplification. The explosion of optogenetic, viral-tracing, single-cell sequencing, and intersectional genetic tools has uncovered considerable molecular and anatomical heterogeneity within these circuits. A synthesis integrating this diversity into a coherent updated model was lacking.

---

### Methods

- **Scope**: Rodent (primarily mouse) literature on striatal and pallidal circuit connectivity, molecular neurochemistry, and function.
- **Synthesis method**: Narrative review; no formal inclusion/exclusion criteria or meta-analytic statistics.
- **Primary evidence types reviewed**: optogenetic circuit mapping, viral anterograde/retrograde tracing (including rabies-based monosynaptic tracing), single-cell RNA sequencing and molecular marker studies, in vivo calcium imaging, in vivo and ex vivo electrophysiology, and targeted genetic manipulations (cell-type-specific knockouts, DREADDs).
- **Coverage**: Striatal composition and microcircuitry; striatal output pathways (dorsal and ventral); pallidal composition (GPe, VP, EPN); prototypical vs. arkypallidal neuron subtypes; dopamine modulation; forebrain-projecting pallidal populations.

---

### Key findings

- **D1-SPN bridging collaterals**: D1-SPNs send collateral projections into the GPe (and VP), making functional synapses and selectively inhibiting LHX6+ but not PV+ prototypical GPe neurons; collateral density is dynamically regulated by D2R signalling.
- **Ventral striatal pathway organisation diverges from the classical model**: Over 50% of VP neurons receive monosynaptic D1-SPN input; both D1-SPN and D2-SPN projections innervate relay and output VP populations, arguing against a clean direct/indirect segregation in the ventral basal ganglia.
- **Competitive model of striatal action selection**: D1-SPNs and D2-SPNs are co-active during movement; action selection is determined by the balance of activity within spatially proximal ensembles, with directional lateral inhibition from D2-SPNs onto D1-SPNs favouring suppression under asynchronous drive.
- **Dopamine asymmetrically modulates SPNs**: Phasic dopamine facilitates D1-SPN firing via Kv1.2 channel inhibition (rather than Kir2 modulation), reduces D2-SPN synaptic output via D2Rs, and bidirectionally modulates AMPA receptor insertion to bias activation toward D1-SPNs.
- **Prototypical GPe subpopulations**: LHX6+ neurons (~50% of GPe) show low-firing irregular activity and inhibit locomotion; PV+ neurons show high firing rates and drive locomotion; the two populations have partially overlapping but distinct projection targets and opposing locomotor effects when activated.
- **Arkypallidal neurons**: ~18% of pallidal neurons; project exclusively back to striatum with massive convergence (>10,000 contacts per neuron; >80% of SPNs receive input); co-release GABA and enkephalin; preferentially innervated by D1-SPNs; under tonic inhibition from prototypical neurons; activated during conditions requiring action suppression.
- **VP neurochemical heterogeneity**: ~18% of prototypical VP neurons are glutamatergic (VPGlu) and ~49% GABAergic (VPGABA); these populations have opposing effects on reward behaviour and are activated in opposing valence conditions. VPGlu neurons drive aversion/reward omission responses; VPGABA neurons support reward seeking.
- **EPN output diversity**: Three transcriptomically defined EPN populations — a GABAergic group, a glutamatergic group, and a GABA/glutamate co-releasing somatostatin+ group — project to distinct downstream targets including LHb and midbrain.
- **Non-canonical pallidal outputs to cortex**: ~5% of GPe/VP neurons are cholinergic (ChAT+), projecting to frontal/orbitofrontal cortex to decorrelate cortical activity; a separate non-cholinergic GABAergic GPe population also projects to frontal cortex and is under striatal and STN control.

---

### Computational framework

Not applicable in the sense of a formal mathematical model. However, the paper is closely related to several computational frameworks:

- **Opponent parallel pathway / go–no-go model**: The classical model implemented in numerous RL-based basal ganglia models is explicitly reviewed and critiqued.
- **Competitive ensemble model**: The paper endorses a model in which the D1/D2 balance within spatially defined SPN ensembles determines action selection, rather than strict segregation of go and no-go signals. The key mechanism is directional lateral inhibition (D2→D1) combined with intrinsic excitability differences (D2-SPNs have lower spike threshold under asynchronous drive).
- **Action suppression via arkypallidal feedback**: Arkypallidal neurons provide a broad inhibitory reset signal to striatum, interpretable as a global suppression mechanism over competing actions — consistent with race-to-threshold or urgency-based selection models.

The review does not formalise any of these as equations but provides the anatomical and physiological constraints that any biologically realistic model must satisfy.

---

### Prevailing model of the system under study

The classical "box-and-arrow" model (Albin et al. 1989; DeLong 1990; Alexander & Crutcher 1990) holds that the basal ganglia contain two segregated output pathways:

1. **Direct pathway** (dSPN/D1-SPN → GPi/SNr): Inhibits output nuclei, disinhibiting thalamus and cortex to facilitate movement.
2. **Indirect pathway** (iSPN/D2-SPN → GPe → STN → GPi/SNr): Activates output nuclei to suppress movement.

In this model, dopamine acts asymmetrically — facilitating the direct pathway via D1Rs and suppressing the indirect pathway via D2Rs — to bias the system toward action execution. The GPe is treated as a homogeneous relay nucleus, and direct and indirect pathways are strictly segregated in both the striatum and the pallidum. The classical model was operationalised in bulk optogenetic studies confirming that D1-SPN stimulation promotes and D2-SPN stimulation inhibits locomotion, further consolidating the go/no-go framing.

---

### What this paper contributes

The review consolidates evidence that substantially revises the prevailing model across several dimensions:

1. **Pathway segregation is incomplete**: D1-SPN bridging collaterals provide a direct D1-SPN input to GPe; in the ventral system, D1-SPNs are a major source of VP input, undermining the direct/indirect equivalence between striatal cell type and pallidal target.
2. **Striatal output is competitive, not oppositional**: D1-SPNs and D2-SPNs are co-active, and action selection reflects ensemble balance rather than exclusive pathway activation. D2-SPNs predominantly laterally inhibit D1-SPNs within local ensembles.
3. **The pallidum is not homogeneous**: At minimum five molecularly distinct populations populate the GPe alone (LHX6+ prototypical, PV+ prototypical, arkypallidal FOXP2+, cholinergic ChAT+, non-cholinergic cortical-projecting). Each has distinct inputs, outputs, intrinsic properties, and functions.
4. **Arkypallidal feedback provides a circuit mechanism for global action suppression**: The preferential D1-SPN→arkypallidal connectivity, combined with tonic prototypical inhibition of arkypallidal neurons, creates a disinhibitory gate for striatal inhibition precisely when the indirect pathway is dominant.
5. **VP is functionally heterogeneous along valence dimensions**: VPGlu and VPGABA neurons encode opposing valences and project to overlapping but functionally distinct downstream targets, more closely analogous to EPN output organisation than previously appreciated.
6. **Open controversies**: The proportion and identity of VP-projecting vs. VTA-projecting D1-SPNs remain unresolved; molecular overlap between LHX6+ and PV+ GPe populations complicates classification; the conditions under which arkypallidal neurons release GABA vs. enkephalin are unknown; no monosynaptic excitatory inputs to arkypallidal neurons have been identified.

---

### Brain regions & systems

- **Dorsal striatum (DSt)** — primary input nucleus; site of D1/D2-SPN action selection competition; receives topographically organised cortical (motor, somatosensory), thalamic (PF, midline), and hippocampal inputs
- **Nucleus accumbens (NAc)** — ventral striatum; integrates limbic inputs (prelimbic/infralimbic cortex, ventral hippocampus, BLA, PVT); ventral arm of the basal ganglia circuit
- **Globus pallidus externus (GPe)** — central focus; updated from homogeneous relay to heterogeneous structure with prototypical (LHX6+, PV+), arkypallidal (FOXP2+), cholinergic, and cortical-projecting subpopulations
- **Ventral pallidum (VP)** — ventral homologue of GPe; similarly heterogeneous (VPGlu, VPGABA, arkypallidal, cholinergic); critical hub for reward/aversion processing
- **Entopeduncular nucleus / GPi (EPN)** — basal ganglia output nucleus; three transcriptomically defined output populations (GABAergic, glutamatergic, GABA+Glu+somatostatin co-releasing); receives selective D1-SPN input onto glutamatergic subpopulation
- **Subthalamic nucleus (STN)** — excitatory basal ganglia nucleus; provides excitatory drive to both LHX6+ and PV+ prototypical GPe neurons; no confirmed excitatory input to arkypallidal neurons
- **Substantia nigra pars reticulata (SNr)** — basal ganglia output; receives direct D1-SPN inhibition and indirect D2→GPe→STN→SNr drive
- **Ventral tegmental area (VTA)** — dopaminergic (VTADA) and GABAergic (VTAGABA) subpopulations; VTAGABA neurons selectively inhibit NAc CINs to enhance associative learning; VTADA neurons receive polysynaptic regulation from VP
- **Lateral habenula (LHb)** — downstream target of both EPN and VP output neurons; receives opposing glutamatergic (aversive) and GABAergic (appetitive) VP signals
- **Parafascicular thalamus (PF)** — exclusively innervated by PV+ (not LHX6+) prototypical GPe neurons; mediates sensory-driven motor responses
- **Motor and orbitofrontal cortex** — targets of GPeChAT+ neurons; activity decorrelated by cholinergic pallidal projection to enhance stimulus discrimination

---

### Mechanistic insight

The paper does not present original data, so it does not itself meet the two-criterion bar of proposing a new algorithm supported by direct neural evidence. However, it synthesises mechanistic insight from the reviewed literature at Marr's three levels with respect to the competitive striatal action selection model:

- **Computational**: The basal ganglia solve the problem of selecting one action while suppressing alternatives, with the selection gated by the sensory–affective context encoded by converging excitatory inputs to spatially defined SPN ensembles.
- **Algorithmic**: Selection is implemented by the balance of D1-SPN and D2-SPN activity within local ensembles: under asynchronous excitatory drive, D2-SPNs' lower spike threshold and directional lateral inhibition onto D1-SPNs defaults the system to suppression; synchronous convergent input overcomes lateral inhibition to enable D1-SPN firing and action execution. Dopamine modulates this balance by increasing D1-SPN excitability (via Kv1.2 suppression) and reducing D2-SPN output (via D2R-mediated synaptic depression).
- **Implementational**: Identified cell-type-specific mechanisms include Kv1.2 channel modulation in D1-SPNs, D2R-coupled Gαi inhibition of D2-SPN output, NMDA receptor magnesium relief in ventral hippocampal to D1-SPN synapses, arkypallidal GABA/enkephalin co-release for broad striatal reset, and the FOXP2 vs. LHX6/NKX2-1 transcription factor lineages determining pallidal neuron identity and connectivity.

The review provides a strong synthesis but notes that many of these mechanistic proposals remain to be directly tested in vivo, particularly the causal role of bridging collaterals and the conditions triggering enkephalin vs. GABA release from arkypallidal neurons.

---

### Limitations & open questions

- Most circuit-mapping evidence derives from ex vivo slice preparations; network connectivity is disrupted and intrinsic properties may differ from in vivo conditions.
- Optogenetic monosynaptic confirmation of connectivity does not establish how presynaptic neurons modulate postsynaptic firing in intact circuits (polysynaptic effects may reverse sign of influence).
- The proportion of VP-projecting vs. VTA-projecting D1-SPNs is contested; dual retrograde tracing studies give contradictory results, potentially due to differential retrograde tracer efficiency and topographic organisation.
- LHX6 and PV overlap in GPe varies substantially across laboratories (~13–21%); their molecular dissociation remains imprecise.
- No direct monosynaptic excitatory inputs to arkypallidal neurons have been identified, leaving the mechanism of their rapid task-related activation unclear.
- Conditions favouring GABA vs. enkephalin release from arkypallidal neurons are unknown.
- Molecular identity of VP arkypallidal neurons is not firmly established (enkephalin is a candidate marker but not confirmed as selective).
- Review focuses exclusively on rodents; extrapolation to primates requires caution.
- Functional study of disease-state circuit adaptations in these molecularly defined subpopulations is nascent, limiting translation to therapeutic targets.

---

### Connections & keywords

**Key citations**:
- Albin, Young & Penney (1989) — original direct/indirect pathway model
- DeLong (1990) — primate model of basal ganglia movement disorders
- Alexander & Crutcher (1990) — opponent parallel pathway hypothesis
- Mallet et al. (2012) *Neuron* — dichotomous GPe organisation, original arkypallidal description
- Mallet et al. (2016) *Neuron* — arkypallidal stop signal to striatum
- Vachez et al. (2021) *Nat Neurosci* — ventral arkypallidal neurons in reward consumption
- Kravitz et al. (2010) *Nature* — optogenetic control of direct/indirect pathways
- Tecuapetla et al. (2016) *Cell* — complementary contributions of striatal pathways
- Brown et al. (2012) *Nature* — VTA GABA pause of accumbal CINs

**Named models or frameworks**:
- Classical direct/indirect pathway (box-and-arrow) model
- Opponent parallel pathway hypothesis
- Focused selection and inhibition of competing motor programs (Mink 1996)
- Competitive model of striatal action selection
- Arkypallidal stop-signal mechanism

**Brain regions**:
- Dorsal striatum, Nucleus accumbens, GPe, VP, EPN/GPi, SNr, STN, VTA, SNc, Lateral habenula, Parafascicular thalamus, Motor cortex, Orbitofrontal cortex, Infralimbic/prelimbic cortex, Ventral hippocampus, Basolateral amygdala, Paraventricular thalamus, Rostromedial tegmental nucleus (RMTg), Mediodorsal thalamus, Lateral hypothalamus

**Keywords**:
- basal ganglia direct and indirect pathways
- striatal spiny projection neurons (D1-SPN, D2-SPN)
- arkypallidal neurons
- prototypical pallidal neurons (LHX6+, PV+, FOXP2+)
- ventral pallidum glutamatergic vs GABAergic subpopulations
- dopamine modulation of striatal excitability
- competitive striatal action selection
- cholinergic interneurons (CINs) and parvalbumin interneurons
- bridging collaterals D1-SPN to GPe
- molecular heterogeneity basal ganglia
