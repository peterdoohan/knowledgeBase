---
source_file: badre2018_frontal_cortex_hierarchical_control.md
paper_id: badre2018_frontal_cortex_hierarchical_control
title: "Frontal Cortex and the Hierarchical Control of Behavior"
authors:
  - "David Badre"
  - "Derek Evan Nee"
year: 2018
journal: "Trends in Cognitive Sciences"
paper_type: review
contribution_type: theoretical
species:
  - human
methods:
  - fmri
  - dynamic_causal_modelling
  - lesion
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - anterior_cingulate_cortex
  - ventromedial_prefrontal_cortex
  - dorsolateral_prefrontal_cortex
  - striatum
  - thalamus
keywords:
  - hierarchical_cognitive_control
  - rostrocaudal_organisation
  - lateral_prefrontal_cortex
  - policy_abstraction
  - schematic_control
  - working_memory_gating
  - corticostriatal_circuits
  - effective_connectivity
  - theta_gamma_phase_amplitude_coupling
  - frontal_lobe_functional_organisation
  - mid_dlpfc_hierarchical_apex
  - contextual_control
  - frontal
  - cortex
  - hierarchical
  - control
  - behavior
wiki_pages:
  - wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory
---

### One-line summary

A review of the rostrocaudal organisation of lateral frontal cortex argues for three functionally discontinuous zones — sensory-motor, contextual, and schematic control — with mid-DLPFC, not RLPFC, as the apex of the frontal processing hierarchy.

---

### Background & motivation

The frontal lobes are critical for cognitive control, yet debate persists over whether they function as a unitary controller or possess meaningful functional sub-organisation. An influential class of theory proposes a rostrocaudal abstraction gradient, where progressively rostral PFC regions support increasingly abstract forms of control, culminating in a hierarchical processing architecture. A decade of neuroimaging, lesion, connectivity, and computational evidence has both supported and challenged this gradient model, necessitating an updated synthesis. This review fills the gap by re-evaluating the evidence and offering a revised framework that moves beyond a unidimensional gradient.

---

### Methods

- Narrative review of empirical fMRI, TMS, lesion, intracranial recording, effective connectivity, and structural connectivity studies of frontal lobe function during hierarchical cognitive control tasks.
- Literature covers manipulations of policy abstraction, temporal abstraction, relational integration, domain generality, working memory gating (input vs. output), and task difficulty.
- Key tasks reviewed include variants of the 12AX task, four-level hierarchical rule tasks, sequential action tasks, and relational integration paradigms.
- Anatomical connectivity evidence drawn from non-human primate tractography and resting-state fMRI parcellations.
- Corticostriatal gating models and computational architectures (hierarchical vs. unitary hub) reviewed and evaluated against the empirical record.
- Medial frontal cortex organisation reviewed in a parallel box section.

---

### Key findings

- Evidence does not support a single, unidimensional rostrocaudal abstraction gradient across the full lateral frontal cortex.
- Three functionally discontinuous zones are consistently distinguished:
  1. **Sensory-motor control zone** (motor/premotor cortex): effector-level stimulus-response control.
  2. **Contextual control zone** (mid-lateral PFC, including prePMd, prePMv, and mid-DLPFC): cognitive control based on currently or recently maintained contextual representations; contains its own local hierarchy.
  3. **Schematic control zone** (RLPFC): control based on superordinate, internally generated, schema-based knowledge — including episodic, relational-integrative, pending-goal, and explore-exploit functions.
- RLPFC is not the apex of the frontal hierarchy; anatomical connectional asymmetry meta-analysis identifies anterior mid-DLPFC (areas 45/46) as having the highest outward-to-inward connectivity ratio among lateral PFC regions.
- Dynamic causal modelling (Nee & D'Esposito 2016) confirms mid-DLPFC as the hierarchical apex: hierarchical strength (outward > inward effective connectivity) peaks at mid-DLPFC and drops back at RLPFC to a level analogous to caudal sensory-motor regions.
- RLPFC functions as a domain-specific input region to the contextual control hierarchy, transmitting schema-based knowledge (likely from vmPFC–hippocampal circuits) into the mid-DLPFC.
- Working memory gating (input and output gating via corticostriatal loops) is a core mechanism of hierarchical control, modulating rostrocaudal activation patterns over and above abstraction level per se.
- Theta-gamma phase-amplitude coupling between PFC and premotor/motor cortex increases with hierarchical control demands, with directional analysis showing PFC theta phase as a stronger predictor of downstream gamma modulation than vice versa.
- A parallel rostrocaudal gradient in medial frontal cortex tracks motivational/conflict signals (caudal SMA → preSMA → dorsal ACC), modulating the intensity of control in corresponding lateral PFC zones.
- Corticostriatal-thalamic loops, especially output gating, coordinate network interactions; multiple topographically organised frontostriatal loops may support separate levels of the hierarchy.

---

### Computational framework

The paper does not develop a new computational model but evaluates two contrasting architectural classes against the empirical record:

1. **Unitary hub controller**: a single high-dimensional context layer supports all control levels by increasing representational capacity without adding structure. Predicts no regional differentiation.
2. **Hierarchical control architecture**: separate, interacting context layers are spatially distinct, with superordinate layers providing top-down signals to subordinate ones. Predicts rostrocaudal functional differentiation and directional inter-regional influence.

Key variables: policy abstraction (depth of context-action decision tree), temporal abstraction (duration/spread of context over time), relational integration (number of feature dimensions to conjoin), working memory input gating (selective encoding), output gating (selective readout from WM).

The corticostriatal gating model (Frank, O'Reilly, Chatham and others) is described as a plausible mechanism: striatum disinhibits thalamic input to PFC to route contextual information, with nested loops supporting separate hierarchical levels. The hierarchical error representation model (Box 3) adds medial-lateral PFC layers with caudal-to-rostral feedback error signals and rostral-to-caudal top-down modulation.

The paper concludes that hierarchical architectures better account for the range of observed effects than unitary hub architectures.

---

### Prevailing model of the system under study

Before this review's contribution, the dominant theoretical framework was the **rostrocaudal abstraction gradient** hypothesis (Koechlin et al. 2003; Badre 2008; Fuster 2001; Petrides 2005). Under this model, lateral PFC is organised along a single continuous gradient from caudal motor/premotor regions (basic stimulus-response control) to rostral RLPFC (maximally abstract, temporally extended, or superordinate control). RLPFC was proposed as the apex of the frontal hierarchy — the most superordinate controller — influencing lower areas in a cascade. This view was supported by fMRI studies showing progressively rostral PFC activation as rule complexity increased, patient studies showing level-commensurate deficits after focal lesions, and structural anatomy showing increasing integrative potential toward the rostral forebrain. Competing accounts included the difficulty hypothesis (rostral PFC reflects task difficulty, not abstraction) and the adaptive maintenance/working memory account (PFC activity reflects demands on context maintenance rather than abstraction level per se).

---

### What this paper contributes

The review establishes that neither a unitary controller nor a unidimensional abstraction gradient adequately characterises lateral frontal organisation. The key conceptual shift is:

- **RLPFC is not the apex**: convergent evidence from connectional asymmetry meta-analysis and dynamic causal modelling places mid-DLPFC at the top of the processing hierarchy.
- **RLPFC is domain-specific for schema-based knowledge**: rather than being a general-purpose high-abstraction controller, RLPFC processes a specific input domain — internally generated, schema-structured representations from vmPFC–hippocampal circuits — and transmits them into the contextual control hierarchy.
- **Three discontinuous zones replace the gradient**: functional organisation is better described as three qualitatively distinct networks (sensory-motor, contextual, schematic) with both local hierarchical structure within zones and global hierarchical interactions between zones, rather than a smooth gradient.
- **Working memory gating and corticostriatal circuits are central mechanisms**: the review identifies gating as a core computational mechanism of hierarchical control, explaining much of the variability in rostrocaudal activation patterns previously attributed to abstraction level per se.
- The review also identifies that the schematic control concept (RLPFC) subsumes episodic, relational-integrative, exploratory, and pending-goal functions previously treated as distinct.

Key unresolved questions identified: how the brain solves hierarchical control problems mechanistically; the neurophysiological basis of systems-level dynamics; the contribution of thalamus and parietal cortex; how learning reshapes network relationships; and the precise mechanism of working memory gating.

---

### Brain regions & systems

- **Rostrolateral PFC (RLPFC / frontal pole, area 10)** — schematic control zone; domain-specific input region for internally generated, schema-based knowledge; involved in episodic control, relational integration, explore-exploit, pending goals, and sequential terminal position effects; receives input from vmPFC.
- **Mid-DLPFC (areas 45/46)** — apex of the frontal processing hierarchy; contextual control zone; domain-general orchestration of lower-order frontal regions; apical hierarchical strength by connectional asymmetry and effective connectivity metrics.
- **Dorsal anterior premotor (prePMd) and ventral anterior premotor (prePMv)** — contextual control zone; subordinate to mid-DLPFC; involved in output gating of lower-order context representations; domain-specific subregions (spatial vs. verbal).
- **Motor cortex and supplementary motor area (SMA)** — sensory-motor control zone; effector-level stimulus-response.
- **Premotor cortex (prePM)** — sensory-motor/contextual boundary; output gating of lower-order contexts; hub-like convergence of mid-DLPFC and sensory-motor inputs.
- **Ventromedial PFC (vmPFC)** — schema storage and retrieval; interacts with hippocampus; provides schematic input to RLPFC.
- **Hippocampus** — schema retrieval and episodic future planning; hippocampal goal representations correlate with RLPFC activation.
- **Caudate nucleus / striatum** — corticostriatal output gating; topographically organised frontostriatal loops regulate working memory updating at each hierarchical level; reward prediction errors for hierarchical rule learning.
- **Thalamus** — intermediary in corticostriatal-thalamic gating circuits; disinhibition mechanism for PFC working memory gating.
- **Dorsal anterior cingulate cortex (dACC) and preSMA / dorsomedial PFC** — parallel medial frontal hierarchy; motivational and conflict signals modulating lateral PFC control intensity; dACC tracks tonic/episodic incentives, preSMA tracks immediate/contextual incentives.
- **Frontal eye fields (FEF) and inferior frontal junction (IFJ)** — domain-specific sensory-motor zone subregions for spatial and verbal/object information respectively.

---

### Mechanistic insight

The paper does not itself present new primary data; it reviews existing work. It does not fully meet the mechanistic bar as set by the SKILL criteria (original algorithm formalised + neural data specifically supporting that algorithm over alternatives in a single paper). However, the review comes close in two respects:

1. The intracranial recording study (Voytek et al. 2015, ref [77]) provides neural dynamics evidence: theta-gamma phase-amplitude coupling within PFC and between PFC and premotor/motor cortex increases with hierarchical control demands, and directional analysis shows PFC theta phase preferentially predicts downstream gamma modulation — consistent with a top-down cascade. This links a specific processing architecture (hierarchical top-down flow) to a measurable neural signature, but the precise algorithm is not formalised in this paper.

2. The dynamic causal modelling study (Nee & D'Esposito 2016, ref [34]) provides effective connectivity evidence placing mid-DLPFC at the hierarchical apex — constituting algorithmic-level evidence about information flow — but the computational formalism is imported from existing models.

The review thus situates mechanistic evidence at Marr's computational level (hierarchical control to manage multilevel contextual contingency and support generalisation) and partially at the algorithmic level (top-down cascading context signals, gating of working memory), but does not provide new implementational-level mechanistic detail (specific cell types, neuromodulators, biophysical mechanisms are not addressed).

---

### Limitations & open questions

- No primary data are collected; all conclusions depend on the consistency of prior literature, which varies in task design, analysis method, and anatomical localisation precision.
- The three-zone framework is heuristic; boundaries between zones are not precisely demarcated and may shift with task demands.
- Working memory gating has been proposed as a central mechanism, but its neural implementation — whether corticocortical, corticostriatal-thalamic, or both — remains unresolved.
- It is unclear how learning and experience reshape the hierarchical network relationships reviewed here.
- The contribution of non-frontal structures (thalamus, parietal cortex, cerebellum) to hierarchical control is underspecified.
- The relationship between local frontal hierarchy and global brain network dynamics (graph theoretic hubs, control theory) requires further investigation.
- More mechanistic computational theory is needed that directly addresses hierarchical control problems at the algorithmic and implementational levels, beyond architecture-level descriptions.
- The RLPFC's role in schematic control is proposed partly by analogy and connectivity; direct causal evidence linking RLPFC specifically to schema retrieval or transmission is limited.

---

### Connections & keywords

**Key citations:**
- Koechlin et al. (2003) Science — original cascade/architecture model of PFC
- Badre & D'Esposito (2007) J Cogn Neurosci — fMRI evidence for rostrocaudal abstraction gradient
- Nee & D'Esposito (2016) eLife — dynamic causal modelling placing mid-DLPFC as hierarchical apex
- Nee & Brown (2013) Cereb Cortex — frontostriatal and frontoparietal networks in hierarchical WM gating
- Chatham et al. (2014) Neuron — corticostriatal output gating
- Voytek et al. (2015) Nat Neurosci — theta-gamma coupling in frontal hierarchical control
- Desrochers et al. (2015) Neuron — necessity of RLPFC for higher-level sequential behavior (TMS)
- Collins & Frank (2013) Psychol Rev — hierarchical task-set learning
- Reynolds et al. (2012) PLoS ONE — test of adaptive maintenance vs. abstraction hypotheses
- Badre et al. (2009) Nat Neurosci — hierarchical control deficits after frontal lesions

**Named models or frameworks:**
- Rostrocaudal abstraction gradient hypothesis
- Cascade model (Koechlin et al. 2003)
- Unitary hub controller architecture
- Hierarchical control architecture
- Corticostriatal gating model (Frank, O'Reilly; Chatham et al.)
- Hierarchical error representation model (Box 3)
- Guided activation model (Stroop; Cohen et al.)
- 12AX task paradigm
- Schematic control framework (proposed here)

**Brain regions:**
- Rostrolateral PFC (RLPFC, frontal pole, area 10)
- Mid-DLPFC (areas 45/46)
- Dorsal anterior premotor cortex (prePMd)
- Ventral anterior premotor cortex (prePMv)
- Motor cortex / SMA
- Ventromedial PFC (vmPFC)
- Hippocampus
- Caudate nucleus / striatum
- Thalamus
- Dorsal anterior cingulate cortex (dACC)
- Premotor / supplementary motor area (preSMA)
- Frontal eye fields (FEF)
- Inferior frontal junction (IFJ)

**Keywords:**
- hierarchical cognitive control
- rostrocaudal organisation
- lateral prefrontal cortex
- policy abstraction
- schematic control
- working memory gating
- corticostriatal circuits
- effective connectivity
- theta-gamma phase-amplitude coupling
- frontal lobe functional organisation
- mid-DLPFC hierarchical apex
- contextual control

### Related wiki pages
- [[wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory|Medial prefrontal cortex in goal-directed spatial navigation and spatial working memory]]
