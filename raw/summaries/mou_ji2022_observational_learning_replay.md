---
source_file: mou_ji2022_observational_learning_replay.md
paper_id: mou_ji2022_observational_learning_replay
title: "Observational learning promotes hippocampal remote awake replay toward future reward locations"
authors:
  - "Xiang Mou"
  - "Abhishekh Pokhrel"
  - "Prakul Suresh"
  - "Daoyun Ji"
year: 2022
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - t_maze
methods:
  - tetrode_recording
  - bayesian_decoding
  - lesion
brain_regions:
  - hippocampus_ca1
keywords:
  - hippocampal_awake_replay
  - remote_replay
  - observational_learning
  - place_cells
  - sharp_wave_ripples_swr
  - population_burst_events_pbes
  - reward_site_targeting
  - prospective_coding
  - spatial_working_memory
  - social_learning
  - bayesian_decoding
  - forward_and_reverse_replay
  - observational
  - learning
  - promotes
  - hippocampal
  - remote
  - awake
  - replay
  - toward
key_citations:
  - davidson2009_hippocampal_replay_extended
---

### One-line summary

Observer rats watching a demonstrator navigate a T-maze show hippocampal CA1 place cell replay — occurring remotely in the physically separate observation box — that preferentially targets the maze's reward sites and predicts the observer's future correct choices.

---

### Background & motivation

Observational learning — acquiring skills by watching others — is widespread across species but poorly understood at the neural circuit level. The hippocampus is a known hub for spatial learning and memory, and awake sharp-wave ripple (SWR)-associated replay of place cell sequences is implicated in spatial decision-making and planning. However, whether and how hippocampal awake replay participates in observational learning of spatial trajectories had not been investigated. This paper addresses this gap by recording CA1 place cells in observer rats performing a demonstrator-guided spatial working memory task.

---

### Methods

- **Task design**: Observer rats (OBs) watched a demonstrator (Demo) run a T-maze from a physically separated observation box; OBs were then placed in the maze and had to replicate the Demo's left/right choice for water reward. Sessions consisted of 30–50 trials.
- **Subject population**: 18 Long-Evans rats trained as observers; 6 surgically implanted with tetrodes for CA1 recording after reaching criterion performance (>70% correct for 2 consecutive days).
- **Control conditions**: Demo replaced by a moving Object, or maze was Empty; a Blocked-view condition was also tested.
- **CA1 lesion experiment**: NMDA infusion into dorsal CA1 (N=5 rats) vs. vehicle (N=5) to assess CA1 dependence of behavior.
- **Neural recordings**: Tetrode recording of CA1 place cells during testing sessions; place cell templates built from self-running in the maze; awake replay identified via Bayesian decoding of population burst events (PBEs) occurring at ripples during reward consumption in the observation box.
- **Key analyses**: Replay rate, replay Z score, replay direction (reward-leading vs. reward-away), replay ending rate in reward zones, bias toward same-side/correct/future trajectory templates, trial-by-trial prediction of future maze choice.

---

### Key findings

- Observer rats reliably learned to follow the demonstrator's left/right choices both in the observation box (poke synchronization index increased significantly over pre-training; F(21,224)=2.8, p=1.1×10⁻⁴) and in the T-maze (mean 86.9% correct in last 3 training sessions).
- Performance in both the box and the maze required the presence of a live demonstrator; control (Object, Empty) conditions reduced maze performance to chance (~50%).
- NMDA lesions of dorsal CA1 significantly impaired both box poke performance and maze performance (maze: NMDA 61.8% vs. vehicle 81.7%, F(1,29)=59, p=4.0×10⁻⁸).
- Place cell patterns acquired during self-running in the maze were replayed remotely (in the physically separated observation box) during reward consumption; replay was highly significant above chance for both outbound (Z=15, p=1.5×10⁻⁵²) and inbound (Z=13, p=3.4×10⁻³⁸) templates.
- Ripple power, PBE rate, replay rate, replay Z score, and match index were all significantly higher under the Demo condition than under Object or Empty controls.
- Remote replay preferentially targeted maze reward sites: reward zone reactivation rate was higher under Demo vs. Object and Empty (p=0.0029 and p=0.035 respectively); replay vectors ended within reward zones at a rate of 1.9× chance under Demo (p=3.3×10⁻⁴), but not under Object or Empty.
- Remote replay content was biased toward the future correct trajectory: replay ratio for correct templates exceeded wrong templates under Demo (Z=3.6, p=1.4×10⁻⁴); replay ratio for future templates exceeded past templates under Demo (Z=3.4, p=3.5×10⁻⁴); neither effect was present under control conditions.
- Trial-by-trial analysis confirmed that remote replay content in the observation box significantly predicted the observer's future maze choice under Demo but not under Object or Empty conditions.
- Reverse replay was notably prominent for inbound trajectories (pointing toward reward sites), even though observers always ran away from the reward site on inbound paths — highlighting a goal-directed, not experience-mirroring, content selection.

---

### Computational framework

Not applicable in the sense of an explicit formal model. The paper uses **Bayesian decoding** of place cell population activity to identify and characterise replay events (trajectory reconstruction from spike timing within PBEs). The framework assumes a probabilistic mapping between neural population states and spatial positions along a linearised trajectory template, enabling moment-by-moment decoding of decoded position during each PBE. The results are interpreted within a **cognitive map / memory consolidation and planning** framework: awake replay is treated as a neural substrate for prospective planning of spatial trajectories, whose content is shaped by socially acquired information about reward locations.

---

### Prevailing model of the system under study

The paper's introduction signals the following baseline understanding: the hippocampus encodes space through place cells that fire sequentially as an animal traverses a trajectory, forming a cognitive map. During awake resting — particularly at reward sites during SWRs — these sequences are replayed, and this replay is thought to support memory consolidation, recall, and future spatial planning. Prior work had shown that awake replay can represent forward or reverse trajectories, occasionally novel routes, and tends to be biased toward upcoming or recently experienced paths. However, all prior demonstrations of awake replay were in the context of self-experienced navigation: replay occurred in the same environment where the place field templates were built. There was no established evidence that replay could occur remotely — i.e., in a physically separate environment — or that it could be triggered by observing a conspecific's actions, leaving the neural mechanisms of observational spatial learning largely uncharacterised.

---

### What this paper contributes

The paper extends the prevailing model in two important directions. First, it establishes that hippocampal awake replay is not confined to the environment where place fields were formed: replay can occur remotely, during reward consumption in a physically separated box, using templates built from self-running in a different environment. This demonstrates a previously undocumented flexibility in replay generation that is independent of the observer's current physical location. Second, it shows that the *content* of replay is shaped by social observation: the presence of a live demonstrator, but not a moving object or an empty maze, drives remote replay to preferentially represent reward-site locations and future correct trajectories, and this replay content predicts the observer's upcoming decisions on a trial-by-trial basis. Together, these findings provide a hippocampal circuit-level mechanism for observational learning of spatial trajectories: social cues from a demonstrator direct the construction of remote awake replay content toward goal-relevant locations, which then guides the observer's own navigation.

---

### Brain regions & systems

- **Hippocampal CA1** — primary recording target; place cell sequences and SWR-associated replay were recorded here. CA1 is the proposed locus of remote awake replay that encodes goal-directed spatial representations during observational learning.
- **Dorsal CA1 specifically** — targeted by NMDA lesions; its damage impaired both box poke performance and maze navigation, establishing a necessary causal role in the behavior.

---

### Mechanistic insight

This paper meets both criteria for the high bar: it formalises a specific algorithmic process (Bayesian-decoded awake replay biased toward reward sites and future trajectories) and provides neural data (CA1 tetrode recordings, NMDA lesion results) that specifically link that process to the observed behaviour.

- **Computational**: The brain is solving the problem of learning which spatial trajectory to take in a novel environment from vicarious experience (observing a demonstrator), rather than through trial-and-error self-exploration.
- **Algorithmic**: The proposed process is that social observation drives the content of CA1 awake SWR-replay toward goal-relevant (reward-site-targeting) trajectory representations of the observed environment. Replay content is prospective — biased toward the future correct trajectory rather than the most recently experienced past trajectory — and predictive of upcoming decisions on a trial-by-trial basis. Bayesian decoding confirms that individual replay events carry spatially specific trajectory information, and replay direction (forward vs. reverse) is selected to point toward reward sites regardless of the observer's own running direction.
- **Implementational**: The paper establishes a necessary role for the dorsal CA1 (NMDA lesion results), demonstrates that replay occurs specifically during SWR-associated PBEs in CA1, and shows that ripple power and PBE rate are themselves modulated by the presence of a live demonstrator. However, the specific cell types, interneuron circuits, or neuromodulatory mechanisms responsible for selecting socially-driven replay content are not addressed.

---

### Limitations & open questions

- The mechanism by which social observation specifically shapes the *content* of remote replay (rather than merely increasing global ripple/PBE rates) is not explained — what circuit-level process links watching a demonstrator to selecting reward-site-targeting templates?
- It is unknown whether non-social observational cues (e.g., a video replay or an inanimate cue that perfectly mimics a demonstrator's movement) could similarly drive remote replay, leaving open the question of what is specifically "social" about the effect.
- The recording was confined to CA1; whether and how other hippocampal subregions (CA3, subiculum) or cortical areas (e.g., prefrontal cortex, visual cortex) contribute to the remote replay and its reward-site bias is not addressed.
- Reverse replay of inbound trajectories (pointing toward reward sites) was a key finding, but the mechanism by which the hippocampus selects reverse rather than forward replay for goal-targeting purposes remains unclear.
- The task is a working memory paradigm (trial-by-trial, no stable spatial reference); generalisation to reference memory or more complex spatial tasks is untested.
- Whether the remote replay seen in the box actually *causes* correct maze navigation (versus being correlative) is not definitively established — a causal manipulation of replay content (e.g., targeted ripple disruption) was not performed.

---

### Connections & keywords

**Key citations**:
- Pfeiffer & Foster (2013) — hippocampal place-cell sequences depict future paths to remembered goals
- Karlsson & Frank (2009) — awake replay of remote experiences
- Davidson et al. (2009) — hippocampal replay of extended experience (Bayesian decoding)
- Foster & Wilson (2006) — reverse replay during awake state
- Diba & Buzsaki (2007) — forward and reverse place-cell sequences during ripples
- Mou & Ji (2016) — social observation enhances cross-environment activation of place cell patterns
- Danjo et al. (2018) — spatial representations of self and other in the hippocampus
- Omer et al. (2018) — social place-cells in the bat hippocampus
- Jadhav et al. (2012) — awake sharp-wave ripples support spatial memory
- Carr et al. (2011) — hippocampal replay in the awake state as substrate for memory

**Named models or frameworks**:
- Bayesian decoding (Davidson et al. 2009; Zhang et al. 1998)
- Cognitive map (O'Keefe & Nadel, 1978)
- Observational working memory task (novel paradigm introduced in this paper)

**Brain regions**:
- Hippocampal CA1

**Keywords**:
- hippocampal awake replay
- remote replay
- observational learning
- place cells
- sharp-wave ripples (SWR)
- population burst events (PBEs)
- reward-site targeting
- prospective coding
- spatial working memory
- social learning
- Bayesian decoding
- forward and reverse replay
