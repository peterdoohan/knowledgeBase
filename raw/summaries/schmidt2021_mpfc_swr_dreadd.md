---
source_file: schmidt2021_mpfc_swr_dreadd.md
title: Disrupting the medial prefrontal cortex with designer receptors exclusively activated by designer drug alters hippocampal sharp-wave ripples and their associated cognitive processes
authors: Brandy Schmidt, A. David Redish
year: 2021
journal: Hippocampus
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Disrupting the medial prefrontal cortex (mPFC) with inhibitory DREADDs impairs post-learning hippocampal sharp-wave ripple (SWR) rates and alters the content of awake SWRs during decision-making, revealing a causal role for mPFC in modulating hippocampal consolidation and planning processes.

### Background & motivation

The hippocampus and medial prefrontal cortex (mPFC) interact during memory consolidation and decision-making, but the nature of this interaction remains unclear. Sharp-wave ripples (SWRs) are high-frequency oscillations in the hippocampus that occur during rest and support memory consolidation. Recent evidence suggests the mPFC may influence hippocampal physiology more than previously recognized, potentially controlling SWR recruitment during planning. This study tests whether disrupting mPFC activity causally affects hippocampal SWRs and their associated cognitive functions.

### Methods

- **Subjects**: 7 male Brown-Norway rats (10-14 months old)
- **Surgery**: mPFC transfected with mCherry-tagged AAV8-CaMKIIa-hM4Di (inhibitory DREADDs) bilaterally in prelimbic cortex
- **Task**: Restaurant Row - a neuroeconomic foraging task where rats make serial stay/skip decisions for different flavored rewards with varying delays (1-30s)
- **4x20 task variant**: 8 days of testing with 4 daily 20-min epochs where one restaurant dispensed 3 pellets and others dispensed 1 pellet
- **Recording**: LFP and neuronal ensembles from hippocampus (CA1) recorded during pre-maze rest (5 min), on-maze behavior, and post-maze rest (5 min)
- **Injection sequence**: 20-day matched-pair design with CNO (5 mg/kg) or vehicle (VEH) in pseudorandomized order, experimenter blind to condition
- **SWR detection**: Bandpass filtered 180-220 Hz, events >1 SD above mean power, speed <5 cm/s, theta/delta ratio <1 SD above mean
- **Bayesian decoding**: One-step decoding to determine spatial representations during SWRs (40 ms time windows, 64 spatial bins)
- **Behavioral measures**: Delay thresholds (subjective value), rate of reinforcement, vicarious trial-and-error (VTE), lingering time, hesitation time

### Key findings

- **mPFC disruption impaired post-learning SWR rates**: SWR rates increased from pre-maze to post-maze rest (replicating prior findings), but this increase was significantly reduced on CNO days compared to VEH days (RM-ANOVA: main effect of Condition F(1,49)=8.36, p=.0057; Condition x Epoch interaction F(1,49)=10.9, p=.0018)
- **On-maze SWRs were unaffected by mPFC disruption**: SWR rates during Waiting (anticipatory) and Lingering (post-reward) epochs on the maze showed no effect of CNO (no main effect of Condition F(1,49)=1.62, p=.21), suggesting mPFC specifically modulates consolidation-related SWRs
- **Waiting vs. Lingering SWRs differ in content**: Waiting SWRs showed more non-local decoding (particularly to Next restaurant) suggesting planning, while Lingering SWRs decoded more locally to Current restaurant (RM-ANOVA Restaurant x Epoch interaction: F(3,66)=25.18, p=5e-11)
- **mPFC disruption altered SWR content**: On CNO days, Waiting epoch SWRs showed increased non-local decoding compared to VEH, with reduced differentiation between Current and other restaurants
- **SWR rates tracked flavor preferences during Waiting**: SWR rates were lowest at Least preferred and highest at Most preferred restaurants (RM-ANOVA main effect of Rank F(3,147)=15.98, p=4.8e-9); this relationship was reduced by mPFC disruption
- **SWR rates tracked trial value**: Waiting SWR rates increased with trial value (Good deals > Difficult > Bad deals; F(2,96)=93.25, p<3e-23); Good deal SWR rates trended toward reduction on CNO days
- **4x20 task novelty increased SWR rates**: SWR rates increased on the novel 4x20 task compared to overtrained Restaurant Row (main effect of Task F(1,261)=4.6, p=.033), primarily driven by pre-maze rest increases
- **Memory of reward value carried across sub-sessions**: Waiting SWR rates were higher for restaurants that previously dispensed 3 pellets but now dispensed 1, compared to restaurants that always dispensed 1 pellet (VEH: t(33)=-4.79, p=3.4e-5); this suggests SWRs track remembered expected value
- **mPFC disruption impaired anticipation of reward size**: On VEH days, rats waited longer for 3-pellet vs 1-pellet rewards (t(74)=-2.97, p=.004), but this difference was absent on CNO days (p=.17), suggesting mPFC is necessary for using remembered reward size to guide decisions

### Computational framework

Not applicable. This is an empirical study using causal manipulation (DREADDs) to test the functional role of mPFC-hippocampal interactions. However, the results constrain computational frameworks of hippocampal-prefrontal communication, particularly models proposing that the mPFC influences hippocampal replay and consolidation processes.

### Prevailing model of the system under study

The prevailing model holds that: (1) hippocampal SWRs during rest facilitate memory consolidation via reactivation of behaviorally relevant cell assemblies; (2) SWRs during awake behavior facilitate planning and decision-making; (3) the mPFC receives monosynaptic input from the hippocampus but sends only indirect projections back, suggesting hippocampal-to-cortical information flow dominates; (4) disrupting SWRs impairs spatial memory and decision-making. The paper challenges the unidirectional view by showing mPFC causally influences hippocampal SWR generation and content.

### What this paper contributes

This paper establishes a causal role for the mPFC in modulating hippocampal SWRs. Key contributions include: (1) demonstrating that mPFC disruption specifically impairs post-learning consolidation SWRs while sparing on-maze SWRs, suggesting distinct neural mechanisms; (2) showing that mPFC affects the content of planning-related SWRs (Waiting epoch), increasing non-local representations; (3) revealing that SWR rates track subjective value (flavor preferences) and trial value (good vs bad deals), and this value-coding depends on intact mPFC; (4) demonstrating that SWRs carry memory of reward value across sub-sessions, suggesting they track expected rather than received value; (5) providing evidence that mPFC is necessary for using remembered reward information to guide decisions, but not for recognizing reward value post-consumption.

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)**: Specifically prelimbic cortex. Transfected with inhibitory DREADDs (hM4Di) to enable causal manipulation. Causal role in modulating hippocampal SWR rates and content.
- **Hippocampus (dorsal CA1)**: Recorded LFPs and neuronal ensembles. Source of SWRs. Shows modulation of SWR rates by value, reward size, and behavioral epoch. SWR content differs between Waiting (planning) and Lingering (consolidation) epochs.
- **Ventral striatum**: Targeted for recording but not analyzed due to low cell yields.

### Mechanistic insight

This paper provides strong mechanistic insight at the algorithmic and implementational levels:

**Computational**: The brain must solve the problem of balancing memory consolidation with ongoing decision-making. The hippocampus needs to both store past experiences and use them to guide future behavior.

**Algorithmic**: The mPFC implements a gating or modulatory mechanism over hippocampal SWRs. Different behavioral contexts (rest/consolidation vs. active decision-making) engage distinct modes of mPFC-hippocampal interaction. SWRs during Waiting epochs show non-local representations (Next > Previous) consistent with planning, while Lingering SWRs show local representations consistent with consolidation. The mPFC disruption specifically: (1) reduces consolidation SWR rates, (2) increases non-local decoding in planning SWRs, (3) impairs the relationship between SWR rates and subjective value.

**Implementational**: The mPFC sends indirect projections to the hippocampus (via thalamus/nucleus reuniens) that can modulate CA1 SWR generation. Inhibitory DREADDs in prelimbic cortex reduce this modulatory input, impairing the normal increase in post-learning SWRs. The cell-type specific expression (CaMKIIα promoter targeting excitatory neurons) suggests the effect is through modulating pyramidal neuron output from mPFC.

### Limitations & open questions

- No CNO-only control group (non-DREADD transfected rats) to rule out potential non-specific CNO effects, though the differential effects on different SWR types argues against global confounds
- Low cell yields in mPFC and ventral striatum prevented analysis of single-unit activity in mPFC during SWRs
- The mechanism by which mPFC influences hippocampal SWRs remains unclear (direct vs. indirect pathways)
- Whether the effects on SWR content represent impaired planning or altered memory retrieval is not fully dissociated
- The causal role of SWRs in the behavioral effects of mPFC disruption was not directly tested (correlational only)
- Long-term effects of chronic mPFC disruption on memory consolidation were not assessed

### Connections & keywords

**Key citations**: Ego-Stengel & Wilson (2010); Girardeau et al. (2009); Jadhav et al. (2012); Foster & Wilson (2006); Karlsson & Frank (2008); Buzsáki (2015); Pfeiffer & Foster (2013); Shin et al. (2019); Steiner & Redish (2014); Schmidt et al. (2019)

**Named models or frameworks**: Sharp-wave ripples (SWRs), Restaurant Row task, 4×20 task, DREADDs (designer receptors exclusively activated by designer drugs), Bayesian decoding of spatial representations, vicarious trial-and-error (VTE)

**Brain regions**: medial prefrontal cortex (mPFC), prelimbic cortex, hippocampus (CA1), dorsal hippocampus, ventral striatum (not analyzed)

**Keywords**: sharp-wave ripples, SWRs, medial prefrontal cortex, DREADDs, memory consolidation, decision-making, hippocampus, neuroeconomics, Restaurant Row, spatial navigation, replay, Bayesian decoding, value-based choice, reward anticipation
