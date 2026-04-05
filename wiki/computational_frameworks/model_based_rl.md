# Model-Based Reinforcement Learning

Model-based RL uses an internal model of the environment (including transition probabilities and reward structure) to plan actions prospectively.

---

## Current understanding

*Placeholder: Awaiting synthesis of key evidence.*

---

## Key evidence

- The anterior cingulate cortex (ACC) encodes predictions of specific future states that will result from chosen actions, based on the current action-state transition probability structure. Calcium imaging in mice showed ACC activity decoded all 10 locations in the task's state-action space with 95% accuracy; second-step state was the most strongly represented event; predicted second-step state rose pre-choice. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- The ACC encodes state-prediction surprise signals that indicate whether an action-state transition was common or rare, distinct from reward prediction errors. Regression analysis showed ACC represented whether transitions were common or rare (state prediction surprise) post-choice; this was specific to transition probability context, not reward probability context. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- ACC activity between trial outcome and subsequent choice is causally necessary for using state transition information to update behavior, but not for basic reward-driven reinforcement. Optogenetic inhibition of ACC from trial outcome to next choice selectively reduced the influence of state transitions on subsequent choice (p=0.007, Bonferroni corrected) without affecting direct reward reinforcement; effect size correlated with individual MB weight (R=-0.91, p=0.0001). ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- The ACC is causally necessary for model-based but not model-free reinforcement learning. Optogenetic inhibition selectively impaired model-based control (reduced influence of state transitions on choice) without affecting model-free reward-driven reinforcement; no significant effect in simpler reversal learning task where MB and MF agree. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- Reward representations in the ACC are state-specific, with distinct encoding for rewards received in different task states rather than a generic reward signal. Calcium imaging showed reward representations were orthogonal for outcomes received in the two different second-step states; ACC encoded reward in a state-specific manner. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- Different populations of ACC neurons carry orthogonal pre-outcome and post-outcome state representations. Population analysis revealed two orthogonal representations of second-step state occurred sequentially (pre-outcome and post-outcome), carried by different neuronal populations. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- A latent-state agent (Bayesian inference over two latent world states + fixed state-action mapping) produces behavior qualitatively identical to a model-based agent on both stay probability and lagged logistic regression analyses. Agents performing Bayesian inference over latent task states produce identical stay probability patterns and multi-trial integration effects as true model-based agents ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- Latent-state and model-based agents can only be discriminated by maximum likelihood model comparison on large datasets; differences are highly significant (P < 10⁻⁵) but small in magnitude. While MLE can statistically distinguish latent-state from model-based agents, the effect sizes are small and require large datasets (>10,000 trials), making discrimination difficult in typical experiments with ~200 trials ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- The two-step task's ability to dissociate model-based from model-free strategies is more fragile than assumed; extended state representations can approximate or match model-based performance without prospective planning. The binary MB/MF dissociation fails because extended-state strategies occupy a middle ground, producing model-like signatures without world models ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- The model-based/model-free dissociation should be viewed as a spectrum rather than a binary distinction, with state representation learning as a key unmeasured variable in the two-step task. Extended state representations create a continuum between pure model-free and pure model-based strategies, making binary classification inadequate ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- An alternative account of dopamine in model-based RL — well-informed scalar reward prediction error (RPE) plus a separate scalar surprise signal — can explain dopamine's involvement without requiring high-dimensional signaling ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- Model-based value estimates can inform dopaminergic RPEs through three mechanisms: (a) offline planning during hippocampal sharp-wave ripples that refines cached values; (b) predictive representations such as the SR that allow rapid value recomputation; and (c) possibly minimal single-step rollouts gated by theta phase resetting ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- A scalar dopaminergic surprise signal can upregulate learning rates in cortical and hippocampal predictive models, explaining stimulus-stimulus learning without requiring vector-valued state prediction errors ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- The abstract relational map in mPFC is genuinely factorised, responding to positional commonality across isomorphic graphs rather than merely encoding within-graph distances. Cross-graph suppression (switch trials) was detected in mPFC, indicating representation of graph position independent of which specific stimulus occupies that position; this operationalises factorisation as defined by the Tolman-Eichenbaum Machine framework ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The MTL maintains concrete, stimulus-specific graph representations while mPFC develops abstract representations, suggesting a division of labour between these systems across consolidation that enables model-based RL generalisation. MTL showed both relevant and irrelevant graph representations simultaneously across both sessions (no abstraction), while mPFC showed emergence of cross-graph abstraction over days; this pattern aligns with systems consolidation theory where MTL maintains episodic specifics while neocortex extracts statistical structure ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The successor representation occupies an intermediate position between model-based and model-free reinforcement learning systems, offering a principled computational tradeoff; SR is more flexible than model-free systems (which are computationally cheap but inflexible to environmental change) but more efficient than model-based systems that use full prospective planning ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- Human revaluation behavior is best explained by a mixture of SR-based and model-based strategies, with model-based computation incrementally refining SR-based value estimates when transition structure changes; this suggests SR and model-based systems cooperate rather than operate as isolated alternatives, with model-based mechanisms refining cached SR estimates when the environment changes ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- During goal-directed navigation, forward replay encodes paths from current location to goal, and replay content strongly correlates with subsequent behavior, suggesting hippocampal forward replay implements model-based planning by simulating future trajectories ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Pfeiffer & Foster (2013) showed forward replay predicts behavior; this supports the view of forward replay as mental simulation for model-based planning.

- Online (on-task) replay correlates with model-based planning flexibility and predicts policy re-evaluation; forward sequenceness positively correlated with Index of Flexibility (mean β = 0.17) and predicted policy changes (+11.1% reward improvement) ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

- Offline replay during the critical rest period following reward-contingency change included replay of subsequently chosen (newly planned) transitions, indicating offline replay can serve model-based re-planning functions ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

- Advance planning is evident in neural representations before choice and outcome; chosen second moves were decodeable during first-move choices and prior to first-outcome onset; early decodability correlated with Index of Flexibility (β = 0.29) ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

---

## History of ideas

---

## Open questions

---

## Related pages

- [Reinforcement Learning](reinforcement_learning.md)
- [Model-free RL](model_free_rl.md)
- [Two-step task](../behaviours/two_step_task.md)
- [Planning](../behaviours/planning.md)
