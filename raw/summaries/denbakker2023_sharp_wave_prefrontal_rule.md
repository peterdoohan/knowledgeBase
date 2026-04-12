---
source_file: denbakker2023_sharp_wave_prefrontal_rule.md
paper_id: denbakker2023_sharp_wave_prefrontal_rule
title: "Sharp-wave-ripple-associated activity in the medial prefrontal cortex supports spatial rule switching"
authors:
  - "Hanna den Bakker"
  - "Marie Van Dijck"
  - "Jyh-Jang Sun"
  - "Fabian Kloosterman"
year: 2023
journal: "Cell Reports"
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - optogenetics
  - tetrode_recording
  - behavioral_analysis
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - anterior_cingulate_cortex
  - prelimbic_cortex
  - infralimbic_cortex
  - thalamus
keywords:
  - sharp_wave_ripples_swrs
  - hippocampal_prefrontal_interaction
  - spatial_rule_switching
  - closed_loop_optogenetics
  - archt_inhibition
  - perseverative_behavior
  - spatial_alternation_task
  - memory_consolidation_timing
  - cognitive_flexibility
  - hippocampal_replay
  - awake_reactivation
  - two_stage_memory_model
  - sharp
  - wave
  - ripple
  - associated
  - activity
  - medial
  - prefrontal
  - cortex
key_citations:
  - buzsaki2015_hippocampal_sharp_wave_ripple
  - fernandez2019_ripples_memory_consolidation
  - girardeau2009_ripples_spatial_memory
  - jadhav2016_hippocampal_prefrontal_swr
  - foster2021_cortico_basal_ganglia
---

### One-line summary

Optogenetic inhibition of the medial prefrontal cortex timed specifically to hippocampal sharp-wave ripples (but not with a 400–450 ms delay) impairs spatial rule switching in rats, providing direct causal evidence that mPFC activity in the ~200 ms following SWR onset is necessary for updating behavioral strategy.

---

### Background & motivation

The hippocampus and medial prefrontal cortex (mPFC) are both implicated in spatial learning, but the precise temporal relationship that makes their interaction functionally critical was unknown. Hippocampal sharp-wave ripples (SWRs) modulate mPFC firing, and disrupting SWRs generally impairs spatial alternation learning, yet no prior study had tested whether the mPFC activity specifically in the window immediately after SWR onset — rather than mPFC activity at other times — is what matters. This paper addresses that gap by delivering closed-loop optogenetic inhibition either on-time (directly following SWR detection) or with a randomized delay, within the same animals.

---

### Methods

- **Subjects**: 11 adult male Long-Evans rats
- **Task**: Three-arm radial maze spatial alternation. Animals learned to alternate between two arms, then underwent rule switches (new arm configuration); performance measured over 15-min learning blocks for up to 8 blocks per day
- **Recordings**: Tetrodes in dorsal hippocampal CA1 for online SWR detection (Falcon real-time software); SWRs detected online with ~40 ms latency, 79–80% sensitivity vs. offline algorithm
- **Optogenetics**: AAV-CamKII-ArchT-GFP injected bilaterally in mPFC; 595 nm LED illumination delivered via tapered optical fibers (2.5 mm active length) spanning anterior cingulate, prelimbic, and infralimbic cortex
- **Experimental design**: Within-animal crossover — on the first day of each rule switch, mPFC was inhibited either on-time (immediately post-SWR, 200 ms duration) or with a 400–450 ms delay (same 200 ms duration); inhibition applied both during maze exploration and rest periods between blocks
- **Behavioral analysis**: Percent correct arm visits, percent correct 4-visit alternation sequences, and detailed error-pattern analysis (back-and-forth, circling, old-rule perseveration); VTE/pausing behavior also assessed
- **Control**: Showed that total LED-on time did not correlate with performance, ruling out a non-specific illumination confound

---

### Key findings

- On-time mPFC inhibition significantly reduced correct alternation performance across all learning blocks vs. delayed inhibition (57.7% vs. 75.7% correct arm visits; t(10) = 3.13, p = 0.011)
- The deficit was present already in the first learning block (before any rest-period inhibitions), indicating an on-maze effect (43.1% vs. 58.4%; t(10) = 2.29, p = 0.045)
- Correct 4-visit alternation sequence performance was also significantly impaired both in the first block (6.7% vs. 24.8%; p = 0.010) and across all blocks (21.5% vs. 55.2%; p = 0.002)
- On-time inhibition caused significantly more circling (perseverative sequential arm visits) across all blocks (25.8% vs. 11.0%; p = 0.017); back-and-forth behavior was unaffected
- Animals in the on-time condition were biased toward the old rule in the first learning block (rule bias −30.9 vs. +10.3 in delayed condition; p = 0.001) and took much longer to switch to the new rule
- VTE/pausing behavior (turning around, lingering, head movements) did not differ between conditions, indicating the deficit is specific to strategic updating rather than general decision deliberation
- Total illumination time was higher in the on-time condition but did not correlate with behavioral performance, ruling out duration as the causal factor

---

### Computational framework

Not applicable in the strict sense — the paper uses no formal computational model. However, the results directly bear on the two-stage model of memory consolidation (Buzsaki, 2015), in which hippocampal SWRs reactivate experience-relevant information and relay it to neocortex. The implicit framework is one of temporal credit assignment: the mPFC must receive and integrate hippocampal input within a specific post-SWR time window to update the current behavioral policy. The key variables are (1) SWR occurrence as a trigger, (2) a ~200 ms temporal window of hippocampal-to-prefrontal information transfer, and (3) mPFC activity within that window as necessary for rule-updating. The paper does not formalise this as a computational model but provides the causal evidence that constrains such models.

---

### Prevailing model of the system under study

The field's working model, as laid out in the paper's introduction, holds that the hippocampus provides memory and spatial map information, while the mPFC guides executive function — particularly the suppression of old strategies and adoption of new ones during rule changes. Hippocampal SWRs were already known to be important for spatial alternation learning (disrupting SWRs slows acquisition; prolonging them improves performance), and SWRs were known to modulate mPFC firing within ~200 ms of SWR onset. However, the causal link was indirect: prior work showed that mPFC inactivation causes perseveration and impairs reversal learning, and that hippocampal–mPFC interactions matter for spatial flexibility, but no study had specifically tested whether mPFC activity timed to SWRs — as opposed to mPFC activity at other times — is the functionally critical element.

---

### What this paper contributes

The paper establishes the first direct causal evidence that the mPFC activity specifically in the ~200 ms post-SWR window is necessary for spatial rule switching. The use of a within-animal, same-duration delayed control condition rules out total inhibition time as a confound and isolates timing as the critical variable. We can now say, not merely speculate, that the hippocampal-to-prefrontal dialogue occurs at SWR-locked moments and that this precisely timed interaction — rather than mPFC function in general — drives the animal's ability to abandon a learned strategy and adopt a new one. The finding also clarifies the nature of mPFC-dependent perseveration: it is driven by the failure to process SWR-transmitted feedback, not by impairments to general deliberative behaviour (VTE was unaffected).

---

### Brain regions & systems

- **Dorsal hippocampal CA1** — site of SWR recording and detection; SWRs here serve as the trigger event for the interaction
- **Medial prefrontal cortex (mPFC)** — site of optogenetic inhibition; encompasses anterior cingulate cortex, prelimbic cortex, and infralimbic cortex; necessary for updating spatial strategy following rule switches; inhibited uniformly across subregions (subregion dissociation not addressed)
- **Nucleus reuniens (thalamus)** — discussed as a candidate mediator of indirect hippocampal–mPFC communication; not directly manipulated but noted as a potential confound/alternative pathway
- **Ventral vs. dorsal hippocampus** — distinguished in the discussion; dorsal SWRs are modulated by novelty and reward while ventral SWRs are not; their separate contributions were not tested in this study

---

### Mechanistic insight

This paper meets the bar.

**Phenomenon**: Rats fail to switch from a previously rewarded spatial alternation rule to a new one when mPFC activity is suppressed immediately (but not 400 ms) after hippocampal SWRs.

**Computational level**: The brain solves the problem of updating a behavioral policy in response to changing reward contingencies. This requires distinguishing current negative feedback (the old rule no longer works) from previously learned associations, and redirecting behaviour accordingly.

**Algorithmic level**: The proposed algorithm is a two-stage communication process: during SWRs, hippocampal assemblies reactivate reward-related spatial information and transmit it to the mPFC; the mPFC then integrates this feedback signal within a ~200 ms window to update its representation of the current rule and suppress the previous one. The timing of inhibition is the key variable — the same total amount of mPFC suppression has no effect if it occurs 400–450 ms after SWR onset, implying that the relevant computation completes within that window.

**Implementational level**: The inhibition targeted CamKII-expressing (excitatory) neurons across the full mPFC depth using ArchT. The paper does not resolve which specific cell types, laminar positions, or synaptic inputs are responsible. The authors note that direct monosynaptic projections from ventral hippocampus to prelimbic/infralimbic cortex and from dorsal hippocampus to prelimbic cortex are candidate anatomical substrates, and they suggest that future experiments should target hippocampal axon terminals in mPFC following SWR onset to test the direct pathway specifically.

**Bonus**: The paper identifies SWR rate as a downstream consequence of mPFC disruption — on-time inhibition led to significantly more subsequent SWR detections than delayed inhibition, suggesting a feedback loop in which failed prefrontal processing increases hippocampal reactivation events.

---

### Limitations & open questions

- Inhibition was applied across all mPFC subregions simultaneously; the contributions of anterior cingulate, prelimbic, and infralimbic cortex could not be dissociated
- SWRs during maze learning vs. rest periods were not separated; only the first-block result hints at the primacy of on-maze SWRs
- Online SWR detection had lower specificity than the offline algorithm (non-match rate ~48–58%), meaning many inhibitions were triggered by non-SWR events; this is the same in both conditions but reduces the precision of the causal claim
- A 200-ms post-detection lockout was applied in delayed but not on-time condition, leading to higher SWR detection rates in the on-time condition; the authors argue this does not explain the behavioral results (no correlation between LED-on time and performance)
- The paper does not record single-unit mPFC activity, so it cannot show what information is represented in mPFC during post-SWR windows, nor confirm that inhibition is complete
- No hippocampal place cell/replay data were collected, so whether the mPFC disruption affects hippocampal replay content (an alternative mechanism) cannot be assessed
- Dorsal vs. ventral hippocampal SWR contributions were not dissociated; their downstream targets differ substantially
- Generalization beyond spatial alternation (to other forms of cognitive flexibility) is unknown

---

### Connections & keywords

**Key citations**:
- Buzsaki (2015) — two-stage memory consolidation model; hippocampal SWRs as cognitive biomarker
- Jadhav et al. (2012) — awake SWR disruption impairs spatial memory (Science)
- Fernandez-Ruiz et al. (2019) — prolonged SWRs improve spatial memory (Science)
- Girardeau et al. (2009) — selective SWR suppression impairs spatial memory
- Jadhav et al. (2016) — coordinated excitation/inhibition of prefrontal ensembles during awake SWRs
- Shin, Tang & Jadhav (2019) — hippocampal-prefrontal replay during learning and decision making
- Berners-Lee, Wu & Foster (2021) — mPFC neurons selective for non-local hippocampal representations during replay
- Rich & Shapiro (2009) — rat mPFC neurons code strategy switches
- Spellman et al. (2015) — ventral hippocampal input to mPFC supports spatial working memory encoding
- Park et al. (2021) — reset of hippocampal-prefrontal circuitry facilitates learning

**Named models or frameworks**:
- Two-stage model of memory consolidation (Buzsaki)
- Closed-loop optogenetic inhibition (SWR-triggered real-time manipulation)
- Falcon real-time closed-loop software (Ciliberti & Kloosterman 2017)

**Brain regions**:
- Medial prefrontal cortex (mPFC): anterior cingulate cortex, prelimbic cortex, infralimbic cortex
- Dorsal hippocampal CA1
- Nucleus reuniens (thalamus)
- Ventral hippocampus (discussed)

**Keywords**:
- sharp-wave ripples (SWRs)
- hippocampal-prefrontal interaction
- spatial rule switching
- closed-loop optogenetics
- ArchT inhibition
- perseverative behavior
- spatial alternation task
- memory consolidation timing
- cognitive flexibility
- hippocampal replay
- awake reactivation
- two-stage memory model
