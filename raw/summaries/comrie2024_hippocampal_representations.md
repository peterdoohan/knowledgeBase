---
source_file: comrie2024_hippocampal_representations.md
title: "Hippocampal representations of alternative possibilities are flexibly generated to meet cognitive demands"
authors: Alison E. Comrie, Emily J. Monroe, Ari E. Kahn, Eric L. Denovellis, Abhilasha Joshi, Jennifer A. Guidera, Timothy A. Krausz, Joshua D. Berke, Nathaniel D. Daw, Loren M. Frank
year: 2024
journal: bioRxiv (preprint, posted September 23, 2024)
paper_type: empirical
contribution_type: empirical
---

### One-line summary

During active navigation, the hippocampus flexibly modulates both the content and spatial extent of non-local representations of alternatives in two dissociable patterns — one tracking the relative expected value of options across successive trials, and the other tracking the degree of uncertainty-driven value updating after an environmental change.

---

### Background & motivation

Animals must go beyond their current experience to decide among alternatives and update internal models of the world; this requires representing "non-local" spatial possibilities that are distant in space or time from the animal's immediate position. The hippocampus is known to produce non-local place-cell sequences during active movement, linked to both decision making and learning, but whether and how the brain selectively generates representations of the most relevant alternatives as cognitive demands shift across experience remained unknown. Prior work had focused largely on representations of immediately upcoming choices on single trials, leaving open how the brain prioritises among many available alternatives over successive trials in complex, dynamic environments. This paper addresses that gap by combining a rich foraging task with within-trial decoding and computational modelling.

---

### Methods

- **Subjects**: 5 adult male Long-Evans rats implanted with tetrode microdrives targeting dorsal hippocampus CA1; also implanted with probes in mPFC and OFC (not the focus of main analyses).
- **Task ("Spatial Bandit")**: A maze with three radially arranged Y-shaped foraging patches, each containing two reward ports. Reward probabilities (0.2, 0.5, or 0.8) were assigned to ports and changed covertly every 60–80 trials, encouraging continual experience-based updating. Animals completed 5,220–10,191 trials across 8–17 recording days.
- **Behavioural analysis**: Trials classified as Stay (remaining in current patch) or Switch (moving to a different patch). Logistic regressions and a Hidden Markov Model (HMM) were fit to estimate trial-by-trial expected values of Stay and Switch options and the relative value between them.
- **Computational model**: A "global" HMM that jointly inferred reward probability states across all six ports (allowing non-local value inference), compared against a "local" HMM that estimated each port independently. Model fit evaluated by leave-one-out cross-validated log-likelihood.
- **Neural decoding**: Clusterless state-space decoding algorithm applied to CA1 multi-unit spiking at 2 cm spatial and 2 ms temporal resolution during running (>10 cm/s). Non-local representations identified as periods in which the decoded position was in a track segment distinct from the animal's actual segment.
- **Key neural analyses**: (1) Proportion of non-local time representing Switch vs. Stay paths ahead of and behind the animal, tracked across successive trials relative to patch Switch events. (2) Maximum distance between decoded and actual position, also tracked across successive trials. Both measures correlated with HMM-derived cognitive variables.

---

### Key findings

- Rats' patch Switch choices depended on both Stay-option value and Switch-option value (logistic regression coefficients significant in all 5 animals, p < 5e-17 and p < 1e-8, respectively), and relative value (Switch minus Stay) ramped upward over successive Stay trials before a Switch.
- Non-local representations of Switch-consistent paths **ahead** of the animal increased progressively over ~20 Stay trials before a Switch and decreased symmetrically afterwards, approximately tracking the evolving relative value (1.3–1.5-fold increase in Switch path representation in the 20 trials before a switch).
- On Switch trials, 70–80% of forward non-local representations corresponded to the Switch path; on Stay trials, ~20–30% did (Wilcoxon p < 1e-100 for all animals).
- Non-local representations of paths **behind** the animal (counterfactual alternatives) showed an identical symmetric modulation pattern around Switches, even though occurring after the behavioural choice on each trial was already made.
- Both ahead and behind representations predicted the subsequent trial's Stay/Switch choice better than chance when measured on the prior trial (all animals, p < 1e-32); prediction was even better when combining both prior-trial and current-trial neural data.
- Maximum non-local **distance** (spatial extent of representations) showed a distinct, asymmetric modulation: relatively stable before a Switch, then sharply elevated on and after the Switch trial (~40 cm increase from baseline across animals), decaying rapidly over subsequent Stay trials.
- The global HMM that allowed non-local inference across all ports provided a significantly better fit to behaviour than the local (independent-port) model in all 5 animals (p < 0.03).
- HMM-estimated outcome entropy and global value update magnitude both mirrored the asymmetric pattern of hippocampal non-local distance, being elevated on and after Switches.
- Alternative patch representations on 10–20% of trials; these remote representations did not predict the specific prior or upcoming patch choice.

---

### Computational framework

The paper employs **reinforcement learning / Bayesian statistical learning** as its computational lens, primarily via a Hidden Markov Model of value inference.

- **What is being modelled**: The animal's trial-by-trial belief about the joint reward probability state across all six ports, updated by reward outcomes.
- **Key variables**: Hidden states = reward contingency assignments across ports; belief state = posterior probability distribution over states; per-port expected value Q derived from belief; relative value = Q(Switch) − Q(Stay); outcome entropy = uncertainty over the upcoming port's value state; global value update = total absolute change in Q across all ports after each trial outcome.
- **Key assumption**: Reward contingencies are correlated across patches (zero-sum-like structure), so an outcome at one port provides Bayesian evidence about values at distant ports — enabling "non-local inference."
- The HMM framework is used descriptively (as a normative ideal-observer baseline) rather than as a mechanistic model of neural implementation; the authors acknowledge that a Q-learning model augmented with non-local activations would approximate the same computations.

---

### Prevailing model of the system under study

The paper's introduction frames hippocampal CA1 as the substrate for a cognitive map — an internal model encoding spatial relationships and associated experience — where place cells signal the animal's current location during normal navigation but are also capable of expressing non-local representations (theta sequences, forward sweeps) at sub-second timescales. The prevailing understanding, as framed by the authors, is that these non-local representations during locomotion are most studied in the context of the immediately upcoming choice on a single trial (prospective sequences at choice points), with comparatively less attention to how representations are modulated across successive trials, to counterfactual paths behind the animal, or to very distant alternatives. The field had also largely attributed non-local updating to offline replay during rest/sleep rather than online movement-associated activity. The paper explicitly pushes against the view that hippocampal non-local representations are either constant predictors of the planned choice or unbiased menus of all options.

---

### What this paper contributes

The results establish that the hippocampus modulates non-local representations in two mechanistically distinct across-trial patterns:

1. **Content modulation** (symmetric around patch Switches): The fraction of non-local activity devoted to the higher-value alternative increases progressively as the relative value of that alternative rises, providing a value-proportionate internal sampling of options both ahead of and behind the animal. This extends across multiple trials (not just the current trial), predicts choices a full trial in advance, and occurs even during path segments with no upcoming choice point.

2. **Extent modulation** (asymmetric around patch Switches): The spatial reach of non-local representations is specifically elevated when outcome uncertainty is high and non-local value updating is greatest (immediately after entering a new patch), consistent with the hippocampus facilitating inference about distant reward states at moments when updating is most needed.

Together, these findings show that hippocampal non-local representations are neither constantly predictive of upcoming choices nor uniformly distributed — they are flexibly and specifically curated across trials in patterns matching distinct cognitive demands (deliberation vs. updating). The paper also establishes that counterfactual (behind-the-animal) representations are dynamically modulated with the same value-related signal as prospective representations, and that animals' behaviour is better captured by a non-local (global) learning model than a local one, implicating hippocampal non-local activity in propagating value information across the environment.

---

### Brain regions & systems

- **Dorsal hippocampus CA1** — primary recording site; locus of non-local place-cell representations whose content and spatial extent are modulated by cognitive demands for decision making and value updating.
- **Medial prefrontal cortex (mPFC)** — discussed in the context of circuit mechanisms; cited as a candidate driver of non-local hippocampal representations given known mPFC-hippocampus coordination and evidence that mPFC spiking predicts subsequent hippocampal non-local activity. Also recorded (probes) but not a focus of reported analyses.
- **Orbitofrontal cortex (OFC)** — implanted (probes) but not analysed in this report.

---

### Mechanistic insight

The paper meets criterion 1 (proposes an algorithm — value-proportionate sampling of alternatives implemented via non-local hippocampal representations, modulated across trials) and partially meets criterion 2 (provides neural recordings that specifically link the pattern of non-local CA1 activity to model-derived cognitive variables).

**Computational level**: The brain must decide among alternatives with changing reward probabilities and update its internal model of remote reward locations. It needs to prioritise which alternatives to internally sample — favouring the most valuable options when the choice is clear, and sampling more evenly when values converge; and to represent distant alternatives specifically when new information must be propagated across space.

**Algorithmic level**: The hippocampus implements value-proportionate sampling by generating non-local representations of alternative paths in proportion to their relative expected value, across successive trials. A separate, dissociable process generates representations extending to distant locations specifically when outcome uncertainty and global value updates are high (after environmental changes). Representations extend both ahead of and behind the animal, and appear to constitute an across-trial accumulation process rather than a purely in-the-moment read-out.

**Implementational level**: Partially addressed. Non-local representations are locked to specific phases of the CA1 theta rhythm (forward representations in late theta phases; backward/counterfactual representations in early theta phases), consistent with known theta-sequence mechanisms. The paper discusses theta-cycle plasticity as a potential learning substrate and notes that non-local activity during locomotion (theta sequences) is distinct from offline sharp-wave ripple replay. However, the paper does not identify specific cell types, synaptic mechanisms, or neuromodulatory systems driving the value-dependent or uncertainty-dependent modulation. mPFC is proposed as a likely circuit-level driver but not empirically tested here.

---

### Limitations & open questions

- The paper does not identify the circuit mechanism by which relative value or uncertainty modulates hippocampal non-local content or extent; mPFC is proposed but not tested.
- The HMM is a normative ideal-observer model, not a mechanistic implementation; the degree to which animals actually perform non-local Bayesian inference versus a simpler heuristic is not fully resolved.
- Remote patch representations (10–20% of non-local trials) were not predictive of specific prior or upcoming patch choices; their functional role remains unclear.
- Whether the content and extent modulations reflect distinct circuit processes or a single mechanism operating at different scales is unresolved.
- The study is limited to dorsal CA1 in rats; generalisability to other hippocampal subfields, other species, or non-spatial domains is open.
- The paper acknowledges that a single trial in advance prediction is significant but could reflect downstream read-out of accumulated value rather than causal influence of hippocampal representations on choices.
- The potential role of mPFC, OFC, and other recorded regions in governing these dynamics was not reported.

---

### Connections & keywords

**Key citations**:
- Foster & Wilson (2006) — reverse replay during awake state
- Miller, Botvinick & Brody (2017) — dorsal hippocampus in model-based planning
- Liu et al. (2021) — experience replay and non-local learning
- Krausz et al. (2023, preprint) — dual credit assignment in spatial environment (companion paper from same lab)
- Hunt et al. (2021) — formalizing planning and information search in naturalistic decision making
- Daw, Niv & Dayan (2005) — competition between model-based and model-free systems
- Denovellis et al. (2021) — clusterless state-space decoding algorithm used here

**Named models or frameworks**:
- Spatial Bandit task (novel task paradigm introduced here)
- Hidden Markov Model (global vs. local variants) for value inference
- Clusterless state-space decoding (Denovellis et al., 2021)
- Theta sequence model of non-local hippocampal representations

**Brain regions**:
- Dorsal hippocampus CA1
- Medial prefrontal cortex (mPFC)
- Orbitofrontal cortex (OFC)

**Keywords**:
- hippocampal non-local representations
- theta sequences
- counterfactual representations
- patch foraging task
- value-guided decision making
- non-local value updating
- Bayesian hidden Markov model
- place cells
- spatial bandit task
- cognitive map
- model-based reinforcement learning
- online replay during locomotion
