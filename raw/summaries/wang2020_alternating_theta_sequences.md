---
source_file: wang2020_alternating_theta_sequences.md
paper_id: wang2020_alternating_theta_sequences
title: "Alternating sequences of future and past behavior encoded within hippocampal theta oscillations"
authors:
  - "Mengni Wang"
  - "David J. Foster"
  - "Brad E. Pfeiffer"
year: 2020
journal: Science
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - open_field
  - linear_track
methods:
  - bayesian_decoding
brain_regions:
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - theta_oscillations
  - phase_precession
  - phase_procession
  - place_cells
  - bimodal_cells
  - forward_sequences
  - reverse_sequences
  - prospective_coding
  - retrospective_coding
  - spatial_navigation
  - hippocampal_ca1
  - entorhinal_cortex
  - sharp_wave_ripples
  - replay
  - gamma_oscillations
  - beta_oscillations
  - multiplexing
  - alternating
  - sequences
  - future
---

### One-line summary
Hippocampal CA1 place cell ensembles encode alternating forward (prospective) and reverse (retrospective) spatial trajectories within single theta oscillations, with reverse sequences driven by phase procession in bimodal cells during a distinct theta phase window associated with entorhinal cortex input.

---

### Background & motivation
The hippocampus is critical for representing and storing sequential information, yet how forward-ordered neural activity can facilitate storage or expression of reverse-ordered sequences (as observed in ripple-based reverse replay) remains unclear. Theta sequences—temporally compressed spatial trajectories organized by theta oscillations—are critical for hippocampal-dependent memory-guided behavior, but prior studies have focused almost exclusively on forward-ordered trajectories. This study investigates whether reverse-ordered sequences coexist with forward sequences within theta oscillations and identifies the cellular and circuit mechanisms underlying this phenomenon.

---

### Methods
- **Subjects and recordings**: Rats engaged in reward-seeking exploration of linear tracks and open arenas; bilateral hippocampal CA1 recordings with large-scale ensemble place cell monitoring (mean ± SEM = 144.3 ± 14.0 putative excitatory units per session)
- **Behavioral paradigm**: Linear track and open field spatial navigation tasks with active exploration (speed ≥10 cm/s)
- **Decoding approach**: Memoryless, uniform-prior Bayesian decoding algorithm to extract spatial information from ensemble activity
- **Theta sequence analysis**: Analysis of 115,845 theta oscillations (7240.3 ± 1126.7 per session) examining temporally compressed spatial trajectories; identification of forward and reverse windows based on posterior probability troughs
- **Cell classification**: Identification of unimodal vs. bimodal cells based on firing rate relationship to theta phase; analysis of phase precession vs. procession patterns
- **Replay analysis**: Comparison of cell participation in forward vs. reverse replay during sharp-wave ripples
- **LFP analysis**: Correlation of theta and beta oscillation power with activity in forward vs. reverse windows

---

### Key findings
- Theta oscillations contain two distinct components: a **forward window** (phases 250°–420°/60°) encoding prospective trajectories ahead of the rat, and a **reverse window** (phases 80°–230°) encoding retrospective trajectories behind the rat
- Forward and reverse components were observed within single theta oscillations and were independently correlated with population activity in their respective windows
- The reverse component was not a trivial consequence of analysis methods or trajectory resetting; it showed statistically significant backward virtual trajectories (p < 0.002 for both open field and linear track)
- **Bimodal cells** (n = 557) displayed two preferred firing phases in theta oscillations: a major peak (200°–430°/70°, comparable to forward window) and a minor peak (80°–190°, consistent with reverse window)
- Bimodal cells were more likely to fire in ripples and preferentially participated in reverse replay compared to forward replay, linking reverse theta sequences to reverse replay
- During the reverse window, many bimodal cells displayed **phase procession** (opposite of phase precession), firing at progressively later theta phases as the rat passed through the place field
- Unimodal cells (n = 1041) also showed phase procession in the reverse window despite lower firing rates, suggesting this is a general feature of hippocampal activity during this period
- Activity in the major peak (forward) window was positively correlated with theta oscillation power (r = 0.78), while activity in the minor peak (reverse) window was correlated with beta oscillation power (r = 0.38, p < 10^-5)
- Theta oscillations with significant reverse sequences showed increased power in fast and medium gamma bands (associated with EC3 input to CA1) but not slow gamma (associated with CA3 input)
- Forward and reverse components are driven by independent, antiphase theta-frequency inputs: CA3 input (trough-associated, forward window) and EC3 input (peak-associated, reverse window)

---

### Computational framework
The paper employs a **dynamical systems** framework for understanding hippocampal sequence generation. The core formalism involves:

- **Theta phase precession/procession as a temporal coding mechanism**: The progressive shift in firing phase relative to spatial position creates compressed temporal sequences within each theta cycle
- **Dual-input circuit model**: Two independent, antiphase theta-frequency inputs (CA3 at trough, EC3 at peak) drive distinct activity windows, each capable of generating sequences through phase modulation
- **Sequence generation via phase coding**: Forward sequences emerge from phase precession (progressively earlier phases) during the CA3-driven window; reverse sequences emerge from phase procession (progressively later phases) during the EC3-driven window

The framework assumes that theta oscillations act as a temporal organizer for spatial sequences, with different input pathways providing the spatial content and phase modulation that determines sequence direction.

---

### Prevailing model of the system under study
Prior to this work, the prevailing model of hippocampal theta sequences held that:

- Theta sequences represent **exclusively forward-ordered, prospective trajectories** ahead of the animal's current position
- These sequences are generated primarily by **theta phase precession** in place cells, where neurons fire at progressively earlier theta phases as the animal traverses the place field
- Theta oscillations serve as a **temporal organizer** for spatial memory, with the trough-to-peak progression organizing forward sequences
- Reverse-ordered sequences (reverse replay) were believed to occur primarily during **rest or sharp-wave ripple events**, not during active theta states
- The cellular mechanisms for generating reverse-ordered sequences from forward-ordered activity were unknown

This paper challenges the assumption that theta sequences are exclusively forward-prospective, demonstrating instead that individual theta cycles contain alternating prospective and retrospective components.

---

### What this paper contributes
This paper makes several significant contributions to our understanding of hippocampal function:

1. **Discovery of reverse theta sequences**: The paper demonstrates that hippocampal theta oscillations contain not only forward-prospective trajectories but also independent reverse-retrospective trajectories within the same theta cycle. This reveals that theta cycles alternate between future and past representation.

2. **Identification of bimodal cells**: The discovery of a distinct population of bimodal place cells that fire at two distinct theta phases provides a cellular substrate for encoding both forward and reverse information. These cells preferentially participate in reverse replay, linking theta-state reverse sequences to ripple-state reverse replay.

3. **Mechanism for reverse sequence generation**: The paper establishes that reverse sequences are generated by phase procession (the opposite of phase precession) during a distinct theta phase window, providing a concrete algorithmic mechanism for how reverse-ordered activity can emerge from the same circuit that generates forward sequences.

4. **Circuit-level input organization**: The demonstration that forward and reverse components are driven by independent, antiphase inputs (CA3 vs. EC3) provides a circuit-level framework for understanding how the hippocampus can multiplex prospective and retrospective information processing.

5. **Link to memory consolidation**: The findings suggest a mechanism by which ongoing experience can be evaluated retrospectively during active behavior, potentially supporting memory storage and the generation of reverse replay during subsequent rest.

---

### Brain regions & systems
- **Hippocampal area CA1** — primary recording site; site of theta sequence generation and bimodal cell activity; receives convergent input from CA3 and EC3
- **Hippocampal area CA3** — source of Shaffer collateral input to CA1; drives forward window activity via trough-associated theta input
- **Entorhinal cortex (EC3)** — source of perforant path input to CA1; drives reverse window activity via peak-associated theta input; provides the spatial content for reverse sequences

---

### Mechanistic insight
This paper provides substantial mechanistic insight that meets the bar for algorithmic and neural-level explanation:

**Computational level**: The brain must solve the problem of representing both future and past trajectories during ongoing behavior to support adaptive navigation and memory. Theta oscillations provide a temporal framework for multiplexing these two representations within single cycles.

**Algorithmic level**: The paper identifies a concrete algorithm for generating reverse sequences:
1. Forward sequences are generated by theta phase precession (firing at progressively earlier phases) during the CA3-driven forward window
2. Reverse sequences are generated by theta phase procession (firing at progressively later phases) during the EC3-driven reverse window
3. Bimodal cells, which fire at both phases, can participate in both sequence types

**Implementational level**: The physical implementation involves:
- **Anatomical segregation**: Distinct inputs from CA3 (Shaffer collaterals, trough-associated) and EC3 (perforant path, peak-associated)
- **Phase locking**: Different theta phases preferentially activate different input pathways
- **Cellular specialisation**: Bimodal cells (similar to deep CA1 pyramidal neurons) show distinct firing patterns and preferential participation in reverse replay
- **Oscillatory signatures**: Beta power and fast/medium gamma power correlate with reverse sequence expression, reflecting EC3 input strength

The paper thus provides a comprehensive mechanistic account spanning all three of Marr's levels, grounded in both algorithmic description and neural data.

---

### Limitations & open questions
- The study was conducted in rats during spatial navigation tasks; whether alternating theta sequences generalize to non-spatial domains or other species (including humans) remains to be determined
- The causal role of alternating theta sequences in behavior was not directly tested through manipulation experiments
- The specific synaptic plasticity mechanisms that might operate differently in forward vs. reverse windows were not directly investigated
- The relationship between reverse theta sequences and subsequent reverse replay during sharp-wave ripples suggests a plasticity mechanism, but the temporal dynamics and durability of this plasticity remain unknown
- Whether bimodal cells represent a distinct cell type (e.g., deep vs. superficial CA1 pyramidal neurons) or a functional state was not definitively established
- The computational function of alternating prospective and retrospective sequences for navigation and memory remains to be fully elucidated

---

### Connections & keywords
- **Key citations**: O'Keefe & Recce 1993 (phase precession), Skaggs et al. 1996 (theta sequences), Foster & Wilson 2006 (reverse replay), Diba & Buzsáki 2007 (reverse replay), Dragoi & Buzsáki 2006 (theta sequences), Pfeiffer & Foster 2013, 2015 (prior work from same lab on sequence coding)
- **Named models or frameworks**: Theta phase precession, theta sequences, reverse replay, attractor networks, Bayesian decoding
- **Brain regions**: Hippocampus, CA1, CA3, entorhinal cortex (EC3)
- **Keywords**: theta oscillations, phase precession, phase procession, place cells, bimodal cells, forward sequences, reverse sequences, prospective coding, retrospective coding, spatial navigation, hippocampal CA1, entorhinal cortex, sharp-wave ripples, replay, gamma oscillations, beta oscillations, multiplexing
