---
source_file: "kurth_nelson2023_replay_compositional_b.md"
paper_id: "kurth_nelson2023_replay_compositional_b"
title: "Replay and compositional computation"
authors: "Zeb Kurth-Nelson, Timothy Behrens, Greg Wayne, Kevin Miller, Lennart Luettgau, Ray Dolan, Yunzhe Liu, Philipp Schwartenbeck"
year: 2023
journal: "Neuron"
paper_type: "review"
contribution_type: "theoretical"
species: ["human"]
tasks: ["t_maze", "hidden_graph_task"]
brain_regions: ["hippocampus", "entorhinal_cortex", "medial_entorhinal_cortex", "lateral_entorhinal_cortex", "prefrontal_cortex", "ventromedial_prefrontal_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl", "tolman_eichenbaum_machine"]
keywords: ["replay", "compositional", "computation"]
key_citations: ["kurth_nelson2016_sequences_non_spatial", "liu2019_human_replay_reorganizes", "gupta2010_replay_not_simple_function", "behrens2018_cognitive_map_organizing_knowledge", "whittington2020_tolman_eichenbaum_machine"]
---

### One-line summary

This perspective proposes that hippocampal replay implements compositional computation by binding entities to generalizable relational roles and assembling these role-bound entities into structured sequences, enabling the brain to derive genuinely new knowledge far beyond simple recapitulation of experience.

---

### Background & motivation

Hippocampal replay was originally understood as rehearsal transferring episodic memories into stable cortical storage (systems consolidation). A subsequent update treated replay as sampling from a learned world model, enabling planning through mental rollouts of possible future trajectories. However, neither framework adequately accounts for growing evidence that replay generates novel arrangements of elements that were never experienced in that combination. The paper proposes a further update: replay instantiates compositional computation in which entities are bound to relational roles and assembled into structured compounds, allowing the brain to derive new knowledge by reasoning about the implications of combining existing pieces — a capacity that far outstrips standard deep learning and may underlie human generalisation from minimal data.

---

### Methods

This is a theoretical review paper. Scope and synthesis approach:

- Reviews rodent spatial replay literature (sharp-wave ripple sequences, T-maze stitching, novel trajectory generation, barrier adaptation, inaccessible-space replay).
- Reviews human MEG replay literature (Kurth-Nelson et al. 2016; Liu et al. 2019; Schwartenbeck et al. 2021) to characterise non-spatial and role-tagged replay.
- Reviews hippocampal binding of entities to roles, organised by three levels of generality: spatial roles, non-Euclidean Euclidean-topology roles, and fully abstract non-Euclidean roles.
- Reviews bidirectional hippocampal-cortical interactions during replay (cortex-to-hippocampus goal-biasing; hippocampus-to-cortex consolidation).
- Proposes experimental predictions for disruption and MEG-decoding tests of the compositional hypothesis.
- Draws an extended analogy with hybrid AI systems (AlphaGo, MuZero, attention-based transformers, DreamCoder) that combine neural networks with compositional search.

---

### Key findings

As a theoretical review, key findings are conclusions drawn from the synthesised literature:

- Replay sequences are not constrained to recapitulate past experience; they stitch together fragments from separate experiences, generate novel trajectories, and replay through never-visited space.
- The predominant view has shifted from consolidation-replay to model-based-replay; this paper proposes a further shift to compositional-replay.
- Two types of composability are identified: (1) binding new entities to existing generalizable relational roles (entity-role separation, analogous to role-filler binding in cognitive science); (2) assembling role-bound entities into an effectively infinite variety of compounds (sequences).
- Human MEG data (Liu et al. 2019) demonstrate that replay sequences in non-spatial tasks include abstract role tags (position, sequence identity) that precede the reactivation of each object by ~50 ms, providing direct evidence for entity-role binding in replay.
- 'Transfer replay' (role codes play out before task objects are experienced) mirrors rodent 'preplay', suggesting roles exist as separable templates prior to acquiring role-fillers.
- Replay in a construction task (Schwartenbeck et al. 2021) assembles building-block representations into novel spatial configurations not reducible to a temporal MDP rollout, demonstrating the second type of composability.
- Replay sequences jump discretely between representations (aligned with gamma oscillation), consistent with a slot-based compositional architecture rather than a continuous trajectory.
- A positive feedback loop is proposed: replay composes existing entities into sequences to derive new knowledge; this knowledge is consolidated into cortex and subsequently available as new entities for higher-order replay.
- The hippocampal-cortex hybrid maps onto machine-learning hybrids (neural networks + compositional search); cortex is hypothesised to prune the combinatorial search space of replay sequences, analogous to AlphaGo's policy network guiding tree search.

---

### Computational framework

**Framework**: Compositional computation / symbolic-connectionist hybrid, grounded in reinforcement learning and cognitive map theories.

**Core formalism**:
- Entities (role-fillers) are bound to roles via conjunctive hippocampal codes, where a 'what' pathway (lateral entorhinal cortex) and a 'where' / relational pathway (medial entorhinal cortex / grid cells) converge.
- A replay sequence constitutes a structured compound: a temporally ordered set of entity-role bindings that, taken together, express a meaning exceeding the sum of parts.
- Key variables: entity representations (object-specific hippocampal codes), role representations (abstract relational codes, potentially carried by grid cells), and conjunctive codes (entity-in-role, carried by hippocampal place/concept cells).
- Assumptions: (i) roles are generalisable and separable from role-fillers; (ii) time is the axis of composition (sequential activation keeps items separate); (iii) replay is not limited to MDP rollouts — elements need not be successive states but can bear arbitrary relational structure; (iv) the output of compositional replay is new propositional knowledge, not necessarily a policy update.

The framework is explicitly speculative and extends predecessor frameworks (world-model-based replay, Dyna) by removing the constraint that replays update value functions or policies.

---

### Prevailing model of the system under study

The introduction positions two successive models of hippocampal replay as the baseline the paper is pushing against:

1. **Consolidation model** (McClelland et al. 1995; Wilson & McNaughton 1994): Hippocampus rapidly encodes new experiences; replay during rest/sleep is rehearsal that transfers this information to cortex for long-term storage. Replay faithfully recapitulates past experience.

2. **Model-based (internal model) view** (Dudai 2012; Foster 2017; Olafsdottir et al. 2018; Pezzulo et al. 2014): Replay is not constrained to repeat experience but draws on a learned transition model, enabling generation of plausible novel trajectories. This model supports online planning (Johnson & Redish 2007; Pfeiffer & Foster 2013) and offline Dyna-like training of value functions (Mattar & Daw 2018; Sutton 1991).

Both models treat replay events as 'rollouts' — sequences of successive predicted world-states linked by transition probabilities — and both are concerned with updating memory or policy. Neither accommodates replay of items that are not temporally successive states, nor replay that discovers abstract relational knowledge without a direct policy consequence.

---

### What this paper contributes

The paper proposes a third-generation account of replay that generalises both predecessors:

- **Relaxes the rollout constraint**: items in a replay sequence need not be successive world-states; they can bear arbitrary relational structure (verb, start-point, patient, etc.), enabling replay to express propositional-like compound knowledge.
- **Generalises the output**: replay need not update a value function or policy; it can derive new factual knowledge about the world (e.g., inferring p > r from p > q and q > r).
- **Extends the role framework**: synthesises evidence that the hippocampal 'where' pathway carries not just spatial roles but potentially fully abstract, non-Euclidean roles, making hippocampus a general-purpose entity-role binding device.
- **Provides mechanistic grounding for novelty generation**: the Liu et al. (2019) and Schwartenbeck et al. (2021) datasets are reinterpreted as evidence of compositional replay constructing novel compounds, not just rollouts.
- **Links to AI**: maps the hippocampal-cortical replay system to hybrid neural-symbolic AI architectures, generating bidirectional hypotheses — e.g., cortex acts as a policy/value network pruning hippocampal compositional search.
- **Proposes testable experiments**: replay disruption + compositional reasoning tasks in rodents; MEG decoding of role-tagged replay during chess-puzzle deliberation in humans.

---

### Brain regions & systems

- **Hippocampus (HC)** — primary locus of replay; generates conjunctive entity-in-role representations; proposed sequence generator that slots content into abstract templates.
- **Medial entorhinal cortex (MEC)** — 'where' / relational pathway; carries abstract role representations (spatial and potentially non-spatial); grid cells are a prime candidate for role tags observed in replay.
- **Lateral entorhinal cortex (LEC)** — 'what' / sensory pathway; carries object/entity representations invariant to arrangement in space.
- **Ventromedial prefrontal cortex (vmPFC)** — value representations that predict whether rewarded sequences are replayed; proposed to bias hippocampal retrieval by conditioning the joint memory distribution on reward.
- **Prefrontal cortex (PFC) broadly** — some PFC neurons are tuned to specific replay sequences (Berners-Lee et al. 2021); could feed back into hippocampus as higher-order entities, enabling nested compositional replay within hundreds of milliseconds.
- **Auditory cortex** — shown to lead hippocampal reactivations in sound-cued replay (Rothschild et al. 2017), illustrating how cortical areas supply content that shapes replay sequences.

---

### Mechanistic insight

The paper does not meet the high bar for this section as defined in the rubric. It is a theoretical perspective/review and does not present new neural recordings or imaging data. It synthesises existing neural datasets (MEG replay in humans, rodent place-cell recordings) but does not itself provide neural data linking its proposed compositional algorithm to measured activity over alternatives.

The closest the paper comes is reinterpreting Liu et al. (2019) — which did acquire MEG data showing role-tagged sequences — as evidence for entity-role binding in replay. However, that evidence was collected by a different study under a different framing. The paper's core contribution is the compositional algorithm itself, not its neural validation.

What the paper does offer at the algorithmic level (Marr level 2): replay sequences implement a slot-based binding operation in which each item is tagged with an abstract role representation ~50 ms before/alongside the item representation itself, and items are chained temporally (possibly one per gamma cycle) to form structured compounds. This is a well-specified algorithmic proposal, but the neural data linking it specifically to the compositional hypothesis over simpler alternatives is not yet available — the authors acknowledge the hypothesis is speculative and propose the necessary experiments.

---

### Limitations & open questions

- The hypothesis is explicitly speculative; causal evidence that replay disruption impairs compositional reasoning (not just memory) does not yet exist.
- It is unclear whether the role representations detected in human MEG are genuinely non-Euclidean (e.g., verb-like) or whether current evidence is limited to position and sequence-membership codes.
- Rodent replay experiments cannot easily probe compositional cognition; human replay disruption (TMS, ultrasound) has not been attempted.
- The mechanism by which cortex biases hippocampal compositional search is unspecified.
- The boundary between compositional replay and model-based rollout replay is not sharply defined; the authors acknowledge simpler replay in simpler settings is better described by rollout models.
- Transfer replay / preplay: whether the pre-task role sequences are hardwired by evolution or learned from prior sequential experience remains unresolved.
- The positive feedback loop (replay → cortical abstraction → new entities for higher-order replay) is highly speculative and lacks direct empirical support.
- Whether non-human animals (beyond limited hints) can represent truly abstract, non-Euclidean roles is unknown.

---

### Connections & keywords

**Key citations**:
- Kurth-Nelson et al. (2016) — non-spatial MEG replay in directed graph task
- Liu et al. (2019) — role-tagged non-spatial replay with position/sequence abstract codes
- Schwartenbeck et al. (2021) — compositional replay in construction task
- Gupta et al. (2010) — T-maze replay stitching separate spatial segments
- Pfeiffer & Foster (2013) — prospective novel-trajectory replay
- Dragoi & Tonegawa (2011) — rodent preplay
- Behrens et al. (2018) — cognitive map framework; role-filler binding in hippocampus
- McClelland et al. (1995) — systems consolidation
- Sutton (1991) — Dyna model-based RL
- Silver et al. (2016) — AlphaGo as hybrid compositional system
- Whittington et al. (2020) — Tolman-Eichenbaum machine; grid cells as relational roles

**Named models or frameworks**:
- Compositional replay hypothesis (this paper)
- Systems consolidation theory
- Model-based replay / Dyna
- Tolman-Eichenbaum Machine (TEM)
- AlphaGo / MuZero (as AI analogs)
- DreamCoder (program synthesis as replay analog)
- Role-filler binding / dynamic binding (Hummel & Holyoak 2003)

**Brain regions**:
- Hippocampus
- Medial entorhinal cortex (grid cells)
- Lateral entorhinal cortex
- Ventromedial prefrontal cortex
- Prefrontal cortex

**Keywords**:
- hippocampal replay
- compositional computation
- entity-role binding
- sharp wave ripples
- non-spatial replay
- MEG replay decoding
- cognitive map
- systems consolidation
- role-filler separation
- grid cells as relational roles
- transfer replay / preplay
- neural-symbolic hybrid AI
