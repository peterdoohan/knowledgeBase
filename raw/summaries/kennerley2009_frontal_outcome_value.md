---
source_file: kennerley2009_frontal_outcome_value.md
title: "Evaluating choices by single neurons in the frontal lobe: outcome value encoded across multiple decision variables"
authors: Steven W. Kennerley, Jonathan D. Wallis
year: 2009
journal: European Journal of Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Single neurons in the frontal cortex — especially anterior cingulate cortex (ACC) — encode the value of choice outcomes across multiple decision variables (probability, payoff, and effort cost), often bridging the choice and outcome phases of a task within the same neuron.

---

### Background & motivation

Adaptive decision-making requires not only evaluating options before a choice (choice evaluation) but also evaluating the experienced outcome afterwards (outcome evaluation), so that future choices can be updated appropriately. Prior work had shown that frontal neurons encode decision variables during choice, but whether and how this extends to the outcome phase — and whether the same neurons participate in both — was unclear. This paper directly addresses that gap by recording from ACC, OFC, and LPFC across both the choice and outcome phases of the same task, using outcomes that vary along three physically distinct dimensions.

---

### Methods

- **Subjects**: Two adult rhesus macaques.
- **Task**: A visual choice task in which two pictures appeared on each trial, each associated with a specific outcome along one of three decision dimensions: (1) probability of juice reward (0.1–0.9), (2) payoff amount (five graded juice volumes), or (3) effort cost (number of lever presses required for fixed reward). Adjacent values were always paired to equate decision difficulty.
- **Neural recording**: Simultaneous multi-electrode recording of 610 single neurons across ACC (n = 213), LPFC (n = 257, areas 9, 46, 45, 47/12l), and OFC (n = 140, areas 11, 13, 47/12o).
- **Analysis**: ANOVA on firing rate within defined outcome epochs (reward epoch, post-reward epoch, movement epoch). Linear regression to characterise value tuning direction. Sliding ROC analysis to compute latency of reward-presence encoding on probability trials. Cross-epoch and cross-variable analyses to assess neurons encoding both choice and outcome phases, and multiple decision variables simultaneously.

---

### Key findings

- **Reward presence/absence (probability trials)**: 40% of all neurons encoded whether reward was delivered during the reward epoch; 39% during the post-reward epoch. ACC showed the highest prevalence (58%) relative to LPFC (32%) and OFC (27%), and ACC encoded this information earliest (median latency 230 ms vs. OFC 320 ms and LPFC 430 ms).
- **Reward magnitude (payoff trials)**: 33% of neurons encoded payoff value during the reward epoch, most prevalently in ACC (46% vs. OFC 30%, LPFC 25%). Value tuning was approximately linear for ~70% of selective neurons; tuning direction (positive vs. negative) was evenly split.
- **Effort cost trials**: 23% of neurons encoded cost value during the movement epoch, again most prevalent in ACC (33% vs. OFC 21%, LPFC 16%). Approximately linear tuning in ~70% of cases.
- **Cross-epoch continuity**: Of 610 neurons, 320 encoded at least one decision variable in both the choice and outcome phases; 76% of these encoded the same variable across both phases. Such neurons were most common in ACC and OFC.
- **Cross-variable multiplexing**: Many neurons encoded outcomes across two or more decision variables simultaneously. Multi-variable neurons were significantly more prevalent in ACC than OFC or LPFC.
- **Integration of cost and payoff**: Unlike the choice phase, outcome-phase neurons did not show consistent integrated cost–payoff encoding (61% same-slope, not above chance), suggesting outcome evaluation is less integrated than choice evaluation.
- **Comparison with prediction error signals**: Frontal neurons did not show the hallmarks of dopamine-like prediction errors (no strong modulation by trial probability value per se; bidirectional value tuning). This dissociates frontal outcome encoding from prediction error signalling.

---

### Computational framework

The paper does not introduce a formal computational model, but situates its findings within Rangel et al.'s (2008) four-process framework for value-based decision-making: (1) state representation, (2) value computation, (3) action selection, and (4) outcome evaluation generating prediction errors. The results place frontal cortex — particularly ACC — at step 2 and 4: computing the values of decision variables both prospectively (during choice) and retrospectively (during outcome evaluation), while leaving prediction-error computation to dopamine/striatal circuits.

Key variables implicitly tracked: outcome value (magnitude, probability, effort), represented as firing rate modulations that are approximately linear in value, bidirectional in sign, and stable across choice and outcome epochs for individual neurons.

---

### Prevailing model of the system under study

Prior to this paper, the dominant accounts of frontal-lobe outcome-related activity centred on two signals: (1) prediction error signals (primarily attributed to dopamine neurons, with frontal cortex sometimes implicated as a recipient), and (2) error-monitoring or expectancy-violation signals thought to arise in ACC and indexed by electrophysiological error-related negativity. OFC was seen as primarily encoding stimulus–reward associations and reward magnitude, while ACC was associated with action–outcome links and performance monitoring. The field's understanding of how individual neurons bridge choice evaluation and outcome evaluation, and whether single neurons encode abstract value across physically disparate outcome dimensions, was limited.

---

### What this paper contributes

This study establishes that a substantial fraction of frontal neurons — particularly in ACC — encode outcome value in a way that is (a) multivariate (spanning reward presence, magnitude, and effort cost), (b) approximately linear and parametric rather than binary, (c) continuous across choice and outcome phases in the same neuron, and (d) distinct from dopaminergic prediction errors. The results upgrade the role of ACC from "error monitor" to a region that provides a rich, ongoing representation of outcome value across decision dimensions, necessary for evaluating whether the experienced outcome warrants behavioural adjustment. They also refine OFC's role, showing it too bridges choice and outcome phases, but less extensively than ACC.

---

### Brain regions & systems

- **Anterior cingulate cortex (ACC)** — primary locus of outcome-value encoding; shows highest prevalence of selective neurons, earliest reward-onset latency, greatest cross-epoch continuity, and most multi-variable multiplexing. Proposed to integrate outcome information across decision variables for adaptive choice adjustment.
- **Orbitofrontal cortex (OFC)** — encodes outcome value (especially payoff magnitude in the post-reward epoch) and bridges choice and outcome phases, but less extensively than ACC. Stronger connections with gustatory/olfactory systems position it for reward-identity encoding.
- **Lateral prefrontal cortex (LPFC)** — encodes outcome variables but at lower prevalence and with longer latencies than ACC. More response-direction selectivity than the other areas, consistent with its stronger motor connections. Less cross-epoch and cross-variable multiplexing.

---

### Mechanistic insight

The paper partially meets the bar. It presents an algorithmic account: frontal neurons (especially ACC) implement outcome evaluation by maintaining parametric, approximately linear value representations that are stable across both the choice and outcome phases of a trial and that generalise across physically different outcome dimensions. Neural data (single-unit recordings from three frontal areas) directly support this over a purely prediction-error or error-monitoring account by showing (i) bidirectional value tuning (incompatible with a unidirectional PE signal), (ii) prevalence of outcome encoding in ACC even for fully predictable (payoff, cost) trials, and (iii) within-neuron cross-epoch coding.

However, the paper does not address the implementational level (specific cell types, laminar organisation, connectivity, or neuromodulatory mechanisms underlying these response properties), so the Marr mapping is incomplete at the implementational level.

- **Computational**: The brain must evaluate the value of the experienced outcome across multiple dimensions (magnitude, probability, effort cost) to determine whether future choices should be updated.
- **Algorithmic**: Individual frontal neurons, concentrated in ACC, represent outcome value as graded, approximately linear firing-rate modulations that are stable across choice and outcome epochs and abstract over specific outcome modalities.
- **Implementational**: Not addressed. Cell-type identity, layer specificity, and synaptic mechanisms are not examined.

---

### Limitations & open questions

- Only two subjects (rhesus macaques); both performing near ceiling, so the full range of outcome-value representations during suboptimal choice is uncharacterised.
- The task design required subjects to always choose the more valuable picture; this limits conclusions about how neurons respond during genuine uncertainty or choice reversal.
- During the choice phase, neurons encoding value cannot be distinguished from neurons encoding the relative value of the two available options (pair value vs. single stimulus value).
- On probability trials, outcome-phase neurons primarily encoded reward presence/absence rather than the trial's probability value; whether this reflects a design limitation (low trial counts for each probability level per session) or a genuine dissociation is unclear.
- The lack of clear integrated cost–payoff encoding at the outcome phase (unlike at choice) is left unexplained and warrants further study.
- The paper acknowledges that outcome activity after reward offset could reflect either outcome magnitude or the forgone alternative — these are confounded.
- No causal manipulation: recording alone cannot establish whether ACC outcome-value signals are necessary for adaptive behaviour.

---

### Connections & keywords

**Key citations**:
- Kennerley et al. (2009, J. Cogn. Neurosci.) — companion paper characterising the same neurons during the choice phase
- Rangel, Camerer & Montague (2008, Nat. Rev. Neurosci.) — decision-making framework used to contextualise findings
- Kennerley et al. (2006, Nat. Neurosci.) — ACC lesion paper showing impairment in optimal decision-making
- Fiorillo, Tobler & Schultz (2003, Science) — dopamine prediction error benchmark
- Padoa-Schioppa & Assad (2006, Nature) — OFC neurons encoding economic value
- Amiez, Joseph & Procyk (2006, Cereb. Cortex) — ACC reward encoding in macaques
- Behrens et al. (2007, Nat. Neurosci.) — ACC and volatility of reward contingencies

**Named models or frameworks**:
- Rangel et al. (2008) four-process valuation framework
- Receiver operating characteristic (ROC) sliding-window analysis
- Prediction error (Schultz/dopamine framework) — used as a contrast

**Brain regions**:
- Anterior cingulate cortex (ACC)
- Orbitofrontal cortex (OFC)
- Lateral prefrontal cortex (LPFC)

**Keywords**:
- outcome evaluation, frontal cortex, anterior cingulate cortex, single-unit recording, decision variables, reward magnitude, effort cost, probability, value encoding, choice evaluation, multi-variable multiplexing, prediction error
