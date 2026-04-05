---
source_file: whitlock2012_functional_parietal_entorhinal.md
title: Functional Split between Parietal and Entorhinal Cortices in the Rat
authors: Jonathan R. Whitlock, Gerit Pfuhl, Nenitha Dagslott, May-Britt Moser, Edvard I. Moser
year: 2012
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Posterior parietal cortex encodes self-motion and action states determined by behavioral organization, while medial entorhinal grid cells maintain spatial maps determined by environmental cues, revealing functionally distinct but parallel processing streams for navigation.

### Background & motivation

The hippocampal-entorhinal circuit is well-established for spatial mapping, but the role of posterior parietal cortex (PPC) in freely moving animals remained unclear. Whether PPC representations are controlled by spatial inputs (like the hippocampal-entorhinal circuit) or by movement-related factors, and whether PPC operates synchronously with or independently from spatial circuits, were unknown. Understanding how different cortical areas contribute to navigation requires distinguishing allocentric spatial representations from egocentric action-based representations.

### Methods

- Single-unit recordings from PPC (layers >500 μm) and MEC (layers II, III, V) in 8 freely foraging rats using chronically implanted microdrives
- Open field foraging task: 1.5 × 1.5 m box with black walls and floor
- Hairpin maze task: 10 interconnected alleys running north-to-south constructed by inserting walls into the open field floor grooves
- Two-room remapping experiments: identical hairpin mazes in different rooms to test spatial input sensitivity
- Virtual hairpin task: stereotyped laps in open field with experimenter-guided baiting to mimic hairpin maze running pattern without physical walls
- Self-motion rate maps: constructed from movement vectors (changes in position/heading over 100 ms windows) rather than spatial position
- Acceleration rate maps: calculated from changes in speed and direction
- Statistical validation: comparison against shuffled data distributions (99th percentile criterion)

### Key findings

- In open field: 43% of PPC cells showed significant self-motion tuning (vs. 15% of grid cells), with discrete firing fields for specific movement states (e.g., forward-left motion, rightward displacement, high forward velocity)
- PPC cells showed prospective coding: tuning to upcoming movements up to 500 ms before execution, with tuning falling off immediately after movement execution
- Grid cells in MEC expressed static spatial maps independent of movement state; only 11-15% showed any self-motion or acceleration tuning beyond chance
- In hairpin maze: PPC cells retuned completely to different movement states (mean correlation between open field and hairpin self-motion maps: r = -0.03); grid cells fragmented into direction-specific firing patterns
- Two-room experiment: PPC cells maintained same firing preferences across rooms (mean r = 0.47) while grid cells realigned completely (mean r = 0.03), showing PPC representations are independent of spatial inputs
- Virtual hairpin task: PPC cells retuned similarly to real hairpin (mean r = 0.32) despite identical physical environment as open field, confirming behavioral rather than spatial determinants of PPC tuning
- Representations in PPC and MEC change independently: PPC retunes with behavioral restructuring while grid cells remain stable (virtual hairpin), and PPC remains stable while grid cells remap (different rooms)

### Computational framework

The paper operates within a **sensorimotor transformation and reference frame transformation** framework. PPC is characterized as implementing egocentric/self-motion encoding, transforming bodily movement signals into action representations. The computational approach involves constructing firing rate maps based on self-motion vectors (velocity, acceleration) rather than allocentric spatial coordinates. This contrasts with the **spatial metric framework** of grid cells in MEC, which implement allocentric spatial coding via hexagonal firing fields. The paper implicitly uses Marr's levels of analysis: computational (what navigation problems are solved), algorithmic (how different representations encode information), and hints at implementation (which brain regions instantiate each representation).

### Prevailing model of the system under study

Prior to this study, the field understood that the hippocampal-entorhinal circuit (place cells and grid cells) provides the neural basis for spatial mapping and navigation. PPC was known to contribute to sensorimotor transformations and spatial navigation based on lesion studies, but its specific computational role was unclear. The prevailing assumption was that cortical representations for navigation would be synchronized across regions, with parietal activity reflecting spatial signals from the medial temporal lobe. Specifically, it was hypothesized that PPC transforms world-based spatial input into signals for directing first-person movements, but whether this transformation was driven by spatial or movement factors remained unresolved.

### What this paper contributes

This paper establishes a **functional split** between PPC and MEC: these areas operate in parallel with distinct, dissociable representations. PPC encodes self-motion and action states determined by behavioral organization, while MEC grid cells encode spatial maps determined by environmental cues. The paper demonstrates that PPC representations can remain stable despite complete remapping of spatial representations in MEC (different rooms), and conversely, PPC cells retune based on behavioral demands even when the spatial environment remains constant (virtual hairpin). This reveals that the parietal contribution to navigation concerns the **organization of actions** rather than the formation of spatial images. The findings also provide the first evidence of prospective coding in rodent PPC, showing tuning to upcoming movements 500 ms in advance.

### Brain regions & systems

- **Posterior parietal cortex (PPC)**: Central role in encoding self-motion and acceleration states; shows prospective coding for upcoming movements; representations determined by behavioral organization rather than spatial structure; maintains stable tuning across different spatial environments when task demands remain constant
- **Medial entorhinal cortex (MEC)**: Contains grid cells with static spatial maps; representations determined by spatial inputs; shows complete realignment (remapping) across different environments; independent of movement state
- **Postrhinal cortex (POR)**: Mentioned as potential anatomical integration site between PPC and MEC via reciprocal connections with both areas
- **Retrosplenial cortex (RSP)**: Mentioned as potential integration site between PPC and MEC; lesions impair navigation requiring path integration
- **Hippocampus**: Mentioned as part of the spatial mapping circuit with place cells; downstream of MEC

### Mechanistic insight

The paper provides strong algorithmic-level characterizations but does not fully meet the high bar for mechanistic insight requiring both an algorithm and neural data supporting that specific algorithm over alternatives. The paper characterizes what representations each area uses (Marr's computational and algorithmic levels): PPC implements self-motion and prospective coding of actions, while MEC implements spatial metric coding via grid cells. However, the paper does not provide neural data (e.g., specific cell types, connectivity patterns, or biophysical mechanisms) that would support one algorithmic implementation over alternative possibilities. The finding that representations in the two areas change independently (double dissociation) constrains models of navigation but does not in itself specify the physical implementation of either representation.

### Limitations & open questions

- The extent to which different anatomical pathways (POR, RSP) contribute to integration of PPC and MEC signals remains unknown
- Targeted manipulations of cellular activity in the pathways connecting the two areas are needed to understand how interactions between PPC and MEC contribute to goal-oriented navigation
- The precise role of cognitive/task demands versus pure behavioral restructuring in driving PPC retuning is not fully resolved
- Whether PPC prospective coding scales differently in tasks with different cognitive contingencies remains to be determined
- The relationship between PPC self-motion coding and specific thalamic or cortical inputs requires further investigation

### Connections & keywords

- **Key citations**: O'Keefe and Nadel (1978), Morris et al. (1982), McNaughton et al. (1996, 2006), Hafting et al. (2005), Derdikman et al. (2009), Fyhn et al. (2007), Nitz (2006), Sato et al. (2006), Andersen and Buneo (2002), Goodale and Milner (1992), Rizzolatti et al. (1997), Fogassi et al. (2005)
- **Named models or frameworks**: Self-motion encoding, prospective coding, grid cells, sensorimotor transformation, reference frame transformation, allocentric vs. egocentric coding, spatial metric system, path integration, cognitive map
- **Brain regions**: Posterior parietal cortex, medial entorhinal cortex, postrhinal cortex, retrosplenial cortex, hippocampus
- **Keywords**: self-motion, grid cells, parietal cortex, entorhinal cortex, navigation, spatial memory, prospective coding, sensorimotor transformation, allocentric, egocentric, remapping, behavioral tuning, acceleration, open field, hairpin maze, virtual hairpin, action organization, double dissociation, movement encoding, head direction, spatial mapping
