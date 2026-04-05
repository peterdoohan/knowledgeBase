---
source_file: hyun2022_cal_light_active_neurons.md
title: "Tagging active neurons by soma-targeted Cal-Light"
authors: Jung Ho Hyun, Kenichiro Nagahama, Ho Namkung, Neymi Mignocchi, Seung-Eon Roh, Patrick Hannan, Sarah Krüssel, Chuljung Kwak, Abigail McElroy, Bian Liu, Mingguang Cui, Seunghwan Lee, Dongmin Lee, Richard L. Huganir, Paul F. Worley, Akira Sawa, Hyung-Bae Kwon
year: 2022
journal: Nature Communications
paper_type: empirical
contribution_type: methodological
---

### One-line summary

Restricting the Cal-Light dual-switch labeling system to the neuronal soma — by adding KA2 or Kv2.1 soma-targeting peptides — substantially improves the signal-to-noise ratio and temporal precision of activity-dependent gene expression, enabling causal dissection of neurons engaged in a wide range of short-lived and disease-related behaviors.

---

### Background & motivation

Identifying which specific neurons drive a given behavior requires tools that can both tag active cells with high temporal precision and subsequently manipulate them. Immediate early gene (IEG)-based systems (e.g., TRAP, c-Fos) have poor temporal resolution (hours) and weak coupling to firing. The original Cal-Light technique — an "AND gate" requiring both calcium (activity) and light — improved temporal precision, but remained susceptible to background calcium from dendritic spikes, synaptic inputs, and internal stores that are unrelated to somatic action potentials. This accumulated non-specific signal lowered labeling selectivity, particularly during long in vivo viral expression windows, and required many light exposures, limiting applicability to brief, transient behaviors.

---

### Methods

- **Tool development (in vitro):** Two soma-targeting peptide motifs — a 150-aa N-terminal fragment of kainate receptor 2 (KA2) and a 65-aa C-terminal fragment of Kv2.1 — were inserted into the Cal-Light construct to restrict plasma membrane expression to the cell body. Expression and signal-to-noise ratio (SNR) were tested in dissociated hippocampal cultures and organotypic cortical slice cultures under pharmacological activity control (TTX, bicuculline) with and without 473 nm blue light.
- **In vivo behavioral applications (mice, C57BL/6J):** ST-KA2 (the best-performing variant) was validated across four behavioral paradigms:
  - Lever-pressing (primary motor cortex, M1; full and mild labeling protocols)
  - Contextual fear conditioning (dorsal hippocampus CA1; three context–shock pairings, 5 s × 3 blue light pulses)
  - Social interaction (medial prefrontal cortex mPFC, layer 5/6)
  - Kainic acid-induced seizure (hippocampal CA1 and dentate gyrus; EEG recording)
- **Optogenetic manipulation:** Labeled neurons expressed halorhodopsin (NpHR; 589 nm inhibition) or ChrimsonR (589 nm activation) to test behavioral causality.
- **Knock-in mouse:** Conditional ST-Cal-Light KI mouse generated at the ROSA26 locus (floxed stop cassette); validated by crossing with Emx1-Cre (excitatory neurons) and PV-Cre (parvalbumin interneurons).
- **Analysis:** Green-to-red fluorescence ratio (G/R) as the primary labeling metric; seizure scored by modified Racine scale; behavior tracked with DeepLabCut and ezTrack.

---

### Key findings

- ST-KA2 achieved 1.8-fold higher SNR than original Cal-Light (OG-Cal) in dissociated cultures (p < 0.005) and approximately 2-fold higher in organotypic slices (p < 0.005), with near-zero background in the absence of light.
- ST-Kv2.1 showed a small amount of light-independent (activity-only) expression, making ST-KA2 the preferred variant.
- In the lever-pressing task, both full (~550 s total light) and mild (~350 s) labeling protocols produced sufficient NpHR expression; 589 nm inhibition significantly reduced lever presses, inter-reward intervals were prolonged, and lick–press matching was impaired; behavior fully recovered the following day.
- In contextual fear conditioning, just three context–shock pairings (15 s total blue light) were sufficient to label hippocampal neurons whose inhibition significantly reduced freezing; reactivation with ChrimsonR triggered freezing in a novel context.
- In the social interaction paradigm, mPFC EGFP expression correlated positively with total blue light exposure (number of social interactions); inhibition of labeled neurons significantly reduced social preference index.
- In the kainic acid seizure model, labeling seizure-active hippocampal neurons (DG, CA1, CA3, mossy cells) followed by NpHR inhibition significantly suppressed seizure score progression and ictal-like EEG discharges on a second KA injection; randomly labeled hippocampal neurons (from lever-pressing context) did not reduce seizure, arguing for seizure-specific cell populations.
- Conditional KI mouse validated: reporter expression required Cre; crossing with Emx1-Cre restricted labeling to CaMKII+ excitatory neurons (86% specificity); crossing with PV-Cre restricted labeling to PV+ interneurons (82% specificity); approximately half of each cell-type population was labeled.

---

### Computational framework

Not applicable in the strict sense — the paper does not deploy a mathematical or computational model of neural computation. The ST-Cal-Light system instantiates a biological "AND gate" logic: gene expression requires simultaneous calcium elevation (somatic action potentials) AND blue light (photon-gated AsLOV2 conformational change exposing a TEV cleavage site). The framework is more accurately described as synthetic biology / molecular engineering rather than computational modelling. The results constrain how temporally specific activity-to-gene-expression coupling can be achieved, which is relevant to any framework (e.g., engram theory, attractor dynamics) that requires empirical identification and manipulation of specific neural ensembles.

---

### Prevailing model of the system under study

The paper targets the general problem of linking neural activity to behavior at single-cell resolution. The prevailing approach as framed by the introduction was IEG-based tagging (TRAP, E-SARE, CANE), which marks active cells on the timescale of hours and with weak coupling to firing frequency. The more recent dual Ca2+/light switch systems (original Cal-Light, FLARE, Cal2) improved temporal precision to minutes but, as the authors emphasise, still accumulated false-positive signal from dendritic calcium sources (synaptic inputs, dendritic spikes, internal Ca2+ stores) that are not tied to somatic output. The implicit working model was therefore that whole-cell calcium is an adequate proxy for neuronal output — a model this paper challenges by showing that sub-compartment specificity (soma vs. dendrites) meaningfully improves selectivity.

---

### What this paper contributes

ST-Cal-Light establishes that restricting the calcium sensor to the soma — so that only action potential-driven somatic calcium transients trigger gene expression — reduces background labeling and increases induction efficiency sufficiently to label neurons engaged in brief, single-trial behaviors (three footshocks, a few minutes of social interaction). This enables causal tests that were previously unfeasible with earlier temporal-resolution tools. Concretely: (1) the paper demonstrates that specific hippocampal subpopulations (not generic hippocampal activity) mediate seizure pathology at the individual cell level; (2) it shows that mPFC neurons active during social interaction are causally required for social preference; (3) the conditional KI mouse provides a platform for cell-type-specific activity labeling without relying on variable viral co-infection ratios. Together, these advances shift the methodological bar for engram studies from requiring many behavioral repetitions to capturing functionally engaged cells from as little as a single brief experience.

---

### Brain regions & systems

- **Primary motor cortex (M1), layer 2/3** — target for labeling lever-pressing-engaged neurons; inhibition of labeled population impairs learned motor behavior.
- **Dorsal hippocampus, CA1** — target for contextual fear memory labeling; inhibition reduces freezing, reactivation triggers fear expression in novel context; also labeled in seizure experiments.
- **Dorsal hippocampus, dentate gyrus (DG) granule cells and mossy cells** — labeled during kainic acid seizure; their inhibition suppresses seizure progression.
- **Hippocampus CA3** — labeled during seizure paradigm; implicated in seizure circuitry.
- **Medial prefrontal cortex (mPFC), layer 5/6** — target for social interaction labeling; inhibition reduces social preference index, implicating mPFC in causal control of social cognition at single-cell resolution.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight at a methodological level but only partially at the circuit-function level.

**What the paper directly addresses:** The mechanistic contribution is primarily implementational — it demonstrates that somatic restriction of a calcium sensor (via KA2 or Kv2.1 targeting peptides) selectively couples somatic action potential calcium to gene expression, reducing dendritic-origin false positives. The mechanistic logic is:

- **Computational**: What problem is the brain solving? (Not addressed by the paper — the paper addresses the problem faced by the experimenter: how to identify which neurons are causally involved in behavior.)
- **Algorithmic**: The "AND gate" algorithm is: gene expression = f(somatic Ca2+) AND f(blue light). Soma-targeting ensures that Ca2+ input comes preferentially from voltage-gated channels activated by axon-hillock-initiated action potentials, not from dendritically confined synaptic events.
- **Implementational**: The physical implementation uses two interacting proteins (CaM–TEV-N and M13–TEV-C) whose interaction is Ca2+-dependent; the TEVseq is buried in AsLOV2 Jα-helix until light-induced unfolding; somatic membrane anchoring is achieved via the KA2 transmembrane motif. This constitutes full implementational description of the molecular tool.

For the behavioral phenomena themselves (fear memory, social cognition, seizure), the paper provides correlation between labeled cells and behavior (loss-of-function and gain-of-function), but does not resolve the algorithmic level for these functions — it does not identify what computations the tagged populations perform, only that they are causally necessary. This is an appropriate limitation given the paper's primary methodological goal.

---

### Limitations & open questions

- ST-Cal-Light requires three separate AAV constructs (or two with the KI mouse plus one AAV); co-infection variability across cells is partially mitigated by the KI line but not fully eliminated.
- Occasional neurons show very high EGFP ("outlier" EGFP signal despite low red marker), attributed tentatively to uncontrolled tTA transcription or protein aggregation — mechanism unresolved.
- Labeling efficiency is sensitive to the ratio of the two Cal-Light construct components; a 1:1 ratio is optimal but difficult to ensure in vivo.
- A single footshock did not produce sufficient labeling for behavioral causality demonstration, setting a practical lower bound on labeling protocol intensity.
- Seizure suppression after NpHR activation may partly reflect indirect circuit effects (not purely direct inhibition of the labeled cells), as the authors acknowledge.
- The KI mouse line requires 6–8 months for distribution, limiting immediate accessibility.
- Optimal labeling parameters (light pulse duration, inter-pulse interval, firing rate) vary by cell type and cannot be universally prescribed.
- The paper does not address long-term stability of labeled engrams or whether repeated re-labeling of the same behavioral epoch is possible.

---

### Connections & keywords

**Key citations:**
- Lee et al. 2017, *Nat. Biotechnol.* (original Cal-Light system, ref 8)
- Kim et al. 2020, *Cell* (FLARE calcium/light switch, ref 7)
- Wang et al. 2017, *Nat. Biotechnol.* (Cal2 system, ref 10)
- Sanchez et al. 2020, *PNAS* (engineered Ca2+-activated protease, ref 9)
- Shemesh et al. 2017, *Nat. Neurosci.* (soma-targeted channelrhodopsin, source of KA2/Kv2.1 targeting motifs, ref 16)
- Guenthner et al. 2013, *Neuron* (TRAP IEG system, ref 1)
- Liu et al. 2012, *Nature* (optogenetic engram activation, ref 3)
- Park et al. 2021, *Nature* (Cal-Light application to hippocampal-prefrontal circuitry, ref 11)
- Bui et al. 2018, *Science* (dentate gyrus mossy cells in seizure, ref 24)

**Named models or frameworks:**
- Cal-Light (original, OG-Cal)
- Soma-targeted Cal-Light (ST-Cal-Light; ST-KA2; ST-Kv2.1)
- FLARE
- TRAP (targeted recombination in active populations)
- Racine seizure scoring scale
- AND gate logic (dual Ca2+/light switch)

**Brain regions:**
- Primary motor cortex (M1)
- Dorsal hippocampus (CA1, CA3, dentate gyrus)
- Hippocampal mossy cells (hilus)
- Medial prefrontal cortex (mPFC)

**Keywords:**
- soma-targeted calcium sensor
- activity-dependent gene expression
- engram tagging
- optogenetics
- calcium-light AND gate
- Cal-Light
- TEV protease reconstitution
- AsLOV2 photosensor
- halorhodopsin (NpHR)
- kainic acid seizure model
- conditional knock-in mouse
- neural circuit causality
