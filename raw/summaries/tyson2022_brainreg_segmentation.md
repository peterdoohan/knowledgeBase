---
source_file: tyson2022_brainreg_segmentation.md
paper_id: tyson2022_brainreg_segmentation
title: "Accurate determination of marker location within whole-brain microscopy images"
authors:
  - "Adam L. Tyson"
  - "Mateo Vélez-Fort"
  - "Charly V. Rousseau"
  - "Lee Cossell"
  - "Chryssanthi Tsitoura"
  - "Stephen C. Lenzi"
  - "Horst A. Obenhaus"
  - "Federico Claudi"
  - "Tiago Branco"
  - "Troy W. Margrie"
year: 2022
journal: "Scientific Reports"
paper_type: empirical
contribution_type: methodological
species:
  - mouse
methods:
  - calcium_imaging
  - electrophysiology
  - neuropixels
brain_regions:
  - hippocampus
  - visual_cortex
keywords:
  - whole_brain_microscopy
  - image_registration
  - atlas_alignment
  - probe_tracking
  - electrophysiology
  - neuropixels
  - serial_two_photon_tomography
  - calcium_imaging
  - retinotopy
  - open_source_software
  - napari_plugin
  - brain_segmentation
  - ccfv3
  - neuroanatomy
  - accurate
  - determination
  - marker
  - location
  - within
  - whole
key_citations:
  - wang2020_alternating_theta_sequences
  - claudi2021_brainrender_visualization_atlas
---

### One-line summary

Development and validation of brainreg and brainreg-segment, open-source napari plugins for accurate registration and segmentation of whole-brain microscopy images to common coordinate frameworks.

### Background & motivation

Systems neuroscience relies on implanted devices and viral injections to stimulate and record from defined neuronal populations. Accurately mapping the location of these devices in a common anatomical coordinate system is critical for correct data interpretation. While whole-brain microscopy and tissue clearing now allow automated high-resolution imaging, existing registration tools are often inflexible, time-consuming, and require considerable computational expertise.

### Methods

- **Software development**: Developed brainreg and brainreg-segment as plugins for the Python-based napari image viewer
- **Registration algorithm**: Two-step process using NiftyReg: (1) affine alignment via block-matching, (2) non-linear free-form deformation with normalized mutual information optimization
- **Validation approaches**:
  - Neuropixels probe tracking: DiI-coated probes inserted in primary visual cortex (VISp) at 1750-2000 μm depth, imaged with serial two-photon tomography
  - Injection volume segmentation: AAV-GFP injections in layer 6 of VISp in Ntsr1-cre mice
  - Functional cell localization: GCaMP7f calcium imaging of layer 2/3 neurons in VISp with receptive field mapping
- **Accuracy assessment**: Three expert raters performed repeated segmentations; electrophysiological landmarks (high-frequency LFP power peak) served as ground truth for probe location

### Key findings

- **Registration consistency**: Brainreg produced identical voxel-to-voxel registrations across 100 repeated runs on the same brains (n=3)
- **Probe tracking accuracy**: Average distance from electrophysiological ground truth (mid-VISp5) was 57.4 μm (range: -141.7 to 134.1 μm, n=21), with all raters within 84.5 μm median error
- **Systematic bias**: Direction of error was positive in 17/18 cases, indicating systematic underestimation of probe track length (median = 69.4 μm), likely due to difficulty detecting probe tips
- **Inter-rater reliability**: Intra-rater variability was below 17.4 μm SD; suboptimal DiI labeling quality was systematically flagged by all raters as a source of error
- **Injection segmentation**: Centroid distances to consensus were below 31.5 μm (median = 12.3 μm) with standard deviations under 10.5 μm across raters
- **Functional validation**: Tool successfully localized GCaMP7f-expressing neurons in layer 2/3 of VISp and demonstrated retinotopic organization of receptive fields in atlas space
- **Performance**: Registration to CCFv3 at 25 μm resolution took approximately 5 minutes on a standard laptop (Dell XPS 9380)

### Computational framework

Not applicable. This is a methods paper presenting software tools for image registration and segmentation. The computational approach involves standard image processing techniques (affine and non-linear registration using normalized mutual information, free-form deformation) rather than a specific theoretical framework for neural computation.

### Prevailing model of the system under study

Prior to this work, whole-brain microscopy registration relied on inflexible, time-consuming tools requiring considerable computational expertise. While methods existed for registering 3D datasets to atlases (e.g., AMAP), there were no open-source, user-friendly tools for segmenting arbitrary structures in registered images. The field lacked accessible pipelines for mapping implanted devices, injections, or cell populations in a common coordinate space.

### What this paper contributes

This paper introduces brainreg and brainreg-segment, open-source napari plugins that democratize whole-brain microscopy registration and segmentation. The tools enable researchers to register and segment whole-brain images on standard computing hardware within minutes, without requiring programming expertise. The validation demonstrates near-cellular resolution accuracy for localizing electrophysiological probes and injection volumes. By integrating with the BrainGlobe Atlas API and brainrender, these tools enable seamless visualization and analysis in common coordinate spaces, facilitating multi-animal pooling and cross-laboratory comparisons.

### Brain regions & systems

- **Primary visual cortex (VISp)** — validation site for probe tracking, injection segmentation, and functional imaging; electrophysiological recordings used high-frequency LFP power peak in layer 5 as ground truth landmark
- **Hippocampal formation** — used as secondary electrophysiological landmark (increased LFP power) to confirm probe depth
- **Layer 2/3 of VISp** — site of GCaMP7f injections and in vivo calcium imaging for retinotopic mapping validation
- **Layer 6 of VISp** — site of AAV-GFP injections for segmentation validation in Ntsr1-cre mice

### Mechanistic insight

Not applicable. This paper presents software tools for image registration and segmentation rather than a mechanistic account of neural computation. The work does not propose or test specific algorithms by which neural circuits perform computations, nor does it provide neural data constraining such algorithms. The validation relies on established electrophysiological landmarks (high-frequency LFP power) to assess spatial accuracy, but does not advance understanding of the mechanisms underlying visual processing or timing.

### Limitations & open questions

- Manual segmentation, while fast (seconds to minutes), may not scale to large multi-laboratory efforts where fully automated methods would be advantageous
- Systematic underestimation of probe track length (positive error bias) suggests difficulty in detecting probe tips, which may require improved labeling protocols or automated tip detection
- Volume estimation showed significant inter-rater differences despite similar centroid positions, indicating variability in judging injection borders
- Atlas resolution affects accuracy: 10 μm and 25 μm atlases yielded similar results, but 50 μm and 100 μm showed reduced accuracy
- Tool is currently limited to mouse brain atlases (CCFv3, UAA) available through BrainGlobe Atlas API

### Connections & keywords

- **Key citations**: Niedworok et al. 2016 (AMAP validation), Liu et al. 2020 (probe localization), Ragan et al. 2012 (serial two-photon tomography), Wang et al. 2020 (Allen CCFv3), Chon et al. 2019 (UAA), Jun et al. 2017 (Neuropixels), Senzai et al. 2019 (layer 5 LFP landmark), Claudi et al. 2020 (BrainGlobe Atlas API), Claudi et al. 2021 (brainrender)
- **Named models or frameworks**: brainreg, brainreg-segment, BrainGlobe Atlas API, napari, CCFv3 (Allen Mouse Brain Common Coordinate Framework version 3), UAA (Unified Anatomical Atlas), AMAP, NiftyReg, suite2p, brainrender
- **Brain regions**: primary visual cortex (VISp), hippocampal formation, layer 2/3, layer 5, layer 6
- **Keywords**: whole-brain microscopy, image registration, atlas alignment, probe tracking, electrophysiology, Neuropixels, serial two-photon tomography, calcium imaging, retinotopy, open-source software, napari plugin, brain segmentation, CCFv3, neuroanatomy
