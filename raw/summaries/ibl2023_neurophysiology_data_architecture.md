---
source_file: "ibl2023_neurophysiology_data_architecture.md"
paper_id: "ibl2023_neurophysiology_data_architecture"
title: "A modular architecture for organizing, processing and sharing neurophysiology data"
authors: "The International Brain Laboratory, Niccol\u00f2 Bonacchi, Gaelle A. Chapuis, Anne K. Churchland, Eric E. J. DeWitt, Mayo Faulkner, Kenneth D. Harris, Julia M. Huntenburg, Max Hunter, In\u00eas C. Laranjeira, Cyrille Rossant, Maho Sasaki, Michael M. Schartner, Shan Shen, Nicholas A. Steinmetz, Edgar Y. Walker, Steven J. West, Olivier Winter, Miles J. Wells"
year: 2023
journal: "Nature Methods"
paper_type: "empirical"
contribution_type: "methodological"
species: ["mouse"]
methods: ["electrophysiology"]
keywords: ["modular", "architecture", "organizing", "processing", "sharing", "neurophysiology", "data"]
---

### One-line summary

The International Brain Laboratory describes a modular, four-component data management and sharing architecture (Alyx, ONE, DataJoint pipelines, Globus integration) that enables individual laboratories and large collaborations to organise, integrate, and share large-scale neurophysiology datasets.

---

### Background & motivation

Large-scale neurophysiology increasingly requires managing hundreds of gigabytes per experiment across multiple recording modalities and multiple laboratories. Existing tools did not support the combination of within-lab colony management, cross-lab data integration, automated preprocessing, and standardised programmatic access needed by distributed collaborations such as the IBL. The paper addresses the gap between bespoke per-lab solutions and the need for a scalable, standards-based system that also accommodates public data sharing.

---

### Methods

- **System design**: Four modular components are described: (1) Alyx — a relational database with a web GUI and REST API linking colony management, metadata, and electronic lab notebooks to experimental data files; (2) ONE (Open Neurophysiology Environment) — a filename and API convention for organising and sharing data files locally and remotely; (3) a distributed task-management system for automated preprocessing (spike sorting, video analysis) that uses member-lab compute nodes queried via HTTP; (4) DataJoint-based automated higher-level analysis pipelines that populate a public-facing website.
- **Data compression**: A threefold lossless compression algorithm was developed for large electrophysiology files.
- **Validation example**: A random forest classifier was trained to predict mouse training time (grouped into quartiles) from behavioural, subject, ambient, and institute-specific features collected across 116 mice from multiple IBL labs. Classification accuracy was evaluated by tenfold cross-validation (F1 score), and feature importance was assessed by permutation testing.
- **Interoperability**: Adapters to Neurodata Without Borders (NWB) and DataJoint are provided; comparison with other sharing systems given in supplementary material.

---

### Key findings

- The full IBL data pipeline successfully integrated data from multiple international laboratories into a single searchable, versioned central store accessible via a unified API.
- A random forest classifier trained on all available features predicted training-time quartile at approximately twice the accuracy of a shuffled-label baseline.
- A single feature — task performance change across the first five training sessions — was overwhelmingly the most important predictor; a classifier using only this feature achieved nearly the same accuracy as the full model (the full model showed only a 14% accuracy increase).
- Age was the only non-task-performance feature with predictive value; site-specific variables (food protein content, humidity) were not important.
- The modular architecture allows components to be adopted independently by single laboratories or by large collaborations.

---

### Computational framework

Not applicable as a formal computational or theoretical framework. The paper is a methods/infrastructure contribution. The validation analysis uses a random forest classifier and permutation-based feature importance — standard machine learning tools applied to predict a behavioural outcome variable. No model of neural computation is proposed or formalised.

---

### Prevailing model of the system under study

The paper's introduction frames the problem as a data-management and infrastructure challenge rather than a scientific question about a neural system. The assumed baseline is a landscape of per-lab, ad-hoc data organisation tools that are not interoperable across institutions or recording modalities. The IBL's own prior work (IBL 2021, eLife) established a standardised behavioural task; the present paper addresses the underlying data infrastructure that makes multi-lab reproducibility possible. No computational model of a brain system is assumed or challenged.

---

### What this paper contributes

This paper establishes a working, openly available data infrastructure that enables multi-laboratory neurophysiology at scale. Before this contribution, no established standard existed for linking colony metadata, raw electrophysiology files, preprocessing pipelines, and programmatic sharing within one unified system. The IBL architecture makes it tractable to run cross-lab analyses (as demonstrated by the training-time prediction example) and sets a precedent and toolchain for future large-scale collaborative neuroscience.

---

### Brain regions & systems

Not applicable. The paper is a methods and infrastructure contribution. The neurophysiology data it manages are from mouse decision-making experiments (visual discrimination task), but no specific brain region is analysed or discussed in the paper body. The level of analysis is entirely at the level of data organisation and behavioural metadata.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight. It presents no algorithm for explaining a neural or psychological phenomenon, and provides no neural recordings, imaging, or pharmacological data. The validation analysis is a proof-of-concept for the data infrastructure, not an investigation of neural mechanisms.

---

### Limitations & open questions

- Manual curation of the full dataset is still required before public release; automated quality control is not yet complete.
- The preprocessing and quality-control methods are described as still evolving, meaning file versioning and pipeline stability are ongoing concerns.
- The training-time prediction example uses only 116 mice; generalisability across task variants or species is untested.
- The architecture was designed around the IBL's specific workflow; adaptation to substantially different experimental paradigms (e.g., human neuroimaging, calcium imaging at large scale) may require additional work.
- The paper does not address long-term archival, data versioning conflicts, or governance of the central Alyx server.

---

### Connections & keywords

**Key citations**:
- The International Brain Laboratory (2021), eLife — standardised decision-making task in mice
- Rübel et al. (2022), eLife — Neurodata Without Borders (NWB) ecosystem
- Teeters et al. (2015), Neuron — Neurodata Without Borders original format
- Yatsenko et al. (2015), bioRxiv — DataJoint
- Foster (2011), IEEE Internet Computing — Globus Online
- Urai et al. (2021), eNeuro — citric acid water alternative to water restriction

**Named models or frameworks**:
- Alyx (relational database / electronic lab notebook system)
- ONE (Open Neurophysiology Environment) — filename and API convention
- DataJoint — automated analysis pipeline framework
- Globus Online — bulk data transfer
- Neurodata Without Borders (NWB) — neurophysiology data standard
- Random forest classifier (used in validation example)

**Brain regions**: None (not applicable).

**Keywords**: neurophysiology data management, open neurophysiology environment, modular data architecture, multi-laboratory collaboration, International Brain Laboratory, data sharing, electronic laboratory notebook, spike sorting pipeline, DataJoint, Neurodata Without Borders, behavioural training prediction, random forest classifier
