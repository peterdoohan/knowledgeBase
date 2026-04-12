---
source_file: greenacre2022_principal_component_analysis.md
paper_id: greenacre2022_principal_component_analysis
title: "Principal component analysis"
authors:
  - "Michael Greenacre"
  - "Patrick J. F. Groenen"
  - "Trevor Hastie"
  - "Alfonso Iodice D'Enza"
  - "Angelos Markos"
  - "Elena Tuzhilina"
year: 2022
journal: "Nature Reviews Methods Primers"
paper_type: review
contribution_type: methodological
keywords:
  - principal_component_analysis
  - singular_value_decomposition
  - biplot
  - dimensionality_reduction
  - low_rank_matrix_approximation
  - sparse_pca
  - correspondence_analysis
  - logratio_analysis
  - functional_pca
  - matrix_completion
  - missing_data_imputation
  - multivariate_statistics
  - principal
  - component
  - analysis
---

### One-line summary

A comprehensive methodological primer on principal component analysis (PCA), covering its mathematical foundations, biplot interpretation, variants (correspondence analysis, sparse PCA, logratio analysis), and modern applications to high-dimensional, missing, image, shape, and functional data.

---

### Background & motivation

PCA is one of the oldest and most universally applied multivariate analysis techniques, reducing a cases-by-variables data table to a small number of linear combinations (principal components) that maximally capture the total variance. Despite its ubiquity, best practices for standardisation, biplot scaling, dimensionality selection, and interpretation are often misunderstood or inconsistently reported. This Primer addresses that gap by providing a unified, rigorous treatment of PCA from definition through to cutting-edge extensions, intended to serve as a definitive reference for applied researchers and downstream computational consumers alike.

---

### Methods

- **Scope**: Narrative review of PCA theory, geometry, computation, and applications; covers standard PCA, correspondence analysis, logratio analysis, sparse PCA, multiple correspondence analysis, and functional PCA.
- **Exposition strategy**: Worked examples throughout using real datasets (World Happiness Report 2021 across 149 countries/territories, Khan child cancer gene-expression data of 63 samples × 2,308 genes, Barents Sea fish abundance data of 600 samples × 66 species, handwritten digit images, mosquito wing morphometrics, knee flexion gait curves).
- **Mathematical framework**: Derivation via eigenvalue decomposition (EVD) of the covariance/correlation matrix and via singular value decomposition (SVD) of the centred data matrix; formal statement of the low-rank least-squares approximation equivalence.
- **Computational extensions reviewed**: Truncated SVD, Lanczos and power methods for large-scale EVD; incremental/online SVD; iterative imputation for missing data (HardImpute, SoftImpute); sparse PCA via lasso and elastic-net penalties.
- **Variants covered**: Correspondence analysis (chi-square distance, profile analysis), canonical correspondence analysis, redundancy analysis, logratio analysis (LRA), multiple correspondence analysis, mixed/interval/symbolic data extensions, functional PCA.
- **Software**: R packages (stats, FactoMineR, ade4, easyCODA, vegan, elasticnet, irlba, softImpute, missMDA, fdapace) and Python (scikit-learn, NumPy) documented in a reference table.

---

### Key findings

- The first two principal components of the World Happiness Report data explain 47.0% and 24.5% of total variance (71.5% combined), with social support and healthy life expectancy as the dominant contributors to PC1 and generosity as the dominant contributor to PC2.
- Scree plot "elbow" criterion identifies these two dimensions as signal; formal methods (permutation tests, cross-validation, Bayesian selection) are reviewed.
- In the 63 × 2,308 child cancer gene-expression dataset, supervised PCA of group centroids separates all four tumour types cleanly, whereas unsupervised PCA shows substantial overlap (especially EW vs RM); sparse centroid PCA achieves comparable separation using only 72 and 79 non-zero genes on PC1 and PC2 respectively, sacrificing ~4 percentage points of explained variance.
- Canonical correspondence analysis of Barents Sea fish data (permutation test P = 0.003) reveals statistically significant temporal shifts in fish community composition between 1999 and 2004, driven by changes in shrimp, polar cod, haddock, and Norway pout relative abundances.
- SoftImpute (singular-value shrinkage) outperforms HardImpute for large-scale matrix completion (Netflix recommender data: 480,189 customers × 17,770 movies, 1% observed), avoiding overfitting at higher ranks.
- Functional PCA of 1,000 knee flexion gait curves reveals that PC1 is a size component (vertical shift) and PC2 is a shape/phase-shift component, jointly explaining the main modes of variation across patients.
- PCA of images (652 handwritten fours, 256-dimensional), shapes (126 mosquito wings, 200-dimensional), and 3D molecule reconstruction are demonstrated as viable applications after appropriate coding of objects as row vectors.

---

### Computational framework

**Framework**: Singular value decomposition (SVD) / eigenvalue decomposition (EVD); low-rank matrix approximation; dimensionality reduction.

**Core formalism**: Given a centred (and optionally column-standardised) data matrix **X** (n × p), the SVD decomposes it as **X = UDV**^T, where **D** is the diagonal matrix of singular values α_1 ≥ α_2 ≥ … ≥ 0, and **U**, **V** are orthonormal matrices of left and right singular vectors respectively. The first r columns of **UD** give the principal (row) coordinates; the first r columns of **V** give the standard (column/variable) coordinates. Eigenvalues λ_k = α_k^2 / n measure the variance explained by each PC. The total variance equals the sum of all eigenvalues, and PCA finds the rank-r approximation of **X** that minimises the residual sum of squares — equivalent to Eckart-Young optimal low-rank approximation.

**Key variables**: Singular values (parts of variance explained), left singular vectors (case scores), right singular vectors (variable loadings/directions), biplot coordinates (principal coordinates for rows, standard coordinates for columns), R² values (quality of approximation per variable), contributions (squared loading elements).

**Assumptions**: Linearity of the approximation; Euclidean (or modified Euclidean) geometry in variable space; variance as the measure of information (not distributional assumptions per se, though probabilistic PCA exists); column-centring is mandatory, column-standardisation is case-specific.

---

### Prevailing model of the system under study

The paper does not study a specific biological or neural system; it reviews PCA as a statistical methodology. The paper's introduction positions PCA as the canonical solution to the problem of summarising multivariate data: the prevailing model it builds on is the classical Pearson (1901)/Hotelling (1933) formulation of PCA as variance-maximising linear combinations, which had been consolidated in textbook form by Jolliffe (2002) and related authors. The introduction acknowledges that this classical framework is well established but that applied users face persistent difficulties with standardisation decisions, biplot interpretation, dimensionality selection, and extension to non-standard data types — the gap this Primer addresses. There is no competing theoretical account that the paper pushes against; rather, the paper consolidates, extends, and synthesises the current methodological landscape.

---

### What this paper contributes

As a methods primer, this paper establishes a unified, authoritative reference that:
- Clarifies the equivalence of the EVD and SVD computational pathways and their relationship to biplot scaling choices (principal coordinates vs standard coordinates).
- Provides explicit guidance on when and how to standardise variables, and on the geometric/spatial requirements for valid biplot interpretation (aspect ratio = 1, perpendicular projection).
- Integrates sparse PCA, correspondence analysis, logratio analysis, functional PCA, and matrix completion into a single conceptual framework centred on low-rank SVD approximation.
- Demonstrates that supervised PCA (of group centroids) is a special case of canonical/constrained analysis, distinct from Fisher's linear discriminant analysis in that it ignores within-group covariance.
- Establishes SoftImpute as superior to HardImpute for large-scale matrix completion, and motivates incremental/online SVD for streaming or memory-constrained settings.

Key unresolved areas noted: the debate over sparse PCA deflation strategies (Camacho et al. 2020, 2021); optimal stopping rules for dimensionality selection in noisy high-dimensional data; and the extension of functional PCA to irregular, sparse longitudinal observations.

---

### Brain regions & systems

Not applicable. The paper is a statistical methods primer with no anatomical focus. The level of analysis is purely mathematical/algorithmic — cases-by-variables data matrices of arbitrary domain. The closest neuroscience application mentioned is dimensionality reduction for neural population recordings (cited in passing: Pang et al. 2016, Curr. Biol.) and brain image PCA (Li et al. 2019), but these are cited as application domains, not analysed in the paper itself.

---

### Mechanistic insight

This paper does not meet the bar. It presents and formalises the PCA algorithm (a mathematical procedure), but it does not provide neural data — or any experimental data of its own — to support any specific algorithm over alternatives. The paper is a methodological review; its closest "mechanistic" contribution is the formal proof that SVD minimises the residual sum of squares (Eckart-Young theorem) and the algorithmic description of iterative imputation for missing data (Box 2), but these are mathematical results, not empirical findings about a neural or biological mechanism.

---

### Limitations & open questions

- **Standardisation**: No universal rule; user judgement required. Automatic standardisation is not built into most software, creating a common source of error.
- **Dimensionality selection**: Scree plot / elbow rule is heuristic; formal methods (cross-validation, Bayesian, permutation) disagree and remain an active research area.
- **Sparse PCA**: Still actively debated — choice of penalty, deflation strategy, and interpretation of sparse coefficients all lack consensus; the lasso and elastic-net approaches sacrifice orthogonality and the variance-decomposition property of classical PCA.
- **Computational scalability**: Full EVD/SVD is O(n p min(n,p)) in time and requires the full matrix in memory; incremental methods introduce approximation error whose properties depend on data streaming order.
- **Missing data**: The iterative imputation algorithm (Box 2) is infeasible for very large sparse matrices; SoftImpute is more scalable but requires tuning the shrinkage parameter.
- **Correspondence analysis for sparse data**: Sparsity of frequency matrices (e.g., 82.6% zeros in the Barents Sea data) can distort chi-square distances; acknowledged but not fully resolved.
- **Functional PCA**: Extension to sparse and irregularly sampled longitudinal data requires additional smoothing assumptions; noisy functional data may require explicit regularisation via smooth basis functions.
- **Non-linearity**: PCA is inherently linear; kernel PCA and nonlinear PCA extensions exist but are not covered in depth.

---

### Connections & keywords

**Key citations**:
- Pearson (1901) — original PCA formulation
- Hotelling (1933) — principal components
- Jolliffe (2002) — Principal Component Analysis textbook
- Eckart & Young (1936) — low-rank matrix approximation
- Gabriel (1971) — biplot
- Cattell (1966) — scree test
- Zou, Hastie & Tibshirani (2006) — sparse PCA
- Mazumder, Hastie & Tibshirani (2010) — SoftImpute / HardImpute
- ter Braak (1986) — canonical correspondence analysis
- Benzécri (1973) — correspondence analysis
- Ramsay & Silverman (2005) — functional PCA
- Khan et al. (2001) — child cancer gene-expression dataset

**Named models or frameworks**:
- Principal component analysis (PCA)
- Singular value decomposition (SVD)
- Eigenvalue decomposition (EVD)
- Biplot (principal coordinates + standard coordinates)
- Correspondence analysis (CA)
- Canonical correspondence analysis (CCA)
- Redundancy analysis (RDA)
- Logratio analysis (LRA)
- Multiple correspondence analysis (MCA)
- Sparse PCA (lasso / elastic-net penalties)
- Functional PCA
- HardImpute / SoftImpute algorithms
- Procrustes analysis (for shape alignment)

**Brain regions**: Not applicable.

**Keywords**: principal component analysis, singular value decomposition, biplot, dimensionality reduction, low-rank matrix approximation, sparse PCA, correspondence analysis, logratio analysis, functional PCA, matrix completion, missing data imputation, multivariate statistics
