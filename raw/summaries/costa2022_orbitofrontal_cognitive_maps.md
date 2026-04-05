---
source_file: costa2022_orbitofrontal_cognitive_maps.md
title: "The role of the lateral orbitofrontal cortex in creating cognitive maps"
authors: Kauê Machado Costa, Robert Scholz, Kevin Lloyd, Perla Moreno-Castilla, Matthew P. H. Gardner, Peter Dayan, Geoffrey Schoenbaum
year: 2022
journal: Nature Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Chemogenetic inactivation of the lateral orbitofrontal cortex (lOFC) during initial Pavlovian conditioning—not at the time of decision-making—impairs the specificity (but not the existence) of subsequent cognitive maps, revealing that the lOFC is a cartographer rather than a reader of cognitive maps, with its selective role being the precise assignment of credit to distinct cue–outcome associations.

---

### Background & motivation

The lOFC is widely implicated in model-based behaviour, but its precise role is contested. The dominant view holds that the lOFC supports decision-making by using pre-formed cognitive maps to simulate outcomes at the moment of choice, functioning as a specialised working memory for mental simulation. An alternative hypothesis proposes that the lOFC is instead a "cartographer"—critical for constructing and modifying maps during learning, not merely reading them at decision time. Prior devaluation experiments requiring lOFC at the probe test were confounded: the probe itself demands map integration, making it impossible to dissociate map creation from map use. This paper provides the first direct test of whether lOFC is necessary specifically during initial map formation.

---

### Methods

- **Subjects**: Male Long-Evans rats; hM4d group (n = 15) and mCherry control group (n = 13); all food-restricted.
- **Chemogenetics**: Bilateral AAV8-CaMKIIa-hM4d-mCherry (DREADD) or control virus infused into lOFC. High-potency agonist JH60 (0.2 mg/kg i.p.) administered before each conditioning session to inactivate lOFC principal neurons transiently and selectively only during conditioning.
- **Task (outcome-specific devaluation)**:
  1. *Conditioning phase* (8 sessions, lOFC inactivated in hM4d group): two auditory cues (A and B) each predicted delivery of a distinct flavoured pellet (banana or bacon).
  2. *Devaluation*: conditioned taste aversion (CTA) using LiCl to devalue the outcome associated with cue B; lOFC not inactivated.
  3. *Devaluation probe*: cues presented without reward; lOFC not inactivated. Outcome-specific responding tested.
- **Control task**: Object recognition task (subset, n = 9 CTRL, n = 10 hM4d) with lOFC inactivated during sample phase—to rule out perceptual, memory, or context-dependent learning confounds.
- **Computational modelling**: Model-based reinforcement learning (RL) algorithm fitted to behavioural data from all task phases. An *imprecision parameter* (χ) was introduced to capture the degree to which credit assignment spreads across cue–outcome pairs during conditioning. An alternative model incorporating model-free learning was also tested for comparison.
- **Analysis**: Two-way and three-way ANOVAs with post-hoc tests; linear regression for parameter–behaviour correlations; parameter recoverability simulations.

---

### Key findings

- **lOFC inactivation during conditioning disrupts devaluation probe performance**: Control rats showed the expected outcome-specific devaluation (responding more to cue A than cue B); hM4d rats responded equally to both cues (group × cue interaction: F₁,₂₆ = 8.013, p = 0.009), confirming lOFC is needed during map creation, not just map use.
- **Effect is generalised devaluation, not complete map failure**: hM4d rats did not respond high to both cues (which would indicate model-free residual); instead they showed generalised (non-specific) devaluation—responding comparably to both cues at a reduced level. This is inconsistent with a full loss of model-based control.
- **CTA acquisition was identical across groups**: Both groups selectively reduced consumption of the LiCl-paired pellet, ruling out lOFC involvement in devaluation learning itself.
- **Object recognition was unaffected**: lOFC inactivation during the sample phase did not impair novel object discrimination at 24 h or 48 h, ruling out perceptual confusion, accelerated forgetting, or context-dependent learning as explanations.
- **Model-based/model-free shift hypothesis rejected**: Fitting a mixed model-based + model-free architecture required addition of a forgetting parameter and produced unreliable parameter recovery; it did not improve mechanistic interpretability and was discarded.
- **Imprecision model fits the data**: A model-based RL model with imprecision parameter χ (which spreads credit updates proportionally across incorrect cue–outcome pairs during conditioning) reproduced all behavioural results. χ was significantly higher in hM4d model fits (p = 0.027) and strongly negatively correlated with differential probe responding (r² = 0.79, p < 0.0001). The value-adjustment parameter ∇pell2cue (capturing asymptotic conditioning performance) was dissociated from probe effects, confirming the two phenomena are orthogonal.
- **Model generalises to an independent dataset**: The imprecision model reproduced the results of an independent study (Sias et al. 2021) in which lOFC terminal inactivation in basolateral amygdala during Pavlovian conditioning impaired specific PIT.

---

### Computational framework

**Model-based reinforcement learning with uncertain state identity (imprecision parameter)**

The paper uses a model-based RL framework in which the agent maintains:
- A state-value distribution for each state s, parameterised as a normal-gamma distribution (mean m_s, precision ρ²_s, with hyperparameters λ_s, α_s, β_s), enabling representation of value uncertainty.
- A state-transition matrix T, where each row is a multinomial distribution over successor states, updated by observed transitions.

The key variable is the *imprecision parameter χ* (0 ≤ χ), which controls how much a received outcome (e.g., banana pellet after cue A) also updates the value of the alternative cue–outcome association (e.g., cue B → banana). When χ = 0, updates are perfectly cue-specific; when χ is large, both cue associations are updated partially after any single outcome, blurring the map. This models a failure of *state identity credit assignment*—the agent still builds a model, but cannot cleanly attribute which outcome belongs to which cue.

The framework assumes a unified model-based learning system (not a mixture of model-based and model-free); model-free learning was tested as an alternative hypothesis (hypothesis b) but rejected on both model-fit and parameter-recovery grounds.

---

### Prevailing model of the system under study

The dominant account of lOFC function, strongly supported by devaluation experiments across species, was that the lOFC acts as a form of specialised working memory enabling mental simulation of outcomes *at the time of decision-making*. On this view, the lOFC reads pre-formed cognitive maps stored elsewhere, and its disruption at the probe test leaves behaviour under model-free (habit-like) control. The lOFC was not considered necessary during initial learning, because map formation was thought to occur in other structures (e.g., amygdala, striatum). A competing proposal—the "orbitofrontal cartographer" hypothesis (Gardner & Schoenbaum 2021)—had accumulated indirect support from studies showing lOFC necessity in tasks requiring map acquisition or updating, but a direct test during the conditioning phase of a standard devaluation paradigm had not been performed.

---

### What this paper contributes

The paper establishes that the lOFC is necessary during initial map *construction*, not merely at the moment of decision. Crucially, it also refines the cartographer hypothesis: lOFC loss does not eliminate model-based learning but degrades its *specificity*. The paper introduces the concept of *credit assignment precision* as the lOFC's selective contribution—the lOFC determines how granular or segregated the states in a cognitive map are, i.e., whether an agent encodes "cue A → banana" and "cue B → bacon" as separate states or collapses them into the undifferentiated "auditory cue → food pellet." This is framed as a state-space segmentation problem rather than a value-representation or simulation problem. The results also challenge the ubiquity of model-free control: the absence of habit-like responding after lOFC disruption suggests that most learning may be model-based by default, with map resolution determined by circuit engagement and task demands rather than the engagement of a separate model-free system.

---

### Brain regions & systems

- **Lateral orbitofrontal cortex (lOFC)** — the primary target of chemogenetic manipulation; proposed here to contribute specifically to state identity credit assignment during cognitive map construction, enabling granular separation of cue–outcome associations. Previously interpreted as required for mental simulation at decision time; this paper recasts it as a cartographer active during learning.
- **Basolateral amygdala (BLA)** — mentioned as a downstream target of lOFC projections (via Sias et al. 2021), relevant for encoding and retrieval of detailed reward memories in the context of specific PIT; not directly manipulated in this study but implicated through computational model replication.
- **Primary auditory cortex** — cited as a site where OFC activity induces learning-dependent changes in representational specificity, consistent with the lOFC's proposed role in sculpting sensory representations during map formation.

---

### Mechanistic insight

This paper meets both criteria for the high bar: it formalises an algorithm (credit assignment precision via the χ parameter in a model-based RL framework) and provides neural data (chemogenetic manipulation of lOFC principal neurons) that specifically support this algorithm over alternatives (model-free takeover, perceptual confusion, value-estimation failure).

**Computational (Marr level 1)**: The brain must construct cognitive maps that assign specific outcomes to specific cues in order to support flexible, inference-based decision-making under changed conditions. The problem is determining how finely to segregate states given uncertain or partially overlapping sensory evidence.

**Algorithmic (Marr level 2)**: The lOFC implements (or contributes to) state identity credit assignment during learning—it regulates χ, the parameter governing how selectively credit (value updates and transition updates) is assigned to the correct cue–outcome pair. When lOFC is active, χ ≈ 0 and the map is specific; when lOFC is inactivated, χ > 0 and credit bleeds across associations, producing a coarser, generalised map. The agent still uses a model-based system; it simply operates over a less precise state space.

**Implementational (Marr level 3)**: The manipulation targeted CaMKII-expressing (putative pyramidal/principal) lOFC neurons via Gi-coupled hM4d DREADDs activated with the high-potency agonist JH60. This confirms that it is excitatory lOFC output (not interneurons or passing fibres) that is required. The paper speculates that the lOFC controls state separation by gating whether ambiguous or hidden states are kept distinct or collapsed—a process that may act via lOFC projections to auditory cortex and amygdala to modulate the specificity of sensory representations and associative encoding. However, the precise synaptic or circuit-level implementation of the χ parameter is not directly resolved.

*Bonus*: The paper explicitly identifies CaMKIIa+ (principal neuron) lOFC activity as the relevant cell class, providing one level of implementational specificity.

---

### Limitations & open questions

- **Male rats only**: Female rats were excluded due to pandemic-related logistical issues; whether sex differences exist in lOFC's role in map construction is unresolved.
- **Single cohort**: The experiment was conducted in one cohort, limiting assessment of reproducibility across cohorts.
- **Unblinded experimenters**: Investigators were not blinded to group allocation during behavioural sessions (though the novel object scoring was independently blinded).
- **Species and subregion differences**: Results may not straightforwardly translate to primates; in macaques, credit assignment has been recently attributed to ventrolateral PFC rather than OFC (areas 11/13). Whether these represent species differences, task differences (Pavlovian vs. instrumental choice), or value-dependent vs. value-independent learning contexts is unresolved.
- **Interpretation of χ**: The paper favours the interpretation that lOFC controls the *granularity* of state representations rather than directly controlling error signal assignment, but the paper acknowledges these are difficult to dissociate behaviourally.
- **Predictive value of lOFC hypo- vs. hyperfunction**: The paper proposes that lOFC hypofunction (substance use disorder, neurodegeneration) leads to overly generalised maps, while hyperfunction (OCD, paranoid psychosis) leads to over-segregated maps—a clinically important but as-yet untested prediction.
- **lOFC vs. medial PFC in rodents**: Whether the rat medial PFC plays an overlapping or complementary role in state credit assignment is unresolved.
- **What determines χ in the intact system**: The paper raises the possibility that task demands and learning context (rather than experimental intervention) normally regulate map granularity, but this is speculative.

---

### Connections & keywords

**Key citations**:
- Behrens et al. (2018) *Neuron* — cognitive maps framework
- Gardner & Schoenbaum (2021) *Behav. Neurosci.* — orbitofrontal cartographer hypothesis
- Wilson et al. (2014) *Neuron* — OFC as cognitive map of task space
- Schuck et al. (2016) *Neuron* — human OFC represents state space
- Daw, Niv & Dayan (2005) *Nat. Neurosci.* — model-based/model-free competition
- Hart et al. (2020) *eLife* — sensory preconditioning requires lOFC during cue-cue learning
- Sias et al. (2021) *eLife* — lOFC-BLA projections and specific PIT
- Dezfouli & Balleine (2019) *PLoS Comput. Biol.* — state-space and action representations in multistage decisions
- Gershman & Niv (2010) *Curr. Opin. Neurobiol.* — learning latent structure
- Walton et al. (2010) *Neuron* — separable learning systems in macaque, OFC and contingent learning

**Named models or frameworks**:
- Orbitofrontal cartographer hypothesis (Gardner & Schoenbaum 2021)
- Model-based reinforcement learning with imprecision parameter (χ) — novel model presented here
- Normal-gamma Bayesian Q-learning (Dearden, Friedman & Russell 1998)
- hM4d DREADD chemogenetics with JH60 (Bonaventura et al. 2019)
- Outcome-specific devaluation (reinforcer devaluation via CTA)
- Pavlovian-to-instrumental transfer (PIT)

**Brain regions**:
- Lateral orbitofrontal cortex (lOFC)
- Basolateral amygdala (BLA)
- Primary auditory cortex

**Keywords**:
- cognitive map construction
- lateral orbitofrontal cortex
- credit assignment precision
- state identity segmentation
- outcome-specific devaluation
- model-based reinforcement learning
- chemogenetics, DREADD
- Pavlovian conditioning
- conditioned taste aversion
- state-space granularity
- orbitofrontal cartographer
- cue–outcome association specificity
