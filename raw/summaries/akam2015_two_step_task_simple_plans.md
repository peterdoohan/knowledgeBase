---
source_file: akam2015_two_step_task_simple_plans.md
title: "Simple Plans or Sophisticated Habits? State, Transition and Learning Interactions in the Two-Step Task"
authors: Thomas Akam, Rui Costa, Peter Dayan
year: 2015
journal: PLoS Computational Biology
paper_type: computational
contribution_type: methodological
---

### One-line summary
This paper demonstrates through simulation that model-free reinforcement learning agents can exhibit behaviour indistinguishable from model-based control on the two-step task, and analyses the mechanisms and analytical corrections needed to avoid this misidentification.

### Background & motivation
The two-step task (Daw et al. 2011) was developed to dissociate model-based from model-free reinforcement learning (RL) in humans and animals. Model-based RL plans prospectively using a learned transition model, while model-free RL caches action values through prediction errors without using such a model. The standard stay-probability analysis — examining how transition type (common/rare) and reward interact to predict repeating a first-step choice — is the main behavioural signature. As animal versions of the task were being developed, modifications to increase reward contrast between strategies were being adopted. The authors set out to identify whether these modifications, and the task's repeating structure more generally, introduce conditions under which model-free agents could masquerade as model-based.

### Methods
All analyses are computational (simulation-based), implemented in Python. Ten sessions of 10,000 trials each were simulated per agent. Two task variants were used:
- **Original task**: 70/30 common/rare transition probability; four drifting reward probabilities (Gaussian random walk on 0.25–0.75); choice at both steps.
- **Reduced task**: 80/20 transition probability; single action at second step; block-structured reward probabilities alternating between 0.8/0.2 and 0.2/0.8 in the two second-step states.

Five agent types were implemented and compared:
1. **Q(1) agent** (standard model-free): updates first-step action value directly from trial outcome, ignoring transition type.
2. **Q(0) agent**: updates first-step value from second-step state value only (no direct outcome signal).
3. **Model-based agent**: computes first-step action values as expectation over second-step state values, weighted by known transition probabilities.
4. **Reward-as-cue agent**: treats the combination of previous trial outcome and second-step state as a discriminative stimulus; learns separate Q-values for each of four such states, producing a fixed stimulus-response mapping.
5. **Latent-state agent**: maintains a Bayesian belief over which of two latent states the world is in (high reward in state a vs. b), and maps this belief to choice deterministically.

Behaviour was evaluated using three analyses: (i) stay-probability plots, (ii) logistic regression of stay/switch with predictors for outcome, transition, and their interaction (with and without a 'correct' predictor), and (iii) lagged logistic regression examining the effect of trial events at multiple lags. Model comparison used data likelihood and BIC.

### Key findings
1. **Spurious transition-outcome interaction for Q(1) on the reduced task**: The standard stay-probability analysis showed a significant transition-outcome interaction for the pure model-free Q(1) agent — the classical signature of model-based behaviour — even though the agent's update rule is blind to transition type. The mechanism is that action values at trial start are correlated with whether the agent chose the 'correct' action, which in turn correlates with which combination of transition and outcome will be observed.

2. **Correction via 'correct' predictor**: Including an additional logistic regression predictor that captures tendency to repeat correct choices (as proposed by Otto et al. 2013) completely removed spurious interaction loading for the Q(1) agent on the block-structured reduced task. A continuous version of the predictor (based on the reward-probability difference between states) was required to fully correct the effect when reward probabilities followed random walks.

3. **Reward-as-cue strategy mimics model-based on one-trial-back analysis**: This agent learns a fixed mapping (e.g., reward in state a → choose A next trial) using model-free RL applied to an extended state space. It produces a strong stay-probability transition-outcome interaction and outperforms Q(1) and Q(0) agents in reward obtained. It can be distinguished by lagged regression: only the immediately preceding trial is predictive of choice (no multi-trial decay).

4. **Latent-state strategy is nearly indistinguishable from model-based**: This agent infers which latent reward state the world is in (via Bayesian update) and applies a fixed action mapping. Its behaviour mimics model-based on both the one-trial-back and multi-lag analyses, with a similarly smooth decay of predictive weight at increasing lags. Discrimination from model-based agents requires explicit model comparison, and differences in likelihood (though statistically significant on 100,000-trial simulated datasets) will be difficult to detect in typical experimental datasets of ~200 trials.

5. **Original task is relatively robust**: The spurious interaction for Q(1) is very weak (P = 0.01, tiny effect) on the original task due to high stochasticity decorrelating action values from subsequent trial events. The reward-as-cue strategy produces only a weak effect. The latent-state strategy, however, produces behaviour qualitatively similar to model-based on the original task as well.

6. **Performance equivalence on original task**: With optimised parameters, Q(1), model-based, and other agents achieve statistically indistinguishable reward rates on the original task, demonstrating the low ceiling imposed by task stochasticity and the lack of performance incentive for model-based control in that version.

### Computational framework
The paper is framed within the model-based vs. model-free RL dichotomy from Daw et al. (2005, 2011). Q(λ) agents generalise between TD(0) and Monte Carlo returns via eligibility traces. The model-based agent uses forward planning with known or learned transition probabilities. Extended-state agents (reward-as-cue, latent-state) introduce an intermediate category: model-free RL algorithms applied to richer or inferred state representations, producing cached state-action mappings that approximate model-based behaviour. The latent-state agent is conceptually linked to the successor representation and to hidden Markov model inference over latent world states. The authors argue the MB/MF distinction is a spectrum rather than a binary.

### Prevailing model of the system under study
At the time, the dominant view held that the two-step stay-probability transition-outcome interaction was a reliable, relatively specific signature of model-based planning, with mixed model-based/model-free fits providing a quantitative measure of the balance between systems. Human subjects on the task were taken to use primarily model-based control (when informed of the structure in advance). Distinct neural circuits — prefrontal cortex and dorsomedial striatum for model-based; dorsolateral striatum for model-free — were assumed to implement these strategies, based on outcome devaluation literature.

### What this paper contributes
- Identifies and mechanistically explains a systematic confound in the standard stay-probability analysis: correlations between trial-start action values and subsequent trial events cause pure model-free agents to show transition-outcome interaction signatures when task structure creates asymmetric reward contingencies.
- Validates the 'correct' predictor correction for this confound.
- Introduces and formally analyses two novel extended-state strategies (reward-as-cue and latent-state) that exploit task regularities to produce model-based-like behaviour without prospective planning.
- Warns that animal versions of the task — which require enhanced reward contrast and involve overtraining — are particularly susceptible to these confounds.
- Raises the possibility that apparently model-based behaviour in humans after extended training may reflect latent-state inference rather than prospective planning.

### Brain regions & systems
The paper is purely computational and does not report neural data. However, the Discussion links extended-state strategies conceptually to cortical-basal ganglia loops: latent-state and reward-as-cue habits, once cached, may be instantiated in associative and limbic striatal sub-regions acting on higher-level cortical state representations, analogous to how stimulus-response habits in simpler tasks depend on dorsolateral striatum. The broader goal-directed vs. habitual literature implicates dorsomedial vs. dorsolateral striatum.

### Mechanistic insight
The core mechanistic insight is that the stay-probability analysis conflates two sources of regularity: (1) the trial-by-trial action value update (which distinguishes MB from MF agents), and (2) pre-existing correlations between action values carried into a trial and the statistical structure of events that will follow that trial. The second source arises because an agent that has learned which option is currently correct will have a larger value difference between options, and this correlates with subsequent transition-outcome combinations via the correctness of the choice. Extended-state strategies exploit a distinct regularity: in a task with block structure, the location of reward is informative about the latent reward state, and a fixed habit mapping from recent reward location to action can approximate or equal the performance of online planning.

### Limitations & open questions
- All results are based on simulation; no empirical human or animal data are analysed to demonstrate that extended-state strategies actually occur.
- The latent-state agent assumes exponentially distributed block lengths, not the fixed-length blocks used in most experiments; this mismatch may affect the degree of mimicry.
- Model comparison between latent-state and model-based agents requires very large datasets (>> typical 200-trial human experiments); practical discrimination remains an open problem.
- The paper does not propose a definitive task modification that fully prevents extended-state strategies while preserving sufficient reward contrast for animal use; reversals in the transition matrix are suggested but not evaluated.
- Mixtures of strategies (which likely characterise real subjects) are not modelled.
- Neural predictions distinguishing latent-state from model-based agents are not developed.

### Connections & keywords
model-based reinforcement learning, model-free reinforcement learning, two-step task, habit, goal-directed behaviour, state representation, latent state inference, stay probability, logistic regression, transition-outcome interaction, eligibility traces, successor representation, basal ganglia, outcome devaluation, hidden Markov model, reward prediction error, automatization, extended state space, behavioural neuroscience methodology
