---
source_file: namboodiri2023_mesolimbic_dopamine_causal.md
paper_id: namboodiri2023_mesolimbic_dopamine_causal
title: "Mesolimbic dopamine release conveys causal associations"
authors:
  - "Huijeong Jeong"
  - "Annie Taylor"
  - "Joseph R Floeder"
  - "Martin Lohmann"
  - "Stefan Mihalas"
  - "Brenda Wu"
  - "Mingkang Zhou"
  - "Dennis A Burke"
  - "Vijay Mohan K Namboodiri"
year: 2023
journal: Science
paper_type: empirical
contribution_type: theoretical
species:
  - mouse
methods:
  - optogenetics
brain_regions:
  - hippocampus
  - striatum
  - nucleus_accumbens
  - ventral_tegmental_area
frameworks:
  - reinforcement_learning
  - successor_representation
  - bayesian_inference
  - temporal_difference_learning
keywords:
  - mesolimbic_dopamine
  - causal_inference
  - reward_prediction_error
  - retrospective_causal_learning
  - pavlovian_conditioning
  - fiber_photometry
  - dlight
  - nucleus_accumbens_dopamine_release
  - temporal_difference_reinforcement_learning
  - contingency_learning
  - optogenetic_inhibition
  - credit_assignment
  - mesolimbic
  - dopamine
  - release
  - conveys
  - causal
  - associations
---

### One-line summary

Mesolimbic dopamine does not encode reward prediction errors (RPEs) as specified by temporal difference reinforcement learning (TDRL), but instead conveys adjusted net contingency for causal relationships (ANCCR) — a retrospective causal association signal that tracks how strongly a stimulus causally predicts a meaningful outcome.

---

### Background & motivation

The dominant theory of mesolimbic dopamine function holds that it encodes reward prediction errors (RPEs) as formalised in temporal difference reinforcement learning (TDRL): dopamine responses rise when rewards are better than expected and fall when rewards are worse than expected, with learned cues acquiring dopamine responses that then extinguish at the time of reward delivery. While this framework has guided decades of research, key empirical observations — such as persistent dopamine responses to both predictive cues and predicted rewards, and characteristic dynamics of dopamine during initial learning — are difficult to reconcile with standard TDRL. This paper proposes an alternative: that mesolimbic dopamine signals the adjusted net contingency for causal relationships (ANCCR), a retrospective causal inference algorithm, and tests this against a series of precisely designed Pavlovian conditioning experiments in head-fixed mice with fiber photometry measurement of nucleus accumbens dopamine release.

---

### Methods

- **Subjects**: Adult C57BL/6 (wild type) and DAT-Cre heterozygous mice; head-fixed preparation; water deprivation.
- **Dopamine measurement**: Fiber photometry using dLight1.3b (genetically encoded dopamine sensor) in nucleus accumbens (NAcc); 405 nm isosbestic control and 470 nm dopamine-dependent signals; ΔF/F computed after baseline correction.
- **Behavioural task design** (seven experiments):
  - Experiment 1: Random reward delivery (unpredicted sucrose, Poisson-distributed ITI) to test dynamics of unpredicted reward responses across sessions.
  - Experiments 2–5: Pavlovian discriminative conditioning (CS+/CS– with auditory cues); including elongated CS duration (Exp 3), background rewards during ITI (Exp 5), and extinction (Exp 4).
  - Experiment 6 ("Trial-less conditioning"): Cue predicts reward at fixed delay, but next cue can appear before reward — removing the standard trial structure.
  - Experiment 7 (Sequential conditioning): Two sequential cues (CS1→CS2→reward); optogenetic inhibition of VTA dopaminergic neurons (stGtACR2 in DAT-Cre mice) during CS2/reward to test causal role of dopamine in learning.
- **Computational models**: TDRL (complete serial compound and microstimulus variants) and ANCCR (retrospective causal contingency model) were simulated in parallel and compared against empirical dopamine and behavioural data across all experiments.
- **Analysis**: Area under the curve of ΔF/F for defined response windows; cumulative sum analysis for abruptness of learning; Pearson correlations; model comparisons using AIC.

---

### Key findings

- **Unpredicted reward response increases with experience** (Test 1): Dopamine release to unpredicted sucrose rewards increased across sessions, opposite to TDRL's prediction of a decrease as context acquires value. ANCCR correctly predicts this increase because repeated unpredicted rewards increase the reward–reward net contingency.
- **Dopamine response to unpredicted reward correlates positively with preceding inter-reward interval (IRI)** (Test 2): Longer IRI predicted larger dopamine response. TDRL predicts the opposite (shorter IRI → larger RPE); ANCCR predicts positive correlation because longer IRI reduces baseline predecessor representation. Pearson correlation t = 5.95, p = 5.7×10⁻⁴ (n = 8 animals).
- **Dopamine cue response precedes and is dissociated from behavioural learning** (Tests 3 and 4): Dopamine cue response arose gradually and reached ~93% of asymptote before behavioural anticipatory licking emerged (which appeared abruptly). ANCCR predicts that a contingency threshold must be crossed before downstream behavioural learning is triggered; TDRL does not naturally produce this dissociation.
- **No omission response when reward is delayed rather than omitted** (Test 5): Extending the CS duration from 2 s to 8 s did not elicit a negative dopamine response at the original reward time, unlike extinction which did. ANCCR correctly predicts no omission state unless reward probability is explicitly reduced.
- **Dopamine cue response persists alongside a positive reward response after conditioning** (Test 6): Both the conditioned cue and fully predicted reward maintained positive dopamine responses at asymptote. TDRL predicts reward response should go to zero once cue is fully predictive.
- **Trial-less conditioning produces positive intermediate cue response** (Test 7 / Experiment 6): When an intermediate cue appeared between a conditioning cue and its reward, it acquired a positive dopamine response — consistent with ANCCR assigning positive contingency to any cue that precedes reward within the causal window, regardless of trial structure.
- **Optogenetic dopamine inhibition during CS2 in sequential conditioning selectively impairs CS2 learning but spares CS1 learning** (Experiment 7): In DAT-Cre animals, inhibiting dopamine from CS2 onset through reward delivery prevented CS2 from becoming a meaningful causal target, disrupting its ANCCR update while leaving CS1 response intact (CS1 dopamine response grew in both groups, but to a lower asymptote in DAT-Cre; CS1 behaviour learned in all DAT-Cre animals). TDRL predicts negative CS1 response — not observed. CS1 response difference between WT and DAT-Cre: t = 2.80, p = 0.017.
- **Simulations of ANCCR reproduced a broad range of classic and novel conditioning phenomena**: blocking, conditioned inhibition, overexpectation, dopamine-driven unblocking, reward magnitude scaling, timescale invariance of acquisition, and ramping dopamine in serial cue sequences.

---

### Computational framework

**Retrospective causal learning / Adjusted Net Contingency for Causal Relationships (ANCCR)**

The paper proposes and formalises ANCCR, a model in which the brain learns causal associations by looking *backwards* from meaningful outcomes (rather than prospectively predicting future value as in TDRL).

**Key variables and operations**:
- **Eligibility trace** of event *i* (E←_i_): an exponentially decaying running sum of past occurrences of *i*, with time constant *T* (set to 1.2 × mean IRI). Enables online estimation of event rates without storing full history.
- **Predecessor representation** (PR, M←_ij_): the average discounted count of *i* occurrences preceding each occurrence of *j* — a retrospective association measure, updated at each occurrence of a meaningful causal target (MCT).
- **Baseline PR** (M←_i,-_): the expected PR of *i* at random moments, representing its background rate.
- **Predecessor representation contingency** (PRC, C←_ij_): PR minus baseline PR — the number of *i*'s selectively preceding *j* beyond chance.
- **Successor representation contingency** (SRC, C→_ij_): derived from PRC via Bayes' rule; the prospective counterpart.
- **Net contingency** (C↔_ij_): weighted sum of SRC and PRC (weight *w*). If it exceeds threshold *θ*, a putative causal link exists.
- **ANCCR** (Ĉ↔_ij_): net contingency adjusted for indirect causes — if event *k* precedes *i* and explains some of *i*'s predictive value, that portion is subtracted from *i*'s contingency. This implements credit assignment in a causal graph.
- **Dopamine response** (DA_i_): postulated to equal the sum of ANCCRs of *i* with respect to all current MCTs, weighted by learned causal weights *R_ij* (related to reward magnitude).
- **Meaningful causal targets**: stimuli whose learned plus innate meaningfulness exceeds a threshold; rewards are innately MCTs; cues become MCTs after learning.
- **Causal weight update** (*R_ij*): updated via a delta rule; when reward is "overcaused" (DA_reward_ < 0), causal weights of recent putative causes are reduced proportional to their uncertainty.

**Key assumptions**: (1) retrospective lookback is computationally cheaper than prospective state-space enumeration; (2) no a priori knowledge of task structure or trial boundaries is required; (3) the Markov property holds in the causal graph, not necessarily in a temporal state space; (4) timescale of learning is set adaptively by the IRI.

---

### Prevailing model of the system under study

The introduction (as reconstructed from the supplementary text's theoretical sections) positions the paper against the canonical **temporal difference reinforcement learning (TDRL) model of mesolimbic dopamine**. In this prevailing view:

- Dopamine neurons encode scalar reward prediction errors: δ = r(t) + γV(s_t) − V(s_{t−1}).
- At the start of learning, dopamine fires to unexpected rewards. As learning proceeds, the RPE signal shifts backward in time to the predictive cue, and the response at the time of reward delivery diminishes to zero once the reward is fully predicted.
- The value function V(s) is estimated prospectively: the brain must maintain internal states representing elapsed time since a cue onset, allowing it to predict future reward.
- Classic phenomena — blocking, conditioned inhibition, extinction, overexpectation — are all explained within this RPE framework.
- Dopamine signals are understood as a teaching signal that updates associative weights in proportion to how surprising an outcome is.

The TDRL framework's core assumption, which this paper contests, is that the brain constructs a Markov state space (dividing delay periods into internal states) and computes value prospectively from these states.

---

### What this paper contributes

The paper makes the case, via a series of nine behavioural tests with matched computational simulations, that the TDRL RPE account of mesolimbic dopamine is incorrect in key respects, and replaces it with ANCCR:

1. **Refutation of the RPE hypothesis for unpredicted rewards**: The increase in dopamine response to unpredicted sucrose over sessions, and its positive correlation with preceding IRI, are opposite to what TDRL predicts and are consistent with ANCCR.
2. **Identification of a dissociation between dopamine contingency learning and behaviour**: Dopamine encodes the learned causal association first; behaviour emerges later and abruptly after threshold crossing — suggesting dopamine drives world-model construction, not direct action-value updates.
3. **Resolution of the "persistent reward response" problem**: ANCCR explains why conditioned cues and fully predicted rewards both maintain positive dopamine responses — because both are genuinely meaningful causal targets. In TDRL, the reward response should extinguish once the cue fully predicts it.
4. **Extension beyond trial structure**: The trial-less conditioning experiment demonstrates that causal associations are learned without requiring trial boundaries, and ANCCR handles this naturally whereas standard TDRL state spaces fail.
5. **Causal role of dopamine at the time of reward in learning**: Optogenetic inhibition during CS2 but not CS1 specifically disrupts learning about CS2's causal role while sparing CS1's — consistent with ANCCR's mechanism whereby dopamine at a MCT gates its retrospective update.
6. **A new computational framework for dopamine**: ANCCR provides a formalised, biologically grounded alternative to TDRL that is more sample-efficient, requires no a priori state-space specification, and explains timescale invariance and complex causal structures.

---

### Brain regions & systems

- **Nucleus accumbens (NAcc)** — primary measurement site; dopamine release (via dLight1.3b fiber photometry) is the central empirical readout; proposed to receive ANCCR signals from mesolimbic dopamine projections.
- **Ventral tegmental area (VTA)** — site of optogenetic manipulation (stGtACR2 in dopaminergic neurons via DAT-Cre); source of mesolimbic dopamine projections whose activity is proposed to encode ANCCR.
- **Mesolimbic dopamine system (VTA → NAcc)** — the central system under investigation; proposed to compute and broadcast ANCCR signals that drive associative learning and the formation of a causal cognitive map.
- **Cortex, hippocampus, striatum** — mentioned in Fig S14 as putative upstream contributors to ANCCR computation (predecessor representations, causal inference), but not directly measured.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Criterion 1 (Algorithm)**: ANCCR is a fully formalised algorithm. It specifies how predecessor representations are updated, how baseline rates are estimated, how net contingency and its causal adjustment are computed, and how the dopamine response is defined as the sum of ANCCRs over all current meaningful causal targets.

**Criterion 2 (Neural data supporting the algorithm)**: Fiber photometry recordings of NAcc dopamine release across seven Pavlovian conditioning experiments, plus optogenetic inhibition of VTA dopaminergic neurons, directly test and support ANCCR predictions over TDRL. Multiple qualitative and quantitative predictions unique to ANCCR — positive correlation between DA and preceding IRI, increase of unpredicted reward response with experience, persistent cue and reward responses, no omission response to delayed (vs. omitted) rewards, positive intermediate cue response, and selective disruption of downstream learning by blocking dopamine at CS2 — are borne out.

**Marr's three levels**:

- **Computational**: The brain solves the problem of inferring causal structure from experience — identifying which stimuli causally predict meaningful outcomes (rewards, punishments). This is framed as retrospective causal credit assignment: given that a reward just occurred, which preceding events caused it?
- **Algorithmic**: The mesolimbic dopamine system computes ANCCR — the adjusted net contingency between each stimulus and every current meaningful causal target. This involves maintaining eligibility traces for all events, estimating predecessor and successor representations via Bayesian inversion, adjusting for indirect causes (credit-assignment correction), and signalling the learned degree of causal relevance. Dopamine at a meaningful causal target gates retrospective updates of association weights for recent stimuli.
- **Implementational**: VTA dopaminergic neurons project to NAcc; their activity is directly measured as the empirical dopamine signal. Optogenetic inhibition of these neurons (via stGtACR2 in DAT-Cre mice) at the time of a downstream MCT (CS2 or reward) selectively prevents that MCT from triggering retrospective updates, without affecting the learning triggered by an upstream MCT (CS1). A putative circuit basis (cortex, hippocampus, midbrain, striatum) for predecessor representation computation and ANCCR is proposed in Fig S14, but not directly tested.

**Bonus — physical implementation**: The paper proposes that eligibility traces (exponentially decaying running sums of event occurrences) are the biophysical substrate of predecessor representation learning, consistent with known synaptic eligibility trace mechanisms. Specific cell types are not identified beyond DAT+ VTA neurons.

---

### Limitations & open questions

- **Main text not included in this file**: The analysed document is the supplementary materials; the abstract, introduction, and main figures are not present, so some details of the primary empirical presentation (e.g., exact effect sizes for Tests 1–6 in main figures) are inferred from supplementary figure descriptions and statistical tables.
- **Temporal delay learning**: ANCCR learns causal associations without a priori knowledge, but the learning of precise temporal delays between causally associated events is identified as a separate problem left for future work. The model uses a pool of eligibility trace time constants as a possible solution but does not fully specify this mechanism.
- **Trial structure assumption**: The model explicitly avoids trial structure, but the experiments were still conducted in sessions with defined cue and ITI periods. Fully free-operant or naturalistic settings would provide stronger tests.
- **Single mesolimbic pathway measured**: Only NAcc dopamine was measured. Different projection targets (e.g., dorsal striatum, prefrontal cortex) may carry distinct signals; the paper notes that NAcc core vs. medial shell may differ in whether they signal signed vs. unsigned ANCCR (relevant to approach vs. avoidance).
- **Optogenetic inhibition specificity**: Inhibition was of all VTA dopaminergic cell bodies, not specific projections; off-target effects on non-mesolimbic dopamine or non-dopaminergic VTA neurons cannot be fully excluded.
- **Causal graph learning in complex environments**: ANCCR is demonstrated for simple cue–reward associations and serial sequences, but extension to richer causal graphs (e.g., multi-step, hierarchical, or partially observable environments) is flagged as an open problem.
- **Extension to punishment and aversion**: The model is stated to generalise to punishments (meaningfully negative causal targets), but this is not empirically tested.
- **Alternative interpretations of some tests**: Supplementary notes carefully address alternative models (reward rate prediction error, semi-Markov models, stress explanations), ruling them out, but the generality of ANCCR relative to all possible extensions of TDRL remains an open question.

---

### Connections & keywords

**Key citations**:
- Schultz, Dayan & Montague (temporal difference RPE / canonical dopamine theory) — the primary model being contested
- Sutton & Barto (TD learning, CSC and microstimulus state representations) — Model 1 basis
- Rescorla & Wagner (associative learning; predecessor to TDRL)
- Daw et al. (semi-Markov model of dopamine timing)
- Matias et al. (initial increase of reward response during conditioning — cited as consistent with ANCCR)
- Tian et al. (ramping dopamine in serial cue sequences — simulated and explained by ANCCR)
- Rosenberg et al. (conditioned taste aversion — used to illustrate superiority of retrospective learning)

**Named models or frameworks**:
- ANCCR (Adjusted Net Contingency for Causal Relationships) — the new model proposed
- TDRL (Temporal Difference Reinforcement Learning) — the model contested
- RPE (Reward Prediction Error) — the quantity TDRL posits dopamine encodes
- Complete Serial Compound (CSC) model — TDRL variant used in comparisons
- Microstimulus model — TDRL variant used in comparisons
- Predecessor representation / Successor representation — representational constructs central to ANCCR
- Semi-Markov model of dopamine — alternative model ruled out

**Brain regions**:
- Nucleus accumbens (NAcc)
- Ventral tegmental area (VTA)
- Mesolimbic dopamine system

**Keywords**:
- mesolimbic dopamine
- causal inference
- reward prediction error
- retrospective causal learning
- Pavlovian conditioning
- fiber photometry
- dLight
- nucleus accumbens dopamine release
- temporal difference reinforcement learning
- contingency learning
- optogenetic inhibition
- credit assignment
