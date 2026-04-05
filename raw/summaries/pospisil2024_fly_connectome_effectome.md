---
source_file: pospisil2024_fly_connectome_effectome.md
title: The fly connectome reveals a path to the effectome
authors: Dean A. Pospisil, Max J. Aragon, Sven Dorkenwald, Arie Matsliah, Amy R. Sterling, Philipp Schlegel, Szi-chieh Yu, Claire E. McKellar, Marta Costa, Katharina Eichler, Gregory S. X. E. Jefferis, Mala Murthy, Jonathan W. Pillow
year: 2024
journal: Nature
paper_type: computational
contribution_type: methodological
---

### One-line summary

The paper introduces a statistical framework (IV-Bayes) combining instrumental variables estimation with the fly connectome as a Bayesian prior to efficiently estimate the "effectome"—a causal model of how neurons affect each other in vivo.

### Background & motivation

A fundamental goal of neuroscience is to obtain a causal model of the nervous system. While the recently completed whole-brain fly connectome specifies synaptic paths by which neurons can affect each other, it does not reveal how strongly they actually affect each other in vivo. Direct causal inference from passive observation is confounded by unobserved variables (unobserved neurons, neuromodulators, measurement artifacts). Optogenetic perturbation offers a solution, but naively estimating all pairwise effects between ~10^5 neurons requires intractable data. The challenge is to develop an efficient experimental and statistical strategy to learn a causal model of the fly brain.

### Methods

- **Instrumental variables (IV) estimation**: Adapted from econometrics, using optogenetic stimulation as an instrumental variable that affects only opsin-expressing neurons and is independent of unobserved confounders
- **Connectome prior**: Used the FlyWire whole-brain connectome (v783) as a Bayesian prior on effectome weights—setting prior mean proportional to signed synapse count (positive for acetylcholine/dopamine, negative for GABA/glutamate/serotonin/octopamine), with variance equal to absolute mean plus a small constant
- **IV-Bayes estimator**: Combined IV approach with ridge regression biased toward the connectome prior; proved consistent (converges to ground truth even with incorrect prior)
- **Eigendecomposition analysis**: Decomposed the connectome weight matrix to identify "eigencircuits"—patterns of neural activity predicted to have largest effects on brain dynamics
- **Simulations**: 
  - Linear dynamical system simulations with 121,327 connected neurons
  - Conductance-based nonlinear neural dynamics model to validate that IV estimates converge to the Jacobian
  - Validation of opponent motion and winner-take-all circuit functionality

### Key findings

- The IV estimator provides consistent estimates of causal effects even with unobserved confounders, whereas standard least-squares regression shows large bias regardless of sample size
- IV-Bayes (using connectome prior) achieves several orders of magnitude faster convergence than raw IV: with maximal simulated samples, IV-Bayes explains ~90% of variance while raw IV still shows no positive variance explained
- The connectome's extreme sparsity (~0.01% of neuron pairs form synapses) enables strong priors that dramatically improve estimation efficiency
- Eigendecomposition reveals that fly brain dynamics are high-dimensional (eigenvalues decay slowly; 1000th eigenvalue ~1/10 of largest)
- Dominant eigencircuits are highly sparse: top 10 eigenvectors involve ~50 neurons (<0.05% of brain), 10th-100th involve ~500 neurons (<0.5%), 100th-1000th involve ~1500 neurons (<1.25%)
- Early eigenvectors are nearly orthogonal to others (operate independently), while later eigenvectors tend to co-occur
- First eigenvector localizes to lobula plate (visual system), recapitulating known opponent motion circuit (VCH, DCH, LPi15, Am1 neurons with mutual/directional inhibition)
- 45th eigenvector contains R4d ring neurons in ellipsoid body with complete mutual inhibition, implementing winner-take-all dynamics for visual spatial selection
- Only ~10% of top 1000 eigencircuits are anatomically localized; non-localized circuits often among the most dominant and robust

### Computational framework

**Instrumental variables (IV) estimation**: The core framework treats optogenetic stimulation as an instrumental variable that satisfies three key assumptions: (1) it directly affects only opsin-expressing neurons (source population), (2) it is independent of all unobserved confounders, and (3) it affects the target population only through its effect on the source population. Under these assumptions, the correlation between the instrument (laser) and outcome (target neuron activity) isolates the causal effect of interest,不受未观测变量影响.

**Linear dynamical systems (LDS)**: Neural dynamics are modeled as a first-order vector autoregressive process: r_t = W·r_{t-1} + noise, where W is the effectome matrix capturing causal effects between neurons. The IV estimator converges to this W even with correlated unobserved noise.

**Bayesian ridge regression (IV-Bayes)**: The estimator combines the IV approach with a Gaussian prior on effectome weights. The prior mean is set proportional to signed synaptic counts from the connectome, with variance scaling with the absolute mean. This biases estimates toward anatomically plausible values while remaining consistent (converging to truth with enough data even if prior is wrong).

**Eigendecomposition for circuit discovery**: The connectome weight matrix is decomposed into eigenvectors (patterns of neural activation) and eigenvalues (determining dynamics timescales). Eigenvectors with large eigenvalues represent "eigencircuits" predicted to dominate brain dynamics. The sparsity of these eigenvectors guides experimental prioritization.

### Prevailing model of the system under study

Before this work, the prevailing understanding was that the fly connectome provides a static anatomical wiring diagram specifying which neurons can potentially affect each other, but not the functional strengths of these interactions. The field recognized that causal relationships cannot be inferred from passive observation alone due to unobserved confounders. While optogenetic perturbation was recognized as a potential solution, there was no clear approach for using it to obtain a complete causal model of neural activity, especially given the intractable data requirements for estimating all pairwise interactions among ~10^5 neurons. The introduction explicitly frames this gap: "a clear approach for how to use these tools to obtain a causal model of neural activity has not emerged."

Additionally, the prevailing view of fly brain dynamics was that they might involve complex global communication patterns, as suggested by graph-theoretic analyses showing the fly brain is a "small-world network" with short paths between almost any pair of neurons. This implied potentially highly effective global communication. The modular, sparse eigencircuit structure proposed in this paper represents a shift from this view.

### What this paper contributes

This paper introduces a complete framework for learning a causal model of the fly brain (the "effectome"), combining statistical methodology (IV-Bayes), computational analysis (connectome eigendecomposition), and experimental guidance. The key contributions are:

1. **IV-Bayes estimator**: A novel statistical estimator that combines instrumental variables with Bayesian priors from the connectome. It is consistent (converges to ground truth even with wrong prior) yet orders of magnitude more efficient than naive IV regression. This enables feasible estimation of the effectome despite the ~10^10 potential parameters.

2. **Connectome as a prior**: Demonstration that the fly connectome's extreme sparsity (~0.01% connected pairs) provides a powerful prior that dramatically improves estimation efficiency. The prior is weighted by signed synapse counts, with flexibility for the data to override incorrect prior assumptions.

3. **Eigencircuit discovery framework**: A data-driven method for identifying "eigencircuits"—small populations of neurons predicted to dominate whole-brain dynamics—through eigendecomposition of the connectome. This provides a principled way to prioritize experiments.

4. **Discovery of sparse, independent dynamics**: Analysis revealing that dominant eigencircuits are highly sparse (top modes involve <0.05% of neurons) and operate largely independently (early eigenvectors are nearly orthogonal). This suggests whole-brain dynamics can be explained by a collection of small, separable circuits rather than complex global interactions.

5. **Specific circuit predictions**: Two detailed circuit predictions: (a) The first eigenvector recapitulates a known opponent motion circuit in the lobula plate (VCH, DCH, LPi15, Am1), validating the approach. (b) The 45th eigenvector identifies an R4d ring neuron circuit in the ellipsoid body with winner-take-all dynamics, providing a novel mechanistic hypothesis for visual spatial selection.

6. **Experimental roadmap**: Specification of the sufficient experimental setting for learning the effectome: sparse subset imaging/stimulation, voltage imaging, holographic stimulation at neuronal timescales, and connectome identification of recorded cells.

The paper thus shifts the prevailing model from "small-world" global communication to a view of largely independent, sparse eigencircuits, and provides a concrete path to experimentally validate this framework.

### Brain regions & systems

- **Lobula plate** (visual system): Contains the opponent motion circuit (VCH, DCH, LPi15, Am1 neurons) identified in the first eigenvector; 75% of synapses in this eigencircuit localized here
- **Ellipsoid body** (central complex): Contains R4d ring neurons identified in eigenvector 45; 99% of synapses localized here; implements winner-take-all dynamics for visual spatial selection
- **Mushroom body**: Identified in top olfactory eigenvectors; involved in olfactory processing
- **Antennal lobe**: Source of projection neurons to lateral horn; identified in olfactory eigenvectors
- **Lateral horn**: Receives projection neurons from antennal lobe; involved in olfactory processing
- **Inferior posterior slope**: Secondary location of synapses from the opponent motion eigencircuit
- **Fan-shaped body**: Minor secondary location (1% of synapses) for R4d ring neuron eigencircuit
- **Mushroom body medial lobe**: Minor secondary location for R4d ring neuron eigencircuit
- **Optic lobes**: General visual processing region containing multiple eigencircuits
- **Pre-motor regions**: Identified in non-localized eigencircuits connecting visual and motor systems

### Mechanistic insight

This paper meets the high bar for mechanistic insight: it presents a formal algorithmic framework and validates it through neural simulations that demonstrate how specific connectivity patterns implement computations.

**Computational level**: The brain must estimate causal effects between neurons despite unobserved confounders. The paper frames this as an instrumental variables problem where optogenetic stimulation serves as an instrument that isolates causal effects from correlations induced by common inputs.

**Algorithmic level**: The solution combines two key algorithms:
1. **IV estimation**: Uses the relationship between laser stimulation (instrument) and target neurons to estimate causal effects, bypassing confounds. The two-stage least squares (2SLS) approach first predicts source neuron activity from laser, then predicts target activity from predicted source activity.
2. **IV-Bayes**: Incorporates the connectome as a Gaussian prior on effectome weights. The prior mean is proportional to signed synaptic counts, with variance scaling with the absolute mean. This biases estimates toward anatomically plausible values while remaining consistent (converging to truth with sufficient data even if prior is wrong).

**Implementational level**: The paper validates through conductance-based neural simulations that the IV estimator converges to the **Jacobian** of the neural dynamics—capturing how small perturbations propagate through the network at specific voltage states. Key biophysical findings:
- The Jacobian between unconnected neurons is always zero, justifying the connectome prior (only 0.01% of pairs are connected in the fly brain)
- Two specific circuits were analyzed in detail at the implementation level:
  1. **Opponent motion circuit (lobula plate)**: VCH, DCH, LPi15, Am1 neurons with mutual/directional inhibition implement opponent motion computation across the fly's eyes. When stimulated unilaterally, VCH/DCH remain active; when stimulated bilaterally, they inhibit each other.
  2. **Winner-take-all circuit (ellipsoid body)**: R4d ring neurons with complete mutual inhibition implement WTA dynamics for visual spatial selection. Simulations show that the neuron with strongest input suppresses all others, enabling selection of specific visual angles.

The paper thus provides a complete Marr's three-level analysis connecting the computational problem (causal inference with confounds), through the algorithmic solution (IV-Bayes with connectome prior), to implementational validation (Jacobian estimation and specific circuit simulations).

### Limitations & open questions

- The method assumes a linear dynamical system, whereas real neural dynamics are highly nonlinear; the paper shows IV estimates converge to the local Jacobian but extending to full nonlinear dynamics remains future work
- The connectome provides a prior mean but does not capture extrasynaptic effects (e.g., neuropeptide signaling, gap junctions), which could cause the prior to be misspecified for some connections
- The eigencircuits identified are predictions based on the connectome prior, not experimentally validated effectome estimates; the actual effectome may differ substantially if anatomical weights do not match functional strengths
- The experimental setting required for full effectome estimation (sparse imaging/stimulation, voltage imaging, holographic stimulation at neuronal timescales, connectome identification) has not yet been achieved simultaneously in practice
- The paper assumes a first-order VAR model with fixed 1ms timescale; slower effects (e.g., through extrasynaptic pathways) would require higher-order autoregressive models
- Natural variation between individual flies' connectomes could make the connectome prior less accurate for any specific fly
- The approach has been validated only in simulation; experimental validation in real flies remains to be done
- The relationship between effectome estimates and behavior requires integrating with models of how descending motor neurons actuate the body
- How to use local Jacobian estimates to learn about changes in state (e.g., synaptic plasticity) remains an open question

### Connections & keywords

**Key citations:**
- Dorkenwald et al. (2024) — FlyWire whole-brain connectome
- Zheng et al. (2018) — EM volume of adult Drosophila brain
- Schlegel et al. (2024) — Whole-brain annotation and multi-connectome cell typing
- Angrist, Imbens & Rubin (1996) — Foundational IV methods in statistics
- Jazayeri & Afraz (2017) — Navigating neural space in search of the neural code
- Das & Fiete (2020) — Systematic errors in connectivity inferred from activity
- Marinescu, Lawlor & Kording (2018) — Quasi-experimental causality in neuroscience
- Lin et al. (2024) — Network statistics of whole-brain Drosophila connectome
- Eckstein et al. (2024) — Neurotransmitter classification from EM images
- Varshney et al. (2011) — Structural properties of C. elegans neuronal network
- Shinomiya et al. (2022) — Neuronal circuits integrating visual motion in Drosophila
- Seelig & Jayaraman (2013) — Feature detection in Drosophila central complex
- Turner-Evans et al. (2020) — Neuroanatomical ultrastructure of biological ring attractor
- Hulse et al. (2021) — Connectome of Drosophila central complex

**Named models or frameworks:**
- Instrumental Variables (IV) estimation
- Two-Stage Least Squares (2SLS)
- IV-Bayes estimator (connectome prior + Bayesian regression)
- Vector Autoregressive model (VAR(1))
- Connectome prior / effectome prior
- Eigencircuits (eigenvector-based circuit decomposition)
- Winner-take-all (WTA) computation
- Opponent motion computation
- Linear dynamical systems (LDS)
- Conductance-based neural dynamics model
- Jacobian estimation

**Brain regions:**
- Lobula plate (visual system)
- Ellipsoid body (central complex)
- Mushroom body
- Antennal lobe
- Lateral horn
- Inferior posterior slope
- Fan-shaped body
- Optic lobes
- Pre-motor regions
- Ventral nerve cord (mentioned as potential confound)

**Keywords:**
- Causal inference
- Instrumental variables
- Connectome
- Effectome
- Whole-brain dynamics
- Drosophila
- Optogenetics
- Bayesian estimation
- Eigendecomposition
- Sparse neural circuits
- Winner-take-all dynamics
- Opponent motion
- Linear dynamical systems
- Jacobian estimation
