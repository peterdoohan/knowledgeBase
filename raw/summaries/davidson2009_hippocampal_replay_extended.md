---
source_file: davidson2009_hippocampal_replay_extended.md
title: "Hippocampal Replay of Extended Experience"
authors: Thomas J. Davidson, Fabian Kloosterman, Matthew A. Wilson
year: 2009
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Hippocampal CA1 place cell ensembles in awake rats replay long behavioral sequences (up to ~7 m) at a characteristic virtual speed of ~8 m/s, spanning trains of multiple sharp-wave ripple events, and can be initiated from locations remote from the animal's current position.

---

### Background & motivation

Place cells in the hippocampus fire in sequence as a rat traverses space, and during pauses in locomotion these sequences are "replayed" in compressed form coincident with sharp-wave ripple (SWR) oscillations. Prior studies used small (1–2 m) linear tracks where the full place-cell sequence fits within a single ripple event (~50–120 ms). It was unknown whether the hippocampus could support replay of much longer trajectories as encountered in natural foraging, and if so, how long sequences would be mapped onto the brief time windows of ripple events. This paper addresses the spatial scale, temporal structure, and directional properties of awake replay in a large environment.

---

### Methods

- **Subjects**: 4 male Long-Evans rats (one of five excluded due to poor position estimation).
- **Environment**: A 10.3 m linear track; food reward at both ends; animals not pretrained, yielding variable behavior with frequent pauses.
- **Recordings**: Simultaneous multi-tetrode/octrode recordings of CA1 single units (23–47 spatially tuned units per rat) plus hippocampal LFP.
- **Behavioral classification**: Movement epochs classified as RUN (>15 cm/s) or STOP (<5 cm/s); candidate replay events identified as multiunit activity (MUA) peaks during STOP.
- **Neural decoding**: Bayesian position reconstruction (Zhang et al., 1998) applied in 20 ms non-overlapping windows during candidate events, yielding a probability distribution over linearized track position. Direction of running (A/B vs B/A) decoded jointly from place-by-direction tuning curves.
- **Replay detection**: A line-finding algorithm (Radon transform) identified the best-fit constant-velocity trajectory in decoded position space. Statistical significance assessed against three shuffles (column-cycle, unit identity, pseudoevent) at Monte Carlo p < 0.01 under all three shuffles.
- **Replay order scoring**: A "replay order score" compared estimated running direction with the physical direction of the replayed trajectory to classify events as forward, reverse, or mixed.
- **Ripple detection**: Band-pass filtered LFP (150–250 Hz), Hilbert amplitude envelope; individual ripple peaks detected at >2.5 SD above mean.

---

### Key findings

- 16% of all candidate events and 33% of long (>250 ms) events contained significant replay trajectories (p < 10^-7 per rat under a binomial test assuming 1% false-positive rate).
- Replayed trajectory length was linearly correlated with event duration (R² = 0.59, slope = 11.1 m/s); median replay speed was 8.1 m/s across all rats, 15–20 times faster than typical running speed (~0.5 m/s).
- Extended replay events (up to ~700 ms, covering up to ~7 m) spanned trains of multiple sharp-wave ripples; number of ripples strongly correlated with event duration (R² = 0.56, ~9.9 ripples/s).
- Reconstruction quality (position estimate mode) and trajectory fidelity (replay line error) were significantly better at ripple peak times than at inter-ripple times, indicating that replay is organized as chains of ripple-associated subsequences.
- 40% of significant replay trajectories were forward-ordered and 26% were reverse-ordered (remainder "mixed"); forward replay was significantly more common (p < 0.005).
- 40% of trajectories started locally (within 50 cm of animal; chance = 17%, p < 0.0005); 20% were robustly "remote" (starting >1 m away and proceeding toward the animal without passing it), far exceeding expected false-positive rate (p < 10^-11).
- Neither forward nor reverse locally initiated replay preferentially represented the animal's actual upcoming or previously taken path when stopped mid-track.
- No significant difference in speed between forward and reverse replay (8.6 vs 7.9 m/s, p = 0.24).

---

### Computational framework

The core analytical framework is **Bayesian neural decoding** (population vector reconstruction). The decoding model assumes that the probability of observing a spike count vector given position (and direction) is given by a Poisson likelihood based on pre-estimated tuning curves, and applies Bayes' theorem to invert this to a posterior over position. Formally: P(x | spikes) ∝ P(spikes | x) · P(x), where P(spikes | x) is a product of Poisson terms over all recorded units. Replay is then defined as a constant-velocity trajectory through the decoded position space, detected by maximizing a replay score (mean posterior probability along the best-fit line) using a Radon-transform-based line-finding algorithm.

The paper does not develop a mechanistic computational model of replay generation per se, but briefly considers two candidate circuit mechanisms: (1) sweeping release of inhibition within a single ripple producing one subsequence (~50 cm), repeated via hippocampal-entorhinal re-entrant loops; (2) continuous operation of a CA3 autoassociative network.

---

### Prevailing model of the system under study

Before this paper, hippocampal awake replay had been characterized primarily on short (1–2 m) linear tracks. The prevailing model was that a single sharp-wave ripple event (~50–120 ms) was sufficient to re-express the full sequence of a traversed environment in compressed form. The biophysical model proposed that sensory inputs drive place cell excitability, and a sweeping inhibitory release during a ripple "reads out" the stored sequence. A key implication of this model was that replay should be spatially constrained to regions that fit within a single ripple — i.e., small spatial scales. Replay was thought to begin at or near the animal's current location, anchored by strong local inputs. Forward replay had been linked to prospective path evaluation and reverse replay to retrospective evaluation of the path just taken.

---

### What this paper contributes

This paper establishes that the hippocampus can replay behavioral sequences far longer than previously demonstrated, spanning up to ~7 m of a 10 m track. This extends the known spatial scale of replay by at least 3–5-fold relative to prior work. Key conceptual advances:

1. **Ripple train organisation**: Extended replay is not a prolonged single ripple but a chain of ripple-associated subsequences, each ~50 cm in extent, linked across multiple ripple events. This provides the first functional interpretation of ripple trains.
2. **Remote initiation**: A substantial fraction (~20%) of replay events begin at locations remote from the animal, demonstrating that awake hippocampal replay is not exclusively driven by local sensory inputs and can access stored sequences independent of current position — previously thought to be a property only of sleep replay.
3. **Constant virtual speed**: Replay proceeds at a fixed ~8 m/s regardless of the animal's actual behavioral speed or trajectory, implying that sequential structure (not timing details of individual episodes) is what is re-expressed.
4. **No strong prospective/retrospective path selectivity**: Locally initiated forward and reverse replay did not preferentially represent the actual upcoming or past path, suggesting replay expresses the set of possible paths associated with the current location rather than encoding what the animal actually did or will do.

---

### Brain regions & systems

- **Hippocampal area CA1**: Primary recording site. Source of place cell sequences and sharp-wave ripples. Locus of replay events characterised in this study.
- **CA3** (discussed but not recorded): Proposed as site of autoassociative network that could sustain extended replay via recurrent connectivity.
- **Entorhinal cortex** (discussed but not recorded): Proposed as relay in re-entrant hippocampal-entorhinal loops that could concatenate ripple-associated subsequences into extended replay.
- **Neocortex** (referenced in discussion): Discussed as potential source of cortical inputs that could bias or cue remotely initiated replay, especially during slow-wave sleep up-states.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight:

1. **Algorithm**: The paper formalises a concrete algorithmic account — extended replay consists of chains of ripple-associated subsequences (~50 cm each), each generated within a single sharp-wave ripple, and strung together across ripple trains. The constant-speed trajectory at ~8 m/s with integrity peaks locked to individual ripple events is the core evidence for this chain-of-subsequences structure.
2. **Neural data**: Multi-electrode CA1 recordings with LFP ripple detection directly support this account — reconstruction quality and trajectory fidelity are significantly higher at ripple peak times than at inter-ripple intervals within the same extended event (mode of position estimate: 0.32–0.41 vs 0.20–0.26; replay line error: 87–131 cm vs 182–227 cm at ripple vs non-ripple times, p < 0.003 for each rat).

Mapped onto Marr's levels:

- **Computational**: The brain is re-expressing stored sequential spatial experience at high speed during pauses, potentially for memory consolidation, prospective/retrospective evaluation of possible paths, or memory recall.
- **Algorithmic**: Each ripple event replays a ~50 cm spatial subsequence of the stored trajectory (corresponding to ~60 ms at 8 m/s); successive ripples within a train carry successive subsequences, collectively reconstituting the full extended sequence. The decoded position and direction estimates reveal this chain structure directly.
- **Implementational**: The paper provides evidence at the level of CA1 population spiking and LFP ripples. Two candidate mechanisms are discussed but not tested: (1) re-entrant hippocampal-entorhinal loops feeding back CA1 output to drive the next subsequence; (2) CA3 autoassociative dynamics. Specific cell types, interneuron circuitry, or neuromodulatory mechanisms are not addressed.

---

### Limitations & open questions

- Only one recording session per animal was analyzed; generalisability across sessions and environments is uncertain.
- The study is purely observational — no causal manipulation of replay (e.g., ripple disruption) was performed, so the functional role of extended replay remains speculative.
- The mechanism generating ripple trains and linking successive subsequences is unknown; re-entrant entorhinal loops and CA3 autoassociation are proposed but untested.
- Rats were not pretrained and showed variable behavior, limiting the ability to relate replay to specific task demands or learning.
- Remote replay could theoretically be influenced by visual cues (the full track was visible), making it unclear whether remote initiation reflects purely internally generated memory access or sensory cueing.
- No strong path selectivity was found for locally initiated forward/reverse replay; the authors note this may reflect task limitations (not enough path choice pressure) and that more cognitively demanding tasks are needed.
- The link between awake extended replay and specific cognitive functions (consolidation, planning, recall) remains speculative.

---

### Connections & keywords

**Key citations**:
- Foster & Wilson (2006) — reverse awake replay on linear track
- Diba & Buzsaki (2007) — forward and reverse hippocampal sequences during ripples
- Lee & Wilson (2002) — SWS memory replay
- Ji & Wilson (2007) — coordinated hippocampal-cortical replay during sleep
- Wilson & McNaughton (1993, 1994) — hippocampal ensemble coding and sleep reactivation
- Zhang et al. (1998) — Bayesian neural decoding framework
- Buzsaki et al. (1992) — hippocampal high-frequency oscillations
- Johnson & Redish (2007) — vicarious trial-and-error / CA3 forward sweeps at decision points

**Named models or frameworks**:
- Bayesian position reconstruction (Zhang et al., 1998)
- Radon transform line-finding (Toft, 1996) for replay detection
- Sharp-wave ripple (SWR) model of sequence replay
- Chain-of-subsequences model of extended replay (proposed here)
- CA3 autoassociative network (August & Levy, 1999)

**Brain regions**:
- Hippocampal area CA1
- CA3
- Entorhinal cortex
- Neocortex (discussed)

**Keywords**:
- hippocampal replay
- place cells
- sharp-wave ripple
- neural decoding
- Bayesian reconstruction
- awake replay
- forward replay
- reverse replay
- memory consolidation
- spatial sequence compression
- ripple train
- remote replay
