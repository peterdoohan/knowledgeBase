---
source_file: berners2022_hippocampal_replay_experience.md
title: Hippocampal replays appear after a single experience and incorporate greater detail with more experience
authors: Alice Berners-Lee, Ting Feng, Delia Silva, Xiaojing Wu, Ellen R. Ambrose, Brad E. Pfeiffer, David J. Foster
year: 2022
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Hippocampal replay emerges after a single lap on a novel track and progressively slows down with repeated experience by adding more, finer-grained hover locations — reflecting incremental incorporation of spatial detail into replay memories.

---

### Background & motivation

Hippocampal (HP) replay — the reactivation of place cell sequences during rest — has been proposed as a substrate for spatial memory, but it was unclear how rapidly replay forms and how it changes with re-exposure to the same environment. Prior work typically studied replay only after animals had run dozens of trials, leaving the one-trial development and moment-by-moment evolution of replay unexplored. This paper addresses when replay first appears, whether it persists, and how repeated experience modifies the temporal and spatial content of replay sequences.

---

### Methods

- **Subjects**: 17 male Long-Evans rats; high-density tetrode recordings of up to hundreds of CA1 pyramidal neurons simultaneously in freely moving animals.
- **Task designs**:
  - *One-lap experiment*: Pre-Rest → 1–2 passes on novel linear track (Run 1) → >1-hour Rest → multi-pass Run 2.
  - *Novel multi-pass experiment*: multiple sessions on novel tracks; replay analyzed per stopping period after each pass.
  - *Remote replay experiment*: two novel tracks (A then B) with intervening rest; local vs. remote replays compared.
  - *Time-control experiments*: rest-only periods after single pass or full session to isolate experience from elapsed time.
  - *Interneuron and PFC experiments*: simultaneous recordings of HP interneurons (from two datasets, including Grosmark et al., 2016) and PFC neurons (from Wu & Foster, 2014 dataset) during replay.
- **Replay detection**: candidate events (100–500 ms elevated population spiking); memoryless Bayesian position decoding (2.5-cm bins, 20-ms time bins); significance assessed via weighted correlation × maximum jump distance threshold matrix compared against 5,000 shuffles.
- **Hover-and-jump analysis**: slow-gamma (25–50 Hz) phase-locking of steps within replays; step count, step size, hover location distributions tracked across passes.
- **Key measures**: replay duration, slope (speed), number of steps, step size, hover location distributions, interneuron modulation index, PFC firing rate during short vs. long replays.

---

### Key findings

- Significant replay was detected after a single pass on a novel track and persisted for at least 1 hour during subsequent rest (post-experience Rest p = 2.0e−4 vs. pre-experience Pre-Rest p = 0.39 across diagnostic parameters).
- Replay duration increased (R = 0.14, p = 8e−9) and slope (speed) decreased (R = −0.054, p = 0.03) across the first 14 passes on novel tracks; these changes were not observed on familiar tracks.
- Slowing was environment-specific: remote replays of a previously explored track (Track A) did not slow while the rat gained experience on a new track (Track B); local replays of the current environment did slow (R = 0.13, p = 8.6e−6).
- Replay slowing was experience-dependent, not time-dependent: replays did not lengthen during rest periods following either a single pass or a full session; slowing resumed only upon return to active running.
- Within the hover-and-jump framework, replay slowed by increasing step number (R = 0.097, p = 1.0e−4) while decreasing step size (R = −0.044, p = 3.0e−5); hover duration, step duration, gamma frequency, and gamma power remained constant.
- Hover locations were consistent across experience (mean pairwise correlation = 0.54, Monte-Carlo p = 0.001); early replays sampled fewer unique hover locations than expected by chance (Monte-Carlo p = 0.022), supporting an insertion rather than a sampling model of detail acquisition.
- HP interneuron modulation to replay increased across passes in two independent datasets (own dataset: N = 19, Z = 2.4, p = 9.3e−3; Grosmark dataset: N = 82, Z = 2.9, p = 2.0e−3).
- PFC neurons remained modulated for longer during long versus short replays (80–160 ms post-replay: Z = −2.7, p = 3.5e−3), suggesting longer replays engage cortical processing more extensively.

---

### Computational framework

The paper uses an **attractor network** framework to interpret hover-and-jump dynamics. Replay is conceptualized as sequential transitions between attractor states, where each "hover" corresponds to dwelling in a low-energy attractor basin representing a particular spatial location, and "jumps" reflect transitions between basins driven by asymmetric synaptic weights established during running.

Key variables: attractor stability (indexed by hover location consistency), inhibitory tone (interneuron modulation), and synaptic connection strength between place cells encoding nearby positions. The model assumes that early in learning, weak synaptic connections and low inhibition permit large jumps between distant representations; with experience, strengthened connections and increased inhibition produce smaller, more numerous steps.

The paper also invokes a **reinforcement learning** framework in the discussion, proposing that the temporal extent of replay acts as an eligibility trace analogous to TD(λ): fast early replays implement a long eligibility window (large λ), which shrinks as learning proceeds — consistent with normative recommendations for bias-variance tradeoff management.

---

### Prevailing model of the system under study

The field understood hippocampal replay as compressed sequential reactivation of place cell sequences occurring during sharp-wave ripples (SWRs) in rest or sleep, proposed to mediate memory consolidation and retrieval. Prior work established that replay rates increase with novelty and that various properties of HP activity (place field emergence, theta sequences, co-firing coordination) develop across trials on a novel track. However, the dominant assumption was that replay required substantial prior experience — studies typically examined replay only after dozens of runs — and whether replay could form from a single experience, persist, and then systematically change in content with re-exposure was unaddressed. The hover-and-jump structure of replay at the slow-gamma timescale (Pfeiffer & Foster, 2015) was established but its experience-dependence was not known.

---

### What this paper contributes

The paper establishes that replay is a one-trial phenomenon: a single pass suffices to produce sustained, significant replay lasting over an hour. This substantially lowers the learning threshold implied by prior work. Beyond onset, the paper reveals that replay is not static: it becomes progressively slower and richer in spatial detail with each additional lap — not via changes to the underlying gamma dynamics, but by inserting new hover locations. This reframes replay not as a fixed record of a single experience but as an incrementally updated world model that grows in resolution with re-exposure. The experience-specificity (local but not remote replays slow; familiar tracks show no slowing; reward changes alone are insufficient) pins the mechanism to encoding processes tied to environmental novelty rather than global state changes or time. The concurrent increase in interneuron modulation and extended PFC engagement during longer replays provides the first evidence linking replay elaboration to both a candidate inhibitory mechanism and to enhanced downstream cortical processing.

---

### Brain regions & systems

- **Hippocampus (CA1)** — primary recording site; source of place cell sequences constituting replay; locus of hover-and-jump attractor dynamics and interneuron-mediated inhibitory control.
- **Prefrontal cortex (PFC)** — recorded simultaneously with HP; shows prolonged modulation during longer replays, consistent with a role in receiving or processing replayed content during memory consolidation.
- **HP interneurons** — recorded within CA1; their increasing modulation to replay across passes is proposed as a mechanism enabling the transition from fast, coarse-grained to slow, fine-grained replay.

---

### Mechanistic insight

The paper meets both criteria for a mechanistic account.

**Computational**: The brain is solving the problem of building a progressively detailed spatial model of a novel environment. Early replay captures the gist of a trajectory (coarse, fast); with experience, replay incorporates finer positional detail, potentially supporting more accurate memory-guided behaviour.

**Algorithmic**: The hover-and-jump structure implements replay as sequential attractor transitions. The number of attractors (hover locations) visited per replay event grows with experience, not by changing individual gamma-cycle dynamics but by inserting new stable attractor states. The ordering of hover locations is consistent across experience, indicating that new attractors are inserted into an existing sequential structure rather than replacing it.

**Implementational**: Interneuron firing modulation during replay increases across passes (two independent datasets), and the paper proposes that low inhibition early in learning permits large representational jumps, while increasing inhibition later constrains step size, yielding finer spatial sampling. Synaptic strengthening between co-active place cells across laps is proposed to establish the new attractor basins. PFC engagement scales with replay duration, indicating downstream consequences of the lengthening. However, the specific cell types mediating inhibition, the synaptic loci of plasticity, and the neuromodulatory signals (locus coeruleus/dopamine are hypothesised but not tested) remain to be determined.

---

### Limitations & open questions

- Interneuron yield was low in the primary dataset (median 1 per session); the effect was confirmed in a secondary publicly available dataset but the specific interneuron subtypes (e.g., PV vs. SOM) are not identified.
- Physical correlates of hover locations (spatial inhomogeneities in stimuli, barriers, or animal behaviour) were not detected; head-scanning or vicarious trial-and-error could contribute but were not examined.
- The paper does not address multi-day dynamics: whether replay slowing reverses as the environment becomes familiar over days is not tested, though other work suggests it might.
- The proposed inhibitory mechanism (low inhibition → large jumps, high inhibition → small steps) is not directly tested; causal manipulation of inhibitory tone during stopping periods is proposed as a future experiment.
- Whether the same elaboration process applies to non-linear environments (mazes with topology) or to non-spatial episodic memories is unknown.
- The relationship between concatenated ripple bouts and gamma-timescale steps is not resolved; the paper cannot rule out that multi-ripple events underlie multi-step replays.
- The locus coeruleus/dopamine hypothesis for novelty-dependent slowing is not tested experimentally.

---

### Connections & keywords

**Key citations**:
- Foster & Wilson (2006) — reverse replay after a single experience; baseline for one-trial replay
- Silva et al. (2015) — trajectory events require prior experience; significance matrix methodology
- Pfeiffer & Foster (2015) — hover-and-jump dynamics and slow-gamma structure of replay
- Cheng & Frank (2008) — coordinated HP activity increases with novel experience across days
- Grosmark et al. (2016) — public dataset used to replicate interneuron findings
- Fernández-Ruiz et al. (2019) — optogenetic prolongation of sharp-wave ripples improves memory
- Buzsáki (2015) — SWR as cognitive biomarker for episodic memory
- Lengyel & Dayan (2008) — hippocampal episodic memory and gist-based control
- Gershman & Daw (2017) — RL and episodic memory integrative framework

**Named models or frameworks**:
- Hover-and-jump dynamics (Pfeiffer & Foster, 2015)
- Memoryless Bayesian position decoding
- TD(λ) eligibility trace analogy for replay speed

**Brain regions**:
- Hippocampus (CA1)
- Prefrontal cortex (PFC)
- Hippocampal interneurons

**Keywords**:
- hippocampal replay
- sharp-wave ripples
- place cells
- one-trial learning
- experience-dependent plasticity
- hover-and-jump dynamics
- slow gamma oscillations
- attractor network
- spatial memory consolidation
- replay speed
- interneuron modulation
- hippocampal-prefrontal interaction
