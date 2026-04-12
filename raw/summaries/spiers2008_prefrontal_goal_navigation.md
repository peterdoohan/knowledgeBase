---
source_file: "spiers2008_prefrontal_goal_navigation.md"
paper_id: "spiers2008_prefrontal_goal_navigation"
title: "Keeping the goal in mind: Prefrontal contributions to spatial navigation"
authors: "Hugo J. Spiers"
year: 2008
journal: "Neuropsychologia"
paper_type: "review"
contribution_type: "review"
species: ["human"]
tasks: ["navigation_task"]
methods: ["electrophysiology", "lesion"]
brain_regions: ["hippocampus", "prefrontal_cortex", "medial_prefrontal_cortex", "anterior_cingulate_cortex", "orbitofrontal_cortex", "ventromedial_prefrontal_cortex", "infralimbic_cortex", "retrosplenial_cortex"]
keywords: ["ciaramelli_2008_primary_case_study_discussed", "spiers_and_maguire_2006", "2007b_neuroimaging_studies_with_london_taxi_drivers", "shallice_and_burgess_1991_supervisory_attentional_system_and_goal_maintenance", "burgess_et_al_2000_multitasking_and_prefrontal_function", "fellows_and_farah_2003_reversal_learning_and_vmpfc", "feierstein_et_al_2006_spatial_goal_coding_in_rodent_orbitofrontal_cortex", "hok_et_al_2005_spatial_goal_coding_in_rodent_prelimbic_infralimbic_cortex", "named_models_or_frameworks", "working_memory_model_baddeley", "cited_implicitly", "supervisory_attentional_system_shallice_and_burgess", "1991", "attractor_dynamics_used_descriptively", "not_formally_modeled", "navigation_network_hippocampal_cortical_system", "brain_regions", "ventromedial_prefrontal_cortex_vmpfc", "rostral_anterior_cingulate_cortex", "anterior_ba10_frontopolar_cortex"]
---

### One-line summary

The ventromedial prefrontal cortex (vmPFC) is necessary for successful navigation, functioning to maintain goal destinations in working memory while suppressing interference from salient but irrelevant locations.

---

### Background & motivation

Spatial navigation is thought to rely on a distributed network including the hippocampus, parahippocampus, retrosplenial cortex, parietal cortex, and caudate nucleus, but the neural substrate for representing spatial goal locations and guiding navigation to them remained unclear. The prefrontal cortex has been associated with behavioural flexibility, working memory, and planning — functions important for achieving goals — yet it was uncertain whether the human prefrontal cortex is necessary for navigation.

---

### Methods

This is a review/commentary paper that synthesizes evidence from multiple sources:
- Discussion of a single-case neuropsychological study (Ciaramelli, 2008) of a patient with bilateral vmPFC and rostral anterior cingulate damage
- Review of prior neuroimaging studies with London taxi drivers navigating a virtual simulation of London (Spiers & Maguire, 2006, 2007b)
- Integration of rodent lesion and electrophysiology studies (Lacroix et al., 2002; Feierstein et al., 2006; Hok et al., 2005)
- Analysis of error patterns in relation to factors including familiarity, route length, and number of turns

---

### Key findings

- A patient with bilateral vmPFC damage showed severe wayfinding difficulties despite intact topographical knowledge of his hometown
- The patient's route description performance improved substantially when given the destination name or a verbal rehearsal cue, but not with visual stimuli — suggesting a working memory deficit for maintaining goals
- Two-thirds of the patient's errors involved routes ending at highly familiar, personally salient locations (previous work or hobby sites), which acted as "attractor" locations luring him away from his true goal
- The vmPFC is necessary for navigation, with a dual role: (a) maintaining the goal destination in working memory, and (b) suppressing irrelevant but salient information
- Neuroimaging data shows medial prefrontal activity correlates with goal proximity during navigation, while anterior BA10 is associated with planning and manipulating route information

---

### Computational framework

Working memory and goal maintenance framework. The paper conceptualizes navigation as requiring active maintenance of goal representations in working memory, drawing on the prefrontal cortex's established role in working memory and inhibitory control. The "attractor" metaphor is used descriptively (not formally) to describe how highly familiar locations can capture behavior — similar to attractor dynamics in neural networks where certain states are preferentially activated. The framework assumes that goal-directed navigation requires suppression of competing representations, with the vmPFC serving as a critical hub for maintaining intention and filtering distractions.

---

### Prevailing model of the system under study

Prior to this work, spatial navigation was understood to rely on a distributed network including the hippocampus (spatial mapping), parahippocampus, retrosplenial cortex (egocentric transformation), parietal cortex, and caudate nucleus. The prefrontal cortex was known to be involved in working memory, planning, and behavioral flexibility, and functional neuroimaging had shown prefrontal activation during navigation tasks. However, it was not established whether the prefrontal cortex was *necessary* for navigation in humans, nor was its specific role in goal representation and maintenance clearly defined. The prevailing view suggested the prefrontal cortex might support navigation through working memory and planning functions, but the precise computational role remained uncertain.

---

### What this paper contributes

This review consolidates evidence establishing that the vmPFC is necessary for successful navigation in humans, not merely involved. It refines the prevailing model by specifying that the vmPFC's role in navigation is twofold: (1) actively maintaining goal destinations in working memory, and (2) suppressing interference from salient but irrelevant locations (characterized as "attractor" locations). The paper integrates neuropsychological findings with neuroimaging and rodent data to support a unified framework where prefrontal structures work alongside the hippocampal navigation network to enable goal-directed behavior. It also raises questions about the specific computational mechanisms — whether the deficit reflects impaired goal maintenance, reversal learning problems, or disruption of attractor state transitions in cortical networks.

---

### Brain regions & systems

- **Ventromedial prefrontal cortex (vmPFC)** — necessary for navigation; maintains goal destinations in working memory and suppresses interference from salient distractor locations
- **Rostral anterior cingulate cortex** — co-lesioned with vmPFC in the patient; region also implicated in navigation deficits
- **Anterior BA10 (frontopolar cortex)** — associated with planning and manipulating route information during navigation
- **Medial prefrontal cortex (BA9/BA32 border)** — activity correlates with proximity to goals during navigation
- **Hippocampus** — part of the broader navigation network; represents maps of large-scale space
- **Parahippocampus** — part of the navigation network
- **Retrosplenial cortex** — converts allocentric spatial information to egocentric space
- **Parietal cortex** — part of the navigation network; egocentric processing
- **Caudate nucleus** — part of the navigation network
- **Orbitofrontal cortex (in rodents)** — cells code spatial information about goals
- **Prelimbic/infralimbic cortex (in rodents)** — cells code spatial goals

---

### Mechanistic insight

This paper does not meet the high bar for mechanistic insight. While it synthesizes evidence about the necessity of vmPFC for navigation and proposes a dual role (goal maintenance and suppression of interference), it does not present or formalize a specific algorithmic process that could explain the phenomenon, nor does it provide neural data that specifically support such an algorithm over alternatives. The paper discusses the "attractor" metaphor descriptively to explain how familiar locations capture behavior, but this is not formalized as a computational model with defined dynamics. The findings constrain the space of possible models by establishing that vmPFC is necessary for maintaining goal representations and suppressing distractors, but the precise algorithmic implementation and its neural instantiation remain unspecified.

---

### Limitations & open questions

- Whether the patient can learn routes in an unfamiliar environment remains untested
- The precise point in the route where the intention is lost is unknown
- Whether the patient can make use of novel shortcuts or reach the goal after a detour is unclear
- Which specific region calculates proximity or directional information to goals remains unidentified
- Whether the deficit reflects impaired goal maintenance, reversal learning problems, or disruption of attractor state transitions in cortical networks is debated
- The distinction between the contributions of vmPFC versus rostral anterior cingulate (both lesioned in the patient) requires further investigation
- Whether the medial prefrontal region is involved in maintaining goal representations while BA10 is important for planning/manipulating information needs further validation
- The specific mechanisms by which vmPFC suppresses interference from salient distractors remain unspecified
- Replication of findings in other similar patients is needed

---

### Connections & keywords

**Key citations:**
- Ciaramelli (2008) — primary case study discussed
- Spiers & Maguire (2006, 2007b) — neuroimaging studies with London taxi drivers
- Shallice & Burgess (1991) — supervisory attentional system and goal maintenance
- Burgess et al. (2000) — multitasking and prefrontal function
- Fellows & Farah (2003) — reversal learning and vmPFC
- Feierstein et al. (2006) — spatial goal coding in rodent orbitofrontal cortex
- Hok et al. (2005) — spatial goal coding in rodent prelimbic/infralimbic cortex

**Named models or frameworks:**
- Working memory model (Baddeley, cited implicitly)
- Supervisory attentional system (Shallice & Burgess, 1991)
- Attractor dynamics (used descriptively, not formally modeled)
- Navigation network (hippocampal-cortical system)

**Brain regions:**
- Ventromedial prefrontal cortex (vmPFC)
- Rostral anterior cingulate cortex
- Anterior BA10 (frontopolar cortex)
- Medial prefrontal cortex (BA9/BA32 border)
- Hippocampus
- Parahippocampus
- Retrosplenial cortex
- Parietal cortex
- Caudate nucleus
- Orbitofrontal cortex
- Prelimbic/infralimbic cortex

**Keywords:**
- Spatial navigation
- Wayfinding
- Ventromedial prefrontal cortex
- Goal maintenance
- Working memory
- Inhibition
- Attractor states
- Topographical disorientation
- Spatial memory
- Neuropsychology
- Prefrontal cortex
- Intention
