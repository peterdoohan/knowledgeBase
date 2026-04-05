---
source_file: nagelhus2023_population_coding.md
title: "Object-centered population coding in CA1 of the hippocampus"
authors: Anne Nagelhus, Sebastian O. Andersson, Soledad Gonzalo Cogno, Edvard I. Moser, May-Britt Moser
year: 2023
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Large-scale simultaneous recordings in hippocampal CA1 reveal that object-related information is encoded as a distributed, emergent population-level property, with population activity reorganising smoothly and continuously as a function of the animal's distance from an object rather than through dedicated object-coding cell types.

---

### Background & motivation

Objects and landmarks are critical components of the brain's cognitive map of space, yet prior work on object coding in the hippocampus has focused predominantly on single-cell responses — object cells and object-vector cells — recorded in relatively small numbers. It remained unclear whether these individual cell types fully capture how the hippocampus represents objects, or whether object information is more broadly distributed across the population. The paper addresses this gap by recording from up to 620 CA1 neurons simultaneously, enabling a population-level characterisation of object coding that was not previously feasible.

---

### Methods

- **Subjects**: 10 male Long-Evans rats (2–3.5 months old at implantation).
- **Recording techniques**: Tetrode implants (7 rats, 25–39 simultaneously recorded cells per session) and Neuropixels 2.0 silicon probes (2 rats, up to 620 cells recorded simultaneously); targeting CA1 (and occasionally CA3) of the hippocampus.
- **Task design**: Rats freely foraged in a 150 cm × 150 cm open-field arena across four consecutive trials per session: (1) no object (NO), (2) object present (O; a 52 × 10 × 10 cm Duplo tower), (3) object moved to a new location (OM), (4) object removed (NO'). Control sessions used four consecutive empty-arena trials.
- **Single-cell analysis**: An iterative template-matching procedure (520 hypothesis tests per cell using Gaussian templates at varying distances, orientations, and widths) classified cells as object-tuned; spatial correlation and rate-overlap metrics quantified trial-by-trial changes.
- **Population decoding**: A Bayesian decoder (adapted from Posani et al., 2017) inferred trial identity (NO vs. O) from population activity vectors in 1 s bins, partitioned by distance and allocentric angle relative to the object.
- **Population coding analyses**: "Words" (unique 10 ms binary spike patterns across the population) and "counts" (total spikes per bin) were used to compute mutual information between population activity and trial type. Kullback-Leibler divergence between word-frequency distributions in NO and O trials was calculated as a function of object distance.
- **Distributed coding analysis**: Decoding was repeated across random subsets of cells (n = 1 to 500) and across subsets retaining cells with the lowest individual distance-tuning scores.
- **Behavioural controls**: Separate decoders used speed, head direction, and occupancy to test whether behavioural differences between NO and O trials could explain neural decoding results; speed/head-direction/occupancy distributions were also subsampled to match between trials before re-running the neural decoder.

---

### Key findings

- 19.9% of CA1 cells (237/1,189) were classified as object-tuned, significantly above the 5.03% chance level estimated from no-object control sessions (p < 5.73 × 10⁻¹⁴¹). Approximately 4.1% were object cells (fields < 15 cm from object) and 13.3% were object-vector cells (fields ≥ 15 cm).
- 67.5% of CA1 cells showed some change in spatial firing pattern or firing rate when the object was introduced; 69.7% changed when the object was moved.
- Object-tuned cells showed only weak stability across days and environments: only 31.4% of 35 cells tracked across days remained object-tuned on more than one day, though this was significantly above chance.
- Population activity successfully decoded object presence (above-chance accuracy in all 16 sessions), with decoding accuracy decreasing monotonically and significantly as a function of distance from the object (distance bin 1 vs. 5: p < 0.0049 across all adjacent bin comparisons, Wilcoxon signed-rank). Decoding accuracy did not vary by allocentric angle.
- Population vector correlations (NO vs. O stacks) showed a stepwise linear increase with distance from the object, saturating at large distances.
- Patterns of joint spiking ("words") carried significantly more mutual information about trial type than total spike counts, and word information decreased with distance from the object; count information did not (H = 4.08, p = 0.39).
- Distance-dependent reorganisation is an emergent population property: individual cells showed minimal distance tuning (most within ±0.2 difference score), but including more cells increased the gradient monotonically up to n = 500 cells. Even the 20% of cells with the lowest distance tuning were sufficient to demonstrate graded reorganisation.
- Single-cell properties (object-tuning score, spatial information, spatial correlation, rate overlap) had at best very weak correlations with individual distance tuning (all |r| ≤ 0.18).
- Removing all object-tuned cells (19.9% of sample) did not abolish the population-level distance gradient, confirming the distributed nature of the representation.
- Behavioural decoders (speed, head direction, occupancy) performed near chance (≈50%) with no distance-dependent structure, ruling out behavioural confounds.

---

### Computational framework

The paper uses **population vector decoding** and **information-theoretic analysis** as its primary analytical framework.

Key elements:
- A **Bayesian decoder** estimates the posterior probability of trial type (NO or O) given an observed population vector (spike counts in 1 s bins), using firing-rate maps as likelihoods and occupancy as a spatial prior.
- **Mutual information** between population "words" (binary 10 ms spike patterns across N cells) and trial type quantifies the information content of combinatorial spiking patterns vs. simple spike counts.
- **Kullback-Leibler divergence** between word-frequency distributions in NO and O trials provides a complementary measure of population-state dissimilarity as a function of spatial context.

The framework assumes that object-related information is best captured by the joint activity of the population (combinatorial code) rather than by the marginal activity of individual cells (rate code). The analysis does not impose a specific mechanistic model but characterises the geometry of population responses in terms of distance from the object as a latent variable.

---

### Prevailing model of the system under study

The introduction frames the prevailing understanding as a **single-cell-centric view** of hippocampal object coding. Prior to this paper, the field understood object coding in CA1 through several discrete cell categories: place cells whose fields are modulated by object presence; object cells (firing at the object's location, moving with the object); and object-vector cells / landmark-vector cells (firing at fixed distance and direction from the object, analogous to the more characterised object-vector cells in MEC). These functional cell types were thought to be the primary carriers of object information. The corollary was that understanding object representation in CA1 required identifying and characterising these specialised cell types, each contributing a specific, stable signal.

The introduction also signals awareness that single-cell responses in CA1 are heterogeneous and complex, with cells showing varied and often unstable responses to objects, and explicitly raises the possibility — motivated by recent work on distributed coding in place and non-place cells (Meshulam et al. 2017; Stefanini et al. 2020) — that object information may instead reside at the population level.

---

### What this paper contributes

The paper demonstrates that object information in CA1 is not primarily carried by dedicated object-coding cell types but is a **distributed emergent property** of the population:

1. **Smooth population-level reorganisation**: The hippocampal map reorganises continuously as a function of the animal's distance from the object, a form of spatial organisation distinct from both global remapping (discrete, orthogonal) and rate remapping (uniform across the environment). This cannot be predicted from single-cell tuning properties.

2. **Emergent nature of the code**: The distance-dependent reorganisation is invisible at the single-cell level but becomes increasingly apparent and stronger as population size grows, and persists even when only the cells with the weakest individual distance tuning are used. This establishes that the property is emergent — it arises from the collective, not from any identifiable subset.

3. **Combinatorial spiking patterns carry the information**: Words (joint spike patterns) carry substantially more information about trial type than spike counts alone, and this information is distance-dependent. This identifies the specific format of the population code.

4. **Object cells are unstable and non-essential**: Contrary to what a dedicated-cell-type account would predict, object-tuned cells were individually unstable across days and environments, and removing them from the analysis did not abolish the population-level gradient.

Together, these findings argue that some aspects of the hippocampal cognitive map are better understood as population-level phenomena than as properties of named functional cell types.

---

### Brain regions & systems

- **Hippocampus CA1** — primary focus; locus of the distributed, distance-dependent population code for objects; also the area where most single-cell analyses (object cells, object-vector cells) were performed.
- **Hippocampus CA3** — recorded in a subset of animals; also showed widespread changes in spatial firing with object presence (reported in supplementary), though not the primary focus.
- **Medial entorhinal cortex (MEC)** — discussed as providing input to CA1; MEC object-vector cells (Høydal et al. 2019) provide a lower-dimensional, more stable object code upstream, in contrast to the heterogeneous and higher-dimensional CA1 code. MEC was not the recording target in this study.

---

### Mechanistic insight

The paper partially meets the bar. It provides large-scale neural data that specifically demonstrates a population-level algorithm (distance-dependent reorganisation as an emergent combinatorial code), and it rules out single-cell and behavioural explanations.

**Computational level**: The hippocampus encodes the animal's relationship to a salient object in the environment. The relevant variable is the animal's distance from the object — the population activity state differs smoothly and continuously as this distance changes.

**Algorithmic level**: The representation is implemented via the joint pattern of spiking across many cells (the "word"), not via the firing rate of individual cells or spike counts. Cells with no individually detectable object tuning collectively produce a graded distance code. The code is distributed: removing any specific subpopulation (including all object-tuned cells) does not abolish it. The information structure is combinatorial — words carry significantly more mutual information than counts, and this advantage is distance-dependent.

**Implementational level**: The paper does not address specific cell types, connectivity, neuromodulators, or biophysical mechanisms that implement this code. The neural hardware is known (CA1 pyramidal cells recorded via tetrodes or Neuropixels), but no data are presented linking the combinatorial code to particular circuit elements or synaptic mechanisms. This level remains unaddressed.

The mechanistic picture is therefore strong at the computational and algorithmic levels but silent at the implementational level.

---

### Limitations & open questions

- The analysis characterises the population code geometrically (distance-dependence, distributed nature) but does not explain the **mechanism** by which CA1 circuits generate a smooth, distributed distance code from the heterogeneous inputs they receive.
- **Object cell instability** across days contrasts with stable MEC object-vector cells; the authors acknowledge possible training-procedure differences (referencing unpublished communication from B. Rivard) but do not resolve whether instability is a true property or a methodological artefact.
- The distance-based reorganisation is **descriptive**: it establishes that distance is the dominant variable organising population activity near objects, but does not address whether the population also encodes allocentric direction, object identity, or higher-order relational information.
- The paper is restricted to **2D open-field foraging** with a single, visually salient object; whether the same population-level properties hold for more naturalistic multi-object environments or for objects used in memory tasks is untested.
- It is unclear whether the **emergent distance code also exists upstream in MEC** (the authors explicitly raise this as an open question, noting the toroidal topology of grid-cell populations as a precedent).
- The Bayesian decoder used occupancy as a prior; while the authors show this does not affect results, the decoder's sensitivity to subtle non-spatial correlates of the object (e.g., olfactory or tactile signals) cannot be fully excluded.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — foundational cognitive map framework
- Høydal et al. (2019, Nature) — MEC object-vector cells
- Deshmukh & Knierim (2013, Hippocampus) — CA1 landmark-vector cells
- Rivard et al. (2004, J. Gen. Physiol.) — CA1 object cells
- Meshulam et al. (2017, Neuron) — collective coding by place and non-place cells
- Stefanini et al. (2020, Neuron) — distributed code in dentate gyrus and CA1
- Gardner et al. (2022, Nature) — toroidal topology of grid-cell population activity
- Leutgeb et al. (2004, Science); Leutgeb et al. (2005, Science) — CA1/CA3 ensemble codes, global and rate remapping
- Schneidman et al. (2006, Nature) — weak pairwise correlations and strong network states
- Posani et al. (2017, J. Comput. Neurosci.) — Bayesian decoding of hippocampal representations
- Jezek et al. (2011, Nature) — theta-paced flickering between place-cell maps

**Named models or frameworks**:
- Cognitive map (O'Keefe & Nadel)
- Object-vector cell framework (Høydal et al.)
- Population vector / Bayesian decoder (Posani et al.)
- Words and counts framework for combinatorial coding (Schneidman et al.; Osborne et al.)
- Global remapping / rate remapping distinction

**Brain regions**:
- Hippocampus CA1
- Hippocampus CA3
- Medial entorhinal cortex (MEC)

**Keywords**: population coding, hippocampus CA1, object coding, object-vector cells, place cells, cognitive map, emergent neural representation, Bayesian decoding, combinatorial spiking code, distributed coding, Neuropixels, remapping
