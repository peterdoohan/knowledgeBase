---
source_file: "samborska2021_hippocampus_prefrontal_gen.md"
paper_id: "samborska2021_hippocampus_prefrontal_gen"
title: "Complementary task representations in hippocampus and prefrontal cortex for generalising the structure of problems"
authors: "Veronika Samborska, James Butler, Mark Walton, Timothy E.J. Behrens, Thomas Akam"
year: 2021
journal: "bioRxiv"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse", "human"]
tasks: ["probabilistic_reversal_learning"]
methods: ["electrophysiology", "representational_similarity_analysis", "behavioral_analysis"]
brain_regions: ["hippocampus", "hippocampus_ca1", "prefrontal_cortex", "medial_prefrontal_cortex"]
frameworks: ["reinforcement_learning", "tolman_eichenbaum_machine"]
keywords: ["abstraction", "generalisation", "transfer_learning", "meta_learning", "schema", "reversal_learning", "representational_similarity_analysis", "singular_value_decomposition", "prefrontal_cortex", "hippocampus", "cellular_modes", "temporal_modes", "policy_representation", "remapping", "learning_set", "task_structure", "sensorimotor", "electrophysiology", "single_unit_recording", "mouse"]
key_citations: ["wilson2014_best_practices_scientific", "schuck2016_orbitofrontal_cortex_state", "behrens2018_cognitive_map_organizing_knowledge", "whittington2020_tolman_eichenbaum_machine", "fyhn2007_remapping_grid_realignment"]
---

### One-line summary

Medial prefrontal cortex maintains abstract, sensorimotor-invariant representations of task structure across problems, while hippocampal CA1 represents sensorimotor-specific instantiations, revealing complementary roles in knowledge generalisation.

---

### Background & motivation

Animals and humans effortlessly generalise prior knowledge to novel situations that share abstract structure but differ in sensorimotor details (e.g., knowing how restaurants work regardless of which restaurant you enter). This requires abstraction—extracting common structure from specific experiences—and binding these abstractions to current sensory particulars. While prefrontal cortex and hippocampus are both implicated in flexible behaviour, their distinct contributions to abstraction and generalisation remain unclear. This study tests whether PFC and hippocampus play complementary roles: PFC abstracting common task structure and hippocampus mapping this structure onto specific sensorimotor contexts.

---

### Methods

- **Subjects**: 9 male C57BL/6J mice (7 with usable data after probe damage/culling)
- **Task**: Probabilistic reversal learning with changing physical layouts. Mice performed initiation poke → choice between two ports → probabilistic reward (80/20 or 90/10). After 75% correct threshold, contingencies reversed. Problems switched after 4 reversals (recording phase) or 10 reversals (training phase).
- **Design**: 10 different port layouts (reflections of 3 basic layout types) allowed dissociation of: (1) same port/same role, (2) different port/same role, (3) same port/different role
- **Recordings**: Silicon probes in dorsal CA1 (345 neurons, n=3 mice) and medial PFC (556 neurons, n=4 mice). Single-unit recordings across multiple problems within sessions.
- **Analysis**: 
  - Linear regression predicting neural activity from choice, outcome, choice×outcome
  - Representational similarity analysis (RSA) with design matrices for trial stage, choice, outcome, physical port, problem-specific representations
  - Singular value decomposition (SVD) to assess generalisation of temporal and cellular modes across problems
  - Cross-problem decoding of trial states
  - Policy estimation via logistic regression of choice history

---

### Key findings

- **Behavioural transfer**: Mice showed meta-learning—fewer trials to reach reversal threshold across problems (F(9,72) = 3.88, p < .001), and acquired new poke sequences in a single reversal late in training vs. gradual learning early (t(17) = 2.45, p = .003).

- **Regional coding differences**: 
  - Choice (A vs B) representation stronger in CA1 than PFC (peak variance: CA1 8.4%, PFC 4.8%, p < .001)
  - Outcome (reward vs no reward) coding stronger in PFC (peak: CA1 7.1%, PFC 12.9%, p < .001)
  - Choice×outcome interaction explained more variance in CA1 (peak: CA1 3.7%, PFC 2.4%, p < .001)

- **Problem generalisation**: Temporal modes (patterns of activity over time/trial types) generalised equally well across problems in both regions. However, cellular modes (co-activating neuron assemblies) generalised significantly better in PFC than CA1 (p < .05).

- **Representational content**: 
  - PFC: Stronger abstract representation of trial stage (initiation vs choice) and outcome (p < .001 for both)
  - CA1: Stronger representation of physical port location and A vs B choice (p < .001)
  - CA1 showed problem-specific representations of A choices (same physical port/meaning across problems), indicating context-induced 'remapping' absent in PFC (p < .001)
  - PFC outcome representations were more general (same neurons responded across ports/problems); CA1 outcome representations were more conjunctive (different neurons for reward on A vs B choices; p < .001)

- **Decoding**: Cross-problem decoding showed PFC predominantly decoded to correct abstract task state, while CA1 predominantly decoded to same physical port as training data.

- **Policy representations**: Both regions encoded policy (integrated choice/outcome history), but:
  - PFC policy representations generalised across problems for both A and B choices
  - CA1 policy representations only generalised for A choices (same physical port); B choice policy representations did not correlate across problems
  - Policy representations in both regions were specific to trial stage (initiation, choice, outcome), not simple value representations

---

### Computational framework

The study employs a reinforcement learning (RL) framework with meta-learning (learning to learn). The task is formalised as a series of partially observable Markov decision processes (POMDPs) sharing the same abstract structure (state transitions, reward contingencies) but differing in observation/action mappings (physical port locations). 

Key computational concepts:
- **Abstraction**: Extracting task structure (initiation → choice → outcome; one option better with reversals) independent of sensorimotor instantiation
- **Generalisation**: Applying learned abstract structure to novel problems with different physical layouts
- **Meta-learning**: Faster learning of new problems due to prior experience with structurally similar problems
- **Policy**: The mapping from states to actions, here formalised via logistic regression on choice/outcome history

The representational similarity analysis (RSA) and singular value decomposition (SVD) analyses provide geometric/mathematical frameworks for quantifying how neural population activity encodes task variables and how these encodings generalise across problems.

---

### Prevailing model of the system under study

The prevailing model, based on the paper's introduction and prior literature, posits that:

1. **Both PFC and hippocampus represent task states and their relationships** — Both regions have been hypothesized to encode task structure, with frontal cortex representing abstract task states and hippocampus encoding episodic sequences and spatial/contextual information.

2. **PFC contains abstract, generalisable representations** — Consistent with theories of prefrontal function in adaptive behaviour, PFC is thought to represent task structure in a manner that generalises across different specific instances.

3. **Hippocampus represents specific experiences** — Following Marr's theory and complementary learning systems accounts, hippocampus is thought to encode specific episodic details, with pattern separation preventing interference between similar experiences.

4. **Interactions between frontal cortex and hippocampus support flexible behaviour** — Prior work suggests these regions interact during inference, rule learning, and when new task rules must be acquired.

The study was designed to test a specific hypothesis derived from spatial cognition research: that PFC might abstract task structure (like entorhinal grid cells abstract spatial structure) while hippocampus maps this abstraction onto specific sensorimotor contexts (like place cells map to specific environments).

---

### What this paper contributes

This paper provides direct empirical evidence for complementary roles of PFC and hippocampus in generalisation:

1. **Complementary abstraction and instantiation**: PFC maintains abstract, problem-general representations of task structure (trial stages, outcomes, policies) that are invariant to sensorimotor specifics, while hippocampus maps these abstractions onto specific sensorimotor contexts, showing 'remapping' between problems even when physical locations and meanings are identical.

2. **Dual temporal scales in PFC**: PFC simultaneously represents behaviour at different time scales—both immediate trial events (initiation, choice, outcome) and integrated policy over multiple trials—both in abstract, generalisable forms.

3. **Mechanistic insight into generalisation**: The paper demonstrates that generalisation relies on abstract representations in PFC that can be flexibly mapped to new sensorimotor contexts via hippocampal binding, providing a neural mechanism for 'schema' abstraction and transfer learning.

4. **Extension of spatial cognition principles to RL**: The findings demonstrate that principles established in spatial memory research (cortical abstraction, hippocampal specific encoding) generalise to non-spatial reinforcement learning tasks, unifying these fields.

5. **Meta-learning at the neural level**: The behavioural and neural data demonstrate meta-learning—faster acquisition of new problems with experience—and link this to the formation of abstract PFC representations that guide behaviour in novel situations.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)**: Maintains abstract, problem-general representations of trial structure (initiation, choice, outcome) and policy that generalise across problems with different sensorimotor implementations. Shows stronger outcome coding and trial stage representation compared to CA1. Represents policy at multiple temporal scales (within-trial events and across-trial integration) in abstract form.

- **Hippocampus (dorsal CA1)**: Represents sensorimotor-specific instantiations of task structure. Shows stronger coding of physical port location, choice identity (A vs B), and choice-outcome interactions compared to PFC. Exhibits 'remapping' between problems—different neurons represent the same event in different problems even when physical location and meaning are identical. Policy representations are tied to specific sensorimotor contexts and only generalise for choices at the same physical port.

---

### Mechanistic insight

This paper meets the high bar for mechanistic insight by presenting both a computational algorithm and neural data supporting that algorithm over alternatives.

**Computational level**: The brain solves the problem of generalising knowledge across structurally similar but sensorimotorily distinct problems by maintaining abstract representations of task structure (PFC) that can be flexibly bound to specific sensorimotor contexts (hippocampus).

**Algorithmic level**: 
- Task structure is represented as low-dimensional patterns of neural activity (temporal modes) corresponding to trial events (initiation, choice, outcome) and integrated policy
- PFC maintains stable cell assemblies (cellular modes) that represent these patterns consistently across problems, enabling abstraction
- Hippocampus dynamically remaps which cell assemblies represent which events based on sensorimotor context, enabling flexible binding of abstraction to specifics
- Representational similarity analysis reveals the structure of these mappings: PFC encodes trial stage and outcome abstractly; CA1 encodes port location and conjunctive features

**Implementational level**:
- Single-unit recordings from dorsal CA1 (345 neurons, 3 mice) and medial PFC (556 neurons, 4 mice)
- SVD decomposition separates cellular modes (co-active cell assemblies) from temporal modes (activity patterns over time/trial types)
- Cross-problem generalisation assessed by how well modes from one problem explain activity in another
- RSA with design matrices for abstract vs. specific features quantifies representational content
- Cross-problem decoding distinguishes abstract state vs. physical port representations

The key mechanistic insight is that generalisation emerges not from a single mechanism but from complementary specialisation: PFC provides stable abstract scaffolding (stable cell assemblies representing task structure), while hippocampus provides flexible contextual binding (remapping assemblies to sensorimotor specifics). This division of labour enables both generalisation (via PFC abstraction) and appropriate action in specific contexts (via hippocampal binding).

---

### Limitations & open questions

- **Recording methodology**: Recordings from PFC and CA1 were performed in separate groups of mice, not simultaneously, limiting direct assessment of interactions between regions during task performance.

- **Causal manipulation**: The study is correlational; causal tests (e.g., optogenetic manipulation) of whether PFC abstraction or hippocampal remapping is necessary for generalisation are not performed.

- **Anatomical specificity**: Recordings targeted dorsal CA1 and medial PFC; whether findings generalise to other hippocampal subfields or prefrontal subregions is unknown.

- **Task domain**: Findings are from a specific reversal learning paradigm; generalisation to other task structures and domains (e.g., spatial navigation, non-RL tasks) requires further study.

- **Mechanism of remapping**: The cause of hippocampal remapping between problems (sensory context change, reward location change, temporal discontinuity) is not fully dissociated.

- **Learning dynamics**: Neural recordings were performed after behavioural asymptote; the neural dynamics during initial learning of problem structure and the formation of abstract representations are not captured.

---

### Connections & keywords

- **Key citations**: Tse et al. (2007, 2011) on schemas and memory consolidation; Harlow (1949) on learning sets; Wang et al. (2018) on prefrontal cortex as meta-RL system; Wilson et al. (2014), Schuck et al. (2016) on OFC as cognitive map; Behrens et al. (2018), Whittington et al. (2020) on Tolman-Eichenbaum machine; Zhou et al. (2020) on evolving schema representations in OFC; Fyhn et al. (2007) on hippocampal remapping and grid realignment; Marr (1971), McNaughton & O'Reilly (1995) on complementary learning systems

- **Named models or frameworks**: Schema theory, learning set, transfer learning, meta-learning/meta-reinforcement learning, reinforcement learning, representational similarity analysis (RSA), singular value decomposition (SVD), Tolman-Eichenbaum Machine, complementary learning systems, cognitive map of task space

- **Brain regions**: medial prefrontal cortex (mPFC), dorsal CA1 (dCA1), hippocampus, entorhinal cortex (mentioned), orbitofrontal cortex (OFC, cited)

- **Keywords**: abstraction, generalisation, transfer learning, meta-learning, schema, reversal learning, representational similarity analysis, singular value decomposition, prefrontal cortex, hippocampus, cellular modes, temporal modes, policy representation, remapping, learning set, task structure, sensorimotor, electrophysiology, single-unit recording, mouse
