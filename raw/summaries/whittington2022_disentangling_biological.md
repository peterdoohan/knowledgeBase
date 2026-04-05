---
source_file: whittington2022_disentangling_biological.md
title: "Disentangling with biological constraints: A theory of functional cell types"
authors: James C.R. Whittington, Will Dorrell, Surya Ganguli, Timothy E.J. Behrens
year: 2022
journal: Preprint (under review)
paper_type: computational
contribution_type: theoretical
---

### One-line summary

Simple biological constraints of nonnegativity and energy efficiency mathematically enforce disentangled neural representations where individual neurons become selective for single task factors, explaining the existence of distinct functional cell types in the brain.

---

### Background & motivation

Neuroscientists have long observed that neurons in higher brain areas exhibit finely tuned, interpretable responses to specific task variables (e.g., grid cells for spatial location, object-vector cells for relative object position), yet lacked a formal theory explaining why such disentangled representations emerge. Simultaneously, machine learning has pursued disentangled representations for improved interpretability and compositional generalization, but achieving disentangling typically requires explicit architectural inductive biases or complex training objectives. This paper bridges these gaps by proving that fundamental biological constraints—nonnegative firing rates and energy efficiency—naturally lead to disentangling without requiring explicit factorization objectives.

---

### Methods

- **Theoretical framework**: Proved two theorems showing that nonnegative neural representations with constrained activity energy naturally disentangle independent task factors
- **Simulation paradigm 1 (supervised learning)**: Trained shallow and deep linear/nonlinear networks on linearly mixed factor data with varying constraint combinations
- **Simulation paradigm 2 (unsupervised learning)**: Trained linear and nonlinear autoencoders on linear and nonlinear mixed data
- **Simulation paradigm 3 (VAE benchmark)**: Trained β-VAEs with ReLU constraints on Shapes3D dataset with MIG (mutual information gap) evaluation
- **Spatial navigation model**: Trained RNNs with path integration constraints on factorized vs. entangled spatial tasks
- **Disentangling metric**: Developed mutual information ratio (MIR) to measure when single neurons care about single factors (vs. standard MIG which measures if single factors are in single neurons)

---

### Key findings

- **Theorem 1**: For linear networks with nonnegative representations and fixed population variance, the minimum activity energy representations are disentangled (each neuron selective for at most one task factor)
- **Theorem 2**: When predicting entangled observations that are linear mixtures of hidden task factors, minimum energy nonnegative representations are disentangled, even without direct access to the underlying factors
- **Shallow supervised networks**: Only models with all three constraints (nonnegativity, activity energy minimization, weight energy minimization) learned disentangled representations; removing any constraint led to entanglement
- **Deep supervised networks**: With linear data, all layers disentangled; with nonlinear data, early layers remained mixed-selective while later layers disentangled (as they become more linearly related to task factors)
- **Autoencoders**: Both linear and nonlinear autoencoders with the biological constraints learned disentangled representations of the underlying task factors
- **VAE benchmark**: Models with ReLU and weight regularization achieved competitive MIG scores, often outperforming β-VAE baselines, while maintaining better reconstruction accuracy (Goldilocks region)
- **Cell type formation**: In spatial navigation tasks with factorized structure (objects can appear anywhere), distinct cell type modules emerged: grid cells for allocentric space and object-vector cells for relative object locations
- **Grid cell warping**: When tasks became entangled (objects fixed in consistent locations), grid cells warped toward objects—explaining experimental observations of reward-induced grid distortions
- **Sparsity is not sufficient**: Sparsity constraints alone do not promote disentangling; the key factor is nonnegativity, not sparsity induced by ReLUs

---

### Computational framework

**Framework**: The paper operates within the framework of **constrained optimization and representational learning**, with formal theorems proving that biological constraints induce specific representational structures.

**Core formalism**:
- Task factors **e** ∈ R^k: independent random variables representing ground truth factors of variation
- Neural representation **z** = M**e** + **b**_z: linear transformation of task factors with mixing weights M and bias
- Observation model **x** = D**e**: entangled observations as linear mixtures of hidden factors
- Generative model **x** = W**z** + **b**_x: neural representation predicting observations via read-out weights W

**Key constraints**:
1. **Nonnegativity**: z_i ≥ 0 for all neurons (enforced via ReLU or soft regularization)
2. **Activity energy**: Minimize E[||**z**||²] (expected squared L2 norm of neural activity)
3. **Weight energy**: Minimize ||**W**||²_F (Frobenius norm of read-out weights)

**Theoretical results**: Under these constraints, the minimum energy solutions are disentangled—each neuron becomes selective for at most one task factor (|M_jk||M_jl| = 0 for k ≠ l).

---

### Prevailing model of the system under study

The prevailing understanding in neuroscience was that neural representations in higher brain areas are shaped by task demands, but the specific structure of these representations (particularly why some neurons show highly selective, interpretable responses while others show mixed selectivity) was not well understood. The literature contained observations of both disentangled representations (e.g., grid cells, object-vector cells, axis-aligned face cells in IT cortex) and entangled mixed-selective representations (e.g., prefrontal cortex neurons, hippocampal conjunction cells), without a unified theory explaining when each should emerge.

In machine learning, disentangling was understood to require explicit architectural inductive biases (e.g., β-VAEs, factorized priors, supervised labels) and was thought to be impossible without strong inductive biases on either the data or model architecture. The prevailing view was that achieving disentangled representations required trading off reconstruction quality.

---

### What this paper contributes

This paper provides a **unified theoretical framework** that explains when and why neural representations disentangle or entangle, based on simple biological constraints rather than explicit architectural design.

**Theoretical contributions**:
1. **Mathematical proof** that nonnegativity and energy efficiency constraints enforce disentangling in linear networks—neurons naturally become selective for single task factors without explicit factorization objectives
2. **Generalization to hidden factors**: The theory extends to cases where networks only observe entangled mixtures of underlying factors, proving that optimal representations still disentangle the hidden factors
3. **Population variance boundedness**: Proved that population variance is bounded by read-out weight norms, connecting activity and weight energy constraints

**Empirical contributions**:
4. **Validated across architectures**: Demonstrated disentangling in shallow/deep networks, linear/nonlinear models, supervised/unsupervised learning, and VAEs
5. **Competitive benchmark performance**: Achieved strong MIG scores on standard disentangling benchmarks without explicit factorization losses
6. **Explained cell type formation**: Showed that spatial representations naturally partition into grid cells and object-vector cells under factorized task structures
7. **Explained grid cell warping**: Provided theoretical account for why grid cells warp toward rewards in some experiments but not others—warping occurs when space and rewards become entangled through stereotyped behavior

**Conceptual reframing**:
8. **Biological constraints as inductive bias**: Established that fundamental biological properties (nonnegative firing, metabolic energy minimization) serve as powerful inductive biases for interpretable representations
9. **Unified account of mixed vs. selective representations**: Explained both disentangled (grid cells, IT face cells) and entangled (PFC mixed-selectivity) representations within a single framework—disentangling occurs when task factors are independent and linear mappings are required; entangling occurs with nonlinear transformations or correlated factors
10. **Trade-off resolution**: Showed that biological constraints can achieve disentangling without sacrificing reconstruction quality, resolving the perceived trade-off in machine learning

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)**: Primary focus—contains grid cells and object-vector cells; theory explains why distinct cell types emerge for spatial vs. object-relative coding
- **Hippocampal formation**: Broader context for spatial navigation and memory; includes CA1, CA3, subiculum with border vector cells
- **Inferior temporal (IT) cortex**: Face processing region where neurons align to axes of data generative factors; cited as evidence of disentangling in biological systems
- **Prefrontal cortex (PFC)**: Region showing mixed-selective neurons; contrasted with disentangled representations to show when entangling vs. disentangling should occur
- **Parietal cortex**: Region with task-specific neurons; cited as another example of disentangled representations
- **Visual cortex**: Early visual areas where neurons are decorrelated; cited as supporting evidence for disentangling principles
- **Drosophila mushroom body**: Kenyon cells cited as example of mixed-selectivity through random projections for linear read-out

---

### Mechanistic insight

**The paper meets the high bar for mechanistic insight**, providing both formal algorithms and neural evidence linking the algorithm to biological data.

**Algorithm (Computational Level)**:
The brain solves the problem of representing task factors efficiently by minimizing expected neural activity energy subject to biological constraints. The formal objective is:
- Minimize E[||**z**||²] (expected L2 norm of neural activity)
- Subject to: z_i ≥ 0 (nonnegative firing rates)
- Subject to: **x** = W**z** + **b**_x (accurate prediction of observations)

**Algorithmic Level**:
The solution to this constrained optimization yields disentangled representations where each neuron becomes selective for at most one task factor. The key algorithmic insight is that nonnegativity forces the bias term to account for all negative contributions from mixed factors, which increases energy. Minimizing energy therefore drives the system toward representations where each neuron only encodes one factor, minimizing the required bias.

**Implementational Level**:
The theory explains specific biological implementations:
1. **Cell type formation**: Distinct cell types (grid cells, object-vector cells) emerge as separate neural modules when task factors (space, objects) are independent
2. **ReLU-like activation**: Nonnegative firing is implemented through rectified activation (ReLU-like) or metabolic constraints
3. **Energy efficiency**: Metabolic constraints minimize firing rates and synaptic weights
4. **Grid cell warping**: When tasks become entangled (rewards consistently in fixed locations), spatial representations warp to incorporate reward location—explaining empirical observations

**Neural evidence supporting the algorithm**:
- Grid cells and object-vector cells in entorhinal cortex form distinct non-overlapping populations (factorized representation of space vs. objects)
- IT cortex face cells align to axes of data generative factors (disentangled object features)
- Visual cortex neurons are decorrelated (energy efficient)
- PFC shows mixed-selectivity when tasks require nonlinear transformations or have correlated factors
- Grid cell warping toward rewards occurs when behavior becomes stereotyped around fixed reward locations (entangled task structure)

**Limitations in mechanistic insight**:
The paper acknowledges that it explains *when* and *why* disentangling occurs, but not *how* specific cell types acquire their characteristic response patterns (e.g., why grid cells have hexagonal firing fields specifically). A companion paper addresses this using group representation theory.

---

### Limitations & open questions

**Acknowledged limitations**:
1. **Limited to factor independence**: The theory assumes task factors are independent; how biological constraints affect representations of correlated factors is less clear
2. **Linear theory, nonlinear extensions**: The theorems are proven for linear networks; while empirical results show the principles extend to nonlinear networks, the formal guarantees do not
3. **Does not explain specific response patterns**: The theory explains why distinct cell types emerge but not why specific cell types have their characteristic patterns (e.g., hexagonal grid cells vs. other spatial codes)
4. **Fixed population variance assumption**: Theorem 1 assumes fixed population variance to prevent representational collapse; alternative constraints (like accurate prediction) are needed in more realistic settings

**Open questions raised**:
1. How do these constraints apply to neural dynamics and temporal representations, not just static spatial representations?
2. Can the theory be extended to hierarchical representations with multiple levels of abstraction?
3. How does the balance between disentangling and mixed-selectivity trade off in real neural circuits with multiple competing task demands?
4. What are the developmental mechanisms that implement these constraints during learning?
5. Can the theory explain why some brain regions (e.g., PFC) seem to favor mixed-selectivity while others (e.g., IT cortex) favor disentangling?

**Unresolved empirical puzzles**:
- The paper notes that grid cell warping toward rewards is observed in some experiments but not others; their theory explains this via task factorization, but more systematic testing is needed
- Mixed-selectivity in PFC is accommodated by the theory (as arising from nonlinear task demands) but the specific conditions favoring disentangling vs. entangling in PFC remain to be fully characterized

---

### Connections & keywords

**Key citations**:
- Hafting et al. (2005) - Discovery of grid cells (foundation for spatial navigation modeling)
- Høydal et al. (2019) - Discovery of object-vector cells (contrast with grid cells)
- Higgins et al. (2017a) - β-VAE for disentangling in machine learning (baseline comparison)
- Locatello et al. (2019) - Proof that disentangling requires inductive bias (theoretical context)
- Rigotti et al. (2013) - Mixed-selectivity in PFC (contrast phenomenon to explain)
- Boccara et al. (2019) and Butler et al. (2019) - Grid cell warping vs. stability observations (empirical puzzle addressed)
- Chang & Tsao (2017) and Bao et al. (2020) - Axis-aligned face cells in IT cortex (supporting evidence)

**Named models or frameworks**:
- β-VAE (beta-variational autoencoder) - Baseline disentangling method for comparison
- Mutual Information Ratio (MIR) - Novel metric introduced to measure disentangling at the neuron level
- Path integration - Structural constraint used in spatial navigation models
- Linear autoencoder - Theoretical framework for proofs
- Cellular automata - Analogy for pattern formation dynamics in spatial representations

**Brain regions**:
- Medial entorhinal cortex (MEC) - Contains grid cells and object-vector cells; primary modeling target
- Hippocampal formation - Broader spatial navigation and memory system
- Inferior temporal (IT) cortex - Face processing with axis-aligned representations
- Prefrontal cortex (PFC) - Mixed-selective neurons; contrast case for theory
- Parietal cortex - Task-specific neurons
- Visual cortex - Decorrelated neural representations
- Drosophila mushroom body - Kenyon cells with mixed-selectivity via random projections

**Keywords**:
- disentangled representations
- nonnegativity constraint
- energy efficiency
- grid cells
- object-vector cells
- functional cell types
- ReLU activation
- variational autoencoder
- mixed selectivity
- factorial task structure
- path integration
- neural population coding
- representational geometry
- biological constraints
- independent component analysis
- linear autoencoder
- pattern formation
- task factorization
- entorhinal cortex
- spatial navigation

---

**Filename mismatch note**: The source file was originally named `tanner2022_connectome.md` but has been renamed to `whittington2022_disentangling_biological.md` to match the actual paper content (first author: Whittington; year: 2022; keywords: disentangling, biological constraints).
