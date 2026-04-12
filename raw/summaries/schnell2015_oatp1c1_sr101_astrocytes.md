---
source_file: schnell2015_oatp1c1_sr101_astrocytes.md
paper_id: schnell2015_oatp1c1_sr101_astrocytes
title: "The multispecific thyroid hormone transporter OATP1C1 mediates cell-specific sulforhodamine 101-labeling of hippocampal astrocytes"
authors:
  - "Christian Schnell"
  - "Ali Shahmoradi"
  - "Sven P. Wichert"
  - "Steffen Mayerl"
  - "Yohannes Hagos"
  - "Heike Heuer"
  - "Moritz J. Rossner"
  - "Swen Hülsmann"
year: 2015
journal: "Brain Structure and Function"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
brain_regions:
  - hippocampus
  - hippocampus_ca1
keywords:
  - sulforhodamine_101_sr101
  - astrocyte_identification
  - oatp1c1_transporter
  - slco1c1
  - thyroid_hormone_transport
  - l_thyroxine_t4
  - organic_anion_transporting_polypeptide
  - transcriptome_analysis
  - rna_sequencing
  - blood_brain_barrier
  - astrocyte_heterogeneity
  - two_photon_microscopy
  - multispecific
  - thyroid
  - hormone
  - transporter
  - oatp1c1
  - mediates
  - cell
  - specific
key_citations:
  - nimmerjahn2004_sulforhodamine_astroglia
  - pannasch2011_astroglial_networks_synaptic
---

### One-line summary

The thyroid hormone transporter OATP1C1 (SLCO1C1) is identified as the molecular mechanism responsible for sulforhodamine 101 (SR101) uptake into hippocampal and cortical astrocytes, explaining region-specific heterogeneity in astrocyte labeling.

---

### Background & motivation

Sulforhodamine 101 (SR101) is widely used as a fluorescent marker for astrocyte identification in neuroscience research, but the molecular mechanism of its cell-specific uptake remained unknown. Furthermore, SR101 labeling efficacy varies across brain regions, with efficient labeling in cortex and hippocampus but poor labeling in brainstem regions. Understanding the molecular basis of SR101 uptake is crucial for interpreting experimental results and avoiding pitfalls when using this dye, particularly given reports of neuronal labeling under pathophysiological conditions and side effects including chemical LTP.

---

### Methods

- **Transgenic mice**: Used hGFAP-EGFP mice (TgN(hGFAP-EGFP)GFEC-Fki) expressing enhanced green fluorescent protein in astrocytes, and Slco1c1 knockout mice (Oatp1c1-/-)
- **Acute brain slice preparation**: Prepared 250–400 μm transversal slices from brainstem and hippocampus, and parasagittal slices from cortex (P8–P43 mice)
- **SR101 staining**: Standard 20 min incubation at 34°C in 1 μM SR101, followed by 10 min washout; T4 competition studies used 1–10 μM L-thyroxine co-applied during loading
- **Two-photon microscopy**: Multifocal two-photon excitation microscopy (TriMScope) with Ti:Sapphire laser at 800 nm; EGFP detected through 531/40 nm filter, SR101 through 641/75 nm filter
- **Image analysis**: Deconvolution with Autoquant, quantification with Imaris software using "spots" feature; calculated percentage of SR101-positive astrocytes and relative SR101 intensity
- **FACS isolation**: FACS Aria II sorting of EGFP-positive astrocytes from dissected cortex, hippocampus, and brainstem into RLT lysis buffer
- **RNA sequencing**: Modified linear amplification protocol with T7 RNA polymerase; Illumina HiSEQ2000 sequencing; DESeq analysis for differential expression

---

### Key findings

- **Region-specific SR101 labeling**: SR101 intensity was consistently weak in all tested brainstem regions compared to strong labeling in hippocampus; within brainstem, lateral superior olive showed slightly more intense labeling but still far below hippocampal levels
- **Cortical homogeneity**: SR101 labeling was indistinguishable across frontal, motor, and visual cortical areas, supporting the approach of comparing forebrain (hippocampus/cortex) versus brainstem astrocytes
- **Transcriptome identification of OATP1C1**: RNA sequencing of FACS-isolated astrocytes identified 359 transporter mRNAs; only seven mRNAs were significantly elevated in forebrain versus brainstem astrocytes, including two isoforms of Oatp1c1/Slco1c1 (approximately 2-fold increase, adjusted p < 0.05)
- **T4 competition**: L-thyroxine (T4), the physiological substrate of OATP1C1, competitively inhibited SR101 uptake in a dose-dependent manner (1–10 μM); SR101 intensity was significantly reduced at all T4 concentrations tested (p < 0.05, one-way ANOVA with Bonferroni t-test)
- **Knockout confirmation**: In hippocampal slices from Slco1c1-/- (Oatp1c1 knockout) mice, no SR101 labeling of astrocytes was observed; unspecific neuronal labeling in CA1 pyramidal layer persisted, confirming this is an OATP1C1-independent mechanism
- **No alternative transport**: The complete absence of astroglial SR101 labeling in knockout mice suggests no alternative route of SR101 uptake exists in hippocampal astrocytes
- **Regional heterogeneity explained**: Lower Oatp1c1 expression in brainstem astrocytes explains the weak SR101 labeling observed in respiratory regions of the ventrolateral medulla

---

### Computational framework

Not applicable. This is an empirical study combining transcriptomics, pharmacology, and genetics to identify a molecular mechanism. The results may constrain models of astrocyte heterogeneity and dye uptake mechanisms but do not employ explicit computational modeling.

---

### Prevailing model of the system under study

Before this study, the molecular mechanism of SR101 uptake into astrocytes was unknown. Initial hypotheses suggested gap-junction hemichannels might be involved, but this was ruled out by experiments showing effective SR101 labeling in Cx30-/-Cx43-/- double knockout mice lacking most gap-junction proteins. Pharmacological profiling indicated that SR101 was likely actively transported via an organic anion-transporting polypeptide (OATP), but the specific transporter identity remained unknown. The field also recognized that SR101 labeling efficiency varied across brain regions, with particular weakness in brainstem compared to forebrain regions, suggesting regional heterogeneity in astrocyte properties.

---

### What this paper contributes

This paper definitively identifies OATP1C1 (SLCO1C1) as the molecular transporter responsible for SR101 uptake into hippocampal and cortical astrocytes. This discovery resolves a long-standing mystery in neuroscience methodology and provides a mechanistic explanation for the region-specific heterogeneity of SR101 labeling: forebrain astrocytes express high levels of OATP1C1 enabling efficient SR101 uptake, while brainstem astrocytes express low levels resulting in weak labeling. The paper demonstrates that the physiological substrate L-thyroxine (T4) competitively inhibits SR101 uptake, and complete absence of astroglial SR101 labeling in Oatp1c1 knockout mice confirms no alternative uptake mechanism exists in hippocampal astrocytes. This knowledge enables more informed use of SR101 in experimental neuroscience and provides a framework for rational design of cell type-selective dyes based on transporter expression profiles.

---

### Brain regions & systems

- **Hippocampus** — primary site of investigation; strong SR101 labeling in astrocytes due to high OATP1C1 expression; CA1 stratum radiatum region specifically analyzed
- **Cerebral cortex** — frontal, motor, and visual cortical areas showed homogeneous SR101 labeling; used as forebrain comparison region
- **Brainstem** — weak SR101 labeling across all tested regions (pontine reticular nucleus, motor trigeminal nucleus, pre-Bötzinger complex, hypoglossal nucleus, inferior olivary nucleus); lateral superior olive showed slightly more intense labeling but still far below forebrain levels
- **Blood-brain barrier** — OATP1C1 expressed on vascular endothelium enables SR101 crossing from bloodstream; distinct from astrocytic uptake mechanism

---

### Mechanistic insight

This paper provides mechanistic insight at multiple levels, though it does not meet the full bar for algorithmic-level Marr's analysis as it does not formalize a computational process.

**Molecular mechanism identified**: The study identifies OATP1C1 as the specific transporter mediating SR101 uptake into astrocytes. This is established through:
- Transcriptome analysis showing Oatp1c1 enrichment in forebrain versus brainstem astrocytes
- Pharmacological competition with the physiological substrate L-thyroxine (T4)
- Genetic validation in Oatp1c1 knockout mice showing complete absence of astroglial SR101 labeling

**Cellular implementation**: The study reveals region-specific heterogeneity in astrocyte properties based on differential transporter expression. OATP1C1 expression correlates with:
- Regional differences in SR101 labeling efficiency
- Co-expression with Aquaporin 4 suggesting preferential targeting to astroglial end feet
- Coordinated expression with type 2 iodothyronine deiodinase (Dio2) for local thyroid hormone metabolism

The paper does not provide algorithmic-level formalization of a computational process, but it does establish the physical mechanism (transporter-mediated uptake) that constrains how SR101 can be used as a tool for astrocyte identification.

---

### Limitations & open questions

- **Transporter inhibition incomplete**: T4 competition did not completely block SR101 uptake, suggesting higher concentrations or longer incubation might be needed for full inhibition, or that some SR101 enters through other low-affinity pathways
- **Cell population contamination**: FACS-isolated EGFP-positive cells may include neural precursors from the subgranular zone and NG2-positive oligodendrocyte precursor cells, though this was not critical for the SR101 transporter identification
- **Unspecific neuronal labeling mechanism unresolved**: The unspecific labeling of pyramidal neurons near the slice surface persists in knockout mice and after T4 application, suggesting a distinct mechanism (possibly pannexin hemichannels) that was not investigated further
- **Vascular SR101 uptake**: SR101 still labels vessels in Oatp1c1 knockout mice, suggesting either a second endothelial transporter or nonspecific binding to vasculature
- **Functional significance of regional OATP1C1 expression**: The physiological role of differential thyroid hormone transporter expression across brain regions remains speculative; connection to local thyroid hormone metabolism needs further investigation
- **Generalizability to other species**: Human OATP1C1 shows similar forebrain-predominant expression, but direct validation of SR101 mechanism in human tissue was not performed

---

### Connections & keywords

**Key citations:**
- Nimmerjahn et al. 2004 — established SR101 as selective marker for cortical astrocytes
- Schnell et al. 2012 — pharmacological profiling suggesting OATP family involvement
- Pizzagalli et al. 2002 — cloning and characterization of OATP1C1 as thyroid hormone transporter
- Mayerl et al. 2012 — Oatp1c1 knockout mouse characterization
- Pannasch et al. 2011 — ruled out gap-junction involvement in SR101 uptake

**Named models or frameworks:**
- OATP1C1/SLCO1C1 thyroid hormone transporter
- Sulforhodamine 101 (SR101) astrocyte labeling paradigm
- FACS-based astrocyte isolation and transcriptome profiling
- Blood-brain barrier transport mechanisms

**Brain regions:**
- Hippocampus (CA1, stratum radiatum, dentate gyrus)
- Cerebral cortex (frontal, motor, visual)
- Brainstem (pontine reticular nucleus, motor trigeminal nucleus, lateral superior olive, pre-Bötzinger complex, hypoglossal nucleus, inferior olivary nucleus)
- Ventrolateral medulla

**Keywords:**
- Sulforhodamine 101 (SR101)
- Astrocyte identification
- OATP1C1 transporter
- SLCO1C1
- Thyroid hormone transport
- L-thyroxine (T4)
- Organic anion transporting polypeptide
- Transcriptome analysis
- RNA sequencing
- Blood-brain barrier
- Astrocyte heterogeneity
- Two-photon microscopy
