---
source_file: "hoang2021_successor_feature_landmarks.md"
paper_id: "hoang2021_successor_feature_landmarks"
title: "Successor Feature Landmarks for Long-Horizon Goal-Conditioned Reinforcement Learning"
authors: "Christopher Hoang, Sungryull Sohn, Jongwook Choi, Wilka Carvalho, Honglak Lee"
year: 2021
journal: "NeurIPS 2021"
paper_type: "computational"
contribution_type: "theoretical"
species: ["human"]
frameworks: ["reinforcement_learning", "successor_representation"]
keywords: ["successor", "feature", "landmarks", "long", "horizon", "goal", "conditioned", "reinforcement", "learning"]
key_citations: ["dayan1993_successor_representation", "barreto2017_successor_features_transfer_c"]
---

### One-line summary

A graph-based planning framework called Successor Feature Landmarks (SFL) that uses successor features to simultaneously enable exploration, build landmark graphs, and derive goal-conditioned policies without additional policy learning.

---

### Background & motivation

Goal-conditioned reinforcement learning (GCRL) becomes intractable for long-horizon goals because the space of state-goal pairs grows exponentially. Prior work either assumed access to human demonstrations, the ability to spawn uniformly across the state space, or ground-truth map information. SFL addresses the exploration challenge in large, high-dimensional state spaces without these assumptions.

---

### Methods

- **Successor Feature Similarity (SFS)**: A distance metric based on the cosine similarity between successor features (SF) computed under a random policy. SFS estimates geodesic distance between states while capturing environmental dynamics.
- **Landmark Graph Construction**: A non-parametric graph G = (L, E) where landmarks L are dynamically added based on SFS novelty (states with SFS < δ_add to nearest landmark), and edges E are formed when landmark transitions exceed threshold δ_edge.
- **Goal-Conditioned Policy**: Derived directly from SFS without policy learning. By setting reward weights w = ψ_π̄(g), the Q-value becomes Q(s, a, g) = ψ_π̄(s, a)^T · ψ_π̄(g), which equals the SFS between state-action and goal.
- **Exploration Strategy**: Count-based sampling of frontier landmarks (landmarks at the edge of explored region), planning paths to them, and using random policy for local exploration at frontiers.

---

### Key findings

- **Random spawn experiments (ViZDoom)**: SFL achieved 67% success on Hard tasks (goals 400-600m away) vs. 26% for SGM (previous state-of-the-art). Used only 2M environment steps vs. 250M+ steps for SPTM/SGM baselines.
- **Fixed spawn experiments (ViZDoom)**: SFL achieved 85% success on Easy, 59% on Medium, 62% on Hard, and 50% on Hardest. MSS baseline achieved only 23%, 9%, 1%, 1% respectively. EC+SPTM and EC+SGM also failed on Hard/Hardest.
- **Fixed spawn experiments (MiniGrid)**: SFL consistently outperformed MSS across difficulty levels, demonstrating robustness across environment types.
- **SFS visualization**: SFS heatmaps showed that states close to a reference state have high SFS values while states across walls have low values, confirming SFS captures geodesic distance structure.

---

### Computational framework

**Successor Features (SF) and Successor Feature Similarity (SFS)**. The framework builds on the decomposition of Q-value functions into successor features ψ_π(s, a) and reward weights w. By using a random policy π̄ to compute SF, SFS becomes a policy-independent metric that captures environmental dynamics. The key insight is that SFS serves triple duty: (1) as a distance estimate for graph construction, (2) as a state novelty measure for exploration, and (3) as a direct computation of Q-values for goal-conditioned policy without additional learning. This unified representation enables knowledge sharing between exploration, planning, and control modules.

---

### Prevailing model of the system under study

Prior to this work, long-horizon GCRL was addressed by augmenting goal-conditioned policies with graph-based planning. Methods like SPTM and SGM used deep networks as distance metrics for graph planning but relied on human demonstrations or replay buffer sampling to populate graph nodes. MSS extended UVFAs to long-horizon tasks using landmark graphs but was limited to low-dimensional state spaces. The prevailing assumption was that exploration mechanisms would be available separately or that the agent could spawn uniformly across the state space. The key gap was a unified framework that simultaneously addresses exploration and long-horizon planning in high-dimensional visual environments without these assumptions.

---

### What this paper contributes

SFL provides a unified framework where successor features serve as the foundation for exploration, graph construction, and goal-conditioned policy computation. The key advances are: (1) SFS as a triple-purpose metric that captures geodesic distance, enables direct Q-value computation without policy learning, and drives exploration via novelty estimation; (2) a graph-based planning framework that scales to high-dimensional visual environments (ViZDoom) without human demonstrations or ground-truth maps; (3) demonstration that a single self-supervised representation (SF) can support all components of a planning system, enabling knowledge sharing and stabilizing learning. The results establish that SFL significantly outperforms prior methods on long-horizon tasks, especially when exploration is required.

---

### Brain regions & systems

Not applicable. This is a purely computational reinforcement learning study with no neuroscientific or biological neural network focus. The work operates at the level of machine learning algorithms and artificial neural networks.

---

### Mechanistic insight

The paper provides algorithmic-level insight but does not meet the bar for mechanistic insight in biological systems. The framework proposes a computational algorithm (SFL using successor features for graph-based planning) and validates it through simulations in MiniGrid and ViZDoom environments. No neural data from biological organisms is presented. The successor feature representation itself is inspired by the successor representation from computational neuroscience (Dayan, 1993), but the paper does not claim or demonstrate biological plausibility for the SFL framework.

---

### Limitations & open questions

- The framework depends on learning good feature embeddings for SF; the authors suggest extending with algorithms for learning more robust feature embeddings.
- Extension to continuous action spaces is left for future work.
- SF learning requires sufficient coverage of the state space; the paper demonstrates this is achievable through frontier-based exploration but does not provide theoretical guarantees.
- The method was evaluated on navigation tasks; generalization to other types of long-horizon RL tasks (e.g., manipulation, hierarchical decision-making) is an open question.

---

### Connections & keywords

**Key citations**: Dayan (1993) - successor representation; Barreto et al. (2017) - successor features for transfer; Savinov et al. (2018) - SPTM; Laskin et al. (2020) - SGM; Huang et al. (2019) - MSS; Kaelbling (1993) - goal-conditioned RL.

**Named models or frameworks**: Successor Feature Landmarks (SFL), Successor Feature Similarity (SFS), Successor Features (SF), Successor Representation (SR), Universal Value Function Approximators (UVFA), Hindsight Experience Replay (HER), SPTM, SGM, MSS, Episodic Curiosity (EC), MiniGrid, ViZDoom.

**Brain regions**: Not applicable.

**Keywords**: successor features, goal-conditioned reinforcement learning, long-horizon planning, graph-based planning, landmark-based navigation, exploration, visual navigation, reinforcement learning, self-supervised learning, representation learning, geodesic distance, perceptual aliasing.
