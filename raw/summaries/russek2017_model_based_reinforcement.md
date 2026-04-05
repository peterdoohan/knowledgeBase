---
source_file: russek2017_model_based_reinforcement.md
title: Predictive representations can link model-based reinforcement learning to model-free mechanisms
authors: Evan M. Russek, Ida Momennejad, Matthew M. Botvinick, Samuel J. Gershman, Nathaniel D. Daw
year: 2017
journal: PLoS Computational Biology
paper_type: computational
contribution_type: theoretical
---

### One-line summary

The successor representation (SR) enables model-like behavioral flexibility while maintaining a core temporal difference (TD) learning mechanism, providing a neurally plausible bridge between model-based and model-free reinforcement learning.

### Background & motivation

Standard theories posit that animals use two distinct systems for decision-making: a flexible but computationally expensive model-based system that plans using an internal model, and an automatic but inflexible model-free system that caches values via TD learning. However, rodent lesion studies and dopamine recordings suggest that these putatively distinct systems may share neural substrates, particularly involving dopaminergic-striatal circuits. This creates a puzzle: how can model-based flexibility arise from neural circuitry thought to implement TD learning?

### Methods

- **Computational framework**: The paper formalizes three reinforcement learning algorithms based on the successor representation (SR), which decomposes value computation into expected future state occupancies (M) and immediate reward weights (w).
- **Algorithm 1 (SR-TD)**: Uses TD learning to learn the successor matrix M directly from experience, caching expected future state occupancies.
- **Algorithm 2 (SR-MB)**: Learns a one-step transition model T and recomputes M at decision time using matrix operations, without requiring offline replay.
- **Algorithm 3 (SR-Dyna)**: Works with state-action pairs (H matrix) and uses offline replay of experienced transitions to update the successor representation, enabling off-policy learning.
- **Simulations**: All three algorithms were tested in grid-world spatial navigation tasks (10x10 environments) comparing performance on: latent learning, detour tasks, and a novel "policy revaluation" task designed to distinguish the algorithms.

### Key findings

- **SR-TD capabilities**: SR-TD successfully solves reward revaluation tasks (latent learning, reward devaluation, sensory preconditioning) without additional retraining, unlike pure model-free TD learning. However, it fails on transition revaluation tasks (detour problems) because cached state occupancies cannot be updated without direct experience of the new trajectories.
- **SR-MB capabilities**: SR-MB solves both reward revaluation and transition revaluation tasks by recomputing M at decision time from an updated one-step transition model. However, it fails on a novel "policy revaluation" task because its value estimates depend on the policy under which M was learned.
- **SR-Dyna capabilities**: With sufficient offline replay, SR-Dyna solves all three task types (reward, transition, and policy revaluation) by using replayed experiences to update the state-action successor matrix H. When replay is insufficient, SR-Dyna degrades to SR-TD behavior, still solving reward revaluation but failing transition and policy revaluation.
- **Computational comparison**: Unlike Dyna-Q, which degrades to pure model-free behavior without sufficient replay (failing all revaluation tasks), SR-Dyna retains reward revaluation capabilities even with limited replay, providing a distinctive empirical signature.

### Computational framework

The paper is grounded in reinforcement learning theory, specifically Markov decision processes (MDPs) and temporal difference (TD) learning. The core innovation is the successor representation (SR), a predictive state representation that decomposes the value function into: (1) expected discounted future state occupancies (the successor matrix M), and (2) reward weights associated with each state. This decomposition allows the agent to adapt to reward changes by updating only the reward weights (w), while transition changes require updating the successor matrix (M). The framework includes three variants: SR-TD (learning M via TD), SR-MB (computing M from a learned one-step model at decision time), and SR-Dyna (updating M via offline replay with off-policy learning).

### Prevailing model of the system under study

The standard view in reinforcement learning neuroscience posits two distinct systems: a model-free system that caches values via TD learning (associated with dorsolateral striatum and dopamine prediction errors) and a separate model-based system that performs tree-search or value iteration using an internal model (associated with dorsomedial striatum and prefrontal cortex). This dual-system view suggests that dopamine's role is primarily in model-free learning, with model-based planning occurring through different, non-dopaminergic mechanisms. The neural substrates were thought to be largely segregated, with different cortico-striatal loops supporting each system.

### What this paper contributes

This paper challenges the strict segregation of model-based and model-free systems by demonstrating that model-like behavioral flexibility can emerge from TD learning operating over predictive state representations (the successor representation). The key contributions are: (1) showing that SR-TD can explain reward revaluation tasks (a hallmark of model-based behavior) while remaining grounded in TD learning; (2) introducing SR-MB and SR-Dyna as extensions that progressively address limitations of the original SR; (3) providing a unified neural implementation where both "model-based" and "model-free" behaviors arise from the same dopaminergic-striatal circuitry operating over different cortical input representations; (4) predicting distinctive behavioral signatures (policy revaluation task, differential effects of replay manipulations) that can distinguish SR-based algorithms from both pure model-free and full model-based learning; and (5) reconciling lesion studies showing overlapping neural substrates for model-based and model-free learning with the computational requirements of flexible planning.

### Brain regions & systems

- **Dorsomedial striatum**: Proposed locus of SR-based value computation; lesions here impair reward devaluation sensitivity, consistent with the SR-TD model.
- **Dorsolateral striatum**: Proposed locus of model-free TD learning over punctate state representations; lesions here preserve devaluation sensitivity even after overtraining.
- **Prefrontal cortex (ventromedial)**: Candidate region for encoding the successor representation (M), providing predictive state input to dorsomedial striatum.
- **Hippocampus**: Alternative candidate for SR encoding; evidence shows hippocampal place cells encode predictive representations consistent with the SR, and hippocampal replay may support SR-Dyna updates.
- **Substantia nigra pars compacta / VTA**: Dopaminergic prediction error signals that update both model-free values (in dorsolateral striatum) and SR-based values (in dorsomedial striatum) via modulation of corticostriatal synapses.
- **Corticostriatal loops**: Parallel but structurally homologous loops (dorsomedial and dorsolateral) proposed to implement different input representations (SR vs. punctate states) while sharing the same TD learning mechanism.

### Mechanistic insight

This paper provides a mechanistic account of how model-based behavioral flexibility can arise from neural circuitry implementing TD learning. The framework meets the criteria for mechanistic insight by specifying both an algorithm and connecting it to neural data.

**Computational level**: The brain must solve the problem of evaluating actions based on long-run cumulative rewards in sequential decision tasks. The SR achieves this by decomposing value into expected future state occupancies (M) and reward weights (w), allowing flexible recomputation when either component changes.

**Algorithmic level**: Three variants are proposed: (1) SR-TD learns M via TD updates from direct experience; (2) SR-MB computes M at decision time from a learned one-step transition model; (3) SR-Dyna updates M via offline replay of experienced transitions using off-policy learning. All three use TD learning for reward weights w, enabling dopaminergic prediction errors to update values in all cases.

**Implementational level**: The framework maps onto cortico-striatal architecture: prefrontal cortex or hippocampus encodes the predictive state representation (M), providing input to medium spiny neurons in dorsomedial striatum that represent values; dopaminergic prediction errors from substantia nigra/VTA modulate corticostriatal synapses to update values. This parallels the known model-free circuit (sensory/motor cortex → dorsolateral striatum) but uses predictive rather than punctate representations. The SR-Dyna variant additionally involves hippocampal replay during rest/sleep to update the successor matrix offline.

### Limitations & open questions

- The current framework does not address how the SR handles hidden states or partial observability, which are common in real-world decision problems.
- The model assumes deterministic or well-estimated transition structures; how SR-based algorithms perform under high environmental stochasticity remains to be fully characterized.
- The neural locus of the SR (hippocampus vs. prefrontal cortex) is not definitively established; both regions have supportive evidence but their specific roles remain unclear.
- The prioritization of replay (which memories to replay when) is left underspecified; the current model uses naive random sampling rather than biologically realistic replay dynamics.
- Whether animals can truly solve transition revaluation (detour) tasks without re-experiencing the full trajectories remains empirically unclear; the classic Tolman results are mixed and modern studies often confound local learning with full-path learning.
- The paper does not fully specify how the brain might arbitrate between different planning strategies (SR-TD, SR-MB, SR-Dyna, pure model-free, full model-based) depending on task demands and time constraints.

### Connections & keywords

- **Key citations**: Dayan (1993) - original successor representation; Sutton & Barto (1998, 2012) - reinforcement learning foundations; Daw, Niv & Dayan (2005) - dual-system model-based/model-free account; Tolman (1948) - cognitive maps and latent learning; Dyna architecture (Sutton, 1991); Stachenfeld, Botvinick & Gershman (2014, 2017) - hippocampal predictive maps; Yin, Ostlund et al. (2005) - dorsomedial striatum lesions and devaluation.
- **Named models or frameworks**: Successor representation (SR); SR-TD (TD learning of successor matrix); SR-MB (model-based recomputation of successor matrix); SR-Dyna (replay-based off-policy successor learning); Dyna-Q; Markov decision processes (MDPs); Temporal difference (TD) learning; Model-based vs. model-free reinforcement learning.
- **Brain regions**: Dorsomedial striatum (DMS); Dorsolateral striatum (DLS); Prefrontal cortex (PFC, ventromedial); Hippocampus; Substantia nigra pars compacta (SnC); Ventral tegmental area (VTA); Basal ganglia; Orbitofrontal cortex (OFC).
- **Keywords**: successor representation, reinforcement learning, model-based, model-free, temporal difference learning, dopamine, striatum, hippocampus, prefrontal cortex, replay, planning, reward revaluation, detour task, latent learning, cognitive map, grid-world, markov decision process, state representation, predictive coding.
