---
source_file: carlson2018_hybrid_electrodes_seizure.md
paper_id: carlson2018_hybrid_electrodes_seizure
title: "Safety and Utility of Hybrid Depth Electrodes for Seizure Localization and Single-Unit Neuronal Recording"
authors:
  - "April A. Carlson"
  - "Ueli Rutishauser"
  - "Adam N. Mamelak"
year: 2018
journal: "Stereotactic and Functional Neurosurgery"
paper_type: empirical
contribution_type: empirical
species:
  - human
methods:
  - electrophysiology
brain_regions:
  - hippocampus
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - amygdala
keywords:
  - hybrid_depth_electrodes
  - behnke_fried_electrode
  - stereoeeg
  - intracranial_epilepsy_monitoring
  - medically_refractory_epilepsy
  - single_unit_recording
  - seizure_localization
  - microwire_array
  - hemorrhage_risk
  - electrode_complication_rate
  - epileptogenic_zone
  - mesial_temporal_lobe
  - safety
  - utility
  - hybrid
  - depth
  - electrodes
  - seizure
  - localization
  - single
---

### One-line summary

A 10-year retrospective case series of 52 patients and 555 depth electrodes demonstrates that hybrid macro-micro depth electrodes (Behnke-Fried) are as safe and effective as standard depth electrodes for intracranial seizure monitoring in medically refractory epilepsy.

---

### Background & motivation

Patients with medically refractory epilepsy often require invasive intracranial monitoring to precisely localize epileptogenic foci that cannot be identified with scalp EEG or other noninvasive methods. Hybrid depth electrodes — standard clinical macroelectrodes augmented with microwire bundles — allow simultaneous single-neuron recording, opening a window onto human cognition at cellular resolution. Despite growing use of hybrid electrodes for both clinical and research purposes, safety and complication data relative to standard non-hybrid electrodes remained sparse, with only one prior study (Hefft et al., n=25) addressing the question. This paper fills that gap with a substantially larger single-center series spanning 11 years.

---

### Methods

- **Design**: Single-center retrospective chart review, 2006–2017, single surgeon (A.N.M.)
- **Subjects**: 52 patients, 53 procedures; mean age 37 ± 14.1 years; mean epilepsy duration 18 ± 15.2 years
- **Electrodes**: 555 total — 244 (44%) standard non-hybrid Spencer depth electrodes (1.1 mm), 288 (52%) hybrid Behnke-Fried electrodes with internal microwires (1.3 mm), 23 (4%) non-hybrid SEEG electrodes (0.8 mm); average 10 electrodes per patient
- **Targets**: Bilateral mesial temporal (amygdala, hippocampus) and frontal (orbitofrontal cortex, pre-SMA, anterior cingulate cortex) structures; no electrodes placed solely for research
- **Outcome measures**: Seizure localization outcome (localized / partially localized / not localized); complication rates per electrode and per case; attribution of complications to electrode type
- **Statistical analysis**: Fisher exact test for group comparisons (hybrid vs. non-hybrid cases)
- **Single-unit yield**: Descriptively reported across the monitoring period

---

### Key findings

- Overall per-electrode complication rate: 2.3%; per-case rate: 20.8% — consistent with published literature (1–26% per case)
- Serious or hemorrhagic complications requiring surgical intervention occurred in 2 patients (0.4% per electrode); no infections, no deaths
- The most common complication was hardware breakage (anchor bolt or electrode fracture, 1.3% per electrode); excluding hardware issues, per-case rate dropped to 11.3% and per-electrode rate to 1.1%
- Per-electrode complication rates did not differ significantly between hybrid cases (1.7%) and standard electrode cases (0.7%) (p not significant)
- No complication could be directly or indirectly attributed to the microwires; clinically significant bleeds did not occur near microwire tips
- Seizure localization success: 61.5% fully localized, 19.2% partially localized, 19.2% not localized; no significant difference between hybrid and non-hybrid groups (p = 1.0, Fisher exact; p = 0.15, 2×3 table)
- Single-unit recording yield improved over the study period: 37% of microwire bundles in early cases vs. 70–80% in later cases; 3–7 isolated units per bundle on average; units recordable for over 2 weeks; amygdala yielded the most reliable recordings

---

### Computational framework

Not applicable. This is a clinical safety and utility study with no explicit computational framework. The results are relevant to neuroscientific research programmes that use hybrid electrodes for human single-neuron studies — including frameworks involving spike-train analysis, theta-phase locking, and correlates of memory and cognition — but the paper itself does not employ or evaluate any computational model.

---

### Prevailing model of the system under study

The introduction situates the work within standard clinical neurosurgical practice for medically refractory epilepsy: stereoEEG (SEEG) with depth electrodes is an established method for localising seizure onset zones in mesial and deep structures inaccessible to scalp EEG or subdural grids. The field already accepted that hybrid macro-micro electrodes are scientifically valuable for studying human cognition at single-neuron resolution (Fried et al., 2014), and prior work had established that standard depth electrodes carry lower complication rates than subdural grids. However, the safety equivalence of hybrid electrodes relative to standard electrodes had not been demonstrated at scale, leaving a practical uncertainty about whether the microwire modification meaningfully increases risk.

---

### What this paper contributes

The paper provides the largest single-center evidence base to date (555 electrodes, 52 patients) confirming that hybrid Behnke-Fried depth electrodes produce complication rates statistically indistinguishable from standard depth electrodes, and localise seizure onset zones with equivalent accuracy. Critically, no complication was directly attributable to the microwire component. This resolves the primary clinical uncertainty about hybrid electrode adoption: the modest increase in electrode diameter (1.1 mm standard vs. 1.3 mm hybrid) does not translate to elevated hemorrhage risk. The paper also characterises single-unit recording yield quantitatively across a long clinical series, documenting that unit quality and stability are sufficient for multi-week cognitive experiments.

---

### Brain regions & systems

- **Amygdala** — primary target for hybrid electrode placement; highest single-unit recording yield
- **Hippocampus** — primary target; bilateral mesial temporal monitoring for memory-related seizure onset
- **Anterior cingulate cortex** — frequent target; relevant to both seizure networks and cognitive single-unit research
- **Pre-supplementary motor area (pre-SMA)** — targeted in frontal epilepsy cases; used for single-unit studies of motor preparation and decision making
- **Orbitofrontal cortex** — targeted for frontal lobe epilepsy monitoring
- **Insula and parieto-occipital regions** — targeted in later SEEG cases for nonstandard seizure presentations

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined. It is a clinical safety study: it presents no algorithm or formal computational process, and provides no neural data designed to arbitrate between mechanistic accounts. The complication and localization data characterise the tool rather than the neural system. Single-unit yield statistics are reported descriptively without linking them to any specific computational or neural mechanism.

---

### Limitations & open questions

- Retrospective single-surgeon, single-center design limits generalisability; surgeon experience and technique may not transfer to other centres
- The study is underpowered to detect small but real differences in complication rates between electrode types; a larger multicenter database is explicitly called for
- Only 4% of electrodes were SEEG type, precluding meaningful comparison of SEEG vs. hybrid safety profiles
- Hardware breakage was the most common complication, likely reflecting a correctable technique issue (over-tightening of anchor bolts); this inflates reported complication rates relative to other series
- The threshold for classifying seizures as "localized" was clinician-defined and not standardised across centres
- Long-term post-resection seizure outcomes are not reported; localisation success is a proxy, not a direct measure of clinical benefit
- Single-unit yield variability is described but not systematically analysed as a function of brain region, electrode age, or patient factors

---

### Connections & keywords

**Key citations**:
- Fried, Rutishauser, Cerf, Kreiman (2014) — *Single Neuron Studies of the Human Brain* (MIT Press); foundational text for hybrid electrode neuroscience
- Hefft et al. [19] — prior small safety study (n=25) of hybrid depth electrodes
- Mullin et al. (2016, Epilepsia) — systematic review and meta-analysis of SEEG complications
- Schmidt et al. (2016, Epilepsia) — large retrospective complications series (317 procedures)
- Rutishauser et al. (2010, Nature) — theta-phase locking of single neurons and human memory
- Kamiński et al. (2017, Nature Neuroscience) — persistently active neurons supporting working memory

**Named models or frameworks**:
- StereoEEG (SEEG) — depth electrode-based intracranial monitoring paradigm
- Behnke-Fried hybrid electrode — macro-micro depth electrode design (Ad-Tech Medical)
- Spencer depth electrode — standard non-hybrid comparator

**Brain regions**:
- Amygdala, hippocampus, anterior cingulate cortex, pre-supplementary motor area, orbitofrontal cortex, insula, parieto-occipital cortex

**Keywords**:
- hybrid depth electrodes, Behnke-Fried electrode, stereoEEG, intracranial epilepsy monitoring, medically refractory epilepsy, single-unit recording, seizure localization, microwire array, hemorrhage risk, electrode complication rate, epileptogenic zone, mesial temporal lobe
