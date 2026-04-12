---
source_file: "wilson2017_good_practices_computing.md"
paper_id: "wilson2017_good_practices_computing"
title: "Good enough practices in scientific computing"
authors: "Greg Wilson, Jennifer Bryan, Karen Cranston, Justin Kitzes, Lex Nederbragt, Tracy K. Teal"
year: 2017
journal: "PLoS Computational Biology"
paper_type: "review"
contribution_type: "review"
keywords: ["wilson_et_al_2014_best_practices_for_scientific_computing_predecessor_paper_for_experienced_computational_researchers", "gentzkow_and_shapiro_2014_code_and_data_for_the_social_sciences_a_practitioners_guide", "noble_2009_a_quick_guide_to_organizing_computational_biology_projects", "wickham_2014_tidy_data_journal_of_statistical_software", "hunt_and_thomas_1999_the_pragmatic_programmer", "martin_2008_clean_code", "mcconnell_2004_code_complete", "named_models_or_frameworks", "tidy_data_principles_wickham", "software_carpentry_data_carpentry_teaching_methodology", "manual_versioning_workflow", "version_control_systems_git", "mercurial", "subversion", "brain_regions", "not_applicable", "keywords", "scientific_computing", "research_reproducibility", "data_management"]
key_citations: ["wilson2014_best_practices_scientific"]
---

### One-line summary

A set of accessible, pragmatic computing practices for researchers new to scientific computing, covering data management, software development, collaboration, project organization, version control, and manuscript preparation.

---

### Background & motivation

Computers are now essential in all branches of science, yet most researchers receive no training in basic lab skills for research computing. This leads to lost data, unnecessarily long analyses, and limited effectiveness in working with software and data. While a previous paper (Wilson et al., 2014) addressed best practices for experienced computational researchers, this paper targets the larger group of researchers who are new to scientific computing and need accessible starting points—the "good enough" practices that provide immediate benefits without overwhelming complexity.

---

### Methods

This is a consensus-based practice guide synthesizing recommendations from:
- The authors' collective experience in scientific computing
- Software Carpentry and Data Carpentry workshops (delivered to over 11,000 people since 2010)
- Published guides including Gentzkow & Shapiro (2014), Noble (2009), Wickham (2014), and others
- Community feedback from researchers across disciplines

The recommendations were filtered based on two criteria: (1) large numbers of researchers use them, and (2) large numbers continue using them months after first trying them out.

---

### Key findings

The paper presents actionable recommendations across six domains:

**Data management (7 practices):**
- Save raw data in its original form with read-only protection
- Backup raw data in multiple locations, including off-site
- Create analysis-friendly "tidy" data where each column is a variable and each row is an observation
- Record all data processing steps via scripts rather than manual manipulation
- Use unique identifiers for every record to enable merging across tables
- Submit data to DOI-issuing repositories (Figshare, Dryad, Zenodo) for citation and access

**Software (10 practices):**
- Place explanatory comments at the start of every program with usage examples
- Decompose programs into functions under 60 lines with 5-6 parameters maximum
- Eliminate code duplication through reusable functions and data structures
- Search for well-maintained libraries before writing new code
- Test libraries before relying on them
- Use meaningful variable and function names following language conventions
- Make dependencies explicit via requirements.txt or README sections
- Use conditional statements instead of commenting/uncommenting code sections
- Provide simple test datasets for verification
- Submit code to DOI-issuing repositories upon publication

**Collaboration (5 practices):**
- Create a project overview README with purpose, contact info, and usage examples
- Create a shared to-do list (plain text or issue tracker)
- Decide on and publicize communication strategies (email, chat, video)
- Make licensing explicit via LICENSE file (CC-0/CC-BY for data/text, MIT/BSD/Apache for software)
- Make the project citable via CITATION file with DOI information

**Project organization (6 practices):**
- Put each project in its own named directory
- Place text documents in `doc` subdirectory
- Place raw data in `data` and generated files in `results` subdirectories
- Place source code in `src` directory
- Place compiled programs in `bin` directory
- Name all files to reflect content/function, avoiding sequential numbers or manuscript locations

**Tracking changes (8 practices):**
- Back up almost everything created by humans immediately
- Keep changes small and focused
- Share changes frequently among collaborators
- Create and use a checklist for saving and sharing changes
- Store projects in folders mirrored off the working machine (Dropbox, GitHub)
- Manual approach: maintain CHANGELOG.txt in reverse chronological order
- Manual approach: copy entire project when significant changes are made
- Full version control: use Git, Mercurial, or Subversion

**Manuscripts (2 approaches):**
- **Approach 1:** Use online tools with rich formatting (Google Docs) for ease of collaboration
- **Approach 2:** Write in plain text (Markdown/LaTeX) with version control for full reproducibility and audit trail

---

### Computational framework

Not applicable. This paper is a practice guide synthesizing recommendations for research computing workflows rather than a computational modeling study. It provides a framework for organizing and documenting computational research rather than modeling a specific neural or cognitive process.

---

### Prevailing model of the system under study

The paper describes the status quo in scientific computing as of 2017: most researchers lack training in computational best practices, leading to ad hoc workflows where data is at risk of being lost, analyses are difficult to reproduce, and collaboration is hampered by poor documentation and organization. The authors assume that the field has recognized these problems but existing recommendations (including their own 2014 "Best Practices" paper) were too advanced for researchers new to computing.

---

### What this paper contributes

This paper establishes a baseline of "good enough" practices that provide immediate benefits without overwhelming complexity. It extends the authors' earlier work by targeting researchers who are new to scientific computing rather than experienced computational scientists. The key contribution is a curated, consensus-based set of recommendations that:

1. Are accessible to researchers with limited computational background
2. Have been validated through extensive teaching (11,000+ workshop participants)
3. Balance immediate productivity gains against learning curve costs
4. Provide a pathway toward more advanced practices (version control, etc.)

The paper also explicitly identifies practices that were deliberately excluded (branches, build tools, unit testing, continuous integration, etc.) because they don't provide sufficient benefit for small-scale projects relative to their learning costs.

---

### Brain regions & systems

Not applicable. This paper focuses on research computing practices and workflows rather than neural systems or brain regions. The target domain is methodology and scientific practice across all disciplines using computation.

---

### Mechanistic insight

Not applicable. This paper does not propose or test a computational algorithm against neural data. It provides recommendations for organizing and documenting computational research. The "mechanism" here refers to workflow practices (version control, project organization, data management) rather than neural or cognitive mechanisms.

---

### Limitations & open questions

The paper acknowledges several limitations:

1. **Scope limitation**: The recommendations are designed for researchers working alone or with a small group of collaborators on projects lasting days to several months. Large-scale software engineering projects require additional practices (code review, continuous integration, etc.) that are deliberately excluded here.

2. **Learning curve barriers**: Even the "good enough" practices may be challenging for some researchers. The authors explicitly note that explaining version control or plain text manuscript workflows to busy collaborators (e.g., "overworked physicians") can be prohibitive.

3. **Adoption challenges**: The paper notes that change is hard, and if researchers don't see benefits quickly enough to justify the pain, they will switch back to old ways. This creates a tension between recommending practices that are immediately useful versus those that pay off only at scale.

4. **Tool evolution**: The paper acknowledges that some recommended tools (e.g., Git Large File Storage) were not yet mature enough to recommend, suggesting that tool recommendations may need updating as technologies evolve.

Open questions identified:
- How can institutions better support adoption of these practices (training, infrastructure)?
- How can the cost of implementing data management plans be properly valued and funded?
- What is the most effective way to introduce version control to newcomers?
- How can collaborative workflows balance ease of use with reproducibility requirements?

---

### Connections & keywords

**Key citations:**
- Wilson et al. (2014) - "Best Practices for Scientific Computing" (predecessor paper for experienced computational researchers)
- Gentzkow & Shapiro (2014) - "Code and Data for the Social Sciences: A Practitioner's Guide"
- Noble (2009) - "A Quick Guide to Organizing Computational Biology Projects"
- Wickham (2014) - "Tidy Data" (Journal of Statistical Software)
- Hunt & Thomas (1999) - "The Pragmatic Programmer"
- Martin (2008) - "Clean Code"
- McConnell (2004) - "Code Complete"

**Named models or frameworks:**
- Tidy data principles (Wickham)
- Software Carpentry / Data Carpentry teaching methodology
- Manual versioning workflow
- Version control systems (Git, Mercurial, Subversion)

**Brain regions:**
Not applicable

**Keywords:**
scientific computing, research reproducibility, data management, version control, software engineering practices, project organization, tidy data, open science, collaborative research, computational workflow, research data management, Git, Software Carpentry
