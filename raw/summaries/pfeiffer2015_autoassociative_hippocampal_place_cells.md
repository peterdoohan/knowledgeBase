---
source_file: pfeiffer2015_autoassociative_hippocampal_place_cells.md
title: Autoassociative dynamics in the generation of sequences of hippocampal place cells
authors: Brad E. Pfeiffer, David J. Foster
year: 2015
journal: Science
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Hippocampal sharp-wave ripple (SWR) sequences are composed of discrete attractor states that sharpen at individual locations before rapidly transitioning to spatially discontiguous locations, with these dynamics locked to the slow-gamma (25-50 Hz) rhythm.

### Background & motivation

Neuronal circuits can produce self-sustaining sequences of activity patterns, but the precise mechanisms remain unknown. Theoretical models suggest that combining fast autoassociation (for pattern stabilization) with slower heteroassociation (for sequence progression) could sustain sequences by allowing each pattern to be corrected before transitioning. However, direct evidence for these jumpy attractor dynamics has been lacking due to the difficulty of recording from large neuronal ensembles at sufficient temporal resolution during internally generated sequences.

### Methods

- **Subjects**: Five rats
- **Recording**: Bilateral ensemble recordings from dorsal hippocampal CA1 neurons (80-263 units per session; mean +- SEM = 159.2 +- 11.8)
- **Behavior**: Exploration of open arenas (circular) and linear tracks
- **SWR detection**: Identified sharp-wave ripple events encoding temporally compressed spatial trajectories (termed trajectory events rather than replay)
- **Decoding**: Memory-less, uniform-prior Bayesian decoding algorithm to decode spatial position from ensemble activity
- **Analysis**: Step size analysis comparing observed vs. predicted smooth trajectories; phase-locking analysis to slow-gamma (25-50 Hz) oscillations; spike shuffling controls to dissociate movement from gamma phase; simulation controls using Poisson spiking based on place fields

### Key findings

- **Discontinuous trajectories**: SWR trajectory events exhibit discontinuous, jumpy movement patterns rather than smooth continuous trajectories. Step sizes showed a large peak at zero (immobility) and a longer tail of larger steps compared to predicted smooth trajectories (Wilcoxon rank-sum test, P < 10^-10).

- **Attractor-like dynamics**: Trajectories alternate between periods of immobility (where consecutive decoding frames represent the same location, allowing the representation to sharpen) and rapid movement (sequential unique positions). Average stationary epochs lasted 24.1 +- 0.38 ms (open field) and 16.7 +- 0.25 ms (linear track); movement epochs lasted 7.9 +- 0.09 ms and 11.2 +- 0.18 ms, respectively.

- **Slow-gamma locking**: Both excitatory spiking and movement during trajectory events are phase-locked to the slow-gamma (25-50 Hz) rhythm, with preferred phases opposing each other (spiking at high activity phases, movement at low activity phases). Step size was negatively correlated with spike count.

- **Causal role of gamma phase**: When spike identities were shuffled to create smooth trajectories (preserving gamma-phase relationships but removing discontinuous dynamics), the correlation between step size and gamma phase was abolished, demonstrating that the discontinuous movement is not an artifact of decoding but reflects genuine gamma-locked attractor dynamics.

- **Generalization across environments**: These findings were consistent across both open field and linear track environments and robust to various decoding criteria.

### Computational framework

The paper operates within the **attractor network** framework, specifically combining **autoassociative** and **heteroassociative** dynamics:

- **Autoassociation**: Fast recurrent connectivity within a network (e.g., CA3) stores and stabilizes discrete memories as attractor states. This allows partial or noisy patterns to converge to stored patterns.
- **Heteroassociation**: Slower connectivity between patterns enables sequence transitions.
- **Theoretical problem**: Pure heteroassociation leads to error accumulation; pure autoassociation cannot generate sequences.
- **Solution**: The paper provides evidence for a hybrid mechanism where attractor strength oscillates at slow-gamma frequency-high activity phases strengthen the current attractor (autoassociation), while low activity phases permit transitions to the next attractor (heteroassociation).

This framework maps onto Marr's levels:
- **Computational**: The brain must retrieve sequential memories while maintaining pattern stability and avoiding runaway excitation. The problem is balancing pattern completion (staying at a location) with sequence progression (moving to the next location).
- **Algorithmic**: The solution combines autoassociative dynamics (for stabilizing each pattern via recurrent connectivity within CA3) with heteroassociative transitions (for moving to the next pattern). The key innovation is that attractor strength oscillates at slow-gamma frequency: high-activity phases enable autoassociation (pattern sharpening), while low-activity phases permit heteroassociation (pattern transition). This creates discrete jumpy sequences rather than continuous drift.
- **Implementational**: The mechanism is implemented via the CA3-CA1 circuit. CA3 contains extensive recurrent excitatory connections (supporting autoassociation) and generates slow-gamma oscillations (25-50 Hz). CA1 recordings show phase-locking of spiking and decoded movement to these gamma oscillations. The physical architecture enables the algorithm: recurrent synapses store patterns, gamma oscillations control their expression.

### Prevailing model of the system under study

Prior to this work, the field understood hippocampal SWR-associated place-cell sequences (often termed replay) as temporally compressed reactivations of spatial trajectories. The prevailing view was that these sequences represented continuous paths through space, serving memory consolidation and planning functions. 

Theoretical work (Hopfield, Kleinfeld, Sompolinsky & Kanter) proposed that sustainable sequences require combining autoassociative dynamics (for pattern correction) with heteroassociative transitions, but direct empirical evidence for such jumpy attractor dynamics in vivo was lacking. The introduction notes that slow-gamma oscillations were known to increase during SWRs and memory tasks, but their specific function in governing sequence dynamics was not established.

### What this paper contributes

This paper provides the first direct empirical evidence for **discrete attractor dynamics** in hippocampal sequence generation, resolving the theoretical problem of how sequences can be both stable and progressive:

1. **Discretization of memory retrieval**: The paper demonstrates that SWR sequences are not continuous but consist of discrete units of information (individual locations), with the representation sharpening at each location before jumping to the next. This reveals a fundamental discretization in hippocampal memory retrieval.

2. **Gamma as a control mechanism**: The paper establishes a functional role for slow-gamma oscillations in controlling attractor dynamics-high gamma phases enable autoassociative pattern completion (sharpening), while low gamma phases permit heteroassociative transitions. This provides an implementation-level account of how the brain alternates between stability and flexibility.

3. **Linking levels of analysis**: The work connects theoretical predictions (from attractor network models) to circuit-level mechanisms (CA3 recurrent connectivity, gamma oscillations) to systems-level phenomena (SWR sequences), providing a rare example of Marr's three levels converging on a single problem.

4. **Generalization of the framework**: The findings suggest that gamma-mediated attractor dynamics may operate throughout cortex (given the prevalence of recurrent connectivity and gamma oscillations), with implications for understanding memory dysfunction in disorders involving gamma abnormalities.

### Brain regions & systems

- **Hippocampus (dorsal CA1)**: Primary recording location. Site of SWR-associated place-cell sequences. Theta and slow-gamma oscillations recorded here reflect input from CA3.
- **Hippocampus (CA3)**: Proposed source of slow-gamma oscillations (25-50 Hz). Contains extensive recurrent excitatory connections supporting autoassociative network dynamics. One synapse upstream from CA1 recording location.
- **Dentate gyrus**: Mentioned in theoretical context as part of heteroassociative network with CA3 for sequence generation during theta.

### Mechanistic insight

This paper meets the high bar for mechanistic insight by providing both an algorithmic account and neural data supporting it:

**Phenomenon**: Hippocampal place-cell sequences during SWRs alternate between discrete attractor states (sharpening at individual locations) and rapid transitions, governed by slow-gamma oscillations.

**Marr's three levels**:

- **Computational**: The brain must retrieve sequential memories while maintaining pattern stability and avoiding runaway excitation. The problem is balancing pattern completion (staying at a location) with sequence progression (moving to the next location).

- **Algorithmic**: The solution combines autoassociative dynamics (for stabilizing each pattern via recurrent connectivity within CA3) with heteroassociative transitions (for moving to the next pattern). The key innovation is that attractor strength oscillates at slow-gamma frequency: high-activity phases enable autoassociation (pattern sharpening), while low-activity phases permit heteroassociation (pattern transition). This creates discrete jumpy sequences rather than continuous drift.

- **Implementational**: The mechanism is implemented via the CA3-CA1 circuit. CA3 contains extensive recurrent excitatory connections (supporting autoassociation) and generates slow-gamma oscillations (25-50 Hz). CA1 recordings show phase-locking of spiking and decoded movement to these gamma oscillations. The physical architecture enables the algorithm: recurrent synapses store patterns, gamma oscillations control their expression.

**Neural evidence**: The paper provides direct neural evidence for the algorithm by showing that (1) decoded position sharpens at specific locations (attractor dynamics), (2) transitions occur preferentially at specific gamma phases (phase-locking), (3) shuffling spikes to create smooth trajectories abolishes the gamma-step size correlation (causal role of gamma), and (4) simulations confirm the decoding is not artifactual.

### Limitations & open questions

- **Causal manipulation**: The study relies on correlational evidence (gamma phase-locking) and spike shuffling controls. Direct causal manipulation of gamma oscillations (e.g., via optogenetics) would strengthen the mechanistic conclusions.
- **CA1 vs. CA3 recordings**: Recordings were from CA1, not CA3. While slow-gamma is thought to originate in CA3, the exact circuit mechanisms cannot be definitively established from CA1 recordings alone.
- **Species generalization**: Findings are from rats; generalization to other species (including humans) requires further validation.
- **Behavioral relevance**: The study focused on awake, immobile animals. How these dynamics relate to specific behavioral states (sleep, decision-making) and their functional consequences for memory remain to be fully explored.
- **Mechanism of gamma generation**: The paper does not address how slow-gamma oscillations are generated in CA3 or how they are modulated during different cognitive states.

### Connections & keywords

- **Key citations**: Hopfield (1982) - autoassociative networks; Kleinfeld (1986) - sequence generation; Sompolinsky & Kanter (1986) - combined auto/heteroassociation; Lisman & Idiart (1995) - gamma and working memory; Lisman et al. (2005) - theta sequence model; Davidson et al. (2009) - hippocampal replay; Carr et al. (2012) - SWR and memory; Pfeiffer & Foster (2013) - previous large-ensemble recording methods
- **Named models or frameworks**: Hopfield model, attractor networks, autoassociative dynamics, heteroassociative dynamics, Marr's three levels of analysis, sharp-wave ripple (SWR) events, trajectory events, slow-gamma oscillations, Bayesian decoding, pattern completion
- **Brain regions**: hippocampus, CA1, CA3, dentate gyrus, dorsal hippocampus
- **Keywords**: attractor networks, autoassociation, heteroassociation, place cells, sharp-wave ripples, SWR, replay, trajectory events, slow-gamma oscillations, gamma rhythm, sequence generation, hippocampus, CA1, CA3, Bayesian decoding, pattern completion, memory retrieval, discrete dynamics, neural sequences
