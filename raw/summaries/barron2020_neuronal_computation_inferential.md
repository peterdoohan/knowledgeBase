---
source_file: "barron2020_neuronal_computation_inferential.md"
paper_id: "barron2020_neuronal_computation_inferential"
title: "Neuronal Computation Underlying Inferential Reasoning in Humans and Mice"
authors: "Helen C. Barron, Hayley M. Reeve, Ren\u00e9e S. Koolschijn, Pavel V. Perestenko, Anna Shpektor, Hamed Nili, Roman Rothaermel, Natalia Campo-Urriza, Jill X. O'Reilly, David M. Bannerman, Timothy E.J. Behrens, David Dupret"
year: 2020
journal: "Cell"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse", "human"]
methods: ["optogenetics", "electrophysiology", "tetrode_recording", "fmri", "representational_similarity_analysis", "lesion", "behavioral_analysis"]
brain_regions: ["hippocampus", "hippocampus_ca1", "prefrontal_cortex", "medial_prefrontal_cortex", "retrosplenial_cortex", "visual_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl", "model_free_rl"]
keywords: ["neuronal", "computation", "underlying", "inferential", "reasoning", "humans", "mice"]
key_citations: ["daw2005_uncertainty_prefrontal_striatal"]
---

### One-line summary

Using a cross-species approach combining 7T fMRI in humans and in vivo electrophysiology plus optogenetics in mice, this study shows that the hippocampus supports inferential reasoning by computing a prospective code that forecasts temporally structured learned associations during choice, while during rest hippocampal sharp-wave/ripples increasingly co-represent inferred reward relationships never directly experienced together.

---

### Background & motivation

Adaptive behavior often requires drawing inferences about outcomes from events that were never directly paired — a capacity thought to depend on multiple brain regions including the hippocampus. However, the precise neuronal computation underlying such inferential decisions remained unknown: specifically, whether the hippocampus predicts unobserved associations on-the-fly during choice, consolidates cognitive short-cuts during rest/sleep, or both. Prior work using lesion studies and human fMRI had implicated the hippocampus, orbitofrontal cortex, medial prefrontal cortex, and perirhinal cortex, but had not resolved the cellular-level mechanism. This study fills that gap by integrating whole-brain imaging, cellular electrophysiology, and causal optogenetic manipulation within the same behavioral paradigm across two species.

---

### Methods

- **Task design**: Three-stage sensory preconditioning paradigm performed over multiple days in both humans and mice. Stage 1 (observational learning): auditory cue Xn paired with visual cue Yn. Stage 2 (conditioning): Yn paired with rewarding (set 1) or neutral (set 2) outcome Zn. Xn was never directly paired with Zn. Stage 3 (inference test): Xn presented alone; reward-seeking behavior measured as index of inference.
- **Human recordings**: 7T fMRI (BOLD) in 22 healthy volunteers during conditioning and inference test; near-whole-brain coverage; univariate GLM and representational similarity analysis (RSA) applied.
- **Mouse recordings**: In vivo multichannel tetrode electrophysiology in dorsal CA1 (dCA1) of 24 mice during task and rest/sleep; spike sorting; GLM-based cue-selective ensemble identification.
- **Optogenetics**: Bilateral dCA1 pyramidal cell silencing (ArchT-GFP) during auditory cues Xn or visual cues Yn to test causal necessity.
- **RSA**: Applied identically across species to compare hippocampal activity patterns during Xn (inference test) with patterns during Yn (conditioning), testing for prospective representation of associated Yn.
- **SWR analysis**: Probability of co-firing of Xn, Yn, Zn cell triplets (and Xn–Zn doublets) during awake sharp-wave/ripples compared across early versus late recording days; inter-spike interval analysis for temporal order of firing.

---

### Key findings

- Both humans and mice showed significant reward-seeking bias for auditory cues Xn (set 1 > set 2) in the inference test despite never directly experiencing Xn with reward (humans p < 0.001; mice p = 0.005).
- Human 7T fMRI revealed significantly greater right hippocampal BOLD signal on correct versus incorrect inference trials (t21 = 4.15, p = 0.022).
- Optogenetic silencing of dCA1 pyramidal cells during Xn presentation impaired inference in ArchT-GFP mice (laser off p < 0.001; laser on p = 0.794; interaction p = 0.029) but had no effect on first-order conditioning or visual discrimination.
- RSA in both species demonstrated that during correct inference, hippocampal activity during Xn showed significantly higher representational similarity with the associated Yn than with non-associated Ym cues (humans: Z21 = 2.24, p = 0.013; mice: Z17 = 3.00, p = 0.001); this pattern was absent on incorrect inference trials.
- In mice, within-set Xn–Yn neuron pairs showed sequential spiking during inference (Yn fired after Xn, p < 0.001), preserving the learned temporal order from observational learning; cross-set pairs showed no such bias.
- Hippocampal activity during Xn did not represent the inferred outcome Zn in either species; inferred outcome Zn was instead represented in mPFC and putative dopaminergic midbrain (mPFC: t21 = 5.09, p = 0.003; midbrain: t21 = 5.56, p < 0.001), even for neutral cues.
- From early to late training days, awake SWRs in mice showed a significant increase in co-representation of set 1 triplets (X1Y1Z1, p < 0.001) but not set 2 triplets; the increase in X1–Z1 co-firing during SWRs occurred over and above any change in activity for single cells.
- During awake SWRs, cells representing Z1 fired significantly earlier than X1 cells (reverse order; p < 0.001), analogous to reward-related reverse replay in spatial tasks; no such bias was observed for set 2 pairs.

---

### Computational framework

The paper uses a **model-based reinforcement learning / prospective memory** framework, framed in terms of cognitive map theory and Tolmanian relational memory.

**Core formalism**: The brain is conceived as maintaining an internal model of sensory transitions (Xn → Yn → Zn). At the time of inferential choice, the hippocampus implements an online, mnemonic chain: in response to Xn, it prospectively retrieves the associated Yn via learned temporal sequence statistics, and this hippocampal output is then propagated to mPFC and midbrain where the inferred outcome Zn is represented. This is explicitly contrasted with model-free (cached-value) accounts in which Xn would directly acquire the value of Zn during encoding.

A complementary mechanism operates offline: during sharp-wave/ripples at rest, hippocampal ensembles co-activate neurons representing Xn and Zn (never directly experienced together), building mnemonic short-cuts via content that goes beyond replay of direct experience. Reverse-order firing during reward-related SWRs is interpreted as supporting retrospective credit assignment, consistent with temporal-difference learning proposals (Sutton, 1988).

Key variables: representational similarity between activity patterns during Xn and Yn (prospective code); probability of co-activation of Xn–Zn cell pairs in SWRs; temporal ordering of spikes within SWRs.

---

### Prevailing model of the system under study

The prevailing view, as laid out in the paper's introduction, held that the hippocampus supports inference through one or both of two broad mechanisms: (1) a model-based, on-the-fly chaining of mnemonic associations at the time of choice, searching through a learned world model to predict outcomes; or (2) integrative encoding during learning, whereby overlapping events come to share neural representations and Xn can directly acquire value from Zn via hippocampal recurrent loops (e.g., Kumaran, 2012; Wimmer and Shohamy, 2012). Additionally, anatomical evidence from lesion studies and human fMRI had implicated a network including hippocampus, orbitofrontal cortex, mPFC, perirhinal cortex, and retrosplenial cortex, but the specific computational role of each region — and especially the cellular-level hippocampal mechanism — was unresolved. The hippocampus was broadly attributed a role in holding a "cognitive map" (O'Keefe and Nadel, 1978) and in memory for sequential events, but how this translated into inferential reasoning beyond directly experienced associations was unclear.

---

### What this paper contributes

This study makes three concrete advances over the prevailing model:

1. **Dissociation of prospective and outcome representations**: By using a many-to-one cue mapping in humans, the paper demonstrates that during inference the hippocampus represents the intermediary cue Yn (prospective code), not the inferred outcome Zn or the value of Yn. This rules out the integrative-encoding account (Wimmer and Shohamy, 2012) and the recurrent medial temporal lobe account (Kumaran, 2012) as the primary on-the-fly mechanism. The inferred outcome is instead computed in downstream mPFC and midbrain.

2. **Temporal-sequence preservation**: The prospective code is not merely set-selective but preserves the learned temporal order of Xn → Yn spiking, providing a cellular description of how mnemonic chains are reconstructed on-the-fly.

3. **SWR-based cognitive short-cuts**: During rest, hippocampal SWRs progressively co-represent reward-related inferred relationships (Xn–Zn) that were never experienced together, and do so in reverse temporal order. This extends the concept of hippocampal replay beyond direct experience to the construction of higher-order relational knowledge — a cellular mechanism for "joining-the-dots" that can explain why sleep facilitates inferential reasoning in humans.

Together, the results support a two-process hippocampal account: online prospective chaining during choice, and offline short-cut construction during rest.

---

### Brain regions & systems

- **Dorsal hippocampal CA1 (dCA1)** — primary locus of the prospective code; necessary for inference (causal, optogenetics); site of SWR-nested inferred relationship representations during rest. In both humans (right hippocampus, BOLD) and mice (pyramidal cell ensembles, electrophysiology).
- **Medial prefrontal cortex (mPFC)** — represents the inferred outcome Zn during correct inference (human fMRI searchlight RSA); proposed to use hippocampal output to form abstract, model-based outcome predictions.
- **Putative dopaminergic midbrain** — also represents inferred outcome Zn during correct inference (human fMRI); discussed in relation to model-based dopamine prediction error signals that extend beyond direct reinforcement.
- **Auditory cortex** — shows elevated BOLD across all inference test trials; used as seed region for psychophysiological interaction analysis revealing hippocampal co-activation during correct inference.
- **Retrosplenial cortex, visual cortex** — co-activate with auditory cortex during correct inference (human PPI), consistent with roles in sensory memory processing.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight.

**The phenomenon**: Inferential reasoning — making correct decisions about outcomes never directly experienced — in both humans and mice.

**Marr's three levels**:

- **Computational**: The problem the brain is solving is how to predict the outcome of a novel choice by chaining together discrete memories (Xn → Yn → Zn). The solution involves two complementary processes: (1) online forward prediction during choice, and (2) offline construction of direct cognitive short-cuts during rest that can reduce future computational cost.

- **Algorithmic**: During inference, dCA1 pyramidal cells implement a prospective retrieval process: in response to Xn, the ensemble activates neurons representing Yn in the same temporal sequence (Xn → Yn) as experienced during observational learning. This set-selective, temporally structured activation is captured via RSA and spike-time cross-correlograms. The hippocampus does not complete the chain to Zn; instead, its output is used by mPFC and midbrain to represent the inferred outcome. During rest, SWR-nested coactivation of Xn and Zn ensembles builds a direct associative code, with Z1 firing before X1 (reverse order) consistent with credit-assignment mechanisms.

- **Implementational**: dCA1 pyramidal cells (CaMKII-positive) are the causal substrate: ArchT-GFP optogenetic silencing of these cells specifically during Xn presentation abolishes inference without affecting first-order conditioning. The SWR mechanism is localised to dCA1 local field potentials and co-firing of anatomically and functionally defined cell ensembles. The study does not specify interneuron subtypes, synaptic mechanisms, or the precise circuit by which dCA1 output reaches mPFC and midbrain, leaving implementation at an ensemble/region level.

**Bonus**: The viral strategy (CaMKII-Cre mice, rAAV2-CamKII-ArchT-GFP) provides cell-type specificity to pyramidal cells, and the authors discuss the intrinsic hippocampal connectivity (Somogyi and Klausberger, 2017) as relevant to understanding SWR content generation, though detailed circuit mechanisms are not resolved.

---

### Limitations & open questions

- The multi-day paradigm (task stages on separate days) means that results may reflect effects of memory consolidation; the inference mechanism might differ with single-session learning, where hippocampus and mPFC may both represent inferred outcomes.
- The study cannot resolve the precise circuit by which hippocampal prospective output (Yn representation) is translated into Zn representation in mPFC and midbrain — multi-site recordings in animal models are identified as a required next step.
- The role of the intermediary Y-cue representation in mPFC and midbrain is not directly assessed; whether those regions independently chain Xn → Yn → Zn or receive Yn representations from hippocampus is not established.
- Comparable SWR analyses were not performed in humans (invasive method required), leaving a gap in the cross-species comparison for the offline mechanism.
- Sleep SWR effects were observed but weaker than awake SWR effects, consistent with other replay studies, but the functional significance of this difference is not resolved.
- All mice were male; sex differences in inference or hippocampal SWR content are not addressed.
- The computational cost reduction from SWR-built short-cuts is theoretically motivated but not formally quantified or tested behaviourally.

---

### Connections & keywords

**Key citations**:
- Bunsey and Eichenbaum, 1996 (hippocampal lesions and transitive inference)
- Preston et al., 2004 (hippocampal contribution to novel relational memory)
- Wimmer and Shohamy, 2012 (hippocampal-mediated preference by association)
- Kumaran, 2012; Kumaran and McClelland, 2012 (recurrent medial temporal lobe models of inference)
- Kriegeskorte et al., 2008 (representational similarity analysis)
- Buzsáki, 2015 (hippocampal sharp-wave/ripples review)
- Daw et al., 2005 (model-based vs model-free reinforcement learning)
- Tolman, 1948 (cognitive maps)
- O'Keefe and Nadel, 1978 (hippocampus as cognitive map)
- Foster and Wilson, 2006; Diba and Buzsáki, 2007 (reverse replay)
- Singer and Frank, 2009 (reward-biased SWR replay)
- Hampton et al., 2006 (mPFC in abstract state-based inference)
- Sadacca et al., 2016 (midbrain dopamine neurons and inferred value)

**Named models or frameworks**:
- Sensory preconditioning paradigm (Brogden, 1939)
- Representational similarity analysis (RSA)
- Model-based reinforcement learning (Daw et al., 2005)
- Cognitive map theory (Tolman, 1948; O'Keefe and Nadel, 1978)
- DABEST (bootstrap-coupled estimation; Ho et al., 2019)
- ArchT-GFP optogenetic silencing

**Brain regions**:
- Dorsal hippocampal CA1 (dCA1)
- Medial prefrontal cortex (mPFC)
- Putative dopaminergic midbrain
- Auditory cortex
- Retrosplenial cortex
- Visual cortex

**Keywords**: inferential reasoning, hippocampal prospective code, sharp-wave ripples, sensory preconditioning, representational similarity analysis, model-based reinforcement learning, cognitive map, memory replay, optogenetics, cross-species approach, mnemonic short-cut, reverse replay
