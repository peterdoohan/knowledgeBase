---
source_file: "tang2024_learning_grid_cells_predictive.md"
paper_id: "tang2024_learning_grid_cells_predictive"
title: "Learning Grid Cells by Predictive Coding"
authors: "Mufeng Tang, Helen Barron, Rafal Bogacz"
year: 2024
journal: "Computational Biology / Conference Proceedings (ICLR)"
paper_type: "computational"
contribution_type: "theoretical"
tasks: ["navigation_task"]
brain_regions: ["hippocampus", "hippocampus_ca1", "entorhinal_cortex", "medial_entorhinal_cortex", "visual_cortex"]
frameworks: ["attractor_networks"]
keywords: ["learning", "grid", "cells", "predictive", "coding"]
key_citations: ["sorscher2023_grid_cells_unified_theory", "dordek2016_grid_cells_pca", "burak2009_path_integration_grid_cells"]
---

### One-line summary

Grid cells emerge naturally in predictive coding networks trained with biologically plausible Hebbian plasticity rules, extending predictive coding theory from visual cortex to hippocampal spatial representations.

---

### Background & motivation

Grid cells in the medial entorhinal cortex (MEC) exhibit striking hexagonal firing patterns and are learned after birth, but the biologically plausible learning mechanisms underlying their development remain unclear. While recurrent neural networks (RNNs) trained with backpropagation through time (BPTT) can develop grid cells, BPTT is biologically implausible. This paper addresses whether predictive coding—a biologically plausible learning rule with local Hebbian plasticity that explains visual cortical representations—can also account for grid cell learning.

---

### Methods

- **Model 1: Sparse Non-negative PCN**: Classical 2-layer predictive coding network with L2 and L1 sparsity constraints on latent activities, trained on static place cell inputs (900 locations, 512 place cells, 256 latent neurons). Inference uses ReLU-constrained dynamics.

- **Model 2: Temporal PCN (tPCN)**: Dynamical extension with recurrent connections trained on path integration tasks. Model receives velocity inputs and sequences of place cell activations from simulated random walk trajectories (50,000 trajectories, 512 place cells, 2048 latent neurons). Uses iterative inference (20 iterations) and local Hebbian learning rules.

- **Comparative analysis**: Compared tPCN performance with RNNs trained by BPTT and 1-step truncated BPTT (tBPTT) on path integration accuracy and grid cell emergence.

- **Robustness testing**: Varied place cell encoding (Gaussian vs. DoS), activation functions (ReLU vs. tanh), environment sizes (1.2m to 1.8m), latent layer sizes (256-2048), and presence/absence of velocity inputs.

---

### Key findings

- Sparse non-negative PCNs develop hexagonal grid cell-like representations in their latent layer when trained on static place cell inputs, with grid scores comparable to non-negative PCA (Figure 2).

- Both sparsity (L1 constraint) and non-negativity (ReLU) are necessary for hexagonal grid emergence; removing either produces amorphous firing fields.

- tPCN successfully performs path integration with performance comparable to RNNs trained by BPTT, though accuracy slightly decreases at higher simulated speeds (Figure 3A-B).

- tPCN develops hexagonal grid representations in its latent layer during path integration, with grid scores comparable to or exceeding those of BPTT-trained RNNs, especially at higher movement speeds (Figure 3C-G).

- Analytically, tPCN's learning rule approximates 1-step truncated BPTT (tBPTT) but with a critical difference: tPCN uses inferred past states rather than forward-propagated states, creating an eligibility trace that allows temporal credit assignment without unrolling (Equations 12-13).

- Grid cell emergence in tPCN is robust across: different output nonlinearities (softmax, tanh), environment sizes, and latent layer sizes. However, Gaussian (rather than DoS) place cell inputs abolish hexagonal grids, and removing velocity inputs severely impairs path integration performance but grid cells still emerge.

- Grid cells can emerge even in models unable to perform path integration (without velocity inputs), suggesting path integration is not a necessary condition for grid cell formation.

---

### Computational framework

**Predictive Coding**: The paper uses predictive coding networks (PCNs), a biologically plausible framework where learning minimizes prediction error through local computation and Hebbian plasticity. The core formalism involves:

- **Generative model**: Place cell inputs **p** are predicted from latent grid cell activities **g** via **p** ≈ **Wg** (for static PCN) or dynamic predictions in tPCN.

- **Loss function**: Minimizes squared prediction error plus sparsity constraints (L2 norm and L1 norm on latents).

- **Inference**: Latent activities **g** are optimized via gradient descent on the loss (EM algorithm), with ReLU constraints ensuring non-negativity.

- **Learning**: Weight updates use Hebbian plasticity based on prediction errors and local activities, avoiding backpropagation's non-local requirements.

**Temporal Predictive Coding (tPCN)**: Extends PCN to dynamic stimuli with recurrent connections, processing sequences via iterative inference that approximates Kalman filtering. The framework maps naturally to hippocampal circuitry with distinct roles for excitatory neurons, interneurons, and error neurons.

---

### Prevailing model of the system under study

The field has developed several computational accounts for grid cell formation:

1. **Oscillatory interference models**: Proposed that grid cells arise from interference between somatic and dendritic membrane potential oscillations in MEC pyramidal neurons. These require specialized biophysical mechanisms and unrealistically large numbers of oscillatory networks.

2. **Recurrent attractor networks**: Hand-tuned recurrent connectivity with center-surround structure can generate grid patterns and perform accurate path integration. However, these models lack an explanation for how the specific recurrent weights develop through learning.

3. **RNN models trained by backpropagation**: Recent work showed that RNNs trained on path integration tasks develop grid-like representations, providing a normative task-driven account. However, BPTT is biologically implausible, requiring unrolling through time and storing all past hidden states.

4. **Non-negative PCA**: Theoretical work showed that grid cells emerge as non-negative principal components of place cell inputs. While this can be learned with biologically plausible Sanger's rule, PCA lacks generalizability to other brain regions and temporal tasks like path integration.

The prevailing view is that grid cells emerge from optimizing spatial computation, but the biologically plausible learning mechanism—particularly one that generalizes across cortical regions—remains unidentified.

---

### What this paper contributes

This paper establishes predictive coding as a biologically plausible, unified learning mechanism for grid cell formation that addresses limitations of prior models:

1. **First demonstration of grid cells via predictive coding**: Shows that classical PCNs with sparse, non-negative constraints develop hexagonal grid representations as latent codes of place cell inputs, matching the performance of non-negative PCA but with greater biological plausibility and generalizability.

2. **Extension to temporal predictive coding (tPCN)**: Demonstrates that tPCN develops grid cells during path integration tasks using only local Hebbian plasticity, avoiding the biological implausibility of BPTT. tPCN performance matches or exceeds BPTT-trained RNNs, especially at higher movement speeds.

3. **Theoretical unification**: Analytically shows that tPCN approximates truncated BPTT with a crucial difference—using inferred past states creates an eligibility trace for temporal credit assignment without unrolling. This explains why grid cells can emerge without backpropagation's biological requirements.

4. **Biological circuit mapping**: Maps tPCN components to MEC-hippocampal circuitry: grid cells as latent representations, interneurons encoding eligibility traces, error neurons in CA1 detecting mismatches, and bidirectional connectivity between regions.

5. **Robustness and dissociation findings**: Shows grid cell emergence is robust across architectures but critically depends on DoS place cell inputs and non-negative constraints. Crucially, demonstrates that grid cells can emerge even without velocity inputs (impaired path integration), suggesting path integration is not necessary for grid cell formation—only self-motion information is required.

The paper extends predictive coding theory from visual cortex to hippocampal spatial representations, proposing a unified learning algorithm that could operate across diverse cortical regions.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)**: Primary focus—contains grid cells that emerge as latent representations in the predictive coding models. The paper maps MEC layer II circuitry to the tPCN architecture, with pyramidal cells as grid cells (latent representations **g**), interneurons encoding past states (eligibility trace **ĝ**_{t-1}), and lateral inhibition mediating error computation.

- **Hippocampus (CA1)**: Proposed locus of error neurons **ε**^{p}_{t} that encode mismatch between place cell activities and grid cell predictions. The paper cites evidence that CA1 serves as a mismatch detector between hippocampus and cortex, and predicts that error neurons in CA1 specifically encode spatial prediction errors during navigation.

- **Hippocampal place cells**: Input layer to the models—provide spatial position encoding that drives grid cell learning. The paper assumes grid cells develop as latent representations of place cell inputs, consistent with experimental evidence that place cells develop earlier than grid cells.

---

### Mechanistic insight

This paper meets the high bar for mechanistic insight by presenting a computational algorithm and connecting it to neural circuit implementation:

**Algorithm**: Predictive coding provides a normative framework where grid cells emerge through prediction error minimization. The key algorithmic components are:
- **Inference**: Latent grid cell activities are optimized via iterative gradient descent to minimize prediction error (fixed-point iteration solving for **g**)
- **Learning**: Weights update via Hebbian plasticity based on presynaptic activity and error signals, without requiring backpropagation through time
- **Temporal extension**: tPCN incorporates recurrent connections and eligibility traces through inferred past states, enabling temporal credit assignment

**Neural data connection**: The paper maps algorithmic components to MEC-hippocampal circuitry:
- Grid cells (latent **g**) in MEC layer II pyramidal neurons
- Interneurons encoding eligibility trace (**ĝ**_{t-1}) enabling temporal integration
- Error neurons (**ε**^{g}_{t}, **ε**^{p}_{t}) computing prediction errors in MEC and CA1
- Bidirectional MEC-hippocampal connectivity implementing feedback and feedforward predictions

The paper cites experimental evidence: CA1 as mismatch detector (Lisman, 1999; Duncan et al., 2012), error-encoding neurons in entorhinal cortex (Ku et al., 2021), inhibitory interneurons in MEC layer II (Jones & Büh1, 1993; Witter & Moser, 2006), and earlier development of place cells than grid cells (Langston et al., 2010; Wills et al., 2010).

**Marr's levels analysis**:
- **Computational**: The brain solves spatial prediction—minimizing prediction error between expected and observed spatial locations during navigation.
- **Algorithmic**: Predictive coding implements this through iterative inference (gradient descent on latent activities) and Hebbian learning (local weight updates driven by prediction errors). tPCN extends this to temporal sequences via eligibility traces from inferred past states.
- **Implementational**: The algorithm maps to MEC-hippocampal circuitry with distinct cell types: grid cells (latent representations), interneurons (eligibility traces), error neurons (prediction error computation), and specific connectivity patterns (recurrent MEC inhibition, bidirectional MEC-hippocampal projections).

---

### Limitations & open questions

- **Multi-modularity**: The grid cells learned by PCN lack the multi-modularity (different spatial scales) observed in biological grid cells and in non-negative PCA models. The authors hypothesize that while sparse PCNs approximate orthonormality, they lack PCA's ability to extract variance-ordered components.

- **Analytical explanation**: A precise analytical explanation for why sparse non-negative PCN develops hexagonal grids remains incomplete. The authors offer an intuitive hypothesis linking the constraints to orthonormality but note a full derivation is "left for future work."

- **Softmax biological plausibility**: While the paper shows that tanh output nonlinearities can substitute for softmax and still produce grids, the biological implementation of softmax Jacobians in neural circuits remains unclear. The authors note that "additional circuitry components can be included to plausibly implement the nonlinearities" but this requires further investigation.

- **Inference iteration requirements**: The relationship between grid score quality and path integration performance is not linear—higher inference iterations improve performance but do not necessarily improve grid scores. The mechanism behind this dissociation is not fully understood.

- **Experimental validation**: While the paper maps tPCN to hippocampal circuitry and cites supporting evidence, direct experimental tests of the specific predictions (e.g., eligibility trace encoding in MEC interneurons, specific error neuron properties) have not been conducted.

---

### Connections & keywords

**Key citations**:
- Rao & Ballard (1999) - Foundational predictive coding model
- Olshausen & Field (1996) - Sparse coding in visual cortex
- Burak & Fiete (2009) - Recurrent attractor network model of grid cells
- Cueva & Wei (2018); Banino et al. (2018) - RNN models of grid cells via BPTT
- Sorscher et al. (2023) - Unified theory of grid cell computational origins
- Dordek et al. (2016) - Non-negative PCA account of grid cells
- Millidge et al. (2024) - Temporal predictive coding networks
- Whittington & Bogacz (2017) - Predictive coding approximates backpropagation

**Named models or frameworks**:
- Predictive Coding Networks (PCNs)
- Temporal Predictive Coding Networks (tPCN)
- Non-negative Principal Component Analysis (PCA)
- Recurrent Neural Networks (RNNs) with BPTT/tBPTT
- Continuous Attractor Network Models
- Oscillatory Interference Models

**Brain regions**:
- Medial entorhinal cortex (MEC)
- Hippocampus (CA1)
- Hippocampal place cells
- MEC layer II (pyramidal cells, interneurons)

**Keywords**:
grid cells, predictive coding, spatial navigation, path integration, medial entorhinal cortex, hippocampus, Hebbian plasticity, biologically plausible learning, recurrent neural networks, temporal predictive coding, representation learning, spatial memory, entorhinal cortex, place cells, eligibility trace
