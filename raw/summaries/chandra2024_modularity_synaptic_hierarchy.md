---
source_file: "chandra2024_modularity_synaptic_hierarchy.md"
paper_id: "chandra2024_modularity_synaptic_hierarchy"
title: "Self-organized emergence of modularity, hierarchy, and mirror reversals from competitive synaptic growth in a developmental model of the visual pathway"
authors: "Sarthak Chandra, Mikail Khona, Talia Konkle, Ila R. Fiete"
year: 2024
journal: "bioRxiv (preprint, doi: 10.1101/2024.01.07.574543)"
paper_type: "computational"
contribution_type: "theoretical"
species: ["mouse", "human", "macaque"]
brain_regions: ["visual_cortex", "primary_auditory_cortex"]
frameworks: ["reinforcement_learning"]
keywords: ["self", "organized", "emergence", "modularity", "hierarchy", "mirror", "reversals", "competitive", "synaptic", "growth"]
---

### One-line summary

A simple synaptic growth rule combining presynaptic activity-dependent strengthening, distance-dependent costs, and heterosynaptic competition applied to an undifferentiated cortical sheet self-organizes a full primate-like visual hierarchy — discrete areas, concentric spatial layout, retinotopy, and polar angle mirror reversals — without detailed genetic specification or external visual input.

---

### Background & motivation

The primate visual cortex is organized into multiple discrete, hierarchically connected areas arranged concentrically on the cortical sheet, each with retinotopic maps and characteristic polar angle mirror reversals at area boundaries. This architectural, spatial, and topographic organization is present before eye-opening, implicating spontaneous activity and genetic factors rather than detailed visual experience. The developmental rules that simultaneously produce all three levels of organization — hierarchy, spatial layout, and topography — are unknown. The paper addresses this gap by asking how much rich cortical structure can emerge from simple, biologically plausible synaptic growth dynamics driven solely by spontaneous activity, without requiring genetic endpoint specification.

---

### Methods

- **Model architecture**: Two-layer initial setup — a semi-elliptical LGN (topographically organized via log-conformal mapping of one visual hemifield) projecting with all-to-all initial connectivity into an undifferentiated, unparcellated semi-infinite cortical sheet with all-to-all recurrent connectivity. No initial area boundaries, topography, or hierarchy in cortex.
- **Spontaneous activity**: Retinal waves modeled as spatially uniform wide-field activation on the timescale of synaptic plasticity (fast wave propagation relative to slow plasticity justifies time-averaging).
- **Core growth rule (heterosynaptic competition)**: Synaptic weight growth rate is proportional to presynaptic firing rate and inversely proportional to soma-to-synapse distance (Δ_ij_ = a_j / (d_ij/d_0)). A competitive rule decrements all incoming (or outgoing) weights by a fixed amount whenever their sum exceeds a bound W_max, strongly penalizing weak synapses and yielding sparse, strong connectivity.
- **Two alternative biologically plausible rules** derived to test robustness of the principle:
  - *Race-to-threshold*: silent synapses accumulate resources; synapse activates when resources exceed a distance- and activity-dependent threshold.
  - *Seek-and-prune*: stochastic synapse formation followed by selective pruning based on a "permanence" factor (= Δ_ij_).
- **Normative abstraction**: The dynamics are distilled into a deterministic algorithm called *local greedy wiring minimization via spontaneous drive* (GWM-S): connections are placed in order of increasing length from the current progenitor layer until out-degree saturation, then the most-innervated set becomes the next layer.
- **Extensions**: Two-cell-type model (type 1 projection neurons vs. type 2 interneurons, set by different d_0/γ parameters); generalization to auditory cortex (tonotopic input geometry) and mouse visual cortex (different cortical geometry).
- **Validation**: Receptive field mapping, polar angle/eccentricity maps, computational connectomics (anterograde/retrograde tracing), comparison to human and macaque empirical retinotopic maps and receptive field size data.
- **Network size**: Simulations use grids of ~75×150 (biophysical rules) to ~150×300 (GWM-S) cortical neurons plus LGN.

---

### Key findings

- Starting from a fully unstructured initial state, the heterosynaptic competition rule self-organizes into 4 discrete visual areas (V1–V4) arranged concentrically on the cortical sheet, matching the known spatial layout of early human visual cortex.
- Each formed area exhibits full retinotopic coverage; eccentricity maps are globally smooth and monotonic; polar angle maps show mirror reversals precisely at area boundaries as independently defined by synaptic hop distance from LGN — the first synapse-level model to reproduce this feature.
- The mechanism implements local greedy wiring minimization: mirror reversals arise because neurons at the inner edge of each area have the shortest connections to the next area's core, while neurons at the outer edge must reach further, producing the topographic flip.
- All three biologically distinct growth rules (heterosynaptic competition, race-to-threshold, seek-and-prune) converge to qualitatively similar endpoints, confirming GWM-S as the underlying principle; however, they produce distinguishably different developmental trajectories in proto-V3 (e.g., diffuse early retinotopy vs. progressive outward expansion).
- Receptive field size increases with eccentricity (inherited from log-conformal LGN mapping) and across hierarchy levels (via hierarchical nesting of similar-sized convolution-like kernels); a mild dip in field size at very large eccentricities is predicted across all rules.
- Connectivity is sparse and convolution-like in retinotopic coordinates, with in- and out-connectivity lengths inversely correlated within each neuron, and a bimodal (sum of two lognormals) wiring-length distribution across the whole network.
- Two-cell-type simulations with cells differing only in d_0 or γ spontaneously produce projection neuron-like (feedforward, inter-areal) and interneuron-like (local, intra-areal) connectivity patterns coexisting within the same hierarchy.
- The same GWM-S process applied to auditory input geometry reproduces tonotopic mirror-reversing areas (A1, R, RT); applied to mouse cortical geometry, it reproduces the mouse V1-plus-secondary-areas retinotopic layout including the characteristic hole in visual field coverage.
- Retinotopy develops sequentially up the hierarchy across all growth rules (a robust, invariant prediction): lower areas stabilize before higher areas.
- The model is robust over ~5 orders of magnitude variation in key parameters (d_0 and γ), with a sharp boundary between hierarchical and non-hierarchical (locally recurrent) connectivity regimes.

---

### Computational framework

The paper uses a **competitive developmental learning / synaptic growth** framework, situated within the broader tradition of activity-dependent self-organization.

The core formalism models synaptic weights as dynamic variables governed by two interacting processes: (1) a growth term proportional to presynaptic firing rate and inversely proportional to distance (Δ_ij_ = a_j / (1 + d_ij/d_0)), capturing axonal resource costs; and (2) a heterosynaptic competition rule that decrements all incoming or outgoing weights of a neuron whenever their sum exceeds a threshold, implementing winner-take-all dynamics at the neuronal level. Activity propagates linearly through thresholded weights with attenuation factor γ per synapse. Key assumptions: (a) spontaneous activity is spatially uniform on the plasticity timescale; (b) synaptic plasticity is much slower than activity propagation; (c) neurons have fixed in- and out-degree bounds. The normative GWM-S principle distills this into a greedy, locally sequential connection-placement algorithm, offering a deterministic characterization of the emergent connectome without simulation.

---

### Prevailing model of the system under study

The paper positions itself against two poles in developmental biology: (1) the chemoaffinity/positional information hypothesis (Sperry, Wolpert) — genes directly specify the detailed endpoint architecture, spatial layout, and topographic order of cortical areas — and (2) the blank-slate/mass-action hypothesis (Lashley, Turing) — external inputs shape all organization. The prevailing mechanistic understanding of visual cortical development acknowledges a role for spontaneous activity (retinal waves, Katz & Shatz 1996) in refining an initial genetically scaffolded topography, but the field lacked a mechanistic model explaining how discrete areal parcellation, hierarchical architecture, concentric spatial layout, and polar angle mirror reversals could all emerge simultaneously from a single self-organizing process without area-specific genetic gradients. The origin of polar angle alternations in particular had no known genetic gradient signal. Existing computational approaches either used global wiring minimization (NP-hard, not biologically plausible as a growth process) or self-organizing map models that specified tuning profiles in advance and did not generate circuit-level connectivity.

---

### What this paper contributes

The paper shows that detailed multi-area cortical architecture — hierarchy, spatial layout, and topography including mirror reversals — can emerge entirely from a single local synaptic growth rule operating on spontaneous activity, without genetic endpoint specification beyond a small set of scalar parameters. Specifically:

- It provides the first synapse-level mechanistic model that simultaneously generates discrete areal parcellation, concentric spatial organization, and retinotopic maps with polar angle mirror reversals.
- It explains the origin of polar angle alternations as a geometric consequence of distance-dependent competitive growth (edge neurons of each area have shortest connections to the next area's near-edge neurons), requiring no area-specific genetic gradients.
- It introduces the GWM-S principle as a unifying theoretical account of what the biologically distinct growth rules all implement, enabling a systematic comparison of developmental predictions across rules.
- It demonstrates that the same rules, with only geometry varied, explain auditory and mouse visual cortical organization, offering a parsimonious account of cortical pluripotency.
- It generates the first full connectome model of the primate ventral visual hierarchy (including log-magnification of the fovea), providing quantitative predictions (bimodal wiring-length distributions, sawtooth wiring-length profiles, inverse in/out-length correlations) for connectomics experiments.
- It proposes that small parameter differences (d_0, γ) between cell types — potentially genetically encoded — are sufficient to generate projection neuron vs. interneuron connectivity classes from the same growth rules.

---

### Brain regions & systems

- **Retina / LGN** — source of spontaneous drive (retinal waves) and topographically organized input; LGN geometry (log-conformal mapping of visual hemifield) is the key initial condition that determines the form of resulting maps.
- **V1 (primary visual cortex)** — first cortical area formed; receives direct LGN innervation (1-hop); anchor for the emerging hierarchy.
- **V2, V3, V4 (extrastriate areas)** — successive areas formed as each prior area saturates its outgoing connections; arranged concentrically around V1; each exhibits mirror-reversed polar angle maps at its boundaries.
- **Auditory cortex (A1, R, RT)** — modeled with tonotopic input geometry to demonstrate cross-modal generalization of the GWM-S principle.
- **Mouse visual cortex (V1, P, LM, AL, RL)** — modeled with different cortical geometry to demonstrate cross-species generalization; the model reproduces the partial visual field coverage and hole in coverage of secondary areas.

---

### Mechanistic insight

The paper meets the bar partially. It formalises a specific algorithm (GWM-S / heterosynaptic competition) that explains a suite of phenomena, and it validates the emergent connectivity against empirical retinotopic maps, receptive field size data, and known spatial layout from human and macaque imaging. However, it does not provide new neural recordings, imaging, lesion, or pharmacology data — all validation is via simulation matched to published empirical patterns (Wandell et al., Freeman & Simoncelli, etc.). The model does address implementational plausibility through three biologically distinct instantiations of the same principle.

Mapping onto Marr's levels for what is offered:
- **Computational**: The problem is building a multi-scale, topographically organized, wiring-efficient feedforward sensory hierarchy from a flat undifferentiated cortical sheet, driven only by internally generated activity before eye-opening.
- **Algorithmic**: Local greedy wiring minimization — prioritize shortest-distance connections from the most active (progenitor) neurons, subject to in/out-degree saturation, sequentially generating discrete areas with inherited topography and mirror reversals at boundaries.
- **Implementational**: Three candidate biological mechanisms (heterosynaptic competition, race-to-threshold, seek-and-prune) are proposed and shown to implement the same algorithm; cell-type differences (projection vs. interneuron connectivity) arise from variation in the distance-scale parameter d_0 or activity-attenuation parameter γ, predicted to have genetic correlates. The paper does not directly map these parameters to specific cell types, molecular markers, or connectivity identified by recording experiments.

---

### Limitations & open questions

- The model uses spatially uniform spontaneous activity (time-averaged retinal waves); finer spatiotemporal wave structure is expected to be needed for more detailed features (orientation maps, ocular dominance columns).
- Only feedforward connections are modeled; top-down (feedback) connections between areas are not generated.
- Laminar cortical structure is absent; the model produces a flat 2D sheet without layer-specific differentiation.
- The model does not yet extend to binocular interactions or ocular dominance formation, requiring two retinas.
- The relationship between growth-rule parameters and specific molecular/genetic factors is hypothesized but not tested; transcriptomic predictions remain to be validated.
- The developmental trajectory predictions that discriminate among growth rules (e.g., in-situ sharpening vs. progressive outward expansion of retinotopy) await developmental neuroimaging experiments in animals at the appropriate age range.
- The model assumes LGN to cortex connectivity is initially non-topographic; in reality some topographic bias likely pre-exists, and the interaction with partial genetic pre-specification is unexplored.
- Extension to parallel/simultaneous (rather than sequential) area development is noted as future work.

---

### Connections & keywords

**Key citations**:
- Katz & Shatz 1996 (synaptic activity and cortical circuit construction)
- Wandell, Dumoulin & Brewer 2007 (visual field maps in human cortex — primary empirical comparison)
- Fiete et al. 2010 (heterosynaptic competition rule for sequence formation in songbird HVC — source of the core learning rule)
- Imam & Finlay 2020 (self-organization of cortical areas — closest prior model)
- Chklovskii, Schikorski & Stevens 2002 (global wiring minimization — contrasted approach)
- Sharma, Angelucci & Sur 2000 (cortical pluripotency / visual inputs drive auditory cortex — motivates generalization)
- Arcaro & Livingstone 2017 (hierarchical retinotopic proto-organization at birth)
- Ackman, Burbridge & Crair 2012 (retinal waves coordinate developing visual system)
- Konkle 2021 (emergent visuotopic maps without feature hierarchy — related SOM approach)

**Named models or frameworks**:
- Local greedy wiring minimization via spontaneous drive (GWM-S)
- Heterosynaptic competition rule
- Race-to-threshold growth rule
- Seek-and-prune growth rule
- Log-conformal mapping (LGN geometry)
- Chemoaffinity hypothesis (Sperry) — contrasted
- Self-organizing maps — contrasted

**Brain regions**:
- Retina, LGN, V1, V2, V3, V4
- Auditory cortex (A1, R, RT)
- Mouse visual cortex (V1, P, LM, AL, RL, PM, RL)

**Keywords**:
- activity-dependent cortical development
- heterosynaptic competition
- visual cortical hierarchy
- retinotopic map formation
- polar angle mirror reversals
- greedy wiring minimization
- self-organized modularity
- spontaneous retinal activity / retinal waves
- cortical parcellation
- convolution-like connectivity
- developmental connectome
- cortical pluripotency
