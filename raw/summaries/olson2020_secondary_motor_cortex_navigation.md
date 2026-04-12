---
source_file: "olson2020_secondary_motor_cortex_navigation.md"
paper_id: "olson2020_secondary_motor_cortex_navigation"
title: "Secondary Motor Cortex Transforms Spatial Information into Planned Action during Navigation"
authors: "Jacob M. Olson, Jamie K. Li, Sarah E. Montgomery, Douglas A. Nitz"
year: 2020
journal: "Current Biology"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
tasks: ["t_maze", "navigation_task"]
methods: ["electrophysiology", "lesion"]
brain_regions: ["hippocampus", "retrosplenial_cortex"]
keywords: ["okeefe_and_dostrovsky_1971_place_cells", "nitz_2006", "2009_ppc_encoding_of_routes_and_spatial_context", "whitlock_et_al_various_ppc_spatial_and_action_encoding", "powell_and_redish_m2_choice_prediction_at_single_location", "alexander_and_nitz_rsc_ppc_spatial_representations", "various_m2_lesion_electrophysiology_studies_erlich", "sul", "murakami_cited_implicitly_via_4148", "named_models_or_frameworks", "choice_probability_cp_area_under_roc_used_as_the_primary_quantitative_framework_for_assessing_neural_discrimination", "generalized_linear_models_supplementary_analysis_of_contextual_variable_contributions", "triple_t_maze_multi_route_navigation_task_paradigm", "brain_regions", "secondary_motor_cortex_m2_medial_agranular_cortex", "posterior_parietal_cortex_ppc", "retrosplenial_cortex_rsc", "primary_motor_cortex_m1", "hippocampus", "entorhinal_cortex"]
---

### One-line summary

Secondary motor cortex (M2) neurons in rats encode both planned and currently-executed left/right turning actions across multiple spatial contexts during navigation, with action identity being the dominant signal over spatial and directional contextual variables.

---

### Background & motivation

Navigation requires integrating complex spatial information about the environment and converting it into specific action plans, often in real time and across changing contexts. While spatial representations in hippocampus, retrosplenial cortex (RSC), and posterior parietal cortex (PPC) are well-documented, how these representations are transformed into motor output is poorly understood. The M2 is a prime candidate for this transformation because of its dense reciprocal connectivity with PPC and RSC (which encode spatial relationships) and its strong projections to primary motor cortex and brainstem motor regions. Prior work had shown M2 predicts upcoming choices at a single location, but whether M2 encodes actions across multiple spatial contexts during naturalistic navigation had not been established.

---

### Methods

- **Subjects**: 7 adult male rats
- **Task**: Triple-T maze with 8 three-turn internal routes sharing a single start location and leading to 8 different goal locations; three reward schedules were used (high-low, visit-all-8, visit-all-4)
- **Neural recordings**: Single-unit electrophysiology from 303 M2 neurons (73 left hemisphere, 230 right hemisphere) across recording sessions; all cleanly isolated units included regardless of firing rate
- **Analysis approach**:
  - Turn spaces defined as 20 cm before to 10 cm after turn apex
  - Choice Probability (CP; equivalent to area under ROC curve) used as a sample-size-invariant measure of discrimination quality between left and right turns
  - Contextual variables (environmental location, route progress, heading direction, route identity, choice vs. forced context) tested by comparing firing rates for like actions across different contexts
  - Generalized linear models used as a complementary approach to assess variable contributions
  - Spatial and temporal dynamics of action encoding analyzed using discrete bins surrounding a single reference turn

---

### Key findings

- 67% (203/303) of M2 neurons significantly discriminated left vs. right turn direction when pooling across all turn locations; 57% discriminated at a single turn location
- Over 50% of neurons had choice probability (CP) exceeding 66% at any given turn; 14% exceeded 90% — far above chance (no shuffled neuron reached 66%)
- Action discrimination strength was consistent across all seven turn locations (Kruskal-Wallis p = 0.115) and across three reward schedule paradigms (p = 0.079)
- Action discrimination was present from the beginning of the approach to a turn and peaked at the turn apex; minimum 15% of neurons were significantly discriminating at every point in the sequence
- Individual neurons' peak discrimination spans were typically under 20 cm, suggesting an evolving ensemble encodes the full action sequence from planning to execution
- All four tested spatial contextual variables (location, route, heading direction, route progress) were significantly encoded above chance, but with CPs substantially lower than action discrimination (contextual CP distributions significantly below action CP, one-sided KS test p < 0.0001 for all)
- Nearly no neurons reached the 90% CP threshold for any contextual variable, compared to 14% for action
- Choice context (forced vs. choice turn) was represented at a level comparable to spatial contextual variables, but did not affect the strength of action discrimination itself — casting doubt on a primary decision-making role for M2
- Neurons encoding action and spatial context were positively correlated (r < 0.5), indicating that action-discriminating neurons also tend to encode spatial context

---

### Computational framework

Not a formal computational paper; no explicit mathematical model is derived. However, the paper implicitly frames M2 function within a **sensorimotor integration / action planning** framework. The key conceptual logic is:

- **What is being modelled (implicitly)**: The transformation of allocentric spatial signals (from PPC and RSC) into action-specific motor commands, analogous to a context-to-action mapping function
- **Key variables**: Turn identity (left/right), environmental location, route, heading direction, route progress, choice availability
- **Core assumption**: A reliable, context-independent action code in M2 is necessary for downstream motor regions to decode action without needing to simultaneously decode spatial context; M2's role is the transformation stage between spatial cognition and motor output

The use of choice probability as a single-trial linear decoding metric provides a computational operationalisation of "decodability" by a downstream reader neuron. The results constrain models of how prefrontal/premotor cortex links spatial representations to action.

---

### Prevailing model of the system under study

Prior to this paper, the M2 (also called medial agranular cortex, premotor cortex, Fr2) had been studied primarily in two-alternative forced-choice paradigms with single sensory cues, and was known to encode action planning and rules during delay periods preceding single decision points. Some prior work had shown M2 neurons predict upcoming navigational choices at a single environmental location. The broader field treated RSC and PPC as the key intermediaries encoding space in multiple reference frames, with M2 as the downstream recipient that converts these signals into motor output — but the scope of this transformation had not been mapped across a multi-route, multi-location navigation task. The prevailing assumption was that M2 firing might reflect a deliberative decision-making process, with discriminatory activity primarily ramping synchronously before a choice point. The paper's introduction also positions M2 as possibly involved in rule encoding and effort/reward anticipation based on neighboring prefrontal sub-region work.

---

### What this paper contributes

The results establish that M2 action encoding is far broader and more spatially robust than previously known:

1. Action identity (left vs. right turn) is encoded by M2 ensembles consistently across all turn locations in a complex multi-route environment — demonstrating context-generalisable action representations, not just single-location predictive activity.
2. The temporal dynamics of action encoding — with individual neurons exhibiting peak discrimination at varied points throughout the approach and execution, rather than synchronous ramping — are more consistent with a continuous planning-to-execution transition process than a deliberative decision-making account.
3. Action discrimination is equally strong at forced-turn sites (where no choice exists) as at choice sites, arguing against a primary decision-making interpretation.
4. Spatial and directional contextual information is present in M2 but is clearly subordinate to action identity, consistent with a model in which spatial signals from PPC and RSC are transformed into action commands in M2.
5. The paper provides the first characterisation of M2 as encoding the full sequence of planned and executed actions during continuous, multi-turn navigation — not just discrete choice-point epochs.

---

### Brain regions & systems

- **Secondary motor cortex (M2) / medial agranular cortex** — primary focus; proposed locus of spatial-to-action transformation during navigation; encodes action identity, spatial context, and choice availability
- **Posterior parietal cortex (PPC)** — major afferent to M2; discussed as encoding spatial position within routes, turn-type, and multiple egocentric/allocentric reference frames; proposed source of contextual spatial input to M2
- **Retrosplenial cortex (RSC)** — major afferent to M2; encodes spatial position and heading direction; discussed as complementary source of allocentric and route-level spatial signals to M2
- **Primary motor cortex (M1)** — major efferent target of M2; discussed as downstream recipient of M2's action output signals
- **Hippocampus, subiculum, perirhinal, postrhinal, entorhinal cortices** — discussed in introduction as part of the broader network providing spatial representations upstream of RSC and PPC

---

### Mechanistic insight

The paper meets both criteria:

1. **Algorithm**: M2 is proposed to implement a spatial-to-action transformation — receiving contextually rich spatial signals from PPC and RSC, and outputting context-generalised action identity signals usable by downstream motor regions. The evolving ensemble dynamics (each neuron discriminating at a narrow spatial window, with peak CP locations spread across the approach) suggest this is implemented by a sequential population code that transitions from action planning to execution continuously.

2. **Neural data**: Single-unit recordings from M2 during naturalistic multi-route navigation directly support the algorithm by showing (a) reliable, context-independent left/right action discrimination across all turn locations and paradigms, (b) persistence of discrimination at forced-turn sites, and (c) the distributed temporal dynamics of peak discrimination across the population.

**Mapped to Marr's levels:**

- **Computational**: The problem being solved is converting a spatial representation of the environment and route into a sequence of specific motor actions (left/right turns) that define a navigation trajectory. The brain must produce reliable, context-generalizable action signals that can be read by motor effectors regardless of the specific spatial location of any given turn.

- **Algorithmic**: M2 represents action identity (left/right) as the dominant signal across an ensemble of neurons, each with a limited spatial window of peak discriminability. The population as a whole provides continuous coverage from early planning through execution. Contextual spatial information (location, route, direction, progress) modulates the magnitude of action-specific firing but does not override action identity. The result is a code from which action can be reliably decoded without decoding spatial context.

- **Implementational**: Single units recorded in rat M2 (medial agranular cortex, layer unspecified) exhibit the described properties. The paper notes M2 receives inputs from PPC and RSC and projects to M1 and brainstem/spinal motor regions. Recent work cited suggests interactions with ventromedial thalamus and cerebellum may also be relevant. Projection specificity of context-independent action neurons to brainstem targets is flagged as a key open question. No specific cell types or neuromodulatory mechanisms are addressed.

---

### Limitations & open questions

- Recording was restricted to one hemisphere predominantly (230/303 neurons from right hemisphere); laterality effects on action tuning were not fully explored
- The correlation between action tuning and context tuning (r < 0.5) leaves open how downstream structures read out a pure action signal; the paper does not resolve whether this occurs via projection specificity or population-level decoding
- Route progress and heading direction were highly correlated in the maze design, making it difficult to fully dissociate their contributions to M2 firing
- Whether M2 activity is necessary (not just correlated) for the observed navigation behavior was not tested; no lesion or inactivation experiments were reported in this study
- The paper does not address layer-specific or cell-type-specific properties of M2 action encoding
- Projection specificity of context-independent action neurons (e.g., to brainstem vs. intracortical targets) is identified as a priority for future work
- Whether similar dynamics hold in environments without well-defined routes or in tasks requiring more flexible navigation is unaddressed

---

### Connections & keywords

**Key citations:**
- O'Keefe & Dostrovsky (1971) — place cells
- Nitz (2006, 2009) — PPC encoding of routes and spatial context
- Whitlock et al. (various) — PPC spatial and action encoding
- Powell & Redish — M2 choice prediction at single location
- Alexander & Nitz — RSC/PPC spatial representations
- Various M2 lesion/electrophysiology studies (Erlich, Sul, Murakami cited implicitly via [41–48])

**Named models or frameworks:**
- Choice Probability (CP) / area under ROC — used as the primary quantitative framework for assessing neural discrimination
- Generalized linear models — supplementary analysis of contextual variable contributions
- Triple-T maze — multi-route navigation task paradigm

**Brain regions:**
- Secondary motor cortex (M2) / medial agranular cortex
- Posterior parietal cortex (PPC)
- Retrosplenial cortex (RSC)
- Primary motor cortex (M1)
- Hippocampus
- Entorhinal cortex

**Keywords:**
- secondary motor cortex, action planning, action execution, navigation, spatial context, multi-route maze, choice probability, sensorimotor integration, premotor cortex, turn direction encoding, context-independent action code, evolving ensemble
