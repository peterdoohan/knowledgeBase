---
source_file: wang2020_allen_mouse_brain_atlas.md
title: The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas
authors: Quanxin Wang, Song-Lin Ding, Yang Li, Josh Royall, David Feng, Phil Lesnar, Nile Graddis, Maitham Naeemi, Benjamin Facer, Anh Ho, Tim Dolbeare, Brandon Blanchard, Nick Dee, Wayne Wakeman, Karla E. Hirokawa, Aaron Szafer, Susan M. Sunkin, Seung Wook Oh, Amy Bernard, John W. Phillips, Michael Hawrylycz, Christof Koch, Hongkui Zeng, Julie A. Harris, Lydia Ng
year: 2020
journal: Cell
paper_type: empirical
contribution_type: methodological
---

### One-line summary

A 3D reference atlas of the mouse brain at 10 μm cellular resolution, constructed from 1,675 mice and parcellated into 43 isocortical areas (with layers), 329 subcortical structures, 81 fiber tracts, and 8 ventricular structures.

### Background & motivation

Large-scale brain mapping projects generate massive multimodal datasets across spatial scales and brain areas, but integration requires a standard 3D reference atlas. Existing atlases had limitations: 2D plate-based atlases lack 3D spatial coherence, and previous 3D atlases had lower resolution (100 μm voxels) with irregular borders when viewed in non-coronal planes. The BRAIN Initiative Cell Census Network required cellular-level resolution (10–20 μm) for cell type mapping.

### Methods

- **Template construction**: Average template created from 1,675 young adult C57BL/6J mice (1,051 male, 621 female) imaged with serial two-photon tomography (STPT) at 0.35 μm/pixel in-plane with 100 μm z-sampling
- **Registration**: Iterative symmetric diffeomorphic registration (following Fonov et al., 2011 methods), with each hemisphere reflected across midline for symmetry (3,350 total image series)
- **Resolution**: Final template at 10 μm isotropic voxels (1,320 × 1,140 × 800 voxels; ~506 million voxels)
- **Parcellation approach**: Direct 3D annotation using ITK-SNAP, with structures drawn in coronal, sagittal, and horizontal planes simultaneously
- **Curved cortical coordinates**: Laplace's equation solved between pial surface and layer 6b/white matter boundary to create streamlines approximating columnar organization
- **Reference datasets**: Multimodal data including transgenic Cre lines (e.g., Calb1-T2A-dgCre, Fezf2-CreER, Rorb-IRES2-Cre), anterograde tracing from Allen Mouse Connectivity Atlas, immunohistochemistry (NeuN, parvalbumin, SMI-32, SMI-99, NF-160, calbindin), cytoarchitecture (Nissl, AChE), and ISH data from Allen Brain Atlas

### Key findings

- **Average template**: High signal-to-noise template revealing anatomical details not visible in single specimens, including whisker barrel fields in SSp-bfd, barrelettes in SPVI, barreloids in VPM, and cortical layers
- **Isocortical parcellation**: 43 areas delineated using curved coordinates and multimodal data; primary sensory areas (VISp, AUDp, SSp) identified by intrinsic contrast and validated with Rorb-IRES2-Cre (L4 marker); retrosplenial areas identified with Chrna2-Cre_OE25; higher visual areas (9 areas) identified using visuotopic connectivity maps and callosal patterns
- **Cortical layers**: 6 layers (L1, L2/3, L4, L5, L6a, L6b) delineated across all isocortical areas using layer-specific Cre lines; L4 absent in prelimbic, infralimbic, orbital, agranular insular, motor, anterior cingulate, retrosplenial, perirhinal, and ectorhinal areas; intersection of areas and layers yielded 242 cortical structure volumes
- **Subcortical structures**: 329 gray matter structures delineated across 11 major divisions (hippocampal formation, cortical subplate, striatum, pallidum, thalamus, hypothalamus, midbrain, pons, medulla, cerebellum, olfactory areas); example: interpeduncular nucleus (IPN) divided into 8 subdivisions (IPR, IPC, IPI, IPL, IPA, IPDM, IPDL, IPRL) using cytoarchitecture, immunohistochemistry, transgene expression, and connectivity data; 36 structures added that were not in previous ARA/CCFv2 ontologies
- **Fiber tracts**: 81 white matter structures delineated using inherent contrast in template, anterograde tracing, and antibody staining; identified separate corpus callosum (cc) and supracallosal cerebral white matter (scwm) based on distinct laminar organization (callosal fibers in mid-to-deep white matter, thalamocortical fibers in upper white matter); added 4 new fiber tracts (optic radiation, auditory radiation, body of corpus callosum, supracallosal cerebral white matter)
- **Ventricular structures**: 8 structures delineated (lateral ventricle, third ventricle, cerebral aqueduct, fourth ventricle, central canal, associated recesses and choroid plexuses) using inherent contrast, Nissl stains, and transgenic lines labeling ependymal epithelia
- **Volume measurements**: Whole brain volumes for 1,675 mice ranged 359–545 mm³ (mean 435 ± 23.5 mm³, CoV = 5.4%); no significant sex difference; CCFv3 template ~15% larger than average individual brain due to morphological template construction
- **Applications**: CCFv3 enables reverse mapping (atlas to individual brain space), volume estimation, integration of multimodal data (MRI, light sheet, electrophysiology, calcium imaging); web applications include Atlas Viewer (2D), Brain Explorer (3D), API and AllenSDK for programmatic access

### Computational framework

Not applicable. This is a resource/methodology paper focused on creating a 3D reference atlas using image registration, averaging, and manual annotation techniques. The computational approaches involve diffeomorphic image registration (symmetric normalization algorithm), Laplace's equation for cortical coordinate generation, and marching cubes for surface mesh generation. The work provides a structural framework that constrains computational models of brain organization but does not itself propose a computational model of neural function.

### Prevailing model of the system under study

Prior to CCFv3, the field relied on 2D plate-based atlases (Allen Reference Atlas, Paxinos and Franklin Mouse Brain in Stereotaxic Coordinates) or lower-resolution 3D atlases (CCFv1 at 200 μm, CCFv2 at 100 μm). These atlases had significant limitations: 2D atlases lack 3D spatial coherence and have straight border lines that don't reflect true cortical curvature; CCFv2 suffered from irregular, non-biological borders when viewed in non-coronal planes due to conversion from 2D annotations; and all existing atlases lacked cellular-level resolution required for modern large-scale cell type mapping efforts (e.g., BRAIN Initiative Cell Census Network).

### What this paper contributes

CCFv3 provides the first cellular-resolution (10 μm isotropic voxel) 3D reference atlas for the mouse brain, constructed from 1,675 mice using iterative symmetric diffeomorphic registration. The atlas introduces: (1) a high signal-to-noise average template revealing anatomical details invisible in single specimens; (2) direct 3D parcellation producing smooth, biologically realistic borders in all planes; (3) curved cortical coordinates enabling accurate columnar/streamline-based analysis of the isocortex; (4) comprehensive annotation of 658 structures (43 isocortical areas with 6 layers each, 329 subcortical gray matter structures, 81 fiber tracts, 8 ventricular structures); (5) 36 newly delineated structures not present in previous atlases; (6) open access web tools, API, and SDK for integration with multimodal datasets. The atlas overcomes fundamental limitations of 2D atlases and previous 3D versions, enabling cellular-resolution data integration across labs and modalities.

### Brain regions & systems

**Isocortex (43 areas with 6 layers each = 242 structures total):**
- Primary sensory areas: VISp (primary visual), AUDp (primary auditory), SSp-bfd (somatosensory barrel field), SSp-m (mouth), SSp-n (nose), SSp-ul (upper limb), SSp-ll (lower limb), SSp-tr (trunk), SSp-un (unassigned)
- Motor areas: MOp (primary motor), MOs (secondary motor)
- Visual areas: VISa (anterior), VISal (anterolateral), VISam (anteromedial), VISl (lateral), VISli (laterointermediate), VISpl (posterolateral), VISpm (posteromedial), VISpor (postrorhinal), VISrl (rostrolateral)
- Auditory areas: AUDd (dorsal), AUDpo (posterior), AUDv (ventral)
- Cingulate areas: ACAd (dorsal), ACAv (ventral)
- Prefrontal areas: PL (prelimbic), ILA (infralimbic), ORBl (lateral orbital), ORBm (medial orbital), ORBvl (ventrolateral orbital)
- Insular areas: AI (agranular insular) - posterior, dorsal, ventral parts
- Retrosplenial areas: RSPagl (agranular), RSPd (dorsal), RSPv (ventral)
- Other areas: ECT (ectorhinal), PERI (perirhinal), TEa (temporal association), FRP (frontal pole), SSs (supplemental somatosensory area)

**Subcortical gray matter (329 structures across 11 major divisions):**
- Olfactory areas: main olfactory bulb, accessory olfactory bulb, olfactory tubercle, piriform area, etc.
- Hippocampal formation: CA1, CA2, CA3, dentate gyrus, subiculum, presubiculum, postsubiculum, etc.
- Cortical subplate: claustrum, endopiriform nucleus, etc.
- Cerebral nuclei: striatum (caudoputamen, nucleus accumbens), pallidum (globus pallidus externa/interna), etc.
- Thalamus: ventral posteromedial (VPM), ventral posterolateral (VPL), lateral geniculate complex (LGd-sh, LGd-co, LGd-ip), lateral posterior, etc.
- Hypothalamus: suprachiasmatic, paraventricular, ventromedial, dorsomedial, lateral hypothalamic area, etc.
- Midbrain: superior colliculus, inferior colliculus, interpeduncular nucleus (8 subdivisions), ventral tegmental area, etc.
- Pons: pontine gray, reticular nuclei, etc.
- Medulla: inferior olivary complex, vestibular nuclei, etc.
- Cerebellum: cerebellar cortex (lobules), cerebellar nuclei (fastigial, interposed, dentate)

**Fiber tracts (81 structures):**
- Corpus callosum (genu, body, splenium, forceps), cingulum bundle, internal/external capsule, cerebral peduncle, optic tract, auditory radiation, etc.

**Ventricular structures (8 structures):**
- Lateral ventricle, third ventricle, cerebral aqueduct, fourth ventricle, central canal, choroid plexuses

### Mechanistic insight

Not applicable. This paper describes the construction of a structural reference atlas and does not propose or test mechanistic models of neural computation or function. The work provides anatomical infrastructure that constrains mechanistic models but does not itself address Marr's levels of analysis for any specific neural computation.

### Limitations & open questions

- The CCFv3 average template is ~15% larger than the average of individual brains used in its construction (506 mm³ vs 435 mm³) due to morphological template construction process
- Relationship to skull fiducial landmarks (e.g., Bregma) is unknown; not suitable for stereotaxic coordinates without additional registration to skull-based imaging
- Registration precision may vary across imaging modalities; best for STPT data
- Manual annotation process was time- and labor-intensive, limiting the number of structures that could be delineated (658 vs 946 in MBSC atlas)
- Some structures could not be delineated due to lack of available multimodal data defining their boundaries
- Straight border lines in 2D atlases may not reflect true cortical curvature, but the biological accuracy of curved borders in CCFv3 has not been systematically validated against independent experimental data
- The atlas represents young adult C57BL/6J mice only; does not capture developmental, aging, or strain variation

### Connections & keywords

**Key citations:**
- Paxinos and Franklin (2001, 2012) - Mouse Brain in Stereotaxic Coordinates (MBSC)
- Dong (2008) - Allen Reference Atlas (ARA)
- Swanson (2004, 2018) - Brain Maps: Structure of the Rat Brain
- Oh et al. (2014) - Allen Mouse Brain Connectivity Atlas (CCFv2)
- Lein et al. (2007) - Allen Brain Atlas gene expression
- Fonov et al. (2011) - Human MRI population average template methods
- Wang and Burkhalter (2007) - Mouse visual cortex area map

**Named models or frameworks:**
- Allen Mouse Brain Common Coordinate Framework v3 (CCFv3)
- Serial Two-Photon Tomography (STPT)
- Symmetric Diffeomorphic Registration (SyN algorithm)
- Laplace-based cortical coordinate system (streamlines)
- Allen Reference Atlas (ARA) ontology
- Brain Maps ontology (Swanson)
- Mouse Brain in Stereotaxic Coordinates (MBSC) ontology

**Brain regions:**
- Isocortex (43 areas with 6 layers each)
- Olfactory areas (main olfactory bulb, accessory olfactory bulb, piriform area)
- Hippocampal formation (CA1, CA2, CA3, dentate gyrus, subiculum, presubiculum, postsubiculum, prosubiculum)
- Cortical subplate (claustrum, endopiriform nucleus)
- Striatum (caudoputamen, nucleus accumbens)
- Pallidum (globus pallidus external/internal segments)
- Thalamus (ventral posteromedial, ventral posterolateral, lateral geniculate complex with shell/core/ipsilateral subdivisions, lateral posterior, anteromedial, anteroventral, laterodorsal, etc.)
- Hypothalamus (suprachiasmatic, paraventricular, ventromedial, dorsomedial, lateral hypothalamic area, etc.)
- Midbrain (superior colliculus, inferior colliculus, interpeduncular nucleus with 8 subdivisions, ventral tegmental area, etc.)
- Pons (pontine gray, reticular nuclei, etc.)
- Medulla (inferior olivary complex, vestibular nuclei, etc.)
- Cerebellum (cerebellar cortex lobules, fastigial/interposed/dentate nuclei)
- Fiber tracts (corpus callosum, cingulum bundle, internal/external capsule, cerebral peduncle, optic tract, auditory radiation, etc.)
- Ventricular system (lateral ventricle, third ventricle, cerebral aqueduct, fourth ventricle, central canal, choroid plexuses)

**Keywords:**
- brain atlas
- common coordinate framework
- mouse brain
- serial two-photon tomography
- image registration
- brain parcellation
- neuroanatomy
- isocortex
- subcortical structures
- fiber tracts
- multimodal integration
- cellular resolution
- Cre driver lines
- connectivity mapping
- Laplace coordinates
- diffeomorphic registration
- open access neuroscience
