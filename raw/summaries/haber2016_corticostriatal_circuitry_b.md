---
source_file: "haber2016_corticostriatal_circuitry_b.md"
paper_id: "haber2016_corticostriatal_circuitry_b"
title: "Corticostriatal circuitry"
authors: "Suzanne N. Haber"
year: 2016
journal: "Dialogues in Clinical Neuroscience"
paper_type: "review"
contribution_type: "review"
species: ["human", "macaque", "monkey"]
methods: ["fmri"]
brain_regions: ["hippocampus", "prefrontal_cortex", "orbitofrontal_cortex", "ventromedial_prefrontal_cortex", "striatum", "ventral_striatum", "nucleus_accumbens", "ventral_tegmental_area", "substantia_nigra", "thalamus", "amygdala"]
frameworks: ["reinforcement_learning"]
keywords: ["alexander_and_crutcher_1990_parallel_processing_model_of_basal_ganglia_circuits", "haber", "fudge_and_mcfarland_2000", "j_neurosci_striato_nigro_striatal_ascending_spiral", "kim", "mailly_and_calzavara_2006", "j_neurosci_reward_related_cortical_inputs_and_striatal_interface_zones", "averbeck", "lehman", "jacobson_and_haber_2014", "j_neurosci_probabilistic_estimates_of_corticostriatal_projection_overlap", "selemon_and_goldman_rakic_1985_longitudinal_topography_of_corticostriatal_projections_in_rhesus_monkey", "draganski_et_al_2008_human_diffusion_mri_evidence_for_basal_ganglia_connectivity", "schultz_1998_predictive_reward_signal_of_dopamine_neurons", "named_models_or_frameworks", "parallel_cortico_subcortical_channels_model_alexander_and_crutcher", "striato_nigro_striatal_ascending_spiral_haber_et_al", "direct_and_indirect_pathways_of_the_basal_ganglia", "hyperdirect_pathway_frontal_cortex_stn", "brain_regions"]
---

### One-line summary

Corticostriatal projections are not strictly parallel and segregated but form extensive zones of convergence that provide an anatomical substrate for integrating limbic, cognitive, and motor information across functional striatal territories, with a striato-nigro-striatal spiral enabling directed information flow from ventral to dorsal striatum.

---

### Background & motivation

The basal ganglia were historically understood as motor structures, but over the past four decades their role has expanded to encompass reward, motivation, cognition, and a broad range of goal-directed behaviors. The dominant organisational framework — parallel, segregated cortico-basal ganglia channels — cannot easily explain how motivation and cognition come to influence motor output, or how adaptive, learned behaviors emerge from the integration of emotionally, cognitively, and motorically driven inputs. This review synthesises primate anatomical tracing, physiology, and human neuroimaging to provide a richer account of how the cortex maps onto the striatum and how information flows between functional domains.

---

### Methods

This is a narrative review drawing primarily on:

- Anterograde and retrograde axonal tracing studies in nonhuman primates (macaques and squirrel monkeys), many from the author's own laboratory.
- Electrophysiological recordings in awake, behaving monkeys.
- Human neuroimaging (diffusion MRI, fMRI, PET) used to validate homologies with monkey anatomy.
- A computational/probabilistic model of corticostriatal projection overlap (Averbeck et al., 2014) to quantify convergence zones.
- The review is scoped to primate corticostriatal circuitry, with particular emphasis on frontal cortical inputs; temporal, parietal, amygdalar, and hippocampal inputs are covered more briefly.

---

### Key findings

- The striatum is organised along a ventromedial-to-dorsolateral gradient: ventral striatum (VS, including nucleus accumbens) receives limbic/reward inputs; central caudate receives associative/cognitive inputs (primarily dorsal PFC); the putamen receives sensorimotor inputs from motor and premotor cortex.
- Despite this topography, dense corticostriatal terminal fields from vmPFC, OFC, and dACC extensively interweave and converge, especially rostrally, creating anatomical "hubs" for integrating reward value, predictability, and salience.
- dPFC terminals invade deep within OFC projection fields (not merely at boundaries), and both converge with dACC inputs; this convergence decays exponentially with cortical separation distance — ~50% overlap for cortical regions 5 mm apart in primates, falling to <20% at 30 mm.
- A rostral anterior striatal region receives overlapping projections from vmPFC, OFC, dACC, dPFC, and vlPFC simultaneously, constituting a potential hub for converting motivational drive into strategic planning.
- Striato-nigro-striatal connections form an ascending spiral: the VS projects broadly to midbrain DA neurons (VTA and medial SNc), whose axons reach striatal territories innervated by dPFC; that central striatum in turn projects to midbrain regions projecting to the sensorimotor striatum. This architecture enables information to flow sequentially from limbic → cognitive → motor circuits.
- The VS influences a wide population of DA neurons but is itself modulated by a relatively limited midbrain region; the dorsolateral striatum does the opposite — influences few DA cells but is modulated by many.
- Fast-spiking GABAergic interneurons in the striatum receive convergent inputs from multiple cortical areas and are more responsive to cortical input than MSNs, suggesting a key integrative role.
- Diffusion MRI in humans replicates the overall topographic and integrative connectivity patterns seen in monkey tracing studies, validating the primate framework.

---

### Computational framework

Not applicable in the strict sense — the paper does not develop or test a computational model. However, it explicitly invokes the concept of parallel vs. integrative processing architectures as competing organisational principles for cortico-basal ganglia circuits. The probabilistic overlap model of Averbeck et al. (2014) is cited to quantify convergence as a function of cortical distance. The striato-nigro-striatal spiral is described as a feedforward/feedback architecture that implements directed information transfer across functional domains. The results most directly constrain reinforcement learning and hierarchical control models that assume the basal ganglia compute value signals and action-selection policies across motivational, cognitive, and motor levels.

---

### Prevailing model of the system under study

The dominant model at the time of writing held that the basal ganglia operate through a set of parallel, largely segregated cortico-subcortical loops: a limbic loop through the VS, a cognitive/associative loop through the caudate, and a sensorimotor loop through the putamen, each topographically maintained through GPi/SNr thalamo-cortical re-entry. This "parallel processing" framework (associated with Alexander & Crutcher, 1990) implied that limbic, cognitive, and motor circuits remain functionally insulated from one another throughout the basal ganglia, and provided the conceptual basis for mapping distinct psychiatric and neurological disorders onto specific striatal territories. The paper takes this topographic model as its starting point and challenges its strictness.

---

### What this paper contributes

The review makes the case that the parallel-channel model, while capturing the broad topographic organisation, misses a functionally critical layer of integration. Specifically it establishes:

1. Zones of dense convergence between prefrontal terminal fields (vmPFC, OFC, dACC, dPFC) within the striatum are not marginal overlaps but substantive anatomical substrates for cross-domain computation.
2. A rostral hub region integrates reward value, predictive signals, and executive control — potentially enabling a "common currency" valuation signal.
3. The striato-nigro-striatal spiral provides a concrete anatomical mechanism by which motivational states (mediated by VS activity) can modulate dopaminergic drive to cognitive and motor striatal territories, thereby influencing goal-directed action selection.
4. These integration principles are conserved in the human brain (diffusion MRI evidence), supporting clinical relevance.

For reviews: the key unresolved questions identified include how exactly convergent inputs at specific striatal loci are gated or weighted, what role the striosome/matrix compartmentalisation plays in the integrative architecture, and how the two organisational principles (segregated channels and integrative hubs) operate simultaneously to support both stable habit execution and flexible updating.

---

### Brain regions & systems

- **Ventral striatum (nucleus accumbens shell and core)** — primary target of limbic cortical and subcortical inputs; entry point of the striato-nigro-striatal spiral; associated with reward and reinforcement.
- **Caudate nucleus (head)** — target of dPFC projections; implicated in working memory and strategic planning; also receives convergent OFC and dACC inputs.
- **Putamen (central/dorsolateral)** — target of motor and premotor cortex; sensorimotor function; procedural learning.
- **Prefrontal cortex: vmPFC, OFC, dACC, dPFC** — functionally distinct subregions providing topographically organised but convergent corticostriatal projections; the focus of the integration argument.
- **Motor and premotor cortex** — project to dorsolateral putamen; reviewed as the distal output of the functional hierarchy.
- **Substantia nigra pars compacta (SNc) and VTA** — midbrain dopaminergic neurons; their organisation into dorsal tier (calbindin+, projects to VS) and ventral tier (calbindin-, projects to DS) underlies the spiral connectivity.
- **Globus pallidus (GPe, GPi) and ventral pallidum (VP)** — output nodes of striatal direct and indirect pathways.
- **Subthalamic nucleus (STN)** — part of the indirect and hyperdirect pathways; receives direct frontal cortex input.
- **Amygdala (basolateral group)** — prominent subcortical input to VS outside the shell; contextual/emotional modulation.
- **Hippocampus (subiculum)** — projects primarily to the VS shell; spatial/contextual input.
- **Thalamus** — relay for basal ganglia output back to cortex; also provides direct glutamatergic input to striatum.

---

### Mechanistic insight

The paper does not fully meet the bar as defined. It is a review that synthesises anatomical tracing, physiology, and imaging — it does not present a formalised algorithm and does not provide neural data directly pitting one algorithm against alternatives. Nevertheless, the striato-nigro-striatal spiral comes close to an implementational mechanism:

- **Computational**: the brain must transfer motivational salience and value signals computed in limbic circuits into action-selection processes implemented in motor circuits; the basal ganglia solve the problem of routing incentive drive to appropriate motor outputs.
- **Algorithmic**: information is passed serially through cascaded striatal-midbrain loops, each loop providing both reciprocal feedback and nonreciprocal feedforward signals to the next functional tier; convergence zones allow combinatorial weighting of inputs from multiple prefrontal regions.
- **Implementational**: the anatomy of the dorsal-tier/ventral-tier DA cell organisation, together with inverse dorsal-ventral topographies of striatal afferents and efferents to midbrain, instantiates the spiral. The differential ratios of afferent/efferent connectivity (VS influences many DA cells but is modulated by few; dorsolateral striatum is the opposite) are specified at the level of identified cell groups.

The limitation is that the paper synthesises anatomical evidence for this architecture but does not provide direct physiological data (e.g., electrophysiology or optogenetic activation/silencing) demonstrating that the spiral specifically mediates cross-domain influence in behaving animals.

---

### Limitations & open questions

- The review is largely anatomical; the functional significance of convergence zones is inferred from connectivity rather than demonstrated by experiments manipulating these specific loci.
- The striosome/matrix compartmental organisation of the striatum — a well-documented histochemical feature — remains poorly integrated into the functional framework presented; its role in integration vs. segregation is acknowledged as unresolved.
- Most primary tracing data come from nonhuman primates; while human diffusion MRI is cited as convergent, tractography cannot resolve fine-scale convergence patterns at the level of individual terminal fields.
- How the two organisational principles (parallel channels and integrative hubs) are dynamically balanced — and under what conditions one dominates — is not addressed.
- The mechanisms by which fast-spiking interneurons weight or gate convergent cortical inputs onto MSNs are not worked out in detail.
- Clinical implications (addiction, OCD, Parkinson, schizophrenia) are mentioned but not developed.

---

### Connections & keywords

**Key citations:**
- Alexander & Crutcher (1990) — parallel processing model of basal ganglia circuits
- Haber, Fudge & McFarland (2000, J Neurosci) — striato-nigro-striatal ascending spiral
- Haber, Kim, Mailly & Calzavara (2006, J Neurosci) — reward-related cortical inputs and striatal interface zones
- Averbeck, Lehman, Jacobson & Haber (2014, J Neurosci) — probabilistic estimates of corticostriatal projection overlap
- Selemon & Goldman-Rakic (1985) — longitudinal topography of corticostriatal projections in rhesus monkey
- Draganski et al. (2008) — human diffusion MRI evidence for basal ganglia connectivity
- Schultz (1998) — predictive reward signal of dopamine neurons

**Named models or frameworks:**
- Parallel cortico-subcortical channels model (Alexander & Crutcher)
- Striato-nigro-striatal ascending spiral (Haber et al.)
- Direct and indirect pathways of the basal ganglia
- Hyperdirect pathway (frontal cortex → STN)

**Brain regions:**
- Ventral striatum, nucleus accumbens (shell, core), caudate nucleus, putamen, dorsal striatum
- vmPFC, OFC, dACC, dPFC, premotor cortex, motor cortex
- Substantia nigra pars compacta (SNc), VTA, retrorubral group
- GPe, GPi, ventral pallidum (VP), STN
- Amygdala (basolateral group), hippocampus (subiculum), thalamus

**Keywords:**
- corticostriatal topography
- striatal functional integration
- ventral striatum reward circuitry
- striato-nigro-striatal spiral
- prefrontal-striatal convergence
- medium spiny neurons
- midbrain dopamine dorsal/ventral tier
- basal ganglia parallel vs. integrative processing
- goal-directed behavior neural architecture
- limbic-to-motor information transfer
- nucleus accumbens shell/core
- primate tract-tracing anatomy
