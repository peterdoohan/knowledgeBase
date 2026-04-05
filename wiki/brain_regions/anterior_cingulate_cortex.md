# Anterior Cingulate Cortex (ACC)

## Current understanding

The anterior cingulate cortex (ACC) is a critical node for model-based reinforcement learning, serving as an action-outcome predictor that generates specific predictions about future states resulting from chosen actions. Rather than simply encoding reward values or outcome surprise, the ACC maintains an internal model of action-state transition probabilities and uses this to predict the specific consequences of actions.

The ACC implements a forward model that predicts which future state an action will lead to, given the current transition probability structure. These predictions are updated through learning from experienced transitions, and when predictions are violated (rare transitions), the ACC registers state-prediction surprise signals distinct from reward prediction errors.

A key insight is that ACC activity during the inter-trial interval (between outcome and next choice) is causally necessary for translating state prediction information into behavioral updates. Inhibition of ACC during this period selectively impairs the influence of state transitions on subsequent choices without affecting basic reward-driven reinforcement. This establishes ACC as selectively necessary for model-based but not model-free control.

At the population level, the ACC encodes the full task state-action space with high fidelity. Reward representations are not generic but state-specific, with orthogonal encoding for rewards received in different task states. Different neuronal populations carry distinct pre-outcome and post-outcome state representations, suggesting orthogonal coding of anticipated versus observed states.

## Key evidence

- The ACC encodes predictions of specific future states that will result from chosen actions, based on the current action-state transition probability structure. Calcium imaging in mice showed ACC activity decoded all 10 locations in the task's state-action space with 95% accuracy; second-step state was the most strongly represented event; predicted second-step state rose pre-choice. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- The ACC encodes state-prediction surprise signals that indicate whether an action-state transition was common or rare, distinct from reward prediction errors. Regression analysis showed ACC represented whether transitions were common or rare (state prediction surprise) post-choice; this was specific to transition probability context, not reward probability context. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- ACC activity between trial outcome and subsequent choice is causally necessary for using state transition information to update behavior, but not for basic reward-driven reinforcement. Optogenetic inhibition of ACC from trial outcome to next choice selectively reduced the influence of state transitions on subsequent choice (p=0.007, Bonferroni corrected) without affecting direct reward reinforcement; effect size correlated with individual MB weight (R=-0.91, p=0.0001). ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- The ACC is causally necessary for model-based but not model-free reinforcement learning. Optogenetic inhibition selectively impaired model-based control (reduced influence of state transitions on choice) without affecting model-free reward-driven reinforcement; no significant effect in simpler reversal learning task where MB and MF agree. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- Reward representations in the ACC are state-specific, with distinct encoding for rewards received in different task states rather than a generic reward signal. Calcium imaging showed reward representations were orthogonal for outcomes received in the two different second-step states; ACC encoded reward in a state-specific manner. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- Different populations of ACC neurons carry orthogonal pre-outcome and post-outcome state representations. Population analysis revealed two orthogonal representations of second-step state occurred sequentially (pre-outcome and post-outcome), carried by different neuronal populations. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- Anterior cingulate cortex BOLD signal during outcome monitoring reflects estimated environmental volatility, with ACC being the only region surviving correction for multiple comparisons in the monitor × volatility interaction (MNI: x=–6, y=26, z=34 mm; max Z=4.2) ([Behrens 2007](../../raw/summaries/behrens2007_learning_value_information_uncertain.md))

- The ACC volatility signal is robust to confounds and cannot be explained by alternative variables including reward, reaction time, prediction error, error likelihood, or local reward variance ([Behrens 2007](../../raw/summaries/behrens2007_learning_value_information_uncertain.md))

- Individual differences in ACC volatility response predict individual differences in learning rate across subjects (r²=0.27, P<0.01), providing a direct link from neural signal to behavioral parameter ([Behrens 2007](../../raw/summaries/behrens2007_learning_value_information_uncertain.md))

- Both estimated volatility and posterior variance on reward rate independently contribute to ACC BOLD signal, suggesting ACC tracks both expected uncertainty (posterior variance) and unexpected uncertainty (volatility changes) ([Behrens 2007](../../raw/summaries/behrens2007_learning_value_information_uncertain.md))

- Agranular anterior cingulate cortex (ACC) connectivity with striatum, amygdala, hippocampus, hypothalamus, and thalamus is largely conserved across rat and macaque, providing a valid cross-species anchor for comparing frontal cortex function. ([Izquierdo 2024](../../raw/summaries/izquierdo2024_prefrontal_cortex_homology.md))

- Bidirectional DREADD manipulation of ACC pyramidal neurons (CaMKII promoter) in rats impairs effort-based choice whether population activity is increased or decreased, and population-level calcium activity (not single cells) is the best predictor of choice, consistent with a role for E/I balance in value computation. ([Izquierdo 2024](../../raw/summaries/izquierdo2024_prefrontal_cortex_homology.md))

- Bilateral optogenetic silencing of ACC excitatory neurons during action selection rapidly and reversibly impairs mice's preference to exert greater physical effort for a larger reward in a barrier T-maze task, establishing a causal, temporally precise role for ACC activity in effort-based decision making. ([Kashay 2022](../../raw/summaries/kashay2022_anterior_cingulate_effort.md))

- Single neurons in the ACC encode the value of choice outcomes across multiple decision variables (probability, payoff, effort cost) with higher prevalence than LPFC or OFC. 40% of neurons encoded reward presence/absence (58% in ACC vs 32% LPFC vs 27% OFC); 33% encoded payoff value (46% ACC vs 30% OFC vs 25% LPFC); 23% encoded effort cost (33% ACC vs 21% OFC vs 16% LPFC). ([Kennerley 2009](../../raw/summaries/kennerley2009_frontal_outcome_value.md))

- ACC neurons encode outcome information earlier than LPFC and OFC, with median latency for reward-presence encoding of 230ms (ACC) vs 320ms (OFC) vs 430ms (LPFC). ([Kennerley 2009](../../raw/summaries/kennerley2009_frontal_outcome_value.md))

- ACC neurons show greater multi-variable multiplexing than OFC or LPFC, with many neurons encoding outcomes across two or more decision variables simultaneously. ([Kennerley 2009](../../raw/summaries/kennerley2009_frontal_outcome_value.md))

- Frontal outcome encoding in ACC is distinct from dopamine-like prediction errors, showing bidirectional value tuning rather than unidirectional RPE signals. ([Kennerley 2009](../../raw/summaries/kennerley2009_frontal_outcome_value.md))

- ACC silencing during the choice phase itself (start gate through choice point) produces the largest effect on effort-based choices; silencing during the start box (pre-trial preparation) also impairs high-reward choices, while silencing confined to the home cage ITI has no effect. ([Kashay 2022](../../raw/summaries/kashay2022_anterior_cingulate_effort.md))

- When effort is equalized by adding a second barrier to the low-reward arm, mice initially perseverate in choosing the formerly low-reward arm under ACC silencing but quickly adjust, ruling out impaired spatial memory, capacity to climb, or reward preference as explanations. ([Kashay 2022](../../raw/summaries/kashay2022_anterior_cingulate_effort.md))

- ACC silencing significantly increases time in the approach zone (pre-choice-point) on high-effort trials, introducing frequent micropauses into otherwise ballistic trajectories; micropauses are nearly absent on control trials but common under silencing, specifically for high-reward choices. ([Kashay 2022](../../raw/summaries/kashay2022_anterior_cingulate_effort.md))

- ACC silencing does not reduce struggling in the tail suspension test or alter average velocity in an open field, indicating effects are specific to goal-directed decision-making contexts rather than general motor or effort deficits. ([Kashay 2022](../../raw/summaries/kashay2022_anterior_cingulate_effort.md))

- Optogenetic silencing of ACC excitatory neurons during action selection acutely impairs mice's preference to exert effort for larger rewards, with the largest effects occurring when silencing is restricted to the choice period (start gate through choice point) ([Kashay 2023](../../raw/summaries/kashay2023_ACC_effort_decision.md))

- ACC silencing introduces frequent micropauses into goal-directed movement trajectories specifically during high-effort choices, chunking movements into discrete segments and increasing time in the approach zone ([Kashay 2023](../../raw/summaries/kashay2023_ACC_effort_decision.md))

## History of ideas

Early models of ACC function emphasized its role in conflict monitoring, error detection, and reward prediction error signaling. The influential computational framework by Alexander and Brown (2011) proposed a fundamental shift in understanding: that ACC functions as an action-outcome predictor, generating expected outcomes of specific actions rather than simply monitoring for errors or reward outcomes.

Prior to Akam et al. (2021), empirical evidence for this action-outcome prediction framework came primarily from human neuroimaging studies showing MB value signals and state prediction errors in anterior/mid-cingulate regions, and lesion work in macaques demonstrating ACC necessity for action-outcome learning. However, these studies did not dissociate state prediction from reward prediction, nor did they establish causal necessity specifically for model-based versus model-free control.

The dominant view before this study was that ACC monitors outcomes and signals errors, but its specific role in predicting future states (as opposed to reward values) and its causal necessity for model-based (but not model-free) reinforcement learning had not been demonstrated. The Alexander and Brown model provided theoretical grounding, but direct empirical tests were lacking, particularly in rodent models with cellular-resolution recordings and causal manipulations.

Akam et al. (2021) established a new empirical foundation by showing that ACC specifically predicts future states given actions, signals state-prediction errors, and is causally necessary for using transition structure to guide behavior. This shifted the understanding of ACC from a generic monitoring system to a specific state-prediction mechanism essential for model-based control.

## Open questions

- What is the specific role of ACC activity at the time of state transition (before outcome) versus during the inter-trial interval? Is the pre-transition period critical for encoding state prediction errors, or is the post-outcome period the key locus?
- Does the state-prediction surprise signal reflect the state prediction error per se, or its motor-action consequences?
- What is the mechanistic basis of the behavioral difference between fixed and changing transition-probability task variants? Do stronger MB influences, latent-state inference with habitual strategies, or successor representations explain this difference?
- How do recording locations and homologies between rodent and primate ACC compare? Can findings be generalized across species?
- Does the ACC represent latent task states (block structure) or forward action-state transition models? Can these roles be fully distinguished?
- What are the downstream circuits through which ACC model-based signals influence behavior? The posterior dorsomedial striatum is implicated but the specific pathways remain to be characterized.
- How does ACC interact with other brain regions (hippocampus, prefrontal cortex, striatum) during model-based decision-making? Are state predictions computed in ACC or received from other regions?

## Related pages

- [Model-based reinforcement learning](../computational_frameworks/model_based_rl.md)
- [Model-free reinforcement learning](../computational_frameworks/model_free_rl.md)
- [State representation](../computational_frameworks/state_representation.md)
- [Two-step task](../behaviours/two_step_task.md)
- [Goal-directed behaviour](../behaviours/goal_directed_behaviour.md)
- [Habits](../behaviours/habits.md)
- [Prefrontal cortex](prefrontal_cortex.md)
- [Effort-based decision making](../behaviours/effort_based_decision_making.md)
