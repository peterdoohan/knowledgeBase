# Medial Prefrontal Cortex

The medial prefrontal cortex (mPFC) is a collection of prefrontal areas situated along the medial surface of the frontal lobe in rodents (encompassing anterior cingulate cortex, prelimbic cortex, and infralimbic cortex) and primates. It supports executive functions, decision-making, emotional regulation, and working memory, and is implicated in numerous psychiatric disorders including schizophrenia, ADHD, addiction, and depression.

## Current understanding

*Placeholder - to be synthesised from accumulated evidence.*

## Key evidence

- Neurons in the medial frontal cortex (mFC) are organized into modular ring attractor structures that encode behavioral sequences through goal-progress tuning. Pairwise coherence analysis and hierarchical clustering revealed mFC neurons form modules with preserved within-module state-tuning relationships across task instances (silhouette scores significantly above permuted controls, Wilcoxon, N=24 days, P=0.003). ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

- Goal-progress tuning is the dominant signal in mFC, with 80% of neurons tuned to fractional progress between consecutive goals independent of specific locations or trajectories. GLM analysis showed 80% of mFC neurons were significantly tuned to goal-progress (one-sample t-test vs. 0, N=1438, P=2.71×10⁻⁸²), with tuning independent of elapsed time, physical distance, speed, and acceleration. ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

- State tuning in mFC does not generalize across tasks but is anchored to specific goal-progress/place conjunctions, contradicting the associative binding model. State-tuning angles shifted across distinct tasks (proportion generalising = 20%, below chance of 25%; z=9.04, P<0.001), while state preferences were highly conserved across repeated sessions of the same task (87% stable, P<0.001). ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

- mFC neurons form mnemonic fields at fixed task-space lags from specific goal-progress/place anchors, enabling distal behavioral prediction. Three convergent cross-validation analyses confirmed state-tuned neurons fire at fixed lags in task-space from specific anchors (t-tests against 0, all P<0.001), and neuronal activity at 'bump time' predicted the animal's choice to visit the anchor on the following trial (regression coefficient significantly positive, P=0.017). ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

- Sleep co-activity in mFC shows ring-shaped offline organization consistent with the Structured Memory Buffer model. During sleep, co-anchored neuron pairs closer in circular task-space showed greater co-activity (regression coefficient for circular distance significantly negative, t=-1.656, P=0.049), with ring structure present in both pre- and post-task sleep. ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

- Prediction errors drive schema learning through updates to world models in mPFC. State prediction errors enhance memory for violating content and support updating of world models in rodents and humans. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Hierarchical RL accounts for schema hierarchy through temporal abstraction in mPFC. Grouping states and actions into subtasks defined by subgoals maps onto how sub-schemas are chunked within larger schemas. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Dimensionality reduction in mPFC underlies schema abstraction. fMRI evidence shows mOFC/vmPFC encodes low-dimensional, abstract task representations; fewer PCA components needed for simpler categorization rules. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- mPFC guides memory reactivation in posterior regions during schema-consistent retrieval. mPFC activity precedes and predicts hippocampal and ventral-temporal activity during retrieval; schema consistency modulates mPFC functional connectivity toward posterior cortex vs hippocampus. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Abstract representations are found in anterior and dorsal mPFC; specific representations in posterior and ventral mPFC. Proposed gradient hypothesis based on heterogeneous studies; more abstract/future-oriented representations in anterior/dorsal mPFC. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Experienced mice demonstrate zero-shot transfer of abstract task structure to new scenarios on the first trial. Mice performing late tasks took the most direct d→a path on the very first trial of new tasks significantly above chance (Wilcoxon, P=0.009), with first-trial performance improving across tasks (one-way repeated-measures ANOVA, F=3.10, P=0.010). ([El-Gaby 2023](../../raw/summaries/elgaby2023_behavioral_structure_mapping.md))

- Medial prefrontal cortex tracks event structure through sustained activity during within-community periods and transient disengagement at boundaries. mPFC showed sustained activity during within-community periods and transient disengagement at community boundaries (P<0.05 corrected), consistent with tracking event structure rather than surprise. ([Schapiro 2013](../../raw/summaries/schapiro2013_event_representation_memory.md))

- The medial prefrontal cortex (mPFC) develops an abstract, stimulus-independent relational map of learned graph structure over the course of several days following initial learning. fMRI repetition suppression revealed a large mPFC cluster (peak t21 = 5.1, MNI [2, 42, 8]; FWE p = 0.003) showing cross-graph suppression that was significantly greater in session 2 than session 1 (SVC FWE p < 0.05, t21 = 3.66), indicating emergence of abstract representation via consolidation ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The abstract relational map in mPFC is genuinely factorised, responding to positional commonality across isomorphic graphs rather than merely encoding within-graph distances. Cross-graph suppression (switch trials) was detected in mPFC, indicating representation of graph position independent of which specific stimulus occupies that position; this operationalises factorisation as defined by the Tolman-Eichenbaum Machine framework ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The abstract mPFC representation emerges in the same pregenual mPFC region previously implicated in grid-like coding of abstract 2D spaces. The session-2 cross-graph effect emerged within an mPFC ROI defined by grid-like coding from Constantinescu et al. (2016) (SVC FWE p = 0.03, t21 = 2.38), and the peak coordinates (MNI [2, 42, 8]) overlapped with the grid-like coding region ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- Representational similarity analysis confirms the emergence of a full abstracted map in right pregenual mPFC from session 1 to session 2. RSA showed a cluster in right pregenual mPFC with emergence of full abstracted map (both within- and across-graph RDM elements) from session 1 to session 2 (SVC FWE p = 0.01); within-graph (p = 0.06) and across-graph (p = 0.11) showed trends, each surviving SVC in the other's mask (p = 0.03 and p = 0.01), suggesting shared representational substrate ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The MTL maintains concrete, stimulus-specific graph representations while mPFC develops abstract representations, suggesting a division of labour between these systems across consolidation. MTL showed both relevant and irrelevant graph representations simultaneously across both sessions (no abstraction), while mPFC showed emergence of cross-graph abstraction over days ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- During awake hippocampal sharp-wave ripples, the medial prefrontal cortex shows coordinated excitation and inhibition of distinct ensembles, with approximately 35% of mPFC neurons significantly modulated (18% excited, 17% inhibited) ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)).

- SWR-excited and SWR-inhibited mPFC cells form functionally distinct ensembles with different spatial coding properties: excited cells have more diffuse spatial firing and higher rates at faster movement speeds, while inhibited cells have concentrated firing around reward sites and low speeds, suggesting content-specific gating of PFC representations during hippocampal replay ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)).

- The medial prefrontal cortex generates independent awake trajectory replay during rule-switching tasks, with replay temporally independent from hippocampal replay (~5% co-occurrence) despite co-occurring with hippocampal SWRs at above-chance rates (40%) ([Kaefer 2020](../../raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md)).

- mPFC replay rate during rule-switching positively predicts behavioral performance: higher mPFC replay rates correlate with faster rule switching (center: r = −0.76, p = 0.01; goal: r = −0.63, p = 0.02), while hippocampal replay at the goal shows the opposite correlation (r = 0.71, p = 0.009), demonstrating distinct functional roles ([Kaefer 2020](../../raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md)).

- The mPFC holds a generalized, trajectory-independent spatial code representing relative position (start-to-goal) rather than specific allocentric locations, unlike the hippocampus which shows no improvement with 1D position decoding (16 ± 3 cm error vs. 46 ± 3 cm for 2D in mPFC) ([Kaefer 2020](../../raw/summaries/kaefer2020_mpfc_replay_ruleswitchal.md)).

### Agranular architecture

- The mPFC is agranular — it lacks a canonical L4 — so thalamic and other long-range inputs are distributed across L1–L6, unlike sensory cortex where primary thalamic input targets L4 ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

### Projection neuron diversity

- Projection neurons span L2–L6 and fall into three major classes (intratelencephalic/IT, pyramidal tract/PT, corticothalamic/CT), each with distinct morphology, intrinsic physiology, and subcellular properties; the mPFC has more broadly distributed corticostriatal and corticoclaustral neurons than sensory cortex ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

### Long-range input specificity

- Long-range inputs are laminar- and cell-type-specific: BLA preferentially targets L2 cortico-amygdalar neurons; mediodorsal (MD) thalamus strongly drives L3 IT cells; ventromedial (VM) thalamus enriches inputs at the distal apical dendrites of L5 PT cells (a motif not seen in sensory cortex); ventral hippocampus (vHPC) preferentially targets L5 IT cells ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

### Reciprocal loop architecture

- Many long-range inputs preferentially contact neurons that project back to the input region, providing a synaptic basis for strong reciprocal loops (e.g. BLA↔mPFC, mPFC↔thalamus) ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

### Local excitatory circuit directionality

- In local excitatory circuits, IT cells strongly innervate PT cells (but not vice versa), imposing a directional flow that ensures local computations are funnelled into output pathways ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

### Interneuron biased connectivity

- mPFC has fewer PV+ interneurons but more SOM+ and CCK+ cells than sensory cortex; PV+, SOM+, CCK+, and NDNF+ interneurons all show biased inhibitory connectivity, preferentially targeting L5 PT cells over IT cells ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

### Input-specific interneuron recruitment

- Long-range inputs recruit distinct interneuron populations: cPFC targets PV+ basket and chandelier cells; MD drives PV+ and SOM+ cells in L3 and VIP+ cells in L1b; VM drives NDNF+ cells in L1a; vHPC activates CCK+ interneurons that show endocannabinoid-mediated presynaptic modulation specifically at IT cell synapses ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

### Disinhibitory circuits

- Disinhibitory circuits exist in the mPFC: VIP+ cells target SOM+ cells; NDNF+ cells in L1 target PV+ cells in L2/3; these allow long-range inputs to gate inhibitory tone in a pathway-specific manner ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

### Dorsoventral gradient

- Wiring rules differ along the dorsoventral axis: BLA and vHPC show graded innervation across ACC, PL, and IL, with distinct laminar and cell-type targeting in each subregion ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

- RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition ([Basu2021](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation ([Basu2021](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Gradient hypothesis: more abstract/future-oriented representations are found in anterior and dorsal mPFC ([Basu2021](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition ([Bein2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation ([Bein2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Gradient hypothesis: more abstract/future-oriented representations are found in anterior and dorsal mPFC ([Bein2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition ([Bein2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation ([Bein2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Gradient hypothesis: more abstract/future-oriented representations are found in anterior and dorsal mPFC ([Bein2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

## History of ideas

*Placeholder - to be synthesised from historical_context annotations.*

- SWR-unmodulated mPFC neurons have superior spatial tuning (0.33 bits/spike) compared to SWR-modulated neurons (0.22 bits/spike for excited, 0.11 for inhibited; p<.001), and also show higher directional selectivity (0.48 vs 0.37 vs 0.27, p<.001) ([den Bakker 2024](../../raw/summaries/denbakker2024_mpfc_spatial_swr.md))

### Theta Coordination with Hippocampus

- Theta-frequency (4–12 Hz) synchronisation between hippocampal CA1 and medial prefrontal cortex is selectively enhanced during the working-memory and decision-making epochs of a spatial alternation task, and is attenuated on error trials, demonstrating that theta rhythms provide a dynamic mechanism for cross-structural coordination. ([Jones 2005](../../raw/summaries/jones2005_theta_hippocampal_prefrontal.md))

- CA1–mPFC neuron-pair cross-correlations are significantly higher during choice (working-memory) epochs than forced-turn epochs on the same section of maze (0.024 vs. 0.009; p < 0.01). Error trials showed intermediate but significantly reduced correlations (0.015; p < 0.05 vs. correct). ([Jones 2005](../../raw/summaries/jones2005_theta_hippocampal_prefrontal.md))

- mPFC neurons show significantly higher circular-concentration (κ) to CA1 theta during choice-correct runs than forced-turn runs (0.19 vs. 0.10; p < 0.01). CA1 phase-locking to its own theta is stable across epochs (κ ≈ 0.43–0.53), indicating the modulation is specific to mPFC coupling. ([Jones 2005](../../raw/summaries/jones2005_theta_hippocampal_prefrontal.md))

- Theta-band (4–12 Hz) CA1–mPFC LFP coherence is significantly elevated during choice-correct vs. forced-turn epochs (0.32 vs. 0.19; p < 0.05) and reduced on error trials (0.20; p < 0.05 vs. correct). No consistent coherence is observed at delta or frequencies above 12 Hz. ([Jones 2005](../../raw/summaries/jones2005_theta_hippocampal_prefrontal.md))

- mPFC firing carries more spatial information (bits per spike) during choice epochs coinciding with enhanced phase-locking. ([Jones 2005](../../raw/summaries/jones2005_theta_hippocampal_prefrontal.md))

- SWR-unmodulated mPFC neurons drive predictive non-local representations of upcoming choice, while SWR-modulated neurons do not; non-local representations decoded from SWR-unmodulated cells were significantly better than chance (p<.001), while models from SWR-modulated cells were not (p=.135); mPFC prediction index preceded behavioral change by ~6-8 trials after rule switch ([den Bakker 2024](../../raw/summaries/denbakker2024_mpfc_spatial_swr.md))

- Prediction errors drive schema learning through updates to world models in mPFC. State prediction errors enhance memory for violating content and support updating of world models in rodents and humans. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Hierarchical RL accounts for schema hierarchy through temporal abstraction in mPFC. Grouping states and actions into subtasks defined by subgoals maps onto how sub-schemas are chunked within larger schemas. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Dimensionality reduction in mPFC underlies schema abstraction. fMRI evidence shows mOFC/vmPFC encodes low-dimensional, abstract task representations; fewer PCA components needed for simpler categorization rules. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- mPFC guides memory reactivation in posterior regions during schema-consistent retrieval. mPFC activity precedes and predicts hippocampal and ventral-temporal activity during retrieval; schema consistency modulates mPFC functional connectivity toward posterior cortex vs hippocampus. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Abstract representations are found in anterior and dorsal mPFC; specific representations in posterior and ventral mPFC. Proposed gradient hypothesis based on heterogeneous studies; more abstract/future-oriented representations in anterior/dorsal mPFC. ([Bein 2024](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- mPFC non-local representations are independent of hippocampal SWRs and theta, while hippocampal representations are SWR- and theta-locked; mPFC decoded segments were not more time-locked to SWRs or biased to theta phase, while hippocampus upcoming-choice representations were significantly more frequent at SWR onset (p=.004) and phase-locked to rising theta phase ([den Bakker 2024](../../raw/summaries/denbakker2024_mpfc_spatial_swr.md))

- SWR-modulated mPFC neurons respond to hippocampal non-local replay content but do not drive prospective mPFC coding; SWR-excited mPFC neurons fired more during hippocampal representations of upcoming choice, while SWR-inhibited neurons fired more during representations of alternative choice; SWR modulation strength greater in ventral than dorsal mPFC (p=.038) ([den Bakker 2024](../../raw/summaries/denbakker2024_mpfc_spatial_swr.md))

- mPFC neurons gradually acquire category selectivity during rule-based visual categorization learning, with 9.8% becoming category-selective after learning rule 1; category-tuning index (CTI) quantifies selectivity as the ratio of between-category to within-category firing rate differences ([Reinert 2021](../../raw/summaries/reinert2021_mouse_prefrontal_categorization.md))

- Go- and NoGo-preferring category-selective populations in mPFC show distinct learning dynamics: Go neurons emerge rapidly (ad hoc, T2-T5) reflecting early choice/reward learning, while NoGo neurons emerge gradually (T4-T5) accumulating with categorization demand ([Reinert 2021](../../raw/summaries/reinert2021_mouse_prefrontal_categorization.md))

- After a rule-switch, Go category-selective mPFC neurons remap their stimulus selectivity while NoGo category-selective neurons are replaced by a new population; 8.6% of neurons encoded new categories after rule-switch while rule 1 selectivity dropped to 0.07% ([Reinert 2021](../../raw/summaries/reinert2021_mouse_prefrontal_categorization.md))

- 4.3% of mPFC neurons are uniquely category-modulated, not explained by choice, reward, or uninstructed behaviors (whisking, eye movements, posture); linear regression decomposition identifies abstract category signal independent of motor and reward confounds ([Reinert 2021](../../raw/summaries/reinert2021_mouse_prefrontal_categorization.md))

- Approximately 25% of prelimbic/infralimbic mPFC neurons have spatial correlates during goal-directed navigation, with fields concentrated at goal locations; 69/272 PL/IL neurons showed place fields with 77% of fields centered on goal trigger zone or food landing zone (chi-squared=47.6, p<0.0001) ([Hok 2005](../../raw/summaries/hok2005_goal_coding_prefrontal.md))

- PL/IL place fields are larger and less spatially coherent than hippocampal place cells, suggesting a coarse goal-centered gradient representation; spatial coherence 0.48 vs 0.68 for hippocampus; field size larger at mean-rate threshold (146 vs 114 pixels) ([Hok 2005](../../raw/summaries/hok2005_goal_coding_prefrontal.md))

- Goal-related firing in mPFC reflects motivational salience of goal locations rather than reward consumption itself, dissociated by spatial separation of trigger zone and food landing zone; relocating feeder shifted landing zone fields while rotating cue card did not; comparable firing during navigation vs foraging episodes ([Hok 2005](../../raw/summaries/hok2005_goal_coding_prefrontal.md))

- mPFC inactivation leaves hippocampal place cell goal-related firing intact but reduces place field overdispersion, suggesting mPFC modulates firing variability rather than average spatial structure; lidocaine inactivation of PL/IL; goal-zone firing rate unchanged (1.17 vs 1.46 Hz, NS); overdispersion significantly reduced (Levene's W=17.850, p<0.001) ([Hok 2013](../../raw/summaries/hok2013_prefrontal_place_cells.md))

- mPFC inactivation increases peak firing rate and spatial coherence within place field centers without affecting spatial selectivity or field size; peak firing rate increased (t(52)=3.047, p<0.01); spatial coherence elevated (p<0.05); spatial information content and field size unchanged ([Hok 2013](../../raw/summaries/hok2013_prefrontal_place_cells.md))

- The mPFC generates independent awake trajectory replay during rule-switching tasks, with replay temporally independent from hippocampal replay (~5% co-occurrence) despite co-occurring with hippocampal SWRs at above-chance rates (40%) ([Kaefer 2020](../../raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md))

- mPFC replay rate during rule-switching positively predicts behavioral performance: higher mPFC replay rates correlate with faster rule switching (center: r = −0.76, p = 0.01; goal: r = −0.63, p = 0.02), while hippocampal replay shows the opposite correlation (r = 0.71, p = 0.009), demonstrating distinct functional roles ([Kaefer 2020](../../raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md))

- The mPFC holds a generalized, trajectory-independent spatial code representing relative position (start-to-goal) rather than specific allocentric locations, with 1D Bayesian decoding yielding 16±3 cm error vs. 46±3 cm for 2D ([Kaefer 2020](../../raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md))

- mPFC disruption with inhibitory DREADDs specifically impairs post-learning consolidation SWRs while sparing on-maze SWRs; SWR rate increase from pre-maze to post-maze rest was significantly reduced on CNO days (F(1,49)=8.36, p=.0057; interaction F(1,49)=10.9, p=.0018), while on-maze SWRs showed no effect (p=.21) ([Schmidt 2021](../../raw/summaries/schmidt2021_mpfc_swr_dreadd.md))

- mPFC disruption alters the content of planning-related SWRs, increasing non-local representations; on CNO days, Waiting epoch SWRs showed increased non-local decoding compared to VEH, with reduced differentiation between Current and other restaurants ([Schmidt 2021](../../raw/summaries/schmidt2021_mpfc_swr_dreadd.md))

- Prefrontal cortex maintains abstract, sensorimotor-invariant representations of task structure that generalize across problems; cellular modes (co-activating neuron assemblies) generalized significantly better in PFC than CA1 (p < .05), with PFC showing stronger abstract representation of trial stage and outcome (p < .001) ([Samborska 2021](../../raw/summaries/samborska2021_hippocampus_prefrontal_gen.md))

- PFC simultaneously represents behaviour at multiple temporal scales—both immediate trial events and integrated policy over multiple trials; PFC policy representations generalized across problems for both A and B choices and were specific to trial stage (initiation, choice, outcome), not simple value representations ([Samborska 2021](../../raw/summaries/samborska2021_hippocampus_prefrontal_gen.md))

- Excitotoxic NMDA lesions of rat medial prefrontal cortex (mPFC) leave spatial learning and working memory intact in the Morris water maze and three-panel runway, while impairing food hoarding, elevating locomotion, and slowing reversal learning. Both reference and working memory were intact in two independent spatial tasks, and probe tests confirmed normal retention of platform locations ([Lacroix 2002](../../raw/summaries/lacroix2002_medial_prefrontal_spatial.md))

- mPFC deficits in spatial tasks reflect attentional and flexibility impairments rather than mnemonic ones. The observed impairments — slower initial training-trial acquisition and slowed reversal learning — occurred against a backdrop of intact ultimate memory performance, and were not attributable to motor or visual deficits ([Lacroix 2002](../../raw/summaries/lacroix2002_medial_prefrontal_spatial.md))

- mPFC-lesioned rats show significantly greater distances traveled (F(1,15) = 8.10, P < 0.02) and more centre entries (F(1,15) = 7.41, P < 0.02) in open-field locomotion, replicating known hyperactivity effects and confirming lesion efficacy ([Lacroix 2002](../../raw/summaries/lacroix2002_medial_prefrontal_spatial.md))

- mPFC lesions significantly slowed reversal learning in the Morris water maze; mPFC rats were significantly slower than controls on day 2 of reversal (F(1,15) = 13.17, P < 0.01), producing a near-significant lesion × days interaction (F(2,30) = 3.18, P = 0.06), suggesting deficits in attentional processes and/or behavioural flexibility ([Lacroix 2002](../../raw/summaries/lacroix2002_medial_prefrontal_spatial.md))

## Open questions

- The review focuses almost exclusively on the mouse PL; whether findings generalise to IL, ACC, other rodents, or primates is explicitly noted as unresolved ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))
- The exact number and identity of cell types in mPFC remains unclear; the IT/PT/CT taxonomy is acknowledged as an oversimplification ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))
- How subregions of mPFC (ACC, PL, IL) communicate with each other via local cortical connections is largely unknown ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))
- The relative functional dominance of feedforward excitation, feedforward inhibition, feedback inhibition, and disinhibition in vivo — and how they combine during behaviour — is unresolved ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))
- How mPFC circuits are disrupted in psychiatric disorders (schizophrenia, depression, ADHD, addiction) remains a major open question ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))
- The functional implications of VM input to PT apical dendrites — particularly for synaptic plasticity — are not yet established ([Anastasiades 2021](../../raw/summaries/anastasiades2021_circuit_medial_prefrontal.md))

## Related pages

- [prefrontal_cortex](prefrontal_cortex.md)
- [prelimbic_cortex](prelimbic_cortex.md)
- [anterior_cingulate_cortex](anterior_cingulate_cortex.md)
- [basolateral_amygdala](basolateral_amygdala.md)
- [mediodorsal_thalamus](mediodorsal_thalamus.md)
- [ventromedial_thalamus](ventromedial_thalamus.md)
- [ventral_hippocampus](ventral_hippocampus.md)
- [cortical_microcircuit](../computational_frameworks/cortical_microcircuit.md)
