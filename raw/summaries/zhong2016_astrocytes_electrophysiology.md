---
source_file: "zhong2016_astrocytes_electrophysiology.md"
paper_id: "zhong2016_astrocytes_electrophysiology"
title: "Electrophysiological behavior of neonatal astrocytes in hippocampal stratum radiatum"
authors: "Shiying Zhong, Yixing Du, Conrad M. Kiyoshi, Baofeng Ma, Catherine C. Alford, Qi Wang, Yongjie Yang, Xueyuan Liu, Min Zhou"
year: 2016
journal: "Molecular Brain"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
methods: ["electrophysiology"]
brain_regions: ["hippocampus_ca1"]
keywords: ["astrocytes", "electrophysiology", "gap_junctions", "potassium_homeostasis", "kir4_1", "developmental_neurobiology", "hippocampus", "passive_astrocytes", "variably_rectifying_astrocytes", "meclofenamic_acid", "neonatal_development", "syncytial_network", "twik_1", "trek_1", "electrophysiological", "behavior", "neonatal", "hippocampal", "stratum", "radiatum"]
---

### One-line summary

Neonatal astrocytes (P1-3) in hippocampal stratum radiatum exhibit distinct electrophysiological properties from mature astrocytes, characterized by rectifying K+ conductances, discrete gap junction coupling, and ~50% reduced K+ uptake capacity.

### Background & motivation

Neonatal astrocytes play critical roles in synaptogenesis, myelination, and neuronal circuit establishment during postnatal brain development. While their morphological and gene expression changes during development are well documented, the extent to which neonatal astrocytes differ electrophysiologically from mature astrocytes remained poorly defined. This study aimed to characterize the functional properties of neonatal astrocytes during the postnatal day 1-3 (P1-3) dormant period to understand their unique physiological identity.

### Methods

- **Animal models**: Wild-type C57BL/6J mice, BAC-ALDH1L1-eGFP transgenic mice (for astrocyte identification), and TWIK-1/TREK-1 double gene knockout (dKO) mice
- **Age range**: Postnatal day 1-3 (P1-3) for neonatal astrocytes; P21-25 for mature astrocyte comparisons
- **Cell identification**: ALDH1L1-eGFP expression and sulforhodamine 101 (SR101) staining; GFAP immunohistochemistry for confirmation
- **Electrophysiology**: Whole-cell patch-clamp recordings in hippocampal stratum radiatum; dual patch recording for gap junction coupling analysis
- **Pharmacological manipulations**: 100 μM meclofenamic acid (MFA) for gap junction inhibition; 100 μM BaCl2 for Kir4.1 inhibition
- **K+ uptake assay**: Intracellular K+ substituted with Na+; current-clamp recording with incremental holding current durations to drive VM to -75 mV
- **Data analysis**: Coupling coefficient calculation; rectification index (RI); Goldman-Hodgkin-Katz (GHK) equation for intracellular K+ concentration estimation

### Key findings

- Neonatal astrocytes exhibit a more negative resting membrane potential (-85 mV) compared to mature astrocytes (-80 mV; P < 0.05)
- Two distinct electrophysiological phenotypes were identified: variably rectifying astrocytes (VRAs, 92%) and passive astrocytes (PAs, 8%); PAs emerged from P2 and increased to 20.83% by P3
- Input resistance was significantly higher in VRAs (45.4 ± 43.2 MΩ) compared to PAs in neonatal (14.3 ± 4.9 MΩ) and mature (10.3 ± 4.9 MΩ) astrocytes (P < 0.05)
- Gap junction inhibition with 100 μM MFA converted all PAs to VRAs, demonstrating that the passive phenotype is caused by gap junction coupling masking intrinsic rectifying K+ conductances, not by intrinsic leak channels as in mature astrocytes
- Rectification index (RI) increased 3-fold in VRAs and 6-fold in PAs after MFA treatment (P < 0.05), and Rin increased from 42.0 ± 41.9 MΩ to 223.7 ± 100.3 MΩ (P < 0.05)
- Neonatal astrocytes predominantly express voltage-gated outward transient K+ current (IKa) and delayed rectifying K+ current (IKd), but lack detectable voltage-gated inward Na+ currents (INa), unlike NG2 glia
- Inward K+ conductance (IKin) showed characteristic inward rectification with Vrev of -79.7 mV; Ba2+-sensitive component matched Kir4.1 activation kinetics, but Ba2+-insensitive currents showed strong outward rectification suggesting additional leak K+ channels
- In TWIK-1/TREK-1 double knockout mice, the Ba2+-insensitive leak conductance remained unchanged, indicating these K2P channels contribute minimally to the leak conductance
- Dual patch recording revealed electrical coupling in 74% (14/19) of neonatal astrocyte pairs with highly variable coupling coefficients (22.3-25.5%); PA-PA homotypic pairs showed higher coupling rates (92.3%) than VRA-VRA pairs (60%)
- Coupling coefficients varied substantially among recording pairs but showed no association with cell-to-cell distance
- Gap junction channels showed linear gating properties (CC values varied insignificantly across voltages from -220 to +40 mV; P > 0.05)
- K+ uptake capacity in neonatal astrocytes was ~50% less than mature astrocytes; net intracellular K+ accumulation after 5-second holding pulses was 9.62 ± 1.90 mM in neonatal vs. 20.73 ± 6.01 mM in mature astrocytes (P < 0.05)

### Computational framework

Not applicable. This is an empirical study using electrophysiological and pharmacological approaches. However, the Goldman-Hodgkin-Katz (GHK) equation is used to calculate intracellular K+ concentrations from reversal potentials, providing a biophysical framework for understanding ion fluxes across the astrocyte membrane.

### Prevailing model of the system under study

Prior to this study, the prevailing model held that astrocytes throughout development were electrophysiologically passive, characterized by high expression of leak K+ channels (particularly Kir4.1) that maintain a stable resting membrane potential around -80 mV. Mature astrocytes were known to form an extensive gap junction-coupled syncytium that enables efficient spatial buffering of K+ ions. The assumption was that neonatal astrocytes were simply immature versions of adult astrocytes, gradually acquiring passive properties and gap junction coupling as they matured. Some previous reports had described voltage-gated K+, Na+, and Ca2+ conductances in early postnatal astroglia, but a systematic analysis was lacking due to the absence of reliable markers for live astrocyte identification.

### What this paper contributes

This paper fundamentally revises the understanding of neonatal astrocyte physiology by demonstrating that they are not merely immature versions of adult astrocytes but represent a distinct electrophysiological stage with unique properties:

1. **Rectifying vs. passive conductances**: Neonatal astrocytes predominantly express voltage-gated rectifying K+ conductances (IKa, IKd, IKin) rather than the linear passive conductances of mature astrocytes. The "passive" phenotype observed in some neonatal astrocytes is an artifact of gap junction coupling masking intrinsic rectifying conductances, fundamentally different from the intrinsic passive conductance of mature astrocytes.

2. **Distinct resting membrane potential**: Neonatal astrocytes maintain a more negative resting potential (-85 mV vs -80 mV in mature astrocytes), attributed to their unique ion channel expression profile and low Na+ permeability.

3. **Discrete gap junction coupling**: Unlike the extensive syncytium of mature astrocytes, neonatal astrocytes show discrete, variable cell-to-cell coupling (74% of pairs) that emerges progressively during P1-3. This suggests newly generated astrocytes are uncoupled at birth and establish connections gradually.

4. **Deficient K+ homeostasis**: The low density of leak K+ conductance and discrete gap junction coupling result in ~50% reduced K+ uptake capacity compared to mature astrocytes, suggesting limited ability to buffer extracellular K+ during neuronal activity.

5. **Diagnostic distinction from NG2 glia**: The absence of voltage-gated Na+ currents in neonatal astrocytes provides a clear electrophysiological criterion to distinguish them from NG2 glia, which express INa.

These findings establish that neonatal astrocytes represent a functionally distinct developmental stage with specialized physiological properties that may be essential for their roles in synaptogenesis, circuit formation, and brain development, rather than simply being immature versions of adult astrocytes.

### Brain regions & systems

- **Hippocampal stratum radiatum (CA1 region)** — primary site of electrophysiological recordings and astrocyte characterization; site where neonatal astrocytes were identified and studied for ion channel expression, gap junction coupling, and K+ uptake capacity

### Mechanistic insight

This paper provides substantial mechanistic insight into neonatal astrocyte physiology by combining electrophysiological characterization with pharmacological manipulations to dissect the molecular mechanisms underlying distinct developmental phenotypes:

**Computational level**: The brain must maintain appropriate extracellular K+ homeostasis during development while establishing neuronal circuits. Neonatal astrocytes solve this problem with a distinct strategy from mature astrocytes, prioritizing cell-autonomous voltage-gated K+ handling over spatial buffering through gap junction networks.

**Algorithmic level**: 
- Neonatal astrocytes implement a variably rectifying algorithm through coordinated expression of IKa (outward transient), IKd (delayed rectifying), and IKin (inward rectifying) K+ conductances, with a 6-fold excess of outward to inward current density
- Gap junction coupling creates a "masking" algorithm where electrical coupling between cells linearizes the overall I-V relationship by shunting intrinsic rectifying conductances, creating the false appearance of passive behavior in ~8% of neonatal astrocytes
- The absence of voltage-gated Na+ currents provides a diagnostic algorithmic signature distinguishing astrocytes from NG2 glia

**Implementational level**:
- **Molecular machinery**: Kir4.1 channels (inward rectifier) contribute to the resting potential but are not solely responsible; Ba2+-sensitive currents match Kir4.1 kinetics while Ba2+-insensitive currents show GHK-type outward rectification suggesting additional unidentified leak K+ channels
- **Gap junction proteins**: Electrical coupling occurs through connexin-based gap junctions (sensitive to meclofenamic acid), with linear gating properties and variable coupling coefficients (22-25%) that are independent of intercellular distance
- **Channel absence**: TWIK-1 and TREK-1 two-pore domain K+ channels do not contribute to leak conductance in neonatal astrocytes (demonstrated in dKO mice)

The paper thus provides a multi-level mechanistic account linking molecular channel expression to cellular electrophysiological phenotypes to network-level properties, with clear experimental support at each level.

### Limitations & open questions

- Stage-specific and origin-specific markers for differentiating astrocytes from different sources (radial glia, subventricular zone progenitors, NG2 glia, local proliferation) remain unavailable; some neonatal astrocyte subpopulations may have been excluded from analysis
- The identity of the Ba2+-insensitive leak K+ conductance that shows GHK-type outward rectification remains unknown; TWIK-1 and TREK-1 were excluded but additional leak K+ channels remain to be identified
- The functional implications of the ~50% reduced K+ uptake capacity for neonatal brain development and neuronal circuit formation are not fully explored
- Whether the similarities between neonatal and reactive astrocytes represent true dedifferentiation or convergent phenotypes in pathological conditions requires further investigation
- The developmental trajectory from P3 to mature astrocytes (P21+) and the precise timing of syncytial network formation remain to be characterized
- The role of specific connexin isoforms in neonatal gap junction coupling was not determined

### Connections & keywords

- **Key citations**: Previous work on mature astrocyte electrophysiology from Zhou lab; literature on NG2 glia electrophysiology (to contrast with astrocytes); studies on reactive astrocyte properties; foundational work on ALDH1L1 as an astrocyte marker
- **Named models or frameworks**: Goldman-Hodgkin-Katz (GHK) equation for calculating ionic currents and reversal potentials; dual patch recording methodology for measuring gap junction coupling
- **Brain regions**: Hippocampus, stratum radiatum, CA1 region
- **Keywords**: astrocytes, electrophysiology, gap junctions, potassium homeostasis, Kir4.1, developmental neurobiology, hippocampus, passive astrocytes, variably rectifying astrocytes, meclofenamic acid, neonatal development, syncytial network, TWIK-1, TREK-1
