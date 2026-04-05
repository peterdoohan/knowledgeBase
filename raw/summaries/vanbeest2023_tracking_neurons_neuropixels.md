---
source_file: vanbeest2023_tracking_neurons_neuropixels.md
title: Tracking neurons across days with high-density probes
authors: Enny H. van Beest, Célian Bimbard, Julie M. J. Fabre, Flóra Takács, Philip Coen, Anna Lebedeva, Kenneth Harris, Matteo Carandini
year: 2023
journal: bioRxiv preprint
paper_type: empirical
contribution_type: methodological
---

### One-line summary

UnitMatch, an open-access pipeline that tracks neurons across days using only average spike waveforms from high-density arrays like Neuropixels, reliably identifies the same neurons across weeks and reveals stable or plastic functional properties across brain regions.

### Background & motivation

Neural activity spans timescales from milliseconds to months. While two-photon imaging can track the same neurons across days, it misses fast timescales and is difficult to implement outside cortex or in multiple areas simultaneously. Chronic electrodes, especially high-density arrays like Neuropixels probes, offer the potential to record from hundreds of neurons across days with millisecond precision. However, existing methods for matching neurons across days do not scale to the vast amounts of data produced by multiple days of Neuropixels recordings. A new scalable approach was needed to track neurons across recordings without requiring concatenation of data files.

### Methods

- **Data collection**: 1,500+ recording sessions from 18 chronically implanted mice over up to 183 days using Neuropixels 1.0 and 2.0 probes in multiple brain regions (visual cortex, hippocampus, striatum, superior colliculus, retrosplenial cortex, thalamus, frontal cortex)
- **Spike sorting**: Each session independently spike sorted with Kilosort (including drift correction within sessions)
- **Quality control**: Well-isolated units selected using Bombcell quality metrics (21.9 ± 11.5% of units passed)
- **UnitMatch algorithm**: 5-step pipeline operating on average spatiotemporal spike waveforms:
  1. Extract 7 waveform parameters (spatial decay, amplitude, centroid, trajectory, distance, direction, weighted-average waveform)
  2. Compute 6 similarity scores (Decay, Waveform, Amplitude, Centroid, Volatility, Route) for all unit pairs
  3. Define putative matches using a data-driven threshold based on within-day cross-validation
  4. Apply drift correction by computing median centroid displacement across putative matches
  5. Train naïve Bayes classifier on similarity score distributions to output match probabilities
- **Validation with functional fingerprints**: Autocorrelograms, visual responses to natural images, and population coupling correlations used to validate tracking accuracy

### Key findings

- **Tracking performance**: UnitMatch found 31.3 ± 11.2% (median ± m.a.d., n = 446 day pairs) of units as matches across consecutive days in chronic recordings, compared to only 4.0 ± 2.8% in acute recordings where reinsertion made tracking unlikely (p < 10^-10)
- **Comparison to alternative methods**: UnitMatch agreed more closely with expert manual curation than spike sorting on concatenated recordings; Kilosort on stitched files tended to overestimate matches, especially with larger gaps between recordings
- **Functional stability validation**: 
  - Autocorrelogram correlations: AUC = 0.78 ± 0.01 across days (0.80 ± 0.01 within days), remaining stable over months (slope = -0.003 ± 0.049 per day)
  - Visual responses (natural images): AUC = 0.86 ± 0.02 across days (0.90 ± 0.02 within days), remaining stable (slope = -0.002 ± 0.009 per day)
  - Population coupling: AUC = 0.92 ± 0.01 across days (0.96 ± 0.01 within days), highly stable even across weeks/months (slope = -0.006 ± 0.030 per day)
- **Application to learning**: UnitMatch successfully tracked striatal neurons during a visuomotor operant learning task, revealing diverse response changes: some units developed visual responses with learning (gradually or abruptly), while others decreased their responses
- **Quality metrics predict matching success**: Unit matching success correlated with standard quality metrics including number of spikes, refractory period violations, peak amplitude, and drift amount; surprisingly, waveform duration and number of peaks also predicted success

### Computational framework

The paper employs a **naïve Bayes classifier** for probabilistic unit matching. The framework treats unit identification as a classification problem where the goal is to compute the posterior probability that two spike waveforms come from the same neuron given their similarity scores.

Key elements of the framework:
- **Feature extraction**: Seven waveform parameters are extracted from the spatiotemporal spike waveform (spatial decay, amplitude, centroid position, trajectory, distance, direction, weighted-average waveform shape)
- **Similarity metrics**: Six similarity scores are computed for each pair of units, each scaled 0-1 (1 = most similar): Decay (D), Waveform (W), Amplitude (A), Centroid (C), Volatility (V), and Route (R)
- **Classification**: A naïve Bayes classifier computes match probability using the probability distributions of similarity scores for putative matches versus non-matches, assuming conditional independence between scores
- **Drift correction**: A rigid transformation is applied to account for electrode drift between recordings, computed from the median centroid displacement of putative matches

The framework assumes that spike waveform shape is a stable, distinctive signature of individual neurons over time, and that similarity in waveform parameters provides evidence for identity matching.

### Prevailing model of the system under study

The prevailing understanding in the field, as laid out in the introduction, is that:
1. Chronic electrodes can record units with consistent spike waveforms across days, indicating they track the same neurons over time
2. Units can maintain distinctive firing properties (inter-spike interval distributions) and functional properties (sensory, cognitive, motor correlates) across days
3. However, functional properties are not necessarily constant and their variation is often the scientific question being investigated
4. High-density arrays like Neuropixels enable recording hundreds of neurons with spike waveforms measured at multiple sites, allowing robust drift correction
5. Current methods for matching neurons across days (e.g., concatenating recordings and spike sorting) do not scale to the large amounts of data from multiple days of Neuropixels recordings

The paper builds on this foundation by proposing a scalable post-sorting matching pipeline that avoids the need for concatenation.

### What this paper contributes

This paper makes the following key contributions to the field:

1. **A scalable, open-access pipeline for tracking neurons across days**: UnitMatch operates after independent spike sorting of each recording session, avoiding the computational and memory bottlenecks of concatenating multiple large Neuropixels recordings. It uses only average spike waveforms, making it applicable to any spike-sorted dataset without requiring access to individual spike times.

2. **Probabilistic matching framework**: Unlike binary matching approaches, UnitMatch provides a match probability for every possible pair of units, allowing users to set appropriate thresholds for their research questions and quantify uncertainty.

3. **Drift correction method**: The paper demonstrates a method for correcting electrode drift between recording sessions by computing the median centroid displacement of putative matches, improving matching accuracy across days.

4. **Extensive validation across multiple brain regions and timescales**: The paper validates UnitMatch using three distinct functional fingerprints (autocorrelograms, visual responses, population coupling) across 18 mice and multiple brain regions (visual cortex, hippocampus, striatum, superior colliculus, etc.) over timescales from days to months (up to 183 days).

5. **Demonstration of applicability to learning paradigms**: The paper shows UnitMatch can track neurons whose functional properties change during learning, illustrating its utility for studying neural plasticity.

6. **Benchmarking against existing methods**: The paper compares UnitMatch to concatenated spike sorting and expert manual curation, showing it performs more similarly to human experts while being faster and more scalable.

### Brain regions & systems

- **Visual cortex (V1)**: Primary site for validating functional stability using visual responses to natural images; neurons showed stable stimulus selectivity across days
- **Hippocampus (HC)**: Recorded alongside visual cortex; part of the general validation dataset
- **Dorsomedial striatum (DMS)**: Site for learning study; neurons showed task-related plasticity during visuomotor operant learning
- **Superior colliculus (SC)**: Part of the multi-region recording dataset
- **Retrosplenial cortex (RSP)**: Part of the multi-region recording dataset
- **Thalamus (THAL)**: Part of the multi-region recording dataset
- **Frontal cortex (FC)**: Part of the multi-region recording dataset
- **Striatum (STR)**: General striatum recordings as part of multi-region dataset

The paper demonstrates that UnitMatch works across diverse brain regions, with particularly detailed validation in visual cortex (functional stability) and striatum (learning-related plasticity).

### Mechanistic insight

This paper does **not** meet the high bar for mechanistic insight as defined in the skill instructions. The paper presents a methodological algorithm (UnitMatch) for tracking neurons across days, but it does not:

1. Present or formalize a computational algorithm that explains a neural phenomenon (e.g., how neural circuits perform a computation)
2. Provide neural data that specifically supports that algorithm over alternatives

What the paper does provide:
- **Algorithmic-level description**: A naïve Bayes classifier that uses spike waveform similarity to match units across recording sessions
- **Methodological validation**: The algorithm is validated using functional stability measures (autocorrelograms, visual responses, population coupling), but these serve as validation metrics rather than as evidence for a specific computational mechanism of brain function

The paper's contribution is primarily methodological—enabling longitudinal studies of neural activity—rather than providing mechanistic insight into how neural circuits perform computations. The functional fingerprints used for validation (ACG, visual responses, population coupling) are treated as stable signatures of neuron identity, not as algorithmic components of neural computation.

### Limitations & open questions

**Acknowledged limitations:**

1. **Declining match rates over time**: The number of units tracked declined with time, potentially due to recording quality degradation, uncorrected drift accumulation, neurons becoming silent or dying, or changes in waveform properties

2. **Quality-dependent performance**: Matching success depends on unit quality metrics (number of spikes, refractory period violations, peak amplitude, drift amount), meaning noisier units are less likely to be successfully tracked

3. **Waveform-based limitation**: UnitMatch relies exclusively on spike waveform shape, which assumes waveform stability. If waveforms change due to electrode movement or physiological plasticity, matching accuracy may degrade

4. **No ground truth**: The paper acknowledges that neither manual curation nor concatenated spike sorting can be considered ground truth, making absolute validation difficult

**Open questions raised:**

1. What is the relative contribution of different factors (recording quality, drift, cell death, waveform changes) to the decline in tracking success over time?

2. Can the algorithm be improved by incorporating additional features beyond waveform shape (e.g., inter-spike interval distributions)?

3. How does UnitMatch performance vary across different brain regions with different cell type compositions and firing patterns?

4. Can waveform-based tracking be combined with functional fingerprints to improve accuracy without circularity?

### Connections & keywords

**Key citations:**
- Steinmetz et al. 2021 (Neuropixels 2.0 probe development)
- Pachitariu et al. 2016 (Kilosort spike sorting)
- Jun et al. 2017 (Neuropixels 1.0)
- Juavinett et al. 2019; Luo et al. 2020; van Daal et al. 2021; Bimbard et al. 2023 (chronic Neuropixels implantation methods)
- Okun et al. 2016; Steinmetz et al. 2021 (prior concatenated spike sorting approaches)

**Named models or frameworks:**
- UnitMatch (the main pipeline developed in this paper)
- Kilosort (spike sorting algorithm)
- Bombcell (quality control pipeline)
- Naïve Bayes classifier (statistical framework for matching)

**Brain regions:**
- Visual cortex (V1)
- Hippocampus
- Dorsomedial striatum
- Superior colliculus
- Retrosplenial cortex
- Thalamus
- Frontal cortex
- Striatum

**Keywords:**
chronic electrophysiology, Neuropixels, unit matching, spike waveform, longitudinal recordings, drift correction, neuron tracking, high-density probes, spike sorting, population coupling, autocorrelogram, visual cortex, striatum, naïve Bayes classifier, open-source software
