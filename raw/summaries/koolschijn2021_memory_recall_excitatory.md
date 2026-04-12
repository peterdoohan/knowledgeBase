---
source_file: "koolschijn2021_memory_recall_excitatory.md"
paper_id: "koolschijn2021_memory_recall_excitatory"
title: "Memory recall involves a transient break in excitatory-inhibitory balance"
authors: "Ren\u00e9e S Koolschijn, Anna Shpektor, William T Clarke, I Betina Ip, David Dupret, Uzay E Emir, Helen C Barron"
year: 2021
journal: "eLife"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
methods: ["fmri", "behavioral_analysis"]
brain_regions: ["hippocampus", "entorhinal_cortex", "visual_cortex"]
keywords: ["memory", "recall", "involves", "transient", "break", "excitatory", "inhibitory", "balance"]
key_citations: ["barron2020_neuronal_computation_inferential"]
---

### One-line summary

During hippocampal-dependent associative memory recall, the ratio of glutamate to GABA in primary visual cortex transiently increases — and this shift is predicted by hippocampal BOLD activity — suggesting the hippocampus gates neocortical memory reinstatement via a disinhibitory mechanism.

---

### Background & motivation

Memories are thought to be stored across distributed neocortical circuits and held dormant by excitatory-inhibitory (EI) balance, which prevents interference from new learning. The hippocampus is believed to act as a "memory index," reinstating cortical representations during recall. However, the precise mechanism by which hippocampal activity coordinates neocortical reinstatement — and specifically whether recall requires a transient perturbation of neocortical EI balance — was unknown. This paper tests whether memory recall is accompanied by measurable breaks in neocortical EI balance that are mediated by hippocampal activity.

---

### Methods

- **Task design**: Three-stage inference task performed over 3 days in virtual reality (VR). Day 1: auditory-visual associative learning (up to 80 pairs). Day 2: visual-outcome conditioning (reward vs. neutral). Day 3 (in scanner): inference test — auditory cues presented alone; participants inferred the associated outcome by recalling the intermediary visual cue.
- **Subject population**: 22 healthy adult volunteers (mean age 22.8 years); final analyses used n=18–19 depending on measure.
- **Imaging**: 7T MRI with a novel interleaved fMRI-fMRS sequence (TR = 4.105 s). fMRI: 3D EPI covering occipital and temporal lobes. fMRS: semi-LASER spectroscopy (TE = 36 ms) with a 2×2×2 cm³ voxel in primary visual cortex (V1).
- **Trial categorisation**: "Remembered" = correct inference test response AND correct post-scan associative recall; "Forgotten" = incorrect on either measure. This conservative approach controls for false positives given inference-test chance = 50%.
- **fMRS analysis**: LCModel quantification of glutamate and GABA (normalised to total creatine, tCr) in an event-related manner, with GABA estimates unconstrained (NRATIO=0) to preserve dynamic range. glu/GABA ratio = (Glu_remembered/GABA_remembered) / (Glu_forgotten/GABA_forgotten). Permutation testing and Monte Carlo simulations used to validate results.
- **fMRI analysis**: SPM12 GLM; "remembered" vs. "forgotten" contrast; hippocampal ROI used to test whether BOLD signal predicted V1 glu/GABA ratio across participants (Spearman correlation). Whole-brain FWE-corrected at p < 0.05.

---

### Key findings

- Participants successfully inferred rewarded and neutral outcomes from auditory cues, and inference performance was predicted by post-scan associative recall performance (r₁₇ = 0.57, p = 0.010).
- BOLD signal was significantly higher for "remembered" versus "forgotten" trials in both visual cortex (t₁₇ = 5.92, p < 0.001) and hippocampus (t₁₇ = 4.33, p = 0.017), replicating prior work with the same task.
- glu/GABA ratio in V1 was significantly elevated during the recall (question) period of "remembered" versus "forgotten" trials (t₁₇ = 2.21, p = 0.041). Permutation testing confirmed: GABA decreased significantly (p = 0.014) and glu/GABA ratio increased (p = 0.007). Bootstrap estimation gave p = 0.017 (95% CI non-overlapping zero).
- The increase in glu/GABA ratio was temporally specific: not present during the preceding tone period or the ITI.
- No change in glu/GABA ratio was observed during conditioning trials, which are not hippocampal-dependent.
- Across participants, hippocampal BOLD signal for "remembered" vs. "forgotten" trials negatively predicted GABA in V1 (r₁₅ = −0.56, p = 0.022) and positively predicted glu/GABA ratio (r₁₅ = 0.52, p = 0.033). Glutamate alone was not significantly predicted (r₁₅ = 0.14, p = 0.585).
- Whole-brain FWE-corrected analysis confirmed the hippocampus was the only brain region where BOLD selectively predicted V1 glu/GABA ratio (left hippocampus: t₁₆ = 11.37, p = 0.005).

---

### Computational framework

The paper does not propose or fit a formal computational model. Instead, it uses a **disinhibitory circuit framework** informed by EI balance theory and prior animal work. The core idea is:

- Memories are held dormant in neocortex by tonic inhibition (EI balance at set point).
- Recall requires a transient perturbation of this balance — a "break" in EI — to release representations from inhibitory control.
- The hippocampus acts as the controller of this perturbation, potentially targeting VIP+ interneurons or analogous disinhibitory circuit motifs, thereby releasing excitatory principal cells from inhibitory suppression.

The framework is grounded in the **hippocampal indexing theory** (Teyler & DiScenna 1985; Teyler & Rudy 2007): the hippocampus stores a sparse index of distributed cortical representations and reinstates them by broadcasting to neocortex. The novel addition is specifying the neocortical mechanism as disinhibition, indexed by glu/GABA ratio measured via fMRS.

MRS measures are interpreted as proxies for metabolic coupling to neurotransmission: a ~1:1 relationship between glutamine-glutamate cycling rate and neuronal oxidative glucose consumption is assumed, making MRS-derived glu/GABA an indirect but physiologically grounded marker of EI balance.

---

### Prevailing model of the system under study

Prior to this paper, the field held that:

1. Memories are stored as sparse distributed representations in neocortex (Buzsáki 2010; Josselyn & Tonegawa 2020) and are held in a silent, dormant state by EI balance — tight coupling between excitatory and inhibitory synaptic conductances that prevents spontaneous reactivation and protects memories from interference (Barron et al. 2016; Froemke et al. 2007; Vallentin et al. 2016; Vogels et al. 2011).
2. The hippocampus provides a memory index that coordinates neocortical reinstatement during recall (Teyler & DiScenna 1985; Teyler & Rudy 2007), consistent with evidence that hippocampal reinstatement precedes or predicts neocortical reinstatement (Pacheco Estefan et al. 2019; Tanaka et al. 2014).
3. The *mechanism* linking hippocampal output to neocortical reactivation was unknown. It was unclear whether hippocampal projections acted via direct excitation of neocortical principal cells, modulation of local inhibition, or some other route.

---

### What this paper contributes

This paper provides the first direct human neurochemical evidence that associative memory recall involves a transient reduction in neocortical GABAergic inhibition, resulting in a shift in the local glu/GABA balance toward excitation. Key advances:

- **Specifies the neocortical mechanism**: Recall is not simply an increase in excitatory drive but a decrease in inhibition (GABA decrease is the driving factor), consistent with disinhibition.
- **Links hippocampal activity to the neocortical EI shift**: The selectivity of the hippocampal BOLD-to-V1 glu/GABA correlation (surviving whole-brain correction; unique to recall period; absent in control ROIs) positions hippocampal output as the gate for this neocortical disinhibition.
- **Cross-species relevance**: The VR inference task was designed to be deployable in rodents (Barron et al. 2020), so future animal studies can directly test whether hippocampal projections target VIP+ or similar disinhibitory interneurons during recall.
- **Methodological contribution**: Demonstrates that event-related fMRS at 7T can resolve within-subject, condition-specific, transient changes in GABA on a ~3 s timescale — extending the utility of fMRS beyond static block-design measures.

---

### Brain regions & systems

- **Hippocampus** — proposed source of the disinhibitory index signal; BOLD activity during recall predicts V1 glu/GABA ratio; left hippocampus survived whole-brain FWE correction as the unique predictor of neocortical EI shift.
- **Primary visual cortex (V1)** — site of fMRS measurement and location of recalled visual cue representations; shows elevated BOLD and elevated glu/GABA ratio during successful recall.
- **Entorhinal cortex / relay regions** — mentioned as anatomical intermediary between sensory cortex and hippocampus; not directly measured.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Phenomenon**: Associative memory recall requires the release of a visual cortical representation from inhibitory control, mediated by hippocampal output.

**Computational level**: The brain must selectively reactivate one of many stored, dormant neocortical representations in response to an associated cue — a pattern-completion problem. Maintaining all other representations dormant requires holding EI balance; selectively reinstating one requires a targeted, transient EI perturbation.

**Algorithmic level**: The algorithm appears to be: hippocampal index signal → preferential targeting of disinhibitory interneurons in visual cortex → reduced GABAergic tone on principal cells → transient release of the stored visual representation into an active state. Evidence: (i) glu/GABA ratio increases in V1 specifically during recall (not tone or ITI); (ii) increase is driven primarily by GABA decrease; (iii) hippocampal BOLD selectively predicts the glu/GABA shift.

**Implementational level**: Not directly resolved in this paper — fMRS measures metabolic pools at coarse spatiotemporal scale and cannot identify specific cell types. The authors draw on rodent literature (Zhang et al. 2014; Krabbe et al. 2019; Lee et al. 2013) for the hypothesis that hippocampal glutamatergic projections target VIP+ interneurons (which disinhibit principal cells by suppressing parvalbumin/somatostatin interneurons), but this specific mechanism is not demonstrated in this study. The paper explicitly notes this as a limitation and calls for future animal work using the cross-species VR task.

**Bonus**: The authors note that rapid (~millisecond) synaptic dynamics are not captured by fMRS, and that MRS-derived GABA primarily reflects intracellular metabolic pools rather than extracellular neurotransmitter. The implementational claim is therefore inferred rather than directly demonstrated.

---

### Limitations & open questions

- **fMRS temporal and spatial resolution**: MRS measures metabolic pools at a coarse scale (2×2×2 cm³ voxel, TR ~4 s) and cannot resolve rapid synaptic dynamics, specific interneuron subtypes, or laminar organisation. Relationship between MRS-derived GABA and physiological EI balance is indirect.
- **GABA measurement without spectral editing**: Non-edited sequence at 7T is used; GABA peaks overlap with glutamate and NAA. Authors validate with Monte Carlo simulations and show no NAA confound, but edited sequences would provide cleaner GABA estimates.
- **Unconstrained GABA estimates**: Disabling LCModel's default GABA priors improves dynamic range but yields absolute GABA values higher than standard estimates; cross-study comparisons are complicated.
- **fMRS voxel restricted to V1**: The choice of ROI was hypothesis-driven (visual cue recall) but other neocortical regions storing the memory traces were not measured.
- **Directionality not established**: The fMRI-fMRS correlation is across subjects, not trial-by-trial within subjects, so the temporal order of hippocampal BOLD change and V1 EI shift cannot be fully resolved.
- **Circuit identity unknown**: Whether hippocampal projections directly target disinhibitory interneurons in human neocortex, as in rodents, remains to be demonstrated. The pathway from hippocampus to V1 is also anatomically indirect.
- **Clinical relevance**: EI disturbances in schizophrenia, autism, epilepsy, and Tourette's syndrome are mentioned as downstream targets for investigation, but no clinical data are presented.
- **Open question**: Can this fMRS-fMRI approach detect hippocampally-mediated EI changes in other neocortical regions (e.g., auditory or association cortex), and is the mechanism generalised beyond visual memory?

---

### Connections & keywords

**Key citations**:
- Teyler & DiScenna 1985; Teyler & Rudy 2007 — hippocampal indexing theory
- Barron et al. 2016 (Neuron) — dormant cortical memories, EI balance, MRS
- Barron et al. 2020 (Cell) — same inference task in humans and mice; hippocampal dependence
- Koolschijn et al. 2019 (Neuron) — hippocampal/neocortical inhibitory engrams protect against interference
- Ip et al. 2017; Ip et al. 2019 — combined fMRI-fMRS sequence development
- Vogels et al. 2011; Froemke et al. 2007; Vallentin et al. 2016 — EI balance and memory storage
- Zhang et al. 2014 — VIP+ disinhibitory circuit in V1 for attentional modulation
- Krabbe et al. 2019 — VIP interneurons and associative learning
- Pacheco Estefan et al. 2019 — hippocampal reinstatement predicts neocortical reinstatement

**Named models or frameworks**:
- Hippocampal indexing theory
- EI balance / excitatory-inhibitory balance
- Disinhibitory circuit motif (VIP interneuron pathway)
- fMRS (functional magnetic resonance spectroscopy)
- LCModel (spectral fitting)
- Three-stage VR inference task

**Brain regions**:
- Hippocampus
- Primary visual cortex (V1)

**Keywords**:
- excitatory-inhibitory balance
- hippocampal indexing
- associative memory recall
- functional magnetic resonance spectroscopy (fMRS)
- glutamate / GABA ratio
- disinhibition
- neocortical memory reinstatement
- 7T MRI
- virtual reality inference task
- semi-LASER spectroscopy
- hippocampal-neocortical coordination
- transient EI perturbation
