---
source_file: tolman1948_cognitive_maps_rats.md
paper_id: tolman1948_cognitive_maps_rats
title: "Cognitive Maps in Rats and Men"
authors:
  - "Edward C. Tolman"
year: 1948
journal: "Psychological Review"
paper_type: empirical
contribution_type: theoretical
species:
  - rat
tasks:
  - y_maze
keywords:
  - cognitive_map
  - latent_learning
  - vicarious_trial_and_error
  - spatial_navigation
  - place_learning
  - stimulus_response_theory
  - map_breadth
  - comprehensive_map
  - strip_map
  - spatial_orientation
  - rat_maze_learning
  - representational_learning
  - cognitive
  - maps
  - rats
  - men
---

### One-line summary

Rats build internal "cognitive maps" of their environment rather than acquiring sequences of stimulus-response connections, and the breadth of these maps — narrow strip-like versus broad and comprehensive — is governed by identifiable experimental conditions that also illuminate human psychological dynamics.

---

### Background & motivation

The dominant framework in 1940s learning theory held that maze behaviour in rats was explained by the strengthening and weakening of stimulus-response (S-R) connections, with the nervous system acting as a "telephone switchboard" routing incoming stimuli to outgoing responses. Tolman and his Berkeley collaborators believed this account was inadequate: rats showed flexible, goal-directed behaviour that suggested internal representations of the environment rather than trained-on response chains. The paper consolidates a programme of experiments designed to demonstrate that rats acquire map-like cognitive representations, and asks what factors determine whether those maps are narrow or broad.

---

### Methods

- **Paper type**: Empirical primary study (review of a programme of related experiments from the Berkeley laboratory and affiliated groups).
- **Subjects**: Laboratory rats in a variety of maze and discrimination apparatus.
- **Task designs** across five experiment types:
  1. *Latent learning* (Blodgett; Tolman & Honzik; Spence & Lippitt): rats explore mazes without food reward; learning assessed when reward is introduced.
  2. *Vicarious Trial and Error (VTE)* (Muenzinger; Tolman): observing hesitation and look-back behaviour at choice points in visual discrimination tasks.
  3. *Searching for the stimulus* (Hudson): one-trial avoidance conditioning with pattern removal at moment of shock to probe what animals associate.
  4. *Hypothesis experiments* (Krech): insoluble four-choice discrimination box; tracking systematic but shifting choice strategies.
  5. *Spatial orientation* (Tolman, Ritchie & Kalish; Ritchie): trained route blocked, radial-arm sunburst apparatus used to assess which direction animals select.
- **Analysis approach**: Behavioural error curves, choice frequency distributions on radial paths, VTE counts as a function of difficulty and learning stage.

---

### Key findings

- Rats that explored a maze without food reward showed sudden, large performance improvements upon introduction of food, demonstrating that learning had occurred covertly — "latent learning" — without reinforcement driving S-R connections.
- VTE frequency is higher for easy (highly discriminable) stimuli early in learning and at difficult stimuli after learning is established, consistent with active stimulus sampling rather than passive responding.
- Removing a conditioned stimulus at the moment of shock prevented a significant proportion of rats from forming avoidance to it, suggesting rats actively search for the source of aversive events post-hoc.
- Rats showed systematic "hypotheses" (persistent choice strategies) even in insoluble problems, indicating top-down cognitive organisation of responding.
- In the sunburst spatial test, after training on a roundabout route, a majority of rats chose the arm pointing most directly toward the former food location, demonstrating a comprehensive spatial map that encodes direction, not merely the trained path.
- Conditions that promote narrow strip-maps (versus broad comprehensive maps): (1) brain damage, (2) impoverished environmental cues, (3) excessive repetition of a single route, (4) very strong motivation or intense frustration.

---

### Computational framework

Tolman does not employ a formal computational framework. The core theoretical construct is the **cognitive map**: an internal representation of environmental layout (routes, paths, spatial relationships) that the nervous system constructs and updates during exploration, and which guides goal-directed action when motivation is engaged. The key assumptions are:

- Learning is representational, not merely associative: the brain constructs an internal model of environmental structure.
- The map can be acquired in the absence of reward ("latent") and is retrieved flexibly when the animal is motivated.
- Maps vary along a strip–comprehensive dimension, capturing the richness and generalisability of the spatial representation.

This prefigures later computational concepts such as world-model learning, model-based planning, and allocentric spatial representations, though none of these formalisms are employed in the paper.

---

### Prevailing model of the system under study

The paper explicitly addresses two versions of the stimulus-response school as the baseline model: (a) a contiguity account in which correct responses become connected to stimuli through more frequent co-occurrence, and (b) a reinforcement account in which positive outcomes retroactively strengthen preceding S-R connections. Both treat the brain as a "telephone switchboard" transmitting environmental inputs to motor outputs via modifiable connections, with no intervening representational stage. The field-theorist position Tolman argues for holds that intervening brain processes are more complex, pattern-structured, and autonomous than S-R theory allows.

---

### What this paper contributes

Tolman consolidates converging behavioural evidence that S-R accounts are insufficient. The latent-learning data show that rats can learn the structure of an environment without any reinforced response chains, ruling out pure reinforcement-contiguity accounts. The spatial-orientation experiments show that what is learned is relational spatial structure (direction to goal) rather than specific motor sequences. Together, these results establish that internal representations — cognitive maps — mediate between environment and action. The paper also identifies the variables that constrain map breadth, connecting rat experimental findings to clinical and social-psychological phenomena (regression, fixation, displacement of aggression onto outgroups) via the unifying idea that strong emotion narrows representational scope.

---

### Brain regions & systems

Not applicable. The paper is behavioural; no anatomical localisation is attempted. The relevant level of analysis is the systems level: the nervous system as a whole is argued to implement a representational map-building process rather than a switchboard-like S-R relay.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined. It proposes an algorithmic-level account (cognitive map construction and retrieval) and marshals converging behavioural evidence in its favour, but provides no neural data — no recordings, imaging, lesion studies, or pharmacological manipulations — that would link the cognitive-map representation to specific neural activity. The argument proceeds entirely at the computational and algorithmic levels.

The paper does not address the implementational level (cell types, connectivity, or biophysics). It therefore represents a foundational computational-level claim — "the brain solves the problem of navigation by constructing and exploiting an internal spatial model" — without specifying the algorithm in formal terms or grounding it in neural hardware.

---

### Limitations & open questions

- No formal specification of what a cognitive map is or how it is computed; the term is used descriptively and analogically.
- All evidence is behavioural; the inferential gap between choice data and internal representation is large.
- The strip–comprehensive dimension is identified empirically but not theorised mechanistically.
- Conditions producing narrow maps (e.g., strong motivation) are described without a causal account of why motivation narrows representation.
- The extension from rat experiments to human psychological mechanisms (regression, fixation, displaced aggression) is acknowledged as speculative and "cavalier."
- The paper does not address how the cognitive map is updated when environmental structure changes.

---

### Connections & keywords

**Key citations**:
- Blodgett (1929) — latent learning in alley maze
- Tolman & Honzik (1930) — latent learning replication with larger groups
- Spence & Lippitt (1946) — Y-maze latent learning with food vs. water
- Muenzinger (1938) — vicarious trial and error
- Lashley (1930) — visual discrimination apparatus; incidental report of spatial shortcutting
- Hudson (Ph.D. thesis, Berkeley) — one-trial avoidance and searching for the stimulus
- Krechevsky/Krech (1932) — hypothesis experiments in four-choice box
- Tolman, Ritchie & Kalish (1946) — spatial orientation, sunburst apparatus

**Named models or frameworks**:
- Cognitive map (Tolman)
- Strip-map vs. comprehensive-map distinction
- Latent learning
- Vicarious trial and error (VTE)
- Stimulus-response (S-R) / telephone switchboard theory (the foil)
- Field theory (Tolman's theoretical camp)

**Brain regions**: Not applicable (no anatomical analysis).

**Keywords**: cognitive map, latent learning, vicarious trial and error, spatial navigation, place learning, stimulus-response theory, map breadth, comprehensive map, strip map, spatial orientation, rat maze learning, representational learning
