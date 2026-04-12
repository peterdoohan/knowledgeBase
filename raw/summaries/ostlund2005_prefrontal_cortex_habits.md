---
source_file: ostlund2005_prefrontal_cortex_habits.md
paper_id: ostlund2005_prefrontal_cortex_habits
title: "Lesions of Medial Prefrontal Cortex Disrupt the Acquisition But Not the Expression of Goal-Directed Learning"
authors:
  - "Sean B. Ostlund"
  - "Bernard W. Balleine"
year: 2005
journal: "The Journal of Neuroscience"
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - lesion
brain_regions:
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - orbitofrontal_cortex
  - prelimbic_cortex
  - infralimbic_cortex
  - striatum
  - dorsomedial_striatum
  - nucleus_accumbens
  - thalamus
  - mediodorsal_thalamus
  - amygdala
  - basolateral_amygdala
keywords:
  - goal_directed_action
  - instrumental_conditioning
  - outcome_devaluation
  - actionoutcome_association
  - habit_learning
  - medial_prefrontal_cortex_lesion
  - prelimbic_cortex
  - outcome_specific_reinstatement
  - incentive_value
  - acquisition_vs_expression_dissociation
  - stimulusresponse_vs_actionoutcome
  - prefrontal_scaffolding
  - lesions
  - medial
  - prefrontal
  - cortex
  - disrupt
  - acquisition
  - but
  - not
key_citations:
  - coutureau2003_infralimbic_prefrontal_goal
  - balleine1998_goal_directed_instrumental_action
wiki_pages:
  - wiki/topics/medial_prefrontal_cortex_in_rat_goal_directed_vs_habitual_control
---

### One-line summary

Excitotoxic lesions of the medial prefrontal cortex (mPFC) made before training abolish goal-directed instrumental performance (outcome devaluation sensitivity), whereas lesions made after training leave this sensitivity intact, demonstrating that the mPFC is required for acquiring but not for storing or expressing action–outcome associations.

---

### Background & motivation

In instrumental conditioning, rats can encode specific action–outcome relationships, allowing them to adjust performance flexibly when the value of an anticipated outcome changes. Prior work had shown that pretraining lesions of the prelimbic area of the mPFC abolish this sensitivity to outcome devaluation and action–outcome contingency degradation, implicating mPFC in goal-directed action. However, it remained unknown whether the mPFC is necessary for encoding (acquisition), storing, or expressing these associations during performance. Resolving this question is important for understanding the neural architecture of goal-directed versus habit-based control and for interpreting deficits observed in drug reinstatement and other translational contexts.

---

### Methods

- **Species and preparation**: Female Long–Evans rats; food-restricted to ~85% free-feeding body weight.
- **Lesion method**: Bilateral excitotoxic NMDA infusions targeting the prelimbic area of mPFC (AP +3.3, ML ±0.7, DV −3.5 from bregma); histology with thionin staining confirmed bilateral PL damage. Rats with only unilateral damage were excluded.
- **Experiment 1**: Posttraining mPFC lesions; rats trained on two lever-press actions each earning a unique outcome (pellets or sucrose, RR-20 schedule), then lesioned after training. Tested on outcome-specific reinstatement and outcome devaluation (specific satiety, 5 min choice extinction test).
- **Experiment 2**: Direct comparison of pretraining vs. posttraining mPFC lesions on both outcome devaluation and reinstatement, without additional retraining between surgery and testing. Three groups: pre-lesion, post-lesion, sham.
- **Experiment 3**: Pretraining mPFC lesions assessed on devalued reinstatement — the reinstating outcome was itself devalued before reinstatement testing, to determine whether reinstatement in lesioned rats depends on incentive value or sensory/discriminative properties of the outcome.
- **Analysis**: Lever presses per minute; choice performance (% of total responses on reinstated lever) for reinstatement tests.

---

### Key findings

- **Posttraining lesions spare outcome devaluation**: In Experiment 1, both sham and posttraining mPFC-lesioned rats showed significant sensitivity to outcome devaluation (fewer responses on the lever paired with the devalued outcome). Sham: F(1,7) = 21.98, p < 0.01; mPFC post: F(1,6) = 11.75, p < 0.05.
- **Pretraining lesions abolish outcome devaluation**: In Experiment 2, pretraining-lesioned rats showed no devaluation effect (F(1,9) = 1.16, ns), while both sham and posttraining-lesioned groups did. The response × group interaction was significant (F(2,28) = 4.17, p < 0.05).
- **Both pre- and posttraining lesions reduce reinstatement magnitude but preserve selectivity**: mPFC lesions (regardless of timing) reduced overall response rates during reinstatement (sham ~22.5 responses/min; pre ~11.3; post ~10.2), but left intact the selectivity of reinstatement — all groups increased their choice of the reinstated action after outcome delivery (phase effect: F(1,28) = 10.28, p < 0.01; no phase × group interaction).
- **Devalued reinstatement dissociates outcome representations**: In Experiment 3, sham rats were insensitive to a devalued outcome during reinstatement (outcome value suppressed reinstatement), whereas pretraining mPFC-lesioned rats showed robust selective reinstatement even for a devalued outcome. This indicates that lesioned rats use only the sensory/discriminative properties of the outcome to guide response selection, not its current incentive value.
- **Reinstatement and devaluation effects are both behaviourally and neurally dissociable** at the level of the mPFC, as implied by the pattern across experiments.

---

### Computational framework

Not applicable as a formal computational model. However, the paper's theoretical framing draws on a dual-system account of instrumental conditioning: a **goal-directed system** encoding action–outcome (A→O) associations (sensitive to outcome devaluation, contingency degradation) and a **habit system** encoding stimulus–response (S→R) associations (insensitive to outcome value). The core computational distinction is between outcome representations that include current incentive value (goal-directed) versus representations driven only by sensory/discriminative features of the stimulus (habit-like).

The results constrain models of goal-directed control by specifying that the mPFC is required during the acquisition window for forming value-laden A→O associations, but that long-term storage and retrieval of these associations is handled by downstream structures (proposed candidates: dorsomedial striatum, basolateral amygdala). This is consistent with prefrontal working memory accounts (Miller & Cohen, 2001) in which the PFC maintains task-relevant representations online during learning, enabling consolidation elsewhere.

---

### Prevailing model of the system under study

The paper's introduction situates mPFC within a broader literature on the neural basis of goal-directed instrumental action. The prevailing understanding going into this study was that the mPFC — specifically the prelimbic (PL) subregion — is a necessary component of the goal-directed learning system in rats. Pretraining PL lesions had been shown repeatedly to abolish sensitivity to outcome devaluation and to contingency degradation, and electrophysiological work in both rats and primates had found mPFC neurons encoding action–outcome relationships. The implicit working model was therefore that the mPFC encodes and/or maintains A→O associations, and that without it, animals default to S→R (habit) control.

What had not been tested, and what the paper directly addresses, was whether this mPFC involvement is specific to encoding (acquisition) or whether it also extends to storage and expression. The possibility that mPFC might permanently store A→O associations — rather than acting as a transient scaffold — was a live alternative prior to this study.

---

### What this paper contributes

This paper establishes a critical temporal dissociation: the mPFC is required for the acquisition of goal-directed action–outcome associations but not for their subsequent storage or expression. Posttraining lesions that would be expected to impair expression if the mPFC were the permanent store leave performance entirely intact. This rules out the hypothesis that mPFC is the site of long-term A→O memory and instead positions it as an acquisition-phase scaffold — consistent with Miller and Cohen's (2001) proposal that PFC keeps relevant representations active during learning, enabling consolidation in downstream structures.

The paper further dissociates two components of outcome-mediated response control: (1) response initiation (overall reinstatement magnitude, mPFC-dependent regardless of timing) and (2) response selection (selectivity of reinstatement to the trained outcome, mPFC-independent). The devalued reinstatement result (Experiment 3) additionally establishes that the intact selectivity seen in lesioned rats is driven by sensory stimulus features, not by incentive value — i.e., lesioned rats behave as if the goal-directed system is offline and they are relying entirely on outcome-as-discriminative-stimulus (an O→A association) rather than outcome-as-anticipated-goal (an A→O association).

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC) / prelimbic cortex (PL)** — primary focus; proposed to be selectively required for the *acquisition* of action–outcome associations during instrumental conditioning. Also contributes to general response initiation (reinstatement magnitude) but not response selection (reinstatement selectivity).
- **Infralimbic cortex (IL)** — minimally implicated in the current lesions and noted (citing Killcross & Coutureau, 2003) to not be necessary for outcome devaluation sensitivity; damage was not systematic and unlikely to explain the pretraining lesion effects.
- **Orbitofrontal cortex (OFC)** — discussed in contrast: OFC lesions disrupt expression of stimulus–outcome associations in Pavlovian conditioning (both pre- and posttraining), unlike the mPFC pattern seen here.
- **Basolateral amygdala (BLA)** — discussed as a candidate downstream storage site; pretraining BLA lesions produce similar deficits (devaluation, contingency degradation insensitivity), and BLA is proposed to encode incentive value representations.
- **Dorsomedial striatum (DMS)** — discussed as a candidate long-term store for A→O associations; unlike mPFC, both pre- and posttraining DMS lesions impair outcome devaluation, consistent with a sustained storage role.
- **Nucleus accumbens core** — noted to contribute to incentive-value-modulated performance but not to A→O encoding per se.
- **Mediodorsal thalamus** — proposed as a hub for DMS-to-PFC feedback necessary during goal-directed learning.

---

### Mechanistic insight

The paper meets criterion 1 (it formalises an algorithmic claim: mPFC is required for acquisition but not expression/storage of A→O associations, implemented as an online working-memory scaffold during training). It also provides neural data (lesion + behavioural assays) that specifically distinguish this account from the alternative hypothesis (mPFC as permanent store). However, it does not provide direct recordings or cellular-level data linking mPFC activity to specific computational variables.

Mapping to Marr's levels:

- **Computational**: The problem is flexible, outcome-sensitive action selection. The animal must learn which actions produce which outcomes and adjust behaviour when outcome values change. Goal-directed control solves this by maintaining a model of A→O relationships weighted by current incentive value.
- **Algorithmic**: The mPFC provides temporary active maintenance of A→O associations during initial training — acting analogously to a working memory buffer — enabling these associations to be consolidated in downstream structures (DMS, BLA). Once consolidated, expression no longer requires mPFC. Without mPFC during acquisition, only S→R (habit) or O→A (discriminative stimulus) associations are formed, leaving behaviour insensitive to outcome value.
- **Implementational**: The paper does not address specific cell types, synaptic mechanisms, or neuromodulators within mPFC. The lesion method (NMDA excitotoxicity targeting PL bilaterally) identifies the region but does not resolve the cellular or circuit implementation.

The paper does not meet the bonus criterion (no data on specific cell types, connectivity patterns, or biophysical mechanisms).

---

### Limitations & open questions

- Lesions encompassed PL but in some rats also extended to ventral IL and ventral anterior cingulate cortex, introducing potential ambiguity about which subregion drives the effects (though selective IL lesion data from other labs are cited to argue against IL involvement).
- The study uses only female Long–Evans rats; generalisability to males or other strains is untested.
- The retraining given in Experiment 1 between surgery and testing complicates interpretation of the posttraining result (partly addressed by Experiment 2, which omitted retraining).
- The paper does not identify where A→O associations are ultimately stored; DMS and BLA are proposed candidates but are not tested in this study.
- The dissociation between outcome devaluation (A→O mediated) and reinstatement selectivity (O→A mediated) rests on an associative theory; direct neural tests of this dissociation within mPFC are not provided.
- It remains unclear how the mPFC "scaffolding" function interfaces with consolidation in downstream structures at a mechanistic level.
- The relevance of these findings to drug relapse (reinstatement model) is discussed but not directly tested; the claim that mPFC-intact response selection is preserved after lesions may have different implications in drug self-administration paradigms.

---

### Connections & keywords

**Key citations**:
- Balleine & Dickinson (1998) — foundational evidence for goal-directed action and mPFC lesion effects
- Corbit & Balleine (2003) — prelimbic cortex in instrumental conditioning; reinstatement spared
- Killcross & Coutureau (2003) — PL vs. IL dissociation; IL lesions spare devaluation sensitivity
- Miller & Cohen (2001) — integrative theory of PFC function; active maintenance during learning
- Colwill & Rescorla (1985, 1986) — action–outcome encoding in instrumental conditioning
- Yin et al. (2005a, 2005b) — dorsomedial striatum in instrumental/A–O learning
- Gallagher et al. (1999); Pickens et al. (2005) — OFC and incentive value in Pavlovian conditioning
- Balleine et al. (2003); Corbit & Balleine (2005) — BLA lesions and instrumental conditioning

**Named models or frameworks**:
- Goal-directed vs. habit dual-system framework (Dickinson, 1989; Balleine & Dickinson, 1998)
- Outcome devaluation paradigm (specific satiety)
- Outcome-specific reinstatement protocol
- Miller & Cohen (2001) active maintenance / PFC scaffolding account

**Brain regions**:
- Medial prefrontal cortex (mPFC)
- Prelimbic cortex (PL)
- Infralimbic cortex (IL)
- Orbitofrontal cortex (OFC)
- Basolateral amygdala (BLA)
- Dorsomedial striatum (DMS)
- Nucleus accumbens core
- Mediodorsal thalamus

**Keywords**:
- goal-directed action
- instrumental conditioning
- outcome devaluation
- action–outcome association
- habit learning
- medial prefrontal cortex lesion
- prelimbic cortex
- outcome-specific reinstatement
- incentive value
- acquisition vs. expression dissociation
- stimulus–response vs. action–outcome
- prefrontal scaffolding

### Related wiki pages
- [[wiki/topics/medial_prefrontal_cortex_in_rat_goal_directed_vs_habitual_control|Medial prefrontal cortex in rat goal-directed vs habitual control]]
