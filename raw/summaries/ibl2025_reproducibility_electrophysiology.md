---
source_file: ibl2025_reproducibility_electrophysiology.md
paper_id: ibl2025_reproducibility_electrophysiology
title: "Reproducibility of in vivo electrophysiological measurements in mice"
authors:
  - "International Brain Laboratory"
  - "Kush Banga"
  - "Julius Benson"
  - "Jai Bhagat"
  - "Dan Biderman"
  - "Daniel Birman"
  - "Niccolò Bonacchi"
  - "Sebastian A Bruijns"
  - "Kelly Buchanan"
  - "Robert AA Campbell"
  - "Matteo Carandini"
  - "Gaëlle A Chapuis"
  - "Anne K Churchland"
  - "M Felicia Davatolhagh"
  - "Hyun Dong Lee"
  - "Mayo Faulkner"
  - "Berk Gerçek"
  - "Fei Hu"
  - "Julia Huntenburg"
  - "Cole Hurwitz"
  - "Anup Khanal"
  - "Christopher Krasniak"
  - "Christopher Langfield"
  - "Petrina Lau"
  - "Nancy Mackenzie"
  - "Guido T Meijer"
  - "Nathaniel J Miska"
  - "Zeinab Mohammadi"
  - "Jean-Paul Noel"
  - "Liam Paninski"
  - "Alejandro Pan-Vazquez"
  - "Cyrille Rossant"
  - "Noam Roth"
  - "Michael Schartner"
  - "Karolina Socha"
  - "Nicholas A Steinmetz"
  - "Karel Svoboda"
  - "Marsa Taheri"
  - "Anne E Urai"
  - "Shuqi Wang"
  - "Miles Wells"
  - "Steven J West"
  - "Matthew R Whiteway"
  - "Olivier Winter"
  - "Ilana B Witten"
  - "Yizi Zhang"
year: 2025
journal: eLife
paper_type: empirical
contribution_type: methodological
species:
  - mouse
methods:
  - electrophysiology
  - neuropixels
brain_regions:
  - hippocampus_ca1
keywords:
  - neuropixels_reproducibility
  - multi_lab_electrophysiology
  - quality_control_standards
  - probe_targeting_variability
  - allen_common_coordinate_framework
  - single_neuron_modulation
  - population_decoding
  - variance_decomposition
  - spike_sorting
  - rigor_criteria
  - systems_neuroscience_replicability
  - multi_task_neural_network_encoding_model
  - reproducibility
  - vivo
  - electrophysiological
  - measurements
  - mice
key_citations:
  - wang2020_alternating_theta_sequences
---

### One-line summary

A ten-lab collaborative study using standardised Neuropixels recordings in mice demonstrates that electrophysiological features are reproducible across laboratories when stringent quality-control criteria (RIGOR) are applied, but that single-neuron modulation metrics and some functional activity measures remain vulnerable to reproducibility failures driven by probe-targeting variability and low statistical power.

---

### Background & motivation

Reproducibility is a fundamental requirement of the scientific method, yet it has been poorly characterised in systems neuroscience, where the technical complexity of extracellular recordings makes replication experiments rare and difficult to publish. Prior multi-lab work by the International Brain Laboratory (IBL) demonstrated reproducible mouse behaviour on a standardised task, but it remained unknown whether neural recording results could likewise be reproduced. Answering this question is critical because most neuroscience data are collected in small individual labs, and understanding the upper bound on reproducibility under carefully controlled conditions sets expectations for the broader literature. This paper fills that gap by collecting 121 Neuropixels recording sessions across ten geographically distributed labs targeting the same brain site.

---

### Methods

- **Design**: Multi-lab replication study; ten IBL labs each performed repeated Neuropixels 1.0 probe insertions targeting identical stereotaxic coordinates (AP −2.0 mm, ML −2.24 mm, DV −4.0 mm, 15° angle) in expert head-fixed mice performing a standardised visual decision-making task (biasedChoiceWorld).
- **Animals**: N = 78 adult C57BL/6 mice (male and female) across ten labs.
- **Recordings**: 121 sessions collected; 82 sessions retained after quality control. 5,312 single neurons analysed for electrophysiological features; 4,400 neurons for functional activity analyses.
- **Brain regions targeted**: Visual areas VISa/am, hippocampal CA1 and dentate gyrus (DG), and thalamic nuclei LP and PO.
- **Histology**: Serial-section two-photon microscopy; probe tracks traced manually and registered to the Allen Common Coordinate Framework (CCF); electrophysiology-to-histology alignment performed per insertion.
- **Quality control (RIGOR)**: Ten criteria applied including neuronal yield, noise level, LFP power, manual visual inspection (drift, epileptiform activity, noisy channels, artefacts), refractory period violation rate, amplitude cut-off estimate, and median spike amplitude (≥50 µV).
- **Analyses**:
  - Permutation tests for across-lab reproducibility of electrophysiological features (firing rate, LFP power, spike amplitude, AP-band RMS, neuronal yield).
  - Wilcoxon-based tests for proportions of task-modulated neurons across six task-period comparisons.
  - PCA-based low-dimensional embedding of PETHs with Kolmogorov-Smirnov tests.
  - Reduced-Rank Regression (RRR) encoding model for single-neuron response profiles; support vector classification to decode lab vs. region identity.
  - Multi-task neural network (MTNN) with leave-one-out covariate analyses to quantify sources of neural variance.
  - Population-level decoder (reduced-rank decoder) for choice, stimulus side, reward, and wheel speed.

---

### Key findings

- **Probe targeting variability**: Mean geometrical displacement from planned insertion site was 356 µm at the brain surface; probe angle differed from plan by ~7.5°. No significant systematic lab-to-lab differences in targeting (permutation test p = 0.19 for surface displacement, p = 0.45 for angle).
- **Electrophysiological features reproducible**: After RIGOR QC, permutation tests showed no significant across-lab differences for neuronal yield, firing rate, LFP power, and AP-band RMS in most regions (only spike amplitude in VISa/am reached significance at α = 0.01). Random Forest classifier could decode brain region from features but could not decode lab identity (above chance only in DG).
- **Functional modulation partially irreproducible**: Single-neuron task-modulation proportions showed significant across-lab differences in VISa/am during stimulus onset (p < 0.01) and in thalamic regions for some firing rate modulation distributions. These failures were driven by outlier labs or sessions rather than systematic biases.
- **Low statistical power**: Single-neuron modulation tests have limited sensitivity; required shifts to produce significance were often below one standard deviation of lab distributions, highlighting that high within-neuron variability limits reproducibility.
- **PCA embedding**: Brain region identity was strongly decodable from 2-PC PETH embeddings (all regions significantly distinct at α = 0.01); lab identity was detectable for 7/10 labs in pooled data but only 6/40 lab-region pairs when tested per region, and this was further attenuated after cell-number control.
- **RRR encoding model**: Brain region decodable from single-neuron response profiles (macro F1 = 0.35, p < 0.0001); lab identity not decodable (macro F1 = 0.14, p = 0.325).
- **MTNN analysis**: Movement covariates (face motion energy, paw speed, wheel velocity) individually explain ~5% of neural variance; lab and session IDs had near-zero unique contribution in leave-one-out analysis, indicating within- and between-lab random effects are small and comparable.
- **Population decoding**: No significant across-lab differences in decodability of choice, stimulus side, reward, or wheel speed for any region after multiple-comparison correction (ANOVA p-values all above adjusted α = 0.01); region identity but not lab identity was decodable from decoding scores.
- **Spatial position and spike waveform**: Neither within-region spatial position nor waveform features explained more than ~5% of firing rate variability in any region.

---

### Computational framework

The paper does not propose a new computational model of neural function. Its primary computational contributions are methodological: a multi-task neural network (MTNN) used as a flexible encoding model to partition neural variance, and a reduced-rank regression (RRR) model for single-neuron response profiling.

**MTNN**: Takes static covariates (lab ID, neuron 3D location) and dynamic covariates (wheel velocity, paw speed, face motion energy, task events, decision strategy) as inputs. Shared fully-connected and bidirectional RNN layers extract nonlinear features across all neurons; neuron-specific fully-connected output layers fit Poisson regression for each cell. Trained to predict trial-by-trial firing rates (50 ms bins, −0.5 to +1 s around movement onset). Effect sizes quantified via single-covariate fits and leave-one-out fits (following Musall et al., 2019). The MTNN is best understood as a tool for variance decomposition rather than as a model of the underlying neural computation.

The paper's broader statistical framework relies on non-parametric permutation tests (maximum absolute CDF difference as test statistic, 50,000 permutations), PCA for dimensionality reduction, and Kolmogorov-Smirnov tests for distributional comparisons.

---

### Prevailing model of the system under study

The introduction situates the paper within a widely shared concern about the reproducibility crisis in biological and psychological science, citing documented failures in neuroscience (place field preplay, spike-timing-dependent plasticity in nematodes, persistence of place fields without visual input). The prevailing working assumption challenged by this paper is that standardisation of methods within a single organisation is sufficient to ensure reproducibility, and that results published from individual labs using conventional quality metrics (stereotaxic coordinates, manual spike sorting, standard single-unit tests) are reliable. The paper also pushes against the implicit assumption that electrophysiological recordings are intrinsically reproducible given sufficient experimental care, and that standard single-neuron analysis approaches (Wilcoxon modulation tests, proportion-of-responsive-neurons metrics) are robust measures of neural function.

---

### What this paper contributes

The paper establishes that reproducibility in Neuropixels electrophysiology depends critically on the type of measure and on the quality-control pipeline applied:

- **Basic electrophysiological features** (firing rate, LFP power, yield) are robustly reproducible across labs when the RIGOR criteria are met, providing reassurance for the field.
- **Standard single-neuron modulation analyses** are not reliably reproducible, failing for some region-test combinations. This is shown to arise from a combination of (a) genuine outlier sessions and labs, (b) probe-targeting errors that sample different sub-populations across insertions, and (c) low statistical power inherent to single-neuron tests given high variability.
- **Multi-variable response profiles** (RRR coefficients, PETH-PCA embeddings) are more reproducible than single-variable modulation metrics, offering a practical recommendation for future analyses.
- **Probe targeting error** (~360 µm at the brain surface) is identified as a significant, previously underappreciated source of experimental variance that is not driven by animal anatomy or systematic lab differences, but by the inherent mismatch between skull landmarks and the CCF.
- The paper introduces **RIGOR** as a publicly available, code-supported set of quality-control standards applicable to any Neuropixels dataset, filling the gap left by the absence of agreed-upon inclusion criteria in the field.

---

### Brain regions & systems

- **VISa/am (secondary visual areas)** — a primary region of interest for visual decision-making; showed the most frequent lab-to-lab reproducibility failure in single-neuron modulation tests; functional responses to stimuli were variable.
- **CA1 (hippocampal field CA1)** — showed generally reproducible electrophysiological features and population activity; spatial position explained a small fraction of firing rate variability.
- **Dentate gyrus (DG)** — characterised by distinctive high LFP power (20–80 Hz) used as an electrophysiological landmark for probe alignment; lab identity was detectable from electrophysiological features in DG (above-chance Random Forest decoding).
- **LP (lateral posterior thalamic nucleus)** — showed more variable functional responses; high-firing and task-modulated neurons had slightly different spatial positions, suggesting spatial sub-sampling contributes to variability.
- **PO (posterior thalamic nucleus)** — showed failures in functional reproducibility for some tests; spatial position and spike amplitude explained small fractions of variability.

---

### Mechanistic insight

This paper does not meet the bar for mechanistic insight as defined here. It provides extensive neural recording data but does not propose or test a specific algorithm for neural computation. The analyses characterise the statistical properties and reproducibility of recorded activity rather than formalising or testing a mechanistic model of how any of the targeted regions (VISa/am, CA1, DG, LP, PO) implement a computation. The MTNN is used as a variance-decomposition tool, not as a candidate algorithm for the neural processes under study. The paper therefore provides no mapping onto Marr's three levels for any specific neural phenomenon.

---

### Limitations & open questions

- The study cannot disentangle whether reproducibility gains come from person-to-person standardisation versus lab-to-lab standardisation of instrumentation and software.
- Centralising the histology pipeline reduces variance, but the additional variability introduced when individual labs process histology independently remains unquantified.
- The RIGOR criteria exclude a substantial fraction of data (82/121 sessions retained); the relationship between exclusion thresholds and reproducibility was not systematically explored.
- Some quality metrics (e.g., minimum trial count of 400) are experiment-specific and would need adaptation for other tasks or species.
- Variability in dentate gyrus electrophysiological features remained detectable across labs even after QC; its source is not identified.
- Outlier labs/sessions driving reproducibility failures could not be explained by mouse behaviour, kinematics, or spatial sub-sampling; their origin is unknown.
- Multi-shank probes and larger cohort sizes are anticipated to reduce variability in cortical regions (which are thin and prone to low cell counts), but this was not tested here.
- The study does not address whether the observed reproducibility generalises to other brain regions, other tasks, or other species.
- Structural MRI-guided targeting could reduce probe placement error but is impractical for most labs; no alternative solution was validated.

---

### Connections & keywords

**Key citations**:
- The International Brain Laboratory et al. (2021) — prior IBL behavioural reproducibility study; source of the standardised decision task.
- Steinmetz et al. (2019) — comparison dataset; source of task-modulation analysis approach.
- Siegle et al. / de Vries et al. (Allen Institute, 2020/2021) — comparison dataset for yield and quality benchmarking.
- Musall et al. (2019) — variance decomposition approach adapted for MTNN.
- Posani et al. (2024) — prior IBL reduced-rank regression application to brain-wide map data.
- Birman et al. (2023) — corrected Allen CCF atlas resolving stereotaxic/CCF angular offset.
- Wang et al. (2020) — Allen Common Coordinate Framework.
- Biderman et al. (2023) — Lightning Pose and Ensemble Kalman Smoother for pose estimation.
- Mathis et al. (2018) — DeepLabCut.

**Named models or frameworks**:
- RIGOR (Recording Inclusion Guidelines for Optimizing Reproducibility)
- Multi-task neural network (MTNN)
- Reduced-rank regression (RRR) encoding model
- Allen Common Coordinate Framework (CCF)
- IBL biasedChoiceWorld task
- ibl-sorter (Kilosort 2.5 Python port)
- Lightning Pose / Ensemble Kalman Smoother (EKS)

**Brain regions**:
- VISa/am (secondary visual areas A and AM)
- CA1 (hippocampal field CA1)
- Dentate gyrus (DG)
- LP (lateral posterior thalamic nucleus)
- PO (posterior thalamic nucleus)

**Keywords**: Neuropixels reproducibility, multi-lab electrophysiology, quality control standards, probe targeting variability, Allen Common Coordinate Framework, single-neuron modulation, population decoding, variance decomposition, spike sorting, RIGOR criteria, systems neuroscience replicability, multi-task neural network encoding model
