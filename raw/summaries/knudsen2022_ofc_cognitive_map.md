---
source_file: knudsen2022_ofc_cognitive_map.md
paper_id: knudsen2022_ofc_cognitive_map
title: "Taking stock of value in the orbitofrontal cortex"
authors:
  - "Eric B. Knudsen"
  - "Joni D. Wallis"
year: 2022
journal: "Nature Reviews Neuroscience"
paper_type: review
contribution_type: review
species:
  - human
methods:
  - optogenetics
  - lesion
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - prefrontal_cortex
  - orbitofrontal_cortex
  - ventromedial_prefrontal_cortex
  - dorsolateral_prefrontal_cortex
  - striatum
  - ventral_striatum
  - amygdala
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - successor_representation
keywords:
  - orbitofrontal_cortex_value_coding
  - cognitive_map_state_transition_graph
  - model_based_reinforcement_learning
  - successor_representation_hippocampus
  - ofchippocampal_interaction
  - reward_contingency_reversal_learning
  - theta_oscillation_reward_learning
  - hypothetical_outcome_coding
  - value_place_fields
  - prefrontal_decision_making
  - goal_directed_behaviour
  - stimulus_outcome_associations
  - taking
  - stock
  - value
  - orbitofrontal
  - cortex
---

### One-line summary

This review critically evaluates two competing accounts of orbitofrontal cortex (OFC) function — the value hypothesis and the cognitive map hypothesis — and proposes a reconciliation in which the OFC computes state values within a hippocampally-learned state-transition graph.

---

### Background & motivation

The OFC has long been understood primarily as a region that signals reward value to guide decision-making, based on neurophysiological recordings in non-human primates and decision deficits in patients with OFC lesions. However, a wave of newer studies using more complex tasks suggests the OFC may encode a much richer "cognitive map" — a structured representation of the relationships between states of the world — raising the question of whether value coding is merely a special case of a broader representational function. A related question is how OFC and hippocampus interact, given that both regions have been implicated in cognitive map-like representations. This review synthesises the evidence for both hypotheses and addresses the division of labour between these two regions.

---

### Methods

This is a narrative review covering neurophysiological, neuroimaging, lesion, and causal manipulation (optogenetics, microstimulation, TMS) studies in humans, non-human primates, and rodents. Inclusion is selective rather than systematic, focusing on studies directly bearing on OFC value coding, model-based/model-free reinforcement learning, cognitive maps, the successor representation, and OFC–hippocampal interactions. The review does not apply formal meta-analytic methods.

---

### Key findings

- OFC neurons encode abstract value across multiple decision dimensions (probability, effort, delay, magnitude, appetitive vs. aversive), and value encoding is more prevalent for the chosen option — but this may reflect a population-level vacillation (flip-flop) between option representations rather than a static preference code.
- OFC damage consistently impairs model-based (inference-based) tasks but spares model-free (cached value) tasks, implicating OFC in state-transition graph-dependent computations rather than value caching per se.
- The vmPFC/OFC uniquely encodes all task states necessary to specify a cognitive map in a human neuroimaging study (Schuck et al. 2016), and the quality of this representation predicts task performance.
- Hippocampal neurons encode "value place fields" — sparse, relational representations of reward values across pictures, analogous to spatial place fields — while OFC neurons encode value more linearly and densely, producing a complementary code.
- Closed-loop theta microstimulation applied at the peak of the hippocampal or OFC theta oscillation severely disrupts reward-based learning, establishing theta-coupled OFC–hippocampal interaction as causally necessary for learning new contingencies.
- Optogenetic inactivation of hippocampus impairs OFC representation of task block structure; hippocampal sequential replay of task states predicts improved vmPFC state representations and better performance.
- OFC neurons encode hypothetical as well as actual outcomes, consistent with using the state-transition graph to generate value predictions for unchosen options.
- A proposed division of labour: hippocampus learns and represents the state-transition graph; OFC integrates reward information to compute the value of graph nodes, enabling flexible, inference-based choice.
- The "hard" version of the cognitive map hypothesis (OFC responsible for the entire map) is not fully supported — some complex tasks do not require OFC when state values remain stable.

---

### Computational framework

The review is organized around two computational frameworks:

1. **Reinforcement learning (model-free vs. model-based)**: Model-free RL caches state values via trial-and-error and is inflexible to contingency changes. Model-based RL maintains a state-transition graph and can recompute values by inference. The OFC is linked to the model-based system: OFC damage impairs tasks that require inference over the graph but not tasks solvable by cached values.

2. **State-transition graphs and the successor representation**: Formal graph-theoretic models represent the world as a network of states (vertices) connected by transition probabilities (edges). The successor representation is an intermediate between model-free and model-based: it caches the predictive structure of state transitions (not values), enabling rapid value updating when goals change while keeping transition learning slow. The hippocampus has been proposed to encode the successor representation. The OFC's role, per the authors' synthesis, is to calculate values at graph vertices given knowledge of reward location.

Key variables: state transition probabilities, state values, reward expectations, hypothetical outcomes. Key assumption: value is inherently relational and must be computed relative to other available options within the map.

---

### Prevailing model of the system under study

Before the cognitive map challenge, the dominant view was the **value hypothesis**: the OFC is a region dedicated to computing and representing the subjective value of anticipated outcomes, translating sensory properties of rewards into a common currency ("goods space") that is independent of action. This view was grounded in Damasio's lesion observations (impaired real-world decision-making with intact other cognition), Padoa-Schioppa's single-unit recordings (OFC neurons encode economic value), and convergent neuroimaging and inactivation evidence across species. The OFC was seen as feeding value signals to downstream areas (e.g., lateral PFC) for action selection. Within this framework, OFC involvement was predicted by whether value computation was required, specifically for novel choices and for updating values when motivational state or contingencies changed.

---

### What this paper contributes

The review establishes that neither the pure value hypothesis nor the pure cognitive map hypothesis fully accounts for the data, and proposes a synthesis: the OFC is responsible for computing the **value of states within a cognitive map** whose structure is learned and maintained by the hippocampus. This reframes "value coding" as a special case of state-value computation within a graph, rather than a domain-specific function. Key advances over prior understanding:

- The vacillation dynamics of OFC population coding (flip-flopping between option representations) provide a mechanistic account of how value representations translate into choices, dissolving the puzzle of apparent "chosen value" neurons.
- The specific failure mode in OFC lesions (intact initial learning, impaired reversal/inference) is explained by the loss of state-value computation rather than vague "behavioural flexibility."
- The review identifies a double dissociation: hippocampus encodes relational/structural map information (sparse, place-field-like), OFC encodes value densely and linearly — suggesting complementary rather than redundant roles.
- Causal evidence (closed-loop theta stimulation, optogenetics, TMS) is reviewed to confirm that the OFC–hippocampal theta-coupled interaction is necessary for updating the value components of the map.
- Outstanding questions: how value is assigned to individual outcomes (a problem shared by both hypotheses); how the OFC and hippocampus negotiate updates to the map when reward expectations are violated; whether long-term graph storage transfers to lateral PFC or other cortex.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC)**: central focus; proposed to compute and represent the value of states within the cognitive map, encode hypothetical outcomes, and support model-based inference; subregions (lateral, medial, ventromedial OFC/vmPFC) are noted but distinctions between them are not deeply resolved in this review.
- **Ventromedial prefrontal cortex (vmPFC)**: closely related to OFC; the Schuck et al. neuroimaging study finds state-space coding specifically here; the authors note the anatomical proximity and potential overlap with OFC.
- **Hippocampus**: proposed to learn and represent the state-transition graph using a relational/successor-representation-like code; encodes "value place fields" (abstract relational value coding) in addition to spatial maps; theta oscillations in hippocampus drive OFC learning signals.
- **Lateral prefrontal cortex (lateral PFC / dorsolateral PFC)**: downstream of OFC for action selection; proposed to hold the state-transition graph in working memory (double dissociation with OFC in Wisconsin card sorting).
- **Entorhinal cortex**: mentioned as a candidate for encoding the state-transition graph prior to hippocampal integration with sensory input (Whittington et al. 2020).
- **Ventral striatum**: implicated alongside OFC in model-based RL.
- **Amygdala**: mentioned in connection with OFC in reinforcer devaluation and motivational control.

---

### Mechanistic insight

The paper meets the bar partially but not fully. It proposes an algorithm (OFC computes state values within a hippocampally-encoded state-transition graph, coupled via theta oscillations) and cites neural data — including direct OFC and hippocampal single-unit recordings, closed-loop theta stimulation studies, and optogenetic inactivations — that bear on this algorithm. However, because this is a review rather than a primary study, it does not itself present the neural data; it synthesises across multiple experiments with different species, tasks, and methods. The convergent evidence is strongly suggestive but the review honestly flags important unresolved issues (e.g., the precise nature of OFC–hippocampal interaction, where the graph is stored long-term).

Mapping onto Marr's three levels:

- **Computational**: the brain must compute the value of actions/options in an environment whose contingencies can change; this requires separating structural knowledge (what states exist and how they connect) from reward knowledge (what value is associated with each state), to allow rapid revaluation without relearning structure.
- **Algorithmic**: the hippocampus encodes a relational state-transition map (possibly the successor representation); the OFC uses incoming reward information to assign values to map nodes and generates hypothetical outcome predictions via map traversal; theta oscillations (likely hippocampally generated) couple the two regions during learning.
- **Implementational**: OFC neurons encode value linearly (dense code); hippocampal neurons encode relational position in state space sparsely (place-field-like); closed-loop theta stimulation at the OFC or hippocampus at the peak of the oscillation disrupts reward learning, indicating that the timing of hippocampal–OFC communication within the theta cycle is mechanistically important. The specific cell types or synaptic mechanisms are not addressed in this review.

**Bonus**: The review cites evidence that theta oscillations originate in the hippocampus and entrain the OFC, and that disrupting this entrainment causally impairs learning — a rare piece of implementational evidence for the communication mechanism.

---

### Limitations & open questions

- Most OFC neurophysiology is from non-human primates performing simple binary choice tasks; the cognitive map hypothesis needs broader causal evidence in humans (e.g., studies of OFC-lesioned patients on cognitive map tasks).
- The boundary conditions for when OFC is necessary remain unclear: some complex tasks do not require OFC even when they could in principle benefit from a cognitive map (e.g., Baxter et al. task with stable state values).
- It is unresolved whether the hippocampus is responsible for initial learning of the state-transition graph while cortex takes over for long-term storage — implications for OFC's role over extended experience are not settled.
- How the OFC and hippocampus negotiate updates when reward expectations are violated (OFC signals driving hippocampal map updates vs. hippocampal map driving OFC value updates) is bidirectional and not resolved.
- The review acknowledges that "value" and "state" representations in OFC are often confounded in tasks that simultaneously change both, making it difficult to dissociate graph-structural from reward-value coding empirically.
- Ecological validity: most OFC tasks use hundreds of repeated trials with simple stimuli, poorly approximating the one-shot, complex decisions that OFC damage most disrupts in daily life.
- The precise contribution of different OFC subregions (lateral vs. medial vs. central) to value versus map functions is not systematically addressed.

---

### Connections & keywords

**Key citations**:
- Padoa-Schioppa & Assad (2006, *Nature*) — foundational OFC value coding study
- Schuck et al. (2016, *Neuron*) — human vmPFC encodes cognitive map of state space
- Rich & Wallis (2016, *Nature Neuroscience*) — OFC population dynamics / flip-flop during decision-making
- Wilson et al. (2014, *Neuron*) — OFC as cognitive map of task space
- Behrens et al. (2018, *Neuron*) — what is a cognitive map?
- Wikenheiser & Schoenbaum (2016, *Nature Reviews Neuroscience*) — OFC–hippocampal division of labour
- Stachenfeld et al. (2017, *Nature Neuroscience*) — hippocampus as predictive map / successor representation
- Knudsen & Wallis (2020, *Neuron*) — closed-loop theta stimulation in OFC disrupts reward learning
- Knudsen & Wallis (2021, *Cell*) — hippocampal neurons map abstract value space
- Schuck & Niv (2019, *Science*) — sequential hippocampal replay of task states

**Named models or frameworks**:
- Value hypothesis of OFC function
- Cognitive map hypothesis of OFC function
- Model-free reinforcement learning
- Model-based reinforcement learning
- Successor representation
- State-transition graph
- Goods-space model (Padoa-Schioppa)
- Iowa Gambling Task (Damasio)
- Wisconsin Card Sorting Test
- Sensory preconditioning paradigm
- Closed-loop theta stimulation

**Brain regions**:
- Orbitofrontal cortex (OFC)
- Ventromedial prefrontal cortex (vmPFC)
- Hippocampus
- Lateral / dorsolateral prefrontal cortex
- Entorhinal cortex
- Ventral striatum
- Amygdala

**Keywords**:
- orbitofrontal cortex value coding
- cognitive map state-transition graph
- model-based reinforcement learning
- successor representation hippocampus
- OFC–hippocampal interaction
- reward contingency reversal learning
- theta oscillation reward learning
- hypothetical outcome coding
- value place fields
- prefrontal decision-making
- goal-directed behaviour
- stimulus-outcome associations
