---
source_file: kunz2019_hippocampal_theta_goal_directed.md
title: "Hippocampal theta phases organize the reactivation of large-scale electrophysiological representations during goal-directed navigation"
authors: Lukas Kunz, Liang Wang, Daniel Lachner-Piza, Hui Zhang, Armin Brandt, Matthias Dümpelmann, Peter C. Reinacher, Volker A. Coenen, Dong Chen, Wen-Xu Wang, Wenjing Zhou, Shuli Liang, Philip Grewe, Christian G. Bien, Anne Bierbrauer, Tobias Navarro Schröder, Andreas Schulze-Bonhage, Nikolai Axmacher
year: 2019
journal: Science Advances
paper_type: empirical
contribution_type: empirical
---

### One-line summary

During goal-directed navigation in humans, large-scale electrophysiological representations of distinct goal cues are dynamically reactivated at cue-specific hippocampal theta phases, and more distinct phase assignment across goals predicts better spatial memory performance.

---

### Background & motivation

Purposefully navigating to a remembered goal location requires maintaining goal-specific representations throughout the navigation period and protecting them from interference by competing goals — a cognitive demand that resembles multi-item working memory. Working memory research suggests that multiple mental contents are kept separate by theta-coupled reactivation at distinct oscillatory phases, but whether an analogous mechanism operates during the complex, real-time behaviour of goal-directed navigation was unknown in humans. The neural basis of goal-directed navigation — particularly the role of hippocampal theta oscillations in organising competing goal representations — remained incompletely understood, especially given that most mechanistic evidence came from rodent studies.

---

### Methods

- **Subjects**: N = 22 presurgical epilepsy patients implanted with intracranial EEG (iEEG) electrodes (2330 usable channels); subset of n = 16 had hippocampal depth electrodes.
- **Task**: Associative object-location memory task in a virtual circular environment; patients first learned object-location associations, then completed 40–160 retrieval trials (cue image → navigate to remembered location → response → feedback → re-encoding).
- **Neural representations**: Time-resolved spatial representational similarity analysis (tr-sRSA) applied to ICA-decomposed, low-pass-filtered (30 Hz) broad-band iEEG time series to identify a temporal region of interest (tROI: 256–530 ms post cue onset) in which identical-cue patterns were more similar than different-cue patterns.
- **Theta detection**: MODAL algorithm applied to hippocampal (and prefrontal) iEEG to detect narrow-band theta bursts and their instantaneous frequency; prevailing hippocampal theta at 3–4 Hz.
- **Representation-to-theta-phase-clustering**: Prototypal cue representations (from tROI) were slid across retrieval-period iEEG patterns (sliding RSA); the preferred theta phase for each trial and cue was extracted via the Moore-Rayleigh test. Within-stability (consistency of preferred phase across trials per cue) and between-similarity (similarity of preferred phases across different cues) were computed and related to memory performance (drop error).
- **Prefrontal extension**: Same analysis applied to prefrontal theta (peak 5–6 Hz) in n = 13 patients; hippocampal–prefrontal phase coupling (PLV) also assessed.
- **Controls**: Surrogate distributions via circular shifting; subset analysis excluding patients with higher epileptic activity; entorhinal cortex as anatomical control region.

---

### Key findings

- tr-sRSA identified a significant tROI (256–530 ms post cue onset, cluster-based permutation test: t_cluster = 799.66, P = 0.019) during which iEEG patterns contained cue-specific information.
- Neural cue representations showed an inverse higher-order similarity relationship with subjective goal-location proximity (t_21 = −2.09, P = 0.049): cues associated with spatially closer (subjectively) goal locations had more distinct neural representations, especially in the second half of the data, consistent with learning-induced representational repulsion.
- Lateral orbitofrontal cortex and rostral middle frontal gyrus were the only regions with above-chance positive contribution to cue representations (both P_corr < 0.05 after Bonferroni correction), though representations were distributed large-scale and neither region alone was necessary or sufficient.
- During goal-directed navigation, cue representations reactivated preferentially at specific hippocampal theta phases (representation-to-theta-phase-clustering: P = 0.004).
- Preferred theta phases of each cue representation were stable across trials (within-stability: P = 0.003) and differed between cue representations (between-similarity: P = 0.012).
- More distinct preferred theta phases for different cues (lower between-similarity) correlated with better spatial memory (lower drop error): Spearman rho(16) = 0.52, P = 0.042; robust to controlling for trial number and movement speed.
- Representation-to-theta-phase-clustering was absent during non-theta periods (P = 0.414) and at entorhinal cortex 3–4 Hz (P = 0.123), confirming hippocampal specificity.
- Parallel findings in prefrontal cortex at 5–6 Hz: significant clustering (P = 0.003), within-stability (P = 0.006), between-similarity (P = 0.031), and correlation with memory performance (rho(13) = 0.63, P = 0.025).
- Prefrontal and hippocampal theta oscillations co-occurred (P = 0.039) and hippocampal–prefrontal 3.5-Hz phase coupling (PLV) was higher on good than bad performance trials during the final 1.5 s of retrieval (P = 0.019, Bonferroni-corrected).

---

### Computational framework

The paper applies **representational similarity analysis (RSA)** combined with **oscillatory phase coding** as its analytical and theoretical framework.

The RSA framework models neural representations as spatial patterns of iEEG activity; representational similarity is measured by Spearman correlation between such patterns. The key computational hypothesis is that multiple competing goals are maintained and separated by assigning their neural representations to distinct phases of the hippocampal theta cycle — an implementation of the **theta phase coding** principle. Formally: each goal cue i has a prototypal neural vector NRV_i; during retrieval, the sliding similarity between NRV_i and the instantaneous brain state NV_t generates a time-varying reactivation signal, whose preferred theta phase (estimated by the weighted Moore-Rayleigh test) is assumed to uniquely index that cue. The core assumption is that phase separation (between-similarity) prevents representational interference across simultaneously maintained goals, analogous to how theta sequences in working memory multiplex multiple items.

---

### Prevailing model of the system under study

Based on the paper's introduction, the prevailing understanding was as follows. Hippocampal theta oscillations are well characterised in rodents (4–10 Hz continuous rhythms during movement, correlated with speed) and to a lesser extent in humans (lower frequency, ~3–4 Hz, bursty rather than continuous, particularly during virtual navigation). Theta was known to coordinate hippocampal activity during spatial navigation and mnemonic processing broadly.

For working memory, theoretical models (Lisman & Idiart 1995; Lisman & Jensen 2013) proposed that multiple items can be maintained by theta-coupled reactivation at distinct theta sub-cycles, and empirical evidence had shown gamma-power bursts for letter-selective representations at distinct theta/alpha phases. Goal-directed navigation was understood to involve prefrontal cortex (spatial goals, future paths) and hippocampus (spatial memory, theta generation), with hippocampal–prefrontal theta coupling enhanced during mnemonic load. However, whether a theta phase-coding mechanism analogous to working memory operated during the complex, continuous behaviour of goal-directed navigation in humans was unknown, and direct evidence for dynamic reactivation of large-scale goal representations at specific theta phases in humans was absent.

---

### What this paper contributes

The paper provides the first direct human iEEG evidence that competing goal representations are dynamically reactivated at distinct hippocampal theta phases during navigation. Specifically, it establishes: (1) cue-specific large-scale electrophysiological representations can be reliably extracted and tracked during the navigation period; (2) these representations reactivate preferentially at cue-specific theta phases that are stable across trials; (3) the degree to which different goals occupy distinct theta phases predicts individual memory performance — finer phase separation yields fewer navigation errors. This extends the theta phase-coding model from short-term memory paradigms to naturalistic, extended goal-directed behaviour, and identifies a neural mechanism by which multiple competing spatial goals can coexist without mutual interference. The parallel finding in prefrontal cortex, together with enhanced hippocampal–prefrontal theta coupling on good trials, further suggests that a distributed hippocampal–prefrontal circuit implements this phase-segregation mechanism. The finding also implies that theta phase coding, previously studied at a single-unit level in rodents, operates at the large-scale network level in humans.

---

### Brain regions & systems

- **Hippocampus (anterior)** — primary source of theta rhythm used to organise goal representation reactivation; preferred theta phases (3–4 Hz) discriminate distinct goal cues; primary locus of representation-to-theta-phase-clustering effect.
- **Lateral orbitofrontal cortex** — top-contributing region to cue-specific neural representations (69.8% positive channels); proposed to encode spatial goals and stimulus-reward associations.
- **Rostral middle frontal gyrus** — second top-contributing region (63.4% positive channels); part of prefrontal cluster for goal representation.
- **Prefrontal cortex (general)** — theta oscillations (5–6 Hz) also show representation-to-theta-phase-clustering; theta phase coupling with hippocampus enhanced during high-load navigation moments.
- **Entorhinal cortex** — used as an anatomical control; representation-to-theta-phase-clustering not observed here at 3–4 Hz, supporting hippocampal specificity.

---

### Mechanistic insight

The paper meets both criteria for a mechanistic insight entry.

**Criterion 1 (algorithm):** The paper formalises a theta phase-coding algorithm in which each competing goal representation is assigned a unique phase window within the ~3–4 Hz hippocampal theta cycle. Reactivation of goal-specific brain-wide activity patterns occurs preferentially at that assigned phase during navigation; phase distinctiveness across goals prevents representational interference.

**Criterion 2 (neural data):** Direct iEEG recordings provide neural evidence specifically supporting phase-based multiplexing over alternatives. The effect is: (a) absent during non-theta periods (ruling out a general retrieval account), (b) absent in entorhinal cortex at the same frequency (ruling out a generic low-frequency oscillation account), (c) significant after controlling for epileptic contamination via a restricted patient subset, and (d) behaviourally predictive in a dose-response manner (more distinct phases → better memory), tying the algorithmic variable directly to behaviour.

**Marr's levels:**

- **Computational**: The problem is maintaining multiple distinct spatial goals across an extended navigation period while preventing interference between them. The brain must represent "which goal, at this moment" without cross-contamination.
- **Algorithmic**: Each goal's large-scale electrophysiological representation (a distributed iEEG pattern) is preferentially reactivated at a cue-specific phase of the 3–4 Hz hippocampal theta oscillation. The Moore-Rayleigh weighted phase-locking value quantifies how strongly each representation is phase-tuned. Between-cue phase separation (operationalised as low between-similarity Rayleigh z) is the key variable predicting performance.
- **Implementational**: The paper characterises the hippocampus as the oscillatory "clock" generating 3–4 Hz theta bursts; prefrontal regions (particularly lateral orbitofrontal and middle frontal gyrus) carry spatially goal-specific information; hippocampal–prefrontal 3.5-Hz phase coupling is enhanced during high-demand navigation moments. The paper does not identify specific cell types, synaptic mechanisms, or neuromodulatory contributions; the implementation is characterised at the level of macroscopic field potentials and inter-regional coupling.

---

### Limitations & open questions

- **Patient population**: All participants were epilepsy patients undergoing presurgical monitoring; generalisation to healthy brains is uncertain, and residual epileptic activity could influence results despite control analyses.
- **Confound of cue identity and goal location**: The task paired each cue object uniquely with one location throughout the experiment, making it impossible to cleanly dissociate neural representations driven by visual object properties from those driven by associated spatial goals. Future designs should orthogonalise cue and goal identity.
- **Capacity of theta phase coding**: It is unknown how many distinct goals can be simultaneously assigned to separate theta phases. The theta/gamma capacity model predicts limits based on frequency ratio; this was not tested.
- **Causal role**: The study is correlational. It is unclear whether theta phase organisation causes better memory or whether both are products of some third factor (e.g., general hippocampal health). Stimulation or disruption studies would be needed.
- **Theta frequency differences**: Hippocampal theta peaked at 3–4 Hz and prefrontal at 5–6 Hz in this virtual-navigation paradigm. The relationship between these two oscillatory sub-bands and their interaction with gamma (for a theta-gamma code) was not fully characterised.
- **Mechanistic depth**: The paper does not identify which cell types or synaptic mechanisms generate the phase-specific reactivation, leaving the implementational level under-specified.
- **Reward vs. spatial content**: The representation of each cue may partially reflect reward history rather than purely spatial goal information; the two were not fully disentangled.

---

### Connections & keywords

**Key citations:**
- Lisman & Idiart (1995) — original theta subcycle model for working memory capacity
- Lisman & Jensen (2013) — theta-gamma neural code review
- Fuentemilla et al. (2010, Curr. Biol.) — theta-coupled periodic replay in working memory
- Bahramisharif et al. (2018, PLOS Biol.) — serial representation at letter-selective sites at distinct theta phases
- Watrous et al. (2018, eLife) — phase-tuned neuronal firing for contextual/navigational goals (MODAL algorithm)
- Jones & Wilson (2005, PLoS Biol.) — theta coordination of hippocampal–prefrontal interactions in spatial memory
- Feierstein et al. (2006, Neuron) — spatial goals in rat orbitofrontal cortex
- Chanales et al. (2017, Curr. Biol.) — representational repulsion for overlapping spatial memories
- Kriegeskorte et al. (2008) — representational similarity analysis framework
- Bush et al. (2017, PNAS) — human hippocampal theta during navigation

**Named models or frameworks:**
- Theta phase coding / theta subcycle model
- Representational Similarity Analysis (RSA)
- Time-resolved spatial RSA (tr-sRSA)
- MODAL algorithm (oscillatory burst detection)
- Moore-Rayleigh test (weighted phase-clustering statistic)
- Theta-gamma neural code

**Brain regions:**
- Hippocampus (anterior)
- Lateral orbitofrontal cortex
- Rostral middle frontal gyrus
- Prefrontal cortex
- Entorhinal cortex

**Keywords:**
- hippocampal theta oscillations
- theta phase coding
- goal-directed navigation
- representational similarity analysis
- intracranial EEG
- working memory analogy
- goal representation reactivation
- prefrontal-hippocampal coupling
- virtual spatial navigation
- oscillatory phase multiplexing
- goal interference separation
- large-scale electrophysiological representations
