---
source_file: "chung2022_neural_recording_neuropixels.md"
paper_id: "chung2022_neural_recording_neuropixels"
title: "High-density single-unit human cortical recordings using the Neuropixels probe"
authors: "Jason E. Chung, Kristin K. Sellers, Matthew K. Leonard, Laura Gwilliams, Duo Xu, Maximilian E. Dougherty, Viktor Kharazia, Sean L. Metzger, Marleen Welkenhuysen, Barundeb Dutta, Edward F. Chang"
year: 2022
journal: "Neuron"
paper_type: "empirical"
contribution_type: "methodological"
species: ["human"]
methods: ["electrophysiology", "neuropixels"]
brain_regions: ["superior_temporal_gyrus"]
keywords: ["high", "density", "single", "unit", "human", "cortical", "recordings", "neuropixels", "probe"]
key_citations: ["paulk2022_neuropixels_human_cortex", "buccino2020_spikeinterface_spike_sorting"]
---

### One-line summary

This paper demonstrates a reliable intraoperative method for recording up to ~100 simultaneously active putative single units across the depth of human neocortex using the Neuropixels probe, providing the first benchmarked cluster-quality metrics for human high-density silicon array recordings.

---

### Background & motivation

Single-unit recordings in humans have historically been severely limited in scale: sharp metal microelectrodes yield one neuron at a time, microwire bundles yield 1–3 neurons per array, and the Utah array cannot sample across cortical depth and requires hours to settle. Meanwhile, animal models have benefited from high-density probes like Neuropixels (960 contacts, 384 simultaneously selectable channels) that can record hundreds of neurons simultaneously. This technological gap means that detailed principles of cortical microcircuit computation established in animals cannot be directly tested in humans. The paper addresses how to translate Neuropixels technology into the intraoperative clinical environment while maintaining patient safety.

---

### Methods

- **Participants**: 15 consecutive neurosurgical patients (craniotomy for epilepsy, tumour, or cavernoma); 8 yielded isolable single units across 11 recording sessions.
- **Probe**: Neuropixels 1.0 NHP-short probe (shank thickness increased from 24 µm to 97 µm vs. rodent version), sterilised with ethylene oxide; inserted to 6–8 mm depth at 50–75 µm/s via micromanipulator fixed to Mayfield skull clamp.
- **Target sites**: cortical tissue destined for surgical resection (superior temporal gyrus, frontal lobe, motor cortex, angular gyrus), recording only within planned resection margins.
- **Recording**: 384-channel "long column" configuration spanning 7.67 mm cortical depth; ~15 min recordings; SpikeGLX acquisition.
- **Spike sorting**: Kilosort 2.5 (automated) followed by manual curation in Phy by an experienced electrophysiologist.
- **Motion quantification**: Kilosort 2.5 drift correction plus custom MTracer software to track fast-timescale motion (20 ms resolution) via high-amplitude spatial marker units.
- **Cell-pair coordination index (CCI)**: Novel cross-correlogram-based metric comparing coordinated firing within ±50 ms versus the 50–100 ms flanking window; tested relationship between CCI and inter-unit distance.
- **Cluster quality metrics**: amplitude, amplitude histogram truncation, SNR, ISI violations, isolation, d-prime, firing rate, spike half-width, spatial spread, amplitude decay, active channels.
- **Anesthesia comparison**: awake, asleep-but-not-anaesthetised, and fully anaesthetised participants compared on time-to-first-spike.

---

### Key findings

- 596 putative single units isolated across 11 recordings from 8 participants; best single-session yield was 94 units, with 34–94 units per participant.
- 50% of units were active within 8.8 ± 9.2 s of reaching target depth; 75% within 33 ± 37 s — timescales compatible with intraoperative constraints.
- Anaesthetised participants showed significantly longer latency to first spike (50th percentile: 18.4 s anaesthetised vs. 3.3 s non-anaesthetised, Wilcoxon p = 0.014).
- Unit yield did not differ by anaesthesia state, hemisphere, sex, or recording location.
- Mean electrode motion was 251 ± 112 µm (mean ± SD) across recordings; motion was negatively correlated with single-unit yield (Spearman R = −0.62, p = 0.040), identifying electrode–brain relative motion as the primary limiting factor.
- Motion did not significantly correlate with presence ratio (R = −0.19, p = 0.57), suggesting intermittent unit disappearance is not strongly predicted by mean motion amplitude alone.
- In all 4 datasets meeting inclusion (>500 eligible cell pairs), cell pairs with positive CCI (temporally coordinated within 50 ms) were significantly closer spatially than those with negative CCI — replicating and extending findings from non-human primate cortex to awake humans.
- Cluster quality metrics were reported for all 596 units, constituting the first objective benchmark for human Neuropixels recordings (median SNR 4.2, median ISI violation rate 0.06%, median isolation 0.993).

---

### Computational framework

Not applicable. The paper is a methodological resource paper with no explicit computational framework for neural computation. The cell-pair coordination index is a descriptive statistical tool (cross-correlogram-based) rather than a model of cortical computation.

The findings constrain frameworks for cortical population coding and microcircuit dynamics: the demonstration that temporally coordinated cell pairs (positive CCI) are spatially closer than anti-correlated pairs is consistent with canonical local recurrent connectivity models and with distance-dependent noise correlations documented in non-human primate studies.

---

### Prevailing model of the system under study

The introduction assumes that the action potential is the fundamental unit of neural computation and that understanding large-scale population activity across cortical layers is essential for understanding human cognition. The prevailing methodological landscape before this paper was one of severe scale limitation: human single-unit recordings were restricted to one to a few neurons simultaneously, using sharp electrodes, microwires, or the Utah array. The existing working model held that Neuropixels-class recordings — routine in rodents and increasingly in non-human primates — were not feasible in humans due to clinical constraints (probe safety, sterilisation, electrical noise in the OR, brain pulsation) and electrode reliability. The paper's introduction treats the human–animal gap not as a conceptual issue but as an engineering/translational one, framing the problem as the absence of a validated intraoperative protocol.

---

### What this paper contributes

This paper establishes that Neuropixels-class recordings at the scale of tens to ~100 simultaneous putative single units are achievable in humans undergoing clinical neurosurgery, bridging a longstanding methodological gap between animal systems neuroscience and human neurophysiology. Concretely:

- It provides the first reported cluster quality metrics for human high-density silicon array recordings, creating a reproducible benchmark.
- It identifies electrode–brain relative motion (driven by cardiac and respiratory pulsations) as the dominant bottleneck limiting yield, quantifies its magnitude (mean ~250 µm), and shows it is substantially larger than in rodent preparations.
- It validates across awake human participants the prediction from non-human primate studies that temporally coordinated cell pairs are spatially closer, demonstrating the methodology is sensitive enough to resolve cortical microcircuit dynamics in humans.
- It provides practical guidance (noise mitigation, probe fracture prevention, piotomy, motion correction) that constitutes an operational protocol for future intraoperative single-unit studies.

---

### Brain regions & systems

- **Superior temporal gyrus** — primary recording target (5 of 8 participants with isolable units); no region-specific analyses beyond yield comparison.
- **Middle frontal gyrus** — one participant; included in overall yield and motion analyses.
- **Ventral motor cortex** — one participant; included in overall analyses.
- **Angular gyrus** — one participant; included in overall analyses.

The paper does not argue for region-specific properties; recordings were opportunistic, constrained to tissue destined for resection. Brain region is a methodological parameter rather than the focus of scientific inquiry.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined. It presents no algorithm-level model of a neural computation, and no neural data are used to discriminate between competing mechanistic accounts.

The CCI analysis establishes that temporally coordinated human cortical neuron pairs are spatially closer than temporally suppressed pairs, consistent with local excitatory connectivity, but this is treated as a proof-of-concept demonstration of the methodology's resolving power rather than as a test of a specific mechanistic hypothesis. No claim is made about cell types, synaptic mechanisms, or oscillatory interactions.

---

### Limitations & open questions

- Recording duration is short (~15 min) relative to animal experiments, likely biasing unit detection toward higher firing rate cells and increasing spike-sorting error rates.
- All recordings are confined to tissue scheduled for resection; this constrains accessible regions and raises questions about whether pathological tissue affects yield.
- Probe fracture occurred in several participants, and shank breakage remains a safety risk, currently managed by restricting recordings to resection sites.
- Brain pulsation amplitude in open craniotomy is substantially larger than in burr hole or animal preparations; computational motion correction (Kilosort 2.5) compensates partially but incompletely.
- Sub-chronic or chronic implants with current Neuropixels geometry are not yet feasible due to material safety, mechanical stability, and signal longevity issues.
- No electrical stimulation capability; layer-resolved stimulation–recording experiments are deferred to future probe generations.
- Manual spike-sorting curation introduces operator-dependent variability; automated pipelines require further validation in human datasets.
- The study does not include task-based paradigms other than passive listening in some participants; cognitive neuroscience applications remain to be demonstrated at this scale.

---

### Connections & keywords

**Key citations**:
- Jun et al. (2017) — original Neuropixels probe description (Nature)
- Steinmetz et al. (2021) — Neuropixels 2.0 and Kilosort drift correction (Science)
- Paulk et al. (2022) — concurrent human Neuropixels study (Nat. Neurosci.)
- Pachitariu et al. (2016, 2021) — Kilosort spike sorting
- Buccino et al. (2020) — SpikeInterface cluster metrics
- Harris et al. (2016) — data quality in neuronal population recordings
- Hochberg et al. (2006, 2012) — Utah array brain–machine interface
- Quiroga et al. (2005) — concept cells (single-unit human recordings)
- Constantinidis & Goldman-Rakic (2002); Smith & Kohn (2008) — correlated discharge and distance in non-human primate cortex

**Named models or frameworks**:
- Kilosort 2.5 (spike-sorting algorithm with drift correction)
- Phy (manual curation GUI)
- SpikeInterface (cluster quality metrics framework)
- MTracer (custom motion-tracking software, this paper)
- Cell-pair coordination index (CCI) (this paper)

**Brain regions**:
- Superior temporal gyrus
- Middle frontal gyrus
- Ventral motor cortex
- Angular gyrus

**Keywords**:
- Neuropixels probe
- intraoperative electrophysiology
- high-density single-unit recording
- human neocortex
- electrode drift / brain pulsation
- spike sorting
- cluster quality metrics
- cortical depth recording
- cell-pair coordination index
- awake craniotomy
- translational neurophysiology
- population coding
