---
source_file: yoshida2006_resolution_uncertainty.md
title: Resolution of Uncertainty in Prefrontal Cortex
authors: Wako Yoshida, Shin Ishii
year: 2006
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary
Distinct regions of prefrontal cortex implement specific computational functions for Bayesian decision-making under uncertainty, with anterior prefrontal cortex (APF) encoding uncertainty about hidden states and medial prefrontal cortex (mPFC) mediating belief revision.

### Background & motivation
Making optimal decisions with uncertain or incomplete information is a fundamental cognitive challenge, particularly in navigation tasks where one must locate a goal from an unknown position. While the neural basis of decision-making has been extensively studied, how the brain resolves uncertainty about partially observable states—maintaining and updating beliefs based on incoming information—remains poorly understood. This study addresses how distinct prefrontal regions implement the computational processes required for sequential decision-making under uncertainty.

### Methods
- **Task design**: Subjects performed a maze navigation task in a learned 7×7 wire-frame maze with no dead-ends or crossroads. In goal-search blocks, subjects navigated to a specified goal from an unknown starting position using only local 3D visual information (current and surrounding grid walls). In visuomotor control blocks, subjects simply pressed buttons corresponding to visually indicated actions.
- **Subjects**: 13 healthy adults (11 male, 2 female, aged 23–28)
- **Key measurements**: fMRI BOLD responses during task performance; reaction times (RTs) for each trial; behavioral sequences of actions and observed scenes
- **Analysis approach**: Hidden Markov Model (HMM) with Bayesian belief updating to estimate subjects' hidden cognitive states (position estimates and operant modes). Two key regression functions derived from the model: (1) Hidden Current Position (HCP) entropy (quantifying uncertainty about position) and (2) Back-Track (BT) probability (likelihood of re-estimation/revision). These parametric modulators were used in fMRI general linear models.

### Key findings
- **Block-level activation**: Goal-search vs. visuomotor subtraction revealed activation in dorsolateral prefrontal cortex (DLPF; BA46), anterior cingulate cortex (ACC; BA32/8), bilateral posterior parietal cortex (PPC; BA40/7), thalamus, and basal ganglia (putamen, caudate, globus pallidus, substantia nigra)
- **Back-track probability correlates**: mPFC (BA9/6) and bilateral PPC activity correlated with BT probability. mPFC showed significantly higher activity during back-track mode vs. update mode (t = 4.20, p < 0.0001)
- **Uncertainty correlates**: Bilateral anterior prefrontal cortex (APF; BA10 medial frontal gyrus and BA9 superior frontal gyrus) activity correlated with HCP entropy (positional uncertainty). Mean correlation with HCP entropy: left r = 0.29 ± 0.22, right r = 0.27 ± 0.19; significantly positive for 10/13 subjects
- **Model validation**: HMM action prediction accuracy was 88.7% ± 2.9%, correlating significantly with task performance (r = 0.49, p < 0.00001). RT peaks coincided with BT peaks in 86.1% of trials, validating the model's cognitive state inference

### Computational framework
**Bayesian inference in partially observable Markov decision processes (POMDPs)**. The paper formalizes navigation under uncertainty as a POMDP, where the subject cannot directly observe their current position (hidden state) but must infer it from observations (3D scenes). The key computational components are:
- **Belief representation**: The subject maintains a probability distribution (belief) over possible position states, computed via incremental Bayesian updating (filtering). Prior belief is updated with observation likelihood to yield posterior belief.
- **Uncertainty quantification**: Shannon entropy of the belief distribution (HCP entropy) quantifies the computational load of maintaining multiple position candidates.
- **Belief revision**: When predictions fail (observed scene ≠ predicted scene), the system back-tracks to re-estimate position, requiring enumeration of new candidates consistent with action history.

The framework assumes optimal or near-optimal Bayesian inference, with the HMM capturing individual differences through parameters for action selection optimality (α = 0.8) and back-track depth (n = 1).

### Prevailing model of the system under study
Before this study, the field understood that prefrontal cortex broadly supports decision-making and executive function, but the specific computational roles of distinct PFC subregions in uncertain environments were not well delineated. The anterior prefrontal cortex (APF, particularly frontopolar BA10) had been implicated in complex cognitive tasks involving multiple competing rules (Braver & Bongiolatti, 2002; Koechlin et al., 2000; Strange et al., 2001), suggesting a role in handling internally-generated information and integrating lateral PFC representations. Medial PFC was associated with self-referential processing and performance monitoring based on reward prediction. The anterior cingulate was linked to error detection and conflict monitoring. However, how these regions specifically implement the computational demands of belief maintenance and updating under partial observability remained unclear.

### What this paper contributes
This paper demonstrates that distinct prefrontal subregions implement specific computational components of Bayesian decision-making under uncertainty:

1. **APF (BA10) encodes uncertainty about hidden states**: The bilateral APF activity correlates with HCP entropy—the Shannon entropy of the belief distribution over possible positions. This establishes that APF maintains the representation of uncertainty itself, not just the position estimate. This extends prior findings by showing APF tracks a continuous measure of uncertainty (entropy) rather than simply indicating presence of conflict or multiple rules.

2. **mPFC (BA9/6) implements belief revision**: Medial PFC activity correlates with back-track probability and is elevated during re-estimation trials. This identifies mPFC as the locus of error detection and subsequent belief revision when predictions fail, linking it to the computational process of updating beliefs based on observation-prediction mismatches.

3. **Methodological innovation**: The paper demonstrates the utility of model-based fMRI analysis using Bayesian inference to estimate hidden cognitive states (beliefs) that cannot be directly observed, then using these estimates as parametric regressors. This marginalization approach overcomes instability from point estimates and provides a template for studying internal cognitive states.

4. **Functional segregation in PFC**: The results support a computational architecture where APF maintains uncertainty representations, mPFC handles belief revision, and lateral PFC/DLPF performs action selection—providing a more nuanced view of PFC organization than previous coarse functional assignments.

### Brain regions & systems
- **Anterior prefrontal cortex (APF; BA10, medial frontal gyrus and superior frontal gyrus)**: Encodes uncertainty about hidden current position (HCP entropy). Activity correlates with the entropy of the belief distribution over possible position estimates, representing the computational load of maintaining multiple position candidates under partial observability.
- **Medial prefrontal cortex (mPFC; BA9/6)**: Implements belief revision and error detection. Activity correlates with back-track probability, increasing during re-estimation trials when predicted scenes mismatch observed scenes. Involved in selecting actions based on both observable stimuli and internally evaluated cognitive states.
- **Dorsolateral prefrontal cortex (DLPF; BA46)**: Involved in higher-order judgment and prediction-based optimal action selection. Activated during goal-search vs. visuomotor control tasks.
- **Anterior cingulate cortex (ACC; BA32/8)**: Detects response conflict and behavioral errors. Constantly activated during goal-search tasks, potentially reflecting conflict induced by multiple action candidates and ambiguity about optimal actions due to uncertain position.
- **Posterior parietal cortex (PPC; BA40/7)**: Maintains egocentric spatial representations and 3D maze topography. Correlates with back-track probability, possibly representing memory reload to enumerate new position candidates during re-estimation.
- **Basal ganglia (putamen, caudate, globus pallidus, substantia nigra)**: Involved in motor-information processing and goal-directed action control via cortico-basal ganglia loops.
- **Thalamus**: Part of cortico-basal ganglia-thalamic circuits for action control.

### Mechanistic insight
This paper provides mechanistic insight at the algorithmic level but not at the implementational (biophysical) level. The paper meets the first criterion by formalizing the decision-making process as a Partially Observable Markov Decision Process (POMDP) solved via Bayesian belief updating. The HMM provides an explicit algorithm: subjects maintain a probability distribution over possible positions (belief state), update this distribution via incremental Bayes after each observation, and trigger back-track operations when predictions mismatch observations.

The paper partially meets the second criterion by using fMRI to identify which brain regions correlate with specific algorithmic variables: APF with belief entropy (uncertainty) and mPFC with back-track probability. However, the neural data are correlational (BOLD responses) rather than providing direct evidence for specific neural implementations (e.g., no single-unit recordings, lesion studies, or pharmacological manipulations). The results constrain the locus of uncertainty representation and belief revision but do not specify how these computations are implemented at the circuit or cellular level.

**Marr's levels analysis:**
- **Computational**: The brain must solve the POMDP problem of estimating hidden states (current position) from observations and selecting actions to reach goals. The optimal solution requires maintaining a belief distribution and updating it via Bayesian inference.
- **Algorithmic**: The HMM implements this via incremental Bayesian filtering: P(x_t|y_{1:t}) ∝ P(y_t|x_t) · P(x_t|y_{1:t-1}). Two cognitive states are tracked: estimate states (position candidates) and operant states (proceed/update vs. re-evaluate/back-track modes). HCP entropy quantifies uncertainty; BT probability signals belief revision.
- **Implementational**: The fMRI data localize these algorithmic components: APF (BA10) implements the maintenance of the belief distribution (as evidenced by entropy correlation), mPFC (BA9/6) implements the back-track/revision process, and DLPF/ACC/PPC support action selection and conflict monitoring. The specific neural circuitry (cell types, connectivity patterns, neuromodulators) is not specified.

### Limitations & open questions
- The HMM parameters (action selection optimality α = 0.8, back-track depth n = 1) were fit to behavior rather than derived from first principles; individual variation was limited but not fully explored.
- The fMRI analysis relies on correlational methods; the observed correlations between BOLD and model variables (entropy, back-track probability) do not establish causal necessity or sufficiency of these regions for the computational functions.
- No direct neural evidence (e.g., single-unit recordings, lesions, stimulation) links the algorithmic variables to specific neural implementations; the localization remains at the level of macroscopic regions.
- The maze task was highly structured (no dead-ends, symmetric topology); generalization to more complex, naturalistic environments with different uncertainty structures is not established.
- The binary operant state model (proceed/update vs. re-evaluate/back-track) may oversimplify the continuous nature of belief revision processes.
- The relationship between HCP entropy and the neural code for uncertainty remains unspecified—whether entropy is explicitly represented or emergent from population activity is not addressed.

### Connections & keywords
- **Key citations**: Koechlin et al. (2000, 2003) on APF and rule learning; Braver & Bongiolatti (2002) on frontopolar cortex and subgoal processing; Strange et al. (2001) on APF and rule learning; Daw et al. (2005) on uncertainty-based competition between prefrontal and striatal systems; Botvinick et al. (1999) on ACC and conflict monitoring; Gehring & Knight (2000) on mPFC and action monitoring; Northoff & Bermpohl (2004) on cortical midline structures and self-referential processing; Cassandra et al. (1994) on POMDPs; Kaelbling et al. (1998) on planning in partially observable domains; Ishii et al. (2002) on Bayesian control of exploration-exploitation
- **Named models or frameworks**: Hidden Markov Model (HMM), Partially Observable Markov Decision Process (POMDP), Bayesian belief updating/incremental Bayes, entropy as uncertainty measure
- **Brain regions**: Anterior prefrontal cortex (APF, BA10), medial prefrontal cortex (mPFC, BA9/6), dorsolateral prefrontal cortex (DLPF, BA46), anterior cingulate cortex (ACC, BA32/8), posterior parietal cortex (PPC, BA40/7), basal ganglia (caudate, putamen, globus pallidus, substantia nigra), thalamus
- **Keywords**: Bayesian inference, uncertainty, prefrontal cortex, POMDP, hidden Markov model, belief updating, entropy, navigation, decision making, fMRI, partial observability, back-track, belief maintenance, anterior prefrontal cortex, medial prefrontal cortex, state estimation
