---
source_file: gabriel2022_behaviordepot_detection.md
paper_id: gabriel2022_behaviordepot_detection
title: "BehaviorDEPOT is a simple, flexible tool for automated behavioral detection based on markerless pose tracking"
authors:
  - "Christopher J Gabriel"
  - "Zachary Zeidler"
  - "Benita Jin"
  - "Changliang Guo"
  - "Caitlin M Goodpaster"
  - "Adrienne Q Kashay"
  - "Anna Wu"
  - "Molly Delaney"
  - "Jovian Cheung"
  - "Lauren E DiFazio"
  - "Melissa J Sharpe"
  - "Daniel Aharoni"
  - "Scott A Wilke"
  - "Laura A DeNardo"
year: 2022
journal: eLife
paper_type: empirical
contribution_type: methodological
species:
  - mouse
  - rat
tasks:
  - t_maze
methods:
  - calcium_imaging
  - optogenetics
  - behavioral_analysis
brain_regions:
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - prelimbic_cortex
keywords:
  - markerless_pose_estimation
  - behavioral_classification
  - heuristic_based_detection
  - keypoint_tracking
  - freezing_detection
  - open_source_behavioral_software
  - deeplabcut
  - fear_conditioning
  - vicarious_trial_and_error
  - ca2_imaging_alignment
  - optogenetics_behavioral_validation
  - rodent_behavioral_analysis
  - behaviordepot
  - simple
  - flexible
  - tool
  - automated
  - behavioral
  - detection
  - based
---

### One-line summary

BehaviorDEPOT is an open-source, GUI-driven MATLAB software package that converts DeepLabCut keypoint tracking data into validated behavioral classifications across a range of standard rodent assays, with a freezing heuristic that exceeds 90% accuracy even in animals wearing tethered head-mounts.

---

### Background & motivation

Quantifying naturalistic animal behavior rapidly, reliably, and with spatiotemporal precision remains a major challenge in systems neuroscience. Manual annotation is slow and inconsistent, while commercially available automated systems are expensive, opaque, and frequently fail when animals wear head-mounted hardware for optogenetics, fiber photometry, or Ca2+ imaging. Existing open-source machine-learning classifiers (e.g., JAABA, SimBA, MARS) either depend on ellipse-fitting trackers that perform poorly in complex arenas, or require large annotated datasets and substantial coding expertise to deploy. BehaviorDEPOT was developed to fill the gap: a no-code, heuristic-based tool that operates on keypoint tracking data and integrates behavioral detection with spatial and temporal experimental metadata, enabling easy alignment with neural recordings.

---

### Methods

- **Software architecture**: Six MATLAB modules with graphical interfaces — Analysis, Experiment, Inter-Rater, Data Exploration, Optimization, and Validation.
- **Input**: Keypoint tracking data (X-Y coordinates + DLC likelihood values per frame) from DeepLabCut or compatible tools; behavior videos.
- **Data pipeline**: Low-confidence points filtered (p < 0.1), Hampel outlier removal, LOWESS smoothing, spline interpolation for missing values; kinematic and postural metrics (velocity, angular velocity, acceleration, distance) computed framewise for each keypoint.
- **Freezing heuristic**: Threshold on back linear velocity (default 0.59 cm/s) and head angular velocity (default 15 deg/s), smoothed with a sliding-window convolution algorithm, minimum bout duration filter (default 0.9 s). A second "jitter" heuristic uses a MATLAB changepoint function as an alternative.
- **Additional heuristics**: novel object exploration (head angle + nose–object distance), VTE in T-maze (head-angle sweeps ≥ 180° in choice zone), rearing, escape, locomotion.
- **Spatial analysis functions**: EPM, OFT, T-maze, three-chamber assay, user-definable ROIs.
- **Validation datasets**: Mice and rats from multiple labs, recorded at 30–75 fps with cameras ranging from webcams to high-resolution FLIR cameras, including animals wearing optogenetic patch cords and UCLA Miniscopes.
- **Comparison**: Head-to-head benchmarking against JAABA using DLC-derived ellipses as input to JAABA.
- **Demonstration experiments**: Contextual fear conditioning with optogenetic mPFC silencing (stGtACR2); Ca2+ imaging (GCaMP7f via Miniscope) during platform-mediated avoidance; EPM, OFT, NOE, and effort-based T-maze in separate cohorts.

---

### Key findings

- **Freezing heuristic accuracy (high-resolution camera, 50 fps)**: Precision = 0.86, Recall = 0.92, F1 = 0.89, Specificity = 0.97; comparable to expert human rater (paired t-test p = 0.95).
- **Webcam generalization (30 fps)**: Precision = 0.98, Recall = 0.88, F1 = 0.93, Specificity = 0.99.
- **Optogenetics patch-cord condition**: Precision = 0.94, Recall = 0.87, F1 = 0.91, Specificity = 0.98 — maintains performance despite tethered hardware that causes commercial software to fail.
- **Miniscope condition**: Precision = 0.85, Recall = 0.93, F1 = 0.89, Specificity = 0.84.
- **External lab validation (rats)**: F1 = 0.91, Specificity = 0.96 after optimization; indistinguishable from human rater (Mann-Whitney U p = 0.89).
- **External lab validation (mice)**: F1 = 0.95, Specificity = 0.95 (p = 0.49 vs. human rater).
- **DLC tracking error sensitivity**: Linear regression revealed tracking errors < 4 pixels produced highest F1 scores; precision and F1 declined with higher errors, but recall and specificity were unaffected.
- **T-maze choice detection**: 100% accuracy across 84 trials in 4 mice; VTE detection closely matched human annotations and detected a significant increase in VTE when a second barrier was added (FBarriers p = 0.003), whereas JAABA labeled every trial as VTE.
- **Comparison vs. JAABA (freezing)**: BehaviorDEPOT had significantly higher recall and F1 score despite using fewer training videos (3 vs. 6); F-test recall: F(1,11) = 51.27, p < 0.001.
- **Optogenetics science result**: mPFC silencing during retrieval enhanced freezing in a novel (non-conditioned) context but not the conditioned context, significantly reducing the discrimination index (p = 0.002), indicating mPFC is critical for specificity of recent fear memories — with BehaviorDEPOT estimates matching manual annotations.
- **Ca2+ imaging**: Nearly half of 513 recorded mPFC neurons were modulated by freezing, platform occupancy, or both, with cells distributed in a salt-and-pepper pattern.

---

### Computational framework

Not applicable as a formal computational framework. The paper's approach is algorithmic and signal-processing based rather than model-theoretic:

- Behaviors are detected through **heuristics** — explicit, human-interpretable rule sets that apply thresholds to kinematic and postural metrics derived from keypoint positions.
- The freezing heuristic is effectively a **low-pass filter on velocity** (back velocity + head angular velocity below threshold) combined with a **sliding-window convolution** to smooth binarized output and a minimum-duration gate.
- The "jitter" heuristic uses a **changepoint detection** algorithm on velocity time series, dividing frames into groups with minimal within-group residual error.
- The VTE heuristic is a **head-angle sweep detector** (180° range within a choice-zone trial).
- A **generalized linear model (GLM)** is used in the Data Exploration Module to rank metrics by predictive value, but this is a development tool, not the core classifier.

The paper sits at Marr's algorithmic level: it specifies what computation detects behavior (threshold-based rules on pose kinematics) without proposing a biological implementation or a computational-level theory of what the brain is doing.

---

### Prevailing model of the system under study

This paper does not study a neural system per se — it is a methods/tools paper whose subject is the problem of behavioral quantification. The prevailing state of the field that the paper pushes against is:

- Most labs still score behavior manually or with closed-source commercial software (e.g., VideoFreeze, ANYmaze, Ethovision), which is slow, inconsistent, and expensive.
- Existing open-source classifiers either rely on coarse centroid/ellipse-based tracking (prone to failure in complex arenas) or require additional rounds of supervised machine learning on large annotated datasets (JAABA, SimBA, MARS), which is computationally intensive and inaccessible to labs without coding expertise.
- Keypoint tracking via DeepLabCut has lowered the barrier to pose estimation, but converting pose data into meaningful behavioral labels remains a bottleneck for most labs.

The paper's framing implies the field lacks a practical bridge between markerless pose estimation and validated, flexible behavioral classification — particularly for labs integrating neural recording hardware.

---

### What this paper contributes

BehaviorDEPOT provides a validated, open-source, no-code solution for converting keypoint tracking data into behavioral classifications that match expert human annotations across diverse experimental configurations. Specific advances over the prior landscape:

1. **Heuristics outperform JAABA** on both freezing (significantly higher recall/F1) and VTE (JAABA could not distinguish VTE from non-VTE trials at all).
2. **Head-mount robustness**: achieves >90% F1 for freezing in animals wearing optogenetic patch cords and Miniscopes — a condition that reliably defeats commercial software.
3. **Spatial-temporal integration**: behavioral detections are stored framewise and can be filtered by user-defined ROIs and time windows, enabling analyses (e.g., "where was the animal when it froze?") not possible with classifiers that return only frame-level labels.
4. **Full pipeline for Ca2+ imaging**: together with the UCLA MiniCAM and MIN1PIPE, provides an end-to-end open-source pipeline from data collection to neural-behavioral alignment.
5. **Heuristic development toolkit**: the four auxiliary modules (Inter-Rater, Data Exploration, Optimization, Validation) systematize the process of defining, optimizing, and validating new heuristics, adding rigor to a step that is typically ad hoc.
6. **Cross-species, cross-lab generalizability**: F1 > 0.90 maintained after optimization on rat and mouse videos recorded in external laboratories.

---

### Brain regions & systems

The paper is primarily a methods paper. Brain regions appear in validation use cases:

- **Medial prefrontal cortex (mPFC) / prelimbic cortex** — targeted for optogenetic silencing (stGtACR2) to probe specificity of contextual fear memory; also imaged with GCaMP7f/Miniscope to record neurons encoding freezing and platform avoidance. Role in paper: validation context demonstrating BehaviorDEPOT's utility in neural-behavioral experiments; science result shows mPFC gates fear memory specificity.
- No other brain regions are focal to the paper's scientific claims.

---

### Mechanistic insight

The paper does not meet the bar. It presents an algorithm (heuristic-based behavior detection from pose kinematics) and validates it against human annotations, but does not provide neural data specifically linking BehaviorDEPOT's behavioral variables to mechanistic accounts of how the brain implements those behaviors. The optogenetics and Ca2+ imaging experiments demonstrate that BehaviorDEPOT-derived behavioral labels can be aligned with neural data (mPFC silencing affects fear specificity; mPFC neurons are modulated by freezing and platform occupancy), but these are proofs of utility, not mechanistic dissections. No mapping onto Marr's three levels is warranted.

---

### Limitations & open questions

- **DLC prerequisite**: Users must first train a keypoint tracking model; dedicated per-setup models are recommended, which requires some initial effort even if pre-trained models are provided.
- **Heuristics require human definitions**: Bias from the researcher's definition of a behavior is encoded in the heuristic parameters; fully unsupervised discovery of behavioral structure is not supported.
- **Generalization to non-rodent species**: The paper asserts BehaviorDEPOT is broadly applicable but does not demonstrate this beyond mice and rats.
- **Complex/social behaviors**: The heuristic approach is acknowledged to be less suited to behaviours that are difficult for humans to label reliably (e.g., social interactions, self-grooming), where unsupervised approaches (B-SOiD, MotionMapper) or supervised ML (SimBA, MARS) may be preferable.
- **Side-view videos**: The velocity-based freezing heuristic may be slightly affected by distortions when the mouse moves toward or away from a side-mounted camera; the jitter heuristic was proposed as a partial solution.
- **Spatial analysis coverage**: Current built-in assay functions cover EPM, OFT, T-maze, and three-chamber; other common paradigms (Y-maze, conditioned place preference) require users to adapt existing functions.
- **MATLAB dependency**: Requires MATLAB (2018+); a standalone EXE is available but full customisation requires a MATLAB license.

---

### Connections & keywords

**Key citations**:
- Mathis et al. 2018 — DeepLabCut (keypoint tracking foundation)
- Kabra et al. 2013 — JAABA (primary comparison system)
- Nilsson et al. 2020 — SimBA
- Segalin et al. 2021 — MARS
- Hsu & Yttri 2021 — B-SOiD
- Anagnostaras et al. 2010 — VideoFreeze commercial system
- Pereira et al. 2019 — SLEAP pose estimation
- Redish 2016 — vicarious trial and error review
- Cai et al. 2016 — UCLA Miniscope
- Lu et al. 2018 — MIN1PIPE

**Named models or frameworks**:
- BehaviorDEPOT (DEcoding behavior based on POsitional Tracking)
- DeepLabCut (DLC)
- JAABA
- UCLA Miniscope / UCLA MiniCAM
- Platform-mediated avoidance (PMA) task
- Barrier T-maze effort-based decision task

**Brain regions**:
- Medial prefrontal cortex (mPFC) / prelimbic cortex

**Keywords**:
- markerless pose estimation, behavioral classification, heuristic-based detection, keypoint tracking, freezing detection, open-source behavioral software, DeepLabCut, fear conditioning, vicarious trial and error, Ca2+ imaging alignment, optogenetics behavioral validation, rodent behavioral analysis
