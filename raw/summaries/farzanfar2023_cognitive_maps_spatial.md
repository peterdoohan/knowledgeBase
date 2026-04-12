---
source_file: "farzanfar2023_cognitive_maps_spatial.md"
paper_id: "farzanfar2023_cognitive_maps_spatial"
title: "From cognitive maps to spatial schemas"
authors: "Delaram Farzanfar, Hugo J. Spiers, Morris Moscovitch, R. Shayna Rosenbaum"
year: 2023
journal: "Nature Reviews Neuroscience"
paper_type: "review"
contribution_type: "theoretical"
species: ["human"]
tasks: ["hexmaze", "virtual_navigation", "navigation_task"]
methods: ["fmri", "lesion"]
brain_regions: ["hippocampus", "entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "ventromedial_prefrontal_cortex", "striatum", "retrosplenial_cortex"]
keywords: ["cognitive", "maps", "spatial", "schemas"]
key_citations: ["epstein2017_cognitive_maps_humans"]
---

### One-line summary

This review proposes that repeated navigation across similarly structured environments gives rise to "spatial schemas" — generalizable, extra-hippocampal spatial knowledge structures that are conceptually and neurally distinct from cognitive maps and event schemas.

---

### Background & motivation

Cognitive maps (environment-specific allocentric spatial representations) and event schemas (abstract knowledge structures derived from repeated event experience) have been studied largely in isolation, and there has been little attempt to integrate them into a unified framework for spatial knowledge. The concept of a "spatial schema" — a prototypical spatial representation derived from statistical abstraction across many similarly structured environments — has not been systematically theorised or operationalised in humans. This review fills that gap by synthesising evidence from rodent spatial learning, human neuroimaging and neuropsychology, and urban analytics to propose a working neurocognitive framework for spatial schema formation, maintenance, and application.

---

### Methods

This is a narrative review synthesising findings across multiple empirical literatures.

- **Scope**: Rodent spatial navigation (paired-associate tasks, village maze paradigm, HexMaze), human neuropsychological case studies (amnesic patients with hippocampal lesions, e.g. K.C.), human fMRI/neuroimaging studies, large-scale virtual navigation datasets (Sea Hero Quest, ~3.9 million participants), and urban analytics/space syntax research.
- **Synthesis method**: Narrative integration across species and levels of analysis; no formal meta-analytic statistics. The review draws on established frameworks (memory consolidation, cognitive map theory, predictive coding) and extends them to the novel concept of spatial schemas.
- **Inclusion criteria**: Studies on spatial navigation, schema formation, episodic memory consolidation, hippocampal–neocortical interaction, and urban data analytics relevant to generalizable spatial representations.

---

### Key findings

- **Conceptual distinction**: Spatial schemas are defined as superordinate, generalizable spatial representations derived from integrating spatial gists across multiple environments sharing common geometric structure — distinct from cognitive maps (environment-specific) and spatial gists (environment-level summaries).
- **HPC independence**: Spatial schemas are proposed to be stored and retrieved independently of the hippocampus (HPC), consistent with evidence that amnesic patients (e.g. K.C.) retain the overall geometric layout of familiar environments while losing perceptual detail.
- **Geometric > surface properties**: Geometric (3D structural) features of environments drive schema formation more than surface (2D, perceptual) properties; HPC-lesioned rats navigate using room geometry but fail when geometry is disrupted.
- **Rodent evidence**: Rats with pre-lesion experience in a complex "village maze" can rapidly re-learn new reward locations (consistent with schema-guided embedding) even following HPC lesions; novel paired associates are acquired in a single trial after schema formation. Rapid consolidation (<24 h) depends on HPC; long-term schema maintenance does not.
- **Human fMRI evidence**: Activity shifts from HPC to vmPFC with overlearning; schema-congruent novel associations are rapidly integrated in vmPFC with reduced HPC involvement. Representational similarity analyses show overlapping associations are integrated in anterior HPC and posterior mPFC.
- **Schema cells**: Neurons in the macaque HPC encode task representations spanning spatial and cognitive dimensions, generalising across environments of similar geometry (not visual similarity), linking to past/future actions — a candidate neural substrate for spatial schemas.
- **RSC generalization**: RSC codes distance-to-goals in well-known environments but not recently learned ones; generalises local codes (e.g. facing direction) across geometrically similar virtual environments.
- **ERC grid-cell contribution**: Grid cell activity in human ERC shifts from sixfold to fourfold rotational symmetry in barrier-segmented environments, suggesting the ERC provides a structural scaffold that adapts to environmental geometry and may support schema instantiation.
- **Urban analytics / Sea Hero Quest**: People who grew up in grid-like cities (e.g. Buenos Aires, Chicago) are worse navigators overall than those from irregular cities (e.g. Prague, Paris), but show a slight advantage in gridlike virtual environments — suggesting that early environmental exposure shapes spatial schemas that influence navigational strategy.
- **Sleep and consolidation**: Sleep facilitates gist extraction, consolidation of spatial representations, and explicit knowledge of spatial regions — mechanisms proposed to underlie schema formation via HPC–neocortical interaction during slow-wave replay.

---

### Computational framework

**Predictive coding and Bayesian prior formation** are invoked as the key computational lens through which spatial schemas operate: schemas function as expectations or "mental models" of environmental structure, biasing perception and encoding when navigating familiar categories of environment.

Additionally, **hidden state inference** is proposed as a mechanism by which the HPC integrates sensory input with stored representations to infer current environmental context; prior schema knowledge biases the stored states used in this inference, enabling more efficient remapping for geometrically familiar environments.

**Space syntax and graph-theoretic methods** (e.g. axial line maps, integration, choice, betweenness centrality) are used as formal tools to quantify environmental geometry and street network structure at urban scales, operationalising the geometric properties that schemas are proposed to capture.

**Neural network and deep learning models** (discussed in Box 2) are noted as converging tools: a neural network replicating HPC-indexing and neocortex-representation streams reproduces rodent schema experiments; deep networks modelling primate parietal cortex suggest high-dimensional scene inputs are projected onto low-dimensional spatial structures akin to spatial schemas.

---

### Prevailing model of the system under study

The dominant pre-existing framework, as laid out in the paper's introduction, treats the hippocampus as the central structure for spatial navigation via cognitive maps: HPC place cells encode unique allocentric representations of individual environments, enabling flexible route planning. Schemas, where studied at all, were primarily investigated in the context of event (non-spatial) memory, with the HPC playing a critical role in rapid schema-congruent encoding and subsequent consolidation to the mPFC. The standard account assumed that spatial generalisation across environments is handled by the HPC through mechanisms such as remapping and pattern separation, with extra-hippocampal neocortical regions receiving memories only after systems consolidation. Spatial representations preserved following HPC damage were attributed to "semantic" or "schematised" forms of memory, but the neural machinery and principles governing such representations were not formally theorised as a distinct class of spatial knowledge structure.

---

### What this paper contributes

The paper provides the first explicit theoretical framework for **spatial schemas** as a category distinct from cognitive maps, spatial gists, and event schemas, and maps out their proposed neural instantiation. Concretely:

- It establishes that spatial schemas are not merely degraded cognitive maps but superordinate, geometry-based knowledge structures derived from experience across multiple similarly structured environments.
- It proposes a clear neural hierarchy: detailed cognitive maps (posterior HPC) → spatial gists (anterior HPC, PHC, RSC, PPC) → spatial schemas (mPFC/vmPFC, RSC, ERC, angular gyrus, extra-HPC network).
- It integrates urban analytics (space syntax, street network entropy) as a novel empirical tool to operationalise and test the environmental properties that drive schema formation — a methodological contribution with practical implications for understanding how city design shapes cognition.
- It identifies geometry (not surface features) as the key dimension along which spatial schemas generalise, grounding this in convergent evidence from lesion studies, fMRI, place cell physiology, and large-scale behavioural data.
- It frames schemas as Bayesian priors in a predictive coding account of spatial navigation, unifying the framework with broader theories of perception and memory.
- It highlights unresolved questions (posterior-to-anterior schema gradient outside HPC; schema–reward interactions; role of oscillations in HPC–PFC–RSC communication) that define the agenda for future empirical work.

---

### Brain regions & systems

- **Hippocampus (HPC), posterior** — detailed cognitive map storage; pattern separation of similar environments; rapid encoding of schema-congruent novel associations; HPC replay during sleep consolidates spatial memories
- **Hippocampus (HPC), anterior** — spatial gist representation; coarse/global spatial code; integration of overlapping item–context associations; more global code for large-scale outdoor navigation
- **Ventromedial prefrontal cortex (vmPFC)** — proposed primary locus of spatial schema storage and retrieval in humans; accelerates encoding of schema-congruent novel information; activity shifts from HPC to vmPFC with overlearning
- **Medial prefrontal cortex (mPFC)** — schema monitoring; consistency checking between stored schemas and novel input; pattern recognition for gist extraction (mice); grid-like coding; proposed locus for schema in rodents (homologous to vmPFC)
- **Retrosplenial cortex (RSC)** — hub for translating egocentric/allocentric frames; generalises local spatial codes across geometrically similar environments; encodes distance-to-goal in well-known environments; long-term spatial structure storage; implicated in event schema instantiation
- **Entorhinal cortex (ERC)** — grid cell-based geometric scaffold; learns transition structure and spatial regularities; mediates HPC–neocortex information transfer; geometry-sensitive (grid symmetry changes with environmental barriers)
- **Parahippocampal cortex (PHC)** — perceptual features and spatial relations; scene-level representation; repetition suppression effects for same-layout rooms
- **Posterior parietal cortex (PPC)** — spatial relations and high-level scene integration; proposed to sit atop cortical hierarchy integrating low-level visual features with categorical spatial concepts
- **Angular gyrus** — statistical learning integration; schema-level binding of spatial gist content; higher-level abstraction than HPC
- **Dorsal striatum** — proposed role in schema-guided navigation via updating transition structure linked to goals (circuits used when novel paths are embedded into existing schema)
- **Occipital place area** — connectivity of visible space; local scene representation

---

### Mechanistic insight

The paper does not meet the bar for a mechanistic insight entry: it is a review that synthesises behavioural, lesion, and neuroimaging evidence and proposes a framework, but does not present a single formalised algorithm and then provide neural data specifically testing that algorithm over alternatives.

The paper describes several candidate mechanisms (HPC hidden-state inference, sleep-dependent replay-mediated consolidation, mPFC-mediated pattern recognition for gist extraction), but these are drawn from disparate studies across species and paradigms rather than from a unified empirical test of one algorithm. Neural data from fMRI, lesions, and single-unit recordings are reviewed but not assembled to adjudicate between specific competing algorithmic accounts of spatial schema formation.

---

### Limitations & open questions

- **Operationalisation**: Spatial schemas lack a standardised experimental paradigm; most "schema" evidence in humans comes from event schema or associative inference tasks, not paradigms designed to probe spatial generalisation across real-world environment categories.
- **Human vs. rodent gap**: The majority of neural mechanistic evidence comes from rodents; it remains unclear how well rodent spatial schema findings map onto the human case given scale, complexity, and the availability of language and semantic systems.
- **HPC role in schema acquisition**: Whether new spatial schemas can be acquired and/or updated following HPC damage remains an open empirical question.
- **Schema vs. gist boundary**: The boundary conditions distinguishing spatial gists from spatial schemas at the neural level are not yet established.
- **Posterior-to-anterior gradient**: Whether schemas form along a posterior-to-anterior gradient outside the HPC (analogous to the within-HPC gradient) is unknown.
- **vmPFC vs. mPFC**: The precise role of ventral vs. dorsal mPFC subregions in spatial schemas — separate from their roles in reward valuation, goal maintenance, and event schemas — requires targeted lesion and imaging studies.
- **Schema–reward interactions**: How schemas interact with motivational states and reward history is underspecified.
- **Neural oscillations**: How oscillatory communication among HPC, PFC, and RSC instantiates spatial schemas during navigation remains to be characterised.
- **Development**: Longitudinal studies examining how early-life navigational experience shapes spatial cue preferences and schema formation across development are lacking.
- **Urban analytics integration**: Systematic quantification of real-world environmental geometry at multiple scales is methodologically challenging; space syntax measures have not yet been validated against neural schema representations.

---

### Connections & keywords

**Key citations**:
- Tse et al. (2007, 2011) — rodent paired-associate schema consolidation studies
- Gilboa & Marlatte (2017) — neurobiology of schemas and schema-mediated memory
- Baraduc, Duhamel & Wirth (2019) — schema cells in macaque hippocampus
- Spiers & Maguire (2007) — remote spatial memory, two-cities study
- Epstein et al. (2017) — cognitive map in humans
- O'Keefe & Nadel (1978) — *The Hippocampus as a Cognitive Map*
- Peer & Epstein (2021) — human brain uses spatial schemas for segmented environments
- Zheng et al. (2021) — mPFC represents common spatial structure across partially overlapping environments
- Marchette, Ryan & Epstein (2017) — RSC generalises spatial codes across geometrically similar environments
- Coutrot et al. (via Sea Hero Quest, referenced as ref. 117) — street network entropy and navigation ability across 3.9 million participants
- Robin & Moscovitch (2017) — details, gist and schema; HPC–neocortical interactions
- Lynch (1960) — *The Image of the City*; urban elements as landmarks, paths, nodes, edges, districts

**Named models or frameworks**:
- Spatial schema (proposed framework)
- Cognitive map (Tolman 1948; O'Keefe & Nadel 1978)
- Systems consolidation / standard model of memory consolidation
- Predictive coding
- Hidden state inference (HPC context inference)
- Space syntax (Hillier & Hanson; Filomena et al.)
- Complementary learning systems (CLS)
- Paired-associate (event arena) task
- Village maze paradigm
- HexMaze
- Sea Hero Quest

**Brain regions**: hippocampus (anterior, posterior), ventromedial prefrontal cortex, medial prefrontal cortex, retrosplenial cortex, entorhinal cortex, parahippocampal cortex, posterior parietal cortex, angular gyrus, dorsal striatum, occipital place area

**Keywords**: spatial schema, cognitive map, spatial gist, memory consolidation, hippocampal–neocortical interaction, geometric resemblance, pattern separation, HPC replay, predictive coding, space syntax, street network entropy, urban navigation
