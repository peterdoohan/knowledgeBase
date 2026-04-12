---
source_file: wilson2017_scientific_computing.md
paper_id: wilson2017_scientific_computing
title: "Good enough practices in scientific computing"
authors:
  - "Wilson G"
  - "Bryan J"
  - "Cranston K"
  - "Kitzes J"
  - "Nederbragt L"
  - "Teal TK"
year: 2017
journal: "PLOS Computational Biology"
paper_type: review
contribution_type: review
frameworks:
  - bayesian_inference
keywords:
  - reproducible_research
  - data_management
  - version_control
  - software_engineering
  - tidy_data
  - scientific_computing
  - open_science
  - project_organization
  - collaborative_research
  - research_workflow
  - data_sharing
  - code_quality
  - open_source_licensing
  - computational_reproducibility
  - research_data_management
  - good
  - enough
  - practices
  - scientific
  - computing
key_citations:
  - wilson2014_best_practices_scientific
---

### One-line summary

A set of accessible, pragmatic computing practices for researchers new to scientific computing, covering data management, software development, collaboration, project organization, version control, and manuscript preparation.

---

### Background & motivation

Computers are now essential in all branches of science, but most researchers lack training in basic lab skills for research computing. This gap leads to data loss, inefficient analyses, and limited ability to work effectively with software and data. While a previous paper addressed "best practices" for experienced computational researchers, there was a need for entry-level recommendations that novices could adopt without overwhelming complexity.

---

### Methods

This perspective synthesizes recommendations from:
- The authors' personal experience in software and data carpentry
- Software Carpentry and Data Carpentry workshops (delivered to >11,000 people since 2010)
- Published guides on reproducible research and data management
- Community feedback and practical adoption criteria

Inclusion criteria for practices: (1) large numbers of researchers use it, and (2) large numbers continue using it months after first trying it.

---

### Key findings

**Data management:**
- Save raw data in its original form with read-only protection
- Back up data in multiple locations, including off-site or cloud storage
- Create "tidy data" where each column is a variable and each row is an observation
- Record all data processing steps via scripts rather than manual actions
- Use unique identifiers for records when working with multiple tables
- Submit data to DOI-issuing repositories (Figshare, Dryad, Zenodo) for accessibility

**Software:**
- Write modular code using short, single-purpose functions (<60 lines, <6 parameters)
- Place explanatory comments at the start of every program with usage examples
- Use meaningful variable and function names following language conventions
- Eliminate code duplication by writing reusable functions
- Search for and test well-maintained libraries before writing new code
- Make dependencies explicit via requirements.txt or README
- Provide simple test datasets for validation
- Submit code to DOI-issuing repositories

**Collaboration:**
- Create a project README with overview, contact info, and usage examples
- Create a CONTRIBUTING file with setup instructions and guidelines
- Maintain a shared to-do list (plain text or issue tracker)
- Decide on explicit communication strategies (email, chat, video)
- Make licenses explicit (CC-0/CC-BY for data/text, MIT/BSD/Apache for software)
- Make projects citable via CITATION file

**Project organization:**
- Put each project in its own directory named after the project
- Use `doc/` for text documents (manuscripts, notebooks)
- Use `data/` for raw data and metadata
- Use `results/` for generated files (cleaned data, figures, tables)
- Use `src/` for source code (human-readable scripts)
- Use `bin/` for compiled programs
- Name files to reflect content/function, not sequence numbers or figure positions

**Tracking changes:**
- Back up everything created by humans
- Keep changes small and focused
- Share changes frequently among collaborators
- Use a checklist for saving and sharing changes
- Store projects in folders mirrored off the working machine
- Use version control systems (Git, Mercurial) when possible

**Manuscripts:**
- Two approaches: (1) online tools with formatting/tracking (e.g., Google Docs), or (2) plain text with version control (Markdown/LaTeX)
- Online tools are more accessible for non-technical collaborators
- Plain text enables full reproducibility and version control integration
- Supplementary materials should use accessible formats (CSV, JSON, not PDF)

---

### Computational framework

Not applicable. This is a review/position paper on research computing practices rather than a computational modeling study. However, the paper provides guidelines that would apply to researchers using various computational frameworks (Bayesian inference, statistical modeling, machine learning, etc.) in their work.

---

### Prevailing model of the system under study

The paper assumes a prevailing landscape where computational research is often conducted ad hoc by researchers without formal training in software engineering or data management. The authors identify common problematic practices: data loss due to poor backup strategies, irreproducible analyses from manual data manipulation, collaboration friction from email-based document exchange, and software that is difficult to understand, test, or reuse. The paper responds to an earlier "Best Practices for Scientific Computing" (2014) that was targeted at experienced computational researchers, recognizing that a lower-barrier entry point was needed for novices.

---

### What this paper contributes

This paper establishes "good enough practices" as a pragmatic, incremental approach to research computing that balances immediate usability with long-term benefits. The key contributions are:

1. **A validated, accessible starting point**: The recommendations are derived from extensive workshop experience (>11,000 participants) and filtered by actual adoption rates—not just theoretical merit.

2. **Two-tier manuscript workflow**: The paper explicitly acknowledges collaboration barriers with non-technical researchers and provides both accessible (Google Docs) and rigorous (plain text + version control) approaches.

3. **Clear scope boundaries**: The "What we left out" section explicitly excludes advanced practices (branches, unit testing, CI, profiling) that would overwhelm beginners, providing a clear learning progression.

4. **Practical project organization**: The concrete directory structure (`data/`, `src/`, `results/`, `doc/`) provides an immediately implementable template.

5. **Licensing and citation guidance**: Explicit recommendations for Creative Commons (data/text) and permissive open source (software) licenses address common confusion about intellectual property in research.

---

### Brain regions & systems

Not applicable. This paper focuses on computational research practices and software engineering principles rather than biological systems or brain regions.

---

### Mechanistic insight

Not applicable. This paper does not propose an algorithm supported by neural data, nor does it address Marr's levels of analysis. It is a prescriptive methodology paper offering practical recommendations for improving research computing workflows. The paper focuses on sociotechnical practices (project organization, version control, collaboration) rather than biological mechanisms.

---

### Limitations & open questions

**Acknowledged limitations:**
- The recommendations target small-scale projects (single researchers or small groups, days to months duration), not large software engineering efforts
- Practices are filtered by adoption likelihood—some valuable practices (code review, unit testing, continuous integration) are excluded because newcomers are unlikely to adopt them
- The two-tier manuscript approach acknowledges a trade-off between accessibility and rigor

**Open questions raised:**
- How can institutional incentives (PIs, universities, funding agencies) better support training in these practices?
- What is the most effective way to transition researchers from "good enough" to more advanced practices as projects scale?
- How can version control systems better accommodate large files and non-technical collaborators?
- What role can research librarians and peer learning groups play in sustaining these practices?

---

### Connections & keywords

**Key citations:**
- Wilson et al. 2014 "Best Practices for Scientific Computing" (predecessor paper for experienced researchers)
- Gentzkow & Shapiro 2014 "Code and Data for the Social Sciences"
- Noble 2009 "A Quick Guide to Organizing Computational Biology Projects"
- Wickham 2014 "Tidy Data"
- Sandve et al. 2013 "Ten Simple Rules for Reproducible Computational Research"
- Hart et al. 2016 "Ten simple rules for digital data storage"

**Named models or frameworks:**
- Tidy data principles (Wickham)
- Software Carpentry/Data Carpentry workshop methodology
- Manual versioning vs. version control systems
- Project organization templates (Noble's rules)

**Brain regions:**
- Not applicable

**Keywords:**
reproducible research, data management, version control, software engineering, tidy data, scientific computing, open science, project organization, collaborative research, research workflow, data sharing, code quality, open source licensing, computational reproducibility, research data management
