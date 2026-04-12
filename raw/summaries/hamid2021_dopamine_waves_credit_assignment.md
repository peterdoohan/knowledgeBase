---
source_file: hamid2021_dopamine_waves_credit_assignment.md
paper_id: hamid2021_dopamine_waves_credit_assignment
title: "Wave-like dopamine dynamics as a mechanism for spatiotemporal credit assignment"
authors:
  - "Arif A. Hamid"
  - "Michael J. Frank"
  - "Christopher I. Moore"
year: 2021
journal: Cell
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - calcium_imaging
  - computational_modeling
brain_regions:
  - striatum
  - dorsomedial_striatum
  - dorsolateral_striatum
  - ventral_tegmental_area
  - substantia_nigra
frameworks:
  - reinforcement_learning
  - temporal_difference_learning
keywords:
  - dopamine_spatiotemporal_waves
  - credit_assignment
  - striatal_subregion_specialisation
  - reward_prediction_error
  - instrumental_vs_pavlovian_learning
  - agency_inference
  - mixture_of_experts_reinforcement_learning
  - eligibility_traces
  - widefield_dopamine_imaging
  - dlight_gcamp6f
  - anticipatory_dopamine_ramps
  - corticostriatal_plasticity
  - wave
  - like
  - dopamine
  - dynamics
  - mechanism
  - spatiotemporal
  - credit
  - assignment
key_citations:
  - schultz1997_neural_substrate_reward_pred
  - montague1996_predictive_hebbian_dopamine
---

### One-line summary

Dopamine signals across the dorsal striatum propagate as spatiotemporal waves whose direction is determined by inferred instrumental agency, providing a mechanism to selectively assign reward credit to functionally specialised striatal subregions.

---

### Background & motivation

The dominant reward prediction error (RPE) hypothesis treats dopamine as a global, scalar signal broadcast uniformly to all striatal targets. However, the dorsal striatum is organised into functionally distinct subregions — dorsomedial (DMS) for goal-directed, action-outcome learning and dorsolateral (DLS) for stimulus-response habits — and theoretical models of hierarchical reinforcement learning predict that credit assignment should be preferentially directed to the subregion responsible for producing a given outcome. Whether striatal dopamine is actually differentiated in this way, and by what organisational principle, was unknown prior to this paper.

---

### Methods

- **Species and preparation**: Head-fixed DAT-cre mice expressing cre-dependent GCaMP6f in midbrain dopamine axons, or injected with the dopamine sensor dLight in the dorsal striatum; chronic ~7 mm² widefield imaging window over dorsal striatum providing 60–80% coverage.
- **Sensors**: Calcium indicator GCaMP6f (dopamine axon activation), dLight (extracellular dopamine release), jRGECO1a (red-shifted calcium indicator for dual-colour experiments), and tdTomato as an inert fluorophore control.
- **Spatial characterisation**: Optic flow algorithms applied to widefield fluorescence frames to extract vector fields, source/sink maps, wave velocity, inter-wave interval, and direction distributions.
- **Tasks**: (1) Instrumental task — escalating tones contingent on wheel running, variable distance per trial (50–150 cm); (2) Pavlovian task — same tones advanced by elapsed time independent of running (4–8 s); (3) Serial reversal task — alternating instrumental and Pavlovian blocks (25–35 trials each) within a single session to test dynamic switching of DA wave direction.
- **Two-photon imaging**: Used to characterise individual dopamine axon segment responses to tone transitions at micrometre resolution.
- **Computational modelling**: (a) Temporal difference (TD) RL simulations with spatially delayed rewards to show that ML wave-induced timing lags produce asymmetric credit assignment; (b) Hierarchical mixture-of-experts (MoE) RL model with a DMS-like "distance expert" accumulating evidence for agency via sub-experts specialised for distinct distance contingencies.
- **Statistical analysis**: ANOVAs, Wilcoxon tests, circular statistics (Omnibus test), and history-dependent regression of wave angle on next-trial running speed.

---

### Key findings

- DA axon activity and dopamine release propagate as spatiotemporal waves across the dorsal striatum, with a strong bias along the mediolateral axis; local correlations decay with distance (two-way ANOVA: F(1,7) = 82.3, p = 4.0×10⁻⁵ for GCaMP6f mice).
- Three canonical wave motifs account for 93 ± 3% of DA transients: centre-out (CO), lateromedial (LM), and mediolateral (ML) waves; each produces distinct relative timing of DA across DMS and DLS.
- Reward delivery in the **instrumental** task triggers ML waves (DMS peaks significantly before DLS; p = 0.031, Wilcoxon); reward in the **Pavlovian** task triggers opponent LM waves (DMS peaks later; p = 0.007, Wilcoxon).
- Opponent wave directions reverse rapidly after within-session contingency reversals (within ~5 trials) and are not explained by differences in running velocity (task × velocity interaction, F(5,70) = 3.81, p = 0.004).
- Spurious locomotion–sensory congruence in Pavlovian trials drives ML-type waves, indicating that wave direction tracks evidence for agency rather than task label per se.
- DMS DA shows positive anticipatory ramps during instrumental trials and negative ramps during Pavlovian trials (effect of task type, p = 10⁻⁶); ramp slopes reverse within sessions after block change (GCaMP6f: p = 0.004; dLight: p = 0.04).
- DMS ramp slope inversely predicts the latency to reward-induced DA peak (p = 0.03 instrumental; p = 0.007 Pavlovian), linking eligibility tagging to credit magnitude.
- Reward wave direction and ramp slope predict next-trial running speed in a history-dependent manner (r = 0.2, p = 0.002 instrumental; r = 0.43, p < 10⁻⁵ Pavlovian); regression coefficients are largest for the most recent trial (history-dependent; Spearman r = 0.34, p = 0.007, model R² = 0.44).
- Within DMS, contiguous sub-territories show steepest DA ramps preferentially for trials with their preferred distance contingency, consistent with sub-expert specialisation.
- Individual DA axon segments (two-photon) respond to single tone transitions and tile the full sequence of escalating tones; transients scale with trial length and tone position within trial, matching model-predicted sub-expert RPE (sRPE) signatures.
- TD RL simulations confirm that temporally delayed rewards to more lateral agents produce shallower value ramps and reduced credit assignment, providing an algorithmic proof of concept.

---

### Computational framework

**Reinforcement learning — temporal difference with spatiotemporal extension, and a hierarchical mixture-of-experts model.**

The paper uses two complementary formalisms:

1. **Spatiotemporal TD RL**: A bank of parallel striatal agents each receives a reward signal delayed in proportion to their lateral position. Eligibility traces allow delayed rewards to credit earlier states. DA wave-induced timing lags effectively convert a uniform reward into spatially graded RPEs, implementing "spatiotemporal difference" credit assignment.

2. **Mixture-of-experts (MoE) RL**: A three-level hierarchy. Level 1: a DMS-like "distance expert" accumulates evidence for agency by comparing the accuracy of its predictions against a "time expert." Level 2: sub-experts within DMS specialise for distinct distance contingencies; their RPEs (sRPEs) at tone/state transitions drive their responsibility weights. Level 3: sRPEs at individual state transitions update sub-expert predictions. The responsibility weight of the distance expert gates reward-wave direction (ML vs. LM), which in turn delivers differential credit and modulates future running speed.

Key variables: responsibility weights (λ), eligibility traces, value functions (V), state prediction errors at tone transitions (sRPEs), and reward prediction errors at outcome (RPEs).

---

### Prevailing model of the system under study

The paper explicitly positions itself against the "global scalar RPE" hypothesis: midbrain DA neurons fire highly synchronously in response to reward prediction errors, and the divergent axon projections broadcast this uniform signal to all striatal targets. Under this view, DA encodes a scalar RPE that is identical across DMS, DLS, and other subregions. Supporting evidence cited by the authors includes the highly divergent architecture of mesostriatal projections (Matsuda et al., 2009), the high synchrony of DA cell pairs (Hyland et al., 2002; Eshel et al., 2016), and the success of scalar RPE models in explaining behaviour and neural data (Schultz et al., 1997; Montague et al., 1996). The prevailing framework treats spatial heterogeneity in striatal DA as noise or an experimental artefact rather than as a functional feature.

---

### What this paper contributes

The paper refutes the global-broadcast view by demonstrating that striatal DA is spatiotemporally heterogeneous in a systematic and functionally relevant way. Specifically:

- DA propagates as directional waves rather than synchronous bursts; wave direction encodes the animal's inferred causal agency over rewards.
- Reward waves are not fixed anatomical features but are dynamically sculpted by task demands, reversing within sessions as contingencies change.
- The directionality of waves produces differential timing of DA peaks across DMS and DLS, providing a mechanism for preferential credit assignment to the subregion most responsible for producing the outcome.
- Anticipatory DA ramps in DMS serve as eligibility tags that link the subregion's predictive accuracy to the magnitude of reward credit it subsequently receives.
- A formal MoE-RL architecture unifies DA ramps, waves, transients, and behavioural adjustments under a single hierarchical inference framework, showing how a DA system can implement actor-specific credit assignment without losing global RPE functionality.

Prior to this paper, spatially tailored DA in the dorsal striatum had been suggested by regional studies but never demonstrated as a coherent large-scale organisational principle with direct behavioural relevance and a computational account.

---

### Brain regions & systems

- **Dorsomedial striatum (DMS)**: Primary target of analysis; implicated in goal-directed, action-outcome learning. In this paper, the site of positive anticipatory DA ramps during instrumental control and the first recipient of ML reward waves in instrumental trials; proposed locus of the "distance expert" in the MoE model.
- **Dorsolateral striatum (DLS)**: Implicated in stimulus-response/habitual behaviour. Receives DA peaks with delay in instrumental trials (after DMS) and earlier than DMS in Pavlovian trials; proposed to receive proportionally less credit for instrumental outcomes.
- **Posterior-tail striatum (TS)**: Partially within the imaging window; mentioned as a third anatomical territory but not the focus of detailed analysis.
- **Midbrain dopamine neurons (VTA/SNc)**: Upstream source of DA axon projections; synchrony vs. sequential recruitment of these neurons is discussed as one candidate origin of wave-like patterns, but not directly recorded.
- **Corticostriatal loops**: The hierarchical corticostriatal circuit architecture (Graybiel, 2008; Haber, 2003) provides the anatomical rationale for the MoE model; glutamatergic and cholinergic interactions with DA axons are discussed as candidate wave-generating mechanisms.

---

### Mechanistic insight

The paper meets both criteria: it presents an algorithm (spatiotemporally directed RPE delivery via DA waves) and provides neural data (widefield and two-photon DA imaging, dual-colour axon and release recordings) that specifically support this algorithm over the global-broadcast alternative.

**Computational**: The brain must solve the credit assignment problem in hierarchically organised striatal circuits — which subregion or "actor" should receive reinforcement for a given outcome? The system must infer agency (did my actions cause this reward?) and direct plasticity accordingly.

**Algorithmic**: Inferred agency is accumulated as a responsibility signal (ramp) in DMS during reward pursuit. At outcome, this ramp biases the timing of reward-evoked DA via wave direction: ML waves deliver DA to DMS first (high credit) when agency is inferred, LM waves delay DMS activation (low credit) in Pavlovian conditions. Temporal delays interact with eligibility traces (analogous to those in TD RL) so that credit propagates to earlier predictive states in proportion to their eligibility. Sub-expert RPEs at tone transitions provide the fine-grained updating needed to discriminate between contingency-specific experts.

**Implementational**: DA axon activation and extracellular release are tightly coupled (dual-colour jRGECO1a + dLight recordings, r >> control). Candidate mechanisms include: (a) sequential recruitment of topographically projecting midbrain DA cells; (b) local striatal microcircuits — cholinergic interneurons driven by cortical/thalamic input can evoke DA release in spatiotemporal patterns; (c) interaction between primed axon excitability during anticipation and synchronous midbrain reward bursts producing sequential propagation. The exact implementational mechanism is not established and is explicitly listed as a limitation.

---

### Limitations & open questions

- The mechanistic origin of DA waves is not determined; candidate mechanisms (midbrain sequential firing, local cholinergic/GABAergic modulation) are proposed but not tested.
- A corresponding "time expert" in the DS was not identified; the model can function with a single DMS expert comparing against a prior expectation of control, but the full MoE structure predicts a separable time-expert territory not directly characterised.
- Causal role of DA waves in learning was not established; the study is correlational with respect to behavioural adaptation (wave direction predicts next-trial speed but does not manipulate it).
- Recordings were made from the dorsal surface of the striatum; contributions of deeper layers and ventral striatum are not captured.
- Population-level synchrony of midbrain DA neurons during wave events was not recorded; the relationship between midbrain population dynamics and striatal wave trajectories remains open.
- How wave generation is coordinated with the glutamatergic and cholinergic afferent activity that drives it is not addressed.

---

### Connections & keywords

**Key citations**:
- Schultz et al. (1997) — foundational RPE hypothesis
- Montague et al. (1996) — TD learning and dopamine
- Frank & Badre (2012); O'Reilly & Frank (2006) — hierarchical corticostriatal RL models (direct predecessor of MoE)
- Doya et al. (2002) — multiple-model RL (MoE precursor)
- Yagishita et al. (2014) — timing constraints on corticostriatal plasticity in vitro
- Hamid et al. (2016) — mesolimbic DA ramps signal value of work
- Eshel et al. (2016) — synchrony and RPE coding in DA neurons
- Dabney et al. (2020) — distributional RL in dopamine
- Hintiryan et al. (2016); Hunnicutt et al. (2016) — mouse corticostriatal projectome

**Named models or frameworks**:
- Reward prediction error (RPE) hypothesis
- Temporal difference (TD) reinforcement learning
- Mixture-of-experts (MoE) model
- Spatiotemporal difference RL
- Semi-Markov state representation
- Eligibility traces

**Brain regions**:
- Dorsomedial striatum (DMS)
- Dorsolateral striatum (DLS)
- Posterior-tail striatum (TS)
- Midbrain dopamine neurons (VTA/SNc)
- Corticostriatal circuits / basal ganglia loops

**Keywords**:
- dopamine spatiotemporal waves
- credit assignment
- striatal subregion specialisation
- reward prediction error
- instrumental vs. Pavlovian learning
- agency inference
- mixture-of-experts reinforcement learning
- eligibility traces
- widefield dopamine imaging
- dLight / GCaMP6f
- anticipatory dopamine ramps
- corticostriatal plasticity
