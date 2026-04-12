---
source_file: sablemeyer2022_geometric_language_thought.md
paper_id: sablemeyer2022_geometric_language_thought
title: "A language of thought for the mental representation of geometric shapes"
authors:
  - "Mathias Sablé-Meyer"
  - "Kevin Ellis"
  - "Josh Tenenbaum"
  - "Stanislas Dehaene"
year: 2022
journal: "Cognitive Psychology"
paper_type: empirical
contribution_type: theoretical
species:
  - human
brain_regions:
  - prefrontal_cortex
frameworks:
  - compositionality
keywords:
  - language_of_thought
  - geometric_shape_perception
  - program_induction
  - minimum_description_length_mdl
  - compositionality
  - recursion
  - complexity_in_cognition
  - shape_representation
  - working_memory
  - human_uniqueness
  - bayesian_concept_learning
  - dreamcoder
  - core_knowledge
  - path_integration
  - discrete_and_continuous_cognition
  - language
  - thought
  - mental
  - representation
  - geometric
---

### One-line summary

Humans represent geometric shapes through a compositional "language of thought" that combines discrete and continuous primitives via repetition, concatenation, and embedding, with perceived complexity determined by the minimum description length (MDL) of the generating program.

---

### Background & motivation

The cognitive origins of geometric knowledge remain debated. While animals possess spatial navigation systems, only humans appear capable of formal, symbolic geometric reasoning in a combinatorial and productive manner. This capacity is evident across human cultures and history, from prehistoric engravings (70,000 years ago) to architectural constructions. The authors propose that human geometric competence arises from a recursive "language of thought" that combines core knowledge systems through compositional operations.

---

### Methods

The paper combines theoretical development of a formal language with two empirical experiments:

**Language specification:**
- Developed a Logo-like programming language with three primitive types:
  - **Drawing primitives**: Turn, Move, Trace (curve integration with continuous parameters)
  - **Control structures**: Concatenation (;), Repeat, Subprogram (isolated execution)
  - **Number system**: Integers (Peano arithmetic) and rational numbers (fractions)
- Complexity defined as Minimum Description Length (MDL): number of nodes in program syntax tree
- Program induction tested using DreamCoder algorithm (neural network + library learning)

**Experiment 1 (N=116 after exclusions):**
- Online delayed match-to-sample task with 68 unique geometric shapes
- Participants self-paced encoding time (spacebar press duration), then selected target from 6 alternatives after 2s delay
- Distractors selected to be perceptually similar (matched on gray level and CNN features)
- Dependent measures: encoding time, choice time, error rate

**Experiment 2 (N=163 for main task, N=27 for subjective ratings):**
- Same delayed match-to-sample procedure with 60 stimuli generated from 5 base shapes (square, circle, S, sigma, square root)
- Four conditions: single shape, repetition (4 copies), concatenation (2 shapes side-by-side), embedding (inner shape forms outline of outer shape)
- Additional subjective complexity ratings (0-100 scale)

---

### Key findings

**Experiment 1:**
- Both encoding time (R² = 0.68, p < .001) and choice time (R² = 0.73, p < .001) were strongly predicted by MDL
- Effects remained significant after controlling for gray level (encoding: R² = 0.46; choice: R² = 0.54)
- MDL remained significant predictor in mixed models controlling for all visual features (number of extremities, intersections, disconnected parts, closure)
- Error rates also correlated with MDL (R² = 0.51, p = .009)

**Experiment 2:**
- **Repetition**: All three measures showed significant linear effects of base shape complexity and number of repetitions (subjective: R² = 0.62; encoding: R² = 0.90; choice: R² = 0.89)
- **Concatenation**: Complexity of concatenated shapes well predicted by sum of constituent complexities (subjective: R² = 0.64; encoding: R² = 0.85; choice: R² = 0.89)
  - Self-concatenated shapes (identical left/right) showed significant "saving" (lower complexity than predicted), consistent with use of repetition instruction
- **Embedding**: Complexity of embedded shapes predicted by sum of outer and inner shape complexities (subjective: R² = 0.53; encoding: R² = 0.64; choice: R² = 0.86)
  - Self-embedded shapes also showed complexity savings

**DreamCoder simulation:**
- Successfully found minimal programs for shape corpora ("Greek" rectilinear, "Celtic" curvilinear)
- Created culture-specific abstractions reflecting training set statistics
- Demonstrated feasibility of tractable program induction for simple geometric shapes

---

### Computational framework

**Program induction / Bayesian concept learning:** The paper treats shape perception as program induction — finding the shortest program that generates a given shape. This connects to probabilistic/Bayesian program induction where the log-likelihood of a program is proportional to its length (MDL). The framework assumes humans search for minimal descriptions, with complexity determined by description length rather than literal stimulus properties.

**Language of thought:** Drawing on Fodor (1975) and Hauser, Chomsky & Fitch (2002), the paper proposes that geometric reasoning relies on a compositional, recursive language of thought that combines discrete and continuous primitives. This extends the "language of geometry" previously developed for spatial sequences (Amalric et al., 2017) to continuous shape representations through integration operations.

**Minimum Description Length (MDL):** A core principle from algorithmic information theory (Kolmogorov complexity) applied to cognitive psychology. The perceived complexity of a shape equals the length of its shortest mental representation, not its physical properties. This unifies work by Leeuwenberg (1971), Chater & Vitányi (2003), and Feldman (2000).

---

### Prevailing model of the system under study

The field historically held that shape perception relies on: (1) low-level visual feature detection (spatial frequency, luminance) processed by the ventral visual stream; and (2) general-purpose neural network mechanisms for object recognition. Geometric competence was thought to emerge from these domain-general perceptual systems or from explicit formal education.

The paper argues this view is incomplete. Evidence from cross-cultural studies (Mundurucu, Himba) and developmental research shows that humans possess intuitive geometric concepts without formal education. The authors' previous work (Sablé-Meyer et al., 2021) showed that baboon behavior on quadrilateral perception could be captured by ventral stream neural network models, but human behavior required an additional symbolic system encoding discrete geometric concepts (parallelism, right angles). This suggests two parallel systems: a visual system shared with other primates, and a uniquely human symbolic system.

---

### What this paper contributes

1. **Formal language proposal:** A concrete specification of a programming language for geometric shapes that combines discrete (integers, repetition) and continuous (path integration, turning) primitives. This extends prior "language of thought" frameworks to the domain of visual shape representation.

2. **Empirical validation of MDL:** Experimental demonstration that perceived geometric complexity (encoding time, choice time, subjective ratings, error rates) is determined by minimum description length in the proposed language, not by low-level visual properties. Effect sizes are large (R² = 0.46-0.73 even after controlling for visual confounds).

3. **Additive laws:** Discovery and empirical confirmation that complexity of composite shapes follows additive laws: concatenation, repetition, and embedding each add fixed costs to constituent complexities. This constrains the space of possible languages and supports the program induction framework.

4. **Computational feasibility:** Demonstration using DreamCoder that program induction for geometric shapes is computationally tractable, with neural network guidance and library learning enabling efficient search. This addresses the "search problem" objection to program induction models.

5. **Species comparison:** Integration with prior work showing that the symbolic system is uniquely human, while non-human primates rely on visual mechanisms. This positions the language of thought as a candidate "human singularity" in cognition.

---

### Brain regions & systems

Not applicable — the paper focuses on behavioral and computational modeling. However, the authors reference relevant neural systems:

- **Ventral visual pathway** — object recognition system (available to both humans and non-human primates); modeled by convolutional neural networks like CORnet
- **Prefrontal cortex** — previously implicated in representation of spatial sequences using nested rules (Wang et al., 2019); suggested as locus of symbolic program manipulation
- **Hippocampal/entorhinal system** — path integration and cognitive map formation (O'Keefe & Nadel, 1978; McNaughton et al., 2006); provides geometric primitives for the proposed language

The paper suggests that the proposed language of thought likely involves prefrontal circuits for program manipulation, distinct from the ventral stream visual processing available to all primates.

---

### Mechanistic insight

The paper does not meet the full mechanistic insight bar as defined, as it does not provide neural data specifically supporting the algorithm over alternatives. However, the paper provides a detailed algorithmic framework:

**Computational level:** Shape perception is formulated as program induction — finding the shortest program that generates a given shape. The computational problem is to compress visual input into a minimal mental description that captures its regularities (repetition, symmetry, embedding). This is justified by the principle that shorter programs are more likely under a Bayesian prior (since program probability decreases exponentially with length).

**Algorithmic level:** The proposed language specifies exact representations and processes:
- **Primitives:** Discrete integers (via Peano arithmetic), fractions, heading direction, path integration, right angle turns, straight lines
- **Control structures:** Concatenation (sequential execution), Repeat (discrete iteration), Subprogram (state isolation for embedding)
- **Trace instruction:** Continuous integration with parameters for duration, speed, acceleration, and turning speed — enables generation of curves (circles, spirals) without infinitesimal discrete loops
- **Complexity metric:** Number of nodes in syntax tree (with special handling for signed numbers and concatenations)

**Implementational level:** The paper does not provide specific neural implementation details (cell types, connectivity, biophysical mechanisms). However, it suggests that:
- Ventral visual pathway implements the visual feature extraction needed for program induction input
- Prefrontal cortex may implement the symbolic program manipulation
- Hippocampal path integration circuits provide the continuous geometric primitives

The DreamCoder implementation demonstrates computational feasibility using a neural network (bottom-up program guidance) combined with symbolic search and library learning, suggesting a possible hybrid neural-symbolic implementation.

---

### Limitations & open questions

1. **Scope limitations:** The language only applies to abstract geometric shapes, not natural object contours (which require medial axis/skeletal representations). Some simple geometric figures (ellipses, parabolas, trapezoids) are difficult to generate efficiently.

2. **Variable binding:** The language lacks local variables to store intermediate values (e.g., turning angle α for trapezoid generation). Adding variables would help describe partial regularities but risks making overly complex shapes too easy to describe.

3. **No named subprograms:** Unlike DreamCoder, the basic language doesn't include reusable abstractions (e.g., a "square" procedure). This limits compression for shapes sharing subcomponents.

4. **Dual-route challenge:** If shapes are too easily discriminated by low-level visual features, humans may not engage symbolic encoding, causing MDL to stop predicting performance (observed in pilot data).

5. **Species specificity:** The symbolic system is proposed as uniquely human, but direct comparative testing with the current stimuli is needed. Previous work with quadrilaterals showed baboons lack symbolic geometric regularity effects.

6. **Transformations:** The language doesn't include mental transformations (rotation, shearing, deformation) that might explain perception of shapes like ellipses (as compressed circles).

7. **Declarative vs imperative:** The language is purely imperative (step-by-step instructions). Some shapes (e.g., circle as equidistance from center) might be better described declaratively via constraints.

---

### Connections & keywords

**Key citations:**
- Fodor (1975) — Language of thought hypothesis
- Hauser, Chomsky & Fitch (2002) — Recursion as uniquely human faculty
- Leeuwenberg (1971) — Coding theory for shape perception (minimum principle)
- Leyton (1984, 2003) — Generative theory of shape
- Amalric et al. (2017) — Language of geometry for spatial sequences
- Chater & Vitányi (2003), Feldman (2000, 2003) — Simplicity/minimum description length in cognition
- Lake et al. (2015) — Probabilistic program induction
- Ellis et al. (2021) — DreamCoder algorithm for program induction
- Sablé-Meyer et al. (2021) — Comparative study with baboons showing human-specific symbolic geometry

**Named models/frameworks:**
- Language of thought (Fodor)
- Minimum Description Length (MDL) / Kolmogorov complexity
- DreamCoder (program induction algorithm)
- Logo programming language (turtle graphics)
- Core knowledge systems (Spelke, Dehaene)
- Probabilistic program induction / Bayesian concept learning
- Leeuwenberg's coding theory
- Leyton's generative theory of shape

**Brain regions:**
- Ventral visual pathway (object recognition)
- Prefrontal cortex (symbolic program manipulation)
- Hippocampus/entorhinal cortex (path integration, cognitive map)

**Keywords:**
- Language of thought
- Geometric shape perception
- Program induction
- Minimum description length (MDL)
- Compositionality
- Recursion
- Complexity in cognition
- Shape representation
- Working memory
- Human uniqueness
- Bayesian concept learning
- DreamCoder
- Core knowledge
- Path integration
- Discrete and continuous cognition
