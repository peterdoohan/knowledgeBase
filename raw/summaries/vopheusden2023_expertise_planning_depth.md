---
source_file: vopheusden2023_expertise_planning_depth.md
title: Expertise increases planning depth in human gameplay
authors: Bas van Opheusden, Ionatan Kuperwajs, Gianni Galbiati, Zahy Bnaya, Yunqi Li, Wei Ji Ma
year: 2023
journal: Nature
paper_type: computational
contribution_type: theoretical
---

### One-line summary

Expertise in a complex board game (four-in-a-row) is characterized by increased planning depth and reduced attentional lapses, as revealed by a validated heuristic search model that predicts human choices, response times, and eye movements.

### Background & motivation

Despite decades of research on planning in board games like chess, it remains debated whether experts plan more steps ahead than novices. Traditional chess studies are difficult to model computationally, while simpler cognitive tasks impose ceilings on planning depth. The authors introduce a game of intermediate complexity (four-in-a-row) that allows skilled players to demonstrate deep planning while remaining tractable for computational modeling.

### Methods

- **Task**: Four-in-a-row game (generalized tic-tac-toe) on a 4x9 board with ~1.2x10^16 non-terminal states
- **Human-versus-human experiment**: n=40 participants, 50-minute sessions, no time pressure
- **Generalization experiment**: n=40 participants, play against computer opponents + 2AFC task + board evaluation task
- **Learning experiment**: n=30 participants, 5 sessions spaced less than or equal to 2 days apart, track skill improvement
- **Time-pressure experiment**: n=30 participants, 5s/10s/20s time limits per move
- **Eye tracking experiment**: n=10 participants, infrared video-based eye tracker (EyeLink 1000)
- **Turing test experiment**: n=30 observers classified move sequences as human or computer
- **Memory and reconstruction experiment**: n=38 (19 experts + 19 novices), memorize and reconstruct board positions
- **Mobile data**: 1,000 randomly selected users from Peak app who played at least 100 games

### Key findings

- **Model validation**: Model predicts out-of-sample choices with 40.8+-1.4% accuracy (chance ~6%, t_39=26, P<0.001)
- **Generalization**: Model predicts 2AFC decisions (58.6+-1.0%, t_39=8.3, P<0.001) and board evaluations (rho=0.377+-0.039, t_39=9.6, P<0.001)
- **Turing test**: Human observers achieved only 55.4% accuracy at discriminating human vs. computer moves
- **Response time prediction**: Model predicts response times (rho=0.351+-0.029, t_39=12, P<0.001)
- **Eye movement prediction**: Model's search distribution correlates with attention distribution (rho=0.535+-0.024, t_9=21, P<0.001), driven by branches reaching up to 7 moves deep
- **Expertise effects (learning experiment)**: Elo ratings increased across sessions (beta=21.6+-4.6, P<0.001); planning depth increased (beta=0.255+-0.061, P<0.001); feature drop rate decreased (beta=-0.0119+-0.0028, P<0.001); heuristic quality did not increase (beta=-0.0067+-0.0020, P=0.0012, slight decrease)
- **Time pressure effects**: Planning depth increased with longer time limits (beta=0.042+-0.018, P=0.019) but playing strength did not improve (beta=-2.0+-1.6, P=0.21); feature drop rate increased at longer time limits (beta=0.0027+-0.0010, P=0.009), canceling out planning benefits
- **Mobile data replication**: 1,000 app users showed increased playing strength (beta=1.13+-0.04, P<0.001), increased planning depth (beta=0.0108+-0.0010, P<0.001), decreased feature drop rate (beta=-2.58e-4+-4.7e-5, P<0.001), and increased heuristic quality (beta=6.12e-4+-4.2e-5, P<0.001) with experience
- **Memory reconstruction**: Experts better reconstruct game-relevant features (3-in-a-row: 84.2% vs 42.1% correct) but take more time, suggesting sharper representation of features enables more evaluations per unit time

### Computational framework

The model is based on **heuristic search** (best-first search), adapted from artificial intelligence literature. The framework consists of:

- **Value function**: Linear combination of board features (centre proximity, connected two-in-a-row, unconnected two-in-a-row, three-in-a-row, four-in-a-row) with learned weights, plus Gaussian noise
- **Active-passive scaling**: Feature weights for the active player are multiplied by constant C to capture turn-dependent value differences
- **Tree search**: Best-first search algorithm iteratively expands nodes on the principal variation (sequence of best moves for both players)
- **Pruning**: Eliminates branches with heuristic values below best move minus threshold theta
- **Early stopping**: Geometric stopping probability gamma after each iteration
- **Feature dropout**: Random omission of features (probability delta) models attentional lapses
- **Lapse rate**: Probability lambda of making random moves

The model implements a bounded rationality account of planning, where computational resources are preferentially allocated to promising branches of the decision tree.

### Prevailing model of the system under study

Before this work, the field held two competing views on the nature of expertise in planning: (1) pattern recognition/chunking accounts (de Groot, Chase & Simon, Gobet) emphasizing experts' superior ability to recognize meaningful board configurations; and (2) search-based accounts (Holding, Campitelli & Gobet) proposing that experts search more and deeper. However, these accounts were difficult to reconcile because chess is too complex for precise computational modeling, while simpler lab tasks impose ceilings on planning depth. The prevailing understanding was that expertise involves both better pattern recognition and deeper search, but their relative contributions and mechanistic relationship remained unclear.

### What this paper contributes

This paper establishes that expertise in complex planning is primarily characterized by increased planning depth and reduced attentional lapses, not improved heuristic quality (feature weights). The key advances are:

1. **Tractable task for expertise research**: Introduced four-in-a-row, a game of intermediate complexity (~10^16 states) that allows deep planning while remaining computationally tractable for modeling.

2. **Validated computational model**: Developed and validated a heuristic search model that predicts human choices (40.8% accuracy), response times (rho=0.351), and eye movements (rho=0.535). The model passes a Turing test (55.4% discrimination accuracy).

3. **Quantification of expertise**: Showed that across learning sessions, Elo gains (+90 points from sessions 1-5) are explained by increased planning depth (+36 points) and reduced attentional lapses (+46 points), with a small negative contribution from heuristic quality (-6.6 points).

4. **Mechanistic insight**: Demonstrated that experts' superior memory for board positions is specifically for game-relevant features (3-in-a-row: 84.2% vs 42.1% reconstruction accuracy), suggesting that sharper feature representations enable more evaluations per unit time, supporting deeper planning.

5. **Replication in naturalistic setting**: Replicated all expertise effects in large-scale mobile data (1,000 users, 100+ games each), showing generalization beyond laboratory settings.

### Brain regions & systems

Not applicable. This is a behavioral and computational modeling study without neural measurements. The authors speculate that orbitofrontal cortex may represent value of future states, and that cingulate and prefrontal cortices may encode prospective information, but these are hypotheses for future work.

### Mechanistic insight

This paper provides strong mechanistic insight at the algorithmic level, though without neural data to constrain implementation.

**Computational**: The brain solves a sequential decision-making problem under bounded computational resources, requiring trade-offs between search depth and breadth.

**Algorithmic**: The paper formalizes human planning as heuristic best-first search with:
- Feature-based value approximation (linear weighted sum of board patterns)
- Selective attention (probabilistic feature dropout, delta)
- Iterative deepening along principal variation
- Value-based pruning (threshold theta)
- Stochastic termination (geometric stopping, gamma)
- Motor lapses (random moves, lambda)

The model predicts not just choices but the temporal dynamics of search (response times) and spatial allocation of attention (eye movements), supporting the algorithmic interpretation.

**Implementational**: No direct neural evidence. Authors hypothesize that orbitofrontal cortex may encode state values, and that neural dynamics during move contemplation may reflect value of the root node over search iterations.

### Limitations & open questions

1. **No neural data**: The model provides behavioral and algorithmic-level accounts but lacks direct neural measurements to constrain implementational details.

2. **Fixed feature set**: The model uses a manually specified set of board features. While the authors show results are robust to alternative specifications, the possibility remains that humans use additional features not captured in the model.

3. **Deterministic games only**: The model applies to deterministic two-player games; stochastic or multiplayer games may require additional computational mechanisms.

4. **Heuristic quality ceiling effect**: Laboratory participants started with near-optimal feature weights, limiting observed improvement with expertise. Mobile data showed heuristic quality improvements, suggesting the laboratory setting may have selected participants with prior game experience.

5. **Time pressure puzzle**: Longer time limits increased planning depth but not playing strength, due to increased attentional lapses canceling out the benefit—suggesting optimal time allocation strategies may differ from simply "more time is better."

6. **Learning mechanism**: The model describes decision-making at a given skill level but does not explain how expertise develops through learning.

### Connections & keywords

- **Key citations**: de Groot (1946), Chase & Simon (1973), Gobet & Simon (1998), Charness (1991), Holding (1985), Campitelli & Gobet (2004), Daw et al. (2011), Huys et al. (2012), Miller & Venditto (2021), Mattar & Lengyel (2022)

- **Named models or frameworks**: Heuristic search, best-first search, minimax, feature-integration theory of attention, value function approximation, bounded rationality, Elo rating system, inverse binomial sampling, multilevel coordinate search

- **Brain regions**: Orbitofrontal cortex (hypothesized), cingulate cortex (hypothesized), prefrontal cortex (hypothesized), hippocampus (cited from animal literature)

- **Keywords**: planning depth, expertise, heuristic search, decision-making, board games, computational cognitive modeling, best-first search, feature dropout, attentional lapses, bounded rationality, eye tracking, response time, Turing test, reinforcement learning, pattern recognition, working memory, four-in-a-row, game playing, Elo rating
