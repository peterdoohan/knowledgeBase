---
source_file: "bendor2012_biasing_hippocampal_replay_sleep.md"
paper_id: "bendor2012_biasing_hippocampal_replay_sleep"
title: "Biasing the content of hippocampal replay during sleep"
authors: "Daniel Bendor, Matthew A. Wilson"
year: 2012
journal: "Nature Neuroscience"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat", "human"]
tasks: ["linear_track"]
methods: ["tetrode_recording", "computational_modeling", "bayesian_decoding"]
brain_regions: ["hippocampus", "hippocampus_ca1", "entorhinal_cortex"]
frameworks: ["bayesian_inference"]
keywords: ["biasing", "content", "hippocampal", "replay", "during", "sleep"]
key_citations: ["girardeau2009_ripples_spatial_memory"]
---

### One-line summary

Presenting task-associated auditory cues to sleeping rats biases hippocampal replay during non-REM sleep toward the spatial memory linked to that cue, providing direct neural evidence for a mechanism by which targeted memory reactivation improves consolidation.

---

### Background & motivation

The hippocampus is known to replay sequences of neural activity associated with recent experiences during non-REM sleep, and this replay has been hypothesised to drive memory consolidation by transferring information to neocortex. Human studies had already shown that presenting task-associated sensory cues during non-REM sleep enhances memory consolidation for the paired experience, but the underlying neural mechanism — whether this benefit is mediated by selective hippocampal replay — was unknown. This paper asks whether externally delivered sensory cues can causally steer the content of hippocampal replay toward a specific encoded memory, which would link the behavioural memory-improvement effect to a specific neural mechanism.

---

### Methods

- **Subjects**: 4 Long-Evans rats implanted with 16–18 tetrode microdrives targeting right dorsal CA1.
- **Task**: Auditory-spatial association task on a 1.5 m linear track. After a nosepoke, Sound R (upward frequency sweep, 5–20 kHz) directed rats to the right reward site; Sound L (downward sweep, 20–5 kHz) directed them to the left. Sessions continued until rats performed above chance (P < 0.05, binomial test).
- **Recording**: 409 neurons total; 199 place cells selected by peak firing rate > 2 spk/s and mean rate < 5 spk/s. 11 sessions across 4 rats met inclusion criteria.
- **Sleep protocol**: After ≥ 200 trials, rats rested/slept for 2–2.5 hours. During this period, Sound R, Sound L, and three control sounds (correct-trial tone, error-trial noise, complex tone unrelated to task) were played in random order with 5–10 s randomised inter-stimulus intervals at 50 dB SPL.
- **Replay detection**: Reactivation events identified from multiunit activity (MUA) transients (z-score ≥ 2 throughout, peak z ≥ 4, minimum 50 ms duration).
- **Sleep staging**: Non-REM defined by high frame activity, intermittent high MUA, minimal movement; REM by elevated theta/total power ratio.
- **Analysis**: (1) Rate bias — per-cell difference in mean firing rate during replay events following Sound R vs. Sound L. (2) Bayesian spatial decoding of ensemble activity during replay events to reconstruct the rat's "virtual position" on the track.

---

### Key findings

- Place cells with right-sided fields showed a positive rate bias (higher firing after Sound R), and left-sided place cells showed a negative rate bias (higher firing after Sound L); the difference was highly significant (r = 0.29, P < 1.1 × 10⁻⁴; mean rate bias ANOVA P < 7.8 × 10⁻⁵).
- Both Sound R and Sound L independently biased replay in the direction associated with each cue relative to control sounds (Sound R vs. controls, right-side P < 0.02; Sound L vs. controls, left-side P < 0.04).
- Acoustic cues did not change the number of replay events (Kruskal-Wallis, P > 0.05), indicating selective content modulation rather than non-specific arousal.
- The bias was absent during awake reactivation events recorded in the same box (ANOVA, P = 0.82), consistent with human studies showing cue-enhancement is specific to non-REM sleep.
- The bias persisted for up to ~10 s after cue offset and was reset by the next acoustic stimulus; it was significant in both early (0–5.4 s) and late (5.4–10.8 s) windows within a cue epoch.
- The bias was stronger in early sleep than late sleep (first half: P < 1.7 × 10⁻⁵; second half: not significant), suggesting a time-limited window of susceptibility.
- Bayesian decoding confirmed ensemble-level bias: replay events after Sound R were more likely decoded as right-sided (P < 0.05) and after Sound L as left-sided (P < 0.002); mean decoded position differed between conditions (Wilcoxon, P < 0.006).
- Excluding the 17 neurons with candidate sound-evoked responses did not eliminate the effect (ANOVA, P < 8.3 × 10⁻⁴), ruling out direct sound-evoked firing as an artefact.

---

### Computational framework

Not applicable as a formal computational model. The paper uses Bayesian spatial decoding (Zhang et al. 1998) as an analysis tool rather than as a theoretical framework: the likelihood of each position on the track given ensemble spike counts is computed using place cell tuning curves, then Bayes' rule is applied to reconstruct the rat's "virtual position" during replay. This is a decoding technique rather than a model of the underlying process.

The results most directly constrain accounts of memory consolidation that invoke a replay-selection mechanism: any model of memory consolidation must accommodate the finding that sensory input during sleep can selectively bias which spatial memories are replayed, without changing replay rate. The data are consistent with cortico-hippocampal models in which persistent cortical activity (e.g. from auditory cortex processing the cue) biases hippocampal sequence initiation before each replay frame.

---

### Prevailing model of the system under study

The introduction assumes the following baseline picture: the hippocampus encodes episodic experiences during waking and then, during non-REM sleep, spontaneously replays compressed neural sequences representing those experiences. This replay has been proposed as a mechanism for memory consolidation — transferring hippocampal representations to neocortex for long-term storage. Supporting evidence includes observations that hippocampal and cortical neurons reactivate correlated activity during sleep (Wilson & McNaughton 1994; Ji & Wilson 2007), that sharp-wave ripples are correlated with coordinated hippocampal-cortical dynamics (Siapas & Wilson 1998; Sirota et al. 2003), and that disrupting ripple-associated activity impairs spatial learning (Girardeau et al. 2009; Ego-Stengel & Wilson 2010). However, the paper explicitly notes that replay's causal role in consolidation had not been definitively demonstrated: disrupting ripples could impair stored memory traces rather than blocking consolidation per se. The human TMR (targeted memory reactivation) literature (Rasch et al. 2007; Rudoy et al. 2009) showed cue-enhanced consolidation but provided no neural-level mechanism.

---

### What this paper contributes

The paper provides the first direct neural demonstration that the content of hippocampal replay during sleep can be selectively manipulated by external stimulation. This fills the mechanistic gap between the human TMR behavioural literature and the rodent replay literature: it shows that the memory-consolidation benefit of sensory cues presented during sleep plausibly operates by biasing hippocampal replay toward the cue-associated memory. The specificity of the effect (only during non-REM sleep, not awake; content-selective without changing replay count; time-limited to early sleep) aligns with the known boundary conditions of the human TMR effect and places additional constraints on theories of replay-driven consolidation. The finding also implies that hippocampal replay is not purely internally driven — it can be steered by cortical input encoding task-relevant sensory information.

---

### Brain regions & systems

- **Hippocampus (dorsal CA1)** — primary recording site; source of place cell sequences and replay events. Central to the paper's argument as the locus of cue-biased reactivation.
- **Neocortex (auditory cortex, implied)** — proposed route through which task-related sounds reach the hippocampus during sleep; the paper cites evidence that auditory cortex remains responsive to sound during non-REM sleep and suggests cortical responses could bias hippocampal replay selection.
- **Entorhinal cortex (discussed, not recorded)** — proposed as a potential intermediate region capable of maintaining persistent activity bridging sensory input and hippocampal replay selection.

---

### Mechanistic insight

The paper meets criterion 1 (proposes an algorithmic account: sensory cues during sleep activate auditory cortex, which via cortico-hippocampal interaction biases which spatial memory sequence is initiated at each replay frame). It also meets criterion 2 in a limited sense: CA1 ensemble recordings directly demonstrate that the decoded content of replay events is selectively shifted by sensory cues, and control analyses rule out direct sound-evoked responses as artefact.

- **Computational**: The brain must select which of multiple encoded memories to consolidate during each sleep session. External sensory cues that were associated with a memory during learning can serve as retrieval cues to prioritise that memory's consolidation.
- **Algorithmic**: During non-REM sleep, cortical frames precede hippocampal frames by ~50 ms. Auditory cortex responses to task-related cues during sleep generate persistent cortical activity that biases hippocampal sequence initiation, steering replay toward the cue-associated spatial memory ensemble without altering the spontaneous occurrence rate of replay events.
- **Implementational**: The paper does not record from auditory cortex or entorhinal cortex, so the proposed cortico-hippocampal route is inferential. The mechanism within CA1 (e.g. which cell types, neuromodulatory states, or connectivity patterns implement the bias) is not addressed. The implementational level therefore remains open.

---

### Limitations & open questions

- Small sample (4 rats, 11 sessions); three of four subjects showed the individual effect, one did not reach significance.
- The paper demonstrates a correlation between cue presentation and replay content but does not intervene on replay itself to confirm the causal chain to memory consolidation.
- The cortico-hippocampal mechanism (auditory cortex → entorhinal cortex → CA1) is proposed but not directly tested; no cortical recordings were made during sleep.
- The bias is content-selective but the paper cannot fully rule out that subtle position biases in the task (animals not at 100% performance) contributed to the correlation between sound and place cell laterality.
- Whether REM sleep replay is susceptible to similar cue-biasing is unaddressed.
- It is unclear whether the effect requires prior formation of an auditory-spatial association (i.e. whether naive exposure to sound during sleep without prior learning would produce any bias).
- The decrease in bias effectiveness across the sleep session (early > late) raises unresolved questions about the homeostatic or capacity limits of replay.

---

### Connections & keywords

**Key citations**:
- Wilson & McNaughton (1994, Science) — original observation of hippocampal ensemble reactivation during sleep
- Ji & Wilson (2007, Nat Neurosci) — coordinated hippocampal-cortical replay
- Rasch et al. (2007, Science) — odour cue TMR enhances human declarative memory
- Rudoy et al. (2009, Science) — cued memory reactivation during sleep strengthens memories
- Diekelmann et al. (2011, Nat Neurosci) — awake reactivation of cued memories is detrimental
- Girardeau et al. (2009, Nat Neurosci) — ripple suppression impairs spatial memory
- Ego-Stengel & Wilson (2010, Hippocampus) — disruption of replay impairs spatial learning
- Davidson, Kloosterman & Wilson (2009, Neuron) — Bayesian decoding of hippocampal replay
- Kali & Dayan (2004, Nat Neurosci) — computational model of hippocampal-neocortical interactions in replay

**Named models or frameworks**:
- Targeted memory reactivation (TMR)
- Bayesian spatial decoding (Zhang et al. 1998)

**Brain regions**:
- Hippocampus (dorsal CA1)
- Auditory cortex (proposed, not recorded)
- Entorhinal cortex (proposed, not recorded)

**Keywords**: hippocampal replay, memory consolidation, non-REM sleep, targeted memory reactivation, place cells, sharp-wave ripples, auditory-spatial association, Bayesian decoding, sensory cueing during sleep, sleep replay content, cortico-hippocampal interaction, reactivation events
