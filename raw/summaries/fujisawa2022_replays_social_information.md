---
source_file: fujisawa2022_replays_social_information.md
paper_id: fujisawa2022_replays_social_information
title: "Replays of socially acquired information in the hippocampus"
authors:
  - "Shigeyoshi Fujisawa"
  - "Ayako Ouchi"
year: 2022
journal: Neuron
paper_type: review
contribution_type: review
species:
  - rat
tasks:
  - t_maze
brain_regions:
  - hippocampus
  - hippocampus_ca1
keywords:
  - hippocampal_replay
  - place_cells
  - observational_learning
  - social_memory
  - sharp_wave_ripples
  - awake_remote_replay
  - prospective_planning
  - cognitive_map
  - t_maze
  - social_observation
  - memory_consolidation
  - sequence_reactivation
  - replays
  - socially
  - acquired
  - information
  - hippocampus
key_citations:
  - mou_ji2022_observational_learning_replay
  - behrens2018_cognitive_map_organizing_knowledge
wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/sharp_wave_ripple_associated_hippocampal_replay
---

### One-line summary

A commentary on Mou et al. (2022) arguing that hippocampal awake remote replays are not limited to self-experienced trajectories but can also be triggered by social observational learning, implicating CA1 replay in planning based on vicariously acquired information.

---

### Background & motivation

Hippocampal place cell replays during rest are widely thought to underlie memory consolidation and future planning for spatial navigation learned through self-running. However, virtually all prior rodent work on this phenomenon has focused on self-centred experience, leaving open how the hippocampus encodes and utilises information acquired by observing others. This is a significant gap because both humans and animals routinely learn from social observation, and understanding the hippocampal basis of such learning has broad implications for theories of memory and cognitive mapping.

---

### Methods

This is a Previews commentary (not a primary study). It summarises and contextualises the empirical findings of Mou et al. (2022), which used the following approach:

- Observer rats (OB) watched a demonstrator rat (Demo) navigate a T-maze and choose one of two reward arms.
- In a subsequent self-running phase, the OB navigated the same maze and could receive reward at the arm chosen by the Demo.
- Hippocampal CA1 activity was recorded in the OB during the observation period.
- Sharp wave ripple (SWR)-associated replay events were identified and decoded to assess trajectory content.
- Pharmacological hippocampal inactivation was used to confirm task dependence on the hippocampus.
- Control conditions without a demonstrator were used to assess baseline replay rates and trajectory representations.

---

### Key findings

- Awake remote replay events in CA1 of the observer rat emerged after the demonstrator reached the goal arm, i.e. at the moment the observer's future rewarded location was determined by social observation.
- Decoded replay content preferentially reflected the observer's future trajectories from the start position to the correct rewarded site, in both forward and reverse directions.
- In the absence of a demonstrator, remote replay events were significantly reduced and reward-trajectory representations disappeared.
- Pharmacological inactivation of the hippocampus significantly impaired task performance, confirming hippocampal necessity.
- Together these findings (as summarised by Fujisawa and Ouchi) show that social observation, not only self-running, can drive awake remote replays that encode future self-relevant trajectories.

---

### Computational framework

The commentary does not develop a formal computational framework. It invokes the cognitive map framework (O'Keefe and Nadel, 1978; Behrens et al., 2018) as the conceptual backdrop: the hippocampus organises a relational map of entities and spatial locations, and replay serves as a mechanism for prospective planning ("tracing routes on a map"). The paper uses a semantic/episodic memory distinction — place cell activity during active exploration reflects general environmental knowledge, while replay reflects episodic-like autobiographical sequences — but does not formalise this computationally.

The results from Mou et al. constrain models of replay-based planning: any such model must accommodate inputs to the replay mechanism that are not derived from first-person locomotor experience.

---

### Prevailing model of the system under study

The standard model, as described in the introduction, holds that hippocampal place cells encode the animal's current position during active exploration, and that sequential reactivation (replay) of these cells during rest or quiet waking reflects prior self-experienced trajectories. Replay is thought to subserve memory consolidation and prospective planning. The dominant paradigm restricts this to self-running experiences: the animal physically traverses routes and later replays them. Non-spatial and social dimensions of hippocampal function were beginning to be recognised (Behrens et al., 2018; Danjo et al., 2018; Oliva et al., 2020) but had not been integrated into the replay literature.

---

### What this paper contributes

By contextualising Mou et al. (2022), this commentary establishes that awake remote replay is not confined to self-experienced trajectories: social observation of another animal's choices is sufficient to trigger goal-directed replay of the observer's own future routes. This extends the replay-planning framework to include vicariously acquired information and suggests that the hippocampus integrates social inputs into prospective memory representations. The commentary also identifies what remains unknown: how CA1 assemblies contribute to the earlier stages of observational learning (understanding others' actions; inferring their intentions), and how the hippocampus organises a cognitive map that embraces both spatial and non-spatial, including social, entities.

---

### Brain regions & systems

- **Hippocampal CA1** — primary locus of the replay events studied; encodes both self-navigational and socially acquired trajectory information.
- **Hippocampus (general)** — proposed seat of the cognitive map; pharmacological inactivation impairs the observational learning task.
- **CA2** — briefly mentioned in the context of Oliva et al. (2020) as a subregion supporting social memory via sharp-wave ripples.

---

### Mechanistic insight

This commentary does not itself provide neural data. It summarises Mou et al. (2022), which does record CA1 activity and links replay events to social-observation-triggered future planning. The primary paper therefore approaches but does not fully satisfy the bar: it provides neural recordings (CA1 single units and SWRs) and decoding analysis showing replay content, alongside pharmacological disruption, but the commentary does not discuss whether these data distinguish the specific algorithm (e.g. how social spatial information is routed into the replay mechanism) from alternatives.

At the level Marr would call algorithmic, the implicit claim is: the replay mechanism accepts inputs encoding future goal locations regardless of whether those locations were personally visited, and generates sequential trajectory representations prospectively. The implementational substrate (which cell types, pathways, or neuromodulators carry social observation signals into CA1) is not addressed.

---

### Limitations & open questions

- How do hippocampal cell assemblies participate in the earlier stages of observational learning — specifically, understanding others' actions and inferring their intentions — remains unknown.
- The mechanism by which social observation (a non-locomotor, non-self-centred experience) gates or triggers the replay machinery in CA1 is not characterised.
- Whether the cognitive map framework scales to embrace fully non-spatial, social entities and relationships in a unified representational scheme is an open question the paper explicitly raises.
- The commentary is brief and does not discuss potential confounds in Mou et al. (e.g. olfactory or incidental cues) or alternative interpretations of the replay content.

---

### Connections & keywords

**Key citations**:
- Mou et al. (2022) — the primary paper being previewed; observational learning and hippocampal remote replay.
- O'Keefe and Nadel (1978) — cognitive map theory.
- O'Keefe and Dostrovsky (1971) — original place cell discovery.
- Foster and Wilson (2006) — reverse replay in awake state.
- Carr et al. (2011) — awake hippocampal replay review.
- Buzsaki and Moser (2013) — memory, navigation, and theta rhythm.
- Behrens et al. (2018) — cognitive map and organising knowledge.
- Danjo et al. (2018) — spatial representations of self and other in hippocampus.
- Oliva et al. (2020) — CA2 sharp-wave ripples and social memory.
- Eichenbaum (2004) — hippocampus and declarative memory.

**Named models or frameworks**:
- Cognitive map (O'Keefe and Nadel)
- Semantic vs. episodic memory distinction applied to hippocampal function
- Observational learning task (Mou et al.)

**Brain regions**:
- Hippocampal CA1
- Hippocampus
- CA2

**Keywords**:
- hippocampal replay
- place cells
- observational learning
- social memory
- sharp wave ripples
- awake remote replay
- prospective planning
- cognitive map
- T-maze
- social observation
- memory consolidation
- sequence reactivation

### Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
- [[wiki/topics/sharp_wave_ripple_associated_hippocampal_replay|Sharp-wave ripple-associated hippocampal replay]]
