---
source_file: bonacchi2020_data_architecture.md
title: Data architecture for a large-scale neuroscience collaboration
authors: Niccolò Bonacchi, Gaelle Chapuis, Anne Churchland, Kenneth D. Harris, Max Hunter, Cyrille Rossant, Maho Sasaki, Shan Shen, Nicholas Steinmetz, Edgar Y. Walker, Olivier Winter, Miles Wells
year: 2020
journal: bioRxiv (preprint)
paper_type: empirical
contribution_type: methodological
---

### One-line summary

The International Brain Laboratory presents a modular, open-source data architecture — comprising the Alyx electronic lab notebook, the ONE data access protocol, and a DataJoint analysis pipeline — that enables distributed neuroscience collaborations to contribute, access, and analyze large-scale neural and behavioral datasets.

---

### Background & motivation

Modern neuroscience faces three converging data management challenges: datasets are growing enormously (hundreds of neurons per session, plus video and behavioural streams); collaborations now span multiple institutions and countries, requiring immediate cross-site data access; and community norms increasingly demand public data sharing with rich metadata. Despite these pressures, most labs lack the infrastructure to manage data rigorously, standardised formats have not been widely adopted, and existing solutions do not scale to large distributed collaborations. The IBL, a 21-laboratory collaboration generating brain-wide neural recordings from mice performing a perceptual decision-making task, needed a purpose-built system to solve these problems at scale.

---

### Methods

This is a methods/software paper describing a deployed system rather than a hypothesis-driven experiment. The key components are:

- **Alyx** — a web-based electronic lab notebook and colony management system backed by a PostgreSQL relational database. Stores metadata (subjects, surgeries, experiments, file locations) and automatically registers data files; triggers nightly data transfer to a central server via Globus Online.
- **Open Neurophysiology Environment (ONE)** — a lightweight data access protocol with Python and MATLAB clients. Defines standardised "dataset types" (object.attribute naming, e.g. `spikes.times`) with guaranteed dimensions and units. Provides four core API functions: `search`, `load_dataset`, `load_object`, `list`. Supports a "ONE Light" variant for upload-to-figshare workflows without a backend database.
- **DataJoint pipeline** — a workflow management system integrating a relational database with automated analysis. Automatically ingests new data, runs behavioural analyses, and populates a web dashboard monitoring mouse training progress across the collaboration.
- **Supporting tools**: lossless electrophysiology compression (~3× ratio, faster than real-time); DeepLabCut for pose estimation; kilosort2 for spike sorting; Brainbox Python analysis library.
- **Scale at time of writing**: 16,000 behavioural sessions, ~400,000 files stored.

---

### Key findings

- The three-module architecture (Alyx / ONE / DataJoint) successfully enables distributed data contribution, access, and automated analysis across 10 geographically separated labs.
- ONE's dataset-type convention (object.attribute naming with cross-referencing via shared indices) provides a flexible, extensible data standard that generalises beyond IBL; ONE Light allows any lab to share data via figshare with no database infrastructure.
- The lossless electrophysiology compression algorithm achieves ~3× compression at ~4× faster than real-time compression and ~3× faster than real-time decompression on a 10-core workstation, enabling practical storage and transfer of Neuropixels recordings.
- The DataJoint-powered web dashboard enables real-time monitoring of behavioural training progress for all mice across the collaboration, lowering the barrier to data exploration for newcomers.
- Each module (Alyx, ONE, ONE Light, DataJoint pipeline, Brainbox) can be adopted independently by labs outside IBL, reducing the cost of adoption.

---

### Computational framework

Not applicable in the sense of a scientific computational model. The paper describes software engineering and data management infrastructure. No mathematical or computational model of neural computation is advanced.

---

### Prevailing model of the system under study

The paper does not study a neural system per se; it addresses the data management practices of the neuroscience field. The introduction characterises the status quo as relying on lab-local, ad hoc data storage that has not scaled with dataset size or collaboration complexity. Standardised formats (NWB) exist but have not been broadly adopted; no lightweight protocol for selective remote data access existed that was practical for distributed teams. The paper positions IBL's architecture as a concrete existence proof that scalable, open, modular data infrastructure is achievable.

---

### What this paper contributes

The paper provides a working, deployed solution to the data management challenge in large-scale collaborative neuroscience. Concretely: (1) Alyx demonstrates that a web-based lab notebook can achieve reliable, real-time metadata capture across geographically distributed sites; (2) the ONE standard establishes that a minimal, four-function API with typed dataset conventions is sufficient to abstract away file formats and network logistics while remaining extensible; (3) ONE Light lowers the barrier to data sharing to a simple file-naming and upload step; (4) the DataJoint pipeline shows that automated ingestion and web-based visualisation of incoming data can be built on top of these foundations. Together, these components represent a transferable template for how large neuroscience collaborations can organise their data infrastructure.

---

### Brain regions & systems

Not applicable as a primary focus. The data architecture is designed to store and provide access to brain-wide Neuropixels recordings across 270 sites in the mouse brain (IBL Brain-Wide Map), but the paper itself does not analyse or interpret neural data from any specific region. The Allen Common Coordinate Framework (CCF) is used for standardising electrode location metadata.

---

### Mechanistic insight

The paper does not meet the bar for this section. It is a software and infrastructure paper with no hypothesis about neural computation and no neural data presented. The criterion of formalising an algorithm that explains a neural phenomenon, supported by neural recordings, is not relevant here.

---

### Limitations & open questions

- The system as described in 2020 was still pre-public-release; quality control and manual curation were ongoing, with public data release planned for September 2020.
- The full architecture requires dedicated technical staff to maintain — a resource most individual labs do not have; the paper acknowledges this but does not fully resolve it.
- ONE's search capabilities in the ONE Light variant are simpler than in the full database-backed implementation, limiting discoverability.
- Long-term interoperability with NWB is flagged as desirable but not yet complete at time of writing; NWB export was only piloted by individual member labs.
- The modular design means different labs may adopt different subsets of the stack, potentially fragmenting interoperability across the broader community.
- Sustainability of the open-source tools beyond the IBL collaboration is not addressed.

---

### Connections & keywords

**Key citations**:
- Jun et al. 2017 (Nature) — Neuropixels probes
- Teeters et al. 2015 (Neuron) — Neurodata Without Borders (NWB)
- Ruebel et al. 2019 (bioRxiv) — NWB:N 2.0
- Yatsenko et al. 2015 (bioRxiv) — DataJoint
- Mathis et al. 2018 (Nature Neuroscience) — DeepLabCut
- Steinmetz et al. 2019 (Nature) — distributed networks for choice (used ONE Light for data sharing)
- International Brain Laboratory 2020 (bioRxiv) — companion behavioural methods paper
- Abbott et al. 2017 (Neuron) — IBL founding paper

**Named models or frameworks**:
- Alyx (electronic lab notebook / colony management system)
- Open Neurophysiology Environment (ONE)
- ONE Light
- DataJoint
- Brainbox (Python analysis library)
- Neurodata Without Borders (NWB)
- Allen Common Coordinate Framework (CCF)
- mtscomp (lossless electrophysiology compression)
- Globus Online (data transfer)
- kilosort2 (spike sorting)
- DeepLabCut (pose estimation)

**Brain regions**: None specifically analysed; Allen CCF coordinates used for electrode localisation.

**Keywords**: data architecture, neuroscience data management, electronic lab notebook, open data standard, Open Neurophysiology Environment, DataJoint, Neuropixels, large-scale collaboration, data sharing infrastructure, spike sorting pipeline, lossless compression, International Brain Laboratory
