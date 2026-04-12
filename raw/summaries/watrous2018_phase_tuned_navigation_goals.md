---
source_file: "watrous2018_phase_tuned_navigation_goals.md"
paper_id: "watrous2018_phase_tuned_navigation_goals"
title: "Phase-tuned neuronal firing encodes human contextual representations for navigational goals"
authors: "Andrew J Watrous, Jonathan Miller, Salman E Qasim, Itzhak Fried, Joshua Jacobs"
year: 2018
journal: "eLife"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
tasks: ["navigation_task"]
brain_regions: ["hippocampus", "entorhinal_cortex", "orbitofrontal_cortex", "amygdala", "medial_temporal_lobe"]
keywords: ["phase", "tuned", "neuronal", "firing", "encodes", "human", "contextual", "representations", "navigational", "goals"]
key_citations: ["ekstrom2003_spatial_navigation"]
---

### One-line summary

Human medial temporal lobe neurons encode navigational goals through phase-tuned firing to slow theta oscillations (~3 Hz), with phase coding and rate coding representing largely distinct neural populations.

---

### Background & motivation

While firing rate changes are well-established as a neural coding mechanism, converging evidence suggests that spike timing relative to oscillatory phase also contributes to neural coding. In rodents, hippocampal neurons show phase precession during navigation, where theta phase carries spatial information. The Spectro-Contextual Encoding and Retrieval Theory (SCERT) hypothesizes that phase-locked neuronal firing to low-frequency oscillations forms a basis of the human neural code. However, it remained unclear whether human MTL neurons show phase coding of navigationally relevant information beyond overall phase preferences, and whether rate and phase coding co-exist in humans as suggested by rodent studies.

---

### Methods

- **Participants**: 12 patients with drug-resistant epilepsy implanted with microwire depth electrodes for seizure monitoring
- **Recording sites**: Medial temporal lobe (hippocampus, entorhinal cortex, amygdala, parahippocampal gyrus) and frontal regions (medial prefrontal/cingulate, motor, orbitofrontal)
- **Neurons recorded**: 1,311 neurons total; 466 MTL neurons with simultaneously recorded LFPs showing 1-10 Hz oscillations for main analyses
- **Task**: Virtual taxi driver navigation task in a circular environment with 6 goal stores on the outer edge; patients navigated to deliver passengers to goal locations
- **Analysis approach**: 
  - Two-way ANOVA for rate coding (factors: goal identity, task period: planning vs. arrival)
  - MODAL (Multiple Oscillations Detection Algorithm) for adaptive detection of narrowband oscillations
  - Rayleigh tests for phase-locking
  - Cross-validated linear decoding (5-fold) to identify phase coding of goal information
  - Permutation testing (500 shuffles) for statistical significance

---

### Key findings

- **Behavioral performance**: Driving time between stores significantly decreased throughout sessions (Kruskal-Wallis, p=0.007), indicating successful learning of the environment
- **Rate coding of goals**: 53 neurons (11% of 466 MTL neurons) showed significant goal-modulated firing rates; present in hippocampus, entorhinal cortex, orbitofrontal cortex, and premotor cortex
- **Rate coding of task periods**: Significant counts of neurons in hippocampus (9/12 patients) and most areas showed firing rate modulation during navigational planning; parahippocampal and motor areas showed modulation during goal arrival
- **Phase-locking**: 144/466 MTL neurons (30%) showed significant phase-locking to low-frequency oscillations (1-10 Hz), significantly above chance; phase-locking was most prominent in hippocampus and clustered near the ascending phase of the oscillation
- **Slow theta prevalence**: 93% of MTL electrodes showed oscillations centered at ~3 Hz (slow theta); slow theta was detected most often across the population
- **Phase coding of goals**: 63 cells (10% of 627 tested) showed significant decoding of goal information from spike phases; proportion significantly above chance (Binomial p<0.0001)
- **Phase coding without rate coding**: Critically, 80% (51/63) of phase-coding cells showed no firing rate effects (p>0.1), indicating phase coding can exist independent of rate changes
- **Hippocampal specificity**: Phase coding differentially occurred in hippocampus (χ²(6)=50, p<0.0001), with 28/63 phase-coding cells from hippocampus across 9 patients
- **Task period specificity**: Distinct hippocampal populations showed phase coding during planning (24/186 neurons, 12%) vs. arrival (24/186 neurons, 12%); only 2 neurons showed both effects
- **Frequency specificity**: Phase coding was specific to slow theta; no phase coding was observed in alpha/beta bands (10-30 Hz; 5.2% vs. 5% chance)
- **Rate vs. phase coding independence**: Rate-coding and phase-coding neurons were largely non-overlapping populations; 13.6% of cells with multiple oscillation bands showed frequency-specific phase locking
- **HFA correlation**: 41% of neurons showed significant positive correlation between high-frequency activity (HFA; 65-120 Hz) and single-neuron firing; however, spike-phase coding and HFA-phase coding were not observed on the same channels

---

### Computational framework

The paper is grounded in the **Spectro-Contextual Encoding and Retrieval Theory (SCERT)** framework, which posits that frequency-specific and phase-locked neuronal firing to low-frequency oscillations forms a basis of the human neural code. The key computational ideas include:

- **Phase coding**: Information is encoded not just in firing rates but in the precise timing of spikes relative to the phase of ongoing oscillations
- **Frequency specificity**: Different oscillatory frequencies may serve distinct computational functions; slow theta (~3 Hz in humans) is particularly important for spatial/navigation processing
- **Dual coding mechanisms**: Rate coding and phase coding can coexist as independent channels of information, potentially multiplexing different types of information or supporting different computational needs
- **Oscillation as temporal reference frame**: Low-frequency oscillations provide a temporal structure that organizes neural firing into phase-specific patterns

The paper also situates its findings within broader theoretical frameworks of neural coding including the theta-phase precession model from rodent hippocampus and general theories of oscillatory phase coding (Nadasdy, 2009; Kayser et al., 2012; Lisman & Jensen, 2013).

---

### Prevailing model of the system under study

Before this paper, the field held several established views about neural coding in the human MTL during navigation:

1. **Firing rate coding of spatial goals**: Based on earlier human single-neuron studies (Ekstrom et al., 2003), it was established that human MTL neurons show increased firing rates when viewing or navigating to specific goal locations.

2. **MTL role in navigational planning**: Human imaging and lesion evidence indicated that the MTL and medial prefrontal cortex form active representations of spatial context and navigational goals to support planning, but this had not been demonstrated at the single-neuron level.

3. **Phase precession in rodents**: Extensive rodent work established that hippocampal place cells show phase precession relative to theta oscillations during navigation, where the theta phase of firing carries spatial information. However, whether similar phase coding exists in humans was unclear.

4. **SCERT predictions**: The Spectro-Contextual Encoding and Retrieval Theory (Watrous & Ekstrom, 2014) proposed that phase coding to low-frequency oscillations contributes to human neural coding, supported by prior LFP work (Watrous et al., 2015a), but this had not been demonstrated at the single-neuron level in humans.

5. **Rate vs. phase relationship**: Rodent studies suggested rate and phase coding could be independent phenomena (Huxter et al., 2003; Hyman et al., 2005), but whether this held in humans was unknown, and the relationship between high-frequency LFP activity and single-neuron phase coding was unclear.

---

### What this paper contributes

This paper provides several important advances to the understanding of neural coding in human navigation:

1. **First demonstration of single-neuron phase coding in human navigation**: The study provides the first evidence that human MTL neurons encode navigational goals through phase-tuned firing to slow theta oscillations (~3 Hz), extending previous LFP-based findings to the single-neuron level.

2. **Phase coding can exist independently of rate coding**: Critically, 80% of phase-coding neurons showed no significant firing rate modulation, demonstrating that phase coding is not merely an epiphenomenon of rate changes but represents a distinct channel of information.

3. **Coexistence of rate and phase coding as distinct populations**: The study shows that rate-coding and phase-coding neurons are largely non-overlapping populations, suggesting these coding mechanisms may serve different computational functions or convey different types of information.

4. **Single-neuron evidence for MTL involvement in navigational planning**: While prior imaging and lesion work implicated the MTL in navigational planning, this study provides the first single-neuron evidence, identifying neurons with enhanced firing during navigational planning periods.

5. **Task-specific phase coding dynamics**: Phase coding was found to be behaviorally relevant, with distinct hippocampal populations showing phase coding during navigational planning versus goal arrival periods, suggesting phase coding supports different behavioral contexts.

6. **MODAL algorithm**: The study introduces and validates a novel method for adaptive detection of narrowband oscillations that can track multiple simultaneous oscillations, advancing the methodological toolkit for analyzing human neural oscillations.

7. **Species comparison findings**: The study finds that human phase coding occurs primarily to slower theta oscillations (~3 Hz) compared to the canonical 8-Hz rodent theta, supporting the view that human navigation-related theta is slower and functionally analogous to rodent theta.

8. **Dissociation between single-neuron and HFA phase coding**: The study finds that spike-phase coding and high-frequency activity (HFA) phase coding do not occur on the same channels, suggesting functional heterogeneity in information representation within the human MTL.

---

### Brain regions & systems

- **Hippocampus**: Primary site of phase coding effects; 28 of 63 phase-coding neurons were hippocampal. Showed significant counts of goal-responsive neurons (rate coding), navigational planning neurons, and phase-locked neurons. Phase coding during both planning and arrival periods was observed. Represents the key structure for contextual representation of navigational goals.

- **Entorhinal cortex**: Site of goal-responsive neurons showing rate coding (e.g., neuron responding to goal store 3). Showed phase-locked and phase-coding neurons. Key node in the hippocampal-entorhinal navigation circuit.

- **Parahippocampal gyrus**: Showed neurons modulated during goal arrival (viewpoint-dependent scene processing). Contained phase-locked neurons. Implicated in navigational arrival and contextual processing.

- **Amygdala**: No significant counts of planning-related neurons were observed. Did show some phase-locked neurons but less prominently than hippocampal regions.

- **Orbitofrontal cortex**: Showed significant counts of goal-responsive neurons (rate coding). Part of the extended network for goal representation.

- **Premotor cortex**: Showed goal-responsive neurons. Involved in the motor planning aspects of navigation.

- **Medial prefrontal/cingulate cortex**: Recording sites included this region; implicated in navigational planning based on prior literature and part of the network showing task-related activity.

---

### Mechanistic insight

This paper provides strong mechanistic insight meeting both criteria: it presents a formal algorithmic framework and provides neural data supporting that algorithm over alternatives.

**Computational level**: The paper addresses how the brain solves the problem of representing multiple navigational goals in working memory to support planning and navigation. The computational problem is maintaining distinct representations of spatial context (which of 6 possible goals is the current target) while navigating. The SCERT framework proposes that oscillatory phase provides a temporal reference frame for encoding contextual information.

**Algorithmic level**: The paper identifies two distinct algorithmic implementations:
1. **Rate coding**: Neurons increase firing rates for specific goals (~11% of cells), with different neurons preferring different goals.
2. **Phase coding**: Neurons fire at different oscillatory phases for different goals (~10% of cells), with 80% of these showing no rate modulation.

The phase coding algorithm uses the phase of slow theta oscillations (~3 Hz) as a reference frame, with different phases carrying information about different goal states. This is implemented through spike-LFP phase relationships that are frequency-specific and behaviorally modulated.

**Implementational level**: The implementation involves:
- **Cell types**: Distinct neuronal populations in the hippocampus (primary site), entorhinal cortex, and other MTL regions implement rate vs. phase coding.
- **Connectivity**: Local circuits within the MTL generate slow theta oscillations that provide the temporal reference frame.
- **Neuromodulation**: The ~3 Hz oscillation frequency is slower than rodent theta, potentially reflecting species differences in network dynamics or neuromodulatory tone.
- **Physiological mechanisms**: The phase coding emerges from the interaction between intrinsic cellular properties (phase preferences for inputs) and network-level oscillations, with phase-locking and phase coding being related but distinct phenomena.

The paper also makes a key implementational observation: spike-phase coding and HFA-phase coding were not observed on the same channels, suggesting functional micro-heterogeneity within the MTL where adjacent cells represent different information types even as they contribute to the same LFP signal.

---

### Limitations & open questions

1. **Sample size and generalizability**: The study involved 12 epilepsy patients, which is typical for human intracranial recording studies but limits generalizability. The authors note that epilepsy involves slowing of neural oscillations, though they argue that ~3 Hz oscillations have been observed in non-epileptic patients and healthy populations.

2. **Temporal precision of task periods**: The analysis divided each delivery into planning (first half) and arrival (second half) periods, which provides equally sized windows but does not capture the precise temporal dynamics of when planning actually occurs or when goal arrival is recognized.

3. **Causal mechanisms**: The study demonstrates correlations between spike phase and goal identity but does not establish causal mechanisms. Whether phase coding is necessary for navigation or is an epiphenomenon of other processes remains unclear.

4. **Relationship between rate and phase coding**: While the study shows that 80% of phase-coding cells lack rate effects, the functional relationship between these coding mechanisms—whether they represent redundant or complementary information channels—remains unresolved.

5. **Species differences**: The study identifies slow theta (~3 Hz) as the primary frequency for phase coding in humans, slower than the canonical 8-Hz rodent theta. The functional implications of this frequency difference and whether it reflects fundamental species differences in neural dynamics or task/speed-related factors is not fully resolved.

6. **Micro-heterogeneity observation**: The finding that spike-phase coding and HFA-phase coding do not co-occur on the same channels suggests functional heterogeneity within the MTL, but the nature and functional significance of this organization remains to be understood.

---

### Connections & keywords

**Key citations**:
- Ekstrom et al., 2003 (foundational work on human place cells)
- Watrous et al., 2015a (prior LFP phase-coding work extending to single neurons)
- Watrous & Ekstrom, 2014 (SCERT theory)
- Huxter et al., 2003; Hyman et al., 2005 (rodent rate vs. phase coding independence)
- O'Keefe & Recce, 1993 (phase precession)
- Jacobs et al., 2007, 2010 (human MTL oscillations and navigation)

**Named models or frameworks**:
- SCERT (Spectro-Contextual Encoding and Retrieval Theory)
- MODAL (Multiple Oscillations Detection Algorithm)
- Phase coding / phase-locking framework
- Rate coding framework

**Brain regions**:
- Hippocampus
- Entorhinal cortex
- Parahippocampal gyrus
- Amygdala
- Orbitofrontal cortex
- Premotor cortex
- Medial prefrontal/cingulate cortex

**Keywords**:
phase coding, rate coding, theta oscillations, slow theta, human hippocampus, medial temporal lobe, navigation, spatial memory, goal-directed behavior, single-neuron recordings, intracranial recordings, virtual reality, oscillatory phase, spike-LFP coupling, SCERT, MODAL, phase-locking, navigational planning, episodic memory
