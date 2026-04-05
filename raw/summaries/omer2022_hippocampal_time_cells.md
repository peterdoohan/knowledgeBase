---
source_file: omer2022_hippocampal_time_cells.md
title: "Contextual and pure time coding for self and other in the hippocampus"
authors: David B. Omer, Liora Las, Nachum Ulanovsky
year: 2022
journal: Nature Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Hippocampal CA1 in bats contains two distinct populations of time cells — contextual time cells that encode time conjunctively with spatial context, and pure time cells that represent elapsed time invariantly across locations — and a separate population encodes elapsed time relative to the actions of another individual.

---

### Background & motivation

The hippocampus is known to encode both space and time, with "time cells" firing transiently at specific moments during temporal gaps in behaviour. Prior work established that time cells undergo "re-timing" across different behavioural contexts, but whether they encode context-dependent time sequences or represent time per se was unclear. Furthermore, nothing was known about whether the hippocampus encodes elapsed time relative to another individual's actions, despite the hippocampus being implicated in social spatial representations. This study addresses both gaps by recording from hippocampal CA1 of freely behaving bats across multiple spatial contexts during a social imitation task.

---

### Methods

- **Species and preparation**: Egyptian fruit bats (*Rousettus aegyptiacus*); observer bat chronically implanted with a four-tetrode microdrive targeting dorsal hippocampal area CA1; wireless neural logger used for continuous recording.
- **Task**: Social observational imitation task. Observer bat watched a demonstrator bat fly to one of two landing balls (A or B) and had to imitate the choice after a variable delay. Both bats were stationary on landing balls during analysed epochs; stationary delay times were highly variable (median ~7.4 s for observer, ~5.7 s for demonstrator).
- **Recording**: 391 well-isolated CA1 neurons recorded across four observer bats; three locations (balls A, B, Start) yielding six alignment conditions (2 bats × 3 locations).
- **Time cell identification**: Neurons were classified as time cells if they showed a statistically significant transient firing in ≥3 consecutive 100-ms bins (shuffle-based test, P < 0.01, Bonferroni-corrected) on at least 40% of trials, providing a stable temporal tuning curve.
- **Key analyses**: Comparison of temporal tuning curves across spatial locations; Δ*T* distributions and Pearson correlation between tuning curves at A vs. B to distinguish contextual vs. pure time cells; Bayesian maximum likelihood decoding of elapsed time; accelerometer-based movement controls; controls for reward delivery timing.

---

### Key findings

- 190/391 recorded CA1 neurons (48.6%) were significant time cells for the observer bat's own landings; time cells formed internally generated firing sequences spanning the 0–8 s behavioural waiting period.
- Two distinct populations of self time cells were identified:
  - **Contextual time cells** (64.7%; 123/190): active in only one spatial location, completely losing temporal tuning in other locations; encode time × spatial context conjunctively.
  - **Pure time cells** (35.3%; 67/190): active in more than one location with similar preferred times across locations; the distribution of preferred-time differences (ΔT) between balls A and B was significantly narrower than three shuffle controls (Ansari–Bradley test P = 3.8×10⁻² to 5.9×10⁻⁵); bimodality of the correlation distribution confirmed by Hartigan's dip test (P = 0.015).
- 61.4% of cells tuned on both A and B had ΔT < 1 s, 2–3× higher than chance.
- Bayesian decoding error was < 0.6 s over the full 8-s range for both subpopulations independently.
- 56/391 neurons (14.3%) were significant **time cells for the other bat** (demonstrator), forming internally generated sequences aligned to the demonstrator's landing; 75% were contextual and ~21% were pure time cells for the other.
- Time cells for self and for other had similar distributions of preferred times (KS test, P = 0.12).
- Temporal tuning was stable across correct (rewarded) and incorrect (non-rewarded) trials (ρ = 0.60, P = 9.8×10⁻¹⁵), ruling out reward-driven firing.
- Accelerometer controls showed no trial-to-trial correlation between movement and spike timing, ruling out movement artifacts.
- Temporal field width scaled with preferred time, consistent with Weber's law.

---

### Computational framework

The paper is empirical and does not formalise a computational model, but it operates within the conceptual framework of **internally generated neural sequences** as a basis for interval timing and episodic memory. The key implicit framework is that populations of sequentially active neurons tile a temporal interval after a triggering event (landing), providing a read-out of elapsed time. This is consistent with a "time cell" population code model: elapsed time is decoded from the current pattern of activity across the ensemble, analogous to how place cells provide a spatial population code.

The distinction between contextual and pure time cells maps loosely onto two levels of temporal abstraction: one context-specific (episodic, conjunctive) and one context-invariant (interval timing). The paper uses Bayesian maximum likelihood decoding to quantify temporal precision, and the ΔT distribution analysis to characterise population-level invariance.

---

### Prevailing model of the system under study

The introduction frames hippocampal time cells as a well-established phenomenon in rodents and humans: neurons fire transiently and sequentially at specific times during behavioural gaps, forming internally generated sequences. The prevailing assumption was that time cells encode context-dependent sequences — i.e., "re-timing" occurs when the context changes (different behaviours, environments, or odours) — and that temporal coding in the hippocampus is fundamentally tied to the specific experience or episode. There was no prior evidence for neurons that purely encode elapsed time independently of context, and nothing was known about whether the hippocampus encodes time relative to another individual's behaviour. The authors also note that, while social spatial representations (social place cells) had been found in rodents, bats and humans, the social dimension of temporal coding was entirely unexplored.

---

### What this paper contributes

The paper makes four advances over the prevailing model:

1. **Two distinct time-cell populations**: It is the first study to demonstrate a bimodal functional organisation within hippocampal time cells — contextual vs. pure — providing the first empirical evidence for neurons that encode elapsed time per se, divorced from spatial context or behavioural sequence.
2. **Location-specific time coding within one environment**: Prior work showed re-timing across different environments or tasks; this paper shows that different spatial locations within the same room are sufficient to dissociate contextual from pure time cells, revealing finer-grained context-dependence.
3. **Pure time cells as a substrate for interval timing**: The existence of neurons with context-invariant preferred times offers a potential neural implementation of scalar timing, consistent with Weber's law for temporal perception.
4. **Time cells for another individual**: Demonstrates for the first time that CA1 encodes temporal sequences aligned to a conspecific's actions, suggesting two reference frames for time (self-triggered and other-triggered) and hinting at a shared neural mechanism for episodic memory of self and other.

---

### Brain regions & systems

- **Hippocampal area CA1 (dorsal)** — primary recording site; proposed locus of both contextual and pure time cell sequences, as well as time cells for the other; also contains overlapping populations of place cells and social place cells.

No other brain regions were recorded from or manipulated.

---

### Mechanistic insight

The paper meets criterion 1 (it implicitly formalises the "time cell sequence" algorithm — internally generated, landmark-triggered sequential firing that tiles a temporal interval) and criterion 2 (it provides single-unit recording data from CA1). It therefore meets the bar for mechanistic insight, though the implementational level is largely absent.

- **Computational**: The brain solves the problem of tracking elapsed time after a salient event (landing), both for self-initiated events and for observed events involving another individual. This supports interval timing perception and the temporal scaffolding of episodic memories (what, where, when).
- **Algorithmic**: Time is represented by the sequential activation of neurons with distinct preferred times, forming a population code for elapsed time. Two distinct coding schemes operate in parallel: a conjunctive time × context code (contextual time cells) that tags memories to specific spatial episodes, and a context-invariant time code (pure time cells) that represents duration abstractly. Both are anchored to a triggering event (landing) rather than to ongoing movement or reward delivery.
- **Implementational**: The paper identifies dorsal CA1 pyramidal neurons as the substrate, using tetrode recordings. Contextual and pure time cells are anatomically intermixed (co-recorded on 75% of tetrodes). Beyond this, the biophysical or circuit-level mechanisms that generate these sequences are not addressed — the paper does not identify specific cell types, connectivity patterns, neuromodulatory inputs, or oscillatory mechanisms driving the sequences.

**Bonus**: No specific cell types or connectivity were identified. The paper rules out sharp-wave ripples as a direct cause of time cell firing and rules out theta-sequence-like periodic mechanisms (time cells fire once per trial).

---

### Limitations & open questions

- The social nature of "time cells for the other" was not fully confirmed: the demonstrator bat could not be replaced by a stationary object for long enough to test whether time cells for other are truly social (object condition abandoned in session 2).
- The distinction between encoding time × spatial context versus time × spatial location could not be resolved — both interpretations are consistent with the contextual time cell data.
- Whether the time cells for the other reflect genuine social temporal representation, replay of self-time sequences triggered by an external cue, or anticipatory coding of self's future landing remains unknown.
- The circuit and biophysical mechanisms generating internally generated time sequences (e.g., the role of recurrent connectivity, entorhinal inputs, neuromodulation) are not addressed.
- The possibility that time cells encode expected reward delivery time (rather than elapsed time per se) was substantially but not definitively ruled out.
- Reward was not given on the start ball, so reward expectation and temporal coding were only partially dissociable.
- Sample sizes are limited (four bats, single hemisphere each); no female animals were used.

---

### Connections & keywords

**Key citations**:
- Pastalkova et al. (2008) *Science* — internally generated hippocampal sequences
- MacDonald et al. (2011) *Neuron* — hippocampal time cells bridging memory gaps
- Eichenbaum (2014) *Nat Rev Neurosci* — time cells review
- Omer et al. (2018) *Science* — social place cells in bat hippocampus
- Danjo et al. (2018) *Science* — spatial representations of self and other in hippocampus
- Heys & Dombeck (2018) *Nat Neurosci* — medial entorhinal time coding during immobility
- Taxidis et al. (2020) *Neuron* — sensory and temporal representations in hippocampal sequences
- Gauthier & Tank (2018) *Neuron* — reward coding in hippocampus

**Named models or frameworks**:
- Time cell population code (internally generated sequences)
- Bayesian maximum likelihood decoding of elapsed time
- Weber's law for interval timing (scalar property of time perception)
- Social observational imitation task

**Brain regions**:
- Hippocampal area CA1 (dorsal)

**Keywords**:
- hippocampal time cells
- contextual time coding
- pure time coding
- interval timing
- internally generated sequences
- social time cells
- episodic memory
- spatial context
- bat hippocampus
- temporal population code
- self vs. other neural representation
- CA1 single-unit recording
