---
source_file: goel2013_prefrontal_planning_real_world.md
paper_id: goel2013_prefrontal_planning_real_world
title: "Lesions to right prefrontal cortex impair real-world planning through premature commitments"
authors:
  - "Vinod Goel"
  - "Oshin Vartanian"
  - "Angela Bartolo"
  - "Lila Hakim"
  - "Anna Maria Ferraro"
  - "Valeria Isella"
  - "Ildebrando Appollonio"
  - "Silvia Drei"
  - "Paolo Nichelli"
year: 2013
journal: Neuropsychologia
paper_type: empirical
contribution_type: empirical
species:
  - human
methods:
  - lesion
brain_regions:
  - prefrontal_cortex
frameworks:
  - successor_representation
keywords:
  - right_prefrontal_cortex
  - ill_structured_problem_solving
  - real_world_planning
  - lateral_transformations
  - vertical_transformations
  - abstract_representations
  - premature_commitment
  - verbal_protocol_analysis
  - frontal_lobe_lesions
  - planning_phases
  - concrete_to_abstract_ratio
  - problem_space
  - lesions
  - right
  - prefrontal
  - cortex
  - impair
  - real
  - world
  - planning
---

### One-line summary

Focal lesions to right prefrontal cortex (but not left PFC or posterior cortex) impair real-world travel planning by driving an over-reliance on concrete representations and premature commitment to solutions before the problem space has been adequately explored.

---

### Background & motivation

The prefrontal cortex is well-established as critical for planning and problem-solving, but prior work has not cleanly dissociated the hemispheric contributions of left versus right PFC. Most planning studies use well-structured tasks (e.g., Tower of London/Hanoi) that require precise, concrete representations and a pre-specified state space. Real-world planning is qualitatively different: it begins as an ill-structured problem requiring vague, abstract representations to explore a broad solution space, before progressively narrowing into more concrete, well-structured phases. Goel (2010) hypothesised that right PFC selectively supports the early, abstract-representation-dependent phases, and that its damage would therefore produce premature concretisation and substandard real-world plans — a prediction this study tests directly.

---

### Methods

- **Design**: Between-groups lesion study with verbal protocol analysis.
- **Participants**: 20 participants across four groups (n=5 each): right PFC lesion (RPFC), left PFC lesion (LPFC), posterior lesion, and healthy normal controls (NC). Patients were matched on age, education, visuospatial IQ, abstract reasoning, and verbal comprehension; no baseline neuropsychological differences were found across groups.
- **Task**: Travel Planning Task (TPT) — participants planned a one-week trip to Italy for a fictional couple, with fixed budget (€3,500), time, and conflicting interests as constraints. Participants had access to a detailed pamphlet and were asked to think aloud.
- **Data collection**: Sessions were videotaped; verbal protocols and written notes were collected. Two raters (blind to group) coded transcripts.
- **Coding scheme**: A trilevel verbal protocol coding scheme (Goel & Pirolli, 1992) was applied:
  - *Plan phase level*: problem-scoping, preliminary planning, refinement, detailing, monitoring.
  - *Episode level*: goals/subgoals (destination, travel, accommodation, sightseeing, eating) and constraints.
  - *Statement level*: operator type (add, propose, evaluate, modify, elaborate, justify, qualify, etc.), content, and abstractness rating (abstract / intermediate / concrete).
- **Key measures**: Quality of plan (completeness + reasonableness, 1–5 scale, inter-rater alpha = .80); concrete-to-abstract statement ratio; time on task; number of statements; operator and episode distributions.
- **Lesion localisation**: MRI/CT scans processed in MEDx/ABLe software; lesions mapped to Brodmann areas via Talairach-space registration.

---

### Key findings

- **Plan quality**: RPFC patients produced significantly lower-quality plans than NC (F[3,16]=4.76, p=.015, partial η²=.47); LPFC and posterior groups did not differ significantly from NC.
- **Time on task**: RPFC and posterior patients spent significantly less time on the task than NC (RPFC M=28.75 min vs NC M=58.80 min; F[3,16]=4.31, p=.024, η²=.48); LPFC patients did not differ from any group.
- **Concrete-to-abstract ratio**: RPFC patients had a significantly higher ratio of concrete-to-abstract statements than NC (F[3,16]=3.90, p=.029, partial η²=.42; Dunnett p=.016); no other group differed from NC.
- **Temporal analysis**: The concrete-to-abstract ratio was significantly elevated for RPFC patients in the middle phase of planning (F[3,15]=4.28, p=.023, η²=.46), with a general trend toward excess concreteness across all phases.
- **Operators, episodes, and planning phases**: No significant between-group differences were found in operator distributions (except NC produced more "qualify" statements), episode types, or allocation of time to problem-solving phases — the deficit was specific to the abstractness dimension.
- NC showed a "judicious interplay" of concrete and abstract representations; RPFC patients locked into concrete detail prematurely.

---

### Computational framework

Not applicable in a formal sense — the paper does not instantiate a mathematical model. However, the paper is organised around a problem-space framework (Newell & Simon tradition, formalised by Goel, 1995) in which:

- A **state space** is traversed by applying **operators** (lateral transformations: movement between ideas; vertical transformations: movement toward detail).
- Real-world problems begin ill-structured and require **lateral transformations** supported by vague, abstract representations; they become progressively well-structured requiring **vertical transformations** supported by concrete representations.
- The key computational claim is that right PFC selectively encodes and maintains abstract/vague representations that enable lateral search; its loss collapses problem-solving prematurely into the concrete, vertical-transformation regime.

This framework could be mapped onto successor representation or tree-search models (breadth of exploration vs depth), though the paper does not make that connection explicitly.

---

### Prevailing model of the system under study

Prior to this paper, the dominant view — largely from split-brain research and neuroimaging of Tower of London/Hanoi tasks — was that the *left* PFC is dominant for planning and problem-solving, with the right PFC playing a minor or purely visuospatial role. Neuroimaging studies of the ToL showed predominantly left or bilateral DLPFC activation. Where lateralisation was found, the left hemisphere was favoured. Some frontal lesion studies found either no hemispheric difference in planning deficits, or worse performance in left-hemisphere patients. The prevailing assumption was therefore that both hemispheres contribute roughly equally (or left > right) to planning, especially in the standard laboratory tasks used.

A secondary assumption was that planning deficits following frontal lobe damage are hemisphere-nonspecific in quality — a general executive impairment — rather than reflecting hemisphere-specific processing modes.

---

### What this paper contributes

The paper establishes, using focal lesion methodology and fine-grained verbal protocol analysis, that the right PFC makes a specific and selective contribution to real-world planning that is not captured by standard well-structured tasks: it supports the maintenance of abstract, vague representations that enable lateral exploration of the problem space. Without this right-PFC contribution, planners prematurely commit to concrete solutions before adequately exploring alternatives.

Concretely:
- We can now say that right PFC is *specifically* required for real-world (ill-structured) planning, while LPFC and posterior lesions produce no detectable planning deficit on this task.
- The locus of the right PFC deficit is the representation system (abstractness), not the operator set, episode structure, or planning-phase allocation.
- This dissociates right PFC from general executive control and from monitoring (no difference in metacognitive monitoring statements), identifying a more specific function: sustaining vague, exploratory representations.
- The results extend Goel & Grafman (2000) from a single-case design to a five-patient RPFC group, and add appropriate comparison groups (LPFC, posterior, NC).

---

### Brain regions & systems

- **Right prefrontal cortex (RPFC)** — primary lesion group; proposed as the locus of abstract-representation support for lateral transformations in ill-structured problem-solving. Lesions centred on right dorsolateral and ventrolateral PFC regions (Brodmann areas quantified via ABLe software; specific BAs listed in Table 2 of the paper, predominantly right frontal).
- **Left prefrontal cortex (LPFC)** — comparison lesion group; theorised by the authors to support concrete, well-structured problem-solving phases. No planning deficit was observed for LPFC patients on this task, consistent with the prediction that LPFC is more critical for later, more structured phases.
- **Posterior cortex** — second comparison lesion group; no planning deficit observed, confirming frontal specificity.
- The paper does not examine subcortical structures or network-level connectivity.

---

### Mechanistic insight

The paper partially meets the bar. It presents a clear process-level algorithm (abstract-to-concrete progression through lateral then vertical transformations) and links it to neural data (focal lesion performance). However, it does not provide neural recordings, imaging, or pharmacology that pinpoint *how* right PFC implements abstract representations at the circuit or cell level.

- **Computational level**: The problem is to explore a large, poorly constrained solution space before committing to a plan. The brain must maintain vague, underspecified representations long enough to generate and evaluate alternative lateral branches before collapsing to a concrete solution.
- **Algorithmic level**: Right PFC is proposed to encode and sustain abstract/vague state representations that permit lateral operators (shifting between ideas) rather than only vertical operators (deepening a single idea). Damage forces the system into an exclusively concrete-vertical mode, narrowing the search tree prematurely and locking in substandard solutions.
- **Implementational level**: Not addressed. The paper maps deficits to right PFC broadly but does not specify cell types, laminar organisation, neuromodulatory mechanisms, or connectivity patterns responsible for abstract representation maintenance.

The paper therefore provides Marr-level-1 and partial level-2 insight, but not level-3.

---

### Limitations & open questions

- **Small sample size**: n=5 per group; results should be interpreted cautiously, especially given the modest statistical power.
- **Lesion heterogeneity**: Lesion locations within the RPFC group are not perfectly homogeneous; the study focuses on right PFC broadly rather than making fine-grained subregion claims.
- **Left PFC null result**: The theoretical framework predicts that LPFC patients should be impaired in the later, well-structured phases (excess abstraction), but this was not observed. The authors suggest the task may not have been long enough or demanding enough to expose these difficulties, or that the lesions did not damage the critical LPFC subregions.
- **Possible age/education confound**: NC showed a non-significant trend toward being younger and more educated than the patient groups, which could contribute to performance differences.
- **No neuroimaging of controls**: The paper cannot specify which precise RPFC subregions are necessary vs. sufficient; only that right frontal lesions as a group produce the deficit.
- **Generalisability**: The task is a single real-world planning scenario; it is unclear whether findings generalise across different types of ill-structured problems.
- **Open question**: What is the neural mechanism by which right PFC sustains abstract representations? Would specific subregions (e.g., right ventrolateral vs. dorsolateral PFC) show dissociable roles?

---

### Connections & keywords

**Key citations**:
- Goel & Grafman (2000) — prior single-case study of right PFC in ill-structured problem solving (architectural design)
- Goel, Grafman, Tajik, Gana & Danto (1997) — financial planning task in frontal patients; verbal protocol methodology
- Kaller, Rahm, Spreer, Weiller & Unterrainer (2011) — Tower of London double dissociation between left and right DLPFC (goal hierarchy vs. search depth)
- Goel (2010) — theoretical framework on lab vs. real-world problems and representational requirements
- Goel (1995) — problem space framework and lateral vs. vertical transformations
- Shallice & Burgess (1991) — frontal lobe strategy application deficits and real-world tasks
- Ericsson & Simon (1993) — verbal protocol analysis methodology
- Roca et al. (2010) — frontal lobe lesions and impaired abstraction

**Named models or frameworks**:
- Problem-space framework (Goel/Newell-Simon tradition): state space, operators, lateral vs. vertical transformations
- Ill-structured vs. well-structured problem distinction
- Verbal protocol analysis (Ericsson & Simon, 1993)
- Travel Planning Task (TPT)
- Tower of London (ToL) / Tower of Hanoi — contrasted, not used

**Brain regions**:
- Right prefrontal cortex (RPFC)
- Left prefrontal cortex (LPFC)
- Posterior cortex (comparison group)

**Keywords**: right prefrontal cortex, ill-structured problem solving, real-world planning, lateral transformations, vertical transformations, abstract representations, premature commitment, verbal protocol analysis, frontal lobe lesions, planning phases, concrete-to-abstract ratio, problem space
