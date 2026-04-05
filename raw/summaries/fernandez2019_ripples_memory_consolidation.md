---
source_file: fernandez2019_ripples_memory_consolidation.md
title: Long-duration hippocampal sharp wave ripples improve memory
authors: Antonio Fernández-Ruiz, Azahara Oliva, Eliezyer Fermino de Oliveira, Florbela Rocha-Almeida, David Tingley, György Buzsáki
year: 2019
journal: Science
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Long-duration hippocampal sharp wave ripples (SPW-Rs), which recruit more spatially selective neurons representing larger portions of planned routes, are causally necessary and sufficient for spatial memory performance in rats.

---

### Background & motivation

Hippocampal sharp wave ripples (SPW-Rs) are widely hypothesized to support memory consolidation and action planning by replaying neuronal sequences during immobility and sleep. Prior work had shown that disrupting ripples impairs memory, but the mechanistic question of what makes some ripples more memory-relevant than others remained open. The duration of ripples follows a skewed distribution, with a minority of unusually long events, and the functional significance of this variability was unknown. This paper asks whether long-duration ripples are specifically tied to mnemonic demand, and whether their prolongation causally improves memory.

---

### Methods

- **Subject population**: Rats (n = 20 main cohort; additional cohorts for controls and ripple-truncation experiments; total approximately 31 rats across conditions).
- **Task design**: Hippocampus-dependent M-maze delayed alternation task. Outbound trials (requires working memory; sensitive to SPW-R disruption) and inbound trials (no memory demand; used as within-animal control).
- **Recordings**: Multisite silicon probe electrophysiology in dorsal CA1; single-unit isolation of pyramidal cells and interneurons.
- **Optogenetics**: Bilateral viral expression of CaMKII-ChR2 in dorsal CA1 pyramidal cells. Closed-loop ripple prolongation: online ripple detection triggered a 100-ms tapered light pulse to extend each detected ripple. Random-stimulation control: same light pulse delivered 400–1000 ms after ripple detection. Ripple truncation: short high-intensity pulses to abort ripples.
- **Comparisons across tasks**: SPW-R duration compared between familiar vs. novel environments, and between memory-demanding tasks (T-maze, M-maze, cheeseboard) vs. non-memory tasks (open field, linear/circular track).
- **Neural content analysis**: Participation probability, baseline firing rate, place field properties, and cross-correlations of neurons active in early vs. late portions of different ripple types.

---

### Key findings

- Long-duration ripples (>100 ms) occurred significantly more often during novel environments vs. familiar (P < 10^−93) and during memory-demanding tasks vs. non-memory tasks (P < 10^−90); doublet and triplet ripples also increased under memory demand.
- Correct M-maze trials were preceded by significantly longer ripples in the delay box compared with error trials (P < 10^−5).
- Closed-loop optogenetic prolongation of ripples significantly improved outbound (memory-dependent) performance vs. both no-stimulation and random-stimulation controls (P < 10^−10, repeated-measures ANOVA); inbound performance was unaffected.
- Animals in the prolonged-ripple condition reached 80% correct criterion significantly earlier than controls (P < 0.05).
- Randomly induced ripples recruited similar neurons to spontaneous short ripples and contained little spatial information; they did not improve memory.
- Optogenetically prolonged ripples recruited an additional, distinct population of lower-firing-rate pyramidal cells with place fields predominantly in the side arms of the maze (the task-relevant locations), not the same cells that fired in the early (spontaneous) part of the ripple.
- Within prolonged ripples, neurons fired in either the early or late part (51% and 43% respectively), but rarely both (6%), indicating sequential recruitment rather than re-activation of the same cells.
- Prolonged ripples showed higher neuronal diversity (fraction of recorded neurons participating) than short spontaneous or randomly induced ripples (P < 10^−60 and 10^−100).
- Neurons representing the same side arm co-fired more strongly during prolonged and spontaneous long ripples than neurons representing opposite arms; this coherence was absent in randomly induced ripples.
- Truncating ripples (preventing long-duration events) impaired outbound but not inbound performance, mirroring electrical disruption results.

---

### Computational framework

Not applicable in the sense of a formal computational model. However, the paper invokes an **attractor network** framework for CA1 dynamics: once a neuronal trajectory is initiated at ripple onset, optogenetic perturbation recruits additional neurons constrained by the current network attractor state rather than generating an arbitrary sequence. This framing is used to explain why closed-loop prolongation (which respects the ongoing attractor trajectory) has memory benefits while random stimulation (which ignores network state) does not. The paper also implicitly invokes a **sequential replay** account of memory consolidation, in which the informational content of a ripple — specifically how much of a future route is represented — determines its mnemonic value.

---

### Prevailing model of the system under study

The introduction frames SPW-Rs as a well-established mechanism for memory consolidation and action planning, supported by a large body of work (Buzsáki 2015; Wilson & McNaughton 1994; Girardeau et al. 2009; Jadhav et al. 2012). The prevailing view held that SPW-Rs in general support memory by replaying experience-related neuronal sequences during rest and immobility, and that disrupting these events impairs subsequent memory. However, the field had not distinguished between short and long ripples, treating ripples largely as a uniform event class. The skewed duration distribution was noted in prior work (Davidson et al. 2009; Pfeiffer & Foster 2015) but its functional significance had not been tested causally. The standard model also debated whether CA1 sequences are computed locally in CA1 or are inherited from upstream regions (CA3, entorhinal cortex).

---

### What this paper contributes

This paper establishes that ripple duration is a functionally meaningful dimension — not all ripples are equivalent for memory. It shows that long-duration ripples are preferentially generated under memory demand and that their prolongation causally improves memory, while randomly induced ripples of similar duration do not. The key mechanistic insight is that the memory benefit depends on the neuronal content of the extended ripple: prolongation respects the ongoing attractor-state trajectory and recruits spatially selective neurons encoding task-relevant locations (side arms), effectively extending the replayed route. This distinguishes informative elongation (driven by network state) from uninformative activation (random stimulation). The results support a model in which the hippocampus generates longer ripples when more of a planned route needs to be represented, and suggest that CA1 sequences are at least partially computed locally rather than being fully inherited from upstream regions.

---

### Brain regions & systems

- **CA1 (dorsal hippocampus)** — primary site of recording and optogenetic manipulation; location of ripple generation, pyramidal cell sequence replay, and place cell activity central to all findings.
- **CA3** — cited as source of excitatory input driving the sharp wave component of SPW-Rs; referenced in framing the question of whether sequences are inherited from upstream or computed locally in CA1.
- **Entorhinal cortex / neocortex** — raised as an alternative explanation: differential effects of closed-loop vs. random stimulation might be mediated by network state in areas upstream from CA1; not directly recorded in this study.

---

### Mechanistic insight

This paper meets both criteria for a mechanistic insight.

**Phenomenon**: Long-duration hippocampal SPW-Rs are associated with better spatial memory, and causally prolonging them improves memory — but only when prolongation respects the ongoing network trajectory.

**Computational level**: The hippocampus solves the problem of representing future routes for memory-guided action. Longer ripples are generated when more of a route needs to be pre-played, enabling prospective coding of planned trajectories.

**Algorithmic level**: SPW-Rs implement sequential neuronal replay. The early (spontaneous) portion initiates a trajectory beginning with high-firing-rate neurons coding the current location (central arm); the late portion extends the sequence by recruiting lower-firing-rate neurons coding upcoming locations (side arms). The sequencing is constrained by the current attractor state of the CA1 network: neurons recruited in the prolonged portion fire coherently with same-side-arm neurons already active, preserving representational structure. Random stimulation bypasses this attractor constraint and recruits the same neurons as short ripples, adding no spatial information.

**Implementational level**: The paper identifies specific cellular substrates: higher-firing-rate pyramidal cells fire in the early (spontaneous) part; lower-firing-rate cells with side-arm place fields are recruited in the late (optogenetically extended) part. Interneurons show parallel patterns. ChR2 expression is targeted to CaMKII+ pyramidal cells in dorsal CA1. The attractor dynamic is proposed to be a local CA1 computation, not purely inherited from CA3 or entorhinal inputs, though this is not directly tested.

**Bonus**: The paper specifies cell-type distinctions (pyramidal cells vs. interneurons), neuromodulatory targeting (CaMKII promoter), and biophysical mechanism (optogenetic depolarisation of ChR2-expressing cells constrained by ongoing network state).

---

### Limitations & open questions

- The study is confined to rats performing spatial tasks; generalisability to non-spatial memory or other species is untested.
- The optogenetic approach activates all CaMKII+ CA1 pyramidal cells, not specific subpopulations; finer-grained dissection of which cells drive the memory benefit is not possible with this method.
- Whether the memory improvement is due to prolongation during the delay period specifically, or occurs across all ripples in the session, is not fully resolved.
- The paper raises but does not resolve whether the critical computation is local to CA1 or depends on state-dependent inputs from upstream regions (CA3, entorhinal cortex).
- Ripple truncation experiments replicate prior disruption studies but do not fully disentangle the role of long-duration events from overall ripple count or content.
- The paper does not address sleep-dependent consolidation — all manipulations are during waking behaviour; whether the same principles apply to sleep ripples is left open.
- The mechanism by which the CA1 network generates longer ripples under memory demand in the first place (i.e., what upstream or neuromodulatory signals regulate ripple duration) is not investigated.

---

### Connections & keywords

**Key citations**:
- Buzsáki (2015) Hippocampus — comprehensive review of SPW-R function
- Jadhav et al. (2012) Science — ripple disruption impairs memory in M-maze
- Wilson & McNaughton (1994) Science — landmark replay during sleep
- Girardeau et al. (2009) Nature Neuroscience — disruption of sleep ripples impairs consolidation
- Davidson et al. (2009) Neuron — long-duration ripples and extended replay
- Pfeiffer & Foster (2015) Science — prospective coding in SPW-Rs
- Stark et al. (2015) PNAS — optogenetic control of CA1 ripples
- Oliva et al. (2016) Neuron; Oliva et al. (2018) Cell Reports — SPW-R generation and CA1 dynamics

**Named models or frameworks**:
- Sharp wave ripple (SPW-R) replay model of memory consolidation
- Attractor network dynamics (CA1 local computation)
- Closed-loop optogenetic manipulation paradigm
- M-maze delayed alternation task (Kim & Frank 2009)

**Brain regions**:
- CA1 (dorsal hippocampus)
- CA3
- Entorhinal cortex

**Keywords**:
- hippocampal sharp wave ripples
- memory consolidation
- sequence replay
- closed-loop optogenetics
- place cells
- spatial working memory
- ripple duration
- attractor dynamics
- prospective coding
- CA1 pyramidal cells
- neuronal diversity
- memory-guided navigation
