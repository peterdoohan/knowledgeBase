---
source_file: seabold2010_statsmodels_econometric.md
paper_id: seabold2010_statsmodels_econometric
title: "Statsmodels: Econometric and Statistical Modeling with Python"
authors:
  - "Skipper Seabold"
  - "Josef Perktold"
year: 2010
journal: "Proceedings of the 9th Python in Science Conference (SciPy 2010)"
paper_type: methodological
contribution_type: methodological
methods:
  - behavioral_analysis
keywords:
  - python
  - statistics
  - econometrics
  - statsmodels
  - open_source_software
  - statistical_modeling
  - generalized_linear_models
  - ordinary_least_squares
  - maximum_likelihood_estimation
  - regression_analysis
  - software_library
  - reproducibility
  - numerical_accuracy
  - scipy
  - numpy
  - time_series_analysis
  - statistical_computing
  - econometric
  - statistical
  - modeling
---

### One-line summary

Statsmodels is a Python library for statistical and econometric analysis that provides a consistent object-oriented API for estimation, inference, and post-estimation diagnostics, filling a gap in Python's statistical ecosystem.

---

### Background & motivation

While R dominates open-source statistics and proprietary software (Stata, SAS, MATLAB) remains prevalent in econometrics, there is growing demand for open-source alternatives that offer transparency and reproducibility. Python's strengths—simple syntax, extensive libraries, and general-purpose applicability—make it an attractive platform for statistical computing, but prior to statsmodels, Python lacked a comprehensive, R-like statistical modeling framework.

---

### Methods

The paper describes the design and implementation of the statsmodels library:

- **Development methodology**: Test-driven development (TDD) with results validated against established statistical software (R, SAS, Stata); distributed version control with code review via mailing lists
- **Core architecture**: Object-oriented design with base `Model` class having `endog` (endogenous/dependent) and `exog` (exogenous/independent) attributes; `LikelihoodModel` subclass for regression models; `Results` and `LikelihoodModelResults` classes for post-estimation outputs
- **Lazy evaluation**: Post-estimation statistics computed on-demand to avoid unnecessary computation
- **Available models**:
  - Regression: OLS, WLS, GLS (ordinary, weighted, generalized least squares)
  - GLM: Generalized linear models with 6 exponential family distributions and 10+ link functions
  - RLM: Robust linear models with 8 M-estimator norms
  - Discrete choice: Logit, Probit, MNLogit, Poisson (maximum likelihood framework)
  - Contrast analysis: Helper functions for linear contrasts
- **Diagnostic tools**: Tests for heteroskedasticity, autocorrelation, hypothesis testing for linear combinations
- **Utility features**: Publication-quality tables via `SimpleTable`, descriptive statistics, Stata .dta file import, 14 built-in example datasets

---

### Key findings

The paper demonstrates the library's capabilities through representative examples:

- **OLS example**: Using Longley's 1967 macroeconomic data (known for high multicollinearity, condition number 456,037), the `OLS` class fits the model and returns a `RegressionResults` object with extensive post-estimation statistics including parameters, standard errors, confidence intervals, R-squared, AIC, BIC, F-statistics, and diagnostic tests
- **GLM example**: Using Gill's education data from the 1998 California STAR program, a binomial GLM with logit link demonstrates modeling success/failure counts; the example shows how to compute interquartile differences in predicted probabilities (e.g., school districts at 75th vs 25th percentile of low-income households show an 11.88% difference in math test scores)
- **Hypothesis testing example**: Using Greene's econometric data, the paper demonstrates joint hypothesis testing via F-tests with linear restrictions (Rβ = q), rejecting the null hypothesis with F=194.44, p≈0
- **Table generation**: The `SimpleTable` class produces publication-ready ASCII and LaTeX output for presenting results

---

### Computational framework

Not applicable. This is a software library paper describing an implementation of classical statistical and econometric methods rather than proposing a new computational framework for understanding neural or cognitive processes. The methods implemented (OLS, GLM, maximum likelihood estimation) follow established frequentist statistical theory with optimization routines from SciPy.

---

### Prevailing model of the system under study

Not applicable. This paper describes a software tool rather than investigating a biological or cognitive system. The "prevailing model" in this context refers to the established landscape of statistical software: proprietary packages (Stata, SAS, MATLAB, SPSS) and the open-source R language dominate applied statistics and econometrics, while Python has lacked a comprehensive statistical modeling framework with a consistent, user-friendly API.

---

### What this paper contributes

The paper introduces statsmodels as a comprehensive Python library that:

- Provides an object-oriented, consistent API for statistical modeling in Python, lowering the barrier for users transitioning from R or proprietary software
- Implements a broad range of classical statistical and econometric models (OLS, GLM, robust regression, discrete choice) with extensive post-estimation diagnostics
- Fills a critical gap in the Python scientific ecosystem, complementing NumPy/SciPy with higher-level statistical modeling capabilities
- Establishes a development workflow (test-driven development, validation against established software) that ensures numerical accuracy and reproducibility
- Demonstrates through working code examples that Python can serve as a viable, open-source alternative for serious statistical and econometric research

The paper also outlines planned future development including time-series models, nonparametric methods, panel data models, and systems of equations, positioning statsmodels as an actively evolving project.

---

### Brain regions & systems

Not applicable. This paper describes a software library for statistical analysis; it does not investigate neural systems or brain function.

---

### Mechanistic insight

Not applicable. This is a software engineering/methods paper about implementing statistical algorithms, not a study of biological or cognitive mechanisms. The algorithms implemented (OLS, iteratively reweighted least squares for GLM, maximum likelihood estimation) are well-established computational procedures from the statistics literature, not novel mechanistic models of neural or cognitive processes.

---

### Limitations & open questions

- **Future development**: The paper acknowledges that statsmodels is "very much still a work in progress" and lists several models in development (time-series analysis, kernel density estimators, nonparametric regression, panel/longitudinal data models, systems of equations, information theory and maximum entropy models)
- **Scope limitations**: The current implementation focuses primarily on frequentist methods; the paper does not discuss Bayesian approaches
- **Software maturity**: Being a relatively new package, the API was still undergoing changes at the time of writing (the paper notes that "recent refactoring has changed the organization of the code")
- **Performance considerations**: The paper does not benchmark computational performance against established proprietary software or discuss optimization for large-scale datasets
- **Community building**: The authors explicitly invite "feedback, discussion, or contributions at any level," indicating ongoing need for community growth and validation

---

### Connections & keywords

**Key citations**:
- Altman & McDonald (2003) — replication and numerical accuracy in statistical software
- Bill Greene's *Econometric Analysis* — textbook source for hypothesis testing example
- Jeff Gill's *Generalized Linear Models: A Unified Approach* — textbook source for GLM example
- Longley (1967) — source of macroeconomic dataset for OLS example
- Cryer & Chan (2008), Kleiber & Zeileis (2008), Vinod (2008) — R textbooks for econometrics
- Choirat & Seri (2009) — "Econometrics with Python" advocacy paper
- Bilina & Lawford (2009) — Python for econometrics research
- Stachurski (2009) — Python-based economic dynamics textbook
- Isaac (2008) — Python for agent-based economic models

**Named models or frameworks**:
- Ordinary Least Squares (OLS)
- Generalized Least Squares (GLS)
- Weighted Least Squares (WLS)
- Generalized Linear Models (GLM)
- Robust Linear Models (RLM) with M-estimators
- Discrete choice models (Logit, Probit, Multinomial Logit, Poisson)
- Maximum likelihood estimation framework
- Test-driven development (TDD) methodology

**Brain regions**: Not applicable

**Keywords**: Python, statistics, econometrics, statsmodels, open source software, statistical modeling, generalized linear models, ordinary least squares, maximum likelihood estimation, regression analysis, software library, reproducibility, numerical accuracy, SciPy, NumPy, time series analysis, statistical computing
