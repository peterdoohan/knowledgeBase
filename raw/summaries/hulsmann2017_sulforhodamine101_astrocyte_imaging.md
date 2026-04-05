---
source_file: hulsmann2017_sulforhodamine101_astrocyte_imaging.md
title: Limitations of Sulforhodamine 101 for Brain Imaging
authors: Swen Hülsmann, Liya Hagos, Heike Heuer, Christian Schnell
year: 2017
journal: Frontiers in Cellular Neuroscience
paper_type: empirical
contribution_type: methodological
---

### One-line summary

Sulforhodamine 101 (SR101), widely used as an astrocyte-specific marker, is neither fully cell-type specific nor physiologically inert, and its excitatory side effects may be mediated by competition with sulfated neurosteroid uptake via OATP1C1.

---

### Background & motivation

SR101 became the dominant tool for labelling astrocytes in living brain tissue following a 2004 paper by Nimmerjahn et al. that described it as an astrocyte-specific marker in the neocortex. Its uptake mechanism was initially unknown, and its physiological effects were assumed to be negligible. This paper reviews accumulating evidence that SR101 labels oligodendrocytes in addition to astrocytes, and that it can induce neuronal hyperexcitability including long-term potentiation (LTP) and seizure-like activity, raising concerns about the validity of experiments performed in its presence.

---

### Methods

- **Study type**: Hypothesis and theory/review article with original experimental data.
- **Experimental data**: Two-photon imaging in acute hippocampal brain slices from transgenic mice (TgN(hGFAP-EGFP) and TgN(PLP-GFP)) and OATP1C1 knockout mice.
- **SR101 labelling protocols**: Varied concentration (1–165 µM), temperature (room temperature vs. 34°C), and incubation duration to assess cell-type specificity.
- **Pharmacological manipulations**: Application of carbenoxolone (CBX, gap junction blocker), MK-571 (ABC-transporter blocker), Probenecid, levothyroxine (T4), and sulfated neurosteroids (DHEAS, estrone-3-sulfate, allopregnanolone sulfate) to probe SR101 uptake mechanisms.
- **Analysis**: Fluorescence intensity quantification via threshold-based pixel analysis (ImageJ); statistical comparisons using Mann-Whitney Rank Sum Test, t-test, and ANOVA (Holm-Sidak method).
- **Literature synthesis**: Narrative review of publications reporting cell-type specificity issues and excitatory side effects.

---

### Key findings

- SR101 labels oligodendrocytes in addition to astrocytes; in cortex, over 30% of SR101-positive cells were oligodendrocytes (Hill and Grutzendler, 2014); ~45% of SR101-positive cells did not express GFAP-EGFP in hippocampus (Schnell et al., 2012).
- SR101 uptake into astrocytes is mediated by the organic anion transporting polypeptide OATP1C1 (SLCO1C1), a thyroid hormone transporter; this was confirmed using OATP1C1 knockout mice and competitive substrates (T4, MK-571, Probenecid).
- Neurons are also transiently labelled by SR101 but extrude it rapidly via an ABC-transporter–dependent mechanism; neuronal labelling at 165 µM/room temperature persists in OATP1C1 knockout mice even with CBX, indicating an independent, unknown uptake route.
- SR101 induces neuronal hyperexcitability at concentrations as low as 1 µM, including LTP outlasting the application period; in vivo, epileptic and seizure-like activity have been reported at 10–100 µM.
- Sulfated neurosteroids (allopregnanolone sulfate at 100 µM) significantly reduced both SR101 intensity (p = 0.032, n = 5 slices/3 mice) and the number of SR101-positive cells (p = 0.040), supporting the hypothesis that SR101 competes with neurosteroid uptake via OATP1C1.
- The authors hypothesise that displaced sulfated neurosteroids (which modulate NMDA receptors and GABA-A receptors) account for SR101-induced hyperexcitability.

---

### Computational framework

Not applicable. The paper is purely empirical and methodological, with no formal computational framework. The results constrain pharmacological and cell-biological models of organic anion transporter function and glial cell identification strategies, but no quantitative modelling is performed.

---

### Prevailing model of the system under study

The paper pushes against the prevailing assumption — established by Nimmerjahn et al. (2004) — that SR101 is a specific, non-perturbing astrocyte marker suitable for both in vivo and slice preparations. The baseline model held that SR101 was taken up selectively by astrocytes via an active transport mechanism (later identified as OATP1C1), that it spread within the astroglial syncytium via gap junctions, and that it did not alter the physiological properties of brain cells. This made it an attractive alternative to genetic labelling approaches (e.g., GFAP-EGFP mice), particularly for electrophysiological experiments requiring live cell identification.

---

### What this paper contributes

The paper systematically dismantles the assumption of SR101 specificity and inertness on two fronts. First, it provides mechanistic clarification: OATP1C1 mediates astrocyte (and oligodendrocyte) labelling, but neurons use an independent, unidentified uptake route, and their apparent selectivity reflects differential efflux rather than differential uptake. Second, it proposes a testable mechanistic hypothesis for the excitatory side effects: competition of SR101 with sulfated neurosteroids at OATP1C1 leads to elevated extracellular neurosteroid levels, which potentiate NMDA receptors and inhibit GABA-A receptors. This hypothesis is supported by neurosteroid-blockade data but not yet fully proven. Practically, the paper establishes that SR101 use requires additional cell-type verification (electrophysiology, post-hoc immunohistochemistry) and that experiments should minimise SR101 concentration and ideally perform labelling after the main experiment.

---

### Brain regions & systems

- **Hippocampus (CA1)** — primary experimental site; used to characterise OATP1C1-dependent astrocyte labelling, neuronal labelling in knockout mice, and LTP induction.
- **Neocortex** — cited for in vivo labelling studies showing oligodendrocyte co-labelling and seizure induction.
- **Brainstem** — highlighted as a region where SR101 labelling is weaker and less specific, attributed to lower regional OATP1C1 expression.
- **Locus coeruleus** — noted as a region where high-concentration SR101 at room temperature preferentially labels neurons.
- **Glial syncytium (astrocyte-oligodendrocyte gap junction networks)** — relevant to the spread of SR101 from astrocytes to oligodendrocytes via Cx32/Cx47 gap junctions.

---

### Mechanistic insight

The paper does not meet the full bar for mechanistic insight at Marr's three levels. It presents a pharmacological hypothesis (an algorithm-level proposal about OATP1C1 competition with neurosteroids) and supports it with blocking experiments, but it does not provide direct neural recordings linking the proposed molecular mechanism to measured electrophysiological changes in the same preparation. The excitatory side effect data (LTP induction, seizure-like activity) come from separate published studies, and the neurosteroid hypothesis is tested only at the level of SR101 uptake blockade, not via downstream electrophysiological readout. The paper's main mechanistic contribution is identifying OATP1C1 as the transporter responsible for astrocyte labelling, supported by genetic knockout validation.

---

### Limitations & open questions

- The neurosteroid hypothesis for SR101-induced hyperexcitability remains to be directly tested by measuring extracellular neurosteroid levels during SR101 application and correlating these with electrophysiological changes.
- The independent neuronal SR101 uptake mechanism (operating independently of OATP1C1 and gap junctions) is unidentified.
- Variability in excitatory side effects across laboratories may reflect differences in endogenous neurosteroid levels (e.g., sex, estrus cycle, stress), but this has not been tested systematically.
- The functional consequences of oligodendrocyte labelling by SR101 are unknown.
- It is unclear whether SR101-induced perturbations affect calcium imaging or other functional measurements that are commonly performed using SR101 as a counterstain.

---

### Connections & keywords

**Key citations**:
- Nimmerjahn et al. (2004) — original paper establishing SR101 as an astrocyte marker
- Schnell et al. (2012) — active SR101 uptake and OATP1C1 pharmacology
- Schnell et al. (2015) — OATP1C1 as the responsible transporter; knockout validation
- Hagos and Hülsmann (2016) — SR101 labelling of oligodendrocytes via OATP1C1
- Hill and Grutzendler (2014) — in vivo oligodendrocyte labelling by SR101
- Kang et al. (2010) — SR101-induced LTP and hyperexcitability
- Rasmussen et al. (2016) — SR101-induced cortical seizure-like activity

**Named models or frameworks**:
- OATP1C1 (organic anion transporting polypeptide 1C1 / SLCO1C1) transporter model
- Neurosteroid competition hypothesis

**Brain regions**:
- Hippocampus (CA1)
- Neocortex
- Brainstem
- Locus coeruleus
- Astrocyte-oligodendrocyte gap junction syncytium

**Keywords**:
- Sulforhodamine 101 (SR101)
- Astrocyte marker specificity
- OATP1C1 (SLCO1C1) organic anion transporter
- Oligodendrocyte co-labelling
- Neurosteroid competition
- Two-photon brain slice imaging
- Neuronal hyperexcitability
- Long-term potentiation (LTP) artefact
- Gap junction dye coupling
- Thyroid hormone transporter
- Glia identification methods
- Methodological pitfalls neuroscience
