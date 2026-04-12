---
title: "Medial prefrontal cortex in goal-directed spatial navigation and spatial working memory"
subtopic_id: prefrontal_goal_representation_and_control__01
parent_topic_id: prefrontal_goal_representation_and_control
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:49:38.727119+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - hartley2003_wayfinding_route
  - patai2021_versatile_wayfinder_prefrontal
  - ito2015_prefrontal_thalamic_hippocampus
  - sauer2022_prefrontal_spatial_representation
  - badre2018_frontal_cortex_hierarchical_control
core_papers:
  - badre2018_frontal_cortex_hierarchical_control
  - bohm2020_pfc_spatial_working_memory
  - ciaramelli2008_vmPFC_navigation_wayfinding
  - ciaramelli2008_vmPFC_wayfinding_navigation
  - dahmani2015_prefrontal_navigation_strategies
  - denbakker2023_sharp_wave_prefrontal_rule
  - elgaby2023_behavioral_structure_mapping
  - farzanfar2023_cognitive_maps_spatial
related_wiki_pages:
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation
  - wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits
---

# Medial prefrontal cortex in goal-directed spatial navigation and spatial working memory

Medial prefrontal cortex (mPFC) is now hard to dismiss as merely “executive support” for navigation, but the strongest evidence does not support a simple view in which it stores stable spatial goals during delay periods. Instead, the literature points to a more conditional role: mPFC carries spatial and contextual signals, helps maintain destinations and behavioral policies when navigation requires flexible control, and interacts with hippocampal circuits during prospective coding, rule updating, and decision epochs. The cleanest causal evidence comes from circuit studies linking mPFC to hippocampal trajectory coding through nucleus reuniens and to replay-linked rule switching; the cleanest counterweight is that canonical goal-selective delay activity can disappear in flexible spatial working-memory tasks [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|den Bakker et al. 2023]] [[raw/summaries/bohm2020_pfc_spatial_working_memory|Böhm et al. 2020]].

## Current view

mPFC appears to contribute to navigation mainly by representing task-relevant state under goal pressure: intended trajectory, current rule, choice context, and destination maintenance, rather than by replacing hippocampal spatial mapping. This fits rodent circuit data and human lesion/fMRI results better than a “goal cell buffer” account [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] [[raw/summaries/ciaramelli2008_vmPFC_wayfinding_navigation|Ciaramelli et al. 2008]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]].

mPFC does contain bona fide spatial signals. During spontaneous unrewarded navigation, 35.1% of prefrontal pyramidal neurons carried significant spatial information, position could be decoded from population activity, and representations remapped in a novel environment with partial reinstatement on return to the familiar one [[raw/summaries/sauer2022_prefrontal_spatial_representation|Sauer et al. 2022]]. Border-tuned neurons have also been reported in mPFC during free foraging [[raw/summaries/long2024_border_cells_prefrontal|Long et al. 2024]].

But spatial tuning alone is not the main story. In goal-directed tasks, the strongest case is that mPFC helps disambiguate future paths and coordinate with hippocampus online and offline. Trajectory-dependent firing is present in mPFC and nucleus reuniens, and disrupting reuniens degrades prospective CA1 coding [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]]. Hippocampal–prefrontal theta synchrony rises during working-memory and decision epochs and weakens on error trials [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]]. Replay-timed mPFC activity is also required for spatial rule switching [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|den Bakker et al. 2023]].

The working-memory literature is notably less clean than older textbook summaries imply. In a flexible spatial working-memory task designed to prevent stereotyped motor solutions, mPFC lacked canonical current-goal-selective delay representations in all previously reported forms [[raw/summaries/bohm2020_pfc_spatial_working_memory|Böhm et al. 2020]]. That pushes the field toward mixed-selectivity, subspace, or latent-state accounts rather than persistent single-goal coding [[raw/summaries/maggi2022_activity_subspaces_prefrontal|Maggi et al. 2022]] [[raw/summaries/fujisawa2008_assembly_prefrontal_cortex|Fujisawa et al. 2008]].

## Strongest evidence

- **Causal circuit evidence for prospective navigation coding.**  
  In a delayed alternation task, 38.2% of mPFC cells and 42.2% of reuniens cells were trajectory-dependent; CA1 showed much stronger trajectory coding than CA3. Reuniens lesions reduced trajectory-dependent CA1 cells from 55.1% to 15.9%, and acute optogenetic reuniens silencing reduced them from 72% to 44% [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]].  
  The important inference is not just “mPFC is active,” but that a prefrontal–thalamic route is required for normal hippocampal prospective disambiguation.

- **Temporally specific mPFC involvement in rule updating.**  
  Optogenetic inhibition of mPFC locked to hippocampal sharp-wave ripples impaired spatial rule switching, whereas the same inhibition delivered 400–450 ms later did not [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|den Bakker et al. 2023]].  
  This is unusually strong evidence that mPFC contributes during a narrow replay-associated window relevant for updating strategy.

- **Error-linked hippocampal–prefrontal coordination.**  
  Theta synchrony between CA1 and mPFC increases during working-memory and decision periods of spatial alternation and is attenuated on error trials [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]].  
  This supports an interaction account: successful spatial working memory depends on coordination, not just local persistence in PFC.

- **Direct evidence that mPFC carries spatial/contextual variables.**  
  mPFC pyramidal neurons show above-chance spatial information, reliable within-session tuning, and context-sensitive remapping; unexpectedly, dorsal mPFC showed stronger spatial tuning than ventral mPFC despite denser hippocampal input ventrally [[raw/summaries/sauer2022_prefrontal_spatial_representation|Sauer et al. 2022]].  
  So mPFC spatial coding is real, but not trivially inherited from hippocampus.

- **Human evidence for goal maintenance during wayfinding.**  
  A patient with bilateral vmPFC damage showed severe wayfinding impairment despite preserved landmark knowledge and spatial memory, and periodic goal rehearsal substantially improved performance [[raw/summaries/ciaramelli2008_vmPFC_wayfinding_navigation|Ciaramelli et al. 2008]].  
  This is consistent with a destination-maintenance or control deficit, though it is a single-case result.

- **Strong negative evidence against a simple persistent-goal model.**  
  In rats performing a flexible spatial working-memory task, mPFC showed no evidence of current-goal-specific delay activity in any canonical form previously reported in the literature [[raw/summaries/bohm2020_pfc_spatial_working_memory|Böhm et al. 2020]].  
  This matters because it directly targets a common claim about prefrontal working memory and fails to confirm it under high-flexibility conditions.

## Landmark papers

- [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]]  
  Key human wayfinding study. Accurate wayfinding tracked hippocampal activation, while route following aligned more with caudate. Important here mainly as a constraint: successful navigation is not reducible to prefrontal engagement.

- [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]]  
  Established theta-frequency coordination between hippocampus and mPFC during spatial working memory, with weaker coupling on error trials.

- [[raw/summaries/ciaramelli2008_vmPFC_wayfinding_navigation|Ciaramelli et al. 2008]]  
  Put vmPFC onto the navigation map by showing a wayfinding deficit that looked more like failure to keep the destination online than loss of spatial knowledge.

- [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]]  
  The core causal circuit paper: mPFC–reuniens–CA1 supports prospective trajectory coding during goal-directed navigation.

- [[raw/summaries/bohm2020_pfc_spatial_working_memory|Böhm et al. 2020]]  
  A pivotal null result. It forced a rethink of canonical goal-selective delay coding in mPFC under truly flexible task demands.

- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]]  
  The clearest synthesis arguing that PFC is part of the navigation system proper, with distinct subregions supporting replanning, strategy choice, goal maintenance, and value-sensitive route decisions.

## Boundaries and tensions

The literature supports **mPFC involvement**, but not a single agreed computation.

One tension is between **spatial coding** and **goal-memory coding**. mPFC clearly contains spatial and contextual signals [[raw/summaries/sauer2022_prefrontal_spatial_representation|Sauer et al. 2022]] [[raw/summaries/long2024_border_cells_prefrontal|Long et al. 2024]], yet flexible-task recordings failed to find canonical delay-period goal representations [[raw/summaries/bohm2020_pfc_spatial_working_memory|Böhm et al. 2020]]. The safest synthesis is that mPFC represents task state in a more distributed or conditional format than classic persistent-firing models predict.

A second tension is between **neural necessity** and **behavioral necessity**. Reuniens disruption strongly reduced CA1 trajectory coding, but did not impair performance in a simple alternation task [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]]. So prospective coding can be circuit-important without being behavior-limiting in easy or overtrained tasks.

A third tension is **hippocampal dominance vs prefrontal control** in human navigation. In virtual wayfinding, hippocampal activity tracked accurate performance more directly than generic task contrasts did [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]]. Human PFC effects are clearest when the task requires detours, strategy selection, internally maintained goals, or value-sensitive planning [[raw/summaries/dahmani2015_prefrontal_navigation_strategies|Dahmani et al. 2015]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]].

Subregional mapping is also unsettled. Human studies implicate vmPFC, dmPFC, and dACC for different aspects of navigation; rodent studies often focus on prelimbic/infralimbic mPFC. Cross-species homology is not clean, and many claims about “mPFC” remain anatomically coarse [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]].

Finally, not all mPFC spatial signals appear to ride on hippocampal theta. Theta synchrony is behaviorally relevant [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]], but mPFC border cells can lack theta rhythmicity [[raw/summaries/long2024_border_cells_prefrontal|Long et al. 2024]]. A single oscillatory coordination mechanism is probably insufficient.

## Open questions

- **What exactly is the goal representation in mPFC?**  
  If canonical persistent delay coding is absent in flexible tasks, does mPFC encode goals as latent state, policy, action plan, or mixed-selective population geometry instead [[raw/summaries/bohm2020_pfc_spatial_working_memory|Böhm et al. 2020]] [[raw/summaries/maggi2022_activity_subspaces_prefrontal|Maggi et al. 2022]]?

- **When does the mPFC–reuniens–CA1 pathway become behaviorally necessary?**  
  The circuit is clearly necessary for normal CA1 prospective coding, but not for performance in simple alternation. Harder detours, longer delays, multiple candidate goals, and conflict-rich tasks are the obvious tests [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]].

- **How do theta and replay divide labor?**  
  Theta-linked coordination looks important during online choice and working memory, while SWR-linked mPFC activity is important for updating rules. Whether these are separate computational modes or two phases of the same control process remains unresolved [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]] [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|den Bakker et al. 2023]].

- **How much of mPFC spatial coding is inherited vs locally constructed?**  
  The dorsal>ventral spatial-tuning gradient argues against a simple “more hippocampal input, more spatial coding” story [[raw/summaries/sauer2022_prefrontal_spatial_representation|Sauer et al. 2022]].

- **How should rodent and human medial frontal findings be aligned?**  
  vmPFC destination maintenance, dmPFC strategy differences, dACC detour/backtracking signals, and rodent prelimbic prospective coding may overlap functionally, but current homology claims are still partly inferential [[raw/summaries/ciaramelli2008_vmPFC_wayfinding_navigation|Ciaramelli et al. 2008]] [[raw/summaries/dahmani2015_prefrontal_navigation_strategies|Dahmani et al. 2015]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]].

- **Does mPFC generalize across environments by encoding structure rather than place?**  
  Work on structured behavioral representations and spatial schemas suggests a route from navigation-specific coding to more abstract task-structure coding, but the direct link is still underdeveloped [[raw/summaries/elgaby2023_behavioral_structure_mapping|Elgaby et al. 2023]] [[raw/summaries/farzanfar2023_cognitive_maps_spatial|Farzanfar et al. 2023]].

## Key papers

- [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] — strongest causal evidence for an mPFC–thalamic–hippocampal pathway supporting prospective trajectory coding.
- [[raw/summaries/bohm2020_pfc_spatial_working_memory|Böhm et al. 2020]] — important falsification of canonical goal-selective delay coding in flexible spatial working memory.
- [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]] — classic evidence that hippocampal–prefrontal theta coordination matters for spatial working memory.
- [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|den Bakker et al. 2023]] — replay-timed causal evidence linking mPFC to spatial rule switching.
- [[raw/summaries/sauer2022_prefrontal_spatial_representation|Sauer et al. 2022]] — direct demonstration that mPFC carries spatial and contextual representations even without reward.
- [[raw/summaries/ciaramelli2008_vmPFC_wayfinding_navigation|Ciaramelli et al. 2008]] — lesion evidence for vmPFC involvement in maintaining navigation goals.
- [[raw/summaries/dahmani2015_prefrontal_navigation_strategies|Dahmani et al. 2015]] — human dissociation between prefrontal subregions supporting spatial vs response navigation strategies.
- [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]] — critical human constraint showing wayfinding success is more directly tied to hippocampus than generic prefrontal activation.
- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]] — useful synthesis placing PFC firmly within the navigation system.
- [[raw/summaries/maggi2022_activity_subspaces_prefrontal|Maggi et al. 2022]] — population-level evidence favoring state/subspace coding over simple persistent mnemonic traces.

## Related wiki pages
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]: Link via hippocampal-prefrontal coordination in flexible navigation: how cognitive-map representations are recruited, read out, or reshaped by mPFC during goal selection, replanning, detours, and replay-guided decisions.
- [[wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation|Hippocampal–prefrontal mechanisms of route planning and detour navigation]]: Link A to B for readers wanting a deeper treatment of mPFC-specific goal representation, policy updating, and spatial working-memory evidence; link B to A for the navigation-task context where mPFC functions are expressed as route planning and detour behavior.
- [[wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits|Prospective spatial coding in hippocampal–medial prefrontal circuits]]: From Page B, link to Page A as the dedicated subpage on hippocampal–prefrontal prospective coding during navigation; from Page A, link back to Page B for the wider mPFC functional context beyond prospective coding.

## Source papers
- [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]] | [[raw/mds/hartley2003_wayfinding_route|source md]]: The Well-Worn Route and the Path Less Traveled: Distinct Neural Bases of Route Following and Wayfinding in Humans
- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]] | [[raw/mds/patai2021_versatile_wayfinder_prefrontal|source md]]: The Versatile Wayfinder: Prefrontal Contributions to Spatial Navigation
- [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] | [[raw/mds/ito2015_prefrontal_thalamic_hippocampus|source md]]: A prefrontal–thalamo–hippocampal circuit for goal-directed spatial navigation
- [[raw/summaries/sauer2022_prefrontal_spatial_representation|Sauer et al. 2022]] | [[raw/mds/sauer2022_prefrontal_spatial_representation|source md]]: Topographically organized representation of space and context in the medial prefrontal cortex
- [[raw/summaries/badre2018_frontal_cortex_hierarchical_control|Badre and Nee 2018]] | [[raw/mds/badre2018_frontal_cortex_hierarchical_control|source md]]: Frontal Cortex and the Hierarchical Control of Behavior
- [[raw/summaries/bohm2020_pfc_spatial_working_memory|Böhm and Lee 2020]] | [[raw/mds/bohm2020_pfc_spatial_working_memory|source md]]: Canonical goal-selective representations are absent from prefrontal cortex in a spatial working memory task requiring behavioral flexibility
- [[raw/summaries/ciaramelli2008_vmPFC_navigation_wayfinding|Ciaramelli 2008]] | [[raw/mds/ciaramelli2008_vmPFC_navigation_wayfinding|source md]]: The role of ventromedial prefrontal cortex in navigation: A case of impaired wayfinding and rehabilitation
- [[raw/summaries/ciaramelli2008_vmPFC_wayfinding_navigation|Ciaramelli 2008]] | [[raw/mds/ciaramelli2008_vmPFC_wayfinding_navigation|source md]]: The role of ventromedial prefrontal cortex in navigation: A case of impaired wayfinding and rehabilitation
- [[raw/summaries/dahmani2015_prefrontal_navigation_strategies|Dahmani and Bohbot 2015]] | [[raw/mds/dahmani2015_prefrontal_navigation_strategies|source md]]: Dissociable contributions of the prefrontal cortex to hippocampus- and caudate nucleus-dependent virtual navigation strategies
- [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|Bakker et al. 2023]] | [[raw/mds/denbakker2023_sharp_wave_prefrontal_rule|source md]]: Sharp-wave-ripple-associated activity in the medial prefrontal cortex supports spatial rule switching
- [[raw/summaries/elgaby2023_behavioral_structure_mapping|El-Gaby et al. 2023]] | [[raw/mds/elgaby2023_behavioral_structure_mapping|source md]]: A Cellular Basis for Mapping Behavioural Structure
- [[raw/summaries/farzanfar2023_cognitive_maps_spatial|Farzanfar et al. 2023]] | [[raw/mds/farzanfar2023_cognitive_maps_spatial|source md]]: From cognitive maps to spatial schemas
