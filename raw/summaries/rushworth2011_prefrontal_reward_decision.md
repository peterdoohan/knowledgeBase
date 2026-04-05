---
source_file: rushworth2011_prefrontal_reward_decision.md
title: Frontal Cortex and Reward-Guided Learning and Decision-Making
authors: Matthew F.S. Rushworth, MaryAnn P. Noonan, Erie D. Boorman, Mark E. Walton, Timothy E. Behrens
year: 2011
journal: Neuron
paper_type: review
contribution_type: review
---

### One-line summary

Four distinct frontal lobe regions—vmPFC/mOFC, lOFC, ACC, and aPFC—make dissociable contributions to reward-guided learning and decision-making through specialized roles in value representation, credit assignment, action selection, and counterfactual evaluation.

### Background & motivation

Reward-guided decision-making depends on distributed neural circuits with many components. While there has been intensive study of reward-related brain activity, the specific functional contributions of different frontal cortex subregions remained unclear. This review synthesizes evidence from human fMRI and animal models to identify four frontal regions with distinct roles in reward-guided behavior, highlighting points of convergence and controversy across species and methods.

### Methods

- Comprehensive review of fMRI studies in human participants examining value-related BOLD signals
- Synthesis of single-neuron recording studies in macaques
- Analysis of lesion studies in macaques comparing effects of medial OFC (mOFC), lateral OFC (lOFC), and ACC lesions
- Comparison of anatomical connectivity patterns using diffusion-weighted MRI tractography
- Meta-analysis of reward-related fMRI activations and their anatomical localization

### Key findings

- **vmPFC/mOFC (ventromedial prefrontal cortex/medial orbitofrontal cortex)**: Encodes the subjective value of chosen and unchosen options; BOLD signal correlates with willingness-to-pay, expected reward value, and temporally discounted value; shows positive correlation with chosen option value and negative correlation with unchosen option value during decision-making; neurons modulated by motivational state/satiety.

- **lOFC (lateral orbitofrontal cortex)**: Critical for credit assignment—associating specific visual stimuli with reward values during learning; lesions cause misattribution of reward credit to wrong stimuli based on temporal proximity rather than causal association; neurons reactivate choice representations at feedback time; represents specific reward identity (taste, texture) rather than abstract value; stronger connections with temporal visual areas than vmPFC/mOFC.

- **ACC (anterior cingulate cortex)**: Integrates action-reward associations and effort costs with reward benefits; neurons sensitive to both reward and effort; essential for determining how animals respond to rewards and whether to invest effort; activity reflects volatility of reward environment and optimal learning rates; connected to motor areas enabling direct influence on action selection; distinct from OFC in specializing in action-based rather than stimulus-based value learning.

- **aPFC (anterior prefrontal cortex)**: Encodes counterfactual value—the value of alternative options not chosen; positive correlation with unchosen option value and negative correlation with chosen option value (opposite pattern to vmPFC/mOFC); activity predicts probability of switching to better alternatives; involved in exploration vs. exploitation decisions; may represent pending alternative behavioral states; in humans, shows strong connectivity with inferior parietal lobule during switching decisions.

- **Double dissociation**: mOFC lesions impair value discrimination when choice options have similar values (fine discrimination), while lOFC lesions impair performance when choice values are very distinct (easy decisions), consistent with credit assignment failure.

- **Species differences**: Human aPFC shows unique connectivity with inferior parietal cortex not seen in macaques; this lateral frontal pole region may represent an evolutionary specialization in hominoids for representing and switching between alternative courses of action.

### Computational framework

The review synthesizes evidence within a reinforcement learning and economic decision-making framework. Key computational concepts include:

- **Value representation**: vmPFC/mOFC encodes expected value (EV) and subjective value (SV) variables that guide choice, similar to state-values in RL models
- **Credit assignment**: lOFC implements mechanisms for associating outcomes with specific stimuli/actions, analogous to the structural credit assignment problem in RL
- **Prediction errors**: Discussion of how different frontal regions process outcome-related signals for learning, with ACC tracking volatility-modulated learning rates
- **Counterfactual learning**: aPFC encodes fictive prediction errors and alternative option values, enabling learning from foregone outcomes
- **Cost-benefit integration**: ACC combines reward and effort costs into integrated value signals for action selection

The review also draws on foraging theory (marginal value theorem) and economic decision theory (willingness-to-pay, Becker-DeGroot-Marschak method) to interpret neural signals.

### Prevailing model of the system under study

Before this review, the field had several established but incomplete or contradictory models:

1. **Reward vs. punishment dichotomy**: vmPFC/mOFC was thought to specialize in positive/appetitive outcomes while lOFC processed negative/punishment outcomes. This review argues this dichotomy is untenable given evidence that vmPFC/mOFC signals both appetitive and aversive value expectations.

2. **Orbitofrontal cortex as a unitary valuation system**: Many studies treated OFC as a single region encoding economic value. The review argues for fundamental functional distinctions between medial (vmPFC/mOFC) and lateral (lOFC) subregions.

3. **ACC as error detection system**: ACC was primarily associated with error detection and conflict monitoring. The review expands this to include reward-guided action selection, effort-based decision-making, and volatility-guided learning rate adjustment.

4. **Anterior prefrontal cortex as higher-order cognitive control**: aPFC was associated with complex reasoning and branching. The review adds a specific role in counterfactual choice representation and learning from foregone alternatives.

### What this paper contributes

This review establishes a new functional taxonomy of frontal cortex organization for reward-guided behavior with four distinct, dissociable roles:

1. **vmPFC/mOFC**: Abstract value representation and comparison for decision-making (not stimulus-specific identity). The region integrates value across reward types and modalities to guide goal selection, with signals modulated by motivational state.

2. **lOFC**: Stimulus-specific credit assignment during learning. This region associates specific visual stimuli with their outcomes, enabling proper attribution of rewards to their causal choices. Lesions cause misattribution of credit based on temporal contiguity rather than causal structure.

3. **ACC**: Action-reward association and cost-benefit integration for action selection. The region combines information about expected rewards, effort costs, and action requirements to guide motor output. It is specialized for learning and selecting actions rather than stimuli.

4. **aPFC**: Counterfactual choice representation and exploration. The region encodes the value of alternative, unchosen options and predicts switching behavior. It enables learning from foregone outcomes and exploration of alternative strategies.

The review also highlights species differences (human aPFC-parietal connectivity not present in macaques) and provides a framework for understanding neuropsychiatric conditions affecting decision-making.

### Brain regions & systems

- **vmPFC/mOFC (ventromedial prefrontal cortex/medial orbitofrontal cortex)**: Area 14m and adjacent medial orbital cortex; encodes abstract subjective value and expected reward; default network member; connects with reward-related subcortical structures; represents value integrated across reward types and modulated by motivational state.

- **lOFC (lateral orbitofrontal cortex)**: Lateral to medial orbital sulcus; specialized for credit assignment—associating specific stimuli with reward outcomes; strong connections with temporal and perirhinal visual areas; represents specific reward identity (taste, texture) rather than abstract value; neurons reactivate choice representations at feedback time.

- **ACC (anterior cingulate cortex)**: Includes ACC sulcus (ACCs) and ACC gyrus (ACCg); cluster 4 in Beckmann et al. (2009) parcellation; area 24c and adjacent regions; integrates action-reward associations; encodes both effort costs and reward benefits; strong motor connections enabling action selection; tracks environmental volatility to guide learning rates; responds to informative feedback during exploration.

- **aPFC (anterior prefrontal cortex)**: Area 10 in frontal pole or transition zone between area 10 and dorsolateral prefrontal cortex (area 46); lateral expansion in hominoids; encodes counterfactual value of unchosen options; predicts switching behavior; involved in exploration vs. exploitation; connects with inferior parietal lobule (IPL) in humans (not macaques); represents pending alternative behavioral states.

- **Posterior parietal cortex**: Shows opposite activation pattern to vmPFC/mOFC during decision-making; activity increases with decision difficulty (correlated with reaction time) and decreases with value difference between options; contrasts with vmPFC/mOFC which shows greater activation when value differences are larger.

- **Inferior parietal lobule (IPL)**: Interacts with aPFC during switching decisions; signals become more correlated on switch trials; coactive during exploratory choices; central IPL region in humans may be unique evolutionary specialization linked to aPFC expansion.

### Mechanistic insight

This review does not present new mechanistic data but synthesizes existing evidence to propose a functional architecture. The mechanistic insights are primarily at the algorithmic and computational levels rather than implementational:

**Computational level**: The four frontal regions solve different problems in reward-guided behavior:
- vmPFC/mOFC: Computes and compares subjective values to select goals
- lOFC: Solves the structural credit assignment problem—linking outcomes to their causal stimuli
- ACC: Integrates costs and benefits to select actions; implements foraging-like decision rules based on reward rate
- aPFC: Represents counterfactual values to enable learning from foregone outcomes and exploration

**Algorithmic level**: 
- vmPFC/mOFC implements value comparison with a frame of reference tied to the chosen option (chosen minus unchosen value), encoding opportunity costs
- lOFC implements credit assignment through reactivation of choice representations at feedback time, enabling specific stimulus-outcome associations
- ACC neurons multiplex information about reward, effort, and action, integrating these into unified value signals for motor control
- aPFC encodes relative unchosen probability/value (unchosen minus chosen), opposite to vmPFC/mOFC, representing the advantage of switching

**Implementational level**: The review notes some implementation-level differences:
- lOFC has stronger connections with visual/temporal areas than vmPFC/mOFC, explaining its stimulus-specificity
- ACC has stronger motor connections than OFC, explaining its action-related functions
- Human aPFC has unique connections with IPL not present in macaques, suggesting evolutionary specialization
- vmPFC/mOFC neurons are modulated by satiety while lOFC neurons are not, reflecting different value representations

The paper does not meet the high bar for mechanistic insight because it does not present new data linking specific algorithms to neural implementations through causal manipulations. However, it provides a comprehensive synthesis that constrains the space of possible mechanisms and highlights the need for future work combining detailed behavior, neural recordings, and causal interventions.

### Limitations & open questions

- The precise anatomical identity of human aPFC and its correspondence to macaque regions remains unclear; the human region may be a unique evolutionary specialization without exact macaque homolog.
- The exact nature of vmPFC/mOFC signals remains debated—whether they reflect automatic valuation, comparison processes, or opportunity costs.
- How vmPFC/mOFC and posterior parietal cortex make different contributions to decision-making remains to be determined.
- The precise computational mechanisms of effort encoding in ACC are uncertain and differ across studies depending on task design.
- Whether human aPFC area implicated in counterfactual choice has an exact homolog in macaques is unclear; recording studies may have been too medial.
- How the four frontal regions interact during natural behavior is largely unknown.
- The role of neuromodulators in shaping frontal cortex contributions to decision-making is not addressed.
- Whether similar functional distinctions exist in non-primate species remains to be determined.
- The relationship between frontal valuation signals and subcortical structures (basal ganglia, amygdala) in decision-making requires further investigation.

### Connections & keywords

**Key citations:**
- Padoa-Schioppa & Assad (2006, 2008) - offer-value and chosen-value neurons in OFC
- Behrens et al. (2007, 2008) - volatility-guided learning and social value in ACC
- Boorman et al. (2009, 2011) - counterfactual choice in aPFC
- Noonan et al. (2010) - double dissociation of mOFC and lOFC lesions
- Kennerley et al. (2006, 2009) - ACC and OFC action/stimulus value encoding
- Rudebeck & Murray (2011) - dissociable effects of OFC lesions
- Daw et al. (2006) - exploratory decisions and cortical substrates
- Plassmann et al. (2007, 2010) - willingness-to-pay and goal value in vmPFC
- Kable & Glimcher (2007) - subjective value and intertemporal choice

**Named models or frameworks:**
- Reinforcement learning (Sutton & Barto, 1998) - prediction errors and value learning
- Becker-DeGroot-Marschak (BDM) method - willingness-to-pay measurement
- Optimal foraging theory / Marginal value theorem (Charnov, 1976) - reward rate and patch-leaving decisions
- Drift-diffusion-like value comparison - vmPFC/mOFC and parietal cortex interactions
- Volatility-guided learning rate adjustment (Behrens et al., 2007) - Bayesian inference about environmental statistics

**Brain regions:**
- vmPFC/mOFC (ventromedial prefrontal cortex/medial orbitofrontal cortex) - value representation and comparison
- lOFC (lateral orbitofrontal cortex) - credit assignment and stimulus-reward learning
- ACC (anterior cingulate cortex) - action-reward associations, effort-cost integration, reward rate monitoring
- aPFC (anterior prefrontal cortex) - counterfactual choice, exploration, alternative option representation
- Posterior parietal cortex - decision difficulty, value difference encoding (opposite pattern to vmPFC)
- Inferior parietal lobule (IPL) - interaction with aPFC during switching decisions
- Ventral striatum - prediction error signals for chosen options
- Dorsal ACC/posterior cingulate - counterfactual prediction errors

**Keywords:**
- reward-guided decision-making
- prefrontal cortex
- orbitofrontal cortex
- value representation
- credit assignment
- reinforcement learning
- counterfactual choice
- effort-based decision-making
- anterior cingulate cortex
- exploration-exploitation
- neuroeconomics
- primate
- fMRI
- lesion studies
