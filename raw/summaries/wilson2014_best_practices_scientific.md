---
source_file: wilson2014_best_practices_scientific.md
title: Best Practices for Scientific Computing
authors: Greg Wilson, D. A. Aruliah, C. Titus Brown, Neil P. Chue Hong, Matt Davis, Richard T. Guy, Steven H. D. Haddock, Kathryn D. Huff, Ian M. Mitchell, Mark D. Plumbley, Ben Waugh, Ethan P. White, Paul Wilson
year: 2014
journal: PLoS Biology
paper_type: review
contribution_type: review
---

### One-line summary

A set of 24 evidence-based best practices for scientific software development that improve code reliability and programmer productivity while reducing errors.

---

### Background & motivation

Scientists increasingly rely on software for research, spending 30% or more of their time developing it, yet 90% are primarily self-taught and lack exposure to basic software engineering practices. This skills gap leads to software errors that have caused high-profile retractions in major journals (Science, PNAS, etc.). The paper addresses this gap by synthesizing decades of research and experience into actionable recommendations.

---

### Methods

- Review and synthesis of existing literature on software engineering practices
- Analysis of empirical studies of scientific computing and software development
- Collective experience from the authors' work teaching computing to scientists
- Survey of guidelines from commercial and open-source software development
- Reference to studies on code review, debugging, and software maintenance

---

### Key findings

The paper presents 24 best practices organized into 8 categories:

1. **Write programs for people, not computers**
   - Don't require readers to hold more than a handful of facts in memory (1a)
   - Make names consistent, distinctive, and meaningful (1b)
   - Make code style and formatting consistent (1c)

2. **Let the computer do the work**
   - Make the computer repeat tasks (2a)
   - Save recent commands in a file for re-use (2b)
   - Use a build tool to automate workflows (2c)

3. **Make incremental changes**
   - Work in small steps with frequent feedback (3a)
   - Use a version control system (3b)
   - Put everything created manually in version control (3c)

4. **Don't repeat yourself (or others)**
   - Every piece of data must have a single authoritative representation (4a)
   - Modularize code rather than copying and pasting (4b)
   - Re-use code instead of rewriting it (4c)

5. **Plan for mistakes**
   - Add assertions to programs to check their operation (5a)
   - Use an off-the-shelf unit testing library (5b)
   - Turn bugs into test cases (5c)
   - Use a symbolic debugger (5d)

6. **Optimize software only after it works correctly**
   - Use a profiler to identify bottlenecks (6a)
   - Write code in the highest-level language possible (6b)

7. **Document design and purpose, not mechanics**
   - Document interfaces and reasons, not implementations (7a)
   - Refactor code in preference to explaining how it works (7b)
   - Embed documentation for a piece of software in that software (7c)

8. **Collaborate**
   - Use pre-merge code reviews (8a)
   - Use pair programming when appropriate (8b)
   - Use an issue tracking tool (8c)

---

### Computational framework

Not applicable. This is a methodology review paper that does not propose a specific computational model. However, the paper discusses how various computational frameworks (numerical integration, matrix operations, etc.) should be implemented using established libraries rather than rewritten from scratch.

---

### Prevailing model of the system under study

Before this paper, the prevailing situation in scientific computing was characterized by:
- Scientists spending 30%+ of time on software development without formal training
- 90% of scientists being self-taught programmers
- Lack of awareness of basic software engineering practices (version control, testing, code review)
- Software errors causing significant retractions in high-profile journals
- Widespread practice of rewriting rather than reusing code
- Limited adoption of automation tools in scientific workflows

---

### What this paper contributes

This paper establishes a comprehensive, evidence-based set of best practices for scientific software development that:
- Synthesizes decades of research and collective experience into 24 actionable recommendations
- Demonstrates that software errors have caused retractions in major scientific journals (Science, PNAS, JMB, etc.)
- Shows that adopting these practices is cost-effective (time investment is quickly offset by productivity gains)
- Provides a roadmap for incremental adoption of practices rather than requiring wholesale change
- Establishes that treating software as experimental apparatus (to be validated like physical equipment) is necessary for reproducible research

---

### Brain regions & systems

Not applicable. This is a computational/methodology paper with no neuroanatomical focus.

---

### Mechanistic insight

This paper does not meet the mechanistic insight bar as defined. While it presents structured recommendations (algorithms for good software development practice), it does not provide neural data supporting any specific algorithm. The paper is purely methodological, synthesizing best practices from software engineering and computer science literature without empirical neural validation.

The paper could be described as providing a "computational level" framework (what problem is being solved: reliable, maintainable scientific software) and "algorithmic level" recommendations (how to implement solutions through specific practices), but without any "implementational level" neural evidence.

---

### Limitations & open questions

- The paper explicitly excludes discussion of reproducible research, publication/citation of code and data, and open science as independent issues (though notes these will be easier with the described skills)
- The recommendations are a starting point, not comprehensive — more advanced practices are available through resources like Software Carpentry
- The paper does not address how to fund or incentivize adoption of these practices at institutional levels
- Limited discussion of field-specific variations in software development needs
- No empirical data presented on adoption rates or effectiveness in specific scientific domains

---

### Connections & keywords

**Key citations:**
- Hannay et al. 2009 (scientific software development survey)
- Prabhu et al. 2011 (computational science practice survey)
- Hatton 1994, 1997 (scientific software accuracy studies)
- Merali 2010 (Nature article on scientific programming errors)
- Fagan 1976 (code inspections)
- McConnell 2004 (Code Complete)
- Hunt & Thomas 1999 (The Pragmatic Programmer / DRY principle)
- Martin 2002 (Agile software development)
- Oram & Wilson 2010 (Making Software)

**Named models or frameworks:**
- Agile development / Scrum / XP
- DRY (Don't Repeat Yourself) Principle
- Version Control Systems (VCS)
- Unit testing / Integration testing / Regression testing
- Defensive programming
- Build tools (Make, SCons)
- Code review / Pair programming
- Issue tracking
- Profiling and optimization

**Brain regions:**
- Not applicable

**Keywords:**
scientific computing, software engineering, best practices, version control, unit testing, code review, agile development, reproducibility, software quality, defensive programming, code documentation, automation, DRY principle, pair programming, debugging, profiling
