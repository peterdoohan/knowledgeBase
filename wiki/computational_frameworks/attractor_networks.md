# Attractor Networks

## Current understanding

*Placeholder - to be synthesised from accumulated evidence.*

## Key evidence

- A belief-instability parameter (κ₁) derived from attractor network principles best accounts for schizophrenia's nonlinear belief-updating pattern, outperforming simple learning-rate and disconfirmatory-bias models across two independent datasets. ([Adams 2018](../../raw/summaries/adams2018_attractor_schizophrenia.md))
- Belief instability (κ₁) and response stochasticity (ζ) are co-elevated in schizophrenia and negatively correlated across subjects, consistent with a shared neurobiological origin in unstable attractor dynamics. ([Adams 2018](../../raw/summaries/adams2018_attractor_schizophrenia.md))
- Nonpsychotic mood disorder patients showed the same elevated belief instability and response stochasticity as schizophrenia patients when acutely unwell, but these parameters normalised after recovery, contrasting with the persistent trait-like differences in schizophrenia. ([Adams 2018](../../raw/summaries/adams2018_attractor_schizophrenia.md))

- Delusions emerge from conditional dependencies among multiple parameters in active inference, with no single parameter being both necessary and sufficient; reduced likelihood precision, policy precision, habit strength, and affective state interact to produce self-reinforcing attractor states. ([Adams 2021](../../raw/summaries/adams_delusions_inference_attractors.md))

- State-space analysis reveals three agent trajectories: those forming habits that can be revised (low false inferences), those forming habits that partially fail to revise (intermediate), and those forming very strong habits with increasing policy precision that create self-reinforcing attractor states (high false inferences). ([Adams 2021](../../raw/summaries/adams_delusions_inference_attractors.md))

- Grid cells in the medial entorhinal cortex demonstrate attractor-like dynamics where firing fields are attracted toward learned goal locations, causing long-lasting deformations of the spatial map. Field attraction strength correlates with pre-probe distance to goal (~30 cm threshold), suggesting an attractor basin around goal locations. ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- The hippocampal-entorhinal circuit exhibits "flickering" dynamics—rapid alternation between discrete attractor states representing pre-learning and post-learning spatial maps during goal learning, with no intermediate representations. This suggests the circuit stores multiple stable spatial maps as distinct attractor states that can coexist and be dynamically accessed. ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Continuous attractor networks of ~10^4 neurons can accurately integrate velocity inputs to produce stable grid responses over biologically relevant timescales (1-10 minutes, 10-100 metres), provided network size is sufficient and neural noise is sub-Poisson ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- A deterministic periodic (toroidal) network of 128^2 neurons accumulates only ~15 cm positional error over 260 m / 20 minutes (average < 0.1 cm/m), demonstrating accurate path integration is achievable in principle ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- In periodic attractor networks, rotations of the population pattern are forbidden by the attractor manifold (energy cost of rotation is non-zero); in aperiodic networks, rotations are flat in energy and driven by noise or velocity input coupling ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- Noise-driven drift in attractor networks is diffusive: D_trans ∝ CV² / N. For a periodic 128^2 network with CV = 1 (Poisson spiking), coherent integration is maintained for ~400 s; for CV = 0.5 (sub-Poisson), duration roughly quadruples ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- Analysis of real dMEC recordings confirms grid cell spiking is significantly sub-Poisson, consistent with the requirement for accurate integration in attractor network models ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- The head direction circuit in the anterior dorsal nucleus of thalamus (ADn) implements a ring attractor, with neural activity constrained to a 1-dimensional ring manifold that is isometric with head direction and invariant across waking and REM sleep. Direct visualization of the ring manifold using thousands of simultaneously recorded neurons confirms states flow back to the ring after perturbations. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

- Grid cell modules in the medial entorhinal cortex (MEC) implement a toroidal continuous attractor, forming a 2-dimensional torus invariant across environments, sleep/wake states, and time. Grid cell co-activity preserved across sleep while place cell co-activity is not validates continuous attractor models and rules out place-cell-primacy models. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

- The oculomotor integrator implements a line attractor where network-level (not cellular) integration maintains stable eye position through recurrent feedback that precisely cancels activity decay. Single neurons lack cellular persistence; network inactivation degrades integration time-constant. EM reconstruction confirms excitatory-ipsilateral, inhibitory-contralateral connectivity predicted by line attractor models. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

- Premotor area ALM exhibits discrete bistable attractor dynamics during delay periods: perturbations are either corrected or flip state, consistent with a two-attractor landscape. Optogenetic perturbations during delay-response tasks reveal bistability; network tends to return to or flip between two discrete attractor states. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

- Prefrontal cortex delay-period activity exhibits diffusive bump dynamics on a 1-dimensional manifold, consistent with continuous attractor working memory models. Bump displacement predicts behavioural error in spatial working memory tasks; population activity flows on a low-dimensional manifold. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

- Modular and mixed-modular attractor architectures can achieve exponentially large representational capacity while maintaining noise-robustness, overcoming the capacity-robustness tradeoff. M independent K-dimensional attractor modules can represent ~N^M discrete states; mixed-modular coding enables zero-shot learning. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

- Locally correlated (coherent) noise enables spiking networks to switch between deterministic exploitation and probabilistic sequence replay strategies, while uncorrelated noise of any amplitude cannot achieve this due to population-level averaging ([Bouhadjar 2022](../../raw/summaries/bouhadjar2022_coherent_noise_sequence_replay.md))

- Uncorrelated noise averages out at population level (variance scales as 1/ρ with population size ρ), leaving recall effectively deterministic regardless of amplitude; coherent noise is required for probabilistic behavior in population-coded systems ([Bouhadjar 2022](../../raw/summaries/bouhadjar2022_coherent_noise_sequence_replay.md))

- Random stimulus locking to spatiotemporal oscillations (travelling waves) at physiological frequencies (alpha 10 Hz, beta 30 Hz, gamma 70 Hz) replicates the full exploration-exploitation strategy continuum, providing a biologically plausible source of locally coherent noise ([Bouhadjar 2022](../../raw/summaries/bouhadjar2022_coherent_noise_sequence_replay.md))

- Neurons in the medial frontal cortex (mFC) are organized into modular ring attractor structures that encode behavioral sequences through goal-progress tuning. Pairwise coherence analysis and hierarchical clustering revealed mFC neurons form modules with preserved within-module state-tuning relationships across task instances (silhouette scores significantly above permuted controls, Wilcoxon, N=24 days, P=0.003). ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

- State tuning in mFC does not generalize across tasks but is anchored to specific goal-progress/place conjunctions, contradicting the associative binding model. State-tuning angles shifted across distinct tasks (proportion generalising = 20%, below chance of 25%; z=9.04, P<0.001), while state preferences were highly conserved across repeated sessions of the same task (87% stable, P<0.001). ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

- Sleep co-activity in mFC shows ring-shaped offline organization consistent with the Structured Memory Buffer model. During sleep, co-anchored neuron pairs closer in circular task-space showed greater co-activity (regression coefficient for circular distance significantly negative, t=-1.656, P=0.049), with ring structure present in both pre- and post-task sleep. ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

## History of ideas

*Placeholder - to be synthesised from historical_context annotations.*

## Open questions

*Placeholder - to be populated from open questions in the literature.*

## Related pages

- [[belief_updating]]
- [[schizophrenia]]
- [[delusions]]
- [[active_inference]]
- [[hierarchical_gaussian_filter]]
- [[computational_psychiatry]]
- [[response_stochasticity]]
- [[mood_disorders]]
- [[prefrontal_cortex]]
- [[state_vs_trait]]
