---
source_file: mehta2000_hippocampal_receptive_fields.md
title: Experience-Dependent Asymmetric Shape of Hippocampal Receptive Fields
authors: Mayank R. Mehta, Michael C. Quirk, Matthew A. Wilson
year: 2000
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Hippocampal CA1 place fields on linear tracks are negatively skewed and become progressively more asymmetric with experience, a result consistent with — and modelled by — NMDA-dependent temporally asymmetric LTP/LTD of feedforward CA3→CA1 synapses.

---

### Background & motivation

Hippocampal place cells fire selectively when a rat occupies a particular region of space, and prior work had shown that place field size and location change with experience. However, the shape of receptive fields had been assumed to be symmetric, and no study had systematically characterised the skewness of place fields or asked whether shape itself changes with experience. Understanding receptive field shape is important because it may reveal the computational signature of underlying plasticity mechanisms and could encode information about the sequential structure of an animal's trajectory.

---

### Methods

- **Subjects**: Three male Long-Evans rats implanted with 12-tetrode microdrive arrays.
- **Task**: Animals ran back and forth on a linear track (150 cm) and then a C-shaped track (150 cm) for food rewards; analysis restricted to passes away from reward locations.
- **Recordings**: 173 place fields from 142 putative CA1 pyramidal cells across 7 sessions.
- **Key measures**: Spatial skewness (third moment of the firing-rate distribution), firing-rate asymmetry index (FRAI; ratio of mean firing rate in second vs. first half of spikes per pass), and lap-by-lap tracking of both measures.
- **Controls**: Behavioural asymmetry index (BAI) computed to rule out asymmetric running behaviour; occupancy distributions verified to be symmetric.
- **Environment switch**: A subset of 20 cells active on both tracks was used to test whether skewness resets upon entering a new environment.
- **Computational model**: Feedforward CA3→CA1 network with biophysical Ca²⁺ dynamics, spike-frequency adaptation, theta-modulated inhibition, and a spike-timing-dependent plasticity (STDP) rule (Markram et al. 1997; Bi and Poo, 1998) applied lap by lap.

---

### Key findings

- 73% of place fields had negative skewness (mean = −0.36 ± 0.12); 78% had negative FRAI (mean = −0.15 ± 0.016), meaning firing rate was on average 35% higher in the second half of a pass through a field.
- Place fields were approximately symmetric at the start of a session; skewness increased ~3-fold (312% change) and FRAI increased ~3.5-fold (354% change) over 17 laps — an order of magnitude larger than experience-dependent changes in field size (51%) or location shift (8.2 cm backward).
- Skewness was reset to near-zero when rats entered a second familiar track, confirming the effect is experience- rather than time-dependent.
- Lap-by-lap fluctuations in skewness correlated with spatial parameters (first spike location, field width) but not with temporal/activity-dependent parameters (spike count, firing rate, spiking duration).
- The computational model reproduced: (1) negative skewness emerging within ~5 laps, (2) larger backward shift of the first spike than the last spike, (3) the pattern of correlations between skewness and spatial vs. temporal variables, and (4) progressive widening of place fields.
- Place field peak location shifted backward by 5.5 cm and field width increased by 7.9 cm, consistent with a shape change dominating previously reported center-of-mass shifts.

---

### Computational framework

The paper employs a **spike-timing-dependent plasticity (STDP)** framework instantiated in a feedforward network. The core formalism is:

- Each CA3→CA1 synapse is updated after every lap according to: ds ∝ ∫∫ f_CA3(t) · f_CA1(t') · K(t − t') dt dt', where K is an asymmetric kernel (positive for pre-before-post, negative for post-before-pre) with time constant τ_ltp = τ_ltd = 10 ms; A_ltp = 0.0006, A_ltd = 0.9 A_ltp.
- The CA1 neuron is modelled with firing-rate dynamics incorporating spike-frequency adaptation via intracellular Ca²⁺ and receives theta-modulated sinusoidal inhibition at 8 Hz.
- 100 CA3 place cells with symmetric Gaussian fields (30 cm width) are uniformly distributed; the rat traverses a 200 cm track at 50 cm/s.
- The key assumption is that NMDA-dependent LTP strengthens synapses from CA3 neurons whose fields precede the CA1 field, and LTD weakens synapses from CA3 neurons whose fields follow — breaking the initial symmetry.

---

### Prevailing model of the system under study

Before this paper, hippocampal place fields were generally modelled and analysed as symmetric (e.g., Gaussian) spatial tuning curves. Experience-dependent plasticity was understood to change place field size and the location of the field's centre of mass (Mehta et al., 1997), and theoretical models (Blum and Abbott, 1996; Tsodyks et al., 1996; Jensen and Lisman, 1996) had shown that asymmetric recurrent connections within CA3 could produce predictive shifts and underlie theta phase precession. The dominant mechanistic story placed the locus of plasticity-driven changes within CA3 recurrent circuits. CA1 was treated as a relatively passive readout of CA3 output, and its place fields were assumed to be symmetric in shape at any given moment.

---

### What this paper contributes

This paper establishes that place field shape — specifically skewness — is the dominant experience-dependent variable in CA1, changing an order of magnitude more than size or location. It demonstrates that field asymmetry can arise from a purely feedforward CA3→CA1 mechanism driven by STDP, without requiring asymmetric recurrent connections in CA3. This repositions CA1 as an active site of plasticity-driven computation rather than a passive relay, and provides a direct mechanistic account linking NMDA-dependent LTP/LTD kinetics to the observed field dynamics. Additionally, it proposes that negatively skewed fields could directly generate theta phase precession through a monotonic increase in excitatory drive — an alternative to CA3-based phase precession models. The reset of skewness across environments suggests a role for skewness as a neural correlate of short-term familiarity with a spatial sequence.

---

### Brain regions & systems

- **Hippocampus CA1** — primary recording site; locus of the experience-dependent skewness changes; proposed site of STDP-driven feedforward plasticity.
- **Hippocampus CA3** — source of excitatory feedforward input to CA1 via Schaffer collaterals; modelled as providing symmetric initial input whose STDP-modified projections drive CA1 field asymmetry.
- **Subiculum** — mentioned in passing: subicular place fields are wider than CA1, consistent with the model's prediction that downstream fields should be broader due to cumulative LTP.

---

### Mechanistic insight

The paper meets both criteria for a mechanistic insight entry.

1. **Algorithm formalised**: STDP of CA3→CA1 feedforward synapses is formalised as a biophysical learning rule with specific asymmetric time constants, coupled to a firing-rate model with spike-frequency adaptation and theta inhibition.
2. **Neural data supporting the algorithm**: CA1 single-unit recordings in behaving rats demonstrate the predicted signature — progressive negative skewness, larger shift of the first spike than the last, and correlation of skewness with spatial rather than temporal variables — all replicated quantitatively by the model.

**Marr's three levels:**

- **Computational**: The brain must encode the sequential structure of visited locations so that an animal can predict upcoming positions and navigate efficiently. The hippocampus builds a predictive spatial representation by storing the order in which locations were encountered.
- **Algorithmic**: Repeated unidirectional traversal activates CA3 and CA1 place cells in temporal sequence. STDP strengthens CA3→CA1 synapses where CA3 precedes CA1 (LTP) and weakens those where CA3 follows CA1 (LTD). Over laps, the synaptic weight matrix comes to reflect the temporal asymmetry of the LTP curve, producing an increasingly negatively skewed CA1 firing profile. The skewness of the field represents cumulative familiarity with the sequence.
- **Implementational**: NMDA receptor-dependent LTP/LTD at CA3→CA1 Schaffer collateral synapses (confirmed in prior literature); spike-frequency adaptation via Ca²⁺-activated currents shapes the baseline (positively skewed) response before experience. The paper does not provide direct synaptic measurements during behaviour, and the NMDA-dependence of the skewness effect is a model prediction awaiting pharmacological validation.

**Bonus**: The paper connects the implementational level to specific receptor kinetics (NMDA-dependent Ca²⁺ dynamics) and to the theta oscillation (8 Hz inhibition), though these are modelled rather than directly manipulated in the neural data.

---

### Limitations & open questions

- The NMDA-dependence of the skewness changes is a key model prediction but was not tested pharmacologically in this study; the paper notes that Kentros et al. (1998) found place fields relatively insensitive to NMDA blockade during random foraging, but predicts the effect would appear on directional linear-track tasks.
- Only three rats were used; the generality of the findings is not assessed across species, sexes, or different track geometries beyond linear and C-shaped tracks.
- The resetting of skewness overnight (when rats return to the home cage and presumably replay sequences in a different order) is proposed but not directly tested.
- The model assumes a feedforward-only architecture; the possible contribution of asymmetric recurrent CA3 connections or entorhinal inputs is not ruled out.
- The relationship between skewness and theta phase precession is proposed qualitatively but not tested with simultaneous LFP recordings in this dataset.
- It is unclear whether the observed asymmetry generalises to two-dimensional open-field environments; all data come from one-dimensional tracks.

---

### Connections & keywords

**Key citations**:
- Mehta, Barnes, McNaughton (1997) — prior experience-dependent place field expansion study
- Blum and Abbott (1996) — CA3 recurrent STDP model of place field shifts
- Tsodyks et al. (1996) — asymmetric CA3 connections and phase precession
- Jensen and Lisman (1996) — CA3 sequence prediction and phase precession
- Markram et al. (1997); Bi and Poo (1998); Zhang et al. (1998) — STDP rules
- O'Keefe and Dostrovsky (1971) — original place cell discovery
- Wilson and McNaughton (1993) — ensemble coding of space
- O'Keefe and Recce (1993) — theta phase precession
- Kentros et al. (1998) — NMDA blockade and place field stability
- McHugh et al. (1996) — CA1-specific NMDAR1 knockout and spatial representation

**Named models or frameworks**:
- Spike-timing-dependent plasticity (STDP)
- Hebbian / NMDA-dependent LTP/LTD
- Theta phase precession (O'Keefe and Recce model)
- Feedforward CA3→CA1 network model

**Brain regions**:
- Hippocampus CA1
- Hippocampus CA3
- Subiculum

**Keywords**:
- place cells
- place field asymmetry
- receptive field skewness
- spike-timing-dependent plasticity (STDP)
- NMDA-dependent LTP/LTD
- experience-dependent plasticity
- theta phase precession
- firing rate asymmetry index (FRAI)
- CA3→CA1 feedforward synapses
- sequence learning
- spatial memory
- hippocampal map
