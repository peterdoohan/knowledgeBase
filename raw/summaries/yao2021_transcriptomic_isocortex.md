---
source_file: "yao2021_transcriptomic_isocortex.md"
paper_id: "yao2021_transcriptomic_isocortex"
title: "A taxonomy of transcriptomic cell types across the isocortex and hippocampal formation"
authors: "Zizhen Yao, Cindy T.J. van Velthoven, Thuc Nghi Nguyen, Jeff Goldy, Adriana E. Sedeno-Cortes, Fahimeh Baftizadeh, Darren Bertagnolli, Tamara Casper, Megan Chiang, Kirsten Crichton, Song-Lin Ding, Olivia Fong, Emma Garren, Alexandra Glandon, Nathan W. Gouwens, James Gray, Lucas T. Graybuck, Michael J. Hawrylycz, Daniel Hirschstein, Matthew Kroll, Kanan Lathia, Changkyu Lee, Boaz Levi, Delissa McMillen, Stephanie Mok, Thanh Pham, Qingzhong Ren, Christine Rimorin, Nadiya Shapovalova, Josef Sulc, Susan M. Sunkin, Michael Tieu, Amy Torkelson, Herman Tung, Katelyn Ward, Nick Dee, Kimberly A. Smith, Bosiljka Tasic, Hongkui Zeng"
year: 2021
journal: "Cell"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "prelimbic_cortex"]
keywords: ["taxonomy", "transcriptomic", "cell", "types", "across", "isocortex", "hippocampal", "formation"]
---

### One-line summary

Single-cell transcriptomics of >1.3 million cells across the entire mouse isocortex and hippocampal formation reveals shared cellular organization between these structures and large-scale continuous gradients of neuron-type variation.

### Background & motivation

The isocortex and hippocampal formation (HPF) are critical for perception, cognition, emotion, and learning. While previous single-cell RNA sequencing (scRNA-seq) studies characterized cell types in individual cortical or hippocampal regions, a comprehensive, unified taxonomy across the entire isocortex and HPF was lacking. This study aimed to establish a complete molecular architecture to understand the relationship between these two major brain structures in terms of development, evolution, connectivity, and function.

### Methods

- **Subjects**: Adult mice (both sexes) using transgenic driver lines for neuronal enrichment
- **Cell isolation**: Fluorescence-activated cell sorting (FACS) to enrich for neurons
- **Sequencing platforms**:
  - 10x Genomics Chromium (10xv2): 1,228,636 cells after QC
  - SMART-Seq v4 (SSv4): 76,381 cells after QC
- **Brain regions**: All regions of the isocortex (CTX) and hippocampal formation (HPF) defined by Allen Mouse Brain Common Coordinate Framework version 3 (CCFv3)
- **Analysis**: Consensus clustering combining both datasets, hierarchical clustering for taxonomy tree, UMAP visualization, differential gene expression analysis, correlation-based matching between CTX and HPF cell types
- **Validation**: Allen Brain Atlas RNA in situ hybridization (ISH) data and Visium spatial transcriptomics

### Key findings

- Derived a cell-type taxonomy comprising **388 transcriptomic types** (364 neuronal) from >1.3 million cells
- **GABAergic neurons**: 6 subclasses, 30 supertypes, 119 clusters shared across isocortex and HPF, with some HPF-specific types (e.g., Lamp5 Lhx6, Vip Cbln4 HPF, Sst Lmo1 HPF, Sst Ctsc HPF)
- **Glutamatergic neurons**: 28 subclasses, 56 supertypes, 241 clusters; discovered complete sets of glutamatergic types in HPF homologous to all major isocortical subclasses (L2/3-L6 IT, L5 PT, L5/6 NP, L6 CT, L6b)
- **Continuous variation**: Identified large-scale continuous gradients of cell types along isocortical depth (L2/3 to L6 IT continuum), across the isocortical sheet (anterior-posterior and medial-lateral gradients), and in hippocampus/subiculum along three dimensions (proximal-distal, dorsal-ventral, superficial-deep)
- **Activity-dependent signatures**: Discovered activity-dependent transcriptional gradients (immediate early genes) across hippocampal and subicular regions, with dorsal regions showing higher activity marker expression
- **Regional modularity**: Medial (RSP/ACA), lateral (TEa-PERI-ECT), and prefrontal areas are most transcriptionally distinct; sensory areas form more continuous domains

### Computational framework

Not applicable. This is an empirical study using single-cell transcriptomics. However, the study employs several computational approaches:
- **Clustering algorithms**: Consensus clustering combining 10x and SMART-Seq data; hierarchical clustering for taxonomy tree construction
- **Dimensionality reduction**: UMAP for visualization, PCA for identifying gradients of variation
- **Differential expression analysis**: To identify cluster-specific marker genes
- **Correlation-based matching**: To establish homologous relationships between CTX and HPF cell types
- **Spatial mapping**: Integration with Allen Brain Atlas ISH and Visium spatial transcriptomics data

### Prevailing model of the system under study

The traditional view held that:
1. The isocortex (neocortex) is a newly evolved, six-layered structure that substantially expanded in mammals, whereas the hippocampal formation (archicortex) is an evolutionarily older structure with simpler 3-5 layer organization
2. The hippocampal formation has a simpler cellular organization than the isocortex
3. Cortical areas have distinct, area-specific glutamatergic neuron types (based on earlier studies of VISp and ALM showing distinct types)
4. Cell types are primarily discrete categories rather than continuous variations

### What this paper contributes

This paper fundamentally challenges and updates the prevailing model:

1. **Shared cellular organization between isocortex and HPF**: Discovers that HPF contains a complete set of glutamatergic types homologous to all major isocortical subclasses (L2/3-L6 IT, L5 PT, NP, CT, L6b), suggesting both structures share a common six-layered circuit organization. This challenges the view that HPF is a simpler, evolutionarily older structure.

2. **Continuous variation as a fundamental principle**: Demonstrates that cell types exhibit large-scale continuous gradients across multiple spatial dimensions (cortical depth, cortical sheet, hippocampal axes), rather than existing as purely discrete categories. This reveals a more nuanced landscape of both discrete and continuous variation.

3. **Most glutamatergic types are shared across cortical areas**: Contrary to the finding that VISp and ALM have distinct glutamatergic types, this study shows that most glutamatergic types are shared across multiple isocortical areas with graded variations, suggesting a unified cortical circuit architecture with regional modularity.

4. **Evolutionary implications**: Proposes that both isocortex and HPF evolved from the simpler three-layered cortex in reptiles into two parallel "six-layered" circuit organizations, with the isocortex undergoing additional area multiplication through accelerated evolution.

### Brain regions & systems

- **Isocortex (CTX)**: All functional areas including primary and higher-order sensory areas (MOp, MOs, SSp, SSs, GU, VISC, AUD, VISp, VISal, VISam, VISl, VISpl, VISpm, VISli, VISpor), motor areas, and associational areas (FRP, ACA, PL, ILA, ORB, AI, RSP, PTLp, TEa, PERI, ECT). The study reveals continuous gradients of glutamatergic cell types across cortical depth and the cortical sheet.

- **Hippocampal formation (HPF)**:
  - **Hippocampal region (HIP)**: CA1, CA2, CA3, dentate gyrus (DG) — contains highly distinct glutamatergic types organized along proximal-distal, dorsal-ventral, and superficial-deep gradients
  - **Retrohippocampal region (RHP)**: Entorhinal cortex (ENTl, ENTm), parasubiculum (PAR), postsubiculum (POST), presubiculum (PRE), subiculum (SUB), prosubiculum (ProS) — contains cell types homologous to isocortical types

- **Key findings by region**: 
  - GABAergic types are largely shared across CTX and HPF, with some HPF-specific types
  - Glutamatergic types in HPF are homologous to all major isocortical subclasses
  - SUB/ProS/CA1 cell types are most related to L5 PT CTX cells (suggesting output projection neuron homology)

### Mechanistic insight

This paper does not meet the bar for mechanistic insight because it does not present or formalize a specific algorithm that explains a neural phenomenon, nor does it provide neural data supporting a particular computational model over alternatives. Instead, this is a comprehensive descriptive and taxonomic study that establishes a molecular architecture of cell types.

However, the paper provides foundational data that constrains future mechanistic models by:
- Establishing homologous relationships between isocortical and hippocampal cell types that predict similar circuit organization principles
- Revealing continuous gradients of cell-type variation that suggest spatially graded functional properties
- Identifying activity-dependent transcriptional signatures that could relate to memory trace formation
- Providing a cell-type-based framework for understanding hippocampal circuit connectivity that can guide future functional studies

### Limitations & open questions

- **Spatial resolution**: Precise spatial distribution and relative proportions of cell types require more comprehensive spatially resolved transcriptomic studies (e.g., multiplexed FISH, in situ sequencing)
- **Activity states**: The study captures steady-state transcriptomes; activity-dependent transcriptional signatures were inferred from IEG expression patterns rather than experimentally manipulated states
- **Connectivity**: Cell-type-based predictions of circuit connectivity remain to be validated with comprehensive projection mapping
- **Functional roles**: The relationship between transcriptomic cell types and specific functional roles (e.g., grid cells, place cells) remains to be established
- **Developmental trajectory**: The study samples adult brain; developmental origins and trajectories of cell types require further investigation
- **Cross-species generalization**: Whether the homologous relationships and gradients identified in mouse apply to other species is unknown
- **Sex differences**: While both sexes were included, systematic analysis of sex differences in cell-type composition was not performed

### Connections & keywords

**Key citations**: Tasic et al., 2018 (previous VISp-ALM cell-type taxonomy); Harris et al., 2018 (hippocampal CA1 interneurons); Zeisel et al., 2015 (single-cell RNA-seq of cortex and hippocampus); Gouwens et al., 2020 (Patch-seq multimodal classification); Ding et al., 2020 (subiculum transcriptomics); Cembrowski & Spruston, 2019 (hippocampal heterogeneity); Cadwell et al., 2019 (cortical development and arealization); Fishell & Rudy, 2011 (cortical interneuron development)

**Named models or frameworks**: Allen Mouse Brain Common Coordinate Framework (CCFv3); SMART-Seq v4; 10x Genomics Chromium; UMAP (Uniform Manifold Approximation and Projection); constellation plots; taxonomy tree; hierarchical consensus clustering

**Brain regions**: Isocortex (primary visual, motor, somatosensory, auditory, gustatory, visceral, anterior cingulate, prelimbic, infralimbic, orbital, agranular insular, retrosplenial, posterior parietal, temporal, perirhinal, ectorhinal areas); Hippocampal formation (dentate gyrus, CA1, CA2, CA3, subiculum, prosubiculum, entorhinal cortex, parasubiculum, postsubiculum, presubiculum)

**Keywords**: single-cell RNA sequencing, transcriptomics, cell-type taxonomy, isocortex, neocortex, hippocampal formation, GABAergic interneurons, glutamatergic neurons, spatial gradients, continuous variation, consensus clustering, homology, cortical layers, entorhinal cortex, subiculum, dentate gyrus, cornu ammonis, molecular architecture
