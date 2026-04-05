---
source_file: baram2024_abstract_relational_map_consolidation.md
title: An abstract relational map emerges in the human medial prefrontal cortex with consolidation
authors: Alon Baram, Hamed Nili, Ines Barreiros, Veronika Samborska, Timothy E. J. Behrens, Mona M. Garvert
year: 2024
journal: bioRxiv (preprint)
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Over the course of several days, the human medial prefrontal cortex develops an abstract, stimulus-independent relational map of learned graph structure, while the medial temporal lobe maintains concrete stimulus-specific graph representations across both time points.

---

### Background & motivation

The brain can generalise knowledge to novel situations by representing the relational structure of an environment separately from its specific sensory details — a process sometimes called factorisation. Rodent studies have shown that such abstraction in mPFC occurs over multiple days via consolidation, but direct evidence in humans has been scarce, and it was unclear whether similar timescales and representational formats apply. Prior human neuroimaging work had implicated mPFC in schema-related and structural encoding, and grid-like codes in mPFC had been linked to abstract relational structure, but the time course of how explicit abstract maps emerge after learning had not been directly studied.

---

### Methods

- **Participants**: 23 healthy adult volunteers (aged 18–32; 14 female); scanned twice with at least one scan between sessions.
- **Training**: Three days of online tasks teaching participants the relational structure of two 17-node associative graphs. The two graphs shared identical non-symmetric structure but had different (orthogonalised) distributions of object stimuli across nodes.
- **Scanner task**: Participants viewed random object sequences with context (relevant graph) indicated by background colour; 12.5% of trials required a button-press choice about which of two objects was reachable in fewer steps from a preceding object. Four blocks per session; two fMRI sessions (day 4 and day 4+1 to +7).
- **fMRI repetition suppression**: Parametric modulators indexed distances between consecutive objects on the relevant and irrelevant graphs, separately for stay (same context) and switch (context-change) trials. Used to detect graph representations in MTL (within-graph, stay trials) and abstract cross-graph structure in mPFC (switch trials).
- **Representational similarity analysis (RSA)**: Searchlight on cortical surface; 34×34 RDMs (17 objects × 2 graphs) correlated with model RDMs reflecting distances on an abstracted graph. Kendall's tau-a used; permutation-based FWE correction (PALM). Focused on session 2 > session 1 contrasts following the repetition suppression results.
- **Post-scan arena task**: Subset of participants (n=19) arranged objects spatially to reflect perceived graph distances, enabling explicit assessment of structural knowledge.
- **Statistical approach**: Mixed-effects models for behaviour; small-volume correction (SVC) for ROI analyses in MTL and mPFC; whole-brain FWE cluster correction for other regions.

---

### Key findings

- Participants learned both graph structures well: arena distances correlated strongly with true link distances (t18 = 6.64, p < 0.001 for Graph 1; t18 = 6.56, p < 0.001 for Graph 2).
- Choice task accuracy was well above chance in both sessions and improved from session 1 to session 2 (t21 = 2.94, p = 0.008).
- **MTL**: fMRI repetition suppression identified a cluster in the left MTL (peak t22 = 4.39, MNI [-24, -22, -28]) reflecting distances on both the relevant and irrelevant graph simultaneously. This effect was present in both sessions and did not differ by session or graph relevance (2×2 ANOVA, all p > 0.2).
- **mPFC — repetition suppression (cross-graph)**: A large cluster in mPFC (peak t21 = 5.1, MNI [2, 42, 8]; FWE cluster-corrected p = 0.003) showed cross-graph suppression (distances defined across graph identity), significant across both sessions. This effect was significantly greater in session 2 than session 1 (SVC FWE p < 0.05, t21 = 3.66, peak MNI [4, 40, 12]).
- The session-2 cross-graph effect also emerged within an mPFC ROI defined by grid-like coding of abstract relationships from Constantinescu et al. (2016) (SVC FWE p = 0.03, t21 = 2.38).
- **mPFC — RSA**: A cluster in right pregenual mPFC showed emergence of a full abstracted map (both within- and across-graph RDM elements) from session 1 to session 2 (SVC FWE p = 0.01). Separate within-graph (p = 0.06) and across-graph (p = 0.11) RSA analyses showed trends in the same mPFC subregion, with each surviving SVC correction in the other's mask (p = 0.03 and p = 0.01), suggesting a shared representational substrate.
- Behavioural effects of graph distance on response times correlated with arena task performance: better structural knowledge predicted stronger RT effects for relevant distances and weaker distraction by irrelevant distances.

---

### Computational framework

The paper does not propose a new computational model. The implicit theoretical framework is **cognitive map / relational structure abstraction**, drawing on the Tolman-Eichenbaum Machine (TEM; Whittington et al., 2020) and related theories. The core idea is factorisation: separating a representation of abstract relational structure (the graph topology) from the identities of the stimuli instantiating that structure. This is operationalised as a "cross-graph" representational format, in which the brain encodes the position of a stimulus within its graph independently of which specific stimulus occupies that position.

Methodologically, the paper uses fMRI repetition suppression and RSA as readouts of representational geometry, using graph-theoretic distances (shortest-path link distances) as the key variable relating neural similarity to structural knowledge.

---

### Prevailing model of the system under study

The introduction frames two converging literatures. First, mPFC is established as a site for schema-like or structural generalisation in humans, with grid-like codes (analogous to entorhinal grid cells) seen during navigation of abstract 2D spaces (Constantinescu et al., 2016; Doeller et al., 2010). These grid-like signals have been interpreted as encoding statistical regularities common across environments, factorised from specific sensory details. Second, systems consolidation theory (McClelland et al., 1995) holds that memories change qualitatively over days-to-weeks: hippocampus/MTL initially stores episodic specifics, while neocortex/mPFC gradually extracts the statistical structure shared across episodes. Rodent work (e.g. Tse et al., 2007, 2011; Morrissey et al., 2017) showed this concretely: mPFC initially represents perceptual features of associations and over time shifts to represent the relational features common across them. In humans, evidence for analogous consolidation-driven abstraction was thin, and the representational form (i.e. an explicit relational map) had not been directly demonstrated.

---

### What this paper contributes

This paper provides direct human neuroimaging evidence that: (1) the MTL simultaneously represents both task-relevant and task-irrelevant graph knowledge at both time points tested; and (2) mPFC develops an abstract, stimulus-independent structural representation — a "relational map" — over the course of several days, without additional training between sessions. Crucially, the abstraction is demonstrated in two fully independent analyses (repetition suppression and RSA), strengthening the interpretation. The paper shows that the mPFC map is genuinely abstract in the sense that it responds to positional commonality across graphs (cross-graph suppression), not merely to within-graph distances. It localises this effect to pregenual mPFC, the same region previously implicated in grid-like coding, bridging the consolidation and cognitive-map literatures. Before this paper, it was unclear whether human mPFC underwent consolidation-driven abstraction on the timescale of days, and what representational format such abstraction would take.

---

### Brain regions & systems

- **Medial temporal lobe (MTL) / left entorhinal cortex–subiculum** — primary locus of both relevant and irrelevant graph representations across both sessions; represents specific stimulus-in-graph associations rather than abstract structure.
- **Medial prefrontal cortex (mPFC) / pregenual mPFC (Brodmann areas 24/32, MNI ~[2, 42, 8])** — locus of abstract, cross-graph relational map; representation emerges over days and is independent of specific stimulus identities; overlaps with region showing grid-like coding of abstract 2D spaces (Constantinescu et al., 2016).

---

### Mechanistic insight

The paper meets the first criterion (it operationalises and tests for a specific algorithm: cross-graph, stimulus-independent structural encoding) and provides fMRI data (BOLD repetition suppression and RSA) supporting this representation over an alternative (stimulus-specific encoding). However, BOLD repetition suppression is an indirect population-level measure that does not identify specific cell types or biophysical mechanisms. It cannot, by itself, distinguish between grid cells, place-like cells, or other coding formats. The paper notes this limitation explicitly: "these indirect repetition suppression effects do not allow us to make any inference about the particular types of cells involved."

Mapping onto Marr's levels:
- **Computational**: The brain needs to extract task-invariant relational structure from experience so that structural knowledge can be transferred to new situations with the same statistics.
- **Algorithmic**: The mPFC computes a factorised representation in which object identity is separated from graph-positional identity, enabling cross-graph generalisation. This representation emerges over multiple days (presumably via offline consolidation).
- **Implementational**: Unresolved at the cellular level. The paper notes topographic overlap with mPFC grid-like signals (Constantinescu et al., 2016) and speculatively invokes neural replay as a candidate mechanism, but provides no direct evidence for either.

The paper does not fully meet the bar because it lacks neural data at the algorithmic or implementational level sufficient to distinguish between candidate mechanisms.

---

### Limitations & open questions

- The consolidation mechanism is not directly probed: no sleep recordings, no replay measurements, and no causal manipulations. The emergence of the abstract map between sessions is inferred from two fMRI timepoints; whether it depends on sleep, number of days, or offline reactivation is unknown.
- The fMRI repetition suppression technique cannot resolve the cell types or microcircuit mechanisms underlying abstract coding in mPFC.
- RSA effects for within-graph and across-graph elements separately did not reach significance (p = 0.06 and p = 0.11), raising a statistical power concern. The full-RDM RSA result and the cross-survival corrections are suggestive but not conclusive.
- The cross-graph suppression effect was strongest on switch trials; whether an abstract map is represented on stay trials remains unclear due to the trial-number constraints that precluded RSA on switch trials alone.
- The sample is relatively small (n = 23; one participant missing session 2), and the inter-session interval varied (1–7 days), potentially masking dose-response relationships between time and abstraction.
- The paper does not address whether the abstract mPFC map generalises to new tasks or environments (structural transfer), which is the functional consequence most emphasised in the framing.
- Whether the MTL plays any role in the initial acquisition of relational structure that is later extracted by mPFC is not directly tested.

---

### Connections & keywords

**Key citations**:
- Behrens et al. (2018) — cognitive map framework
- Whittington et al. (2020) — Tolman-Eichenbaum Machine; factorisation of structure
- Garvert et al. (2017) — MTL abstract relational map; fMRI repetition suppression
- Constantinescu et al. (2016) — grid-like coding of abstract 2D knowledge in mPFC
- McClelland et al. (1995) — complementary learning systems; neocortical consolidation
- Tse et al. (2007, 2011) — mPFC schema consolidation in rodents
- Kriegeskorte et al. (2008) — representational similarity analysis
- Barron, Garvert & Behrens (2016) — fMRI repetition suppression as representational readout
- Tompary & Davachi (2017) — human mPFC representational overlap post-consolidation
- Mark et al. (2024) — entorhinal flexible structural representations

**Named models or frameworks**:
- Tolman-Eichenbaum Machine (TEM)
- fMRI repetition suppression
- Representational similarity analysis (RSA)
- Complementary learning systems (CLS) theory
- Graph-learning paradigm (two isomorphic graphs with orthogonalised object distributions)

**Brain regions**:
- Medial temporal lobe (MTL)
- Entorhinal cortex / subiculum
- Medial prefrontal cortex (mPFC) / pregenual mPFC

**Keywords**:
- cognitive map consolidation
- abstract relational structure
- medial prefrontal cortex abstraction
- medial temporal lobe graph representation
- fMRI repetition suppression
- representational similarity analysis
- structural generalisation
- systems consolidation
- graph-learning task
- cross-graph transfer
- schema abstraction
- factorised representations
