---
source_file: nimmerjahn2004_sulforhodamine_astroglia.md
paper_id: nimmerjahn2004_sulforhodamine_astroglia
title: "Sulforhodamine 101 as a specific marker of astroglia in the neocortex in vivo"
authors:
  - "Axel Nimmerjahn"
  - "Frank Kirchhoff"
  - "Jason N D Kerr"
  - "Fritjof Helmchen"
year: 2004
journal: "Nature Methods"
paper_type: empirical
contribution_type: methodological
species:
  - mouse
  - rat
methods:
  - calcium_imaging
keywords:
  - sulforhodamine_101_sr101
  - astrocyte_labelling
  - in_vivo_two_photon_microscopy
  - protoplasmic_astrocytes
  - calcium_imaging
  - neuron_glia_communication
  - gap_junction_coupling
  - gliovascular_interface
  - astrocyte_calcium_waves
  - neocortex
  - astroglia_specificity
  - fluorescent_dye_marker
  - sulforhodamine
  - 101
  - specific
  - marker
  - astroglia
  - vivo
---

### One-line summary

Brief topical application of sulforhodamine 101 (SR101) to the neocortical surface selectively and robustly labels protoplasmic astrocytes in vivo, enabling simultaneous two-photon imaging of astroglial and neuronal calcium dynamics.

---

### Background & motivation

Methods for studying glial cell structure and function in the intact brain had been lacking, despite growing evidence that astrocytes play active signalling roles in the CNS including modulation of synaptic function, long-range signalling, and regulation of cerebral blood flow. Existing approaches (transgenic EGFP lines, bulk calcium dye loading) could not unambiguously separate astrocytes from neurons in vivo. A simple, specific in vivo labelling method for astroglia was needed to enable functional studies of neuron-glia communication in the living brain.

---

### Methods

- **Subject population**: Wistar rats (P13–P28) and C57BL/6 mice (P23–P270), including transgenic lines expressing EGFP in astrocytes (GFAP-EGFP) or microglia (CX3CR1-EGFP).
- **Task/labelling**: SR101 (25–100 µM) applied briefly (1–5 min) to exposed neocortical surface or via micropipette pressure ejection; Texas Red-hydrazide used as a paraformaldehyde-fixable analogue for post-hoc immunostaining.
- **Key measurements**: Two-photon in vivo imaging up to 700 µm depth; immunohistochemistry for S-100β (astrocyte marker), CNPase (oligodendrocyte marker), and NeuN (neuronal marker); astrocyte volume density estimation; radial density analysis of cell-to-cell distances.
- **Functional imaging**: Multicell bolus loading of Oregon Green 488 BAPTA-1 AM (OGB-1 AM) for calcium indicator loading combined with SR101 to simultaneously measure calcium dynamics in identified astrocytes and neurons.
- **Gap junction investigation**: Carbenoxolone (CBX, 100 µM) applied to assess contribution of gap junctions to dye spread.
- **Analysis approach**: Maximum intensity projections, volume density counting, radial density histograms, fluorescence ΔF/F traces at 15 Hz frame rate.

---

### Key findings

- SR101 specifically labels protoplasmic astrocytes: 95.1 ± 1.1% of SR101-labeled cells were S-100β-positive (n = 520 cells, 4 animals); zero overlap with NeuN-positive neurons (n = 554 cells); only 15/565 cells showed overlap with CNPase-positive oligodendrocytes.
- In GFAP-EGFP transgenic mice, 97.2 ± 1.9% of EGFP-expressing astrocytes were co-labeled by SR101 (n = 1,064 cells); SR101 did not label CX3CR1-EGFP microglial cells (3/638 exceptions, likely macrophages).
- SR101 spread through gap junctions: carbenoxolone markedly suppressed labelling at the local application site.
- Astrocyte volume densities: rats 28.1 ± 1.2 × 10³ cells/mm³ (layer 1) and 17.9 ± 1.4 × 10³ cells/mm³ (layer 2/3); mice approximately 25% lower; a distinct peak in the radial density distribution at ~15 µm indicated frequent paired astrocyte cell bodies.
- Cortical microvasculature was completely enveloped by end feet of SR101-labeled astrocytes, confirmed by co-staining with FITC-dextran injected intravenously.
- SR101 combined with OGB-1 AM enabled unambiguous separation of astroglial and neuronal calcium signals: astroglial transients had slow onset (~13 s 10–90% rise time) and long plateau (~19 s half-width), sometimes propagating as waves; neuronal transients were fast (decay τ ≈ 0.37 s), consistent with action potential-evoked somatic calcium influx.
- No phototoxicity observed over hours to 3 weeks; staining was stable and reproducible across repeated applications.

---

### Computational framework

Not applicable. This is a purely methodological and descriptive empirical study with no explicit computational framework. The results constrain models of astrocyte network organisation (gap-junction-coupled syncytia), neurovascular coupling, and the biophysics of neuron-glia calcium signalling, but the paper itself does not formalise or test a computational account.

---

### Prevailing model of the system under study

Prior to this paper, astrocytes were increasingly recognised as active participants in CNS signalling rather than purely passive support cells, but this understanding was based almost entirely on in vitro (cell culture and brain slice) studies. The field lacked tools to observe astroglial structure and function directly in the intact, living brain. Transgenic EGFP mouse lines existed but covered only a fraction of astrocytes; bulk calcium dye loading could not reliably separate neuronal from astroglial signals. The paper's introduction signals a field in which the in vivo relevance of astrocyte calcium oscillations and waves — well characterised in vitro — remained unknown.

---

### What this paper contributes

SR101 surface application provides the first simple, robust, and highly specific method for labelling all protoplasmic astrocytes in the intact rodent neocortex, validated against multiple orthogonal markers. This enables in vivo studies that were not previously possible: (1) morphometric quantification of the astroglial distribution in living tissue, (2) visualisation of the complete astrocyte-microvasculature relationship in vivo, and (3) unambiguous separation of astroglial from neuronal calcium dynamics during spontaneous activity. The paper provides direct in vivo evidence that astrocytic calcium oscillations and propagating waves occur in the living brain — a key open question given prior reliance on in vitro preparations.

---

### Brain regions & systems

- **Neocortex (layers 1 and 2/3)** — primary focus; SR101 labelling characterised in neocortical protoplasmic astrocytes of rat and mouse.
- **Cortical microvasculature** — structural relationship to SR101-labeled astrocyte end feet examined.
- **Cerebellum (negative result)** — Bergmann glia in cerebellum did not take up SR101 in vivo, indicating region-specific uptake mechanisms.

---

### Mechanistic insight

The paper does not meet the bar for the Mechanistic insight section. It presents a methodological contribution (SR101 as a selective astrocyte label) and descriptive functional findings (distinct calcium dynamics in astrocytes vs. neurons), but it does not formalise an algorithm or provide neural data that discriminates between competing mechanistic accounts of astroglial function. The mechanism of SR101 uptake itself is noted as unknown — a transporter system is speculated but not identified. The calcium imaging data demonstrate that astroglial and neuronal calcium signals can be distinguished in vivo but do not test specific hypotheses about the computations or algorithms underlying neuron-glia communication.

---

### Limitations & open questions

- The mechanism of selective SR101 uptake by protoplasmic astrocytes is unknown; endocytosis vs. specific transporter uptake is unresolved.
- SR101 specificity varies by brain region — Bergmann glia in cerebellum do not take up SR101, so the method cannot be generalised without per-area validation.
- A small number of exceptions (macrophages, occasional NG2-positive glial progenitors) indicate the label is not absolutely exclusive.
- The physiological significance of spontaneous in vivo astroglial calcium oscillations and waves — including their relationship to neuronal activity and blood flow regulation — is not addressed by this study and remains an open question.
- Long-range spread via gap junctions means the spatial precision of SR101 labelling near application boundaries may be limited.

---

### Connections & keywords

**Key citations**:
- Stosiek et al. (2003) — multicell bolus loading for two-photon calcium imaging of neuronal networks
- Nolte et al. (2001) — GFAP-EGFP transgenic mouse line
- Jung et al. (2000) — CX3CR1-EGFP microglial mouse line
- Hirase et al. (2004) — prior in vivo calcium dynamics in cortical astrocytes
- Dani et al. (1992) — neuronal activity triggers calcium waves in hippocampal astrocytes (in vitro)
- Ehinger et al. (1994) — SR101 uptake by oligodendroglia in rabbit retina (earlier in vitro observation)

**Named models or frameworks**:
- Tripartite synapse (astrocyte-neuron-synapse signalling framework)
- Multicell bolus loading (OGB-1 AM technique from Stosiek et al. 2003)

**Brain regions**:
- Neocortex (layers 1 and 2/3)
- Cortical microvasculature
- Cerebellum (negative control)

**Keywords**:
- sulforhodamine 101 (SR101), astrocyte labelling, in vivo two-photon microscopy, protoplasmic astrocytes, calcium imaging, neuron-glia communication, gap junction coupling, gliovascular interface, astrocyte calcium waves, neocortex, astroglia specificity, fluorescent dye marker
