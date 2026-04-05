---
source_file: akam2021_anterior_cingulate_model.md
title: "The Anterior Cingulate Cortex Predicts Future States to Mediate Model-Based Action Selection"
authors: Thomas Akam, Ines Rodrigues-Vaz, Ivo Marcelo, Xiangyu Zhang, Michael Pereira, Rodrigo Freire Oliveira, Peter Dayan, Rui M. Costa
year: 2021
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary
Using a novel two-step task in mice with calcium imaging and optogenetics, this study shows that ACC encodes action-state predictions and state-prediction surprise signals, and is causally necessary for model-based but not model-free reinforcement learning.

### Background & motivation
Model-based (MB) and model-free (MF) reinforcement learning (RL) represent parallel behavioral control systems that enable flexible and habitual behavior, respectively. MB control requires predicting the specific consequences of actions (states and rewards), but how this is implemented in the brain is poorly understood. Prior tasks for dissociating MB from MF control (e.g., the two-step task, Daw et al. 2011) were not well-suited to rodent neurophysiology, and had not been combined with single-unit recordings or causal manipulations in anterior cingulate cortex (ACC). An influential computational model (Alexander and Brown, 2011) proposed that ACC generates specific action-outcome predictions required for MB RL, but direct empirical tests were lacking.

### Methods
- **Task**: A novel two-step task for mice with four nosepoke ports; first-step choices (top/bottom port) led probabilistically (0.8/0.2) to one of two second-step states (left-active/right-active), where a water reward could be obtained. Critically, action-state transition probabilities underwent periodic reversals (unlike the original Daw 2011 task). Reward probabilities also changed independently, enabling dissociation of state prediction from reward prediction in neural activity. Dataset: 17 mice, 400 sessions, 230,237 trials.
- **Behavioral analysis**: Logistic regression of stay probabilities as a function of trial outcome and transition type (common or rare); lagged regression to assess multi-trial influences; RL model comparison to identify best-fitting mixture of MB and MF strategies with forgetting, perseveration, and multi-level motor representations.
- **Calcium imaging**: GCaMP6f expressed in ACC pyramidal neurons (CaMKII promoter); GRIN lens + miniature fluorescence microscope (miniscope); CNMF-E for cell extraction; n = 4 mice, 21 sessions, 2,385 neurons, 3,732 trials. Regression analysis of neuronal activity using predictors for choice, second-step state, outcome, and their interactions with transition/reward probability states.
- **Principal component analysis and decoding**: Population trajectory visualization; multinomial logistic regression decoding of 10 task state-action locations (95% accuracy).
- **Optogenetics**: JAWS (red-shifted inhibitory opsin) expressed bilaterally in ACC under CaMKII; red LED chronically implanted above cortical surface; single-trial inhibition from trial outcome to subsequent choice (randomly 1/6 trials). Experimental n = 11 JAWS mice; control n = 12 GFP mice; 77,350 and 71,071 trials respectively.
- **Control task**: Probabilistic reversal learning task (MB and MF recommend same behavior) to assess specificity of ACC effect.

### Key findings
1. **Behavioral dissociation**: The novel task recruited both MB and MF RL mechanisms. Common state transitions were reinforcing (MB signature), while the transition-outcome interaction was near zero but appeared with a lag (as predicted by models with transition-probability learning). Behavior best fit by a mixed MB+MF model with additional forgetting, perseveration, and multi-level motor representations.
2. **ACC state-action representation**: ACC activity decoded all 10 locations in the task's state-action space with 95% accuracy. Choice representation ramped up over the second before choice; second-step state was the most strongly represented event. Two orthogonal representations of second-step state occurred sequentially (pre-outcome and post-outcome), carried by different neuronal populations.
3. **Reward contextualized by state**: Reward representations were orthogonal for outcomes received in the two different second-step states — ACC encoded reward in a state-specific manner, not a general reward signal.
4. **Model-based decision variables**: ACC represented (a) current transition probability configuration, (b) predicted second-step state given chosen action (rising pre-choice), (c) whether transitions were common or rare (state prediction surprise, post-choice), and (d) the interaction of the reached second-step state with transition and reward probabilities (potential substrate for MB credit assignment). These were specific to transition probability context, not reward probability context.
5. **Causal necessity**: Optogenetic inhibition of ACC from trial outcome to next choice selectively reduced the influence of state transitions (common/rare) on subsequent choice (p = 0.007, Bonferroni corrected) without affecting direct reward reinforcement or transition-outcome interaction. Effect size across subjects strongly correlated with individual MB weight parameter (R = -0.91, p = 0.0001). No significant effect in simpler reversal learning task where MB and MF agree.

### Computational framework
The study is grounded in the model-based vs. model-free RL framework (Daw et al., 2005; Sutton and Barto, 1998). MB control maintains an internal model of action-state transition probabilities T(s'|c) and state values V(s), computing action values by forward simulation: Qmb(c) = sum_s P(s|c) * V(s). MF control caches values via temporal-difference (TD) prediction errors directly from reward. The paper tests and broadly confirms the Alexander and Brown (2011) theory that ACC implements action-outcome (specifically action-state) predictions. The best-fitting behavioral RL model incorporated forgetting for unchosen actions/unvisited states, multi-trial perseveration at choice and motor levels, and a mixture of MB, MF, and motor-level MF controllers with separate weights (Gmb, Gmf, Gmo). Transition probabilities were learned with a learning rate aT and forgetting rate fT, updated from experienced transitions.

### Prevailing model of the system under study
ACC has been broadly associated with monitoring action outcomes, reward-guided action selection, and updating behavior when outcomes are unexpected. An influential computational account (Alexander and Brown, 2011) proposes ACC as an action-outcome predictor generating expected outcomes of specific actions. Prior neuroimaging in humans found MB value signals and state prediction errors in anterior/mid-cingulate regions. Lesion work in macaques demonstrated ACC is needed for action-outcome learning. The dominant view before this paper was that ACC monitors outcomes and signals errors, but its specific role in predicting future states (as opposed to reward) and its causal necessity for MB (but not MF) RL had not been demonstrated.

### What this paper contributes
- First combined single-neuron recording and causal optogenetic manipulation in ACC using a task that formally dissociates MB from MF RL in mice.
- Establishes that ACC predicts future states given chosen actions (not just outcome value), and encodes state-prediction surprise.
- Demonstrates causally that ACC is selectively necessary for using action-state transitions to update choices, but not for basic reward-driven reinforcement.
- Introduces a novel two-step task variant with transition probability reversals that prevents confounded habitual strategies and enables dissociation of state vs. reward prediction in neural signals.
- Shows reward signals in ACC are context-specific (state-dependent), not generic.

### Brain regions & systems
- **Anterior cingulate cortex (ACC)**: Primary region of study; targeted at boundary of areas 24a/24b and mid-cingulate 24a'/24b'; expressed GCaMP6f and JAWS for imaging and inhibition.
- **Posterior dorsomedial striatum**: Massive innervation target of the recorded ACC region; known to be necessary for goal-directed action (outcome devaluation paradigms). Implicated as a downstream effector of ACC model-based signals.
- **Prefrontal cortex (broader context)**: Prelimbic, infralimbic, orbitofrontal cortices — differentially connected with rostral vs. caudal ACC; relevant for interpreting discrepancies with more rostral recording studies.

### Mechanistic insight
ACC predicts the specific second-step state that a chosen first-step action will lead to, given the current transition probability structure. This prediction is updated by learning from experienced state transitions. When a rare (surprising) transition occurs, ACC registers a state prediction error (common/rare transition signal). Crucially, ACC activity between trial outcome and next choice is necessary for translating that state prediction error into a behavioral update (altered subsequent choice), but not for reward-driven reinforcement. Different non-overlapping populations of ACC neurons carry the pre-outcome and post-outcome state representations, suggesting orthogonal coding of anticipated vs. observed states. Reward encoding is strongly gated by the state in which it is received, consistent with a role in assigning credit for rewards back to the action-state transition that produced them.

### Limitations & open questions
- Imaging performed in only 4 mice (small n), limiting statistical power for some sub-analyses.
- Optogenetic inhibition was applied from trial outcome to subsequent choice; it remains unclear whether ACC activity at the time of the state transition itself (before outcome) is critical for encoding the state prediction error, or whether the post-outcome period is the key locus.
- Whether the surprise signal reflects the state prediction error per se or its motor-action consequences cannot be fully resolved with the current design.
- The mechanistic basis of the behavioral difference between fixed and changing transition-probability task variants is unresolved — possible explanations include stronger MB influence, latent-state inference with habitual strategies, or successor representations.
- Cross-species generalization: recording locations and homologies between rodent and primate ACC require further validation.
- The role of ACC in representing latent task states (block structure) vs. forward action-state transition models remains to be fully distinguished.

### Connections & keywords
model-based reinforcement learning, model-free reinforcement learning, anterior cingulate cortex (ACC), two-step task, state prediction, action-outcome learning, calcium imaging, optogenetics, JAWS, GCaMP6f, miniscope, mice, sequential decision-making, transition probability, state prediction error, goal-directed behavior, habitual behavior, dorsomedial striatum, Alexander and Brown model, forward model, cognitive flexibility, population decoding, lagged logistic regression, RL model comparison
