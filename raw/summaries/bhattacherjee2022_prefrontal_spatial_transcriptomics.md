---
source_file: bhattacherjee2022_prefrontal_spatial_transcriptomics.md
paper_id: bhattacherjee2022_prefrontal_spatial_transcriptomics
title: "Understanding prefrontal cortex functions by decoding its molecular, cellular and circuit organization"
authors:
  - "Aritra Bhattacherjee"
  - "Chao Zhang"
  - "Brianna Watson"
  - "Mohamed Nadhir Djekidel"
  - "Jeffrey R. Moffitt"
  - "Yi Zhang"
year: 2022
journal: "bioRxiv (preprint, posted December 29, 2022)"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - behavioral_analysis
brain_regions:
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - prelimbic_cortex
  - infralimbic_cortex
  - striatum
  - nucleus_accumbens
  - amygdala
  - periaqueductal_gray
keywords:
  - spatial_transcriptomics
  - merfish
  - prefrontal_cortex
  - cell_type_atlas
  - projection_circuits
  - chronic_pain
  - descending_pain_inhibition
  - l5_extra_telencephalic_neurons
  - ion_channel_expression
  - spared_nerve_injury
  - activity_regulated_genes
  - cortical_cell_composition
  - understanding
  - prefrontal
  - cortex
  - functions
  - decoding
  - its
  - molecular
  - cellular
---

### One-line summary

Using spatially resolved single-cell transcriptomics (MERFISH) in mouse, this study decodes the cellular, molecular, and circuit organisation of the prefrontal cortex, revealing distinct neuron subtypes, unique ion-channel gene expression, target-specific projection circuits, and — critically — a molecularly defined L5 ET1 neuron cluster projecting to PAG that is preferentially deactivated in chronic neuropathic pain.

---

### Background & motivation

The prefrontal cortex (PFC) performs uniquely diverse functions — cognition, executive control, emotional regulation, and modulation of pain — yet its cellular and circuit organisation relative to adjacent cortical areas was poorly understood. Prior single-cell RNA-seq studies characterised PFC cell types but lacked spatial information, making it impossible to link molecular identity to layer position, subregion, or long-range projection target. The emergence of multiplexed spatial transcriptomics (MERFISH) now allows simultaneous cell typing and spatial mapping at single-cell resolution, filling this gap. A secondary motivation is the escalating clinical problem of chronic pain: the PFC-to-PAG circuit has been implicated in descending pain inhibition, but its molecular identity was unknown.

---

### Methods

- **Species and tissue**: Wildtype male C57BL/6 mice (~10 weeks); coronal cryosections of frontal cortex (+2.5 to +1.3 mm from Bregma) from 3 independent biological replicates.
- **MERFISH profiling**: 416-gene MERFISH library (cell-type markers, ion channels, neuropeptides, GPCRs, activity-regulated genes); 24-bit combinatorial barcoding with error-robust fluorescence in situ hybridisation; 487,224 high-quality cells obtained after quality control.
- **Cell clustering**: Two-round unsupervised clustering (Leiden method; Seurat V4; Harmony for batch correction) yielding 52 hierarchically organised cell subtypes (18 excitatory, 19 inhibitory, 15 non-neuronal).
- **Spatial registration**: MERFISH slices aligned to Allen Mouse Brain CCF v3 to define PFC and its subregions (ACAd, PL, ILA, DPP).
- **iSpatial imputation**: Integration of MERFISH and existing PFC scRNA-seq (GSE124952) to extend spatial expression predictions to the full transcriptome (~20,733 genes).
- **Projection prediction**: Co-embedding of MERFISH and a retrograde-labelling scRNA-seq dataset (GSE161936) with a multi-class support vector machine (AUC = 0.913) to assign projection identities to spatially localised MERFISH clusters; validated by retrograde AAV-mCherry injections into PAG and amygdala combined with smFISH.
- **Chronic pain model**: Spared nerve injury (SNI) in mice; brains harvested 6 weeks post-surgery; MERFISH performed on paired sham/SNI slices; differentially expressed genes per cluster identified via logistic regression with batch correction; activity-regulated gene (ARG) score (Arc, Junb, Fos, Npas4, Nr4a1) used to quantify neuronal hypoactivity.

---

### Key findings

- **Distinct cellular composition**: Several excitatory neuron subtypes are selectively enriched (~8-fold) or depleted in PFC relative to adjacent frontal cortical areas; L2/3 IT 1, L5 ET 1, and L5 IT 1 are among the most enriched.
- **Subregion heterogeneity**: Distinct neuron subtypes are differentially distributed across PFC subregions (ACAd, PL, ILA, DPP), suggesting a cellular substrate for subregion-specific functions (e.g., fear encoding in ILA, reward memory in PL).
- **Unique transcriptional signature**: 54 genes enriched and 40 depleted in PFC vs. adjacent cortex (adjusted p < 0.05, DEG > 20%); differentially expressed genes are strongly enriched for voltage-gated potassium channels (particularly delayed rectifiers: Kcna2, Kcnb2, Kcnc2, Kcnc3, Kcnq3, Kcnq5 — depleted), AMPA receptor subunit Gria1 (enriched), and auxiliary AMPA receptor subunit Cacng8 (enriched). iSpatial extended this to 190 enriched and 182 depleted genes transcriptome-wide.
- **Target-intrinsic projection organisation**: Most subcortical targets receive heterogeneous projections from multiple neuron subtypes across layers; PAG is the notable exception — it receives projections almost exclusively from L5 ET neurons (predominantly L5 ET 1), confirmed by retrograde AAV tracing + smFISH (100% of PAG-projecting PFC neurons co-expressed the L5 ET1 marker Pou3f1).
- **Chronic pain affects specific subtypes**: L5 ET 1 shows the largest number of differentially expressed genes in SNI vs. sham; followed by L6 CT 2 and L5 ET 2. Activity-regulated gene scores are significantly reduced in L5 ET 1 in the SNI condition; Fos smFISH confirmed significant depletion of Fos in Pou3f1+ (L5 ET1) neurons in chronic pain (significant by Mann-Whitney test).
- **Pathway enrichment**: Opioid signalling, endocannabinoid pathway, and glutamate receptor signalling are the top enriched pathways in PFC-specific genes.

---

### Computational framework

Not a primarily computational paper. The main analytical tools are:

- **Unsupervised clustering** (Leiden algorithm, KNN graph in Harmony-corrected PCA space) for cell-type identification.
- **Support vector machine (SVM)** with radial basis function kernel for multi-class projection prediction, trained on retrograde-labelling scRNA-seq and applied to MERFISH cells (AUC = 0.913 on held-out test set).
- **iSpatial**: A bioinformatics tool for integrating scRNA-seq and MERFISH to impute spatial gene expression for genes not directly measured by MERFISH.
- **Logistic regression** for differential expression between pain and control conditions, with batch effects modelled as covariates.

These are data-analysis frameworks rather than computational models of neural computation. Results constrain models of PFC circuit function, cortical excitability, and descending pain modulation but do not themselves constitute such a model.

---

### Prevailing model of the system under study

The introduction frames the PFC as a functionally unique, agranular cortical region integrating diverse multimodal inputs to govern cognition, executive action, emotion, and pain modulation — functions qualitatively different from unimodal sensory cortices. The prevailing assumptions the paper pushes against are: (1) that prior scRNA-seq work had established PFC cell type diversity but without spatial context, leaving it unclear how types are arranged in layers, subregions, and circuits; (2) that different cortical regions have different baseline electrical properties, but the molecular substrates of these differences were unknown; (3) that a PFC-to-PAG projection is involved in descending inhibition of pain (long-standing anatomical knowledge), but its molecular and cell-type identity was uncharacterised; and (4) that chronic pain causes PFC hypoactivity (shown by field potentials and transcranial stimulation studies), but which specific cell types are affected was unknown.

---

### What this paper contributes

- Provides the first spatially resolved, cell-type-resolved transcriptomic atlas of the mouse PFC using MERFISH, mapping 52 subtypes in 3D anatomical space and across subregions.
- Establishes that PFC cell composition is quantitatively distinct from adjacent cortical areas in ways that likely underlie its unique functional portfolio (especially enrichment of long-range projection neurons and depletion of certain thalamo-recipient IT subtypes).
- Identifies a molecular basis for the distinct electrophysiological properties of PFC: selective enrichment/depletion of specific ion channel subunits (particularly potassium channels and AMPA receptor components) relative to adjacent cortex.
- Resolves the long-hypothesised PFC-PAG pain circuit to a specific, molecularly defined neuron subtype (L5 ET1, marked by Pou3f1), and shows this subtype undergoes the greatest transcriptional and activity change in chronic neuropathic pain, providing the first cell-type-level mechanistic anchor for this circuit.
- Maps projection targets to neuron subtypes with spatial resolution, revealing that most PFC targets receive heterogeneous multi-subtype projections while PAG receives a uniquely homogeneous L5 ET input.

---

### Brain regions & systems

- **Prefrontal cortex (PFC)** — primary region of study; spatial organisation, cell type composition, transcriptome, and projection circuits mapped at single-cell resolution.
  - **Anterior cingulate cortex, dorsal (ACAd)** — PFC subregion; enriched in L6 IT 1, L2/3 IT 4; associated with compulsive/cognitive functions.
  - **Prelimbic cortex (PL)** — PFC subregion; enriched in L2/3 IT 2 and L4/5 IT 2; associated with reward/cue memory.
  - **Infralimbic cortex (ILA)** — PFC subregion; enriched in L5 ET 1, L6 CT 2-4; associated with fear/trauma encoding.
  - **Dorso-peduncular cortex (DPP)** — PFC subregion mapped but not specifically highlighted.
- **Periaqueductal gray (PAG)** — major output target of PFC L5 ET1 neurons; key site for descending pain inhibition; receives nearly exclusive input from L5 ET1.
- **Amygdala** — receives projections from L6 CT 2 (majority) and L5 ET 1; implicated in affective aspects of pain and fear/emotion.
- **Nucleus accumbens (NAc)** — receives projections primarily from L6 CT 1, L5 ET 1, and some L6 CT 2.
- **Dorsal striatum (DS)** — receives projections from L6 CT 1, 2, and 3.
- **Hypothalamus** — receives projections from L5 ET 1 and L6 CT 1.
- **Contralateral PFC (cPFC)** — receives projections from superficial IT neurons (L2/3).
- **Adjacent frontal cortex (motor cortex and other non-PFC frontal regions)** — used as contrast to define PFC-enriched/depleted genes and cell types.

---

### Mechanistic insight

The paper partially meets the bar. It presents a mechanistic claim — that L5 ET1 neurons constitute the cell-type identity of the PFC-PAG descending pain-inhibition circuit, and that their hypoactivation in chronic pain underlies pain chronification — and provides neural data (retrograde tracing, smFISH, ARG scores) that support this over an unresolved alternative (circuit identity unknown). However, the study does not formalise an algorithm for how L5 ET1 activity suppresses pain, nor does it provide direct causal manipulation data (e.g., optogenetic activation/inhibition of L5 ET1 during pain behaviour). The evidence is therefore anatomical and correlative at the circuit level rather than algorithmic.

Mapping onto Marr's levels:
- **Computational**: The PFC-PAG circuit solves the problem of descending modulation/inhibition of nociceptive signals, integrating cortical state with spinal pain processing.
- **Algorithmic**: L5 ET1 neurons (Pou3f1+) in PFC layers 5 project exclusively to PAG; their transcriptional profile and activity are specifically altered in chronic neuropathic pain, suggesting reduced drive onto PAG as the mechanism of failed descending inhibition.
- **Implementational**: L5 ET1 neurons reside in PFC layer 5, are of the extra-telencephalic (ET) projection class, express Pou3f1 as a marker, and show reduced activity-regulated gene expression (Fos, Arc, etc.) and downregulated transcriptome in chronic pain. The specific cell-type marker and layer location are identified; however, detailed biophysical mechanisms, neuromodulatory inputs, and PAG target cell types are not characterised in this study.

---

### Limitations & open questions

- **Causal evidence lacking**: The paper identifies L5 ET1 as the most affected subtype in chronic pain but does not perform direct gain- or loss-of-function experiments (e.g., chemogenetics, optogenetics) to establish causality in pain behaviour.
- **Mouse-only data**: All findings are in male C57BL/6 mice; generalisability to females, other strains, and humans is unknown.
- **Preprint status**: As of the preprint date (December 2022), peer review had not been completed.
- **MERFISH gene panel limitation**: Only 416 genes were directly measured; the remaining transcriptome was inferred via iSpatial, introducing prediction uncertainty for non-panel genes.
- **Projection prediction is computational, not anatomical**: For most targets except PAG and amygdala (validated by retrograde tracing), projection identities are predictions from an SVM model, not direct anatomical experiments.
- **Afferent inputs not characterised**: The study maps PFC outputs but not inputs; which upstream signals drive L5 ET1 activity, and how these change in chronic pain, remains unknown.
- **Functional heterogeneity within L5 ET1**: L5 ET1 projects almost exclusively to PAG, but whether subsets within this cluster also project to other targets or differ in their pain-related adaptations is unresolved.
- **Open question**: Do the L6 CT 2/3 subtypes (projecting to amygdala, NAc, hypothalamus) mediate the affective/negative component of chronic pain? Direct evidence is absent.

---

### Connections & keywords

**Key citations**:
- Zhang et al. (GSE124952 / prior PFC scRNA-seq, cited as reference 19) — prior scRNA-seq dataset used for iSpatial integration
- Chen et al. (Allen Brain Institute scRNA-seq, cited as reference 23) — used for cell-type correspondence validation
- Economo et al. (GSE161936, cited as reference 2) — retrograde labelling + scRNA-seq dataset used for projection prediction
- Moffitt et al. (referenced as [29]) — MERFISH methods paper (Xia et al. / Moffitt lab protocols)
- Prior SNI model papers (cited as reference 74, Decosterd & Woolf)

**Named models or frameworks**:
- MERFISH (Multiplexed Error-Robust Fluorescence In Situ Hybridisation) — spatial transcriptomics platform
- iSpatial — bioinformatic tool for MERFISH + scRNA-seq integration to impute transcriptome-wide spatial expression
- Allen Mouse Brain Common Coordinate Framework v3 (CCFv3) — reference atlas for spatial registration
- Spared Nerve Injury (SNI) model — standard mouse model of chronic neuropathic pain

**Brain regions**:
- Prefrontal cortex (PFC), anterior cingulate cortex (ACAd), prelimbic cortex (PL), infralimbic cortex (ILA), dorso-peduncular cortex (DPP), periaqueductal gray (PAG), amygdala, nucleus accumbens, dorsal striatum, hypothalamus, contralateral PFC, motor cortex

**Keywords**:
- spatial transcriptomics, MERFISH, prefrontal cortex, cell-type atlas, projection circuits, chronic pain, descending pain inhibition, L5 extra-telencephalic neurons, ion channel expression, spared nerve injury, activity-regulated genes, cortical cell composition
