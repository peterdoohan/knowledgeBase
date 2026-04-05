# Successor Representation

The successor representation (SR) is a computational framework in reinforcement learning that caches expected discounted future feature occupancy, separating long-run state prediction from immediate reward computation.

---

## Current understanding

*No content yet — will be synthesised from Key evidence once sufficient facts are collected.*

---

## Key evidence

- The successor representation occupies an intermediate position between model-based and model-free reinforcement learning systems, offering a principled tradeoff between computational efficiency and flexibility; it is more flexible than model-free systems (which are computationally cheap but inflexible to environmental change) but more efficient than model-based systems (which are flexible but computationally costly) ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- The SR predicts asymmetric revaluation behavior: reward devaluation produces rapid value updating (because the reward function is factored out of the SR), whereas transition devaluation produces slow updating (because the SR encodes compiled transition statistics); Momennejad et al. (2017) confirmed this asymmetry in humans, providing first direct behavioral evidence distinguishing SR from pure model-based or model-free systems ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- Human revaluation behavior is best explained by a mixture of SR-based and model-based strategies, with model-based computation incrementally refining SR-based value estimates when transition structure changes; this cooperative framework (Russek et al., 2017) suggests SR and model-based systems work together rather than operating as isolated alternatives ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- The successor representation (SR) account of dopamine faces a critical dimensionality problem: the rat brain has ~17 million cortico-striatal neurons but only ~70,000 midbrain dopamine neurons, making it implausible that dopamine carries the high-dimensional vector-valued SR prediction error ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- The SR account does not naturally predict the large body of quantitative RPE-consistent data, including findings that dopamine neuron stimulation is strongly reinforcing — a phenomenon well-explained by scalar RPE theory ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- The SR account fails to explain the specificity required for optogenetic dopamine stimulation to unblock stimulus-stimulus learning (C→X) without recruiting neurons specifically selective for predictions about X ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- Both humans and rats navigate using successor representation strategies rather than pure model-based or model-free approaches, with SR agent providing best fit for both species (70% human trials, 60% rat trials; SR vs. MF log-likelihood ratio = 1911.1 for humans, 842.0 for rats) ([de Cothi 2022](../../raw/summaries/decothi2022_predictive_spatial_navigation.md))

- Trajectory diffusivity and clustering show both humans and rats fall closest to SR agent behavior; t-SNE clustering showed distinct agent clusters with both species closest to SR (humans: SR vs. MF t(17) = −55.7, p < 0.001; rats: SR vs. MF t(8) = −11.1, p < 0.001) ([de Cothi 2022](../../raw/summaries/decothi2022_predictive_spatial_navigation.md))

- The neural metric for relational knowledge in entorhinal cortex follows successor representation/communicability rather than Euclidean or link distance, indicating the system warps relational space according to expected future visitation ([Garvert 2017](../../raw/summaries/garvert2017_relational_knowledge_maps.md))

- Anterior PFC encodes the longest predictive horizons (up to ~875 m) while posterior hippocampus encodes the shortest (~25 m), demonstrating a multiscale successor-representation hierarchy across hippocampal and prefrontal gradients; fMRI RSA during naturalistic virtual navigation with gamma values 0.1-0.9 corresponding to 25-875m horizons ([Brunec 2022](../../raw/summaries/brunec2022_predictive_representations_hierarchies.md))

- Goal-directed navigation shows longer and stronger predictive representations than GPS-guided navigation, with top-down goal representations shaping spatial scale of predictive coding; gamma x condition interaction F(2,1448)=7.49, p<0.001; goal-directed condition showed enhanced antPFC and aHPC predictive similarity at longer horizons ([Brunec 2022](../../raw/summaries/brunec2022_predictive_representations_hierarchies.md))

- Path distance modulates predictive representations oppositely in antPFC vs hippocampus: longer routes strengthen antPFC predictive signals but weaken hippocampal representations; antPFC: F(1,149)=91.51, p<0.001, eta_p^2=0.38; hippocampus showed opposite trend with weaker signals for longer routes, suggesting PFC carries global planning representation while hippocampus remains locally scoped ([Brunec 2022](../../raw/summaries/brunec2022_predictive_representations_hierarchies.md))

---

- OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals ([Basu2021](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- Hippocampus-OFC implements two-system architecture: hippocampus encodes current position, OFC encodes goal ([Basu2021](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

## History of ideas

---

## Open questions

---

## Related pages

- [Model-based RL](model_based_rl.md)
- [Model-free RL](model_free_rl.md)
- [Reinforcement Learning](reinforcement_learning.md)
- [State Representation](state_representation.md)
