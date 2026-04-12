---
source_file: "panteleeva2020_hunting_behavior_rodents.md"
paper_id: "panteleeva2020_hunting_behavior_rodents"
title: "Facultative Hunting Behavior in Rodents as a Possible Evolutionarily Stable Strategy"
authors: "S.N. Panteleeva, J.V. Levenets, Zh.I. Reznikova"
year: 2020
journal: "Biology Bulletin Reviews"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
tasks: ["foraging_task"]
brain_regions: ["amygdala"]
keywords: ["maynard_smith_and_price_1973_ess_theory_foundation", "eisenberg_and_leyhausen_1972_phylogenesis_of_predatory_behavior_in_mammals", "kreiter_and_timberlake_1988_predation_in_peromyscus_mice", "experience_dependence", "konczal_et_al_2016_genomic_response_to_selection_for_predatory_behavior_in_bank_voles", "han_et_al_2017_neural_control_of_predatory_hunting_by_central_amygdala", "reznikova_et_al_2017_hunting_behavior_in_field_mice", "fragmentation_of_stereotypes", "named_models_or_frameworks", "evolutionarily_stable_strategy_ess_theory", "fixed_complex_of_actions_fca_innate_releasing_mechanisms", "first_order_markov_process_for_behavioral_sequence_analysis", "leyhausen_eisenberg_framework_for_evolution_of_predatory_behavior", "brain_regions", "central_nucleus_of_the_amygdala_cited_from_han_et_al", "2017", "not_studied_here", "keywords", "facultative_hunting_behavior", "predatory_behavior"]
---

### One-line summary

Three rodent species with different dietary specializations (granivorous, herbivorous, omnivorous) possess facultative, innate hunting behavior toward mobile prey, which the authors propose represents an evolutionarily stable strategy for expanding food resource spectra.

---

### Background & motivation

While rodents are known to include invertebrates in their diet, direct observation of hunting behavior for mobile prey had been limited to a few specialized species. Most information came from stomach content analysis rather than behavioral observation. The authors sought to characterize the hunting behavior of non-specialized rodent species to understand whether facultative hunting represents a behavioral adaptation that allows dietary flexibility, and whether this could be understood through the lens of evolutionarily stable strategy (ESS) theory.

---

### Methods

- **Subjects**: Three rodent species with different dietary specializations:
  - Striped field mouse (*Apodemus agrarius*, n=26) — granivorous
  - Narrow-skulled vole (*Lasiopodomys gregalis*, n=46) — herbivorous
  - Campbell's dwarf hamster (*Phodopus campbelli*, n=19) — omnivorous/euryphage
  - Common shrew (*Sorex araneus*, n=11) — insectivorous comparison species
- **Prey**: Speckled cockroaches (*Nauphoeta cinerea*) as safe mobile prey; additional experiments with red wood ants (*Formica aquilonia*) as dangerous prey for hamsters
- **Design**: Laboratory observation in transparent arenas (30×30×35 cm) with video recording (~100 hours total)
- **Analysis**: 
  - Behavioral sequences coded using Noldus Observer XT 10.1
  - First-order Markov chains for transition probabilities between behavioral elements
  - Hunting effectiveness: ratio of successful to unsuccessful attacks
  - Hunting rate: behavior elements per second
  - Statistical comparisons: Fisher's exact test, Mann-Whitney U, Kruskal-Wallis H-test with Bonferroni correction

---

### Key findings

- **Facultative hunting**: Unlike shrews where all individuals hunted (obligate), hunting in rodents was facultative — manifested completely but not in all individuals. First presentation hunting rates: field mice 65.4% (17/26), Campbell's dwarf hamsters 36.8% (7/19), narrow-skulled voles 18.5% (9/46).
- **Hunting effectiveness**: Field mice and shrews were most successful (69.2% and 62.3% successful attacks respectively), significantly higher than Campbell's dwarf hamsters (20%) and narrow-skulled voles (25.4%) (p < 0.0017).
- **Hunting rate**: Shrews hunted fastest (2.9 elements/second), significantly higher than all rodent species. Field mice: 2.1, narrow-skulled voles: 1.6, Campbell's dwarf hamsters: 1.4 elements/second.
- **Behavioral stereotype structure**: All species showed a universal stereotype structure: detection → pursuit (running or walking) → attack → prey processing → consumption. Key elements included pursuit, bite, and capture with paws (rodents only).
- **Species-specific attack patterns**: 
  - Field mice and voles: capture prey with teeth first, then with paws; immobilize with series of quick bites ("bite to death")
  - Campbell's dwarf hamsters: can initiate attack with both teeth and paws (>25% of cases); immobilize prey by biting off limbs — a more specialized hunting tactic unique among rodents studied
  - Shrews: use only teeth, no paw capture — considered more primitive
- **Innate and experience-independent**: Hunting stereotypes manifested according to "all-at-once" principle — complete from first encounter, no improvement with experience. Laboratory-born naive animals showed identical hunting behavior to wild-caught animals.
- **Evolutionarily stable strategy**: The authors propose that facultative hunting behavior in rodents represents an ESS, where the proportion of hunters in populations can vary with environmental conditions without the strategy being displaced.

---

### Computational framework

Not applicable. This is a behavioral ecology study using ethological observation methods and Markov chain analysis of behavioral sequences. The computational framework is purely descriptive/statistical rather than mechanistic or algorithmic. The results could constrain models of innate behavioral pattern generation and evolutionary game theory models of strategy frequency dynamics in populations.

---

### Prevailing model of the system under study

Prior to this work, hunting behavior in rodents was primarily studied in specialized predatory species (e.g., *Onychomys* grasshopper mice) and a few laboratory rodent models (golden hamsters, house mice, white-footed mice). The prevailing view was that: (1) hunting behavior in non-specialized rodents requires experience to develop efficiently (as shown in *Peromyscus* mice); (2) specialized predatory rodents have innate hunting behavior with morphological and physiological adaptations; (3) most rodent species consume invertebrates opportunistically based on stomach content analysis, but direct hunting behavior was not well-characterized. The field lacked systematic comparative analysis of hunting behavior across rodent species with different dietary specializations.

---

### What this paper contributes

This paper provides the first detailed experimental characterization of facultative hunting behavior in three non-specialized rodent species with different dietary niches (granivorous, herbivorous, omnivorous). Key contributions:

1. **Established facultative hunting as a behavioral phenomenon**: Unlike specialized insectivores where all individuals hunt, hunting in these rodents is facultative — manifested completely in a subset of individuals (18–65% depending on species) and not at all in others.

2. **Demonstrated innate, experience-independent expression**: Hunting stereotypes manifest according to the "all-at-once" principle — complete from first encounter with prey, with no improvement through experience. This contrasts with previous findings in *Peromyscus* mice where experience was required for efficient hunting.

3. **Characterized species-specific tactical variations**: While the overall stereotype structure is universal, species differ in attack patterns (teeth-first vs. paws-first) and prey immobilization tactics (biting vs. limb removal). Campbell's dwarf hamsters show the most specialized behavior with limb-biting.

4. **Proposed ESS framework**: The facultative nature of hunting is proposed to represent an evolutionarily stable strategy, allowing populations to maintain hunting capacity for expanding food resources without all individuals bearing the costs of predatory behavior.

---

### Brain regions & systems

Not applicable. This is a behavioral ecology study with no neural measurements. The authors reference neural control of predatory hunting in the introduction (citing Han et al., 2017 regarding central amygdala control), but no brain regions are studied in this work.

---

### Mechanistic insight

This paper does not meet the bar for mechanistic insight. It provides detailed behavioral description and quantitative analysis of hunting sequences, but:

1. **No algorithmic formalization**: While the authors use Markov chains to describe transition probabilities between behavioral elements, this is a descriptive statistical tool rather than a formalized algorithmic model of how the behavior is generated or controlled.

2. **No neural data**: The paper contains no neural recordings, imaging, lesion studies, or pharmacological manipulations. The authors cite other work on neural control of predatory behavior (central amygdala) but do not provide any new neural data themselves.

The paper provides valuable ethological description that could constrain future mechanistic models, but it does not itself formalize an algorithm or provide neural evidence for how hunting behavior is neurally implemented.

---

### Limitations & open questions

- **Laboratory conditions**: All observations were conducted in laboratory arenas, which may not fully capture natural hunting contexts.
- **Limited prey types**: Only two prey types were tested (cockroaches and ants for hamsters). Generalization to other mobile prey types is unclear.
- **Naive vs. experienced comparison**: While the authors compared laboratory-born and wild-caught field mice, they could not fully control for all environmental experiences.
- **Genetic mechanisms**: The authors propose ESS but did not conduct genetic studies to demonstrate heritability or identify genetic loci associated with hunting behavior.
- **Population-level dynamics**: The ESS hypothesis predicts frequency-dependent selection, but this was not tested in natural populations over time.
- **Neural basis**: The neural mechanisms underlying the hunting stereotype remain unknown.
- **Open question**: How do carriers of "dormant" behavioral fragments interact with complete-hunters in natural populations to enable rapid spread of hunting behavior through social learning?

---

### Connections & keywords

**Key citations:**
- Maynard Smith and Price (1973) — ESS theory foundation
- Eisenberg and Leyhausen (1972) — phylogenesis of predatory behavior in mammals
- Kreiter and Timberlake (1988) — predation in *Peromyscus* mice, experience dependence
- Konczal et al. (2016) — genomic response to selection for predatory behavior in bank voles
- Han et al. (2017) — neural control of predatory hunting by central amygdala
- Reznikova et al. (2017) — hunting behavior in field mice, fragmentation of stereotypes

**Named models or frameworks:**
- Evolutionarily Stable Strategy (ESS) theory
- Fixed Complex of Actions (FCA) — innate releasing mechanisms
- First-order Markov process for behavioral sequence analysis
- Leyhausen-Eisenberg framework for evolution of predatory behavior

**Brain regions:**
- Central nucleus of the amygdala (cited from Han et al., 2017, not studied here)

**Keywords:**
facultative hunting behavior, predatory behavior, rodent foraging, evolutionarily stable strategy, innate behavioral stereotypes, behavioral ecology, Apodemus agrarius, Lasiopodomys gregalis, Phodopus campbelli, fixed action patterns, ethology, behavioral sequence analysis, Markov chains, prey capture tactics, hunting stereotype