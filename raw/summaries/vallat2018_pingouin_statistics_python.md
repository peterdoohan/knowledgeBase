---
source_file: vallat2018_pingouin_statistics_python.md
title: Pingouin: statistics in Python
authors: Raphael Vallat
year: 2018
journal: Journal of Open Source Software
paper_type: methodological
contribution_type: methodological
---

### One-line summary

Pingouin is an open-source Python package that provides easy-to-use functions for common statistical analyses, bridging the gap between Python and R in statistical capabilities.

### Background & motivation

Python is the fastest growing programming language for data science and machine learning, but it significantly lags behind R in general statistical analysis capabilities. This gap forces many scientists to rely on R for statistical analyses despite preferring Python for other aspects of their workflow. Pingouin was developed to partially fill this gap by providing a comprehensive, user-friendly statistical package native to Python.

### Methods

- **Software design**: Python 3 package built primarily on top of Pandas library for seamless integration into data analysis pipelines
- **Statistical functions implemented**:
  - Basic tests: ANOVAs, ANCOVAs, post-hoc tests, non-parametric tests
  - Effect sizes: various effect size measures
  - Advanced tests: Bayesian T-tests (Rouder et al., 2009)
  - Specialized correlations: repeated measures correlations (Bakdash & Marusich, 2017), robust correlations (Pernet et al., 2012)
  - Circular statistics (Berens, 2009)
- **Documentation**: Extensive API documentation and Jupyter notebook examples provided
- **Distribution**: Open-source package available to the scientific community

### Key findings

- Pingouin successfully provides a comprehensive set of statistical functions commonly used in scientific research, all within a Python environment
- The package integrates seamlessly with Pandas-based data analysis workflows, eliminating the need to switch between Python and R for statistical analysis
- Implementation includes both basic and advanced statistical methods, from standard ANOVAs to Bayesian T-tests and specialized correlation analyses
- The package addresses a significant gap in the Python scientific ecosystem, potentially reducing reliance on R for statistical analyses

### Computational framework

Not applicable. This is a software/methodological paper introducing a statistical package, not a computational modeling paper. The framework is a statistical computing library built on Python's scientific stack (Pandas, NumPy, SciPy).

### Prevailing model of the system under study

The prevailing situation before this work was that Python, despite its popularity in data science and machine learning, was considered inadequate for comprehensive statistical analysis compared to R. Many scientists maintained dual workflows: Python for data processing and machine learning, R for statistical testing. The implicit assumption was that Python's statistical ecosystem was insufficient for rigorous scientific work.

### What this paper contributes

This paper introduces Pingouin as a significant step toward making Python a viable standalone environment for statistical analysis. It demonstrates that a well-designed Python package can provide the statistical functionality that previously drove researchers to R. The contribution is primarily methodological: a practical tool that reduces workflow friction and expands Python's capabilities in scientific computing. The paper does not present new statistical theory but rather implements and makes accessible existing statistical methods within the Python ecosystem.

### Brain regions & systems

Not applicable. This is a methodological/software paper about statistical analysis tools, not a neuroscience study. The paper focuses on computational statistics and data analysis methods.

### Mechanistic insight

Not applicable. This paper does not address neural mechanisms or biological processes. It is a software paper introducing a statistical computing package. The paper does not present or test hypotheses about how neural systems work.

### Limitations & open questions

- The paper acknowledges that Python is still behind R in statistical capabilities, suggesting Pingouin is a partial solution rather than complete parity
- The scope is limited to specific statistical tests; many advanced statistical methods available in R may not yet be implemented
- Long-term maintenance and community adoption of the package remain open questions
- The paper does not provide empirical validation of the package's statistical accuracy against established implementations
- Integration with other Python scientific libraries and interoperability with R via rpy2 are mentioned as future directions

### Connections & keywords

- **Key citations**: Rouder et al. (2009) - Bayesian T-tests; Bakdash & Marusich (2017) - repeated measures correlations; Pernet et al. (2012) - robust correlations; Berens (2009) - circular statistics; McKinney (2010) - Pandas library
- **Named models or frameworks**: Pingouin statistical package, Pandas data analysis library, Bayesian hypothesis testing, robust statistics, circular statistics
- **Brain regions**: Not applicable
- **Keywords**: Python, statistics, open-source software, data analysis, ANOVA, correlation, Bayesian statistics, effect size, non-parametric tests, scientific computing, statistical software package
