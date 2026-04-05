# Hierarchical Reinforcement Learning

Hierarchical reinforcement learning is a computational framework in which decisions are organized across multiple levels of abstraction, with higher-level policies selecting among temporally extended actions (options or subroutines) that are executed by lower-level controllers. This framework maps naturally onto the hierarchical organization of frontal cortex and the distinction between automatic and controlled processing.

---

## Current understanding

Hierarchical RL extends standard RL by introducing abstraction over actions. Rather than selecting primitive actions (e.g., individual muscle movements), agents can select temporally extended "options" or subroutines that run until termination conditions are met. This creates a multi-level decision architecture where higher levels operate at longer timescales and coarser granularities, while lower levels handle fast motor execution.

This computational structure recapitulates key features of frontal cortex organization. The prefrontal cortex is organized hierarchically, with anterior regions operating at longer timescales and more abstract representations than posterior regions. The framework captures the distinction between automatic processing (well-learned action sequences executed by lower levels) and controlled processing (deliberate selection among options by higher levels). It also models the "cost of control"—the cognitive effort required to override automatic responses and engage higher-level control.

The hierarchical RL framework bridges RL and cognitive control research. Traditional RL focused on simple action selection, while cognitive control research focused on prefrontal mechanisms for task switching and inhibition. Hierarchical RL provides a unified computational account where both are special cases of multi-level decision making, with cognitive control corresponding to the engagement of higher-level option selection over lower-level habits.

---

## Key evidence

- Multi-level RL architectures in deep RL recapitulate features of frontal hierarchy, including cost-of-control mechanisms, automatic versus controlled processing distinctions, and timescale gradients across cortical areas. These architectures provide computational models for how frontal cortex might organize behavior hierarchically ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- Prefrontal cortex exhibits a rostro-caudal gradient where progressively more abstract behavioral representations are encoded more anteriorly, mapping the actor extensions required by HRL to distinct neural structures ([Botvinick 2008](../../raw/summaries/botvinick2008_hierarchical_behavior_prefrontal.md))

- Temporally abstract actions (options) reduce effective search-tree depth and accelerate learning, demonstrated by faster convergence in four-rooms navigation with doorway options versus primitive actions alone ([Botvinick 2009](../../raw/summaries/botvinick2009_hierarchical_behavior_reinforcement.md))

- Mismatched options cause negative transfer, slowing learning relative to primitive-action baseline; window-targeting options in door-navigated mazes and doorway options preventing shortcut exploitation demonstrate this phenomenon ([Botvinick 2009](../../raw/summaries/botvinick2009_hierarchical_behavior_reinforcement.md))

- Dorsolateral prefrontal cortex houses option representations; dorsolateral striatum implements option-specific policies; orbitofrontal cortex computes option-specific value functions ([Botvinick 2009](../../raw/summaries/botvinick2009_hierarchical_behavior_reinforcement.md))

- The hierarchical RL framework connects to earlier work by Botvinick et al. (2009) that linked hierarchical RL to prefrontal cortex function; deep RL extends this with modern scalable architectures that can learn hierarchical policies from high-dimensional inputs ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

### Behavioral Composition and Q-Value Averaging

- Mice compose novel hierarchical tasks by additively combining cortical action-value (Q) representations from previously learned subtasks, mirroring the arithmetic Q-averaging operation identified in deep reinforcement learning agents. Mice with subtask pretraining learned the composite task in approximately one session, whereas naive mice showed substantially slower acquisition (P < 0.001). ([Makino 2022](../../raw/summaries/makino2022_arithmetic_value_hierarchical.md))

- In deep RL agents, initializing the composite Q function by averaging the two subtask Q functions (Q_Composite = (Q_Task1 + Q_Task2)/2) produced rapid learning; initializing by taking the maximum of Q_Subtask did not (P < 0.001 vs scratch for average; P = 0.89 vs scratch for maximum). This establishes Q-averaging as the correct compositional operation for hierarchical behavior. ([Makino 2022](../../raw/summaries/makino2022_arithmetic_value_hierarchical.md))

- Q_Subtask representations were retained in individual cortical neurons during the early composite task phase (Q_Task1-encoding neurons: 8.3%, above chance of 5.3%, P < 0.001), with stable cortical distribution across subtasks and composite task (R² = 0.98 for Task 1, R² = 0.76 for Task 2). This demonstrates that subtask knowledge is preserved and reused during composition. ([Makino 2022](../../raw/summaries/makino2022_arithmetic_value_hierarchical.md))

- Mixed Q_Composite representations — single neurons spatially tuned to high-value states from both subtasks simultaneously — were observed in cortex at the early composite stage (20.7% of neurons, above chance of 16.1%, P = 0.006), consistent with averaging of Q_Subtask functions. This provides direct neural evidence for Q-averaging in biological circuits. ([Makino 2022](../../raw/summaries/makino2022_arithmetic_value_hierarchical.md))

- Population manifold analysis showed that intrinsic neural population geometry was preserved between subtask expert stages and composite task early stage (KL divergence significantly lower than shuffled baseline, P < 0.001), while subtask learning itself caused major manifold restructuring. The preservation of intrinsic population manifolds across task contexts enables reuse without costly representational restructuring. ([Makino 2022](../../raw/summaries/makino2022_arithmetic_value_hierarchical.md))

- Over composite task learning, Q representations transitioned from dedicated (subtask-segregated) to distributed (cross-cortical) circuits; this redistribution in mice was predicted with R² = 1.0 by the redistribution observed in ANN subnetworks (P < 0.001). This establishes a precise algorithmic correspondence between biological and artificial networks during hierarchical learning. ([Makino 2022](../../raw/summaries/makino2022_arithmetic_value_hierarchical.md))

- Policy entropy during subtask pretraining predicted composite task performance across individual mice (R² = 0.57, P < 0.001, n = 15 mice). Mice trained with deterministic policies (fixed initial position) learned the composite task more slowly (P < 0.001). This establishes that policy stochasticity (exploration) during pretraining is critical for compositional flexibility. ([Makino 2022](../../raw/summaries/makino2022_arithmetic_value_hierarchical.md))

- Neurons in mice and ANNs trained with higher-entropy policies showed broader directional tuning (P < 0.001 by KS test), providing a mechanistic link between policy stochasticity and compositional flexibility. Maximum-entropy (stochastic) subpolicies produce broadly tuned Q representations that enable flexible policy adjustment in composite tasks. ([Makino 2022](../../raw/summaries/makino2022_arithmetic_value_hierarchical.md))

---

- RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition ([Basu2021](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

## History of ideas

The hierarchical organization of behavior has been recognized since the early days of cybernetics and cognitive psychology. Miller, Galanter, and Pribram's "Plans and the Structure of Behavior" (1960) proposed that action is organized hierarchically, with "TOTE" (Test-Operate-Test-Exit) units representing temporally extended actions. This psychological intuition awaited computational formalization.

The formal RL framework for hierarchy emerged with the "options framework" proposed by Sutton, Precup, and Singh (1999). Options extend the primitive action space to include temporally extended actions with policies, initiation conditions, and termination conditions. This created a principled mathematical framework for hierarchical RL that preserved the convergence guarantees of standard RL while enabling temporal abstraction.

The neuroscience connection developed through work by Botvinick and colleagues. Botvinick (2008) and Botvinick et al. (2009) proposed that hierarchical RL provides a normative framework for understanding prefrontal cortex organization. The anterior-posterior gradient in frontal cortex was mapped to a hierarchical level gradient, with more anterior regions representing higher-level options and more posterior regions representing lower-level motor programs. The framework also accounted for the cost of cognitive control as the opportunity cost of engaging higher-level option selection over automatic lower-level execution.

The deep RL revolution transformed hierarchical RL from a theoretical framework to a practical learning system. Earlier hierarchical RL required hand-designed option hierarchies. Deep hierarchical RL (e.g., using feudal networks, option-critic architectures, or hierarchical actor-critic) can learn hierarchical policies from high-dimensional inputs, with the hierarchy emerging from the learning process rather than being pre-specified. This made hierarchical RL more relevant as a model of how biological hierarchies might develop through experience.

The current frontier involves connecting deep hierarchical RL to specific frontal circuits. The framework predicts that different prefrontal regions should show different temporal scales of activity modulation, different sensitivities to reward at different hierarchical levels, and different patterns of connectivity consistent with hierarchical information flow. Testing these predictions requires combining deep RL modeling with multi-region neural recordings during hierarchical decision tasks.

---

## Open questions

- How does the hierarchical organization in deep RL map onto specific anatomical circuits in frontal cortex? Are there precise correspondences between network layers and cortical layers, or between network modules and cortical areas?

- What is the developmental origin of behavioral hierarchies? Can hierarchical RL explain how structured behavior emerges during development, or does it require pre-existing hierarchical biases?

- How does the brain learn hierarchical policies rather than having them hand-designed? What neural mechanisms support the discovery of useful options or subroutines from experience?

- What is the neural implementation of the "cost of control"? How does the brain compute and factor in the cognitive effort cost of engaging higher-level control over automatic responding?

- How do hierarchical RL models account for the flexibility of human behavior? Can the framework explain rapid restructuring of hierarchies when task demands change, or transfer of subroutines across contexts?

- What distinguishes hierarchical RL from other mechanisms for sequential action organization (e.g., motor programs, chunking, schemas)? Can these be empirically distinguished?

## Key evidence

- Motor chunks and HRL options share three key structural properties: both are treated as single action units, both reduce computational complexity, and both facilitate more efficient learning of new sequences (transfer effects in M×N task; faster RTs with chunks in DSP task). ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

- In the M×N task, participants who retained previously learned chunks outperformed those whose chunks were disrupted by set shuffling, directly paralleling the efficiency gains predicted by HRL for option reuse. ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

- In the DSP task, participants can spontaneously discover more efficient chunk patterns even when instructed to use suboptimal ones, suggesting a biological analogue of the option-discovery process. ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

- Devaluation experiments in rodents show that dorsomedial PFC lesions eliminate sequence-level suppression, implicating this region in representing sequences as chunks. ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

- dlPFC represents movement sequences at multiple levels of abstraction simultaneously (shape, current movement, serial order), consistent with tracking option-specific policies and preparation before execution. ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

- Dorsal striatum (DS) activity shows task bracketing (start/stop signals for sequences) that closely parallels HRL initiation and termination conditions; this emerges with training and is present in rats, monkeys, and humans (caudate, putamen). ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

- Caudate neurons with outcome and cost representations become more tightly linked to sequence end with overlearning, consistent with the pseudo-RPE update signal required for option learning. ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

- Direct-pathway spiny projection neurons (dSPNs) preferentially signal sequence-level start/stop, while indirect-pathway SPNs (iSPNs) signal transitions between subsequences (options); stimulation of either population disrupts the option-specific policy. ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

- Disruption of striatal dopamine (pharmacologically or in Parkinson's patients off levodopa) impairs sequence chunking, implicating dopamine in option formation. ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

- Pre-SMA activity is higher for novel than overlearned sequences, suggesting a role in option discovery; SMA is more strongly activated for familiar chunked sequences, suggesting a role in option execution. ([Janssen 2022](../../raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md))

---

## Related pages

- [Deep Reinforcement Learning](deep_reinforcement_learning.md)
- [Reinforcement Learning](reinforcement_learning.md)
- [Model-based RL](model_based_rl.md)
- [Model-free RL](model_free_rl.md)
- [Prefrontal Cortex](../brain_regions/prefrontal_cortex.md)
- [Cognitive Control](../behaviours/cognitive_control.md) (if exists)
- [Action Selection](../behaviours/action_selection.md) (if exists)
