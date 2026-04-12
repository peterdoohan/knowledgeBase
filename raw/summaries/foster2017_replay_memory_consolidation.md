---
source_file: foster2017_replay_memory_consolidation.md
paper_id: foster2017_replay_memory_consolidation
title: "Replay Comes of Age"
authors:
  - "David J. Foster"
year: 2017
journal: "Annual Review of Neuroscience"
paper_type: review
contribution_type: review
methods:
  - bayesian_decoding
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - prefrontal_cortex
  - striatum
  - ventral_striatum
  - nucleus_accumbens
  - ventral_tegmental_area
frameworks:
  - reinforcement_learning
  - attractor_networks
keywords:
  - hippocampal_replay
  - place_cells
  - sharp_wave_ripples
  - awake_replay
  - reverse_replay
  - forward_replay
  - memory_consolidation
  - reinforcement_learning
  - attractor_network
  - value_learning
  - spatial_planning
  - preplay
  - bayesian_decoding
  - cognitive_map
  - nmda_dependent_plasticity
  - replay
  - comes
  - age
key_citations:
  - davidson2009_hippocampal_replay_extended
  - gupta2010_replay_not_simple_function
  - ambrose2016_reverse_replay_hippocampal
---

### One-line summary

This review synthesises two decades of hippocampal replay research to argue that replay does not recapitulate experience but instead samples from an internal model of spatial contingencies, serving functions in learning, planning, and decision-making that go well beyond systems memory consolidation.

---

### Background & motivation

The classical story of hippocampal replay — that place cells reinstate, during sleep, compressed versions of prior waking experience, thereby supporting transfer of memories from hippocampus to cortex — was established around 20 years before this review. However, a large body of subsequent work revealed that many of the initially described properties (sleep-only occurrence, temporal compression of specific episodes, repeated-experience requirement) do not hold generally. This review assembles the updated phenomenology to show how a revised picture fundamentally changes what replay can and cannot be doing, and proposes new functional interpretations grounded in reinforcement learning theory.

---

### Methods

This is a narrative review with no new data collection. The scope and synthesis approach are as follows:

- Covers the replay literature from the first reports of coordinated reactivation (Wilson & McNaughton 1994) through studies published up to approximately 2016.
- Focuses specifically on the detailed phenomenology of hippocampal place-cell replay rather than the broader sharp-wave ripple or theta sequence literatures.
- Deliberately excludes careful treatment of awake vs. sleep distinctions and hippocampal subfield differences where the empirical data do not yet support them.
- Addresses statistical and methodological debates (preplay, Bayesian decoding shuffles) in depth.
- Integrates RL theory to frame functional interpretations.

---

### Key findings

- Awake replay occurs reliably during brief pauses after single laps on a novel track, often in reverse order; this was missed in earlier work because of overtraining and insufficient simultaneous cell recording (Foster & Wilson 2006 and subsequent studies).
- Replay does not replicate the most recent experience; it can depict remote environments and novel trajectories never directly experienced, suggesting it reflects a learned model of traversable space rather than an episodic record (Gupta et al. 2010; Wu & Foster 2014).
- Replay duration scales with the distance depicted, not with the duration of the original behavioral episode, consistent with a constant-speed internal simulation (Davidson et al. 2009; Wu & Foster 2014).
- High-cell-count recordings reveal that awake replay is discontinuous, alternating between hovering at attractor locations and jumping between them, consistent with heteroassociative dynamics superimposed on Hopfield-style autoassociative attractors (Pfeiffer & Foster 2015).
- NMDA receptor activation is required for replay formation but not retrieval, paralleling its role in behavioral memory (Silva et al. 2015 and others); effects on place field shape are much weaker.
- Reverse replay rate is selectively modulated by reward magnitude and reward prediction errors, while forward replay rate is unaffected, linking reverse replay to value learning (Ambrose et al. 2016).
- Forward replay before goal-directed navigation predicts the animal's subsequent trajectory and is selective for the current goal location and task phase, indicating prospective planning (Pfeiffer & Foster 2013a).
- Preplay reports (Dragoi & Tonegawa 2011, 2013a,b) are challenged on methodological grounds: a statistical error in how shuffles were constructed appears to generate spurious significance, and Silva et al. (2015) found no preplay evidence with greater recording power.
- Hippocampal reactivation coordinates with nucleus accumbens, prefrontal cortex, and VTA dopamine neurons during sharp-wave ripple events, consistent with a role in value learning.
- Two animal models of schizophrenia show normal place fields during running but grossly overactive, noisy sharp-wave ripples during stopping, suggesting "diseases of replay" may underlie some neuropsychiatric symptoms.

---

### Computational framework

The review frames replay function within reinforcement learning (RL), specifically the formalism of Markov decision processes (MDPs).

- **States and values**: place cells are treated as providing state representations for an RL agent navigating toward goals. Value functions over states can be learned by pairing place-cell sequences with reward-related signals.
- **Reverse replay and value iteration**: backward replay from reward locations provides an efficient mechanism for spreading value information along incoming trajectories. Because the MDP is Markovian, a single backward pass covers multiple potential starting states simultaneously. A simple model pairs reverse replay with a phasic dopaminergic signal to drive value learning in downstream areas (Foster & Wilson 2006).
- **Forward replay and options**: forward sequences are tentatively linked to RL "options" (extended action sequences), allowing the system to evaluate multi-step plans and reduce state-space dimensionality for generalisation.
- **Attractor networks**: the discontinuous structure of awake replay is explained by a two-timescale recurrent network combining fast Hopfield-style autoassociative dynamics (CA3) with slower heteroassociative connections linking successive attractor states. This predicts jumpy sequences and slowing of replay speed with experience, as attractors deepen.
- **STDP and bidirectional weights**: a neuromodulatory (dopamine-enabled) symmetric STDP rule can explain how forward experience creates bidirectional synaptic connections that support both forward and reverse replay.

---

### Prevailing model of the system under study

Before this review's contribution, the dominant framework was the systems consolidation account: hippocampal place cells fire in temporally compressed sequences during slow-wave sleep, recapitulating the order of activation from prior waking experience. This was thought to provide a mechanism by which episode-specific memory traces are transferred from hippocampus to neocortex for long-term storage, with the hippocampus acting as a temporary buffer. The replay phenomenon was assumed to require multiple repetitions of experience, to be specific to the most recent or most frequent experience, to occur primarily during sleep, and to faithfully compress the temporal structure of the original behavioral episode. Place cells themselves were understood as largely stimulus-bound spatial representations, and replay was their off-line re-expression.

---

### What this paper contributes

The review establishes that nearly every classical feature of replay fails to generalise:

- Replay occurs during wakefulness, immediately after single experiences.
- It does not faithfully recapitulate experience; it can reverse order, ignore recent history, and generate novel trajectories.
- It represents distance/topology rather than temporally compressed episodes.
- It is goal-selective and task-phase-selective, predicting upcoming behavior.
- Reverse and forward replay are functionally dissociable, with only reverse replay tied to reward magnitude.

Together these observations shift the interpretation from "offline memory consolidation" to "online and offline sampling from a learned world model," closer to Tolman's cognitive map concept than to a tape recorder. The review also establishes that preplay, as previously reported, is likely a statistical artifact, and provides a detailed critique of shuffle methods for decoded replay significance testing. The attractor-network framework for sequence generation, supported by the discontinuous structure of high-cell-count recordings, offers a mechanistic alternative to simple chain models and predicts specific empirical phenomena (replay slowing with experience, jumping dynamics).

---

### Brain regions & systems

- **Hippocampus (CA1, CA3)** — primary locus of replay; CA3 proposed as the fast autoassociative attractor network; CA1 as the output stage where most recordings have been made. Distinguishing CA1 vs. CA3 contributions to replay phenomenology remains unresolved.
- **Entorhinal cortex** — upstream source of spatially tuned inputs (grid cells) that may initially define place representations without requiring Hebbian learning.
- **Nucleus accumbens (ventral striatum)** — exhibits coordinated reactivation with hippocampal ripples; candidate site for value storage driven by reverse replay.
- **Prefrontal cortex** — coordinates with hippocampal sharp-wave ripples; implicated in working memory use of awake replay (Jadhav et al. 2016).
- **Ventral tegmental area (VTA) dopamine neurons** — fire in coordination with hippocampal reactivation; candidate neuromodulatory signal coupling reverse replay to reward-prediction-error-based value learning.

---

### Mechanistic insight

The paper partially meets the bar. It synthesises a body of work that collectively identifies an algorithm (heteroassociative/autoassociative attractor sequence generation; dopamine-gated reverse-replay value learning) and includes neural recording data supporting specific aspects of this algorithm — notably the discontinuous replay structure linking to attractor dynamics (Pfeiffer & Foster 2015), and the reward-selectivity of reverse vs. forward replay (Ambrose et al. 2016). However, as a review rather than a primary study, the paper does not itself provide direct neural evidence pitting the attractor algorithm against alternatives.

Mapping the evidence onto Marr's levels:

- **Computational**: The brain is solving the problem of learning a generalisable model of spatial contingencies and associating locations with values, so that future navigation can be planned efficiently without exhaustive forward search.
- **Algorithmic**: Replay events sample trajectories from an internal world model (cognitive map). Reverse replay, paired with a dopaminergic reward signal, propagates value information backward along trajectories. Sequence generation involves fast autoassociative attractor recovery (place sharpening) interleaved with slower heteroassociative transitions between attractor states; this produces the empirically observed hovering-and-jumping pattern and accounts for bidirectional replay from bidirectional STDP weights.
- **Implementational**: NMDA-receptor-dependent plasticity encodes the heteroassociative weights. CA3 recurrent collaterals implement fast autoassociation. Dopamine release from VTA, coordinated with ripple events, modulates STDP symmetry and may gate which transitions are strengthened. Slow gamma rhythm weakly entrains the alternation between hovering and jumping phases within individual replay events. Inhibitory interneurons (not disinhibition) control the controlled recruitment of spikes during replay.

---

### Limitations & open questions

- The exact circuit mechanisms distinguishing awake from sleep replay remain uncharacterised; the review treats them as phenomenologically similar but acknowledges this could mask important differences.
- CA1 vs. CA3 contributions to replay generation have not been dissociated at the level of recorded replay events.
- The function of forward replay is not resolved: the review considers value retrieval, options-based planning, and a prediction-learning account, but cannot adjudicate between them with available data.
- How goal selectivity and task-phase selectivity are mechanistically implemented — i.e. what biases a replay to start at the current location and end at a remembered goal — is unclear and requires extensions to the existing sequence-generation models.
- The time window over which replay consolidation might reactivate memories from previous days, and whether this represents a form of catastrophic-interference-prevention interleaved replay (McClelland et al. 1995), remains unsettled.
- Whether the two-dimensional discontinuous replay structure generalises beyond the linear-track and open-field paradigms used in key studies is unknown.
- The relationship between replay and neuropsychiatric disease (schizophrenia models show disrupted ripple-associated replay) is noted but mechanistically unexplored.
- Theta sequences, which share many properties with replay, are deliberately excluded; how the two phenomena interact or dissociate is not addressed.

---

### Connections & keywords

**Key citations**: Wilson & McNaughton 1994 (pairwise reactivation during sleep); Lee & Wilson 2002 (sequenced sleep replay); Foster & Wilson 2006 (awake reverse replay); Davidson et al. 2009 (extended awake replay); Gupta et al. 2010 (replay not a simple function of experience); Dragoi & Tonegawa 2011/2013 (preplay claims); Silva et al. 2015 (refutation of preplay; NMDA requirement); Pfeiffer & Foster 2013a (goal-directed forward replay); Pfeiffer & Foster 2015 (attractor dynamics); Ambrose et al. 2016 (reward modulation of reverse replay); Jadhav et al. 2012 (awake replay and working memory); Sutton & Barto 1998 (RL framework); McClelland et al. 1995 (complementary learning systems); Hopfield 1982 (attractor networks); Tolman 1948 (cognitive maps).

**Named models or frameworks**: Systems memory consolidation; Complementary Learning Systems (CLS); Markov decision process (MDP); Reinforcement learning (temporal difference / value iteration); Hopfield attractor network; Heteroassociative sequence model (Kleinfeld 1986; Sompolinsky & Kanter 1986); Spike-timing-dependent plasticity (STDP); Bayesian decoding of replay; Cognitive map (Tolman).

**Brain regions**: Hippocampus (CA1, CA3); entorhinal cortex; nucleus accumbens (ventral striatum); prefrontal cortex; ventral tegmental area (VTA).

**Keywords**: hippocampal replay, place cells, sharp-wave ripples, awake replay, reverse replay, forward replay, memory consolidation, reinforcement learning, attractor network, value learning, spatial planning, preplay, Bayesian decoding, cognitive map, NMDA-dependent plasticity
