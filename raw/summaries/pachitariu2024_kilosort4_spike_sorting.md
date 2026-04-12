---
source_file: "pachitariu2024_kilosort4_spike_sorting.md"
paper_id: "pachitariu2024_kilosort4_spike_sorting"
title: "Spike sorting with Kilosort4"
authors: "Marius Pachitariu, Shashwat Sridhar, Jacob Pennington, Carsen Stringer"
year: 2024
journal: "Nature Methods"
paper_type: "computational"
contribution_type: "methodological"
methods: ["electrophysiology", "neuropixels"]
brain_regions: ["hippocampus", "hippocampus_ca1", "anterior_cingulate_cortex", "prelimbic_cortex", "striatum", "thalamus", "visual_cortex"]
keywords: ["spike", "sorting", "kilosort4"]
key_citations: ["buccino2020_spikeinterface_spike_sorting"]
---

### One-line summary

Kilosort4 is a spike-sorting framework using graph-based clustering with hierarchical merging trees that outperforms all prior algorithms on both static and drifting simulated recordings, correctly identifying neurons with low amplitudes and small spatial extents.

---

### Background & motivation

Spike sorting — extracting single-neuron firing times from extracellular electrophysiology recordings — is a critical but difficult problem in systems neuroscience. A key complication is non-stationarity: probe drift during recording causes spike waveforms to change over time, leading to errors in clustering. Prior Kilosort versions addressed drift but relied on scaled k-means or recursive pursuit clustering algorithms that left significant room for improvement, particularly for neurons with small amplitudes or under high-drift conditions. The field also lacked reliable benchmarking because biophysical simulations used previously produced unrealistic waveforms.

---

### Methods

- **Framework**: Kilosort4 is implemented in Python with PyTorch, enabling full GPU acceleration.
- **Preprocessing pipeline**: Common average referencing (CAR), temporal high-pass filtering (FIR approximation of Butterworth filter), channel whitening via local ZCA transform, and drift correction using linear interpolation of drift traces combined with kriging-based data alignment.
- **Template deconvolution**: A two-stage process — (1) simple predefined templates (46,080 for Neuropixels1) detect spikes and extract PC features; (2) learned templates are derived from clustering the initial detections and used in an iterative matching pursuit with background subtraction to decontaminate features from overlapping spikes.
- **Graph-based clustering with merging trees**: Applied twice (template learning and final assignment). Core steps: (i) nearest-neighbor graph construction using the FAISS library with landmark-based subsampling for speed; (ii) iterative neighbor reassignment optimising modularity (gamma=1) initialised with k-means++ to produce intentionally oversplit clusters; (iii) hierarchical merging tree traversed from high to low modularity threshold, with each potential merge tested against two criteria: bimodality of spike projections along the regression axis between subclusters, and absence of refractory period violations in the cross-correlogram.
- **Simulation benchmarking**: Two types of ground-truth simulation — hybrid (real recording background, real spike waveforms inserted at offset positions) and full (simulated 1/f noise + multi-unit activity background). Drift simulations used densely sampled electric fields from 11 high-drift IBL recordings to simulate five drift profiles: no drift, medium, high, fast, and step drift. Performance metric: score = 1 − FP − FN per unit, threshold of 0.8 used for binary classification as correctly sorted.
- **Ablation study**: Six ablations tested across all simulation conditions (no drift correction, rigid-only correction, no template deconvolution, no reclustering, no cross-correlogram information, no deconvolution for clustering features).
- **Competing algorithms evaluated**: IronClust, SpyKING CIRCUS, SpyKING CIRCUS2, MountainSort4, HDSort, HerdingSpikes — all run through SpikeInterface wrappers for consistency.

---

### Key findings

- Kilosort4 outperformed all other algorithms in every simulation condition (no drift, medium drift, high drift, fast drift, step drift, step drift with aligned sites).
- In the no-drift condition, Kilosort4 correctly identified 551/600 ground-truth units at score > 0.8; the best non-Kilosort algorithm (IronClust) found ~182.
- In high-drift conditions, Kilosort4 identified 502 units vs. ~59 for IronClust and fewer for algorithms lacking drift correction.
- The step drift condition (qualitatively similar to chronic chronic implant dynamics) was the condition where Kilosort4's advantage over Kilosort2.5 and 3 was largest.
- Kilosort4's high true-positive rate does not come at the cost of more false positives: false positive "good" unit counts were similar across Kilosort versions (roughly 50–100).
- Ablation results showed drift correction and template deconvolution are the most critical steps; cross-correlogram-based merges/splits are also important; nonrigid motion correction and deconvolution for feature extraction had smaller but consistent benefits.
- Biophysical simulations were found to produce unrealistic waveforms outside the distribution of real neurons, explaining why prior studies using them concluded Kilosort generated excessive false positives — an artefact of the benchmark, not the algorithm.
- IronClust was the next best algorithm, finding roughly 50% of units compared to Kilosort4's 80–90% in drift conditions.

---

### Computational framework

Kilosort4 uses a **graph-based modularity optimisation** framework for clustering. The core formalism:

- A k-nearest-neighbor graph is constructed over spike PC features in Euclidean space.
- The modularity cost function H = (1/2m) * sum_c [e_c - gamma * K_c^2 / 2m] is optimised, where m is total edges, e_c is intra-cluster edges, K_c is sum of degrees in cluster c, and gamma is a resolution parameter (set to 1 for the initial reassignment).
- Iterative node reassignment greedily moves nodes to improve modularity, converging at a local minimum; initialisation uses k-means++ with 200 clusters to seed the process.
- A hierarchical merging tree is then built by varying gamma from infinity to 0, recording the sequence of modularity-optimal merges; each proposed merge is accepted or rejected based on two domain-specific criteria (bimodal spike projections, non-refractory cross-correlograms).
- Template deconvolution uses a generative/reconstructive model (matching pursuit) to subtract overlapping spike contributions from extracted PC features, improving cluster separability.

Key assumptions: spikes from the same neuron form approximately Gaussian clusters in PC feature space after background subtraction; the two split/merge criteria (bimodality and cross-correlogram refractoriness) capture the dominant sources of error that human curators would identify.

---

### Prevailing model of the system under study

The paper's introduction frames the spike-sorting pipeline as consisting of four sequential stages: preprocessing, spike detection, clustering, and postprocessing. The dominant prior understanding was that non-stationarity (probe drift) is the primary challenge for sorting accuracy, that matching pursuit is the key innovation for handling spike collisions, and that template-based approaches require extensive manual curation because clustering is imperfect. The field had converged on drift correction (Kilosort2.5) as a necessary preprocessing step, but clustering remained the bottleneck. Prior work had used scaled k-means or recursive pursuit for clustering, with postprocessing merges/splits using bimodality and cross-correlogram criteria — but these were applied coarsely after template learning rather than as a principled hierarchical algorithm.

---

### What this paper contributes

Kilosort4 reframes the clustering step: rather than treating templates as putative final clusters, it discards templates after feature extraction and applies a more powerful graph-based algorithm to the decontaminated spike features. This separation of concerns — using templates only for detection and background subtraction, then clustering independently — allows stronger clustering algorithms to be applied without being constrained by the quality of template learning.

Concretely, the paper establishes that (1) graph-based modularity optimisation with intentional oversplitting followed by principled merging substantially outperforms k-means-based or recursive-pursuit clustering; (2) realistic simulation benchmarking (using real electric field profiles from drifting recordings) is necessary to fairly evaluate spike sorters, and biophysical simulation benchmarks are unreliable; and (3) the step drift condition — relevant for chronic implant experiments — is where algorithmic improvements matter most.

The paper also clarifies the relative importance of each algorithmic component through ablation: drift correction is indispensable, template deconvolution is critical, CCG-based merges are important, and nonrigid motion correction provides modest additional benefit.

---

### Brain regions & systems

Not applicable as the paper's primary focus. Recordings used for validation span multiple regions (visual cortex, hippocampus, thalamus, anterior cingulate cortex, prelimbic cortex, lateral septal nucleus, striatum, corpus callosum, olfactory bulb, CA1, somatosensory cortex, etc.), but these serve only as data sources for benchmarking — no anatomical claims are made about any specific region.

---

### Mechanistic insight

The paper does not meet the bar. It presents and formalises a spike-sorting algorithm (graph-based clustering with hierarchical merging trees) and validates it against ground-truth simulated data, but does not provide neural data that specifically supports the algorithm's specific computational choices over alternatives. The validation is engineering benchmarking rather than mechanistic neuroscience: it demonstrates that the algorithm recovers more units with fewer errors, but does not link any component of the algorithm to a specific neural mechanism or compare model predictions against measured neural activity patterns.

---

### Limitations & open questions

- **Tetrode and Utah array data**: Kilosort4 is not well suited to probes without a well-defined linear geometry or with large inter-electrode spacing (>40 µm), limiting applicability to older recording technologies.
- **Retinal arrays**: Large arrays with thousands of electrodes may exceed GPU RAM and require splitting into sections.
- **Fast drift**: The 2-second bin size used for drift estimation cannot be reduced below a minimum required for reliable estimation, leaving fast drift (sub-2-second timescales) only partially corrected; performance remains acceptable but the limitation is acknowledged.
- **Chronic recordings**: The step drift simulation is encouraging for multi-day chronic implant use cases, but this has not been explicitly validated.
- **Nonrigid motion correction**: The ablation shows this step has smaller-than-expected benefit, possibly because other steps redundantly compensate; the conditions under which nonrigid correction is critical remain unclear.
- **Manual curation**: Even with Kilosort4's improvements, the authors recommend continued manual quality checking in Phy, implying that fully automated spike sorting is not yet reliable in all conditions.
- **Future probe designs**: The authors note that probe design decisions have historically been influenced by computational requirements (e.g., Neuropixels2's aligned sites and reduced vertical spacing motivated by drift correction needs), raising the open question of what design changes would most benefit algorithmic sorting.

---

### Connections & keywords

**Key citations**:
- Pachitariu et al. 2016 (Kilosort1, bioRxiv) — original Kilosort framework
- Steinmetz et al. 2021 (Neuropixels 2.0, Science) — drift correction methodology
- Buccino et al. 2020 (SpikeInterface, eLife) — unified spike-sorting benchmarking framework
- International Brain Laboratory et al. 2022 (IBL dataset, bioRxiv) — primary benchmarking dataset
- Traag, Waltman & Van Eck 2019 (Leiden algorithm, Sci. Rep.) — graph clustering reference
- Rossant et al. 2016 (Phy, Nat. Neurosci.) — manual curation visualization tool
- Newman & Girvan 2004 (modularity, Phys. Rev. E) — modularity cost function foundation

**Named models or frameworks**:
- Kilosort (versions 1, 2, 2.5, 3, 4)
- SpikeInterface
- Phy (visualisation/curation GUI)
- Leiden algorithm, Louvain algorithm
- ZCA (zero-phase component analysis) whitening
- Matching pursuit (template deconvolution)
- Hybrid ground-truth simulation

**Brain regions**: Visual cortex, hippocampus, thalamus, anterior cingulate cortex, prelimbic cortex, lateral septal nucleus, striatum, corpus callosum, olfactory bulb, CA1, somatosensory cortex (all used as benchmarking data sources only)

**Keywords**: spike sorting, Kilosort4, graph-based clustering, modularity optimisation, merging tree, template deconvolution, matching pursuit, probe drift correction, Neuropixels, extracellular electrophysiology, ground-truth simulation, benchmark
