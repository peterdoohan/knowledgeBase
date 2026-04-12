---
source_file: "findlay2021_replay_wake_sleep.md"
paper_id: "findlay2021_replay_wake_sleep"
title: "The evolving view of replay and its functions in wake and sleep"
authors: "Graham Findlay, Giulio Tononi, Chiara Cirelli"
year: 2021
journal: "Sleep Advances"
paper_type: "review"
contribution_type: "review"
species: ["rat", "human"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "medial_entorhinal_cortex", "prefrontal_cortex", "striatum", "ventral_striatum", "thalamus", "visual_cortex"]
frameworks: ["reinforcement_learning", "model_free_rl", "temporal_difference_learning"]
keywords: ["evolving", "view", "replay", "its", "functions", "wake", "sleep"]
key_citations: ["liu2019_human_replay_reorganizes", "gridchyn2020_replay_selective_memory", "stella2019_hippocampal_reactivation_brownian", "gupta2010_replay_not_simple_function", "ambrose2016_reverse_replay_hippocampal"]
---

### One-line summary

Hippocampal replay is a far more complex, generative, and wake-active phenomenon than the classical sleep-consolidation narrative suggested, and recent reinforcement learning frameworks — particularly Mattar and Daw's prioritised memory access model — offer the most promising unifying account of its diverse features.

---

### Background & motivation

Hippocampal replay was originally described as temporally compressed re-expression of sequential place-cell activity during sleep, and was assigned a central role in memory consolidation via a "two-stage" hippocampal-to-neocortical transfer. However, subsequent work revealed that replay-like activity also occurs during wakefulness, can unfold in reverse order, can represent novel trajectories never directly experienced, and may serve functions including credit assignment, decision-making, and planning — none of which are easily accommodated by the classical framework. This review addresses the gap between the simple classical picture and the growing complexity of findings, surveying current evidence and evaluating theoretical efforts to unify disparate results under a coherent framework.

---

### Methods

This is a narrative review of the rodent and human replay literature.

- **Scope**: Primarily single-unit sequence replay in rodents (mostly rats); includes human MEG/intracranial studies and theoretical/computational accounts.
- **Exclusions**: Reactivation studies without sequential structure are largely excluded, though discussed for historical context.
- **Synthesis method**: Narrative synthesis organised thematically (classical replay, wake replay features, modelling perspectives, methodological issues, future directions).
- **Methodological commentary**: Extensive critical discussion of statistical challenges in replay detection (shuffle methods, false-positive rates, lack of standardisation across labs).

---

### Key findings

- Replay occurs robustly during wakefulness, often immediately after a single experience, and frequently in reverse order — findings incompatible with the classical view of replay as a sleep-specific rehearsal mechanism.
- Replay can represent trajectories never directly experienced by the animal ("novel trajectories"), implicating a model-based, generative process rather than simple trace replay.
- Forward replay dominates before a run (~95%), reverse replay after (~85%); reverse replay is selectively sensitive to reward magnitude and counterfactual scenarios, while forward replay is largely reward-insensitive.
- Replay during sleep appears to be weaker, less frequent, and less structured than during wake (Tang et al., 2017), even though sleep SPW-Rs are larger; sleep replay is almost always "remote" by default given standard recording setups.
- Evidence for functionally distinct subtypes of SPW-Rs (or of forward vs. reverse replay) is limited; Joo and Frank (2018) argue each SPW-R serves multiple cognitive functions.
- Mattar and Daw's (2018) prioritised memory access model — framing replay as prioritised Bellman backups ordered by "need × gain" — reproduces a wide range of empirical findings including asymmetric reward-sensitivity of forward vs. reverse replay, novel trajectory generation, and punishment-biased replay.
- Human MEG evidence (Liu et al., 2019) demonstrates sequential replay of abstract, non-spatial sequences coincident with ripple-band activity, replaying inferred "true sequences" rather than experienced sequences; reverse replay is triggered by reward.
- Methodological standardisation is a critical unsolved problem: no two replay studies share precisely the same detection methods, false-positive rates are difficult to estimate, and replay-score distributions are often continuous rather than bimodal.

---

### Computational framework

**Reinforcement learning (RL) — prioritised memory access (Mattar & Daw, 2018)**

The paper centres its theoretical discussion on RL, specifically Mattar and Daw's formalisation of replay as prioritised Bellman backups. In this framework:

- **What is being modelled**: Spatial navigation as a Markov decision problem; each place-cell reactivation corresponds to a "backup" — updating the expected value of a state-action pair.
- **Key variables**: "Need" (probability of visiting a state soon given current policy) × "Gain" (how much value improvement a backup of that state would yield) determines which memories are prioritised for replay.
- **Key assumptions**: Navigation is Markovian (state history does not determine optimal action); gain is computed from true state-action values in simulation (a known limitation); replay events between trials are the substrate for backup operations.
- **Why it is powerful**: Because gain is asymmetric with respect to reward increases vs. decreases, the model naturally captures the asymmetric sensitivity of forward and reverse replay to reward changes. It also allows novel trajectory construction (by composing previously experienced sub-paths) and is in principle not limited to spatial states.

The review also contextualises earlier RL proposals (temporal difference learning, model-based vs. model-free replay) and notes that the framework does not yet explain when replay occurs or generalise to non-Markovian tasks (e.g. spatial working memory).

---

### Prevailing model of the system under study

The authors frame the paper against the "classical" picture of replay developed from the late 1980s through ~2005: hippocampal replay during slow-wave sleep is a temporally compressed recapitulation of sequential place-cell activity observed during prior wakefulness. This replay is closely coupled to sharp-wave ripples (SPW-Rs), which propagate to neocortex and support a "two-stage" memory consolidation process in which labile hippocampal traces are gradually transferred to stable neocortical representations. According to this view, replay is fundamentally a sleep phenomenon: high cholinergic tone during wake favours encoding and suppresses CA3-driven SPW-Rs, while low cholinergic tone during NREM sleep favours CA3 population bursts and thus SPW-R-mediated consolidation. The discovery of robust awake replay, reverse replay, and replay of novel trajectories progressively eroded each pillar of this model.

---

### What this paper contributes

This review establishes the following updated picture:

1. **Replay is not sleep-specific**: It occurs robustly during wakefulness, with some evidence that awake replay is actually stronger and more structured than sleep replay (Tang et al., 2017).
2. **Replay is generative, not merely recapitulative**: It can construct novel trajectories from learned sub-paths, consistent with model-based computation over a cognitive map rather than passive trace reactivation.
3. **Replay is sensitive to motivational state, not just recent experience**: Reverse replay is modulated by reward value, counterfactual reward availability, and punishment — suggesting a function in value learning and credit assignment.
4. **A unifying RL framework is now available and promising**: Mattar and Daw's prioritised memory access model accounts for more empirical findings than any prior account, though significant limitations remain.
5. **Methodological standards need urgent attention**: The lack of consistent definitions, detection methods, and statistical frameworks makes cross-study comparison unreliable and may inflate apparent replication rates.

Key unresolved questions identified: whether replay during sleep is functionally special despite being weaker; whether distinct SPW-R or replay subtypes exist; the role of dopaminergic systems in modulating replay; the existence of single-unit replay in humans; and how to study replay in non-place, non-spatial cell types.

---

### Brain regions & systems

- **Hippocampus (CA1, CA3)** — primary locus of replay; CA3 recurrent connectivity drives sharp-wave depolarisation of CA1; CA1 place-cell sequences constitute the main replay template studied.
- **CA2** — proposed to trigger SPW-Rs, more so during NREM than wake; may link nesting location to replay content.
- **Medial entorhinal cortex (MEC, superficial layers)** — provides input to hippocampus; some evidence of replay independent of CA1; proposed to exert greater influence on replay during wake than NREM.
- **Prefrontal cortex (prelimbic/ventromedial)** — shows coordinated replay with hippocampus; suggested to activate early relative to SPW-Rs, possibly initiating replay; replay in cingulate and prelimbic cortices reported.
- **Primary visual cortex (V1)** — Ji and Wilson (2007) report replay of location-tuned V1 sequences coordinated with hippocampal replay during slow-wave sleep.
- **Parietal cortex** — some evidence of replay-like activity during slow-wave sleep.
- **Ventral striatum** — possible replay coordinated with hippocampus.
- **Auditory cortex** — Rothschild et al. show bidirectional coordination with CA1 around SPW-Rs during learning, suggesting a cortical-hippocampal-cortical loop.
- **Thalamus / subcortical structures** — noted as understudied; SPW-Rs route to lateral septum and subcortical structures, but the functional significance is unclear.

---

### Mechanistic insight

The paper does not present primary neural data; it is a review. It therefore does not independently meet the bar of presenting an algorithm AND providing neural data that specifically supports that algorithm over alternatives. However, it comes close to meeting this bar by synthesising evidence across studies:

- At the **computational level**, Mattar and Daw's framework specifies what problem replay solves: prioritised credit assignment to maximise long-term reward.
- At the **algorithmic level**, the framework specifies a process (Bellman backups ordered by need × gain) and the review marshals a wide range of empirical observations (asymmetric reward modulation, novel trajectory generation, forward/reverse asymmetry) that are consistent with this algorithm.
- At the **implementational level**, the review acknowledges that CA3 recurrent connectivity drives SPW-Rs and that cholinergic modulation gates the encoding/consolidation balance — but concedes that the precise neural implementation of "gain" and "need" computation is unknown.

The review explicitly notes that the current state of the art cannot distinguish between candidate heuristics the brain might use to approximate the gain term, and that the link between Bellman backup operations and specific firing sequences has not been experimentally verified at the unit level.

---

### Limitations & open questions

- **Methodological heterogeneity**: No consensus on replay detection methods; false-positive rates are difficult to estimate and method-dependent; replay scores are often continuous, not binary.
- **Wake vs. sleep confounds**: Most sleep studies record animals in separate enclosures, making sleep replay remote by default — complicating direct wake vs. sleep comparisons.
- **Reverse replay in sleep**: Very few reports; unclear whether this reflects a genuine sleep-specific suppression or a confound with time since experience and remote vs. local replay.
- **REM sleep**: Putative REM replay is rare, lacks SPW-R dependence, lacks temporal compression, and many "post-task" events were actually pre-task — the status of REM replay is highly uncertain.
- **Preplay**: Well-powered replication attempts have failed; statistical artefact explanations remain plausible.
- **Mattar-Daw model limitations**: Does not explain when replay occurs; assumes true gain is available (omniscient experimenter limitation); assumes Markovian decision structure (fails for working memory tasks).
- **Human single-unit replay**: No single-unit intracranial evidence despite existence of place-like cells, concept cells, and ripples in human recordings.
- **Non-hippocampal replay**: Relationship between hippocampal and cortical replay events, and their respective contributions to cognition, is poorly characterised.
- **Dopaminergic and neuromodulatory mechanisms**: Role of dopamine and acetylcholine in modulating replay content and timing is largely unexplored at fine temporal scales.

---

### Connections & keywords

**Key citations**:
- Foster & Wilson (2006) — first report of awake reverse replay
- Mattar & Daw (2018) — prioritised memory access / Bellman backup model of replay
- Joo & Frank (2018) — review arguing against functional SPW-R subtypes
- Tang et al. (2017) — wake reactivation stronger than sleep reactivation
- Liu et al. (2019) — human MEG demonstration of abstract sequential replay
- Pfeiffer & Foster (2013) — forward replay predicts future path to goal
- Diba & Buzsáki (2007) — forward and reverse replay during ripples
- Grosmark & Buzsáki (2016) — sleep sequenceness lower than wake
- Gridchyn et al. (2020) — assembly-specific disruption of replay
- Stella et al. (2019) — Brownian-motion-like replay tiling environment
- Gupta et al. (2010) — nonlocal and novel trajectory replay
- Ambrose et al. (2016) — reverse replay modulated by reward change
- van der Meer et al. (2020) — methodological review of second-order replay analysis
- Klinzing et al. (2019) — mechanisms of sleep memory consolidation

**Named models or frameworks**:
- Two-stage model of memory consolidation (Buzsáki 1989)
- Prioritised memory access / prioritised Bellman backup model (Mattar & Daw 2018)
- Cognitive map (Tolman; O'Keefe & Nadel)
- Model-based vs. model-free reinforcement learning
- Temporal difference learning
- Preplay / preconfigured sequence hypothesis (Dragoi & Tonegawa)

**Brain regions**:
- Hippocampus (CA1, CA2, CA3)
- Medial entorhinal cortex (MEC)
- Prefrontal cortex (prelimbic, cingulate, ventromedial)
- Primary visual cortex (V1)
- Auditory cortex
- Parietal cortex
- Ventral striatum
- Lateral septum

**Keywords**:
- hippocampal replay
- sharp-wave ripples (SPW-Rs)
- memory consolidation
- reinforcement learning
- Bellman backup
- prioritised memory access
- forward and reverse replay
- cognitive map
- place cells
- awake vs. sleep replay
- credit assignment
- preplay
