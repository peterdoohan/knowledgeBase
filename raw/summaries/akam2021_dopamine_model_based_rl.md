---
source_file: akam2021_dopamine_model_based_rl.md
paper_id: akam2021_dopamine_model_based_rl
title: "What is dopamine doing in model-based reinforcement learning?"
authors:
  - "Thomas Akam"
  - "Mark E Walton"
year: 2021
journal: "Current Opinion in Behavioral Sciences"
paper_type: review
contribution_type: theoretical
methods:
  - optogenetics
  - lesion
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - striatum
  - ventral_striatum
  - nucleus_accumbens
  - ventral_tegmental_area
  - substantia_nigra
  - amygdala
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - successor_representation
  - temporal_difference_learning
keywords:
  - keywords_dopamine
  - reward_prediction_error_rpe
  - state_prediction_error_spe
  - model_based_reinforcement_learning
  - model_free_reinforcement_learning
  - successor_representation
  - surprise_signal
  - basal_ganglia
  - striatum
  - hippocampus
  - offline_planning
  - sharp_wave_ripples
  - cortico_basal_ganglia_loops
  - volume_transmission
  - dopamine_heterogeneity
  - temporal_difference_learning
  - unblocking
  - optogenetics
  - vta
  - snc
key_citations:
  - daw2005_uncertainty_prefrontal_striatal
wiki_pages:
  - wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning
  - wiki/topics/successor_representation_as_a_predictive_map_in_reinforcement_learning_and_hippocampal_prefrontal_coding
---

### One-line summary
This review evaluates two accounts of how dopamine participates in model-based reinforcement learning — dopamine as a successor representation (SR) prediction error vs. dopamine as a well-informed scalar reward prediction error (RPE) plus a separate scalar surprise signal — and argues in favor of the latter.

### Background & motivation
Dopamine is classically associated with reward prediction errors (RPEs), the key teaching signal in model-free RL. A growing body of evidence, however, implicates dopamine in model-based RL: dopaminergic RPEs are informed by inference over hidden states; dopamine neurons respond to surprising but non-rewarding events (state prediction errors, SPEs); and both causal manipulations and natural variation in dopamine affect model-based behavior. These findings challenge the sufficiency of the RPE account and demand a richer mechanistic explanation.

### Methods
This is a theoretical/computational review. The authors critically evaluate a specific prior computational proposal — that dopamine encodes a vector-valued SPE used to update a feature-based successor representation (Gardner et al., 2018) — by examining its compatibility with neuroscientific data on anatomy, physiology, and lesion/optogenetic experiments. They then propose an alternative two-component account and evaluate its explanatory scope against the same evidence.

### Key findings
1. The SR account of dopamine faces a critical dimensionality problem: the rat brain has ~17 million cortico-striatal neurons but only ~70,000 midbrain dopamine neurons, making it implausible that dopamine carries the high-dimensional vector-valued SR prediction error.
2. The SR account does not naturally predict the large body of quantitative RPE-consistent data, including findings that dopamine neuron stimulation is strongly reinforcing.
3. The SR account fails to explain the specificity required for optogenetic dopamine stimulation to unblock stimulus-stimulus learning (C→X) without recruiting neurons specifically selective for predictions about X.
4. An alternative account — well-informed scalar RPE + scalar surprise signal — can explain dopamine's involvement in model-based RL without requiring high-dimensional signaling.
5. Model-based value estimates can inform dopaminergic RPEs through: (a) offline planning during hippocampal sharp-wave ripples that refines cached values; (b) predictive representations such as the SR that allow rapid value recomputation; (c) possibly minimal single-step rollouts gated by theta phase resetting.
6. A scalar dopaminergic surprise signal (evaluated early in the sensory hierarchy but projected to high-level cortical areas) can upregulate learning rates in cortical and hippocampal predictive models, explaining stimulus-stimulus learning impairments and optogenetic unblocking without requiring vector-valued SPEs.
7. Dopamine heterogeneity is partially explained by partial summation of value over state features across parallel cortico-basal-ganglia loops; the radically different profile of tail-of-striatum dopamine neurons (threat-responsive, aversive) likely reflects a separate axis of reinforcement.

### Computational framework
- Model-free RL: temporal difference (TD) learning with scalar RPE (δ = r_t + γv_t − v_{t−1}); RPE updates weight vector mapping state features to scalar value.
- Model-based RL: internal world model predicts future states given actions; values computed by simulating future trajectories (roll-outs).
- Successor representation (SR): caches expected discounted future feature occupancy, separating long-run state prediction from immediate reward. Value = SR × reward vector. Updated via vector-valued TD prediction error.
- Authors' preferred account: scalar RPE informed by model-based values (from offline planning, SR, or minimal rollout) + scalar surprise signal that modulates learning rates in predictive models.

### Prevailing model of the system under study
The dominant framework is the RPE theory of dopamine (Schultz, Dayan, Montague 1997): phasic dopamine signals the temporal difference between expected and received reward, serving as the teaching signal for model-free value learning in the basal ganglia. The parallel model-based/model-free framework (Daw et al. 2005; Balleine & Dickinson 1998) assigns striatal dopamine primarily to model-free learning, with prefrontal cortex and hippocampus supporting model-based learning. Recent evidence challenged this clean division.

### What this paper contributes
- A systematic critique of the SR-dopamine hypothesis, identifying dimensionality, empirical coverage, and mechanistic specificity as its main weaknesses.
- A positive alternative account: dopamine supports model-based RL through (1) offline planning-driven RPEs, (2) RPEs incorporating model-based value estimates (SR or minimal rollout), and (3) a scalar surprise signal that permissively upregulates cortical/hippocampal model learning.
- A reconciliatory conclusion: dopamine's involvement in model-based RL is compatible with a refined RPE theory and does not require abandoning the scalar RPE framework.

### Brain regions & systems
- Ventral tegmental area (VTA) / substantia nigra pars compacta (SNc): source of dopamine neurons
- Striatum (ventral striatum / nucleus accumbens, dorsal striatum, tail of striatum): target of dopamine; cortico-striatal synapses as locus of cached value storage
- Prefrontal cortex / medial frontal cortex: target of dopamine surprise signal; model updating and learning rate modulation
- Hippocampus: sharp-wave ripples for offline planning; theta sequences for minimal rollout; place cells and predictive maps
- Amygdala: dopamine projections mediating surprise-induced attention to preceding cues
- Cortico-basal-ganglia loops: parallel loops with partial summation of value information explaining dopamine heterogeneity

### Mechanistic insight
- Dopaminergic RPEs can reflect model-based values if those values are cached in advance (offline) or approximated via the SR, not requiring real-time roll-outs.
- The surprise signal is a low-level, early-latency, valence-independent signal transmitted from midbrain to high-level cortical areas, functionally enabling rapid updating of cortical predictive models when new information invalidates prior predictions.
- Co-occurrence of RPE and surprise signals in the same cells may serve to focus representational capacity on task-relevant state features, and to drive novelty-seeking exploration.
- Volume transmission and partial summation across cortico-basal-ganglia loops naturally produces heterogeneity in what is conceptually a scalar signal.

### Limitations & open questions
- The dimensionality of dopamine signals has not been precisely quantified; the argument rests on cell-count disparities rather than direct measurement.
- The mechanisms by which the surprise signal specifically upregulates stimulus-stimulus (model) learning vs. value learning are not fully specified.
- Whether movement-related and other non-reward dopamine responses can be absorbed into partial summation of value or require additional axes of reinforcement remains open.
- The temporal feasibility of theta-phase minimal rollouts informing dopamine RPEs is speculative and lacks direct experimental evidence.
- The relationship between dopaminergic surprise signaling and acetylcholine/noradrenaline surprise signals is acknowledged but not resolved.

### Connections & keywords
Keywords: dopamine, reward prediction error (RPE), state prediction error (SPE), model-based reinforcement learning, model-free reinforcement learning, successor representation, surprise signal, basal ganglia, striatum, hippocampus, offline planning, sharp-wave ripples, cortico-basal-ganglia loops, volume transmission, dopamine heterogeneity, temporal difference learning, unblocking, optogenetics, VTA, SNc
Related papers: Gardner et al. 2018 (SR-dopamine hypothesis, ref [36]); Stachenfeld et al. 2017 (hippocampus as predictive map); Daw et al. 2011 (model-based influences on striatal prediction errors); Russek et al. 2017 (SR linking model-based and model-free RL); Sharpe et al. 2017 (dopamine transients and model-based associations); Mattar & Daw 2018 (prioritized replay); Menegas et al. 2018 (tail-of-striatum dopamine and threat); Langdon et al. 2018 (review of model-based predictions for dopamine)

### Related wiki pages
- [[wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning|Goal-directed vs habitual control in corticostriatal reinforcement learning]]
- [[wiki/topics/successor_representation_as_a_predictive_map_in_reinforcement_learning_and_hippocampal_prefrontal_coding|Successor representation as a predictive map in reinforcement learning and hippocampal–prefrontal coding]]
