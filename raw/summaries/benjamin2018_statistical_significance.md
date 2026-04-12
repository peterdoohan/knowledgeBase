---
source_file: benjamin2018_statistical_significance.md
paper_id: benjamin2018_statistical_significance
title: "Redefine Statistical Significance"
authors:
  - "Daniel J. Benjamin"
  - "James O. Berger"
  - "Magnus Johannesson"
  - "Brian A. Nosek"
  - "E.-J. Wagenmakers"
  - "68 additional co-authors"
year: 2018
journal: "Nature Human Behaviour"
paper_type: review
contribution_type: methodological
frameworks:
  - bayesian_inference
keywords:
  - statistical_significance_threshold
  - p_value
  - bayes_factor
  - false_positive_rate
  - reproducibility_crisis
  - null_hypothesis_significance_testing
  - type_i_error
  - replication_rate
  - prior_odds
  - statistical_power
  - p_hacking
  - open_science
  - redefine
  - statistical
  - significance
---

### One-line summary

A large consortium of researchers argues that the default P-value threshold for claiming new discoveries should be lowered from 0.05 to 0.005, on the grounds that P < 0.05 provides only weak Bayesian evidence and generates unacceptably high false positive rates.

---

### Background & motivation

The reproducibility crisis in science has prompted extensive scrutiny of research practices such as P-hacking, publication bias, and underpowered studies. However, the authors argue that an underappreciated root cause is that the conventional threshold of P < 0.05 is too lenient: it corresponds to only weak Bayesian evidence (Bayes factors of roughly 2.5–3.4) and produces high false positive rates, especially when prior odds of a true effect are low. The proposal is framed as an immediately actionable, broadly applicable fix that complements but does not replace more comprehensive reforms.

---

### Methods

This is a theoretical and policy-oriented commentary, not an empirical study. The authors:

- Derive the relationship between P values and Bayes factors under standard assumptions (i.i.d. normal observations, two-sided z-test), using several classes of alternative hypotheses (power curve, likelihood ratio bound, UMPBT, local-H1 bound).
- Compute false positive rates as a function of statistical power and prior odds using a standard formula relating alpha, power (1 - beta), and the proportion of true null hypotheses (phi).
- Reference empirical replication rates from the Open Science Collaboration psychology replication project (n = 93) and an experimental economics replication project (n = 16) to motivate the proposed threshold.
- Address potential objections including increased false negative rates, field heterogeneity, and the argument that NHST should be abandoned altogether.

---

### Key findings

- A two-sided P value of 0.05 corresponds to Bayes factors of approximately 2.5 to 3.4 in favour of H1 — characterised as "weak" or "very weak" evidence under conventional Bayes factor classifications.
- Under prior odds of 1:10 (plausible for psychology based on prediction markets and replication data), P < 0.05 yields a false positive rate exceeding 33% regardless of statistical power.
- Lowering the threshold to P < 0.005 reduces this minimum false positive rate to approximately 5%, and P < 0.005 corresponds to Bayes factors of approximately 14–26 ("substantial" to "strong" evidence).
- Empirical replication rates approximately double when initial studies used P < 0.005 versus 0.005 < P < 0.05: 50% vs 24% in psychology; 85% vs 44% in experimental economics.
- Maintaining 80% power under the new threshold requires approximately 70% larger sample sizes, but the authors argue efficiency gains from avoiding false-premise follow-up studies outweigh this cost.
- The proposal explicitly does not apply to fields already using stricter thresholds (genomics: 5 × 10^-8; high-energy physics: ~3 × 10^-7).

---

### Computational framework

The paper uses basic Bayesian inference as an evaluative framework, not as a proposed replacement for NHST. The core formalism is:

- **Posterior odds = Bayes factor × prior odds** (Bayes' rule applied to H0 vs H1).
- The Bayes factor (BF) is defined as the ratio of likelihoods f(x_obs | H1) / f(x_obs | H0).
- The false positive rate formula: FPR ≈ (alpha × phi) / (alpha × phi + (1 - beta) × (1 - phi)), where phi is the proportion of true null hypotheses and 1 - beta is power.

The framework is used descriptively — to show that a frequentist threshold of 0.05 corresponds to weak Bayesian evidence — not to propose that researchers switch to Bayesian methods, though many authors express a personal preference for Bayesian approaches.

---

### Prevailing model of the system under study

The "system" here is the scientific inference pipeline used across empirical disciplines that rely on null hypothesis significance testing (NHST). The prevailing standard, inherited from Ronald Fisher's early 20th-century work, uses P < 0.05 as the threshold for declaring statistical significance. The paper's introduction signals that this threshold has long been criticised by statisticians but has persisted due to convention, training inertia, and lack of consensus on alternatives. The introduction also frames the replication crisis as evidence that the threshold is quantitatively inadequate, not merely philosophically contested.

---

### What this paper contributes

The paper formalises, with explicit Bayesian and frequentist calculations, why P < 0.05 is too permissive for claims of new discoveries: it provides only weak evidential support and yields false positive rates that are unacceptably high given realistic prior odds. By anchoring the proposed threshold of 0.005 to both Bayes factor benchmarks and empirical replication data, the paper moves beyond prior advocacy for stricter thresholds (e.g., Johnson 2013, Greenwald et al. 1996) to build a critical-mass endorsement. It distinguishes the proposal from a general rejection of NHST, treating the threshold change as a pragmatic reform within the existing statistical culture rather than a paradigm shift.

---

### Brain regions & systems

Not applicable. The paper is a statistical methodology commentary with no anatomical focus. The level of analysis is the statistical inference procedure applied across empirical sciences broadly, with particular examples drawn from psychology, experimental economics, and biomedical research.

---

### Mechanistic insight

The paper does not meet the bar for this section. It presents no neural data and proposes no algorithmic account of any neural or cognitive process. It is a statistical policy proposal, not a mechanistic investigation.

The paper's contribution is at the level of meta-scientific methodology: it provides a formal account of why the current inference standard is inadequate, but does not model any cognitive or neural mechanism.

---

### Limitations & open questions

- The choice of 0.005 remains arbitrary; the paper acknowledges that the appropriate threshold depends on prior odds, number of hypotheses tested, study design, and the relative costs of type I vs type II errors.
- The proposal applies only to studies using NHST and claims of new discoveries; it does not address confirmatory replications, policy decisions, or publication standards.
- Increasing sample sizes by ~70% may be infeasible in many research contexts, potentially creating perverse incentives (e.g., pressure to meet the new threshold at the expense of transparency or replication).
- The paper does not specify how "suggestive" evidence (0.005 < P < 0.05) should be treated in practice, leaving this to community norms.
- The authors acknowledge that P-hacking, multiple testing, publication bias, and low power are arguably larger problems, and that this proposal does not address them.
- No mechanism is provided for enforcing or monitoring adoption across diverse research communities.

---

### Connections & keywords

**Key citations:**
- Greenwald et al. (1996) — Psychophysiology — earlier proposal to lower the threshold
- Johnson (2013) — PNAS — uniformly most powerful Bayesian test (UMPBT)
- Open Science Collaboration (2015) — Science — psychology replication project
- Camerer et al. (2016) — Science — experimental economics replication project
- Kass & Raftery (1995) — J. Am. Stat. Assoc. — Bayes factor classification conventions
- Szucs & Ioannidis (2017) — PLoS Biology — statistical power in psychology
- Wasserstein & Lazar (2016) — Am. Stat. — ASA statement on P values
- Fisher (1925) — Statistical Methods for Research Workers — origin of 0.05 threshold
- Sellke, Bayarri & Berger (2001) — Am. Stat. — local-H1 bound on Bayes factors

**Named models or frameworks:**
- Null hypothesis significance testing (NHST)
- Bayes factor
- Uniformly most powerful Bayesian test (UMPBT)
- Genome-wide significance threshold (5 × 10^-8)
- Five-sigma rule (high-energy physics)

**Brain regions:** Not applicable.

**Keywords:** statistical significance threshold, P value, Bayes factor, false positive rate, reproducibility crisis, null hypothesis significance testing, type I error, replication rate, prior odds, statistical power, P-hacking, open science
