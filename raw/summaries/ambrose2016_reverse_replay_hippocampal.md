---
source_file: ambrose2016_reverse_replay_hippocampal.md
paper_id: ambrose2016_reverse_replay_hippocampal
title: "Reverse Replay of Hippocampal Place Cells Is Uniquely Modulated by Changing Reward"
authors:
  - "R. Ellen Ambrose"
  - "Brad E. Pfeiffer"
  - "David J. Foster"
year: 2016
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - linear_track
methods:
  - tetrode_recording
  - bayesian_decoding
  - behavioral_analysis
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - ventral_tegmental_area
frameworks:
  - reinforcement_learning
keywords:
  - hippocampal_replay
  - sharp_wave_ripples_swrs
  - reverse_replay
  - forward_replay
  - place_cells
  - reward_modulation
  - temporal_credit_assignment
  - memory_consolidation
  - awake_replay_directionality
  - dopamine_hippocampus_interaction
  - adaptive_reward_coding
  - bayesian_sequence_decoding
  - reverse
  - replay
  - hippocampal
  - place
  - cells
  - uniquely
  - modulated
  - changing
key_citations:
  - singer2009_reward_reactivation_hippocampus
---

### One-line summary

Reverse, but not forward, hippocampal replay rates track changes in reward magnitude, establishing a functional dissociation between the two directions of awake replay during sharp-wave ripples.

---

### Background & motivation

Hippocampal place cells replay behavioural sequences during sharp-wave ripple (SWR) oscillations both in sleep and during awake pauses. Awake replay can occur in forward order (same as experienced) or reverse order (opposite to experience), and competing hypotheses link awake replay to reward-based learning (temporal credit assignment) and to memory retrieval for decision making. Prior work had shown that the mere presence vs. absence of reward modulates overall SWR rate, but no study had tested whether changing reward magnitude selectively affects replay directionality. The question of whether forward and reverse replay have distinct functional roles had therefore remained open.

---

### Methods

- **Subjects**: 5 male Long-Evans rats, implanted with 40-tetrode microdrives targeting CA1 of the hippocampus; 120 ± 10 single units isolated per session.
- **Task**: Linear track running (1.5–1.8 m); rats ran 15–20 laps per epoch across three successive epochs per day.
- **Reward manipulation**: Two experiments — Experiment 1 increased reward 4× at one track end during epoch 2; Experiment 2 removed reward at one end during epoch 2. Epochs 1 and 3 had equal reward at both ends.
- **SWR detection**: Ripple power (150–250 Hz LFP) peaks >3 SD above mean identified as candidate events.
- **Replay detection**: Bayesian decoding of spike trains in 10 ms windows during stopping periods; weighted correlation threshold >0.6 used to identify significant trajectory replays (~15–20% of SWRs).
- **Directional classification**: Unidirectional place fields computed; replays assigned a forward or reverse label when downward or upward decoding probability exceeded 66.5% (79% and 77% of replays classifiable in Experiments 1 and 2, respectively).
- **Statistics**: Poisson generalised linear mixed models (GLMMs) with rat and session as nested random effects; multiple comparisons corrected with single-step method.

---

### Key findings

- **SWR and overall replay rates track reward**: Both increased significantly at the 4× reward end (Exp. 1: z = 5.24, p = 1.61 × 10⁻⁷ for SWRs; z = 3.45, p = 5.67 × 10⁻⁴ for replays) and decreased significantly when reward was removed (Exp. 2: z = −6.66, p = 2.67 × 10⁻¹¹ for SWRs; z = −3.16, p = 0.0016 for replays).
- **Reverse replay selectively reflects reward changes**: Reverse replay rate increased at increased reward and decreased at decreased reward (Exp. 1: z = 3.57, p = 3.60 × 10⁻⁴; Exp. 2: z = −2.05, p = 0.041). Forward replay rate was unaffected in both experiments (Exp. 1: z = 0.305, p = 0.76; Exp. 2: z = −1.83, p = 0.068).
- **Adaptive (relative) reward coding**: The modulation reflected relative reward magnitude, not absolute levels — increasing reward at one end simultaneously elevated reverse replay there and depressed it at the unchanged end, and vice versa.
- **Cross-temporal consistency**: A bootstrap analysis showed that relative reward increases produced similar patterns of replay rate coefficients across both experiments (SSD p = 0.005), while opposite-valence phases were anticorrelated.
- **Reverse replay elevated after reward reinstatement**: In Experiment 2, reverse (but not forward) replay was significantly elevated at the previously unrewarded end when baseline reward was restored in epoch 3 (z = 3.35, p = 0.0049), consistent with sensitivity to reward prediction error-like signals.
- **Both replay types locally initiated**: ~86% of replays in Exp. 1 and ~78% in Exp. 2 were locally initiated (starting at animal's current position).

---

### Computational framework

The paper does not develop a formal computational model but frames its interpretation within reinforcement learning theory, specifically the temporal credit assignment problem (Sutton and Barto, 1998). The core idea is that locally initiated reverse replay propagates value information backward along the path leading to the reward site, enabling place cells with fields distal from reward to become associated with reward value. This is consistent with an eligibility-trace or TD-learning logic in which reverse-ordered reactivation during a reward-triggered neuromodulatory signal (dopamine) serves as the backward-propagating value update. The paper also invokes spike-timing-dependent plasticity (STDP) modified by dopamine, noting that reverse-order firing that would normally induce LTD can be converted to LTP by dopamine, providing a candidate synaptic implementation. The rate changes themselves are interpreted cautiously — as a byproduct of reward-triggered initiation of reverse replay rather than as an encoding of reward magnitude per se.

---

### Prevailing model of the system under study

Prior to this paper, the field recognised two classes of awake hippocampal replay — forward and reverse — occurring during SWRs at rest locations. Reverse replay was originally proposed as a learning mechanism for temporal credit assignment (Foster and Wilson, 2006): by replaying the recent incoming trajectory in reverse at a reward location, place cells along the path could be associated with reward via a simultaneous dopamine signal. Forward replay was later associated with memory retrieval and prospective planning, with studies reporting that it could predict upcoming behavioural choices (Pfeiffer and Foster, 2013; Jadhav et al., 2012). However, both forms of replay were often studied jointly or using SWR rate as a proxy without directional decomposition. The presence (vs. absence) of reward had been shown to modulate SWR rate (Singer and Frank, 2009), but whether reward magnitude specifically and differentially modulated forward vs. reverse replay was untested. The implicit assumption was that both replay types might respond similarly to reward, or that their distinction was primarily spatial/content-based rather than reward-related.

---

### What this paper contributes

By varying reward magnitude within a simple linear track task and decomposing replay by direction, Ambrose et al. demonstrate for the first time that reverse and forward replay are functionally distinct in their relationship to reward. Specifically:

- Reverse replay is shown to be a reward-sensitive signal, tracking both increases and decreases in reward and encoding relative (not absolute) reward magnitude across the environment.
- Forward replay is shown to be reward-insensitive under the same conditions, consistent with a role in planning or memory retrieval rather than in credit assignment.
- The bidirectional control (forward vs. reverse within the same stopping periods) rules out trivial behavioral confounds such as differential stopping time.
- The results support the hypothesis that reverse replay selectively participates in memory consolidation of recent reward-related experience, and implicate dopaminergic input (from VTA, whose neurons also adaptively code reward range) as a likely trigger.

---

### Brain regions & systems

- **Hippocampus CA1** — primary recording site; source of place cell sequences and SWR-associated replay; the locus of reward-modulated reverse replay.
- **Ventral tegmental area (VTA)** — discussed as likely modulatory input; VTA dopamine neurons show the same adaptive range coding of reward, are activated during hippocampal SWRs and replay (Gomperts et al., 2015), and promote later hippocampal reactivation (McNamara et al., 2014). Not directly recorded in this study.
- **CA3-CA1 synapse** — discussed in relation to dopamine-modulated STDP and the mechanism by which reverse replay might strengthen forward associations (Brzosko et al., 2015).

---

### Mechanistic insight

This paper meets both criteria for a mechanistic insight entry.

1. It formalises an algorithm: locally initiated reverse replay at reward locations serves as a backward-propagating credit assignment mechanism, proposed to pair spatial trajectories with reward signals for value learning.
2. It provides neural data specifically supporting this mechanism over the alternative (that both directions of replay are reward-sensitive): tetrode recordings from CA1 with directional Bayesian decoding directly show that only reverse replay tracks reward changes.

**Computational level**: The brain is solving the temporal credit assignment problem — associating spatial locations distant from reward with the value of reward encountered later.

**Algorithmic level**: During stopping periods at reward locations, SWR-associated reverse replay re-activates place cell sequences representing the immediately preceding incoming trajectory in time-compressed reverse order. This replay is selectively triggered at a rate proportional to relative reward magnitude (or reward prediction error), allowing value information to propagate to place representations distal from the reward.

**Implementational level**: The paper presents suggestive (indirect) evidence: VTA dopamine neurons fire during hippocampal SWRs and replay; dopamine neuromodulation can convert reverse-order STDP from LTD to LTP at CA3-CA1 synapses; and the adaptive range coding of reward seen in reverse replay matches the known adaptive coding of reward by dopamine neurons. However, no direct recordings of VTA neurons simultaneous with replay, or pharmacological manipulation of dopamine during replay, were performed — the implementational account remains inferential.

---

### Limitations & open questions

- Only 15–20% of SWRs contained detectable replay; the remaining SWRs may carry directional content not captured. The authors argue random cell sampling should not bias direction, but this is unverified.
- Removal of reward (Exp. 2) induced behavioral changes (reduced stopping time at unrewarded end), complicating direct rate comparisons; the relative reward coding interpretation partially rescues this.
- The link to dopamine is entirely indirect — no VTA recordings or dopaminergic pharmacology were performed in this study.
- It is unclear whether the rate of reverse replay is the functionally meaningful variable, or whether rate changes are a byproduct of reward-triggered initiation (the authors prefer the latter but acknowledge both are possible).
- Remote replays were too infrequent for analysis; the role of remote reverse replay (of non-current locations) in credit assignment is unknown.
- The linear track task minimises planning demands, so the null effect of reward on forward replay may not generalise to more complex environments where planning is adaptive.
- Whether the same directional dissociation holds in 2D environments or tasks requiring active decision making is unknown.

---

### Connections & keywords

**Key citations**:
- Foster and Wilson (2006) — original report of reverse replay and credit assignment hypothesis
- Diba and Buzsáki (2007) — first report of both forward and reverse replay on the linear track
- Singer and Frank (2009) — reward presence modulates SWR rate
- Pfeiffer and Foster (2013) — forward replay predicts upcoming trajectories
- Jadhav et al. (2012) — SWR disruption impairs spatial working memory
- Gomperts et al. (2015) — VTA neurons coordinate with hippocampal replay
- McNamara et al. (2014) — dopamine promotes hippocampal reactivation
- Brzosko et al. (2015) — dopamine converts reverse STDP from LTD to LTP
- Tobler et al. (2005) — adaptive range coding of reward by dopamine neurons
- Sutton and Barto (1998) — reinforcement learning and temporal credit assignment

**Named models or frameworks**:
- Temporal credit assignment (reinforcement learning framework)
- Spike-timing-dependent plasticity (STDP) modified by dopamine
- Bayesian decoding of place cell sequences
- Poisson GLMM (statistical framework)

**Brain regions**:
- Hippocampus CA1
- Ventral tegmental area (VTA)
- CA3-CA1 synapse

**Keywords**:
- hippocampal replay
- sharp-wave ripples (SWRs)
- reverse replay
- forward replay
- place cells
- reward modulation
- temporal credit assignment
- memory consolidation
- awake replay directionality
- dopamine-hippocampus interaction
- adaptive reward coding
- Bayesian sequence decoding
