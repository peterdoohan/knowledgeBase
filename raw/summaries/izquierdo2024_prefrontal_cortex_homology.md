---
source_file: "izquierdo2024_prefrontal_cortex_homology.md"
paper_id: "izquierdo2024_prefrontal_cortex_homology"
title: "A Cross-Species Analysis of Prefrontal Cortex Homology Based on Anatomical Connectivity, Behavior, and Cell Types"
authors: "Alicia Izquierdo"
year: 2024
journal: "The Frontal Cortex: Organization, Networks, and Function (Str\u00fcngmann Forum Reports, vol. 34, MIT Press)"
paper_type: "review"
contribution_type: "review"
species: ["mouse", "rat", "human", "macaque"]
tasks: ["foraging_task"]
methods: ["calcium_imaging", "optogenetics"]
brain_regions: ["prefrontal_cortex", "anterior_cingulate_cortex", "orbitofrontal_cortex", "dorsolateral_prefrontal_cortex", "prelimbic_cortex", "infralimbic_cortex", "striatum", "thalamus", "mediodorsal_thalamus", "amygdala"]
frameworks: ["mixed_selectivity"]
keywords: ["heilbronner_et_al_2016_cortico_striatal_connectivity_homology_in_rat_and_macaque", "van_heukelum_et_al_2020_acc_connectivity_meta_analysis_across_species", "a_p_parcellation", "krienen_et_al_2020_scrna_seq_of_interneurons_across_primates_and_mouse", "hodge_et_al_2019_scrna_seq_comparing_mouse_and_human_cortical_cell_types", "kozlenkov_et_al_2020_gene_regulatory_elements_in_glu_gaba_neurons_across_primates", "rudebeck_and_izquierdo_2022_foraging_innovations_framework", "laubach_et_al_2018_survey_of_rodent_frontal_cortex_nomenclature_and_publication_trends", "kepecs_and_fishell_2014_interneuron_diversity_and_combinatorial_complexity", "rigotti_et_al_2013_mixed_selectivity_and_high_dimensional_representations_in_pfc", "fusi_et_al_2016_mixed_selectivity_in_pfc", "uylings_et_al_2003_five_criteria_framework_for_cross_species_pfc_comparison", "named_models_or_frameworks", "foraging_innovations_framework_rudebeck_and_izquierdo_2022_prediction", "evaluation", "action", "social_cognition", "optimal_foraging_theory_marginal_value_theorem_charnov_1976", "phylogenetic_refinement_cisek_2019", "rose_and_woolsey_cytoarchitectonic_criterion_for_pfc"]
key_citations: ["fusi2016_mixed_selectivity_cognition"]
---

### One-line summary

This review synthesises evidence across connectivity, foraging behavior, and transcriptomic cell-type data to argue that rodent and primate PFC share conserved agranular connectivity motifs but diverge substantially in interneuron specialisation and laminar cell-type organisation, with rodents lacking the granular PFC expansions that support prediction-based and valueless-reward representations in primates.

---

### Background & motivation

A steep rise in mouse PFC publications over the past two decades has made it urgent to clarify which aspects of rodent frontal cortex genuinely translate to primate PFC. The classical definition of PFC hinges on the presence of a granule-cell Layer IV — a criterion rodents fail by default — yet researchers frequently treat rodent medial frontal cortex as a PFC homologue without systematically examining the basis for that claim. This chapter addresses the gap by reviewing what connectivity patterns, foraging-based behavioral criteria, and emerging transcriptomic cell-type data can and cannot tell us about cross-species homology, and proposes that cell-type information must be integrated with connectivity and behavior to resolve persistent ambiguities.

---

### Methods

This is a narrative review of the comparative neuroscience literature. Scope and approach:

- Coverage spans anatomical connectivity tracing studies (anterograde viral tracers in rat and macaque), diffusion tensor imaging in humans, and single-cell/single-nucleus RNA sequencing (scRNA-Seq / snRNA-Seq) in rodent and primate.
- Inclusion is structured around Uylings et al.'s (2003) five-criteria framework for cross-species PFC comparisons, with primary emphasis on criterion 2 (connectivity) and criterion 5 (functional/behavioral properties).
- Behavioral comparisons draw on optimal foraging theory and the "foraging innovations" framework developed in Rudebeck and Izquierdo (2022), categorising PFC functions as Evaluation, Prediction, Action, and Social cognition.
- The chapter also reports original empirical findings from the author's own lab (LFP theta recordings during reversal learning; DREADD + calcium imaging studies of ACC pyramidal neurons in rats) as illustrative data points, but the primary contribution is synthetic.

---

### Key findings

- Agranular OFC and ACC connectivity with striatum, amygdala, hippocampus, hypothalamus, and thalamus is largely conserved across rat and macaque (Heilbronner et al. 2016; van Heukelum et al. 2020), with anterior–posterior parcellation (not dorsal–ventral) providing the best cross-species alignment.
- Rodent frontal cortex is completely agranular; primate PFC uniquely contains granular areas (e.g., lateral and dorsolateral PFC, area 46) that support visual representations of "valueless" reward unavailable in rodents.
- Primate PFC has significantly higher proportions of interneurons relative to V1 than rodent, with more specialised spatial expression gradients for interneuron marker genes (Sst, Pvalb, Vip, Lamp5) across PFC vs. V1 — a specialisation in expression, not origin (Krienen et al. 2020).
- Gene regulatory elements in glutamatergic and GABAergic cell subtypes diverge more across species than shared-type GREs, with the most divergent gene families being neurotransmitter receptors (especially serotonin), ion channels, and cell adhesion molecules — likely impacting microcircuit function and possibly contributing to translation failures in preclinical work (Hodge et al. 2019).
- Rat frontal cortex subregions show less functional specialisation than primate: OFC and ACC exhibit redundant theta-band signals during reversal learning (Ye et al. 2023b) and both impair confidence reporting when inhibited (Stolyarova et al. 2019), contrasting with the OFC/ACC division of labour for stimuli vs. actions seen in primates.
- Bidirectional DREADD manipulation of ACC pyramidal neurons (CaMKII promoter) in rats impaired effort-based choice whether population activity was increased or decreased, and population-level calcium activity (not single cells) was the best predictor of choice — consistent with a role for E/I balance in value computation.
- Primate cortical evolution favoured clustering of cell types; mouse L3 pyramidal neurons are morphologically homogeneous across areas, whereas macaque L3 lateral PFC neurons are substantially larger with different dendritic topology compared to macaque V1.

---

### Computational framework

Not applicable in a strict sense — the paper does not develop or apply a computational model. However, the review implicitly invokes a framework of **dimensionality and mixed selectivity**: interneuron diversity is framed as enabling high-dimensional neural representations (Rigotti et al. 2013; Fusi et al. 2016) and combinatorial complexity, providing the E/I balance required for adaptive PFC function. The foraging innovations framework (Evaluation, Prediction, Action) maps loosely onto learning-theoretic categories (stimulus, outcome, action) and serves as an organising schema for comparing species differences in PFC function. Results could constrain models of how interneuron diversity supports representational capacity and flexible credit assignment across species.

---

### Prevailing model of the system under study

The field's starting point, as described in the paper's introduction, is the cytoarchitectonic criterion: PFC is defined by the presence of a granule-cell Layer IV (L4), and on this strict criterion rodents lack a PFC homologue. Despite this, researchers have widely treated rodent medial frontal cortex (prelimbic, infralimbic, anterior cingulate) as functionally equivalent to primate PFC, partly because mouse studies are far more tractable and partly because connectivity and behavioural data offer partial support for homology. The prevailing working model thus holds that there is sufficient functional and anatomical similarity between rodent agranular frontal cortex and primate agranular areas (ACC, caudal OFC) to justify cross-species translation, while acknowledging uncertainty about how far this extends to granular primate PFC. The paper explicitly engages with and refines this "partial homology" view.

---

### What this paper contributes

The review consolidates cross-species comparisons across three distinct dimensions (connectivity, foraging behavior, cell types) and arrives at a more nuanced account than either "rodent PFC is homologous" or "there is no homologue":

- Agranular ACC and OFC connectivity is genuinely conserved and provides a valid cross-species anchor, particularly when parcellated along the anterior–posterior axis.
- The foraging innovations framework provides principled behavioral predictions: rodent frontal cortex should be most comparable to primate for action-selection and evaluation functions, but substantially less so for prediction and long-range planning that depend on granular PFC and expanded visual representations.
- Cell-type data reveal that primate PFC interneuron specialisation (in proportion and expression gradients, not origin) goes well beyond what rodent models capture, and that microcircuit divergence in neurotransmitter receptors and ion channels is likely functionally significant — with potential implications for why preclinical rodent findings fail to translate therapeutically.
- The key unresolved questions the review identifies are: (a) how transcriptomically defined cell types map onto functional signals (task-related activity) and connectivity motifs across species, (b) whether spatial cell-type gradients in mouse frontal cortex generalise to rat and NHP, and (c) how to systematically integrate scRNA-Seq data with behaviour and connectivity in a comparative framework.

---

### Brain regions & systems

- **Prefrontal cortex (PFC)** — central focus; cross-species comparisons of homology in agranular vs. granular subdivisions.
- **Orbitofrontal cortex (OFC), agranular (area 13 / caudal OFC)** — conserved connectivity with striatum and amygdala across species; proposed locus of stimulus value and reversal learning.
- **Anterior cingulate cortex (ACC; areas 24, 25, 32)** — conserved agranular area with autonomic and limbic connectivity; functionally less specialised in rat than primate; role in action selection and effort-based choice.
- **Prelimbic (PL) and Infralimbic (IL) cortex** — rodent agranular areas mapped to primate areas 32 and 25 respectively; role in goal-directed vs. habitual behaviour.
- **Midcingulate cortex (MCC)** — primate-expanded region whose growth is proposed to displace ACC rostrally and ventrally, contributing to cortical folding.
- **Lateral / dorsolateral PFC (area 46)** — granular, primate-specific; supports working memory and visual-based reward representations absent in rodent.
- **Ventrolateral PFC** — granular, primate-specific; mediates knowledge of reward availability independent of desirability.
- **Striatum** — key connectivity target used to parcellate and compare fronto-cortical circuits across species.
- **Amygdala** — conserved fronto-cortical connectivity target across species.
- **Mediodorsal thalamus** — classically used to define PFC (Rose & Woolsey criterion); receives projections from PFC across species.

---

### Mechanistic insight

The paper does not meet the high bar for mechanistic insight as defined here. It reviews and proposes, but does not itself provide neural data directly testing a specific algorithm against alternatives. The DREADD + calcium imaging studies described (Hart et al. 2020; Ye et al. 2023b; Stolyarova et al. 2019) provide relevant empirical data on population-level ACC activity and OFC/ACC theta signals, but these are cited to illustrate species differences in specialisation, not to adjudicate between algorithmic-level accounts of how a specific computation is implemented. The paper is primarily a synthesis arguing for why the field needs to combine cell-type transcriptomics with connectivity and task-related neural signals — a call for mechanistic studies rather than a mechanistic study itself.

---

### Limitations & open questions

- Most transcriptomic studies reviewed compare mouse (sometimes rat) with human or macaque; thorough rat–macaque comparisons are lacking, which is a gap given that the most theory-driven pathway-dissection work has been done in rats.
- The mouse tissue in Hodge et al. (2019) was from V1 and anterior lateral motor cortex, not PFC — limiting conclusions about PFC-specific cell-type divergence.
- No transcriptomic atlas exists for macaque PFC; a marmoset CNS atlas (Lin et al. 2022) is available but NHP coverage is incomplete.
- CaMKII and synapsin promoters used in DREADD studies transduce both excitatory and inhibitory neurons more than previously assumed, complicating cell-type-specific interpretation.
- Studies combining molecularly defined cell-type information with task-related electrophysiology or calcium imaging across species are rare; this is identified as the key methodological gap.
- The Allen Brain Atlas lacks rat connectomics, which the author identifies as a missed opportunity.
- Optogenetic efficacy for studying higher-order cognitive function in NHPs remains uncertain.
- The foraging innovations framework (Prediction, Evaluation, Action) is theoretically motivated but the mapping from these categories to specific PFC subregions remains underspecified.

---

### Connections & keywords

**Key citations:**
- Heilbronner et al. (2016) — cortico-striatal connectivity homology in rat and macaque
- van Heukelum et al. (2020) — ACC connectivity meta-analysis across species, A-P parcellation
- Krienen et al. (2020) — scRNA-Seq of interneurons across primates and mouse
- Hodge et al. (2019) — scRNA-Seq comparing mouse and human cortical cell types
- Kozlenkov et al. (2020) — gene regulatory elements in Glu/GABA neurons across primates
- Rudebeck and Izquierdo (2022) — foraging innovations framework
- Laubach et al. (2018) — survey of rodent frontal cortex nomenclature and publication trends
- Kepecs and Fishell (2014) — interneuron diversity and combinatorial complexity
- Rigotti et al. (2013) — mixed selectivity and high-dimensional representations in PFC
- Fusi et al. (2016) — mixed selectivity in PFC
- Uylings et al. (2003) — five-criteria framework for cross-species PFC comparison

**Named models or frameworks:**
- Foraging innovations framework (Rudebeck and Izquierdo 2022): Prediction, Evaluation, Action, Social cognition
- Optimal foraging theory / marginal value theorem (Charnov 1976)
- Phylogenetic refinement (Cisek 2019)
- Rose and Woolsey cytoarchitectonic criterion for PFC
- DREADDs (designer receptors exclusively activated by designer drugs)
- MAPSeq (multiplexed analysis of projections by sequencing)
- Single-cell RNA sequencing (scRNA-Seq) / single-nucleus RNA-Seq (snRNA-Seq)

**Brain regions:**
Prefrontal cortex, orbitofrontal cortex (OFC), anterior cingulate cortex (ACC), prelimbic cortex, infralimbic cortex, midcingulate cortex (MCC), lateral PFC, dorsolateral PFC, ventrolateral PFC, striatum, amygdala, mediodorsal thalamus, inferior temporal cortex, perirhinal cortex, nucleus accumbens

**Keywords:**
cross-species PFC homology, prefrontal cortex cytoarchitecture, agranular cortex, interneuron specialisation, single-cell transcriptomics, cortico-striatal connectivity, foraging innovations, phylogenetic refinement, mixed selectivity, excitatory-inhibitory balance, granular vs. agranular PFC, rodent-primate translation
