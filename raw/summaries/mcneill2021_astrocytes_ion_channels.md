---
source_file: mcneill2021_astrocytes_ion_channels.md
title: "Ion Channels and Electrophysiological Properties of Astrocytes: Implications for Emergent Stimulation Technologies"
authors: Jessica McNeill, Christopher Rudyk, Michael E. Hildebrand, Natalina Salmaso
year: 2021
journal: Frontiers in Cellular Neuroscience
paper_type: review
contribution_type: review
---

### One-line summary

This review synthesises the extensive electrophysiological heterogeneity of astrocytes — spanning K+, Na+, and Ca2+ channels and signalling — and evaluates the implications of that heterogeneity for the physiological validity of optogenetic and DREADD-based astrocyte manipulation.

---

### Background & motivation

Astrocytes were historically regarded as electrically silent support cells, but accumulating evidence shows they are electrically dynamic, ionically active, and functionally diverse across brain regions. Despite this, the electrophysiological properties of astrocyte subpopulations remain poorly characterised, and the relationship between regional physiology, ion channel expression, and function has not been systematically mapped. Concurrently, optogenetics and DREADDs are increasingly being applied to astrocytes without full appreciation of whether these tools produce physiologically valid manipulations given the unique electrophysiology of glial cells. This review addresses both gaps: characterising the diversity of astrocyte electrophysiology, and evaluating what this diversity means for experimental design using emergent stimulation technologies.

---

### Methods

- Scope: narrative review of primary literature on astrocyte electrophysiology across CNS regions, covering K+, Na+, and Ca2+ channels, membrane potential, membrane resistance, and Ca2+ signalling.
- Also reviews the use of optogenetics (ChR2, halorhodopsin, Arch, melanopsin) and DREADDs (hM3Dq, hM4Di) in astrocytes.
- Synthesis is narrative (not meta-analytic); studies from rodents (in vitro, slice, in vivo) and limited human data are considered.
- Comparisons across species (rodent vs. human) and across developmental timepoints are addressed.

---

### Key findings

- Astrocytes have a highly negative resting membrane potential (RMP), typically more hyperpolarised than neurons, ranging from approximately -62 mV (optic nerve) to -90 mV (hippocampal stratum oriens), with substantial within-region variability.
- RMP is influenced by multiple factors: ion channel composition (especially Kir4.1), morphology, neighbouring neuronal inputs, and intracellular cAMP/PKA signalling.
- Astrocytes have very low membrane input resistance (~1-3 MΩ), reflecting high ionic permeability at rest; this varies by region (VTA ~1 MΩ vs. cortex/hippocampus ~3 MΩ) and changes under reactive conditions (e.g. CNS injury).
- K+ homeostasis relies on spatial buffering through inward-rectifying channels (principally Kir4.1), two-pore domain leak channels (TREK1, TWIK1), and voltage-gated Kv channels; expression of all these subtypes is regionally and subregionally heterogeneous.
- Voltage-dependent Na+ channels (Nav1.2, Nav1.3, Nav1.5, Nav1.6) are expressed in astrocytes and their expression is heterogeneous across CNS regions and morphological subtypes; Nav1.6 upregulation in reactive astrocytes is linked to epileptogenesis, and Nav1.5 is implicated in wound closure and injury response.
- Ca2+ signalling is the physiological hallmark of astrocytes: it is driven by GqPCR-IP3R2-mediated release from ER stores, supplemented by extracellular Ca2+ influx; spontaneous Ca2+ events occur predominantly in fine processes (~80-85% of events), vary in frequency and amplitude inter- and intra-regionally, and can propagate as waves through the glial syncytium via gap junctions.
- Subcellular Ca2+ microdomains (restricted transients) co-exist with somatic and wave-like signals, suggesting spatially localised astrocyte-synapse communication.
- For optogenetics: ChR2 drives Na+ (and Ca2+) influx causing Ca2+ transients and gliotransmitter release; halorhodopsin hyperpolarises via Cl- influx; Arch hyperpolarises via proton efflux and also evokes Ca2+ transients; melanopsin activates GqPCR-IP3 signalling and is considered more physiologically matched to endogenous astrocyte Ca2+ pathways.
- Due to low membrane resistance, astrocytes produce smaller current changes to optogenetic stimulation than neurons, likely requiring stronger or more sustained stimulation parameters.
- The glial syncytium raises concerns about "double stimulation" and "spillover" effects: activation of opsin- or DREADD-expressing astrocytes may propagate to coupled non-expressing neighbours via gap junctions, and astrocytes already stimulated optogenetically may be additionally driven by gap-junction input from neighbouring stimulated cells.
- Some electrophysiological properties (RMP, passive conductance, membrane resistance) appear conserved between human and rodent astrocytes, but the evidence base is thin.

---

### Computational framework

Not applicable. The paper is a descriptive biological review with no explicit computational or mathematical framework. The results could, in principle, constrain biophysical models of astrocyte-neuron interaction (e.g. conductance-based models of K+ spatial buffering) and constrain network-level models of gliotransmission and synaptic modulation. The discussion of Ca2+ microdomain vs. wave signalling is qualitatively consistent with reaction-diffusion and compartmental modelling frameworks, but these are not formalised here.

---

### Prevailing model of the system under study

The introduction positions astrocytes against a prior view of them as passive support cells: electrically silent, functioning mainly to provide structural and metabolic support for neurons. By the time of writing, this view had already been substantially revised — astrocytes are known components of the tripartite synapse, capable of glutamate uptake, gliotransmission, K+ buffering, blood-brain barrier regulation, and Ca2+ signalling. However, the prevailing implicit model that the review pushes against is one in which astrocytes are treated as a relatively homogeneous population: a generic "astrocyte" physiology applicable across brain regions. The authors argue this is inadequate, and that the field has not yet characterised the extent to which astrocytes differ electrophysiologically within and between regions, nor what those differences mean for their functions or for experimental manipulation.

---

### What this paper contributes

The review establishes that astrocyte electrophysiology is heterogeneous at every level — between regions, within regions (subregionally), across morphological subtypes, across subcellular compartments, and across development. This heterogeneity is documented across the key electrophysiological parameters: RMP, membrane resistance, K+ channel expression and subtype composition, Na+ channel expression and current properties, and Ca2+ signalling dynamics. The paper identifies two key unresolved problems: (1) the functional significance of the physiological heterogeneity for the broader synaptic network remains largely unclear; (2) optogenetics and DREADDs — increasingly used to probe astrocyte function — produce manipulations whose physiological validity depends critically on which astrocyte subtype is targeted, in which region, under what experimental conditions, and using which specific opsin or DREADD variant. The review identifies specific risks (double stimulation, syncytium spillover, non-physiological Ca2+ kinetics) that are often overlooked in experimental design.

---

### Brain regions & systems

- Hippocampus (CA1, stratum radiatum, stratum oriens, stratum pyramidale, stratum lucidum, dentate gyrus) — primary locus of electrophysiological characterisation; RMP, resistance, K+ channel, Na+ channel, and Ca2+ signalling heterogeneity all documented here.
- Cortex (neocortex, somatosensory cortex, layers I-VI) — heterogeneity of Kir4.1 expression, Ca2+ oscillation frequency (layer I vs. II/III), and Na+ transient amplitude documented.
- Cerebellum (Bergmann glia, granule cell layer, Purkinje cell layer) — distinct Kir4.1, Nav1.6, and IP3R2 localisation patterns across morphological subtypes.
- Optic nerve — fibrous astrocytes with distinct RMP range and Na+ current properties; Kir4.1 in endfeet and processes.
- Spinal cord — Na+ channel (Nav1.2, Nav1.3, Kv1.5) and K+ channel expression characterised.
- Ventral tegmental area (VTA) — lower membrane resistance than cortex or hippocampus.
- Thalamus, striatum, olfactory bulb — spontaneous Ca2+ oscillation heterogeneity documented.
- Retina (Muller glia) — Kir4.1 preferentially in perivascular endfeet.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined. It is a review that collates descriptive electrophysiological data and does not present or formalise an algorithm, nor does it provide new neural data linking a specific mechanistic account to measured physiological activity. The closest it comes is in mapping K+ spatial buffering to Kir4.1 expression and passive conductance, and linking Nav1.6 upregulation in reactive astrocytes to Ca2+-mediated glutamate release and epileptogenesis — but these are narrative syntheses of existing primary work rather than a new algorithmic account supported by targeted neural evidence.

---

### Limitations & open questions

- The functional significance of regional and subregional electrophysiological diversity for network activity and neuronal computation remains largely uncharacterised.
- The relationship between astrocyte morphology, RMP, and ion channel density has not been directly tested; morphology is proposed as a contributing factor but not causally established.
- The mechanisms driving developmental changes in astrocyte electrophysiology are unknown; KCC2 expression changes are proposed as one candidate.
- Cross-species validity is poorly established: few studies have directly compared rodent and human astrocyte electrophysiology; early human studies may have recorded NG2+ cells rather than astrocytes.
- Differences between in vitro, acute slice, and in vivo preparations have not been systematically compared for astrocyte electrophysiology.
- For optogenetics and DREADDs: the extent to which gap-junction-mediated spillover and double stimulation occur under different experimental conditions is largely unexplored; the subcellular localisation of opsins and DREADD receptors within astrocytes, and its functional consequences, have not been characterised.
- The physiological conditions under which different opsin variants (ChR2 vs. ChETA vs. CatCh vs. melanopsin) produce equivalent or divergent downstream effects in astrocytes remain poorly understood.
- Whether astrocyte subtypes that differ electrophysiologically require distinct opsin or DREADD variants for physiologically valid manipulation has not been addressed.

---

### Connections & keywords

- **Key citations**: Kofuji and Newman (2004) — Kir4.1 and K+ buffering; Tang et al. (2009) — hippocampal astrocyte passive conductance; Petravicz et al. (2008) — IP3R2 and Ca2+ signalling; Mederos et al. (2019) — melanopsin vs. ChR2 in astrocytes; Murphy-Royal et al. (2020) — glial syncytium, LTP, and stress; Poskanzer and Yuste (2016) — Arch hyperpolarisation and Ca2+ transients; Boyden et al. (2005) — optogenetics; Roth (2016) — DREADDs; Verkhratsky and Nedergaard (2018) — astrocyte physiology textbook; Bayraktar et al. (2020) — single-cell transcriptomics of cortical astrocyte layers; Rurak et al. (2020) — developmental TRAPseq of cortical astrocyte gene expression; Liddelow et al. (2017) — A1/A2 reactive astrocyte classification; Araque et al. (2014) — gliotransmitters and synaptic modulation.
- **Named models or frameworks**: tripartite synapse, glial syncytium, K+ spatial buffering model, reactive astrogliosis (A1/A2 classification), optogenetics (ChR2, halorhodopsin, Arch, Arch-T, melanopsin, ChETA, SFO, CatCh), DREADDs (hM3Dq, hM4Di), TRAPseq.
- **Brain regions**: hippocampus (CA1, stratum radiatum, stratum oriens, stratum pyramidale, stratum lucidum, dentate gyrus), neocortex, somatosensory cortex, cerebellum, optic nerve, spinal cord, ventral tegmental area, thalamus, striatum, olfactory bulb, retina.
- **Keywords**: astrocyte electrophysiology, ion channel heterogeneity, potassium spatial buffering, Kir4.1, two-pore domain K+ channels (TREK1, TWIK1), voltage-gated sodium channels (Nav), calcium signalling, IP3R2, gliotransmission, optogenetics in astrocytes, DREADDs in astrocytes, glial syncytium, reactive astrogliosis, astrocyte subtype diversity.
