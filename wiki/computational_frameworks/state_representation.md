# State Representation

State representation refers to how agents encode and use information about the current situation to guide behaviour, ranging from simple sensory features to inferred latent variables.

---

## Current understanding

*Placeholder: Awaiting synthesis of key evidence.*

---

## Key evidence

- The anterior cingulate cortex (ACC) encodes predictions of specific future states that will result from chosen actions, based on the current action-state transition probability structure. Calcium imaging in mice showed ACC activity decoded all 10 locations in the task's state-action space with 95% accuracy; second-step state was the most strongly represented event; predicted second-step state rose pre-choice. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- Reward representations in the ACC are state-specific, with distinct encoding for rewards received in different task states rather than a generic reward signal. Calcium imaging showed reward representations were orthogonal for outcomes received in the two different second-step states; ACC encoded reward in a state-specific manner. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- Different populations of ACC neurons carry orthogonal pre-outcome and post-outcome state representations. Population analysis revealed two orthogonal representations of second-step state occurred sequentially (pre-outcome and post-outcome), carried by different neuronal populations. ([Akam 2021](../../raw/summaries/akam2021_anterior_cingulate_model.md))

- Extended-state strategies demonstrate that enriching the state representation allows model-free RL to approximate model-based behaviour. The reward-as-cue agent treats the combination of previous trial outcome and second-step state as a discriminative stimulus, learning a fixed stimulus-response mapping. The latent-state agent maintains a Bayesian belief over latent reward states and maps this belief to choice deterministically, producing behaviour nearly indistinguishable from model-based planning ([Akam 2015](../../raw/summaries/akam2015_two_step_task_simple_plans.md))

- The entorhinal cortex encodes the relational structure of abstract reinforcement learning problems, generalizing across different sensory exemplars of the same structure. This demonstrates that EC represents abstract task structure in a format that enables generalization to new sensory contexts, extending spatial cognitive map mechanisms to arbitrary relational structures ([Baram 2021](../../raw/summaries/baram2021_entorhinal_ventromedial_rl.md))

- The abstract relational map in mPFC is genuinely factorised, responding to positional commonality across isomorphic graphs rather than merely encoding within-graph distances. Cross-graph suppression (switch trials) was detected in mPFC, indicating representation of graph position independent of which specific stimulus occupies that position; this operationalises factorisation as defined by the Tolman-Eichenbaum Machine framework ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The abstract relational map in mPFC is genuinely factorised, responding to positional commonality across isomorphic graphs rather than merely encoding within-graph distances. Cross-graph suppression (switch trials) was detected in mPFC, indicating representation of graph position independent of which specific stimulus occupies that position; this operationalises factorisation as defined by the Tolman-Eichenbaum Machine framework ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md)).

---

## History of ideas

---

## Open questions

---

## Related pages

- [Model-based RL](model_based_rl.md)
- [Model-free RL](model_free_rl.md)
- [Latent State Inference](latent_state_inference.md)
