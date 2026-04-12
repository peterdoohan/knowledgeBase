---
source_file: nour2021_impaired_replay_schizophrenia.md
paper_id: nour2021_impaired_replay_schizophrenia
title: "Impaired neural replay of inferred relationships in schizophrenia"
authors:
  - "Matthew M. Nour"
  - "Yunzhe Liu"
  - "Atheeshaan Arumuham"
  - "Zeb Kurth-Nelson"
  - "Raymond J. Dolan"
year: 2021
journal: Cell
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - representational_similarity_analysis
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_temporal_lobe
keywords:
  - hippocampal_replay
  - sharp_wave_ripple
  - schizophrenia
  - cognitive_map
  - transitive_inference
  - meg
  - tdlm
  - sequenceness
  - relational_memory
  - structural_inference
  - representational_similarity_analysis
  - post_learning_rest
  - impaired
  - neural
  - replay
  - inferred
  - relationships
key_citations:
  - liu2019_human_replay_reorganizes
  - kurth_nelson2016_sequences_non_spatial
  - suh2013_impaired_ripple
  - barron2020_neuronal_computation_inferential
  - behrens2018_cognitive_map_organizing_knowledge
  - garvert2017_relational_knowledge_maps
wiki_pages:
  - wiki/topics/computational_models_of_schizophrenia_attractor_dynamics_and_nmda_hypofunction
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
---

### One-line summary

Patients with schizophrenia show reduced spontaneous neural replay of inferred sequential relationships during post-learning rest, co-occurring with elevated hippocampal ripple power and distorted neural representations of task structure, mirroring abnormalities seen in rodent schizophrenia models.

---

### Background & motivation

Schizophrenia is characterised by distorted associative representations, impairments in relational inference, and well-replicated hippocampal structural and functional abnormalities. In rodents, genetic mouse models of schizophrenia show disrupted hippocampal sharp wave–ripple (SWR) complexes and impaired sequential place cell reactivation (replay) during rest. Whether analogous replay abnormalities exist in human patients, and whether they link to impairments in model-based cognitive map construction, had not been tested non-invasively before. This paper fills that gap by leveraging MEG-based replay detection methods to test the hypothesis that impaired hippocampal replay underlies the relational inference deficits characteristic of schizophrenia.

---

### Methods

- **Participants**: 28 patients with schizophrenia (13 unmedicated) and 27 healthy controls, matched for age, sex, IQ, and educational attainment; all tested at a London MEG facility.
- **Task (structural inference)**: Participants first learned an "unscrambling rule" during a pre-scan training visit, then applied it to a new picture set during MEG. They passively observed scrambled visual sequences and had to infer the correct sequential embedding (linear chains of 4 pictures each) of 8 novel pictures.
- **Knowledge assessment**: Quizzes after each of three Applied Learning sessions assessed within-sequence (order) and cross-sequence (set membership) knowledge separately; a sequence learning efficiency measure was derived to isolate impairments specific to sequential order inference.
- **MEG replay detection (TDLM)**: Stimulus-specific multivariate decoders trained on a pre-learning Stimulus Localizer were applied to a 5-minute post-learning rest session. Temporally Delayed Linear Modelling (TDLM) quantified forward and backward sequenceness (asymmetry of sequential state reactivation) at lags from 10–600 ms.
- **Ripple analysis**: Replay onsets (>95th percentile sequential reactivation probability at 40 ms lag) were used to epoch MEG data for time-frequency analysis (120–150 Hz). Source reconstruction used LCMV beamforming.
- **High co-activation analysis**: Epochs of high instantaneous co-reactivation were used to probe reactivation separation for structurally adjacent versus distant state pairs, and an "inferential reactivation" measure tested whether transitive associations were preferentially replayed.
- **Representational Similarity Analysis (RSA)**: Learning-induced changes in whole-brain evoked-response similarity between picture pairs (Stimulus Localizer vs. Position Probe) were regressed onto design matrices encoding position, within-sequence adjacency, and cross-sequence adjacency representations.

---

### Key findings

- Patients showed a specific impairment in sequence learning efficiency (Z = 2.81, p = 0.005), selectively affecting within-sequence order knowledge; cross-sequence (set membership) learning was not impaired. The deficit was most pronounced for transitive inferences.
- Controls exhibited significant forward sequenceness during post-learning rest at 40–60 ms lags (peak at 50 ms: β = 1.31 ± 0.33, PFWE < 0.001), whereas patients showed no significant sequenceness at any lag (peak non-significant: β = 0.49 ± 0.41, PFWE = 0.80).
- A group × session interaction confirmed that the experience-induced boost in replay (post- minus pre-learning sequenceness) was significantly greater in controls than patients (F(1,52) = 8.08, p = 0.006); this effect held after excluding medicated patients.
- Replay-associated ripple power (120–150 Hz) was significantly elevated in patients versus controls at replay onset (2.69 ± 0.12 vs. 1.89 ± 0.15, t(51) = −2.6, p = 0.01), mirroring rodent model findings.
- Source reconstruction localised replay-associated ripple power to the left medial temporal lobe (hippocampus) in the combined sample (PFWE < 0.05 whole-brain corrected).
- In high co-activation epochs, patients showed a blunted reactivation-separation gradient for structurally close versus far state pairs (group × distance interaction: F(1,52) = 12.2, p = 0.001), and a reduced inferential reactivation signature (group × session interaction: F(1,52) = 4.46, p = 0.04).
- RSA revealed that controls alone formed a significant abstracted position representation following learning (cluster PFWE = 0.032), while patients instead showed "confusion" representations (similarity for adjacent pictures). Group × representation ANOVA interaction: F(2,106) = 4.03, p = 0.02.
- Across patients, sequence learning efficiency positively predicted both post-learning sequenceness (r(25) = 0.39, p = 0.044) and the strength of the position representation (r(26) = 0.52, p = 0.005).
- In patients, replay-associated ripple power predicted the strength of the emergent position representation (r(24) = 0.48, p = 0.012; significant group difference in this relationship, binteraction = −0.035, p = 0.042), suggesting a compensatory role for augmented SWR power.
- No effects were attributable to antipsychotic medication.

---

### Computational framework

The paper uses a **cognitive map** framework rooted in hippocampal-entorhinal representations of relational structure. The core computational idea is that the hippocampus builds structured internal models (maps) of the world by encoding abstract sequential relationships between entities; these maps are extended and consolidated through offline replay and sharp wave–ripple events.

**Key variables and formalisms**:
- *Sequenceness* (forward minus backward TDLM regression coefficient): operationalises the degree to which spontaneous neural state reactivations during rest follow the inferred sequential order of task states, at a given temporal lag.
- *TDLM*: a two-stage lagged regression approach that first estimates pairwise state-to-state reactivation coefficients at each lag, then regresses this empirical transition matrix onto the hypothesised task structure matrix.
- *Ripple power*: 120–150 Hz high-frequency oscillatory power co-occurring with replay onsets; used as a proxy for SWR activity.
- *RSA position representation*: quantifies whether pictures at the same ordinal position in different sequences acquire more similar neural representations after learning.

The framework assumes that replay "stitches together" associative memories to enable transitive inference — that is, replay is not merely a record of experienced transitions but actively encodes inferred, unobserved relationships.

---

### Prevailing model of the system under study

The introduction frames the field as holding the following baseline understanding: (1) the hippocampal-entorhinal cortex (HEC) supports cognitive map-like representations for both spatial and non-spatial relational structures; (2) during rest, sequential place cell reactivation (replay) co-occurs with sharp wave–ripples and contributes to memory consolidation and the extension of relational knowledge beyond direct experience; (3) schizophrenia involves distorted associative representations, with clinical manifestations (delusions, conceptual disorganisation) proposed to reflect a compromise in structured mental representations. Prior to this paper, animal model work had shown hippocampal replay and ripple abnormalities in genetic mouse models of schizophrenia, but it was unknown whether analogous deficits existed in human patients or whether they related to the specific cognitive impairments characteristic of the disorder.

---

### What this paper contributes

The paper provides the first direct evidence in humans that schizophrenia is associated with: (1) reduced spontaneous offline neural replay of inferred (non-spatial) sequential structure; (2) elevated hippocampal ripple power at replay events — an exact parallel to rodent model findings; and (3) a failure to form abstracted position representations of task structure. Together, these converging abnormalities link neurobiological findings in animal models to specific cognitive impairments (relational/transitive inference) in human patients. The results support the hypothesis that impaired hippocampal replay, and the resulting failure to build or consolidate cognitive maps, provides a neurocomputational mechanism connecting known hippocampal pathophysiology in schizophrenia to its higher-order cognitive and symptomatic features. The finding that augmented ripple power in patients correlates with what position representation does emerge suggests a compensatory, rather than simply degraded, SWR dynamic.

---

### Brain regions & systems

- **Hippocampus (left medial temporal lobe)** — primary locus of replay-associated ripple power; source reconstructed as the origin of 120–150 Hz oscillations at replay onsets; proposed site of cognitive map construction and consolidation.
- **Hippocampal-entorhinal cortex (HEC)** — treated as the system supporting map-like relational representations across spatial and non-spatial domains; the theoretical target of the study's hypotheses.
- **Default mode network (DMN)** — discussed in the context of hippocampal SWR coupling with DMN at rest, and its relationship to imaginative and compositional cognition implicated in psychosis; not directly measured.

---

### Mechanistic insight

The paper partially meets the bar. It proposes a specific algorithm (TDLM-measured sequential replay as the mechanism linking learning to relational inference) and provides neural data (MEG sequenceness, ripple power localised to hippocampus via beamforming, RSA position representations) supporting that algorithm's differential operation in patients versus controls.

**Computational**: The brain is solving the problem of extending knowledge beyond directly observed transitions — forming a relational cognitive map that enables transitive inference. This requires an internal model of sequential structure that goes beyond memorised pairwise associations.

**Algorithmic**: Spontaneous offline sequential reactivation (replay) of inferred state transitions, co-occurring with hippocampal SWRs, consolidates and extends the relational map. In controls, replay is predominantly forward, occurs at ~40–50 ms transition lags, and correlates with the emergence of an abstracted position representation. In patients, this replay sequence is disrupted even when explicit declarative knowledge of task structure is matched at ceiling — suggesting the deficit is in the automatic consolidation process, not in explicit knowledge storage per se.

**Implementational**: The paper does not directly identify cell types, specific connectivity, or neuromodulators. However, it links its findings to the broader schizophrenia literature on hippocampal excitation–inhibition imbalance (cortical E/I perturbation in mouse models disrupts both SWRs and replay). Elevated ripple power in patients is interpreted in light of pathologically hypersynchronous hippocampal activity (cf. temporal lobe epilepsy parallels), possibly reflecting disinhibition or NMDA receptor dysfunction. This level of implementation is cited from prior rodent and pharmacological work rather than measured directly here.

---

### Limitations & open questions

- Group differences might in principle reflect confounds of motivation or attention, though the authors argue against this based on matched task engagement and decoding accuracy.
- MEG has limited sensitivity to high-frequency power from deep structures such as hippocampus; ripple analyses are therefore potentially underpowered and must be interpreted cautiously.
- Replay-conditional ripple detection introduces an inherent bias toward underestimating ripple power in patients (where replay evidence is weaker), meaning the reported patient elevation is conservative.
- No direct causal evidence that replay drives (rather than correlates with) relational map formation; causal manipulation of replay is identified as a key priority.
- Replay strength does not correlate with subjectively reported symptoms, raising questions about whether the deficit is a trait-level marker with a complex relationship to time-varying clinical state.
- Specificity to schizophrenia versus other psychotic or neurological disorders (e.g., temporal lobe epilepsy, which also shows pathological ripples) remains unresolved.
- The relationship between replay and the putative neural representation of task structure present during learning itself is speculative; the study cannot disentangle whether replay drives schema formation or reflects pre-existing differences in schema strength.

---

### Connections & keywords

**Key citations**:
- Liu et al. (2019) — *Cell* — Human replay spontaneously reorganises experience; source of the TDLM method and structural inference task used here.
- Liu et al. (2021a) — *eLife* — TDLM validation paper.
- Kurth-Nelson et al. (2016) — *Neuron* — Fast sequences of non-spatial state representations in humans; prior MEG replay method.
- Suh et al. (2013) — *Neuron* — Impaired hippocampal ripple-associated replay in a mouse model of schizophrenia.
- Barron et al. (2020) — *Cell* — Neuronal computation underlying inferential reasoning in humans and mice.
- Behrens et al. (2018) — *Neuron* — What is a cognitive map? Organising knowledge for flexible behaviour.
- Garvert et al. (2017) — *eLife* — Map of abstract relational knowledge in human HEC.
- Wimmer et al. (2020) — *Nature Neuroscience* — Episodic memory retrieval success associated with rapid replay.
- Altimus et al. (2015); Zaremba et al. (2017) — rodent schizophrenia models with replay/ripple abnormalities.

**Named models or frameworks**:
- Temporally Delayed Linear Modelling (TDLM)
- Cognitive map (Tolman/O'Keefe & Nadel framework)
- Representational Similarity Analysis (RSA)
- Sharp wave–ripple (SWR) framework

**Brain regions**:
- Hippocampus (left medial temporal lobe)
- Hippocampal-entorhinal cortex (HEC)
- Default mode network (DMN)

**Keywords**: hippocampal replay, sharp wave ripple, schizophrenia, cognitive map, transitive inference, MEG, TDLM, sequenceness, relational memory, structural inference, representational similarity analysis, post-learning rest

### Related wiki pages
- [[wiki/topics/computational_models_of_schizophrenia_attractor_dynamics_and_nmda_hypofunction|Computational models of schizophrenia: attractor dynamics and NMDA hypofunction]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
