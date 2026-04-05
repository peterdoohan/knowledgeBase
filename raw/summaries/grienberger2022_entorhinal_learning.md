---
source_file: grienberger2022_entorhinal_learning.md
title: "Entorhinal cortex directs learning-related changes in CA1 representations"
authors: Christine Grienberger, Jeffrey C. Magee
year: 2022
journal: Nature
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Entorhinal cortex layer 3 (EC3) provides a target-like instructive signal that drives behavioural timescale synaptic plasticity (BTSP) in hippocampal CA1, producing the reward-site over-representation observed during spatial learning.

---

### Background & motivation

Experience-dependent changes in hippocampal population activity — particularly the over-representation of rewarded locations by place cells — are required for successful spatial learning, but the neural mechanisms producing these changes have been unknown. Synaptic plasticity, generally assumed to be Hebbian, is the canonical explanation, yet no direct physiological account had linked a specific plasticity mechanism to a specific upstream instructive signal. This paper asks what drives the formation of the CA1 reward over-representation and identifies EC3 as the source of the instructive signal.

---

### Methods

- **Task and subjects**: Head-fixed adult mice (GP5.17 and pOxr1-Cre lines) ran on a 180-cm linear treadmill. A habituation day (day 0: blank belt, variable reward) was followed by a learning day (day 1: cue-enriched belt, fixed reward location — "environment A"; or blank belt with a salient visual cue 50 cm before reward — "environment B").
- **CA1 imaging**: Two-photon Ca²⁺ imaging of GCaMP6f-expressing dorsal CA1 pyramidal neurons (n = 18 animals, up to 1,278 place cells per session).
- **EC3 axonal imaging**: Two-photon Ca²⁺ imaging of GCaMP6f-expressing EC3 axons in stratum lacunosum-moleculare of CA1 (n = 792–808 axons, 7–8 animals).
- **Pharmacology**: Local application of NMDA receptor antagonist D-AP5 (50–75 µM) or CaV2.3 blocker SNX-482 (10 µM) to dorsal CA1 to test the role of plateau potentials / BTSP.
- **Optogenetics**: Retrograde AAV strategy to express ArchT specifically in EC3 neurons projecting to the recorded CA1 region (pOxr1-Cre mice); 594-nm light delivered to entorhinal cortex during a ±18 cm zone around the reward.
- **Computational model**: Two-state Markov chains (n = 2,000) simulating EC3 persistent firing; plateau probability in CA1 inferred by thresholding summed EC3 input after subtracting feedforward inhibition.
- **Analysis**: Place cell identification by spatial information content and lap reliability; place field width, induction-lap velocity, and place field peak shift quantified to test for BTSP signatures.

---

### Key findings

- On day 1, CA1 place cell density near the reward site increased more than twofold relative to day 0 (chi-squared test, P = 3.47×10⁻³⁶), alongside elevated spatial information and lap-to-lap reliability.
- Place fields emerged abruptly in single laps (mean ~22.6 laps before onset) and showed hallmarks of BTSP: backward shift of the place field relative to the induction-lap activity location (Kolmogorov-Smirnov test, P = 1.13×10⁻⁷) and place field width proportional to induction-lap velocity (R = 0.990, P = 0.001).
- Local application of D-AP5 or SNX-482 significantly reduced the CA1 reward over-representation (chi-squared test, P = 0.04 for both), confirming BTSP dependence.
- Optogenetic inhibition of EC3 axons projecting to the recorded CA1 region prevented the reward over-representation (P = 8.82×10⁻¹⁹) without altering behavioural measures (licking, running) or mean Ca²⁺ event amplitude.
- EC3 axons showed moderate, stochastic spatial tuning; only ~19% had consistent firing between interleaved laps. Despite uniform spatial distribution across the track, EC3 axons showed elevated tuning and stability near the reward site.
- A Markov-chain model showed that three factors account for the CA1 over-representation: (1) uniform moderate EC3 tuning across the track, (2) enhanced EC3 tuning near the reward site, and (3) increased animal dwell time at the reward. Model with all three elements achieved R = 0.81 with data.
- In environment B (single salient visual cue, no belt cues), EC3 activity showed a ~fourfold increase near the visual cue location, and CA1 place cell density was correspondingly greatest near the cue — confirmed by the model and replicated optogenetically.
- EC3 population activity around the over-representation site remained constant throughout the learning session even as new place field formation declined, indicating a target signal (not error signal) form. By the end of the session, CA1 population activity profile closely matched the stable EC3 profile (CA1–EC3 correlation R = 0.60 in the late session vs. R = –0.13 early).

---

### Computational framework

The paper uses a **target-signal / supervised plasticity** framework inspired by target-propagation ideas. The core formalism is:

- EC3 provides each CA1 pyramidal neuron with a desired (target) activity pattern via excitatory input to the distal apical tuft.
- This target is compared in the apical dendrite with an inhibitory signal representing the actual CA1 population activity (proposed to be carried by OLM interneurons).
- The mismatch (excess excitation) generates dendritic Ca²⁺ plateau potentials.
- Plateau potentials serve as local error signals driving BTSP at CA3 feedforward synapses on each cell individually.
- As CA1 activity approaches the EC3 target, plateau probability decreases and plasticity saturates.

The Markov-chain model is used to capture EC3 persistent firing statistics and predict CA1 plateau probability and place field distribution across space. Key variables: EC3 activation/inactivation transition probabilities (P₀₁, P₁₀), dwell time per spatial bin, plateau threshold, and running speed. The framework assumes: (a) BTSP is the sole relevant plasticity form; (b) the CA1 feedback comparator signal opposes EC3 input; (c) EC3 activity is primarily determined by environmental saliency.

---

### Prevailing model of the system under study

Before this paper, the field understood that the hippocampus forms experience-dependent place cell representations, and that reward-site over-representations are required for spatial learning. Synaptic plasticity was broadly assumed to mediate these changes, but the dominant framework was Hebbian (spike-timing-dependent or rate-based plasticity driven by CA3 and/or entorhinal co-activation). The authors note that BTSP had been described previously as a distinct, plateau-potential-driven, behaviourally timescale plasticity, but its role in forming the reward over-representation in an intact learning animal had not been established. Similarly, EC3 was known to target the distal apical tuft and to regulate plateau probability in vitro and in vivo, but had not been identified as an instructive signal specifically directing hippocampal learning-related representational change. The form of instructive signals driving learning in the hippocampus — error signal versus target signal — was entirely open.

---

### What this paper contributes

The paper establishes a complete causal chain from EC3 activity through BTSP to the CA1 reward over-representation:

1. **BTSP is the mechanism**: Pharmacological blockade of plateaus (SNX-482) and of NMDA receptor-dependent BTSP induction (D-AP5) each significantly reduces the over-representation, and place field properties (abrupt onset, backward shift, velocity-width scaling) match BTSP predictions.
2. **EC3 is necessary**: Optogenetic inhibition of the EC3 projection selectively to the recorded CA1 volume eliminates the reward over-representation, without affecting behaviour.
3. **EC3 provides the instructive signal**: EC3 activity reflects the spatial distribution of salient environmental cues (uniform in environment A, cue-peaked in environment B), predicting where CA1 place cell density will be elevated. The model quantitatively accounts for the observed CA1 distribution from three elements of EC3 activity.
4. **Signal form is target, not error**: EC3 activity remains stable throughout the learning session while CA1 plasticity decreases, establishing EC3 as a target signal rather than an error signal. This distinguishes hippocampal learning from cerebellar or other error-signal-based supervised learning schemes and raises the broader possibility that target-signal-driven learning operates in other brain regions.

---

### Brain regions & systems

- **Hippocampal CA1** — primary site of learning-related representational change; locus of BTSP induction via plateau potentials in distal apical dendrites; CA3 feedforward synapses are the plasticity target.
- **Entorhinal cortex layer 3 (EC3) / medial entorhinal cortex** — source of the instructive target signal; axons project to stratum lacunosum-moleculare of CA1; activity encodes the spatial distribution of salient environmental cues; necessary for CA1 over-representation formation.
- **Stratum lacunosum-moleculare (of CA1)** — the layer where EC3 axons terminate and where plateau potentials are initiated; site of EC3 axonal imaging.
- **Orions lacunosum-moleculare (OLM) interneurons** — proposed (but not directly tested here) to carry feedback representing actual CA1 population activity to the apical tuft comparator.
- **CA3** — feedforward excitatory input to CA1 perisomatic regions; synapses modified by BTSP to shape place cell firing after plateau induction.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Phenomenon**: Spatial learning drives a reward-site over-representation in CA1, implemented through de novo place field formation.

**Computational level**: The brain must construct a spatial map that allocates representational resources to behaviourally relevant locations. The problem is to convert an external environmental signal into a structured hippocampal population code.

**Algorithmic level**: EC3 delivers a target activity pattern to each CA1 pyramidal neuron via its distal apical tuft input. The apical dendrite compares this target against a feedback signal representing current CA1 population activity. When EC3 input exceeds the feedback (i.e., the target is not yet met), a dendritic Ca²⁺ plateau potential is generated. BTSP then modifies CA3 synaptic weights according to an asymmetric, behaviourally-timescale rule, shifting the cell's place field to precede the plateau location and widening it in proportion to running speed. As the CA1 ensemble converges on the EC3 target, plateau probability declines and plasticity saturates. The EC3 signal remains constant (target), and local plateaus serve as cell-specific error signals.

**Implementational level**: EC3 layer 3 neurons (identified via pOxr1-Cre; medial entorhinal cortex) project axons to stratum lacunosum-moleculare and provide large-amplitude, NMDA receptor-rich synaptic input that initiates plateau potentials. Plateau induction is CaV2.3-dependent (blocked by SNX-482) and NMDA-receptor-dependent (blocked by D-AP5). The feedback comparator signal source is unresolved but OLM interneurons are proposed. EC3 neurons show two-state persistent firing (modelled as Markov chains), consistent with prior literature on graded persistent activity in entorhinal cortex.

**Bonus — implementation details**: Cell type (EC3 projection neurons, CA1 pyramidal cells), the CaV2.3 channel as the plateau mechanism, NMDA receptors for BTSP induction, and the projection anatomy (stratum lacunosum-moleculare vs. perisomatic CA3 targeting) are all specified. The OLM feedback pathway remains a hypothesis.

---

### Limitations & open questions

- The feedback signal that conveys actual CA1 population activity to the apical tuft comparator is not identified; OLM interneurons are proposed but not tested.
- How EC3 neurons acquire their environmentally specific target activity pattern is unknown; the paper notes this as a key open question.
- The optogenetic manipulation affects a subset of EC3 projection neurons (those projecting to the imaged CA1 volume), so the full contribution of EC3 may be underestimated, and off-target effects cannot be fully excluded.
- Pharmacological manipulations (D-AP5, SNX-482) are local but not cell-type-specific; effects on interneurons or other elements cannot be ruled out.
- The model uses a fixed threshold and simplified feedforward inhibition; the relationship between model parameters and actual biophysical quantities is qualitative.
- All experiments are in head-fixed mice on a linear track; generalisation to freely moving animals and 2D environments is assumed but untested.
- Whether the same EC3-BTSP mechanism applies to other types of hippocampal learning (non-spatial, temporal association, etc.) is open.

---

### Connections & keywords

**Key citations**:
- Bittner et al. (2017) *Science* — original BTSP paper
- Milstein et al. (2021) *eLife* — bidirectional BTSP
- Bittner et al. (2015) *Nature Neuroscience* — EC3 input regulates plateau probability
- Grienberger et al. (2017) *Nature Neuroscience* — inhibitory suppression in CA1 place cells
- Magee & Grienberger (2020) *Annual Review of Neuroscience* — review of synaptic plasticity forms
- Dupret et al. (2010) *Nature Neuroscience* — reward over-representation required for spatial learning
- Turi et al. (2019) *Neuron* — VIP interneurons in spatial learning
- Cholvin et al. (2021) *Neuron* — entorhinal inputs converted to stable hippocampal maps
- Sacramento et al. (2018) *NeurIPS* — dendritic microcircuits approximate backpropagation
- Enikolopov et al. (2018) *Neuron* — target signals driving plasticity in electric fish

**Named models or frameworks**:
- Behavioural timescale synaptic plasticity (BTSP)
- Two-state Markov chain model of EC3 persistent firing
- Target-signal framework (contrasted with error-signal frameworks)
- Dendritic comparator / target propagation framework (Sacramento et al.)

**Brain regions**:
- Hippocampal CA1
- Entorhinal cortex layer 3 (EC3) / medial entorhinal cortex
- Stratum lacunosum-moleculare
- CA3
- OLM (oriens lacunosum-moleculare) interneurons

**Keywords**:
- behavioural timescale synaptic plasticity (BTSP)
- CA1 place cell over-representation
- dendritic plateau potentials
- entorhinal cortex layer 3 instructive signal
- target signal vs. error signal learning
- spatial reward learning
- two-photon calcium imaging
- optogenetic circuit dissection
- Markov chain model of persistent firing
- CaV2.3 plateau initiation
- hippocampal map formation
- supervised synaptic plasticity
