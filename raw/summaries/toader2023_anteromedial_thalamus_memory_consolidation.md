---
source_file: toader2023_anteromedial_thalamus_memory_consolidation.md
title: "Anteromedial thalamus gates the selection and stabilization of long-term memories"
authors: Andrew C. Toader, Josue M. Regalado, Yan Ran Li, Andrea Terceros, Nakul Yadav, Suraj Kumar, Sloane Satow, Florian Hollunder, Alessandra Bonito-Oliva, Priya Rajasethupathy
year: 2023
journal: Cell
paper_type: empirical
contribution_type: empirical
---

### One-line summary

The anteromedial (AM) thalamus preferentially encodes salient memories during training and, via progressive functional coupling with anterior cingulate cortex, is both necessary and sufficient to gate the consolidation of contextual memories into long-term cortical storage.

---

### Background & motivation

Systems consolidation — the gradual transfer of memories from hippocampus to cortex over weeks to months — is well established, but the circuit mechanisms that select which memories get stabilised, and that mediate the actual transfer, remain poorly understood. Prior work focused on hippocampus–cortex interactions, largely bypassing subcortical circuits that connect the two. The anterior thalamus sits at an anatomical nexus (receiving hippocampal input via the mammillary bodies and projecting directly to anterior cingulate cortex, ACC) but its causal role in consolidation had not been investigated. This paper fills that gap by combining longitudinal neural recordings, bidirectional optogenetic manipulations, and a novel multi-region cellular-resolution imaging approach.

---

### Methods

- **Behavioural task**: Head-fixed mice performed a virtual-reality contextual memory task (multi-modal cues, sucrose vs. airpuff outcomes) over a training phase (days 1–5) followed by weekly retrieval probes spanning up to 55 days. A two-reward variant (high-reward vs. low-reward contexts) was used for consolidation-enhancement experiments.
- **Brain-wide retrograde tracing**: rgAAV injection into ACC identified upstream regions (anterior thalamus, BLA, entorhinal cortex) for recording targeting.
- **Multi-site fibre photometry**: GCaMP6f was expressed in ACC, hippocampus (HPC), anterior thalamus (ANT), BLA, and entorhinal cortex; bulk calcium signals were recorded daily during training and weekly during consolidation. A generalised linear model decomposed variance by task variable.
- **Optogenetic inhibition**: Projection-defined inhibition of the AM-to-ACC circuit (retroAAV-Cre in ACC + floxed-stGtACR2 in AM) was delivered during training or during the consolidation window; contextual fear conditioning was used as an independent behavioural validation.
- **Optogenetic excitation**: SSFO-based gain amplification of AM-to-ACC projections during training tested whether salient-memory consolidation could be extended to less salient memories.
- **Chemogenetic inhibition**: hM4Di DREADDs were used to establish hippocampal vs. ACC dependence at recent vs. remote time points.
- **Multi-region cellular-resolution imaging**: A novel fibre-bundle-based system (600 µm Fujikura bundles, Nikon 10× objective, Photometrics Prime 95b camera) enabled simultaneous single-cell-resolution GCaMP imaging of AM, HPC, and ACC in the same behaving mouse, tracked longitudinally across up to 34 days.

---

### Key findings

- Anterior thalamus (ANT) contained sustained, learned-association-specific neural correlates (both cue-selective and anticipatory-lick-correlated signals) that persisted throughout the weeks-long consolidation window; these were absent in BLA and entorhinal cortex.
- Bilateral inhibition of AM-to-ACC projections during training produced no recent memory deficit but a significant remote memory impairment (both in the VR task and contextual fear conditioning; fear conditioning remote freezing: 64% mCherry vs. 39% stGtACR2, p < 0.01).
- SSFO-based gain amplification of AM-to-ACC during training selectively rescued remote retrieval of the otherwise unconsolidated low-reward context (significant interaction Group × Context × Session, p = 0.0244), without affecting high-reward consolidation or behaviour in a control retrosplenial-to-ACC cohort.
- Cellular-resolution imaging revealed that AM preferentially encoded the high-reward context during training, whereas HPC and ACC showed equal encoding of both contexts at that time point.
- AM–ACC pairwise functional correlations progressively increased across weeks (peaking ~R20), while HPC–AM and HPC–ACC correlations did not.
- ACC cells that were highly correlated with AM cells at R20 were significantly more likely to maintain high-reward tuning at R34 (Wilcoxon rank-sum p < 0.01), and were more central in the ACC functional network than expected by chance.
- Intra-ACC ensemble correlations for the high-reward context increased from R6 to R34; inhibition of AM-to-ACC during training disrupted this context-specific ensemble synchrony at remote time.

---

### Computational framework

The paper is primarily circuit-level and experimental, but implicitly operates within a **systems consolidation** framework. The core computational idea is that consolidation requires both *selection* (identifying which memories are worth storing long-term) and *stabilisation* (tuning and synchronising cortical ensembles over time). AM thalamus is proposed to implement selection by preferentially encoding salient experiences, and to implement stabilisation by progressively strengthening correlated activity with ACC, thereby coordinating cortical ensemble timing.

Key variables in this framework: differential salience encoding (AM tuning to high- vs. low-reward contexts); inter-regional functional coupling (AM–ACC Pearson correlation over time); intra-cortical ensemble synchrony (pairwise ACC correlations); and behavioural discrimination index (lick-rate difference between reward and aversive contexts at recent vs. remote retrieval).

The authors explicitly note that computational models (Tome et al. 2022; Fiebig & Lansner 2014) have predicted a role for thalamo-cortical coordination in consolidation, lending theoretical grounding to the circuit mechanism identified here.

---

### Prevailing model of the system under study

The standard model of systems consolidation (Buzsaki 1996; McClelland et al. 1995; Frankland & Bontempi 2005) posits that the hippocampus initially encodes new memories and over weeks "trains" the neocortex — particularly ACC — to form more enduring representations. Alternative dual-trace models (Nadel & Moscovitch 1997; Kitamura et al. 2017) propose that cortex and hippocampus form parallel representations from the outset, with hippocampal dependence declining over time. Both classes of model focus on the hippocampus–cortex axis. The Papez circuit (hippocampus → mammillary bodies → anterior thalamus → cingulate) has long been known from lesion studies (Aggleton & Brown 1999; Korsakoff syndrome patients with anterior thalamic lesions show retrograde amnesia), but the specific mechanistic contribution of the anterior thalamus to active consolidation — particularly the anteromedial nucleus projecting to ACC — was unexplored. The field lacked both the causal tools and the longitudinal multi-region cellular-resolution imaging needed to test whether and how the thalamus participates in the consolidation process.

---

### What this paper contributes

This paper establishes the AM thalamus as an active, causal participant in memory consolidation rather than a passive relay. Specifically:

1. **Selection**: AM acts as a salience filter during training, preferentially encoding high-salience memories at the cellular level — a function not observed in hippocampus or ACC at the same stage.
2. **Stabilisation**: AM progressively increases functional coupling with ACC over weeks, and the specific ACC cells co-active with AM during this period are the ones that maintain tuning and ensemble synchrony at remote time — providing a mechanism for how a transient thalamic signal has lasting cortical effects.
3. **Bidirectional causality**: Inhibition of AM-to-ACC impairs remote (but not recent) memory; gain amplification rescues consolidation of otherwise forgotten (low-salience) memories. This bidirectionality is rare and clinically significant — it suggests that the AM–ACC axis could in principle be targeted to enhance or weaken long-term memory storage.
4. **Dissociation from hippocampus**: HPC–ACC and HPC–AM correlations do not increase over the consolidation period, implying that the progressive HPC-to-cortex transfer standard model must be refined to include an AM-gating step that operates somewhat independently.

---

### Brain regions & systems

- **Anteromedial thalamus (AM)** — primary focus; identified as the salience-selective memory filter and coordinator of long-term cortical consolidation via progressive coupling with ACC.
- **Anterior cingulate cortex (ACC)** — target of AM projections; the site of long-term cortical memory storage; dependent on AM input for ensemble tuning and synchrony at remote time points.
- **Hippocampus (HPC / CA1)** — required for learning and recent memory retrieval; becomes dispensable at remote time; does not show the progressive inter-regional coupling with AM or ACC seen during consolidation.
- **Anterior thalamus (ANT, broadly)** — screened by photometry; provided bulk-level memory signals; AM is the specific nucleus mediating the effects.
- **Basolateral amygdala (BLA)** — recorded alongside other regions; showed sucrose-related signal increases but no sustained memory-correlate signal comparable to AM.
- **Entorhinal cortex (ENT)** — recorded; showed no prominent sustained memory-related signals at the bulk level.
- **Mammillary bodies** — part of the Papez circuit; provide indirect hippocampal input to AM (anatomical tracing confirmed; not directly manipulated).
- **Retrosplenial cortex (RSP)** — used as a specificity control for the SSFO excitation experiment; RSP-to-ACC gain amplification did not rescue low-reward consolidation.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight:

1. It formalises an algorithm: AM selects salient memories during training, then coordinates cortical ensemble stabilisation via progressive inter-regional coupling — a two-stage mechanism (selection then stabilisation) implemented by a specific thalamo-cortical projection.
2. It provides neural data (cellular-resolution longitudinal calcium imaging, optogenetic perturbations) that link the model's specific variables (AM–ACC correlations, ACC ensemble synchrony) to the proposed algorithm — not merely to behaviour.

**Marr's levels:**

- **Computational**: The brain must solve a memory selection problem — not all experiences are worth storing long-term, and resources for long-term cortical storage are limited. The system must identify high-value or high-salience experiences and preferentially route them to durable cortical representations.
- **Algorithmic**: AM preferentially encodes salient experiences (selection step) and then, over weeks, increases functional coupling with ACC (stabilisation step). ACC cells that are co-active with AM gain preferential tuning and become more highly interconnected in the ACC network, creating stable ensemble representations accessible at remote time. Disrupting AM-to-ACC activity during training prevents this cascade even though the encoding and recent memory are unaffected.
- **Implementational**: The study identifies the AM-to-ACC projection as the critical route (confirmed by projection-specific optogenetics via retroAAV-Cre strategy). The temporal dynamics operate over weeks, consistent with a slow synaptic strengthening or network reorganisation process. The paper does not resolve the specific synaptic, cellular, or molecular mechanisms (e.g., LTP rules, neuromodulatory identity of relevant AM cells), but notes that the findings provide circuit-level entry points toward transcriptional and epigenetic programs for long-term memory maintenance.

**Bonus**: The study is noteworthy for developing a new optical technology — the multi-region fibre-bundle imaging system — that enabled the key mechanistic observations (simultaneous AM + HPC + ACC single-cell tracking for up to 34 days), and for demonstrating bidirectional control (both inhibition and excitation alter consolidation outcome), which goes beyond correlation to establish causal sufficiency.

---

### Limitations & open questions

- **Extinction and reconsolidation confounds**: Repeated weekly retrieval sessions may contribute to the observed changes in neural dynamics. A fully between-subjects design (separate cohorts for each time point) would more precisely isolate consolidation-specific effects.
- **Defining remote memory**: The study lumps R27, R34, and R55 as "remote"; future work should define more precise time windows to capture intermediate transitions.
- **AM activity beyond training**: The paper focuses on AM's role during training; its continued contributions during offline consolidation (e.g., sleep replay, sharp-wave ripples) remain unexplored.
- **Temporal resolution**: GCaMP imaging lacks the temporal resolution to study precise oscillatory mechanisms (theta, spindles, ripples) during online or offline periods; paired electrophysiology would be needed.
- **Other thalamic nuclei and limbic circuits**: Crosstalk with other anterior thalamic nuclei and limbic regions (BLA, entorhinal) was not ruled out; their coordinated or independent contributions to different memory types remain open.
- **Cellular mechanisms**: The study identifies the projection but not the synaptic or molecular basis of the progressive AM–ACC coupling; plasticity rules, neuromodulatory inputs to AM, and epigenetic programs are identified as future directions.
- **Human relevance**: While Korsakoff syndrome provides translational relevance, direct mapping to human anterior thalamic function and memory disorders awaits further investigation.

---

### Connections & keywords

**Key citations**:
- Frankland & Bontempi (2005) — standard systems consolidation model
- Kitamura et al. (2017) — engrams and circuits in systems consolidation
- Aggleton & Brown (1999) — hippocampal–anterior thalamic axis and episodic memory
- McClelland, McNaughton & O'Reilly (1995) — complementary learning systems
- Nadel & Moscovitch (1997) — multiple trace theory
- Tome, Sadeh & Clopath (2022) — computational prediction of thalamo-cortical coordination in consolidation
- Buzsaki (1996) — hippocampo-neocortical dialogue
- Zhu et al. (2018) — dynamic salience processing in paraventricular thalamus

**Named models or frameworks**:
- Standard model of systems consolidation
- Multiple trace theory
- Papez circuit
- stGtACR2 optogenetic inhibition
- SSFO (stabilised step function opsin) gain amplification
- GCaMP6f calcium imaging
- Generalised linear model (encoding model for photometry data)
- Fibre-bundle multi-region imaging system (novel technology developed in this paper)

**Brain regions**:
- Anteromedial thalamus (AM)
- Anterior cingulate cortex (ACC)
- Hippocampus (HPC / CA1)
- Anterior thalamus (ANT)
- Basolateral amygdala (BLA)
- Entorhinal cortex (ENT)
- Mammillary bodies
- Retrosplenial cortex (RSP)

**Keywords**:
- Systems memory consolidation
- Anteromedial thalamus
- Thalamo-cortical circuit
- Memory selection and stabilisation
- Longitudinal calcium imaging
- Multi-region imaging
- Optogenetic projection manipulation
- Inter-regional functional coupling
- Cortical ensemble synchrony
- Salience encoding
- Remote memory retrieval
- Virtual-reality memory task
