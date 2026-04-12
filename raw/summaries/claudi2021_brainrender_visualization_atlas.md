---
source_file: "claudi2021_brainrender_visualization_atlas.md"
paper_id: "claudi2021_brainrender_visualization_atlas"
title: "Visualizing anatomically registered data with brainrender"
authors: "Federico Claudi, Adam L Tyson, Luigi Petrucco, Troy W Margrie, Ruben Portugues, Tiago Branco"
year: 2021
journal: "eLife"
paper_type: "computational"
contribution_type: "methodological"
species: ["mouse", "human"]
methods: ["neuropixels"]
brain_regions: ["hippocampus", "thalamus", "periaqueductal_gray"]
keywords: ["visualizing", "anatomically", "registered", "data", "brainrender"]
key_citations: ["wang2020_alternating_theta_sequences"]
---

### One-line summary

Brainrender is an open-source Python package that enables interactive 3D visualization of multidimensional datasets registered to any neuroanatomical atlas, filling a gap left by tools restricted to single atlases or data types.

---

### Background & motivation

Large-scale brain imaging and connectomics projects generate multidimensional datasets that must be co-registered to a common reference frame for meaningful interpretation. Existing 3D visualization tools (e.g., cocoframer, BrainMesh, SHARPTRACK) are each locked to a single atlas or species, cannot combine data from multiple sources in one rendering, and are unavailable in Python — the dominant language of the modern neuroscience software ecosystem. There was therefore no general-purpose, Python-based tool allowing researchers with modest programming skills to produce high-quality 3D renderings that merge atlas structure, cell locations, neuronal morphologies, connectomics streamlines, and other data types in a single scene.

---

### Methods

- **Software design**: Open-source Python package (≥3.6) built on top of the vedo rendering engine (VTK-based) and BrainGlobe's AtlasAPI, which provides a unified programmatic interface to multiple atlases (Allen Mouse, larval zebrafish, human, and others).
- **Atlas integration**: Uses AtlasAPI to download 3D mesh data and hierarchical region metadata; the same code works for any supported atlas by simply specifying the atlas name.
- **Data type support**: Renders brain region meshes, labeled cell coordinates (.npy), neuronal morphologies (.swc via morphapi), mesoscale connectomics streamlines (.json), implanted probe tracks, volumetric gene expression data, and arbitrary 3D meshes (.obj, .stl).
- **Output formats**: Interactive real-time rendering, high-resolution screenshots, animated videos (keyframe-based), and embeddable HTML interactive scenes.
- **GUI**: A graphical user interface covers core functionality (render regions, cells, images) for users who prefer not to write Python.
- **Benchmarking**: Performance tested across four machine configurations (with/without GPU, macOS/Linux/Windows) for five task types: rendering 10k/100k/1M cells, slicing scenes, rendering all Allen brain regions (~1678 meshes), animation, and volumetric gene expression rendering.

---

### Key findings

- Brainrender can render 10,000 cells in under 2 seconds on standard laptop hardware; a GPU improves interactive frame rate by approximately 3.5×.
- At 1 M cells (98 M mesh vertices), frame rates range from 0.03–2.65 fps depending on hardware; for typical use cases (far fewer vertices) performance is adequate without a GPU.
- Brainrender is 20× faster than napari at rendering mesh data (though 5× slower for raw image/voxel data), and achieves superior rendering quality in both cases.
- The same Python code can visualize data from mouse, zebrafish, and human atlases without modification beyond specifying the atlas name.
- All figures and videos in the paper were produced directly in brainrender without post-processing, demonstrating publication-ready output quality.

---

### Computational framework

Not applicable in the sense of a neuroscientific model. Brainrender is a software engineering contribution. Its technical framework is:

- **Rendering engine**: vedo (Python wrapper around VTK) for 3D mesh rendering.
- **Atlas abstraction**: BrainGlobe AtlasAPI provides a unified interface mapping region names to 3D mesh files and hierarchical ontologies.
- **Scene/Actor model**: A central Scene object coordinates camera, lighting, and rendering; data items are encapsulated as Actors with configurable appearance properties (color, transparency, slicing planes).
- **Data pipeline**: Raw experimental data (coordinates, .swc files, image volumes) is parsed into the Actor format, decoupling data ingestion from rendering.

---

### Prevailing model of the system under study

The paper does not study a neural system in the theoretical sense. Its introduction surveys the landscape of existing neuroanatomical visualization software and identifies their limitations: single-atlas lock-in (cocoframer, BrainMesh, SHARPTRACK), single-species focus (natverse for Drosophila), restricted data types (Simple Neurite Tracer for morphology only), single-brain image data (MagellanMapper), and non-Python implementation. The implicit baseline "model" is therefore a fragmented software ecosystem requiring researchers to use multiple incompatible tools or invest substantial custom development effort to combine atlas and experimental data in 3D.

---

### What this paper contributes

Brainrender provides a single, extensible Python tool that replaces the fragmented toolchain. Concretely:

- Any atlas supported by the AtlasAPI can be used without code modification, eliminating atlas lock-in.
- Multiple data types (cells, morphologies, probes, streamlines, gene expression, custom meshes) can appear together in one rendering — previously requiring separate tools or bespoke code.
- Publication-quality figures, animated videos, and interactive online HTML visualizations are produced programmatically with minimal code, lowering the barrier for dissemination of anatomically registered data.
- Integration with other BrainGlobe tools (cellfinder, brainreg, morphapi) creates a cohesive end-to-end pipeline from raw image data through registration to visualization within a single Python ecosystem.

---

### Brain regions & systems

Not applicable as a primary focus. Brainrender is a generic visualization tool applicable to any brain region or species. Brain regions appear in the paper only as demonstration examples:

- Superior colliculus (mouse) — shown with viral injection volumes and probe tracks
- Primary motor cortex (mouse) — shown with efferent connectomics streamlines
- Hippocampus (mouse) — shown with gene expression data
- Periaqueductal gray (mouse) — shown with single-neuron morphology reconstruction
- Cerebellum and tectum (larval zebrafish) — shown with region meshes and gene expression
- Thalamus (mouse) — shown with neuron morphology projections
- Human precentral/postcentral gyrus and temporal lobe — shown to demonstrate multi-species capability

---

### Mechanistic insight

Does not meet the bar. Brainrender is a software tool paper; it does not propose or test any algorithm describing a neural computation, and presents no neural recording, imaging, or lesion data in the scientific sense. The paper's evidence is entirely about software performance benchmarks and visualization quality demonstrations.

---

### Limitations & open questions

- Pre-processing steps (atlas registration of raw image data) remain technically demanding and must be done outside brainrender; the tool handles visualization only after registration.
- Adding new atlases to the AtlasAPI requires substantial programming skills and is non-trivial for most users.
- Volumetric/image data rendering is substantially slower (5×) than napari and less developed than mesh-based rendering.
- High-performance rendering software (e.g., Blender) can surpass brainrender on mesh complexity, but at the cost of a steep learning curve and no built-in atlas integration.
- Embedding interactive HTML renderings in web pages remains technically challenging; further development is needed to make online dissemination seamless.
- Installation of Python and brainrender may be difficult for users without programming experience; a standalone desktop application is a stated future goal.
- The GUI covers only core functionality; advanced programmatic usage is still required for complex custom visualizations.

---

### Connections & keywords

**Key citations**:
- Claudi et al. 2020 — BrainGlobe AtlasAPI (foundational dependency)
- Oh et al. 2014 — Allen Mouse Connectome (atlas and streamlines data source)
- Wang et al. 2020 — Allen Mouse Brain Common Coordinate Framework CCFv3
- Kunst et al. 2019 — larval zebrafish cellular-resolution atlas
- Winnubst et al. 2019 — MouseLight single-neuron morphology dataset
- Steinmetz et al. 2019 — Neuropixels probe data used as demonstration
- Tyson et al. 2020a — cellfinder (integrated BrainGlobe tool)
- Tyson & Rousseau 2020b — brainreg (integrated BrainGlobe registration tool)
- Bates et al. 2020 — natverse (compared tool, Drosophila-focused)
- Arshadi et al. 2020 — Simple Neurite Tracer (compared tool)
- Musy et al. 2019 — vedo rendering engine (core dependency)
- Ascoli et al. 2007 — NeuroMorpho.Org (morphology database accessed via morphapi)

**Named models or frameworks**:
- BrainGlobe suite
- BrainGlobe AtlasAPI
- brainrender Scene/Actor model
- vedo (VTK-based rendering engine)
- morphapi

**Brain regions**: Superior colliculus, primary motor cortex, hippocampus, periaqueductal gray, cerebellum, tectum, thalamus, secondary motor cortex, retrosplenial cortex, zona incerta, lateral geniculate nucleus

**Keywords**: 3D brain visualization, neuroanatomical atlas, Python neuroscience tools, atlas registration, brain-wide imaging, neuronal morphology rendering, mesoscale connectomics, BrainGlobe, open-source neuroscience software, multi-atlas compatibility, interactive 3D rendering, volumetric data visualization
