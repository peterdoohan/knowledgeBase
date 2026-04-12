---
title: "Model-based vs model-free reinforcement learning frameworks in anterior cingulate future-state control"
subtopic_id: anterior_cingulate_future_state_and_model_based_control__02
parent_topic_id: anterior_cingulate_future_state_and_model_based_control
page_type: methods
page_worthiness: 3
status: draft_llm
generated_at: "2026-04-12T19:49:48.370292+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - schultz1997_neural_substrate_reward_pred
  - daw2005_uncertainty_prefrontal_striatal
  - akam2021_anterior_cingulate_model
  - loosen2020_computational_psychiatry_ocd
  - lowet2020_distributional_reinforcement_brain
core_papers:
  - akam2021_anterior_cingulate_model
  - daw2005_uncertainty_prefrontal_striatal
  - huang2020_model_based_model_free_neural
  - loosen2020_computational_psychiatry_ocd
  - lowet2020_distributional_reinforcement_brain
  - schultz1997_neural_substrate_reward_pred
  - wilson2013_ofc_cognitive_map
---

# Model-based vs model-free reinforcement learning frameworks in anterior cingulate future-state control

In ACC work, the model-based/model-free distinction is most useful as an experimental interpretation rule, not a complete theory of ACC. The key question is whether ACC activity reflects cached reward value updated by reward prediction errors, or prospective knowledge about action→state structure that can guide choice when transitions change. On current evidence, ACC future-state signals fit the model-based side better: in two-step tasks, ACC encodes predicted next states and surprise about violated state transitions, and ACC inhibition selectively impairs transition-guided updating while sparing simpler reward reinforcement [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]]. But that does not show ACC alone implements full planning; hybrid control, broader prefrontal-striatal circuitry, and task-state representations outside ACC remain central.

## Current view

Model-free RL provides the baseline comparison: action values are cached and updated by temporal-difference reward prediction errors, without requiring an explicit transition model [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]]. In ACC tasks, this predicts reinforcement by reward history but not selective sensitivity to whether an action commonly or rarely leads to a particular future state.

Model-based RL instead uses a representation of task structure, especially action→state transitions, to compute or update values prospectively. In the ACC literature, the decisive signatures are therefore not generic value or reward signals, but state-prediction signals, transition-structure representations, and behavior that changes as a function of transition knowledge [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]].

The strongest ACC-specific claim currently supported is narrower than “ACC does planning.” It is that ACC contributes to using predicted future states for action selection in tasks that formally dissociate transition structure from immediate reward reinforcement [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]].

Human neuroimaging evidence points in the same direction but is coarser. A meta-analysis reported that model-based learning additionally recruits vmPFC/anterior cingulate, whereas model-free learning shows a different subcortical emphasis [[raw/summaries/huang2020_model_based_model_free_neural|Huang et al. 2020]]. That supports association, not process specificity.

## Strongest evidence

The clearest ACC-relevant evidence is the mouse two-step study in [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]].

- The task was designed to dissociate transition structure from reward, including reversals of transition probabilities to reduce simple habitual shortcuts.
- Behavior was not purely model-based or purely model-free; it was best fit by a mixed model that also required forgetting, perseveration, and multi-level motor representations.
- ACC population activity decoded the task’s state-action space and represented the upcoming second-step state before outcome delivery.
- ACC encoded current action-state transition structure and surprise when the observed second-step state violated expectation.
- Reward signals in ACC were state-specific rather than a generic scalar reward code.
- Optogenetic inhibition from outcome to next choice selectively reduced the effect of experienced state transitions on the next decision, while leaving basic reward reinforcement comparatively intact.

Taken together, that is stronger evidence for ACC involvement in model-based updating than for a purely model-free value cache. The causal result matters: ACC disruption affected the use of transition information, not just reward responsiveness.

The broader computational scaffolding comes from [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]], which formalized model-based and model-free controllers as competing systems with different costs and uncertainties. That framework helps interpret ACC effects as part of a prefrontal-striatal controller that is useful when transition knowledge is informative and worth its computational cost.

By contrast, [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]] is foundational for the model-free side of the comparison: TD-like dopamine prediction errors explain how cached values can be learned without explicit transition models. This is essential background because ACC future-state claims are meaningful only relative to that alternative.

## Landmark papers

- [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]]  
  Established the temporal-difference prediction-error framework that anchors the model-free comparator. Not ACC-specific, but still the reference point for saying a signal is “more than” reward prediction error.

- [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]]  
  Gave the modern computational distinction between model-based tree search and model-free caching, plus an arbitration account based on uncertainty. This remains the main formal lens for interpreting prefrontal/striatal dissociations.

- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]]  
  Argued that OFC provides a cognitive map of task space. Important here because ACC future-state coding may depend on a broader state-representation system rather than ACC alone constructing the task model.

- [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]]  
  The strongest ACC-specific empirical paper: future-state representations, transition surprise, and selective causal necessity for model-based choice updating in a two-step task.

- [[raw/summaries/huang2020_model_based_model_free_neural|Huang et al. 2020]]  
  Meta-analytic support that model-based learning engages vmPFC/anterior cingulate more than model-free learning, though without the mechanistic resolution of single-task causal studies.

## Boundaries and tensions

Future-state coding is not equivalent to full model-based planning. ACC may encode one-step action→state predictions or task variables needed for model-based control without itself performing multi-step evaluation.

ACC reward signals in [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]] were state-contextualized, which argues against a simple scalar reward code. But state-specific reward coding still does not tell us whether ACC computes values, supplies state features, or reports learning signals for another circuit.

The behavioral dissociation is model-dependent. In the two-step task, the canonical transition-by-outcome interaction was near zero and only emerged with a lag, consistent with learning of transition probabilities rather than a textbook fixed-transition model [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]]. So “model-based” inference depends on fitting the right task assumptions.

Motor confounds remain real. [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]] included multi-level motor representations in the best-fitting behavioral model, and the authors note that the surprise signal might partly reflect motor-action consequences rather than a pure state-prediction error.

The MB/MF dichotomy is probably too coarse for some ACC questions. [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] emphasizes arbitration, not strict segregation; [[raw/summaries/loosen2020_computational_psychiatry_ocd|Loosen et al. 2020]] similarly argues against treating reduced model-based behavior as automatically implying excessive habitual/model-free control.

Even the “model-free baseline” is not conceptually fixed. Standard TD accounts remain foundational [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]], but broader RL theory now includes richer distributional variants of prediction learning [[raw/summaries/lowet2020_distributional_reinforcement_brain|Lowet et al. 2020]]. That does not erase the MB/MF distinction, but it cautions against treating model-free as synonymous with a single scalar value signal.

## Open questions

- Does ACC learn the transition model, read it out, or arbitrate when it should control behavior?
- Is ACC causally required at the moment of state transition, during the post-outcome update period, or both? [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]] did not isolate these epochs cleanly.
- How much of ACC “future-state” activity is abstract state prediction versus motor sequence structure?
- Are ACC signals limited to one-step predictions, or do they support deeper prospective rollout?
- How does ACC interact with OFC task-state representations and striatal value-learning systems during model-based choice?
- Under what task conditions does ACC lose control to cached strategies, as predicted by uncertainty/computation tradeoff accounts [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]]?
- How well do rodent ACC findings generalize to human anterior cingulate signals in two-step and reversal tasks?

## Key papers

- [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]] — best direct evidence that ACC predicts future states and is selectively necessary for model-based choice updating.
- [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] — core formal framework for model-based/model-free competition and arbitration.
- [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]] — canonical model-free TD prediction-error account used as the main alternative interpretation.
- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] — key state-representation framework relevant to whether ACC future-state signals depend on broader task maps.
- [[raw/summaries/huang2020_model_based_model_free_neural|Huang et al. 2020]] — meta-analytic human evidence linking anterior cingulate/vmPFC more strongly to model-based than model-free learning.
- [[raw/summaries/lowet2020_distributional_reinforcement_brain|Lowet et al. 2020]] — useful caution that model-free learning itself may be richer than a single mean-value TD signal.
- [[raw/summaries/loosen2020_computational_psychiatry_ocd|Loosen et al. 2020]] — argues that apparent model-based deficits need not reduce to “too much habit,” relevant for interpreting frontostriatal control.

## Source papers
- [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]] | [[raw/mds/schultz1997_neural_substrate_reward_pred|source md]]: A Neural Substrate of Prediction and Reward
- [[raw/summaries/daw2005_uncertainty_prefrontal_striatal|Daw et al. 2005]] | [[raw/mds/daw2005_uncertainty_prefrontal_striatal|source md]]: Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control
- [[raw/summaries/akam2021_anterior_cingulate_model|Akam et al. 2021]] | [[raw/mds/akam2021_anterior_cingulate_model|source md]]: The Anterior Cingulate Cortex Predicts Future States to Mediate Model-Based Action Selection
- [[raw/summaries/loosen2020_computational_psychiatry_ocd|Loosen and Hauser 2020]] | [[raw/mds/loosen2020_computational_psychiatry_ocd|source md]]: Towards a computational psychiatry of juvenile obsessive-compulsive disorder
- [[raw/summaries/lowet2020_distributional_reinforcement_brain|Lowet et al. 2020]] | [[raw/mds/lowet2020_distributional_reinforcement_brain|source md]]: Distributional Reinforcement Learning in the Brain
- [[raw/summaries/huang2020_model_based_model_free_neural|Huang et al. 2020]] | [[raw/mds/huang2020_model_based_model_free_neural|source md]]: Goal-oriented and habitual decisions: Neural signatures of model-based and model-free learning
- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] | [[raw/mds/wilson2013_ofc_cognitive_map|source md]]: Orbitofrontal Cortex as a Cognitive Map of Task Space
