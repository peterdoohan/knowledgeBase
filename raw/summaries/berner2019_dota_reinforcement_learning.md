---
source_file: berner2019_dota_reinforcement_learning.md
paper_id: berner2019_dota_reinforcement_learning
title: "Dota 2 with Large Scale Deep Reinforcement Learning"
authors:
  - "Christopher Berner"
  - "Greg Brockman"
  - "Brooke Chan"
  - "Vicki Cheung"
  - "Przemysław Dębiak"
  - "Christy Dennison"
  - "David Farhi"
  - "Quirin Fischer"
  - "Shariq Hashme"
  - "Chris Hesse"
  - "Rafal Józefowicz"
  - "Scott Gray"
  - "Catherine Olsson"
  - "Jakub Pachocki"
  - "Michael Petrov"
  - "Henrique Pondé de Oliveira Pinto"
  - "Jonathan Raiman"
  - "Tim Salimans"
  - "Jeremy Schlatter"
  - "Jonas Schneider"
  - "Szymon Sidor"
  - "Ilya Sutskever"
  - "Jie Tang"
  - "Filip Wolski"
  - "Susan Zhang (OpenAI)"
year: 2021
journal: "arXiv preprint (posted March 2021; describes April 2019 results)"
paper_type: computational
contribution_type: empirical
species:
  - human
frameworks:
  - reinforcement_learning
keywords:
  - large_scale_reinforcement_learning
  - self_play
  - distributed_training
  - ppo
  - lstm_policy
  - long_horizon_credit_assignment
  - data_staleness
  - sample_reuse
  - batch_size_scaling
  - continual_training
  - model_surgery
  - esports_ai
  - partial_observability
  - multi_agent_coordination
  - dota
  - large
  - scale
  - deep
  - reinforcement
  - learning
---

### One-line summary

OpenAI Five demonstrates that existing deep reinforcement learning methods, scaled to ~770 PFLOPs/s·days of compute over 10 months of self-play training, can defeat the Dota 2 world champions and win 99.4% of games against the general public.

---

### Background & motivation

Dota 2 is a complex real-time strategy game presenting challenges that prior AI milestones (Chess, Go, Atari) did not: long time horizons (~20,000 timesteps per episode), partial observability, high-dimensional continuous state and action spaces (~16,000 observations; 8,000–80,000 actions per timestep), and a live game environment that changes as updates are released. Prior work had demonstrated superhuman performance in board games (AlphaGo, AlphaZero) and early progress in video games (Atari DQN, StarCraft II AlphaStar), but no system had defeated world champions at a major esports title. The paper asks whether existing RL algorithms—with no algorithmic novelty beyond scale—can close this gap, and whether training can be sustained across continuous changes to the environment without restarting from scratch.

---

### Methods

- **Environment**: Dota 2 5v5 played on a subset of 17 heroes; semantic observation space (~16,000 floats/categoricals) rather than raw pixels; discretised action space.
- **Model architecture**: Five replicas of a shared policy (identical parameters θ); each replica controls one hero. Core is a single-layer 4096-unit LSTM (~159M parameters total; LSTM constitutes 84% of parameters). Observations are encoded into a single vector before the LSTM; outputs are policy logits and a value function.
- **Training algorithm**: Proximal Policy Optimization (PPO) with Generalised Advantage Estimation (GAE, λ=0.95). Adam optimiser with truncated BPTT over 16-timestep windows.
- **Distributed training system (Rapid)**: Rollout workers (CPUs) run self-play games at ~0.5× real-time; forward-pass GPUs sample actions in batches of ~60; optimizer GPUs (up to 1,536) compute gradients on experience buffers and synchronise via NCCL2 allreduce. Peak batch size: ~2.95 million timesteps per gradient step.
- **Self-play**: 80% of games against the latest policy; 20% against a pool of past policy snapshots.
- **Surgery**: Toolset for continuing training across changes to the model architecture, observation space, action space, and game version — using function-preserving or approximately function-preserving weight transformations, annealing of new features, and zero-padding of new weight matrices. ~20 surgeries performed over 10 months.
- **Reward shaping**: Dense reward function including kills, resource collection, and team-symmetrized signals; constructed once at project start with minor tweaks.
- **Evaluation**: TrueSkill rating against a fixed pool of reference agents; human evaluation against amateur, semi-pro, and professional teams culminating in a best-of-three match against world champions (Team OG).
- **Ablation experiments**: Batch size scaling (61k–1,966k timesteps), data staleness (queue length 0–32), and sample reuse (0.5–8×) in early training at 8× smaller scale. Long-horizon credit assignment studied by fine-tuning a skilled agent with different discount horizons (45s–720s).

---

### Key findings

- OpenAI Five defeated Dota 2 world champions Team OG 2-0 on April 13, 2019, the first AI victory over an esports world champion.
- In OpenAI Five Arena (7,257 public games), OpenAI Five won 99.4%; only 29 teams defeated it across 42 games.
- **Surgery**: Validated by training "Rerun" from scratch in the final environment; Rerun required ~150 PFLOPs/s·days and ~2 months to reach superhuman performance — roughly 20% of OpenAI Five's total compute. Rerun surpassed OpenAI Five's final TrueSkill (>98% winrate against OpenAI Five), suggesting surgery introduced a skill ceiling below the from-scratch optimum.
- **Batch size**: Increasing batch size from 61k to 983k timesteps yielded ~2.5× speedup to reach TrueSkill 175; speedup was sublinear in compute but still meaningful. Speedup appeared to increase at higher skill levels.
- **Data staleness**: Increasing staleness by ~8 parameter versions (a few minutes in a multi-month experiment) caused significant training slowdown. The final system targeted staleness of 0–1.
- **Sample reuse**: Reusing each data sample even 2–3× caused ~2× training slowdown; sample reuse of 8× prevented learning a competent policy. Final system targeted sample reuse ~1.
- **Long-horizon credit assignment**: Fine-tuning a skilled agent with progressively longer discount horizons (up to 6–12 minutes) monotonically increased win rate, demonstrating effective credit assignment across tens of thousands of timesteps.
- **Reaction time**: OpenAI Five reacted to game events in 217ms on average (typical human ~250ms), suggesting near-human-level reaction speed.
- **Win probability and auxiliary predictions**: The LSTM hidden state could be decoded to predict game outcomes and hero participation in future objectives with calibrated accuracy that improved over training.

---

### Computational framework

**Reinforcement learning — actor-critic with policy gradients (PPO/GAE).**

- The agent is modelled as a policy π: observation history → distribution over actions, parameterised as a recurrent neural network (LSTM).
- The objective is to maximise expected discounted return under a shaped reward function. PPO constrains the policy update using a clipped surrogate objective to prevent large parameter changes per step.
- GAE is used for advantage estimation: A(s,a) = Σ_t (γλ)^t δ_t, where δ_t = r_t + γV(s_{t+1}) − V(s_t). GAE λ=0.95 and discount horizon up to 840 seconds are used in the final system.
- Staleness is defined as the difference in parameter versions between data generation and optimisation; the system is designed to keep staleness near zero.
- Self-play provides the opponent distribution; past-opponent sampling (20%) prevents cycling and stabilises learning.
- The value function is shared with the policy (common LSTM trunk, separate heads). Win probability and auxiliary predictions (net-worth rank, building destruction) are trained as supervised heads on the LSTM state.

---

### Prevailing model of the system under study

The paper's framing — inherited from the broader deep RL literature — is that existing RL algorithms (PPO, actor-critic, self-play) are in principle sufficient for any goal-directed sequential decision-making task, but their practical reach is limited by computational scale and the tractability of long-horizon credit assignment. The introduction cites AlphaGo (2016), Atari DQN (2013), and concurrent StarCraft work (AlphaStar) as benchmarks, positioning Dota 2 as the next frontier due to its larger state/action spaces and longer time horizons. The implicit null hypothesis is that existing methods would fail to generalise to this regime — either through credit assignment failure over 20,000-step episodes, training instability in partially observable high-dimensional environments, or the practical impossibility of sustaining a long training run when the environment is continually changing.

---

### What this paper contributes

The paper establishes that no new RL algorithm is required to reach world-champion level in a highly complex, partially observable, real-time strategy game — scale alone is sufficient. It provides quantitative evidence for specific scaling laws in the RL regime: (1) batch size speedup is meaningful but sublinear; (2) data quality (staleness, sample reuse) matters more than raw compute and degrades sharply even at small violations; (3) effective credit assignment over 6–12 minute horizons is achievable by current gradient-based methods when a skilled agent is fine-tuned with longer discounts. The surgery methodology demonstrates that a 10-month training run can be maintained across ~20 changes to the model and environment at ~20% of the cost of restarting from scratch per change, though with a skill ceiling cost. Together, these findings provide an empirical foundation for the hypothesis that RL scaling — not algorithmic innovation — is the bottleneck for solving complex real-world-like tasks.

---

### Brain regions & systems

Not applicable. This is a purely computational study of an artificial agent; there is no anatomical, neural, or cognitive-neuroscience content. The level of analysis is algorithmic and systems-level AI engineering.

---

### Mechanistic insight

The paper does not meet the bar. It presents and implements a specific RL algorithm (PPO with GAE, LSTM policy) and provides extensive behavioural data (win rates, TrueSkill trajectories, ablation speedups) that characterise the algorithm's performance. However, it provides no neural data — it is an AI systems paper, not a neuroscience paper. The concepts of credit assignment, value function learning, and temporal discounting are studied at the computational/algorithmic level only, with no mapping to neural implementation.

---

### Limitations & open questions

- Surgery introduces a skill ceiling: Rerun (from-scratch) surpassed OpenAI Five's final skill despite using only 20% of the compute; how to maintain long-running training without this performance cost is identified as an open problem.
- Certain game mechanics were scripted (item buying, courier control) rather than learned; the paper acknowledges this may be suboptimal.
- The observation space is a hand-engineered semantic approximation rather than raw pixels; visual processing challenges are explicitly out of scope.
- The hero pool was restricted to 17 of 117 heroes; generalisation to the full game is unaddressed.
- Hyperparameter schedule was not optimised; the authors note Rerun's schedule is far from optimal and a single further tuning pass would likely improve it.
- Batch size speedup was studied only in early training at small scale; whether speedup increases at higher skill (as speculated) is untested.
- Off-policy robustness: high sensitivity to data staleness motivates exploring optimisers more robust to off-policy data, but this is left for future work.
- AlphaStar's full-information value network (opponent state visible to critic but not to policy) is identified as a potentially important technique not yet explored for Dota 2.
- The paper does not quantify the extent to which results generalise beyond Dota 2; the authors conjecture generality but provide no direct evidence.

---

### Connections & keywords

**Key citations**:
- Silver et al. 2016 (AlphaGo) — primary benchmark for scale comparison
- Vinyals et al. 2019 (AlphaStar / StarCraft II) — concurrent most-relevant comparison
- Schulman et al. 2017 (PPO) — core optimisation algorithm
- Schulman et al. 2015 (GAE) — advantage estimation method
- Horgan et al. 2018 (Ape-X / distributed prioritised experience replay) — related distributed RL system
- McCandlish et al. 2018 (large-batch training empirical model) — motivates batch size scaling analysis
- Chen et al. 2016 (Net2Net) — conceptual basis for surgery
- Mnih et al. 2013 (DQN / Atari) — foundational deep RL milestone
- Mnih et al. 2016 (A3C) — asynchronous actor-critic precursor
- Espeholt et al. 2018 (IMPALA) — related distributed deep RL architecture

**Named models or frameworks**:
- OpenAI Five — the trained agent
- Rapid — OpenAI's custom distributed training platform
- PPO (Proximal Policy Optimization)
- GAE (Generalised Advantage Estimation)
- Surgery — the continual transfer / model-morphing toolset
- Rerun — the from-scratch validation training run
- TrueSkill — automated skill rating system used for evaluation
- Net2Net — function-preserving transformation framework (adapted for surgery)

**Brain regions**: Not applicable.

**Keywords**: large-scale reinforcement learning, self-play, distributed training, PPO, LSTM policy, long-horizon credit assignment, data staleness, sample reuse, batch size scaling, continual training, model surgery, esports AI, partial observability, multi-agent coordination
