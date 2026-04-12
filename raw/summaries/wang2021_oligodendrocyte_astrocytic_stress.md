---
source_file: wang2021_oligodendrocyte_astrocytic_stress.md
paper_id: wang2021_oligodendrocyte_astrocytic_stress
title: "Reduced Oligodendrocyte Precursor Cell Impairs Astrocytic Development in Early Life Stress"
authors:
  - "Yuxin Wang"
  - "Yixun Su"
  - "Guangdan Yu"
  - "Xiaorui Wang"
  - "Xiaoying Chen"
  - "Bin Yu"
  - "Yijun Cheng"
  - "Rui Li"
  - "Juan C. Sáez"
  - "Chenju Yi"
  - "Lan Xiao"
  - "Jianqin Niu"
year: 2021
journal: "Advanced Science"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
tasks:
  - open_field
methods:
  - calcium_imaging
brain_regions:
  - hippocampus
  - hippocampus_ca1
keywords:
  - oligodendrocyte_precursor_cell
  - astrocyte_development
  - wnt_signaling
  - wnt7a
  - wnt7b
  - catenin
  - early_life_stress
  - parental_isolation
  - gap_junction
  - connexin_43
  - glial_cell_interaction
  - neuropsychiatric_disorder
  - hippocampus
  - paracrine_signaling
  - reduced
  - oligodendrocyte
  - precursor
  - cell
  - impairs
  - astrocytic
key_citations:
  - rouach2008_astrocyte_metabolism
  - murphy-royal2020_stress_astrocyte_lactate_ltp
---

### One-line summary

OPC-derived Wnt7a/b ligands are required for astrocytic development via Wnt/β-catenin signaling, and their loss in early life stress causes astrocyte maldevelopment and neuropsychiatric symptoms.

### Background & motivation

Early life stress (e.g., parental neglect in left-behind children) is a major contributor to neuropsychiatric disorders in adulthood, including anxiety and depression. While astrocyte maldevelopment has been implicated in these disorders, the mechanism of astrocytopathy remains unclear. This study addresses the gap by investigating how reduced oligodendrocyte precursor cells (OPCs) impair astrocytic development through a novel paracrine signaling mechanism.

### Methods

- **Mouse model:** Improved parental isolation model (pups separated from parents 8h/day, P2-P12) with father-only control group to distinguish caring deprivation from nutrient deficiency
- **OPC ablation:** Pdgfra[CreER]:DTA transgenic mice with tamoxifen-induced OPC elimination (P4-P7)
- **Conditional knockout:** Pdgfra[CreER]:Wnt7b-flox and Wnt7a-flox mice for OPC-specific Wnt ligand deletion
- **Histology:** Immunostaining for astrocyte markers (GFAP, BLBP, Cx43, Cx30), OPC markers (Olig2, NG2), neuronal activity (c-Fos)
- **Functional assays:** gap-FRAP for gap junction function, calcium imaging for astrocytic activity
- **RNA-seq:** Transcriptome profiling of isolated astrocytes (P7) with pathway enrichment analysis
- **Rescue experiments:** Osmotic pump micro-injection of Wnt7a/b into hippocampus (P14, 4-day infusion)
- **Behavioral tests:** Cliff avoidance (impulsivity), tail suspension (depression), elevated plus maze/open field (anxiety), novel object recognition (cognition)

### Key findings

- **Parental isolation model:** Isolated mice displayed increased impulsive, depressive, and anxiety-like behaviors but normal cognition; hippocampal astrocytes showed reduced branching (48.9% by BLBP, 70.4% by GFAP), decreased Cx43 (73.5%) and Cx30 (35.5%), impaired gap junction function, and reduced Ca2+ activity
- **Sequential pathology:** OPC reduction (P4) preceded astrocyte abnormalities (P7) and neuronal dysfunction (P10), suggesting OPCs regulate astrocyte development
- **OPC ablation phenocopies isolation:** Genetic OPC elimination reproduced astrocyte maldevelopment (reduced branching, Cx43 downregulation, impaired gap junctions, reduced Ca2+ activity) and neuronal dysfunction
- **Paracrine mechanism:** OPC-conditioned medium (but not OL-conditioned medium or membrane proteins) promoted astrocytic Cx43 expression, gap junction function, and Ca2+ activity
- **Wnt/β-catenin pathway:** RNA-seq identified Wnt pathway downregulation in isolated astrocytes; Wnt7a/b treatment upregulated astrocyte markers (Cx43, Gfap), functional genes (Grin2c, Kcnj10, Slc1a2), and Wnt pathway markers (Axin2, Notum), while XAV939 (Wnt antagonist) blocked these effects
- **OPC-specific Wnt7b knockout:** Wnt7b cKO in OPCs caused astrocyte maldevelopment (68.0% BLBP branching, 77.9% GFAP branching, 55.5% Cx43), reduced neuronal activity, and anxiety-like behavior; Wnt7a cKO showed no phenotype (consistent with lower Wnt7a expression in OPCs)
- **Therapeutic rescue:** Hippocampal Wnt7a/b micro-injection in isolation mice restored astrocytic β-catenin activation, increased branching (42.9% BLBP, 32.8% GFAP), and increased Cx43 (52.9%) and Cx30 (193.7%)

### Computational framework

Not applicable. This is an empirical study focused on molecular and cellular mechanisms. The findings could constrain models of glial cell-cell communication and Wnt signaling in neural development.

### Prevailing model of the system under study

The field previously understood that: (1) astrocyte maldevelopment and connexin dysregulation occur in early life stress models and neuropsychiatric disorders; (2) OPCs are primarily viewed as precursors to myelinating oligodendrocytes, though emerging evidence suggested myelinindependent roles; (3) defective astrocytes can impair OPC development in neural disorders; (4) Wnt/β-catenin signaling is important for astrocyte activation and is altered in stress-induced abnormal astrocytes. The paper notes that most mechanistic studies focused on single cell types, ignoring interactions between different glial cell types.

### What this paper contributes

This paper establishes a novel direction of glial crosstalk: OPCs regulate astrocyte development via paracrine Wnt7a/b signaling. Key contributions include:

1. **Novel mechanism**: OPC-derived Wnt ligands (especially Wnt7b) are required for astrocytic Wnt/β-catenin pathway activation and subsequent astrocyte maturation and network formation
2. **Temporal causality**: Demonstrated that OPC reduction precedes and causes astrocyte maldevelopment (P4 vs P7), establishing OPCs as upstream regulators
3. **Myelin-independent role**: This function is distinct from OPCs' traditional role as myelinating oligodendrocyte precursors
4. **Disease relevance**: Links early life stress (parental isolation) to OPC reduction → astrocyte maldevelopment → neuronal dysfunction → neuropsychiatric behaviors
5. **Therapeutic potential**: Demonstrated that focal Wnt7a/b replenishment can rescue astrocytic maldevelopment, suggesting a therapeutic strategy for early life stress-related disorders

### Brain regions & systems

- **Hippocampus (CA1 region)** — primary site of investigation; shows astrocyte maldevelopment, OPC reduction, and neuronal dysfunction; site of Wnt7a/b rescue injections
- **Cerebral cortex** — secondary region examined; shows similar OPC and astrocyte alterations
- **Glial cell systems**: OPCs, astrocytes, oligodendrocytes, microglia (the latter two not significantly affected)

### Mechanistic insight

This paper provides strong mechanistic insight into glial cell-cell communication:

**Computational level**: The brain must coordinate development of different glial cell types to ensure proper neural circuit function. The paper reveals that OPCs serve as a signaling hub that regulates astrocyte maturation.

**Algorithmic level**: The mechanism involves paracrine secretion of Wnt7a/b ligands from OPCs, which activate the Wnt/β-catenin pathway in astrocytes. This signaling cascade upregulates astrocyte maturation markers (GFAP, Cx43) and functional genes (Kcnj10, Slc1a2, Aqp4). The effect is specific to Wnt7a/b (other Wnt ligands like Wnt4, Wnt10a are less effective) and acts through a paracrine (not direct contact) mechanism.

**Implementational level**: The physical implementation involves: (1) OPCs as Wnt7a/b-secreting cells, with Wnt7b being the predominant ligand; (2) Astrocytes expressing Wnt receptors (Frizzled family) that respond to low concentrations of Wnt7a/b; (3) β-catenin stabilization and nuclear translocation activating transcription of astrocyte-specific genes; (4) Downstream effects on gap junction proteins (Cx43, Cx30) enabling astrocytic network formation and Ca2+ signaling.

This meets the mechanistic insight bar because it provides both a specific signaling algorithm (Wnt/β-catenin pathway activation) and supporting neural data (OPC reduction, Wnt7b cKO, rescue experiments) that causally links the mechanism to the observed phenotypes.

### Limitations & open questions

- The study focuses on early developmental stages (P2-P23); whether OPC-derived Wnt signaling regulates astrocytes in adulthood remains unclear
- The contribution of OL myelination to later-stage neuropsychiatric symptoms in the parental isolation model cannot be fully ruled out
- Whether endothelial/vascular effects of Wnt7a/b contribute to the observed phenotypes was excluded but not comprehensively studied in all contexts
- The father-only control group provides care but not maternal care; the specific contribution of maternal vs. paternal care was not isolated
- Whether this mechanism operates in human early life stress-related disorders requires validation
- The relationship between astrocyte maldevelopment and specific neuropsychiatric symptoms (impulsivity, depression, anxiety) is correlative; causal links need further investigation

### Connections & keywords

**Key citations:**
- Allen & Lyons (2018) - glial cell interactions in CNS function
- Rouach et al. (2008) - astrocytic networks and neuronal activity
- Kang et al. (2010) - Pdgfra-CreER for OPC targeting
- Yuen et al. (2014) - Wnt7a/b in OPC and vascular development
- Daneman et al. (2009) - Wnt signaling in blood-brain barrier
- Murphy-Royal et al. (2020) - stress-induced astrocytic network impairment

**Named models or frameworks:**
- Parental isolation mouse model (early life stress)
- Pdgfra-CreER:DTA OPC ablation model
- Wnt/β-catenin signaling pathway
- Gap-FRAP (fluorescence recovery after photobleaching) for gap junction function
- RNA-seq transcriptome analysis

**Brain regions:**
- Hippocampus (CA1)
- Cerebral cortex

**Keywords:**
oligodendrocyte precursor cell, astrocyte development, Wnt signaling, Wnt7a, Wnt7b, β-catenin, early life stress, parental isolation, gap junction, connexin-43, glial cell interaction, neuropsychiatric disorder, hippocampus, paracrine signaling
