---
source_file: "denbakker2024_mpfc_spatial_swr.md"
paper_id: "denbakker2024_mpfc_spatial_swr"
title: "Neurons in the medial prefrontal cortex are involved in spatial tuning and signaling upcoming choice independently from hippocampal sharp-wave ripples"
authors: "Hanna den Bakker, Fabian Kloosterman"
year: 2024
journal: "bioRxiv (preprint)"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
methods: ["neuropixels", "bayesian_decoding"]
brain_regions: ["hippocampus", "hippocampus_ca1", "prefrontal_cortex", "medial_prefrontal_cortex"]
keywords: ["neurons", "medial", "prefrontal", "cortex", "involved", "spatial", "tuning", "signaling", "upcoming", "choice"]
key_citations: ["shin2019_hippocampal_prefrontal_replay_b", "jadhav2016_hippocampal_prefrontal_swr"]
---

### One-line summary

SWR-unmodulated mPFC neurons — not the SWR-modulated subpopulation commonly studied — are primarily responsible for spatial tuning, directional selectivity, and predictive non-local representations of upcoming choice during spatial rule learning in rats.

---

### Background & motivation

The hippocampus is thought to transfer spatial information to the neocortex during sharp-wave ripple (SWR) events, and a subset of mPFC neurons fires in response to these SWRs. A natural hypothesis is that these SWR-modulated mPFC neurons are the ones that integrate hippocampal spatial information to guide decision making. However, the functional properties of the complementary SWR-unmodulated mPFC population have not been systematically characterised. This paper addresses that gap by comparing the spatial coding and predictive properties of SWR-modulated versus SWR-unmodulated neurons across the dorsal-ventral extent of the mPFC during active rule learning.

---

### Methods

- **Subjects**: 6 male Long Evans rats implanted with Neuropixels 1.0 probes (5 with dual mPFC + hippocampus implants, 1 mPFC only).
- **Task**: Spatial rule switching on a plus-maze; animals learned 4 rules across days (allocentric: go North or go South; cue-based: go to illuminated or non-illuminated arm) via trial and error, with auditory feedback.
- **Recordings**: Chronic high-density Neuropixels recordings spanning the full dorsal-ventral depth of the mPFC; simultaneous hippocampal recordings in 5 animals.
- **Spike sorting**: Kilosort 2 with manual curation in Phy2; quality control via SpikeInterface (ISI violations < 0.1); putative fast-spiking interneurons excluded; 5943 clusters retained.
- **SWR detection**: Ripple-band filtering (160–225 Hz) with contrast frequency signal; threshold = median + 9×MAD.
- **Cell classification**: SWR-excited, SWR-inhibited, or SWR-unmodulated based on z-scored firing rate in 0–200 ms post-SWR window vs. shuffle.
- **Spatial tuning**: Spatial information score (bits/spike) for each neuron; SWR windows excluded.
- **Head direction selectivity**: Directional selectivity index across three direction categories at choice point.
- **Theta cycle skipping**: Spike autocorrelation peaks at 125 ms and 250 ms; index compared to theta-preserving shuffle.
- **Bayesian decoding**: Multi-unit spike features decoded to maze position; cross-validated decoding error < 20 cm required (40 mPFC sessions, 12 hippocampal sessions); separate decoding models built for SWR-modulated and SWR-unmodulated subpopulations.
- **Prediction index**: Non-local decoded representations of upcoming vs. alternative goal arm; time-locking of segments to SWRs and hippocampal theta phase assessed.

---

### Key findings

- **SWR modulation prevalence**: 13.96% of mPFC neurons were SWR-excited, 5.46% SWR-inhibited, and 80.59% SWR-unmodulated; SWR-modulated neurons had higher overall firing rates.
- **Dorsal vs. ventral mPFC**: SWR modulation strength was significantly greater in ventral than dorsal mPFC (mean absolute z-score, dorsal: 0.09 vs. ventral: 0.20, p=.038), consistent with denser hippocampal projections to ventral mPFC. Preferred theta phase differed between subregions: dorsal cells fired near the peak, ventral cells near the trough.
- **SWR-unmodulated neurons are more spatially tuned**: Spatial information scores were highest for SWR-unmodulated cells (0.33 bits/spike) vs. SWR-excited (0.22) and SWR-inhibited (0.11) neurons (p<.001).
- **SWR-unmodulated neurons are more directionally selective**: Maximum absolute directional selectivity index: SWR-unmodulated 0.48 vs. SWR-excited 0.37 vs. SWR-inhibited 0.27 (p<.001).
- **Theta cycle skipping**: More prevalent in SWR-unmodulated (28.94%) than SWR-excited (22.72%) or SWR-inhibited (12.39%) neurons (p<.001).
- **mPFC decodes upcoming choice**: Bayesian decoding of mPFC population activity predicted the animal's future arm choice; the mPFC prediction index preceded the behavioral change by ~6–8 trials after a rule switch.
- **SWR-unmodulated neurons drive predictive decoding**: Non-local representations of upcoming choice decoded from SWR-unmodulated cells were significantly better than chance (p<.001); models built from SWR-modulated cells were not (p=.135).
- **mPFC predictive representations are independent of hippocampal SWRs and theta**: Decoded segments of upcoming/alternative choice in mPFC were not more time-locked to SWRs or biased to a particular theta phase than shuffle.
- **Hippocampal predictive representations are SWR- and theta-locked**: In the hippocampus, upcoming-choice representations were significantly more frequent at SWR onset (p=.004) and phase-locked to the rising phase of theta (Rayleigh's Z=1.05, p=.001); mPFC non-local representations did not overlap in time with hippocampal non-local representations.
- **SWR-modulated mPFC neurons respond to hippocampal non-local events**: SWR-excited mPFC neurons fired more during hippocampal representations of upcoming choice, while SWR-inhibited neurons fired more during hippocampal representations of alternative choice.

---

### Computational framework

Not explicitly computational. The paper uses Bayesian decoding to recover spatial position estimates from multi-unit spike features, enabling characterisation of local and non-local representations. The prediction index is a simple decision variable derived from summed decoded probabilities.

Implicitly, the results constrain frameworks that assign hippocampal-to-cortical transfer (via SWRs) a central role in cortical spatial map formation and prospective decision making. The findings suggest that the relevant mPFC computations — spatial mapping, head direction selectivity, theta cycle skipping, and prospective coding — are not primarily driven by hippocampal SWR input.

---

### Prevailing model of the system under study

The dominant hypothesis in the field is that the hippocampus transfers learned spatial information to the prefrontal cortex during SWR events, and that this transfer is necessary for adaptive spatial learning. Supporting evidence cited includes: (1) spatial maps in neocortex degrade following hippocampal lesions, (2) disrupting mPFC activity in the 200 ms window following SWR onset impairs spatial rule reversal (a finding from the same lab), and (3) mPFC neurons responsive to SWRs are also phase-locked to hippocampal theta, suggesting a shared functional network. The implicit prediction of this model is that SWR-modulated mPFC neurons are the primary site of spatial information integration and prospective coding.

---

### What this paper contributes

The paper challenges the assumption that SWR-modulated mPFC neurons are the primary integrators of hippocampal spatial information for decision making. Instead, it shows that it is the SWR-unmodulated mPFC population that has superior spatial tuning, directional selectivity, theta cycle skipping, and predictive non-local coding. The SWR-modulated population appears to respond to hippocampal replay content (exciting or suppressing in parallel with hippocampal upcoming-vs-alternative coding) but does not itself drive prospective spatial representations in the mPFC. The paper also shows that the timing of mPFC and hippocampal non-local representations is largely non-overlapping, suggesting that the two regions engage in prospective coding through distinct mechanisms. Together, these findings suggest a division of labour: SWR-modulated neurons may signal which hippocampal reactivations are relevant, while SWR-unmodulated neurons maintain and update the spatial map used for behavioral guidance.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)** — primary site of investigation; encodes spatial information, upcoming choice, and directional signals independently of hippocampal SWR events.
  - **Dorsal mPFC** — less strongly SWR-modulated; theta phase-locked neurons fire near peak of oscillation.
  - **Ventral mPFC** — more strongly SWR-modulated (consistent with denser hippocampal connectivity); theta phase-locked neurons fire near trough of oscillation.
- **Hippocampus (dorsal CA1)** — reference region; source of SWR events and theta oscillations; non-local representations in hippocampus are SWR- and theta-locked, in contrast to those in mPFC.

---

### Mechanistic insight

The paper partially meets the bar. It presents empirical data (in vivo Neuropixels recordings in freely moving rats) linking specific neural subpopulations to specific computations (spatial mapping, predictive coding), and it dissociates two populations based on their relationship to a physiological event (SWRs). However, it does not formalise an algorithm for how SWR-unmodulated neurons construct or update the spatial map. It characterises properties of the two populations and their differential engagement in decoding, but does not provide a mechanistic account of how the populations interact or how prediction signals arise. The paper therefore provides strong characterisation data and a functional dissociation, but stops short of proposing or testing a specific algorithm.

Mapping what is established onto Marr's levels:
- **Computational**: The mPFC must compute a prospective spatial representation sufficient to guide rule-based navigation choices on a trial-by-trial basis, and this representation must update ahead of overt behavioral change following rule switches.
- **Algorithmic**: SWR-unmodulated neurons carry spatial information, directional selectivity, and theta cycle skipping, and their population activity can be decoded to predict upcoming choice; the SWR-modulated subpopulation is co-modulated with hippocampal replay content but does not drive prospective mPFC coding.
- **Implementational**: Dissociation between dorsal and ventral mPFC in SWR modulation strength and preferred theta phase is noted, consistent with anatomical connectivity differences. Cell-type identity of SWR-modulated vs. SWR-unmodulated neurons is not established (putative interneurons were excluded, but no further cell-type characterisation was performed).

---

### Limitations & open questions

- The study is correlational; the causal role of SWR-unmodulated neurons in spatial learning was not tested (e.g., via selective optogenetic silencing).
- Whether the SWR-modulated and SWR-unmodulated populations interact sequentially (e.g., hippocampal reactivation modulates SWR-modulated cells, which in turn update SWR-unmodulated cells' spatial map) is speculative and untested.
- Hippocampal decoding quality was limited to 12 sessions from 3 animals, constraining conclusions about hippocampus-mPFC temporal overlap.
- The paper does not characterise the cell types or laminar positions of SWR-modulated vs. SWR-unmodulated neurons.
- Subregion-specific functional dissociations between dorsal and ventral mPFC were observed (theta phase preference, SWR modulation strength) but not causally interrogated.
- The task involved interleaved rest periods between trials; this means the relationship between within-trial encoding and post-trial consolidation cannot be cleanly separated.
- The paper is a preprint (bioRxiv, not peer-reviewed as of July 2025).

---

### Connections & keywords

**Key citations**:
- Benchenane et al. (2010) — mPFC cells modulated by SWRs and phase-locked to theta (ref [12])
- Shin et al. (2019) — non-local mPFC representations predictive of behavior, post-error engagement (ref [29])
- Jadhav et al. (2016) — non-local hippocampal replay modulates mPFC activity (ref [13])
- den Bakker / Kloosterman lab prior work — disrupting mPFC during SWR window slows spatial rule reversal (ref [14])
- Guise & Bhaskaran (2021) — dorsal/ventral mPFC spatial tuning (ref [35])
- Lubenov & Siapas (2009) — theta traveling wave in hippocampus (ref [44])
- Kay et al. (2020) — theta cycle skipping in mPFC predicts upcoming choice (ref [39])

**Named models or frameworks**:
- Bayesian decoding model (multi-unit spike feature decoding)
- Prediction index (non-local decoded probability difference)
- Theta cycle skipping

**Brain regions**:
- Medial prefrontal cortex (mPFC), dorsal mPFC, ventral mPFC
- Hippocampus (CA1)

**Keywords**:
- sharp-wave ripples (SWRs)
- medial prefrontal cortex
- spatial tuning
- non-local representations
- prospective coding
- theta oscillations
- theta cycle skipping
- Bayesian population decoding
- hippocampal-prefrontal interaction
- spatial rule learning
- Neuropixels recordings
- functional dissociation SWR-modulated vs. unmodulated
