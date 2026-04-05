---
source_file: liu2019_human_replay_reorganizes.md
title: "Human Replay Spontaneously Reorganizes Experience"
authors: Yunzhe Liu, Raymond J. Dolan, Zeb Kurth-Nelson, Timothy E.J. Behrens
year: 2019
journal: Cell
paper_type: empirical
contribution_type: empirical
---

### One-line summary

During rest, human hippocampal replay does not simply recapitulate visual experience but spontaneously reorders novel objects according to previously learned abstract structural rules, and each replay event contains a factorized representation of sequence identity and position that precedes the object-specific sensory representation by ~50 ms.

---

### Background & motivation

Hippocampal replay — the spontaneous reactivation of neural sequences during rest — is well established in rodents as a mechanism for memory consolidation and planning, but its functional role in human cognition and non-spatial domains was poorly understood. It had been proposed that replay might support rapid generalisation of abstract knowledge to new experiences, but it remained unclear whether human replay could use previously learned structural knowledge to reorganise the order of novel experiences rather than merely echoing the order in which they were perceived. The paper also asked whether replayed representations include abstract, factorized codes (encoding structural roles independently of sensory identity), analogous to the entorhinal grid-cell system that generalises spatial structure across environments.

---

### Methods

- **Subjects**: Study 1: 21 participants (MEG); Study 2: 22 participants (MEG). Two-day protocol in both studies.
- **Task design**: Participants first learned, on Day 1, an abstract unscrambling rule relating a scrambled visual presentation order to a "true" sequential order. On Day 2, novel objects were presented in a scrambled order consistent with the same rule.
  - In Study 1, individual pairwise transitions were preserved in the scrambled stream (allowing Hebbian associative mechanisms as an alternative explanation).
  - In Study 2, all pairwise transitions were disrupted — correct sequence reconstruction required abstract structural transfer, ruling out simple associative mechanisms.
- **MEG acquisition**: Whole-brain CTF MEG 275-channel system; resting periods of 5 min after each task phase.
- **Decoding approach**: Lasso logistic regression classifiers trained on functional localizer data (random presentation of objects before the main task) to decode individual object identities ("stimulus code") from MEG sensor patterns. In Study 2, additional classifiers were trained for "position code" (sequence position, generalising across sequences) and "sequence code" (sequence identity, generalising across positions).
- **Sequenceness measure**: Cross-correlation-based measure applied to time series of decoded reactivation probabilities, testing whether decoded representations systematically follow a hypothesised transition matrix at particular time lags (up to 600 ms). Significance assessed by permutation testing (shuffled transition matrices).
- **Length-n sequenceness**: Extended measure controlling for all transitions up to length n−1 to detect chains of length n.
- **Time-frequency analysis**: MEG power at ripple frequencies (120–150 Hz) around replay event onsets; source localisation via beamforming.
- **Value manipulation (Study 1 only)**: One sequence designated as reward-associated; second rest period recorded after value learning.

---

### Key findings

- **Replay follows inferred, not experienced, order**: During rest after novel object exposure, MEG sequenceness followed the rule-defined "true" sequence order but not the order of visual experience (Study 1: peak sequenceness at 40 ms lag, b = 0.017 ± 0.005; Study 2: peak at 40 ms, b = 0.021 ± 0.009). This persisted from the first minute of rest throughout the 5-min rest period.
- **Ruling out associativity (Study 2)**: Even when all pairwise transitions in the scrambled stream were disrupted, replay still followed the rule-defined order, demonstrating genuine structural transfer rather than Hebbian chain-association.
- **Direction reverses after reward**: After value learning (Study 1), forward replay switched to reverse replay of the rule-defined sequence (b = −0.028 ± 0.010). Only the rewarded sequence reversed; the neutral sequence remained forward.
- **Reward-triggered reverse replay begins immediately**: Reverse replay of the rewarded sequence appeared during value learning itself (b = −0.053 ± 0.016) and continued during subsequent decision-making (b = −0.055 ± 0.020).
- **Length-4 sequences confirmed**: Multi-step sequenceness analysis demonstrated replay chains of the maximum possible length (4 items), confirming true sequential reordering rather than pairwise coincidence.
- **Factorized structural codes precede sensory codes during replay (Study 2)**: During applied learning, sequence code peaked at 150 ms, stimulus code at 200 ms, and position code at 300 ms post-stimulus. During rest, both position and sequence codes were reactivated ~40–60 ms before the corresponding stimulus code. Position-code replay led stimulus-code replay by 50 ms (Wilcoxon p = 0.013).
- **Transfer replay before object exposure**: In Study 2, position codes replayed in reverse order during a rest period *before* participants had ever seen the Day 2 objects (peak at 30 ms lag, b = −0.036 ± 0.008). Greater pre-exposure transfer replay correlated with faster reduction in position-code activation across learning (interaction p = 0.007).
- **Sharp-wave ripple correlate in humans**: At replay onset, power in the 120–150 Hz band (SWR-band) was significantly elevated compared to baseline in both studies; source localisation placed this increase in the medial temporal lobe / hippocampus (peak MNI: X = 18, Y = −12, Z = −27). Broadband power increase 30 ms post-onset localised to visual cortex (peak MNI: X = 20, Y = −97, Z = −13).
- **vmPFC and reward**: Contrasting rewarded vs neutral sequence replay revealed vmPFC/ventral striatum activation; reward outcome representations co-occurred with rewarded-sequence replay onset (t(20) = 3.20, p = 0.005).

---

### Computational framework

The paper does not develop a formal computational model, but its conceptual framework draws on **factorized / disentangled representations** and **cognitive map theory** (Behrens et al., 2018).

The core idea is that an abstract structural code (encoding relational roles such as "sequence 1, position 2") is kept orthogonal to sensory identity codes, analogous to how entorhinal grid cells encode spatial structure independently of the specific environment. This factorization means the same structural template can be instantiated with new sensory content, enabling fast generalisation. Key variables: a stimulus code (specific sensory identity), a position code (ordinal slot within any sequence), and a sequence code (which sequence an item belongs to). The assumptions are that these codes are neurally separable, that position/sequence codes can be activated independently of current sensory input (allowing preplay and replay), and that a structural template "slots in" new objects during replay to impose the correct order.

---

### Prevailing model of the system under study

The introduction presents two relevant background frameworks:

1. **Rodent hippocampal replay**: Place cells and grid cells spontaneously reactivate spatial trajectories during rest and sleep. Replay is time-compressed, can be forward or reverse (the latter increases after reward), and co-occurs with sharp-wave ripples. Replay has been proposed to support memory consolidation and model-based planning. Prior to this paper, evidence for analogous replay in humans was limited (Kurth-Nelson et al., 2016 showed fast non-spatial sequences in humans, but without the rodent-replay hallmarks).
2. **Factorization in entorhinal cortex**: Grid cells represent spatial structure (position within a metric space) independently of the sensory environment — remapping experiments show the grid persists across different environments. This factorization is proposed to allow structural knowledge to transfer across contexts. The analogous mechanism in non-spatial cognition was speculative.

The prevailing assumption was therefore that human replay, if it existed in non-spatial domains, would primarily recapitulate experienced sequences, and that structural generalisation during replay would require extended offline consolidation rather than being immediate.

---

### What this paper contributes

The paper demonstrates that:

1. **Human replay is not a passive echo of experience**: replay immediately reorganises novel object sequences according to previously learned abstract rules, even when no pairwise transitions from those rules were ever directly experienced (Study 2). This shows that replay is constructive and structure-guided.
2. **Factorized codes are present in human replay**: structural representations (position and sequence identity) are not merely behaviour-relevant codes for task performance — they are actively co-replayed, preceding sensory representations by ~50 ms. This is consistent with a role for structural codes in retrieving the correct item for each sequential slot during replay.
3. **Transfer / preplay of structural codes**: abstract position codes play out in reverse order before novel objects are ever seen, and their strength predicts subsequent learning, suggesting that pre-existing structural templates scaffold the rapid integration of new experiences.
4. **Hallmarks of rodent SWR-replay are present in humans**: time-compression (~40–50 ms per step), reward-triggered direction reversal (rewarded sequences only), and co-occurrence with ripple-band (120–150 Hz) power increases source-localised to the hippocampus. These convergent features substantially strengthen the homology between human MEG-measured replay and rodent hippocampal SWR-associated replay.

Together, these results move the field from speculation to evidence that human replay actively uses abstract structural knowledge to infer novel sequence orderings, providing a plausible mechanism for the rapid inference and generalisation that characterise human cognition.

---

### Brain regions & systems

- **Hippocampus** — proposed locus of SWR-associated replay; source of 120–150 Hz power increase at replay onset (peak MNI: 18, −12, −27). Broadband power increase at replay onset also localised here (0 ms offset).
- **Visual cortex** — broadband power increase 30 ms after replay onset (peak MNI: 20, −97, −13); proposed locus of sensory (stimulus-code) representations being replayed, consistent with coordinated hippocampal–neocortical replay.
- **Medial entorhinal cortex (mEC)** — discussed in the introduction and framework as the likely source of structural / factorized codes (analogous to grid cells), though not directly measured in this MEG study.
- **Ventromedial prefrontal cortex (vmPFC) / ventral striatum** — activated at the onset of rewarded-sequence replay, ~10 ms before replay events; proposed to encode value and potentially instruct the initiation of reverse replay.
- **Posterior temporal sensors** — MEG sensor topography of position and sequence codes; contrasted with occipital dominance of stimulus code, suggesting anatomically distinct substrates.

---

### Mechanistic insight

This paper meets both criteria for a mechanistic insight entry.

**Phenomenon**: During rest, humans spontaneously replay novel object sequences in an order implied by abstract structural knowledge (not the experienced order), and each replay event contains a factorized structural representation (position and sequence codes) that systematically precedes the sensory representation by ~50 ms.

**Marr's three levels:**

- **Computational**: The problem being solved is rapid generalisation — how to immediately integrate new sensory experiences into an existing structural framework so that their relational significance is preserved and can guide future inference and planning. Replay serves to bind new sensory content to pre-existing structural templates.

- **Algorithmic**: The proposed algorithm has two components. First, structural codes (position, sequence identity) are maintained independently of sensory codes (factorization), allowing the same relational template to be "slotted into" new objects. Second, during replay, structural codes are activated first (position/sequence code ~50 ms before stimulus code), suggesting a retrieval process in which the structural slot is activated and then used to cue the appropriate sensory representation. Evidence from MEG decoding of three distinct classifier types (stimulus, position, sequence), each peaking at different latencies during stimulus presentation and in replay, directly supports this sequential activation.

- **Implementational**: Source localisation points to hippocampus as the origin of SWR-band activity at replay onset, with visual cortex engaged 30 ms later. This is consistent with a hippocampal-to-neocortical flow where hippocampal SWRs trigger sequential reactivation of neocortical sensory representations. The vmPFC/ventral striatum precedes rewarded-sequence replay by ~10 ms, suggesting value-based gating of which sequence is triggered. The study does not identify specific cell types or synaptic mechanisms, so the implementational level is only partially addressed.

**Bonus**: The reward-direction reversal (only rewarded sequences reverse; neutral sequences remain forward) and the vmPFC/reward-outcome representation co-occurrence during replay provide evidence for a neuromodulatory/value-system role in shaping replay content and direction.

---

### Limitations & open questions

- **No causal manipulation**: The study cannot establish whether replay is causally necessary for the structural generalisation or subsequent memory — only correlational. Disruption experiments (online SWR detection and interruption) are needed.
- **MEG source localisation**: Source localisation with MEG is inherently limited by the forward model and inversion priors; anatomical claims (hippocampus, vmPFC) should be treated as indicative, not definitive.
- **Preplay vs. learned structure**: It remains ambiguous whether "transfer replay" of position codes before Day 2 experience reflects learned structural knowledge or a preconfigured neural dynamic (as in rodent preplay). The two accounts are not distinguished here.
- **No correlation with behaviour**: Replay strength did not correlate with task accuracy (possibly a ceiling effect — all participants reached 100% accuracy at test), leaving the functional relevance of individual differences in replay strength unresolved.
- **Abstract vs. spatial replay**: Whether the factorized position codes observed here are truly analogous to grid cells, or are a different type of abstract structural code, cannot be determined without recordings from mEC or direct spatial comparisons.
- **Mechanism of direction reversal**: How rewards specifically cause a switch from forward to reverse replay, and why reversal is selective to the rewarded sequence, is not mechanistically explained.
- **Factorization across tasks**: Whether position codes are shared across different task contexts (not just different stimulus sets within the same task) remains an open question.

---

### Connections & keywords

**Key citations**:
- Kurth-Nelson et al. (2016) — prior evidence for fast non-spatial sequences in humans
- Ambrose et al. (2016) — reward-triggered direction reversal of hippocampal replay in rodents
- Behrens et al. (2018) — cognitive map framework and factorized representations
- Ji & Wilson (2007) — coordinated hippocampal–visual cortex replay during sleep
- Dragoi & Tonegawa (2011) — rodent hippocampal preplay
- Olafsdottir et al. (2016) — coordinated grid and place cell replay
- Foster & Wilson (2006) — awake reverse replay of hippocampal place cells
- Gupta et al. (2010) — hippocampal replay of never-experienced trajectories

**Named models or frameworks**:
- Sequenceness measure (cross-correlation-based replay detection)
- Factorized / disentangled representations
- Cognitive map theory (Behrens et al., 2018)
- Transfer replay (human analogue of rodent preplay)
- Sharp-wave ripples (SWRs)

**Brain regions**:
- Hippocampus
- Visual cortex
- Medial entorhinal cortex (mEC)
- Ventromedial prefrontal cortex (vmPFC)
- Ventral striatum

**Keywords**:
- hippocampal replay
- non-spatial replay
- sequential reactivation
- factorized representations
- structural generalisation
- sharp-wave ripples
- MEG decoding
- sequenceness
- abstract sequence learning
- transfer replay
- reward-triggered reverse replay
- cognitive map
