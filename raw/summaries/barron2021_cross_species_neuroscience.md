---
source_file: "barron2021_cross_species_neuroscience.md"
paper_id: "barron2021_cross_species_neuroscience"
title: "Cross-species neuroscience: closing the explanatory gap"
authors: "Helen C. Barron, Rogier B. Mars, David Dupret, Jason P. Lerch, Cassandra Sampaio-Baptista"
year: 2021
journal: "Philosophical Transactions of the Royal Society B"
paper_type: "review"
contribution_type: "theoretical"
species: ["human"]
methods: ["calcium_imaging", "optogenetics", "electrophysiology", "neuropixels", "fmri", "representational_similarity_analysis", "computational_modeling"]
brain_regions: ["hippocampus", "visual_cortex"]
frameworks: ["reinforcement_learning", "temporal_difference_learning"]
keywords: ["krizhevsky_et_al_deep_neural_networks_visual_cortex_229", "kriegeskorte_et_al_rsa_framework_204", "207", "208", "rescorla_and_wagner", "schultz_et_al_td_learning_and_dopamine_215218", "jun_et_al_neuropixels_probes_79", "boto_et_al_wearable_opm_meg_10", "tolman_cognitive_maps_186", "brodmann_cytoarchitecture_across_species_112", "named_models_or_frameworks", "representational_similarity_analysis_rsa", "temporal_difference_td_learning_rescorlawagner_algorithm", "physiologically_based_pharmacokinetic_pbpk_modelling", "connectivity_blueprints_cross_species_mri_homology_mapping", "allometric_scaling", "brain_regions", "hippocampus", "inferotemporal_cortex_area_it", "primary_visual_cortex_v1"]
---

### One-line summary

A framework is proposed for closing the explanatory gap between macroscopic non-invasive measures of the human brain and microscopic invasive measures in animal models through a three-armed cross-species approach combining shared tools, shared behavioural assays, and common analytical spaces.

---

### Background & motivation

Contemporary neuroscience faces a fundamental explanatory gap: non-invasive methods (fMRI, MEG) available in humans capture only coarse macroscopic activity, while invasive electrophysiology and genetic tools in animals provide cellular and circuit-level resolution but are difficult to link to higher cognition. Because research laboratories tend to be species-specific, these two levels of description remain largely disconnected. The clinical cost of this gap is high — neuropsychiatric drugs have among the highest Phase III failure rates of any disease area — largely because preclinical animal findings fail to translate to human patients. The paper argues that preserved mammalian neural homology justifies and motivates a systematic cross-species programme to bridge this divide.

---

### Methods

This is a theoretical opinion piece/review; no original data are collected. The scope and synthesis method are:

- Narrative review of the state of non-invasive (fMRI, MEG, EEG) and invasive (electrophysiology, calcium imaging, optogenetics, axonal tracing) recording methods, including their capabilities and limitations.
- Review of evidence for structural and functional neural homology across mammals (genomics, cytoarchitecture, functional connectivity, place cells).
- Proposal and elaboration of a three-armed cross-species framework (different tools within a species; same tools across species; different tools across species with common analytical translation).
- Discussion of specific enabling technologies: cross-species MRI (including small-animal fMRI), virtual reality behavioural assays, representational similarity analysis (RSA), and computational modelling approaches (reinforcement learning, biophysical/pharmacokinetic models, deep neural networks).
- Discussion of translational implications for neuropsychiatric drug development.

---

### Key findings

As a theoretical opinion piece, the paper does not report empirical findings. Its key conclusions are:

- The explanatory gap between macro- and microscopic neuroscience is a structural consequence of species-specific laboratory practices, not an insurmountable biological barrier.
- Preserved homology of neuronal subtypes, microcircuit organisation, functional connectivity networks, and neural codes (e.g., place cells across rats, mice, bats, monkeys, and humans) broadly justifies cross-species inference.
- Three complementary approaches are identified: (1) simultaneous multi-modal recording within a species to calibrate non-invasive signals; (2) same-tool comparative studies across species (especially cross-species MRI); (3) different tools across species with quantitative translation into a common representational space.
- Representational similarity analysis (RSA) is highlighted as a method-agnostic framework that can compare representational geometry across fMRI and electrophysiology data — as demonstrated by matching representational structure in human and macaque inferotemporal cortex.
- Virtual reality behavioural assays provide species-appropriate but formally comparable tasks; wearable OPM-MEG now enables MEG during free movement, narrowing the gap with rodent paradigms.
- Reinforcement learning / temporal difference models provide the clearest existing example where a single computational account describes both single-unit dopamine activity in macaques and BOLD reward prediction error signals in humans.
- High neuropsychiatric drug failure rates are partly attributable to this translational gap; a cross-species infrastructure could help identify non-invasive biomarkers linked to microcircuit pathophysiology.

---

### Computational framework

The paper does not develop a single computational framework but reviews several that can serve as bridging tools:

- **Representational Similarity Analysis (RSA)**: Constructs representational dissimilarity matrices (RDMs) from multi-channel neural responses across conditions. The correlation between RDMs from different recording modalities or species quantifies shared representational geometry, abstracting away from modality-specific signal properties. This is the paper's primary recommended analytical bridge.
- **Temporal difference (TD) reinforcement learning**: A reward prediction error algorithm that has been successfully mapped onto both midbrain dopamine neuron spiking (animal electrophysiology) and BOLD signals in the human midbrain — the paper's showcase example of successful cross-species computational unification.
- **Biophysically plausible network models** and **physiologically based pharmacokinetic (PBPK) models**: Discussed as tools for translating cellular-level drug/physiological effects across species.
- **Deep neural networks**: Used as representational models of visual cortex with predictive power across human fMRI and macaque electrophysiology.

The underlying assumption shared by all these frameworks is that mammalian brains solve similar computational problems using conserved circuit motifs, making algorithmic descriptions transferable across species with appropriate scaling or mapping.

---

### Prevailing model of the system under study

The paper's introduction characterises the field as operating under a de facto species-silo model: human neuroscientists work with macroscopic non-invasive tools; animal neuroscientists work with microscopic invasive tools; and the two communities rarely formally relate their findings. The dominant assumption has been that the resolution limits of non-invasive methods are simply a permanent constraint on what can be known about the human brain at the circuit level, and conversely that the behavioural complexity achievable in rodent models is insufficient to probe higher cognition. Translational attempts in psychiatry have largely proceeded by constructing face-valid rodent disease models and expecting pharmacological findings to generalise, without a mechanistic framework linking animal circuit phenotypes to human imaging biomarkers.

---

### What this paper contributes

The paper formalises the explanatory gap as a solvable infrastructure problem rather than a fundamental barrier, and proposes a concrete three-armed strategy to address it. It establishes that: (a) mammalian neural homology is sufficiently deep to justify systematic cross-species comparison; (b) technical advances (cross-species MRI, wearable MEG, VR, optogenetics, neuropixels, cryo-coil small-animal MRI) now make the three-armed approach feasible; (c) RSA provides an existing method-agnostic tool for translating representational content across recording modalities and species; (d) the TD learning / dopamine case study shows that full cross-level integration is achievable in principle.

Key unresolved questions identified: how to handle the non-linear relationship between neural activity and the BOLD signal when cross-species comparisons depend on fMRI; how to perform spatial homology mapping for anatomically distant species (e.g., rodent vs. human) beyond simple one-to-one region labelling; how to achieve awake, freely-behaving small-animal fMRI at scale; and whether the representational correspondences demonstrated for visual cortex and hippocampus generalise to higher-order association areas.

---

### Brain regions & systems

- **Hippocampus** — central case study for cross-species comparison; place cells conserved across mammals; replay discussed as candidate for cross-species non-invasive measurement; pattern separation/completion models bridging circuit and fMRI levels.
- **Inferotemporal cortex (area IT)** — RSA demonstration comparing representational geometry in human fMRI and macaque electrophysiology.
- **Visual cortex (V1 and beyond)** — laminar fMRI and columnar fMRI discussed; gamma oscillations compared across human MEG and primate invasive recordings; deep neural network models of the visual hierarchy.
- **Midbrain dopamine system** — TD learning / reward prediction error as the canonical cross-species computational success story.
- **Primary somatosensory cortex** — somatotopic mapping used as example of non-invasive mapping with clinical relevance.
- **Default mode network** — cited as example of conserved large-scale functional connectivity across primates (macaque, chimpanzee, human).
- **Frontal and temporal cortex (arcuate fasciculus)** — cross-species tractography used to identify evolutionary specialisation.

---

### Mechanistic insight

The paper does not itself present new neural data or a novel algorithm, so it does not meet the bar for mechanistic insight as defined. It reviews the TD learning / dopamine case as an existing example that meets the bar (algorithm formalised, matched to electrophysiology in macaques and mice, and BOLD signal in humans), but this is cited literature rather than a contribution of the present paper. The paper's own contribution is a methodological and theoretical roadmap, not a mechanistic finding.

---

### Limitations & open questions

- The BOLD signal is an indirect, nonlinear index of neural activity; neurovascular coupling varies across species, brain regions, and anaesthetic states, complicating cross-species fMRI comparisons.
- Small-animal fMRI is predominantly conducted under anaesthesia, which alters baseline activity, cerebral blood flow, and BOLD contrast in species- and drug-specific ways.
- Electrophysiology is biased toward large spikes and samples only a spatial subset of neurons; RSA applied to such data may overlook representational information visible to other modalities.
- Spatial homology mapping between phylogenetically distant species (rodent–human) may require gene expression and connectivity data beyond simple anatomical atlases.
- The success of TD learning as a cross-species bridge may be exceptional; the paper acknowledges that similarly parsimonious models bridging cellular and macroscopic descriptions may be rare in other domains.
- Behavioural translation remains difficult for disorders with high-order cognitive or social components (schizophrenia, depression) where full rodent models are unrealistic.
- Publication bias in animal studies inflates apparent translational promise of preclinical drug findings.

---

### Connections & keywords

**Key citations:**
- Krizhevsky et al. (deep neural networks / visual cortex) [229]
- Kriegeskorte et al. — RSA framework [204, 207, 208]
- Rescorla & Wagner; Schultz et al. — TD learning and dopamine [215–218]
- Jun et al. — Neuropixels probes [79]
- Boto et al. — wearable OPM-MEG [10]
- Tolman — cognitive maps [186]
- Brodmann — cytoarchitecture across species [112]

**Named models or frameworks:**
- Representational Similarity Analysis (RSA)
- Temporal difference (TD) learning / Rescorla–Wagner algorithm
- Physiologically based pharmacokinetic (PBPK) modelling
- Connectivity blueprints (cross-species MRI homology mapping)
- Allometric scaling

**Brain regions:**
- Hippocampus
- Inferotemporal cortex (area IT)
- Primary visual cortex (V1)
- Midbrain dopamine system
- Primary somatosensory cortex
- Default mode network
- Frontal and temporal cortex / arcuate fasciculus

**Keywords:**
- cross-species neuroscience
- explanatory gap
- representational similarity analysis
- non-invasive neuroimaging
- small-animal fMRI
- neural homology
- BOLD signal / neurovascular coupling
- laminar fMRI
- optogenetics
- reward prediction error
- virtual reality behavioural assays
- neuropsychiatric drug translation
