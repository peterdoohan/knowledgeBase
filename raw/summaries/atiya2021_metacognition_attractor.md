---
source_file: atiya2021_metacognition_attractor.md
title: "Explaining distortions in metacognition with an attractor network model of decision uncertainty"
authors: Nadim A. A. Atiya, Quentin J. M. Huys, Raymond J. Dolan, Stephen M. Fleming
year: 2021
journal: PLoS Computational Biology
paper_type: computational
contribution_type: theoretical
---

### One-line summary

A biologically-plausible attractor network model of decision uncertainty, extended with a dedicated uncertainty-monitoring population, explains dissociable distortions in metacognitive bias, sensitivity, and efficiency — and links psychiatric symptom scores to a single circuit-level parameter (uncertainty modulation strength) estimated from first-order performance data alone.

---

### Background & motivation

Distortions in metacognition (the ability to monitor and evaluate one's own cognition) are common across mental health disorders, yet the neural mechanisms underlying these distortions remain poorly understood. Existing algorithmic-level models of decision confidence — while useful for relating brain function to psychopathology — are difficult to map to specific neurobiological mechanisms. A gap therefore exists between biologically-plausible circuit models of decision-making and formal metrics of metacognitive performance (bias, sensitivity, efficiency). Closing this gap could enable circuit-level interpretation of metacognitive dysfunction and provide tools for inferring metacognitive performance in settings where explicit confidence reports are unavailable.

---

### Methods

- **Model architecture**: A three-population neural circuit model comprising (1) two mutually-inhibiting, self-excitatory sensorimotor populations encoding competing choices (adapted from Wong & Wang 2006), and (2) a dedicated "uncertainty-monitoring" (UM) population that integrates summed sensorimotor activity as a leaky integrator and feeds excitatory feedback back to both sensorimotor populations. Decision uncertainty per trial = maximum firing rate of the UM population.
- **Key free parameters**: (1) gain — maps stimulus dot-difference to input current in sensorimotor populations (indexes perceptual sensitivity); (2) uncertainty modulation strength (UM, wu) — governs the weight of excitatory feedback from the monitoring population to sensorimotor populations.
- **Simulation**: Model was simulated across a grid of gain and UM values; metacognitive bias, meta-d', and M-ratio (meta-d'/d') were estimated from simulated confidence-accuracy matrices using HMeta-d (Fleming 2017).
- **Fitting to empirical data**: Model fitted to first-order performance (accuracy and RT) of ~495 participants per experiment from Rouault et al. (2018) online perceptual dot-discrimination task (Amazon Mechanical Turk). Subplex optimisation minimised a cost function over overall accuracy and RT. Confidence reports were used only to set distribution-matching thresholds (out-of-sample test).
- **Psychiatric analysis**: Linear regressions with z-scored self-report questionnaire scores (depression, generalised anxiety, schizotypy, impulsivity, OCD, social anxiety) predicting fitted gain and UM parameters, controlling for age, gender, and IQ.

---

### Key findings

- Increasing gain strongly increases d' (β₁ = 0.5, R² = 0.99, p < 0.001) and meta-d' (β₁ = 28.45, R² = 0.99, p < 0.001) but has only a weak effect on metacognitive bias.
- Increasing UM has no significant effect on d' (β₁ = 5.65, R² = 0.01, p = 0.15) but negatively affects metacognitive bias (β₁ = −122.83, R² = 0.20, p < 0.001), meta-d' (β₁ = −98.83, R² = 0.50, p < 0.001), and metacognitive efficiency M-ratio (β₁ = −100.49, R² = 0.58, p < 0.001).
- Manipulating gain and UM jointly confirmed a double dissociation: d' is driven by gain; metacognitive sensitivity is driven by UM.
- The model fitted to first-order performance (accuracy and RT) accurately predicted participants' confidence reports as an out-of-sample test, replicating the empirical confidence × difficulty × accuracy interaction.
- Self-reported depression, generalised anxiety, schizotypy, social anxiety, and OCD scores were all significantly associated with weaker UM (p < 0.05), while impulsivity was not; no symptom score predicted gain.
- The UM parameter provides a low-dimensional implicit marker of metacognitive (dys)function comparable in sensitivity to direct metacognitive measures (effect sizes slightly smaller than those predicting empirical mean confidence).

---

### Computational framework

**Dynamical systems / attractor networks.** The model is a reduced mean-field version of a spiking neural network (building on Wang 2002 and Wong & Wang 2006) that exhibits attractor dynamics — winner-take-all behaviour under sufficiently asymmetric inputs. The core formalism is:

- Two coupled differential equations governing synaptic gating variables (S_L, S_R) with self-excitation (w+), mutual inhibition (w−), and nonlinear input-output function H.
- A third leaky-integrator differential equation for the uncertainty-monitoring population U, driven by the sum of sensorimotor firing rates and subject to excitatory feedback of strength wu (UM).
- Decision uncertainty is read out as the maximum value of U reached before a decision threshold is crossed.

Key assumptions: (1) confidence is inversely related to decision uncertainty; (2) the uncertainty-monitoring population is a higher-order node anatomically associated with prefrontal cortex; (3) the integration window for uncertainty is set by decision time (not a fixed interval).

---

### Prevailing model of the system under study

The paper situates itself against two complementary traditions. First, algorithmic-level models of metacognition (signal detection theory metrics: meta-d', M-ratio) successfully characterise the information-theoretic efficiency of metacognitive judgements and have linked psychiatric symptoms to dissociable metacognitive profiles — but are silent about neural implementation. Second, detailed biophysical models of decision-making (Wang 2002; Wong & Wang 2006) provide circuit-level accounts of choice and RT but had not been extended to explain confidence and metacognition. More recent work by Atiya et al. (2019, 2020) introduced the uncertainty-monitoring population to account for confidence and change-of-mind behaviours, but had not mapped this formalism onto standard metacognitive metrics or psychopathology. The prevailing assumption was thus that dissociable metacognitive distortions (e.g. confidence reductions in depression without performance changes, as shown by Rouault et al. 2018) must reflect higher-order computational differences, but the circuit mechanism was unspecified.

---

### What this paper contributes

The paper demonstrates that a single biologically-grounded parameter — the strength of the feedback from a higher-order uncertainty-monitoring population back to the decision circuit (UM) — can account for the full pattern of dissociable metacognitive distortions without affecting perceptual sensitivity. Specifically:

- Before this paper, it was known that psychiatric symptoms correlate with lower confidence and reduced metacognitive sensitivity, but no circuit-level account existed.
- This paper shows that these effects can be explained by a weaker UM parameter, providing a first mechanistic interpretation: weaker excitatory feedback from a prefrontal-like monitoring node reduces confidence signal quality without impairing sensory processing.
- It also shows that model parameters constrained only by RT and accuracy are sufficient to predict confidence out-of-sample — enabling implicit inference of metacognitive profiles from tasks without explicit confidence reports (animals, children, brief tasks).
- The UM parameter serves as a low-dimensional transdiagnostic marker of metacognitive dysfunction, replicating and extending the Rouault et al. (2018) findings with a circuit-level interpretation.

---

### Brain regions & systems

- **Prefrontal cortex (anterior/medial)** — proposed anatomical locus of the uncertainty-monitoring population. The paper draws on neurophysiological evidence (Kepecs et al. 2008; Fleming & Dolan 2012; Bang & Fleming 2018) and lesion studies (Fleming et al. 2014) showing that prefrontal regions encode decision confidence and that anterior PFC lesions selectively impair metacognitive accuracy without affecting task performance.
- **Sensorimotor cortex / parietal areas (implicit)** — the sensorimotor module is presented as a generic decision circuit without explicit anatomical attribution; the authors note that future work should combine parallel parietal evidence-accumulation populations with prefrontal monitoring nodes.

---

### Mechanistic insight

The paper proposes an algorithm (excitatory feedback from an uncertainty-monitoring population modulating evidence accumulation) but does not provide neural data — it is a purely computational/modelling paper validated against behavioural data. It does not meet the bar for mechanistic insight as defined here, because:

1. The uncertainty-monitoring module and its UM parameter are consistent with prefrontal involvement in metacognition, and the model's dissociation between UM and gain parallels lesion dissociations — but no neural recordings, imaging, pharmacology, or lesion data specific to the model's variables are collected or analysed.
2. The psychiatric associations are with self-report questionnaire scores, not neural measurements.

The paper thus links computation to behaviour, but not to neural implementation. It explicitly calls for future neuroimaging work to test the model's predictions at a circuit level.

---

### Limitations & open questions

- The UM integration window is set by decision time rather than being fixed; this creates a strong positive correlation between UM activity and RT, preventing the model from accounting for tasks where slow responses are associated with high confidence (speed-accuracy trade-off reversals).
- The model was less stable when fit to staircase-difficulty data (Experiment 2), suggesting that systematic variation in task difficulty is necessary to constrain UM inference — limiting applicability to staircase designs.
- The model does not incorporate post-decisional evidence processing or extended evidence accumulation after a decision threshold is crossed.
- The high positive correlation between the losing sensorimotor population's firing rate and the UM population's activity may limit the model in settings with atypical confidence-RT relationships.
- Results showing significant symptom-UM associations were only robustly obtained for Experiment 1 (fixed difficulty); Experiment 2 (staircase) showed qualitatively similar but non-significant trends.
- The model does not address the physical implementation (cell types, neuromodulators) of the uncertainty-monitoring circuit.
- Future work should combine the full model (including a motor output network) with continuous motor trajectories to study uncertainty, indecisiveness, and compulsivity.

---

### Connections & keywords

**Key citations**:
- Rouault, Seow, Gillan, Fleming (2018) — Biological Psychiatry — source dataset and original psychiatric symptom analyses.
- Wong & Wang (2006) — foundational reduced attractor network model of perceptual decisions.
- Wang (2002) — original spiking network model of probabilistic decision-making.
- Atiya et al. (2019) Nature Communications — neural circuit model with uncertainty-monitoring population.
- Atiya et al. (2020) PLoS Computational Biology — changes-of-mind extension of the same model.
- Fleming & Dolan (2012) — neural basis of metacognitive ability review.
- Fleming (2017) — HMeta-d hierarchical Bayesian metacognitive efficiency estimation.
- Maniscalco & Lau (2012) — meta-d' signal detection theoretic framework.
- Kepecs et al. (2008) — neural correlates of decision confidence.
- Bang & Fleming (2018) — medial PFC encoding of decision confidence.
- Fleming et al. (2014) — anterior PFC lesions and metacognitive impairment.

**Named models or frameworks**:
- Wong-Wang attractor network model
- HMeta-d (hierarchical Bayesian meta-d')
- M-ratio (meta-d'/d') metacognitive efficiency measure
- Signal detection theory (SDT) framework for metacognition
- Subplex optimisation method
- Distribution matching (for mapping simulated uncertainty to confidence ratings)

**Brain regions**:
- Prefrontal cortex (anterior/medial)
- Sensorimotor cortex (implicit)

**Keywords**:
- attractor network
- decision confidence
- metacognition
- uncertainty monitoring
- computational psychiatry
- metacognitive efficiency
- M-ratio
- meta-d'
- uncertainty modulation
- dynamical systems model
- perceptual decision-making
- psychiatric symptom transdiagnostic
