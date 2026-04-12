---
source_file: kurth_nelson2016_sequences_non_spatial.md
paper_id: kurth_nelson2016_sequences_non_spatial
title: "Fast Sequences of Non-spatial State Representations in Humans"
authors:
  - "Zeb Kurth-Nelson"
  - "Marcos Economides"
  - "Raymond J. Dolan"
  - "Peter Dayan"
year: 2016
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - human
tasks:
  - navigation_task
methods:
  - computational_modeling
  - behavioral_analysis
brain_regions:
  - hippocampus
frameworks:
  - reinforcement_learning
  - model_based_rl
keywords:
  - hippocampal_replay
  - neural_sequences
  - meg_decoding
  - non_spatial_task
  - reverse_sequenceness
  - state_representations
  - cognitive_map
  - planning
  - temporal_compression
  - multivariate_pattern_analysis
  - sharp_wave_ripples
  - model_based_reinforcement_learning
  - fast
  - sequences
  - non
  - spatial
  - state
  - representations
  - humans
---

### One-line summary

During a non-spatial planning task, human MEG spontaneously encodes fast reverse sequences of up to four task-state representations during object-free planning periods, providing the first evidence for hippocampal-replay-like sequences in humans outside the spatial domain.

---

### Background & motivation

Fast internally generated sequences of neural representations — most famously hippocampal "replay" in rodents — are thought to support memory consolidation, credit assignment, and online planning. However, prior to this study all evidence came from spatial tasks in non-human animals, leaving open whether such sequences are a general mechanism of neural computation or are specific to spatial navigation in rodents. The paper addresses this gap by asking whether analogous sequences can be detected non-invasively in humans performing a non-spatial reasoning task.

---

### Methods

- **Task**: 12 healthy adult participants performed a six-state non-spatial navigation task in a MEG scanner. Each state was defined by a unique visual object (e.g. bird, hammer, cat). From each state, two deterministic transitions were available. Participants planned four-move paths to maximise reward across a trial; reward drifted across trials and two randomly designated "neg" states flipped the cumulative sign of reward.
- **Training**: Participants were trained to criterion (100% quiz accuracy on transition structure) before scanning; model comparison on behaviour strongly favoured tree-search planning models over stimulus-response models.
- **MEG acquisition**: 275-channel axial gradiometer (CTF Omega), resampled to 100 Hz, high-pass filtered at 0.5 Hz.
- **Classifier training**: Lasso-regularised logistic regression models were trained per participant per object on MEG sensor patterns at 200 ms post-stimulus-onset, from a secondary task in which objects were presented visually while participants were still in the scanner.
- **Sequenceness analysis**: Classifiers were applied to MEG from the planning period (no object on screen). A cross-correlation–based "sequenceness" measure quantified whether decoded state-probability time series followed forward or reverse paths through the task's transition matrix. Significance was assessed with mixed-effects models and permutation tests (shuffling state identities, 28 unique permutations).
- **Length analysis**: A generalised version of the sequenceness measure tested whether sequences of length 3, 4, and 5 states occurred at a consistent 40 ms state-to-state lag.

---

### Key findings

- Reverse sequenceness peaked at a 40 ms state-to-state lag and was significant by both parametric (p = 0.0015) and non-parametric (exceeded threshold from 20–70 ms lag) tests.
- The effect was consistent across all 12/12 participants.
- Classifier cross-validated accuracy reached 53.7% ± 3.8% (chance = 16.7%), confirming reliable decoding of individual objects.
- Sequences of length 3 (p = 0.009) and length 4 (p = 0.004) were reliably detected at 40 ms lag; length 5 sequences were not (p = 0.4).
- A complete four-state sequence lasted approximately 120 ms — a temporal compression factor of ~9 relative to the 350 ms visual cross-fade during task execution, or ~25–100 relative to full move execution including feedback display.
- No significant trial-by-trial relationship was found between sequenceness magnitude and earnings (p = 0.83), planning time (p = 0.27), or the specific moves chosen on a given trial (p = 0.85). Sequences were no more likely to contain the subsequently chosen state pair than unchosen pairs.
- The dominant direction was reverse (not forward), contrasting with theta sequences in rodents but resembling sharp-wave ripple (SWR) sequences.

---

### Computational framework

The paper uses a **state-space / cognitive map** framework combined with **multivariate pattern classification** of MEG signals. States are discrete nodes in a graph defined by the task's transition structure; the key quantities are the probabilities assigned by trained logistic regression classifiers to each state at each 10 ms time bin. The "sequenceness" measure formalises whether these probability time series are correlated at a lag consistent with traversal of the transition matrix in forward or reverse direction. The framework assumes that learned state representations are reinstated as spatial MEG patterns during planning even in the absence of the corresponding sensory input, mirroring evidence for cortical pattern reinstatement in memory retrieval.

---

### Prevailing model of the system under study

The paper builds on a well-established finding from rodent electrophysiology: hippocampal place cells spontaneously replay sequences of positions (forward during theta / active movement; forward and reverse during sharp-wave ripples at rest), hypothesised to support memory consolidation and planning. The prevailing assumption challenged here is that such fast internally generated sequences are (a) specific to spatial tasks, and (b) measurable only invasively in non-human animals. The introduction also invokes Tolman's cognitive map hypothesis — that the hippocampus constructs abstract relational maps for non-spatial as well as spatial problems — as motivation for expecting sequences in a non-spatial human task.

---

### What this paper contributes

Prior to this work it was unknown whether fast spontaneous neural sequences existed outside spatial tasks or could be detected non-invasively in humans. The paper demonstrates that: (1) sequences of decodable state representations occur in MEG during human planning in a non-spatial task; (2) these sequences are predominantly reverse in direction; (3) they extend to four states within ~120 ms; and (4) their occurrence is reliable across all participants. This establishes fast sequential state replay as a domain-general mechanism present in the human brain, consistent with the hypothesis that the hippocampus (or associated cortical circuits) uses abstract cognitive maps across problem types. The absence of a trial-by-trial relationship with chosen moves leaves the functional role (prospective planning vs retrospective consolidation vs working memory maintenance) unresolved.

---

### Brain regions & systems

- **Posterior/occipital and posterior temporal cortex** — the locus of classifiable MEG signals; the sensors selected by lasso regression were predominantly occipital and posterior temporal, indicating that decoded sequences most likely reflect reactivation of visual cortical representations.
- **Hippocampus** — implicated as a probable upstream driver of cortical sequences (via sharp-wave ripples coupled to cortical activity), by analogy with the rodent literature, but not directly measured; the paper explicitly notes MEG is poorly suited to detect hippocampal signals directly.

---

### Mechanistic insight

The paper does not meet the full bar. It demonstrates an algorithmic-level phenomenon (sequential state representations following the task's transition structure in reverse order) but does not provide neural data directly linking the specific algorithm — e.g. hippocampal SWR-triggered cortical reactivation — to the measured MEG sequences. The MEG classifiers capture cortical visual signals; whether hippocampus drives these sequences, or whether they arise from intrinsic cortical dynamics, remains unresolved. No recordings or lesion data from hippocampus or any other candidate circuit are provided.

---

### Limitations & open questions

- Small sample (n = 12); insufficient power to detect inter-individual relationships between sequenceness, planning time, and earnings.
- MEG cannot directly resolve hippocampal contributions; the source of the sequences (hippocampus vs intrinsic cortex) is unknown.
- The functional role of reverse sequences (retrospective consolidation, offline planning, working memory maintenance) is not resolved; no trial-by-trial relationship with subsequent behaviour was found.
- Classifiers were trained at a single time point (200 ms post-stimulus), limiting sensitivity to other temporal facets of object representation.
- Whether sequences occur preferentially during within-trial rest/pausing (analogous to rodent SWR epochs) versus active deliberation could not be disambiguated given the unstructured planning period.
- It is unclear whether sequences follow a strict start-state or are initiated remotely; the analysis found no preference for sequences containing the participant's first chosen move.
- Length-5 sequences were not detectable, but whether this reflects a genuine upper bound or limited statistical power is uncertain.

---

### Connections & keywords

- **Key citations**: Foster & Wilson 2006 (reverse replay rodent SWRs); Diba & Buzsaki 2007 (forward/reverse SWR sequences); Pfeiffer & Foster 2013 (prospective hippocampal sequences); Kurth-Nelson et al. 2015 (MEG decoding of retrieved object representations); Tolman 1948 (cognitive maps); Buzsaki & Moser 2013 (memory/navigation theta); Huys et al. 2012 (sequential reasoning task); Ji & Wilson 2007 (coordinated hippocampal-cortical replay); Kali & Dayan 2004 (offline replay and memory consolidation); Sutton 1991 (Dyna architecture).
- **Named models or frameworks**: Sequenceness measure (cross-correlation on decoded state probability time series); lasso-regularised logistic regression classifier; cognitive map / state-space framework; Dyna (offline planning by Sutton 1991).
- **Brain regions**: Posterior/occipital cortex, posterior temporal cortex, hippocampus (inferred/implicated).
- **Keywords**: hippocampal replay, neural sequences, MEG decoding, non-spatial task, reverse sequenceness, state representations, cognitive map, planning, temporal compression, multivariate pattern analysis, sharp-wave ripples, model-based reinforcement learning.
