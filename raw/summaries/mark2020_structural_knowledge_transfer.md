---
source_file: "mark2020_structural_knowledge_transfer.md"
paper_id: "mark2020_structural_knowledge_transfer"
title: "Transferring structural knowledge across cognitive maps in humans and models"
authors: "Shirley Mark, Rani Moran, Thomas Parr, Steve W. Kennerley, Timothy E. J. Behrens"
year: 2020
journal: "Nature Communications"
paper_type: "computational"
contribution_type: "theoretical"
species: ["human"]
methods: ["computational_modeling"]
brain_regions: ["hippocampus", "entorhinal_cortex"]
frameworks: ["reinforcement_learning", "successor_representation", "bayesian_inference", "structural_form_discovery"]
keywords: ["transferring", "structural", "knowledge", "across", "cognitive", "maps", "humans", "models"]
key_citations: ["dayan1993_successor_representation", "behrens2018_cognitive_map_organizing_knowledge", "schapiro2013_event_representation_memory", "kemp2008_structural_discovery_form", "stachenfeld2017_hippocampus_predictive_map"]
---

### One-line summary

Humans transfer abstract structural knowledge (graph topology) across tasks with novel stimuli, and a computational model using basis-set representations of structural forms accounts for this capacity in ways that pure associative learning cannot.

---

### Background & motivation

Cognitive maps encode relationships between task elements, but standard associative representations (such as the Successor Representation) encode structure in a way that is entangled with the specific stimuli of an environment — they cannot be generalised to novel sensory contexts. Yet many real-world environments share underlying structural forms (periodicity, hierarchy, community structure, grid topology), and humans appear to exploit this regularity when encountering new tasks. The gap this paper fills is a principled computational account of how structural knowledge can be represented in a format that abstracts away from stimulus identity, enabling transfer to entirely new sensory environments, and empirical evidence that humans actually do this.

---

### Methods

- **Model**: A hierarchical generative model in which each structural form (hexagonal grid, community graph) is represented by a basis set — specifically, eigenvectors of the graph Laplacian for hexagonal structures, and community-assignment plus connecting-node-assignment vectors for community graphs. Given observations, a Bayes-optimal agent infers the structural form and graph size via MAP estimation (approximated using BIC), then estimates transition matrices by scaling/interpolating the relevant basis set. Compared against associative baselines: online SR (TD learning), SR calculated from learned transition matrix (SR-A), and spectrally regularised SR (SRreg).
- **Experiment 1 — transfer of hexagonal structure**: 60 participants (30 per group). Day 1: random-walk learning of two hexagonal graphs (different pictures). Day 2: paired-presentation learning of a new hexagonal graph with omitted edges (missing links). Participants tested on distance-estimation questions where correct answers required inferring the existence of omitted edges. Group 1 had a "correct" hexagonal prior; Group 2 had an "incorrect" community-structure prior.
- **Experiment 2 — transfer of community structure**: 40 participants (20 per group). Day 1: random-walk learning of two graphs (hexagonal or community). Day 2: random-walk learning and navigation on a community-structured graph. Measured: learning pace (reaction time per pair), navigation efficiency (steps to target), and frequency of connecting-node choices.
- **Subject population**: UCL students, mean age 23.5; all experiments approved by UCL Research Ethics Committee.

---

### Key findings

- **Model — inference of unobserved edges**: The basis-set model correctly inferred structural form and graph size, and solved "missing links" distance-estimation problems significantly above chance (p < 0.001). Simple associative models (SR-online, SR-A) performed at or below chance. Spectrally regularised SR (SRreg) performed above chance without transfer, but this advantage is invariant to prior-day structure and is not knowledge transfer.
- **Experiment 1 — humans infer unobserved trajectories**: Participants with a hexagonal prior (correct) outperformed those with a community-structure prior (incorrect) on both all distance questions (mean P(correct): 0.56 vs 0.52; t = 2.54, p = 0.0068, d = 0.699) and inference-only questions (0.54 vs 0.50; t = 2.29, p = 0.016, d = 0.565). Effect was driven by a subset of participants who performed reliably above chance at the individual level (p < 10⁻⁵), suggesting the transfer is an all-or-nothing inferential process rather than a graded effect.
- **Experiment 2 — policy transfer**: Participants with a correct community-structure prior learned associations faster (shorter RT per pair; p = 0.003, t = 3.19, d = 1.01), navigated to targets in fewer steps (significant for starting distances 2, 3, and 4; d = 0.63–0.85), and chose connecting nodes more frequently — including when doing so was the wrong local choice (p = 0.006, t = 2.88, d = 0.91). This last result rules out model-free value explanations.
- **Model — community structure**: Basis-set model correctly inferred number of communities and connecting-node identities directly from emission-matrix learning, without additional computation.

---

### Computational framework

**Hierarchical Bayesian inference over structural forms**, implemented via a Hidden Markov Model (HMM) with a structured prior on transition matrices.

- **What is modelled**: The agent observes a sequence of stimuli (graph nodes) generated by a Markov process. It must infer the latent structural form governing transitions, the graph size, and the identity of each stimulus.
- **Key variables**: Structural form Sf (categorical); graph dimensions θ; transition matrix A (approximated from basis set); emission matrix B; observations O.
- **Basis sets**: Each structural form is encoded as a set of basis vectors (Usf) — eigenvectors of a reference hexagonal transition matrix for grids; community-membership and connecting-node assignment vectors for community graphs. Given inferred Sf and θ, the transition matrix is reconstructed as A = f(Usf^θ · Ssf · (Usf^θ)^T), where Ssf is a diagonal weight matrix.
- **Inference**: Structural form and graph size are inferred by MAP, with likelihood approximated via BIC using the Baum–Welch algorithm to estimate the emission matrix.
- **Key assumption**: Transfer is possible because the basis sets are stored in a form that is invariant to stimulus identity — only the emission matrix needs to be re-learned for each new environment.

---

### Prevailing model of the system under study

The paper positions the Successor Representation (SR; Dayan 1993; Stachenfeld et al. 2017) as the dominant computational model of cognitive maps. In this framework, each state's representation encodes the expected discounted future occupancy of all other states — a compact but stimulus-entangled encoding of transition structure. The SR allows flexible navigation and generalisation of predictions within an environment, but because the representation fuses the transition structure with stimulus-specific state identities, it cannot be straightforwardly transferred to new environments with different stimuli. The prevailing view thus treated the hippocampus as a "predictive map" implementing SR-like representations, without an explicit mechanism for cross-context structural transfer. Tolman's cognitive map concept (1948) provides the broader motivating framework, and the introduction treats schemas (Kemp et al. 2010; Halford et al. 1998) and analogical transfer (Reeves & Weisberg 1994) as psychological precursors, but these lacked a computational implementation.

---

### What this paper contributes

The paper establishes that humans go beyond what any purely associative or smoothed-SR model can achieve: their performance on inference tasks depends on the structural form of graphs they experienced in a prior session with entirely different stimuli. This is the first clear behavioural dissociation between associative learning (which is session- and stimulus-specific) and structural knowledge transfer (which is cross-session and stimulus-invariant).

The basis-set model provides a concrete computational mechanism: representing each structural form as a fixed set of basis vectors (derived from spectral graph theory) allows the agent to (a) infer the structural form governing a new environment, (b) reconstruct approximate transition matrices without re-learning them, and (c) directly read off task-relevant state identities (connecting nodes) from the emission matrix alone. These capabilities are not available to SR-based models.

The work also provides a principled link between grid-cell eigenvectors and structural knowledge representation, extending the "hippocampus as predictive map" view to a "hippocampal–entorhinal system as structural knowledge library" view — each basis set potentially corresponding to a stored, reusable grid-like code.

---

### Brain regions & systems

This is primarily a computational and behavioural paper with no neural data. The paper explicitly connects its framework to neural structures in the discussion:

- **Entorhinal cortex (grid cells)** — proposed as the likely neural substrate for hexagonal basis sets; grid-cell activity patterns resemble eigenvectors of hexagonal transition matrices, and grid cells remap across environments while preserving their hexagonal firing pattern, consistent with a basis-set that is reused across tasks.
- **Entorhinal cortex (boundary cells)** — proposed as a component of a basis set capturing special nodes in translational-invariant graphs (an asymmetric transition structure induced by boundary-preferring policies generates right eigenvectors resembling boundary cell patterns).
- **Hippocampus** — implicitly invoked as the seat of SR-like associative maps and as a system that interacts with entorhinal basis sets; attractor dynamics in hippocampus/entorhinal cortex are cited as supporting stable storage and recall of grid patterns.

No brain recording or imaging data are reported.

---

### Mechanistic insight

The paper does not meet the full bar for mechanistic insight as defined here: it proposes a computational algorithm (basis-set HMM inference) and validates it against human behaviour, but provides no neural data (recordings, imaging, lesion, pharmacology) linking specific model variables to measured neural activity. The computational and algorithmic levels are clearly articulated; the implementational level is speculative (discussed with reference to grid cells and attractor networks in the Discussion, but not tested). In Marr's terms: the computational and algorithmic levels are addressed; the implementational level is proposed but not evidenced.

---

### Limitations & open questions

- Only a subset of participants in Experiment 1 showed reliable structural transfer, and the paper cannot distinguish whether this reflects individual differences in capacity or in task difficulty (large graphs, no visual cues, no feedback).
- The model has perfect memory and no stochasticity, so it systematically outperforms humans; the source of human variability and failure is not modelled.
- The paper cannot determine from Experiment 2 whether participants transfer the abstract transition structure itself (via basis sets) or only a high-level behavioural policy ("prefer connecting nodes") — both accounts are consistent with the data.
- The basis sets are hand-designed for two structural forms; a theory of how the brain discovers or acquires basis sets for novel structural forms is not provided.
- No neural data; the hypothesised link to grid cells, boundary cells, and hippocampal attractor networks remains untested.
- Whether the community-structure experiment also involves inference of unobserved transitions (as Experiment 1 does) is not cleanly disentangled from policy transfer.
- The paper notes that the brain may use both abstract and associative representations in parallel, but does not model their interaction.

---

### Connections & keywords

**Key citations**:
- Stachenfeld, Botvinick & Gershman (2017) — hippocampus as predictive map (SR)
- Dayan (1993) — Successor Representation
- Kemp & Tenenbaum (2008) — discovery of structural form
- Tenenbaum et al. (2011) — growing a mind: statistics, structure, abstraction
- Mahadevan & Maggioni (2007) — proto-value functions / graph Laplacian eigenvectors for RL
- Hafting et al. (2005) — grid cells in entorhinal cortex
- Behrens et al. (2018) — what is a cognitive map?
- Schapiro et al. (2013) — neural representations from community structure
- Garvert, Dolan & Behrens (2017) — abstract relational knowledge in hippocampal–entorhinal cortex
- Constantinescu, O'Reilly & Behrens (2016) — gridlike code for conceptual knowledge

**Named models or frameworks**:
- Successor Representation (SR)
- Hidden Markov Model (HMM)
- Basis sets model (this paper's contribution)
- Spectral regularisation / eigendecomposition-filtered SR (SRreg)
- Bayesian Information Criterion (BIC) for model selection
- Baum–Welch algorithm

**Brain regions**:
- Entorhinal cortex (grid cells, boundary cells)
- Hippocampus

**Keywords**:
- structural knowledge transfer
- cognitive maps
- graph learning
- basis set representations
- successor representation
- Hidden Markov Model
- spectral graph theory
- graph Laplacian eigenvectors
- community structure
- hexagonal grid
- abstract relational knowledge
- connecting nodes
