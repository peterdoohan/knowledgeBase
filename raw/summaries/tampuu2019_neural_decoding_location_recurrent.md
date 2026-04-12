---
source_file: "tampuu2019_neural_decoding_location_recurrent.md"
paper_id: "tampuu2019_neural_decoding_location_recurrent"
title: "Efficient neural decoding of self-location with a deep recurrent network"
authors: "Ardi Tampuu, Tambet Matiisen, H. Freyja \u00d3lafsd\u00f3ttir, Caswell Barry, Raul Vicente"
year: 2019
journal: "PLoS Computational Biology"
paper_type: "computational"
contribution_type: "methodological"
species: ["rat"]
tasks: ["open_field", "foraging_task", "navigation_task"]
methods: ["tetrode_recording", "bayesian_decoding"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "medial_entorhinal_cortex"]
frameworks: ["bayesian_inference"]
keywords: ["key_citations_okeefe_and_dostrovsky_1971_place_cell_discovery", "okeefe_and_nadel_1978_cognitive_map_theory", "wilson_and_mcnaughton_1993_hippocampal_ensemble_coding", "zhang_et_al_1998_bayesian_decoding_framework", "hochreiter_and_schmidhuber_1997_lstm", "goodfellow_et_al_2016_deep_learning", "named_models_or_frameworks_long_short_term_memory_lstm_networks", "recurrent_neural_networks_rnns", "bayesian_decoding_with_flat_priors_mle", "bayesian_decoding_with_memory_continuity_constraint", "backpropagation_through_time_bptt", "rmsprop_optimizer", "brain_regions_hippocampal_ca1", "hippocampal_ca3", "medial_entorhinal_cortex_mec", "keywords_neural_decoding", "recurrent_neural_networks", "lstm", "place_cells", "hippocampus"]
---

### One-line summary

A deep recurrent neural network (RNN) decoder using LSTM units outperforms standard Bayesian approaches for decoding self-location from hippocampal place cell activity, achieving lower errors through flexible integration of temporal context without requiring explicit prior assumptions.

### Background & motivation

Place cells in the mammalian hippocampus signal self-location with sparse, spatially stable firing fields, and decoding accuracy from these cells provides a lower bound on the information the hippocampus conveys about location. Traditional Bayesian decoders require assumptions about firing rate statistics (typically Poisson) and explicit prior distributions, but hippocampal activity is known to violate Poisson statistics with high variability and dynamic, context-dependent firing. This paper addresses whether deep RNNs can overcome these limitations by learning to integrate temporal context without hand-coded priors.

### Methods

- **Subjects**: Five male Lister Hooded rats with tetrode recordings from CA1 hippocampus
- **Tasks**: (1) 2D open field foraging (1m x 1m square), (2) 1D Z-shaped track navigation (600 cm total length)
- **Neural data**: Spike counts from hippocampal neurons in overlapping time windows (200-4000 ms, 200 ms shift between windows)
- **RNN architecture**: "Many-to-one" LSTM network with 2 hidden layers of 512 LSTM units each, input layer (size = number of neurons), output layer (2 nodes for x,y coordinates)
- **Training**: 100 time steps of spike count vectors (approximately 20 seconds of activity) to predict location at center of last window; RMSprop optimizer, learning rate 0.001, 50 epochs, batch size 64, 10-fold cross-validation
- **Comparison decoders**: (1) Simple Bayesian decoder with flat prior (MLE), (2) Bayesian decoder with memory (continuity constraint + occupancy-based prior)

### Key findings

- **2D decoding accuracy**: RNN achieved best median error of 10.18±0.23 cm (1200 ms window) and best mean error of 12.50±0.39 cm (1400 ms window), outperforming both Bayesian decoders (simple Bayes: 12.00 cm median, 15.83 cm mean; Bayes with memory: 11.31 cm median, 15.46 cm mean)
- **1D decoding accuracy**: RNN consistently outperformed both Bayesian approaches across all 5 animals, with particularly large advantage for the animal with fewest recorded neurons (R2217, n=40)
- **Error distribution**: RNN errors followed unimodal distribution with few large errors (>35 cm: 1.7%), while Bayesian decoders made more extreme errors (>35 cm: ~8%; >50 cm: ~2.7%)
- **Robustness to small sample sizes**: When downsampling to 5 neurons, RNN achieved 30.9 cm error vs. 46.0 cm for Bayesian decoder, demonstrating RNN's advantage with limited neural data
- **Factors affecting accuracy**: Lower error in well-sampled regions (Spearman r = -0.16, p < 0.001), regions with higher summed neural activity (Spearman r = -0.31, p < 0.001), near environmental boundaries (orthogonal to wall: r = 0.31, p < 0.001), and during movement vs. stationary periods (mean error: 12.1 cm moving vs. 16.5 cm stationary)
- **Sensitivity analysis**: Knockout and gradient sensitivity measures were correlated (Spearman ρ = 0.57, p < 0.001) but captured different aspects; neither correlated with Skaggs information score. High-firing inhibitory neuron (#55) was most influential by knockout but ranked 47th by gradient. Sensitivity to neurons decreased with firing rate (near place field center, small changes less influential than at edges), consistent with theoretical predictions about information content at firing rate boundaries

### Computational framework

The paper employs **deep recurrent neural networks (RNNs)**, specifically **Long Short-Term Memory (LSTM)** networks, as a machine learning framework for neural decoding. The core formalism treats neural decoding as a supervised sequence-to-scalar regression problem: given a temporal sequence of spike count vectors (input), the network learns to predict the animal's spatial coordinates (output). The LSTM architecture uses gating mechanisms (input, forget, output gates) to selectively maintain or update internal state representations over time, allowing the network to flexibly integrate relevant temporal context without explicit assumptions about the prior distribution or noise model. Training via backpropagation through time (BPTT) minimizes mean squared error between predicted and true locations, adjusting connection weights to optimize the learned temporal integration policy.

### Prevailing model of the system under study

The prevailing model of hippocampal spatial coding treats place cells as providing a stable, sparse representation of self-location relative to the environment. Standard decoding approaches model place cell firing as Poisson processes with firing rates determined by spatial position, and apply Bayesian inference with explicit priors (flat or informed by movement history/occupancy) to estimate position from spike counts. The field assumes that hippocampal activity is primarily driven by current location, though with acknowledged complications: place cells can fire during non-local replay events, show direction-dependent activity on linear tracks, and gradually refine their firing fields with experience. The prevailing view implicitly assumes that Poisson statistics and hand-designed priors adequately capture the mapping from spikes to position, despite evidence that place cell firing variability greatly exceeds Poisson predictions.

### What this paper contributes

This paper demonstrates that RNNs can decode self-location from hippocampal activity more accurately than standard Bayesian methods, establishing a new lower bound on the information content of place cell populations. The RNN achieves superior performance by learning to flexibly integrate temporal context over approximately 20 seconds of preceding neural activity, without requiring explicit assumptions about Poisson firing statistics or hand-coded priors over position. The paper also introduces new analysis tools: gradient-based sensitivity analysis enables dynamic quantification of how spike count perturbations influence decoding, complementing traditional knockout approaches. Key insights include: (1) decoding accuracy is highest near environmental boundaries (orthogonal to walls), consistent with boundary-anchored spatial representations; (2) the RNN is more robust to small neural populations than Bayesian methods, suggesting particular utility for recordings with limited neurons; (3) sensitivity to individual neurons is highest at place field edges (where firing rate changes most rapidly), aligning with theoretical predictions about information-maximizing coding. These results establish RNNs as a practical and biologically relevant methodology for neural decoding and provide new tools for exploring the temporal dynamics of the neural code.

### Brain regions & systems

- **Hippocampal CA1** — primary source of recorded neural activity; place cells provide spatially modulated firing used for decoding self-location
- **Hippocampal CA3** — mentioned as containing place cells but not a source of recorded data in this study
- **Medial entorhinal cortex (MEC)** — targeted for recordings but data not analyzed in this study; mentioned as source of grid cells

### Mechanistic insight

This paper does **not** meet the bar for mechanistic insight. The RNN is a functional machine learning tool that learns to map spike sequences to positions, but the paper does not provide evidence that the brain implements LSTM-like gating mechanisms for spatial decoding. The RNN learns an algorithmic solution (sequence-to-coordinate mapping) but this is not validated as the algorithm the brain actually uses. There is no neural data presented that links specific RNN variables or operations to biological neural activity—the RNN is a tool for decoding, not a model of how the brain decodes. The paper does not address the implementational level (specific cell types, connectivity, or biophysical mechanisms). The RNN provides a computational benchmark and analysis tool, but not a mechanistic explanation of how the hippocampus supports spatial navigation.

### Limitations & open questions

- The RNN requires substantial training data and computational resources compared to Bayesian methods; training took ~4 hours on high-end GPU per cross-validation fold
- The RNN decoder is a "black box"—interpretation of what the network learns requires additional analysis tools (sensitivity analyses, dimensionality reduction)
- The study does not determine whether the RNN's performance advantage stems from better handling of non-Poisson variability, flexible temporal integration, or both
- It remains unclear whether the brain actually uses RNN-like recurrent computations for spatial decoding, or whether the RNN simply provides a better statistical estimator
- The analysis focused on CA1 place cells; whether RNNs would show similar advantages for other brain regions or cell types (grid cells, interneurons) is unknown
- The study used offline decoding; real-time decoding with RNNs would require addressing computational latency

### Connections & keywords

**Key citations:** O'Keefe & Dostrovsky 1971 (place cell discovery), O'Keefe & Nadel 1978 (cognitive map theory), Wilson & McNaughton 1993 (hippocampal ensemble coding), Zhang et al. 1998 (Bayesian decoding framework), Hochreiter & Schmidhuber 1997 (LSTM), Goodfellow et al. 2016 (deep learning)

**Named models or frameworks:** Long Short-Term Memory (LSTM) networks, Recurrent Neural Networks (RNNs), Bayesian decoding with flat priors (MLE), Bayesian decoding with memory (continuity constraint), backpropagation through time (BPTT), RMSprop optimizer

**Brain regions:** Hippocampal CA1, Hippocampal CA3, Medial entorhinal cortex (MEC)

**Keywords:** neural decoding, recurrent neural networks, LSTM, place cells, hippocampus, spatial navigation, self-location, Bayesian decoding, deep learning, sensitivity analysis, spike train analysis, CA1, rodent, cross-validation
