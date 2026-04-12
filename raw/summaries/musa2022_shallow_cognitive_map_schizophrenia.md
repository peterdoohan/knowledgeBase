---
source_file: musa2022_shallow_cognitive_map_schizophrenia.md
paper_id: musa2022_shallow_cognitive_map_schizophrenia
title: "The shallow cognitive map hypothesis: A hippocampal framework for thought disorder in schizophrenia"
authors:
  - "Ayesha Musa"
  - "Safia Khan"
  - "Minahil Mujahid"
  - "Mohamady El-Gaby"
year: 2022
journal: Schizophrenia
paper_type: review
contribution_type: theoretical
species:
  - mouse
methods:
  - electrophysiology
  - fmri
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - prefrontal_cortex
  - superior_temporal_gyrus
  - inferior_frontal_gyrus
frameworks:
  - bayesian_inference
  - attractor_networks
keywords:
  - attractor_dynamics
  - hippocampal_cognitive_maps
  - positive_formal_thought_disorder
  - pattern_separation
  - pattern_completion
  - sharp_wave_ripples
  - hippocampal_replay
  - schizophrenia_circuit_pathology
  - pv_interneurons
  - aberrant_salience
  - hippocampal_prefrontal_synchrony
  - relational_memory
  - shallow
  - cognitive
  - map
  - hypothesis
  - hippocampal
  - framework
  - thought
  - disorder
key_citations:
  - nour2021_impaired_replay_schizophrenia
  - behrens2018_cognitive_map_organizing_knowledge
  - suh2013_impaired_ripple
  - adams2018_attractor_schizophrenia
  - tolman1948_cognitive_maps_rats
wiki_pages:
  - wiki/debates/grid_cells_as_a_mechanism_for_path_integration
  - wiki/topics/sharp_wave_ripple_associated_hippocampal_replay
---

### One-line summary

The "shallow cognitive map hypothesis" proposes that positive formal thought disorder in schizophrenia arises from the shallowing of hippocampal attractor states, which disorganizes the relational cognitive maps needed for coherent thought.

---

### Background & motivation

Positive formal thought disorder (conceptual disorganization, tangentiality, derailment) is a defining feature of schizophrenia, yet its neural and computational basis remains poorly understood. The hippocampus is known to support relational cognitive mapping — the ability to organize memories into structured representations supporting flexible inference — and hippocampal pathology is strongly implicated in schizophrenia. Prior dynamical-systems accounts suggested that shallow cortical attractors could give rise to thought disorder, but these were not grounded in hippocampal cognitive-mapping mechanisms specifically. This paper attempts to unify hippocampal circuit-level pathologies observed in schizophrenia under a single overarching computational principle: the shallowing of hippocampal attractors.

---

### Methods

This is a narrative theoretical review. The synthesis covers:

- Computational and dynamical-systems accounts of hippocampal function (attractor networks, pattern separation/completion, place cell replay)
- Human neuroimaging and electrophysiology studies in schizophrenia patients (fMRI, MEG, PET, cerebral blood volume MRI)
- Rodent in vivo electrophysiology studies using genetic mouse models of schizophrenia (Df(16)A+/−, GriA1 knockout, Nogo-A knockout, PGC-1α knockout, DISC1 overexpression)
- Postmortem and molecular studies of hippocampal circuit elements in schizophrenia
- GWAS and gene expression data relevant to synaptic plasticity genes
- Epigenetic findings linking environmental factors (e.g. childhood trauma) to hippocampal molecular changes

No formal inclusion criteria or quantitative meta-analytic methods are employed; evidence is synthesized narratively around three testable predictions.

---

### Key findings

(As a theoretical review, these are the key conclusions drawn from synthesized literature rather than original findings.)

- Hippocampal offline replay of sequential representations is impaired in schizophrenia, as evidenced by MEG studies (Nour et al. 2021) showing impaired neural replay of inferred relationships alongside augmented hippocampal ripple power; this mirrors results in multiple rodent schizophrenia models.
- Representational analysis in patients (Nour et al.) revealed that item representations systematically confused adjacent elements across distinct sequences, consistent with disorganized relational mapping rather than simple memory loss.
- Multiple apparently contradictory hippocampal circuit pathologies — reduced dentate gyrus pattern separation, enhanced CA3 pattern completion, loss of PV interneurons, aberrant salience via GluA1/AMPA dysfunction, loss of CA1 goal-location overrepresentation — can all be understood as convergent routes to shallowing hippocampal attractors.
- Hippocampal hyperactivity at rest (correlated with psychotic symptoms) and hypoactivity during hippocampus-dependent tasks may be reconciled: enhanced offline ripple power may reflect a compensatory response to impaired online relational processing.
- GWAS risk genes for schizophrenia are enriched in hippocampus and frontal cortex, and disproportionately implicate synaptic plasticity genes (GluA1, GluN2A), consistent with the framework.
- Epigenetic mechanisms (REST-mediated NMDA receptor subunit switching, histone deacetylase changes) may link environmental risk factors to increased CA3 LTP capacity and thus to disorganized cognitive maps.
- The framework generates specific predictions: positive correlation between conceptual disorganization (PANSS) and (i) relational memory task impairment, (ii) representational confusion across sequences, and (iii) cross-sequence jumps during awake replay.

---

### Computational framework

The paper is grounded in the **dynamical systems / attractor network** framework.

The core formalism models hippocampal network states as a high-dimensional energy landscape. Discrete attractors (energy valleys) represent distinct memories or contexts; the depth of each valley determines how persistently the network occupies that state and how much perturbation is required to transition to a different attractor. Key quantities:

- **Attractor depth**: determined by the balance of recurrent excitatory connectivity (CA3-CA3), feedforward excitation, and GABAergic inhibition. Deeper attractors = more stable, more distinct memories.
- **Pattern separation** (dentate gyrus/CA3): orthogonalises overlapping inputs, deepening the energy barriers between attractors for distinct experiences.
- **Pattern completion** (CA3 recurrent): retrieves full memories from partial cues by pulling the network into an existing attractor; excessive PC lowers inter-attractor barriers.
- **Replay** (SWR-associated or theta-sequence-based): modelled as trajectories through the attractor landscape, with coherent replay reflecting well-separated, deep attractors.

The framework assumes that shallowing of this landscape — whether via reduced inhibition, altered LTP, or other mechanisms — lowers the energy cost of transitions between unrelated attractor states, generating the aberrant associations that manifest as thought disorder.

---

### Prevailing model of the system under study

Before this paper, the field held the following working model:

1. Schizophrenia involves widespread pathology across multiple brain regions including hippocampus, prefrontal cortex, and temporal cortex, with no single unifying computational account.
2. Hippocampal pathologies (interneuron loss, LTP dysregulation, pattern separation deficits, hyperactivity at rest) were documented as a collection of largely independent circuit-level findings — notably, the direction of plasticity changes was contradictory across studies (both enhanced and impaired LTP reported).
3. Thought disorder was primarily attributed to cortical (prefrontal, temporal) dysfunction, including disrupted semantic networks, with hippocampal involvement acknowledged but not mechanistically integrated.
4. The "shallow attractor" idea had been proposed for cortical networks generally (Loh, Rolls & Deco 2007; Hamm et al. 2017; Adams et al. 2018), but was not linked specifically to hippocampal cognitive-mapping computations.
5. Cognitive mapping impairments (relational memory, transitive inference) were documented in schizophrenia patients, but their relationship to the attractor dynamics underlying thought disorder had not been formally drawn.

---

### What this paper contributes

The paper does not present new data but makes a novel theoretical synthesis. Its key contributions are:

1. **Unification**: Shows that the diverse and apparently contradictory hippocampal circuit pathologies of schizophrenia can all be understood as different routes to a single computational outcome — shallowing of attractor depth — regardless of whether pathology increases or decreases plasticity.
2. **Specificity of mechanism**: Links the general "shallow attractor" idea to hippocampal cognitive-mapping computations specifically (replay, pattern separation/completion, goal overrepresentation), grounding it in a well-characterised neural substrate.
3. **Explaining dissociations**: Provides an account of why relational/inferential memory is selectively impaired early in disease progression, while direct associative memory is relatively preserved — inferred relational attractors are shallower by default and thus more vulnerable.
4. **Predictive framework**: Generates explicit, testable predictions linking attractor depth to symptom severity (conceptual disorganization PANSS subscores), replay organisation, and molecular/genetic stratification.
5. **Treatment implications**: Suggests that understanding thought disorder as shallow cognitive maps licenses a combinatorial pharmacological + cognitive-behavioural approach, with potential for personalised interventions targeting distinct aetiological streams.

The open questions it identifies as key unresolved issues include: whether hippocampal versus cortical replay is primarily impaired; whether replay is disorganized (aberrant inter-sequence transitions) versus simply absent; how hippocampal-cortical (PFC, STG) interaction deficits contribute; and whether attractor shallowing in one region drives shallowing in connected regions via activity-dependent cross-regional plasticity.

---

### Brain regions & systems

- **Hippocampus (general)** — primary locus of analysis; proposed site of shallow attractor dynamics driving disorganized cognitive maps and thought disorder
- **Dentate gyrus (DG)** — pattern separation; impaired in schizophrenia via interneuron loss and reduced glutamate release, proposed to reduce inter-attractor barriers
- **CA3** — pattern completion via recurrent excitatory connectivity; proposed to be hyperactive and excessively associative in schizophrenia, driving shallow attractor transitions; locus of GluA1/AMPA-mediated aberrant salience
- **CA1** — goal-location overrepresentation (goal attractor deepening); impaired in schizophrenia mouse models (Df(16)A+/−); NMDA-receptor-dependent
- **Prefrontal cortex (PFC, including dorsolateral, medial, orbital)** — proposed to host analogous cognitive map attractors for task-space and abstract relational maps; hippocampal-PFC theta coherence is impaired in schizophrenia; PFC attractor shallowing tentatively linked to working memory deficits and possibly delusions
- **Superior temporal gyrus (STG)** — implicated in formal thought disorder via semantic processing; hippocampal-STG theta synchrony proposed to support semantic cognitive mapping
- **Inferior frontal gyrus** — implicated in semantic/language networks associated with formal thought disorder (referenced but not central to the framework)
- **Entorhinal cortex** — hippocampal input region; recurrent entorhinal-CA3 synapses implicated in metaplastic enhancement of CA3 pattern completion

---

### Mechanistic insight

The paper proposes a mechanistic account but does not itself provide neural recordings. It does not fully meet the bar as defined: it synthesises existing neural data (recordings from rodent models, MEG/fMRI from patients) in support of the attractor-shallowing algorithm, but no single dataset in the review provides direct evidence linking the specific attractor-depth variable to measured neural activity while also ruling out alternative accounts.

Mapping onto Marr's levels as articulated by the paper:

- **Computational**: The hippocampus solves the problem of building structured relational maps from experience, enabling coherent inferential thought. In schizophrenia, the system fails to maintain distinct, stable representations for separate relational contexts.
- **Algorithmic**: Pattern separation orthogonalises inputs to deepen inter-attractor barriers; recurrent CA3 activity instantiates pattern completion to traverse intra-attractor states; SWR-associated replay sequences trajectories through the attractor landscape to consolidate and retrieve relational structure. Shallowing of the attractor landscape — via any of several pathological routes — reduces the energy cost of transitions between unrelated attractors, producing disorganized replay and aberrant associations.
- **Implementational**: Specific cellular substrates discussed include PV interneuron loss (in DG, CA3, CA1) reducing inhibitory control of excitatory spread; dysregulated LTP at CA3-CA3 and CA3-CA1 synapses (both enhanced and impaired, with attractor-depth framing reconciling this); GluA1 (AMPA) dysfunction in CA2/CA3 mediating aberrant salience; GluN2B-containing NMDA receptor upregulation in CA3 linked to enhanced LTP capacity; REST-mediated epigenetic remodelling of NMDA receptor subunit composition; reduced DG neurogenesis and glutamate release. The physical implementation is discussed at the level of identified cell types, receptor subunits, and synaptic connectivity, though causal chains from molecule to attractor depth to behaviour remain largely incomplete.

The paper does not meet the high bar for this section because no single study it cites provides neural data specifically supporting the attractor-shallowing algorithm over alternatives (e.g., pure loss-of-function without attractor-landscape interpretation). The mechanistic picture is synthesised across multiple partial datasets.

---

### Limitations & open questions

- The framework currently lacks a formal mathematical instantiation that would allow quantitative predictions about the relationship between specific circuit parameters and attractor depth.
- Whether hippocampal replay is disorganized (cross-sequence intermixing) versus simply impaired (loss of function) remains empirically unresolved; Nour et al. did not find direct evidence for disorganized replay per se.
- Causal directionality is unclear: hippocampal pathology is proposed as a driver of hyperdopaminergia and cortical dysfunction, but the reverse is also plausible.
- Studies in schizophrenia patients typically exclude those with severe thought disorder (for ethical reasons), creating a systematic gap in precisely the patients most relevant to testing the framework.
- The relationship between offline rest replay and on-task sequential activity (theta sequences) and their respective contributions to thought disorder is unclear.
- It is not established whether attractor shallowing in hippocampus drives shallowing in connected regions (mPFC, STG) or vice versa, leaving the circuit-level propagation of pathology unresolved.
- Pattern completion enhancement in CA3, while theoretically central, lacks direct in vivo electrophysiological or behavioural demonstration in schizophrenia patients or most animal models reviewed.
- How the framework integrates with predictive coding / Bayesian accounts of psychosis (briefly mentioned in the conclusions) is not developed.

---

### Connections & keywords

**Key citations**:
- Nour et al. (2021) — impaired neural replay of inferred relationships in schizophrenia (Cell)
- Behrens et al. (2018) — cognitive map framework (Neuron)
- Tamminga, Stan & Wagner (2010) — hippocampal formation in schizophrenia; PS/PC imbalance hypothesis
- Zaremba et al. (2017) — impaired hippocampal place cell dynamics in 22q11.2 deletion mouse model
- Suh et al. (2013) — impaired hippocampal ripple-associated replay in schizophrenia mouse model
- Adams et al. (2018) — attractor-like dynamics in belief updating in schizophrenia
- Sigurdsson et al. (2010) — impaired hippocampal-prefrontal synchrony in schizophrenia mouse model
- Loh, Rolls & Deco (2007) — dynamical systems hypothesis of schizophrenia
- Tolman (1948) — cognitive maps in rats and men

**Named models or frameworks**:
- Shallow cognitive map hypothesis
- Attractor network / dynamical systems framework
- Pattern separation / pattern completion framework (DG/CA3)
- Wagner's model of stimulus processing (aberrant salience)
- Sharp-wave ripple (SWR) replay
- Theta sequences

**Brain regions**:
- Hippocampus (DG, CA3, CA1)
- Prefrontal cortex (dorsolateral, medial, orbital)
- Superior temporal gyrus
- Inferior frontal gyrus
- Entorhinal cortex

**Keywords**:
- attractor dynamics
- hippocampal cognitive maps
- positive formal thought disorder
- pattern separation
- pattern completion
- sharp-wave ripples
- hippocampal replay
- schizophrenia circuit pathology
- PV interneurons
- aberrant salience
- hippocampal-prefrontal synchrony
- relational memory

### Related wiki pages
- [[wiki/debates/grid_cells_as_a_mechanism_for_path_integration|Grid cells as a mechanism for path integration]]
- [[wiki/topics/sharp_wave_ripple_associated_hippocampal_replay|Sharp-wave ripple-associated hippocampal replay]]
