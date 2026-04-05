---
source_file: adams2018_attractor_schizophrenia.md
title: "Attractor-like Dynamics in Belief Updating in Schizophrenia"
authors: Rick A. Adams, Gary Napier, Jonathan P. Roiser, Christoph Mathys, James Gilleen
year: 2018
journal: The Journal of Neuroscience
paper_type: computational
contribution_type: theoretical
---

### One-line summary

A belief-instability parameter derived from attractor network principles — not a simple learning-rate bias — best accounts for schizophrenia's nonlinear belief-updating pattern across two independent datasets, with belief instability and response stochasticity co-elevated and mutually correlated in keeping with the unstable attractor hypothesis.

---

### Background & motivation

Subjects with schizophrenia (Scz) make abnormally large belief revisions following unexpected evidence in probabilistic inference tasks ("disconfirmatory bias"), yet also update less than controls to consistent evidence — a pattern that prior accounts framed either as a generic learning-rate difference or a bias specifically toward disconfirmatory information. Neither explanation captures the full nonlinear updating profile. The "unstable attractor" hypothesis proposes that NMDAR or dopamine-D1 receptor hypofunction in cortex flattens the energy landscape of recurrent neural networks, making quasi-stable attractor states easier to escape but harder to deepen — which would jointly predict overweighting of unexpected evidence, underweighting of consistent evidence, greater stochasticity in responding, and a correlation between these two signatures. No prior computational study had formally tested this mechanistic account of the beads-task belief-updating abnormalities in Scz.

---

### Methods

- **Task**: "Probability estimates" version of the beads task; subjects rate the probability that a sequence of beads comes from a given jar (85:15 or 80:20 ratios) after each bead, without deciding when to stop.
- **Datasets**:
  - Dataset 1 (n = 80; 18 Scz/schizo-affective, 22 nonpsychotic mood disorders as clinical controls, 35 nonclinical controls; all male) — collected at two time points (when unwell and after recovery for clinical groups).
  - Dataset 2 (n = 167; 56 Scz, 111 controls; mixed sex) — stable outpatients; four sequences per subject.
- **Perceptual model**: Hierarchical Gaussian Filter (HGF) — a variational Bayesian framework with individual parameters. Six nested models tested, varying which parameters were free: evolution rate (ω), initial belief variance (σ₂(0)), a disconfirmatory bias parameter (α, AR(1) pull toward maximum uncertainty), and a belief instability scaling factor (κ₁), always paired with response stochasticity (ζ).
- **Key model distinction**: Models 5 and 6 (containing κ₁) embed attractor-like dynamics by making the sigmoid mapping from belief tendency to predicted probability nonlinear and state-dependent — high κ₁ mimics a shallow energy landscape (easy switching, difficult stabilisation). Models 3 and 4 (containing α) encode a simpler disconfirmatory pull.
- **Model selection**: Protected exceedance probabilities (Bayesian model comparison) computed separately for each group in each dataset at each time point.
- **Statistical comparisons**: Kruskal–Wallis and Mann–Whitney U tests on parameter distributions; Spearman correlations between parameters; confound analyses for IQ and working memory.

---

### Key findings

- Model 6 (HGF with belief instability κ₁ and response stochasticity ζ, plus free σ₂(0)) had the highest exceedance probability in all groups in both datasets and at both time points — it was the winning model even among controls, not just Scz.
- Belief instability κ₁ was significantly higher in Scz than nonclinical controls in Dataset 1 (baseline: χ²(2,80) = 9.64, p = 0.008, η² = 0.12; follow-up: χ²(2,55) = 8.0, p = 0.02, η² = 0.15) and Dataset 2 (Z = −5.6, p = 3×10⁻⁸, r = 0.43).
- Response stochasticity ζ was significantly lower (i.e., higher stochasticity) in Scz in Dataset 1 (baseline: χ²(2,80) = 11.9, p = 0.003, η² = 0.15) and Dataset 2 (Z = 3.9, p = 0.0001, r = 0.30).
- These two parameters were negatively correlated in all three experiments (Dataset 1 baseline: ρ = −0.38, p = 0.0004; Dataset 1 follow-up: ρ = −0.52, p = 0.0001; Dataset 2: ρ = −0.35, p = 10⁻⁶), consistent with a shared neurobiological origin.
- In Dataset 1, clinical controls (nonpsychotic mood disorders) showed the same parameter pattern as Scz when unwell (both κ₁ and ζ differed significantly from nonclinical controls at baseline) but were indistinguishable from nonclinical controls at follow-up — suggesting a state-dependent rather than trait mechanism in mood disorders, contrasting with the persistent trait-like difference in Scz.
- Parameters did not significantly correlate with positive or negative symptom scores (except a weak association of ζ with negative symptoms in Dataset 2); response stochasticity ζ correlated with delusion-proneness (PDI) across all subjects in Dataset 1 (ANCOVA F(1,67) = 7.1, p = 0.01).
- Group differences in κ₁ and ζ persisted after controlling for IQ and working memory discrepancies between groups.

---

### Computational framework

**Hierarchical Gaussian Filter (HGF)** — a variational Bayesian inference scheme for belief updating under uncertainty (Mathys et al., 2011).

- **What is modelled**: trial-by-trial updating of a latent "tendency" variable x₂ (log-odds of the jar identity), which drives predictions of observable bead colour via a logistic sigmoid.
- **Key variables**: x₁ (jar probability), x₂ (tendency; the primary latent state), and model parameters: ω (evolution rate / process noise), σ₂(0) (initial belief variance), ζ (response precision / inverse stochasticity), κ₁ (belief instability scaling factor), and α (AR(1) disconfirmatory pull, in alternative models).
- **Attractor dynamics extension (Models 5–6)**: κ₁ rescales the sigmoid argument so that updates are largest when beliefs are intermediate and smallest (relative to standard HGF) when beliefs are near certainty. High κ₁ makes confident beliefs "high energy" states — easy to escape, hard to stabilise — directly mimicking a flattened attractor energy landscape. The HGF itself does not implement spiking attractor networks; κ₁ is a phenomenological approximation of what unstable attractor states would do to inference.
- **Key assumption**: The pattern of differential updating to confirmatory versus disconfirmatory evidence is driven by a single continuous parameter (κ₁) governing state stability rather than by separate learning rates for different evidence types.

---

### Prevailing model of the system under study

The paper's introduction frames prior work in terms of two competing accounts of Scz belief-updating abnormalities:

1. **Simple learning-rate or evidence-weighting accounts**: Scz use less evidence before deciding ("jumping to conclusions"), overweight recent evidence, or have a specific bias toward disconfirmatory information — all treated as fixed-direction parameter shifts in otherwise standard Bayesian or RW-style models.
2. **Stochasticity accounts**: Scz are noisier responders (Moutoussis et al., 2011), but this was not linked to structured updating biases.

Underlying the paper's alternative hypothesis is the **unstable attractor hypothesis** (Rolls et al., 2008; Durstewitz and Seamans, 2008): in Scz, NMDAR hypofunction (on pyramidal cells and/or via reduced drive to inhibitory interneurons) or cortical dopamine-D1 hypofunction flattens the energy wells of recurrent cortical networks (Hopfield-type). Network states corresponding to beliefs become less stable, making transitions between attractor states easier in both directions and making states more vulnerable to noise. This hypothesis had been applied to working memory deficits (Murray et al., 2014) but had not been formally instantiated in a belief-updating model and tested against behavioural data.

---

### What this paper contributes

The paper provides the first formal computational model — and cross-validated evidence across two independent datasets — linking the unstable attractor hypothesis to the specific nonlinear signature of belief updating in Scz. Key advances over the prevailing view:

- The "disconfirmatory bias" framing is shown to be an incomplete description: Scz do not simply update more to one class of evidence; rather, they exhibit nonlinear state-dependent updating that is simultaneously over-responsive to evidence crossing the belief midpoint and under-responsive to evidence pushing beliefs toward certainty. A single parameter κ₁ unifies these opposing asymmetries.
- Belief instability and response stochasticity are not independent — they co-vary across all experiments, consistent with the hypothesis that both reflect a common underlying loss of network stability rather than unrelated noise sources.
- The same parameter changes appear transiently in nonpsychotic mood disorders during acute illness, suggesting the neural mechanism is not Scz-specific but may be present whenever acute brain state disruptions occur — while in Scz it appears to be a stable trait.
- Healthy controls also favour Model 6 over simpler alternatives, suggesting that the κ₁ parameter captures something real about normal belief updating (a slight asymmetry that stabilises confident beliefs), which is exaggerated in Scz.

---

### Brain regions & systems

The paper is primarily computational and behavioural; no neuroimaging or recording data are collected. Brain regions are discussed in the theoretical framing only:

- **Prefrontal cortex (PFC)** — proposed primary locus of attractor instability; recurrent PFC networks are hypothesised to implement the quasi-stable belief states whose energy landscape is flattened in Scz.
- **NMDA receptors on pyramidal cells** — weakened recurrent excitation hypothesised to reduce attractor depth.
- **NMDA receptors on inhibitory interneurons** — reduced drive to interneurons would reduce lateral suppression of competing attractor states.
- **Dopamine D1 receptors in PFC** — alternative or complementary route to attractor destabilisation (Durstewitz and Seamans, 2008).
- **Striatum** — mentioned in relation to dopamine D2 antagonism effects on medication, and striatal dysfunction in reversal learning (Schlagenhauf et al., 2014).

---

### Mechanistic insight

The paper does not meet the bar for this section. It proposes a mechanistic algorithm (belief instability via κ₁ as a proxy for attractor network shallowing) and fits it to behavioural data from two independent datasets, but it provides no neural data — no recordings, imaging, lesion, or pharmacology — that specifically support the attractor algorithm over alternatives.

The paper explicitly acknowledges this gap: "More detailed spiking network modeling, pharmacological (or other NMDAR) manipulations, and imaging are required in the future to understand how neuromodulatory function in both pyramidal cells and inhibitory interneurons contributes to real attractor dynamics and probabilistic inference." The computational link between κ₁ and NMDAR function is currently theoretical; no direct mapping between the model's parameters and measured neural activity has been tested.

---

### Limitations & open questions

- All Scz subjects were taking antipsychotic medication during testing, which may attenuate group differences (dopamine D2 antagonists likely reduce some response variability and overconfidence).
- IQ was not well matched across groups in Dataset 1; while within-group regressions showed no significant IQ-parameter correlations, a confounding contribution cannot be excluded.
- The HGF does not implement actual attractor states; κ₁ is a phenomenological summary of what such dynamics would do to inference, not a direct measure of network stability.
- No empirical link between κ₁ and NMDAR function has been tested (e.g., pharmacological challenge, neuroimaging of E/I balance).
- Relationships between computational parameters and symptom dimensions were weak or absent — the mechanistic path from NMDAR hypofunction to κ₁ to clinical symptoms remains uncharacterised.
- Heterogeneity within Scz (hallucinating vs. non-hallucinating; positive vs. negative symptom profiles) is not captured; sufficient power to detect subgroup effects was lacking.
- The datasets used different response scales (continuous vs. Likert) and bead ratios (85:15 vs. 80:20), introducing some cross-dataset inconsistency.

---

### Connections & keywords

**Key citations**:
- Mathys et al. (2011) — Hierarchical Gaussian Filter original paper
- Rolls et al. (2008) — Computational models of schizophrenia and dopamine modulation in PFC
- Durstewitz and Seamans (2008) — Dual-state theory of PFC dopamine function
- Peters and Garety (2006) — Original Dataset 1 analysis; disconfirmatory updating
- Moutoussis et al. (2011) — Response stochasticity in psychosis
- Jardri et al. (2017) — Circular inference in schizophrenia (overcounting likelihoods)
- Hamm et al. (2017) — Altered cortical ensembles in mouse models of schizophrenia
- Murray et al. (2014) — Attractor working memory model of schizophrenia
- Hopfield (1982) — Attractor network foundations

**Named models or frameworks**:
- Hierarchical Gaussian Filter (HGF)
- Hopfield attractor network
- Unstable attractor hypothesis of schizophrenia
- Beads task / "probability estimates" version
- Bayesian model selection (protected exceedance probability; Rigoux et al., 2014)
- AR(1) disconfirmatory bias model

**Brain regions**:
- Prefrontal cortex (PFC)
- Striatum (secondary discussion)

**Keywords**:
- attractor network instability
- schizophrenia
- belief updating
- Hierarchical Gaussian Filter
- probabilistic inference
- beads task
- disconfirmatory bias
- NMDA receptor hypofunction
- computational psychiatry
- response stochasticity
- Bayesian model comparison
- belief instability parameter
