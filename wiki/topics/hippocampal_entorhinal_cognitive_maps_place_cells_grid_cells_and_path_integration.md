---
title: "Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration"
subtopic_id: cognitive_maps__02
parent_topic_id: cognitive_maps
page_type: topic
page_worthiness: 5
status: draft_llm
generated_at: "2026-04-12T19:25:29.480262+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - behrens2018_cognitive_map_organizing_knowledge
  - fyhn2007_remapping_grid_realignment
  - liu2019_human_replay_reorganizes
  - sorscher2022_grid_cells_path_integration
  - nour2021_impaired_replay_schizophrenia
core_papers:
  - alonso2021_hexmaze_cognitive_map
  - behrens2018_cognitive_map_organizing_knowledge
  - bush2015_grid_cells_navigation_vector
  - findlay2021_replay_wake_sleep
  - foster2017_replay_memory_consolidation
  - fyhn2007_remapping_grid_realignment
  - garvert2017_relational_knowledge_maps
  - iyer2024_grid_cells_abstract_velocity
---

# Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration

The best-supported account is that the hippocampal–entorhinal system represents spatial state spaces in a way that is both metric and predictive. In this view, hippocampal place cells supply context-sensitive state representations, medial entorhinal grid cells supply a reusable metric scaffold useful for path integration, and replay samples from learned transition structure rather than merely echoing recent sensory sequences. The case is strongest for physical space; claims that the same code cleanly generalizes to all abstract domains remain plausible but less securely established.

## Current view

A useful synthesis is: hippocampal maps are not just “where am I now?” codes, and entorhinal maps are not just static spatial lattices. The system appears to encode transition structure, expected future occupancy, and context-dependent state identity [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

Place-cell representations are strongly context sensitive. Across environments, hippocampal ensembles can globally remap; across more subtle manipulations, they can rate-remap without changing the underlying spatial reference frame. That dissociation matters because it implies that “place” in hippocampus is not a fixed sensory label but part of a contextually organized state representation [[raw/summaries/fyhn2007_remapping_grid_realignment|Fyhn et al. 2007]].

Grid-cell ensembles in medial entorhinal cortex look more like a reusable metric coordinate system. During hippocampal global remapping, co-recorded grid cells shift coherently while preserving their internal phase relationships and spacing, consistent with attractor-style population dynamics rather than independent field-by-field remapping [[raw/summaries/fyhn2007_remapping_grid_realignment|Fyhn et al. 2007]].

On the computational side, grid-like codes are a natural solution for path integration under specific constraints. In trained path-integrator networks, hexagonal responses emerge robustly when the place-code correlation structure and nonnegativity conditions predicted by theory are respected [[raw/summaries/sorscher2022_grid_cells_path_integration|Sorscher et al. 2022]]. This does not prove biology uses that exact algorithm, but it strengthens the claim that grids are functionally tied to self-motion integration.

Replay now looks less like passive memory consolidation and more like model-based sampling from a cognitive map. Reviews synthesize evidence that replay occurs in wake as well as sleep and can support planning and credit assignment [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]]. In humans, replay can reorganize novel experience according to latent structural rules rather than experienced order, suggesting access to an internal map of relations [[raw/summaries/liu2019_human_replay_reorganizes|Liu et al. 2019]].

A more ambitious current view is that these spatial codes instantiate a general mechanism for relational structure learning. Reviews and human work argue for successor-representation-like coding and grid-like generalization in non-spatial tasks [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]]. But the evidential base here is much thinner than for physical navigation.

## Strongest evidence

- **Grid ensembles realign coherently during global remapping.**  
  In different enclosures or rooms, hippocampal global remapping coincided with a coherent translation/rotation of MEC grid ensembles, while preserving relative phases and spacing across co-recorded cells. That is hard to reconcile with independent remapping of single cells and fits attractor-like coordinate-frame shifts [[raw/summaries/fyhn2007_remapping_grid_realignment|Fyhn et al. 2007]].

- **Rate remapping does not require grid realignment.**  
  When hippocampal cells changed firing rates without changing place-field locations, MEC grid alignment largely stayed fixed. This is a strong dissociation: not all hippocampal remapping is inherited from MEC coordinate changes [[raw/summaries/fyhn2007_remapping_grid_realignment|Fyhn et al. 2007]].

- **Replay follows inferred structure, not just experienced sequences.**  
  In humans, post-learning replay tracked the rule-defined sequence order rather than the order in which objects were visually encountered; after reward learning, replay direction flipped selectively into reverse for the rewarded sequence. Structural codes for sequence identity/position preceded item-specific sensory codes by ~50 ms [[raw/summaries/liu2019_human_replay_reorganizes|Liu et al. 2019]]. This is among the clearest evidence that replay is constructive and map-based.

- **Path-integration networks naturally generate grids under theory-predicted conditions.**  
  Hexagonal grid responses emerge in nearly all trained path-integrator models when the required correlation structure and nonnegativity constraints are present. This directly links grid periodicity to a concrete computational problem rather than treating it as a descriptive curiosity [[raw/summaries/sorscher2022_grid_cells_path_integration|Sorscher et al. 2022]].

- **Predictive-map accounts explain nontrivial place-field distortions.**  
  The successor-representation framing explains policy-dependent distortions such as field stretching on one-way tracks and clustering near reward, which pure “current location” accounts handle less naturally [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

- **Behavior in rich environments shows gradual map formation rather than one-shot competence.**  
  In the HexMaze, mice showed staged improvement: initial goal learning, faster learning after weeks, then rapid one-session updating after long experience. That pattern fits progressive map construction and reuse, though it is behavioral rather than cell-level evidence [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]].

- **Clinical perturbation provides convergent evidence on replay.**  
  Schizophrenia patients showed reduced replay of inferred sequential structure along with altered ripple-associated activity and weaker structural representations. This is not specific to spatial maps, but it supports the broader claim that replay supports relational map formation [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]].

## Landmark papers

- [[raw/summaries/fyhn2007_remapping_grid_realignment|Fyhn et al. 2007]]  
  Established the key systems result that grid ensembles preserve internal geometry across contexts and undergo coherent realignment during hippocampal global remapping.

- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]]  
  Framed place and grid codes as transition-structure representations, connecting spatial navigation to successor representations and model-based reinforcement learning.

- [[raw/summaries/bush2015_grid_cells_navigation_vector|Bush et al. 2015]]  
  Gave a concrete algorithmic account of how multi-module grid codes could support vector navigation by encoding displacement between arbitrary states.

- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]]  
  Helped consolidate the shift from “replay as offline recapitulation” to “replay as internal model sampling” for planning and learning.

- [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]]  
  Important for extending the map idea beyond physical space, with human evidence favoring successor-like relational coding.

- [[raw/summaries/liu2019_human_replay_reorganizes|Liu et al. 2019]]  
  Strong human evidence that replay reorganizes experience according to latent structure rather than experienced order.

- [[raw/summaries/sorscher2022_grid_cells_path_integration|Sorscher et al. 2022]]  
  Clarified when trained path-integrator networks do and do not produce grid cells, tightening the computational link between grids and path integration.

## Boundaries and tensions

The cleanest evidence is for spatial coding in rodents. Extensions to abstract domains are intriguing, but the review literature is explicit that direct evidence outside low-dimensional, task-designed spaces is still sparse [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

Grid cells look like a universal metric scaffold, but the causal chain remains unresolved. [[raw/summaries/fyhn2007_remapping_grid_realignment|Fyhn et al. 2007]] shows tight coupling between grid realignment and global remapping, not whether entorhinal changes drive hippocampal remapping, reflect it, or are jointly reset by other inputs.

Theoretical accounts of vector navigation are elegant, but much of the evidence is still algorithmic or computational. [[raw/summaries/bush2015_grid_cells_navigation_vector|Bush et al. 2015]] and [[raw/summaries/sorscher2022_grid_cells_path_integration|Sorscher et al. 2022]] show what grid codes can do and when they should emerge, not that brains necessarily exploit those exact mechanisms in everyday navigation.

Successor-representation accounts explain several place-field phenomena well, but they do not eliminate simpler spatial interpretations. The live question is not whether hippocampal cells encode location—they do—but how much of that code reflects current position versus predictive occupancy under a policy [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

Replay evidence is strong conceptually and weaker causally. Human MEG studies show structure-sensitive sequenceness, but source localization and ripple inference from deep structures are limited; causal necessity still requires perturbation [[raw/summaries/liu2019_human_replay_reorganizes|Liu et al. 2019]] [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]].

Path-integration models explain why hexagonal codes appear under certain conditions, but they do not yet explain the full biological complexity of grid organization, especially multiple scales across the dorsoventral axis [[raw/summaries/sorscher2022_grid_cells_path_integration|Sorscher et al. 2022]].

Finally, the hippocampal–entorhinal system is probably not the whole map story. Reviews increasingly place orbitofrontal and prefrontal cortices in the business of representing latent task structure and using it for flexible behavior, which blurs strict anatomical ownership of “cognitive maps” [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] [[raw/summaries/kleinflugge2022_medial_orbital_frontal|Klein-Flügge et al. 2022]].

## Open questions

- What actually resets grid phase, orientation, and scale across context changes: landmarks, self-motion error correction, hippocampal feedback, or some combination?
- When hippocampal place fields distort with policy or reward, is the best description a successor representation, a goal-modulated place code, or both?
- Are grid codes necessary for vector navigation and detour behavior, or just one efficient implementation among several?
- How are multiple grid scales coordinated, and how do single-scale path-integration models extend to the dorsoventral MEC hierarchy?
- What is the causal role of replay in planning, consolidation, and generalization? Correlation is no longer the main issue; intervention is.
- How far do hippocampal–entorhinal coding principles generalize beyond physical space into discrete, abstract, or hierarchical task domains?
- How is map information divided across hippocampus, entorhinal cortex, and prefrontal/orbitofrontal cortex during learning versus online control?

## Key papers

- [[raw/summaries/fyhn2007_remapping_grid_realignment|Fyhn et al. 2007]] — strongest direct evidence that MEC grids provide a coherent spatial reference frame that realigns during hippocampal global remapping.
- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] — synthesis linking place/grid codes to transition structure, successor representations, and flexible behavior.
- [[raw/summaries/bush2015_grid_cells_navigation_vector|Bush et al. 2015]] — canonical algorithmic account of grid-based vector navigation.
- [[raw/summaries/sorscher2022_grid_cells_path_integration|Sorscher et al. 2022]] — computational clarification of when grid cells robustly emerge in trained path integrators.
- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] — influential replay review emphasizing planning and internal-model sampling.
- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] — updated replay synthesis connecting rodent replay phenomena to reinforcement-learning ideas.
- [[raw/summaries/liu2019_human_replay_reorganizes|Liu et al. 2019]] — key human evidence that replay reorganizes experience according to latent structure.
- [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]] — evidence for successor-like relational maps in human hippocampal–entorhinal cortex.
- [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]] — behavioral evidence that map formation in complex environments is staged and time-dependent.
- [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]] — clinical evidence linking impaired replay to weaker relational map formation.

## Source papers
- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] | [[raw/mds/behrens2018_cognitive_map_organizing_knowledge|source md]]: What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior
- [[raw/summaries/fyhn2007_remapping_grid_realignment|Fyhn et al. 2007]] | [[raw/mds/fyhn2007_remapping_grid_realignment|source md]]: Hippocampal remapping and grid realignment in entorhinal cortex
- [[raw/summaries/liu2019_human_replay_reorganizes|Liu et al. 2019]] | [[raw/mds/liu2019_human_replay_reorganizes|source md]]: Human Replay Spontaneously Reorganizes Experience
- [[raw/summaries/sorscher2022_grid_cells_path_integration|Sorscher et al. 2022]] | [[raw/mds/sorscher2022_grid_cells_path_integration|source md]]: When and why grid cells appear in trained path integrators
- [[raw/summaries/nour2021_impaired_replay_schizophrenia|Nour et al. 2021]] | [[raw/mds/nour2021_impaired_replay_schizophrenia|source md]]: Impaired neural replay of inferred relationships in schizophrenia
- [[raw/summaries/alonso2021_hexmaze_cognitive_map|Alonso et al. 2021]] | [[raw/mds/alonso2021_hexmaze_cognitive_map|source md]]: The HexMaze: A Previous Knowledge Task on Map Learning for Mice
- [[raw/summaries/bush2015_grid_cells_navigation_vector|Bush et al. 2015]] | [[raw/mds/bush2015_grid_cells_navigation_vector|source md]]: Using Grid Cells for Navigation
- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] | [[raw/mds/findlay2021_replay_wake_sleep|source md]]: The evolving view of replay and its functions in wake and sleep
- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] | [[raw/mds/foster2017_replay_memory_consolidation|source md]]: Replay Comes of Age
- [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]] | [[raw/mds/garvert2017_relational_knowledge_maps|source md]]: A map of abstract relational knowledge in the human hippocampal–entorhinal cortex
- [[raw/summaries/iyer2024_grid_cells_abstract_velocity|Iyer et al. 2024]] | [[raw/mds/iyer2024_grid_cells_abstract_velocity|source md]]: Flexible mapping of abstract domains by grid cells via self-supervised extraction and projection of generalized velocity signals
