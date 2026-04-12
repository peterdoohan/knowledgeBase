---
source_file: jadhav2016_hippocampal_prefrontal_swr.md
paper_id: jadhav2016_hippocampal_prefrontal_swr
title: "Coordinated Excitation and Inhibition of Prefrontal Ensembles during Awake Hippocampal Sharp-Wave Ripple Events"
authors:
  - "Shantanu P. Jadhav"
  - "Gideon Rothschild"
  - "Demetris K. Roumis"
  - "Loren M. Frank"
year: 2016
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - behavioral_analysis
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - ventral_hippocampus
keywords:
  - sharp_wave_ripples_swr
  - hippocampal_prefrontal_coordination
  - memory_reactivation
  - awake_replay
  - theta_phase_locking
  - swr_excited_and_swr_inhibited_prefrontal_ensembles
  - content_specific_inhibition
  - experience_dependent_coordination
  - spatial_memory
  - cross_structure_ensemble_co_activation
  - glm_ensemble_decoding
  - hippocampal_place_cells
  - coordinated
  - excitation
  - inhibition
  - prefrontal
  - ensembles
  - during
  - awake
  - hippocampal
key_citations:
  - singer2013_hippocampal_swr_decisions
  - jones2005_theta_hippocampal_prefrontal
wiki_pages:
  - wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning
---

### One-line summary

During awake hippocampal sharp-wave ripple (SWR) events, distinct prefrontal cortical ensembles are coordinately excited or inhibited in a content-specific manner that mirrors their spatial and temporal co-activity during active exploration.

---

### Background & motivation

The hippocampus and prefrontal cortex (PFC) are both necessary for spatial memory, and functional disconnection of these structures impairs performance, but the specific patterns of activity mediating their interaction during awake behaviour were unknown. Hippocampal SWRs had been causally implicated in awake spatial memory (disrupting them impairs learning), and hippocampal replay during SWRs can represent past and future spatial trajectories — but whether and how this replay engages PFC had not been examined in the awake state. Prior work on sleep SWRs showed mostly excitatory PFC responses, leaving open the question of whether awake SWRs drive a qualitatively similar or different form of hippocampal-prefrontal communication.

---

### Methods

- **Subject population**: 6 male Long Evans rats, 3 per task
- **Tasks**: W-track spatial alternation task (8 days) and Y-track auditory cue-guided spatial task (8–12 days); animals learned over multiple sessions
- **Recordings**: Simultaneous multisite multitetrode recordings in dorsal hippocampal CA1 and medial PFC (prelimbic/infralimbic); 536 CA1 and 312 PFC putative excitatory neurons recorded across all animals
- **SWR detection**: CA1 LFP filtered at 150–250 Hz; SWRs detected during low-speed periods
- **Analysis of SWR modulation**: Custom SWR-modulation metric comparing 0–200 ms post-SWR-onset firing to shuffled baselines; neurons classified as SWR-excited, SWR-inhibited, or unmodulated
- **Theta phase locking**: Circular statistics on phase-aligned PFC firing during movement (>5 cm/s)
- **Pairwise CA1-PFC correlations**: Spike count correlations during SWR windows; theta cross-covariance during movement; spatial correlations from linearised firing rate maps
- **Ensemble-level analysis**: GLM (log link) predicting PFC SWR spiking from CA1 ensemble activity; cross-validated; theta-trained models also applied to SWR data
- **Pre-task rest control**: CA1-PFC correlations during pre-task rest compared to task period to test experience-dependence

---

### Key findings

- 35% of PFC neurons (109/312) were significantly SWR-modulated; unlike in sleep, awake SWRs produced approximately equal numbers of excited (18%, 57/312) and inhibited (17%, 52/312) PFC cells
- CA1 population activity preceded PFC responses: mean peak latencies were 54 ms (CA1), 100 ms (SWR-excited PFC), 84 ms (SWR-inhibited PFC)
- SWR-modulated PFC neurons were more strongly theta phase-locked during movement than unmodulated neurons (77% of excited and 71% of inhibited cells significantly phase-locked vs. 53% of unmodulated, p < 0.01)
- SWR-excited and SWR-inhibited PFC cells form functionally distinct ensembles: excited cells have more diffuse spatial firing and higher firing rates at higher movement speeds; inhibited cells have more spatially concentrated firing and preferentially fire at low speeds / around reward
- 16% of CA1-PFC pairs were significantly SWR-correlated (vs. ~5% by chance, p < 10^-8), with both positive and negative correlations
- SWR correlation between CA1-PFC pairs was significantly predicted by their theta-period cross-covariance (r = 0.39, p < 10^-4 for both excited and inhibited populations) and by spatial overlap of their firing fields
- GLM ensemble models confirmed content-specific CA1-PFC interactions: the same CA1 neuron could positively predict one PFC neuron and negatively predict another; prediction accuracy increased with CA1 ensemble size
- Theta-trained GLMs could significantly predict SWR-period PFC spiking, indicating that SWR reactivation recapitulates theta-period co-activity structure
- CA1-PFC SWR correlations were absent during pre-task rest and were not predicted by rest-period activity, establishing that structured coordination is experience-dependent

---

### Computational framework

The paper is primarily empirical; it does not formalise an explicit computational model. However, it interprets the data through the lens of **memory reactivation and representational replay**. The implicit framework is that:

- During active exploration (theta state), co-active hippocampal-prefrontal cell pairs form functional ensembles encoding spatial and task information
- During awake SWRs, these ensembles are reactivated: pairs that were co-active during theta are preferentially co-active during SWRs (positive correlations), while pairs that did not co-activate during theta are anti-correlated
- Structured inhibition during SWRs is proposed to suppress PFC representations inconsistent with the replayed hippocampal content, effectively "gating" ongoing activity to allow replay-consistent content to dominate

A GLM with a log link function is the primary quantitative tool for testing these ensemble-level interactions, but it is used as a descriptive/inference tool rather than a formal model of the computation.

---

### Prevailing model of the system under study

Before this paper, the field understood hippocampal SWRs as a key mechanism for memory consolidation and retrieval, primarily through their role in reactivating hippocampal place cell sequences. Hippocampal-PFC interactions were known to occur during theta oscillations (PFC neurons phase-lock to hippocampal theta during movement), and sleep SWRs had been associated with PFC reactivation. However, the prevailing view was that (1) SWR-related modulation of PFC was predominantly excitatory (based on sleep studies), and (2) awake SWRs had not been examined in the context of hippocampal-PFC coordination. The dominant model was one in which hippocampal replay during SWRs drives downstream cortical targets via excitation, potentially supporting consolidation and retrieval. The possibility that SWRs also drive structured inhibition of PFC — and that this inhibition is content-specific — had not been proposed.

---

### What this paper contributes

The paper establishes that awake SWRs coordinate hippocampal-prefrontal activity in a content-specific and experience-dependent manner that is qualitatively richer than previously appreciated. Specifically:

1. Awake SWRs drive both excitation and inhibition of distinct PFC subpopulations — unlike sleep SWRs which predominantly excite PFC. This is a novel empirical finding that changes the picture of how SWRs engage downstream areas.
2. The co-activation patterns during awake SWRs mirror the co-activity structure from the theta state (movement period), demonstrating that SWRs reactivate experience-specific hippocampal-prefrontal representations, not just hippocampal ones.
3. Structured inhibition is content-specific: SWR-inhibited PFC cells are most suppressed when the hippocampal replay content is spatially inconsistent with that cell's preferred representation. This supports a mechanism by which SWRs can selectively suppress competing PFC representations during memory retrieval or deliberation.
4. Task-specific coordination is not detectable before each day's experience, confirming that the structured CA1-PFC correlations are built up through behavioural experience rather than reflecting fixed connectivity.

---

### Brain regions & systems

- **Hippocampal CA1** — primary source of SWR-related activity; place cell sequences during theta; replay during SWRs; activity leads PFC during both states
- **Medial prefrontal cortex (prelimbic and infralimbic)** — site of SWR-modulated excitation and inhibition; encodes task events and spatial trajectories; proposed locus of content-gating during hippocampal replay
- **Hippocampal-prefrontal circuit** — the functional ensemble whose coordination during both theta and SWR states is the central subject of study; indirectly connected (predominantly via intermediate/ventral hippocampus, not direct dorsal CA1-PFC projections)

---

### Mechanistic insight

This paper meets the bar for mechanistic insight. It both formalises a candidate algorithm (content-specific gating of PFC representations by hippocampal SWR-driven excitation and inhibition) and provides neural data (simultaneous hippocampal-PFC recordings with GLM analysis) that support this algorithm over simpler alternatives (e.g., uniform SWR-driven excitation).

- **Computational**: The brain solves the problem of selectively reactivating experience-relevant representations in PFC during awake memory retrieval/deliberation, while suppressing competing representations that are inconsistent with the current hippocampal replay content.
- **Algorithmic**: During an SWR, the hippocampus reactivates a sequence representing a past or imagined trajectory. PFC cells whose spatial/task representations overlap with the replayed content are excited; those with non-overlapping representations are inhibited. The pattern of excitation/inhibition mirrors the theta-state co-activity structure, implying that the hippocampal-prefrontal connectivity forged during exploration is the template for SWR-driven reactivation. GLM analyses confirm that CA1 ensemble activity during SWRs can predict, and is predicted by, PFC activity in content-specific ways.
- **Implementational**: The paper does not identify specific cell types or synaptic mechanisms mediating the inhibition. The authors note that the predominantly dorsal CA1 recordings used have only minor direct projections to PFC; coordinated reactivation likely depends on indirect pathways through intermediate/ventral hippocampus. No pharmacological or optogenetic manipulation of specific interneuron populations was performed. The implementational level thus remains largely open.

**Bonus**: The paper notes a parallel finding in VTA (Gomperts et al., 2015) where both excitation and inhibition are seen during SWRs, suggesting a general principle of structured dual-polarity responses beyond the hippocampal-PFC circuit.

---

### Limitations & open questions

- Recordings were predominantly in dorsal CA1, which has minimal direct projections to PFC; the actual circuit mediating coordination (likely via ventral/intermediate hippocampus) was not directly sampled
- The precise interneuron populations mediating PFC inhibition during SWRs were not identified; the mechanism of inhibition (feedforward from hippocampus vs. local PFC recurrent inhibition) is unknown
- The paper cannot establish causal directionality from its correlational data; while CA1 tended to lead PFC, reversal (PFC predicting CA1 SWR activity) also yielded above-chance performance
- GLM ensemble analyses were limited by small CA1 ensemble sizes; prediction improved with ensemble size, suggesting the full picture may not have been captured
- The analysis of replay content and PFC spiking was limited to a small number of datasets with sufficient simultaneously recorded CA1 ensembles and SWR-modulated PFC cells
- It remains unclear whether the observed patterns generalise to other PFC subregions or to different types of memory tasks beyond spatial navigation
- The relationship between awake SWR coordination and downstream effects (e.g., on striatum or sensory cortex) was not examined

---

### Connections & keywords

**Key citations**:
- Jadhav et al. (2012) Science — causal role of awake SWRs in spatial memory
- Carr, Jadhav & Frank (2011) Nat Neurosci — hippocampal replay in awake state
- Peyrache et al. (2009) Nat Neurosci — PFC replay during sleep SWRs
- Siapas & Wilson (1998) Neuron — hippocampal-cortical interactions during sleep SWRs
- Siapas, Lubenov & Wilson (2005) Neuron — prefrontal phase locking to hippocampal theta
- Jones & Wilson (2005) PLoS Biol — theta coordination of hippocampal-PFC interactions
- Foster & Wilson (2006) Nature — reverse replay in awake state
- Karlsson & Frank (2009) Nat Neurosci — awake replay of remote experiences
- Gomperts, Kloosterman & Wilson (2015) eLife — VTA neurons and hippocampal SWRs
- Singer et al. (2013) Neuron — SWR activity predicts correct decisions

**Named models or frameworks**:
- Sharp-wave ripple (SWR) replay framework
- Generalised linear model (GLM, log link) for ensemble prediction
- Two-stage memory model (Buzsaki 1989) — implicit background

**Brain regions**:
- Hippocampal CA1
- Medial prefrontal cortex (prelimbic, infralimbic)

**Keywords**:
- sharp-wave ripples (SWR)
- hippocampal-prefrontal coordination
- memory reactivation
- awake replay
- theta phase locking
- SWR-excited and SWR-inhibited prefrontal ensembles
- content-specific inhibition
- experience-dependent coordination
- spatial memory
- cross-structure ensemble co-activation
- GLM ensemble decoding
- hippocampal place cells

### Related wiki pages
- [[wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning|Hippocampal sharp-wave ripple replay and prefrontal coordination during planning]]
