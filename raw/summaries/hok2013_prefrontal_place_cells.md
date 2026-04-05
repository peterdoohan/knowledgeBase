---
source_file: hok2013_prefrontal_place_cells.md
title: "Prefrontal Cortex Focally Modulates Hippocampal Place Cell Firing Patterns"
authors: Vincent Hok, Ehsan Chah, Etienne Save, Bruno Poucet
year: 2013
journal: The Journal of Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Inactivation of the medial prefrontal cortex (mPFC) in overtrained rats leaves hippocampal place cell goal-related firing intact but reduces place field overdispersion, suggesting the mPFC modulates the variability of hippocampal spatial codes rather than their average structure.

---

### Background & motivation

The medial prefrontal cortex (mPFC) and hippocampus are strongly interconnected: the hippocampus projects directly to mPFC, while mPFC projects back only indirectly (via entorhinal cortex and nucleus reuniens). Prior work showed that mPFC neurons fire selectively at a goal location during navigation and that hippocampal lesions abolish this goal activity. Hippocampal place cells themselves develop secondary firing fields at goal locations, raising the hypothesis that coordinated place cell activity at the goal drives mPFC planning computations. However, it was unknown whether the reverse is also true — whether mPFC integrity is required to sustain hippocampal place cell goal-related firing. This study tests that hypothesis by pharmacologically inactivating mPFC while recording hippocampal CA1 place cells during an established goal-oriented navigation task.

---

### Methods

- **Subjects**: Male Long–Evans rats (n = 6) overtrained (>2 months) on a goal-oriented navigation task in which the animal must remain in an unmarked 10 cm radius goal zone for 2 s to trigger food pellet release.
- **Surgical preparation**: Bilateral 23-gauge guide cannulae implanted targeting prelimbic mPFC; 16-wire nichrome electrode arrays implanted over dorsal hippocampal CA1.
- **Inactivation protocol**: Within-session design with four consecutive 16-min sessions — Standard 1 (baseline), Saline injection + recording, Lidocaine injection (10 µg/0.5 µl/side) + recording, Standard 2 (recovery). Animals served as their own controls.
- **Electrophysiology**: Single-unit isolation of 53 CA1 pyramidal cells via off-line spike sorting (DataWave/Offline Sorter); local field potentials (LFPs) recorded from two electrodes.
- **Spatial analyses**: Firing rate maps (2.5 cm pixels), spatial information index (Skaggs et al., 1993), spatial coherence (Muller and Kubie, 1987), between-session spatial correlation.
- **Goal-related activity**: Firing rates during the 2 s delay period; peri-event time histograms (PETHs) aligned to goal zone entry; theta band (5–10 Hz) power and peak frequency from LFPs.
- **Overdispersion**: Variance of standardised Z-scores across passes through the place field centre (Fenton and Muller, 1998 method); 36 cells qualified.
- **Behavioural measures**: Correct responses, success rate, locomotion speed, post-stimulus reaction time.

---

### Key findings

- **No behavioural impairment**: mPFC inactivation did not affect number of correct responses, success rate, or locomotion in overtrained rats, confirming that mPFC is no longer needed for task execution after extensive training.
- **Reaction time effect confirms lidocaine efficacy**: Post-stimulus locomotion change ratio was significantly reduced under lidocaine vs. saline (t(18) = 4.395, p < 0.001), verifying effective inactivation.
- **Goal-related firing preserved**: Mean goal-zone firing rate was not significantly altered (1.17 ± 0.21 vs. 1.46 ± 0.27 Hz, NS). Theta ratio and theta peak frequency during the goal period were also unchanged. Temporal dynamics of goal-related firing (gradual ramp peaking ~1 s after goal entry) were intact.
- **Focal increase in place field peak firing**: mPFC inactivation increased overall firing rate (p < 0.05) and peak firing rate within the place field centre (t(52) = 3.047, p < 0.01), and elevated spatial coherence (p < 0.05), without affecting spatial selectivity, information content, field size, or bursting propensity.
- **Spatial stability maintained**: Between-session spatial correlation was not significantly different between Standard 1/saline and saline/lidocaine pairs (0.47 vs. 0.49, NS).
- **Overdispersion reduced**: The variance of Z-scores across passes (overdispersion) was significantly lower under lidocaine than saline (Levene's W = 17.850, p < 0.001; confirmed at single-cell level t(35) = 2.048, p < 0.05). Saline variance: χ² = 3.624; lidocaine variance: χ² = 2.128.

---

### Computational framework

Not applicable in the sense that the paper does not develop or fit a formal computational model. However, the authors interpret overdispersion within a **multi-state attractor / attentional switching framework** (following Jackson and Redish, 2007; Fenton et al., 2010): place cell ensembles are thought to toggle between distinct spatial "place codes" corresponding to different attentional states, and the variance of firing across passes (overdispersion) reflects this switching. Under this framework, mPFC inactivation is proposed to bias the ensemble toward a single preferred place code, reducing code-switching and thereby decreasing overdispersion while locally sharpening the preferred field. The results constrain network models in which prefrontal top-down input drives state transitions in hippocampal attractor dynamics.

---

### Prevailing model of the system under study

The paper's introduction presents a model in which hippocampus and mPFC form a functionally coupled navigation system. Hippocampal place cells provide a precise spatial map, and mPFC neurons encode goal locations in a coarse, goal-trajectory planning code. The coordinated firing of large fractions of hippocampal cells at the goal was hypothesised to interact with mPFC to compute optimal paths. The dominant assumption, supported by lesion and disconnection studies (Wang and Cai, 2006; Kyd and Bilkey, 2003, 2005), was that mPFC integrity is required for hippocampal spatial stability and goal-related firing — i.e. that mPFC exerts a top-down organising influence that sustains the hippocampal goal signal. Prior lesion work also showed that mPFC damage destabilises place fields over time and makes them more reactive to cue changes (Kyd and Bilkey, 2003, 2005).

---

### What this paper contributes

The key contribution is a double dissociation using reversible inactivation (sidesteps long-term compensatory effects of lesions): mPFC inactivation does NOT affect (a) goal-related firing of place cells, (b) theta-band network activity during goal occupancy, or (c) global spatial stability. This rules out the hypothesis that mPFC drives the hippocampal goal signal and shows that the goal representation can be maintained autonomously by the hippocampus (or its subcortical inputs). What mPFC inactivation does affect is the trial-to-trial variability (overdispersion) of place field firing — specifically, removing prefrontal input reduces overdispersion and increases firing coherence within the field centre. This supports a revised model in which mPFC's primary modulatory role is not to establish the spatial/goal map but to regulate the attentional or cognitive state-switching that generates firing variability, potentially maintaining behavioural flexibility. The paper also adds the methodological point that effects of mPFC lesions on waveform characteristics (Kyd and Bilkey, 2005) are likely long-term adaptation artefacts rather than acute functional consequences.

---

### Brain regions & systems

- **Medial prefrontal cortex (prelimbic area)** — site of lidocaine inactivation; proposed to modulate hippocampal ensemble state-switching and behavioral flexibility; shown to be dispensable for goal-related place cell firing in overtrained animals.
- **Hippocampal CA1** — recording site; principal locus of place cell activity, goal-related firing, and overdispersion; receives indirect input from mPFC via entorhinal cortex and nucleus reuniens.
- **Ventral tegmental area (VTA)** — discussed as a potential relay: mPFC pyramidal cells regulate VTA dopaminergic neurons, which project to CA1 interneurons; one mechanistic hypothesis for how mPFC inactivation disinhibits CA1 firing.
- **Perirhinal / entorhinal cortex** — discussed as an alternative relay pathway through which prefrontal inactivation could alter CA1 inhibitory tone.

---

### Mechanistic insight

The paper partially meets the bar. It provides neural recordings that rule out one hypothesised algorithm (mPFC driving goal signals) and identify a specific effect on place field overdispersion. However, it does not formalise or fit an explicit algorithm for the overdispersion phenomenon, and the proposed mechanism (mPFC biasing attractor state selection) is interpretive rather than formally demonstrated.

Mapping what is established onto Marr's levels:

- **Computational**: The brain must flexibly re-engage spatial codes when task contingencies change; mPFC contributes to this flexibility without being required for the core spatial map in overtrained animals.
- **Algorithmic**: Place cell ensembles express multiple alternating place codes (high overdispersion reflects switching between them); mPFC input modulates the probability of switching between these ensemble states. Removing mPFC input biases the system toward a single dominant code, reducing variance across passes.
- **Implementational**: Possible via mPFC → VTA → CA1 dopaminergic disinhibition, or via mPFC → perirhinal/entorhinal → CA1 interneuron pathway. Neither pathway is directly tested here.

The mechanistic picture is thus incomplete at the implementational level, and the algorithmic claim (state-switching) is inferred from overdispersion statistics rather than directly observed via simultaneous ensemble recordings with state decoding.

---

### Limitations & open questions

- Only overtrained animals were studied; the acute role of mPFC during task acquisition remains open. The authors acknowledge that mPFC goal activity may be critical during learning rather than execution.
- The study cannot determine whether goal signals are generated intrinsically within the hippocampus or depend on other extra-hippocampal sources (e.g., subicular–entorhinal loop, subcortical structures).
- The overdispersion reduction is interpreted as reduced state-switching, but this interpretation requires direct ensemble decoding of co-recorded place cells — a technique not used here (53 cells from 6 rats, small samples per rat).
- The indirect mPFC → hippocampus projection pathways (via VTA or entorhinal cortex) are proposed but not tested; the cellular mechanism of overdispersion modulation remains unknown.
- Lidocaine spread beyond prelimbic cortex cannot be fully ruled out, though histological verification of cannula placement and the reaction-time control suggest targeted inactivation.
- Generalisability to other task demands (e.g., shifting the goal location) is not addressed; the authors flag this as a necessary future experiment.

---

### Connections & keywords

**Key citations**:
- Hok et al. (2005) — mPFC goal-related firing in navigation task
- Hok et al. (2007a) — hippocampal place cell goal-related firing
- Fenton and Muller (1998) — overdispersion methodology
- Fenton et al. (2010) — attention-like modulation and place code switching
- Jackson and Redish (2007) — multiple spatial maps / ensemble state-switching
- Kyd and Bilkey (2003, 2005) — mPFC lesion effects on hippocampal place cells
- Burton et al. (2009) — hippocampal lesion abolishes mPFC goal activity
- O'Keefe and Nadel (1978) — cognitive map theory

**Named models or frameworks**:
- Cognitive map theory (O'Keefe and Nadel)
- Multi-state place code / attentional switching framework (Fenton et al., 2010; Jackson and Redish, 2007)
- Overdispersion as index of cognitive state

**Brain regions**:
- Medial prefrontal cortex (prelimbic area)
- Hippocampal CA1
- Ventral tegmental area (VTA)
- Perirhinal cortex
- Entorhinal cortex

**Keywords**:
- hippocampal place cells
- medial prefrontal cortex inactivation
- goal-related firing
- overdispersion
- place field firing variability
- lidocaine reversible inactivation
- hippocampal-prefrontal interaction
- spatial navigation
- attentional state-switching
- CA1 ensemble dynamics
- theta oscillations
- behavioral flexibility
