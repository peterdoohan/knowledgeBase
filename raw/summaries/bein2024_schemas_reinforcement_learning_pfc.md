---
source_file: bein2024_schemas_reinforcement_learning_pfc.md
paper_id: bein2024_schemas_reinforcement_learning_pfc
title: "Schemas, reinforcement learning, and the medial prefrontal cortex"
authors:
  - "Oded Bein"
  - "Yael Niv"
year: 2024
journal: "Not specified in source (opinion paper)"
paper_type: review
contribution_type: theoretical
species:
  - human
methods:
  - electrophysiology
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca3
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - orbitofrontal_cortex
  - ventromedial_prefrontal_cortex
  - retrosplenial_cortex
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - bayesian_inference
  - hierarchical_rl
keywords:
  - schema_learning
  - reinforcement_learning
  - medial_prefrontal_cortex
  - dimensionality_reduction
  - prediction_error
  - hierarchical_reinforcement_learning
  - latent_cause_inference
  - orbito_medial_prefrontal_cortex
  - cognitive_map
  - memory_consolidation
  - event_segmentation
  - representation_learning
  - schemas
  - reinforcement
  - learning
  - medial
  - prefrontal
  - cortex
key_citations:
  - niv2019_representation_learning_task_states
  - wilson2014_best_practices_scientific
  - schuck2016_orbitofrontal_cortex_state
---

### One-line summary

This opinion paper proposes that reinforcement learning — specifically prediction-error-driven learning, hierarchical RL, and dimensionality reduction — provides a computational account of how schemas are acquired, and that the medial prefrontal cortex (mPFC) subserves both RL and schemas through dimensionality reduction and guided memory reactivation, with gradients of abstraction along the ventral-dorsal and posterior-anterior mPFC axes.

---

### Background & motivation

Schemas (rich associative knowledge structures about the typical unfolding of events) are central to psychology and neuroscience but lack a satisfying computational account. Reinforcement learning (RL) offers a rigorous framework for learning environmental structure and goal-oriented behaviour, but RL algorithms scale poorly to the high-dimensional complexity of real-world events — the "curse of dimensionality." The authors identify a shared neural substrate: the orbito-medial PFC (mOFC/vmPFC and mid-mPFC) is implicated in both RL state representations and schema-related memory processes, motivating a synthesis of the two fields. The paper asks whether RL mechanisms can bridge the computational gap and explain how schemas are learned, structured, and deployed.

---

### Methods

This is a narrative review and theoretical opinion piece.

- Scope: Selective synthesis of animal and human behavioural, computational, neuroimaging, lesion, and electrophysiology studies bearing on schemas and RL.
- No inclusion/exclusion criteria stated; coverage is representative rather than exhaustive.
- Synthesis method: The authors identify three RL computational principles (prediction errors, hierarchical RL, dimensionality reduction) and map each to schema phenomena, then propose a unified account of mPFC function integrating both literatures.
- Two additional boxes address: (1) rapid hippocampal learning and schema formation; (2) the relationship between schemas and cognitive maps.

---

### Key findings

This is a theoretical paper; findings are proposed claims supported by cited evidence rather than original data.

- **Prediction errors drive schema learning**: Studies in rodents and humans show that state prediction errors (violations of learned transition probabilities) enhance memory for the violating content and support updating of world models, consistent with schema learning via RL-style prediction error signals.
- **Hierarchical RL accounts for schema hierarchy**: Temporal abstraction in hierarchical RL — grouping states and actions into subtasks defined by subgoals — maps onto how sub-schemas are chunked within larger schemas. Latent-cause inference (Bayesian grouping of observations by inferred common source) provides a mechanism for instantiating relevant schemas or initiating new ones at event boundaries.
- **Dimensionality reduction underlies schema abstraction**: RL representation learning (attending to goal-relevant dimensions, filtering episodic detail) corresponds to schema formation. fMRI evidence shows mOFC/vmPFC encodes low-dimensional, abstract task representations, with fewer PCA components needed for simpler categorization rules (Mack et al., 2020) and similar neural patterns for items sharing a contextual feature but not their episodic details (Tompary & Davachi, 2017).
- **mPFC represents both RL states and schemas**: Multivoxel patterns in mOFC/vmPFC decode latent task states and are sensitive to Bayesian state inference. Mid-mPFC representations generalize across schema instances (different restaurant visits) and preserve sequential order while abstracting over perceptual modality.
- **mPFC guides memory reactivation in posterior regions**: mPFC activity precedes and predicts hippocampal and ventral-temporal activity during retrieval. Lesions to mOFC/vmPFC impair hippocampal representations, face familiarity signals in posterior regions, and the evaluation of retrieved memories. Schema consistency modulates mPFC functional connectivity toward posterior cortex (consistent) vs. hippocampus (inconsistent).
- **Gradient hypothesis**: More abstract/future-oriented representations are found in anterior and dorsal mPFC; more specific and detailed representations engage posterior and ventral mPFC (connected to hippocampus). This gradient is proposed to reflect the degree of dimensionality reduction required.

---

### Computational framework

**Reinforcement learning**, specifically the intersection of model-based RL, hierarchical RL, and representation learning (dimensionality reduction).

Core formalism:
- Tasks are partitioned into discrete **states** (Markovian contexts encoding information sufficient to guide behaviour). An agent learns transition probabilities between states and reward distributions (the "world model") via model-based RL.
- **Prediction errors** (reward prediction errors and state prediction errors) signal discrepancies between expected and observed outcomes, driving updates to the world model. Formally: δ = r + γV(s') − V(s) for reward PE; analogous signals exist for state transitions.
- **Hierarchical RL** introduces temporal abstraction: subtasks are defined by start states, policies ("options"), transition probabilities, and termination states ("subgoals"). Reaching a subgoal yields a pseudo-reward, allowing standard RL to solve subtasks. This allows reuse of sub-schemas across larger schemas.
- **Latent-cause inference**: Bayesian inference groups current observations under a latent cause (a prior schema or new one), with a new cause created when observations diverge sufficiently from existing models.
- **Representation learning / dimensionality reduction**: The agent learns which environmental dimensions are reward-predictive (goal-relevant) and attends to these, reducing the effective state-space dimensionality. Goal-irrelevant but statistically reliable dimensions may also be retained for flexible behaviour.

Key assumption: schemas are the mPFC's representation of the world model and policy in model-based RL, structured hierarchically and pruned to a low-dimensional summary of repeated experience.

---

### Prevailing model of the system under study

The introduction signals two coexisting literatures that the paper bridges:

1. **Schema research**: Schemas have been characterised as associative, hierarchically organised knowledge structures (Bartlett, 1932; Schank & Abelson, 1977) that influence perception, attention, learning, and memory. The neural literature implicated mPFC in schema-based processing (e.g., van Kesteren et al., 2012; Gilboa & Marlatte, 2017), but no agreed computational account of schema *acquisition* existed. Computational models of semantic networks and category learning captured some aspects but did not address goal-directed, temporally structured learning.

2. **RL and mPFC**: Within RL, the mOFC/vmPFC is widely held to represent a "cognitive map" of task states — a structured representation of the current context used to guide decisions (Wilson et al., 2014; Schuck et al., 2016). A competing view holds that mOFC/vmPFC primarily encodes economic value (Levy & Glimcher, 2012; Padoa-Schioppa & Conen, 2017). RL algorithms, while powerful in simple environments, were acknowledged to fail at the complexity of naturalistic cognition.

The working assumption the authors push against is that schemas and RL are *disparate* frameworks operating at different levels of ecological complexity, and that the mPFC's roles in RL and schema memory are coincidental rather than mechanistically unified.

---

### What this paper contributes

The paper's main theoretical contribution is a unified framework proposing that:

1. **RL mechanisms are sufficient to account for schema learning**: prediction errors, hierarchical organisation via subgoals, and dimensionality reduction map onto core properties of schemas. This fills the acknowledged gap of a computational account for how schemas are learned through experience.

2. **The mPFC's dual roles (RL states + schema memory) are not coincidental**: both reflect a single function — dimensionality reduction and the storage of abstract, low-dimensional world models. The mPFC encodes simplified representations of environmental structure that guide memory reactivation in posterior cortex, serving both RL planning and schema-guided memory retrieval.

3. **The gradient hypothesis is novel**: the proposal that the degree of dimensionality reduction (specific to abstract) maps onto posterior-to-anterior and ventral-to-dorsal axes of the mPFC is a testable prediction not previously formalised. It synthesises disparate findings about where in the mPFC different types of information are encoded.

What can now be said that could only be speculated before: schemas and RL state representations may be computationally equivalent structures implemented in overlapping mPFC circuits, with the extent of abstraction — not the type of knowledge — determining the specific mPFC subregion engaged.

---

### Brain regions & systems

- **Medial orbitofrontal cortex / ventromedial PFC (mOFC/vmPFC)** — proposed to represent latent task states (requiring memory retrieval) and specific/moderately abstract schemas; connected to hippocampus and ventral temporal cortex; involved in Bayesian state inference, economic value, and schema instantiation.
- **Mid-mPFC** (dorsal to mOFC/vmPFC on the medial wall) — proposed to represent more abstract schematic knowledge; sensitive to transition probabilities between states and inter-event structure; functionally connected to posterior medial cortex (precuneus, parahippocampal cortex, angular gyrus, anterolateral temporal lobe).
- **Anterior mPFC / frontopolar cortex** — proposed to represent highly abstract, future, or counterfactual states; evidence from prospective planning studies shows predictions about the far future are represented more anteriorly.
- **Hippocampus** — critical for rapid learning and event segmentation during initial schema formation; represents detailed, episodic state information via pattern separation (CA3/dentate gyrus); interacts with posterior mOFC/vmPFC for detailed state retrieval.
- **Posterior medial cortex** (including precuneus, retrosplenial cortex) — represents events over large timescales, abstracting episodic details; functionally connected to mid-mPFC; proposed recipient of schema-guided reactivation signals.
- **Ventral temporal cortex** — represents object identity and perceptual features; receives top-down guidance from mOFC/vmPFC during object recognition.

---

### Mechanistic insight

This paper does not meet the bar for mechanistic insight as defined. It is a theoretical review that proposes an RL-based computational account of schema learning and mPFC function. It synthesises existing fMRI, lesion, and electrophysiology evidence, but does not itself present a formalised algorithm and match it against neural data that specifically distinguish it from alternatives.

More specifically: the paper proposes that dimensionality reduction in mPFC implements both RL state representations and schemas, and that mPFC activity guides memory reactivation in posterior regions. The cited neural evidence (e.g., Schuck et al., 2016; Mack et al., 2020; Tompary & Davachi, 2017; Baldassano et al., 2018) is consistent with these claims, but none of the cited studies was designed to adjudicate between the RL-schema framework and alternative accounts (e.g., pure value coding, match-mismatch signalling). The implementational level (specific cell types, neuromodulators, circuit mechanisms) is not addressed.

---

### Limitations & open questions

- Most supporting evidence comes from simplified lab tasks (few associations, short timescales); it is unclear whether the findings generalise to acquiring and updating complex, well-learned schemas in naturalistic settings.
- The role of prediction errors in *updating* already-consolidated schemas (as opposed to initial acquisition) has not been directly tested.
- The gradient hypothesis (posterior-to-anterior = specific-to-abstract) is speculative and derived from heterogeneous studies with different stimuli and paradigms; direct within-subject comparisons along the mPFC axis are lacking.
- The paper does not specify how latent-cause inference interacts with hierarchical RL computationally — the integration is proposed but not formalised.
- Whether schemas are stored primarily in mPFC or whether mPFC merely indexes/coordinates representations stored elsewhere remains unresolved.
- The distinction between schemas and cognitive maps (addressed in Box 2) highlights that hierarchical, asymmetric relational information may not be captured by distance-based cognitive map formalisms, but no alternative formalism is offered.
- The frequency-based (unsupervised) learning account of schema formation is not fully ruled out; the prediction-error account and frequency account may both contribute.
- How dimensionality reduction scales to the richness and flexibility of human schemas (including cultural, narrative, and social dimensions) is unaddressed.

---

### Connections & keywords

**Key citations:**
- Sutton & Barto (2018) — RL textbook foundational reference
- Dayan & Niv (2008) — RL and the brain
- Niv (2019) — representation learning and dimensionality reduction in RL
- Gilboa & Marlatte (2017) — schemas and mPFC review
- Wilson et al. (2014) — mOFC as cognitive map of task states
- Schuck et al. (2016) — mOFC/vmPFC encodes latent states requiring memory
- Baldassano et al. (2018) — mPFC represents real-world event schemas
- Mack et al. (2020) — dimensionality reduction in vmPFC during categorisation
- Tompary & Davachi (2017) — schema-like integration and mPFC after consolidation
- van Kesteren et al. (2012) — mPFC routes memory encoding based on schema consistency
- Botvinick, Niv & Barto (2009) — hierarchical RL and its neural foundations
- Gershman & Niv (2010); Franklin et al. (2020) — latent cause inference
- Reagh & Ranganath (2023) — mPFC encodes schematic, not episodic, movie representations
- Leong et al. (2017) — mPFC activity tracks dimensionality-reduced RL value

**Named models or frameworks:**
- Reinforcement learning (model-based and model-free RL)
- Hierarchical reinforcement learning (options framework, temporal abstraction)
- Latent-cause inference (Bayesian clustering of observations)
- Representation learning / dimensionality reduction
- Cognitive map (Tolman; Behrens et al., 2018)
- Event Segmentation Theory (Zacks, 2020)
- Complementary Learning Systems (McClelland et al., 1995)
- Schemas / event schemas / scripts (Bartlett; Schank & Abelson)

**Brain regions:**
- Medial orbitofrontal cortex (mOFC)
- Ventromedial prefrontal cortex (vmPFC)
- Mid-medial prefrontal cortex (mid-mPFC)
- Anterior / frontopolar PFC
- Hippocampus (CA1, CA3, dentate gyrus)
- Posterior medial cortex (precuneus, retrosplenial cortex)
- Ventral temporal cortex
- Parahippocampal cortex
- Entorhinal cortex

**Keywords:**
- schema learning
- reinforcement learning
- medial prefrontal cortex
- dimensionality reduction
- prediction error
- hierarchical reinforcement learning
- latent cause inference
- orbito-medial prefrontal cortex
- cognitive map
- memory consolidation
- event segmentation
- representation learning
