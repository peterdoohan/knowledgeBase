# Temporal Difference (TD) Learning

Temporal difference (TD) learning is a foundational reinforcement learning algorithm for learning predictions about future rewards. It provides a computational framework for understanding how agents can learn from delayed feedback without requiring complete episode outcomes.

---

## Current understanding

TD learning solves the problem of predicting future rewards by using bootstrapping — updating predictions based on other predictions. The core insight is that predictions at time t should be consistent with predictions at time t+1, plus any immediate reward received. This creates a locally computable prediction error signal that can drive learning even when the final outcome is far in the future.

---

## Key evidence

- The temporal difference (TD) learning algorithm provides a formal account of dopamine neuron activity, where the prediction error signal δ(t) = r(t) + γV̂(t+1) - V̂(t) matches observed dopamine responses: positive when outcomes are better than expected, zero when expectations match, and negative when outcomes are worse than expected ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- The TD framework explains the shift of dopamine responses from primary rewards to reward-predicting cues with learning: as the value function V̂(t) is updated, the prediction error at the time of the fully-predicted reward approaches zero, while errors occur at the earlier predictive cue ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- The TD framework provides a quantitative account of blocking and secondary conditioning phenomena in classical conditioning, explaining why learning is sometimes prevented when outcomes are fully predicted ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- The TD prediction error signal can serve dual purposes: learning predictions (critic function) and guiding action selection (actor function) through connection to dynamic programming principles ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- The RL formalism defines an agent in an environment selecting actions to maximize cumulative reward; the central quantities are state values V(s), action values Q(s,a), and reward-prediction errors (RPEs) δ = r + γV(s') − V(s). This TD error serves as the learning signal for value updates and matches dopaminergic activity patterns ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- The integration of deep learning and RL uses the RPE as the error signal for backpropagation, updating weights throughout the network. Key stabilization mechanisms include experience replay and target networks, which address the instability that arises from correlating learning with the data being learned ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- TDRL predictions about dopamine dynamics are systematically contradicted by empirical data measuring nucleus accumbens core dopamine release. TDRL predicts dopamine responses should decrease to unpredicted rewards over sessions, correlate negatively with inter-reward intervals, and emerge simultaneously with behavioral learning; however, empirical data show the opposite pattern in all cases, supporting ANCCR instead ([Jeong 2022](../../raw/summaries/jeong2022_mesolimbic_dopamine_causal.md))

- D1-MSN stimulation drives VTA dopamine neurons via a hardwired biphasic linear filter that computes a temporal difference, demonstrating that TD error calculations are built into the dopamine-striatum microcircuit; optogenetic stimulation of lNAc D1-MSNs with 7 graded patterns produced dopamine responses matching TD error predictions including negative steady-state, with LTI model CV R^2 = 0.81 ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

- The temporal discount factor gamma is hardwired in the D1-MSN to dopamine circuit and set by the balance of excitatory and inhibitory components; bootstrapped median gamma = 0.53 discount/sec from optotagged dopamine neurons, matching independent behavioral estimate of 0.56 from Masset et al. 2025; gamma = e^(-sigma) where sigma is LTI model pole ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

- TD computation is conserved across striatal subregions with region-specific parameters: biphasic impulse responses observed in lNAc, DMS, and DLS with cross-validated R^2 = 0.64-0.92; DLS showed faster dynamics (shorter time to minimum, P=0.01); gamma closer to 1 for DMS and DLS vs lNAc ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

---

## History of ideas

The TD learning algorithm was developed in the engineering and artificial intelligence literature (Sutton & Barto, 1981, 1987, 1988) before being connected to neuroscience. The Rescorla-Wagner model (1972) provided a psychological foundation for understanding prediction errors in classical conditioning. The critical insight connecting TD learning to dopamine neurons came from Montague, Dayan & Sejnowski (1996) and was elaborated in this 1997 review by Schultz, Dayan & Montague, which synthesized diverse experimental observations into a unified computational framework.

---

## Open questions

- How is the complete serial-compound stimulus representation (required by TD learning) biologically implemented in the brain?
- What are the time scales of prediction that dopamine-mediated TD learning can support?
- How does the brain handle the credit assignment problem when multiple stimuli contribute to a prediction error?
- How does the scalar TD error signal enable discrimination between different reward types and sensory cues?

---

## Related pages

- [[reinforcement_learning]]
- [[model_based_rl]]
- [[model_free_rl]]
- [[reward_prediction_error]]
- [[ventral_tegmental_area]]
- [[conditioning]]
