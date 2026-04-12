---
source_file: "dienes2014_bayes_factor.md"
paper_id: "dienes2014_bayes_factor"
title: "Using Bayes to get the most out of non-significant results"
authors: "Zoltan Dienes"
year: 2014
journal: "Frontiers in Psychology"
paper_type: "review"
contribution_type: "methodological"
frameworks: ["bayesian_inference"]
keywords: ["jeffreys_1939_1961_original_bayes_factor_framework_and_threshold_conventions", "rouder_et_al_2009_bayesian_t_tests_and_default_bayes_factors", "gallistel_2009_importance_of_proving_the_null", "bayes_factor_methodology", "royall_1997_likelihood_paradigm_and_stopping_rule_independence", "cumming_2011_dance_of_the_p_values", "confidence_interval_inference", "kruschke_2010a", "2013b_bayesian_data_analysis_and_rope_based_inference", "cohen_1988_statistical_power_analysis", "wagenmakers_2007_practical_critique_of_p_values", "dienes_2008", "2011_prior_bayes_factor_work_by_the_author", "named_models_or_frameworks", "dienes_2008_online_bayes_factor_calculator", "jeffreys_scale_of_evidence_b_3_b_1_3", "lindleys_paradox", "equivalence_testing_rogers", "howard_and_vessey", "1993"]
---

### One-line summary

Bayes factors provide a principled method for distinguishing genuine evidence for the null hypothesis from mere data insensitivity in non-significant results, overcoming the key limitations of power calculations and confidence intervals.

---

### Background & motivation

Non-significant results are routinely misinterpreted in empirical science: researchers either wrongly treat them as evidence against a theory, or dismiss them as uninformative. The problem is that a non-significant p-value conflates two distinct situations — data that genuinely support the null, and data that are simply too noisy to distinguish the null from the alternative. Power and confidence intervals each partially address this, but both require specification of a minimal interesting effect size, which is often the hardest aspect of a theory to pin down. This paper argues that Bayes factors resolve the ambiguity more flexibly and coherently, and provides a practical tutorial for their application.

---

### Methods

This is a methodological tutorial paper; there is no primary data collection. The approach is:

- Comparative analysis of three approaches to interpreting non-significant results: (1) power, (2) confidence/credibility intervals, (3) Bayes factors.
- Detailed worked examples drawn from published and illustrative datasets, covering uniform, normal, and half-normal prior distributions for the alternative hypothesis.
- Use of the Dienes (2008) online Bayes factor calculator (http://www.lifesci.sussex.ac.uk/home/Zoltan_Dienes/inference/bayes_factor.swf), which takes a parameter estimate (mean difference) and its standard error as input, alongside a user-specified prior distribution for the alternative.
- Three prior distributions considered: uniform (when a plausible maximum is known), normal (when a likely value is known and smaller deviations are also plausible), and half-normal (when a typical effect size is known and the prediction is directional).
- Discussion of robustness checks, stopping rules, small-df corrections, and extensions to meta-analysis, correlations, and contingency tables (Appendices 1–3).

---

### Key findings

- A p-value, however large, cannot by itself constitute evidence for the null hypothesis; it does not distinguish evidence from insensitivity.
- Bayes factors yield three distinct conclusions: evidence for the alternative (B > 3), evidence for the null (B < 1/3), or data insensitivity (1/3 ≤ B ≤ 3); Jeffreys' threshold of 3/1/3 roughly corresponds to the p = 0.05 criterion scientists are accustomed to.
- Power requires specifying the minimal interesting effect size — often the hardest quantity to justify — and cannot use the actual data to evaluate their sensitivity. Post-hoc observed power adds no information beyond the p-value.
- Confidence intervals can evaluate insensitivity using the data themselves, but asserting the null still requires specifying a null region (i.e., a minimally interesting value), just as power does.
- Bayes factors require specifying only a rough expected value or maximum plausible effect — quantities that are often easier to justify from prior data or design logic than the minimal interesting value.
- In worked examples, non-significant results sometimes yielded B indicating insensitivity (e.g., mood and implicit learning: B = 0.89), sometimes substantial evidence for the null (e.g., distraction–placebo additivity: B = 0.29; imagery vs active control after additional data: B = 11.45), demonstrating the method's discriminating power.
- Bayes factors are valid regardless of stopping rule: one can collect data sequentially until B > 3 or B < 1/3 without inflating error rates, unlike orthodox sequential testing.
- Bayes factors and confidence intervals are complementary: Bayes is most sensitive to a well-specified maximum; intervals are most sensitive when the minimum is known. Neither dominates in all cases.

---

### Computational framework

The paper applies Bayesian hypothesis testing via the Bayes factor. The Bayes factor B is defined as the ratio of the marginal likelihoods of the data under two hypotheses:

B = P(data | H1) / P(data | H0)

The null H0 places all probability mass at zero (point null). The alternative H1 is specified as a probability distribution over plausible population parameter values — uniform, normal, or half-normal — whose parameters are set using prior data, design constraints, or theoretical commitments. The Dienes (2008) calculator assumes the sampling distribution of the parameter estimate is Gaussian with known variance (appropriate when df > 30, with a correction for smaller samples). The framework does not require specifying prior odds over the two hypotheses, treating B alone as the measure of evidential strength. This approach bridges subjective Bayesianism (the prior over H1 encodes scientific judgment) and objective Bayesianism (distributions are derived from verifiable, public constraints rather than introspection).

---

### Prevailing model of the system under study

The paper addresses the prevailing framework of null hypothesis significance testing (NHST) as practised in psychology and adjacent sciences. The introduction characterises the dominant culture as one in which researchers dichotomise outcomes into significant and non-significant, treat the latter as grounds for either claiming null effects or as grounds for dismissing theories, without a coherent basis for either inference. Power is acknowledged as the orthodox corrective, but the paper treats it as underused and conceptually limited for the post-hoc evaluation of non-significant data. Confidence intervals are presented as an improvement recommended by the APA, but still insufficient in isolation. The paper's own theoretical landscape is one in which Bayesian methods are known in principle but not yet embedded in everyday practice — authors must still perform orthodox tests to satisfy reviewers, with Bayes offered as a supplement.

---

### What this paper contributes

The paper formalises the case that Bayes factors are the most practically tractable route to extracting useful conclusions from non-significant results. It provides a step-by-step tutorial across a range of real and representative experimental designs (between-subjects t-tests, interaction contrasts, paired comparisons, sequential data collection), making the method accessible to researchers with no prior Bayesian training. The key conceptual advance is demonstrating that the specification burden placed on Bayes — identifying a prior distribution for H1 — is actually lighter than that placed on power or interval methods, because it requires only a rough expected value or maximum rather than a minimally interesting value. The paper also makes explicit that the method is valid under optional stopping, which is not the case for orthodox sequential testing. By positioning Bayes as compatible with (rather than replacing) orthodox statistics, it proposes an incremental adoption path that requires no institutional revolution.

---

### Brain regions & systems

Not applicable. The paper is a statistical methods tutorial with no anatomical focus. The level of analysis is the experimental level in psychology broadly, with examples drawn from implicit learning, hypnosis, psychotherapy outcomes, and brain-computer interface research.

---

### Mechanistic insight

The paper does not meet the bar for this section. It proposes a statistical algorithm (Bayes factor computation) and illustrates it with behavioural and experimental data, but does not provide neural data of any kind. There is no mapping of the statistical framework onto neural mechanisms or Marr's levels in the sense relevant here.

---

### Limitations & open questions

- The Dienes (2008) calculator assumes normally distributed sampling distributions with known variance; it is limited to one-degree-of-freedom contrasts, and requires a small-df correction for samples with fewer than ~30 degrees of freedom.
- Specification of the prior distribution for H1 is unavoidably a matter of scientific judgment; the paper acknowledges that this opens the door to abuse (representing a theory in a way that flatters the obtained result). Transparency and public scrutiny are offered as the remedy.
- Researchers cannot use the obtained effect itself to set the scale of the prior — doing so double-counts the data.
- The approach does not exploit the full power of Bayesian inference (hierarchical modelling, posterior distributions, formal updating of prior odds), which the paper explicitly flags as a limitation.
- Robustness checks (sensitivity to choice of prior distribution shape) are recommended but not always feasible; when different representations yield qualitatively different conclusions, more data must be collected or ambiguity must be acknowledged.
- Whether the Jeffreys threshold of 3/1/3 is the right conventional cutoff is not rigorously justified; Lindley's paradox (B increasing support for null as N grows at fixed p = 0.05) is noted but not fully resolved.
- The paper acknowledges that Sanborn and Hills (2014) identify limits to the error-control properties of optional stopping with Bayes factors, though Rouder (2014) is cited in defence.

---

### Connections & keywords

**Key citations:**
- Jeffreys (1939/1961) — original Bayes factor framework and threshold conventions
- Rouder et al. (2009) — Bayesian t-tests and default Bayes factors
- Gallistel (2009) — importance of proving the null; Bayes factor methodology
- Royall (1997) — likelihood paradigm and stopping-rule independence
- Cumming (2011) — dance of the p-values; confidence interval inference
- Kruschke (2010a, 2013b) — Bayesian data analysis and ROPE-based inference
- Cohen (1988) — statistical power analysis
- Wagenmakers (2007) — practical critique of p-values
- Dienes (2008, 2011) — prior Bayes factor work by the author

**Named models or frameworks:**
- Dienes (2008) online Bayes factor calculator
- Jeffreys' scale of evidence (B > 3 / B < 1/3)
- Lindley's paradox
- Equivalence testing (Rogers, Howard & Vessey, 1993)
- Bayesian Information Criterion (BIC) — discussed in Appendix 2 as an alternative

**Brain regions:** None.

**Keywords:** Bayes factor, null hypothesis significance testing, non-significant results, statistical inference, prior distribution, half-normal prior, optional stopping, data sensitivity, type II error, confidence intervals, equivalence testing, Bayesian statistics
