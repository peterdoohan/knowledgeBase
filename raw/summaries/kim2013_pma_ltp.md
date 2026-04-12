---
source_file: kim2013_pma_ltp.md
paper_id: kim2013_pma_ltp
title: "Phorbol 12-Myristate 13-Acetate Enhances Long-Term Potentiation in the Hippocampus through Activation of Protein Kinase C δ and ε"
authors:
  - "Eung Chang Kim"
  - "Myeong Jong Lee"
  - "Sang Yep Shin"
  - "Geun Hee Seol"
  - "Seung Ho Han"
  - "Jaeyong Yee"
  - "Chan Kim"
  - "Sun Seek Min"
year: 2013
journal: "Korean Journal of Physiology and Pharmacology"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
brain_regions:
  - hippocampus
  - hippocampus_ca1
frameworks:
  - reinforcement_learning
keywords:
  - long_term_potentiation
  - protein_kinase_c
  - pkc
  - phorbol_ester
  - pma
  - nmda_receptor
  - hippocampus_ca1
  - synaptic_plasticity
  - theta_burst_stimulation
  - nmdar_trafficking
  - novel_pkc_isoforms
  - phorbol
  - myristate
  - acetate
  - enhances
  - long
  - term
  - potentiation
  - hippocampus
  - through
---

### One-line summary

PMA enhances hippocampal LTP induction via activation of PKCδ and/or PKCε in a manner dependent on NMDA receptor activity.

---

### Background & motivation

Protein kinase C (PKC) has long been implicated in synaptic plasticity and LTP in the hippocampus, but the field lacked clarity on which specific PKC isoforms mediate the effects of the phorbol ester PMA on LTP induction. PMA is a stable diacylglycerol analogue and canonical PKC activator, and prior work had shown it could influence spine morphology and ERK activation, but the isoform specificity of its LTP-facilitating action was unknown. This study aimed to identify the responsible isoforms and to confirm that the effect depends on NMDAR activation.

---

### Methods

- **Subjects**: Male C57BL/6N mice, 3–5 weeks old.
- **Preparation**: Acute hippocampal slices (400 µm, horizontal); extracellular field recordings in CA1 stratum radiatum; Schaffer collateral stimulation.
- **LTP induction**: Single episode of theta-burst stimulation (TBS; 8 bursts × 4 pulses at 100 Hz, 200 ms inter-burst interval).
- **Drug treatments**: PMA applied ≥1 h before TBS at 100 nM, 200 nM, and 1 µM; inhibitors tested: Ro 31-8220 (non-selective PKC inhibitor, 10 µM), rottlerin (selective PKCδ inhibitor, 1 µM), TAT-εV1-2 peptide (PKCε inhibitor, 500 nM), and DL-APV (NMDAR antagonist, 50 µM).
- **Measurements**: fEPSP slope as percentage of baseline, averaged 58–60 min post-TBS; paired-pulse facilitation (PPF) at multiple inter-stimulus intervals to assess presynaptic function.
- **Analysis**: Student's t-test and one-way ANOVA with Fisher's PLSD post hoc test.

---

### Key findings

- PMA dose-dependently enhanced LTP magnitude: vehicle 130 ± 5.15%; PMA 100 nM: 142 ± 4.38%; 200 nM: 146 ± 5.51% (p < 0.05); 1 µM: 164 ± 11.14% (p < 0.01).
- PMA did not affect baseline fEPSP amplitude, indicating no general change in basal synaptic transmission.
- The non-selective PKC inhibitor Ro 31-8220 (10 µM) blocked PMA-facilitated LTP (123 ± 9.1% vs. 146 ± 5.5% with PMA alone).
- The selective PKCδ inhibitor rottlerin (1 µM) blocked facilitation (121 ± 6.0%).
- The PKCε inhibitor TAT-εV1-2 (500 nM) blocked facilitation (125 ± 4.9%).
- The NMDAR antagonist DL-APV (50 µM) eliminated PMA-enhanced LTP (110 ± 7.13% vs. 164 ± 11.14% for 1 µM PMA alone; p < 0.001).
- PPF ratios were not significantly different between PMA-treated and vehicle-treated slices, suggesting PMA's effects are primarily postsynaptic.

---

### Computational framework

Not applicable. This is a pharmacological electrophysiology study with no explicit computational framework. The results constrain models of PKC-mediated modulation of NMDAR trafficking and synaptic plasticity, and could inform reinforcement learning or Hebbian synaptic plasticity models that require specification of the molecular signalling cascades underlying LTP.

---

### Prevailing model of the system under study

Prior to this paper, the field understood that PKC activation is necessary for hippocampal LTP maintenance and induction, and that PMA (as a pan-PKC activator via its mimicry of diacylglycerol) can potentiate synaptic strength. Multiple PKC isoforms were known to be expressed in hippocampus (including classical isoforms α, β, γ and novel isoforms δ, ε, η, θ), but the isoform specificity of PMA's LTP-facilitating action was unresolved. The atypical isoform PKMζ had emerged as important for late LTP maintenance via AMPAR trafficking. The broader assumption was that PKC facilitates LTP by promoting NMDAR trafficking to the plasma membrane and modulating NMDAR gating, with CaMKII as a downstream mediator.

---

### What this paper contributes

This paper narrows the previously non-specific attribution of PMA's LTP effects to PKC in general, demonstrating that it is specifically PKCδ and/or PKCε (novel, calcium-independent isoforms) that mediate PMA-facilitated LTP induction in CA1. It also confirms that NMDAR activity is required for this facilitation, linking these novel PKC isoforms to the canonical NMDAR-dependent plasticity cascade. Before this paper, one could only speculate about which isoforms were relevant; the isoform-specific pharmacology here provides direct evidence ruling out the classical isoforms as primary mediators of PMA's LTP-facilitating effect in this preparation.

---

### Brain regions & systems

- **Hippocampus CA1 (stratum radiatum / Schaffer collateral–CA1 synapse)** — primary site of LTP recording and the locus of all reported effects.
- **Hippocampus CA1 pyramidal cells** — postsynaptic neurons whose synaptic strength (fEPSP slope) is the dependent measure.

---

### Mechanistic insight

This paper partially meets the bar. It presents a pharmacological dissection of the algorithm (PKCδ/ε → NMDAR-dependent LTP facilitation) and uses neural data (field recordings from hippocampal slices) to support these specific isoforms over others. However, it does not directly measure the downstream molecular events (e.g., NMDAR trafficking, CaMKII phosphorylation) proposed as the mechanistic intermediaries, nor does it address implementational details such as specific subcellular localisation of PKCδ/ε or their direct substrates in this preparation.

- **Computational**: The hippocampus must strengthen recently co-active synapses in an activity-dependent manner (Hebbian plasticity / associative memory).
- **Algorithmic**: Activation of PKCδ and PKCε (triggered here by PMA acting as a diacylglycerol analogue) facilitates NMDAR-dependent LTP, plausibly via increased NMDAR trafficking to the synapse and/or CaMKII autophosphorylation, lowering the threshold for LTP induction.
- **Implementational**: The paper identifies PKCδ and PKCε as the relevant isoforms at the CA1 synapse, but does not resolve their subcellular localisation, direct phosphorylation targets, or downstream cascade at the biophysical level.

---

### Limitations & open questions

- Only two novel PKC isoforms were pharmacologically blocked; other isoforms activated by PMA (e.g., PKCη, PKCθ) were not assessed and may also contribute.
- The study uses a single episode of TBS, which induces relatively modest LTP; generalisability to stronger or more naturalistic stimulation protocols is unclear.
- The mechanistic intermediaries (NMDAR trafficking, CaMKII phosphorylation, AMPAR insertion) were not directly measured — they are inferred from prior literature.
- PPF data suggest presynaptic changes are unlikely but are not definitive; postsynaptic mechanisms remain to be fully characterised.
- Only male mice of a single strain and narrow age range were used, limiting generalisability.
- The use of rottlerin as a selective PKCδ inhibitor has been questioned in the literature regarding off-target effects.

---

### Connections & keywords

**Key citations**:
- Lan et al. (2001) *Nat Neurosci* — PKC modulates NMDAR trafficking and gating
- Yan et al. (2011) *J Biol Chem* — PKC promotes NMDAR trafficking via CaMKII autophosphorylation
- Sacktor (2008) *Prog Brain Res* — PKMζ and late LTP maintenance
- Goldin & Segal (2003) *Eur J Neurosci* — PKC/ERK and dendritic spine plasticity in hippocampal neurons
- Malenka et al. (1986) *Nature* — phorbol ester potentiation of hippocampal synaptic transmission

**Named models or frameworks**:
- Theta-burst stimulation (TBS) LTP induction protocol
- Paired-pulse facilitation (PPF) as assay of presynaptic function

**Brain regions**:
- Hippocampus CA1
- Schaffer collateral pathway

**Keywords**: long-term potentiation, protein kinase C, PKCδ, PKCε, phorbol ester, PMA, NMDA receptor, hippocampus CA1, synaptic plasticity, theta-burst stimulation, NMDAR trafficking, novel PKC isoforms
