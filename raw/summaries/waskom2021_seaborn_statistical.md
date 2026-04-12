---
source_file: "waskom2021_seaborn_statistical.md"
paper_id: "waskom2021_seaborn_statistical"
title: "seaborn: statistical data visualization"
authors: "Michael L. Waskom"
year: 2021
journal: "Journal of Open Source Software"
paper_type: "computational"
contribution_type: "methodological"
keywords: ["key_citations_tukey_1977", "hunter_2007", "mckinney_2010", "wickham_2014", "2016", "harris_et_al_2020", "cumming_and_finch_2005", "waskom_and_wagner_2017", "named_models_or_frameworks_matplotlib", "pandas", "numpy", "grammar_of_graphics_ggplot2", "tidy_data", "brain_regions_not_applicable", "keywords_data_visualization", "statistical_graphics", "python", "matplotlib", "declarative_api", "exploratory_data_analysis"]
---

### One-line summary

Seaborn is a Python library that provides a high-level, declarative interface for statistical data visualization built on matplotlib, with tight integration to pandas data structures.

### Background & motivation

Data visualization is essential for scientific understanding and communication, but matplotlib's low-level API can make common statistical visualization tasks cumbersome. For example, creating a scatter plot with marker size representing a numeric variable and marker shape representing a categorical variable requires manual transformations and loops. Seaborn addresses this gap by offering a dataset-oriented API that automates semantic mappings and statistical transformations while retaining access to matplotlib's flexibility for publication-quality figures.

### Methods

- **API design**: Declarative, dataset-oriented interface where users specify variables and plot types, and seaborn handles mapping data values to visual attributes (color, size, style)
- **Function classification**: Functions are either "axes-level" (add to existing matplotlib figures like pyplot) or "figure-level" (create new figures with faceting/conditional subplots)
- **Statistical transformations**: Built-in computation of means, medians, regression fits, kernel density estimates, histograms, with automatic 95% confidence interval error bars computed via bootstrap
- **Data format support**: Optimized for pandas DataFrames in "tidy" format, but also supports wide-form data, numpy arrays, and Python collections
- **Theming system**: Multiple built-in themes controlling style and scaling, implemented via matplotlib rcParams so they affect all matplotlib figures

### Key findings

- Seaborn provides a high-level interface that substantially reduces boilerplate code for common statistical visualizations compared to raw matplotlib
- The declarative API automatically handles semantic mappings (e.g., inferring qualitative vs. quantitative color scales based on data type)
- Figure-level functions enable faceting/conditional subplots with minimal syntax, automatically handling legend placement and subplot organization
- Integration with pandas enables efficient exploratory data analysis where variables can be reassigned to different plot roles without data modification
- The library exposes underlying matplotlib objects, allowing users to drop down to low-level customization when needed for publication-quality figures
- Default parameters are "opinionated" (e.g., 95% confidence intervals rather than standard errors) to facilitate "inference by eye"

### Computational framework

Seaborn implements a layered visualization framework built on top of matplotlib. The core abstraction is the separation between:
1. **Data layer**: pandas DataFrames or arrays holding the raw data
2. **Mapping layer**: Semantic mappings that bind data variables to visual attributes (position, color, size, style)
3. **Statistical layer**: Transformations applied to data before rendering (aggregation, estimation, regression)
4. **Rendering layer**: matplotlib primitives for actual drawing

The framework assumes a "tidy data" convention where each variable forms a column and each observation forms a row. This structure enables the declarative API: users specify what variables map to which aesthetics, and seaborn handles the data reshaping and looping internally.

### Prevailing model of the system under study

Before seaborn, the scientific Python visualization ecosystem was dominated by matplotlib, which provides a flexible but low-level API modeled on MATLAB's plotting interface. This approach requires users to manually handle data transformations, looping over categorical variables, and mapping data values to visual properties. The prevailing paradigm for statistical visualization involved either writing substantial boilerplate code in matplotlib or using R's ggplot2, which implements a formal Grammar of Graphics but requires switching languages. The gap was a Python-native, high-level statistical visualization library that could leverage the scientific Python stack while providing a more ergonomic API for common data analysis tasks.

### What this paper contributes

This paper introduces seaborn as a mature, stable library that bridges the gap between rapid exploratory data analysis and publication-quality figure generation in Python. The key contributions are:
- A declarative API that automates semantic mappings and statistical transformations, reducing the cognitive load and code verbosity for common visualization tasks
- Tight integration with pandas data structures that enables efficient exploration of multidimensional datasets through variable reassignment without data modification
- A two-level function hierarchy (axes-level and figure-level) that provides both granular control over individual plots and high-level faceting capabilities
- Opinionated defaults (e.g., bootstrap confidence intervals) that facilitate statistical inference through visual inspection
- Preservation of matplotlib compatibility that allows users to access low-level customization when needed, distinguishing seaborn from grammar-of-graphics systems like ggplot2

### Brain regions & systems

Not applicable. This is a software/methodology paper describing a data visualization library. The paper focuses on computational tools for statistical graphics rather than neural systems.

### Mechanistic insight

Not applicable. This paper does not provide mechanistic insights about neural computation or brain function. It describes a software tool for data visualization. The "mechanisms" described are at the software architecture level: the declarative API, semantic mapping system, and statistical transformation pipeline. These enable efficient data exploration but do not constitute claims about how the brain processes information.

### Limitations & open questions

- Seaborn does not implement a formal Grammar of Graphics like ggplot2, limiting its ability to produce arbitrary visualizations compared to grammar-based systems
- Complex multi-panel figures with arbitrary plot type combinations require falling back to matplotlib
- The declarative API trades some flexibility for convenience; users must occasionally drop to the matplotlib layer for fine-grained control
- Color palette selection, while flexible, requires user judgment as no universal defaults work for all data types and accessibility needs
- Wide-form data support is less ergonomic than long-form/tidy data, requiring more mental overhead to predict output

### Connections & keywords

- Key citations: Tukey (1977), Hunter (2007), McKinney (2010), Wickham (2014, 2016), Harris et al. (2020), Cumming & Finch (2005), Waskom & Wagner (2017)
- Named models or frameworks: matplotlib, pandas, numpy, Grammar of Graphics (ggplot2), tidy data
- Brain regions: Not applicable
- Keywords: data visualization, statistical graphics, Python, matplotlib, pandas, declarative API, exploratory data analysis, faceting, semantic mapping, bootstrap confidence intervals, tidy data, publication-quality figures
