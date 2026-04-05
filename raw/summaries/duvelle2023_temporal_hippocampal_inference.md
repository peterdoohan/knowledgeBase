---
source_file: duvelle2023_temporal_hippocampal_inference.md
title: "Temporal context and latent state inference in the hippocampal splitter signal"
authors: Éléonore Duvelle, Roddy M Grieves, Matthijs AA van der Meer
year: 2023
journal: eLife
paper_type: review
contribution_type: theoretical
---

### One-line summary

This review synthesises two decades of rodent hippocampal splitter-cell research and argues that neither temporal context models (TCM) nor latent state inference, alone, can account for all features of the data, and that their integration is likely necessary.

---

### Background & motivation

Hippocampal 'splitter cells' fire differentially on the overlapping segment of trajectories that differ in past and/or future, providing a window into internally generated representations during ongoing experience. Despite two decades of data, the field has been fragmented by inconsistent terminology, heterogeneous task designs, and variable analysis methods, making it difficult to draw theoretical conclusions. This review addresses that gap by establishing a common framework and translating across single-cell and ensemble perspectives, then applying two leading computational theories—temporal context models and latent state inference—to synthesise the experimental record and generate testable predictions.

---

### Methods

- **Scope**: comprehensive narrative review of rodent (and selected human/primate) literature on hippocampal splitter cells from approximately 2000 to 2022.
- **Terminology standardisation**: the authors unify multiple existing terms (trajectory coding, differential activity, context-dependent activity, journey-dependence) under the single label 'splitter cells' and define the 'splitter signal' at the ensemble level.
- **Single-cell and ensemble frameworks**: individual cell analyses are translated into population-level representational geometry (PCA-based ensemble similarity / neural trajectory distance) to enable cross-study and cross-modality comparison.
- **Theory evaluation**: two computational models (temporal context model / successor representation and latent state inference via HMMs, CRPs, deep networks) are formalised, their unique predictions extracted, and then each prediction is matched against the available experimental data (summarised in Table 1).
- **Proposed analyses**: representational similarity analysis (RSA) is outlined as a principled approach for distinguishing trajectory, goal, and state-based encoding, with a novel multi-branch maze design described to probe temporal horizon effects.

---

### Key findings

- **Temporal gradedness is well supported**: multiple studies find more retrospective splitters near the start of the overlapping segment and more prospective splitters near the choice point, consistent with a decaying temporal trace (TCM) and inconsistent with instantaneous discrete state switching.
- **Flexibility and task-dependence favour latent state models**: the presence/absence and strength of the splitter signal depends on training history, the order of task experience, whether barriers were used, and whether experience was blocked or interleaved—all predicted by state-inference accounts but not by TCM, which is agnostic to task relevance.
- **Retrospective splitting consistently exceeds prospective**: across all surveyed CA1 and CA3 studies, retrospective splitters outnumber prospective splitters by more than 2:1, and decoding accuracy for past paths exceeds that for future paths; this is partially explained by TCM (retrospective is 'free' via a memory buffer; prospective requires learned transitions).
- **Splitter signal and behaviour are correlated but dissociable**: on error trials the splitter signal is degraded or incorrect (supporting a functional role), but cue-guided decisions can override an intact splitter signal without changing it (situation 3 dissociation), suggesting hippocampal splitters may be necessary primarily to bridge memory-dependent delays.
- **Task-context determines splitter expression**: when animals are trained on a single irrelevant task, splitters are often absent; when animals have experience with multiple tasks (including memory-dependent ones), splitters persist even on cued tasks—consistent with latent state learning persisting across task switches.
- **Barriers and discrete trial structure promote splitting**: tasks that used barriers or blocked trial structures report systematically higher splitter percentages than those with continuously varied or interleaved experience, in agreement with state-inference models' sensitivity to experience clustering.
- **NRe inactivation selectively reduces prospective (not retrospective) splitting**, suggesting distinct anatomical substrates for the two types, consistent with TCM's proposal that they arise from different mechanisms.

---

### Computational framework

The paper evaluates two complementary frameworks:

**Temporal context model (TCM) / Successor representation (SR)**
- Core formalism: each moment of experience is represented as a blend of current input and an exponentially decaying trace of recent past events. Associations form between co-active trace and current state, yielding a temporally graded retrospective component. A forward-looking SR is derived by learning expected future state occupancy from past transitions (formally equivalent to TCM's prospective component).
- Key variables: decay time constant τ (determines temporal horizon), memory buffer contents, current location features.
- Key assumption: the memory buffer is always operative; retrospective splitting does not require learning and is available from the first trial. Prospective splitting (SR) does require learning of state transitions.
- Prediction signature: graded decrease in retrospective splitting along the central stem away from the branch point; displacement of the splitter signal to a delay period when a delay is inserted.

**Latent state inference**
- Core formalism: the agent infers discrete hidden states (e.g. 'left rewarded', 'right rewarded') from the non-stationary stream of sensory observations, actions, and outcomes. Models include Hidden Markov Models, Dirichlet process / Chinese Restaurant Process (CRP), and deep/recurrent networks (e.g. Tolman-Eichenbaum Machine). State learning is gradual and depends on experience order; state selection at run-time is fast.
- Key variables: posterior belief over latent states, learned transition matrix, state-observation emission probabilities.
- Key assumption: only states that have predictive value for outcomes are learned; the model is fundamentally atemporal at inference time (no explicit past/future representations).
- Prediction signature: constant splitter strength along the central stem (no gradient); dependence on training procedure and task relevance; generalisation across remapped tasks with the same structure.

---

### Prevailing model of the system under study

Prior to this review, the dominant theoretical framing of splitter cells treated them mainly as extended place cells whose selectivity reflects the animal's recent past trajectory or upcoming future trajectory, with the simplest explanation being a passive sensory trace of place-cell activity from adjacent arm locations. Concurrently, the hippocampal literature had separate active debates about: (1) whether splitters reflect memory demand (not clearly supported), (2) whether they are hardwired cell types or ensemble phenomena (the latter increasingly favoured), and (3) how they relate to broader theories of hippocampal function (context representation, episodic memory, cognitive map). Two theoretical frameworks—temporal context and latent state inference—had each been applied to other hippocampal phenomena (free recall, remapping, place-cell geometry) but had not been jointly applied to the well-constrained splitter literature. The field lacked a common vocabulary and systematic cross-study comparison, making it impossible to adjudicate between theories.

---

### What this paper contributes

The review establishes that splitter-cell data cannot be explained by either TCM or latent state inference in isolation: temporal gradedness (a TCM signature) is robustly replicated while the training-history and task-relevance effects (a state-inference signature) are also clearly present. This dual-theory evaluation is novel and enables the authors to propose a productive synthesis: TCM-style temporal traces provide the input features that make latent state learning tractable (augmenting the current state with recent history resolves aliasing), while latent state structure determines whether and how those traces are organised into useful representations. This synthesis aligns with and motivates the emerging class of 'hybrid' models (e.g. Madarász & Behrens 2019, Whittington et al. 2020). The paper also introduces an ensemble-RSA framework with specific matrix predictions that distinguishes trajectory, goal, and state coding—a tool applicable across recording modalities and species.

---

### Brain regions & systems

- **Dorsal CA1 (rodent hippocampus)** — primary focus; locus of most splitter-cell studies; proposed site where temporal context and latent state signals are integrated into ensemble activity that disambiguates overlapping trajectories.
- **Dorsal CA3** — also shows splitter activity; CA3 inactivation selectively disrupts retrospective (not prospective) splitting, implicating CA3 inputs in the retrospective component.
- **Dentate gyrus** — shows splitter-like activity; implicated in pattern separation that could contribute to state splitting.
- **Subiculum** — splitter activity reported; downstream of CA1, potential output structure.
- **Medial entorhinal cortex (mEC)** — splitter activity in small proportions; lesions do not disrupt CA1 splitting, but lateral entorhinal cortex (lEC; proposed source of decaying memory traces, Tsao et al. 2018) is noted as a critical uninvestigated node.
- **Medial prefrontal cortex (mPFC)** — trajectory-dependent activity; mPFC inactivation reduces CA1 splitting; mPFC–NRe–CA1 pathway is the best-characterised extrinsic circuit for the splitter signal.
- **Nucleus reuniens (NRe)** — thalamic relay between mPFC and hippocampus; NRe inactivation selectively reduces prospective splitting, suggesting a specific role in the prospective component.
- **Supramammillary nucleus** — inactivation reduces splitting in NRe and CA1 but not mPFC, indicating it gates the mPFC contribution to CA1.
- **Orbitofrontal cortex (OFC)**, **anterior cingulate cortex (ACC)**, **posterior parietal cortex**, **striatum**, **retrosplenial cortex** — all show trajectory-dependent activity; roles in contributing to or reading out the hippocampal splitter signal.

---

### Mechanistic insight

The paper does not present new neural recordings, so it does not itself meet the two-criterion bar (new algorithm + neural data supporting that algorithm over alternatives). However, it marshals existing neural data against two algorithmic proposals. The closest it comes to a mechanistic account:

- **Computational (Marr level 1)**: the hippocampus solves the problem of disambiguating overlapping sensory trajectories to support correct action selection, either by maintaining a temporal trace of recent experience (TCM) or by inferring the discrete latent task state (hidden state inference).
- **Algorithmic (Marr level 2)**: TCM proposes exponentially decaying activity traces as the representational substrate; latent state inference proposes posterior belief over discrete states updated by observations, actions, and outcomes. The review identifies distinct behavioural/neural signatures—graded vs. uniform splitter distributions along the stem—that map onto these two algorithms.
- **Implementational (Marr level 3)**: only partially addressed. The mPFC–NRe–CA1 circuit is identified as the best-characterised anatomical substrate, with NRe specifically implicated in the prospective component. Lateral entorhinal cortex is hypothesised (but not tested) as the source of decaying temporal traces. No specific cell types or biophysical mechanisms are identified.

The paper does not provide new implementational evidence and explicitly calls for future work to test these mechanistic hypotheses.

---

### Limitations & open questions

- **Publication bias**: negative results (no splitters found) are likely under-reported, making it hard to assess the true prevalence and boundary conditions of the phenomenon.
- **Confounded study comparisons**: differences in recording location, analysis method, behavioural confound control, and significance threshold make cross-study quantitative comparisons unreliable; within-animal across-task comparisons are the gold standard but rare.
- **Cannot fully dissociate trajectory, goal, policy, and task-state coding**: existing maze designs conflate these in most cases; a purpose-built multi-branch maze with RSA analysis is proposed but not yet implemented.
- **Temporal horizon and multiple timescales**: tasks with a single branch point cannot reveal the full temporal horizon of splitter coding or whether the dorsal-ventral hippocampal gradient encodes multiple timescales simultaneously.
- **Speed of emergence of prospective vs. retrospective splitting**: systematic within-animal longitudinal comparisons across learning have rarely been conducted; the TCM prediction (retrospective emerges before prospective) has not been cleanly tested.
- **Generalisability of state representations**: evidence that splitter activity transfers across remapped environments with the same structure is mixed (supported by Takahashi 2013, Sun et al. 2020; contradicted by Bahar & Shapiro 2012, Hallock & Griffin 2013).
- **Individual differences**: the degrees of freedom in state-space learning mean that different animals may adopt different state representations for the same task, complicating group-level analyses.
- **Locus of prospective vs. retrospective dissociation in circuits**: selective effects of NRe lesions on prospective splitting are intriguing, but corresponding tests for CA3 effects on prospective splitting, and for other nodes (lEC, ventral hippocampus), have not been done.

---

### Connections & keywords

**Key citations**:
- Wood et al. 2000 (original splitter cell report, T-maze)
- Frank et al. 2000 (original splitter cell report, W-maze)
- Ferbinteanu & Shapiro 2003 (plus maze, retrospective/prospective distinction)
- Howard & Kahana 2002; Howard et al. 2005 (temporal context model)
- Gershman 2018; Dayan 1993 (successor representation)
- Gershman & Niv 2010; Niv 2019 (latent state inference)
- Whittington et al. 2020 (Tolman-Eichenbaum Machine)
- Stachenfeld et al. 2017 (hippocampus as predictive map)
- Madarász & Behrens 2019 (hybrid state / SR model)
- George et al. 2021 (aliased HMM model of splitter cells)
- Tsao et al. 2018 (lateral entorhinal decaying memory traces)
- Ito et al. 2015 (NRe–CA1 circuit, prospective vs. retrospective)
- Ainge et al. 2007a (delayed alternation, hippocampus-dependent splitting)
- Pastalkova et al. 2008 (time cells, delay-period splitting)
- Kinsky et al. 2020; Levy et al. 2021 (calcium imaging, splitter development)

**Named models or frameworks**:
- Temporal context model (TCM)
- Successor representation (SR)
- Latent state inference / hidden state inference
- Chinese Restaurant Process (CRP) / Dirichlet process
- Hidden Markov Model (HMM)
- Tolman-Eichenbaum Machine (TEM; Whittington et al. 2020)
- Representational similarity analysis (RSA)
- Marr's three levels of analysis

**Brain regions**:
- Hippocampus (dorsal CA1, dorsal CA3, dentate gyrus, subiculum)
- Medial entorhinal cortex (mEC), lateral entorhinal cortex (lEC)
- Medial prefrontal cortex (mPFC), anterior cingulate cortex (ACC), orbitofrontal cortex (OFC)
- Nucleus reuniens (NRe)
- Supramammillary nucleus
- Posterior parietal cortex, striatum, retrosplenial cortex

**Keywords**:
- splitter cells
- hippocampal trajectory coding
- temporal context model
- successor representation
- latent state inference
- place cell ensemble geometry
- retrospective vs. prospective coding
- hippocampal remapping
- neural representational similarity analysis
- mPFC–NRe–hippocampus circuit
- time cells
- episodic memory encoding
