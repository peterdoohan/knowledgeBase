# Hippocampus

## Current understanding

*(To be synthesized once sufficient evidence accumulates)*

---

## Key evidence

- Cognitive map formation in mice occurs in three distinct phases over 12+ weeks: initial slow learning requiring 7+ sessions (naive phase), intermediate phase showing offline gains by session 2 starting at week 3, and expert phase showing good performance in session 1 with additional offline gains by session 2 starting at week 12+; authors hypothesize hippocampal involvement in early phases with potential shift to hippocampal independence in later phases ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))
- Cognitive map buildup depends on time elapsed (weeks) rather than training frequency, suggesting systems consolidation involving transfer of spatial knowledge from hippocampus to neocortical structures over the 12-week training period ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))
- Old goal location memories are not overwritten by new learning; probe trials showed animals crossed both current and previous goal locations more than control nodes, suggesting hippocampal memory encoding supports retention of multiple spatial memories ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))

- Hippocampal place cells encode the successor representation matrix, with individual place fields corresponding to columns of the SR matrix; place fields exhibit radial symmetry in open fields, distortion around barriers, skew along travel direction, and clustering near reward — all consistent with the SR model of Stachenfeld et al. (2017) that reframes place cells from current location encoding to predictive map encoding ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- Pre-exposure facilitation of contextual fear conditioning is abolished by hippocampal lesions, consistent with the hippocampus encoding a predictive map (successor representation) that generalizes conditioned fear across states; this reinterprets Fanselow (2010) findings through the SR framework as evidence that the hippocampus supports generalization of fear responses via predictive state representations ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- Model-based value estimates can inform dopaminergic RPEs through offline planning during hippocampal sharp-wave ripples that refines cached values, providing a mechanism for hippocampal influence on dopaminergic reward prediction errors ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- A scalar dopaminergic surprise signal can upregulate learning rates in hippocampal predictive models, explaining stimulus-stimulus learning without requiring vector-valued state prediction errors ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- The entorhinal-hippocampal circuit represents abstract task structure in a manner analogous to spatial structure representation. The entorhinal cortex encodes relational structure of abstract RL problems, generalizing across sensory exemplars but remapping between different structures, mirroring how grid cells and place cells remap between spatial environments ([Baram 2021](../../raw/summaries/baram2021_entorhinal_ventromedial_rl.md))

- The hippocampus tracks path distance to goals rather than detecting detours per se; right posterior hippocampal activity correlates with magnitude of change in path distance to goal at detours, and rodent lesion evidence shows hippocampus supports optimal path selection rather than detour capability itself ([Spiers 2015](../../raw/summaries/spiers2015_detour_problem_navigation.md))

- Hippocampal place cell replay sequences constitute the neural substrate of cognitive-map-based route planning; CA1 replay rapidly adapts to reconfigured maze barriers without global place field remapping, with 87% of sessions showing high barrier conformity in replay ([McNaughton 2022](../../raw/summaries/mcnaughton2022_route_cognitive_map.md))

- Hippocampal replay rapidly adapts to new barrier configurations without requiring global place field remapping; CA1 place cells maintained stable location-specific firing across barrier reconfigurations while replay sequences showed 87% barrier conformity ([McNaughton 2022](../../raw/summaries/mcnaughton2022_route_cognitive_map.md))

- Replay is more closely aligned to future trajectories than past trajectories, consistent with prospective planning function; replay was more closely aligned to future trajectories than past trajectories across all sessions in barrier maze experiments ([McNaughton 2022](../../raw/summaries/mcnaughton2022_route_cognitive_map.md))

- The human hippocampal-entorhinal system implicitly encodes a map-like metric representation of discrete non-spatial relationships between objects, best described by a successor representation (predictive map) rather than Euclidean distance ([Garvert 2017](../../raw/summaries/garvert2017_relational_knowledge_maps.md))

- fMRI adaptation in bilateral entorhinal cortex and hippocampal formation decreased monotonically with link distance on hidden graphs, recovering graph topology (r = 0.65, p = 0.003) even without explicit awareness of structure ([Garvert 2017](../../raw/summaries/garvert2017_relational_knowledge_maps.md))

- The neural metric for relational knowledge in hippocampal-entorhinal system follows successor representation/communicability rather than Euclidean distance; when communicability competed with Euclidean distance, communicability alone predicted activity (FWE p = 0.006) ([Garvert 2017](../../raw/summaries/garvert2017_relational_knowledge_maps.md))

- Online (on-task) replay correlates with model-based planning flexibility and predicts policy re-evaluation; forward sequenceness positively correlated with Index of Flexibility (mean β = 0.17) and predicted policy changes (+11.1% reward improvement) ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

---

- OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals ([Basu2021](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- Hippocampus-OFC implements two-system architecture: hippocampus encodes current position, OFC encodes goal ([Basu2021](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- Ventral hippocampal inputs are necessary for OFC's representation of target direction during decision-making ([Basu2021](../../raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md))

- RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition ([Basu2021](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation ([Basu2021](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- Auditory cues associated with specific spatial locations bias hippocampal replay during non-REM sleep ([Basu2021](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Replay bias is specific to non-REM sleep and absent during awake reactivation ([Basu2021](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay represents selective content modulation rather than non-specific arousal ([Basu2021](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Auditory cues associated with specific spatial locations bias hippocampal replay during non-REM sleep ([Bendor2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Replay bias is specific to non-REM sleep and absent during awake reactivation ([Bendor2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay represents selective content modulation rather than non-specific arousal ([Bendor2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Auditory cues associated with specific spatial locations bias hippocampal replay during non-REM sleep ([Bendor2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Replay bias is specific to non-REM sleep and absent during awake reactivation ([Bendor2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay represents selective content modulation rather than non-specific arousal ([Bendor2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

## History of ideas

*(Chronological narrative of how understanding evolved)*

---

## Open questions

- Closed-loop optogenetic disruption of content-specific hippocampal reactivation during sleep selectively impairs recall of targeted memories while leaving undisrupted memories intact; animals showed significantly worse recall for target-environment goals than control-environment goals (dwell time p < 0.0009, goal-zone crossings p < 0.0006, path length p < 10⁻⁵) ([Gridchyn 2020](../../raw/summaries/gridchyn2020_replay_selective_memory.md))

- Place maps destabilized by disrupted replay can recover after relearning, suggesting replay is not required for long-term map stabilization but for context-association consolidation; place field similarity of target environment was significantly lower at probe and first post-learning trial (p < 0.0056 and p < 0.027), but recovered by trials 6-10 (all p > 0.34) ([Gridchyn 2020](../../raw/summaries/gridchyn2020_replay_selective_memory.md))

- The hippocampal formation functions as a hierarchical generative model organizing experiences into items, sequences, and maps, enabling generative replay rather than verbatim memory replay; a three-layer model uses predictive coding and Bayesian inference, with generative replay resampling fictive trajectories from learned model, accounting for novel sequences never experienced ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Hippocampal place cells encode the successor representation matrix, with individual place fields corresponding to columns of the SR matrix; place fields exhibit radial symmetry in open fields, distortion around barriers, skew along travel direction, and clustering near reward — all consistent with the SR model that reframes place cells from current location encoding to predictive map encoding ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- Pre-exposure facilitation of contextual fear conditioning is abolished by hippocampal lesions, consistent with the hippocampus encoding a predictive map (successor representation) that generalizes conditioned fear across states; this reinterprets Fanselow (2010) findings through the SR framework as evidence that the hippocampus supports generalization of fear responses via predictive state representations ([Gershman 2018](../../raw/summaries/gershman2018_successor_representation_learning.md))

- Hippocampal replay during rest/pauses can represent future goal-directed routes but does so reliably only under high mnemonic demand, not on stereotyped tracks; replay of future goal locations is significantly higher during high-demand trials (search phase and first repetition) versus low-demand trials (p < 0.05) ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))

- Hippocampus is necessary for generating subgoals during detour navigation; right posterior hippocampal activity at detours correlates with magnitude of change in path distance to goal, and rodent lesion evidence shows hippocampus supports optimal path selection rather than detour capability itself ([Spiers 2015](../../raw/summaries/spiers2015_detour_problem_navigation.md))

- Hippocampal place cell replay sequences constitute the neural substrate of cognitive-map-based route planning; CA1 replay rapidly adapts to reconfigured maze barriers without global place field remapping, with 87% of sessions showing high barrier conformity in replay ([McNaughton 2022](../../raw/summaries/mcnaughton2022_route_cognitive_map.md))

- Hippocampal replay rapidly adapts to new barrier configurations without requiring global place field remapping; CA1 place cells maintained stable location-specific firing across barrier reconfigurations while replay sequences showed 87% barrier conformity ([McNaughton 2022](../../raw/summaries/mcnaughton2022_route_cognitive_map.md))

- Replay is more closely aligned to future trajectories than past trajectories, consistent with prospective planning function; replay was more closely aligned to future trajectories than past trajectories across all sessions in barrier maze experiments ([McNaughton 2022](../../raw/summaries/mcnaughton2022_route_cognitive_map.md))

- The hippocampus represents sensorimotor-specific instantiations of task structure, showing remapping between problems even when physical locations and meanings are identical; CA1 showed stronger representation of physical port location and A vs B choice (p < .001), with problem-specific representations indicating context-induced remapping absent in PFC (p < .001) ([Samborska 2021](../../raw/summaries/samborska2021_hippocampus_prefrontal_gen.md))

- Hippocampal upcoming-choice representations are SWR- and theta-locked, unlike mPFC representations; in hippocampus, upcoming-choice representations were significantly more frequent at SWR onset (p=.004) and phase-locked to rising theta phase, while mPFC non-local representations did not overlap in time with hippocampal non-local representations ([den Bakker 2024](../../raw/summaries/denbakker2024_mpfc_spatial_swr.md))

- Hippocampal activity patterns during the planning period significantly decode the future goal location before navigation begins; classifier accuracy 29.4% (t16=7.54, P=1.19e-6) for future goal decoding during pre-navigation planning period ([Brown 2016](../../raw/summaries/brown2016_prospective_goals_hippocampus.md))

- During planning, hippocampal representations show confusion between the true goal and intervening sub-goals along the optimal route, consistent with sequential trajectory simulation; MVPA confusion matrices show classifier errors reflect route waypoints and pattern reinstatement of intermediate locations ([Brown 2016](../../raw/summaries/brown2016_prospective_goals_hippocampus.md))

- Trial-by-trial hippocampal goal evidence positively correlates with planning-period activity in lateral and medial frontopolar cortex, suggesting PFC-hippocampal coupling during prospective simulation; FPC activity tracked trial-by-trial goal coding strength in hippocampus ([Brown 2016](../../raw/summaries/brown2016_prospective_goals_hippocampus.md))

- Disrupting one memory trace via targeted replay blockade does not degrade other related memories, arguing against circuit reorganization; same animals in same rest period showed intact memory for control environment whose replay was spared, with impairment selective to environment whose reactivation was blocked ([Gridchyn 2020](../../raw/summaries/gridchyn2020_replay_selective_memory.md))

- Hippocampus represents sensorimotor-specific instantiations of task structure, showing remapping between problems even when physical locations and meanings are identical; CA1 showed stronger representation of physical port location and A vs B choice (p < .001), with problem-specific representations indicating context-induced remapping absent in PFC (p < .001) ([Samborska 2021](../../raw/summaries/samborska2021_hippocampus_prefrontal_gen.md))

- Hippocampal upcoming-choice representations are SWR- and theta-locked, unlike mPFC representations; in hippocampus, upcoming-choice representations were significantly more frequent at SWR onset (p=.004) and phase-locked to rising theta phase, while mPFC non-local representations did not overlap in time with hippocampal non-local representations ([den Bakker 2024](../../raw/summaries/denbakker2024_mpfc_spatial_swr.md))

- SWR rates track subjective value and trial value, with this value-coding dependent on intact mPFC; SWR rates were lowest at Least preferred and highest at Most preferred restaurants (F(3,147)=15.98, p=4.8e-9); Waiting SWR rates increased with trial value (Good deals > Difficult > Bad deals; F(2,96)=93.25, p<3e-23) ([Schmidt 2021](../../raw/summaries/schmidt2021_mpfc_swr_dreadd.md))

- mPFC disruption with inhibitory DREADDs specifically impairs post-learning consolidation SWRs while sparing on-maze SWRs; SWR rate increase from pre-maze to post-maze rest was significantly reduced on CNO days (F(1,49)=8.36, p=.0057; interaction F(1,49)=10.9, p=.0018), while on-maze SWRs showed no effect (p=.21) ([Schmidt 2021](../../raw/summaries/schmidt2021_mpfc_swr_dreadd.md))

- Astroglial metabolic networks in hippocampus sustain synaptic transmission during glucose deprivation via gap junction-mediated glucose and lactate trafficking ([Rouach 2008](../../raw/summaries/rouach2008_astrocyte_metabolism.md))

- mCx30.2 connexin is expressed in hippocampal neurons, suggesting specialized electrical coupling functions in this region ([Rackauskas 2007](../../raw/summaries/rackauskas2007_gap_junction_permeability.md))

- Sensory cues presented during non-REM sleep can selectively bias hippocampal replay toward the associated spatial memory. Place cells with right-sided fields showed positive rate bias after Sound R; left-sided cells showed negative rate bias after Sound L (r = 0.29, P < 1.1 × 10⁻⁴). ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay is specific to non-REM sleep and does not occur during awake reactivation. Bias was absent during awake reactivation events (ANOVA, P = 0.82), consistent with human TMR literature showing cue-enhancement specific to non-REM. ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Acoustic cues bias replay content without changing the overall rate of replay events. Acoustic cues did not change number of replay events (Kruskal-Wallis, P > 0.05), indicating selective content modulation rather than non-specific arousal. ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay shows a time-limited window of susceptibility during sleep. Bias was stronger in early sleep than late sleep (first half: P < 1.7 × 10⁻⁵; second half: not significant), suggesting capacity limits for replay modulation. ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Sensory cues presented during non-REM sleep can selectively bias hippocampal replay toward the associated spatial memory. Place cells with right-sided fields showed positive rate bias after Sound R; left-sided cells showed negative rate bias after Sound L (r = 0.29, P < 1.1 × 10⁻⁴). ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay is specific to non-REM sleep and does not occur during awake reactivation. Bias was absent during awake reactivation events (ANOVA, P = 0.82), consistent with human TMR literature showing cue-enhancement specific to non-REM. ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Acoustic cues bias replay content without changing the overall rate of replay events. Acoustic cues did not change number of replay events (Kruskal-Wallis, P > 0.05), indicating selective content modulation rather than non-specific arousal. ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay shows a time-limited window of susceptibility during sleep. Bias was stronger in early sleep than late sleep (first half: P < 1.7 × 10⁻⁵; second half: not significant), suggesting capacity limits for replay modulation. ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- How do different hippocampal subregions (CA1, CA3, DG) contribute differentially to memory and spatial processing?
- What is the precise relationship between hippocampal replay and offline memory consolidation?
- How do astroglial metabolic networks interact with hippocampal synaptic plasticity and memory formation?

---

## Related pages

- [Astrocytes](astrocytes.md)

- [Cognitive map](../behaviours/cognitive_map.md)
- [Spatial navigation](../behaviours/spatial_navigation.md)
- [Memory consolidation](../behaviours/memory_consolidation.md)
- [Schema learning](../behaviours/schema_learning.md)
