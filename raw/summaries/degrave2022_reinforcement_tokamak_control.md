---
source_file: degrave2022_reinforcement_tokamak_control.md
paper_id: degrave2022_reinforcement_tokamak_control
title: "Magnetic control of tokamak plasmas through deep reinforcement learning"
authors:
  - "Jonas Degrave"
  - "Federico Felici"
  - "Jonas Buchli"
  - "Michael Neunert"
  - "Brendan Tracey"
  - "Francesco Carpanese"
  - "Timo Ewalds"
  - "Roland Hafner"
  - "Abbas Abdolmaleki"
  - "Diego de las Casas"
  - "Craig Donner"
  - "Leslie Fritz"
  - "Cristian Galperti"
  - "Andrea Huber"
  - "James Keeling"
  - "Maria Tsimpoukelli"
  - "Jackie Kay"
  - "Antoine Merle"
  - "Jean-Marc Moret"
  - "Seb Noury"
  - "Federico Pesamosca"
  - "David Pfau"
  - "Olivier Sauter"
  - "Cristian Sommariva"
  - "Stefano Coda"
  - "Basil Duval"
  - "Ambrogio Fasoli"
  - "Pushmeet Kohli"
  - "Koray Kavukcuoglu"
  - "Demis Hassabis"
  - "Martin Riedmiller"
year: 2022
journal: Nature
paper_type: computational
contribution_type: methodological
frameworks:
  - reinforcement_learning
keywords:
  - deep_reinforcement_learning
  - tokamak_magnetic_control
  - plasma_shape_control
  - actor_critic
  - mpo
  - sim_to_real_transfer
  - free_boundary_plasma_model
  - grad_shafranov_equation
  - domain_randomization
  - zero_shot_transfer
  - nuclear_fusion
  - real_time_control
  - snowflake_divertor
  - negative_triangularity
  - magnetic
  - control
  - tokamak
  - plasmas
  - through
  - deep
---

### One-line summary

A deep reinforcement learning architecture trained entirely in simulation successfully controls the full set of magnetic coils in a real tokamak, achieving accurate closed-loop plasma shaping across a diverse range of configurations including novel ones never previously demonstrated.

---

### Background & motivation

Nuclear fusion via magnetic confinement in tokamaks requires precise, high-frequency, closed-loop control of plasma position, current, and shape using multiple coupled magnetic coils — a high-dimensional, non-linear, time-varying control problem. The conventional approach relies on precomputed feedforward coil currents combined with multiple independent PID controllers, real-time plasma equilibrium reconstruction, and gain-scheduled linear controllers, all requiring substantial engineering effort to redesign whenever a new plasma configuration is desired. Reinforcement learning offers a radically different paradigm: specifying what the controller should achieve rather than how, allowing a single learned controller to replace the entire nested conventional architecture. Prior to this work, RL had not been applied to full magnetic controller design in a tokamak, due to challenges including high-dimensional actuation, long time horizons, rapid instability growth, and indirect shape measurement.

---

### Methods

- **Architecture overview**: Three-phase pipeline — (1) designer specifies objectives as a reward function; (2) deep RL (MPO actor-critic) trains a control policy in a physics simulator; (3) the trained policy is deployed zero-shot on real tokamak hardware.
- **Simulator**: Free-boundary plasma-evolution model (FGE software package) solving the Grad-Shafranov equation, coupled circuit equations for coil and plasma currents; computationally cheap enough for RL data collection.
- **RL algorithm**: Maximum a posteriori policy optimization (MPO), an actor-critic algorithm supporting distributed parallel data collection and data-efficient off-policy learning.
- **Asymmetric actor-critic**: The actor (policy network) is a small 4-layer MLP (266k parameters) satisfying real-time constraints (inference within 50 µs at 10 kHz); the critic uses a larger recurrent LSTM network (718k parameters) to handle non-Markovian dynamics, delays, and state inference during training only.
- **Domain randomization**: Plasma resistivity, pressure profile (β_p), current density profile (q_A), sensor noise, and power-supply delays are varied during training to ensure robustness.
- **Inputs/outputs**: Policy takes 92 sensor measurements (magnetic flux loops, field probes, coil currents) plus up to 132 time-varying control targets; outputs voltage commands to 19 control coils.
- **Deployment**: Policy is compiled to real-time binary code using tfcompile and runs on the TCV digital control system at 10 kHz; no fine-tuning after simulation training (zero-shot transfer).
- **Hardware**: Experiments performed on the Tokamak à Configuration Variable (TCV) at the Swiss Plasma Center, EPFL.
- **Training scale**: 5,000 parallel simulator actors on distributed infrastructure; 1–3 days of training per configuration.

---

### Key findings

- The RL controller successfully transfers from simulation to hardware without any fine-tuning, bridging the sim-to-real gap.
- Fundamental capability benchmark (current ramp, elongation, position, and diversion): plasma current RMSE of 0.62 kA (0.47% of target) and shape RMSE of 0.75 cm (2.9% of vessel half-width) across a full 1-second discharge.
- High elongation (κ = 1.9) with vertical instability growth rate of 1.4 kHz successfully stabilized despite acting at only 10 kHz; shape RMSE 1.6 cm, I_p RMSE 1.2 kA.
- ITER-like shape with neutral beam heating (H-mode entry, β_p up to 1.12): I_p RMSE 2.6 kA, shape RMSE 1.4 cm — demonstrating robustness to externally applied heating perturbations.
- Diverted negative triangularity (δ = −0.8): achieved with triangularity RMSE of 0.070, shape RMSE 1.3 cm.
- Snowflake divertor configuration with time-varying X-point distance (from 34 cm to 6.6 cm separation): X-point RMSE 3.7 cm, shape RMSE 0.65 cm.
- Two simultaneous plasma "droplets" sustained for the entire 200 ms control window — a previously undemonstrated configuration — achieved with minimal reward-function specification changes.
- Asymmetric actor-critic design is critical: a symmetric feedforward critic of comparable or even much larger size (up to 1,024-unit width, 3.4M parameters) fails to match the performance of the smaller recurrent critic (718k parameters).
- The controller autonomously discovers emergent behaviors, including creating a low-elongation round plasma to self-eliminate vertical instability when given only position/current objectives, and learning to spike coil voltages to prevent power supply "sticking" near zero current.

---

### Computational framework

The paper uses **deep reinforcement learning** (specifically the actor-critic MPO algorithm) to learn a closed-loop control policy.

- **What is being modelled**: A continuous-time, continuous-state, continuous-action control problem. The agent observes magnetic sensor readings and control targets (state s_t) and outputs voltage commands to 19 coils (action a_t) to maximize a scalar reward signal specifying proximity to desired plasma shape, current, and position.
- **Key variables**: Coil voltages (actions); magnetic flux and field measurements plus coil currents (observations); plasma current I_p, plasma boundary shape, vertical/radial position, X-point location (reward-relevant quantities); β_p and q_A (plasma profile parameters varied for robustness).
- **Actor-critic asymmetry**: The critic learns a Q-value function using an LSTM to handle partial observability and temporal correlations; the actor (policy) is constrained to a fast feedforward MLP for real-time deployment. MPO uses a KL-divergence constraint on policy updates for stable, data-efficient learning.
- **Key assumptions**: The Grad-Shafranov equilibrium assumption (toroidally symmetric force balance) is valid at the timescales of interest; a free-boundary model has sufficient fidelity for sim-to-real transfer; the reward function can be decomposed into weighted combinations of per-objective quality measures.

---

### Prevailing model of the system under study

The paper's introduction describes a well-established conventional control paradigm for tokamak magnetic control: precomputed feedforward coil-current and voltage profiles derived by solving an inverse equilibrium problem, supplemented by a set of independent single-input single-output PID controllers (for vertical stabilization, radial position, and plasma current), a real-time plasma equilibrium reconstruction algorithm running in the outer loop, and gain scheduling to handle time-varying targets. This architecture is effective but requires extensive expert engineering effort for each new plasma configuration, imposes computational overhead from real-time equilibrium reconstruction, and is fundamentally limited by its reliance on linearized dynamics. The introduction frames the field's prior state as one in which control is engineering-driven and configuration-specific, with the research community having identified machine learning — and specifically RL — as a priority opportunity but without prior demonstrations of RL achieving full magnetic controller design on hardware.

---

### What this paper contributes

The paper replaces the entire conventional nested control architecture with a single learned neural-network controller that can be applied to a broad range of plasma configurations by changing only the reward function specification. Key advances over the prior state:

- Demonstrates for the first time that RL can learn a magnetic confinement controller that transfers zero-shot from simulation to a real tokamak, successfully controlling 19 coils simultaneously.
- Eliminates the need for real-time equilibrium reconstruction as a separate module — the controller infers shape from raw magnetic measurements implicitly.
- Drastically reduces the controller development cycle: new configurations are produced by modifying the reward specification rather than redesigning the control architecture.
- Enables exploration of previously difficult or untested configurations (negative triangularity, snowflake, simultaneous droplets) with a general framework rather than bespoke engineering.
- Provides empirical justification that free-boundary equilibrium simulators have sufficient fidelity to develop controllers that transfer to hardware, supporting their use for future device design.
- Establishes that asymmetric actor-critic designs (expressive recurrent critic, constrained feedforward actor) are essential for high-dimensional physical control problems with partial observability and temporal correlations.

---

### Brain regions & systems

Not applicable. This paper is a computational/engineering study on tokamak plasma control. The level of analysis is engineering and physics: the control problem is framed at the level of physical actuators (magnetic coils), physical states (plasma current, position, shape), and a learned feedback controller. There is no biological or neuroscientific content.

---

### Mechanistic insight

Not applicable by the criteria of this section. The paper does not present a neural or cognitive algorithm, nor does it provide neural data. It is an engineering and applied RL study. The paper proposes and validates an RL-based control architecture for a physical system (tokamak plasma), but this is entirely outside the domain of neuroscience or cognitive mechanism. No mapping to Marr's levels is relevant here.

---

### Limitations & open questions

- Steady-state tracking errors remain for some quantities (e.g., elongation κ) due to the feedforward nature of the policy; recurrent policies could reduce this but risk overfitting to simulation dynamics and failing to transfer.
- The controller is not guaranteed to avoid plasma disruptions; a fallback machine-protection layer is required for deployment on less forgiving devices.
- Training time (1–3 days) with 5,000 parallel actors represents substantial computational cost, though simpler configurations can achieve comparable performance with far fewer actors.
- The simulator does not model transport of plasma pressure and current density profiles, which limits fidelity for strongly heated or transient plasmas; coupling to more complete physics simulators is noted as future work.
- Robustness properties of the non-linear learned controller are not analytically characterized; formal stability guarantees are absent.
- The approach has been demonstrated on TCV only; applicability to different devices (e.g., ITER) requires re-parameterization and is assumed but not yet demonstrated.
- Fine-tuning on real plant data is not yet incorporated, though it is identified as a potential avenue for improving performance on complex previously-unseen configurations.

---

### Connections & keywords

**Key citations**:
- Humphreys et al. (2020) — fusion ML research needs workshop (Priority Research Opportunities)
- Abdolmaleki et al. (2018) — MPO (relative entropy regularized policy iteration)
- Carpanese (2021) — FGE free-boundary simulator
- Moret et al. (2015) — LIUQE real-time equilibrium reconstruction
- Bellemare et al. (2020) — stratospheric balloon navigation with RL (Nature)
- Bishop et al. (1995) — early neural network plasma position control
- Seo et al. (2021) — feedforward beta control via RL on KSTAR
- De Tommasi (2019) — survey of plasma magnetic control in tokamaks
- Kates-Harbeck et al. (2019) — deep learning for disruption prediction (Nature)

**Named models or frameworks**:
- Maximum a posteriori policy optimization (MPO)
- Grad-Shafranov equation
- FGE (free-boundary equilibrium solver)
- LIUQE (real-time equilibrium reconstruction code)
- Asymmetric actor-critic architecture
- Domain randomization / parameter variation

**Brain regions**: None (not a neuroscience paper)

**Keywords**: deep reinforcement learning, tokamak magnetic control, plasma shape control, actor-critic, MPO, sim-to-real transfer, free-boundary plasma model, Grad-Shafranov equation, domain randomization, zero-shot transfer, nuclear fusion, real-time control, snowflake divertor, negative triangularity
