---
source_file: "salvan2022_serotonin_networks.md"
paper_id: "salvan2022_serotonin_networks"
title: "Serotonin regulation of behavior via large-scale neuromodulation of serotonin receptor networks"
authors: "Piergiorgio Salvan, Madalena Fonseca, Anderson M. Winkler, Antoine Beauchamp, Jason P. Lerch, Heidi Johansen-Berg"
year: 2022
journal: "Nature Neuroscience"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse", "human"]
methods: ["optogenetics", "fmri"]
brain_regions: ["hippocampus", "prefrontal_cortex", "amygdala"]
keywords: ["grandjean_et_al_2019_source_of_mouse_ofmri_data_used_in_the_study", "smith_et_al_2015_human_connectome_project_data_and_positive_negative_mode_framework", "dayan_and_huys_2008_computational_framework_for_serotonin", "inhibition", "and_negative_mood", "cools", "roberts_and_robbins_2008_serotoninergic_regulation_of_emotional_and_behavioral_control", "deakin_and_graeff_1991_5_ht_and_mechanisms_of_defence_aversive_processing_theory", "lein_et_al_2007", "hawrylycz_et_al_2012_allen_brain_institute_transcriptomic_atlases", "named_models_or_frameworks", "serotonin_receptor_networks_srns_the_core_construct_developed_in_this_paper", "transcriptomic_neuroimaging_mapping_the_methodological_approach_combining_gene_expression_with_fmri", "dual_regression_fsl_dr_the_statistical_technique_for_extracting_network_time_courses_and_connectivity_maps", "canonical_correlation_analysis_cca_the_multivariate_statistical_framework_linking_srns_to_behavior", "residualized_dr_stage_1_the_control_analysis_establishing_specificity_to_serotonin_receptors", "brain_regions", "dorsal_raphe_nucleus_drn", "amygdala", "temporal_cortex"]
---

### One-line summary

The brain-wide spatial distribution of different serotonin receptor types confers functional specificity at the network level, with distinct serotonin receptor networks (SRNs) mediating separable behavioral effects on impulsivity and negative affect through two independent modes of neuromodulation.

### Background & motivation

While serotonin receptors are well understood at the single-cell level, how different receptor types organize brain-wide activity to regulate distinct behaviors remains unknown. Serotonin has paradoxically been linked to both behavioral inhibition and impulsive aggression, as well as to both aversive processing and reward. This study addresses whether heterogeneous brain-wide distributions of serotonin receptor types might provide a macroscale principle for organizing these diverse behavioral effects.

### Methods

- **Transcriptomic-neuroimaging mapping**: Combined Allen Institute gene expression maps of serotonin receptor genes (HTR1-7) with fMRI data using FSL Dual Regression to extract serotonin receptor networks (SRNs)
- **Mouse optogenetics-fMRI**: Re-analyzed publicly available ofMRI data from ePet-Cre mice expressing ChR2 in DRN serotonin neurons (n=8 ChR2, n=4 eYFP controls, 63 and 18 runs respectively)
- **Pharmacological manipulation**: Analyzed ofMRI data from mice treated with acute fluoxetine (4.5 mg/kg) during DRN stimulation (n=6, 18 runs)
- **Human resting-state fMRI**: Analyzed HCP data from 812 subjects (aged 22-35, 410 females) with four 15-min rs-fMRI runs per subject
- **Canonical correlation analysis (CCA)**: Tested population covariation between SRN functional connectivity and 45 behavioral measures including delay discounting, reward/punishment processing, affect, and psychiatric symptoms
- **Statistical inference**: Permutation-based testing with FWE correction for multiple comparisons across time, brain regions, SRNs, and behavioral variables

### Key findings

- Optogenetic activation of DRN serotonin neurons produced heterogeneous, receptor-specific changes in SRN amplitude: Htr2c and Htr1a increased, while Htr3a and Htr3b decreased (the only ionotropic receptors)
- SRN functional connectivity changes were independent of amplitude changes, with different receptors showing distinct spatial patterns of connectivity modulation (both local and global effects)
- Fluoxetine had bidirectional effects: downregulated Htr1a and Htr1b SRN responses, but upregulated Htr4 SRN responses, consistent with known pharmacological mechanisms
- Htr1a and Htr4 SRN activity showed negative correlation across subjects, supporting a negative feedback control loop hypothesis
- CCA revealed two statistically significant orthogonal modes of population variation linking SRNs to behavior:
  - **Mode 1**: Linked HTR1A, HTR1F, and HTR2C SRN connectivity in amygdala/temporal cortex to greater delay discounting (impulsivity), antisocial problems, and anger/aggression
  - **Mode 2**: Linked HTR1A and HTR4 SRN connectivity in parietal cortex/rolandic operculum to slower reward responses, depression, anxiety, panic, and sadness
- Univariate analyses failed to detect associations between single SRNs and behavior; only the multivariate CCA approach revealed significant relationships

### Computational framework

The study employs a **multivariate receptor-field modeling** approach grounded in **network neuroscience** and **neuromodulatory control theory**. The core formalism combines transcriptomic maps (spatial distributions of receptor gene expression) with fMRI time-series through dual regression, yielding subject-specific temporal dynamics (SRN amplitude) and spatial connectivity patterns (SRN functional connectivity) for each receptor type. This framework treats serotonin receptors as basis functions for decomposing brain-wide neuromodulatory effects, with the admixture of receptors determining regional sensitivity to serotonin release. The CCA component models behavior as arising from linear combinations of SRN connectivity patterns, testing whether population variation in receptor-network organization maps onto distinct behavioral phenotypes.

### Prevailing model of the system under study

Prior to this work, the field understood serotonin receptors primarily at the single-cell level, with known diversity in spatial distribution, chemical affinities, and cellular effects. The prevailing view held that distinct serotonin effects on behavior (behavioral inhibition vs. impulsive aggression; aversive processing vs. reward) might arise from anatomically segregated projections from the DRN and MRN, or from functionally distinct DRN sub-systems. However, a comprehensive theory of how the serotonin system is organized at the macroscopic brain-wide level to support diverse functions remained elusive. The paper's introduction signals that the field lacked understanding of how heterogeneous receptor distributions might provide a brain-wide organizational principle for serotonin's diverse behavioral effects.

### What this paper contributes

This paper establishes that heterogeneous brain-wide distributions of different serotonin receptor types constitute a **macroscale principle of organization** for serotonin regulation of brain networks and behavior. Specifically:

1. **Receptor-specific network modulation**: Demonstrates that the same DRN serotonin activation differentially modulates distinct SRNs in both amplitude and functional connectivity, showing that receptor spatial distributions confer specificity at the network (not just local) level.

2. **Pharmacological validation**: Shows that fluoxetine's bidirectional effects on specific SRNs (downregulating Htr1a/Htr1b, upregulating Htr4) can be captured by the transcriptomic-neuroimaging approach, validating its utility for studying drug mechanisms.

3. **Behavioral relevance in humans**: Identifies two independent modes of population variation linking SRN functional connectivity to distinct behavioral phenotypes—Mode 1 (impulsivity/antisocial/aggression linked to HTR1A/HTR1F/HTR2C in amygdala/temporal cortex) and Mode 2 (negative reward bias/depression/panic linked to HTR1A/HTR4 in parietal/insula). This provides a mechanistic explanation for serotonin's "paradoxical" effects on behavior.

4. **Multivariate necessity**: Demonstrates that single-receptor analyses fail to capture behavior-SRN relationships; only multivariate approaches (CCA) reveal the admixture patterns that link receptor networks to behavior.

### Brain regions & systems

- **Dorsal raphe nucleus (DRN)**: Source of serotonin neurons; optogenetic stimulation site in mice; primary locus of serotonergic cell bodies
- **Amygdala**: High 5-HT2C receptor density; implicated in intertemporal choice processing; shows HTR1A/HTR1F/HTR2C SRN connectivity associations with delay discounting
- **Temporal cortex**: Shows HTR1A/HTR1F/HTR2C SRN functional connectivity associated with impulsivity/aggression phenotype (CCA Mode 1)
- **Parietal cortex**: Shows HTR1A/HTR4 SRN functional connectivity associated with reward processing/depression phenotype (CCA Mode 2)
- **Rolandic operculum/Insula**: Putative reward-related regions; show HTR1A/HTR4 SRN connectivity associated with slower reward responses and negative bias
- **Prefrontal cortex**: Implicated in impulsivity and behavioral control; receives serotonergic projections
- **Hippocampus**: Region with serotonergic innervation; implicated in memory and plasticity
- **Brain-wide networks**: SRNs characterized across the entire brain via transcriptomic-neuroimaging mapping; not restricted to specific anatomical loci but defined by receptor expression patterns

### Mechanistic insight

This paper meets the mechanistic insight bar. It provides both an algorithmic framework and neural data supporting specific computational mechanisms.

**Computational level**: The brain solves the problem of achieving diverse behavioral regulation through a single neuromodulator (serotonin) by leveraging heterogeneous receptor distributions as a basis set for decomposing and routing neuromodulatory signals to distinct functional networks.

**Algorithmic level**: The mechanism involves:
1. **Receptor-field encoding**: Brain regions express distinct admixtures of serotonin receptor types (HTR1A, HTR1F, HTR2C, HTR4, etc.), creating unique "receptor fingerprints"
2. **Network-level modulation**: DRN serotonin release differentially modulates these receptor networks (SRNs) based on their receptor composition—some networks increase activity (HTR2C, HTR1A), others decrease (HTR3A/B)
3. **Multivariate behavioral mapping**: Behavioral phenotypes emerge from specific combinations (admixtures) of SRN functional connectivity patterns, not single receptors—captured via CCA as orthogonal modes of population variation

**Implementational level**: The physical implementation involves:
- **Dorsal raphe nucleus**: Source of serotonin neurons with widespread projections
- **Receptor-specific circuitry**: Different receptor types (GPCRs vs. ionotropic 5-HT3) with distinct cellular effects and affinities
- **Fluoxetine mechanisms**: Bidirectional drug effects—downregulating 5-HT1A/1B autoreceptors (increasing serotonin availability) while upregulating 5-HT4 signaling (mediating antidepressant effects)
- **Amygdala and parietal circuits**: Key nodes where receptor-specific SRN connectivity patterns link to impulsivity (HTR1A/1F/2C in amygdala/temporal cortex) versus reward/depression phenotypes (HTR1A/4 in parietal/insula)

### Limitations & open questions

- **Correlational nature**: The transcriptomic-neuroimaging approach is correlational and cannot establish causal relationships
- **Gene expression limitations**: Uses transcriptomic atlases rather than direct protein measurements; limited by co-expression of different receptors and spatial resolution of gene expression maps
- **No individual receptor density variation**: Cannot capture individual differences in receptor densities that PET imaging could provide (though PET lacks the temporal dynamics and sample sizes needed for population studies)
- **DRN-only stimulation**: Focuses on dorsal raphe serotonin neurons; median raphe nucleus (MRN) also contributes to brain serotonin with complementary projection patterns
- **fMRI signal interpretation**: SRN fMRI signatures likely reflect complex receptor signaling transduction pathways and cross-neuromodulator cascade events; caution needed in interpreting underlying cellular mechanisms
- **Cross-species translation**: While the approach bridges mouse and human data, differences in receptor distributions and neuromodulatory mechanisms between species may limit direct translation
- **Open questions**: Whether genetic polymorphisms in serotonin receptors endow individual variation in SRNs; whether other neuromodulatory systems share similar organizational principles; how chronic versus acute drug effects differ in SRN modulation

### Connections & keywords

**Key citations:**
- Grandjean et al. (2019): Source of mouse ofMRI data used in the study
- Smith et al. (2015): Human Connectome Project data and positive-negative mode framework
- Dayan & Huys (2008): Computational framework for serotonin, inhibition, and negative mood
- Cools, Roberts & Robbins (2008): Serotoninergic regulation of emotional and behavioral control
- Deakin & Graeff (1991): 5-HT and mechanisms of defence (aversive processing theory)
- Lein et al. (2007); Hawrylycz et al. (2012): Allen Brain Institute transcriptomic atlases

**Named models or frameworks:**
- Serotonin Receptor Networks (SRNs): The core construct developed in this paper
- Transcriptomic-neuroimaging mapping: The methodological approach combining gene expression with fMRI
- Dual Regression (FSL DR): The statistical technique for extracting network time-courses and connectivity maps
- Canonical Correlation Analysis (CCA): The multivariate statistical framework linking SRNs to behavior
- Residualized DR-stage 1: The control analysis establishing specificity to serotonin receptors

**Brain regions:**
- Dorsal raphe nucleus (DRN)
- Amygdala
- Temporal cortex
- Parietal cortex
- Rolandic operculum
- Insula
- Prefrontal cortex
- Hippocampus
- Median raphe nucleus (MRN, discussed as related system)

**Keywords:**
serotonin, neuromodulation, serotonin receptor networks, transcriptomic-neuroimaging mapping, optogenetics-fMRI, dorsal raphe nucleus, fluoxetine, impulsivity, delayed reward discounting, depression, canonical correlation analysis, functional connectivity, cross-species translation, G protein-coupled receptors, 5-HT3 receptors
