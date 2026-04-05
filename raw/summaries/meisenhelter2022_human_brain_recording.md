---
source_file: meisenhelter2022_human_brain_recording.md
title: "Probing the human brain at single-neuron resolution with high-density cortical recordings"
authors: Stephen Meisenhelter, Ueli Rutishauser
year: 2022
journal: Neuron
paper_type: review
contribution_type: review
---

### One-line summary

This Neuron "Previews" commentary synthesises the significance of two concurrently published studies (Chung et al. 2022; Paulk et al. 2022) demonstrating the first successful use of the Neuropixels high-density silicon probe for intraoperative single-neuron recordings in the human cortex.

---

### Background & motivation

Extracellular single-neuron recordings are a cornerstone tool for understanding neural computation, and simultaneously recording from large populations of neurons has revealed insights into population-level coding that single-cell recordings cannot provide. In non-human animals, high-density silicon probes (especially Neuropixels) have dramatically increased the number of simultaneously recorded neurons, but equivalent technology had not been applied in humans. Previous human single-neuron recordings used microwire bundles or Utah arrays, which lack the spatial density needed for laminar-resolution recordings and high-confidence spike sorting. This commentary contextualises two studies that overcome the technical and clinical hurdles blocking Neuropixels use in humans.

---

### Methods

This is a review/commentary piece synthesising two primary studies; no original data were collected by the authors.

- **Literature covered**: Chung et al. (2022) and Paulk et al. (2022), both published in the same issue/period of Neuron and Nature Neuroscience respectively, reporting intraoperative Neuropixels recordings in neurosurgical patients (epilepsy surgery or brain tumour resection).
- **Synthesis method**: Narrative commentary; the authors describe the technical challenges and solutions reported by both groups, highlight key metrics (signal quality, unit yield, brain motion), and discuss future opportunities.
- Key technical parameters reported from the primary studies: 960-channel probe, 10 mm shank, electrode contacts every 20 µm (12 × 12 µm pads), median 54.2 single units per probe, median signal-to-noise ratio 4.2, noise floor 6.81 µV (300–6,000 Hz band), single units became active ~8.8 s post-insertion, mean brain pulsation ~251 µm vertical displacement.

---

### Key findings

- Neuropixels probes can be used safely in intraoperative human recordings: probes were inserted only into tissue scheduled for resection, sterilised to medical grade, and no histological tissue compatibility problems were observed.
- Up to ~100 single units were recorded simultaneously per session (up to 20 min), with a median of 54.2 single units per probe.
- The typical electrode settling problem seen in animal recordings was largely absent: units became active within ~8.8 s of insertion, making short intraoperative sessions feasible.
- A single neuron was detectable on a median of 11 channels, markedly improving spike-sorting confidence over less-dense arrays.
- 52% of units (Paulk et al.) were visible on multiple channels at ≥5 SD above background noise.
- Brain pulsation (~251 µm average vertical motion) was manageable: a motion-correction algorithm and probe geometry (7 mm of 10 mm shank inserted) allowed continuous tracking and correction.
- Probe fragility (snapping) occurred in early subjects in both studies but resolved with increasing operator experience.
- The key unique advantage of Neuropixels over prior human recording tools (Behnke-Fried microwires, Utah array) is the laminar-resolution spatial density, enabling assessment of activity across cortical layers and local field potential mapping at micro-scale.

---

### Computational framework

Not applicable. This is a commentary on recording technology and its application; no computational framework is employed. The findings are directly relevant to frameworks requiring population-level or laminar-resolved neural data (e.g. canonical microcircuit models, cortical column models), but no such framework is formalised here.

---

### Prevailing model of the system under study

The introduction frames the field around a well-established trend: the number of simultaneously recorded neurons in animal studies has doubled roughly every 7 years, and population-level recordings have provided qualitatively new insights into neural computation unavailable from single-cell data. In humans, however, recordings remained technically constrained to microwire bundles or Utah arrays — technologies with far lower spatial density than modern silicon probes. The prevailing assumption was that high-density silicon probes were not translatable to humans because of fragility, noise in the operating room environment, brain pulsation, anaesthesia, and regulatory/safety requirements. The commentary's premise is that this assumption is now being overturned.

---

### What this paper contributes

This commentary establishes that the Neuropixels probe can be used in humans and identifies exactly what is new: laminar-resolution recording across the full depth of human cortex, simultaneous observation of neurons within and across cortical columns, and the prospect of recording synaptically connected cell pairs in vivo. It maps the specific technical solutions found by Chung et al. and Paulk et al. (noise mitigation, motion correction, insertion protocol) and situates these advances in the broader context of the field. It also identifies next-priority applications — epilepsy (ictogenesis, cortical dysplasia network dynamics) — and future hardware directions (flexible polyimide substrates enabling chronic implantation with comparable density).

---

### Brain regions & systems

- **Human cortex (general)** — primary recording target; the studies recorded from cortex in tissue slated for resection.
- **Prefrontal cortex (BA9)** — used as an illustrative example in figures (NeuN and SMI32 staining overlaid with probe geometry).
- **Middle temporal gyrus** — cited in figure caption for a reconstructed spiny neuron used to illustrate spike visibility across channels.
- **Epileptogenic focus / cortical dysplasia** — identified as a key future target for investigating ictogenesis using this technology.

---

### Mechanistic insight

This paper does not meet the bar. It is a commentary piece that does not present original data, nor does it formalise an algorithm or link specific computational variables to measured neural activity. It describes recording methodology and contextualises technical achievements. It does not make mechanistic claims about neural computation.

---

### Limitations & open questions

- **Anaesthesia confound**: most recordings were conducted under general anaesthesia, which substantially alters neuronal activity; even in patients awoken during surgery, residual anaesthetic effects persist. The extent to which intraoperative recordings generalise to the awake, behaving state is unknown.
- **Short recording duration**: sessions were limited to ~20 min (tissue about to be resected), precluding behavioural paradigms or longitudinal measurements.
- **Probe fragility**: silicon probe breakage occurred in early subjects; while manageable (fragments removed with forceps), this is a safety concern limiting adoption.
- **Non-implantable base**: the current Neuropixels design has a rigid base in the same plane as the shank, precluding chronic implantation without further hardware innovation.
- **Single-use sterilisation**: probes were discarded after one use, raising questions about cost and scalability for broader clinical research.
- **Open questions**: Can a chronic, high-density silicon implant be developed (e.g. using flexible polyimide substrates)? What are the long-term tissue compatibility properties? Can this technology be extended beyond epilepsy/tumour surgery to other neurosurgical patient populations?

---

### Connections & keywords

**Key citations**:
- Chung et al. (2022) — the primary study being reviewed (Neuron 110, 2409–2421)
- Paulk et al. (2022) — concurrent companion study (Nature Neuroscience 25, 252–263)
- Jun et al. (2017) — original Neuropixels probe development (Nature 551, 232–236)
- Vyas et al. (2020) — population-level neural computation review (Annual Review of Neuroscience)
- Hong and Lieber (2019) — novel electrode technologies review (Nature Reviews Neuroscience)
- Mosher et al. (2020) — heartbeat-related modulation of extracellular action potentials in humans; prior Rutishauser lab human recording work
- Siegle et al. (2021) — large-scale Neuropixels survey of mouse visual system (Nature)
- Feinsinger et al. (2022) — ethical guidelines for intracranial neuroscientific research in humans (Neuron)

**Named models or frameworks**:
- Neuropixels probe (silicon-based high-density extracellular recording array)
- Utah array
- Behnke-Fried microwire electrodes

**Brain regions**:
- Human cortex
- Prefrontal cortex (BA9)
- Middle temporal gyrus
- Cortical dysplasia (epileptogenic focus)

**Keywords**: Neuropixels probe, human intracranial recording, intraoperative electrophysiology, single-unit recording, high-density silicon electrode, spike sorting, cortical laminar recording, local field potential, brain pulsation motion correction, epilepsy surgery, extracellular action potential, neural population recording
