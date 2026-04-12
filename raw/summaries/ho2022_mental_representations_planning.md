---
source_file: "ho2022_mental_representations_planning.md"
paper_id: "ho2022_mental_representations_planning"
title: "People construct simplified mental representations to plan"
authors: "Mark K. Ho, David Abel, Carlos G. Correa, Michael L. Littman, Jonathan D. Cohen, Thomas L. Griffiths"
year: 2022
journal: "Nature"
paper_type: "computational"
contribution_type: "theoretical"
species: ["mouse", "human"]
tasks: ["navigation_task"]
brain_regions: ["prefrontal_cortex"]
frameworks: ["successor_representation"]
keywords: ["people", "construct", "simplified", "mental", "representations", "plan"]
key_citations: ["gershman2018_successor_representation_learning"]
---

### One-line summary

People plan by actively constructing simplified task representations — "value-guided construals" — that optimally balance cognitive complexity against utility for achieving goals, rather than planning over a fixed, complete representation.

---

### Background & motivation

Standard theories of planning in psychology, economics, and AI assume that a decision-maker has a fixed, complete representation of a task and then uses heuristics to limit the search over action sequences. This approach treats task representations as given rather than as something the agent controls. The paper argues that this misses a key source of planning efficiency: the ability to selectively simplify the task representation itself before planning. The gap being addressed is the lack of a principled, computationally grounded account of how people form simplified, purpose-built representations for planning, and the lack of empirical evidence bearing directly on this process.

---

### Methods

- **Model**: A Markov decision process (MDP) framework is extended with a "construal" layer. A construal is a subset of primitive cause–effect relationships (modelled as a product of experts over transition functions). The Value of Representation (VOR) for a construal equals its behavioural utility (expected return when executing the construal's optimal plan in the real environment) minus a cognitive cost equal to the cardinality of the construal. An outer optimisation selects the construal; an inner optimisation plans within it.
- **Paradigm**: Online maze-navigation task (Prolific platform). Participants navigated 2D mazes composed of a start, goal, fixed centre walls, and blue tetromino-shaped obstacles. Each obstacle corresponds to one cause–effect relationship. Fully observable but compositionally structured — all elements visible, but participants must decide which to integrate.
- **Experiments (all preregistered)**:
  - *Initial experiment* (n = 161): standard navigation with post-trial awareness probes (8-point scale) for each obstacle.
  - *Up-front planning experiment* (n = 162): obstacles hidden during execution; early-termination trials to isolate planning-phase awareness.
  - *Critical mazes recall experiment* (n = 156): obstacles visible only before first move; recall probes (forced choice + confidence) using "critical" obstacles — relevant to planning but far from the optimal path.
  - *Perception control* (n = 164/172) and *execution control* (n = 163/161): yoked baselines in which participants viewed identical mazes without planning, or followed breadcrumbs without planning, respectively.
  - *Process-tracing experiments* (n = 167/179): mouse-hovering paradigm in which obstacles are hidden until revealed by hovering, externalising the planning process.
- **Alternative models tested**: trajectory-based heuristic search (RTDP), graph-based heuristic search (LAO*), successor representation overlap, bottleneck state distance, and six perceptual/navigational distance measures — all compared in global HGLMs.
- **Analysis**: Hierarchical (generalised) linear models (HGLMs) with by-participant and by-maze random intercepts; likelihood ratio tests; AIC-based necessity and sufficiency analyses across 9 measures and 825 participants (84,215 observations total).

---

### Key findings

- Value-guided construal (VGC) predicted awareness of obstacles in the initial experiment: likelihood ratio test X²(1) = 2,297.21, p < 1×10⁻¹⁶, β = 0.133.
- VGC predicted recall accuracy and confidence in the critical mazes experiment: accuracy X²(1) = 249.34, p < 1×10⁻¹⁶, β = 0.648; confidence X²(1) = 432.76, p < 1×10⁻¹⁶, β = 0.104.
- VGC remained a significant, positive predictor of all planning measures after including perception-control and execution-control responses as covariates (e.g., accuracy: X²(1) = 106.36, p = 6.2×10⁻²⁵), ruling out perception and execution as sufficient explanations.
- VGC predicted hovering probability and hover duration in process-tracing experiments (initial mazes hovering: X²(1) = 1,221.76, p < 1×10⁻¹⁶; critical mazes hovering: X²(1) = 1,361.92, p < 1×10⁻¹⁶).
- In AIC knock-out analyses across all nine planning measures, removing VGC produced the largest or second-largest degradation in fit relative to all ten alternative predictors.
- VGC was the best or second-best single-predictor model across all measures, and was always a component of the best two-predictor model.
- A generalised construal-modification model (dynamic, sequential construal updating) achieved fitted R² values of 0.30–0.87 across all nine measures.
- Critically, VGC successfully identified "critical" obstacles — those relevant to planning but distant from the optimal path — which distance-based heuristics failed to capture.

---

### Computational framework

**Resource-rational / value of information framework**, instantiated via Markov decision processes with a nested optimisation structure.

- **What is modelled**: The selection of a task representation (construal) prior to and during planning. The agent chooses which subset of cause–effect relationships to include in an internal model of the task.
- **Key variables**: The set of primitive cause–effect relationships {φ₁, …, φN} (each a potential function over state-action-nextstate transitions); a construal c ⊆ {φ₁, …, φN}; the construed transition function T_c via a product-of-experts combination; the plan π_c optimal for T_c; the behavioural utility V^{π_c}(s₀) evaluated under the true dynamics; the cognitive cost C(c) = |c|; the Value of Representation VOR(c) = V^{π_c}(s₀) − λ|c|.
- **Key assumptions**: (i) Construals are subsets of primitive cause–effect relationships combined via a product of experts. (ii) Cognitive cost is proportional to the number of cause–effect relationships included (description-length/sparsity interpretation). (iii) The decision-maker selects construals via a softmax over VOR. (iv) The paper deliberately does not commit to an algorithmic account of how optimal construals are found — it is a normative, computational-level analysis.
- The framework generalises to a sequential construal-modification MDP in which the agent re-evaluates its construal at each state during planning, with a consistency cost penalising construal changes.

---

### Prevailing model of the system under study

The dominant framework the paper pushes against is the **Newell–Simon heuristic search model** and its descendants: a decision-maker holds a complete, fixed representation of a task (e.g., all chess pieces and rules), and reduces planning cost by limiting, pruning, or chunking the search over action sequences — not by simplifying the task representation itself. In psychology, this includes depth-limited planning, tree pruning, habit–goal-directed tradeoffs, and chunking of action sequences. In AI, it includes algorithms like RTDP and A*. The common assumption across all these approaches is that the task representation is given and fixed; only the planning computation over that representation is subject to resource constraints or heuristics. The paper also acknowledges accounts based on the successor representation and bottleneck-based subgoal selection as related representational mechanisms, but notes these are derived from fixed task dynamics rather than actively controlled construals.

---

### What this paper contributes

The paper demonstrates empirically and computationally that the task representation itself — not just the planning computation — is subject to active, value-guided control. Specifically:

- It formalises construal selection as an optimisation over a VOR criterion, providing a principled normative account of when and which task elements should be incorporated into a planning representation.
- It shows that this account predicts human attentional patterns during planning across multiple dependent measures (awareness, recall, confidence, mouse-hovering), multiple experimental designs, and after controlling for ten alternative mechanisms.
- Crucially, VGC correctly predicts that people represent obstacles that are relevant to planning but distant from the optimal path ("critical obstacles") — a pattern that distance-based heuristics and successor-representation accounts fail to capture.
- The results establish that planning-related attentional biases are not reducible to perceptual salience or execution byproducts.
- The framework conceptually links efficient planning to the broader problem of constructing purpose-built, simplified representations — connecting to work on object representation, structured abstraction, and resource rationality.

---

### Brain regions & systems

Not applicable. The paper is purely behavioural and computational with no anatomical focus. The level of analysis is Marr's computational level (what problem is being solved) and partially the algorithmic level (what representations are used). The paper explicitly notes that how people identify or learn optimal construals — and what neural mechanisms implement this — are open questions for future work. The framework is cited as relevant to prefrontal cortex function via its connection to cognitive control and the expected value of control (Miller & Cohen 2001; Shenhav et al. 2013), but no neural data are presented.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined here. It proposes a computational-level algorithm (VOR-based construal selection) and validates it against behavioural data, but does not provide neural recordings, imaging, lesion, or pharmacological data linking the model's specific variables (e.g., VOR computations, construal probabilities) to measured neural activity. The paper is explicitly framed as a normative, behavioural investigation; understanding the neural implementation is flagged as a key direction for future research.

---

### Limitations & open questions

- The paper establishes that people behave *as if* they optimally select construals, but provides no process-level account of how such optimal construals are identified or learned. The computational cost of exhaustive VOR evaluation is acknowledged; tractable algorithms for construal optimisation are discussed in a Supplementary Discussion but not evaluated empirically.
- The maze paradigm is fully observable and compositionally structured by design — generalisability to partially observable or non-compositional environments is unaddressed.
- The relationship between construal and other cognitive processes (attention, working memory, executive control) is not mechanistically specified; construal is inferred from downstream memory, not observed directly.
- The paper does not address how construal strategies are acquired across development or learning, or how they generalise across tasks.
- Neural substrates of the construal process — which brain regions implement the outer construal loop, and how they interact with planning circuits — remain entirely open.
- The cognitive cost function (cardinality of construal) is minimal and theoretically motivated by description length and sparsity, but its psychological basis is not directly tested.

---

### Connections & keywords

**Key citations**:
- Newell & Simon (1972/1976) — heuristic search, fixed task representation baseline
- Griffiths, Lieder & Goodman (2015); Lewis, Howes & Singh (2014); Gershman, Horvitz & Tenenbaum (2015) — resource rationality
- Miller & Cohen (2001); Shenhav, Botvinick & Cohen (2013); Shenhav et al. (2017) — cognitive control, expected value of control
- Stachenfeld, Botvinick & Gershman (2017) — hippocampus as predictive map, bottleneck states
- Gershman (2018) — successor representation
- Hinton (2002) — product of experts
- Gabaix (2014) — sparsity-based bounded rationality
- Callaway et al. (2022) — rational use of cognitive resources in planning

**Named models or frameworks**:
- Value-guided construal (VGC) — the paper's own model
- Value of Representation (VOR)
- Construal modification MDP
- Heuristic search (RTDP, LAO*)
- Successor representation
- Product of experts
- Resource-rational analysis

**Brain regions**: None (purely behavioural/computational paper)

**Keywords**: value-guided construal, task representation, resource rationality, planning, Markov decision process, bounded rationality, cognitive control, problem solving, attention and memory, maze navigation, description length, sparsity, heuristic search, successor representation, nested optimisation
