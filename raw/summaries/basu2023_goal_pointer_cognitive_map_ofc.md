---
source_file: "basu2023_goal_pointer_cognitive_map_ofc.md"
paper_id: "basu2023_goal_pointer_cognitive_map_ofc"
title: "A goal pointer for a cognitive map in the orbitofrontal cortex"
authors: "Raunak Basu, Hiroshi T. Ito"
year: 2023
journal: "Current Opinion in Neurobiology"
paper_type: "review"
contribution_type: "review"
species: ["human"]
tasks: ["navigation_task"]
methods: ["optogenetics", "electrophysiology", "fmri", "lesion"]
brain_regions: ["hippocampus", "hippocampus_ca1", "entorhinal_cortex", "medial_entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "orbitofrontal_cortex", "ventromedial_prefrontal_cortex", "ventral_tegmental_area", "substantia_nigra", "retrosplenial_cortex", "amygdala"]
frameworks: ["reinforcement_learning", "model_free_rl", "successor_representation"]
keywords: ["goal", "pointer", "cognitive", "map", "orbitofrontal", "cortex"]
key_citations: ["basu2021_ofc_navigation_goals", "russek2017_model_based_reinforcement", "campagner2023_cortico_collicular_shelter", "wilson2014_best_practices_scientific", "zhou2021_schema_orbitofrontal", "bohm2020_pfc_spatial_working_memory"]
---

### One-line summary

The orbitofrontal cortex (OFC) maintains a persistent, spatially specific representation of a future navigational goal throughout a journey, functioning as a dedicated "goal pointer" that is distinct from the hippocampal system tracking current position.

---

### Background & motivation

Goal-directed navigation requires the brain to simultaneously track one's current location and maintain a representation of a remote destination that lies outside immediate sensory perception. While spatially tuned neurons in the hippocampus and parahippocampal cortices reliably encode an animal's instantaneous position, it has remained unclear how the brain represents a future goal location persistently and independently of the continuously changing sensory inputs associated with intermediate positions. This review addresses whether the brain possesses a second, separate spatial representation system dedicated to encoding navigational goals, and proposes the OFC as the anatomical locus of this system.

---

### Methods

This is a narrative review covering empirical and theoretical literature on goal-directed navigation. The scope includes:

- Rodent electrophysiology and optogenetics studies examining place cells, grid cells, and OFC neurons during spatial navigation tasks
- Human fMRI studies of prospective goal coding
- Theoretical and computational models linking successor representations, value functions, and spatial navigation
- Clinical neuropsychological observations (vmPFC/OFC lesion patients)
- Studies on wider brain circuits including mPFC, retrosplenial cortex (RSC), and superior colliculus (SC)

The synthesis is narrative, organised around an algorithmic framing: what computational problems must a goal representation system solve?

---

### Key findings

- Hippocampal place cells over-represent reward locations and generate brief forward trajectory sequences, but these goal-related signals occur close to or at the goal location, not persistently from journey onset — making them insufficient alone for prospective goal coding.
- OFC neurons (Basu et al., 2021, Nature) fire with goal-location specificity prior to navigation onset and maintain this pattern throughout the journey, invariant to intermediate locations traversed — constituting a persistent spatial goal map.
- Optogenetic perturbation of OFC activity specifically at navigation onset caused animals to navigate to incorrect destinations, establishing a causal role for OFC in goal selection.
- Population-level OFC dynamics unfold as destination-specific neural trajectories that originate at motion onset and evolve deterministically until the goal is reached.
- Goal-specific prospective OFC activity has been replicated in human fMRI during virtual navigation.
- mPFC does not exhibit prospective or persistent goal coding (Bohm & Lee, 2020), suggesting OFC is the primary locus.
- An RSC-to-superior colliculus circuit encodes shelter direction for escape behavior, indicating that distinct circuits may serve different navigational demands (e.g., escape vs. reward-seeking).
- Ventral hippocampal inputs are necessary for the OFC's representation of target direction during decision-making, suggesting hippocampus-to-OFC communication supports spatial map formation in OFC.

---

### Computational framework

The review explicitly frames the problem using reinforcement learning and successor representation theory. Key elements:

- **Successor representation (SR)**: encodes the expected future occupancy of states, with columns resembling place cell firing fields. The SR separates state-transition structure from reward.
- **Reward vector / value function**: navigation can be implemented by gradient ascent along a value function computed by multiplying the SR matrix by a reward vector (probabilities of reward at individual states). Changing the goal requires only updating the reward vector, leaving the SR intact.
- **Goal pointer as reward vector**: the review proposes that the OFC provides the persistent reward-state representation (analogous to a reward vector) that can be applied to the hippocampal SR to compute goal-directed value gradients.
- **Neural trajectory dynamics**: population-level OFC coding is described in terms of deterministic, destination-specific neural trajectories — a dynamical systems framing.
- **Task-state model**: recent OFC theory (Wilson et al., 2014; Wikenheiser & Schoenbaum, 2016) casts OFC as encoding a cognitive map of task-state space with transition probabilities, which the review extends to spatial navigation.

---

### Prevailing model of the system under study

Before this review's central contribution (Basu et al., 2021), the dominant view was that the hippocampal-entorhinal system provided the primary substrate for goal-directed navigation. Place cells over-represent reward locations, generate forward trajectory sequences during theta oscillations and sharp-wave ripples, and some CA1 neurons encode goal-directed vectors. The OFC was well established as a region encoding value, outcome identity, decision confidence, and reward history — but its role in spatial navigation was peripheral. Theoretical models of navigation assumed an external goal signal feeding into the hippocampus but did not specify its source. The review's framing implies the field lacked an identified brain region that could persistently hold a future spatial goal throughout an entire journey, independent of current sensory context.

---

### What this paper contributes

The review synthesises evidence that the OFC is the brain's dedicated goal pointer: a region that encodes a future navigational destination persistently from before motion onset until goal arrival, independently of intermediate locations and sensory inputs. This extends the hippocampal cognitive map framework by proposing a two-system architecture: hippocampus encodes current position (the SR/map), while OFC encodes the goal (the reward vector). The review further proposes specific mechanistic hypotheses — that OFC goal signals may selectively amplify hippocampal trajectory sequences terminating at the goal, and that OFC goal representations emerge through a decision process in which neural ensembles compete among candidate locations. Open questions raised include how spatial maps form in OFC from hippocampal inputs, how OFC-hippocampus interaction produces route planning, and how task-state encoding in OFC interfaces with goal selection.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC)** — primary focus; proposed to encode the future navigational goal persistently as a "goal pointer," causally required for correct destination selection
- **Hippocampus (CA1, ventral subiculum)** — encodes current position via place cells; over-represents reward locations; generates forward trajectory sequences; provides direct anatomical input to OFC
- **Medial entorhinal cortex** — grid cells providing metric spatial representation; over-represents goal locations
- **Medial prefrontal cortex (mPFC)** — implicated in spatial working memory and trajectory planning, but shown not to exhibit prospective persistent goal coding
- **Retrosplenial cortex (RSC)** — contains neurons tuned to shelter direction; projects to SC for escape-directed navigation
- **Superior colliculus (SC)** — downstream target of RSC; mediates correct orientation during escape behavior
- **Amygdala** — proposed contributor to reward-related signals that help OFC form reward-location representations
- **Dopaminergic nuclei (VTA, SNc)** — proposed to provide reinforcement signals facilitating OFC spatial map formation at reward delivery
- **Nucleus reuniens** — disynaptic relay enabling bidirectional OFC-hippocampus communication

---

### Mechanistic insight

The review does not itself present new empirical data, but it integrates evidence from Basu et al. (2021) — which does meet the bar. That primary study provides:

1. An algorithm: persistent, prospective goal coding implemented as destination-specific neural trajectories in OFC that originate before navigation onset and evolve deterministically.
2. Neural data: single-unit recordings and population analyses from OFC during a goal-alternation task, plus optogenetic perturbation specifically linking OFC activity at navigation onset to correct goal selection.

Mapped to Marr's levels:
- **Computational**: the problem is maintaining a representation of a remote, currently unperceived goal location throughout a journey to enable flexible, goal-directed route planning.
- **Algorithmic**: OFC neural ensembles switch from encoding current position to encoding the target location at navigation onset; this goal-specific population state persists robustly despite traversal of intermediate locations, implemented as a deterministic neural trajectory in state space.
- **Implementational**: the review is speculative at this level, but proposes that hippocampal (ventral CA1/subiculum) inputs during reward consumption, gated by dopaminergic and amygdalar reinforcement signals, establish goal-location representations in OFC; during navigation, the absence of reinforcement may disengage hippocampal sensory input, enabling OFC to sustain the stored goal pattern. Cell-type specificity and synaptic mechanisms are not characterised.

---

### Limitations & open questions

- How spatial representations in OFC are formed from hippocampal input — and whether they depend on it — remains untested.
- The mechanism by which OFC goal signals interface with hippocampal trajectory sequences during route planning is hypothetical.
- How the brain forms a conjunctive code of position and value accessible from a distant starting location without explicit sensory triggers is unresolved.
- The relationship between value-based decision-making in OFC and spatial goal selection is unclear; goal values must integrate route effort and geometry, involving brain-wide circuits not yet characterised.
- How task-rule encoding in OFC (state-transition models) relates mechanistically to the emergence of a specific goal representation is an open question.
- Most key evidence comes from rodent linear-track tasks; generalisability to more complex, naturalistic environments is not established.
- The review notes that distinct circuits may serve different navigational demands (reward-seeking vs. escape), but the full landscape of goal-coding systems across species and behavioral contexts is uncharted.

---

### Connections & keywords

**Key citations**:
- Basu et al. (2021) Nature — the orbitofrontal cortex maps future navigational goals (primary empirical anchor)
- Pfeiffer & Foster (2013) Nature — hippocampal place-cell sequences depict future paths to remembered goals
- Stachenfeld, Botvinick & Gershman (2017) Nat Neurosci — the hippocampus as a predictive map
- Russek et al. (2017) PLoS Comput Biol — successor representation linking model-based and model-free RL
- Feierstein et al. (2006) Neuron — spatial goal representation in rat OFC
- Wikenheiser et al. (2017) Neuron — ventral hippocampus suppression impairs OFC task-structure encoding
- Bohm & Lee (2020) eLife — absence of goal coding in mPFC
- Campagner et al. (2023) Nature — RSC-SC circuit for shelter-directed escape
- Wilson et al. (2014) Neuron — OFC as cognitive map of task space
- Rich & Wallis (2016) Nat Neurosci — decoding subjective decisions from OFC
- Zhou et al. (2021) Nature — evolving schema representations in OFC ensembles

**Named models or frameworks**:
- Cognitive map (Tolman)
- Successor representation
- Reward vector / value function (RL)
- OFC as cognitive map of task-state space
- Goal-pointer / goal map hypothesis

**Brain regions**:
- Orbitofrontal cortex (OFC)
- Hippocampus (CA1, ventral subiculum)
- Medial entorhinal cortex
- Medial prefrontal cortex (mPFC)
- Retrosplenial cortex (RSC)
- Superior colliculus (SC)
- Amygdala
- Nucleus reuniens
- Dopaminergic nuclei (VTA, SNc)

**Keywords**:
- goal-directed navigation
- orbitofrontal cortex goal representation
- cognitive map
- prospective coding
- persistent goal coding
- place cells
- successor representation
- navigational goal pointer
- neural trajectory dynamics
- hippocampus-OFC interaction
- value-based decision-making
- spatial working memory
