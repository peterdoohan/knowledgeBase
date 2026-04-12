---
source_file: huang2023_hierarchical_replay_working_memory.md
paper_id: huang2023_hierarchical_replay_working_memory
title: "Hierarchical replay of multi-regional sequential spiking associated with working memory"
authors:
  - "Ermeng Huang"
  - "Da Xu"
  - "Huangao Zhu"
  - "Zhaoqin Chen"
  - "Yulei Chen"
  - "Xiaoxing Zhang"
  - "Chengyu T. Li"
year: 2023
journal: "bioRxiv (preprint)"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - neuropixels
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - prelimbic_cortex
frameworks:
  - attractor_networks
keywords:
  - working_memory
  - spike_coupling
  - activity_motifs
  - synfire_chain
  - cell_assembly
  - hierarchical_neural_dynamics
  - neural_replay
  - olfactory_delayed_paired_association
  - neuropixels
  - hippocampal_prefrontal_circuit
  - population_activity_waves
  - nested_loops
  - hierarchical
  - replay
  - multi
  - regional
  - sequential
  - spiking
  - associated
  - working
key_citations:
  - fujisawa2008_assembly_prefrontal_cortex
---

### One-line summary

Brain-wide Neuropixels recordings in mice performing an olfactory working-memory task reveal that millisecond-scale spike-coupling motifs (chains, loops, and nested loops) are hierarchically organised across hippocampal and prefrontal circuits, replayed spontaneously outside the delay period, and modulated on demand to support memory-specific population activity waves.

---

### Background & motivation

Working memory (WM) requires the active maintenance of information over seconds, yet individual neurons fire at the millisecond scale — creating a fundamental gap between the timescale of spiking and the timescale of behavior. Existing theories (cell-assembly, attractor networks, synfire chains, transient population trajectories) each explain part of this picture but have not been tested in a unified, brain-wide framework. Previous work characterised local spike coupling in WM but the global, cross-region dynamic organisation and whether WM-related spiking motifs are replayed beyond the task delay period remained unclear.

---

### Methods

- **Task**: Head-fixed mice performed an olfactory delayed paired-association (ODPA) task with 3- or 6-second delay periods; correct licking required associating sample and test odors.
- **Subjects**: 40 male C57BL/6J mice; 223 dual Neuropixels probe insertions across 116 sessions.
- **Recordings**: Neuropixels probes recorded 33,028 single units across 62 brain regions (Allen Brain Atlas parcellation); 285 ± 13 units simultaneously per session.
- **Memory neuron identification**: Neurons with significantly different delay-period firing to the two sample odors (Wilcoxon rank-sum test, p < 0.05) were classified as memory neurons.
- **Activity waves**: Temporal centre-of-mass (TCOM) used to characterise population-level sequential activity across the delay period; validated by cross-validated held-in/held-out analysis.
- **Spike coupling (SC)**: Asymmetric peaks in spike cross-correlograms identified directional SC between neuron pairs (10 ms latency window, Poisson null model).
- **Motif analysis**: SC used to identify activity chains (3–9 neurons in feed-forward sequence), single loops (3–5 neurons with recurrent closure), and nested loops (chains and loops linked by shared neurons). Graph-theoretic metrics applied.
- **Replay**: Motif occurrence quantified during pre-task, inter-trial interval (ITI), and post-task epochs and compared with delay-period and shuffled baselines.
- **Spike sorting**: Kilosort2; histological track reconstruction from fluorescent probe labels.

---

### Key findings

- 27.8% of recorded neurons (9,182/33,028) were memory-selective; the majority were transient (showing odor selectivity for only part of the delay), with only 0.5–2.9% being sustained.
- Population TCOM sorting revealed brain-wide activity waves that correlated with behavioural performance and propagated from olfactory and hippocampal regions outward.
- Spike coupling (SC) was stronger for congruent memory-neuron pairs encoding the same odor identity and was directionally consistent with the wave timing in memory neurons.
- Activity chains (3,044 consistent, 2,021 inconsistent; Z-score 38.7 vs 33.8 above shuffle) and single loops (occurrence ~22 ms duration, enriched in hippocampal and prefrontal circuits) were significantly over-represented for memory neurons.
- 16.6% of memory neurons participated in activity chains or single loops; chain/loop spikes comprised a median 3.9% of total delay-period spikes.
- >97.7% of chains and single loops were embedded in nested loops (4–82 neurons; 3–217 SC edges; 12.7 ms median consecutive activation).
- Time constants followed a power-law hierarchy: chains < single loops < nested loops (longest 1% durations: 24.4 ms, 47.8 ms, 61.8 ms respectively); extrapolation from recorded subsets suggested that simultaneous recording from thousands of neurons could produce motif sequences spanning the full delay period.
- Activity motifs were replayed during pre-task baseline, ITI, and post-task epochs at ~2/3 of the delay-period rate (all significantly above shuffle).
- Hippocampal neuron-containing motifs replayed at a frequency matching the preferred-delay condition and were suppressed following non-preferred odors; removal of hippocampal neurons most strongly disrupted nested loop integrity.
- Motif occurrence was slightly but significantly reduced in error vs. correct trials during both delay and ITI.

---

### Computational framework

The paper uses a **graph-theoretic / cell-assembly** framework. Neurons are treated as nodes and directional spike couplings as edges. Motif types (chains, loops, nested loops) are graph substructures defined by edge topology and temporal ordering. The key computational idea is that hierarchically nested recurrent and feed-forward spike sequences can bridge the millisecond-to-second temporal gap: short motifs at the bottom, longer (higher time-constant) nested structures at the top, collectively sustaining WM information across the delay.

The framework draws on Hebb's cell-assembly hypothesis and the synfire chain model, and tests their coexistence in a unified hierarchy. Key variables are spike coupling rate, motif occurrence frequency, and temporal centre-of-mass (for relating motifs to the population wave). The framework assumes that SC reflects functional connectivity (possibly synaptic), though it does not directly resolve monosynaptic connections.

---

### Prevailing model of the system under study

The introduction frames the field as divided among four main accounts of how WM is maintained:

1. **Cell-assembly / recurrent loop hypothesis** (Hebb, Harris, Buzsaki): sequential or recurrent spiking in neurons with recurrent connectivity outlasts short inputs.
2. **Point-attractor dynamics** (Hopfield, Wang, Inagaki): sustained firing of individual neurons in a bistable attractor underpins WM.
3. **Synfire chain** (Abeles, Diesmann, Ikegaya): feed-forward pools of neurons propagate synchronised spikes sequentially.
4. **Transient population trajectory / heterogeneous dynamics** (Harvey, Rabinovich): locally unstable but globally stable trajectories encode information transiently rather than through persistent firing.

Prior empirical work had mostly addressed these in isolated regions (especially prefrontal cortex and hippocampus) and in separate studies. Whether WM-related spiking is confined to the demand period or is replayed outside it was an open question, as was whether the four mechanisms coexist in an integrated hierarchy.

---

### What this paper contributes

The paper establishes that the four classes of motifs proposed by competing theories are not mutually exclusive but are instead hierarchically nested within a single organisational framework. Activity chains (synfire-like), single loops (cell-assembly-like), and nested loops (combining both) co-occur across brain regions, with progressively longer time constants at each level. This is the first brain-wide demonstration that WM-related spiking motifs are replayed spontaneously outside the delay period — before, after, and between task trials — not just during the memory maintenance window. It also places hippocampal neurons as critical structural hubs whose removal preferentially disrupts nested loop integrity and whose associated motifs persist at full preferred-delay rate even in spontaneous off-task periods. Together, these findings reframe WM maintenance as a brain-wide, hierarchically structured, and spontaneously active phenomenon rather than a purely on-demand, regionally localised process.

---

### Brain regions & systems

- **Hippocampus (HIP / RHP)** — central hub for motif integrity and replay; removal of hippocampal neurons disproportionately disrupted nested loops; replay of hippocampus-containing motifs matched preferred-delay levels even outside task.
- **Prefrontal cortex — infralimbic (ILA), prelimbic (PL), orbitofrontal (ORB)** — prominent participants in activity chains, single loops, and cross-region spike coupling; key nodes in the hierarchical motif structure.
- **Anterior insular cortex (AI)** — contributed to cross-region single loops; previously established role in olfactory WM maintenance.
- **Piriform cortex (PIR) / Anterior olfactory nucleus (AON) / Taenia tecta (TT)** — olfactory regions with highest proportion of memory neurons; activity waves propagated outward from these areas; AON connectivity predicted regional memory-neuron density.
- **Endopiriform nucleus dorsal (EPd)** — high connectivity (node degree) within nested loops.
- **Retrohippocampal region (RHP)** — wave timing correlated with anatomical projections from this region to downstream areas.
- **Dorsal peduncular area (DP), somatomotor areas (MO)** — involved in cross-region activity motifs.

---

### Mechanistic insight

The paper meets both criteria for a mechanistic insight.

1. It formalises an algorithm: hierarchically nested spike-coupling motifs (chains → single loops → nested loops) as the computational substrate bridging millisecond spiking and second-scale WM maintenance.
2. It provides neural recordings (Neuropixels, 33,028 neurons, 62 regions) that specifically link motif structure, memory selectivity, and behavioral performance.

**Marr's three levels:**

- **Computational**: The brain must maintain a sensory representation across a delay period (seconds) while individual neurons are active only transiently (milliseconds). The problem is temporal integration without requiring persistent firing from every involved neuron.
- **Algorithmic**: The solution is a hierarchy of recurrent spike-coupling structures. At the bottom, directional spike couplings (10 ms) link neurons into chains (feed-forward, ~11 ms duration) and single loops (recurrent, ~22 ms). These are embedded in nested loops (4–82 neurons, ~13 ms per activation episode but with power-law tails extending to ~62 ms for the longest 1%). Memory-selective (congruent) neuron pairs have stronger coupling, motifs are memory-specific, and their directional flow aligns with the brain-wide activity wave. The same motifs are replayed spontaneously outside the task, suggesting they represent learned circuit attractors rather than purely stimulus-driven responses.
- **Implementational**: Hippocampal neurons are disproportionately important for nested-loop integrity (their removal induces loop shrinkage, splitting, and abolition faster than removing equivalent numbers of non-hippocampal neurons or random SCs). Olfactory regions (AON, PIR, EPd) and orbitofrontal / prefrontal cortex are also high-connectivity nodes. The study does not resolve specific cell types, layers, or synaptic mechanisms; it notes that combined whole-cell and extracellular recording will be needed to confirm the monosynaptic basis.

**Bonus**: The paper does not address specific cell types or neuromodulators, which remain open questions flagged in the discussion.

---

### Limitations & open questions

- SC is inferred from spike cross-correlograms on extracellular data; monosynaptic connectivity is not directly confirmed. Future work combining whole-cell and extracellular recording in vivo is needed.
- Only hundreds of neurons were recorded simultaneously from a brain containing ~70 million; the authors extrapolate (linearly) that thousands of simultaneous neurons would yield motifs spanning the full delay, but this has not been demonstrated empirically.
- The plasticity rules governing how activity motifs are shaped during learning remain unknown; the study is a snapshot of well-trained animals.
- The mechanism by which hippocampal neurons specifically scaffold nested loops (cell type, connectivity, projection target) is unresolved.
- Increased non-memory single-loop replay after task execution is unexplained; may reflect anticipatory or post-task behavioural states.
- The paper is a preprint (bioRxiv, October 2023); peer review status at time of summary is not confirmed.
- Recordings were exclusively in male mice; generalisation to female mice or other species is untested.

---

### Connections & keywords

**Key citations**:
- Hebb (1949) — cell assembly hypothesis
- Abeles (1982), Diesmann et al. (1999), Ikegaya et al. (2004) — synfire chain
- Hopfield (1982), Inagaki et al. (2019) — attractor network / persistent activity
- Harvey et al. (2012), Rabinovich et al. (2008) — transient population dynamics
- Fujisawa et al. (2008) — behaviour-dependent assembly dynamics in mPFC
- Zhang et al. (2019), Zhu et al. (2020) — olfactory WM and insular cortex
- Taxidis et al. (2020) — hippocampal sequences in olfactory WM
- Skaggs & McNaughton (1996), Wilson & McNaughton (1994), Foster & Wilson (2006) — hippocampal replay
- Spellman et al. (2015) — hippocampal-prefrontal input in spatial WM
- Jun et al. (2017) — Neuropixels probes

**Named models or frameworks**:
- Olfactory delayed paired-association (ODPA) task
- Synfire chain
- Attractor network / point attractor
- Cell-assembly hypothesis (Hebbian assembly)
- Transient population trajectory
- Temporal centre-of-mass (TCOM) activity wave analysis
- Kilosort2 spike sorting

**Brain regions**:
Hippocampus (HIP), retrohippocampal region (RHP), prefrontal cortex (ILA, PL, ORB), anterior insular cortex (AI), piriform cortex (PIR), anterior olfactory nucleus (AON), taenia tecta (TT), endopiriform nucleus dorsal (EPd), dorsal peduncular area (DP), somatomotor areas (MO)

**Keywords**:
working memory, spike coupling, activity motifs, synfire chain, cell assembly, hierarchical neural dynamics, neural replay, olfactory delayed paired association, Neuropixels, hippocampal-prefrontal circuit, population activity waves, nested loops
