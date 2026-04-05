---
source_file: chandra2024_visual_cortex_development.md
title: "Self-organized emergence of modularity, hierarchy, and mirror reversals from competitive synaptic growth in a developmental model of the visual pathway"
authors: Sarthak Chandra, Mikail Khona, Talia Konkle, Ila R. Fiete
year: 2024
journal: bioRxiv (preprint, doi: 10.1101/2024.01.07.574543)
paper_type: computational
contribution_type: theoretical
---

### One-line summary

A biologically plausible competitive synaptic growth rule driven by spontaneous retinal activity causes an unstructured cortical sheet to self-organize into a hierarchically connected, concentrically arranged set of discrete visual areas with retinotopic maps and mirror-reversed polar angle at area boundaries.

---

### Background & motivation

The primate visual cortex is organized at three levels simultaneously: architecturally (multiple discrete hierarchically connected areas), spatially (concentric arrangement on the cortical sheet), and topographically (retinotopy with mirror reversals of polar angle at area boundaries). These features emerge before eye-opening, implicating spontaneous activity and genetic factors rather than visual experience. The developmental rules that generate all three organizational levels in concert are unknown. Existing models either require globally specified connectivity or optimization principles that are biologically implausible (NP-hard global wiring minimization) or model only a subset of the organizational properties. The paper asks how much cortical structure can emerge from simple local synaptic growth rules fueled by spontaneous retinal activity alone.

---

### Methods

- **Model architecture**: LGN neurons (arranged according to a log-conformal map of the visual hemifield) project to an initially undifferentiated cortical sheet with all-to-all connectivity; no topographic structure exists at initialization.
- **Spontaneous activity**: Retinal waves are modeled as uniform wide-field activation (spatiotemporal dynamics averaged out over plasticity timescale).
- **Synaptic growth rule (heterosynaptic competition)**: Synapse growth rate is proportional to presynaptic activity and inversely proportional to soma-to-synapse distance. Whenever summed synaptic weights into or out of a neuron exceed a threshold, all weights are decremented by a fixed amount — a multiplicatively competitive rule that prunes weak synapses.
- **Three biologically distinct rules**: In addition to heterosynaptic competition, two alternative rules implementing the same principle are compared — *race-to-threshold* growth (silent synapses become active when accumulated resources cross a distance- and activity-dependent threshold) and *seek-and-prune* growth (stochastic synapse formation followed by pruning based on a permanence factor).
- **Theoretical principle derived**: Local greedy wiring minimization via spontaneous drive (GWM-S) — connections are placed in order of increasing wiring length from the most active progenitor neurons until degree saturation, then the most-innervated set becomes the new progenitor.
- **Generalization**: Model is applied to auditory cortex (tonotopic LGN-analogue projecting to a rectangular strip) and to mouse visual cortex geometry.
- **Cell type extension**: Two interleaved cell types with different distance-scale parameters are simulated simultaneously, predicting projection neuron vs. interneuron connectivity patterns.

---

### Key findings

- Starting from all-to-all unstructured connectivity, competitive synaptic growth spontaneously produces discrete hierarchically connected visual areas (V1–V4) with concentric spatial arrangement matching human posterior occipital cortex.
- Retinotopic eccentricity maps are globally smooth; polar angle maps show mirror reversals at area boundaries — the same hallmarks used experimentally to delineate visual area borders in humans and macaques.
- Connectomic boundaries defined by the number of synaptic hops from LGN coincide exactly with polar angle reversal locations, demonstrating two independent structural measures converging on the same area boundaries.
- Receptive fields increase in size with eccentricity (within each area) and across the hierarchy, consistent with macaque and human data; the model predicts a mild dip in receptive field size at large eccentricities.
- Connectivity between adjacent areas is convolution-like (sparse, local, tiled patches in retinotopic coordinates), providing a bottom-up mechanistic origin for the architectural assumptions built into convolutional deep neural networks.
- Wiring lengths show a sawtooth pattern across areas; in- and out-wiring lengths are inversely correlated within neurons; the full distribution of wiring lengths is bimodal and well-fit by a sum of two lognormals.
- All three growth rules produce the same endpoint organization but distinguishable developmental trajectories: heterosynaptic competition establishes a rough proto-V3 retinotopy that sharpens in situ, whereas seek-and-prune and race-to-threshold rules expand retinotopic coverage from the V2 boundary outward.
- Interneuron-like connectivity (purely local, no feedforward projections) and projection-neuron-like connectivity emerge simultaneously from the same growth rule when two cell types are assigned different distance-scale parameters.
- The GWM-S principle applied to auditory cortex geometry generates tonotopic areas with mirror reversals; applied to mouse visual cortex geometry it reproduces the known visual field coverage pattern including a central hole.
- A regime boundary exists in parameter space (γ, d₀): one side yields hierarchical organization, the other purely local non-hierarchical connectivity — posited as a genetic control knob distinguishing projection neurons from interneurons.

---

### Computational framework

**Competitive synaptic growth / local greedy wiring minimization.** The paper formalizes a developmental algorithm in which synapses grow at a rate ∆ᵢⱼ ∝ aⱼ / (dᵢⱼ/d₀ + 1), where aⱼ is presynaptic firing rate and dᵢⱼ is soma-to-synapse distance, subject to a heterosynaptic competition rule that prunes weak connections whenever total synaptic weight exceeds a per-neuron threshold. Activity propagates linearly across sufficiently strong synapses, attenuated by a factor γ per hop.

The key variables are: synaptic weight matrix W; the distance scale d₀ (governs spatial spread of connectivity); the activity attenuation factor γ (promotes feedforward hierarchy over lateral connections); in/out degree caps k^in, k^out (determine relative area sizes). The framework assumes a separation of timescales between activity propagation (fast) and synaptic plasticity (slow), and that spontaneous retinal activity provides uniform wide-field drive on the plasticity timescale.

The central theoretical claim is that this local, greedy, activity- and distance-dependent process implements a form of wiring minimization that is both biologically plausible and computationally tractable, unlike global wiring minimization approaches (which are NP-hard).

---

### Prevailing model of the system under study

The introduction frames two dominant and opposing views. The chemoaffinity hypothesis (Sperry; Tessier-Lavigne & Goodman) holds that genes directly specify detailed endpoint connectivity — which areas exist, how many, and their topographic organization. The opposing view (Lashley, Turing) treats the brain as a highly plastic blank slate shaped entirely by external inputs. The paper's own framing situates the work in a third, middle-ground position: genes specify only a small number of parameters of a developmental growth program; rich structure then emerges from the dynamics of that program driven by internally generated spontaneous activity. The introduction acknowledges that the formation of hierarchical visual areas, spatial organization, and topographic mirror reversals before eye-opening is well established experimentally, but the developmental rules responsible remain unknown. No prior model is described as providing a synapse-level mechanistic account of all three organizational levels simultaneously.

---

### What this paper contributes

The paper provides the first synapse-level mechanistic model that simultaneously accounts for all three levels of visual cortex organization — discrete areal modularity, concentric spatial arrangement, and retinotopic topography with polar angle mirror reversals — from a single parsimonious growth rule. Key advances over prior work:

- Establishes that area boundaries defined by wiring-hop distance and those defined by topographic mirror reversals are predicted to coincide — a new testable prediction linking two independent organizational measures.
- Proposes that the same principle, applied to different input geometries, explains hierarchical organization across sensory modalities (auditory cortex, mouse visual cortex) — providing a mechanistic account of cortical pluripotency.
- Derives a tractable theoretical principle (GWM-S) from the biological growth dynamics, enabling analytical insight and prediction of structurally distinct but endpoint-equivalent developmental trajectories.
- Generates a full connectome de novo (rather than assuming connectivity), enabling detailed predictions for connectomics experiments including wiring length distributions, eccentricity-dependent receptive field shapes, and a saw-tooth pattern of wiring length across area boundaries.
- Shows that cell-type-specific connectivity patterns (projection neuron vs. interneuron) emerge from the same growth rule via a single parameter difference, providing a developmental account of cell-type specificity.

Key unresolved questions: how spatiotemporal structure of retinal waves drives fine-scale features such as orientation selectivity and ocular dominance columns; how laminar cortical organization arises; whether top-down feedback connections can emerge from similar rules; whether the model extends to higher cortical areas beyond early sensory hierarchies.

---

### Brain regions & systems

- **Primary visual cortex (V1)** — the first-hop area in the hierarchy; emerges as the most strongly LGN-driven region at the center of the modeled cortical sheet.
- **V2, V3, V4** — successive hierarchical areas encircling V1; emerge sequentially as out-degree saturation propagates outward from the LGN-proximal set.
- **Lateral Geniculate Nucleus (LGN)** — modeled as the structured input source; its geometry (log-conformal mapping of the visual hemifield) is the primary architectural constraint driving subsequent cortical organization.
- **Auditory cortex (A1, R, RT)** — modeled by substituting cochlear/MGN geometry for visual input; tonotopic mirror reversals emerge from the same growth rule.
- **Mouse visual cortex (V1, P, PM, LM, RL)** — alternative cortical geometry used to validate generalization; the model reproduces known visual field coverage maps including a central coverage hole.
- **Prefrontal cortex, parietal cortex, cerebellum, striatum, hippocampus** — mentioned in the Discussion as candidate regions where topographic map organization similar to that generated by the model has been observed, suggesting potential generalization of the GWM-S principle.

---

### Mechanistic insight

The paper partially meets the bar. It presents a formalized algorithm (GWM-S / heterosynaptic competition) that could explain the developmental origin of visual area organization, and it provides extensive quantitative comparisons between model outputs and empirical maps (retinotopic eccentricity, polar angle reversals, receptive field size scaling, mouse visual cortex coverage). However, the paper does not provide neural data — recordings, imaging, or lesion studies — that specifically support the model's proposed algorithm over alternatives. The empirical comparisons are with published endpoint anatomical and functional maps, not developmental recordings that would distinguish between the three proposed growth rules or validate the GWM-S mechanism directly.

At the algorithmic level, the paper is detailed: the key computation is local greedy wiring minimization driven by spontaneous activity, where distance-dependent competitive synapse growth sequentially stabilizes the shortest available connections and thereby partitions the cortical sheet into a hierarchy of discrete retinotopic areas. At the implementational level, the paper proposes specific biological substrates — heterosynaptic competition at synapses, presynaptic activity-dependent growth rates, degree caps on individual neurons, and distance-dependent resource trafficking from soma to synapse — and notes that model parameters (d₀, γ, degree caps) may correspond to genetically specified quantities distinguishing cell types and cortical areas. These mechanistic proposals are explicit but remain predictive rather than empirically validated in the paper itself.

---

### Limitations & open questions

- Model covers only the pre-eye-opening backbone connectivity; it does not address feature tuning (orientation selectivity, ocular dominance columns, color maps) that emerges later with patterned visual input.
- Laminar cortical structure and area-specific specializations are not addressed.
- Top-down feedback connections are absent from the model.
- The spatiotemporal structure of retinal waves is averaged out; finer spatiotemporal statistics may be required for more detailed structural features.
- Two retinas would be needed to model ocular dominance stripe formation.
- Developmental trajectory predictions distinguishing the three growth rules (heterosynaptic competition vs. seek-and-prune vs. race-to-threshold) have not been experimentally tested.
- Genetic identity of the model parameters (d₀, γ) remains speculative — specific gene expression patterns are predicted but not identified.
- Generalization to higher cortical areas (prefrontal, parietal) is proposed but not demonstrated.
- The model does not yet incorporate parallel or simultaneous modular circuit development observed in some species.

---

### Connections & keywords

**Key citations**:
- Katz & Shatz 1996 (Science) — synaptic activity and construction of cortical circuits
- Fiete, Senn, Wang, Hahnloser 2010 (Neuron) — heterosynaptic competition rule for sequence formation in songbird HVC (same rule extended here)
- Imam & Finlay 2020 (PNAS) — self-organization of cortical areas in development and evolution (most closely related prior developmental model)
- Chklovskii, Schikorski, Stevens 2002 (Neuron) — global wiring optimization in cortical circuits (contrasted against)
- Wandell, Dumoulin, Brewer 2007 (Neuron) — visual field maps in human cortex (empirical benchmark)
- Konkle 2021 (bioRxiv) — emergent organization of visuotopic maps without feature hierarchy (self-organizing map approach, contrasted against)
- Lee et al. 2020 (bioRxiv) — topographic deep ANNs (global supervised wiring minimization, contrasted against)

**Named models or frameworks**:
- Local greedy wiring minimization via spontaneous drive (GWM-S)
- Heterosynaptic competition growth rule
- Race-to-threshold growth rule
- Seek-and-prune growth rule
- Chemoaffinity hypothesis (Sperry)
- Self-organizing maps (Kohonen; Konkle)
- Log-conformal mapping (retina to LGN)

**Brain regions**: V1, V2, V3, V4, LGN, auditory cortex (A1, R, RT), MGN, mouse visual cortex (V1, P, PM, LM, RL), prefrontal cortex, parietal cortex, cerebellum, striatum, hippocampus

**Keywords**: visual cortex development, synaptic competition, heterosynaptic plasticity, cortical area formation, retinotopic maps, polar angle mirror reversal, wiring minimization, spontaneous retinal activity, retinal waves, self-organization, cortical hierarchy, developmental connectome
