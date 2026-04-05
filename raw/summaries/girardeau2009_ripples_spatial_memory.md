---
source_file: girardeau2009_ripples_spatial_memory.md
title: "Selective suppression of hippocampal ripples impairs spatial memory"
authors: Gabrielle Girardeau, Karim Benchenane, Sidney I Wiener, György Buzsáki, Michaël B Zugaro
year: 2009
journal: Nature Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Selective real-time elimination of hippocampal sharp wave–ripple (SPW-R) complexes during post-training sleep causally impairs spatial reference memory consolidation in rats.

---

### Background & motivation

Memory consolidation is thought to involve reactivation of waking experiences during post-learning rest and sleep, with hippocampal sharp wave–ripple (SPW-R) complexes proposed as the key mechanism for transferring labile memories from the hippocampus to the neocortex. Prior to this work, all evidence linking SPW-Rs to memory consolidation was correlative — studies showed SPW-Rs co-occur with replay of place-cell sequences, but no study had demonstrated a causal necessity. This paper addresses that gap by asking whether eliminating SPW-Rs during the consolidation window directly impairs subsequent memory performance.

---

### Methods

- **Subjects**: 26 adult rats in three groups — test (n=7, online ripple suppression), stimulated control (n=7, yoked stimulation with 80–120 ms delay), unimplanted control (n=12, no surgery).
- **Task**: Spatial reference memory task on an eight-arm radial maze; the same three arms baited daily; three trials per day over 15 days.
- **Intervention**: Online detection of SPW-Rs via real-time ripple-band filtering and threshold detection; threshold crossing triggered single-pulse stimulation of the ventral hippocampal commissure, which interrupted the ongoing ripple and transiently silenced hippocampal spiking (~86% of offline-detected SPW-Rs suppressed online).
- **Controls**: Stimulated controls received the same number of pulses but with a random 80–120 ms delay, ensuring stimulations fell outside ripple episodes and hippocampal ripples remained intact.
- **Rest period**: SPW-Rs suppressed for 1 h immediately following each training session.
- **Key measurements**: Behavioral performance index on the radial maze; LFP recordings; unit activity in hippocampus and neocortex (anterior cingulate, prelimbic/infralimbic prefrontal cortex); sleep architecture (REM/SWS ratio); ripple incidence.
- **Analysis**: Two-factor ANOVA (day × group) for behavioral comparisons; t-tests for pairwise comparisons; cross-correlograms of stimulations and offline-detected SPW-Rs to verify suppression.

---

### Key findings

- Online commissural stimulation suppressed ~86% of all SPW-Rs and transiently silenced hippocampal (but not neocortical) spiking activity.
- Sleep architecture (REM/SWS ratio) was not significantly altered by SPW-R suppression, ruling out a nonspecific sleep disruption confound.
- Test rats (ripple-suppressed) showed significant performance impairment relative to both control groups (two-factor ANOVA, p < 0.001 for main factors, p < 0.01 for interaction).
- Control rats exceeded upper chance performance after ~5 days; test rats continued at chance until day 8 (t-test, p < 0.05).
- Stimulated controls did not differ from unimplanted controls (two-factor ANOVA, p > 0.05), confirming the effect was specific to ripple suppression, not stimulation per se.
- Test rats did not adopt stereotyped turning strategies, and working memory errors were low (<1 per trial on average) in all groups.
- The magnitude of impairment was comparable to that seen in hippocampus-lesioned rats in a prior study.

---

### Computational framework

Not applicable in the sense of a formal computational model. However, the paper's interpretive framework invokes spike timing–dependent plasticity (STDP) and NMDA receptor-dependent synaptic reinforcement: the proposal is that SPW-Rs temporally compress hippocampal replay sequences into a window compatible with NMDA activation and STDP induction, thereby enabling synaptic consolidation. The results constrain models of systems consolidation in which timed hippocampal output — rather than slow global oscillations alone — is the critical trigger for neocortical plasticity.

---

### Prevailing model of the system under study

Prior to this paper, the dominant view held that memory consolidation during sleep involves hippocampal reactivation of waking activity patterns, coordinated by SPW-R events that temporally compress place-cell replay sequences and facilitate information transfer to the neocortex (Buzsáki, 1989; Wilson & McNaughton, 1994; Kudrimoti et al., 1999). SPW-Rs were thought to be coordinated with neocortical slow oscillations and sleep spindles, enabling widespread cortical consolidation. However, all evidence was correlative: SPW-Rs and memory performance co-varied, but it was unknown whether SPW-Rs were causally necessary or merely epiphenomenal to the consolidation process.

---

### What this paper contributes

This paper establishes the first causal evidence that hippocampal SPW-Rs are necessary for spatial memory consolidation. By eliminating SPW-Rs in real time during the post-training window — while leaving sleep architecture and neocortical activity intact — the authors show that suppressing ripples is sufficient to produce a robust memory deficit. This rules out the main alternative interpretations (nonspecific stimulation effects, sleep disruption) and elevates SPW-Rs from correlate to causal mechanism. The finding narrows the consolidation window to the period of hippocampal ripple activity occurring in the first ~1 hour post-training, consistent with the known temporal distribution of replay.

---

### Brain regions & systems

- **Hippocampus** — primary locus of SPW-R generation and replay; site of intervention; the region whose output is causally necessary for consolidation.
- **Ventral hippocampal commissure** — stimulation target; used to interrupt hippocampal SPW-Rs and silence pyramidal cell activity.
- **Anterior cingulate cortex** — monitored as a candidate site of hippocampal-neocortical transfer; neocortical firing was unaffected by stimulation at the intensities used.
- **Prelimbic/infralimbic prefrontal cortex** — similarly monitored; activity unaffected, confirming selectivity of the hippocampal intervention.
- **Neocortex (general)** — proposed downstream target of hippocampal replay output during systems consolidation; not directly disrupted in this study.

---

### Mechanistic insight

This paper meets both criteria for the high bar.

1. It formalises an algorithmic proposal: SPW-R-associated temporal compression of hippocampal replay sequences enables spike timing-dependent plasticity and NMDA-mediated synaptic reinforcement within and downstream of the hippocampus.
2. It provides causal neural intervention data — real-time LFP-triggered commissural stimulation — that specifically links SPW-R elimination to memory failure, while controlling for nonspecific stimulation effects and sleep disruption.

**Computational level**: The brain must stabilise recently encoded spatial memories by transferring or reinforcing neural representations during offline periods.

**Algorithmic level**: Reactivation of waking place-cell sequences, compressed within SPW-R events, produces spike timing patterns compatible with Hebbian (NMDA/STDP) plasticity; this reactivation must occur in the hippocampus and be transmitted to neocortical targets.

**Implementational level**: SPW-R generation in hippocampal CA3-CA1 circuitry, commissural connectivity enabling bilateral synchrony, and coordination with neocortical slow oscillations and sleep spindles (cited but not directly manipulated here). The paper does not identify specific cell types or molecular mechanisms beyond noting NMDA and STDP as candidate substrates.

**Bonus**: The intervention is at the level of a specific oscillatory event in a defined circuit (hippocampal commissure), providing circuit-level implementation detail, though intracellular or cell-type-specific mechanisms are not resolved.

---

### Limitations & open questions

- Only ~86% of SPW-Rs were suppressed online; the remaining ~14% and ripples occurring after the 1-hour window may partially account for the residual (slow) learning seen in test rats.
- The study does not track what happens to neocortical representations — it is inferred, but not shown, that the deficit reflects failure of hippocampal-to-neocortical transfer specifically.
- The mechanism by which commissural stimulation suppresses ripples (inhibitory interneuron recruitment vs. direct desynchronisation) is not characterised in detail.
- It is unclear whether SPW-Rs are required for initial encoding, consolidation, or both; the design targets only the post-training window, but online suppression during behaviour was not attempted.
- The study uses a spatial reference memory paradigm; generalisability to other memory types (episodic, non-spatial) is not addressed.
- The paper does not examine whether the deficit is permanent or whether extended training would eventually rescue performance.

---

### Connections & keywords

**Key citations**:
- Buzsáki, G. (1989) *Neuroscience* 31:551–570 — foundational SPW-R consolidation framework
- Wilson & McNaughton (1994) *Science* — hippocampal replay during sleep
- Kudrimoti, Barnes & McNaughton (1999) *J. Neurosci.* — reactivation of place-cell ensembles during SPW-Rs
- Zugaro, Monconduit & Buzsáki (2005) *Nat. Neurosci.* — commissural stimulation method
- Jarrard (1995) *Behav. Brain Res.* — hippocampal lesion effect on radial maze performance (benchmark comparison)
- Sirota et al. (2003) *PNAS* — hippocampal SPW-Rs coordinated with neocortical oscillations
- Siapas & Wilson (1998) *Neuron* — hippocampal-neocortical coupling during sleep
- Peyrache et al. (2009) *Nat. Neurosci.* — prefrontal replay coordinated with hippocampal SPW-Rs

**Named models or frameworks**:
- Sharp wave–ripple (SPW-R) consolidation model (Buzsáki 1989)
- Spike timing–dependent plasticity (STDP)
- Systems consolidation (hippocampal-to-neocortical transfer)
- Two-stage memory model

**Brain regions**:
- Hippocampus
- Ventral hippocampal commissure
- Anterior cingulate cortex
- Prelimbic/infralimbic prefrontal cortex
- Neocortex

**Keywords**:
- sharp wave–ripple complexes
- memory consolidation
- hippocampal replay
- spatial reference memory
- radial arm maze
- online closed-loop neural stimulation
- sleep-dependent consolidation
- place cells
- hippocampal-neocortical transfer
- spike timing–dependent plasticity
- causal intervention
- post-training sleep
