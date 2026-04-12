---
source_file: liu2022_hippocampal_sharp_wave.md
paper_id: liu2022_hippocampal_sharp_wave
title: "A consensus statement on detection of hippocampal sharp wave ripples and differentiation from other fast oscillations"
authors:
  - "Anli A. Liu"
  - "Simon Henin"
  - "Saman Abbaspoor"
  - "Anatol Bragin"
  - "Elizabeth A. Buffalo"
  - "Jordan S. Farrell"
  - "David J. Foster"
  - "Loren M. Frank"
  - "Tamara Gedankien"
  - "Jean Gotman"
  - "Jennifer A. Guidera"
  - "Kari L. Hoffman"
  - "Joshua Jacobs"
  - "Michael J. Kahana"
  - "Lin Li"
  - "Zhenrui Liao"
  - "Jack J. Lin"
  - "Attila Losonczy"
  - "Rafael Malach"
  - "Matthijs A. van der Meer"
  - "Kathryn McClain"
  - "Bruce L. McNaughton"
  - "Yitzhak Norman"
  - "Andrea Navas-Olive"
  - "Liset M. de la Prida"
  - "Jon W. Rueckemann"
  - "John J. Sakon"
  - "Ivan Skelin"
  - "Ivan Soltesz"
  - "Bernhard P. Staresina"
  - "Shennan A. Weiss"
  - "Matthew A. Wilson"
  - "Kareem A. Zaghloul"
  - "Michaël Zugaro"
  - "György Buzsáki"
year: 2022
journal: "Nature Communications"
paper_type: review
contribution_type: methodological
species:
  - human
brain_regions:
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - amygdala
keywords:
  - sharp_wave_ripple_spw_r
  - high_frequency_oscillation_hfo
  - hippocampal_memory_consolidation
  - pathological_ripple_p_ripple
  - interictal_epileptiform_discharge_ied
  - laminar_electrode_recording
  - closed_loop_stimulation
  - gamma_oscillation_broadband_high_frequency_activity
  - ripple_detection_threshold
  - machine_learning_event_classification
  - translational_neurophysiology
  - cholinergic_modulation_of_oscillations
  - consensus
  - statement
  - detection
  - hippocampal
  - sharp
  - wave
  - ripples
  - differentiation
key_citations:
  - fernandez2019_ripples_memory_consolidation
  - girardeau2009_ripples_spatial_memory
---

### One-line summary

A consensus statement from over 30 neuroscientists identifying six core methodological problems in hippocampal sharp wave ripple (SPW-R) detection and offering practical recommendations to standardise recording, detection, and reporting across species.

---

### Background & motivation

Hippocampal sharp wave ripples (SPW-Rs) are the most synchronous network pattern in the mammalian brain, implicated in memory consolidation, working memory, and replay of experience. Decades of rodent work have established their functional necessity, and recent human intracranial EEG studies have extended these findings to episodic and semantic memory. However, recording, detection, and reporting methods differ substantially across and within laboratories, likely driving much of the variance in published findings. This consensus statement, produced collaboratively by rodent, primate, and human SPW-R researchers, aims to identify key sources of variability and provide shared standards as a foundation for translational discovery.

---

### Methods

This is a narrative review and consensus paper, not an original data collection study.

- Scope: rodent, non-human primate, and human intracranial EEG (iEEG) literature on hippocampal SPW-Rs and related high-frequency oscillations (HFOs).
- Synthesis method: expert consensus from a meeting of more than 30 active SPW-R researchers; supplemented by review of published methods tables (Supplementary Table S1) cataloguing detection parameters across studies.
- Six problem areas are identified and discussed in sequence: (1) artifact rejection, (2) electrode configuration and detection thresholds, (3) arousal and behavioral state confounds, (4) extra-CA1 ripple-like events, (5) overlap with gamma oscillations and broadband activity, and (6) separation from pathological ripples (p-ripples) in epilepsy patients.
- Recommendations are issued for experimental design, automated detection, feature reporting, and data/code sharing.

---

### Key findings

- Detection parameters (bandpass filter range, amplitude threshold, duration threshold) vary so widely across studies that reported SPW-R rates differ by up to two orders of magnitude (0.01 to >10 Hz).
- SPW-R frequency band criteria differ by species: rodents 100–250 Hz, monkeys 95–250 Hz, humans 70–250 Hz (most use 80–150 Hz); this species difference may partly be biological (slower ripple frequency in primates, ~110–125 Hz) and partly methodological.
- Inclusion or exclusion of the sharp wave component in detection criteria dramatically changes event counts (e.g., 1.9 events/min with sharp wave required vs. 10–40 events/min without).
- Muscle artifacts, locally recorded action potentials, and filtered line noise are major sources of false positives; current source density (CSD) from multi-site laminar recordings is the gold standard for eliminating them.
- SPW-Rs in rodents and monkeys are strongly anti-correlated with cholinergic tone and are suppressed during high arousal, whereas gamma oscillations are enhanced; this physiological distinction can be used to separate the two event types.
- Chandelier and O-LM interneurons are silent during SPW-Rs but fire with gamma; ripple power in the CA1 pyramidal layer is negatively correlated with gamma power in dendritic layers, providing an additional mechanistic criterion for separation.
- Pathological ripples (p-ripples) overlap with physiological SPW-Rs in frequency (80–200 Hz) and cannot be reliably distinguished by amplitude or frequency alone; spectral variability, proximity to the epileptogenic zone, and phase relationship to NREM slow oscillations are more useful discriminators.
- Machine learning approaches (RNN/LSTM, CNNs, unsupervised clustering on spectral features) outperform simple threshold methods and are recommended for automated detection, including real-time closed-loop applications.
- Key recommendations: (a) localise electrodes to CA1 pyramidal layer; (b) compare task-detected ripples to NREM SPW-Rs as a benchmark; (c) report distribution of SPW-R features rather than means; (d) share curated datasets and detection code; (e) assign confidence scores to detected events.

---

### Computational framework

Not applicable in a strict sense — the paper does not develop or apply a formal computational model. It does, however, engage with signal-processing frameworks (bandpass filtering, CSD analysis, wavelet transforms, power spectral density) and machine learning methods (supervised: RNN/LSTM, CNN; unsupervised: spectral clustering) as tools for event detection and classification. The paper implicitly frames SPW-R detection as a classification problem under uncertainty, and calls for probabilistic confidence scoring rather than binary threshold decisions. The results described constrain future computational models of hippocampal memory replay by emphasising the importance of distinguishing SPW-Rs from gamma bursts and p-ripples before attributing cognitive functions to detected events.

---

### Prevailing model of the system under study

The introduction grounds the paper in a well-established model of SPW-Rs as the brain's primary mechanism for offline memory consolidation and prospective planning. CA3 pyramidal neurons generate a synchronous volley targeting CA1 str. radiatum, triggering large transmembrane currents (the sharp wave) and exciting CA1 interneurons; their interaction produces the ripple oscillation (110–180 Hz in rodents). During SPW-Rs, compressed forward and reverse spike sequences replay past experience and prospectively recombine trajectories. SPW-Rs are absent during theta-dominated active states and are suppressed by cholinergic neuromodulation; they dominate quiescent and NREM sleep states. This framework, developed primarily in rodents, is assumed to generalise to primates, though human iEEG evidence is more recent and methodologically less controlled.

---

### What this paper contributes

The paper does not generate new experimental data; its contribution is methodological. It establishes, through community consensus, that the variance in published SPW-R findings across laboratories is substantially attributable to inconsistent recording and detection practices rather than biology alone. It provides a structured taxonomy of six distinct sources of methodological error or ambiguity — artifacts, threshold variability, state confounds, anatomical specificity, gamma/SPW-R conflation, and pathological contamination — and maps specific recommendations onto each. For translational work specifically, it identifies the conflation of high gamma broadband activity with SPW-Rs as a particularly consequential unresolved issue: many human iEEG "ripple" detections may reflect fast gamma or p-ripples rather than true CA1 pyramidal-layer SPW-Rs. The paper establishes NREM sleep SPW-Rs as a necessary positive control for cognitive-task ripple detection, and recommends macro-micro electrode combinations and concurrent unit recordings as the standard for verifying event identity in humans.

---

### Brain regions & systems

- **Hippocampal CA1 pyramidal layer** — primary locus of SPW-R generation; ripple oscillations are largest and most reliably recorded here; the definitive recording target for SPW-R studies.
- **Hippocampal CA3** — source of the synchronous excitatory input (sharp wave) that triggers CA1 ripples; CA3/CA2 volley is the pacemaker of the SPW-R complex.
- **Hippocampal CA2** — can independently trigger SPW-R variants with inverted polarity (negative SPW in str. oriens); a minority source of SPW-R initiation.
- **Dentate gyrus** — generates fast oscillations distinct from CA1 ripples; theta phase-locked gamma at 100–150 Hz present in molecular layer; must be distinguished from CA1 ripples.
- **Subiculum / entorhinal cortex** — CA1-coupled ripples extend into subicular-entorhinal axis but with decreasing amplitude; often inadvertently included in human electrode placements.
- **Neocortex (lateral temporal, precuneus, medial prefrontal cortex — default mode network)** — site of ripple-coupled fast oscillations (80–120 Hz) during memory tasks; coupled to hippocampal SPW-Rs but generated by distinct mechanisms.
- **Lateral septum, amygdala, piriform cortex, parietal cortex** — reported sites of SPW-R-coupled fast oscillations in rodents; included as context for the discussion of ripples outside CA1.

---

### Mechanistic insight

The paper meets criterion 1 (it describes the algorithm of SPW-R generation: CA3 synchronous volley → CA1 dendritic depolarisation and interneuron recruitment → pyramidal-interneuron interaction → ripple oscillation) and partially meets criterion 2 (it cites extensive neural data from rodents and primates including laminar recordings, CSD analysis, unit recordings, and optogenetics). However, as a review/consensus paper it does not itself present original neural data linking a specific algorithm to measured activity; it synthesises existing evidence.

The mechanistic content that is well-supported by cited data can be mapped as follows:

- **Computational**: the brain replays and recombines past experience offline to consolidate memory, select future actions, and support generalisation — a function requiring coordinated, compressed sequential reactivation of distributed cell assemblies.
- **Algorithmic**: SPW-Rs implement this by synchronising a large fraction of the CA1 pyramidal population within ~100 ms windows; forward and reverse spike sequences are compressed ~20x relative to real-time; interneuron–pyramidal cell interactions pace the oscillation and control recruitment timing.
- **Implementational**: the ripple is physically generated by fast perisomatic inhibitory currents (positive LFP domes in pyramidal layer) interleaved with synchronous population spikes (sharp negative troughs); chandelier and O-LM interneurons are excluded during SPW-Rs; acetylcholine levels modulate SPW-R vs. gamma dominance via medial septal cholinergic projections; CA2 pyramidal neurons can independently initiate SPW-R variants. The distinction from gamma is supported by cell-type-specific firing patterns and layer-specific CSD profiles.

The paper does not present new data specifically supporting one algorithm over alternatives; it reviews and synthesises existing support. The mechanistic account is well-grounded but second-hand.

---

### Limitations & open questions

- It remains unresolved whether many putative human iEEG "ripples" detected during cognitive tasks are true CA1 pyramidal-layer SPW-Rs or instead fast gamma bursts, broadband HFO, or p-ripples.
- The discrepancy in the temporal relationship between SPW-Rs and behavior across species (rodents: post-exploration; macaques: pre-retrieval; humans: pre-conscious recall) is unexplained; proposed accounts (fragmented theta in primates, different cholinergic dynamics) are conjectural.
- Whether SPW-Rs in the ventral hippocampus can occur during attentive behavior has not been systematically studied.
- The performance of supervised and unsupervised machine learning detectors relative to threshold methods has not been benchmarked in a standardised comparison.
- The biological vs. methodological contribution to the apparently shorter SPW-R duration in humans compared to rodents has not been resolved.
- Real-time, closed-loop SPW-R detection in humans remains unreliable; current filter-based methods detect only ~50% of larger-amplitude events.
- Whether detected neocortical "ripples" share generative mechanisms with hippocampal SPW-Rs, or represent a functionally distinct class of fast oscillation, requires further investigation.
- Shared, curated, publicly available datasets and a community-validated detection algorithm do not yet exist; the paper calls for their development.

---

### Connections & keywords

**Key citations**:
- Buzsáki (2015) — comprehensive review of SPW-R function (Hippocampus 25:1073–1188)
- Joo & Frank (2018) — SPW-R in memory retrieval and consolidation (Nat Rev Neurosci 19:744–757)
- Fernandez-Ruiz et al. (2019) — long-duration SPW-Rs improve memory (Science 364:1082–1086)
- Norman et al. (2019) — human hippocampal ripples linked to visual episodic recollection (Science 365)
- Norman et al. (2021) — hippocampal ripples and default mode network during recollection (Neuron 109)
- Vaz et al. (2019) — coupled ripples between MTL and neocortex in human memory retrieval (Science 363)
- Zhang et al. (2021) — cholinergic suppression of SPW-Rs impairs working memory (PNAS 118)
- Girardeau et al. (2009) — selective suppression of ripples impairs spatial memory (Nat Neurosci 12)
- Stark et al. (2014) — pyramidal cell–interneuron interactions underlie ripple oscillations (Neuron 83)

**Named models or frameworks**:
- Sharp wave ripple (SPW-R) complex
- Current source density (CSD) analysis
- Closed-loop perturbation / real-time ripple detection
- Pathological ripple / high-frequency oscillation (HFO) framework (epilepsy)
- RNN/LSTM and CNN detection algorithms

**Brain regions**:
- Hippocampal CA1 (pyramidal layer, str. radiatum, str. oriens)
- Hippocampal CA2, CA3
- Dentate gyrus
- Subiculum, entorhinal cortex
- Neocortex: lateral temporal cortex, precuneus, medial prefrontal cortex (default mode network)
- Lateral septum, amygdala, piriform cortex

**Keywords**:
- sharp wave ripple (SPW-R)
- high-frequency oscillation (HFO)
- hippocampal memory consolidation
- pathological ripple (p-ripple)
- interictal epileptiform discharge (IED)
- laminar electrode recording
- closed-loop stimulation
- gamma oscillation / broadband high-frequency activity
- ripple detection threshold
- machine learning event classification
- translational neurophysiology
- cholinergic modulation of oscillations
