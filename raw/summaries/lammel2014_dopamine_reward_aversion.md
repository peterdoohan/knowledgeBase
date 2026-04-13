---
source_file: lammel2014_dopamine_reward_aversion.md
paper_id: lammel2014_dopamine_reward_aversion
title: "Reward and aversion in a heterogeneous midbrain dopamine system"
authors:
  - "Stephan Lammel"
  - "Byung Kook Lim"
  - "Robert C. Malenka"
year: 2014
journal: Neuropharmacology
paper_type: review
contribution_type: review
species:
  - mouse
methods:
  - optogenetics
  - electrophysiology
  - retrograde_tracing
  - patch_clamp
  - in_vivo_microdialysis
  - conditioned_place_preference
brain_regions:
  - ventral_tegmental_area
  - nucleus_accumbens
  - medial_prefrontal_cortex
  - prefrontal_cortex
  - basolateral_amygdala
  - lateral_habenula
  - rostromedial_tegmental_nucleus
  - laterodorsal_tegmentum
  - substantia_nigra
frameworks:
  - reinforcement_learning
  - reward_prediction_error
keywords:
  - dopamine_neuron_heterogeneity
  - vta_subpopulations
  - projection_specific_dopamine_circuits
  - reward_prediction_error
  - aversive_signalling
  - optogenetic_circuit_dissection
  - mesolimbic_vs_mesocortical_dopamine
  - lateral_habenula
  - synaptic_plasticity_ampar_nmdar
  - social_defeat_stress
  - addiction_dopamine
  - conditioned_place_preference_aversion
  - reward
  - aversion
  - heterogeneous
  - midbrain
  - dopamine
  - system
key_citations:
  - schultz1997_neural_substrate_reward_pred
wiki_pages:
  - wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning
---

### One-line summary

The midbrain dopamine system comprises anatomically and functionally distinct VTA DA neuron subpopulations — defined by their projection targets — that differentially mediate reward, aversion, and stress-related behaviours via separable input-output microcircuits.

---

### Background & motivation

For decades, midbrain dopamine (DA) neurons were treated as a functionally homogeneous population whose phasic activity encodes reward prediction errors. However, this view could not easily account for observations that aversive stimuli also activate DA neurons and alter DA release, nor for the diversity of physiological properties found across VTA cells. This review synthesises emerging evidence — largely from the authors' own work using optogenetics, retrograde tracing, and projection-specific slice electrophysiology — that distinct VTA DA subpopulations, identifiable by their axonal projection targets, serve fundamentally different functions in reward and aversion. The goal is to reconcile previously contradictory findings and motivate a circuit-level understanding of how VTA DA heterogeneity contributes to addiction and depression.

---

### Methods
This is a narrative review covering literature up to early 2013, with particular emphasis on studies from the Malenka laboratory and closely related work.

- **Scope**: rodent (primarily mouse) studies of VTA DA neuron anatomy, physiology, and behaviour; some primate single-unit data included for context.
- **Key techniques reviewed**: retrograde tracing with fluorescent retrobeads; patch-clamp slice electrophysiology of identified DA subpopulations; optogenetics (ChR2-based activation of specific inputs); conditioned place preference/aversion assays; in vivo microdialysis; social defeat and chronic mild stress models of depression.
- **Synthesis method**: narrative, organised thematically — heterogeneity of the mesocorticolimbic system, afferent control of DA subpopulations, stress and depression, and drug-induced synaptic plasticity.

### Key findings

- VTA DA neurons projecting to NAc medial shell, NAc core, mPFC, and BLA are predominantly located in the medial VTA (PN and medial PBP nuclei) and have unconventional electrophysiology: absent or minimal Ih, high maximal firing frequencies (~20–30 Hz), broad action potentials, small after-hyperpolarisations, and high basal AMPAR/NMDAR ratios (~0.6).
- VTA DA neurons projecting to NAc lateral shell are located in the lateral VTA (lateral PBP) and have classical properties: prominent Ih, firing up to ~10 Hz, short action potentials with prominent after-hyperpolarisations, and low basal AMPAR/NMDAR ratios (~0.4).
- LDT inputs to the VTA preferentially contact DA neurons projecting to NAc lateral shell; optogenetic activation of these inputs produces conditioned place preference (CPP) blocked by intra-NAc DA receptor antagonism.
- LHb inputs to the VTA preferentially excite DA neurons projecting to mPFC and (via RMTg GABAergic relay) inhibit DA neurons projecting to NAc lateral shell; optogenetic activation of LHb-VTA inputs produces conditioned place aversion (CPA) blocked by intra-mPFC DA receptor antagonism.
- A single cocaine injection selectively potentiates AMPAR/NMDAR ratios on DA neurons projecting to NAc medial shell but not mPFC; a formalin aversive stimulus has the opposite selectivity, potentiating medial VTA DA neurons projecting to mPFC but not NAc medial shell. Both stimuli modify synapses on DA neurons projecting to NAc lateral shell.
- In social defeat stress models, VTA DA neuron hyperactivity is associated with a susceptible (depression-like) phenotype in mice; optogenetic phasic activation of VTA DA neurons can either promote susceptibility or reverse stress-induced depression-like behaviour depending on the stress protocol, with conflicting findings highlighting the importance of which DA subpopulation is manipulated.

---

### Computational framework

Not applicable in the formal sense — the paper does not develop or apply an explicit computational model. The theoretical framing is closest to reinforcement learning: reward prediction error (RPE) signalling is discussed as the canonical account of DA neuron phasic activity (Schultz 1997), and the review's central argument is that the RPE framework, if valid, applies differentially across DA subpopulations rather than uniformly across all DA neurons. The circuit-level specificity described (which inputs drive which DA subpopulations, projecting where) provides constraints for any computational account of how RPE-like signals are generated and transmitted to downstream structures.

---

### Prevailing model of the system under study

The introduction situates the paper against a longstanding "uniform DA neuron" model in which VTA DA cells are treated as a single population whose phasic burst firing encodes RPEs — excited by unexpected rewards or reward-predicting cues, inhibited by reward omission, and largely inhibited by aversive stimuli. Under this view, drugs of abuse were thought to hijack this single reward system by potentiating excitatory synapses on VTA DA neurons. The identification of DA neurons relied on electrophysiological proxies (prominent Ih, broad action potentials, D2R-mediated hyperpolarisation), which the paper argues led to systematic under-sampling of medial VTA DA subpopulations with unconventional properties.

---

### What this paper contributes

The review consolidates a revised model in which the VTA is a heterogeneous mosaic of DA (and non-DA) subpopulations organised by projection target, each with distinct anatomical location, electrophysiological properties, afferent connectivity, and functional role. Specifically:

- Reward and aversion are not processed by a single DA circuit but by parallel, largely non-overlapping circuits: reward is primarily mediated via LDT → lateral VTA DA → NAc lateral shell, whereas aversion is mediated via LHb → (RMTg) → medial VTA DA → mPFC.
- Drug-induced and aversion-induced synaptic plasticity in VTA are projection-specific, not uniform, resolving earlier confusion from studies that sampled only lateral VTA "conventional" DA neurons.
- Contradictory results in the stress and depression literature (activation of VTA DA neurons producing either pro- or anti-depressant effects) are reframed as potentially reflecting manipulation of different DA subpopulations, and the LHb-RMTg-VTA circuit is proposed as a key node linking aversive signalling to depression-related behaviours.

The key open question the review identifies is whether the full anatomical map of VTA inputs (now known to be far more extensive than previously appreciated) can be resolved into input-specific functional channels targeting specific DA subpopulations.

---

### Brain regions & systems

- **Ventral tegmental area (VTA)** — central focus; heterogeneous source of mesocorticolimbic DA projections, subdivided into medial VTA (PN, medial PBP, IF, CLi, RLi) and lateral VTA (lateral PBP).
- **Nucleus accumbens (NAc) — medial shell, core, lateral shell** — principal DA projection targets, with shell subdivisions functionally distinguished; NAc lateral shell linked to reward/reinforcement, NAc medial shell linked to both reward and cocaine-induced plasticity.
- **Medial prefrontal cortex (mPFC)** — target of medial VTA DA neurons; implicated in aversion-related DA signalling and depression-associated behaviours.
- **Basolateral amygdala (BLA)** — target of medial VTA DA neurons; role in aversive processing inferred from anatomical data.
- **Lateral habenula (LHb)** — key aversive/negative reward signal input to VTA; directly excites mPFC-projecting DA neurons and indirectly (via RMTg) inhibits NAc lateral shell-projecting DA neurons.
- **Rostromedial tegmental nucleus (RMTg / tail of VTA)** — GABAergic relay between LHb and NAc lateral shell-projecting VTA DA neurons; mediates inhibitory arm of aversive signal.
- **Laterodorsal tegmentum (LDT)** — excitatory input to VTA; preferentially drives NAc lateral shell-projecting DA neurons and promotes reward/CPP.
- **Substantia nigra pars compacta (SNc)** — briefly discussed as also exhibiting functional heterogeneity linked to dendritic architecture and K-ATP channel expression, but not a primary focus.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight:

1. It formalises an algorithm: distinct input channels (LDT, LHb) route reward and aversive signals through segregated VTA microcircuits to separate projection-defined DA subpopulations that release DA in different terminal fields, producing opposite behavioural outcomes.
2. It summarises neural data — optogenetic circuit dissection, projection-specific slice electrophysiology, AMPAR/NMDAR synaptic ratio measurements, and in vivo behavioural assays — that support this specific circuit model over a uniform DA system account.

**Bonus**: implementational details are addressed: specific cell types (VTA DA vs. GABAergic neurons; RMTg GABA neurons), neurotransmitter co-release (glutamate, GABA alongside DA), and synaptic receptor mechanisms (AMPAR/NMDAR potentiation) are discussed.

Mapping to Marr's levels:

- **Computational**: The brain solves the problem of separately tracking rewarding and aversive outcomes and translating these into approach/avoidance learning. Reward prediction error signals (encoding discrepancy between expected and actual outcomes) must be routed to appropriate downstream structures.
- **Algorithmic**: Reward signals are transmitted via LDT → lateral VTA DA → NAc lateral shell; aversive signals via LHb → medial VTA DA → mPFC (with concurrent disinhibition/inhibition of reward pathway via RMTg GABA neurons). Synaptic potentiation (AMPAR/NMDAR ratio increase) is a projection-specific plasticity mechanism encoding experience.
- **Implementational**: Medial VTA DA neurons (PN, medial PBP) have unconventional electrophysiology (low/absent Ih, high firing frequencies), distinct molecular markers (lower DAT, VMAT2 expression), and receive LHb excitatory input; lateral VTA DA neurons (lateral PBP) have classical properties and receive LDT excitatory input. RMTg GABAergic neurons serve as an inhibitory relay between LHb and reward-pathway DA neurons.

---

### Limitations & open questions

- Most circuit dissection work was performed in mice; the relevance to primate VTA organisation (larger, less geometrically compact) remains to be established.
- The contradictory optogenetic findings on VTA DA neuron activation in stress and depression (pro-depressant in Chaudhury et al. 2013 vs. anti-depressant in Tye et al. 2013) are noted but not resolved; the authors suggest subpopulation differences and stress-protocol differences as likely explanations, but these remain speculative.
- The full connectivity matrix of VTA inputs (now known to be extensive, per Watabe-Uchida et al. 2012) has not been functionally characterised for most afferent pathways.
- The role of DA co-transmitters (glutamate, GABA) released by DA neurons themselves in mediating behaviour is not well characterised.
- Whether SNc DA neuron heterogeneity follows similar input-output logic to VTA heterogeneity is largely unresolved.
- The review acknowledges that sampling biases in prior single-unit recording studies may have systematically missed medial VTA DA neurons with unconventional properties, making quantitative estimates of the fraction of DA neurons responding to aversive stimuli uncertain.

---

### Connections & keywords

**Key citations**:
- Lammel et al. (2008) Neuron — initial characterisation of mesoprefrontal DA neuron subpopulation with unconventional properties
- Lammel et al. (2011) Neuron — projection-specific synaptic plasticity induced by cocaine vs. aversive stimuli
- Lammel et al. (2012) Nature — input-specific (LDT vs. LHb) optogenetic control of reward and aversion via VTA microcircuits
- Schultz (1997) — foundational reward prediction error hypothesis for DA neurons
- Bromberg-Martin, Matsumoto & Hikosaka (2010) Neuron — dopamine in motivational control: rewarding, aversive, alerting
- Chaudhury et al. (2013) Nature — optogenetic activation of VTA DA neurons elicits susceptibility to social defeat
- Tye et al. (2013) — optogenetic activation of VTA DA neurons reverses depression-associated behaviours
- Hikosaka (2010) — lateral habenula in stress evasion and value-based decision-making
- Ungless & Grace (2012) — criteria for identification of VTA DA neurons in vivo and in vitro

**Named models or frameworks**:
- Reward prediction error (RPE) hypothesis (Schultz 1997)
- Conditioned place preference / conditioned place aversion (CPP/CPA) paradigms
- Social defeat stress model of depression
- AMPAR/NMDAR ratio assay for synaptic potentiation

**Brain regions**:
- Ventral tegmental area (VTA): medial VTA (mVTA), lateral VTA (lVTA)
- Nucleus accumbens (NAc): medial shell, core, lateral shell
- Medial prefrontal cortex (mPFC)
- Basolateral amygdala (BLA)
- Lateral habenula (LHb)
- Rostromedial tegmental nucleus (RMTg)
- Laterodorsal tegmentum (LDT)
- Substantia nigra pars compacta (SNc)

**Keywords**:
- dopamine neuron heterogeneity
- VTA subpopulations
- projection-specific dopamine circuits
- reward prediction error
- aversive signalling
- optogenetic circuit dissection
- mesolimbic vs. mesocortical dopamine
- lateral habenula
- synaptic plasticity AMPAR/NMDAR
- social defeat stress
- addiction dopamine
- conditioned place preference/aversion

### Related wiki pages
- [[wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning|Dopamine reward prediction error and temporal-difference learning]]
