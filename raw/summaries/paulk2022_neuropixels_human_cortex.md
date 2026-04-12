---
source_file: "paulk2022_neuropixels_human_cortex.md"
paper_id: "paulk2022_neuropixels_human_cortex"
title: "Large-scale neural recordings with single neuron resolution using Neuropixels probes in human cortex"
authors: "Angelique C. Paulk, Yoav Kfir, Arjun R. Khanna, Martina L. Mustroph, Eric M. Trautmann, Dan J. Soper, Sergey D. Stavisky, Marleen Welkenhuysen, Barundeb Dutta, Krishna V. Shenoy, Leigh R. Hochberg, R. Mark Richardson, Ziv M. Williams, Sydney S. Cash"
year: 2022
journal: "Nature Neuroscience"
paper_type: "empirical"
contribution_type: "methodological"
species: ["human"]
methods: ["electrophysiology", "neuropixels"]
brain_regions: ["prefrontal_cortex", "dorsolateral_prefrontal_cortex"]
keywords: ["jun_et_al_2017_original_neuropixels_1_0_probe_description", "steinmetz_et_al_2021_neuropixels_2_0_improvements", "trautmann_et_al_2019_neuropixels_in_nhps", "population_dynamics_without_spike_sorting", "jia_et_al_2019_high_density_probes_reveal_dendritic_backpropagation_and_neuron_classification", "truccolo_et_al_2011_single_neuron_dynamics_in_human_focal_epilepsy", "cash_and_hochberg_2015_review_on_single_neurons_in_clinical_neurology", "named_models_or_frameworks", "neuropixels_probe_technology_1_0_and_1_0_s_variants", "kilosort_3_0_spike_sorting_algorithm", "wavemap_umap_louvain_clustering_for_waveform_classification", "burst_suppression_detection_algorithm_westover_et_al", "brain_regions", "dorsolateral_prefrontal_cortex_dlpfc", "lateral_temporal_lobe_cortex", "keywords", "neuropixels", "human_electrophysiology", "intraoperative_recording", "single_unit_activity"]
---

### One-line summary

The authors developed and validated a modified Neuropixels 1.0-S probe and associated techniques for large-scale single-unit recordings in human cortex during intraoperative neurosurgical procedures, demonstrating the ability to record from over 200 well-isolated neurons simultaneously.

### Background & motivation

While animal models have benefited from high-density multi-electrode arrays capable of recording hundreds to thousands of neurons, human intracranial electrophysiology has been limited to small numbers of isolatable units (10–150) per device. This gap limits understanding of human-specific cognitive processes and their dysfunction. The Neuropixels probe, with 384 channels and 20 µm electrode spacing, has revolutionized animal recordings but required significant adaptation for safe, effective use in human intraoperative settings.

### Methods

- **Probe development**: Used a modified Neuropixels 1.0-S probe with thicker shank (100 µm vs. 25 µm) to reduce fracture risk during human neurosurgical insertion
- **Sterilization**: Developed ethylene oxide sterilization protocols with IMEC and Bioseal; packaged probes in modified SteriBest Trays for safe transport
- **Surgical insertion**: Two approaches tested: (1) ROSA robot with Alpha Omega manipulator for DBS cases traversing dlPFC; (2) sterile syringe attached to Greenberg retractor-mounted micromanipulator for open craniotomies
- **Participants**: 9 patients total (3 successful recordings analyzed: 2 DBS patients in dlPFC—one awake, one anesthetized; 1 temporal lobe epilepsy patient under general anesthesia; 6 unsuccessful recordings due to electrode fracture or excessive noise)
- **Movement correction**: Developed semi-automated post-hoc manual registration using LFP-based tracking of tissue motion (cardiac/respiratory pulsation) in Blender, followed by spatial interpolation
- **Spike sorting**: Kilosort 3.0 with manual curation in Phy; clusters classified as single units vs. multi-unit activity (MUA) based on waveform consistency and ISI distributions
- **Unit classification**: Three approaches compared: (1) single-channel classification (RS, FS, PS based on waveform duration and polarity); (2) multi-channel PCA + k-means clustering; (3) WaveMAP (UMAP + Louvain clustering)
- **Analysis of clinical events**: Aligned single-unit activity to interictal epileptiform discharges (IIDs) and burst suppression events; computed pairwise unit covariance

### Key findings

- **Recording yield**: Successfully recorded 201 ± 151 isolatable units per session (262 units in Pt. 01 anesthetized dlPFC; 312 units in Pt. 02 awake dlPFC; 29 units in Pt. 03 anesthetized temporal lobe). Single units: Pt. 01: 202; Pt. 02: 178; Pt. 03: 19
- **Waveform diversity**: Identified 8 separable single-unit classes using WaveMAP (4 positive spike classes, 4 negative classes including RS-like, FS-like, triphasic, broad). Positive spike units had wider waveforms (494.2 µs duration vs. 349.6 µs for FS/RS) and higher firing rates (1.1 Hz vs. 0.3–0.4 Hz)
- **Spatial spread**: 52% of units had significant deflections across multiple channels (up to 12 channels). Positive spike units showed significantly higher spatial spread than RS/FS units. Waveform classes showed differential laminar distributions along the probe
- **Movement artifact**: Tissue motion from cardiac/respiratory pulsation was 80–100 µm on average, with mean velocity of 76.5 µm/s. Movement was significantly higher in the awake patient (LFP variance: 26.15) compared to anesthetized patients (2.31 and 4.47). Post-hoc manual correction reduced motion to 20–40 µm (sub-cellular scale)
- **Unit tracking stability**: Units could be tracked through time with high correlation between movement-corrected and raw data (mean Pearson's r: 0.64–0.65). Mean detection time range: 480 ± 130 s; units detected for 71–82% of recording duration
- **Spike-field relationships**: Single units showed significant modulation by interictal epileptiform discharges (IIDs) and burst suppression. During IIDs: significant increase in spike rate in half-second after IID peak (P < 0.005). During burst suppression: 25–55% of units showed significant firing rate modulation, with different units responding before, during, or after burst onset
- **Pairwise unit interactions**: 6.9% of unit pairs showed significant covarying relationships (8 s.d. above baseline). Average absolute lag: 13.9 ms; 58% of pairs showed >5 ms lag, 46% showed >10 ms lag

### Computational framework

Not applicable. This is a methods/technical paper focused on developing and validating a new recording technology for human use. The paper does not propose or test a computational model. However, the data generated could constrain models of:
- Neuronal population dynamics during anesthesia (burst suppression mechanisms)
- Circuit-level interactions during epileptiform activity
- Cell type-specific contributions to LFP signals

### Prevailing model of the system under study

The field assumed that large-scale single-unit recordings in humans were technically limited by existing electrode technologies (microwires, Utah arrays, laminar electrodes), which could only isolate 10–150 units per device with limited spatial resolution (>150 µm contact spacing). This constrained observations to neurons with large, distinct waveforms and high firing rates, biasing sampling toward certain cell types. The prevailing assumption was that cardiac and respiratory motion artifacts would make stable single-unit recordings difficult in the human operating room without physical brain stabilization (which was not possible for patient safety reasons).

### What this paper contributes

This paper demonstrates that large-scale single-unit recordings in human cortex are feasible using adapted Neuropixels probes, fundamentally expanding the scale and quality of human electrophysiology:

- **Technical feasibility**: Developed a thicker Neuropixels 1.0-S probe (100 µm shank) that withstands human neurosurgical insertion, along with sterilization protocols, grounding configurations, and surgical integration (robotic and manual approaches)
- **Recording scale**: Achieved 200+ simultaneously recorded single units per session—a 2–20× increase over existing human technologies—demonstrating the ability to capture large neuronal populations in intraoperative settings
- **Motion correction**: Developed semi-automated post-hoc registration using LFP-based tracking that reduces motion artifacts to sub-cellular scale (~20–40 µm), enabling stable unit isolation despite cardiac/respiratory brain pulsation
- **Cell type classification**: Using high-density spatial sampling, identified 8 separable unit classes with distinct waveform features, firing rates, and laminar distributions—providing more nuanced cell type categorization than traditional RS/FS binary classification
- **Spike-field relationships**: Demonstrated that single-unit activity modulates with clinically relevant LFP events (interictal discharges, burst suppression), validating the approach for studying pathophysiology
- **Circuit interactions**: Detected pairwise covariance between units with millisecond-scale temporal lags, suggesting the approach can reveal microcircuit dynamics

The paper establishes a foundation for studying human cortical function at unprecedented spatiotemporal resolution and opens pathways for clinical applications including epilepsy mechanisms, brain-computer interfaces, and neurosurgical planning.

### Brain regions & systems

- **Dorsolateral prefrontal cortex (dlPFC)** — Recorded from two patients during DBS placement for movement disorders; one awake, one under general anesthesia. Site traversed en route to subcortical targets.
- **Lateral temporal lobe cortex** — Recorded from one patient undergoing anterior temporal lobectomy for epilepsy; under general anesthesia with burst suppression.

The paper notes recordings were limited to tissue already planned for resection or cannula passage, ensuring patient safety even if electrode fracture occurred.

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined in the template. While it presents methods for recording neural activity and demonstrates relationships between units and LFP events, it does not:

1. Present or formalize a computational algorithm that explains a neural phenomenon
2. Provide neural data that specifically supports that algorithm over alternatives

The paper is primarily methodological, establishing feasibility of high-density recordings in humans. It describes observations (cell type diversity, spike-field relationships, pairwise covariances) but does not mechanistically explain how these phenomena arise or what computational principles govern them. The findings establish a foundation for future mechanistic studies but do not themselves provide algorithmic or implementational-level explanations.

### Limitations & open questions

- **Sample size and selection**: Only 3 successful recordings from 9 attempted cases; limited to neurosurgical patients with specific clinical indications (epilepsy, DBS), not representative of healthy brain
- **Recording duration**: Limited to ~15 minutes per case due to operating room time constraints; may miss cell types that fire infrequently or in specific contexts; optimal stability requires 45+ minutes based on animal studies
- **Anesthesia confounds**: Two of three recordings under general anesthesia with burst suppression, affecting observed physiology; spike rates and waveform shapes may be altered by anesthetic agents
- **Motion artifacts**: Brain pulsation from cardiac/respiratory rhythms caused 80–100 µm movement; manual correction reduced to 20–40 µm but likely excluded smaller-amplitude units; automated motion correction methods not yet validated for human data
- **Spatial sampling limitations**: Only a single linear electrode array per recording; cannot sample widespread circuits or inter-columnar interactions; insertion angles limited by surgical constraints (burr hole location, curved gyral surfaces)
- **Cell type identification**: Cannot definitively link extracellular waveform classes to specific cell types without histological validation; positive spikes hypothesized to be axonal but unconfirmed in human tissue
- **Clinical translation barriers**: Acute recordings only; chronic implantation not addressed; electrode fracture risk (2 of 9 cases); regulatory and safety hurdles for chronic human use remain

### Connections & keywords

**Key citations:**
- Jun et al. (2017) — Original Neuropixels 1.0 probe description
- Steinmetz et al. (2021) — Neuropixels 2.0 improvements
- Trautmann et al. (2019) — Neuropixels in NHPs, population dynamics without spike sorting
- Jia et al. (2019) — High-density probes reveal dendritic backpropagation and neuron classification
- Truccolo et al. (2011) — Single-neuron dynamics in human focal epilepsy
- Cash & Hochberg (2015) — Review on single neurons in clinical neurology

**Named models or frameworks:**
- Neuropixels probe technology (1.0 and 1.0-S variants)
- Kilosort 3.0 spike sorting algorithm
- WaveMAP (UMAP + Louvain clustering for waveform classification)
- Burst suppression detection algorithm (Westover et al.)

**Brain regions:**
- Dorsolateral prefrontal cortex (dlPFC)
- Lateral temporal lobe cortex

**Keywords:**
Neuropixels, human electrophysiology, intraoperative recording, single-unit activity, cell type classification, waveform analysis, motion correction, brain-computer interface, epilepsy, deep brain stimulation, dorsolateral prefrontal cortex, temporal lobe, silicon probe, spike sorting, laminar distribution, interictal discharges, burst suppression
