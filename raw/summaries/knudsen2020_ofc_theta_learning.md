---
source_file: "knudsen2020_ofc_theta_learning.md"
paper_id: "knudsen2020_ofc_theta_learning"
title: "Closed-Loop Theta Stimulation in the Orbitofrontal Cortex Prevents Reward-Based Learning"
authors: "Eric B. Knudsen, Joni D. Wallis"
year: 2020
journal: "Neuron"
paper_type: "empirical"
contribution_type: "empirical"
species: ["macaque"]
tasks: ["t_maze"]
brain_regions: ["hippocampus", "hippocampus_ca1", "orbitofrontal_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl", "model_free_rl"]
keywords: ["closed", "loop", "theta", "stimulation", "orbitofrontal", "cortex", "prevents", "reward", "based", "learning"]
key_citations: ["daw2005_uncertainty_prefrontal_striatal", "behrens2018_cognitive_map_organizing_knowledge", "jones2005_theta_hippocampal_prefrontal", "padoaschioppa2006_orbitofrontal_economic_value", "wikenheiser2016_cognitive_maps_hippocampus"]
---

### One-line summary

Closed-loop microstimulation that disrupts theta oscillations in the orbitofrontal cortex (OFC) causally impairs reward-based value learning in macaques, and this OFC theta is driven by hippocampal input.

---

### Background & motivation

The OFC is known to encode reward predictions from environmental cues and is essential for flexible, value-guided decision-making. A prominent theta oscillation (4–8 Hz) in OFC has been observed during reward learning tasks, but whether this oscillation has causal significance for learning — rather than merely correlating with it — was unknown. Prior methods for disrupting neural activity (lesions, pharmacology, open-loop stimulation) could not selectively disrupt oscillations without also affecting single-neuron firing rates, making it impossible to isolate the functional contribution of the oscillatory signal. This paper addresses that gap using a novel closed-loop approach.

---

### Methods

- **Subjects**: Two male rhesus macaques (Macaca mulatta).
- **Task**: A value discrimination learning task in which animals chose between pairs of probabilistically rewarded novel pictures. Reward contingencies (Prew) drifted over the course of a session via bounded random walk, requiring continuous value updating. Free-choice (80%) and forced-choice (20%) trials ensured animals were exposed to all contingencies. Learning speed was quantified as trials to re-establish criterion performance after a drift.
- **Recordings**: Local field potentials (LFPs) and single-unit activity recorded from OFC (areas 11/13) and anterior hippocampus (CA1) using multisite linear probes (16-channel Plexon K/V-probes), up to 6 electrodes per session.
- **Closed-loop stimulation**: A real-time feature extractor computed analytic amplitude and phase of theta (4–8 Hz) from ongoing LFP via Hilbert transform. When theta power exceeded a threshold, a biphasic 50 µA current pulse was delivered to OFC (or HPC) at the peak theta phase, via a single platinum-iridium microelectrode adjacent to the recording probe. Mean stimulation lag was 64 ± 3 ms.
- **Control conditions**: Open-loop (randomly jittered) stimulation; closed-loop beta (13–30 Hz) stimulation; stimulation during choice epoch or outcome epoch; stimulation during the late fixation epoch only.
- **Analyses**: Cross-trial phase alignment (mean resultant vector length R), reinforcement learning (RL) model fits to behaviour (TD update with softmax), single-neuron value regression (value-centric and picture-centric models), theta phase-locked firing, phase-power relationships, HPC-OFC cross-area phase synchrony (PLV), and directional influence via generalized partial directed coherence (GPDC).

---

### Key findings

- OFC LFP showed a prominent theta oscillation during task performance, with cross-trial theta phase alignment that increased specifically during drift periods (when animals were actively relearning values), particularly in the fixation epoch.
- Closed-loop theta stimulation during the fixation epoch severely impaired learning (significantly more trials required to reach criterion; p < 0.0005 in both subjects, corrected for multiple comparisons). No other stimulation condition — including open-loop theta, late-fixation theta, beta closed-loop, outcome-epoch theta, or choice-epoch theta — had any significant effect on learning.
- Closed-loop theta stimulation disrupted theta cross-trial phase alignment while paradoxically increasing theta power, reversing the normally positive power-phase alignment relationship (beta coefficient shifted from positive during sham to negative during stimulation; V: p = 2×10⁻¹⁹, T: p = 6×10⁻⁸).
- Approximately 37–65% of OFC neurons were theta phase-locked. About 37–54% of OFC neurons encoded current picture values in their firing rates during the fixation epoch; value encoding was stronger during drift than stable periods and was greater when firing rates were aligned to the theta oscillation versus jittered (2-way ANOVA, F > 1000, p < 10⁻¹⁵ for both subjects).
- Closed-loop theta stimulation significantly reduced neuronal value encoding in OFC; beta stimulation had no such effect.
- Stimulation did not significantly alter single-neuron firing rates, confirming that behavioural and oscillatory effects were not due to non-specific suppression of neural activity (F < 2, p > 0.1 for all conditions).
- HPC and OFC theta oscillations were synchronised (high PLV) during fixation and choice epochs. HPC-OFC theta synchrony tracked the learning cycle: it decreased at drift onset and recovered as animals relearned new values.
- GPDC directional analysis showed that influence during drift was predominantly in the HPC→OFC direction.
- Closed-loop theta stimulation of HPC (not OFC) impaired learning equivalently to OFC stimulation and disrupted bidirectional HPC-OFC theta influence (whereas OFC stimulation only reduced OFC→HPC influence), suggesting HPC drives OFC theta.

---

### Computational framework

The paper uses a **reinforcement learning (RL)** framework to characterise behaviour and provide trial-by-trial value estimates used in neural analyses.

The RL model is a standard temporal-difference model: value estimate Qi,t = Qi,t-1 + α(reward − Qi,t-1), with softmax choice rule parameterised by inverse temperature β. Parameters α and β are fit to maximise R² on choice behaviour per session.

This framework is not itself the mechanistic claim of the paper — it serves as a measurement tool to index the value representations OFC neurons are encoding. The mechanistic claim is that the theta oscillation is the medium through which OFC computes and coordinates these value representations during learning, with HPC providing the theta input.

---

### Prevailing model of the system under study

Prior to this paper, OFC was understood as a key region for encoding stimulus-reward associations and enabling value-based decision-making (Padoa-Schioppa & Assad, 2006; Rich & Wallis, 2014; Hunt et al., 2018). The canonical view was that OFC neurons represent the expected reward values of options, and that this representation supports choice behaviour. Neuronal oscillations in OFC — including a prominent theta rhythm observed during value learning (van Wingerden et al., 2010) — were treated as correlates of learning rather than causal contributors.

The broader context for oscillatory mechanisms was that theta rhythms could in principle organise cognition via spike-timing-dependent plasticity and cross-area synchronisation (Buzsáki et al., 2013; Canolty et al., 2010), and that HPC–PFC theta coherence was associated with memory and learning in rodents (Jones & Wilson, 2005; Benchenane et al., 2010) and primates (Brincat & Miller, 2015). However, establishing causal significance was challenging because standard perturbation methods (lesions, pharmacological inactivation) could not isolate oscillatory signals from firing rate effects. The causal contribution of OFC theta to reward learning in primates was thus open.

---

### What this paper contributes

This paper provides the first direct causal evidence that theta oscillations in OFC are necessary for reward-based value learning in primates. By developing a closed-loop stimulation method that selectively disrupts theta phase alignment without altering single-neuron firing rates, the authors demonstrate that:

1. The theta oscillation itself — not just OFC activity in general — is critical for flexible value updating.
2. OFC neurons encode value information preferentially at specific theta phases during learning, and this phase-locked encoding is disrupted by theta stimulation.
3. HPC drives OFC theta during learning, extending the HPC–prefrontal theta interaction framework to the OFC and to reward learning specifically.

The results update the prevailing model by specifying the oscillatory mechanism through which OFC performs value computations: theta phase alignment organises the firing of anatomically interspersed OFC value-coding neurons, and HPC provides the temporal scaffolding for this process. This places OFC in a hippocampal-dependent circuit for model-based RL, in which HPC constructs cognitive maps and OFC uses them to generate reward predictions.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC, areas 11/13)** — primary locus of investigation; site of theta oscillations, value-encoding neurons, and closed-loop stimulation; proposed to use hippocampal theta input to coordinate value representations during learning.
- **Hippocampus (HPC, anterior CA1)** — proposed source of theta drive to OFC; synchronised with OFC theta during learning; independently stimulated to show it causally disrupts learning and bidirectional HPC-OFC influence.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Phenomenon**: Flexible reward-based value learning requires the OFC, and is associated with theta oscillatory dynamics during cue fixation.

**Computational level**: The problem the brain is solving is online value updating — tracking changing reward contingencies and using current value estimates to guide choices. The OFC must maintain current value representations and update them based on prediction errors.

**Algorithmic level**: OFC neurons encoding picture values (in a value-centric, picture-invariant code) fire at specific phases of the theta oscillation during the fixation epoch. Cross-trial theta phase alignment (not theta power per se) is the relevant variable — it reflects the temporal coordination of value-coding neurons across trials and is specifically enhanced during learning (drift periods). Disrupting this phase alignment via closed-loop stimulation reduces the amount of value information encoded by OFC neurons and impairs learning. The HPC provides the theta rhythm that coordinates this population-level phase alignment; GPDC analysis shows HPC→OFC as the dominant direction of influence during learning.

**Implementational level**: Single-unit recordings confirm that stimulation does not affect OFC firing rates, ruling out a general excitability account. The closed-loop system demonstrates that it is the temporal structure of spiking relative to theta phase — rather than the rate code — that is being disrupted. HPC CA1 (a region with strong direct projections to OFC in macaques) is the source structure. The authors do not address cell-type-specific mechanisms (e.g., interneuron vs. pyramidal cell contributions to phase locking) or synaptic implementation of STDP, but note these as downstream mechanisms through which phase-locked HPC input could drive OFC plasticity.

---

### Limitations & open questions

- **Single electrode / one hemisphere**: Stimulation was delivered via a single electrode in OFC or HPC per session; bilateral or multi-site effects were not assessed.
- **HPC controls**: The HPC stimulation experiment lacked the same battery of control conditions (epoch specificity, frequency specificity, open-loop controls) as the OFC experiment; the mechanism of the HPC-mediated learning impairment is therefore less firmly established.
- **Directionality of causal chain**: While GPDC suggests HPC→OFC predominance, the analysis cannot resolve whether disrupting OFC theta affects downstream structures (e.g., amygdala, striatum) that independently contribute to learning impairment.
- **Task design and strategy**: The small picture set and continuously changing contingencies may have encouraged an explicit working-memory-like strategy, potentially limiting generalisability to tasks that rely more heavily on model-free RL.
- **Permanent lesions vs. transient disruption**: OFC lesions do not impair a similar task (Rudebeck et al., 2017), suggesting compensatory plasticity can occur; the closed-loop disruption reveals the acute necessity of theta but does not fully resolve long-term circuit-level redundancy.
- **Cell-type and synaptic mechanisms**: How theta phase locking is implemented at the level of specific cell types, synaptic plasticity rules, or neuromodulatory inputs remains unknown.

---

### Connections & keywords

**Key citations**:
- van Wingerden et al. (2010) — prior correlative evidence of OFC theta during rodent value learning
- Brincat & Miller (2015) — theta HPC–lateral PFC coherence during associative learning in monkeys
- Jones & Wilson (2005) — theta coordination of HPC–mPFC interactions in spatial memory
- Benchenane et al. (2010) — theta coherence at choice point during T-maze learning
- Padoa-Schioppa & Assad (2006) — OFC neurons encode economic value
- Daw et al. (2005) — model-free vs. model-based RL and prefrontal/striatal competition
- Wikenheiser & Schoenbaum (2016) — cognitive maps in HPC and OFC
- Behrens et al. (2018) — what is a cognitive map
- Buzsáki et al. (2013) — theta, spike timing-dependent plasticity, scaling
- Jadhav et al. (2012) — closed-loop HPC manipulation (sharp-wave ripples)

**Named models or frameworks**:
- Closed-loop microstimulation (novel methodological contribution)
- Temporal difference reinforcement learning (TD-RL) / softmax choice model (used as measurement tool)
- Generalized Partial Directed Coherence (GPDC)
- Phase-locking value (PLV) / cross-area phase alignment
- Model-based vs. model-free RL (Daw et al. 2005 framework — theoretical context)
- Cognitive map (OFC-HPC division of labour)

**Brain regions**:
- Orbitofrontal cortex (OFC, areas 11/13)
- Hippocampus (HPC, anterior CA1)

**Keywords**:
- OFC theta oscillations
- closed-loop microstimulation
- reward-based learning
- value encoding
- phase-locked firing
- hippocampal-OFC synchrony
- cross-trial phase alignment
- model-based reinforcement learning
- primate neurophysiology
- spike-timing-dependent plasticity
- local field potential
- orbitofrontal cortex
