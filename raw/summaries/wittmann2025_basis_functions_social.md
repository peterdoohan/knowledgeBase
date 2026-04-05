---
source_file: wittmann2025_basis_functions_social.md
title: Basis functions for complex social decisions in dorsomedial frontal cortex
authors: Marco K. Wittmann, Yongling Lin, Deng Pan, Moritz N. Braun, Cormac Dickson, Lisa Spiering, Shuyi Luo, Caroline Harbison, Ayat Abdurahman, Sorcha Hamilton, Nadira S. Faber, Nima Khalighinejad, Patricia L. Lockwood, Matthew F. S. Rushworth
year: 2025
journal: Nature
paper_type: empirical
contribution_type: empirical
---

### One-line summary

The dorsomedial prefrontal cortex (dmPFC) and anterior cingulate cortex (ACC) represent combinatorial possibilities for social interaction using basis functions—a compressed, low-dimensional format that enables efficient decision-making in multi-agent contexts, rather than relying exclusively on agent-centric representations.

---

### Background & motivation

Navigating social environments requires tracking relationships between multiple individuals, which becomes computationally demanding as group size increases due to exponential growth in possible relationships. Traditional models suggest the brain uses agent-centric coding, tagging information to specific individuals like "oneself" or "the other," but this approach struggles with the combinatorial complexity of multi-person interactions. The authors propose that the brain might instead use basis functions—a compressed, dimensionality-reduced representation that captures patterns of social interaction rather than individual identities, similar to coding schemes observed in visual, motor, and spatial domains.

---

### Methods

- **Study 1 (Social fMRI experiment)**: 56 participants performed a memory-guided social decision-making task during fMRI scanning. Participants observed performance sequences of four players (self, partner, two opponents) presented in randomized order, then made binary engage/avoid decisions comparing team performances.
- **Task design**: Each trial comprised an observation phase (performance cues for all four players shown sequentially, 0.2s per cue) and a decision phase (binary comparison of cued players from memory). Three decision types: self decisions (self vs. opponent), partner decisions (partner vs. opponent), and group decisions (self+partner vs. both opponents).
- **Basis function framework**: Three orthogonal basis functions (w1 = [-1, 1, -1, 1], w2 = [1, 1, -1, -1], w3 = [1, -1, -1, 1]) define a 3D subspace of the 4D sequential performance space. Performance scores projected onto these basis functions via dot products (b = W·pos).
- **Study 2 (Behavioral experiment)**: 795 participants in a between-subjects design comparing group condition (including group decisions) vs. no-group condition (only self/partner decisions) to test whether basis function compression improves decision accuracy.
- **Study 3 (Control fMRI experiment)**: 32 participants performed a non-social motor version of the task (comparing finger tap counts assigned to left/right hand fingers) to test domain-generality of basis function coding.
- **Analyses**: fMRI GLMs tested for neural correlates of basis function projections while controlling for agent-centric representations; ROI analyses using independent ROIs; drift-diffusion modeling of decision dynamics; Bayesian model comparison.

---

### Key findings

- **Agent-centric representations replicated**: Perigenual ACC encoded self-performance and dmPFC encoded partner performance during the decision phase, replicating previous findings; participants were more accurate (P=0.041) and faster (P<0.001) for self vs. partner decisions, replicated in study 2 (both P<0.001).
- **Basis function coding in dmPFC/ACC**: Neural activity in dmPFC/ACC encoded projections onto all three basis functions during the observation phase: b1 (t55=2.886, P=0.006), b2 (t55=2.749, P=0.008), b3 (t55=3.081, P=0.003); aggregate mean effect (t55=5.02, P<0.001, Cohen's d=0.671); null vector showed no effect (P=0.820, BF01=6.684).
- **Sequential relevance sorting**: Basis functions were organized by relevance for upcoming decisions; primary basis functions (sufficient for group decisions) were processed before secondary basis functions (needed for dyadic decisions); drift-diffusion modeling showed significant onset asynchrony between primary and secondary basis functions in self decisions (t55=3.71, P<0.001) and partner decisions (t55=2.20, P=0.032).
- **Behavioral signatures of basis function compression**: The model predicted that irrelevant players would inappropriately influence decisions based on team membership; this was confirmed in self decisions (partner effect: P=0.003; irrelevant opponent: P<0.001) and partner decisions (both irrelevant player effects: P<0.001).
- **Group condition improves decision accuracy**: Participants in the group condition (with group decisions) showed higher accuracy on matched self decisions (P=0.038) and partner decisions (P=0.024) compared to the no-group condition, despite the superficially more complex task; decision weights for relevant players were stronger in the group condition (self: P=0.002; partner: P=0.003).
- **Domain-generality of basis function coding**: The control fMRI experiment (motor task) showed significant basis function effects in pgACC (P=0.003) and frontal pole; however, self-biases and socially-specific inverted basis functions in dmPFC/vStr were absent, suggesting shared basis function computations with domain-specific social processing stages.
- **Decision variables in vmPFC**: Final decision variables (chosen-unchosen) were encoded in vmPFC in both social and motor tasks, suggesting a common final pathway for decision-making across domains.

---

### Computational framework

The paper employs a **basis function** computational framework, which compresses high-dimensional social information into a low-dimensional representational space. The core formalism involves three orthogonal basis functions (w1 = [-1, 1, -1, 1], w2 = [1, 1, -1, -1], w3 = [1, -1, -1, 1]) that define a 3D subspace of the 4D sequential performance space. Performance scores are projected onto these basis functions via dot products (b = W·pos), yielding compressed representations that can be linearly combined to construct any decision variable needed for the task.

The framework assumes that: (1) social information can be efficiently compressed without loss of task-relevant information; (2) representations are sequentially organized by relevance (primary vs. secondary basis functions) to enable hierarchical decision-making; and (3) the same coding principles may operate across social and non-social domains, with domain-specific processing layered atop shared basis function computations.

---

### Prevailing model of the system under study

The prevailing model of social cognition, as described in the paper's introduction, posits that the brain represents social information in an **agent-centric** manner, tagging knowledge about abilities or attitudes to specific individuals such as "oneself" or "the other." This framework has informed understanding of key social brain regions, particularly the dorsomedial prefrontal cortex (dmPFC) and anterior cingulate cortex (ACC), which are thought to track self-relevant and other-relevant information. According to this model, navigating social environments requires maintaining independent representations of each individual's identity and their relationships, a process that becomes increasingly computationally demanding as group size increases.

---

### What this paper contributes

This paper demonstrates that the brain does not rely exclusively on agent-centric representations but instead employs **basis functions**—compressed, combinatorial representations that capture patterns of social interaction rather than individual identities. The findings show that dmPFC and ACC encode sequential basis functions that efficiently summarize the social task space, enabling flexible decision-making in multi-agent contexts. This challenges the prevailing agent-centric model by showing that social information is organized along abstract dimensions (basis functions) that are orthogonal to individual identity.

The paper establishes that these representations are sorted by relevance and integrated sequentially during decision-making, with primary basis functions (sufficient for group decisions) influencing choices earlier than secondary basis functions (needed for dyadic decisions). This serial organization explains why participants make more accurate decisions in contexts that include group decisions, despite the superficially more complex task space. Furthermore, the demonstration of similar basis function coding in a non-social motor task suggests these are general computational principles that extend beyond the social domain, with domain-specific processing layered atop shared basis function computations.

---

### Brain regions & systems

- **Dorsomedial prefrontal cortex (dmPFC)**: Primary locus of basis function representations during observation phase; extends from (−2, 28, 44) to (2, 48, 18) MNI; also encodes partner performance and opponent-related signals during decision phase; shows stronger inverted social basis function effects than motor basis functions.
- **Perigenual anterior cingulate cortex (pgACC)**: Encodes self-performance during decision phase; also shows basis function effects during observation phase; peak at (−8, 42, 14) MNI; primary region where basis function effects replicate across social and motor tasks.
- **Anterior cingulate cortex (ACC) gyrus**: Adjacent to dmPFC; shows basis function encoding extending from dmPFC.
- **Ventromedial prefrontal cortex (vmPFC)**: Encodes final decision variables (chosen vs. unchosen value differences) during decision phase; shows social DV (chosen–unchosen) in social task and motor DV in control task; peak around (−2, 60, −12) MNI; represents common final pathway for decision-making across domains.
- **Ventral striatum (vStr)**: Encodes inverted social basis functions during decision phase; shows stronger effects in social vs. motor task; peak around (−6, 14, −2) and (8, 18, −2) MNI.
- **Lateral prefrontal cortex (lPFC)**: Encodes inverted social basis functions during decision phase; shows stronger effects in social vs. motor task; peak around (−44, 42, 4) MNI.
- **Frontal pole**: Shows prominent basis function effects in the control (motor) fMRI experiment; peak around (−14, 56, 24) MNI; shows uniformly positive effects for all three basis function projections.
- **Lateral primary motor cortex**: Shows stronger activation in motor vs. social task during decision phase.

---

### Mechanistic insight

This paper meets the high bar for mechanistic insight by presenting a formal algorithm (basis functions) and providing neural data that specifically support that algorithm over alternatives (agent-centric models).

**Computational**: The brain must solve the problem of efficiently representing and navigating social environments with multiple interacting agents. The problem is computationally challenging because the number of possible relationships grows exponentially with group size. The basis function framework provides a compressed, low-dimensional representation that preserves task-relevant information while reducing computational load. The computational goal is to enable flexible decision-making across varying social contexts without requiring independent representations for every possible combination of individuals.

**Algorithmic**: The representations and processes are implemented via three orthogonal basis functions (w1 = [-1, 1, -1, 1], w2 = [1, 1, -1, -1], w3 = [1, -1, -1, 1]) that define a 3D subspace of the 4D sequential performance space. Performance scores are projected onto these basis functions via dot products (b = W·pos). The algorithm involves: (1) encoding sequential performance information into basis function projections during the observation phase; (2) sorting basis functions by relevance—primary basis functions (sufficient for group decisions) are processed before secondary basis functions (needed for dyadic decisions); (3) sequentially integrating basis functions during decision-making with temporal asynchrony (confirmed by drift-diffusion modeling); (4) transforming basis functions into agent-centric decision variables through inversion for final choice.

**Implementational**: The basis function algorithm is realized in specific neural hardware. The dmPFC and ACC implement the basis function encoding during the observation phase, with neural activity covarying with projections onto the three basis functions (t55 = 2.886, P=0.006 for b1; t55 = 2.749, P=0.008 for b2; t55 = 3.081, P=0.003 for b3). The vmPFC implements the final decision variable computation, showing chosen-unchosen value differences. The ventral striatum and lateral PFC implement inverted basis functions during decision-making. The frontal pole shows basis function effects in the non-social motor task. Drift-diffusion modeling confirms the sequential integration algorithm with significant onset asynchrony between primary and secondary basis functions (t55 = 3.71, P<0.001 for self decisions). The paper also provides formal mathematical proofs that the basis functions are orthogonal and sufficient to construct all decision variables in the task.

---

### Limitations & open questions

- **Effect sizes**: The basis function effects show moderate effect sizes, and future research should establish their relative importance in social processes compared to agent-centric representations.
- **Generalization to naturalistic social contexts**: The task used a structured, game-like scenario with defined teams and performance metrics; whether basis function coding extends to more naturalistic, unstructured social interactions remains to be tested.
- **Relationship to identity construction**: The paper proposes that basis functions may serve as a computational scaffold for constructing player identities, but the developmental trajectory and causal relationship between basis functions and agent-centric representations are not established.
- **Neural implementation differences across domains**: While basis function coding was found in both social and motor tasks, the precise neural implementations differed (e.g., frontal pole in motor vs. dmPFC/ACC in social), and the reasons for these differences require further investigation.
- **Causal role of dmPFC/ACC**: The fMRI results are correlational; causal manipulation (e.g., via TMS or lesion studies) is needed to establish the necessity of dmPFC/ACC basis function encoding for social decision-making.
- **Temporal dynamics of basis function integration**: While drift-diffusion modeling revealed onset asynchrony between primary and secondary basis functions, the precise temporal dynamics and neural mechanisms of this sequential integration remain to be fully characterized.

---

### Connections & keywords

- **Key citations**: Behrens et al. 2018 (cognitive maps), Chang & Tsao 2017 (face processing basis functions), Tanji & Shima 1994 (motor sequence coding), Pouget & Sejnowski 1997 (parietal basis functions), Wittmann et al. 2016 (self-other mergence), Lockwood et al. 2018 (self-other ownership), Constantinescu et al. 2016 (grid-like codes), Stachenfeld et al. 2017 (hippocampal predictive maps), Sadtler et al. 2014 (neural constraints on learning), Maier et al. 2020 (attribute integration in decisions)
- **Named models or frameworks**: Basis function framework, Drift-diffusion model (DDM), Agent-centric coding model, Cognitive map theory, Predictive coding, Hierarchical decision process, General linear model (GLM)
- **Brain regions**: Dorsomedial prefrontal cortex (dmPFC), Perigenual anterior cingulate cortex (pgACC), Anterior cingulate cortex (ACC), Ventromedial prefrontal cortex (vmPFC), Ventral striatum (vStr), Lateral prefrontal cortex (lPFC), Frontal pole, Lateral primary motor cortex
- **Keywords**: basis functions, social decision-making, dorsomedial prefrontal cortex, anterior cingulate cortex, multi-agent interactions, sequential coding, representational compression, agent-centric coding, group decisions, ventromedial prefrontal cortex, drift-diffusion model, fMRI, combinatorial representations, decision variables, cognitive maps, self-other distinction
