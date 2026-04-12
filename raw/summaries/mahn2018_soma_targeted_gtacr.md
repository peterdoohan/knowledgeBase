---
source_file: "mahn2018_soma_targeted_gtacr.md"
paper_id: "mahn2018_soma_targeted_gtacr"
title: "High-efficiency optogenetic silencing with soma-targeted anion-conducting channelrhodopsins"
authors: "Mathias Mahn, Lihi Gibor, Pritish Patil, Katayun Cohen-Kashi Malina, Shir Oring, Yoav Printz, Rivka Levy, Ilan Lampl, Ofer Yizhar"
year: 2018
journal: "Nature Communications"
paper_type: "empirical"
contribution_type: "methodological"
species: ["mouse", "rat"]
methods: ["optogenetics", "electrophysiology"]
brain_regions: ["prefrontal_cortex", "medial_prefrontal_cortex", "nucleus_accumbens", "amygdala", "basolateral_amygdala"]
keywords: ["high", "efficiency", "optogenetic", "silencing", "soma", "targeted", "anion", "conducting", "channelrhodopsins"]
---

### One-line summary

Soma-targeted variants of the anion-conducting channelrhodopsin GtACR2 achieve high-efficiency optogenetic neuronal silencing with improved membrane targeting, reduced axonal excitation, and lower light power requirements compared to existing inhibitory opsins.

### Background & motivation

Optogenetic silencing tools enable time-resolved functional interrogation of defined neuronal populations, but existing ion-pumping rhodopsins (halorhodopsin, archaerhodopsin) require high light power and can cause tissue heating and phototoxicity. Anion-conducting channelrhodopsins (ACRs) from Guillardia theta (GtACRs) offer high single-channel conductance and favorable photon-ion stoichiometry, but suffer from poor membrane targeting in mammalian cells and can cause transient axonal excitation due to depolarized chloride reversal potential in axons. This study addresses these limitations through enhanced membrane targeting and subcellular compartmentalization.

### Methods

- **In vitro electrophysiology**: Whole-cell patch-clamp recordings from cultured rat hippocampal neurons and acute mouse brain slices expressing GtACR variants
- **Viral vectors**: AAV-mediated expression of GtACR2, engineered ACRs (iC++, iChloC), and soma-targeted variants (stGtACR2, stGtACR2-PEST)
- **Molecular engineering**: Fusion of GtACR2 with ER export/trafficking signals (eGtACR2) or soma-targeting motif from Kv2.1 potassium channel (stGtACR2)
- **In vivo electrophysiology**: Extracellular recordings with optrode drives in awake, behaving mice during optogenetic silencing of mPFC neurons
- **Behavioral assays**: Fear conditioning and extinction paradigm with BLA silencing using stGtACR2
- **Histology**: c-Fos immunolabeling to quantify neuronal activity suppression

### Key findings

- GtACR2 produces significantly larger stationary photocurrents (628.5 ± 61.8 pA) compared to engineered ACRs iC++ (330.2 ± 37.9 pA) and iChloC (136.3 ± 21.4 pA) in cultured hippocampal neurons
- GtACR2 activation triggers antidromic spikes in axons due to depolarized chloride reversal potential in this compartment; this effect is also observed with iC++ but not iChloC
- Overexpression of KCC2 chloride extruder in cultured neurons reduces GtACR2-mediated antidromic spiking from 76% to 41% of trials, supporting the hypothesis that axonal chloride concentration drives excitatory effects
- Soma-targeted GtACR2 (stGtACR2) shows 2.6-fold increase in stationary photocurrents compared to untargeted GtACR2 in acute brain slices, with average photocurrents exceeding 2 nA at −35 mV
- stGtACR2 significantly reduces antidromic spike probability in vivo compared to GtACR2 (3% vs 19% of units when illuminating NAc-projecting axons)
- In vivo extracellular recordings show stGtACR2 achieves significantly higher silencing efficacy than GtACR2 at lower light powers (52-61% vs 21-43% of units showing significant firing rate reduction)
- c-Fos labeling demonstrates stGtACR1 and stGtACR2 produce significant activity suppression in the illuminated cortex, while eNpHR3.0 does not achieve significant suppression under comparable conditions
- Temporally precise BLA inhibition during CS presentation in fear extinction training impairs extinction learning (stGtACR2: 54 ± 6% freezing vs control: 28 ± 4% during early recall)

### Computational framework

Not applicable. This is a methodological paper focused on developing and validating improved optogenetic tools. The paper does not propose or test a computational model of neural computation. However, the findings constrain how inhibitory optogenetic tools can be used to perturb neural circuits, with implications for interpreting perturbation-based causal inference in systems neuroscience.

### Prevailing model of the system under study

The prevailing understanding was that anion-conducting channelrhodopsins (ACRs) provide efficient optogenetic inhibition due to their high conductance and favorable photon-ion stoichiometry. However, their utility in mammalian systems was limited by two factors: (1) poor membrane targeting leading to intracellular protein accumulation, and (2) axonal excitation due to chloride conductance in compartments with depolarized chloride reversal potential. The chloride reversal potential in axons was assumed to be more depolarized than in soma/dendrites due to absence of the KCC2 chloride extruder from axonal membranes. Existing ion-pumping rhodopsins (halorhodopsin, archaerhodopsin) were the standard tools for optogenetic silencing but required high light power and caused tissue heating/phototoxicity.

### What this paper contributes

This paper establishes that soma-targeted GtACR variants (stGtACR1, stGtACR2) overcome the key limitations of non-targeted ACRs and outperform existing inhibitory opsins. The study demonstrates that: (1) fusion with the Kv2.1 soma-targeting motif dramatically improves membrane localization and increases photocurrents 2.6-fold; (2) soma-targeting reduces axonal excitation from 19% to 3% of units in vivo; (3) stGtACRs achieve widespread cortical silencing at light powers an order of magnitude lower than ion pumps; (4) the tool enables temporally precise behavioral manipulations, as demonstrated by impaired fear extinction when BLA activity is inhibited during CS presentation. These findings establish stGtACRs as the current state-of-the-art for optogenetic neuronal silencing in mammalian systems.

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)** — primary site for in vivo silencing validation using extracellular recordings and c-Fos labeling; demonstrates widespread cortical silencing efficacy
- **Basolateral amygdala (BLA)** — target region for behavioral demonstration; temporally precise inhibition during fear extinction training impairs extinction learning
- **Nucleus accumbens (NAc)** — target for testing antidromic spiking in projection neurons; light delivery to distal axons reveals differences between GtACR2 and stGtACR2
- **Cultured hippocampal neurons** — primary in vitro model for characterizing photocurrents, antidromic spiking, and KCC2 effects on chloride homeostasis
- **Cortico-cortical projection neurons** — used to assess axonal neurotransmitter release and antidromic spike propagation in acute slices

### Mechanistic insight

This paper provides mechanistic insight at multiple levels, though it does not fully satisfy the high bar for Marr's three levels as it focuses on tool development rather than neural computation.

**Algorithmic level**: The paper establishes the biophysical mechanism by which ACRs inhibit neuronal activity: light-gated chloride conductance clamps membrane potential toward the chloride reversal potential. The study reveals that this same mechanism can paradoxically excite axons when the chloride reversal potential is depolarized relative to the action potential threshold. The soma-targeting strategy algorithmically restricts the chloride conductance to compartments where the reversal potential is hyperpolarizing.

**Implementational level**: The paper identifies the molecular implementation: KCC2 expression maintains low intracellular chloride in somatodendritic compartments but is absent from axons, creating a compartmentalized chloride gradient. The soma-targeting motif from Kv2.1 physically restricts GtACR2 protein to the somatodendritic membrane, preventing accumulation in axons where it would cause excitation.

The paper does not address the computational level (what problem the brain is solving) as it is a methodological tool development study.

### Limitations & open questions

- The study notes that transient light onset-evoked antidromic spikes may still occur with stGtACR2 at high light powers, requiring careful calibration of light delivery protocols
- Rebound excitation following prolonged inhibition (potentially due to release of synaptic depression) remains a caveat for any optogenetic silencing experiment
- The effective addressable brain volume is constrained by light power requirements; novel light delivery methods (e.g., tapered fibers) may help overcome this limitation
- The study does not fully characterize the long-term stability of stGtACR2 expression or potential photobleaching effects during extended illumination
- The molecular mechanism by which the Kv2.1 targeting motif restricts protein to the soma is not fully elucidated
- The paper raises the possibility of combining stGtACR2 with red-shifted tools for dual-color experiments, but this is not directly tested

### Connections & keywords

**Key citations**:
- Govorunova et al. 2015 (GtACR1/GtACR2 discovery)
- Gradinaru et al. 2010 (trafficking signals for optogenetic tools)
- Mattis et al. 2011 (comparative analysis of microbial opsins)
- Baker et al. 2016 (soma-targeted channelrhodopsin)
- Sierra-Mercado et al. 2011 (BLA inhibition and fear extinction)

**Named models or frameworks**:
- GtACR1/GtACR2 (naturally-occurring anion-conducting channelrhodopsins)
- stGtACR1/stGtACR2 (soma-targeted variants)
- eGtACR2 (ER export signal enhanced variant)
- iC++ and iChloC (engineered ACRs for comparison)
- eNpHR3.0 and eArch3.0 (ion pump-based inhibitory opsins for comparison)

**Brain regions**:
- Medial prefrontal cortex (mPFC)
- Basolateral amygdala (BLA)
- Nucleus accumbens (NAc)
- Hippocampus (cultured neurons)
- Cortico-cortical projections

**Keywords**:
optogenetics, channelrhodopsin, GtACR2, neuronal silencing, soma targeting, anion channel, chloride conductance, antidromic spiking, fear extinction, basolateral amygdala, medial prefrontal cortex, KCC2, Kv2.1 trafficking motif