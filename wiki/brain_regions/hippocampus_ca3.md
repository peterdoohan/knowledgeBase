# Hippocampus CA3

## Current understanding

The CA3 subregion of the hippocampus functions as an auto-associative network critical for pattern completion and sequence generation during replay events. CA3 pyramidal cells receive recurrent collateral connections from other CA3 neurons, creating attractor dynamics that support bidirectional sequence reactivation. Symmetric spike-timing-dependent plasticity (STDP) at CA3-CA3 synapses provides a mechanistic basis for reverse replay generation, enabling backward propagation of activity despite forward-directed experience.

---

## Key evidence

- Symmetric spike-timing-dependent plasticity (STDP) at CA3-CA3 synapses explains how reverse replay can emerge despite forward-directed experience, with attractor network dynamics in auto-associative CA3 networks supporting bidirectional sequence reactivation ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Mishra et al. (2016) demonstrated symmetric STDP in CA3; proposed as mechanism for reverse replay generation.

- The "preplay" phenomenon—where ripple sequences before novel experience match subsequent place cell firing order—remains controversial; while Dragoi & Tonegawa (2011) reported preplay suggesting pre-configured maps, subsequent studies found no evidence when controlling for experience-dependent plasticity, leading Grosmark & Buzsáki (2016) to propose a hybrid model with "rigid" pre-configured cells and "plastic" experience-dependent cells in CA3 ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)).

- CA3 hippocampal ensembles in rats transiently represent spatial locations ahead of the animal — sweeping forward along each potential path one at a time — during pauses at high-cost decision points, in a brain state characterised by theta and gamma oscillations rather than sharp-wave ripples. ([Johnson 2007](../../raw/summaries/johnson2007_hippocampus_decision.md))

- Decoded representations in CA3 sweep preferentially forward of the animal (not behind); the probability mass in front significantly exceeded that behind in all sessions (sign-rank test, p < 10⁻¹⁰). ([Johnson 2007](../../raw/summaries/johnson2007_hippocampus_decision.md))

- CA3 sweeps encode each arm separately in sequence — the joint probability of representing both arms simultaneously was near zero, indicating the representation samples one future path at a time. ([Johnson 2007](../../raw/summaries/johnson2007_hippocampus_decision.md))

- Similar forward sweeps in CA3 were observed during error correction (when the rat reversed on the wrong arm), with the representation sweeping to the unchosen correct arm. ([Johnson 2007](../../raw/summaries/johnson2007_hippocampus_decision.md))

- LFPs at the choice point showed strong theta (7 Hz) and gamma (30–80 Hz) power but no sharp-wave ripple activity — contrasting with feeder sites, which showed replay during sharp-wave ripples. ([Johnson 2007](../../raw/summaries/johnson2007_hippocampus_decision.md))

- Sweep stop times in CA3 aligned significantly to the rising phase of theta (Watson's U² = 0.52, p < 0.0001). ([Johnson 2007](../../raw/summaries/johnson2007_hippocampus_decision.md))

- On the multiple-T task, forward sweeps and time spent at the choice point decreased across laps as behaviour automated. On the cued-choice task, non-local activity was maintained throughout the session, consistent with continued moment-to-moment deliberation. ([Johnson 2007](../../raw/summaries/johnson2007_hippocampus_decision.md))

---

## History of ideas

The CA3 region has long been hypothesized to serve as an auto-associative network capable of pattern completion, based on its extensive recurrent collateral connectivity. The discovery of reverse replay by Foster and Wilson (2006) posed a mechanistic puzzle: how can sequences activate in reverse order when experience drives plasticity in the forward direction? The discovery of symmetric STDP in CA3 by Mishra et al. (2016) provided a resolution—bidirectional synaptic plasticity rules enable both forward and reverse sequence propagation in the same network.

The preplay controversy highlighted the complex interplay between pre-configured network dynamics and experience-dependent plasticity in CA3. Initial reports of preplay by Dragoi and Tonegawa (2011) suggested that hippocampal sequences might be largely pre-configured, with experience merely selecting from existing patterns. However, subsequent work by Silva et al. (2015) found no evidence for preplay when controlling for prior experience, suggesting that apparent preplay may reflect rapid, experience-dependent plasticity. Grosmark and Buzsáki (2016) proposed a hybrid model in which "rigid" cells with pre-configured connectivity participate in pre-experience replay, while "plastic" cells are incorporated via experience-dependent mechanisms.

---

## Open questions

- What proportion of CA3 cells are "rigid" versus "plastic" in the Grosmark & Buzsáki model?
- How do cholinergic and dopaminergic inputs modulate the balance between rigid and plastic cell contributions to replay?
- What is the precise role of CA3-CA1 feedforward connections in shaping replay content?
- Do the symmetric STDP rules in CA3 differ between different cell types or subregions?

---

## Related pages

- [[hippocampal_replay]]
- [[reverse_replay]]
- [[forward_replay]]
- [[place_cells]]
- [[sharp_wave_ripples]]
- [[attractor_networks]]
- [[hippocampus]]
- [[hippocampus_ca1]]
