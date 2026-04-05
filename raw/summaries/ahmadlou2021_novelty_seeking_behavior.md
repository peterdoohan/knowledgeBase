---
source_file: ahmadlou2021_novelty_seeking_behavior.md
title: A cell type–specific cortico-subcortical brain circuit for investigatory and novelty-seeking behavior
authors: Mehran Ahmadlou, Janou H. W. Houba, Jacqueline F. M. van Vierbergen, Maria Giannouli, Geoffrey-Alexander Gimenez, Christiaan van Weeghel, Maryam Darbanfouladi, Maryam Yasamin Shirazi, Julia Dziubek, Mejdy Kacem, Fred de Winter, J. Alexander Heimel
year: 2021
journal: Science
paper_type: empirical
contribution_type: empirical
---

### One-line summary

A GABAergic, TAC1-expressing subpopulation of zona incerta neurons (ZIm) receives excitatory input from prefrontal cortex and gates deep investigatory behavior through a projection to the periaqueductal gray, selectively amplifying novelty-seeking exploration without affecting locomotion or approach.

---

### Background & motivation

Investigatory and novelty-seeking behaviors are fundamental to survival, enabling animals to acquire information about novel stimuli such as objects, conspecifics, or prey. Despite extensive study of the behavioral and psychological dimensions of curiosity and novelty preference, the neural circuits that gate whether an animal engages in deep versus shallow investigation were poorly understood. Prior work had implicated the zona incerta (ZI) — a diencephalic GABAergic structure — in defensive behavior, feeding, predatory hunting, and fear memory, but its role in appetitive investigatory behavior was unexplored. This paper asks which cell types and circuits in ZI drive the transition from superficial sniffing to deep, committed investigation of novel stimuli.

---

### Methods

- **Subjects**: C57BL/6J mice and Cre-driver lines (GAD2-Cre, PV-Cre, SST-Cre, TAC1-Cre) of both sexes, 2–5 months old.
- **Behavioral paradigm**: Free-access double-choice (FADC) object investigation test and social interaction test; behaviors labeled frame-by-frame using JAABA software. A Hidden Markov Model (HMM) identified two latent investigatory states (shallow vs. deep), operationalised as sniff-without-bite vs. sniff-followed-by-bite for objects, and approach-investigation-without-grab vs. with-grab for social stimuli. A deep vs. shallow preference (DSP) index was derived as an arctangent ratio.
- **Optogenetics**: ChR2 activation (20 Hz, 465 nm) and stGtACR2 silencing of cell-type-specific ZIm populations (GAD2, TAC1, PV, SST) during behavior.
- **Chemogenetics**: hM4Di-mediated inhibition of ZIm somata or of axon terminals in downstream targets (PAG, MLR, PnO) via local CNO injection.
- **Fiber photometry**: GCaMP6s recordings from ZIm^GAD2 and PAG neurons during object and social investigation.
- **In vivo electrophysiology**: 16-channel laminar probe recordings from PAG, MLR, and PnO during optogenetic ZIm manipulation.
- **Anatomy**: Retrograde and monosynaptic rabies tracing; anterograde AAV tracing of PL→ZI and ZIm^TAC1→PAG projections; RNAscope multiplex in situ hybridization for TAC1, VGAT, PV, and SST co-expression in ZIm.
- **Arousal measurement**: Pupil dilation and whisker activity in head-fixed and freely moving mice during optogenetic manipulations.
- **Self-stimulation nose-poke test**: Optogenetic self-activation of ZIm^GAD2 as a measure of rewarding/motivational value.

---

### Key findings

- Mice display dramatically more deep investigation (sniff→bite→grab) of novel versus familiar objects (DSP: novel 0.51 ± 0.12 vs. familiar -0.45 ± 0.17 rad, p < 10⁻⁴); the only action whose transition probability differed between familiar and novel objects was sniff-to-bite.
- Photo-activation of ZIm^GAD2 neurons massively increased novel object investigation duration (novel tdTOM: 13.90 ± 3.42 s vs. novel ChR2: 55.56 ± 4.92 s, p < 10⁻⁶) and shifted the DSP toward deep investigation; photo-inhibition had the opposite effect.
- ZIm^GAD2 activity increased selectively during deep investigation events (GCaMP6s Z-score deep: 4.09 ± 0.49 vs. shallow: 0.80 ± 0.24, p < 10⁻⁷), and this signal was also seen during social investigation but not during food interaction.
- Photo-activation of ZIm^GAD2 neurons increased arousal (pupil dilation and whisker activity) and mice self-stimulated ZIm^GAD2 (106 ± 20 returns to opto-port vs. 673 ± 179 to non-opto, p < 0.05), suggesting the activation is rewarding/motivating.
- Prefrontal cortex (prelimbic, PL) sends excitatory projections to ZIm; chemogenetic silencing of PL→ZIm terminals abolished deep investigation (investigation duration CNO+tdTOM: 73.33 ± 23.13 s vs. CNO+hM4Di: 2.05 ± 0.50 s, p < 10⁻⁵).
- Among ZIm efferents, only the ZIm→PAG projection was required for deep investigation: silencing ZIm^GAD2→PAG terminals strongly reduced investigation duration and DSP; silencing ZIm→MLR or ZIm→PnO had no effect on investigation. ZIm activation inhibited PAG firing (off: 19.51 ± 3.31 Hz vs. on: 14.64 ± 2.21 Hz, p < 10⁻⁴), consistent with a disinhibitory gating mechanism.
- Among ZIm interneuron subtypes (GAD2, PV, SST, TAC1), only ZIm^TAC1 activation increased novel object investigation duration (TAC1: 58.68 ± 8.43 s vs. tdTOM: 13.90 ± 3.42 s, p < 10⁻⁵) and DSP; TAC1 cells constitute a distinct subpopulation non-overlapping with PV or SST cells in ZIm.
- ZIm^TAC1 neurons also activated arousal signals (pupil and whisker), and their projections to PAG and MLR were confirmed anatomically.

---

### Computational framework

Not applicable in a strict formal sense. The paper uses a Hidden Markov Model (HMM) to decompose observable investigatory behavior into latent states (idle, shallow investigation, deep investigation), deriving a DSP index as a compact behavioral readout. Conceptually, the paper proposes a gain-modulation and thresholding model: PL provides non-specific motivational drive to ZIm, which multiplies and thresholds this signal (gated by sensory context) before relaying deep investigation signals to PAG. The results constrain models of subcortical gating of goal-directed behavior and cortico-diencephalic control of arousal and curiosity.

---

### Prevailing model of the system under study

Prior to this paper, the zona incerta was understood as a GABAergic diencephalic structure with broad projections to cortex, thalamus, hypothalamus, and brainstem. It had been implicated in defensive behaviors, predatory hunting (ZI GABAergic neurons integrating sensory prey signals to drive appetitive pursuit), rapid binge eating (ZI GABA neuron activation), and fear memory modulation via CeA inputs. The prefrontal cortex (prelimbic area) was known to encode social and spatial information and project to subcortical structures, but its connection to ZI in the context of investigatory behavior was unknown. The PAG was established as a hub for defensive and escape behavior (via inhibitory inputs from ZI PV neurons), but its role downstream of an investigatory circuit had not been described. ZI was broadly seen as a multifunctional "zone of uncertainty" whose cell-type-specific functions were only beginning to be resolved.

---

### What this paper contributes

This paper identifies a previously unknown function for a specific ZI cell type — TAC1-expressing GABAergic neurons — in promoting deep, committed novelty investigation. It establishes a three-node cortico-subcortical circuit: PL (excitatory) → ZIm^GAD2/TAC1 (inhibitory) → PAG, where ZIm activity gates the transition from shallow to deep investigation by inhibiting PAG, thereby disinhibiting investigatory approach. This extends the known repertoire of ZI functions beyond defensive and consummatory behavior into the domain of novelty-seeking and curiosity. Critically, the paper dissociates deep investigation from general locomotion (inhibiting ZIm^GAD2 does not reduce open-field travel distance) and from approach (approach frequency is preserved; only deep engagement with objects is affected), suggesting the circuit specifically modulates the depth or commitment of investigation rather than general motivational arousal. The self-stimulation result implies that ZIm^GAD2 activation is intrinsically rewarding, linking the circuit to the affective value of curiosity.

---

### Brain regions & systems

- **Zona incerta, medial (ZIm)**: Core locus of the paper; GABAergic TAC1-expressing neurons here gate deep investigation; receives PL input and projects to PAG.
- **Prelimbic cortex (PL)**: Upstream excitatory driver of ZIm; PL→ZIm projection is required for deep investigation of both objects and conspecifics.
- **Periaqueductal gray (PAG)**: Downstream target of ZIm^GAD2/TAC1; ZIm activation inhibits PAG, and blocking ZIm→PAG terminals abolishes deep investigation; PAG activity is also elevated during deep investigation events (fiber photometry). PAG provides the output gate for investigation depth.
- **Mesencephalic locomotor region (MLR)**: Receives ZIm^TAC1 axons but silencing this projection does not affect investigation; likely involved in locomotion/arousal components.
- **Pedunculopontine/pontine reticular nucleus (PnO)**: Receives ZIm input; silencing ZIm→PnO does not affect investigation; role here is subordinate.
- **Zona incerta, rostral (ZIr)**: Tested and found not to drive novel object investigation (ZIr^GAD2 activation primarily drives food preference), distinguishing sub-regional ZI functions.

---

### Mechanistic insight

The bar is not fully met. The paper proposes a gain-modulation + thresholding algorithm (PL signal amplified by ZIm sensory context, thresholded before PAG output) and presents a conceptual model (Fig. S19), but does not formally specify this as an algorithm with defined input-output computations. The neural data (ZIm^GAD2 photometry elevated during deep investigation, PAG inhibited by ZIm activation, PAG photometry elevated during deep investigation) are consistent with a disinhibitory gating mechanism but do not uniquely discriminate between disinhibition and a purely modulatory gain change. The paper lacks simultaneous recordings from PL, ZIm, and PAG during investigation that would be necessary to test the algorithmic account with neural data.

---

### Limitations & open questions

- The file studied is the supplementary material; the main paper figures and textual narrative are not reproduced here, limiting access to some quantitative claims presented in the main text.
- The paper uses a non-overlapping 10-minute test protocol; 2-minute tests are used for photo-stimulation, and the authors note results are consistent when truncating, but the duration asymmetry is a minor confound.
- Sample sizes for chemogenetic experiments (especially social interaction: n = 3 per group) are small.
- The mechanism by which ZIm^TAC1 neurons integrate sensory novelty signals (and discriminate novel from familiar) is not resolved; inputs from thalamus and midbrain are hypothesized but not demonstrated.
- Whether the ZIm^TAC1 population directly inhibits PAG or does so via a ZIm^GAD2 → PAG intermediate is not fully resolved.
- It is unclear whether the PL excitatory signal to ZIm conveys novelty-specific information or non-specific motivational arousal.
- The relationship between ZIm-driven curiosity and dopaminergic reward signals is not investigated.
- Generalizability to other species or to human curiosity circuits is unaddressed.

---

### Connections & keywords

- **Key citations**: Zhao et al. 2019 (Nat. Neurosci.; ZI GABAergic neurons and hunting); Zhang & van den Pol 2017 (Science; ZI GABA and binge eating); Chou et al. 2018 (Nat. Commun.; ZI and defense behaviors); Zhou et al. 2018 (Nat. Neurosci.; CeA→ZI and fear memory); Tovote et al. 2016 (Nature; midbrain circuits for defensive behaviour); Murugan et al. 2017 (Cell; PFC social and spatial coding); Mitrofanis 2005 (Neuroscience; ZI function review); Ennaceur & Delacour 1988 (novel object recognition test).
- **Named models or frameworks**: Hidden Markov Model (HMM) of investigatory behavior states; deep vs. shallow preference (DSP) index; free-access double-choice (FADC) object investigation task; gain modulation + thresholding model (Fig. S19).
- **Brain regions**: zona incerta (medial, ZIm; rostral, ZIr), prelimbic cortex (PL), periaqueductal gray (PAG), mesencephalic locomotor region (MLR), pontine reticular nucleus (PnO).
- **Keywords**: zona incerta, novelty-seeking behavior, investigatory behavior, GABAergic neurons, TAC1 neurons, optogenetics, fiber photometry, cortico-subcortical circuit, prefrontal cortex, disinhibition, deep investigation, periaqueductal gray
