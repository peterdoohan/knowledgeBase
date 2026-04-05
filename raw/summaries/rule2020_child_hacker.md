---
source_file: rule2020_child_hacker.md
title: The Child as Hacker
authors: Joshua S. Rule, Joshua B. Tenenbaum, Steven T. Piantadosi
year: 2020
journal: Trends in Cognitive Sciences
paper_type: review
contribution_type: theoretical
---

### One-line summary

Children's learning can be understood as "hacking"—iteratively improving mental representations (symbolic programs) along multiple dimensions through diverse, intrinsically motivated techniques—extending beyond current Bayesian program induction models that focus narrowly on simplicity and fit.

---

### Background & motivation

Human cognitive development presents a radical challenge: children universally acquire sophisticated cognitive abilities (intuitive theories, language, mathematics) that exceed current AI capabilities, yet do so simultaneously and efficiently. Existing computational models of learning as program induction (Bayesian LOT models) reduce learning to stochastic search for simple, accurate programs. However, real human learning involves richer objectives and more diverse techniques than these models capture. This paper proposes that "hacking"—a style of programming emphasizing iterative improvement along multiple dimensions through internally motivated goals—provides a better metaphor for understanding children's learning.

---

### Methods

This is a theoretical/review paper that synthesizes existing literature across cognitive science and computer science. The paper:

- Reviews existing "learning as programming" frameworks in cognitive science
- Draws on software engineering literature (particularly refactoring and program synthesis) to characterize hacking practices
- Uses arithmetic learning (sum-to-min strategy transition) as a concrete example to illustrate the framework
- Compares the child as hacker to related metaphors (child as scientist, workshop/evolutionary metaphors)
- Surveys recent developments in program induction and synthesis from machine learning

---

### Key findings

- **Learning as programming is well-established**: Symbolic programs provide the best formal account of human algorithmic knowledge across domains (logic, mathematics, language, intuitive theories). Learning can be understood as program induction—discovering programs that explain observed data.

- **Current models are too narrow**: Most Bayesian LOT models reduce learning to stochastic search for short, accurate programs (simplicity + fit). Real programmers use many more techniques (debugging, refactoring, adding types, extracting functions) and pursue many more values (speed, modularity, generality, elegance, robustness).

- **Hacking provides a richer framework**: Hackers iteratively improve code along multiple dimensions through diverse techniques, guided by constantly shifting internal goals. This captures:
  - Multiple values beyond simplicity (Table 1 lists 18 values including accuracy, speed, modularity, generality, elegance, novelty)
  - Multiple techniques beyond parameter tuning (Table 2 lists 13 techniques including adding functions, debugging, refactoring, profiling, writing libraries, inventing languages)
  - Intrinsic motivation and dynamic goal management

- **Arithmetic learning exemplifies hacking**: Children's progression from sum to min strategy (and beyond) shows hallmark hacking features:
  - Multiple strategies maintained simultaneously (not single-best)
  - Strategies optimized for different values (speed, memory, accuracy)
  - Discovery of structural insights (commutativity) enabling improvements
  - Transition from procedural to memory-based solutions (retrieval)

---

### Computational framework

The paper proposes **program induction** as the computational framework, specifically extended through the metaphor of **hacking**. Key elements:

- **Representational level**: Symbolic programs (language of thought) provide Turing-complete expressive power for representing knowledge
- **Learning as search**: Finding programs that explain observed data, but with important extensions:
  - Search guided by multiple objectives (not just simplicity + fit)
  - Search uses diverse transformation operators (not just stochastic sampling)
  - Search is intrinsically motivated with dynamically changing goals
- **Evaluation metrics**: Programs assessed on many dimensions (accuracy, conciseness, speed, efficiency, modularity, generality, robustness, elegance, novelty, etc.)

The framework draws on:
- Bayesian program learning (Goodman, Tenenbaum, Piantadosi)
- Inductive programming and program synthesis (Gulwani et al.)
- Software engineering practices (Fowler's refactoring)
- Resource rationality (Lieder & Griffiths)
- Novelty search (Lehman & Stanley)

---

### Prevailing model of the system under study

The prevailing model of cognitive development includes several related frameworks:

1. **Child as scientist**: Children construct intuitive theories (causal models) about the world, using epistemic practices similar to scientists—collecting evidence, revising theories based on evidence, seeking accurate, general, and simple explanations. This view has been formalized using Bayesian inference over causal networks and probabilistic programs.

2. **Rational constructivism**: Emphasizes sophisticated learning mechanisms including Bayesian statistical inference, constructive thinking processes (analogy, mental simulation, learning by thinking), and active curiosity-driven exploration.

3. **Learning as programming (current LOT models)**: Learning is program induction—finding short, accurate programs that explain data. Learners stochastically sample from posterior distributions over programs, balancing simplicity (prior) and fit (likelihood).

4. **Overlapping waves (Siegler)**: Development involves maintaining multiple strategies, with selection based on context-specific utility, rather than uniform stage-like progressions.

---

### What this paper contributes

This paper extends and enriches the prevailing models in several ways:

1. **Broader view of representations**: Programs may go beyond purely causal models to include procedural knowledge, libraries, and even new programming languages for specific domains. This suggests formalizing intuitive theories as domain-specific libraries or languages for writing generative programs.

2. **Richer objectives**: Learning is guided by many values beyond accuracy, generality, and simplicity (Table 1). The paper identifies 18 values including speed, efficiency, modularity, elegance, novelty, robustness, and portability. Learners may prioritize different values at different times, and may even choose less accurate or more complex solutions if they win on other dimensions.

3. **More diverse learning mechanisms**: Learning uses many techniques beyond stochastic sampling (Table 2). The paper identifies 13 techniques including adding functions, debugging, refactoring, profiling, handling errors, writing libraries, and inventing languages. These techniques operate at multiple timescales and can be combined in flexible ways.

4. **Intrinsic motivation and dynamic goal management**: Learners generate their own goals, pursuing them for intrinsic reward rather than just extrinsic utility. Goals change dynamically based on progress, boredom, getting stuck, or pursuing other projects. This explains children's efficient learning despite seemingly random, piecemeal behavior.

5. **Concrete application to arithmetic**: The paper demonstrates how the framework explains the well-studied sum-to-min transition and related phenomena in arithmetic learning, showing how hacker-like values and techniques map onto actual developmental patterns.

---

### Brain regions & systems

Not applicable. This is a theoretical/computational paper that does not focus on specific neural implementations. The paper proposes that mental representations are analogous to symbolic programs, but does not specify how these are implemented neurally. The authors note that this is an algorithmic-level theory that remains to be connected to neural implementation.

---

### Mechanistic insight

This paper does **not** meet the high bar for mechanistic insight because it does not provide neural data supporting a specific algorithm over alternatives. However, it does propose a formal algorithmic framework that could guide future empirical work.

The paper proposes that learning operates at Marr's **computational** and **algorithmic** levels:

- **Computational level**: The problem is program induction—finding programs that explain observed data. The goal is to find programs that are accurate, concise, and satisfy other hacker values (speed, modularity, elegance, etc.).

- **Algorithmic level**: The processes include diverse techniques for improving programs (adding functions, debugging, refactoring, profiling, etc.) and dynamic goal management for selecting which values to optimize. These go beyond the stochastic sampling mechanisms typically assumed in Bayesian LOT models.

- **Implementational level**: Not addressed. The paper notes that connecting the algorithmic-level theory to neural implementation remains an important direction for future work.

The paper's contribution is in expanding the algorithmic-level description of learning to include a broader set of values and techniques inspired by hacking. While this provides a richer formal framework, it does not yet provide the neural evidence required to establish a mechanistic account.

---

### Limitations & open questions

The paper acknowledges several limitations and open questions:

- **Lack of formal implementation**: The child as hacker is currently a metaphor and conceptual framework, not a formal computational model. Developing such models will require sustained interdisciplinary effort similar to what produced formal models of the child as scientist.

- **Lack of neural grounding**: The algorithmic-level theory remains to be connected to neural implementation. How hacking-like processes are implemented in the brain is unknown.

- **Many empirical questions**: Which hacking techniques are attested in children and when do they appear? Which values guide children's learning? How can individual learning episodes be interpreted as improving code? How do children move through the space of computationally expressive hypotheses?

- **Core knowledge mapping**: How can core knowledge be mapped to an initial codebase? How can domain-specific knowledge be modeled as code libraries?

- **Integration of symbolic and statistical information**: How does the mind integrate symbolic/discrete and statistical/continuous information during learning?

- **Goal management**: What data structures support goal management? How do children move between different learning objectives?

---

### Connections & keywords

**Key citations:**
- Fodor (1975) - Language of Thought
- Goodman et al. (2008) - Church probabilistic programming language
- Goodman et al. (2015) - Probabilistic language of thought
- Lake et al. (2017) - Building machines that learn and think like people
- Siegler & Jenkins (1989) - How Children Discover New Strategies
- Siegler (1996) - Emerging Minds (overlapping waves/evolutionary metaphors)
- Schulz (2012) - The origins of inquiry
- Gopnik (2012) - Scientific thinking in young children
- Tenenbaum et al. (2011) - How to grow a mind
- Baum (2004) - What Is Thought?

**Named models or frameworks:**
- Child as hacker (novel contribution)
- Learning as programming
- Language of Thought (LOT)
- Probabilistic Language of Thought
- Child as scientist
- Rational constructivism
- Overlapping waves (Siegler)
- Workshop metaphor (Siegler)
- Evolutionary metaphor (Siegler)
- Resource rationality
- Novelty search
- Program induction
- Bayesian program learning

**Brain regions:**
- Not applicable (theoretical/computational paper)

**Keywords:**
- cognitive development
- program induction
- language of thought
- computational modeling
- symbolic representations
- arithmetic learning
- strategy discovery
- intuitive theories
- Bayesian learning
- software engineering
- intrinsic motivation
- cognitive architecture
---
