---
source_file: samborska2021_hippocampus_prefrontal_gen_b.md
paper_id: samborska2021_hippocampus_prefrontal_gen_b
title: "Complementary task representations in hippocampus and prefrontal cortex for generalising the structure of problems"
authors:
  - "Veronika Samborska"
  - "James Butler"
  - "Mark Walton"
  - "Timothy E.J. Behrens"
  - "Thomas Akam"
year: 2021
journal: "bioRxiv (preprint)"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
tasks:
  - probabilistic_reversal_learning
methods:
  - electrophysiology
  - representational_similarity_analysis
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - medial_prefrontal_cortex
frameworks:
  - reinforcement_learning
  - tolman_eichenbaum_machine
keywords:
  - generalisation
  - transfer_learning
  - meta_learning
  - schema
  - reversal_learning
  - medial_prefrontal_cortex
  - hippocampus
  - ca1
  - representational_similarity_analysis
  - singular_value_decomposition
  - abstraction
  - remapping
  - policy_representation
  - cell_assemblies
  - low_dimensional_representations
  - complementary_learning_systems
  - cognitive_map
  - sensorimotor_abstraction
  - episodic_memory
  - learning_set
key_citations:
  - behrens2018_cognitive_map_organizing_knowledge
  - whittington2020_tolman_eichenbaum_machine
  - baram2021_entorhinal_ventromedial_rl
wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/hippocampal_prefrontal_replay_in_planning
---

### One-line summary

Mice generalise knowledge across structurally equivalent but physically distinct reversal learning problems, with medial prefrontal cortex maintaining abstract problem-general representations while hippocampal CA1 represents problem-specific sensorimotor details.

---

### Background & motivation

Animals effortlessly generalise prior knowledge to novel situations that share abstract structure but differ in sensorimotor details. This ability—described as schema, learning set, transfer learning, or meta-learning—requires abstracting common structure from sensorimotor particulars. While both prefrontal cortex and hippocampus have been implicated in representing task states and their relationships, it remains unclear what distinguishes representations in these regions and how abstract knowledge is bound to specific situations.

---

### Methods

- **Subjects**: 9 male C57BL/6J mice (7 with usable recordings)
- **Behavioural task**: Probabilistic reversal learning with varying physical port layouts
  - Trial structure: initiation poke → choice between two ports → probabilistic reward → reversal after 75% correct threshold
  - Multiple problems per session (up to 3) with different port locations but identical abstract structure
- **Neural recordings**: Single-unit electrophysiology
  - dCA1: 345 neurons (3 mice, 91-162 neurons/mouse)
  - mPFC: 556 neurons (4 mice, 117-175 neurons/mouse)
- **Analysis approaches**:
  - Linear regression predicting neural activity from trial variables
  - Representational similarity analysis (RSA) with design matrices
  - Singular value decomposition (SVD) to assess generalisation of temporal and cellular modes
  - Cross-problem decoding using support vector classification
  - Movement controls using DeepLabCut pose estimation

---

### Key findings

- **Behavioural generalisation**: Mice showed transfer learning across problems, with fewer trials to reach reversal threshold (F(9,72) = 3.88, p < .001) and reduced out-of-sequence pokes (F(9,72) = 15.78, p < .001) across problems
- **Meta-learning evidence**: Animals acquired new poke sequences in a single reversal late in training vs. gradual learning early in training (t(17) = 2.45, p = .003), and adapted to reversals faster at end vs. beginning of training (t(17) = 5.29, p < .001)
- **Regional differences in trial event representation**:
  - Choice representation stronger in CA1 than PFC (peak variance: CA1 8.4% vs PFC 4.8%, p < .001)
  - Outcome coding stronger in PFC than CA1 (peak variance: PFC 12.9% vs CA1 7.1%, p < .001)
  - PFC showed stronger abstract representation of trial stage and outcome (p < .001)
  - CA1 showed stronger representation of physical port and A vs B choice (p < .001)
  - CA1 but not PFC showed problem-specific representation of A choices (p < .001), indicating 'remapping' in hippocampus
- **SVD generalisation results**:
  - Temporal modes (trial event patterns) generalised equally well across problems in both regions
  - Cellular modes (cell assemblies) generalised significantly better in PFC than CA1 (p < .05)
  - Combined cellular-temporal mode pairs generalised significantly better in PFC than CA1 (p < .05)
- **Cross-problem decoding**: PFC predominantly decoded to correct abstract task state when trained on one problem and tested on another; CA1 predominantly decoded to same physical port
- **Policy representations**: Both regions represented policy (integrated history of choices and outcomes), but:
  - Policy correlations across problems were larger in PFC than CA1 (p < .05)
  - PFC policy representations generalised across problems at all trial stages (initiation, choice, outcome)
  - CA1 policy representations only generalised on A choices (same port across problems), not B choices

---

### Computational framework

Reinforcement learning (RL) with meta-learning/learning-to-learn. The paper conceptualises generalisation as abstraction of task structure (common rules, trial sequences) separate from sensorimotor particulars (specific port locations). This maps onto:
- **Computational level**: Maximising reward by integrating choices and outcomes over extended histories to form policies, while generalising across structurally similar problems
- **Algorithmic level**: Distinct representations—PFC maintains abstract task variables (trial stage, outcome, policy) divorced from sensorimotor details; CA1 binds abstract variables to specific spatial/port configurations
- **Implementation level**: Single neurons in PFC show consistent tuning to abstract events across problems; CA1 neurons remap between problems, with different cells representing the same abstract event in different contexts

The framework also connects to Marr's three levels and complementary learning systems theory, where cortex abstracts structure and hippocampus encodes specific episodes.

---

### Prevailing model of the system under study

The prevailing model in the field was that:
1. Both prefrontal cortex and hippocampus represent task states and their relationships, but their computational roles were not clearly distinguished
2. PFC represents abstract task structure and variables (value, prediction error) important for learning actions de novo
3. Hippocampus represents spatial/episodic details and may support rapid learning of new task rules, particularly when inferences must be made at task boundaries
4. Interactions between frontal cortex and hippocampus support generalisation, but the specific nature of representational differences between regions was unclear

The field lacked understanding of how abstract knowledge is bound to specific sensorimotor contexts, and whether PFC and hippocampus play distinct, complementary roles in this process.

---

### What this paper contributes

This paper establishes that:
1. **PFC and hippocampus play complementary roles in generalisation**: PFC abstracts common structure across related problems (schema/learning-set), while hippocampus maps this structure onto the specifics of the current situation

2. **Different representational geometries**: 
   - PFC maintains problem-general representations—same neurons represent same abstract events (trial stage, outcome, policy) regardless of sensorimotor particulars
   - CA1 exhibits problem-specific representations—different neurons represent the same abstract event in different problems ('remapping'), with stronger tuning to physical port locations

3. **Temporal vs cellular generalisation dissociation**: Both regions share low-dimensional temporal patterns (same trial events represented), but PFC cell assemblies generalise across problems while CA1 assemblies do not

4. **Abstract policy representations**: Both regions represent policy (integrated choice-outcome history), but PFC representations are abstracted across problems at all trial stages, while CA1 policy representations are tied to specific ports

5. **Meta-learning in mice**: The behavioural paradigm demonstrates sophisticated meta-learning—mice learn to learn new problem structures faster with experience, acquiring both trial sequences and reversal adaptation in single trials after extensive training

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)** — Primary locus of abstract, problem-general representations. Neurons maintain consistent tuning to trial events (initiation, choice, outcome) and policy across different physical problem instantiations. Represents task structure divorced from sensorimotor particulars. Stronger outcome coding than CA1.

- **Dorsal CA1 (dCA1)** — Represents problem-specific sensorimotor details. Neurons exhibit 'remapping' between problems—different cells represent the same abstract event in different contexts. Stronger representation of physical port location and A vs B choice identity than PFC. Binds abstract task variables to specific spatial/port configurations. Shows problem-specific policy representations tied to particular ports.

---

### Mechanistic insight

This paper provides mechanistic insight that meets the high bar—both algorithm and neural data supporting it over alternatives.

**Phenomenon**: Generalisation of knowledge across problems with shared abstract structure but different sensorimotor implementations.

**Marr's levels analysis**:

- **Computational**: The brain must solve the problem of maximising reward while generalising across structurally similar problems. This requires maintaining abstract representations of task structure (trial stages, outcomes, policies) that can be flexibly mapped onto new sensorimotor contexts.

- **Algorithmic**: Two distinct representational schemes:
  1. **PFC**: Abstract task variables represented by consistent cell assemblies across problems. Same neurons code same abstract events regardless of sensorimotor particulars. Low-dimensional temporal modes are shared across problems, and the same cellular modes (cell assemblies) are reused.
  2. **CA1**: Concrete episodic representations that bind abstract variables to specific contexts. Different neurons code same abstract event in different problems ('remapping'). Temporal modes are shared (same events represented), but cellular modes are not—different cell assemblies are recruited in each problem.

- **Implementational**: Single-unit recordings show PFC neurons maintain consistent firing fields to abstract trial events (initiation, choice, outcome) across problems, even when physical port locations change. CA1 neurons show 'remapping'—firing preferences shift between problems, with some cells showing port-specific 'place cell'-like activity. The SVD analysis demonstrates that cellular mode generalisation is significantly stronger in PFC than CA1 (p < .05), while temporal mode generalisation is equivalent.

**Why this meets the bar**: The paper proposes a specific algorithm (dual representational systems: abstract/PFC vs. context-bound/hippocampus) and provides direct neural evidence from single-unit recordings showing that the same PFC neurons code abstract events across problems while different CA1 neurons code the same events in different problems. This supports the algorithm over alternatives (e.g., unified representational system, or purely spatial coding).

---

### Limitations & open questions

- **Limited to reversal learning**: Findings are specific to a particular probabilistic reversal learning paradigm; generalisation to other task structures requires further study
- **No causal manipulation**: The study is correlational; causal role of PFC vs. hippocampus in generalisation not established through lesions, optogenetics, or pharmacology
- **Prefrontal subregion specificity**: Recordings targeted medial PFC but did not distinguish between subregions (anterior cingulate, prelimbic, infralimbic) that may have different roles
- **Hippocampal subfield specificity**: Recordings targeted dorsal CA1 but did not assess CA3, dentate gyrus, or subiculum contributions
- **Species generalisation**: Findings in mice require validation in primates/humans
- **Mechanism of remapping**: The 'surprise' signal at problem transitions suggests abrupt representational change, but the mechanism driving hippocampal remapping is not identified
- **Cortical-hippocampal interactions**: The study records from separate groups of animals; simultaneous recordings would reveal how PFC and hippocampus interact during generalisation
- **Role of entorhinal cortex**: Given entorhinal grid cells abstract spatial structure, their role in non-spatial task abstraction remains unclear

---

### Connections & keywords

**Key citations**:
- Tse et al. (2007, 2011) — Schema and memory consolidation
- Harlow (1949) — Learning sets
- Wang et al. (2018) — Prefrontal cortex as meta-reinforcement learning system
- O'Keefe & Dostrovsky (1971) — Hippocampal place cells
- Behrens et al. (2018) — What is a cognitive map?
- Whittington et al. (2020) — Tolman-Eichenbaum Machine
- Zhou et al. (2020) — Evolving schema representations in orbitofrontal cortex
- Baram et al. (2021) — Entorhinal and ventromedial prefrontal cortices abstract RL problems

**Named models or frameworks**:
- Schema theory (Tse et al.)
- Learning set (Harlow)
- Transfer learning / Meta-learning / Meta-reinforcement learning (Wang et al.)
- Representational similarity analysis (RSA; Kriegeskorte et al.)
- Singular value decomposition (SVD) for population activity decomposition
- Complementary learning systems (Marr, McNaughton & O'Reilly)
- Cognitive map theory (Behrens et al., Tolman-Eichenbaum Machine)
- Marr's three levels of analysis

**Brain regions**:
- Medial prefrontal cortex (mPFC)
- Dorsal CA1 (dCA1) hippocampus
- Entorhinal cortex (mentioned in discussion)
- Orbitofrontal cortex (OFC; discussed in relation to prior work)
- Anterior cingulate cortex (mentioned as part of mPFC)

**Keywords**:
- generalisation
- transfer learning
- meta-learning
- schema
- reversal learning
- medial prefrontal cortex
- hippocampus
- CA1
- representational similarity analysis
- singular value decomposition
- abstraction
- remapping
- policy representation
- cell assemblies
- low-dimensional representations
- complementary learning systems
- cognitive map
- sensorimotor abstraction
- episodic memory
- learning set

### Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]
- [[wiki/topics/hippocampal_prefrontal_replay_in_planning|Hippocampal–prefrontal replay in planning]]
