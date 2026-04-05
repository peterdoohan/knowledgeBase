# Orbitofrontal Cortex (OFC)

## Current understanding

The orbitofrontal cortex (OFC) is a prefrontal region critical for flexible, value-guided decision-making. Rather than simply encoding cached reward values, the OFC computes the value of states within a cognitive map whose structure is learned and maintained by the hippocampus. This reframes "value coding" as state-value computation within a graph, enabling rapid inference-based choice when contingencies change.

## Key evidence

### OFC Theta Oscillations and Learning

- Closed-loop microstimulation that disrupts theta oscillations in the orbitofrontal cortex (OFC) causally impairs reward-based value learning in macaques. Closed-loop theta stimulation during the fixation epoch severely impaired learning (significantly more trials required to reach criterion; p < 0.0005 in both subjects, corrected). No other stimulation condition — including open-loop theta, late-fixation theta, beta closed-loop, outcome-epoch theta, or choice-epoch theta — had any significant effect on learning. ([Knudsen 2020](../../raw/summaries/knudsen2020_ofc_theta_learning.md))

- Theta phase alignment (not theta power per se) is the critical variable for learning. Closed-loop theta stimulation disrupted theta cross-trial phase alignment while paradoxically increasing theta power, reversing the normally positive power-phase alignment relationship (beta coefficient shifted from positive during sham to negative during stimulation; V: p = 2×10⁻¹⁹, T: p = 6×10⁻⁸). Cross-trial theta phase alignment increased specifically during drift periods (when animals were actively relearning values), particularly in the fixation epoch. ([Knudsen 2020](../../raw/summaries/knudsen2020_ofc_theta_learning.md))

- OFC neurons encode value information preferentially at specific theta phases during learning. Approximately 37–65% of OFC neurons were theta phase-locked. About 37–54% of OFC neurons encoded current picture values in their firing rates during the fixation epoch; value encoding was stronger during drift than stable periods and was greater when firing rates were aligned to the theta oscillation versus jittered (2-way ANOVA, F > 1000, p < 10⁻¹⁵ for both subjects). Closed-loop theta stimulation significantly reduced neuronal value encoding in OFC; beta stimulation had no such effect. ([Knudsen 2020](../../raw/summaries/knudsen2020_ofc_theta_learning.md))

- Stimulation did not significantly alter single-neuron firing rates, confirming that behavioural and oscillatory effects were not due to non-specific suppression of neural activity (F < 2, p > 0.1 for all conditions). ([Knudsen 2020](../../raw/summaries/knudsen2020_ofc_theta_learning.md))

### Hippocampal-OFC Interaction

- HPC and OFC theta oscillations were synchronised (high PLV) during fixation and choice epochs. HPC-OFC theta synchrony tracked the learning cycle: it decreased at drift onset and recovered as animals relearned new values. ([Knudsen 2020](../../raw/summaries/knudsen2020_ofc_theta_learning.md))

- GPDC directional analysis showed that influence during drift was predominantly in the HPC→OFC direction. ([Knudsen 2020](../../raw/summaries/knudsen2020_ofc_theta_learning.md))

- Closed-loop theta stimulation of HPC (not OFC) impaired learning equivalently to OFC stimulation and disrupted bidirectional HPC-OFC theta influence (whereas OFC stimulation only reduced OFC→HPC influence), suggesting HPC drives OFC theta. ([Knudsen 2020](../../raw/summaries/knudsen2020_ofc_theta_learning.md))

### Cognitive Map and State-Value Computation

- OFC damage consistently impairs model-based (inference-based) tasks but spares model-free (cached value) tasks, implicating OFC in state-transition graph-dependent computations rather than value caching per se. ([Knudsen 2022](../../raw/summaries/knudsen2022_ofc_cognitive_map.md))

- The vmPFC/OFC uniquely encodes all task states necessary to specify a cognitive map in a human neuroimaging study (Schuck et al. 2016), and the quality of this representation predicts task performance. ([Knudsen 2022](../../raw/summaries/knudsen2022_ofc_cognitive_map.md))

- Hippocampal neurons encode "value place fields" — sparse, relational representations of reward values across pictures, analogous to spatial place fields — while OFC neurons encode value more linearly and densely, producing a complementary code. ([Knudsen 2022](../../raw/summaries/knudsen2022_ofc_cognitive_map.md))

- OFC neurons encode hypothetical as well as actual outcomes, consistent with using the state-transition graph to generate value predictions for unchosen options. ([Knudsen 2022](../../raw/summaries/knudsen2022_ofc_cognitive_map.md))

- A proposed division of labour: hippocampus learns and represents the state-transition graph; OFC integrates reward information to compute the value of graph nodes, enabling flexible, inference-based choice. ([Knudsen 2022](../../raw/summaries/knudsen2022_ofc_cognitive_map.md))

### Economic Value and State Representation

- OFC neurons in area 13 encode economic value of offered and chosen goods independently of visuospatial configuration and motor response; 54% of recorded neurons had activity modulated by offer type, with offer value, chosen value, and taste explaining 79% of offer-type-modulated responses, while fewer than 5% of neurons showed dependence on spatial position or motor response direction ([Padoa-Schioppa 2006](../../raw/summaries/padoaschioppa2006_orbitofrontal_economic_value.md))

- Value coding in OFC follows a temporal sequence: offer value → chosen value → taste, with chosen value emerging during the delay before the go signal, providing a process-level account of evaluation unfolding from valuation to selection to consumption coding ([Padoa-Schioppa 2006](../../raw/summaries/padoaschioppa2006_orbitofrontal_economic_value.md))

- Chosen-value responses in OFC track subjective (not physical) value, covarying with behavioral relative value across sessions and juice pairs (regression slope ratio k* = behavioral relative value n*), establishing genuine subjective value coding ([Padoa-Schioppa 2006](../../raw/summaries/padoaschioppa2006_orbitofrontal_economic_value.md))

- Human orbitofrontal cortex encodes a cognitive map of task-relevant hidden states, with multivariate fMRI decoding showing 16-way classification accuracy of 12.2% (chance = 6.25%, p < 0.001); decoding fidelity correlates with lower error rates (r = -0.58, p = 0.002) ([Schuck 2016](../../raw/summaries/schuck2016_orbitofrontal_cortex_state.md))

- OFC selectively encodes hidden, task-relevant state components (previous category, previous age, current category all significantly decoded at p < 0.02) but not observable (current age, p > 0.72) or task-irrelevant information (p > 0.66), demonstrating curated representations for task relevance ([Schuck 2016](../../raw/summaries/schuck2016_orbitofrontal_cortex_state.md))

- Decoding accuracy in OFC decreases in trials preceding behavioral errors, dropping from 11% (5 trials before error) to 4.2% on error trials (mixed-effects model p = 0.03), providing evidence that OFC state representations are functionally relevant for decision-making ([Schuck 2016](../../raw/summaries/schuck2016_orbitofrontal_cortex_state.md))

- OFC represents abstract task-state identity (a pointer to the current state) rather than just expected reward value, serving as a cognitive map for learning and decision-making in downstream structures; multivariate decoding shows OFC encodes all unobservable task-state components while filtering out task-irrelevant information ([Niv 2019](../../raw/summaries/niv2019_representation_learning_task_states.md))

- Orbitofrontal cortex (OFC) provides covert reward signals after the animal commits to a path during VTE, encoding outcome-specific reward expectations post-decision, distinct from ventral striatum which provides pre-decision evaluation ([Redish 2016](../../raw/summaries/redish2016_vicarious_trial_error.md))

- Orbitofrontal cortex computes option-specific state-value functions with extended temporal scope, representing reward value in a context- and option-dependent manner according to the hierarchical RL framework ([Botvinick 2008](../../raw/summaries/botvinick2008_hierarchical_behavior_prefrontal.md); [Botvinick 2009](../../raw/summaries/botvinick2009_hierarchical_behavior_reinforcement.md))

- OFC neurons develop abstract schema representations that generalize across learning problems with identical structure but different sensory stimuli. Cross-problem decoding showed strong correlations between canonical components from different problems emerged with learning. ([Zhou 2021](../../raw/summaries/zhou2021_schema_orbitofrontal.md))

- OFC neural representations converge onto a common low-dimensional solution across different subjects. Cross-subject decoding showed neural representations converged on common solution across rats; first three canonical components showed increasingly strong relationships to same task features. ([Zhou 2021](../../raw/summaries/zhou2021_schema_orbitofrontal.md))

- OFC dimensionality reduction accelerates with experience across successive problems. Percentage of variance explained by first three LDA components increased from day 1 to day 15; poke latency patterns reflecting schema knowledge emerged more quickly across successive problems. ([Zhou 2021](../../raw/summaries/zhou2021_schema_orbitofrontal.md))

- OFC neural schema decomposes into components representing current value, odour overlap, and positional alternation. First three canonical components developed clear relationships to specific task features: CC1 to current value, CC2 to odour overlap, CC3 to positional alternation. ([Zhou 2021](../../raw/summaries/zhou2021_schema_orbitofrontal.md))

- OFC neurons persistently encode the animal's future navigational destination throughout a journey, forming an internal goal map. 80.8% of OFC neurons showed spatial tuning; 86.9% showed conjunctive coding of position and navigation phase; goal well representation emerged ~1.1s before motion onset and was maintained throughout journey. ([Basu 2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC goal representation is causally necessary for accurate navigation. Optogenetic perturbation at motion onset increased navigational errors significantly (P = 0.020); pharmacogenetic silencing also increased error rates; effect specific to destination selection not motor execution. ([Basu 2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC represents the chosen goal rather than the correct goal, tracking the animal's decision. In error trials, OFC population activity decoded the animal's incorrect destination as accurately as correct goal in correct trials; goal coding tracks chosen destination including errors. ([Basu 2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC goal identity is encoded orthogonally to the direction of neural trajectory evolution during navigation. Axis of maximal goal-well separability was nearly orthogonal to direction of neural trajectory evolution; linear dynamic model reproduced both correct and error trial trajectories from motion onset. ([Basu 2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- Agranular orbitofrontal cortex (OFC) connectivity with striatum, amygdala, hippocampus, hypothalamus, and thalamus is largely conserved across rat and macaque, with anterior-posterior parcellation providing the best cross-species alignment. ([Izquierdo 2024](../../raw/summaries/izquierdo2024_prefrontal_cortex_homology.md))

- Rat frontal cortex subregions show less functional specialization than primate OFC and ACC, exhibiting redundant theta-band signals during reversal learning and both impairing confidence reporting when inhibited, contrasting with the OFC/ACC division of labor for stimuli vs. actions seen in primates. ([Izquierdo 2024](../../raw/summaries/izquierdo2024_prefrontal_cortex_homology.md))

- OFC neurons persistently encode the animal's future navigational destination throughout a journey ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC goal coding is viewpoint-invariant and represents the chosen (not correct) goal ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC activity at navigation onset is causally necessary for accurate goal selection ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals ([Basu2021](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- Hippocampus-OFC implements two-system architecture: hippocampus encodes current position, OFC encodes goal ([Basu2021](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- Ventral hippocampal inputs are necessary for OFC's representation of target direction during decision-making ([Basu2021](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation ([Basu2021](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- OFC neurons persistently encode the animal's future navigational destination throughout a journey ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC goal coding is viewpoint-invariant and represents the chosen (not correct) goal ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC activity at navigation onset is causally necessary for accurate goal selection ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals ([Basu2023](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- Hippocampus-OFC implements two-system architecture: hippocampus encodes current position (SR/map), OFC encodes goal (reward vector) ([Basu2023](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- Ventral hippocampal inputs are necessary for OFC's representation of target direction during decision-making ([Basu2023](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- OFC neurons persistently encode the animal's future navigational destination throughout a journey ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC goal coding is viewpoint-invariant and represents the chosen (not correct) goal ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC activity at navigation onset is causally necessary for accurate goal selection ([Basu2021](../../raw/summaries/basu2021_ofc_navigation_goals.md))

- OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals ([Basu2023](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- Hippocampus-OFC implements two-system architecture: hippocampus encodes current position (SR/map), OFC encodes goal (reward vector) ([Basu2023](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- Ventral hippocampal inputs are necessary for OFC's representation of target direction during decision-making ([Basu2023](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

## History of ideas

The OFC has long been understood primarily as a region that signals reward value to guide decision-making, based on neurophysiological recordings in non-human primates and decision deficits in patients with OFC lesions. This "value hypothesis" dominated the field, with OFC neurons shown to encode economic value independent of action (Padoa-Schioppa & Assad, 2006). However, a wave of newer studies using more complex tasks suggested the OFC may encode a much richer "cognitive map" — a structured representation of the relationships between states of the world. The current synthesis reconciles these views: the OFC computes the value of states within a cognitive map whose structure is learned by the hippocampus. This reframes "value coding" as state-value computation within a graph, rather than a domain-specific function.

The discovery that OFC theta oscillations are causally necessary for reward learning (Knudsen & Wallis, 2020) provided a mechanistic basis for understanding how hippocampal and OFC representations are coordinated. The finding that hippocampus drives OFC theta during learning, and that disrupting this interaction impairs value updating, places OFC in a hippocampal-dependent circuit for model-based reinforcement learning.

## Open questions

- What are the specific cellular and synaptic mechanisms by which theta phase locking organizes value-coding neurons in OFC?
- How does the OFC-hippocampal circuit handle conflicts between learned values and new reward information during rapid contingency changes?
- What is the precise division of labor between OFC subregions (lateral, medial, central) for value versus map functions?
- How are state representations in OFC updated when the task structure changes (transition revaluation)?
- Do OFC neurons encode the successor representation directly, or only state values given a learned structure?

## Related pages

- [[hippocampus]]
- [[ventromedial_prefrontal_cortex]]
- [[cognitive_map]]
- [[model_based_rl]]
- [[model_free_rl]]
- [[successor_representation]]
- [[reward_processing]]
- [[theta_oscillations]]
- [[value_encoding]]
- [[decision_making]]
