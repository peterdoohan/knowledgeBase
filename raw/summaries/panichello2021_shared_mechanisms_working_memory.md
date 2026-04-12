---
source_file: "panichello2021_shared_mechanisms_working_memory.md"
paper_id: "panichello2021_shared_mechanisms_working_memory"
title: "Shared mechanisms underlie the control of working memory and attention"
authors: "Matthew F. Panichello, Timothy J. Buschman"
year: 2021
journal: "Nature"
paper_type: "empirical"
contribution_type: "empirical"
species: ["macaque"]
methods: ["electrophysiology", "behavioral_analysis"]
brain_regions: ["prefrontal_cortex"]
frameworks: ["mixed_selectivity"]
keywords: ["shared", "mechanisms", "underlie", "control", "working", "memory", "attention"]
---

### One-line summary

Lateral prefrontal cortex acts as a domain-general controller by encoding selection from working memory and attention to sensory stimuli in a shared population representation, while both operations transform item representations from independent subspaces into a common behavioural template subspace.

---

### Background & motivation

Cognitive control guides behaviour by regulating what information is represented in the brain and when. Attention is known to control sensory processing via top-down signals from prefrontal and parietal cortex, and a functionally analogous "selection" mechanism has been proposed to control which item is prioritised within working memory. However, whether these two forms of control — attention and working memory selection — share a common neural substrate or are implemented by distinct mechanisms had not been tested directly with simultaneous multi-region recordings at the population level. This paper fills that gap by asking whether the same prefrontal circuits that deploy attention to sensory inputs also implement the selection of items held in mind.

---

### Methods

- **Subjects**: Two adult male rhesus macaques (8–9 years old).
- **Task design**: Animals switched between two tasks in a blocked fashion:
  - *Retrospective (retro) task*: Two coloured squares were encoded into working memory; after a delay, a spatial cue indicated which item (upper/lower) to select and report by saccade to a colour wheel.
  - *Prospective (pro) task*: The spatial cue was presented before the stimuli, allowing the animal to attend to the relevant location during encoding. A single continuous delay preceded the response.
  - A subset of trials presented only one item to assess baseline memory performance. Colour was drawn from a photometrically isoluminant CIELAB circle (64 possible values). Response error was the angular deviation between presented and reported colour.
- **Neural recordings**: Simultaneous multi-electrode recordings across four regions per session (23 sessions total): lateral prefrontal cortex (LPFC, 682 neurons), frontal eye fields (FEF, 187 neurons), parietal cortex (area 7a/b, 331 neurons), and visual area V4 (341 neurons).
- **Analysis approach**:
  - Logistic regression classifiers trained to decode cued location (upper/lower) from pseudo-population firing rates; cross-task generalisation tested by training on retro and testing on pro trials (and vice versa).
  - Colour information quantified using a normalised circular entropy (colour modulation index); z-scored and compared across selected/non-selected items and across time.
  - Geometry of mnemonic representations examined via PCA of population activity, fitting colour planes to upper/lower item representations, and measuring the cosine of the angle between planes before and after the selection cue.
  - Subspace alignment between retro and pro trials tested via correlation of population vectors at matched time points.

---

### Key findings

- **Behavioural**: Mean absolute angular error was 51.8° (retro, two items), 46.1° (pro), and 38.1° (single item). Earlier retro cues improved precision (β = 4.67°/s, P < 0.001). Pro trials showed smaller load-induced error increase (9.01° vs. 13.7° for pro vs. retro).
- **Selection signal timing**: Above-chance classification of the cued location emerged first in LPFC (175 ms post-cue), then FEF (245 ms), parietal (285 ms), and V4 (335 ms). LPFC onset was significantly earlier than parietal (P = 0.005) and V4 (P = 0.048).
- **Shared population code in LPFC**: Classifiers trained on retro trials generalised significantly to pro trials (and vice versa) in LPFC, following the time course of the selection classifier. Individual LPFC neurons also showed correlated selectivity across the two tasks (r = 0.09, P = 0.036).
- **Independent representations in posterior regions**: Generalisation was non-significant in parietal cortex and V4; FEF showed a trend (P = 0.12). Single-neuron correlations were non-significant in FEF, V4, and parietal.
- **Enhancement of memory representations**: Selection increased colour information about the selected item in LPFC (from 475 ms post-cue), FEF (715 ms), and parietal (565 ms). On inaccurate trials, the selection enhancement was absent in LPFC, FEF, and parietal, linking it to behavioural outcome.
- **Subspace geometry — pre-selection**: Before the cue, LPFC encoded upper and lower items in near-orthogonal subspaces (median angle between colour planes: 79.1°, IQR 71.4–85.1°). Overlapping but distinguishable neural populations: 31–35% of colour-selective neurons encoded both items, but upper and lower colour vectors were mildly anti-correlated (mean r = −0.067, P = 0.009).
- **Subspace transformation — post-selection**: Selection caused the selected item's representation to move from its item-specific subspace into a new, common "template" subspace. The angle between upper and lower colour planes decreased from ~79° to ~20° (IQR 11.6–29.0°) post-cue (P = 0.006). Colour area in the post-selection subspace increased from 27.8 to 261.9 units² (P < 0.001). The degree of this transformation correlated with behavioural accuracy (P = 0.027).
- **Pro task alignment**: On pro trials, colour planes were aligned from immediately after stimulus offset (early median angle ~34.5°; no significant change over time). The post-selection template subspace on retro trials and the pro trial subspace were weakly but significantly correlated (mean ρ = 0.06, P = 0.015), emerging only after selection.
- **Gradient across regions**: The degree of the subspace transformation decreased progressively from LPFC through FEF, parietal, to V4, consistent with a gradient from flexible, integrative prefrontal representations to more static visual-cortex representations.

---

### Computational framework

The paper does not explicitly adopt a named computational framework, but its analysis and interpretation are grounded in the framework of **neural population geometry / subspace decomposition**. The key formalisms are:

- Representations are described as vectors in a high-dimensional neural state space. Multiple items are encoded in **orthogonal subspaces** of this space, allowing simultaneous maintenance without mutual interference.
- **Cognitive control operates as a linear transformation**: selection rotates the population representation of a target item from its item-specific subspace into a shared, read-out-accessible "template" subspace.
- The paper uses PCA to identify 2D "colour planes" for each item location, measures their angular separation over time, and tracks the alignment of these planes relative to task events.
- The conceptual model is that the **dimensionality and geometry** of prefrontal representations determines what downstream circuits can read out, and that control is implemented by dynamically reconfiguring this geometry rather than by gating or inhibition per se.

---

### Prevailing model of the system under study

The introduction frames the field as holding two separate but analogous accounts: (1) **attention** selects among sensory inputs via top-down signals from prefrontal and parietal cortex that amplify the neural representation of task-relevant stimuli; and (2) a structurally similar "internal attention" or **retrospective cueing** mechanism selects items from working memory, restoring or strengthening their neural representation. The shared assumption in the literature was functional homology — both processes reduce interference and enhance target representations — but whether they shared the same neural circuitry or were implemented by anatomically and representationally distinct systems was an open question. The implicit baseline model treated attention and working memory selection as parallel but potentially separable processes, with prefrontal, parietal, and visual cortex each contributing differently. Existing human neuroimaging work had suggested common activations, but population-level representational geometry in nonhuman primates had not been characterised.

---

### What this paper contributes

The paper establishes three concrete advances beyond the prior functional homology hypothesis:

1. **Shared population code in LPFC**: Cross-task generalisation of logistic regression classifiers demonstrates that LPFC encodes the control signal (which item/location is selected or attended) in a common population representation — not merely that it activates during both tasks.
2. **Domain-specific representations in posterior cortex**: FEF, parietal, and V4 maintain task-specific representations of selection and attention, distinguishing them from LPFC. This dissociates a domain-general prefrontal controller from domain-specific posterior modules.
3. **Subspace transformation as the mechanistic act of selection**: Before selection, working memory items are encoded in orthogonal subspaces, which protects items from mutual interference. Selection causes the target item's representation to rotate into a common "template" subspace accessible to downstream read-out circuits. This transformation — not just a gain change — is tracked quantitatively across time, correlates with behavioural accuracy, and mirrors what happens during attention (alignment is immediate on pro trials). This provides a geometrical account of how cognitive control changes "what and when" cognitive computations are engaged.

---

### Brain regions & systems

- **Lateral prefrontal cortex (LPFC)** — domain-general controller; encodes a shared population representation of both selection and attention; first region to represent the selection signal; site of the subspace transformation linking item-specific to template representations.
- **Frontal eye fields (FEF)** — carries selection and attention information but in independent (non-generalising) population codes; represents the selection signal slightly later than LPFC; shows some subspace transformation, albeit weaker.
- **Parietal cortex (area 7a/b)** — encodes selection and attention independently; carries colour information; limited subspace transformation; plays a role in maintenance and enhancement of selected memories but does not generalise across tasks.
- **Visual area V4** — latest to represent the selection signal; encodes colour information; no significant cross-task generalisation of the control signal; colour enhancement by selection is linked to behavioural accuracy but not consistently to the selection cue; least flexible geometry.

---

### Mechanistic insight

This paper meets both criteria for the high bar: it formalises an algorithm (orthogonal subspace encoding followed by selection-driven rotation into a template subspace) and provides neural recordings that specifically support this algorithm.

**Computational**: The brain must simultaneously maintain multiple distinct items in working memory without mutual interference, yet be able to rapidly render one item accessible to output circuits on demand. The problem is to separate storage from retrieval flexibility.

**Algorithmic**: Items are stored in near-orthogonal subspaces of LPFC population activity (pre-selection median angle ~79°), which minimises representational interference. A selection cue triggers a transformation — formalised as the rotation of the selected item's colour plane into a common template subspace (post-selection angle ~20°) — that makes the selected colour readable by any downstream circuit monitoring that subspace. The non-selected item is simultaneously re-encoded into a subspace nearly orthogonal to the template (~80°), preventing it from interfering with the read-out. The same template subspace is used on pro trials from the outset, establishing representational convergence across the two forms of cognitive control.

**Implementational**: The paper provides single-unit and population-level data from LPFC, FEF, parietal, and V4. Mixed selectivity (31–35% of LPFC neurons encoding both items, Rigotti et al. 2013) is invoked as the substrate for the overlapping but geometrically separated codes. The temporal hierarchy (LPFC earliest, V4 latest, both for selection signal and subspace transformation) implies that LPFC initiates the transformation and propagates it downstream. However, the paper does not identify specific cell types, connectivity motifs, or neuromodulatory mechanisms, so the implementation in neural hardware is inferred from population dynamics rather than directly characterised.

---

### Limitations & open questions

- Only two monkeys; sessions were recorded acutely with tungsten electrodes, limiting single-unit yield and long-term stability.
- The analysis relies on pseudo-populations assembled across sessions, which cannot capture within-session population dynamics or noise correlations.
- The subspace transformation is described geometrically but the circuit mechanism generating it is not identified — the paper cannot distinguish whether LPFC reorganises its own representations autonomously, receives a top-down control signal, or is driven by a feedback loop with subcortical structures.
- Selection did not suppress the non-selected memory (unlike attention suppressing non-attended stimuli), leaving open why these two otherwise homologous operations differ in their competitive dynamics.
- The degree of cross-task generalisation in LPFC, while significant, is modest (individual neuron correlation r = 0.09), raising the question of whether the shared code is a minor component of a larger task-specific code.
- The paper focuses on spatial selection (upper/lower); whether the same geometry applies when selection is feature-based rather than location-based is untested.
- The functional consequence of the gradient of transformation across LPFC → FEF → parietal → V4 is not traced to downstream read-out circuits.

---

### Connections & keywords

**Key citations**:
- Miller & Cohen (2001) — integrative theory of PFC function
- Buschman & Kastner (2015) — integrated theory of attention
- Gazzaley & Nobre (2012) — top-down modulation bridging attention and working memory
- Myers, Stokes & Nobre (2017) — prioritisation in working memory beyond sustained attention
- Rigotti et al. (2013) — importance of mixed selectivity in complex cognitive tasks
- Bernardi et al. (2020) — geometry of abstraction in hippocampus and PFC
- Sprague, Ester & Serences (2016) — restoring latent visual WM representations
- Bouchacourt & Buschman (2019) — flexible model of working memory
- Panichello et al. (2019) — error-correcting dynamics in visual working memory

**Named models or frameworks**:
- Retrospective cueing (retrocue) paradigm
- Neural population geometry / subspace decomposition framework
- Domain-general controller model of LPFC

**Brain regions**:
- Lateral prefrontal cortex (LPFC)
- Frontal eye fields (FEF)
- Parietal cortex (area 7a/b)
- Visual area V4

**Keywords**:
- working memory selection
- retrospective cueing
- spatial attention
- prefrontal cortex population geometry
- neural subspace decomposition
- orthogonal item encoding
- representational transformation
- domain-general control
- mixed selectivity
- cross-task generalisation
- colour wheel delayed estimation
- non-human primate electrophysiology
