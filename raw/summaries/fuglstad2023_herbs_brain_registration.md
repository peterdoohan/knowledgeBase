---
source_file: fuglstad2023_herbs_brain_registration.md
title: "Histological E-data Registration in rodent Brain Spaces"
authors: Jingyi Guo Fuglstad, Pearl Saldanha, Jacopo Paglia, Jonathan R Whitlock
year: 2023
journal: eLife
paper_type: empirical
contribution_type: methodological
---

### One-line summary

HERBS is an open-source Python GUI tool that integrates pre-surgical coordinate planning and post-experiment histological registration of electrode tracks, viral expression, and anatomical features into a single user-friendly platform for rodent neuroscience.

---

### Background & motivation

Accurate anatomical recordkeeping in rodent neuroscience — matching histological tissue sections to reference atlases and localising recording electrodes or viral injection sites — is critically important but has become increasingly burdensome as large-scale multi-region recordings grow more common. Existing tools either offer limited functionality (e.g. only pre-surgical planning or only 3D rendering), require paid software licenses (e.g. MATLAB-based SHARP-TRACK), or demand programming proficiency. No single package combined pre-surgical coordinate generation with post-experiment registration and 3D visualisation in a click-button interface, particularly for rat users whose needs are underserved relative to the many mouse-specific tools.

---

### Methods

HERBS is a methodological/tool paper; validation was demonstrated through worked examples on in-house rodent tissue.

- **Software**: Python 3.8 package (PyPI and GitHub), cross-platform (Windows, macOS, Linux), GUI built with PyQt5, rendering via PyOpenGL; core numerical operations via NumPy, SciPy, and OpenCV.
- **Reference atlases**: Waxholm Space (WHS) Atlas of the Sprague Dawley Rat Brain v4 (>200 labeled cortical and subcortical regions) and Allen Mouse Brain Atlas; both downloadable through HERBS; extensible to user-supplied atlases.
- **Pre-surgical planning**: users click start/end points on 2D atlas slices; HERBS computes insertion angle, depth, and Bregma-relative coordinates.
- **Post-experiment registration**: triangulation-based piecewise affine (non-rigid) transformation warps histological sections to atlas templates using user-defined anchor points; supports coronal, sagittal, and horizontal planes with up to 30° tilt correction for oblique sections.
- **Electrode reconstruction**: users click ≥4 points along a DiI- or fluorescence-stained track; HERBS outputs 3D trajectory, per-region channel counts, and probe geometry.
- **Viral/cell registration**: magic-wand tool delineates fluorescent expression boundaries per slice; volumes are reconstructed in 3D and read-outs list affected regions with voxel counts and percentages.
- **Validation tissue**: Neuropixels 1.0 probes (DiI-stained) and AAV5-mDlx-ChR2-mCherry bilateral injections in adult Long-Evans rats; sections immunostained and digitized with Zeiss Axio Scan.Z1.
- **Companion tool**: TRACER (Python pipeline toolkit) provided for users wanting programmatic access.

---

### Key findings

- HERBS successfully reconstructed Neuropixels 1.0 probe trajectories from histological sections, producing read-outs of probe inclination, insertion length, and per-region channel counts that matched in vivo LFP landmarks (minor discrepancies attributed to paraformaldehyde-induced tissue shrinkage, not the software).
- Viral expression volumes (AAV in cingulate cortex, 11 tissue slices) were reconstructed in 3D and quantified per brain region as voxel count and percentage coverage.
- Pre-surgical planning was demonstrated for a 4-shank Neuropixels 2.0 probe targeting retrosplenial cortex, visual cortex, and hippocampus simultaneously, with a detailed per-shank read-out.
- Template matching via piecewise affine transformation substantially reduced registration error compared to global warping, especially for tissue with non-uniform shrinkage.
- HERBS is the only publicly available single-package tool combining pre-surgical coordinate generation, histological image processing, electrode/viral registration, and 2D/3D visualization for both rats and mice without requiring programming.

---

### Computational framework

Not applicable as a standalone computational framework. HERBS uses classical computer vision algorithms:

- **Triangulation-based piecewise affine transformation** for non-rigid registration of histological sections to atlas templates (warping histology to match atlas geometry).
- **Rigid registration** as an alternative simpler option.
- **Magic wand (flood-fill / threshold-based region selection)** for semi-automatic delineation of fluorescent expression boundaries.

No formal probabilistic or machine-learning framework is employed; the tool is deterministic and user-guided. The paper notes that future versions aim to incorporate machine vision for automatic template matching.

---

### Prevailing model of the system under study

The paper is a tools/methods paper and does not investigate a specific neural system or brain process. Its introduction assumes the standard practice in systems neuroscience: experimenters target brain regions using stereotaxic coordinates derived from printed atlases (Franklin & Paxinos; Papp et al.), and post hoc anatomy is verified by manually overlaying histological sections with atlas templates using general-purpose image software (ImageJ, Adobe Illustrator/Photoshop). This workflow is well established but acknowledged to be slow, subjective, and not scalable to datasets involving many probes or tissue sections. The prevailing model is therefore one of manual, labor-intensive anatomical curation, which HERBS is designed to replace with a systematic, reproducible GUI-driven pipeline.

---

### What this paper contributes

HERBS removes a key methodological bottleneck by unifying the full anatomical registration workflow — from pre-surgical planning to post-experiment 3D reconstruction — in a single GUI that requires no programming. Concretely, researchers can now:

- Generate stereotaxic coordinates without consulting printed atlases or writing code.
- Register arbitrary numbers of electrodes, viral volumes, cells, or tracers to a standard reference space using non-rigid (piecewise affine) tissue-to-atlas warping.
- Obtain quantitative, reproducible read-outs (region labels, channel counts, voxel volumes) rather than qualitative visual inspections.
- Do all of the above for both rats and mice, closing a gap left by the predominantly mouse-centric existing tooling ecosystem.

The paper does not change theoretical understanding of any neural circuit; its contribution is entirely methodological.

---

### Brain regions & systems

The paper is a methods tool; no specific brain region is the focus of a theoretical argument. Brain regions appear only as illustrative targets in worked examples:

- **Retrosplenial cortex, visual cortex, hippocampus (intermediate)** — example multi-shank Neuropixels 2.0 pre-surgical planning trajectory in rat.
- **Visual cortex to auditory cortex** — example electrode track reconstruction from DiI-stained Neuropixels 1.0 in rat.
- **Cingulate cortex (Cg1) and surrounding areas** — example AAV viral expression reconstruction in rat frontal cortex.

All regions are illustrative; the tool is region- and species-agnostic.

---

### Mechanistic insight

This paper does not meet the bar for mechanistic insight. It presents a software tool, not a model or algorithm explaining a neural computation, and it does not provide neural data in support of any mechanistic hypothesis. There is no phenomenon being explained at Marr's computational, algorithmic, or implementational levels — the contribution is methodological rather than explanatory.

---

### Limitations & open questions

- **Template matching scalability**: manual anchor-point matching is time-consuming for large datasets (many slices from viral or tracer studies); automated machine-vision matching is planned for future versions.
- **Tissue shrinkage**: paraformaldehyde fixation causes non-uniform shrinkage that introduces small but unavoidable discrepancies between in vivo probe positions and histological reconstructions; piecewise affine warping mitigates but cannot fully correct this.
- **Probe length estimation consistency**: estimates become less consistent when larger numbers of histological slices are used, possibly due to averaging across clicked points and inter-slice misalignment.
- **Installation barrier**: users unfamiliar with Python may find installation challenging, despite the minimal runtime coding requirement.
- **Atlas coverage**: out-of-the-box support is limited to WHS rat and Allen Mouse Brain atlases; other atlases require manual file preparation by the user.
- **No automatic registration**: all tissue-to-atlas matching is currently semi-manual (user-defined anchor points), limiting throughput compared to fully automated pipelines like Brainreg.

---

### Connections & keywords

**Key citations**:
- Shamash et al. 2018 (SHARP-TRACK — predecessor electrode reconstruction tool)
- Claudi et al. 2021 (Brainrender — 3D visualization tool)
- Tyson et al. 2020/2022 (Brainreg — automated whole-brain registration)
- Papp et al. 2014 (Waxholm Space rat brain atlas v1)
- Wang et al. 2020 (Allen Mouse Brain Common Coordinate Framework)
- Andy P. 2022 (Neuropixels Trajectory Explorer)
- Simmons & Swanson 2009 (sources of error in histological data comparison)
- Yushkevich et al. 2006 (ITK-SNAP)

**Named models or frameworks**:
- HERBS (Histological E-data Registration in rodent Brain Spaces)
- TRACER (Toolkit for Reconstructing Anatomical CoorindatEs in Rats)
- Waxholm Space (WHS) Atlas of the Sprague Dawley Rat Brain
- Allen Mouse Brain Atlas / Common Coordinate Framework
- BrainGlobe Atlas API
- Neuropixels Trajectory Explorer
- Brainrender / Brainreg

**Brain regions**:
- Retrosplenial cortex
- Visual cortex
- Auditory cortex
- Hippocampus
- Cingulate cortex (Cg1)

**Keywords**:
- histological brain registration
- rodent brain atlas
- electrode track reconstruction
- Neuropixels
- stereotaxic coordinate planning
- viral expression mapping
- piecewise affine transformation
- graphical user interface (GUI)
- Waxholm Space atlas
- Allen Mouse Brain Atlas
- open-source neuroscience tools
- anatomical data curation
