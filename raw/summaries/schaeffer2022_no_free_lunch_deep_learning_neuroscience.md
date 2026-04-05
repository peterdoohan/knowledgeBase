---
source_file: schaeffer2022_no_free_lunch_deep_learning_neuroscience.md
title: "No Free Lunch from Deep Learning in Neuroscience: A Case Study through Models of the Entorhinal-Hippocampal Circuit"
authors: Rylan Schaeffer, Mikail Khona, Ila Rani Fiete
year: 2022
journal: bioRxiv (preprint, posted August 7, 2022)
paper_type: computational
contribution_type: methodological
---

### One-line summary
A large-scale hyperparameter study of deep learning models of grid cells shows that grid-like representations emerge only from a narrow, post-hoc set of implementation choices — not from the path integration objective itself — undermining the claim that such models reveal what the brain optimizes.

### Background & motivation
A series of prominent deep learning (DL) papers argued that training recurrent neural networks to perform path integration (estimating spatial position from velocity inputs) causes grid-cell-like representations to emerge, suggesting this reveals the brain's optimization objective. The authors question whether these results reflect fundamental truths about the entorhinal-hippocampal circuit or are instead artifacts of specific, unannounced implementation decisions — a concern motivated by analogous findings in deep reinforcement learning where results attributed to algorithms were later traced to implementation details.

### Methods
- Re-implemented and extended the public code from prior publications (Banino et al. 2018, Sorscher et al. 2019/2020, Nayebi et al. 2021).
- Trained more than 5,500 recurrent networks on a 2.2 m × 2.2 m arena path integration task.
- Conducted large-scale hyperparameter sweeps across: RNN architecture (RNN, LSTM, GRU, UGRNN), activation function (ReLU, Tanh, Sigmoid, Linear), optimizer (SGD, Adam, RMSProp), supervised readout target encoding (Cartesian, Polar, Gaussian, Difference-of-Gaussians/DoG, Difference-of-Softmaxes/DoS), loss function type, dropout, initialization, regularization, and random seed.
- For bump-like population readouts, additionally swept field width (σE), surround scale (s = σI/σE), number of fields per unit, and field width heterogeneity.
- Evaluated grid cell emergence using the gridness score (threshold set at 0.8 after showing that commonly used lower thresholds of 0.3–0.4 produce false positives) and position decoding error (<10 cm threshold for "optimal" encoding).
- Applied Fourier/Turing instability theory to explain why specific readout choices favor hexagonal pattern formation.

### Key findings
1. Almost all networks across all hyperparameter configurations learn to path integrate (decode position with <10 cm error), but the vast majority never develop grid-like representations.
2. Grid cell emergence is almost exclusively gated by the choice of supervised readout target: only the Difference-of-Softmaxes (DoS) encoding reliably produces grid cells; Cartesian, Polar, Gaussian, and true DoG targets do not.
3. The DoS encoding used in prior papers (Sorscher et al., Nayebi et al.) was not disclosed in the main texts — the published papers describe Difference-of-Gaussians but the released code uses Difference-of-Softmaxes.
4. Grid period is set entirely by the externally chosen σE hyperparameter, not by any intrinsic task property.
5. Multiple grid modules (a hallmark of biological grid cells, with period ratios ~1.4) do not emerge; networks learn only a single spatial period, and period ratios derived from sweeping σE are non-biological.
6. Adding biologically realistic heterogeneity to place cell readouts (multiple fields, multiple scales) abolishes grid cell emergence while preserving accurate path integration.
7. Standard grid scores (threshold 0.3–0.37) used in prior ANN work are unreliable: units with scores up to 1.3 can visually resemble non-grid patterns.

### Computational framework
Networks receive a 2D initial position and a sequence of 2D velocity inputs. Supervised learning (backpropagation through time) trains the recurrent hidden layer to produce, via a linear readout, an encoding of current 2D position. Encodings tested include low-dimensional Cartesian, high-dimensional Cartesian, Polar, Gaussian place-cell-like bumps, DoG bumps, and DoS bumps. Grid cell emergence in the hidden layer is assessed via spatial rate maps and the 60° gridness score. The theoretical explanation draws on the Turing instability / continuous attractor formalism: periodic spatial patterns emerge only when the readout correlation matrix (≈ recurrent weight matrix in a linearized approximation) has an inhibitory surround with sufficient power at non-zero spatial frequencies, a condition met by DoS but not by pure Gaussian or true DoG encodings.

### Prevailing model of the system under study
Grid cells in medial entorhinal cortex (MEC) are widely understood to arise from continuous attractor dynamics driven by translation-invariant recurrent connectivity with a difference-of-Gaussians lateral interaction profile. This mechanism explains path integration, toroidal population geometry, stability of pairwise cell-cell relationships across environments, and the discretization of grid cells into modules with fixed period ratios (~1.2–1.5). The hippocampus contains place cells with heterogeneous, often multi-field responses, and receives input from MEC grid cells. The prevailing DL narrative prior to this paper held that path integration as a training objective is sufficient to cause grid cells to emerge as the efficient representational solution.

### What this paper contributes
This paper provides a systematic, large-scale empirical rebuttal to the claim that path integration training causes grid cell emergence in ANNs. It demonstrates that: (a) the result depends on a specific, unrealistic, and undisclosed readout encoding (DoS), not the path integration objective; (b) grid cell properties (multiple modules, biologically realistic period ratios) are absent even when grid-like cells appear; (c) the grid score metric widely used in the field is unreliable at standard thresholds. The paper formalizes this as an informal "No Free Lunch" theorem for neuroscience DL models: without incorporating appropriate biological inductive biases and constraints, DL models cannot be expected to make novel, a priori predictions about neural tuning curves. The authors propose a list of biologically motivated loss function components (non-negativity, equivariance, high capacity, error correction, whitened representations) that may more robustly yield grid cells.

### Brain regions & systems
- Medial entorhinal cortex (MEC): site of grid cells
- Hippocampus (HPC): site of place cells; receives MEC input
- Entorhinal-hippocampal circuit / hippocampal formation

### Mechanistic insight
The key mechanistic insight is Fourier-theoretic: grid cell emergence requires the readout correlation matrix (which, in the linearized dynamics approximation, acts as the effective recurrent weight matrix) to have an inhibitory surround — placing Fourier power on an annulus at non-zero spatial frequency rather than at the origin. Pure Gaussian tuning curves cannot satisfy this condition; Difference-of-Softmaxes does (because the softmax normalization effectively sharpens the inhibitory surround relative to the excitatory center). This explains why the specific, unrealistic DoS encoding is uniquely capable of producing grid cells in these models, and why biologically realistic heterogeneous place cell readouts (which destroy the translational invariance of the correlation matrix) abolish grid emergence.

### Limitations & open questions
- The sweep, while large (>5,500 networks), could not cover the full hyperparameter volume; the search was deliberately biased toward configurations known to produce grid cells, meaning findings conservatively favor prior results.
- The paper does not present a positive model that robustly produces grid cells with biologically realistic constraints; the proposed loss function components (capacity, error correction, whitening) are hypotheses, not demonstrated results.
- It is unclear whether population-level dynamics (rather than single-unit tuning) might be more robustly predicted by path integration models, a point the authors acknowledge as a potentially more durable use of DL in neuroscience.
- The analysis focuses on supervised path integration; other architectures (e.g., successor representations, Tolman-Eichenbaum Machine) are noted but not systematically evaluated.
- Open question: what minimal set of biologically grounded loss terms and architectural constraints would cause grid cells to emerge robustly and as a novel prediction?

### Connections & keywords
grid cells, place cells, medial entorhinal cortex, hippocampus, path integration, deep learning, recurrent neural networks, continuous attractor networks, Turing instability, pattern formation, Difference-of-Gaussians, Difference-of-Softmaxes, hyperparameter sensitivity, inductive bias, No Free Lunch, gridness score, spatial navigation, neural coding, representational geometry, model criticism
