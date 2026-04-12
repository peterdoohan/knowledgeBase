---
source_file: liu2023_hippocampus_amygdala_memory_formation.md
paper_id: liu2023_hippocampus_amygdala_memory_formation
title: "Emerging many-to-one weighted mapping in hippocampus-amygdala network underlies memory formation"
authors:
  - "Jun Liu"
  - "Arron F Hall"
  - "Dong V Wang"
year: 2023
journal: "bioRxiv (preprint)"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - optogenetics
  - electrophysiology
  - tetrode_recording
  - behavioral_analysis
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - entorhinal_cortex
  - amygdala
  - basolateral_amygdala
keywords:
  - hippocampusamygdala_communication
  - sharp_wave_ripples
  - memory_consolidation
  - contextual_fear_conditioning
  - many_to_one_weighted_mapping
  - bla_cell_assemblies
  - independent_component_analysis
  - glm_population_decoding
  - closed_loop_optogenetics
  - sleep_dependent_consolidation
  - episodic_memory_indexing
  - dual_site_electrophysiology
  - emerging
  - many
  - one
  - weighted
  - mapping
  - hippocampus
  - amygdala
  - network
key_citations:
  - fernandez2019_ripples_memory_consolidation
  - girardeau2009_ripples_spatial_memory
  - buzsaki2015_hippocampal_sharp_wave_ripple
---

### One-line summary

During contextual fear memory formation in mice, the majority of dorsal CA1 hippocampal neurons rapidly establish weighted communications with a small, preconfigured basolateral amygdala assembly — a "many-to-one weighted mapping" that is consolidated during sleep via sharp-wave ripples and is causally necessary for memory formation.

---

### Background & motivation

The formation of episodic memories requires coordinated activity across brain regions, particularly the hippocampal dorsal CA1 (dCA1) and the basolateral amygdala (BLA), but how these regions encode and exchange information at the population level remains poorly understood. Two competing hypotheses exist for how the hippocampus encodes the "what" of episodic events: sparse coding in distributed ensembles, and a binding/linking role for the hippocampus that does not itself store event content. Neither hypothesis has been directly tested against the other at the level of dCA1–BLA ensemble interactions. The paper aims to fill this gap by characterising the network-level communication principle between dCA1 and BLA across all stages of memory — acquisition, consolidation, and retrieval.

---

### Methods

- **Subjects**: Male C57BL/6 mice (3–4 months old); n = 5 mice for in vivo recording, n = 22 mice (3 groups) for closed-loop optoinhibition.
- **Task**: Contextual fear conditioning (up to 10 footshocks, 0.75 mA); behavioural phases: pre-training sleep, training, post-training sleep, contextual recall test.
- **Electrophysiology**: Dual-site in vivo tetrode recording of dCA1 (up to 16 tetrodes) and BLA (up to 16 tetrodes) simultaneously in freely behaving mice throughout all memory phases. Local field potentials and single-unit spikes recorded continuously.
- **Assembly detection**: Independent component analysis (ICA) of BLA population spike matrices to identify co-activation assemblies (Marchenko–Pastur threshold for significant components; activation events defined at >5 s.d.).
- **Ripple classification**: Sharp-wave ripples band-pass filtered 100–250 Hz; "memory-associated ripples" defined as those coinciding with BLA memory assembly activation (>2 s.d.) within 150 ms, and with BLA assembly showing >5-fold footshock response sustained ≥10 min.
- **GLM decoding**: Generalised linear models (log link) trained on 50% of ripples to predict BLA assembly firing rate from dCA1 population spike counts across 100-ms time windows; prediction power quantified as correlation coefficient.
- **Closed-loop optoinhibition**: AAV-CaMKII-stGtACR2 bilaterally in BLA; dCA1 ripples (>8 s.d. amplitude) triggered immediate bilateral BLA inhibition (0.5 mW, 150 ms) during 2 h post-training rest/sleep. Three groups: closed-loop, delayed (~160 ms), no-stimulation.
- **Statistics**: ANOVA with Bonferroni post-hoc, Wilcoxon rank-sum, Student's t test; significance threshold p < 0.05.

---

### Key findings

- A small subset of BLA neurons formed a "BLA memory assembly" (identified by ICA) that robustly increased activity after a subset of dCA1 ripples in post-training sleep, but not in pre-training sleep — indicating an emergent dCA1-ripple-to-BLA-assembly communication that arises specifically with learning.
- BLA assemblies were largely preconfigured (pre-existing before training), but only the memory assembly developed new coupling to dCA1 ripples after learning; communication was strongest in early post-training sleep and gradually decayed.
- Memory-associated dCA1 ripples had significantly larger amplitude and longer duration than non-memory ripples; they contained distinct spike content, with approximately one-third of dCA1 neurons increasing and one-third decreasing activity specifically during memory-associated ripples.
- GLM decoding showed that dCA1 population spikes reliably predicted BLA memory assembly firing rate during post-training sleep (significant across multiple time windows, e.g., p = 0.0002 for 0–100 ms window) but not pre-training sleep; prediction of non-memory BLA neurons decreased after learning (p = 0.0002–0.0008), suggesting learning biases dCA1 output toward newly formed memories.
- Both high-weight and low-weight dCA1 neurons (top 50% vs. bottom 50% by BLA-assembly correlation) contributed to decoding BLA assembly activity, demonstrating that the mapping is distributed across the dCA1 population — the "many-to-one" principle.
- Place cells were distributed similarly across high- and low-weight dCA1 neurons with comparable place field sizes (p = 0.22), indicating that spatial and non-spatial (memory) coding are carried by partially overlapping dCA1 populations.
- Closed-loop BLA optoinhibition triggered by large dCA1 ripples immediately after training significantly impaired contextual fear memory (reduced freezing vs. delayed and no-stimulation groups; p = 0.0013, F2,19 = 9.583; post-hoc p = 0.0303 and p = 0.0011), causally demonstrating that dCA1-ripple-coincident BLA activity is necessary for memory consolidation.
- Anatomical tracing confirmed that dCA1 does not project directly to BLA; communication is di-synaptic via entorhinal, perirhinal, and ectorhinal cortices, consistent with the ~35 ms dCA1→BLA lag observed electrophysiologically.

---

### Computational framework

Not a formal computational framework paper, but the study is framed around the concept of **weighted population coding** and **population-level decoding**. The core idea is that distinct dCA1 population activity vectors establish unique weighted projections (many-to-one mappings) onto a specific BLA assembly, effectively implementing a form of rapid one-shot associative binding.

The GLM decoder formalises this: BLA assembly spike count is modelled as a log-linear function of dCA1 population spike counts across time bins, with learned weights capturing the emergent communication structure. The framework assumes that the key representational variable is the population firing pattern (not single-neuron activity), that weights are rapidly established via a mechanism akin to long-term potentiation during acquisition, and that ripple-associated reactivations during sleep consolidate these mappings. The many-to-one architecture provides high coding capacity (combinatorially many possible dCA1 patterns) and robustness/redundancy (no single dCA1 neuron is essential).

---

### Prevailing model of the system under study

The paper situates itself against two established hypotheses for how hippocampal CA1 encodes episodic event content ("what"). The first is **sparse coding**: event information is sparsely distributed across small ensembles of hippocampal neurons. The paper notes this has limited empirical support; in fact recent findings show up to 50% of CA1 neurons activate during fear memory procedures and up to 30% co-activate across two distinct contexts, inconsistent with sparse representations. The second is the **binding/linking hypothesis**: the hippocampus does not itself encode event information but instead links distributed representations across other brain areas. While conceptually influential (Eichenbaum, Fortin), this view lacks a mechanistic account of how CA1 achieves such linking.

Beyond encoding, the prevailing view of dCA1–BLA interactions holds that: (1) BLA neurons form distinct assemblies representing salient events; (2) dCA1 ripples during sleep play a critical role in memory consolidation; (3) some correlated reactivation between dCA1 and BLA exists during sleep (Girardeau et al. 2017); and (4) BLA assemblies may be preconfigured prior to learning (Miyawaki & Mizuseki, 2022). However, the specific population-level communication principle — how many dCA1 neurons relate to which BLA assembly, and whether this relationship is learning-dependent — was unknown.

---

### What this paper contributes

The paper proposes and provides evidence for a specific new principle: **many-to-one weighted mapping**, in which the majority of dCA1 neurons collectively establish differentiated (weighted) communication with a single, small BLA memory assembly specifically as a consequence of learning. This extends previous work in three ways:

1. It moves beyond pairwise dCA1–BLA neuron correlations (Girardeau et al. 2017) to characterise the full population-level relationship, showing that a large fraction of dCA1 neurons (not just a selective few) contribute to indexing the memory.
2. It demonstrates that this mapping is learning-dependent and emerges de novo: while BLA assemblies are preconfigured, their coupling to dCA1 ripples is not — it arises specifically after training and decays over early post-training sleep.
3. It provides causal evidence that dCA1-ripple-coincident BLA activity is necessary for consolidation: closed-loop optoinhibition of BLA locked to large-amplitude ripples impairs fear memory, whereas delayed (by ~150 ms) stimulation does not.

The findings reframe dCA1 as an indexing device that rapidly creates unique weighted mappings rather than directly encoding event content or merely binding pre-formed codes, offering a mechanistic middle ground between the sparse-coding and binding hypotheses.

---

### Brain regions & systems

- **Dorsal CA1 (dCA1)** — proposed to index episodic events by establishing many-to-one weighted mappings to BLA assemblies; generates sharp-wave ripples during slow-wave sleep that drive memory consolidation; encodes both spatial (place cells) and non-spatial (event) information in partially overlapping populations.
- **Basolateral amygdala (BLA)** — forms preconfigured assemblies that represent salient events; a specific small "BLA memory assembly" develops new coupling to dCA1 ripples after learning; causally required for memory consolidation during post-training sleep.
- **Entorhinal cortex (deep layers), perirhinal cortex, ectorhinal cortex** — identified as the di-synaptic relay pathway between dCA1 and BLA (confirmed by anterograde and retrograde tracing); the locus of the many→fewer convergence in the anatomical hierarchy.

---

### Mechanistic insight

The paper meets both criteria for this section.

**Phenomenon**: Episodic fear memory formation requires coordinated hippocampus–amygdala communication, but the population-level principle governing how dCA1 encodes and transmits event information to the BLA was unknown.

**Computational level**: The brain must rapidly create a unique, stable index for a new episodic event that can be reactivated during sleep to consolidate long-term memory. The problem is to assign a specific BLA assembly (representing the emotional/motivational significance of the event) to a unique dCA1 population code for that event, enabling later retrieval via pattern completion.

**Algorithmic level**: Many dCA1 neurons simultaneously acquire differentiated weights in their communication with a specific BLA memory assembly during acquisition (likely via rapid LTP). This many-to-one mapping is represented as a population activity vector in dCA1 → weighted projection → scalar assembly activation in BLA. During post-training slow-wave sleep, large-amplitude, elongated dCA1 ripples reactivate the specific subset of dCA1 neurons (with both increases and decreases relative to baseline) that carry the memory-specific content, driving the BLA memory assembly. This reactivation is most prominent in early post-training sleep. GLM decoding demonstrates that the full dCA1 population (both high- and low-weight neurons) is necessary for reliable prediction of BLA assembly activity.

**Implementational level**: Addressed partially. The communication is anatomically di-synaptic via deep-layer entorhinal/perirhinal/ectorhinal cortices (confirmed by tracing), consistent with the 35 ms dCA1→BLA lag. BLA pyramidal neurons are the target of optoinhibition (CaMKII-promoter stGtACR2), implicating excitatory BLA cells in consolidation. The ripple oscillation (100–250 Hz) is the temporal carrier; memory-associated ripples are selectively larger in amplitude and longer in duration, and triggered at high threshold (8 s.d.) in the closed-loop experiment. The paper does not resolve which specific cell types or synaptic mechanisms implement the rapid weight changes during acquisition.

**Bonus**: The paper provides direct causal evidence linking the algorithm (ripple-triggered BLA activation) to the phenomenon (memory consolidation) via closed-loop optogenetics. The anatomical specificity of the relay pathway is confirmed with tracing data.

---

### Limitations & open questions

- Small sample size for electrophysiology experiments (n = 5 mice); GLM decoding restricted to the 3 mice with ≥50 simultaneous dCA1 neurons.
- The paper does not resolve whether the mechanism of rapid weight establishment during acquisition is LTP or another plasticity mechanism; this remains speculative.
- The di-synaptic relay via entorhinal/perirhinal/ectorhinal cortex is anatomically confirmed but the intermediate population dynamics (how convergence from ~400k dCA1 to ~83k BLA neurons is achieved) are not measured.
- Memory-associated ripples showed larger amplitude in mice, whereas a previous study in rats found no amplitude difference; species differences are noted but not resolved.
- It is unclear whether many-to-one weighted mapping generalises beyond contextual fear memory to other episodic memory types, or whether the BLA assembly specifically represents the aversive valence component rather than contextual content per se.
- The paper does not directly address retrieval mechanisms: how dCA1–BLA communication during recall relates to the pattern established during acquisition and consolidation.
- The preprint had not undergone peer review at the time of posting (September 2023).

---

### Connections & keywords

**Key citations**:
- Girardeau, Inema & Buzsaki (2017) — hippocampus–amygdala reactivation during sleep
- Miyawaki & Mizuseki (2022) — preconfigured BLA assemblies
- Fernandez-Ruiz et al. (2019) — long-duration ripples improve memory
- Rothschild, Eban & Frank (2017) — GLM decoding of cortical–hippocampal communication
- Girardeau et al. (2009) — ripple suppression impairs spatial memory
- Buzsaki (2015) — hippocampal sharp wave-ripple review
- Kitamura et al. (2017) — engrams and circuits for memory consolidation

**Named models or frameworks**:
- Many-to-one weighted mapping (novel framework proposed here)
- ICA-based assembly detection (Lopes-dos-Santos et al., 2013)
- GLM decoding
- Contextual fear conditioning (standard paradigm)
- Closed-loop optoinhibition

**Brain regions**:
- Dorsal CA1 (dCA1)
- Basolateral amygdala (BLA)
- Entorhinal cortex (deep layers)
- Perirhinal cortex
- Ectorhinal cortex

**Keywords**: hippocampus–amygdala communication, sharp-wave ripples, memory consolidation, contextual fear conditioning, many-to-one weighted mapping, BLA cell assemblies, independent component analysis, GLM population decoding, closed-loop optogenetics, sleep-dependent consolidation, episodic memory indexing, dual-site electrophysiology
