---
source_file: heindorf2018_motor_cortex_perturbation.md
title: Mouse Motor Cortex Coordinates the Behavioral Response to Unpredicted Sensory Feedback
authors: Matthias Heindorf, Silvia Arber, Georg B. Keller
year: 2018
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Motor cortex (M1) is necessary for corrective responses to unexpected visual perturbations but not for executing the same movements spontaneously, with layer 2/3 signalling perturbation occurrence independently of response magnitude while layer 5 pyramidal tract (PT) neurons encode the magnitude of the resulting corrective turn.

---

### Background & motivation

The role of motor cortex in movement control is contested: M1 lesions produce severe deficits in primates but surprisingly little overt impairment in rodents during unconstrained locomotion, suggesting that cortical control may be selectively engaged rather than universally required. A compelling hypothesis is that M1 becomes critical when movement must be guided by cortically processed sensory feedback — particularly when sensory input deviates from predictions. This paper addresses that gap by examining whether M1 is specifically required for responding to unexpected visual perturbations, and by recording layer-specific neural activity to understand the underlying cortical computations.

---

### Methods

- **Task**: Head-fixed mice navigated a virtual corridor on a spherical treadmill, learning to make corrective turns to reach a water reward. Sudden 30-degree visual offset perturbations ("induced turns") were introduced from training day 3 onward, requiring rapid corrective responses; mice also executed unsolicited "spontaneous turns".
- **Optogenetic inactivation**: Bilateral M1 inhibition via channelrhodopsin-2 in vGAT+ interneurons (vGAT::ChR2 mice) during either chronic training (n = 12 mice) or brief (3 s) windows concurrent with perturbations in expert mice (n = 14–15 mice). Ibotenic acid lesions in a separate cohort (n = 5) confirmed optogenetic results.
- **Calcium imaging**: Two-photon imaging of GCaMP6f in layer 2/3 excitatory neurons (AAV2/1-EF1a-GCaMP6f; 1,154 neurons, 8 mice) and layer 5 PT neurons (Sim1-Cre intersectional strategy; 560 neurons, 11 mice), plus supplementary recordings from layer 5 IT neurons (Tlx3-Cre, 9 mice).
- **Analysis**: Neural responses were split by turn direction (contra- vs. ipsiversive), turn acceleration magnitude, and training epoch (early vs. late days). Population vector correlation analyses and subspace projections tracked co-activation of ipsi- and contraversive ensembles.

---

### Key findings

- M1 inhibition during training blocked task learning (performance remained at chance: p = 0.17 vs. p < 10⁻⁶ for controls); inhibition in expert mice significantly reduced performance.
- M1 inhibition did not impair spontaneous turning speed or frequency (p = 0.07), confirming that M1 is not required for the motor act itself.
- M1 inhibition reduced the probability of a corrective turn in response to visual offset perturbations from ~74% to ~45%, and nearly abolished responses during chronic inhibition (28% vs. 74%); delayed turns resumed immediately after inhibition ceased.
- Layer 2/3 activity scaled linearly with spontaneous turn acceleration (R² = 0.08, p < 10⁻¹⁰) but was **independent** of induced turn magnitude (no linear trend, p = 0.86); it responded to the perturbation regardless of whether the mouse subsequently turned.
- Layer 5 PT activity scaled linearly with both spontaneous (R² = 0.04, p < 10⁻¹⁰) and **induced** turn acceleration (linear trend p < 10⁻⁷), tracking behavioral response magnitude.
- With learning: layer 2/3 responses to contraversive turns **decreased** (became bilateral), while layer 5 PT responses to contraversive turns **increased** and stabilised (time constant ~13.6 days vs. ~3.3 days for L2/3).
- During induced turns, layer 2/3 showed transient **co-activation of both contra- and ipsiversive turn neurons** (population vectors positively correlated for ~666 ms), irrespective of perturbation direction; layer 5 PT showed no such co-activation.
- Layer 5 IT neurons were intermediate between L2/3 and L5 PT in both learning-related changes and perturbation response, consistent with a L2/3 → L5 IT → L5 PT processing hierarchy.
- Activity during spontaneous turns was higher when turns were directed toward the target vs. away, suggesting M1 engagement scales with visual guidance demands.

---

### Computational framework

**Predictive processing / sensorimotor mismatch detection.** The paper does not formalise a quantitative model, but interprets findings through the lens of predictive processing: M1 layer 2/3 neurons signal a deviation between actual and expected sensory feedback (analogous to prediction-error signals proposed for visual cortex), which then updates an internal motor state representation encoded in layer 5 PT neurons. In this framing:

- Layer 2/3 computes or receives a mismatch signal (sensory perturbation independent of the specific motor response).
- Layer 5 PT encodes the selected motor output and its magnitude, downstream of response selection.

An alternative (not mutually exclusive) interpretation is also discussed: layer 2/3 co-activates multiple competing motor plan ensembles simultaneously, with one selected for output by layer 5 PT via local cortical competition — consistent with the idea of parallel motor plan preparation followed by selection (analogous to "preparing not to move" or parallel action planning in primate motor cortex).

---

### Prevailing model of the system under study

The introduction frames a well-established tension: M1 stimulation reliably evokes movement (via direct corticospinal projections), M1 neurons correlate with movement parameters (speed, direction, muscle activity, dynamics), and M1 lesions cause severe deficits in primates. Yet in rodents, M1 lesions leave basic locomotion largely intact (Kawai et al., 2015). The prevailing working model was therefore that M1's role is most prominent for dexterous fine-movement control or during learning, and may be dispensable once movement is automated. A subsidiary hypothesis gaining traction at the time of publication — grounded in work on visual cortex as a mismatch detector (Attinger et al., 2017; Fiser et al., 2016; Zmarz and Keller, 2016) and on motor cortex responses to unexpected perturbations in cats (Marple-Horvat et al., 1993) and rodents (Lopes et al., 2016) — was that M1 is specifically engaged when movement requires cortical sensory feedback processing.

---

### What this paper contributes

The results sharpen and empirically ground the hypothesis that M1 is not a general movement executor but a sensory-feedback-gated motor coordinator. Key advances:

1. **Causal dissociation**: M1 inactivation disrupts visually guided corrective turns but leaves spontaneous turning intact, providing a within-animal, within-task causal double dissociation not previously demonstrated cleanly in mice.
2. **Layer-specific functional roles**: The paper provides direct evidence that L2/3 and L5 PT have distinct computational signatures within the same task. L2/3 signals perturbation occurrence (a sensory/mismatch event) while L5 PT signals the motor response magnitude — a division consistent with predictive processing hierarchies.
3. **Co-activation of competing motor plans**: The observation of symmetric co-activation of ipsi- and contraversive ensembles in L2/3 following a perturbation (but not in L5 PT) provides a mechanistic handle on how the cortex might prepare multiple action options before committing to one.
4. **Learning dynamics**: The opposing direction of learning-related changes in L2/3 (decreasing, bilateralizing) vs. L5 PT (increasing, lateralizing, stabilizing) offers a framework for understanding how motor skill consolidation shifts computational load across cortical layers.

---

### Brain regions & systems

- **Primary motor cortex (M1) / caudal forelimb area (CFA)** — core locus of study; necessary for visually guided corrective turns and task learning; target of optogenetic inactivation and two-photon calcium imaging.
- **Layer 2/3 of M1** — signals sensory perturbation independently of motor response magnitude; shows co-activation of competing motor plans; decreases in directional selectivity with learning.
- **Layer 5 pyramidal tract (PT) neurons of M1** — encodes behavioral response magnitude; maintains directional selectivity; increases and stabilises with learning; projects to subcortical motor centres.
- **Layer 5 intratelencephalic (IT) neurons of M1** — intermediate response properties between L2/3 and L5 PT; consistent with hierarchical L2/3 → L5 IT → L5 PT processing.
- **Spinal cord / subcortical motor circuits** — proposed downstream targets of L5 PT output; sufficient for basic locomotion without cortical input.
- **Visual cortex** — implicitly referenced as a provider of visuomotor mismatch signals to M1 (via parietal cortex); not directly recorded.

---

### Mechanistic insight

The paper meets both criteria for a mechanistic insight entry.

**Phenomenon**: Motor cortex mediates corrective motor responses to unexpected visual perturbations, with layer-specific computation — layer 2/3 detecting the perturbation and layer 5 PT encoding the corrective response.

- **Computational level**: The brain must detect deviations between intended and actual sensory state and translate them into appropriate corrective motor commands with the correct magnitude and direction. During unexpected perturbations, multiple corrective options must be rapidly prepared before one is selected.

- **Algorithmic level**: L2/3 neurons implement (or receive) a perturbation-detection signal: they respond to the visual offset independent of subsequent turning direction or amplitude, and transiently co-activate both the contraversive and ipsiversive turn ensembles (~666 ms). This co-activation is consistent with parallel preparation of competing motor plans. L5 PT then encodes the selected plan with a magnitude that scales linearly with turn acceleration, representing a committed motor output. The L2/3 → L5 IT → L5 PT hierarchy is consistent with sequential selection: early co-activation in L2/3, intermediate co-activation evidence in L5 IT, and resolved directional commitment in L5 PT.

- **Implementational level**: The paper provides direct imaging data from genetically defined cell types (L2/3 excitatory neurons via vGAT-Cre exclusion; L5 PT via Sim1-Cre; L5 IT via Tlx3-Cre) using two-photon calcium imaging of GCaMP6f, tied to causal inactivation with optogenetics. The known unidirectional connectivity from L2/3 → L5 IT → L5 PT (cited anatomy: Anderson et al., 2010; Kiritani et al., 2012; Weiler et al., 2008) provides the implementational substrate for the sequential selection process.

**Bonus**: The paper identifies specific projection neuron subtypes (PT vs. IT), uses intersectional viral strategies for cell-type specificity, and grounds the layer-specific dynamics in known anatomical microcircuit connectivity. However, it does not address neuromodulatory mechanisms or synaptic-level biophysics.

---

### Limitations & open questions

- **Calcium imaging is not spike-resolved**: GCaMP6f signals are biased towards bursting activity and may differ in signal fidelity between cell types, limiting direct quantitative comparison of response magnitudes across L2/3 and L5 PT.
- **Spontaneous turns are not cleanly classified**: It is not possible to determine on a trial-by-trial basis whether a spontaneous turn was visually guided or not; the authors use target-direction as a proxy, which is imperfect.
- **Causal role of L2/3 co-activation not tested**: The co-activation of ipsi- and contraversive ensembles in L2/3 is observed, but whether disrupting it (e.g., by selectively silencing one ensemble) changes the subsequent L5 PT response or the corrective behavior is not tested.
- **Species generalisability**: Findings are in mice; the far greater dependence of primates on M1 for movement suggests quantitative if not qualitative differences that are not addressed.
- **Learning-related changes: cause vs. consequence**: The authors acknowledge that changes in M1 activity with training could reflect altered behavioral strategy (smaller errors as performance improves) rather than representing a causal mechanism of skill consolidation.
- **Downstream pathways**: How L5 PT activity translates into the brainstem/spinal circuits that execute the corrective turn is not investigated.
- **What drives L2/3 co-activation**: Whether the L2/3 perturbation signal comes from visual cortex, parietal cortex, or internal motor state representations is not resolved.

---

### Connections & keywords

**Key citations**:
- Kawai et al. (2015) — motor cortex required for learning but not executing a motor skill (Neuron)
- Lopes et al. (2016) — robust role for motor cortex in rapid responses to feedback perturbations
- Attinger et al. (2017) — visuomotor coupling shapes visual cortex development; mismatch in visual cortex
- Fiser et al. (2016) — experience-dependent spatial expectations in mouse visual cortex
- Zmarz & Keller (2016) — mismatch receptive fields in visual cortex
- Rao & Ballard (1999) — predictive coding in visual cortex
- Adams et al. (2013) — predictions not commands: active inference in the motor system
- Churchland et al. (2012) — neural population dynamics during reaching (dynamic attractor)
- Li et al. (2015) — motor cortex circuit for motor planning and movement
- Peters et al. (2017) — reorganization of corticospinal output during motor learning
- Huber et al. (2012) — multiple dynamic representations in motor cortex during sensorimotor learning
- Kiritani et al. (2012) — hierarchical connectivity in corticospinal-corticostriatal microcircuit
- Weiler et al. (2008) — top-down laminar organisation of excitatory network in motor cortex

**Named models or frameworks**:
- Predictive processing / sensorimotor mismatch detection
- Hierarchical motor cortex microcircuit (L2/3 → L5 IT → L5 PT)
- Virtual reality spherical treadmill navigation task

**Brain regions**:
- Primary motor cortex (M1) / caudal forelimb area (CFA)
- Layer 2/3 of M1
- Layer 5 pyramidal tract (PT) neurons
- Layer 5 intratelencephalic (IT) neurons

**Keywords**:
- motor cortex, visually guided movement, sensory perturbation, unexpected feedback, corrective turns
- layer 2/3 vs. layer 5 PT, calcium imaging, two-photon imaging, GCaMP6f
- optogenetic inactivation, vGAT-ChR2, Sim1-Cre, Tlx3-Cre
- mismatch detection, predictive processing, motor plan co-activation, response selection
- virtual reality, spherical treadmill, mouse motor learning, sensorimotor integration
