---
source_file: porter2025_maze_rodent_behavior.md
paper_id: porter2025_maze_rodent_behavior
title: "Adapt-A-Maze: An Open-Source Adaptable and Automated Rodent Behavior Maze System"
authors:
  - "Blake S. Porter"
  - "Jacob M. Olson"
  - "Christopher A. Leppla"
  - "Éléonore Duvelle"
  - "John H. Bladon"
  - "Matthijs A. A. van der Meer"
  - "Shantanu P. Jadhav"
year: 2025
journal: eNeuro
paper_type: empirical
contribution_type: methodological
species:
  - rat
tasks:
  - morris_water_maze
methods:
  - optogenetics
  - electrophysiology
  - tetrode_recording
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - ventral_tegmental_area
keywords:
  - modular_maze
  - open_source_hardware
  - automated_behavior
  - rodent_navigation
  - electrophysiology_compatible
  - lick_detection
  - pneumatic_barriers
  - spatial_memory
  - reward_delivery
  - reproducibility
  - systems_neuroscience
  - tetrode_recording
  - place_cells
  - dopamine_neurons
  - sequence_memory
  - adapt
  - maze
  - open
  - source
  - adaptable
key_citations:
  - wijnen2024_maze_learning
---

### One-line summary

Development of an open-source, modular, and automated maze system (Adapt-A-Maze) that enables rapid configuration changes, standardized reproducibility across labs, and artifact-free neural recordings at approximately one-third the cost of commercial alternatives.

### Background & motivation

Traditional rodent maze systems are either inflexible single-piece designs or expensive commercial systems with proprietary software, limiting experimental flexibility and reproducibility. The field increasingly needs the ability to rapidly switch between maze environments within recording sessions to study contextual memory, spatial remapping, and flexible decision-making. Current solutions require either permanent allocation of space for multiple mazes or time-consuming physical reconfiguration, and commercial systems can cost tens of thousands of dollars.

### Methods

- **Hardware design**: Modular anodized aluminum track pieces (3" wide, 7/8" walls) designed on an 18-inch grid system, connected via custom 3D-printed PLA track joints
- **Leg assembly**: Individual track pieces supported by T-slotted beam legs (15" standard, up to 36" available) with quick-lock connector system
- **Reward system**: Integrated reward wells with IR beam break lick detection, visible signaling LEDs, and automated liquid reward delivery via syringe pumps; programmed lick requirements (typically >25 ms but <250 ms) before reward dispensing
- **Automated barriers**: Pneumatically driven barriers (0.4s up/down at 12 PSI, adjustable via flow control valves) controlled via 24V solenoids and relay board interfaced with TTL-capable controllers
- **Controller compatibility**: SpikeGadgets ECU, Arduino, Raspberry Pi, Neuralynx, Digital Lynx, Open Ephys
- **Validation**: Tested in rats with electrophysiology (tetrode recordings from hippocampus, prefrontal cortex, VTA) and optogenetics, demonstrating artifact-free operation during barrier movements and reward delivery

### Key findings

- Cost reduction: Complete eight-arm radial maze AAM system costs ~$9,500 (or ~$5,500 with peristaltic pumps) compared to $27,744 quoted for a commercial automated eight-arm maze in March 2025
- Assembly efficiency: Initial learning takes ~30 minutes for new users; experienced users can assemble a linear track in ~10 minutes and an eight-arm radial maze with barriers in ~1 hour
- Automation reliability: Pneumatic barriers operate at ~10 PSI with minimal air requirements; rats habituate to barrier sounds within 1–2 exposure sessions
- Neural recording compatibility: No detectable electrical artifacts in hippocampal LFP during simultaneous barrier operation and reward delivery
- Validation in real experiments: Successfully used to study hippocampal place cell encoding during sequence navigation tasks and VTA dopamine neuron responses around reward consumption
- Example neural data showed: spatially selective hippocampal neurons firing at end platforms of arms; neurons with selective firing to multiple arms; and diverse VTA responses including phasic responses at reward delivery, tonic responses during licking, and preemptive firing before lick onset

### Computational framework

Not applicable. This is a methodological paper focused on hardware development for behavioral neuroscience. The empirical data presented demonstrates system validation through established behavioral and neurophysiological measurements (place cell mapping, sequence memory tasks, reward-related neural activity) rather than computational modeling. The work enables experiments that could constrain models of spatial navigation, decision-making, and memory but does not itself propose or test computational frameworks.

### Prevailing model of the system under study

The prevailing model in the field assumes that rodent maze experiments require choosing between inflexible low-cost designs (single-piece wooden or plastic mazes) and expensive commercial systems with proprietary software. The field operates under the constraint that switching between maze environments within a single recording session is technically difficult or prohibitively time-consuming. Additionally, there is an implicit assumption that artifact-free electrophysiology requires expensive, custom-engineered solutions or significant technical expertise that limits adoption. The paper explicitly challenges these assumptions by demonstrating that open-source, modular, and automated designs can achieve the same or better functionality at lower cost with broader accessibility.

### What this paper contributes

This paper establishes that a modular, open-source maze system can match or exceed commercial alternatives in functionality while costing approximately one-third the price. The work demonstrates that rapid reconfiguration of maze environments (minutes rather than hours) is feasible within standard recording sessions, enabling new experimental paradigms studying contextual transitions and spatial remapping. The paper provides complete documentation and validation that artifact-free neural recording is achievable with open-source, non-proprietary hardware, lowering barriers to entry for systems neuroscience research. The automated barrier and reward systems reduce experimenter variability and increase throughput, while the standardized design enhances reproducibility both within and across laboratories. The work shifts the prevailing model from a binary choice between cheap inflexible designs and expensive commercial systems to a new paradigm where flexibility, automation, and affordability are not mutually exclusive.

### Brain regions & systems

- **Hippocampus (dorsal CA1)** — Recorded place cells during sequence navigation tasks; used as validation of artifact-free recording capability and demonstration of spatial selectivity in the AAM system
- **Prefrontal cortex** — Targeted for tetrode recordings alongside hippocampus; contributes to rule-switching task performance
- **Ventral tegmental area (VTA)** — Recorded dopamine neurons during reward consumption; demonstration of heterogeneous reward-related responses (phasic, tonic, preemptive) using the AAM reward system

### Mechanistic insight

Not applicable. This paper does not propose or test a specific algorithmic model of neural function. The work is methodological, presenting a hardware system that enables empirical investigations. The neural data presented validates that the system can record typical physiological phenomena (place cell firing, reward-related dopamine activity) without introducing artifacts, but does not itself provide mechanistic insight into how these neural computations are implemented. The paper enables future experiments that could constrain mechanistic models but does not directly address Marr's levels of analysis.

### Limitations & open questions

- **Physical stability**: Linear tracks can be unstable to forceful bumps; grid-based design limits some radial configurations
- **Three-dimensional limitations**: Current track pieces cannot create true 3D maze designs; requires modifications for vertical navigation
- **Spatial translation difficulty**: Simple translations or rotations of the maze in the room are difficult due to weak connections between track segments relative to leg weight
- **Grid constraints**: The 18-inch grid system limits potential maze designs for certain radial configurations, though users can create custom track pieces
- **Wear and tear**: Barrier material (corrugated plastic) can dislodge from air cylinders over hundreds of cycles; reward wells can be scratched by frustrated rats attempting to chew them
- **Electrical interference**: Pneumatic cylinders were chosen to avoid electrical interference from stepper motors (which were tested but found unsatisfactory); static discharge can occur in low humidity
- **Drainage**: Current reward well designs lack a drainage system; researchers must track wells where reward was dispensed but not consumed
- **Cleaning**: While aluminum is easy to clean, bleach must be kept off reward wells; tubes require periodic cleaning with pipe cleaners if viscous solutions are used
- **Open questions**: How will the research community extend and modify the system? What new experimental paradigms will emerge from rapid within-session maze reconfiguration? Can the system be adapted for mice or other species with appropriate size scaling?

### Connections & keywords

- **Key citations**: Wijnen et al. (2024) — review of rodent maze studies; Hoshino et al. (2020) — similar modular track system; O'Keefe and Dostrovsky (1971) — place cells; Olton and Samuelson (1976) — radial arm maze; Morris et al. (1982) — water maze; Tolman et al. (1946) — cognitive maps; Karlsson and Frank (2009) — awake replay; Small (1901) — early maze studies
- **Named models or frameworks**: Adapt-A-Maze (AAM) system; SpikeGadgets ECU (environmental control unit); DeepLabCut (pose estimation); MountainSort (spike sorting)
- **Brain regions**: hippocampus, dorsal CA1, prefrontal cortex, ventral tegmental area (VTA)
- **Keywords**: modular maze, open-source hardware, automated behavior, rodent navigation, electrophysiology-compatible, lick detection, pneumatic barriers, spatial memory, reward delivery, reproducibility, systems neuroscience, tetrode recording, place cells, dopamine neurons, sequence memory
