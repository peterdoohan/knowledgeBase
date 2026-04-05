---
source_file: hartley2003_wayfinding_route.md
title: The Well-Worn Route and the Path Less Traveled: Distinct Neural Bases of Route Following and Wayfinding in Humans
authors: Tom Hartley, Eleanor A. Maguire, Hugo J. Spiers, Neil Burgess
year: 2003
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Wayfinding (finding novel paths) and route following (following well-learned routes) engage distinct neural systems in humans, with the hippocampus supporting accurate wayfinding and the caudate nucleus supporting route following.

### Background & motivation

Navigation in large-scale environments can be accomplished either by constructing a flexible cognitive map of spatial relationships between places (place learning, hippocampus-dependent) or by storing a sequence of actions associated with a familiar route (response learning, caudate-dependent). This dissociation had been firmly established in rodents, but prior human neuroimaging studies of navigation had not explicitly separated tasks requiring cognitive map use from those solvable by memorised action sequences, and had also conflated engagement with a task from successful performance of it. The study was designed to close this gap by comparing wayfinding and route-following tasks in a within-subject fMRI design, and by separately modelling performance quality alongside task engagement.

### Methods

- **Design**: fMRI study with 16 healthy right-handed male volunteers using virtual reality (VR) navigation
- **Virtual environments**: Two distinctive virtual towns built in Quake2; subjects explored Town 1 freely for 15 min pre-scan (cognitive map training) and repeatedly followed a fixed route in Town 2 until it was well-learned (response/route training)
- **Experimental tasks (fMRI, blocked design, 50 s epochs)**:
  - *Wayfinding*: navigate between novel sequences of landmark pairs in Town 1, requiring a cognitive map.
  - *Route following*: repeatedly follow the same memorised 8-landmark route in Town 2.
  - *Trail following* (control): follow visible green markers to targets in Town 1; no spatial memory required.
- **Performance measure**: distance error — extra path length relative to the ideal shortest path, calculated trial-by-trial using a resistive grid algorithm. Route-following performance was near ceiling for all subjects; wayfinding varied substantially between subjects.
- **fMRI analysis**: SPM99, random effects; general linear model including condition regressors, trial-by-trial wayfinding accuracy as a within-subjects parametric regressor, and VR movement parameters (speed, turn rate/direction) as covariates of no interest. Between-subjects correlations computed between individual overall wayfinding accuracy and fMRI activation contrasts.
- **Scanner**: 2 Tesla Siemens Magnetom VISION; 32-slice EPI, TR = 3.2 s.

### Key findings

- **Within-subjects performance effect**: Right posterior hippocampus (MNI 30, -33, -3; Z = 3.29) and right insula (42, -12, 12; Z = 4.27) showed parametrically greater activation on more accurate wayfinding trials; the hippocampus was not activated in performance-independent task comparisons.
- **Between-subjects — wayfinding accuracy vs. wayfinding > trail following**: Left anterior hippocampus (-30, -18, -15; r = 0.74, p < 0.001) was more active in better navigators; right hippocampus showed the same trend (r = 0.62, p = 0.005) but did not reach significance.
- **Between-subjects — route following accuracy vs. wayfinding > route following**: Right caudate head (21, 24, 6; r = -0.78, p < 0.001) showed a negative correlation with wayfinding accuracy, indicating good navigators preferentially activated caudate during route following, not during wayfinding.
- **Post-hoc confirmation**: The same caudate voxel showed a positive correlation with performance in route following > trail following (r = 0.47, p < 0.05).
- **Performance-independent effects**: Wayfinding broadly engaged parahippocampal, fusiform, retrosplenial, posterior parietal, precuneus, caudate body, and prefrontal cortices; route following engaged a smaller network including caudate body, insula, and motor/premotor areas.
- **Perirhinal cortex**: Bilaterally more active in good navigators during wayfinding vs. route following (peak 33, -12, -30; r reported but not given a specific value in the text), interpreted as reflecting identification of landmarks from novel perspectives.
- **Hippocampus absent from performance-independent contrasts**: The performance regressor captured hippocampal variance, explaining why hippocampus was absent from simple task comparisons — poor navigators' deactivation cancelled good navigators' activation.

### Computational framework

Not applicable in the sense of a formal mathematical model; the paper uses a cognitive-map / response-learning theoretical framework grounded in animal learning theory (Tolman 1948; O'Keefe & Nadel 1978; Packard & McGaugh 1996). The key conceptual claim is that two representational systems exist in parallel: a flexible allocentric cognitive map (hippocampus-dependent) that supports novel route computation, and an action-based response representation (caudate-dependent) that supports fluent execution of overlearned routes. The subject's choice of which representation to deploy determines both performance and the pattern of neural activation. The results constrain reinforcement-learning accounts that assign distinct roles to model-based (hippocampus/PFC) and model-free / habit (striatum) systems.

### Prevailing model of the system under study

Prior to this paper, the human neuroimaging literature treated navigation as a largely undifferentiated cognitive process. Studies had identified a consistent network (parahippocampal, retrosplenial, posterior parietal, fusiform cortices, and hippocampus), but had not distinguished whether tasks required flexible spatial knowledge or rote route memory, and had not systematically separated task engagement from task success. A related debate concerned whether hippocampal activation in navigation reflected encoding/retrieval of spatial layout per se or simply the difficulty and perceptual demands of the task. The dominant view, drawn from rodent neurophysiology (place cells, O'Keefe & Nadel 1978; caudate response learning, Packard & McGaugh 1996), held that hippocampus supports a cognitive map while caudate supports response learning, but this had not been cleanly demonstrated in human imaging. The authors introduce this framework explicitly as the organising hypothesis to test.

### What this paper contributes

The paper establishes that the rodent place/response-learning dissociation maps onto a hippocampus/caudate dissociation in humans during naturalistic virtual navigation. The key advance is methodological and empirical: by modelling trial-by-trial accuracy as a parametric covariate, the authors show that hippocampal engagement is specifically tied to navigational success, not merely to the attempt. This resolves conflicts in the earlier literature — discrepancies between studies in whether hippocampus was activated are explained by variation in performance levels and the degree to which tasks could be solved by route memory. A further contribution is distinguishing within-subjects (right posterior hippocampus tracks moment-to-moment accuracy) from between-subjects (left/bilateral anterior hippocampus distinguishes good from poor navigators) effects, with different lateralisation profiles. The paper also offers a reinterpretation of earlier findings: Maguire et al. (1998a) caudate activation during VR navigation likely reflected fluent route following, and Gron et al.'s (2000) sex difference in hippocampal activation may be largely attributable to performance differences.

### Brain regions & systems

- **Right posterior hippocampus** — parametrically activated by within-subject trial-to-trial accuracy in wayfinding; proposed to compute or retrieve the spatial map needed for accurate navigation.
- **Left (and bilateral) anterior hippocampus** — more active in good navigators than poor navigators during wayfinding; between-subjects marker of cognitive-map proficiency.
- **Right caudate head** — more active in good navigators during route following; negatively correlated with wayfinding accuracy, indicating appropriate deployment of response learning for learned routes.
- **Bilateral caudate body** — activated in both wayfinding and route following relative to trail following; proposed to play a general role in navigation rather than specifically supporting either representation type.
- **Parahippocampal cortex (bilateral, right-dominant)** — strongly activated in performance-independent wayfinding; involved in perceptual-spatial processing of scene/landmark identity.
- **Perirhinal cortex (bilateral)** — more active in good navigators during wayfinding vs. route following; proposed to support recognition of landmarks from novel viewpoints.
- **Retrosplenial cortex** — activated in wayfinding (performance-independent); implicated in reference frame transformations.
- **Posterior parietal cortex / precuneus** — activated in wayfinding (performance-independent); involved in spatial transformations and retrieval of imageable spatial information.
- **Medial prefrontal cortex** — specifically activated in wayfinding vs. route following and trail following; interpreted as executive planning for novel routes.
- **Right insula** — within-subjects performance effect; linked to crossmodal bodily motion representation in the absence of vestibular/somatosensory input.
- **Premotor cortex, SMA, lateral parietal/somatosensory cortex** — more active in route following than wayfinding; associated with the action-based representation of a memorised motor sequence.

### Mechanistic insight

The paper meets both criteria for this section. It presents a specific algorithm — parallel deployment of a hippocampus-based cognitive map (allocentric place representation) vs. a caudate-based action-sequence representation — and provides fMRI data that link the specific variables of that algorithm (within-subject accuracy for the hippocampus; between-subject route-following proficiency for the caudate head) to measured neural activity, distinguishing the two systems over alternatives.

**Computational**: The brain must select the appropriate representational strategy given the navigational demand: flexible path computation from a cognitive map when a novel route is required; execution of a stored action sequence when a familiar route is available. Using the wrong strategy incurs a performance cost in the mismatched condition (caudate deployment during wayfinding impairs accuracy; hippocampal map use during route following does not impair but adds perceptual overhead).

**Algorithmic**: The hippocampal system represents spatial locations allocentrically, in terms of their geometric relationships to landmarks ("where is goal X relative to the current position?"), enabling computation of novel paths. The caudate system represents a sequence of body-relative actions ("turn left at junction Y, then forward to landmark Z"), enabling fast, automatic route execution. The two representations coexist in parallel; performance reflects which is selected.

**Implementational**: The paper does not address specific cell types or biophysical mechanisms. However, it does localise the hippocampal effect to anterior vs. posterior subregions (anterior shows between-subjects, posterior shows within-subjects effects), and specifically to the head of the caudate for response-learning effects vs. the body for a more general navigational role. No pharmacological, optogenetic, or single-unit data are provided; the paper is purely fMRI.

**Bonus**: The posterior hippocampal structural enlargement in taxi drivers (Maguire et al. 2000) is discussed as potentially arising from the sustained activation of this region during accurate navigation across years of experience — an intriguing link between functional activation and structural plasticity, though speculative.

### Limitations & open questions

- **Male-only sample**: All 16 subjects were male, so sex differences in navigation strategies cannot be addressed and generalisability to women is untested.
- **Small N**: With 16 subjects, between-subjects correlations may be inflated and are certainly underpowered to detect all relevant effects. The uncorrected p < 0.001 threshold (without family-wise error correction) was justified by a priori hypotheses but remains liberal.
- **Within-subjects analysis limited to wayfinding**: Route-following performance was near ceiling for all subjects, precluding a parallel within-subjects analysis for that condition.
- **Route-following performance uniformly high**: Because all subjects learned the route well, individual differences in caudate engagement during route following cannot be fully explored with the accuracy regressor.
- **No distinction between hippocampal subfields**: fMRI resolution was insufficient to differentiate CA1, CA3, dentate gyrus, or subiculum contributions.
- **Action vs. cognitive map selection mechanism**: The paper assumes parallel co-existence of representations and that subjects select one, but does not characterise the selection mechanism — what determines which system dominates?
- **Open question**: How do the place/response systems interact during transitions from novel to familiar routes, and at what point does a route become automated enough for caudate to take over?
- **Generalisation beyond spatial navigation**: Whether the hippocampus/caudate dissociation applies to non-spatial domains (e.g., conceptual or social navigation) is not addressed.

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — The Hippocampus as a Cognitive Map (foundational framework)
- Packard & McGaugh (1996) — hippocampus vs. caudate inactivation in place vs. response learning in rats
- Maguire et al. (1998a) — prior fMRI navigation study; hippocampus and caudate in VR navigation
- Maguire et al. (2000) — structural hippocampal enlargement in London taxi drivers
- Tolman (1948) — cognitive maps in rats and men
- Gron et al. (2000) — sex differences in hippocampal activation during VR navigation
- Poldrack et al. (2001) — interactive memory systems in humans

**Named models or frameworks**:
- Cognitive map / place learning (O'Keefe & Nadel)
- Response learning (Potegal, Packard & McGaugh)
- SPM99 (general linear model, random effects fMRI analysis)

**Brain regions**:
- Hippocampus (posterior, anterior)
- Caudate nucleus (head, body)
- Parahippocampal cortex
- Perirhinal cortex
- Retrosplenial cortex
- Posterior parietal cortex / precuneus
- Medial prefrontal cortex
- Insula
- Premotor cortex / SMA

**Keywords**:
- spatial navigation, fMRI
- wayfinding vs. route following
- place learning vs. response learning
- cognitive map
- hippocampus, caudate nucleus
- virtual reality navigation
- performance-related hippocampal activation
- allocentric vs. egocentric navigation
- within-subjects vs. between-subjects performance effects
- navigational accuracy, individual differences
