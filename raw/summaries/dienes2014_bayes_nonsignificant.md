---
source_file: dienes2014_bayes_nonsignificant.md
paper_id: dienes2014_bayes_nonsignificant
title: "Using Bayes to get the most out of non-significant results"
authors:
  - "Zoltan Dienes"
year: 2014
journal: "Frontiers in Psychology"
paper_type: review
contribution_type: methodological
frameworks:
  - bayesian_inference
keywords:
  - bayes_factor
  - non_significant_results
  - null_hypothesis_significance_testing
  - statistical_inference
  - prior_distribution
  - half_normal_prior
  - uniform_prior
  - optional_stopping
  - p_value
  - evidence_strength
  - interval_estimation
  - type_ii_error
  - bayes
  - get
  - most
  - out
  - non
  - significant
  - results
---

### One-line summary

Bayes factors provide a principled method for distinguishing between genuine null effects and merely insensitive data from non-significant results, overcoming the limitations of power and interval-based approaches.

---

### Background & motivation

Non-significant results are ubiquitous in psychology and related sciences, yet no automatic conclusion follows from them: a non-significant result may indicate evidence for the null hypothesis or simply reflect underpowered, insensitive data. The field has lacked a coherent framework for choosing between these two interpretations, leading to widespread misuse — sometimes treating non-significance as evidence against a theory, sometimes ignoring informative null results. Power and confidence intervals partially address the problem but each requires specification of a minimally interesting effect size that is often difficult to justify. Bayes factors offer a way to use the data themselves to determine sensitivity, while requiring only a rough characterisation of what the theory predicts.

---

### Methods

This is a methodological tutorial/review paper. The approach is:

- Compares three approaches to interpreting non-significant results: power, interval estimates (confidence/credibility intervals), and Bayes factors.
- Focuses on a simple online Bayes factor calculator (Dienes, 2008) that accepts a parameter estimate and its standard error, and a prior distribution over the alternative hypothesis.
- Three prior distributions for the alternative are discussed: uniform (when an upper bound is known), normal (when a typical expected value is known without strong directional constraint), and half-normal (when a typical expected value is known and the effect is directional).
- Illustrates application through a series of worked examples drawn partly from published studies, covering between-subjects comparisons, interactions, paired comparisons, multi-step data collection with sequential stopping rules, and correlations.
- Provides correction factors for small degrees of freedom and discusses robustness checks (varying prior specification to verify qualitative conclusion stability).

---

### Key findings

- A p-value, no matter how high, does not in itself provide evidence for the null hypothesis; it cannot distinguish evidence for the null from data insensitivity.
- Bayes factors (B) yield three interpretable outcomes: B > 3 (substantial evidence for alternative), B < 1/3 (substantial evidence for null), and 1/3 ≤ B ≤ 3 (insensitive data).
- Unlike power, Bayes factors use the actual data to assess sensitivity; unlike confidence intervals, they can support the null without requiring specification of a minimally interesting effect size.
- A Bayes factor retains its meaning as strength of evidence regardless of stopping rule, enabling principled sequential data collection until B > 3 or B < 1/3.
- Worked examples show: (i) two identical condition means can yield B indicating insensitivity, not null support; (ii) non-significant interactions can yield B < 1/3 (substantial null support); (iii) the same data with a smaller SE shifts B from insensitive to supporting the null.
- Qualitative conclusions are typically robust to moderate variation in prior specification (uniform vs. half-normal vs. normal), which can be verified by robustness checks.
- The Jeffreys (1939/1961) cutoffs of 3 and 1/3 roughly correspond to a p of 0.05 when the obtained effect is near the predicted value, providing continuity with existing standards.

---

### Computational framework

The paper uses Bayesian inference, specifically Bayes factors as a measure of relative evidence between two hypotheses.

The Bayes factor B is the ratio of the likelihood of the data under the alternative hypothesis to the likelihood under the null:

B = p(data | H1) / p(data | H0)

The null hypothesis is a point null (population value = 0 by default). The alternative hypothesis is represented as a prior distribution over possible population parameter values — uniform, normal, or half-normal — whose parameters are set using domain knowledge (e.g., effect sizes from related conditions, logical constraints from the design). The Dienes (2008) calculator assumes the sampling distribution of the parameter estimate is normal with known variance (with a correction for small df).

The framework does not require commitment to full Bayesian inference (no posterior updating is required); the Bayes factor is treated as a standalone measure of evidential strength.

---

### Prevailing model of the system under study

The paper is not about a brain system or neural process; it is about statistical practice in psychology and related sciences. The prevailing practice the paper argues against is null hypothesis significance testing (NHST), in which non-significant results are routinely either (a) treated as evidence against a theory, or (b) dismissed as uninformative, without any principled basis for choosing between these interpretations. The paper's introduction characterises the field as stuck with p-values that cannot distinguish evidence for the null from data insensitivity, and notes that power and confidence intervals only partially remedy this. The introduction references Cohen (1990), Rosenthal (1993), Rouder et al. (2007), Greenwald (1993), and Pashler & Harris (2012) as indicators of the scope of the problem.

---

### What this paper contributes

The paper establishes Bayes factors as a practical, accessible tool that resolves the core interpretive problem with non-significant results. Concretely:

- It shows through simulation and worked examples that a high p-value can correspond to any of three evidential states (for null, for alternative, or insensitive), while Bayes factors cleanly separate these.
- It provides concrete rules of thumb for specifying alternative hypothesis distributions from existing data, logical constraints, or standardised effect sizes, reducing the perceived difficulty of applying Bayes in practice.
- It introduces a practical stopping rule framework (collect until B > 3 or B < 1/3) that is unavailable under NHST without pre-specification.
- It positions Bayes factors as complementary to (not a wholesale replacement of) NHST for near-term adoption: use orthodox statistics where required, add Bayes wherever non-significant results appear.
- Key unresolved questions noted: how to handle priors when no constraints exist; how to extend beyond one-degree-of-freedom contrasts; limits on sequential sampling strategies (see Sanborn & Hills, 2014; Rouder, 2014).

---

### Brain regions & systems

Not applicable. The paper is a methodological tutorial on statistical inference and does not target any specific brain region or neural system. The level of analysis is statistical/epistemological, applicable across all empirical sciences.

---

### Mechanistic insight

Does not meet the bar. The paper proposes and illustrates a statistical method (Bayes factors) for interpreting non-significant results. It does not present or formalise a computational algorithm for a psychological or neural process, nor does it provide neural data. The paper is a methodological contribution to statistical practice, not a mechanistic account of any cognitive or neural phenomenon.

---

### Limitations & open questions

- Specifying the prior for the alternative hypothesis requires scientific judgment; the approach is open to abuse if researchers reverse-engineer priors from observed effect sizes (explicitly prohibited but not mechanically preventable).
- The Dienes (2008) calculator assumes a normally distributed sampling distribution and is restricted to one-degree-of-freedom contrasts; extensions to complex hypotheses require other Bayesian tools.
- For very small sample sizes (df < 30), a correction to the SE is required; the paper notes this may overcorrect slightly.
- The approach does not incorporate uncertainty in the estimates used to set prior bounds (e.g., uncertainty in the maximum of a uniform), though the paper notes this typically strengthens, not weakens, conclusions already supporting the null.
- The relationship between the Jeffreys cutoffs (3, 1/3) and error rates is approximate and context-dependent; the cutoffs do not carry absolute frequentist guarantees analogous to alpha = 0.05.
- The paper focuses on t-test / F-test (one df) contexts; generalisation to more complex designs (multilevel models, mixed effects) is not demonstrated.

---

### Connections & keywords

**Key citations:**
- Jeffreys (1939/1961) — original Bayes factor framework and cutoffs
- Cohen (1988, 1990) — power analysis and critiques of NHST
- Rouder et al. (2009) — Bayes factors for psychology, default priors
- Kruschke (2010a, 2011, 2013) — Bayesian data analysis, inference by intervals
- Royall (1997) — likelihood inference and evidence
- Cumming (2011) — confidence intervals and "dance of the p-values"
- Wagenmakers (2007) — critique of p-values in psychology
- Gallistel (2009) — Bayes factors in neuroscience
- Dienes (2008) — online Bayes calculator and introductory text

**Named models or frameworks:**
- Bayes factor (Jeffreys)
- Dienes (2008) online Bayes factor calculator
- Null hypothesis significance testing (NHST)
- Inference by intervals (confidence intervals, credibility intervals)
- Sequential Bayes / optional stopping

**Brain regions:** None.

**Keywords:** Bayes factor, non-significant results, null hypothesis significance testing, statistical inference, prior distribution, half-normal prior, uniform prior, optional stopping, p-value, evidence strength, interval estimation, Type II error
