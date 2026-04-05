---
source_file: mckenzie2022_hippocampal_replay.md
title: "Once is enough for hippocampal replay"
authors: Sam McKenzie
year: 2022
journal: Neuron
paper_type: review
contribution_type: review
---

### One-line summary

A Neuron "Previews" commentary contextualising Berners-Lee et al. (2022), which showed that a single traversal of a novel track is sufficient to produce significant CA1 replay, and that further experience progressively elaborates replay structure with finer spatial resolution.

---

### Background & motivation

Episodic memories are typically formed from single experiences, yet studying the neural basis of one-shot learning is methodologically difficult because conventional neural analyses require many repetitions to average out noise. The hippocampus is well established as critical for episodic encoding and retrieval, and sharp-wave ripple (SPW-R)-associated replay is a candidate mechanism linking experience to memory consolidation, but it was unclear how quickly replay emerges and how it changes with accumulating experience. This commentary highlights new evidence bearing directly on those questions.

---

### Methods

This is a commentary/preview article synthesising the findings of one primary empirical paper (Berners-Lee et al., 2022) and placing it in the broader context of the hippocampal replay and place-cell literature. No new data are collected or analysed by the author.

- Scope: primarily focuses on Berners-Lee et al. (2022), which used high-density tetrode recordings (>200 simultaneous CA1 neurons) in rats exploring a novel linear track.
- The reviewed paper used Bayesian decoding of population bursts and parameter sweeps across multiple definitions of replay events, comparing pre- and post-exposure replay against shuffled null distributions.
- Additional references drawn on include work on preplay (Dragoi & Tonegawa, 2011), plateau potential-based plasticity (Bittner et al., 2017), interneuron contributions to SPW-Rs (McKenzie et al., 2021), and ripple duration effects on memory (Fernandez-Ruiz et al., 2019).

---

### Key findings

- A single traversal of a novel location is sufficient for significant CA1 replay to emerge within the following hour; before track exposure, candidate replay events were statistically indistinguishable from shuffled null distributions.
- Replay events grew longer with repeated experience (>10 exposures), but this elongation required active experience and was not explained by the mere passage of time.
- Replay structure evolves in a "hover and jump" fashion: decoded position dwells for ~12 ms then transitions in discrete steps; experience decreases the distance skipped per step and increases the number of steps needed to traverse the full track.
- Early hover points persisted throughout learning while new, intermediate hover points were added, suggesting that initial impressions form a scaffold onto which finer-grained detail is layered.
- Longer replay events co-occurred with increased interneuron activity and with extended prefrontal cortex activation, implicating interneuron plasticity and hippocampal-prefrontal coordination in learning-related replay changes.
- No evidence for preplay (pre-experience hints of future sequences) was detected under the definitions and null distributions used by Berners-Lee et al., though the commentary notes this remains a contested question in the field.

---

### Computational framework

The commentary does not introduce a new computational framework. It situates the findings within the **complementary learning systems (CLS) framework** (McClelland et al., 1995), in which the hippocampus is a fast-learning system that uses replay as a teaching signal to drive slow, interleaved learning in neocortex. The key quantities are:

- Sequential neural reactivation (replay) during SPW-Rs as a candidate mechanism for transferring episodic content to neocortex.
- The rate and specificity of experience-dependent plasticity (one-shot vs. gradual), and how replay statistics (length, step size, hover duration) parametrically track experience.

---

### Prevailing model of the system under study

The introduction assumes a well-established model in which hippocampal place cells form ordered sequences during spatial navigation, and these sequences are reactivated ("replayed") during subsequent SPW-Rs, primarily during rest or sleep. Replay has been conceptualised as a mechanism for memory consolidation within the CLS framework. Prior to Berners-Lee et al., the standard assumption was that meaningful replay required multiple exposures for reliable signal to emerge, largely because neural data are noisy and standard analyses depend on trial-averaging. The commentary also notes an ongoing debate about the core computational role of the hippocampus: spatial representation versus general-purpose episodic memory storage.

---

### What this paper contributes

The commentary establishes that the key new knowledge from Berners-Lee et al. is empirical: replay can emerge from a single experience, resolving a methodological limitation that had left this question open. It further articulates how replay is not static after initial formation but is progressively elaborated — shorter steps, more hover points, longer events — with additional experience. The commentary identifies candidate mechanisms (plateau potentials, interneuron plasticity) while honestly flagging that the mechanistic basis for one-shot learning remains unknown. It raises the preplay debate as an unresolved issue with direct bearing on how prior network structure shapes encoding. The broader significance — that replay may transfer episodic content to neocortex and that unique episodes must be related to existing knowledge — is framed as an agenda for future work.

---

### Brain regions & systems

- **Hippocampus (CA1)** — primary locus of study; site of place field activity, SPW-R generation, and replay sequences whose properties change with experience.
- **Prefrontal cortex** — co-activates during longer replay events, consistent with a role in hippocampal-neocortical dialogue during consolidation.
- **CA1 interneurons** — proposed to pace ripple oscillations and, through plasticity, to mediate learning-related changes in replay structure.

---

### Mechanistic insight

The bar requires both a formalised algorithm and neural data supporting that algorithm over alternatives. This commentary does not present new neural data; it summarises and contextualises the work of Berners-Lee et al. Accordingly, the bar is not met.

The Berners-Lee et al. findings provide strong evidence that experience-dependent plasticity within CA1 (possibly involving plateau potentials and/or interneuron plasticity) rapidly and progressively reconfigures replay structure, but the commentary itself does not map these observations onto a specific algorithmic account with supporting neural recordings. The underlying mechanism — whether plateau potentials, pre-existing network structure (preplay), or interneuron-driven reconfiguration — remains an open empirical question acknowledged by the author.

---

### Limitations & open questions

- The neural mechanism of one-shot place field formation and replay emergence is unknown; plateau potentials (Bittner et al., 2017) are a candidate but not demonstrated to be necessary or sufficient.
- The preplay debate is unresolved: whether prior network structure partially determines which sequences are encoded on first exposure remains contested, and the answer depends heavily on how null distributions are constructed.
- Whether interneuron plasticity causally drives the observed changes in replay length and structure is speculative; the co-occurrence of increased interneuron activity with longer replays is correlational.
- The functional role of replay itself remains debated: spatial map formation versus episodic memory consolidation versus future planning.
- Whether replay encodes episodic content from more complex, non-spatial experiences — and how unique episodes become integrated into existing neocortical knowledge — are identified as key open questions.
- The physiological basis for the ripple oscillation itself is still debated, complicating mechanistic interpretation.

---

### Connections & keywords

- **Key citations**: Berners-Lee et al. (2022); Wilson & McNaughton (1994); Buzsaki (2015); McClelland, McNaughton & O'Reilly (1995); Bittner et al. (2017); Dragoi & Tonegawa (2011); Epsztein et al. (2011); Pfeiffer & Foster (2015); Fernandez-Ruiz et al. (2019); McKenzie et al. (2021).
- **Named models or frameworks**: Complementary Learning Systems (CLS) framework; Bayesian decoding of population bursts; hover-and-jump replay model.
- **Brain regions**: hippocampus (CA1); prefrontal cortex; CA1 interneurons.
- **Keywords**: hippocampal replay, sharp wave ripples (SPW-R), place cells, one-shot learning, episodic memory, memory consolidation, complementary learning systems, preplay, interneuron plasticity, Bayesian decoding, experience-dependent plasticity, spatial sequences.
