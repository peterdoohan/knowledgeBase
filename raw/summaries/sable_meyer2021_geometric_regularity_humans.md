---
source_file: sable_meyer2021_geometric_regularity_humans.md
title: Sensitivity to geometric shape regularity in humans and baboons: A putative signature of human singularity
authors: Mathias Sablé-Meyer, Joël Fagot, Serge Caparos, Timo van Kerkoerle, Marie Amalric, Stanislas Dehaene
year: 2021
journal: Proceedings of the National Academy of Sciences (PNAS)
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Humans across all tested populations show a geometric regularity effect (enhanced detection of intruder shapes based on Euclidean regularities like right angles, parallelism, and symmetry) that is absent in baboons, not captured by CNNs or VAEs, but is captured by a symbolic model based on discrete geometric properties.

### Background & motivation

Humans are unique among primates in their ability to create and manipulate formal symbolic systems (language, mathematics, music). This study investigates whether this symbolic capacity extends to elementary visual perception of geometric shapes. Previous work showed that humans possess intuitive geometric knowledge independent of formal education, but it remained unclear whether this reflects a human-specific capacity or a general primate ability. The study addresses this gap by comparing human and baboon performance on identical shape perception tasks.

### Methods

- **Task design**: Geometric intruder task — participants detected which of six quadrilaterals was different (the "intruder"). The intruder was created by displacing one vertex of a reference shape by a fixed distance.
- **Stimuli**: 11 reference quadrilaterals varying in geometric regularity (from square with 4 regularities to arbitrary irregular quadrilateral with 0 regularities), matched for average inter-vertex distance.
- **Participants**:
  - 605 French adults (experiment 1)
  - 117 French adults (experiment 2, with swapped/canonical displays)
  - 27 French adults (subjective complexity ratings)
  - 11 French adults (visual search task)
  - 16 French adults (sequential presentation of vertices)
  - 28 French kindergartners (mean age 5.3 years)
  - 22 uneducated Himba adults from rural Namibia (no formal schooling, no geometric vocabulary)
  - 20 baboons (Papio papio) with extensive training (avg. 5,200+ trials to criterion, then ~6,305 trials on geometric task)
- **Analysis approach**: Repeated-measures ANOVA, linear regression correlating error rates with geometric regularity, correlation analyses across populations and models.
- **Modeling**: Comparison of CNN (CORnet, V1-IT layers), VAE, and symbolic model (discrete geometric property vectors with L1 distance metric).

### Key findings

- **Geometric regularity effect in humans**: Error rates varied dramatically with shape regularity (2% to 40% across shapes), strongly correlated with number of geometric regularities (r² = 0.64, P = 0.0031). Effect was robust across all experimental manipulations.
- **Replication across populations**: Effect replicated in French kindergartners (r² = 0.97 correlation with adults) and uneducated Himba adults (r² = 0.55 with French adults, r² = 0.59 with kindergartners), indicating independence from education, culture, and language.
- **Absence in baboons**: Despite extensive training (>5,000 trials) and eventual performance improvement (to ~53% error rate), baboons showed no geometric regularity effect. Their performance did not correlate with human regularity effect (nonsignificant correlation with human error rates).
- **Double dissociation in modeling**:
  - CNN model (ventral pathway) captured baboon behavior well (r = 0.81) but poorly predicted human behavior (r = 0.48, P = 0.024 difference).
  - Symbolic model (discrete geometric properties) captured human behavior well (r = 0.84) but poorly predicted baboon behavior (r = 0.44, P < 0.001 difference).
  - VAE failed to capture either human or baboon behavior.
- **Mechanistic insights**: The geometric regularity effect is not due to early preattentive pop-out (visual search showed serial processing) but arises from a higher-level representation where geometric properties can be ascertained even when not simultaneously present (sequential presentation experiment replicated the effect).

### Computational framework

The paper uses two competing computational frameworks to model shape perception:

1. **Neural network framework (ventral visual pathway model)**: CORnet, a CNN trained on ImageNet, models hierarchical feature extraction from V1 through IT cortex. It assumes shapes are encoded as distributed activation patterns in a continuous feature space, similar to object recognition mechanisms. The model predicts outlier detection based on L2 distance in activation space.

2. **Symbolic framework**: A discrete symbolic model where each shape is encoded as a binary vector of geometric properties (equal angles, equal sides, parallelism, right angles). The model assumes categorical perception of geometric invariants and predicts task difficulty based on L1 (Manhattan) distance between symbolic vectors. This reflects a "language of thought" for geometry where discrete symbolic rules are applied to perceptual input.

The double dissociation between these frameworks' predictive power suggests two distinct processing routes: a shared perceptual route (captured by CNNs) and a human-specific symbolic route.

### Prevailing model of the system under study

The prevailing model assumes that shape perception relies primarily on the ventral visual pathway, where hierarchical CNN-like processing extracts features from simple orientations (V1) to complex object representations (IT cortex). This model, supported by extensive neurophysiology and computational modeling, treats geometric shape perception as a continuous process of feature extraction and pattern matching similar to general object recognition. Under this framework, differences between species would be quantitative (degree of training, acuity) rather than qualitative (different representational formats). The introduction notes that previous work established humans possess intuitive geometric knowledge, but the neural basis and whether this is human-specific remained unclear. The paper challenges the assumption that ventral pathway processing alone can explain human geometric perception.

### What this paper contributes

This paper provides empirical evidence for a qualitative difference between human and nonhuman primate shape perception, challenging the prevailing ventral-pathway-only model. Key contributions:

1. **Discovery of a human-specific cognitive universal**: The geometric regularity effect (sensitivity to Euclidean regularities) is present across all human populations tested (Western adults, young children, uneducated non-Western adults) and is independent of education, language, and culture. This establishes a new candidate for human cognitive singularity at the perceptual level.

2. **Demonstration of absence in nonhuman primates**: Extensive training (>5,000 trials) failed to produce the geometric regularity effect in baboons, despite their eventual task proficiency. This provides strong evidence that the effect is not simply a matter of training or general visual ability.

3. **Computational double dissociation**: The paper shows that CNN models of the ventral pathway capture baboon behavior but fail to capture human behavior, while a symbolic model captures human behavior but not baboon behavior. This provides computational-level evidence for two distinct processing strategies and challenges the adequacy of purely neural network approaches to human visual cognition.

4. **Challenge to "carpentered world" hypothesis**: The effect's presence in uneducated Himba adults and absence in baboons living in similar environments refutes the idea that the geometric regularity effect arises from exposure to rectilinear man-made objects.

5. **Methodological contribution**: The geometric intruder task provides a simple, scalable paradigm for comparing shape perception across species and human populations.

### Brain regions & systems

Not applicable — The paper focuses on behavioral and computational-level analysis. However, the authors discuss relevant neural systems in the Discussion:

- **Ventral visual pathway (V1 → IT cortex)**: Proposed locus of the perceptual/CNN-like strategy shared with baboons. The CNN model (CORnet) is explicitly mapped to layers V1, V2, V4, and IT.
- **Dorsal and inferior prefrontal cortex**: Proposed locus of the symbolic strategy unique to humans. The authors cite prior work showing these regions are activated during geometric reasoning and are expanded in humans. They suggest these regions may implement the "language of geometry" needed for symbolic shape representation.

### Mechanistic insight

The paper provides strong mechanistic insight at the computational and algorithmic levels, though not at the implementational (neural hardware) level.

**Computational level**: The problem is identifying an outlier shape among six quadrilaterals. The paper shows this can be solved via two distinct computational approaches:
1. **Perceptual similarity**: Treat shapes as images and detect the outlier based on feature-space distance (L2 norm in CNN activation space). This approach is shared with baboons and CNNs.
2. **Symbolic comparison**: Extract discrete geometric properties (equal angles, equal sides, parallelism, right angles) and detect outliers based on symbolic distance (L1 norm between binary property vectors). This approach is unique to humans.

**Algorithmic level**: The symbolic model assumes:
- **Representation**: Shapes are encoded as binary vectors over four geometric properties (equal angles, equal sides, parallelism, right angles), with a tolerance parameter (12.5%) for detection.
- **Process**: Outlier detection proceeds by computing the L1 (Manhattan) distance between the reference and deviant property vectors. Smaller distances predict harder trials.

The paper does not address the implementational level (specific cell types, circuits, or biophysical mechanisms), though it hypothesizes that prefrontal cortex may implement the symbolic strategy. The double dissociation between CNNs (capturing baboons) and symbolic models (capturing humans) provides strong evidence that two distinct algorithmic routes exist for solving the same computational problem.

### Limitations & open questions

1. **Single nonhuman species**: Only baboons (Papio papio) were tested. The claim of human uniqueness would be strengthened by testing other primates, particularly chimpanzees.

2. **Response time differences**: Baboons responded much faster than humans (~2 s vs. ≥5 s), which may have prevented the deployment of a more abstract strategy. Slower response times might enable symbolic processing.

3. **Training differences**: Baboons required extensive training (>5,000 trials) while humans needed minimal instruction. The training procedures were necessarily different across species.

4. **Causal neural evidence**: The paper relies on computational modeling and behavioral data. Direct neural recordings or perturbations would strengthen claims about distinct neural routes.

5. **VAE limitations**: The VAE was trained only on the 11 reference shapes, which may not have been sufficient to learn meaningful representations.

6. **Generalization to other geometric domains**: The task focused on quadrilaterals. Whether the symbolic capacity generalizes to other geometric structures (3D shapes, topological properties) remains to be tested.

7. **Alternative symbolic models**: Only one symbolic model was tested. Other formalizations of geometric intuition might also capture human behavior.

### Connections & keywords

**Key citations**:
- Dehaene et al. (2006) — Core knowledge of geometry in Amazonian indigene group
- Izard et al. (2011) — Flexible intuitions of Euclidean geometry in Amazonian indigene group
- Amalric et al. (2017) — The language of geometry: Fast comprehension of geometrical primitives and rules
- Dillon et al. (2019) — Geometric categories in cognition
- Westphal-Fitch et al. (2012) — Production and perception rules underlying visual patterns
- Schrimpf et al. (2018) — Brain-score platform for comparing ANNs to brain
- Kubilius et al. — Brain-like object recognition with shallow recurrent ANNs

**Named models or frameworks**:
- CORnet (CNN model of ventral visual pathway)
- Symbolic model (discrete geometric property vectors, L1 distance)
- Variational Autoencoder (VAE)
- Minimal description length / coding theory (Leeuwenberg)
- Language of thought (Fodor)
- Language of geometry (Amalric & Dehaene)

**Brain regions**:
- Ventral visual pathway (V1, V2, V4, IT cortex)
- Dorsal prefrontal cortex
- Inferior prefrontal cortex

**Keywords**: geometric regularity, shape perception, comparative cognition, human uniqueness, symbolic reasoning, convolutional neural networks, ventral visual pathway, baboons, cross-cultural psychology, core knowledge, intruder detection, Euclidean geometry, prefrontal cortex
