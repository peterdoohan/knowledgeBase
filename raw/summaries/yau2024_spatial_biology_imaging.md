---
source_file: yau2024_spatial_biology_imaging.md
title: "INSIHGT: an accessible multi-scale, multimodal 3D spatial biology platform"
authors: Chun Ngo Yau, Jacky Tin Shing Hung, Robert A. A. Campbell, Thomas Chun Yip Wong, Bei Huang, Ben Tin Yan Wong, Nick King Ngai Chow, Lichun Zhang, Eldric Pui Lam Tsoi, Yuqi Tan, Joshua Jing Xi Li, Yun Kwok Wing, Hei Ming Lai
year: 2024
journal: Nature Communications
paper_type: empirical
contribution_type: methodological
---

### One-line summary

INSIHGT is a non-destructive, accessible 3D spatial biology method utilizing superchaotropes and host-guest chemistry to achieve homogeneous, deep penetration of macromolecular probes up to centimeter scales, enabling quantitative multi-modal molecular imaging of intact tissues.

---

### Background & motivation

Biological systems are complex, encompassing intertwined spatial, molecular and functional features, but methodological constraints limit the completeness of information that can be extracted. Current 3D immunohistochemistry methods suffer from limited antibody penetration, signal inhomogeneity across depth, long incubation times, and requirements for specialized equipment. There is a need for an accessible, scalable, and affordable method that enables deep, homogeneous, and quantitative 3D molecular phenotyping of intact tissues without these limitations.

---

### Methods

- **Method development**: Screened weakly coordinating superchaotropes (WCS) and host-guest chemistry systems for antibody penetration enhancement, identifying closo-dodecahydrododecaborate ([B12H12][2-]) with γ-cyclodextrin (γCD) or 2-hydroxypropyl-γ-cyclodextrin (2HPγCD) as optimal
- **INSIHGT protocol**: Two-stage process: (1) infiltrate tissue with antibodies + [B12H12][2-] in PBS (Buffer A) to prevent antibody-antigen binding and enable deep penetration; (2) add 2HPγCD (Buffer B) to complex [B12H12][2-] and reinstate antibody-antigen binding
- **Benchmarking**: Compared INSIHGT against CUBIC-HV, iDISCO, SHANEL, and SWITCH-ELAST using hemibrain bulk-staining followed by cut-staining reference comparison
- **Validation**: Tested 357 antibodies (90.5% compatible), 21 lectins, nucleic acid probes, neurotransmitters, and post-translational modifications
- **Multi-modal integration**: Combined immunostaining with RNA FISH HCR, DNA staining, and lectin histochemistry
- **Multi-round multiplexing**: Demonstrated 28-plex imaging in mouse hypothalamus over 7 rounds using antibody elution with sodium sulfite
- **Applications**: Mouse whole brain (3-year-old), kidney (14 samples parallel), hypothalamus (28-plex); Human cortex (1.5×1.5×3 cm), cerebellum (1.75×2.0×2.2 cm), brainstem with dementia with Lewy bodies (1.0×1.4×1.4 cm)
- **Analysis methods**: Cell segmentation with Cellpose 2.0, UMAP clustering, structure tensor analysis for fiber orientation, SNT plugin for filament tracing

---

### Key findings

- **INSIHGT achieves deepest and most homogeneous penetration**: Signal decay distance constant (τ) approached ideal (τ→0+) with negligible decay across penetration depth; achieved ~2 cm penetration in human tissues; 10–20× penetration enhancement over iDISCO+ with 3 days vs 7 days staining
- **Quantitative 3D immunostaining**: Pearson correlation r = 0.752 (c-Fos) and r = 0.512 (parvalbumin) between INSIHGT bulk-staining and cut-staining reference signals
- **High antibody compatibility**: 323 of 357 tested antibodies (90.5%) produced expected patterns—at least 6× more than any other deep immunostaining method demonstrated
- **Multi-modal compatibility**: Compatible with antigens, mRNAs (FISH HCR), neurotransmitters, epigenetic modifications (histone methylation/acetylation), glycosylations (lectins), and nucleic acid probes; RNA integrity number (RIN) = 7.2 post-INSIHGT (vs 9.0 control); DNA yield and sequencing quality preserved
- **Multi-round multiplexing**: Achieved 28-plex molecular profiling in mouse hypothalamus (25 protein markers + 3 vessel channels) over 7 rounds; identified 42 cell type clusters via UMAP; demonstrated NPY-proximal cell type analysis
- **Novel biological discoveries**: Discovered previously undescribed podocyte-to-parietal epithelial cell (PEC) microfilaments traversing the Bowman space in mouse kidneys (1078 inclusions traced); identified sparsely distributed neurofilament-intensive inclusion bodies in human cerebellum with unique morphologies; mapped age-related changes in 3-year-old mouse brain including thalamic/striatal cavitations and hippocampal calbindin deposits
- **Clinical compatibility**: Post-INSIHGT tissues retain full compatibility with traditional 2D histology (H&E, PAS, Alcian blue, Masson's trichrome); indistinguishable from pre-INSIHGT controls by senior pathologist; enables "next-generation histopathology" workflow combining 3D imaging with traditional pathology

---

### Computational framework

Not applicable. This is a primarily methodological/empirical paper focused on developing a chemical approach for 3D tissue imaging. However, the paper employs several computational analysis techniques:

- **Cell segmentation**: Cellpose 2.0 (deep learning-based cell segmentation) for 3D cell identification and morphological analysis
- **Dimensionality reduction**: Uniform Manifold Approximation and Projection (UMAP) for cell type clustering based on 51 markers (mean intensity, standard deviation, and distance to nearest vessel)
- **Filament tracing**: SNT plugin for ImageJ for manual tracing and morphometric analysis of microfilaments and neurofilament inclusions
- **Structure tensor analysis**: For fiber orientation visualization and fractional anisotropy computation in cerebellar neural and glial filaments
- **Image registration**: Affine and non-rigid registration for multi-round multiplexing image alignment

The computational framework primarily serves to extract quantitative information from the volumetric imaging data enabled by INSIHGT, rather than representing a formal computational model of biological processes.

---

### Prevailing model of the system under study

The prevailing understanding of 3D immunohistochemistry (IHC) is that deep antibody penetration faces a "reaction barrier" due to high binding affinities and low antibody concentrations, which deplete antibodies at tissue surfaces before reaching deeper regions. Current methods address this through various strategies: (1) modulating antibody-antigen binding kinetics using detergents/chaotropes (e.g., SDS in SWITCH, urea in CUBIC), (2) applying external force fields (electrotransport in eFLASH), (3) mechanical compression/stretching (mELAST), or (4) extremely long incubation times (weeks). However, these approaches generally compromise between penetration depth, signal homogeneity, staining quality, and accessibility—deep penetration typically requires long incubation times with inhomogeneous signals, while faster methods produce weak or non-specific staining. The field lacks an accessible technology that balances authenticity, volume of data extracted, and operational simplicity.

---

### What this paper contributes

This paper introduces INSIHGT (In situ Host-Guest Chemistry for Three-dimensional Histology), a fundamentally different approach to deep 3D immunostaining that overcomes the trade-offs plaguing existing methods. The key innovation is using weakly coordinating superchaotropes (specifically closo-dodecahydrododecaborate [B12H12][2-]) to transiently inhibit antibody-antigen binding during tissue infiltration, followed by host-guest complexation with cyclodextrin derivatives to restore binding. This enables deep, homogeneous antibody penetration with simple room-temperature incubation—no specialized equipment, force fields, or weeks-long incubation required.

INSIHGT represents a substantial advance over existing methods: it achieves near-ideal signal homogeneity (τ→0+) with negligible decay across centimeter-scale penetration depth, validates 90.5% of tested antibodies (6× more than any prior method), and processes whole organs in 3 days versus weeks for comparable methods. The method is also the fastest from tissue to image (6 days for whole mouse brain), uses off-the-shelf reagents at room temperature, and costs significantly less than electrotransport or mechanical compression systems.

Beyond technical improvements, INSIHGT enables previously impossible biological investigations: discovering novel podocyte-to-PEC microfilaments in kidney glomeruli, characterizing unique neurofilament inclusion bodies in human cerebellum, and performing 28-plex spatial proteomic analysis with cell type clustering. The non-destructive nature allows post-3D-imaging retrieval for traditional 2D histology and nucleic acid sequencing, enabling a "next-generation histopathology" workflow that bridges 3D molecular imaging with clinical diagnostics. This establishes INSIHGT as a foundation for volumetric spatial multi-omics and holistic systems biology studies.

---

### Brain regions & systems

- **Kidney glomeruli**: Site of discovery of novel podocyte-to-parietal epithelial cell (PEC) microfilaments traversing the Bowman space; used for demonstrating fine-scale 3D imaging of compact structures
- **Cerebellum**: Human cerebellum used for discovering sparsely distributed neurofilament-intensive inclusion bodies; mouse cerebellum used for method development and benchmarking
- **Cerebral cortex**: Human cortex (1.5×1.5×3 cm) used for demonstrating centimeter-scale penetration and parvalbumin neuron mapping in layer 4
- **Thalamus**: Identified cavitations in aged mouse brain (3-year-old) and elevated c-Fos expression around these cavitations, suggesting effects on baseline neuronal activities
- **Striatum**: Identified cavitations in aged mouse brain showing age-related structural changes
- **Hippocampus**: Mapped calbindin-positive deposits in stratum radiatum of aged mouse; demonstrated calcium-binding protein multiplexing (CALB1, CALB2, PVALB)
- **Hypothalamus**: Site of 28-plex multi-round multiplexing demonstration; used for NPY-proximal cell type analysis via spatial morpho-proteomics
- **Brainstem**: Human brainstem with dementia with Lewy bodies (1.0×1.4×1.4 cm) stained for phosphorylated alpha-synuclein; enabled MRI registration and radio-histopathology correlation
- **Locus coeruleus**: Confirmed localization of Lewy body pathologies in DLB patient, correlating with REM sleep behavior disorder symptoms
- **Substantia nigra**: Confirmed Lewy body pathology localization in DLB patient

---

### Mechanistic insight

Not applicable. This paper presents a methodological advance rather than mechanistic insight into biological processes. The mechanism described is chemical—how superchaotropes and host-guest chemistry enable deep antibody penetration—not a biological mechanism of neural computation or circuit function. While the paper reveals previously unknown biological structures (podocyte-PEC microfilaments, cerebellar neurofilament inclusions), the mechanistic basis of these structures' formation or function is not addressed.

---

### Limitations & open questions

- **Antigen density limitations**: Extremely dense antigens (e.g., GAPDH, type I collagen, actin, myosin) remain difficult for whole organ staining with homogeneous penetration
- **Tissue size limitations**: Practically limited to ~2 cm³ sized tissues; larger tissues may require enhanced protocols
- **Small molecule dye penetration**: Penetration homogeneity of small molecule dyes and lectins still suboptimal for millimeter-scale tissues
- **Multi-round deterioration**: Staining specificity and sensitivity deteriorate with each antibody elution round using sulfite or β-mercaptoethanol; better 3D immunostaining elution methods needed
- **Species validation**: Multi-round staining has not yet been applied to tissues from species other than mouse
- **Biological unknowns**: Function and significance of discovered podocyte-to-PEC microfilaments and neurofilament inclusion bodies remain to be determined; whether microfilament hotspots are driven by podocyte signals, environmental factors, or PEC signals is unknown

---

### Connections & keywords

- **Key citations**: iDISCO (Renier et al. 2014), SWITCH (Murray et al. 2015), CUBIC (Susaki et al. 2020), SHANEL (Mai et al. 2022), eFLASH (Yun et al. 2019), mELAST (Ku et al. 2020), Cellpose 2.0 (Pachitariu & Stringer 2022), Human Protein Atlas
- **Named models or frameworks**: INSIHGT (In situ Host-Guest Chemistry for Three-dimensional Histology), weakly coordinating superchaotrope (WCS) concept, host-guest chemistry, structure tensor analysis, UMAP clustering
- **Brain regions**: Kidney glomeruli, cerebellum, cerebral cortex, thalamus, striatum, hippocampus, hypothalamus, brainstem, locus coeruleus, substantia nigra
- **Keywords**: 3D immunohistochemistry, tissue clearing, deep immunostaining, host-guest chemistry, superchaotrope, closo-dodecahydrododecaborate, cyclodextrin, spatial transcriptomics, multi-plex imaging, light-sheet microscopy, confocal microscopy, podocyte, neurofilament, dementia with Lewy bodies, cell type profiling, spatial proteomics
