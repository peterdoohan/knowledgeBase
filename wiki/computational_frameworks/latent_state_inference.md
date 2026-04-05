# Latent State Inference

Latent state inference involves learning to identify unobservable states of the environment from observable evidence, enabling flexible behaviour in changing environments.

---

## Current understanding

*Placeholder: Awaiting synthesis of key evidence.*

---

## Key evidence

- The latent-state strategy maintains a Bayesian belief over which of two latent reward states the world is in (e.g., high reward in state a vs. state b) and maps this belief to choice deterministically. This produces behaviour that mimics model-based control on both one-trial-back and multi-lag analyses, with a similarly smooth decay of predictive weight at increasing lags. Discrimination from true model-based agents requires explicit model comparison, and differences in likelihood will be difficult to detect in typical experimental datasets of ~200 trials ([Akam 2015](../../raw/summaries/akam2015_two_step_task_simple_plans.md)).

---

## History of ideas

---

## Open questions

---

## Related pages

- [State Representation](state_representation.md)
- [Model-based RL](model_based_rl.md)
- [Bayesian Inference](bayesian_inference.md)
