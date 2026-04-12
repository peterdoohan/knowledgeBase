---
title: "Computational models of schizophrenia: attractor dynamics and NMDA hypofunction"
subtopic_id: clinical_and_computational_psychiatry__01
parent_topic_id: clinical_and_computational_psychiatry
page_type: topic
page_worthiness: 3
status: draft_llm
generated_at: "2026-04-12T19:50:20.289631+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - nour2021_impaired_replay_schizophrenia
  - adams2018_attractor_schizophrenia
  - jauhar2022_schizophrenia
  - ivanov2021_psychotropic_drugs_mental_illness
  - atiya2021_metacognition_attractor
core_papers:
  - adams2018_attractor_schizophrenia
  - atiya2021_metacognition_attractor
  - braun2018_maps_network_mental_disorders
  - durstewitz2020_psychiatric_network_dynamics
  - howes2016_aberrant_salience_schizophrenia
  - ivanov2021_psychotropic_drugs_mental_illness
  - jauhar2022_schizophrenia
  - nour2021_impaired_replay_schizophrenia
---

# Computational models of schizophrenia: attractor dynamics and NMDA hypofunction

The strongest computational story here is narrower than many broad “predictive processing” accounts: schizophrenia is plausibly associated with reduced stability of recurrent network states, producing nonlinear belief updating, noisier commitment to latent structure, and abnormal offline replay of relational information. Human evidence is better for the computational phenotype than for its proposed synaptic cause. In particular, attractor instability has direct behavioral and systems-level support, whereas NMDA-receptor hypofunction remains an upstream mechanistic hypothesis supported mainly indirectly, with mixed post-mortem evidence and no decisive therapeutic confirmation [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]] [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]] [[raw/summaries/jauhar2022_schizophrenia|Jauhar et al. 2022]].

## Current view

A defensible synthesis is a two-level model.

At the computational level, schizophrenia involves unstable or shallow attractor-like dynamics in recurrent circuits. This predicts state-dependent, nonlinear belief updating rather than a simple global increase in learning rate or generic noise. That claim has direct support from model comparison across independent datasets [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]].

At the systems level, this instability may extend beyond prefrontal decision circuits to hippocampal/entorhinal mechanisms for relational structure and replay. Patients show impaired spontaneous replay of inferred sequences and distorted task-structure representations after learning [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]].

NMDA hypofunction is best treated as a candidate mechanism for these dynamics, not a settled finding. The broader schizophrenia literature supports converging dopaminergic and glutamatergic involvement, but the glutamate/NMDA branch remains substantially indirect; ketamine-like models are informative, yet post-mortem NMDA findings are inconsistent and glutamatergic treatments have not delivered clear large-trial success [[raw/summaries/jauhar2022_schizophrenia|Jauhar et al. 2022]].

This makes the field asymmetric: the computational description is more mature than the receptor-level attribution.

## Strongest evidence

- [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]] gives the cleanest human evidence for attractor-like instability in schizophrenia.
  - A model including belief instability and response stochasticity outperformed simpler alternatives across two independent datasets.
  - Schizophrenia groups showed higher belief instability and higher response stochasticity.
  - The two parameters covaried across experiments, consistent with a shared underlying process rather than unrelated deficits.
  - The key result is qualitative, not just quantitative: patients were not simply “over-updating,” but showed nonlinear updating that depended on current belief state.

- [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]] provides direct human evidence for abnormal offline dynamics linked to relational learning.
  - Controls showed significant post-learning forward replay; patients did not.
  - Patients were selectively impaired in sequence-order learning and especially transitive inference, not in all aspects of task learning.
  - Replay-associated ripple power was elevated in patients despite weaker sequenceness, echoing abnormalities seen in rodent models.
  - This is one of the strongest bridges from circuit-level abnormal dynamics to higher-order cognitive impairment in schizophrenia.

- [[raw/summaries/jauhar2022_schizophrenia|Jauhar et al. 2022]] is important mainly as a constraint.
  - Cognitive impairment is core to schizophrenia, and hippocampal/PFC abnormalities are replicated.
  - But the glutamatergic/NMDA account is not yet closed: evidence is indirect, post-mortem receptor results are inconsistent, and pharmacological translation remains weak.

- [[raw/summaries/atiya2021_metacognition_attractor|Atiya et al. 2021]] is supporting rather than disorder-specific evidence.
  - It shows that attractor-network variants can dissociate first-order performance from metacognitive distortions using a low-dimensional circuit parameter.
  - Relevant because schizophrenia-spectrum phenotypes include metacognitive disturbance, but this paper is not schizophrenia-specific and should not be overread.

## Landmark papers

- [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]]
  - Landmark because it moved the field beyond vague claims of “jumping to conclusions” or generic Bayesian abnormality.
  - It formalized unstable-attractor behavior as a specific nonlinear signature in belief updating.

- [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]]
  - Landmark because it brought replay—a mechanistic concept from rodent hippocampal work—into human schizophrenia.
  - It tied abnormal offline dynamics to impaired inference about latent relational structure.

- [[raw/summaries/durstewitz2020_psychiatric_network_dynamics|Durstewitz et al. 2020]]
  - Landmark at the framework level.
  - It argues that psychiatric disorders should be understood as disorders of network dynamics, making attractor instability a general explanatory target rather than a schizophrenia-only idea.

- [[raw/summaries/jauhar2022_schizophrenia|Jauhar et al. 2022]]
  - Landmark as a skeptical synthesis.
  - It keeps the glutamate/NMDA story in view while making clear that dopamine has stronger translational grounding and that glutamatergic evidence remains incomplete.

## Boundaries and tensions

- The main attractor evidence in schizophrenia is computationally strong but mechanistically indirect.
  - In [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]], the instability parameter is a phenomenological summary of what unstable attractors would do to inference; it is not a direct measure of attractor depth or recurrent gain.

- NMDA hypofunction is still more hypothesis than established human disease mechanism.
  - [[raw/summaries/jauhar2022_schizophrenia|Jauhar et al. 2022]] explicitly notes that support is mainly indirect and that post-mortem NMDA findings are inconsistent.
  - Large clinical success of glutamatergic interventions has not materialized.

- Cross-level unification is incomplete.
  - The belief-updating work centers prefrontal/striatal inference dynamics [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]].
  - The replay work centers hippocampal–entorhinal structure learning [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]].
  - These may reflect one shared dynamical pathology, but that is not yet shown.

- Specificity to schizophrenia is limited.
  - In [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]], clinical controls with mood disorders showed a similar parameter pattern when unwell.
  - That pushes the interpretation toward a transdiagnostic state/process marker rather than a schizophrenia-specific signature.

- Medication and measurement remain nontrivial issues.
  - In [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]], all schizophrenia subjects were medicated.
  - In [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]], the replay effect survived exclusion of medicated patients, but MEG-based ripple inference in deep structures is still technically limited.

- These models do not capture the whole clinical phenomenon.
  - They explain aspects of belief dynamics, replay, and metacognition, but not the language-rich, autobiographical, and interpersonal structure of psychotic experience emphasized in conceptual critiques such as [[raw/summaries/ivanov2021_psychotropic_drugs_mental_illness|Ivanov et al. 2021]].

## Open questions

- Can attractor-instability parameters be tied directly to NMDA-dependent physiology in humans, rather than inferred by analogy?

- Are replay abnormalities a cause of impaired relational inference and psychotic symptoms, or a downstream correlate of broader hippocampal dysfunction?

- Is the computational phenotype trait-like, episode-linked, or treatment-sensitive?
  - Existing evidence leaves room for both trait and state components.

- Do prefrontal belief instability and hippocampal replay failure arise from the same circuit pathology, or are they partially dissociable routes to similar symptoms?

- How should dopamine-centered aberrant salience models be integrated with attractor/NMDA accounts rather than treated as rivals [[raw/summaries/howes2016_aberrant_salience_schizophrenia|Howes et al. 2016]] [[raw/summaries/jauhar2022_schizophrenia|Jauhar et al. 2022]]?

- Can these models stratify patients or predict response better than standard symptom measures?
  - That remains largely unproven.

## Key papers

- [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]] — strongest direct evidence that schizophrenia involves nonlinear belief updating consistent with unstable attractor dynamics.

- [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]] — strongest human evidence linking schizophrenia to impaired offline replay and distorted relational structure representations.

- [[raw/summaries/jauhar2022_schizophrenia|Jauhar et al. 2022]] — best broad clinical review for placing attractor/NMDA models in the context of stronger dopaminergic evidence and mixed glutamatergic evidence.

- [[raw/summaries/durstewitz2020_psychiatric_network_dynamics|Durstewitz et al. 2020]] — dynamic-systems framework arguing that psychiatric symptoms may arise from altered network dynamics such as attractor instability.

- [[raw/summaries/atiya2021_metacognition_attractor|Atiya et al. 2021]] — useful circuit model showing how attractor architectures can generate dissociable metacognitive distortions; relevant but not schizophrenia-specific.

- [[raw/summaries/howes2016_aberrant_salience_schizophrenia|Howes et al. 2016]] — key complementary dopamine account that any NMDA/attractor model must reckon with.

- [[raw/summaries/ivanov2021_psychotropic_drugs_mental_illness|Ivanov et al. 2021]] — conceptual reminder that computational and receptor-level models capture only part of clinically meaningful psychopathology.

## Source papers
- [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]] | [[raw/mds/nour2021_impaired_replay_schizophrenia|source md]]: Impaired neural replay of inferred relationships in schizophrenia
- [[raw/summaries/adams2018_attractor_schizophrenia|Adams et al. 2018]] | [[raw/mds/adams2018_attractor_schizophrenia|source md]]: Attractor-like Dynamics in Belief Updating in Schizophrenia
- [[raw/summaries/jauhar2022_schizophrenia|Jauhar et al. 2022]] | [[raw/mds/jauhar2022_schizophrenia|source md]]: Schizophrenia
- [[raw/summaries/ivanov2021_psychotropic_drugs_mental_illness|Ivanov and Schwartz 2021]] | [[raw/mds/ivanov2021_psychotropic_drugs_mental_illness|source md]]: Why Psychotropic Drugs Don't Cure Mental Illness—But Should They?
- [[raw/summaries/atiya2021_metacognition_attractor|Atiya et al. 2021]] | [[raw/mds/atiya2021_metacognition_attractor|source md]]: Explaining distortions in metacognition with an attractor network model of decision uncertainty
- [[raw/summaries/braun2018_maps_network_mental_disorders|Braun et al. 2018]] | [[raw/mds/braun2018_maps_network_mental_disorders|source md]]: From Maps to Multi-dimensional Network Mechanisms of Mental Disorders
- [[raw/summaries/durstewitz2020_psychiatric_network_dynamics|Durstewitz et al. 2020]] | [[raw/mds/durstewitz2020_psychiatric_network_dynamics|source md]]: Psychiatric Illnesses as Disorders of Network Dynamics
- [[raw/summaries/howes2016_aberrant_salience_schizophrenia|Howes and Nour 2016]] | [[raw/mds/howes2016_aberrant_salience_schizophrenia|source md]]: Dopamine and the aberrant salience hypothesis of schizophrenia
