---
source_file: "pachitariu2023_kilosort_spike_sorting.md"
paper_id: "pachitariu2023_kilosort_spike_sorting"
title: "Solving the spike sorting problem with Kilosort"
authors: "Marius Pachitariu, Shashwat Sridhar, Carsen Stringer"
year: 2023
journal: "bioRxiv (preprint, posted January 7, 2023)"
paper_type: "computational"
contribution_type: "methodological"
methods: ["electrophysiology", "neuropixels"]
keywords: ["solving", "spike", "sorting", "problem", "kilosort"]
key_citations: ["buccino2020_spikeinterface_spike_sorting"]
---

### One-line summary

This paper describes the full algorithmic lineage of the Kilosort spike-sorting framework (versions 1–4) and introduces Kilosort4, a GPU-accelerated Python implementation featuring a novel graph-based clustering algorithm that substantially outperforms all tested competitors across a range of simulated drift conditions.

---

### Background & motivation

Spike sorting — extracting the firing times of individual neurons from extracellular electrophysiology recordings — is a critical but difficult step in systems neuroscience. The two main obstacles are the non-stationarity of spike waveforms caused by probe drift (vertical movement of the electrode relative to tissue over the course of a recording) and the dense overlap of electrical fields from nearby neurons (the "collision problem"). Early automated algorithms required extensive manual curation due to imperfect clustering; improving automation while handling realistic drift patterns is the central goal of the Kilosort development effort. This paper also introduces a realistic simulation framework for benchmarking, which prior approaches lacked.

---

### Methods

- **Framework**: Kilosort4 is fully implemented in Python using PyTorch for GPU acceleration; previous versions (1–3) were MATLAB + CUDA.
- **Preprocessing pipeline** (applied on-demand per batch in K4): common average referencing, FIR temporal high-pass filtering (>300 Hz), local ZCA channel whitening, and drift correction via Gaussian kriging interpolation (inherited from Kilosort 2.5/Steinmetz et al. 2021).
- **Template deconvolution**: universal templates (46,080 for Neuropixels 1) are used for initial spike detection and PC feature extraction; a matching-pursuit algorithm iteratively detects and subtracts spike contributions to decontaminate overlapping spikes; background-subtracted PC features are passed to clustering.
- **Kilosort4 clustering — graph-based algorithm**:
  - Nearest-neighbor graph constructed with brute-force FAISS search over a subsampled landmark set (nsub = 25,000 per 40 µm probe section).
  - Bipartite graph formulation enables parallel GPU optimization of a modularity cost function.
  - Initialized with K-means++ (200 clusters); iterative neighbor reassignment to local minimum.
  - Hierarchical merging tree constructed by sweeping modularity resolution parameter γ; splits/merges decided by (1) bimodality of spike projection along regression axis and (2) refractoriness of cross-correlogram.
  - Global merges applied across probe sections using waveform cross-correlation.
- **Simulation framework**: realistic drift patterns (no drift, medium, high, fast, step, step-aligned) were generated using dense waveform banks extracted from 11 high-drift IBL Neuropixels recordings; 600 ground-truth single units + 600 multi-units added with realistic inter-spike intervals and amplitudes; background noise "unwhitened" with real whitening matrices.
- **Benchmark comparisons**: Kilosort 1–4 vs. IronClust, MountainSort4, SpyKING CIRCUS, SpyKING CIRCUS 2, HDSort, HerdingSpikes, Tridesclous2 — all run via SpikeInterface wrappers on identical simulations.

---

### Key findings

- Kilosort4 correctly identified the most units across all six drift conditions; in the no-drift case 526/600 ground-truth units scored above 0.8 (1 − FP − FN), and in the high-drift case 477/600 — compared to the next best algorithm (Kilosort 2.5/3 at ~320–460).
- On the step-drift condition (hardest), Kilosort4 recovered 43 units vs. 25–27 for Kilosort 2.5/3 and ≤11 for all other algorithms; using the aligned Neuropixels 2 site layout recovered this to 512 units.
- Kilosort 2, 2.5, 3, and 4 all outperformed every non-Kilosort algorithm in every condition; IronClust was the nearest non-Kilosort competitor (~50% recovery vs. 80–90% for Kilosort4).
- Algorithms without explicit drift correction (MountainSort4, SpyKING CIRCUS) matched IronClust at no/medium drift but degraded dramatically at high drift.
- Kilosort4's performance was nearly independent of ground-truth unit amplitude, firing rate, and spatial extent; several competing algorithms had strong amplitude-dependent performance degradation that was not recoverable by lowering detection thresholds.
- The bipartite graph formulation and landmark subsampling enabled Kilosort4 to scale to large recording durations with manageable compute, running in ~25 minutes per 45-minute recording on an RTX 3090.
- The graph-based clustering in Kilosort4 found more small clusters than direct Leiden/Louvain application by initializing with K-means++ and exploiting the well-behaved local minima of the neighbor-reassignment step.

---

### Computational framework

The paper's core contribution is algorithmic. The key frameworks are:

1. **Matching pursuit / generative model of extracellular recording**: the recorded voltage is modelled as a sum of scaled, shifted spike templates plus residual noise. Inference (spike detection) and learning (template estimation) proceed via an EM-style algorithm. Matching pursuit iteratively detects and subtracts spike contributions to identify overlapping spikes — the fundamental "collision" problem.

2. **Graph-based modularity clustering**: clusters are defined as stationary points of an iterative neighbor-reassignment algorithm that greedily optimizes a modularity cost function. Key variables: nearest-neighbor adjacency graph (N-by-nsub bipartite matrix), modularity score Q, resolution parameter γ. The framework assumes that neural spike features from distinct units form compact clusters separable by graph community structure, with refractoriness of autocorrelograms as a ground-truth constraint.

3. **Hierarchical merging tree**: a dendrogram over clusters constructed by sweeping γ from ∞ to 0; splits/merges tested by bimodality of 1D projections and refractory cross-correlogram statistics. This embeds neuroscience domain knowledge (refractory period) directly into the clustering decision boundary.

---

### Prevailing model of the system under study

The paper positions itself against the state of the field as of ~2016–2022. The prevailing understanding was:
- Spike sorting was a sequential pipeline (preprocessing → detection → clustering → post-processing) that could not be fully automated due to drift and collisions.
- Human curation via GUIs like Phy was a necessary final step; algorithms were designed to over-split so that curators could perform easier merges.
- Drift was a recognized key problem; Kilosort 2.5 (Steinmetz et al. 2021) had established drift correction via probe position estimation and spatial interpolation as the most effective available approach.
- Competing algorithms (IronClust, SpyKING CIRCUS, MountainSort) had closed much of the gap on simple (no-drift) recordings but lagged on high-drift conditions.
- Benchmarking was hampered by the lack of realistic ground-truth datasets: cell-attached recordings were short, low-drift, and biased toward large units; synthetic simulations did not capture realistic waveform shape changes across depths.

---

### What this paper contributes

The paper establishes three concrete advances:

1. **Kilosort4 as state-of-the-art**: graph-based clustering with a hierarchical merging tree and refractory-period splitting criteria substantially closes the gap between automated output and the theoretical maximum, particularly under difficult high- and step-drift conditions. The best previous algorithm (Kilosort 2.5) found ~53% of units under step drift; Kilosort4 finds ~72%, and the aligned probe configuration recovers ~85%.

2. **Complete algorithmic documentation**: for the first time, all algorithmic steps across Kilosort versions 1–4 are described in a single paper, including drift tracking (Kilosort 2), bimodal pursuit (Kilosort 2), recursive pursuit (Kilosort 3), and the new graph-based approach (Kilosort 4). This fills a major gap in the literature.

3. **Realistic simulation framework**: by using waveforms extracted from real high-drift recordings at multiple depth positions (not synthetically generated), the benchmark captures waveform shape changes that purely synthetic approaches miss. This framework is released as a resource for the community.

---

### Brain regions & systems

Not applicable in a strict anatomical sense. The paper operates at the level of extracellular electrophysiology signal processing and is agnostic to brain region — the method applies to any probe recording. Validation data were drawn from IBL Neuropixels recordings in mouse brain (unspecified regions) and from the Steinmetz "Single Phase 3" dataset (also mouse, unspecified region). The paper's contribution is at the measurement/instrumentation level of analysis rather than at the systems neuroscience level.

---

### Mechanistic insight

This paper does not meet the bar. It presents a spike-sorting algorithm — a signal-processing pipeline — rather than a mechanistic account of a neural computation. It does not formalize an algorithm that the brain uses, nor does it provide neural data linking the algorithm's variables to measured neural activity in any explanatory sense. The paper is entirely at the implementational/methodological level: it improves the fidelity with which single-unit activity can be extracted from raw electrophysiology, thereby enabling mechanistic studies by others, but does not itself constitute a mechanistic insight at any of Marr's three levels.

---

### Limitations & open questions

- **Tetrodes and Utah arrays**: drift correction requires a defined probe geometry with vertical spacing ≤40 µm; Kilosort4 is not applicable to tetrodes or Utah arrays without modification. Kilosort2 (drift tracking, no geometry required) may be preferable there.
- **Fast drift**: drift estimation uses 2-second bins; sub-second drift cannot be corrected by the estimation step, though clustering robustness partially compensates.
- **Step drift**: even Kilosort4 struggled significantly on step drift (non-aligned probe), recovering only ~7% of units; the aligned Neuropixels 2 configuration largely recovers performance, suggesting this is a probe geometry constraint rather than a fundamental algorithmic limit.
- **Chronic multi-day recordings**: step drift simulations are encouraging but the method has not been explicitly tested on recordings separated by days.
- **Cerebellar complex spikes**: variable waveform shapes are not well-modelled by a single template; specialized algorithms are needed.
- **Retinal arrays**: feasible but may require GPU RAM partitioning for very large arrays.
- **Simulation diversity**: waveform bank is 597 units from 11 recordings; whether this fully captures the diversity of real waveforms across brain areas, species, and probe types is unknown.
- **No human curation benchmark**: the paper does not report agreement between Kilosort4's automated output and expert-curated output, leaving the absolute quality of the automated results relative to curated results unquantified.

---

### Connections & keywords

**Key citations**:
- Pachitariu et al. 2016 (bioRxiv) — original Kilosort1
- Steinmetz et al. 2021 (Science) — Neuropixels 2.0 and drift correction
- International Brain Laboratory 2022 (bioRxiv) — IBL dataset used for waveform bank and benchmarking
- Rossant et al. 2016 (Nature Neuroscience) — Phy GUI
- Buccino et al. 2020 (eLife) — SpikeInterface unified benchmark platform
- Traag et al. 2019 (Scientific Reports) — Leiden algorithm
- Blondel et al. 2008 (J. Stat. Mech.) — Louvain algorithm
- Mallat & Zhang 1993 (IEEE) — matching pursuit
- Arthur & Vassilvitskii 2006 — K-means++
- Johnson et al. 2019 (IEEE) — FAISS neighbor search

**Named models or frameworks**:
- Kilosort (versions 1, 2, 2.5, 3, 4)
- Matching pursuit (template deconvolution)
- Bimodal pursuit algorithm
- Recursive pursuit (Kilosort3 clustering)
- Graph-based modularity clustering with bipartite neighbor reassignment
- Hierarchical merging tree
- ZCA (Zero Phase Component Analysis) whitening
- SpikeInterface (benchmarking platform)
- Phy (visualization/curation GUI)
- IronClust, MountainSort4, SpyKING CIRCUS (competitor algorithms)

**Brain regions**: Not applicable (method paper).

**Keywords**: spike sorting, extracellular electrophysiology, Neuropixels, probe drift, drift correction, template deconvolution, matching pursuit, graph-based clustering, modularity optimization, refractory period, spike waveform, GPU acceleration, PyTorch, simulation benchmark
