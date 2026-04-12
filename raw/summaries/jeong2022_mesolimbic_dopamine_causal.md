---
source_file: jeong2022_mesolimbic_dopamine_causal.md
paper_id: jeong2022_mesolimbic_dopamine_causal
title: "Mesolimbic dopamine release conveys causal associations"
authors:
  - "Huijeong Jeong"
  - "Annie Taylor"
  - "Joseph R. Floeder"
  - "Martin Lohmann"
  - "Stefan Mihalas"
  - "Brenda Wu"
  - "Mingkang Zhou"
  - "Dennis A. Burke"
  - "Vijay Mohan K Namboodiri"
year: 2022
journal: Science
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - optogenetics
brain_regions:
  - orbitofrontal_cortex
  - nucleus_accumbens
  - ventral_tegmental_area
frameworks:
  - reinforcement_learning
  - bayesian_inference
keywords:
  - mesolimbic_dopamine
  - reward_prediction_error
  - temporal_difference_reinforcement_learning
  - retrospective_causal_inference
  - causal_associative_learning
  - nucleus_accumbens
  - fiber_photometry
  - dlight_dopamine_sensor
  - pavlovian_conditioning
  - cue_reward_association
  - extinction_learning
  - optogenetics
  - mesolimbic
  - dopamine
  - release
  - conveys
  - causal
  - associations
wiki_pages:
  - wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning
  - wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning
---

### One-line summary

Mesolimbic dopamine release in the nucleus accumbens core tracks a retrospective causal associative signal (ANCCR) rather than a temporal difference reward prediction error (TDRL RPE), challenging the dominant theory of dopamine's role in reward learning.

---

### Background & motivation

The dominant framework for reward learning holds that animals learn prospective predictions of reward via reward prediction errors (RPEs), and that mesolimbic dopamine neurons signal these RPEs according to temporal difference reinforcement learning (TDRL). This view has been supported by decades of data on dopaminergic cell body firing and nucleus accumbens (NAcc) dopamine release. However, an alternative framework proposes that animals can learn by retrospectively inferring the causes of meaningful outcomes, which generates qualitatively different predictions about dopamine dynamics. The paper asks whether mesolimbic dopamine release actually encodes TDRL RPE or instead conveys a causal associative signal, using experimental designs that maximally separate the two hypotheses.

---

### Methods

- **Subjects**: Head-fixed mice implanted with fiber photometry probes in nucleus accumbens core (NAcc).
- **Dopamine measurement**: Fiber photometry of dLight 1.3b, a genetically encoded fluorescent dopamine sensor, expressed in NAcc to measure sub-second mesolimbic dopamine release.
- **Model development**: A new algorithm — Adjusted Net Contingency for Causal Relations (ANCCR) — was developed and formalised as an alternative to TDRL. ANCCR computes whether a stimulus precedes reward more than expected by chance (retrospective association), converts this to a prospective prediction via Bayes' rule, and constructs a causal map of associations.
- **Eleven experimental tests** were designed so that ANCCR and TDRL RPE make qualitatively different (often opposing) predictions:
  - Tests 1–2: Unpredicted rewards with exponential inter-reward intervals; measured whether dopamine response increases or decreases with repeated exposures, and whether it correlates positively or negatively with the preceding inter-reward interval.
  - Tests 3–7: Cue-reward learning paradigm; assessed temporal relationship between dopaminergic learning and behavioral learning, response to delay extension, extinction, and manipulations of retrospective vs. prospective contingency.
  - Test 8: "Trial-less" cue-reward learning with unpredictable inter-cue intervals; tested response to intermediate cues presented during an ongoing cue-to-reward interval.
  - Tests 9–11: Assessed whether dopamine backpropagates from reward to cue onset during trace conditioning, whether sequential conditioning produces ordered vs. simultaneous cue responses, and whether optogenetic inhibition of dopamine during a second-order interval prevents first-order cue learning.
- **Optogenetics**: Inhibition of dopaminergic cell bodies during specific task epochs in sequential conditioning experiments.
- **Behavioral measure**: Anticipatory licking as an index of learned cue-reward association.

---

### Key findings

- In the unpredicted-reward paradigm, dopamine response to sucrose **increased** across sessions to a high positive asymptote — consistent with ANCCR but inconsistent with RPE (which predicts a decrease as the reward becomes contextually predicted).
- The dopamine response to sucrose correlated **positively** with the preceding inter-reward interval — consistent with ANCCR (longer IRI lowers baseline reward rate) but opposite to TDRL RPE (which predicts negative correlation).
- During cue-reward learning, dopaminergic cue responses emerged and reached their peak **before** the onset of anticipatory licking — consistent with ANCCR's prediction that dopaminergic learning precedes behavioral learning, inconsistent with TDRL's tight coupling.
- Extending the cue-reward delay produced **no significant change** in the dopaminergic cue response — consistent with ANCCR, inconsistent with RPE (which predicts temporal discounting).
- After extinction, dopamine cue response remained **significantly positive** long after behavioral extinction — consistent with ANCCR's "long-term memory" of retrospective association, inconsistent with TDRL (which predicts the cue response decays to zero with the behaviour).
- Adding unpredicted intertrial rewards (weakening retrospective but not prospective contingency) caused a more rapid decline in dopamine cue response — consistent with ANCCR's dependence on retrospective association.
- In the "trial-less" paradigm, intermediate cues presented during an ongoing cue-to-reward interval produced a **positive but reduced** dopamine response, not the negative response predicted by TDRL.
- During sequential conditioning, dopamine responses to second-order cue (cue2) and first-order cue (cue1) increased **together** early in learning before diverging — consistent with ANCCR, inconsistent with TDRL's ordered backpropagation.
- Optogenetic inhibition of dopamine neurons during the cue2-to-reward interval did not prevent learning of cue1 responses — consistent with ANCCR, inconsistent with TDRL's prediction of no learning under such conditions.

---

### Computational framework

**Retrospective causal inference / ANCCR (Adjusted Net Contingency for Causal Relations)**

The framework departs from TDRL by positing that the mesolimbic dopamine system does not track forward-looking value predictions but rather signals whether a stimulus is a "meaningful causal target" — i.e., whether it reliably precedes a rewarding outcome more than expected by chance.

Key variables and operations:
- **Net contingency**: measures whether a stimulus precedes reward at a rate above baseline (retrospective association). This is computed over an appropriate timescale set by the inter-reward interval.
- **Bayes' rule conversion**: the retrospective contingency is converted to a prospective prediction.
- **ANCCR signal**: an adjusted net contingency that the algorithm proposes is broadcast by mesolimbic dopamine. At asymptote, ANCCR ≈ 1 × incentive value for a fully predictive cue, and approaches 0 for uninformative stimuli.
- **Causal map**: the system builds an associative graph of which stimuli cause which outcomes, including second-order associations.

Key assumptions: (1) animals track the rate of events over time rather than tile delays with discrete states; (2) the retrospective causal trace is maintained across extinction; (3) behavioral learning (e.g., timed licking) requires an internal threshold crossing of ANCCR, making behavioral acquisition more abrupt than dopaminergic learning. The framework is timescale-invariant, unlike TDRL which requires a fixed state-space representation of temporal delays.

---

### Prevailing model of the system under study

Before this paper, the dominant model held that mesolimbic dopamine neurons — especially those projecting from the ventral tegmental area (VTA) to NAcc — encode temporal difference reward prediction errors (TDRL RPE). In this framework, animals learn by maintaining a forward-looking value function over a sequence of internal states that tile temporal delays, and dopamine release broadcasts the scalar RPE signal used to update these values. This model was supported by foundational studies showing that dopamine neuron firing (Schultz, Dayan, and Montague 1997) and NAcc dopamine release track RPE across a wide range of conditioning paradigms. The TDRL RPE account was widely taken as causally necessary for behavioral learning, with optogenetic stimulation and inhibition studies providing apparent causal support. The paper's introduction acknowledges this as the "dominant theory" and treats it as the null hypothesis against which the ANCCR framework is tested.

---

### What this paper contributes

The paper provides systematic empirical evidence — across eleven distinct experimental tests — that NAcc mesolimbic dopamine release does **not** conform to TDRL RPE predictions and instead matches the predictions of a retrospective causal learning algorithm (ANCCR). Specifically, the results show that: (1) dopamine signals increase rather than decrease to repeated unpredicted rewards; (2) dopamine learning leads rather than tracks behavioral learning; (3) dopamine cue responses survive extinction; and (4) the causal structure of sequential conditioning is acquired without a backpropagating dopamine signal. Together, these results reframe the computational role of mesolimbic dopamine from a prediction-error signal in a prospective value system to a signal of causal associative strength in a retrospective inference system. The paper also proposes ANCCR as an alternative learning algorithm that accounts for a wide range of published dopamine observations previously attributed to RPE, while additionally explaining several anomalies (e.g., persistent dopamine responses to predicted rewards, violation of RPE backpropagation dynamics).

---

### Brain regions & systems

- **Nucleus accumbens core (NAcc)**: primary measurement site; proposed locus of mesolimbic dopamine release that has been the strongest target for TDRL RPE evidence; here shown to track ANCCR rather than RPE.
- **Ventral tegmental area (VTA)**: site of mesolimbic dopaminergic soma; targeted for optogenetic inhibition in sequential conditioning experiments.
- **Orbitofrontal cortex (OFC)**: discussed as a candidate source of retrospective cue-reward memory information conveyed to the dopaminergic system, based on prior work (Namboodiri et al. 2019) showing OFC neurons maintain long-term retrospective associations.
- **Mesolimbic dopamine system (VTA → NAcc)**: the central system under study; its functional role is recharacterised from RPE signalling to causal associative signalling.

---

### Mechanistic insight

The paper meets both criteria for mechanistic insight: it formalises a specific algorithm (ANCCR) and provides neural data (fiber photometry of NAcc dopamine release) that systematically favour this algorithm over the leading alternative (TDRL RPE) across eleven independent tests.

**Computational level**: The brain is solving the problem of identifying which environmental stimuli reliably cause meaningful outcomes (rewards). This is framed as retrospective causal inference — given a reward just received, what preceded it more than chance would predict?

**Algorithmic level**: The ANCCR algorithm computes a net contingency between a stimulus and reward over an appropriate timescale, converts this retrospective measure to a prospective causal probability via Bayes' rule, and maintains a causal map of associations. Mesolimbic dopamine release broadcasts the ANCCR value of the current stimulus — signalling whether it is a meaningful causal target. Unlike TDRL, the algorithm does not decompose delays into sequential states, is timescale-invariant, and preserves retrospective associations across extinction. Behavioral learning (anticipatory licking) occurs as a separate downstream process triggered when ANCCR crosses an internal threshold.

**Implementational level**: The paper identifies NAcc core dopamine release (measured via the dLight 1.3b sensor) as the neural substrate of ANCCR signalling. OFC projections to VTA are proposed as the source of long-term retrospective cue-reward memory. Optogenetic inhibition of VTA dopamine neurons during specific task epochs was used to probe causal necessity, finding that dopamine during second-order cue-to-reward intervals is not required for first-order cue learning (contrary to TDRL). The paper does not resolve specific cell types or synaptic mechanisms within NAcc or VTA.

---

### Limitations & open questions

- The state-space assumptions of TDRL are highly flexible; the authors cannot exclude the possibility that some novel state-space formulation of TDRL could fit the data, making an exhaustive falsification of TDRL impossible.
- The paper tests dopamine release specifically in NAcc core; whether dopamine in other striatal subregions (e.g., NAcc shell, dorsal striatum) also tracks ANCCR rather than RPE remains open.
- The mechanism by which the brain sets the appropriate timescale for the ANCCR computation (i.e., how it estimates the inter-reward interval) is assumed rather than derived; multiple-timescale parallel systems are proposed as a candidate solution but not tested here.
- The source of retrospective cue-reward memory conveyed to the dopaminergic system is proposed to be OFC (based on prior work) but is not directly tested in this study.
- Whether ANCCR extends to instrumental (action-contingent) learning, including action-conditional cognitive maps, remains to be addressed.
- The relation between ANCCR signalling in the mesolimbic system and the putative RPE-like signals observed in dopaminergic cell body recordings (electrophysiology) is not directly resolved; the paper specifically focuses on NAcc dopamine release rather than VTA firing.

---

### Connections & keywords

**Key citations**:
- Schultz, Dayan, Montague (1997) — foundational RPE study in dopamine neurons
- Rescorla and Wagner (1972) — classical conditioning model underpinning RPE
- Niv and Schoenbaum (2008); Niv (2009) — TDRL RPE framework
- Namboodiri et al. (2019) — OFC long-term retrospective memory
- Namboodiri and Stuber (2021) — prospective and retrospective cognitive maps
- Gallistel, Craig, Shahan (2019) — contingency, contiguity, causality in conditioning
- Amo et al. (2022) — dopamine backpropagation consistent with TDRL RPE
- Kim et al. (2020) — unified framework for dopamine signals across timescales
- Steinberg et al. (2013); Chang et al. (2016) — causal RPE evidence via optogenetics
- Mohebi et al. (2019) — dissociable dopamine dynamics for learning and motivation

**Named models or frameworks**:
- ANCCR (Adjusted Net Contingency for Causal Relations) — the novel algorithm proposed in this paper
- TDRL (Temporal Difference Reinforcement Learning) — the dominant hypothesis under challenge
- Rescorla-Wagner model
- dLight 1.3b (genetically encoded dopamine sensor)

**Brain regions**:
- Nucleus accumbens core (NAcc)
- Ventral tegmental area (VTA)
- Orbitofrontal cortex (OFC)

**Keywords**:
- mesolimbic dopamine
- reward prediction error
- temporal difference reinforcement learning
- retrospective causal inference
- causal associative learning
- nucleus accumbens
- fiber photometry
- dLight dopamine sensor
- Pavlovian conditioning
- cue-reward association
- extinction learning
- optogenetics

### Related wiki pages
- [[wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning|Orbitofrontal cortex as a cognitive map of task state for model-based reinforcement learning]]
- [[wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning|Task-state representation and hidden-state inference in orbitofrontal–hippocampal reinforcement learning]]
