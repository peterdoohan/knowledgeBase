# Two-Step Task

The two-step task is a behavioral paradigm developed to dissociate model-based from model-free reinforcement learning strategies in humans and animals.

---

## Current understanding

*Placeholder: Awaiting synthesis of key evidence.*

---

## Key evidence

- A two-step task with periodically reversing action-state transition probabilities enables dissociation of state prediction from reward prediction signals. The novel task design with transition probability reversals (unlike the original Daw 2011 task) prevented confounded habitual strategies and enabled independent measurement of state vs. reward prediction in neural activity. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- A pure Q(1) model-free agent can show a spurious transition-outcome interaction in stay probability on the reduced two-step task, which is classically interpreted as a signature of model-based behavior. This occurs on the reduced task (80/20 transitions, block-based reward probabilities) due to correlations between action values at trial onset and subsequent trial events ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- The original two-step task with higher stochasticity (70/30 common/rare transitions) decorrelates trial-start action values from subsequent events, eliminating the confound seen in the reduced task. The spurious interaction is very weak (P = 0.01) in the original task compared to the reduced task ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- Including a 'correct' predictor in logistic regression (repeat the choice that was correct on the previous trial) eliminates the spurious transition-outcome interaction for Q(1) agents and serves as an effective correction. A continuous version based on the reward-probability difference between states is required when reward probabilities follow random walks ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- A reward-as-cue agent (model-free RL over 4 states defined by previous outcome × second-step state) learns a fixed stimulus-response mapping that produces a strong transition-outcome interaction indistinguishable from model-based behavior by one-trial-back analysis. This extended state representation enables sophisticated model-free behavior that mimics planning ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- Reward-as-cue strategies can only be detected by lagged regression showing no multi-trial integration, distinguishing them from true model-based planning. While they produce strong stay-probability interactions, they show no multi-trial reward history effects (unlike true model-based agents which integrate across trials) ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- A latent-state agent (Bayesian inference over two latent world states + fixed state-action mapping) produces behavior qualitatively identical to a model-based agent on both stay probability and lagged logistic regression analyses. Agents performing Bayesian inference over latent task states produce identical stay probability patterns and multi-trial integration effects as true model-based agents ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- The two-step task's ability to dissociate model-based from model-free strategies is more fragile than assumed; extended state representations can approximate or match model-based performance without prospective planning. The binary MB/MF dissociation fails because extended-state strategies occupy a middle ground, producing model-like signatures without world models ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

- The model-based/model-free dissociation should be viewed as a spectrum rather than a binary distinction, with state representation learning as a key unmeasured variable in the two-step task. Extended state representations create a continuum between pure model-free and pure model-based strategies, making binary classification inadequate ([Akam 2015](../../raw/summaries/akam2015_two_step_task_habits.md))

---

## History of ideas

---

## Open questions

---

## Related pages

- [Model-based RL](../computational_frameworks/model_based_rl.md)
- [Model-free RL](../computational_frameworks/model_free_rl.md)
- [Decision Making](decision_making.md)
- [Planning](planning.md)
