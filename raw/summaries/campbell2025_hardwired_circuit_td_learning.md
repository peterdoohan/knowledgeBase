---
source_file: campbell2025_hardwired_circuit_td_learning.md
paper_id: campbell2025_hardwired_circuit_td_learning
title: "A hardwired neural circuit for temporal difference learning"
authors:
  - "Malcolm G. Campbell"
  - "Yongsoo Ra"
  - "Zhiqin Chen"
  - "Shudi Xu"
  - "Mark Burrell"
  - "Sara Matias"
  - "Mitsuko Watabe-Uchida"
  - "Naoshige Uchida"
year: 2025
journal: "bioRxiv (preprint)"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - calcium_imaging
  - optogenetics
  - electrophysiology
  - neuropixels
brain_regions:
  - striatum
  - dorsomedial_striatum
  - dorsolateral_striatum
  - nucleus_accumbens
  - ventral_tegmental_area
frameworks:
  - reinforcement_learning
  - temporal_difference_learning
keywords:
  - temporal_difference_learning
  - dopamine_reward_prediction_error
  - d1_medium_spiny_neurons
  - nucleus_accumbens
  - temporal_discounting_discount_factor_gamma
  - linear_time_invariant_systems
  - biphasic_impulse_response
  - antidromic_optotagging
  - neuropixels_electrophysiology
  - grabda3m_dopamine_photometry
  - patterned_optogenetic_stimulation
  - hardwired_neural_circuit
  - hardwired
  - neural
  - circuit
  - temporal
  - difference
  - learning
key_citations:
  - jeong2022_mesolimbic_dopamine_causal
  - schultz1997_neural_substrate_reward_pred
---

### One-line summary

Optogenetic stimulation of nucleus accumbens D1 medium spiny neurons drives VTA dopamine neurons via a hardwired biphasic linear filter that computes a temporal difference, demonstrating that TD error calculations are built into the dopamine-striatum microcircuit and that the temporal discount factor gamma is set by the balance of excitatory and inhibitory components of this pathway.

---

### Background & motivation

Midbrain dopamine neurons signal reward prediction errors (RPEs) that closely resemble the temporal difference (TD) error term in reinforcement learning, but the circuit mechanisms by which TD error-like activity arises in dopamine neurons have remained unknown. A leading hypothesis holds that bidirectional interactions between dopamine neurons and the striatum — particularly via D1 and D2 medium spiny neurons (MSNs) — generate these signals, but this had never been directly tested experimentally. Two obstacles have prevented progress: natural reward tasks engage learning processes brain-wide, confounding the specific contributions of dopamine-striatum loops, and dopamine neuron diversity complicates interpretation. This paper addresses both obstacles by using optogenetic stimulation as an artificial, controllable reward signal to isolate the dopamine-lNAc circuit in isolation.

---

### Methods

- **Species and subjects**: Head-fixed mice (n = 74 total; multiple transgenic lines including DAT-Cre, DAT-Flp, Tac1-Cre, A2a-Cre and combinations thereof).
- **Opto-conditioning task**: Odor CS+/CS- paradigm in which optogenetic stimulation of VTA dopamine axons in lNAc (ChrimsonR, calibrated to 8 µL water reward via GRABDA3m photometry) substituted for natural reward; mice trained for up to 30 days.
- **Neural recordings**: Fiber photometry of lNAc dopamine release (GRABDA3m), calcium imaging of lNAc D1-MSNs and D2-MSNs (GCaMP8m), and large-scale Neuropixels electrophysiology with antidromic optotagging of lNAc-projecting VTA dopamine neurons and orthodromic optotagging of lNAc D1-MSNs.
- **Open-loop D1 stimulation experiment**: Seven graded optogenetic stimulation patterns (step, ramp-up, ramp-down, and varying frequency pulse trains) delivered to lNAc D1-MSNs (ChrimsonR in Tac1-Cre mice) while simultaneously recording D1-MSN spiking (Neuropixels), lNAc dopamine release (GRABDA3m photometry), and lNAc-projecting VTA dopamine neuron spiking (antidromic optotagging, Neuropixels 2.0).
- **LTI systems analysis**: Linear time-invariant (LTI) systems identification used to estimate the transfer function (impulse response / filter) from D1-MSN activity to dopamine release, with model order selection to compare TD vs. pure derivative models; gamma extracted from the model zero via gamma = e^(-sigma).
- **Multi-region experiment**: D1-MSNs stimulated in lNAc, dorsomedial striatum (DMS), and dorsolateral striatum (DLS) independently, with dopamine photometry recorded at all three sites.
- **Muscimol inactivation**: lNAc inactivated (muscimol vs. saline, alternating days) in mice trained on a natural-reward classical conditioning task while recording VTA dopamine neuron calcium (GCaMP6f, somatic; n = 6 mice).
- **Behavioral monitoring**: Face/body video motion energy analysis to control for movement-related confounds.

---

### Key findings

- **Opto-conditioning generates TD error-like dopamine signals**: After training, lNAc-projecting dopamine neurons developed the three canonical TD RPE signatures — cue response to CS+ (mean z-score difference CS+–CS- = +0.13 ± 0.04, P = 0.0017), omission dip at expected-but-absent stimulation (mean z-score difference = -0.19 ± 0.05, P = 0.00054), and expectation-dependent suppression of stimulation response (predicted vs. unpredicted: 17.13 vs. 19.52 %dF/F, P = 0.0051).
- **D1-MSNs acquire a value-like signal; D2-MSNs do not**: lNAc D1-MSN calcium responses to odors were selectively potentiated by the CS+ over training (mean z-score difference = +0.62 ± 0.25, marginally significant, P = 0.0504 in D1 mice; not significant in D2 mice, P = 0.84). The signal was value-like (persistent, not locked to dopamine release itself).
- **D1-MSN stimulation drives dopamine via a TD transformation**: When D1-MSNs were stimulated with 7 patterned inputs, dopamine responses qualitatively matched TD error predictions including a negative steady-state response (distinguishing TD from a pure derivative), while D1-MSN activity itself faithfully tracked stimulation patterns. LTI model fit: CV R^2 = 0.81 (D1-MSNs to dopamine release), 0.69 (D1-MSNs to dopamine neuron spiking).
- **TD model outperforms pure derivative**: An order-1 TD LTI model significantly outperformed a derivative-constrained model (gamma = 1) for both photometry and single-unit data (P < 0.001 for single neurons, n = 55).
- **Temporal discount factor gamma extracted**: Bootstrapped median gamma from optotagged dopamine neurons was 0.53 discount/sec, closely matching an independent behavioral estimate of 0.56 discount/sec from Masset et al. 2025.
- **Gamma is linked to the P/N ratio**: The ratio of the positive to negative area of the biphasic impulse response (P/N) is mathematically linked to gamma via an exponential relationship, pointing to the balance of excitatory and inhibitory circuit components as the biological substrate of temporal discounting.
- **TD computation is widespread across striatal subregions**: Biphasic impulse responses were observed for D1-MSN stimulation in lNAc, DMS, and DLS (cross-validated R^2 = 0.64–0.92 across regions). DLS showed faster dynamics (shorter time to minimum, P = 0.01), while estimated gamma was numerically closer to 1 for DMS and DLS compared to lNAc (though not significantly different, P = 0.23).
- **lNAc carries a value signal necessary for TD RPE in natural tasks**: Muscimol inactivation of lNAc reduced CS+ dopamine responses (-2.30 %dF/F, P = 0.0029) and increased predicted reward responses (+5.47 %dF/F, P = 0.0013) without affecting unpredicted reward or omission responses, consistent with lNAc providing the value signal whose derivative is computed by VTA.
- The TD computation occurs between D1-MSN spiking and VTA dopamine neuron spiking (latency of excitatory response to D1 stimulation: 50–100 ms), ruling out purely local mechanisms such as dopamine release modulation or D1-MSN spike-rate adaptation.

---

### Computational framework

**Temporal difference (TD) reinforcement learning / linear time-invariant (LTI) systems analysis.**

The paper formalises the transformation from striatal D1-MSN activity to dopamine neuron activity as convolution with a biphasic linear filter. In the TD framework, the error signal delta_t = R_t + gamma * V(S_t) - V(S_{t-1}), where gamma is the temporal discount factor. When gamma < 1 this is approximately a temporal derivative of value but with a negative steady-state component for sustained input. The equivalent LTI representation is the order-1 transfer function whose impulse response h_T(t) = delta(t) + ln(gamma) * delta'(t). The key parameters are: the positive lobe P (fast excitatory component), the negative lobe N (delayed inhibitory component), and gamma = e^(-sigma) where sigma is the pole of the fit LTI model. The ratio P/N determines gamma: larger N relative to P means a stronger preference for immediate reward. The model assumes the transformation is linear and time-invariant — an approximation that is empirically validated to first order (CV R^2 ~ 0.7–0.8), though higher-order models do not improve prediction.

---

### Prevailing model of the system under study

The prevailing model, as framed by the paper's introduction, is that phasic dopamine activity encodes a TD reward prediction error (RPE) — the Schultz et al. (1997) model extended to include derivative-like ramping dopamine (Kim et al. 2020). Under this model, dopamine acts as a teaching signal updating value representations in striatum. The striatum (particularly its D1 and D2 MSN populations) was thought to project value-related signals back to dopamine neurons to close the TD loop, but this remained a hypothesis. The exact circuit mechanism computing the temporal difference — the derivative-like operation at the heart of TD learning — was unknown. Alternative views have questioned whether TD RL is the right description of dopamine at the behavioral level. The relationship between gamma (temporal discounting) and any specific neural mechanism was entirely unknown.

---

### What this paper contributes

The paper provides the first direct causal demonstration that the D1-MSN-to-dopamine-neuron circuit performs a temporal difference computation, establishing that TD error generation is hardwired rather than learned or emergent from distributed brain dynamics. Specifically:

- It shows that optogenetically stimulating lNAc D1-MSNs with arbitrary temporal patterns drives VTA dopamine neurons in a pattern matching the TD error of the input, not the input itself — demonstrating the TD transformation is an intrinsic circuit property.
- It identifies the biphasic impulse response of the circuit as the computational substrate: the rapid positive lobe (net disinhibitory effect) and delayed negative lobe (net inhibitory effect) together implement the temporal difference.
- It provides the first circuit-level mechanism for the temporal discount factor gamma: gamma is set by the ratio of the positive and negative areas of the impulse response (P/N), grounding a higher-order cognitive parameter (time horizon of reward preference) in the balance of excitatory and inhibitory inputs from D1-MSNs to VTA.
- It extends the finding across lNAc, DMS, and DLS, suggesting a conserved computational motif across striatal subregions with region-specific parameters.
- The muscimol experiments bridge the artificial opto-conditioning paradigm to natural reward learning, confirming that lNAc provides a value signal to dopamine neurons in standard conditioning.

---

### Brain regions & systems

- **Lateral nucleus accumbens (lNAc)** — primary focus; site of dopamine release recording, D1/D2-MSN calcium imaging, and Neuropixels striatal recordings; argued to be the striatal locus of value-like signals that drive TD error in dopamine neurons.
- **VTA (ventral tegmental area)** — site of dopamine neuron cell bodies; antidromically optotagged lNAc-projecting neurons recorded during conditioning and D1 stimulation experiments; site of somatic GCaMP recording in muscimol experiment.
- **D1 medium spiny neurons (D1-MSNs)** — the key striatal cell type whose activation generates a temporal difference transformation in downstream dopamine activity; selective plasticity under dopamine stimulation.
- **D2 medium spiny neurons (D2-MSNs)** — recorded for comparison; do not show opto-conditioning-induced value-like potentiation, consistent with asymmetric plasticity rules.
- **Dorsomedial striatum (DMS)** — secondary site in multi-region experiment; also shows biphasic (TD) transfer function; gamma closer to 1, faster dynamics than lNAc.
- **Dorsolateral striatum (DLS)** — secondary site; biphasic transfer function present with the fastest dynamics (shortest time to negative lobe), gamma closest to 1.
- **Ventral pallidum (VP) / SNr** — hypothesised (but not directly tested) as intermediate nodes in the disinhibitory circuit computing the temporal difference between D1-MSNs and VTA dopamine neurons.

---

### Mechanistic insight

This paper meets both criteria for the high bar:

1. It presents a specific algorithm — the order-1 TD LTI transformation, formalised as convolution with a biphasic filter h_T(t) = delta(t) + ln(gamma)*delta'(t) — which would explain TD error generation.
2. It provides neural data (antidromic optotagging with Neuropixels + GRABDA3m photometry + D1-MSN optotagging) that specifically support this algorithm: D1-MSN activity faithfully tracks stimulation patterns while simultaneously recorded dopamine responses match TD error predictions quantitatively across 7 distinct temporal patterns. The TD model outperforms both simpler (zeroth-order) and more complex (second-order) alternatives.

**Bonus**: The paper constrains the physical implementation (response latency 50–100 ms; occurs between D1-MSN spiking and VTA DA spiking; rules out dopamine autoreceptor adaptation and local release modulation; implicates disinhibitory microcircuits via VP/SNr).

**Computational level**: The brain is computing a temporal difference of value estimates across adjacent time steps, implementing the error signal needed for TD learning. This enables credit assignment across time using only temporally local computations.

**Algorithmic level**: D1-MSNs encode a value-like prediction of upcoming reward. VTA dopamine neurons compute the temporal difference of this signal via convolution with a biphasic filter: rapid positive (net-excitatory, disinhibitory) followed by delayed negative (net-inhibitory) components. The resulting output is a TD RPE. The temporal discount factor gamma is encoded in the P/N ratio of the impulse response.

**Implementational level**: The TD transformation occurs between D1-MSN spiking and VTA DA neuron spiking with a latency of 50–100 ms, ruling out purely intrinsic mechanisms. Hypothesised circuit substrates include: (a) direct D1-MSN projections to VTA (providing fast disinhibitory signal via local GABAergic interneurons within VTA), and (b) D1-MSN projections via ventral pallidum or SNr back to VTA (providing the delayed inhibitory component). The balance of these pathways determines gamma. The TD computation is replicated across lNAc, DMS, and DLS, indicating the underlying circuit motif is conserved with region-specific tuning.

---

### Limitations & open questions

- All D1 stimulation experiments used artificial optogenetic inputs; whether the LTI approximation holds for more complex, naturalistic D1-MSN activity patterns remains to be tested.
- The study did not identify the specific synaptic or circuit mechanism underlying the biphasic filter (e.g. relative contributions of direct VTA interneurons, ventral pallidum pathway, or short-term synaptic plasticity).
- The multi-region experiment (Fig. 5) used stimulation patterns 1–4 only and fewer mice per site; DLS recordings in particular had small n for some site combinations.
- Dopamine neuron heterogeneity was not fully characterised — different dopamine neurons within lNAc-projecting population may differ in gamma or filter shape (hinted at by Extended Data Fig. 10b/c).
- The relationship between the circuit-level gamma measured here and behavioural temporal discounting in individual animals was not directly tested; this would require linking single-neuron impulse response shapes to behaviour in delay discounting tasks.
- Only ventral and dorsal striatum were tested; medial NAc, amygdala, and tail of striatum were explicitly flagged as important targets for future work.
- The paper does not address how non-lNAc circuits (e.g. hippocampus, PFC, amygdala) modulate or override the hardwired TD computation during naturalistic behaviour, nor what factors might set or shift gamma over development or with addiction.
- Whether the artificial opto-conditioning paradigm produces learning at the same rate and with the same parameters as natural reward conditioning remains unclear; cue and omission responses were ~5% of natural reward responses.

---

### Connections & keywords

**Key citations**:
- Schultz, Dayan & Montague (1997) — foundational TD RPE model of dopamine
- Kim et al. (2020) — derivative-like ramping dopamine as TD error
- Masset et al. (2025) — independent behavioural estimate of gamma = 0.56 discount/sec
- Sutton & Barto (1998) — TD learning algorithm
- Watabe-Uchida et al. — prior work on dopamine neuron diversity and projection targets
- Jeong et al. (2022) — dopamine as causal teaching signal

**Named models or frameworks**:
- Temporal difference (TD) reinforcement learning (Sutton & Barto)
- Linear time-invariant (LTI) systems identification
- TD LTI model (order-1 transfer function)
- Reward prediction error (RPE) model of dopamine (Schultz 1997)
- Minimal TD learning loop (authors' framework, Extended Data Fig. 10a)

**Brain regions**:
- Lateral nucleus accumbens (lNAc)
- Ventral tegmental area (VTA)
- Substantia nigra pars compacta (SNc)
- Dorsomedial striatum (DMS)
- Dorsolateral striatum (DLS)
- Ventral pallidum (VP)
- Substantia nigra pars reticulata (SNr)

**Keywords**:
- temporal difference learning
- dopamine reward prediction error
- D1 medium spiny neurons
- nucleus accumbens
- temporal discounting / discount factor gamma
- linear time-invariant systems
- biphasic impulse response
- antidromic optotagging
- Neuropixels electrophysiology
- GRABDA3m dopamine photometry
- patterned optogenetic stimulation
- hardwired neural circuit
