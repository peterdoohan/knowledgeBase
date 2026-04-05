---
source_file: neupane2022_mental_navigation_entorhinal.md
title: Vector production via mental navigation in the entorhinal cortex
authors: Sujaya Neupane, Ila Fiete, Mehrdad Jazayeri
year: 2022
journal: bioRxiv (preprint)
paper_type: empirical
contribution_type: empirical
---

### One-line summary

The entorhinal cortex generates endogenous periodic activity matching the temporal structure of memorized landmarks during mental navigation, with continuous attractor dynamics that reduce behavioral variability through transient reset events.

### Background & motivation

Cognitive maps enable flexible mental computations without sensory input, but direct evidence for endogenous recruitment of these structured representations during purely mental navigation has been lacking. While spatially selective responses in hippocampus and entorhinal cortex have been documented during physical and virtual navigation, the critical prediction that cognitive maps are recruited endogenously during mental navigation without external input remained untested.

### Methods

- **Task design**: Monkeys performed a mental navigation (MNAV) task requiring them to produce one-dimensional displacement vectors between pairs of visual landmarks using a joystick without sensory feedback about intermediate landmarks
- **Pre-training**: Animals first learned a navigate-to-sample (NTS) task with visible landmarks to learn the linear map structure and joystick speed
- **Generalization test**: 15 of 30 possible landmark pairs were used for training; 15 held-out pairs tested for model-based generalization
- **Subjects**: Two male rhesus macaques (M. mulatta)
- **Recordings**: 32-channel and 64-channel laminar probes targeting posterior entorhinal cortex; 1478 single- and multi-units isolated using Kilosort 2.0 (Monkey A: 614, Monkey M: 864)
- **Analysis**: Periodicity index (PI) computed from autocorrelograms; targeted dimensionality reduction for population-level distance coding; cross-correlation analysis for attractor dynamics

### Key findings

- **Behavioral performance**: Monkeys successfully performed mental navigation, with produced vectors closely matching actual vectors (regression slopes near 1.0); animals immediately generalized to held-out landmark pairs, indicating use of structured cognitive map rather than model-free stimulus-response associations
- **Neural periodicity**: 16% (Monkey A) and 8.5% (Monkey M) of task-modulated EC neurons showed significant periodicity at 0.65 sec, matching the temporal distance between landmarks; periodicity was stronger during navigation than inter-trial intervals and weaker on error trials
- **Phase-locking to behavior**: Activity peaks were phase-locked to joystick offset at multiples of 0.65 sec, indicating animals learned to associate landmarks with specific phases of periodic activity
- **Distance coding**: Population-level analysis revealed robust linear encoding of temporal distance at joystick offset (tracking distance traveled) and weaker encoding at onset (representing desired distance)
- **Attractor dynamics**: Pairs of periodic neurons showed invariant cross-correlation structure across mental navigation and inter-trial intervals, consistent with continuous attractor dynamics; broad distribution of relative firing phases across cell pairs
- **Model predictions**: Continuous attractor network with Hebbian learning explained internal landmark reconstruction; model predicted that internal landmarks transiently slow path integration (reset dynamics), reducing behavioral variability; this prediction was confirmed by reanalysis of behavior showing sublinear growth of standard deviation with temporal distance

### Computational framework

**Continuous attractor network (CAN) with Hebbian learning**. The core model consists of grid cells (GCs) with lateral interactions creating repeating activity bumps that move via velocity inputs, supporting path integration. The model was augmented with plastic GC-to-landmark neuron (LM) connections using Oja's rule. Learning proceeded in two stages: first with both external and internal inputs (mimicking visible landmark conditions), then with internal inputs alone (mimicking mental navigation). The model demonstrates how internally generated landmarks can transiently reset path integration dynamics, reducing variability by dividing longer intervals into shorter segments.

### Prevailing model of the system under study

The prevailing understanding of cognitive maps, based on rodent and primate studies, holds that the hippocampal-entorhinal circuit encodes spatial and non-spatial relational structures during navigation. Grid cells in entorhinal cortex exhibit periodic firing patterns that support path integration, and these responses have been documented during both physical navigation and sensory-driven virtual navigation. The continuous attractor network model has been established as the canonical computational framework for grid cell dynamics, explaining how periodic spatial representations emerge from recurrent connectivity. However, a foundational prediction of cognitive map theory—that these structured representations can be recruited endogenously during purely mental navigation without sensory input—had not been directly tested prior to this work.

### What this paper contributes

This paper provides the first direct evidence that the entorhinal cortex recruits cognitive map representations endogenously during mental navigation without sensory feedback. The findings demonstrate that EC neurons generate periodic activity matching the temporal structure of memorized landmarks, and that this periodicity is linked to behavior (weaker on error trials, phase-locked to joystick offset). The paper establishes that these neural dynamics exhibit signatures of continuous attractor dynamics (invariant cross-correlation structure, broad phase distribution). The modeling work provides a circuit mechanism for how Hebbian plasticity enables internal reconstruction of landmarks, and generates a novel prediction—that internal landmarks transiently reset path integration dynamics—which was confirmed by behavioral reanalysis showing sublinear growth of timing variability. These results bridge the gap between cognitive map theory and neural circuit dynamics, demonstrating how structured EC representations support endogenous mental computations.

### Brain regions & systems

- **Entorhinal cortex (EC)** — primary recording site; neurons showed periodic activity matching landmark structure, distance coding, and signatures of continuous attractor dynamics during mental navigation; task-modulated neurons concentrated in posterior EC
- **Hippocampus** — mentioned as interconnected with EC and part of the cognitive map system; not directly recorded

### Mechanistic insight

This paper meets the high bar for mechanistic insight by presenting both a computational algorithm and neural data supporting it. The continuous attractor network model with Hebbian learning provides an algorithmic account of how internal landmarks are reconstructed, and this algorithm makes a specific prediction (transient reset dynamics reducing variability) that is confirmed by behavioral data.

**Marr's three levels:**

- **Computational**: The brain must solve the problem of producing precise temporal intervals during mental navigation without external feedback. The solution involves using a cognitive map with structured landmark representations to segment longer intervals into shorter, more reliable segments.

- **Algorithmic**: A continuous attractor network performs path integration via velocity inputs. Plastic connections from grid cells to landmark neurons (via Hebbian learning) enable internal reconstruction of landmark activity. During mental navigation, internally generated landmarks transiently "pin" the active bumps, resetting the dynamics and reducing accumulated variability.

- **Implementational**: The model is implemented in the entorhinal cortex, with grid cell-like neurons showing periodic activity and ramping responses. The neural signatures (periodicity at 0.65 sec, invariant cross-correlation structure, phase-locking to behavior) are consistent with continuous attractor dynamics in primate EC. The biological basis of plastic GC-to-LM connections remains to be tested.

### Limitations & open questions

- The biological basis of plastic connectivity between grid cells and landmark neurons, a key computational assumption, remains untested
- The velocity input in the experiment is internally generated (efference copy/reafference), requiring calibration of velocity gain or attractor landscape changes; the specific calibration mechanism is not fully characterized
- The source of distance coding signals at joystick onset and offset in EC is unknown; could reflect interactions with hippocampus or inputs from other brain areas
- The role of ramping activity in EC neurons is unclear—it may reflect inherited properties from recurrent interactions or inputs from other areas encoding upcoming events
- The model predicts the system should accommodate new joystick speeds if it can adjust velocity gain; this was not tested in the current experiment

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) — The Hippocampus as a Cognitive Map (foundational theory)
- Hafting et al. (2005) — Grid cells in entorhinal cortex
- Burak & Fiete (2009) — Continuous attractor network model of grid cells
- Yoon et al. (2013) — Evidence for continuous attractor dynamics in grid cells
- Behrens et al. (2018) — What Is a Cognitive Map?

**Named models or frameworks:**
- Cognitive map theory (O'Keefe & Nadel)
- Continuous attractor network (CAN) model
- Path integration
- Hebbian learning / Oja's rule
- Bayesian observer model

**Brain regions:**
- Entorhinal cortex (EC)
- Hippocampus
- Medial entorhinal cortex (MEC)

**Keywords:**
mental navigation, cognitive map, grid cells, entorhinal cortex, continuous attractor network, path integration, Hebbian learning, temporal distance coding, periodicity, landmark representation, endogenous recruitment, vector production, non-human primate, macaque monkey