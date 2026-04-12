---
source_file: "gramfort2013_meg_eeg_analysis_python.md"
paper_id: "gramfort2013_meg_eeg_analysis_python"
title: "MEG and EEG data analysis with MNE-Python"
authors: "Alexandre Gramfort, Martin Luessi, Eric Larson, Denis A. Engemann, Daniel Strohmeier, Christian Brodbeck, Roman Goj, Mainak Jas, Teon Brooks, Lauri Parkkonen, Matti H\u00e4m\u00e4l\u00e4inen"
year: 2013
journal: "Frontiers in Neuroscience"
paper_type: "computational"
contribution_type: "methodological"
brain_regions: ["visual_cortex"]
frameworks: ["bayesian_inference"]
keywords: ["meg", "eeg", "data", "analysis", "mne", "python"]
---

### One-line summary

MNE-Python is an open-source Python package providing a comprehensive, reproducible pipeline for MEG and EEG data analysis, encompassing preprocessing, source localisation, time-frequency analysis, connectivity estimation, and decoding.

---

### Background & motivation

MEG and EEG analysis requires expertise spanning physics, signal processing, statistics, and numerical methods, yet existing packages (Brainstorm, EEGLAB, FieldTrip, SPM) are all MATLAB-based. The complexity of the M/EEG pipeline — segmentation, forward modelling, denoising, ill-posed inverse problems, statistical control — demands a well-documented, flexible, and reproducible toolchain. MNE-Python fills the gap by providing a pure-Python implementation with tight integration into the scientific Python ecosystem, enabling scripted, reproducible analyses and collaborative development across institutions.

---

### Methods

- **Software architecture**: object-oriented Python API with three core data containers — `Raw`, `Epochs`, and `Evoked` — mirroring the standard M/EEG processing workflow.
- **Preprocessing**: band-pass/high-pass/low-pass/notch FIR and IIR filtering (FFT-based, optionally GPU-accelerated via CUDA); signal space projection (SSP) for artifact suppression; FastICA (via Scikit-Learn) for component-based artifact removal.
- **Forward modelling**: boundary element method (BEM) and finite element method (FEM) head models; source spaces defined on the cortical surface (FreeSurfer ico-5, ~10,242 vertices/hemisphere) or volumetric grids.
- **Linear inverse methods**: Minimum Norm Estimate (MNE), dSPM, sLORETA — all implemented as linear matrix operators applicable to Evoked, Epochs, or Raw data; LCMV and DICS beamformers.
- **Non-linear inverse methods**: Mixed-Norm Estimates (MxNE), Time-Frequency MxNE (TF-MxNE), and gamma-MAP sparse Bayesian learning.
- **Statistics**: parametric and non-parametric cluster-based permutation tests across arbitrary dimensions (spatio-temporal, time-frequency, source space).
- **Decoding/MVPA**: integration with Scikit-Learn classifiers (e.g., linear SVM) for time-resolved cross-validation decoding.
- **Functional connectivity**: bivariate spectral measures (coherence, imaginary coherence, PLV, wPLI) in sensor and source space, with cortical parcellation support (FreeSurfer aparc).
- **Surface-based normalisation**: morphing of source estimates to a common brain (fsaverage) using FreeSurfer spherical registration.
- **Integration**: NumPy, SciPy, matplotlib, Mayavi, Scikit-Learn, Pandas, Nibabel; FIF file format for interoperability; ~44,000 lines of code, 86% test coverage.

---

### Key findings

- MNE-Python demonstrates end-to-end source localisation in fewer than 30 lines of Python code (Table 1), including filtering, epoching, covariance estimation, inverse operator construction, and morphing.
- ICA-based cardiac and ocular artifact removal is achievable in fewer than 20 lines (Table 2) using automated scoring via Pearson correlation or variance.
- Time-resolved SVM decoding on sensor-space MEG data shows reliable differentiation of auditory versus visual conditions starting at ~50 ms post-stimulus, peaking at ~100 ms (N100m).
- Source localisation with sparse non-linear solvers (TF-MxNE, gamma-MAP) recovers primary and secondary visual cortex activations following visual stimulation; gamma-MAP additionally identifies a right fusiform gyrus source consistent with the visual ventral stream.
- Cluster-based statistics applied to source-space time-frequency data identify significant activations following auditory stimulation; spatio-temporal contrasts between auditory and visual conditions are visualised on the cortical surface.
- All-to-all alpha-band (8–13 Hz) connectivity between the 68 cortical regions of the FreeSurfer aparc parcellation can be computed using a memory-efficient generator-based pipeline (Table 4).

---

### Computational framework

The paper is a software methods paper rather than a study proposing a new computational model of neural processing. The computational frameworks it implements include:

- **Linear inverse modelling**: regularised least-squares minimisation (ℓ2-norm, MNE/dSPM/sLORETA); the inverse problem is cast as finding the minimum-norm current distribution consistent with sensor measurements, given a forward model.
- **Sparse Bayesian / convex optimisation**: MxNE and TF-MxNE use mixed-norm (ℓ2,1) penalties promoting spatially sparse but temporally smooth source configurations; gamma-MAP uses hierarchical Bayesian inference.
- **Beamforming**: LCMV and DICS construct adaptive spatial filters by minimising output power subject to a unit-gain constraint at the target location.
- **Spectral connectivity**: phase-based bivariate measures (PLV, coherence, imaginary coherence, wPLI) estimated via multitaper methods.

Key variables in all inverse approaches: sensor data matrix **Y**, forward operator **G** (relating source currents to sensor readings), noise covariance **C**, and source current distribution **J**. The fundamental assumption is that M/EEG signals arise from current dipoles on the cortical surface.

---

### Prevailing model of the system under study

The paper's introduction frames M/EEG analysis as a pipeline engineering problem rather than positioning itself against a specific neuroscientific theory. The prevailing context is that M/EEG offers millisecond temporal resolution complementing the spatial resolution of fMRI, enabling study of oscillatory dynamics and rapid neural computations (Tallon-Baudry et al., 1997; Fries, 2009). The theoretical landscape assumed is that existing MATLAB-based packages each implement parts of this pipeline, but fragmentation, limited reproducibility, and the non-open nature of MATLAB constrain collaborative science. There is no detailed theoretical framing of how neural circuits generate M/EEG signals beyond the standard biophysical dipole model (Hämäläinen et al., 1993).

---

### What this paper contributes

MNE-Python consolidates state-of-the-art M/EEG methods — including several algorithms previously published only by the authors (MxNE, TF-MxNE, graph-based variability) — into a single, openly licensed, well-tested Python package. By demonstrating that complex pipelines can be expressed in a small number of readable, reproducible scripts, the paper:

- Provides a community infrastructure that lowers the barrier to adopting advanced inverse methods (non-linear sparse solvers, non-parametric statistics, MVPA) in standard laboratory workflows.
- Promotes reproducibility through scripted pipelines, version-controlled code, and shared datasets.
- Establishes a collaborative development model (multi-institution, open pull-request review, 86% test coverage) that has since become the dominant paradigm for academic neuroimaging software.
- Reduces methodological heterogeneity by providing common, well-documented implementations of competing methods in the same environment.

---

### Brain regions & systems

The paper uses M/EEG data primarily to demonstrate software functionality rather than to make claims about specific brain regions. Regions mentioned in the context of example analyses:

- **Auditory cortex** — source of auditory N100m response; used to validate dSPM and LCMV source localisation.
- **Primary visual cortex (V1) and secondary visual cortex (V2)** — identified by TF-MxNE and gamma-MAP in response to visual hemifield stimulation.
- **Right fusiform gyrus** — additional source identified by gamma-MAP following visual stimulation, consistent with the visual ventral stream.
- **Cortical surface (general)** — FreeSurfer parcellation into 68 aparc regions used for connectivity analysis.

The paper is primarily a methods/software contribution; regional findings are illustrative, not investigative.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight at Marr's three levels. It is a software methods article that implements and demonstrates existing algorithms; it does not propose a new algorithmic account of a neural phenomenon, nor does it provide neural recording data designed to adjudicate between algorithmic alternatives. The source localisation examples demonstrate that multiple inverse methods (MNE, dSPM, LCMV, TF-MxNE, gamma-MAP) recover broadly consistent cortical activation patterns for well-characterised auditory and visual responses, but this serves as a validation of implementation correctness rather than as a test of competing theories of neural computation.

---

### Limitations & open questions

- No GUI for interactive processing; users must write scripts, which requires programming literacy.
- Dipole-fitting (parametric overdetermined methods) is not implemented in MNE-Python at the time of publication.
- Connectivity estimation is limited to bivariate spectral measures; multivariate methods (e.g., partial coherence, Granger causality) are noted as a planned future addition.
- Connectivity estimates in source space are sensitive to the spatial spread of source estimates and should be interpreted with caution; beamformer-based connectivity may still reflect spurious connections from latent common drivers.
- The forward modelling pipeline depends on FreeSurfer for cortical surface reconstruction, introducing a dependency on an external, compute-intensive step.
- The paper notes ongoing concerns about reproducibility in neuroimaging more broadly (Carp, 2012a,b): MNE-Python addresses software-level reproducibility but cannot resolve variability arising from differing acquisition hardware or experimental protocols across labs.

---

### Connections & keywords

**Key citations**:
- Gramfort et al. (2013a) — companion paper describing the full MNE software suite
- Hämäläinen et al. (1993) — foundational review of MEG theory and instrumentation
- Dale et al. (2000) — dSPM method
- Hämäläinen & Ilmoniemi (1994) — minimum norm estimate
- Pascual-Marqui (2002) — sLORETA
- Van Veen et al. (1997) — LCMV beamformer
- Gross et al. (2001) — DICS beamformer
- Gramfort et al. (2012) — MxNE
- Gramfort et al. (2013b) — TF-MxNE
- Wipf & Nagarajan (2009) — gamma-MAP
- Maris & Oostenveld (2007) — non-parametric cluster-based statistics
- Pedregosa et al. (2011) — Scikit-Learn
- Oostenveld et al. (2011) — FieldTrip
- Delorme & Makeig (2004) — EEGLAB
- Tadel et al. (2011) — Brainstorm

**Named models or frameworks**:
- MNE (Minimum Norm Estimate)
- dSPM (Dynamic Statistical Parametric Mapping)
- sLORETA
- LCMV (Linearly Constrained Minimum Variance) beamformer
- DICS (Dynamic Imaging of Coherent Sources) beamformer
- MxNE (Mixed-Norm Estimate)
- TF-MxNE (Time-Frequency Mixed-Norm Estimate)
- gamma-MAP (sparse Bayesian learning)
- SSP (Signal Space Projection)
- FastICA
- FreeSurfer cortical parcellation (aparc)

**Brain regions**:
- Auditory cortex
- Primary visual cortex (V1)
- Secondary visual cortex (V2)
- Right fusiform gyrus

**Keywords**:
- magnetoencephalography (MEG)
- electroencephalography (EEG)
- source localisation
- electromagnetic inverse problem
- open-source neuroimaging software
- reproducible research
- independent component analysis (ICA)
- cluster-based permutation statistics
- functional connectivity
- multivariate pattern analysis (MVPA)
- beamforming
- sparse Bayesian inference
