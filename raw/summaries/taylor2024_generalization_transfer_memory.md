---
source_file: "taylor2024_generalization_transfer_memory.md"
paper_id: "taylor2024_generalization_transfer_memory"
title: "How do we generalize?"
authors: "Jessica Elizabeth Taylor, Aurelio Cortese, Helen C Barron, Xiaochuan Pan, Masamichi Sakagami, Dagmar Zeithamova"
year: 2024
journal: "Journal of Neuroscience Research"
paper_type: "review"
contribution_type: "review"
species: ["human"]
brain_regions: ["hippocampus", "entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "ventromedial_prefrontal_cortex", "striatum"]
frameworks: ["tolman_eichenbaum_machine"]
keywords: ["mcclelland", "mcnaughton_and_oreilly_1995_complementary_learning_systems_theory", "eichenbaum_1999_memory_integration_theory", "kumaran_and_mcclelland_2012_remerge_model", "ashby_and_colleagues_covis_model", "decision_bound_theory", "pan", "sakagami_et_al_2008", "2014_functional_category_reward_prediction_task", "zeithamova", "preston_et_al_memory_integration_and_generalization_studies", "barron", "dolan_and_behrens_2013_online_evaluation_of_novel_choices", "schlichting_and_preston_hippocampal_memory_integration", "named_models_or_frameworks", "complementary_learning_systems_theory", "memory_integration_theory", "remerge_recurrency_and_episodic_memory_results_in_generalization", "covis_competition_between_verbal_and_implicit_system", "prototype_models_of_categorization"]
---

### One-line summary

This Generative Adversarial Collaboration synthesizes multiple theoretical accounts of generalization, concluding that memory integration, on-the-fly computation, and offline consolidation mechanisms likely coexist and operate under different conditions rather than being mutually exclusive.

### Background & motivation

Generalization—the ability to transfer information from past experiences to novel situations—is fundamental to adaptive behavior but has been studied across disparate fields (psychology, neuroscience, machine learning) using different terminology and tasks. This paper emerged from a Generative Adversarial Collaboration (GAC) that initially sought to arbitrate between two accounts: (1) generalization through integration of experiences into summary representations versus (2) on-the-fly computation using separately stored individual memories. The collaboration revealed that these mechanisms are likely complementary rather than competing.

### Methods

- **Approach**: Synthetic review and theoretical integration from a multi-lab collaboration
- **Scope**: Integration of literatures on categorization, episodic inference, and memory consolidation across humans, non-human primates, and rodents
- **Analytical framework**: Comparison of proposed generalization mechanisms and identification of barriers to synthesis

### Key findings

- **Multiple mechanisms coexist**: Complementary learning systems (hippocampal fast learning vs. cortical/striatal slow statistical learning), memory integration (hippocampal-mPFC), on-the-fly generalization through memory co-activation (REMERGE model), offline generalization during sleep/rest (sharp-wave ripples), and rule-based generalization (decision bound theory) are all likely valid under different conditions.

- **Representational formats vary**: Similar experiences tend to be integrated into generalized representations (prototypes), while dissimilar experiences remain as separate exemplars; temporal proximity and within-category coherence bias toward integration.

- **Neural systems show parallel organization**: The anterior hippocampus and mPFC represent coarser, integrated information while the posterior hippocampus and LPFC represent finer-grained, specific information.

- **Task terminology creates fragmentation**: "Similarity-based generalization," "relational generalization," and "rule-based generalization" may describe overlapping phenomena studied under different names in different fields; episodic inference tasks and categorization tasks may share underlying mechanisms despite surface differences.

- **Species and methodology differences create gaps**: Rodent studies focus on cellular mechanisms in targeted regions; human studies use whole-brain imaging with coarser resolution; non-human primate studies bridge these but with limited regional sampling.

### Computational framework

The paper discusses multiple computational frameworks rather than proposing a single model:

- **Complementary learning systems**: Fast hippocampal learning of individual episodes vs. slow cortical/striatal statistical learning of regularities (connectionist models)

- **REMERGE model**: Recurrent network where generalization emerges from on-the-fly co-activation of separately stored episodic memories through pattern completion

- **Prototype vs. Exemplar models**: Mathematical models of categorization assuming generalization from abstracted prototypes versus stored exemplars; these serve as indices of integrated versus separate memory representations

- **Decision bound theory**: Framework from categorization research where generalization arises from learned boundaries in perceptual space

- **Predictive cognitive maps**: Grid cell and place cell-based representations that organize relational knowledge into structured maps supporting flexible inference

### Prevailing model of the system under study

Before this synthesis, the field largely treated different forms of generalization as dissociable phenomena supported by distinct neural systems. The complementary learning systems framework dominated explanations of how both specific memory and generalization coexist, positing a division between hippocampal (specific) and cortical/striatal (generalized) representations. Memory integration theory offered an alternative hippocampal-centric view for rapid generalization through online integration. On-the-fly and offline mechanisms were often treated as competing rather than complementary accounts. The categorization literature operated largely independently from the episodic memory literature, with debates about prototype vs. exemplar representations not clearly connected to hippocampal function.

### What this paper contributes

This paper establishes that multiple generalization mechanisms likely operate simultaneously, in parallel, or under different conditions rather than being mutually exclusive alternatives. It identifies specific barriers to synthesis in the generalization literature: inconsistent terminology (different terms for similar phenomena, same terms for different phenomena), species differences in methodology and regional focus, and task design variations that obscure whether common or distinct mechanisms are engaged. The paper proposes three concrete research directions: (1) large-N individual differences studies to test whether different generalization tasks measure common underlying abilities; (2) human fMRI studies of functional categorization to bridge monkey LPFC findings with human hippocampal literature; (3) causal manipulations in monkeys to test necessity of hippocampus vs. LPFC for functional categorization. The synthesis reveals that prototype/exemplar model predictions can serve as indices of integrated vs. separate memory representations, offering a quantitative bridge between categorization and episodic memory research.

### Brain regions & systems

- **Hippocampus**: Fast encoding of individual episodes; memory integration through overlapping representations; anterior hippocampus represents coarser/integrated information, posterior hippocampus represents finer-grained/specific information; sharp-wave ripples support offline integration during rest/sleep

- **Medial prefrontal cortex (mPFC) / Ventromedial prefrontal cortex (VMPFC)**: Represents integrated, generalized information; interacts with hippocampus during memory integration and generalization; involved in prototype-based categorization

- **Lateral prefrontal cortex (LPFC)**: Represents specific, fine-grained information; codes functional categories in monkeys; codes abstract category information and flexible category boundaries; integrates sensory and motor information for abstract representations

- **Striatum**: Slow incremental learning of stimulus-response mappings; represents reward predictions for category members after initial generalization has occurred; not involved in initial computation of generalization

- **Entorhinal cortex**: Contains grid cells that may support generalization through predictive cognitive maps; big-loop recurrence between deep and superficial layers supports memory integration

- **Posterior parietal cortex**: Abstract representation of category information (in primates)

### Mechanistic insight

The paper does not provide mechanistic insight at the Marr's three levels bar. As a review/synthesis paper, it discusses multiple algorithms and their neural correlates but does not itself present new neural data supporting a specific algorithm over alternatives. The paper surveys existing work where:

- **Computational level**: The problem is defined as transferring knowledge from learned experiences to novel situations, with different frameworks proposing different objective functions (statistical learning of regularities, integration of related episodes, co-activation of relevant memories)

- **Algorithmic level**: Multiple algorithms are discussed (REMERGE, complementary learning systems, memory integration, prototype/exemplar models, decision bound theory) but the paper does not arbitrate between them with new data

- **Implementational level**: Various neural implementations are surveyed (hippocampal-cortical interactions, LPFC category coding, sharp-wave ripples) but the paper does not provide new empirical evidence linking specific algorithms to specific neural mechanisms

The paper's contribution is at the level of theoretical synthesis and identification of research gaps, not mechanistic validation.

### Limitations & open questions

- **Terminology fragmentation**: Multiple terms exist for similar phenomena (e.g., "relational generalization," "transfer," "secondary stimulus generalization," "mediated stimulus generalization") and the same term "generalization" is used for different phenomena (similarity-based vs. relational vs. rule-based)

- **Unclear construct validity**: It remains unknown whether different generalization tasks measure the same underlying ability or distinct abilities; no large-N individual differences studies have tested for shared variance across episodic inference, categorization, and other generalization tasks

- **Species differences**: Difficult to determine whether discrepancies between human, monkey, and rodent findings reflect true mechanistic differences or differences in tasks, methods, and a priori regions of interest

- **Causal mechanisms**: Most evidence is correlational; causal evidence for necessity of specific regions (hippocampus vs. LPFC) for different generalization types is lacking

- **Integration vs. separation**: Conditions determining when experiences are integrated versus stored separately are not fully understood; temporal proximity, similarity, and task factors all play roles but their interactions are unclear

- **Prototype vs. exemplar representations**: Whether these represent truly distinct neural mechanisms or different points on a continuum remains debated

- **Direction of representational change**: Whether representations evolve from specific to general or general to specific over learning varies across studies and is not well understood

### Connections & keywords

**Key citations:**
- McClelland, McNaughton & O'Reilly (1995) - Complementary learning systems theory
- Eichenbaum (1999) - Memory integration theory
- Kumaran & McClelland (2012) - REMERGE model
- Ashby & colleagues - COVIS model, decision bound theory
- Pan, Sakagami et al. (2008, 2014) - Functional category reward prediction task
- Zeithamova, Preston et al. - Memory integration and generalization studies
- Barron, Dolan & Behrens (2013) - Online evaluation of novel choices
- Schlichting & Preston - Hippocampal memory integration

**Named models or frameworks:**
- Complementary learning systems theory
- Memory integration theory
- REMERGE (Recurrency and Episodic MEmory Results in GEneralization)
- COVIS (Competition between Verbal and Implicit System)
- Decision bound theory
- Prototype models of categorization
- Exemplar models of categorization
- SUSTAIN (network model of category learning)
- Predictive cognitive maps / Tolman-Eichenbaum Machine

**Brain regions:**
- Hippocampus (anterior/posterior distinction)
- Medial prefrontal cortex (mPFC)
- Ventromedial prefrontal cortex (VMPFC)
- Lateral prefrontal cortex (LPFC)
- Striatum
- Entorhinal cortex
- Posterior parietal cortex

**Keywords:**
generalization, transfer, memory integration, complementary learning systems, episodic inference, categorization, hippocampus, prefrontal cortex, prototype, exemplar, relational generalization, similarity-based generalization, sharp-wave ripples, functional categories, generative adversarial collaboration
