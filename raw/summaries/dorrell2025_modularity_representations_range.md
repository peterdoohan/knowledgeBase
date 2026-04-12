---
source_file: dorrell2025_modularity_representations_range.md
paper_id: dorrell2025_modularity_representations_range
title: "Range, Not Independence, Drives Modularity in Biologically Inspired Representations"
authors:
  - "Will Dorrell"
  - "Kyle Hsu"
  - "Luke Hollingsworth"
  - "Jin Hwa Lee"
  - "Jiajun Wu"
  - "Chelsea Finn"
  - "Peter E. Latham"
  - "Tim Behrens"
  - "James C.R. Whittington"
year: 2025
journal: "International Conference on Learning Representations (ICLR 2025)"
paper_type: computational
contribution_type: theoretical
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - prefrontal_cortex
frameworks:
  - mixed_selectivity
keywords:
  - modularity
  - mixed_selectivity
  - nonnegative_representations
  - energy_efficiency
  - range_independence
  - source_support
  - disentangled_representations
  - grid_cells
  - entorhinal_cortex
  - recurrent_neural_networks
  - linear_autoencoder
  - convex_hull_modularisation_condition
  - range
  - not
  - independence
  - drives
  - biologically
  - inspired
  - representations
key_citations:
  - whittington2023_disentanglement_constraints
  - dorrell2023_actionable_grid_constraints
  - butler2019_reward_locations_entorhinal_maps
  - boccara2019_grid_goal_attractor
wiki_pages:
  - wiki/debates/grid_cells_as_a_mechanism_for_path_integration
---

### One-line summary

A normative theory of nonnegative, energy-efficient neural representations shows that modularity is governed by the "range independence" (rectangular support) of source variables, not by their statistical independence, and this principle explains puzzling differences in how entorhinal grid cells respond to space and reward across experimental paradigms.

---

### Background & motivation

Biological and artificial neural networks exhibit a striking dichotomy: some neurons encode single meaningful variables (modular or pure-tuned coding) while others are mixed-selective, responding to combinations of variables. Prior theory (Whittington et al., 2023) showed that statistical independence of source variables drives modularisation in biologically constrained linear autoencoders, but statistical independence is a very strong condition rarely satisfied in natural data. This left unexplained many empirical cases where modularisation occurs despite statistical dependence (e.g., grid cell modules) and cases where mixing appears in seemingly well-structured data (e.g., entorhinal reward–space representations). The paper addresses when, precisely, any given dataset will produce modular versus mixed representations under biological constraints.

---

### Methods

- **Model class**: Nonnegative, energy-efficient (L2 norm on activities and weights) linear autoencoders, motivated by the efficient coding hypothesis and ReLU networks with weight decay.
- **Main theoretical result**: Theorem 2.1 derives necessary and sufficient conditions on a finite sample of sources that determine whether the optimal biologically constrained linear autoencoder modularises. The conditions take the form of a set of inequalities depending on the support's extremal structure (joint minima/maxima of source pairs) and pairwise correlations; equivalently (Theorem 2.2), modularity holds iff the convex hull of the data encloses a data-derived ellipse defined by matrix F.
- **Key concept**: "Range independence" (or extreme-point independence) — sources are range independent if all extremal corner combinations are present in the data, making the support sufficiently rectangular.
- **Extensions**: Results generalised analytically to other activity norms (Appendix B.4) and multidimensional source variables such as angular variables on a 2D circle (Appendix B.5).
- **Empirical validation in nonlinear feedforward networks**: Three tasks — (1) a what-where regression task with binary images, (2) a nonlinear source autoencoding task, and (3) disentangled representation learning on Isaac3D images using QLAE — tested whether corner-cutting in source distributions degrades modularity relative to other distributional manipulations (correlation injection, central data removal).
- **Empirical validation in RNNs**: (1) Optimal nonnegative linear RNNs trained on sinusoidal regression, with analyses depending on frequency ratios (irrational, rational non-harmonic, harmonic); (2) nonlinear ReLU RNNs on a frequency-mixing task; (3) nonlinear teacher-student distillation RNNs with controlled source statistics.
- **Neuroscience application**: Linear RNNs trained to integrate actions and report self-position plus displacement from a reward, with reward placement varying from fully random to fully fixed, modelling the Butler et al. (2019) vs. Boccara et al. (2019) experimental contrast.
- **Modularity metric**: Conditional information-theoretic modularity (CInfoM), measuring conditional mutual information specialisation; normalised source multiinformation (NSI) used to quantify statistical dependence.

---

### Key findings

- **Necessary and sufficient conditions**: Modularity of the optimal biologically constrained linear autoencoder is determined by whether the convex hull of the data encloses the ellipse E (defined by matrix F derived from data extrema and correlations). This is strictly weaker than requiring statistical independence.
- **Range independence suffices**: If all pairwise extreme-point combinations exist in the dataset (range independence / rectangular support), the representation modularises regardless of statistical dependencies — sources can be strongly correlated and still produce modular representations.
- **Precision of theory**: A single missing datapoint at a corner of the support can switch the representation from modular to mixed, confirmed empirically.
- **Corner cutting, not correlation, drives mixing**: Across three nonlinear feedforward tasks, removing corner data induced substantially more mixing than introducing equivalent statistical dependence while preserving rectangular support, or removing central data.
- **RNNs and frequency ratios**: In linear sinusoidal RNNs, irrational frequency ratios produce range-independent supports and modularise; harmonic ratios produce large missing corners and mix; rational non-harmonic ratios preserve corners and modularise. These patterns replicate in nonlinear ReLU RNNs.
- **Grid cell modules**: The non-harmonic frequency structure of grid cell modules (Dorrell et al., 2023) is now formally justified as a consequence of range independence between constituent frequencies.
- **Space-reward modularisation in entorhinal cortex**: Butler et al. (2019) results (modular spatial and reward cells) arise because random reward scattering maintains range independence between space and reward; Boccara et al. (2019) results (mixed space-reward cells) arise because fixed reward locations eliminate corner combinations, creating range dependence. Linear RNN simulations reproduce this pattern as the proportion of fixed-reward environments varies.
- **Spurious mixed selectivity from missing variables**: When a neuron purely encodes a hidden third variable that is statistically dependent on two analysed variables, it will appear mixed-selective if the analyst does not condition on the third variable — a potential confound for analyses of entorhinal mixed selectivity (e.g., Hardcastle et al., 2017).

---

### Computational framework

The paper uses a **nonnegative linear autoencoder** framework inspired by the efficient coding hypothesis and biological constraints on neural firing:

- **What is modelled**: The encoding of a set of source variables s (factors of variation) into a nonnegative latent representation z, with reconstruction of s from z.
- **Key variables**: Source vectors s ∈ R^ds, latent activity z ∈ R^dz (dz > ds), encoding weights W_in, decoding weights W_out, biases b_in and b_out.
- **Objective**: Minimise a weighted sum of reconstruction error, L2 activity norm, and L2 weight norm, subject to z ≥ 0 (nonnegativity of firing rates).
- **Key assumptions**: (1) Firing rates are nonneg; (2) energy efficiency penalises both activity magnitude and weight magnitude; (3) perfect reconstruction is assumed in the main theory (relaxed in Appendix C to allow a reconstruction–efficiency tradeoff). The framework maps directly to neural networks with ReLU activations and weight decay.
- **Modularisation criterion**: Whether the optimal solution has each row of W_in with at most one non-zero entry (each neuron functionally dependent on at most one source).
- **Range independence**: A property of the data distribution's support — sources are range independent if for all pairs (j, j'), the joint minimum of each variable is achieved independently, i.e., the support's extremal corners are all populated.

---

### Prevailing model of the system under study

The paper addresses two intersecting debates. In the disentangled representation learning and mechanistic interpretability communities, the prevailing assumption — formalised in Whittington et al. (2023) — was that **statistical independence** of latent factors is the key condition under which biologically constrained networks produce modular (disentangled) representations. In neuroscience, the prevailing view of entorhinal cortex emphasised modular, pure-tuned neurons (grid cells encoding self-position, object-vector cells, heading cells) but faced a challenge from recordings showing mixed-selectivity (Hardcastle et al., 2017). The dominant theoretical account of mixed selectivity (Rigotti et al., 2013) attributed it to the computational advantage of nonlinear mixed codes for enabling flexible linear readouts. The introduction signals that the paper pushes against the statistical independence assumption and against the idea that mixed selectivity in entorhinal recordings always reflects a functional computation rather than a structural property of the source distribution.

---

### What this paper contributes

- Replaces the statistical independence condition with the strictly weaker **range independence (rectangular support) condition**, extending the theory to any dataset and making it testable by examining the data support rather than computing statistical dependence measures.
- Provides a precise geometric test for modularity: draw ellipse E from the data, check if the convex hull encloses it.
- Explains why **grid cell modules** exist by showing non-harmonic frequency ratios are range-independent and hence optimally modularised — formalising a previously intuitive argument.
- Resolves a **conflict between two entorhinal experiments**: Butler et al. (2019) and Boccara et al. (2019) differ in whether reward-position combinations are range independent, not just statistically dependent. This constitutes a concrete, experimentally grounded prediction from the theory.
- Raises a principled alternative to the nonlinear classification account of mixed selectivity: some apparent mixed selectivity is a statistical artifact of missing encoded variables, not a functional computation.
- Validates that the linear theory's qualitative trends transfer to nonlinear feedforward and recurrent networks, extending its practical scope substantially.

---

### Brain regions & systems

- **Medial entorhinal cortex** — primary focus; proposed to contain grid cells, object-vector cells, and heading direction cells whose modular vs. mixed coding patterns are explained by range independence of encoded variables.
- **Grid cells (entorhinal cortex)** — modular hexagonal spatial codes; their multi-module structure explained by range independence of non-harmonically related constituent frequencies.
- **Ventral and dorsal visual streams** — motivate the what-where regression task as a modular coding analogy, though no direct neural data from these streams are analysed.
- **Cerebellum, mushroom body, prefrontal cortex, hippocampus** — mentioned in the discussion as candidate loci where nonlinear mixed selectivity via the Rigotti et al. (2013) mechanism may genuinely operate, in contrast to entorhinal cortex.

---

### Mechanistic insight

The paper meets one criterion (it formalises an algorithm — the nonnegative efficient coding optimisation and the range independence condition that determines its output) but does not provide neural recording data directly supporting this specific algorithm over alternatives. It uses published experimental contrasts (Butler et al. vs. Boccara et al.) as convergent evidence for the theory's predictions, but does not collect new neural data.

Therefore, this paper does not fully meet the bar: it develops a normative computational model that predicts when neural representations should modularise, and it reconciles two conflicting datasets with its theoretical prediction, but the mechanistic link between the model's specific variables (source support geometry, the ellipse test, range independence) and measured single-unit activity has not been directly tested. Future experiments manipulating source support geometry while recording entorhinal neurons would be needed.

---

### Limitations & open questions

- Theory currently provides necessary and sufficient conditions only for the L2 activity norm and for 1-dimensional source variables in the main linear case; generalisation to other norms and multidimensional sources is only sufficient (not necessary).
- The main theory assumes perfect reconstruction; allowing a reconstruction–efficiency tradeoff causes very low-probability points to be discounted, but the full implications of this tradeoff are not explored.
- No extension to nonlinear networks: the nonlinear predictions are empirical generalisations of the linear theory, not derivations from it.
- The theory identifies a binary (modular vs. not) outcome; a graded theory of how mixed the optimal representation is remains to be developed.
- Biological factors not addressed include connection sparsity, anatomical constraints, noise, and additional computational roles of the network.
- Experimental validation in biological neural recordings is absent; the paper reconciles existing datasets but does not design new experiments to directly test the range independence mechanism.
- The "spurious mixed selectivity from missing variables" argument is illustrated with a simulation but not tested against real entorhinal recordings.
- Whether the non-harmonic frequency ratio results for RNNs extend fully to nonlinear settings is only partially shown.

---

### Connections & keywords

**Key citations**:
- Whittington et al. (2023) — predecessor theory based on statistical independence; directly extended and superseded
- Dorrell et al. (2023) — grid cell module emergence from minimal constraints; formalised in this work
- Hafting et al. (2005) — discovery of grid cells
- Stensola et al. (2012) — grid cell modules in rats
- Butler et al. (2019) — reward-space modular entorhinal recordings
- Boccara et al. (2019) — reward-space mixed-selective entorhinal recordings
- Rigotti et al. (2013) — nonlinear mixed selectivity for flexible readout
- Hsu et al. (2023, 2024) — QLAE disentangled representation learning
- Tatli and Erdogan (2021a,b) — polytopic matrix factorisation with sufficient spread conditions
- Hardcastle et al. (2017) — mixed selectivity in medial entorhinal cortex

**Named models or frameworks**:
- Nonnegative energy-efficient linear autoencoder (biologically inspired linear autoencoder)
- Quantised Latent Autoencoding (QLAE; Hsu et al., 2023)
- Conditional information-theoretic modularity metric (CInfoM)
- Normalised source multiinformation (NSI)
- Efficient coding hypothesis (Barlow, 1961)

**Brain regions**:
- Medial entorhinal cortex
- Grid cells
- Object-vector cells
- Heading direction cells
- Ventral visual stream (what pathway)
- Dorsal visual stream (where pathway)

**Keywords**: modularity, mixed selectivity, nonnegative representations, energy efficiency, range independence, source support, disentangled representations, grid cells, entorhinal cortex, recurrent neural networks, linear autoencoder, convex hull modularisation condition

### Related wiki pages
- [[wiki/debates/grid_cells_as_a_mechanism_for_path_integration|Grid cells as a mechanism for path integration]]
