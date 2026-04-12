---
source_file: "raju2022_space_sequence.md"
paper_id: "raju2022_space_sequence"
title: "Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus"
authors: "Rajkumar Vasudeva Raju, J. Swaroop Guntupalli, Guangyao Zhou, Miguel L\u00e1zaro-Gredilla, Dileep George"
year: 2022
journal: "DeepMind (preprint)"
paper_type: "computational"
contribution_type: "theoretical"
brain_regions: ["hippocampus"]
frameworks: ["successor_representation", "tolman_eichenbaum_machine"]
keywords: ["space", "latent", "sequence", "structured", "learning", "unified", "theory", "representation", "hippocampus"]
key_citations: ["stachenfeld2017_hippocampus_predictive_map"]
---

### One-line summary

Spatial representations in the hippocampus emerge from latent higher-order sequence learning, where "space" is not explicitly encoded but arises as a byproduct of learning sequential relationships among aliased sensory observations.

---

### Background & motivation

The hippocampus exhibits a bewildering variety of neural phenomena—place cells, time cells, splitter cells, event-specific representations, landmark vector cells, and various remapping patterns—that have been characterized using Euclidean spatial concepts. Without a unifying principle, each experiment appears to discover new anomalies. The authors propose that treating space as a latent sequence can provide a unified computational explanation for these diverse phenomena, suggesting that place-field mapping itself (interpreting sequential responses in spatial terms) may be a source of apparent anomalies.

---

### Methods

- **Model architecture**: Clone-structured Causal Graph (CSCG), an extension of cloned Hidden Markov Models that includes actions
- **Core mechanism**: Learning latent graphs from aliased observations where multiple nodes can emit the same observation; clones (multiple hidden states per observation) disambiguate sequential contexts
- **Learning algorithm**: Expectation-Maximization (EM) with pseudocount smoothing, analogous to spike-timing-dependent plasticity
- **Inference**: Message-passing using simple integrate-and-fire neurons (biologically plausible)
- **Training environments**: 2D and 3D layouts, mazes, linear tracks, multiple connected rooms, hairpin mazes; both allocentric and egocentric observation/action settings
- **Validation approach**: Replicating 15+ classic and recent hippocampal phenomena from the literature (Table 1)

---

### Key findings

- CSCG successfully learns latent topologies from purely sequential aliased observations in diverse environments (2D/3D rooms, mazes, buckyball surfaces) without Euclidean assumptions or explicit location inputs
- Allocentric "spatial" representations naturally emerge from higher-order sequence learning on egocentric inputs
- CSCG performs latent transitive inference, stitching together global maps from disjoint overlapping experiences (Fig. 2C)
- Multiple maps are simultaneously represented without explicit map boundary instructions; appropriate map recalled via hidden state inference (Fig. 2D)
- **Replication of classic remapping phenomena**:
  - Geometry-change remapping (O'Keefe & Burgess 1996): Place fields anchored to boundaries split/expand when room elongated
  - Cue rotation (Muller & Kubie 1987): Place fields rotate with cue card; barriers disrupt fields near them
  - Landmark vector cells (Deshmukh & Knierim 2013): Place fields show dual components when landmark moved
  - Linear track distance coding (Sheehan et al. 2021): Fields code distance from start/end; gradually widen with distance
- **Direction sensitivity**: Elongated room place fields show direction-dependent activation (left peak for rightward travel, etc.)—explained by sequential contexts occurring in directional walks
- **Event-specific rate remapping (Sun et al. 2020)**: CSCG naturally produces lap-specific responses without explicit lap-boundary markers; remaps appropriately when reward lap changed
- **Connectivity experiments (Duvelle et al. 2021)**: Place fields unchanged when doors locked/barriers introduced without visual changes—CSCG explains this as blocked paths affecting few sequential contexts
- **Place field repetition**: Reproduced in identical rooms (Fuhs et al. 2005); direction-dependent repetition in hairpin maze (Derdikman et al. 2009)
- **Place field size/shape variations**: Fields expand toward center of empty rooms, elongate at edges (Tanni et al. 2022)—explained by inability to split long identical sequential contexts

---

### Computational framework

**Clone-structured Causal Graph (CSCG)** — a higher-order sequence learning model that extends cloned Hidden Markov Models with actions.

**Core formalism**:
- Environment represented as directed multigraph G = {V, E} with nodes V and edges E
- Each node emits a discrete observation; multiple nodes can emit same observation (aliasing)
- Hidden states (clones) C(x) represent nodes emitting observation x in different sequential contexts
- Action-augmented transition matrix: T_uvw = P(z_{n+1}=v, a_n=w | z_n=u)
- Joint probability: P(x_{1:N}, a_{1:N}, z_{1:N}) = P(z_1) ∏_{n=1}^{N-1} P(z_{n+1}, a_n | z_n) P(x_n | z_n)

**Key assumptions**:
- Spatial representations emerge from learning sequential structure, not from explicit spatial coding
- Agents have no global positioning system; must infer location from aliased sensory-motor sequences
- Clones disambiguate identical observations in different temporal contexts
- Message-passing inference enables planning/replay without explicit place field decoding

**Learning**: EM algorithm (Baum-Welch) with pseudocount smoothing; biologically plausible implementation via spike-timing-dependent plasticity.

---

### Prevailing model of the system under study

Prior to this work, the dominant view was that hippocampal place cells explicitly encode spatial locations in a Euclidean framework. Place fields were thought to represent specific locations in space, with remapping phenomena interpreted as the system re-encoding locations under changed circumstances. Various specialized cell types (boundary vector cells, landmark vector cells, splitter cells, time cells, lap cells) were catalogued as distinct coding schemes without a unified theoretical framework. The prevailing assumption was that spatial mapping requires either explicit spatial inputs or grid cell scaffolding to construct place representations.

---

### What this paper contributes

This paper proposes and demonstrates a fundamental reframing: spatial representations in the hippocampus are not explicitly encoded but emerge as a byproduct of latent higher-order sequence learning. The key contributions include:

1. **Unified theoretical framework**: The Clone-structured Causal Graph (CSCG) model explains over 15 diverse hippocampal phenomena (remapping, direction sensitivity, event-specific representations, place field repetition, etc.) through a single principle—sequential context learning—without postulating special coding mechanisms for each phenomenon.

2. **Reinterpretation of place fields**: Place fields are not responses to locations but to sequential contexts; the apparent "spatial" nature is an emergent property of how sequential responses overlay on Euclidean maps when analyzed by experimenters.

3. **Resolution of anomalies**: The model explains why place fields sometimes remap and sometimes don't, predicting that changes affecting sequential contexts determine remapping, not mere geometric or connectivity changes.

4. **Mechanistic basis for cognitive maps**: Shows how cognitive maps can be learned from pure sensory-motor sequences without Euclidean assumptions, GPS, or explicit spatial inputs.

5. **Testable predictions**: Generates novel predictions about place field behavior (e.g., uniqueness of visual context controls field expansion, not rate of visual change).

---

### Brain regions & systems

- **Hippocampus** — primary focus; place cells and their diverse phenomena explained as emergent properties of sequence learning
- Not applicable at anatomical level — the paper is purely computational and does not make claims about specific anatomical circuits, though it suggests CSCG operations could map to hippocampal circuits via biologically plausible learning (STDP) and inference (message passing) mechanisms

---

### Mechanistic insight

This paper **meets the high bar** for mechanistic insight. It presents a formal algorithm (CSCG) and demonstrates how it explains neural data (place cell phenomena) that specifically support this algorithm over alternatives.

**Marr's three levels analysis**:

- **Computational level**: The brain solves the problem of learning structure from aliased sequential observations to enable navigation, planning, and episodic memory. The problem is to invert the observation stream to learn a latent generative model of the environment's topology from purely sensory-motor experience without explicit spatial inputs.

- **Algorithmic level**: CSCG implements this through: (1) Cloning — creating multiple latent states (clones) per observation to disambiguate sequential contexts; (2) Higher-order graph learning — learning transition probabilities between clones conditioned on actions; (3) Message-passing inference — forward-backward algorithm for state estimation and planning; (4) EM learning — parameter updates analogous to STDP.

- **Implementational level**: The paper sketches biological plausibility: clones map to neuronal assemblies; emission matrix structure maps to bottom-up connectivity; transition matrix maps to lateral connections; message-passing maps to neural dynamics with integrate-and-fire neurons; EM learning maps to STDP-based plasticity. However, specific cell types, biophysical mechanisms, and connectivity patterns are not detailed.

---

### Limitations & open questions

- The model was tested primarily on discrete grid-world environments; generalization to continuous real-world spaces requires further validation
- While biologically plausible mechanisms are sketched, specific neural implementations (cell types, circuits, neuromodulators) remain underspecified
- The model does not incorporate grid cells; the authors suggest grid cells could provide optional scaffolding but this interaction is not modeled
- Active learning and exploration strategies are not developed; current model uses random walks
- Temporal abstraction through community detection is mentioned but not fully explored
- Reward mechanisms and value-based decision making are not integrated

---

### Connections & keywords

**Key citations**: O'Keefe and Burgess (1996); Muller and Kubie (1987); Deshmukh and Knierim (2013); Sheehan et al. (2021); Sun et al. (2020); Duvelle et al. (2021); Fuhs et al. (2005); Derdikman et al. (2009); Tanni et al. (2022); Eichenbaum (2004); Stachenfeld et al. (2017); Whittington et al. (2018); Dedieu et al. (2019); George et al. (2021)

**Named models or frameworks**: Clone-structured Causal Graph (CSCG), cloned Hidden Markov Models, Temporal Context Model (TCM), Tolman-Eichenbaum Machine (TEM), Successor Representation (SR), Boundary Vector Cell model, Dynamic Markov Coding

**Brain regions**: Hippocampus, place cells

**Keywords**: sequence learning, latent representations, cognitive maps, place cells, remapping, hippocampus, higher-order graphs, hidden Markov models, aliased observations, spatial representation, transitive inference, schema learning, replay, planning, clone-structured models
