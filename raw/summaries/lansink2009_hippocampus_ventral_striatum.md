---
source_file: "lansink2009_hippocampus_ventral_striatum.md"
paper_id: "lansink2009_hippocampus_ventral_striatum"
title: "Hippocampus Leads Ventral Striatum in Replay of Place-Reward Information"
authors: "Carien S. Lansink, Pieter M. Goltstein, Jan V. Lankelma, Bruce L. McNaughton, Cyriel M. A. Pennartz"
year: 2009
journal: "PLoS Biology"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
methods: ["tetrode_recording"]
brain_regions: ["hippocampus", "hippocampus_ca1", "striatum", "ventral_striatum", "nucleus_accumbens"]
frameworks: ["reinforcement_learning"]
keywords: ["sleep_replay", "memory_consolidation", "place_cells", "reward_related_neurons", "hippocampal_striatal_reactivation", "sharp_wave_ripples", "theta_oscillations", "temporal_compression", "forward_replay", "spike_timing_dependent_plasticity", "explained_variance_method", "cross_structural_reactivation", "hippocampus", "leads", "ventral", "striatum", "replay", "place", "reward", "information"]
key_citations: ["schultz1997_neural_substrate_reward_pred"]
---

### One-line summary

During post-behavioral sleep in rats, hippocampal place cells and ventral striatal reward-related neurons jointly reactivate in a temporally compressed, forward-ordered manner, with the hippocampus consistently leading the ventral striatum — directly supporting the consolidation-theory prediction that the hippocampus orchestrates replay in its target structures.

---

### Background & motivation

Forming associations between spatial locations and rewards is essential for foraging and learned behavior, and depends on the hippocampus (HC) and ventral striatum (VS). The HC encodes spatial context via place cells, while the VS encodes reward-related information. Although the HC projects directly to the VS, it was unknown whether these two structures reactivate coherently during sleep and, if so, what temporal dynamics govern this process. Prior multi-area recording studies had not addressed whether cross-structural replay depends on the *type* of behavioral information encoded by cell assemblies, nor had they tested whether the HC leads VS during reactivation as consolidation theories predict.

---

### Methods

- **Subjects**: four male Wistar rats implanted with a split microdrive containing five tetrodes targeting dorsal hippocampal CA1 and seven tetrodes targeting the ventral striatum.
- **Task**: rats ran a triangular track repeatedly, visiting three reward wells baited with one of three food rewards (sucrose solution, vanilla dessert, chocolate mousse) per lap.
- **Recording design**: each daily session comprised a pre-behavior rest episode, a track-running episode, and a post-behavior rest episode; local field potentials and multi-unit spike trains were recorded simultaneously from HC and VS.
- **Reactivation measure**: explained variance (EV) method — Pearson correlation matrices of spike-train correlations across all simultaneously recorded HC-VS cell pairs were compared across episodes; REV (reversed EV, swapping pre- and post-behavioral rest) served as within-session control.
- **Subgroup analyses**: cell pairs were partitioned by (1) theta-rhythm modulation of each cell, (2) expression of place fields (HC) and reward-related correlates (VS), and (3) preferred firing order (HC→VS vs VS→HC) as assessed by temporal bias scores in cross-correlograms.
- **Replay dynamics**: cross-correlograms of "Double Correlate" pairs (place field + reward-related unit) were used to test forward direction, firing-order preservation, and temporal compression of replay relative to behavior.
- **Sleep-phase analysis**: reactivation was assessed separately for quiet wakefulness–slow-wave sleep (QW-SWS) and REM sleep.

---

### Key findings

- Cross-structural HC-VS reactivation was significant: EV = 9.7 ± 3.0% vs. REV = 1.4 ± 0.5% (p < 0.01; n = 21 sessions).
- Reactivation decayed gradually over at least 1 hour of post-behavioral rest and was significant during QW-SWS but not during REM sleep.
- **Theta modulation**: cell pairs in which both the HC and VS unit were theta-modulated showed stronger reactivation than pairs where only one or neither cell was theta-modulated.
- **Behavioral correlates**: "Double Correlate" pairs (HC place field + VS reward-related unit) showed very strong reactivation (EV: 22.9%, REV: 0.1%); no other subgroup (Place Field only, Reward-related only, No Correlates) showed significant reactivation.
- **Firing order**: HC→VS pairs showed the strongest reactivation (EV: 15.2%, REV: 0.0%); multilinear regression confirmed that both "Double Correlate" status (p < 0.02) and HC→VS firing order (p < 0.002) were independent predictors of a pair's contribution to session EV.
- Cross-structural replay was forward-directional: in 89% of pairs (43/47), the firing-order sign was preserved from track running to post-behavioral sleep (p < 0.0001 sign test).
- The hippocampal cell fired before the striatal cell in 83.7% of forward-reactivating pairs (36/43; p < 0.0001).
- Replay was temporally compressed by approximately 10-fold: peak cross-correlogram offsets during track running averaged ~2526 ms vs. ~53 ms during post-behavioral sleep (p < 0.01; n = 47).
- Reactivation was sparsely distributed: removing the top 17 contributing pairs (8.9% of 192 Double Correlate pairs) reduced [EV − REV] below 5%.

---

### Computational framework

The paper does not develop a new computational model but invokes **memory consolidation theory** and the **two-stage model of memory trace formation** (Buzsaki 1989; McClelland et al. 1995) as its interpretive framework. In this framework:

- **Encoding stage** (awake, theta-dominated): HC encodes spatial sequences via theta phase precession; temporal alignment of HC and VS activity by a shared theta oscillation creates near-synchronous firing windows that enable cross-structural plasticity.
- **Consolidation stage** (sleep, sharp wave-ripple dominated): HC reactivates stored sequences during sharp wave-ripples and orchestrates reactivation in projection targets (here, VS). The 10-fold temporal compression during sleep brings multi-second place–reward sequences into a timescale (~100 ms) compatible with spike timing-dependent plasticity (STDP) at HC→VS synapses.

The study also invokes **reinforcement learning** concepts (Rescorla-Wagner; Sutton & Barto; Schultz et al.) to frame the functional significance: the preferential HC→VS firing order during replay is suited to implement a backwards association from reward to the series of place representations leading to it, consistent with temporal difference-style credit assignment.

---

### Prevailing model of the system under study

As described in the introduction, the prevailing model at the time held that:

1. HC place cells encode spatial context during active behavior, with theta phase precession providing a temporal code.
2. VS neurons encode reward-related information (expectation, delivery, predictive cues) and receive anatomical input from HC, amygdala, PFC, and midline thalamus.
3. Sleep reactivation occurs independently within HC (spatial information) and VS (reward information).
4. Memory consolidation theories (Marr, Buzsaki, McClelland et al., McNaughton et al.) predict that the HC initiates replay in its projection targets, but this directional leadership had not been empirically demonstrated in a subcortical structure.

The key unknown was whether HC and VS reactivate *jointly*, whether this joint reactivation is selective for behaviorally relevant (place + reward) information, and whether the HC indeed leads the VS temporally during replay.

---

### What this paper contributes

The paper provides the first direct electrophysiological evidence that:

1. HC and VS reactivate *coherently* across structures during sleep — not as independent ensembles but in a coordinated, temporally structured manner.
2. This cross-structural reactivation is selective: it is strongly tied to pairs carrying *both* spatial (HC) and reward-related (VS) information, not to cells lacking such correlates.
3. The HC leads the VS in replay — the HC→VS temporal order is preferentially expressed during sleep reactivation (not VS→HC), consistent with the anatomical directionality of the HC→VS projection and with the consolidation-theory prediction of hippocampal orchestration.
4. Replay is forward-ordered and approximately 10-fold compressed, placing it on a timescale compatible with STDP at HC→VS synapses, making synaptic strengthening of place–reward associations mechanistically plausible.

Together, these findings supply a concrete offline mechanism for how associations between spatial context and motivational salience could be stored and consolidated — an open question prior to this work.

---

### Brain regions & systems

- **Hippocampus (CA1)** — encodes spatial location via place cells during behavior; initiates and leads cross-structural replay during QW-SWS; generates sharp wave-ripple complexes that trigger reactivation.
- **Ventral striatum (nucleus accumbens core and shell)** — encodes reward-related information (firing time-locked to reward site visits); receives replayed spatial input from HC and is proposed as the site where place–reward associations are consolidated via STDP.
- **Hippocampal–ventral striatal circuit** — the direct anatomical projection (subiculum → VS) is the proposed substrate through which HC orchestrates VS reactivation; the directionality of this projection is consistent with the observed HC→VS firing order in replay.

---

### Mechanistic insight

This paper meets both criteria: it formalises the HC-leads-VS replay algorithm and supports it with multi-site neural recordings (tetrode electrophysiology in rats).

- **Computational**: The brain needs to associate spatial locations (encoded by HC) with reward outcomes (encoded by VS) across time, so that future behavior can be directed toward rewarded locations. Memory consolidation of these associations requires offline reprocessing.
- **Algorithmic**: During QW-SWS, HC sharp wave-ripples trigger sequential reactivation of HC place-cell ensembles, which in turn drive coordinated reactivation of VS reward-related units. The sequence is replayed in forward order at ~10x compression. The HC→VS firing order is preserved from behavior, ensuring that place representations precede reward representations during replay — a temporal structure suitable for Hebbian/STDP strengthening of HC→VS synapses encoding the association.
- **Implementational**: The HC→VS projection (via subiculum) provides the anatomical substrate. Sharp wave-ripple complexes (detected as 100–300 Hz oscillations in CA1 pyramidal layer LFP) index the reactivation windows. Theta-rhythm entrainment of both HC and VS cells during encoding predicts which pairs will later reactivate strongly, suggesting that theta-based synchrony during encoding establishes the synaptic weights that support subsequent coordinated replay.

**Bonus**: the paper identifies theta-phase modulation during encoding as a significant (though, in multilinear regression, secondary) determinant of subsequent reactivation — pointing toward a specific neuromodulatory/oscillatory implementation mechanism for gating the encoding of associations that will later be replayed.

---

### Limitations & open questions

- **Causality**: The paper explicitly acknowledges that a causal role of ensemble reactivation in memory consolidation remains unproven; the correlation between replay and consolidation does not establish that replay is necessary or sufficient.
- **Small n**: Only four rats were used, which limits statistical power and generalisability.
- **REM sleep**: Reactivation was absent during REM sleep; the authors acknowledge this could reflect genuine specificity to SWS or be a consequence of short REM duration or variability across sessions, which they attempt to control for but cannot fully exclude.
- **Core vs. shell**: Recordings spanned both nucleus accumbens core (58%) and shell (42%); no gross differences were found, but the study was not powered to detect functional dissociations between subregions.
- **Non-overlapping place fields**: 29.8% of reactivating pairs had non-overlapping firing fields on the track, meaning that replay can link spatially remote HC activity to VS reward responses — the mechanisms governing how these distal associations are formed and replayed remain unclear.
- **Theta modulation**: Theta modulation was not a significant independent predictor in multilinear regression once behavioral correlates and firing order were controlled, leaving its mechanistic role in enabling cross-structural reactivation unclear.
- **STDP assumption**: The argument that 10-fold compression enables STDP is theoretical; direct evidence for synaptic weight changes at HC→VS synapses driven by replay is not provided.

---

### Connections & keywords

- **Key citations**: Wilson & McNaughton 1994 (hippocampal reactivation during sleep); Skaggs & McNaughton 1996 (forward replay in HC); Lee & Wilson 2002 (sequential replay in SWS); Pennartz et al. 2004 (VS reactivation and hippocampal ripples); Lansink et al. 2008 (preferential VS reactivation of motivationally relevant information); Hoffman & McNaughton 2002 (coordinated reactivation in primate neocortex); Ji & Wilson 2007 (coordinated HC-visual cortex replay); Buzsaki 1989 (two-stage model); McClelland et al. 1995 (complementary learning systems); Marr 1971 (simple memory theory); Schultz et al. 1997 (neural substrate of prediction and reward); Sutton & Barto 1998 (reinforcement learning).
- **Named models or frameworks**: Two-stage model of memory consolidation (Buzsaki 1989); complementary learning systems theory (McClelland et al. 1995); explained variance (EV) reactivation method; temporal bias method (Skaggs & McNaughton 1996); spike timing-dependent plasticity (STDP).
- **Brain regions**: hippocampus (CA1), ventral striatum (nucleus accumbens core and shell), subiculum (anatomical substrate of HC→VS projection).
- **Keywords**: sleep replay, memory consolidation, place cells, reward-related neurons, hippocampal-striatal reactivation, sharp wave-ripples, theta oscillations, temporal compression, forward replay, spike timing-dependent plasticity, explained variance method, cross-structural reactivation.
