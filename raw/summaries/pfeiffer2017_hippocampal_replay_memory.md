---
source_file: pfeiffer2017_hippocampal_replay_memory.md
paper_id: pfeiffer2017_hippocampal_replay_memory
title: "The content of hippocampal \"replay\""
authors:
  - "Brad E. Pfeiffer"
year: 2017
journal: Hippocampus
paper_type: review
contribution_type: review
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - prefrontal_cortex
  - amygdala
frameworks:
  - reinforcement_learning
  - attractor_networks
keywords:
  - hippocampal_replay
  - sharp_wave_ripples
  - place_cells
  - memory_consolidation
  - memory_retrieval
  - forward_replay
  - reverse_replay
  - theta_sequences
  - spatial_memory
  - systems_consolidation
  - temporal_credit_assignment
  - preplay
  - awake_replay
  - sleep_replay
  - goal_directed_navigation
  - attractor_networks
  - spike_timing_dependent_plasticity
  - content
  - hippocampal
  - replay
key_citations:
  - davidson2009_hippocampal_replay_extended
  - gupta2010_replay_not_simple_function
  - ambrose2016_reverse_replay_hippocampal
  - lee2002_memory_sequential_experience
---

### One-line summary
Hippocampal replay events encode diverse content including past experiences, future paths, and novel combinations of learned information, supporting both memory consolidation and planning functions.

### Background & motivation
Hippocampal "replay" refers to temporally compressed neuronal sequences that reactivate during sharp-wave ripples, primarily during non-exploratory states like sleep or quiet rest. While initially hypothesized to serve memory consolidation via reactivation of prior experiences, recent findings suggest replay may also support memory retrieval for future planning, represent novel never-experienced paths, or reflect pre-configured network dynamics. This review synthesizes evidence on replay content to constrain models of circuit mechanisms and mnemonic function.

### Methods
This is a narrative review of the literature on hippocampal replay. The review covers:
- Historical studies on sleep reactivation and the two-stage memory model
- Awake replay discoveries including forward and reverse sequences
- Analysis of replay content including remote experiences, reward modulation, and learned information
- Models of replay generation including preplay vs. experience-dependent plasticity
- Functional implications for memory consolidation and planning

### Key findings
- **Early sleep replay studies**: Initial work demonstrated that hippocampal neurons active during exploration show increased firing during subsequent sleep, with pairwise correlations preserved during ripples (Wilson & McNaughton, 1994). Sleep sequences showed temporal compression and preserved temporal order.

- **Awake replay diversity**: Foster & Wilson (2006) discovered "reverse replay" where sequences activate in opposite temporal order to experience. Both forward and reverse replay occur during awake states, with reverse replay enhanced by reward.

- **Minimal experience requirements**: Reverse replay can occur after a single traversal of a novel track, demonstrating that behavioral repetition is not strictly necessary. However, experience-dependent plasticity does enhance replay expression.

- **Remote and constructed experiences**: Replay can encode trajectories in physically separate environments (Karlsson & Frank, 2009) and novel "shortcut" paths never actually taken (Gupta et al., 2010), indicating replay represents learned spatial relationships rather than mere replication of prior activity.

- **Reward modulation**: The number of reverse replays correlates with reward magnitude (Ambrose et al., 2016), and dopaminergic activation enhances replay likelihood (McNamara et al., 2014), suggesting salience signals bias replay content.

- **Preplay controversy**: Dragoi & Tonegawa (2011) reported "preplay" where ripple sequences before novel experience match subsequent place cell firing order, suggesting pre-configured hippocampal maps. However, subsequent studies found no evidence for pre-play when controlling for experience-dependent plasticity (Silva et al., 2015). Grosmark & Buzsáki (2016) proposed a resolution: "rigid" cells with pre-configured connectivity participate in pre-experience replay, while "plastic" cells are incorporated via experience-dependent mechanisms.

- **Forward replay and future behavior**: During goal-directed navigation, forward replay encodes paths from current location to goal, and replay content strongly correlates with subsequent behavior (Pfeiffer & Foster, 2013). Replay can also encode paths to avoid (Wu et al., 2017), suggesting it provides outcome predictions to inform rather than dictate behavior.

- **Functional dissociation**: Reverse replay appears suited for memory consolidation (linking outcomes to prior actions), while forward replay serves memory retrieval for planning. Sleep and awake replay may have distinct functions: sleep replay for consolidation, awake replay for retrieval and working memory.

### Computational framework
The review discusses several computational frameworks:

- **Two-stage memory model**: Hippocampus forms rapid labile traces during exploration, with subsequent off-line reactivation during sleep serving to consolidate memories or transfer them to cortex (Marr, 1971; Buzsáki, 1989).

- **Attractor network dynamics**: Replay reflects activation patterns in auto-associative CA3 networks. Symmetric STDP in CA3 (Mishra et al., 2016) explains how reverse replay can emerge despite forward-directed experience.

- **Reinforcement learning**: Reverse replay may solve temporal credit assignment by bringing outcomes close in time to preceding actions (Foster & Wilson, 2006). Forward replay may implement model-based planning by simulating future trajectories.

- **Predictive coding**: The hippocampus constructs predictions about future states, with replay representing mental simulation of possible paths (Buckner, 2010).

### Prevailing model of the system under study
Before this review, the prevailing model held that hippocampal replay primarily serves memory consolidation via reactivation of prior experiences during sleep. Replay was viewed as a direct replication of waking neural activity patterns, temporally compressed but otherwise faithful to experience. The two-stage memory model (Marr, 1971; Buzsáki, 1989) provided the theoretical framework, with replay serving to consolidate synaptic changes or transfer information to cortex. Awake replay was less studied, and its functional significance was unclear.

### What this paper contributes
This review advances understanding by synthesizing evidence that replay is far more diverse than simple replication of prior activity:

1. **Functional diversity**: Forward and reverse replay serve distinct functions—reverse for consolidation, forward for planning. The correlation between reverse replay and reward magnitude (Ambrose et al., 2016) supports a consolidation role, while the correlation between forward replay and future behavior (Pfeiffer & Foster, 2013) supports a planning role.

2. **Content diversity**: Replay encodes not just past experience but also novel combinations of learned information ("shortcuts"; Gupta et al., 2010), remote environments (Karlsson & Frank, 2009), and paths to avoid (Wu et al., 2017).

3. **Experience requirements**: While some replay requires experience-dependent plasticity, reverse replay can occur after single experiences (Foster & Wilson, 2006), and "preplay" may reflect pre-configured network dynamics (Dragoi & Tonegawa, 2011; Grosmark & Buzsáki, 2016).

4. **Circuit mechanisms**: The review synthesizes evidence for symmetric STDP in CA3 (Mishra et al., 2016) explaining reverse replay, and proposes models for goal-directed replay involving asymmetric synaptic weight gradients toward salient locations.

5. **State-dependent functions**: Sleep and awake replay may have distinct functions—consolidation vs. retrieval—rather than serving a single mnemonic purpose.

The review concludes that "replay" is a misnomer for a diverse set of phenomena that likely reflect multiple network mechanisms serving different cognitive functions.

### Brain regions & systems
- **Hippocampus (CA1, CA3)**: Primary focus—locus of replay events. CA3 recurrent circuitry with symmetric STDP supports reverse replay. CA1 shows coordinated reactivation with CA3 during ripples.
- **Medial entorhinal cortex (MEC)**: Bidirectional communication with hippocampus. MEC shows ripple-band activity and grid cell replay. Deep MEC layers participate in hippocampal replay chains; superficial layers may replay independently. MEC inhibition reduces multi-ripple events and fragments spatial representations.
- **Prefrontal cortex**: Coordinated excitation and inhibition during awake hippocampal ripples (Jadhav et al., 2015).
- **Amygdala**: May coordinate with replay to provide valence information during fear memory retrieval (Wu et al., 2017; Girardeau et al., 2017).
- **Dopaminergic inputs**: From midbrain to hippocampus, modulate replay likelihood and may bias content via reward signals.

### Mechanistic insight
This paper does not meet the bar for mechanistic insight as defined in the skill instructions. As a review paper, it synthesizes existing evidence rather than presenting new neural data to support a specific algorithm. However, the review discusses Marr's three levels in the context of proposed models:

- **Computational level**: The hippocampus solves problems of memory consolidation (storing experiences for long-term retention) and memory retrieval (using stored information to guide future behavior). Reverse replay may solve temporal credit assignment by linking outcomes to preceding actions.

- **Algorithmic level**: Multiple proposed algorithms are discussed. The two-stage model proposes initial encoding via plastic changes followed by off-line reactivation. Attractor network dynamics with symmetric STDP in CA3 explain how reverse replay can emerge. Models of goal-directed replay propose asymmetric synaptic weight gradients toward salient locations, with auto-associative and hetero-associative dynamics during gamma cycles controlling spatial representation transitions.

- **Implementational level**: The review discusses specific neural mechanisms including: symmetric STDP at CA3-CA3 synapses (Mishra et al., 2016); cholinergic signaling and theta sequences facilitating plasticity (Isaac et al., 2009); dopaminergic modulation of replay likelihood (McNamara et al., 2014); gamma oscillation dynamics structuring replay content (Pfeiffer & Foster, 2015); and the role of MEC-hippocampal interactions in concatenating replay events (Yamamoto & Tonegawa, 2017).

### Limitations & open questions
The review identifies several key limitations and open questions:

- **Preplay controversy**: The existence and interpretation of "preplay" (replay of never-experienced sequences before first experience) remains unresolved, with conflicting results across studies.

- **Mechanism of path selection**: How does the hippocampus select specific paths from the infinite possibilities in open fields? The models proposed remain speculative.

- **Forward vs. reverse generation**: No current evidence indicates that forward and reverse replays are generated via distinct network mechanisms; understanding how the same circuitry produces both is unresolved.

- **MEC involvement controversy**: Whether superficial MEC (which provides input to hippocampus) participates in replay remains unclear, with conflicting reports.

- **Conscious vs. automatic**: It remains unknown whether replay reflects conscious memory recollection or subconscious automatic mechanisms.

- **State-dependent functions**: The precise functional differences between sleep and awake replay, and how they relate to consolidation vs. retrieval, require further clarification.

- **Causal evidence**: Much evidence is correlational; more causal manipulations (e.g., optogenetic disruption of specific replay types) are needed to establish function.

### Connections & keywords
**Key citations**:
- Wilson & McNaughton (1994) - First multi-neuron reactivation evidence
- Foster & Wilson (2006) - Discovery of reverse replay
- Lee & Wilson (2002) - Temporal compression in sleep replay
- Davidson et al. (2009) - Extended replay via ripple concatenation
- Gupta et al. (2010) - Never-experienced shortcut paths in replay
- Pfeiffer & Foster (2013) - Goal-directed forward replay
- Dragoi & Tonegawa (2011) - Preplay of future sequences
- Ambrose et al. (2016) - Reward modulation of reverse replay
- Grosmark & Buzsáki (2016) - Rigid vs. plastic cell populations
- Yamamoto & Tonegawa (2017) - MEC-hippocampal replay interactions

**Named models or frameworks**:
- Two-stage model of memory formation (Marr, 1971; Buzsáki, 1989)
- Attractor network dynamics
- Reinforcement learning / temporal credit assignment
- Theta sequences and phase precession
- Auto-associative and hetero-associative network dynamics
- Preplay vs. replay models
- Model-based planning/prediction

**Brain regions**:
- Hippocampus (CA1, CA3, dentate gyrus)
- Medial entorhinal cortex (MEC)
- Prefrontal cortex
- Amygdala
- Dopaminergic midbrain inputs

**Keywords**:
hippocampal replay, sharp-wave ripples, place cells, memory consolidation, memory retrieval, forward replay, reverse replay, theta sequences, spatial memory, systems consolidation, temporal credit assignment, preplay, awake replay, sleep replay, goal-directed navigation, attractor networks, spike-timing-dependent plasticity
