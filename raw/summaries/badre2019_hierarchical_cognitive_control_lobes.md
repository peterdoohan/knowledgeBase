---
source_file: badre2019_hierarchical_cognitive_control_lobes.md
title: "Hierarchical cognitive control and the frontal lobes"
authors: David Badre, Theresa M. Desrochers
year: 2019
journal: "Handbook of Clinical Neurology, Vol. 163 (3rd series): The Frontal Lobes"
paper_type: review
contribution_type: review
---

### One-line summary

The frontal lobes support hierarchical cognitive control through at least three functionally distinct lateral zones — sensorimotor, contextual, and schematic control — organized as a processing hierarchy rather than a simple gradient, with rostrolateral PFC playing a specialised role in sequential task monitoring near sequence boundaries.

---

### Background & motivation

Cognitive control — the ability to choose actions based on internal goals rather than habit — is routinely needed in complex, hierarchically structured settings where multiple goals and contingencies must be managed simultaneously. Deficits in hierarchical control are disproportionately disabling for patients with frontal lobe damage, yet standard laboratory executive function tests often fail to capture them. A mechanistic account of how the frontal lobes implement hierarchical control is needed both to close the gap between lab measures and real-world dysfunction and to enable better diagnosis and therapeutic intervention across neurological and psychiatric conditions.

---

### Methods

This is a narrative review chapter synthesising fMRI, lesion, ECoG, TMS, and effective connectivity studies focused on two forms of hierarchical control: policy abstraction (managing multiple contextual contingencies) and sequential task control. Inclusion is focused on the authors' own research programme and closely related work, particularly studies using policy-order manipulations and sequential task paradigms. Synthesis is theoretical rather than meta-analytic, though one quantitative meta-analysis (Badre and Nee, 2018) is central to the conclusions.

---

### Key findings

- fMRI studies (Koechlin et al., 2003; Badre and D'Esposito, 2007) show a rostrocaudal progression of activation in lateral frontal cortex as policy abstraction increases, engaging dorsal premotor, anterior premotor, DLPFC, and then RLPFC in sequence.
- Focal lesion studies (Badre et al., 2009; Azuar et al., 2014) confirm this organisation is functionally necessary: patients show deficits at the policy level corresponding to their lesion site and above, but not below.
- A meta-analysis (Badre and Nee, 2018) identifies three discrete lateral frontal zones rather than a single gradient: (1) sensorimotor control (motor/premotor), (2) contextual control (anterior premotor to DLPFC), and (3) schematic control (RLPFC/lateral frontopolar cortex).
- These zones correspond to distributed frontoparietal networks, not isolated frontal areas; the same network boundaries account for parietal as well as frontal activations (Choi et al., 2018).
- Effective connectivity analysis (Nee and D'Esposito, 2016) and TMS replication (Nee and D'Esposito, 2017) establish a processing hierarchy with mid-DLPFC at its apex, receiving domain-specific inputs from caudal areas and schematic input from RLPFC, and exerting domain-general top-down influence on premotor regions.
- ECoG in epilepsy patients (Voytek et al., 2015) shows directional low-frequency-to-high-gamma coupling from rostral PFC to premotor/motor cortex that increases with higher-order policy — consistent with a rostral-to-caudal processing hierarchy.
- For sequential tasks, RLPFC activity ramps across serial positions within a four-item task sequence (Desrochers et al., 2015); single-pulse TMS to RLPFC causes increasing errors at later sequence positions, confirming necessity.
- The ramping RLPFC signal is not modulated by external cue availability or by whether task-switching is required (Desrochers et al., 2019), suggesting it tracks approach to a sequence boundary rather than task uncertainty per se.
- RLPFC activation during navigation correlates with hippocampal goal representations (Brown et al., 2016), supporting its role in accessing explicit memory-based plans.

---

### Computational framework

The paper invokes a hierarchical reinforcement learning / working memory gating framework as its primary computational lens, drawing on cortico-striatal gating models (Chatham and Badre, 2015; Frank and Badre, 2012).

The core idea is that the control system is organised as a policy hierarchy: higher-order policies select among lower-order policies rather than mapping directly to responses. The key computational variables are: (a) the order of contextual contingency a region must represent, (b) the temporal extent over which a context must be maintained, and (c) gating signals from cortico-striatal loops that control when and what contextual representations are updated or read out. Rostral frontal regions represent higher-order, more temporally extended contexts; caudal regions represent more immediate, response-proximal policies. Basal ganglia interactions are hypothesised to gate transitions between levels of this hierarchy, enabling learning and generalisation of hierarchical rule structures.

---

### Prevailing model of the system under study

Prior to the empirical programme reviewed here, the dominant view — associated with Fuster's perception-action cycle — held that the frontal lobes are organised along a single rostrocaudal gradient, with temporal abstraction (the duration over which a context must be held in working memory) as the organising dimension. More rostral frontal cortex was thought to support more temporally extended, abstract goals; more caudal frontal cortex was thought to support more immediate, concrete motor actions. The gradient was conceived as continuous rather than zonal. There was no consensus on whether this reflected a true processing hierarchy (with rostral areas causally organising caudal ones) or merely a functional correlation. Koechlin and colleagues (2003) formalised this into a "cascade model" of PFC organisation, distinguishing episodic, contextual, and sensory branches from rostral to caudal PFC.

---

### What this paper contributes

The review refines the simple gradient model in two important ways. First, it establishes that lateral PFC is better characterised by at least three discrete functional zones corresponding to distributed frontoparietal networks than by a single continuous gradient along a single dimension of abstraction. The most rostral zone (RLPFC/schematic control) is functionally distinct from the gradient logic: it is not simply active for higher-order policy but is selectively recruited when control requires access to an explicit internal model — schematic, hypothetical, or memory-derived. Second, and crucially, the review synthesises converging causal and directional evidence (lesion, TMS, ECoG, effective connectivity) for a true processing hierarchy with mid-DLPFC at its apex, resolving the longstanding question of whether the rostrocaudal organisation merely reflects correlation or genuine causal influence. The chapter also establishes RLPFC as the locus of sequential control monitoring, specifically near chunk boundaries, and links this to hippocampal goal representations.

For reviews: the key unresolved questions are (1) the precise mechanisms of hierarchical inter-region communication (e.g., the role of basal ganglia gating), (2) the neural representations and dynamics supporting hierarchical control in non-human animals, and (3) how value/motivational signals from medial frontal cortex interact with this lateral frontal hierarchy.

---

### Brain regions & systems

- **Motor cortex / premotor cortex (dorsal, PMd; ventral, PMv)** — sensorimotor control zone; maps simple stimulus-response policies; lowest level of the lateral frontal hierarchy.
- **Anterior dorsal premotor cortex (prePMd) / Inferior frontal junction (IFJ) / prePMv** — contextual control zone (caudal portion); supports selection of first- and second-order policies; receives domain-specific (spatial/verbal) inputs; within the hierarchy, positioned below DLPFC.
- **Dorsolateral PFC (DLPFC) / mid-DLPFC** — contextual control zone (rostral portion); apex of the processing hierarchy; domain-general; exerts top-down influence on premotor contextual control regions; engaged for third-order and higher policy.
- **Rostrolateral PFC (RLPFC) / lateral frontopolar cortex** — schematic control zone; not the extreme of the abstraction gradient but rather a gateway for schema/memory-based control inputs; necessary near sequential task boundaries; connected with medial frontal and medial temporal (hippocampal) networks.
- **Pre-supplementary motor area (pre-SMA) / medial frontal cortex** — co-activated with RLPFC during sequential tasks; ramping signal observed; role in sequential monitoring.
- **Basal ganglia** — proposed to implement gating functions that regulate which contextual representations are updated and read out by separate frontal networks; critical for learning and generalisation of hierarchical rules.
- **Hippocampus** — represents prospective goals during navigation; strength of goal representation correlates with RLPFC activation, supporting RLPFC's role in accessing memory-based plans.
- **Parietal cortex** — frontoparietal networks extend into parietal cortex; the same three-network structure (sensorimotor, association network 1, association network 2) that explains frontal rostrocaudal differences also accounts for parietal activation differences across policy levels.

---

### Mechanistic insight

This paper partially meets the bar. It synthesises neural data (fMRI, lesion, TMS, ECoG, effective connectivity) that support a specific hierarchical processing algorithm over alternatives, and provides causal evidence via lesion and TMS. However, the implementational level (specific cell types, laminar organisation, biophysical mechanisms) is not directly addressed — only briefly noted via anatomical observations (dendritic spine density, laminar differentiation) without mechanistic formalisation.

- **Computational**: The problem is coordinating multiple levels of contextual contingency simultaneously to produce appropriate actions, while also maintaining an internal model of sequential structure across time.
- **Algorithmic**: A hierarchical control architecture in which higher-order context representations (in more rostral regions) select among lower-order context representations (in more caudal regions), which in turn select among immediate responses. Gating by cortico-striatal circuits controls when representations are updated vs. held stable. RLPFC provides schema/memory inputs into this hierarchy at demand-driven junctures (e.g., sequence boundaries). Causal directionality is supported by effective connectivity (Nee and D'Esposito, 2016), TMS (Nee and D'Esposito, 2017), and ECoG oscillatory coupling (Voytek et al., 2015).
- **Implementational**: Partially addressed. Anatomical features noted as consistent with the hierarchy (reduced cell density and longer connectional distance in more rostral areas; greater dendritic spine density), but no mechanistic account of the specific neural implementation of gating or inter-region signalling is provided. The basal ganglia gating hypothesis is invoked conceptually but not implemented at a biophysical level.

---

### Limitations & open questions

- The review acknowledges that relatively few experiments have directly manipulated hierarchical control demands, limiting the evidentiary base for fine-grained claims.
- Multiple dimensions of abstraction (policy order, temporal abstraction, relational integration, domain specificity, working memory updating) tend to co-vary in existing tasks, making it difficult to identify which single variable organises the rostrocaudal hierarchy.
- The hierarchical organisation is most clearly demonstrated in humans; animal models are limited because the tasks require language and abstract rule following. This constrains mechanistic (cellular/circuit) investigation.
- The functional role of RLPFC near sequence boundaries remains imprecisely specified: whether it represents the overarching goal, signals uncertainty, or performs some other computation is not yet resolved.
- How value and motivational signals from medial frontal cortex interact with the lateral frontal processing hierarchy is largely uncharacterised.
- The mechanisms by which cortico-striatal gating operates at a neural circuit level — which populations, timescales, neuromodulators — are not yet established.

---

### Connections & keywords

**Key citations**:
- Badre and D'Esposito (2007) — foundational fMRI evidence for rostrocaudal policy-order organisation
- Koechlin, Ody, and Kouneiher (2003) — cascade model of PFC; parallel fMRI evidence
- Badre et al. (2009) — lesion evidence confirming hierarchical deficits
- Badre and Nee (2018) — meta-analysis establishing three functional zones
- Nee and D'Esposito (2016, 2017) — effective connectivity and TMS evidence for processing hierarchy
- Voytek et al. (2015) — ECoG oscillatory evidence for rostral-to-caudal directional influence
- Desrochers et al. (2015) — fMRI and TMS evidence for RLPFC in sequential control
- Desrochers et al. (2019) — follow-up isolating boundary monitoring as driver of RLPFC ramping
- Chatham and Badre (2015) — cortico-striatal gating model
- Frank and Badre (2012) — hierarchical RL in cortico-striatal circuits
- Choi et al. (2018) — functional networks underlying rostrocaudal hierarchy

**Named models or frameworks**:
- Perception-action cycle (Fuster, 2001)
- Cascade model of prefrontal cortex (Koechlin et al., 2003)
- Policy abstraction framework (Badre, 2008; Badre and Nee, 2018)
- Cortico-striatal gating / working memory gating model (Chatham and Badre, 2015; Frank and Badre, 2012)
- Hierarchical reinforcement learning (Frank and Badre, 2012)
- Multiple errands test (ecological validity neuropsychology)

**Brain regions**:
- Rostrolateral prefrontal cortex (RLPFC) / lateral frontopolar cortex
- Dorsolateral prefrontal cortex (DLPFC) / mid-DLPFC
- Anterior dorsal premotor cortex (prePMd)
- Ventral anterior premotor cortex (prePMv) / inferior frontal junction (IFJ)
- Motor cortex / dorsal premotor cortex (PMd)
- Pre-supplementary motor area (pre-SMA)
- Medial prefrontal cortex
- Basal ganglia
- Hippocampus
- Parietal cortex

**Keywords**:
- hierarchical cognitive control
- rostrocaudal organisation of prefrontal cortex
- policy abstraction
- schematic control
- contextual control zone
- sequential task control
- RLPFC / frontopolar cortex
- cortico-striatal gating
- working memory updating
- effective connectivity
- fMRI hierarchical tasks
- frontal lobe executive function
