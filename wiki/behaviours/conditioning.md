# Classical Conditioning

Classical conditioning is a fundamental form of associative learning where organisms learn to predict biologically significant events (unconditioned stimuli, US) from neutral predictive cues (conditioned stimuli, CS). It provides a model system for studying how predictions are formed and updated based on experience.

---

## Current understanding

Classical conditioning is understood as a process of learning predictive relationships between stimuli. The Rescorla-Wagner model formalized this as error-driven learning, where associations are updated based on the discrepancy between expected and actual outcomes. The temporal difference (TD) learning framework extends this to account for the timing of predictions, explaining how responses can shift from the unconditioned stimulus to earlier predictive cues as learning progresses.

---

## Key evidence

- Dopamine neuron responses in classical conditioning shift from primary rewards (unconditioned stimuli) to reward-predicting conditioned stimuli with learning; after conditioning, the primary reward no longer elicits phasic dopamine responses if fully predicted ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- When an expected reward is omitted in classical conditioning paradigms, dopamine neurons show a phasic depression below baseline firing rate at the precise time the reward should have occurred, indicating an internal representation of expected reward timing ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- The temporal difference (TD) learning framework provides a quantitative account of blocking and secondary conditioning phenomena in classical conditioning, explaining why learning is prevented when outcomes are fully predicted and how new stimuli can acquire predictive value through association with already-predictive cues ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- Dopamine neurons do not respond to conditioned stimuli that predict aversive outcomes (air puffs, saline), indicating that the dopamine prediction error signal specifically encodes appetitive value rather than general salience or arousal ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

---

## History of ideas

Classical conditioning as a phenomenon was first systematically studied by Pavlov in the early 20th century. The Rescorla-Wagner model (1972) provided the first formal computational account, introducing the concept of error-driven learning. Kamin's (1969) blocking phenomenon showed that learning requires prediction errors, not just contiguity. The temporal difference learning framework, developed by Sutton and Barto (1981, 1987), extended these ideas to account for the temporal dynamics of prediction. The critical connection to neuroscience came in the 1990s when Schultz and colleagues demonstrated that dopamine neurons encode TD prediction errors, providing a neural substrate for the computational principles of classical conditioning.

---

## Open questions

- How does the brain implement the complete serial-compound stimulus representation required for TD learning?
- What neural mechanisms enable the precise timing representations needed for dopamine depression at omitted rewards?
- How does the brain handle compound stimuli where multiple cues predict the same outcome?
- What distinguishes appetitive from aversive prediction error systems?

---

## Related pages

- [[temporal_difference_learning]]
- [[reinforcement_learning]]
- [[reward_prediction_error]]
- [[ventral_tegmental_area]]
- [[dopamine]]
- [[blocking]]
- [[secondary_conditioning]]
