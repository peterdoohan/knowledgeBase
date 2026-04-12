---
title: "Dopamine reward prediction error and temporal-difference learning"
subtopic_id: striatal_and_dopaminergic_reinforcement_learning__04
parent_topic_id: striatal_and_dopaminergic_reinforcement_learning
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:49:22.473250+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - schultz1997_neural_substrate_reward_pred
  - montague1996_predictive_hebbian_dopamine
  - lammel2014_dopamine_reward_aversion
  - bogacz2020_dopamine_action_inference
  - hamid2021_dopamine_waves_credit_assignment
core_papers:
  - bakermans2020_reinforcement_learning_dopamine
  - behrens2007_learning_value_information_uncertain
  - bogacz2020_dopamine_action_inference
  - campbell2025_hardwired_circuit_td_learning
  - fiore2015_basal_ganglia_behavior
  - hamid2021_dopamine_waves_credit_assignment
  - hauser2016_adhd_neural_gain
  - lammel2014_dopamine_reward_aversion
---

# Dopamine reward prediction error and temporal-difference learning

The durable core claim is that a major subset of midbrain dopamine activity behaves like a temporal-difference (TD) reward prediction error (RPE): positive for better-than-expected outcomes, near-zero for fully expected rewards, and negative for omissions at the expected time. The strongest support comes from classic primate physiology and the computational fit between those data and TD learning [[raw/summaries/montague1996_predictive_hebbian_dopamine|Montague et al. 1996]] [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]]. But the simple picture of a single, global, scalar dopamine teaching signal is now too narrow. Later work shows projection-defined heterogeneity, movement-related and action-related signals not reducible to standard RPE, and spatially structured dopamine dynamics that could support credit assignment across striatal subregions [[raw/summaries/lammel2014_dopamine_reward_aversion|Lammel et al. 2014]] [[raw/summaries/lee2019_dopamine_movement_selectivity|Lee et al. 2019]] [[raw/summaries/hamid2021_dopamine_waves_credit_assignment|Hamid et al. 2021]].

## Current view

The classical TD-RPE account remains the best-supported first-pass description of phasic dopamine responses in appetitive conditioning. Two findings still anchor the field: responses shift from reward to reward-predicting cues with learning, and expected reward omission produces a dip at the time reward should have occurred [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]].

What has changed is the scope of the claim. Dopamine is not well-described as a uniform broadcast of one scalar teaching signal to all targets. Midbrain dopamine neurons differ by projection target, input connectivity, electrophysiology, and behavioral correlates; reward- and aversion-related processing can be separated across microcircuits [[raw/summaries/lammel2014_dopamine_reward_aversion|Lammel et al. 2014]].

A further refinement is that some dopamine signals appear tied to action, movement, or agency-dependent credit assignment rather than only cached reward value. DMS-projecting dopamine neurons show movement selectivity not explained by standard RPE formulations [[raw/summaries/lee2019_dopamine_movement_selectivity|Lee et al. 2019]], and dorsal striatal dopamine can propagate as task-dependent waves whose direction flips with contingency reversals [[raw/summaries/hamid2021_dopamine_waves_credit_assignment|Hamid et al. 2021]].

So the field has mostly moved from “dopamine = TD error” to “some dopamine signals instantiate TD-like appetitive prediction errors, but the full dopamine system is computationally heterogeneous.”

## Strongest evidence

- **Cue-to-reward transfer and omission dips.** The canonical empirical pattern is hard to ignore: naive animals show phasic dopamine responses to unexpected reward; after conditioning, the response transfers to the conditioned stimulus; once reward is fully predicted, reward delivery itself elicits little or no phasic response; omission causes a depression at the expected reward time [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]]. This is the clearest physiological match to signed TD error.

- **A quantitative TD framework fits the phenomenology.** The prediction-error formulation was not just a verbal analogy. A formal model reproduced transfer from reward to cue, negative signals for omission/mistakes, extinction, and effects of temporal uncertainty, tying mesencephalic dopamine to RL variables already defined in TD learning [[raw/summaries/montague1996_predictive_hebbian_dopamine|Montague et al. 1996]].

- **Temporal specificity matters.** The omission-related dip occurs at the time reward was expected, implying an internal representation of expected reward timing, not merely a generic disappointment signal [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]]. This is one of the strongest reasons the data were taken to support TD-like rather than simpler reward-reactivity accounts.

- **Recent circuit-level support is emerging.** A newer report argues that a nucleus accumbens D1 → VTA pathway can implement a biphasic linear filter that computes a temporal difference and that the discount factor can be set by the balance of excitatory and inhibitory components [[raw/summaries/campbell2025_hardwired_circuit_td_learning|Campbell et al. 2025]]. If this holds up, it would move the literature from algorithmic resemblance toward identified circuit implementation.

- **But the strongest counterevidence is also strong.** Projection-defined heterogeneity in VTA undermines any literal one-channel dopamine model [[raw/summaries/lammel2014_dopamine_reward_aversion|Lammel et al. 2014]]. Movement selectivity in DMS-projecting dopamine neurons is not explained by RPE alone [[raw/summaries/lee2019_dopamine_movement_selectivity|Lee et al. 2019]]. Dorsal striatal dopamine waves suggest structured, non-synchronous teaching signals tuned by inferred agency [[raw/summaries/hamid2021_dopamine_waves_credit_assignment|Hamid et al. 2021]].

## Landmark papers

[[raw/summaries/montague1996_predictive_hebbian_dopamine|Montague et al. 1996]]  
First explicit computational framing of mesencephalic dopamine as a TD-like prediction error broadcast. Important because it turned disparate physiological observations into a formal learning rule.

[[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]]  
The canonical synthesis. Established the empirical “signature pattern” for dopamine RPE: cue transfer, no response to fully predicted reward, and a dip for omission.

[[raw/summaries/lammel2014_dopamine_reward_aversion|Lammel et al. 2014]]  
A major revision to the unitary dopamine story. Organized evidence that VTA dopamine neurons form projection-defined subcircuits with separable roles in reward, aversion, and stress-related behavior.

[[raw/summaries/hamid2021_dopamine_waves_credit_assignment|Hamid et al. 2021]]  
Shifted the debate from “is dopamine an RPE?” toward “how is dopamine targeted in space and time to solve credit assignment?” The wave framework directly challenges the global-broadcast assumption.

[[raw/summaries/bogacz2020_dopamine_action_inference|Bogacz et al. 2020]]  
A notable theoretical extension arguing that distinct dopaminergic loops may encode different prediction errors, including action-deviation signals in habit circuits rather than reward errors alone.

## Boundaries and tensions

- **Scalar mean RPE vs heterogeneous population code.** The original account treats dopamine as a scalar “better/worse than expected” signal [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]] [[raw/summaries/montague1996_predictive_hebbian_dopamine|Montague et al. 1996]]. Later reviews argue that diversity across dopamine neurons may reflect a richer code, potentially distributional RL rather than a single expected-value error [[raw/summaries/bakermans2020_reinforcement_learning_dopamine|Bakermans et al. 2020]] [[raw/summaries/lowet2020_distributional_reinforcement_brain|Lowet et al. 2020]]. This is promising but not yet a clean replacement for the classical account.

- **Reward error vs movement/action signals.** DMS-projecting dopamine neurons carry movement selectivity that standard RPE cannot explain away as value coding [[raw/summaries/lee2019_dopamine_movement_selectivity|Lee et al. 2019]]. This creates real pressure on any theory claiming all dopamine transients are reward errors.

- **Global broadcast vs targeted credit assignment.** Classic models implicitly assume a broadly shared teaching signal. Hamid et al. instead show directional dopamine waves across dorsal striatum, with wave direction tracking inferred instrumental agency and reversing after contingency changes [[raw/summaries/hamid2021_dopamine_waves_credit_assignment|Hamid et al. 2021]].

- **Appetitive core vs aversive/stress signaling.** Schultz’s classic account emphasized insensitivity to aversive events in dopamine neurons [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]]. Lammel et al. argue that this was partly a sampling problem: different VTA subpopulations participate in distinct reward and aversion circuits [[raw/summaries/lammel2014_dopamine_reward_aversion|Lammel et al. 2014]].

- **Algorithmic elegance vs biological implementation gaps.** The classical TD account requires a temporally extended state representation and some mechanism for expected reward timing. Both remain underspecified biologically in the original frameworks [[raw/summaries/montague1996_predictive_hebbian_dopamine|Montague et al. 1996]] [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]].

- **Fixed learning rules vs uncertainty-sensitive adaptation.** RL accounts often use fixed learning rates, but human data show adaptive learning-rate control with volatility estimates reflected in ACC during outcome monitoring [[raw/summaries/behrens2007_learning_value_information_uncertain|Behrens et al. 2007]]. That does not refute dopamine RPE, but it implies that TD-style learning in brains is likely modulated by uncertainty estimates outside the classic model.

## Open questions

- Which dopamine populations truly encode classical reward TD errors, and which encode other variables such as movement, salience, threat, or action deviation [[raw/summaries/lammel2014_dopamine_reward_aversion|Lammel et al. 2014]] [[raw/summaries/lee2019_dopamine_movement_selectivity|Lee et al. 2019]] [[raw/summaries/bogacz2020_dopamine_action_inference|Bogacz et al. 2020]]?

- How is the temporal state representation implemented biologically? The original TD accounts require a representation of cue history and reward timing, but the neural substrate for that representation remains unresolved [[raw/summaries/montague1996_predictive_hebbian_dopamine|Montague et al. 1996]] [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]].

- What circuit computes negative prediction errors, given low tonic firing and the asymmetry between increases and pauses in dopamine activity?

- Are dopamine waves causally necessary for credit assignment, or are they an epiphenomenal readout of upstream computations? Hamid et al. provide strong correlational evidence, but not causal proof [[raw/summaries/hamid2021_dopamine_waves_credit_assignment|Hamid et al. 2021]].

- How general is the projection-defined heterogeneity seen in mouse VTA to primates, where anatomical organization is less compact [[raw/summaries/lammel2014_dopamine_reward_aversion|Lammel et al. 2014]]?

- Does population diversity in dopamine responses instantiate distributional RL, or is “distributional” mostly a descriptive summary of mixed cell types and task variables [[raw/summaries/bakermans2020_reinforcement_learning_dopamine|Bakermans et al. 2020]] [[raw/summaries/lowet2020_distributional_reinforcement_brain|Lowet et al. 2020]]?

- How should action planning be integrated with dopamine teaching signals? Active-inference-inspired accounts such as DopAct are conceptually attractive, but the core predictions about separate reward and action-error dopaminergic loops need stronger direct tests [[raw/summaries/bogacz2020_dopamine_action_inference|Bogacz et al. 2020]].

## Key papers

- [[raw/summaries/montague1996_predictive_hebbian_dopamine|Montague et al. 1996]] — formalized the dopamine-as-TD-error hypothesis.
- [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]] — canonical physiological case for reward prediction error.
- [[raw/summaries/lammel2014_dopamine_reward_aversion|Lammel et al. 2014]] — projection-specific heterogeneity in reward and aversion circuits.
- [[raw/summaries/lee2019_dopamine_movement_selectivity|Lee et al. 2019]] — movement selectivity in dopamine neurons is not reducible to RPE.
- [[raw/summaries/hamid2021_dopamine_waves_credit_assignment|Hamid et al. 2021]] — dopamine waves as a candidate mechanism for spatiotemporal credit assignment.
- [[raw/summaries/bogacz2020_dopamine_action_inference|Bogacz et al. 2020]] — theory of distinct dopaminergic prediction errors for reward and action inference.
- [[raw/summaries/lowet2020_distributional_reinforcement_brain|Lowet et al. 2020]] — review of distributional RL as an alternative/refinement to scalar RPE.
- [[raw/summaries/campbell2025_hardwired_circuit_td_learning|Campbell et al. 2025]] — reported circuit-level implementation of TD computation in accumbens–VTA circuitry.

## Source papers
- [[raw/summaries/schultz1997_neural_substrate_reward_pred|Schultz et al. 1997]] | [[raw/mds/schultz1997_neural_substrate_reward_pred|source md]]: A Neural Substrate of Prediction and Reward
- [[raw/summaries/montague1996_predictive_hebbian_dopamine|Montague et al. 1996]] | [[raw/mds/montague1996_predictive_hebbian_dopamine|source md]]: A Framework for Mesencephalic Dopamine Systems Based on Predictive Hebbian Learning
- [[raw/summaries/lammel2014_dopamine_reward_aversion|Lammel et al. 2014]] | [[raw/mds/lammel2014_dopamine_reward_aversion|source md]]: Reward and aversion in a heterogeneous midbrain dopamine system
- [[raw/summaries/bogacz2020_dopamine_action_inference|Bogacz 2020]] | [[raw/mds/bogacz2020_dopamine_action_inference|source md]]: Dopamine role in learning and action inference
- [[raw/summaries/hamid2021_dopamine_waves_credit_assignment|Hamid et al. 2021]] | [[raw/mds/hamid2021_dopamine_waves_credit_assignment|source md]]: Wave-like dopamine dynamics as a mechanism for spatiotemporal credit assignment
- [[raw/summaries/bakermans2020_reinforcement_learning_dopamine|Bakermans et al. 2020]] | [[raw/mds/bakermans2020_reinforcement_learning_dopamine|source md]]: Reinforcement Learning: Full Glass or Empty — Depends Who You Ask
- [[raw/summaries/behrens2007_learning_value_information_uncertain|Behrens et al. 2007]] | [[raw/mds/behrens2007_learning_value_information_uncertain|source md]]: Learning the value of information in an uncertain world
- [[raw/summaries/campbell2025_hardwired_circuit_td_learning|Campbell et al. 2025]] | [[raw/mds/campbell2025_hardwired_circuit_td_learning|source md]]: A hardwired neural circuit for temporal difference learning
- [[raw/summaries/fiore2015_basal_ganglia_behavior|Fiore et al. 2015]] | [[raw/mds/fiore2015_basal_ganglia_behavior|source md]]: Evolutionarily conserved mechanisms for the selection and maintenance of behavioural activity
- [[raw/summaries/hauser2016_adhd_neural_gain|Hauser et al. 2016]] | [[raw/mds/hauser2016_adhd_neural_gain|source md]]: Computational Psychiatry of ADHD: Neural Gain Impairments across Marrian Levels of Analysis
