---
source_file: kurth2023_replay_compositional_computation.md
title: "Replay and compositional computation"
authors: Zeb Kurth-Nelson, Timothy Behrens, Greg Wayne, Kevin Miller, Lennart Luettgau, Ray Dolan, Yunzhe Liu, Philipp Schwartenbeck
year: 2023
journal: Neuron
paper_type: review
contribution_type: theoretical
---

### One-line summary

This perspective proposes that hippocampal replay implements compositional computation by binding entities to generalizable relational roles and stringing these role-bound entities into structured sequences, thereby deriving qualitatively new knowledge beyond simple recapitulation of experience.

---

### Background & motivation

Hippocampal replay was originally understood as rehearsal that transfers episodic memories to the cortex (systems consolidation). A more recent view treats replay as sampling from a learned transition model, enabling planning via mental rollouts through possible future states. However, both frameworks constrain replay to sequences of temporally successive states and cannot account for growing evidence that replay generates novel arrangements of elements that were never experienced together. This paper proposes a more general account: that replay implements a form of compositional computation capable of deriving genuinely new knowledge by recombining entities and their relational roles into structured compound representations.

---

### Methods

This is a perspective/review paper that synthesises existing experimental findings and proposes a new theoretical framework. It does not present new data.

- Scope: rodent spatial replay experiments (sharp wave ripple-nested sequences; theta sequences), human MEG replay studies (nonspatial tasks), and relevant AI/machine learning systems.
- Synthesis approach: narrative review organised around two types of composability (entity–role binding and combinatorial sequencing), drawing on evidence from hippocampal electrophysiology, human MEG decoding, and computational modelling literature.
- The paper also derives experimental predictions to test the hypothesis and draws parallels with hybrid neural-symbolic AI systems (e.g., AlphaGo, MuZero, attention-based networks).

---

### Key findings

- Replay sequences in both rodents and humans are not constrained to recapitulate experienced transitions; they synthesise trajectories through unvisited space, novel spatial combinations, and entirely novel nonspatial orderings.
- Human MEG data (Liu et al. 2019) demonstrate that replay does not replay objects in the order experienced but in a rule-defined order never directly observed, consistent with compositional reorganisation.
- During replay, each replayed object is accompanied (with a ~50 ms lag) by representations of its abstract relational role (position and sequence membership), suggesting role-tagging of each element within a replay sequence.
- "Transfer replay" — spontaneous role-code sequences occurring before participants have encountered the objects to which those roles will be assigned — indicates that role representations exist separately from role-fillers and are subsequently bound to new content.
- In a mental construction task (Schwartenbeck et al. 2021), replay sequences during deliberation dynamically explored combinatorial arrangements of building blocks, with sequential sampling narrowing from all stable-block pairings to combinations consistent with the emerging partial solution, suggesting replay samples compositional hypotheses to resolve uncertainty.
- Replay in spatial tasks hops discretely between positions at the gamma timescale (Pfeiffer & Foster 2015), consistent with gamma organising information into cognitively relevant discrete slots suitable for compositional recombination.
- Disruption of sharp wave ripples in rodents causally impairs spatial learning (Girardeau et al. 2009), supporting a functional role for replay beyond epiphenomenon.
- Hippocampal replay is coordinated with grid cell sequences in the medial entorhinal cortex (Ólafsdóttir et al. 2016), suggesting replay events may simultaneously carry conjunctive hippocampal codes, role codes (mEC/grid cells), and sensory codes (lEC).

---

### Computational framework

The paper proposes a **compositional computation** framework for hippocampal replay, drawing on classical ideas of role-filler binding from symbolic cognition and tensor product representations.

- **What is being modelled**: the hippocampus as a system that binds sensory-specific entity representations (from the "what" pathway via lateral entorhinal cortex) to abstract relational role representations (from the "where" pathway via medial entorhinal cortex), and strings these role-bound entities into sequences.
- **Key variables**: (1) entity representations — sensory-specific codes for individual objects or states; (2) role representations — abstract relational codes (e.g., spatial position, sequence membership, potentially arbitrary roles like "verb" or "agent"); (3) conjunctive hippocampal representations — bindings of entity to role; (4) replay sequences — ordered strings of role-bound entities forming compound structures.
- **Two types of composability**: (i) separation of entity and role, allowing new entities to be bound to existing roles and vice versa (generalisation); (ii) combinatorial sequencing of role-bound entities into an effectively infinite space of compound structures from a finite set of elements.
- **Relationship to prior frameworks**: generalises both consolidation theory (replay need not recapitulate veridical experience) and model-based replay / Dyna (replay need not follow transition-defined rollouts; it can derive new facts rather than just updating value functions or policies).
- **Mapping to AI**: the cortex is likened to a deep neural network that prunes the search space, while hippocampal replay performs compositional search; the hippocampal-cortical loop is analogous to systems like AlphaGo/MuZero that hybridise neural networks with discrete compositional search, with a positive feedback loop where search results improve network representations.

---

### Prevailing model of the system under study

Before this paper's contribution, the dominant model of hippocampal replay had two successive phases. The original view (consolidation hypothesis; McClelland et al. 1995; Wilson & McNaughton 1994) held that the hippocampus rapidly encodes new episodic experiences and that replay during rest and sleep reactivates these stored experiences to drive gradual cortical consolidation. A later revision acknowledged that replay sequences need not directly recapitulate experience but are instead constrained by a learned transition model of the world's dynamics — effectively treating replay as model-based rollouts or mental simulation along MDP trajectories. This model-based account accommodated observations of novel-trajectory replay in spatial tasks (flexible rerouting around barriers, replay of never-traversed paths) and connected replay to planning (Pfeiffer & Foster 2013; Ólafsdóttir et al. 2018). In both frameworks, each element in a replay sequence was assumed to represent a successive state in a temporal chain, and the key function was either memory transfer to cortex or evaluation/training of a policy or value function.

---

### What this paper contributes

The paper argues that the transition-model / rollout account is too restrictive and that replay implements a more general compositional computation. Specifically:

- Replay sequences can contain elements that are not successive states in any experienced or fictive MDP; elements may bear arbitrary relational roles to one another, enabling the expression of complex conceptual structures.
- New knowledge can be derived by composing elements with roles into compound statements, even when that compound was never experienced — going beyond planning or value-function updating to genuine knowledge derivation.
- The existing finding that each replayed item is accompanied by abstract role codes (Liu et al. 2019) is reinterpreted as evidence for role-tagging, the hallmark of a compositional system.
- The paper establishes a connection between hippocampal entity-role binding (supported by the what/where pathway convergence and non-Euclidean role representations such as lap-cell data) and the compositional structure of replay sequences, unifying these previously separate literatures.
- The framework generates concrete experimental predictions: disrupting replay should impair the derivation of new relational knowledge (not just memory consolidation); replay sequences should carry general-purpose role tags (not merely position/sequence codes); and role representations should appear in replay for tasks with rich relational structure (family trees, logical rules, etc.).
- For AI, the paper reframes the brain–AI analogy: rather than mapping replay to experience replay or Dyna, it maps replay to the compositional search component of hybrid neural-symbolic systems, with the cortex providing the neural network component and a mutual feedback loop driving open-ended learning.

---

### Brain regions & systems

- **Hippocampus** — primary locus of replay sequences; generates conjunctive codes binding entity identity to relational role; proposed site of compositional computation via sequential activation of role-bound entity representations; coordinates with entorhinal cortex during replay.
- **Medial entorhinal cortex (mEC) / grid cells** — proposed carrier of abstract relational role representations (spatial coordinates, non-Euclidean roles); coordinates with hippocampal place cells during replay events; candidate anatomical substrate for role tags observed in MEG.
- **Lateral entorhinal cortex (lEC)** — carries sensory-specific entity representations (the "what" stream); converges with mEC in hippocampus to form conjunctive codes.
- **Prefrontal cortex (PFC) / ventromedial PFC (vmPFC)** — influences the content of replay; vmPFC value representations predict replay of rewarded sequences; some PFC neurons are selective for particular replay sequences; proposed to orchestrate hippocampal retrieval by conditioning on task-relevant features such as reward.
- **Neocortex broadly** — receives and stores knowledge derived by replay (consolidation); likened to a deep neural network that learns latent abstractions and biases hippocampal sequence generation; forms a positive feedback loop with hippocampal compositional computation.

---

### Mechanistic insight

The paper partially meets the bar. It presents a well-articulated algorithmic-level account (compositional computation via role-filler binding and sequential composition) and draws on neural data (MEG replay with role-tag decoding, place-cell/grid-cell coordination during replay, sharp wave ripple disruption effects) that are consistent with and supportive of this account. However, the paper is a theoretical perspective synthesising existing studies rather than presenting new neural data specifically designed to test the compositional-computation hypothesis over alternatives. The role-tag data of Liu et al. 2019 (same lead author group) come closest to mechanistic support, but those experiments were not designed to distinguish compositional computation from simpler sequential models with position codes.

- **Computational level**: the brain solves the problem of deriving new relational knowledge by combining existing pieces of knowledge in novel configurations — enabling strong generalisation beyond experienced situations and supporting open-ended learning and creativity.
- **Algorithmic level**: replay sequences represent ordered strings of hippocampal conjunctive codes (entity bound to role), where role representations (~50 ms lag) precede or co-occur with entity representations. Roles are abstract and transferable (preplay / transfer replay confirms roles exist independently of current role-fillers). Sequences are not constrained to temporal transitions but can traverse arbitrary relational graphs. Cortical representations bias which compositions are generated; compositions in turn update cortical representations.
- **Implementational level**: partially addressed. The what/where pathway convergence (lEC and mEC inputs to hippocampus) provides the anatomical substrate for entity-role binding. Gamma oscillations are proposed to discretise sequence elements into separate slots. Sharp wave ripples gate replay events and drive hippocampal–cortical communication. Grid cells in mEC are the proposed anatomical carrier of role codes. PFC neurons selective for specific replay sequences are noted as a possible substrate for higher-order sequence composition. However, specific cell types, synaptic mechanisms, and the precise circuitry generating compositional sequences are not resolved and are acknowledged as open questions.

---

### Limitations & open questions

- The hypothesis is speculative and not yet directly tested; no experiment has been designed specifically to demonstrate that replay causally enables compositional knowledge derivation as opposed to simpler sequential consolidation.
- Role representations observed in Liu et al. 2019 were limited to position and sequence membership; whether hippocampal replay carries more general roles (verb, agent, patient, conditional, etc.) is unknown.
- It is difficult to rule out that the replay patterns attributed to compositional computation could be explained by rollouts through a fictive internal MDP; the authors acknowledge this but argue it is implausible for the Schwartenbeck et al. 2021 construction task.
- Whether the compositional machinery is uniquely human or exists in non-human animals to any substantial degree is unclear.
- Whether preplay/transfer replay sequences reflect hard-coded sequential templates (evolution) or learned templates (prior experience) is unresolved.
- The anatomical precision needed to dissociate role codes (mEC/grid cells) from conjunctive codes (hippocampus) during replay has not been achieved; the proposed three-stream coordinated replay (hippocampal conjunctive codes + mEC role codes + lEC sensory codes) is a prediction, not yet confirmed.
- The causal contribution of replay to compositional computation (rather than being an epiphenomenon of computations performed elsewhere) requires direct disruption experiments in humans, which have not yet been attempted.
- How the brain selects which entities and roles are relevant for a given compositional query, and how context shapes this selection, is not addressed mechanistically.

---

### Connections & keywords

**Key citations**:
- Liu, Y., Dolan, R.J., Kurth-Nelson, Z., and Behrens, T.E.J. (2019). Human replay spontaneously reorganizes experience. *Cell* 178, 640–652.
- Schwartenbeck, P., Baram, A., et al. (2021). Generative replay for compositional visual understanding in the prefrontal-hippocampal circuit. SSRN.
- Pfeiffer, B.E., and Foster, D.J. (2015). Autoassociative dynamics in the generation of sequences of hippocampal place cells. *Science* 349.
- Whittington, J.C.R., et al. (2020). The Tolman-Eichenbaum Machine. *Cell* 183.
- Behrens, T.E.J., et al. (2018). What is a cognitive map? *Neuron* 100.
- Girardeau, G., et al. (2009). Selective suppression of hippocampal ripples impairs spatial memory. *Nature Neuroscience* 12.
- Silver, D., et al. (2016). Mastering the game of Go with deep neural networks and tree search (AlphaGo). *Nature* 529.
- McClelland, J.L., McNaughton, B.L., and O'Reilly, R.C. (1995). Complementary learning systems. *Psychological Review* 102.
- Dragoi, G., and Tonegawa, S. (2011). Preplay of future place cell sequences. *Nature* 469.
- Kurth-Nelson, Z., et al. (2016). Fast sequences of non-spatial state representations in humans. *Neuron* 91.

**Named models or frameworks**:
- Compositional computation / role-filler binding
- Dyna (Sutton 1991)
- Tolman-Eichenbaum Machine (TEM)
- AlphaGo / MuZero
- Complementary learning systems (CLS)
- Systems consolidation theory
- Transformer / attention-based neural networks
- DreamCoder

**Brain regions**:
- Hippocampus
- Medial entorhinal cortex (mEC)
- Lateral entorhinal cortex (lEC)
- Prefrontal cortex (PFC) / ventromedial PFC
- Neocortex

**Keywords**:
- hippocampal replay
- compositional computation
- role-filler binding
- relational representation
- sharp wave ripples
- theta sequences
- nonspatial replay
- MEG replay decoding
- entity-role binding
- systems consolidation
- model-based planning
- cognitive map
