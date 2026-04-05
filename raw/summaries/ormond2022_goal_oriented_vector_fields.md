---
source_file: ormond2022_goal_oriented_vector_fields.md
title: Hippocampal place cells have goal-oriented vector fields during navigation
authors: Jake Ormond, John O'Keefe
year: 2022
journal: Nature
paper_type: empirical
contribution_type: empirical
---

### One-line summary

A subset of CA1 hippocampal place cells in rats fire as egocentric vector fields oriented toward goal-proximal "convergence sinks" (ConSinks), forming a population-level navigational signal that points toward the goal and updates when the goal moves.

---

### Background & motivation

Hippocampal place cells are well established as providing a world-centred positional code, but how this spatial representation supports flexible, goal-directed navigation — particularly along indirect routes — has been unclear. In open-field foraging, place cells are largely omnidirectional, yet goal-directed tasks render them directional. Prior studies could not fully assess non-goalward firing because animals tend to travel directly toward the goal, leaving the directional tuning profile undersampled. The honeycomb maze, which forces binary choices at every step and elicits full 360° scanning at each choice point, allows veridical characterisation of directional firing across all headings at every position on the maze.

---

### Methods

- **Subjects**: Five male Lister hooded rats with bilateral tetrode arrays (32 tetrodes, 16 per hemisphere) targeting dorsal CA1.
- **Task**: Honeycomb maze (61 hexagonal platforms, ~200 cm across). Rats navigated to a fixed goal via a series of binary platform choices; the maze was rotated 30° and wiped with ethanol every four trials to prevent scent-trail use. A second recording session tested goal-shift (goal 1 → goal 2 within a single session).
- **Comparison condition**: Same cells recorded during open-field foraging (all platforms raised) within the same session.
- **Place cell identification**: Cells with significant spatial information (Skaggs et al. 1993) and spatial coherence (Muller & Kubie 1989) from spike-sorted tetrode data (KiloSort + Phy). Total: 456 cells (navigation session), 360 cells (goal-shift session).
- **ConSink analysis**: The arena was tiled with candidate sink positions (~7-cm grid). For each candidate, the egocentric heading relative to that position was computed per spike, and the mean resultant length (MRL) of the resulting circular distribution was calculated. The candidate position with the maximum MRL was the ConSink. Significance was assessed against two shuffle controls (head-direction shuffle and spike-train time shift).
- **Encoding analysis**: Linear-nonlinear Poisson (LN) nested models tested whether individual ConSink cells encoded relative direction, distance, and/or allocentric direction to the sink, and identified the simplest significant variable combination via tenfold cross-validation.
- **Error analysis**: Firing rates during two 4-s wait periods before correct vs. error choices were compared to dissociate spatial representation from impending action selection.
- **Statistics**: Non-parametric two-sided tests throughout (Wilcoxon signed-rank, Wilcoxon rank-sum, Rayleigh test); no pre-determined sample sizes.

---

### Key findings

- 31.1% of CA1 place cells (142/456) displayed significant ConSink tuning during goal-directed navigation; mean preferred relative direction = −6.20° (not significantly different from 0°, i.e. cells fire when the animal faces the sink).
- ConSink positions were distributed across and beyond the maze but were significantly denser near the goal than near an anti-goal control location (z = −4.92, p = 8.6 × 10⁻⁷).
- Population vector fields (summing platform-associated vectors across ConSink cells) converged to a population ConSink close to the goal for all five animals.
- After a goal switch, ConSinks redistributed from the original goal to the new goal; cells with ConSinks during both goal epochs (n = 28) moved their ConSinks significantly toward the new goal (Wilcoxon signed-rank, z = −2.48, p = 0.013). ConSinks moved progressively closer to the goal with continued training, both across trials within a day and after a goal switch.
- 86.6% of ConSink cells (123/142) significantly encoded at least one of: relative direction, distance, or allocentric direction to the sink; 57% encoded combinations sufficient to calculate the full goal direction vector from any location.
- Population firing rate varied monotonically with angular deviation from the goal direction, forming a "fantail" pattern that provides sufficient information to choose between any available pair of platforms.
- Only 13% of place cells showed ConSink tuning during open-field foraging (vs. 31% during navigation), and foraging ConSinks were not clustered around the navigation goal.
- Before error choices (during both wait periods 1 and 2), goal-directed firing rates were significantly reduced (z = 5.61, p = 1.97 × 10⁻⁸ for wait period 1) and the fantail was rotated away from the goal, even before the animal knew which platforms would be offered — suggesting the firing predicts choice rather than merely accompanying movement.

---

### Computational framework

The paper uses a **vector-field / egocentric goal-coding** framework, closely related to the cognitive map tradition but formalising place cell activity as spatially varying egocentric direction fields rather than pure positional codes.

Core formalism: each ConSink cell fires maximally when the animal's head direction is aligned with the egocentric direction from the animal to a fixed environmental point (the ConSink). The cell's tuning is therefore characterised by three quantities — relative direction to the sink, distance to the sink, and allocentric direction to the sink — any combination of which can be used to reconstruct the goal vector. At the population level, the sum of ConSink cell vectors converges on a population ConSink near the goal. The "fantail" describes how population firing rate decreases monotonically as a function of angular deviation from the goal direction; the animal can navigate by following the direction of highest population rate.

Key assumptions: ConSinks are featureless locations learned through repeated goal-directed experience; they do not correspond to the place field centres of the encoding cells; and the navigational signal is graded rather than binary, allowing probabilistic choice between available paths.

---

### Prevailing model of the system under study

The introduction situates the work against the standard cognitive map framework (O'Keefe & Nadel, 1978): CA1 place cells provide an allocentric, world-centred representation of current position, and this positional code is generally treated as non-directional during unconstrained foraging. The prevailing model acknowledged that place cells become directional when goals are present (McNaughton et al., 1983) and that place fields move toward goals (Dupret et al., 2010; Kobayashi et al., 1997), but there was no account of how the spatial code is organised at a population level to actually generate navigational decisions — particularly in the case where no direct path to the goal is available. The paper also engages with prior reports of goal-heading cells in bats (Sarel et al., 2017), mice (Jercog et al., 2019), primates, and humans, noting that these studies could not assess non-goalward firing because animals predominantly travelled directly toward the goal.

---

### What this paper contributes

The paper provides the first systematic demonstration that a substantial fraction of CA1 place cells are tuned not simply to heading toward the goal but to heading toward learned intermediate spatial anchors (ConSinks) distributed around the environment and concentrated near the goal. This extends the prevailing model in three ways:

1. **Population geometry**: the spatial representation is not just a position code plus a goal-direction signal; it has a vector-field structure in which population firing rate encodes graded proximity to the goal direction from every location, enabling optimal choice in indirect-path scenarios.
2. **Learning dynamics**: ConSinks are not fixed anatomical landmarks — they emerge and move with experience, concentrating around the current goal and shifting to a new goal within a single session. Importantly, this reorganisation is faster than remapping of place fields, implying partially dissociable mechanisms.
3. **Representation–action dissociation**: because wait periods precede knowledge of upcoming choices, the observation that correct-choice trials have stronger, more goal-directed firing establishes that the vector-field representation is a causal antecedent of — not merely a correlate of — spatial behaviour.

---

### Brain regions & systems

- **Dorsal CA1 (hippocampus)** — the sole recording site; proposed as the locus of the vector-field / ConSink representation that supports flexible goal navigation.

No other brain regions are directly studied. The paper briefly notes that ConSink-like cells have been reported in lateral entorhinal cortex and postrhinal cortex in other species, but these regions are not investigated here.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight.

**Criterion 1 (algorithm)**: The paper formalises a specific algorithm — egocentric heading-to-ConSink tuning, aggregated across a population of cells with ConSinks distributed near the goal, producing a fantail population code that monotonically encodes deviation from the goal direction. This algorithm is specified mathematically (LN models, vector summation, MRL) and is shown to be computationally sufficient for solving the maze task.

**Criterion 2 (neural data supporting the algorithm)**: Direct tetrode recordings from identified CA1 pyramidal cells during behaviour provide evidence for this specific algorithm: the ConSink tuning is stronger than allocentric head-direction tuning in every ConSink cell; population vector fields converge on goal-proximal locations; the fantail pattern is present on correct trials and disrupted on error trials before choice; and ConSinks reorganise with goal learning, not simply with place-field remapping.

**Marr's levels:**

- **Computational**: The brain must compute, from any location in a familiar environment, a direction vector pointing toward the goal, even when direct paths are unavailable. It must also compare the goal-proximity value of any two paths simultaneously available.
- **Algorithmic**: CA1 ConSink cells encode egocentric heading relative to learned spatial anchors (ConSinks), multiplexing relative direction, distance, and allocentric direction. At the population level, firing rate varies as the cosine of angular deviation from the goal direction (the fantail), allowing simple readout of the optimal choice as the direction with the highest population firing rate.
- **Implementational**: Recordings are from identified CA1 pyramidal cells using tetrodes in freely moving rats. The paper does not address specific cell types, interneurons, neuromodulatory mechanisms, or synaptic plasticity rules; it does note that ConSink reorganisation appears faster than place-field remapping, suggesting a distinct plasticity substrate, but this is not directly investigated.

---

### Limitations & open questions

- The mechanism by which ConSinks are created, positioned, or updated is unknown. The paper acknowledges this explicitly.
- It is unresolved whether ConSink cells are a distinct cell type or whether any place cell can acquire ConSink tuning depending on experience.
- The reinforcement mechanism — what drives ConSinks to cluster near the goal — is uncharacterised.
- The paper cannot determine whether the difference in ConSink prevalence between the navigation and foraging tasks is due to the goal context per se, or to differences in maze structure between the two configurations.
- All five animals could not be included in the goal-switch analysis (rat 5 required multiple days to learn the new goal), limiting within-session comparison for that animal.
- The study records only from dorsal CA1; it is unknown whether the ConSink signal originates there or is inherited from entorhinal or subcortical inputs.
- The translation from the spatial representation (ConSink vector fields) to the motor output (choice platform selection) is not addressed.

---

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) — *The Hippocampus as a Cognitive Map* (foundational framework)
- Wood et al. (2018), *Nature* — original honeycomb maze paper
- Sarel et al. (2017), *Science* — vectorial goal representations in bat hippocampus
- Jercog et al. (2019), *Nature Communications* — heading relative to reference points modulates mouse place cells
- Dupret et al. (2010), *Nature Neuroscience* — place field reorganisation toward goals and memory
- McNaughton et al. (1983), *Experimental Brain Research* — directional place cell firing in linear tracks
- Hardcastle et al. (2017), *Neuron* — LN modelling approach for mixed selectivity
- Redish (2016), *Nature Reviews Neuroscience* — vicarious trial and error

**Named models or frameworks:**
- Cognitive map (O'Keefe & Nadel)
- Convergence sink (ConSink) — introduced in this paper
- Fantail model — introduced in this paper
- Linear-nonlinear Poisson (LN) nested model (Hardcastle et al. 2017)
- Honeycomb maze (Wood et al. 2018)

**Brain regions:**
- Dorsal CA1 (hippocampus)

**Keywords:**
- hippocampal place cells
- goal-directed navigation
- convergence sink (ConSink)
- egocentric heading coding
- vector field representation
- cognitive map
- honeycomb maze
- directional place cell tuning
- population vector coding
- reward location remapping
- spatial action selection
- vicarious trial and error
