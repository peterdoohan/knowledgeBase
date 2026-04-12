---
source_file: "momennejad2017_successor_representation_humans.md"
paper_id: "momennejad2017_successor_representation_humans"
title: "The successor representation in human reinforcement learning"
authors: "I. Momennejad, E. M. Russek, J. H. Cheong, M. M. Botvinick, N. D. Daw, S. J. Gershman"
year: 2017
journal: "Nature Human Behaviour"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
tasks: ["two_step_task"]
methods: ["fmri", "computational_modeling", "behavioral_analysis"]
brain_regions: ["hippocampus", "prefrontal_cortex", "orbitofrontal_cortex", "ventromedial_prefrontal_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl", "model_free_rl", "successor_representation", "temporal_difference_learning"]
keywords: ["dayan_1993_original_proposal_of_the_successor_representation_neural_computation", "gershman_et_al_2012_sr_and_temporal_context_model", "daw_et_al_2011_model_based_influences_on_striatal_prediction_errors_two_step_task", "stachenfeld", "botvinick_and_gershman_2017", "preprint_hippocampus_as_predictive_map_place_cells_and_sr", "sutton_1991_dyna_architecture_model_based_experience_replay_for_sr_updating", "schapiro_et_al_2013_fmri_evidence_for_sr_like_representations_in_hippocampus_and_pfc", "garvert", "dolan_and_behrens_2017_abstract_relational_maps_in_hippocampalentorhinal_cortex", "tolman_1948_cognitive_maps_in_rats_and_men", "named_models_or_frameworks", "successor_representation_sr", "model_free_mf_temporal_difference_learning", "model_based_mb_reinforcement_learning", "hybrid_srmb_model", "srdyna_offline_replay_updating_the_sr", "mfmb_hybrid_daw_et_al_standard_two_system_account", "brain_regions", "hippocampus"]
---

### One-line summary

Human behaviour in sequential decision tasks is best explained by a hybrid successor representation strategy that caches multi-step future state predictions, producing asymmetric sensitivity to reward revaluation versus transition revaluation.

---

### Background & motivation

Theories of reinforcement learning have focused on a dichotomy between model-free (MF) algorithms that cache action values and model-based (MB) algorithms that plan flexibly using a one-step internal model. However, there exist intermediate strategies that have been underexplored empirically. The successor representation (SR) — which caches long-run predictions about future state occupancies rather than fully computed values or one-step transitions — was previously proposed as a biologically plausible algorithm but had not been directly tested against competing accounts in humans. The central challenge was that SR and MB algorithms make identical predictions for the standard reward revaluation tasks used to support MB learning, so new experimental designs were needed to dissociate them.

---

### Methods

- **Experiment 1 (passive learning; n = 58):** Participants passively traversed three-step sequential trajectories. Task had three phases: learning, re-learning (revaluation), and test. Revaluation conditions (within-participant): reward revaluation (terminal reward swapped), transition revaluation (state-to-state connections swapped), and no-change control. Key measure: change in continuous preference rating for starting states between phases 1 and 3 (revaluation score). Response times also recorded.
- **Experiment 2 (active decision-making; n = 88, Amazon Mechanical Turk):** Participants navigated a three-stage decision tree (rooms in a castle). Revaluation conditions (within-participant, counterbalanced): reward revaluation, transition revaluation, policy revaluation (reward change that alters the optimal policy at an intermediate state), and control. Key measure: binary switch in starting-state action choice at test.
- **Computational modelling:** Three models compared against behaviour: pure MB, pure SR, and a hybrid SR–MB (linear combination). Models assumed asymptotic learning within each phase and were fit using leave-one-out cross-validation. Likelihood-based model comparison.
- Statistical analysis: repeated-measures ANOVA, planned pairwise t-tests (Bonferroni corrected), logistic regression with cluster-robust standard errors for experiment 2.

---

### Key findings

- **Experiment 1:** Mean revaluation scores: reward revaluation = 0.52, transition revaluation = 0.45, control = 0.031. Reward revaluation produced significantly higher revaluation scores than transition revaluation (t₅₇ = 2.89, P = 0.016), and both revaluation conditions exceeded control (P < 0.001).
- **Response times (Experiment 1):** Transition revaluation produced significantly slower responses than reward revaluation (t₅₇ = 2.08, P < 0.05) and control. Accuracy of transition revaluation correlated with response time (rho = 0.31, P = 0.01), suggesting effortful computation.
- **Experiment 2:** Proportion switching: reward = 0.66, transition = 0.47, policy = 0.50, control = 0.08. Reward revaluation produced significantly more switching than both transition (P = 0.0034) and policy revaluation (P = 0.0043). Transition and policy revaluation did not differ (P = 0.577), despite involving different surface features.
- **Model comparison:** Only the hybrid SR–MB model adequately captured the asymmetric pattern across all revaluation conditions in both experiments. Pure SR predicts zero sensitivity to transition/policy revaluation; pure MB predicts equal sensitivity to all; neither fit the data.
- The policy revaluation result rules out the hypothesis that the reward–transition asymmetry reflects differential learning rates for R versus T, and is inconsistent with MB–MF arbitration accounts based on prediction error type.

---

### Computational framework

The paper uses **reinforcement learning** and the **successor representation (SR)** framework.

The SR is a matrix M where element M(i,j) stores the expected discounted future occupancy of state j when starting from state i — that is, how many discounted future visits to state j are expected on trajectories beginning in state i. Formally:

M(s₀, j) = E[Σₜ γᵗ · I(sₜ = j)]

Value is computed as the inner product of M with the reward vector R: V(s) = M(s, ·) · R. This separates the cached predictive map (M) from the immediate reward function (R), allowing instant adaptation to reward changes (update R only) but not to structural/transition changes (which would require re-learning M from experience).

Key variables: M (successor matrix, policy-dependent), R (reward vector), T (one-step transition matrix, used only in MB), γ (discount/planning-horizon parameter). The hybrid model combines SR and MB value estimates via a weighting parameter w. Models assumed asymptotic representations by end of each phase; learning rates were not estimated due to task structure constraints.

---

### Prevailing model of the system under study

Prior to this paper, the dominant framework for understanding flexible versus habitual choice was the MF–MB dichotomy. MF learning (temporal difference) caches long-run action values, producing computationally cheap but inflexible behaviour. MB learning stores one-step transition and reward functions and recomputes values online via iterative simulation, producing flexible but computationally expensive behaviour. Hybrid MF–MB models blending these two were used to explain individual differences in goal-directed versus habitual behaviour. The standard empirical tool for distinguishing these strategies was reward revaluation, but the paper's introduction notes that SR and MB algorithms make identical predictions in those tasks — meaning much prior evidence for MB learning was equally consistent with an SR account. The field had not yet developed tasks capable of empirically distinguishing SR from MB strategies.

---

### What this paper contributes

By introducing transition revaluation and policy revaluation conditions, this paper provides the first direct empirical evidence that humans employ SR-like representations. The key new finding is a systematic asymmetry: humans are more sensitive to reward revaluation than to transition or policy revaluation, a pattern uniquely predicted by SR-based (but not MB or MF) algorithms. This rules out both pure MB (which predicts equal sensitivity to all revaluation types) and pure MF accounts. The paper also shows that a hybrid SR–MB model (but not pure SR) fits the data, suggesting the SR is used in combination with residual MB computation. Furthermore, the policy revaluation result eliminates differential learning rates for R versus T as an explanation, and is inconsistent with arbitration accounts based on prediction error type. Together, the results reframe what has been called "model-based" flexible behaviour in humans: much of it may reflect fast retrieval from cached multi-step predictions rather than costly online planning.

---

### Brain regions & systems

The paper is primarily behavioural and computational; no neuroimaging or electrophysiology data are reported. However, the discussion proposes candidate neural substrates based on prior work:

- **Hippocampus** — proposed locus of SR storage and updating; implicated in place cell predictive representations, sequential and statistical learning, and offline replay processes that could update the SR's predictive map.
- **Ventromedial prefrontal cortex (vmPFC)** — proposed contributor to SR representations; implicated in abstract state-based inference, value integration, and goal-state proximity coding; well-connected to hippocampus.
- **Orbitofrontal cortex (OFC)** — proposed contributor to cognitive map-like representations of task and state spaces; may form and update the SR in conjunction with hippocampus.

These are discussed as targets for future neuroimaging studies, not as empirically supported claims in this paper.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined here. It presents a formal SR algorithm and fits it to human behaviour, providing strong evidence that humans use SR-like cached representations. However, the paper contains no neural data (no recordings, imaging, lesion, or pharmacology). The neural substrates (hippocampus, vmPFC, OFC) are discussed speculatively in the discussion as predictions for future work. The algorithmic-level evidence is strong, but the implementational level is entirely unaddressed empirically.

---

### Limitations & open questions

- The paper does not address trial-by-trial learning dynamics; models assume asymptotic representations within each phase, leaving learning rates unconstrained.
- The hybrid SR–MB combination is treated as a linear mixture for simplicity; the true nature of multi-system interaction (e.g., Dyna-like offline replay updating the SR, or MB augmentation at decision time) is not adjudicated.
- No neural data are provided; proposed roles for hippocampus, vmPFC, and OFC remain speculative.
- The discount parameter γ (controlling planning horizon) was fixed at 1 in experiment 1 (deterministic task); its role in naturalistic settings with variable timescales is unexplored.
- Substantial individual differences were observed; future work should characterise what drives variability in SR versus MB reliance, including relevance to psychiatric populations.
- The policy revaluation condition controls for some alternative explanations but the paper acknowledges its findings are not exhaustive — other shortcuts between MF and MB may exist.
- How the SR planning horizon is rationally adapted to environmental volatility is raised as an open question.

---

### Connections & keywords

**Key citations:**
- Dayan (1993) — original proposal of the successor representation (Neural Computation)
- Gershman et al. (2012) — SR and temporal context model
- Daw et al. (2011) — model-based influences on striatal prediction errors (two-step task)
- Stachenfeld, Botvinick & Gershman (2017, preprint) — hippocampus as predictive map (place cells and SR)
- Sutton (1991) — Dyna architecture (model-based experience replay for SR updating)
- Schapiro et al. (2013) — fMRI evidence for SR-like representations in hippocampus and PFC
- Garvert, Dolan & Behrens (2017) — abstract relational maps in hippocampal–entorhinal cortex
- Tolman (1948) — cognitive maps in rats and men

**Named models or frameworks:**
- Successor Representation (SR)
- Model-free (MF) temporal difference learning
- Model-based (MB) reinforcement learning
- Hybrid SR–MB model
- SR–Dyna (offline replay updating the SR)
- MF–MB hybrid (Daw et al. standard two-system account)

**Brain regions:**
- Hippocampus
- Ventromedial prefrontal cortex (vmPFC)
- Orbitofrontal cortex (OFC)

**Keywords:**
- successor representation
- reinforcement learning
- reward revaluation
- transition revaluation
- model-based learning
- model-free learning
- habitual behaviour
- semi-flexible choice
- cognitive map
- revaluation asymmetry
- policy revaluation
- offline replay
