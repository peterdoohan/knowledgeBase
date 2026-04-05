# Model-Free Reinforcement Learning

Model-free RL learns action values directly from experience through prediction errors, without building an explicit model of the environment.

---

## Current understanding

*Placeholder: Awaiting synthesis of key evidence.*

---

## Key evidence

- The ACC is causally necessary for model-based but not model-free reinforcement learning. Optogenetic inhibition selectively impaired model-based control (reduced influence of state transitions on choice) without affecting model-free reward-driven reinforcement; no significant effect in simpler reversal learning task where MB and MF agree. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- A pure Q(1) model-free agent can show a spurious transition-outcome interaction in stay probability on the reduced two-step task, which is classically interpreted as a signature of model-based behavior ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- The spurious transition-outcome interaction in Q(1) model-free agents arises from correlations between action values at trial onset and subsequent trial events, not from prospective planning. Mathematical analysis shows that Q(1) agents maintain eligibility traces from previous trials, creating correlations between first-step action values and trial events that mimic model-based evaluation ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- Including a 'correct' predictor in logistic regression (repeat the choice that was correct on the previous trial) eliminates the spurious transition-outcome interaction for Q(1) agents and serves as an effective correction. A continuous version based on the reward-probability difference between states is required when reward probabilities follow random walks ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- A reward-as-cue agent (model-free RL over 4 states defined by previous outcome × second-step state) learns a fixed stimulus-response mapping that produces a strong transition-outcome interaction indistinguishable from model-based behavior by one-trial-back analysis. This extended state representation enables sophisticated model-free behavior that mimics planning ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- Reward-as-cue strategies can only be detected by lagged regression showing no multi-trial integration, distinguishing them from true model-based planning. While they produce strong stay-probability interactions, they show no multi-trial reward history effects (unlike true model-based agents which integrate across trials) ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- Both extended-state agents (reward-as-cue and latent-state) outperform classical model-free strategies in reward obtained, providing an incentive for their acquisition with extended training. Agents using extended state representations achieve higher cumulative reward than pure Q(0) or Q(1) agents, suggesting why animals might develop these strategies ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- The model-based/model-free dissociation should be viewed as a spectrum rather than a binary distinction, with state representation learning as a key unmeasured variable in the two-step task. Extended state representations create a continuum between pure model-free and pure model-based strategies, making binary classification inadequate ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- The successor representation occupies an intermediate position between model-based and model-free reinforcement learning systems, offering a principled computational tradeoff; SR is more flexible than model-free systems (which are computationally cheap but inflexible to environmental change) but more efficient than full model-based systems ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- Offline (rest-period) replay correlates with model-free rigidity and reflects consolidation of habitual policies; off-task forward sequenceness during rest correlated negatively with Index of Flexibility (more rest-replay in less flexible, more model-free subjects) ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

---

## History of ideas

---

## Open questions

---

## Related pages

- [Reinforcement Learning](reinforcement_learning.md)
- [Model-based RL](model_based_rl.md)
- [Two-step task](../behaviours/two_step_task.md)
