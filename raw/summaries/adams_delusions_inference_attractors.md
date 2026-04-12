---
source_file: adams_delusions_inference_attractors.md
paper_id: adams_delusions_inference_attractors
title: "Everything is connected: Inference and attractors in delusions"
authors:
  - "Rick A. Adams"
  - "Peter Vincent"
  - "David Benrimoh"
  - "Karl J. Friston"
  - "Thomas Parr"
year: 2021
journal: "Schizophrenia Research"
paper_type: computational
contribution_type: theoretical
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - striatum
frameworks:
  - successor_representation
  - active_inference
  - bayesian_inference
keywords:
  - active_inference
  - delusions
  - attractor_dynamics
  - policy_precision
  - likelihood_precision
  - habitual_learning
  - bayesian_psychiatry
  - computational_psychiatry
  - dopamine_d2_receptors
  - paranoia
  - schizophrenia
  - choice_induced_preference_change
  - everything
  - connected
  - inference
  - attractors
key_citations:
  - stachenfeld2017_hippocampus_predictive_map
---

### One-line summary

An active inference Markov decision process model shows that delusional beliefs — false, certain, and incorrigible — can emerge from moderate, individually insufficient changes to likelihood precision, policy precision, habitual priors, and affective state, because Bayesian belief updating creates self-reinforcing attractor states from which the agent cannot easily escape.

---

### Background & motivation

Delusions — false beliefs held with certainty and resistant to contradictory evidence — appear paradoxical for Bayesian accounts of cognition, especially given that schizophrenia is characterised by *decreased*, not increased, certainty in the brain's world model. Prior computational work on schizophrenia has identified abnormalities in belief updating (larger updates to unexpected information, smaller updates to expected information), but these parameters have mixed relationships to delusions specifically, suggesting they are not the sole causal explanation. The paper addresses the puzzle of how an inference engine that globally underweights sensory evidence can simultaneously generate beliefs of incorrigible certainty — and proposes that feedback loops intrinsic to Bayesian updating itself are the key mechanism.

---

### Methods

- **Model**: Active inference partially observable Markov decision process (MDP) agent, implemented in SPM/Matlab. The agent performs a 250-trial social-inference task in which it must decide whether to trust or distrust an advisor and choose a card colour (blue or green).
- **Task structure**: Each trial has three timesteps (advice received, choice made, feedback received). The advisor is trustworthy (90% accurate) or untrustworthy (90% inaccurate); trustworthiness is either consistent across all trials or changes halfway through.
- **Key model parameters varied**:
  - Likelihood precision (*a*): how reliably feedback informs the agent about the world (range 0.60–0.99).
  - Habit resistance (*Dir*(**e**)): initial strength of the Dirichlet prior over policies, resisting new habit formation (range 2–600).
  - Policy precision prior (1/β): the agent's prior confidence in selecting policies (range 0.25–1.75).
  - Mood (*c*): stable prior over interoceptive (arousal) outcomes, representing positive or negative affective bias (range −4.5 to +4.5).
  - Choice precision (α): softmax stochasticity of overt action selection (range 0.5–2.75).
- **Affective model extension**: Trust/distrust decisions are coupled to an affective hidden state (calm vs. angry), and the agent observes interoceptive arousal outcomes; mood biases expected arousal.
- **Simulation design**: Five sets of 972 simulations each, pseudorandomly sampling the parameter space; two task sequences (consistently trustworthy; changing trustworthiness) × two model versions (with/without affect), plus a treatment simulation.
- **Delusion score**: Composite 0–3 score based on proportion of false posterior inferences, their certainty (>80% confidence), and incorrigibility (false inference followed by another false inference). Threshold criteria: falsity >66% (consistent) or >33% (changing trustworthiness); certainty >66%; incorrigibility >66%.
- **Antipsychotic simulation**: Once an agent made 10 false inferences, policy precision (1/β) was reduced proportionally, simulating D2 receptor antagonism.
- **Analysis**: Spearman's ρ correlations between parameters and delusion score; standardised regression betas for interaction effects.

---

### Key findings

- No single parameter change was both necessary and sufficient for delusions; delusions emerged from conditional dependencies among parameters.
- Reduced likelihood precision was the strongest individual determinant of delusion score (ρ = −0.64 in the full model) but was necessary rather than sufficient — it required interaction with habits and/or affect.
- Policy precision was the second strongest predictor (ρ = 0.48); habit resistance was weaker (ρ = −0.20).
- Without affect, the model produced no delusions 'proper' in the consistently-trustworthy sequence (0%), and 1.0% in the changing-trustworthiness sequence.
- Adding affective states tripled the delusion rate: 1.3% (consistent) and 3.2% (changing trustworthiness).
- Mood's primary contribution was to the *direction* (theme) of delusions (distrusting vs. trusting) rather than their frequency or certainty.
- Domain-general likelihood imprecision produced domain-specific (social) delusions when affect was included, because affect was coupled to social inference policies.
- Simulated antipsychotic treatment (reducing policy precision after 10 false inferences) reduced delusional agents from 31 to 5 (out of 972), without directly changing habits — the effect arose through recurrent updating among γ, policies, habits, and beliefs.
- State-space analysis identified three agent trajectories: those that form habits but can revise them (blue; low false inferences), those that form habits and partially fail to revise them (yellow/green; intermediate), and those that form very strong habits with increasing policy precision that form a self-reinforcing attractor (red; high false inferences).
- The model reproduced choice-induced preference change and an optimism bias in self-directed inferences as additional emergent phenomena.
- Delusion-like priors (habits) about the advisor's trustworthiness dominated over those about card identity specifically in models with affect, mirroring the social/affective themes of clinical delusions.

---

### Computational framework

**Active inference (Markov decision process formulation)** — a Bayesian framework in which both perception and action are cast as inference problems under a generative model, and the agent minimises variational free energy (F) for past/present beliefs and expected free energy (G) for future policy selection.

**Key variables and structure**:
- *Hidden states* (s): advisor trustworthiness, correct card, affective state, decision state.
- *Outcomes* (o): advice received, feedback received, arousal, observed choice.
- *Likelihood matrices* (**A**/**a**): probabilistic mapping from hidden states to outcomes; precision of **a**{2} (feedback) is the key manipulated parameter.
- *Transition matrices* (**B**/**b**): state evolution across timesteps; some are policy-dependent (trusting the advisor transitions affective state).
- *Policies* (π): sequences of control states. Prior over policies encoded by habits *Dir*(**e**) and policy precision γ. Policy precision γ is updated trial-to-trial: if anticipated policies match actual free-energy reduction, γ increases; otherwise it decreases (interpretable as a reward prediction error).
- *Habits*: Dirichlet accumulation of policy counts — purely a function of how often a policy has been selected, regardless of outcome valence.

**Core insight**: Because posterior beliefs about states are computed by Bayesian model averaging weighted by policy posteriors (Q(s) = Σ_π Q(π) Q(s|π)), the dominant policy shapes state inference. This creates bidirectional conditional dependencies — habits reinforce beliefs, beliefs reinforce habits, affect reinforces beliefs, beliefs reinforce affect, and policy precision amplifies both loops — producing basins of attraction in the free-energy landscape.

---

### Prevailing model of the system under study

The paper situates itself against a Bayesian/predictive-coding account of schizophrenia in which the dominant pathology is *reduced precision* of the brain's model — both sensory likelihoods and prior beliefs become less reliable. This framework (Adams et al., 2013; Fletcher & Frith, 2009; Sterzer et al., 2018) successfully explains phenomena such as resistance to visual illusions, smooth pursuit deficits, and reduced oddball EEG responses, and has been formalised as imprecise hierarchical generative models. From this vantage, schizophrenia is characterised by decreased confidence rather than increased confidence — making the certainty and incorrigibility of delusions appear deeply anomalous. Prior computational work in the field had also focused on belief-updating abnormalities in sequential inference tasks, typically modelled via hidden Markov models with altered likelihood or transition precision, volatility, or non-linear updating styles. These models could account for belief instability in schizophrenia but had mixed relationships with delusions specifically.

---

### What this paper contributes

The paper resolves the apparent paradox of incorrigible delusions within a globally imprecise brain by identifying *attractor dynamics* intrinsic to Bayesian belief updating itself. Specifically:

1. It shows that reduced likelihood precision alone does not produce delusions; rather, it acts as a permissive condition enabling other parameters (habits, policy precision, affect) to drive the system into self-reinforcing attractor states.
2. It provides a mechanistic account of why no single variable explains delusions — the conditional dependencies of variational inference necessarily create multi-factorial failure modes, analogous to "computational diaschisis".
3. It explains why delusions have strong affective themes: domain-general precision loss becomes domain-specific (social) pathology when affective states are coupled to social-inference policies.
4. It offers a novel computational mechanism for antipsychotic action: D2 receptor antagonism reduces policy precision (γ), breaking the habit–belief loop without directly altering habit strength, thereby allowing posterior beliefs to update again.
5. It reframes delusions as a *failure mode* of normal Bayesian updating — not a categorically different process — which explains their continuity with subclinical paranoia and their return on relapse (habit re-exposure).
6. It accounts for choice-induced preference change and optimism bias as emergent properties of the same model, grounding known psychological phenomena in active inference.

---

### Brain regions & systems

The paper is primarily computational with no direct neuroimaging or lesion data, but anatomical hypotheses are invoked:

- **Striatum (dorsal/tail of striatum)** — proposed locus of policy precision (γ), encoded by dopaminergic projections, particularly D2 receptors in the indirect pathway. The antipsychotic simulation is interpreted as D2R antagonism reducing γ. Cited support: fMRI (Schwartenbeck et al., 2015) and PET (Adams et al., 2020) data from active inference tasks; optogenetic study in mice linking tail-of-striatum dopamine to sensory expectations and false alarms (Schmack et al., 2021).
- **Prefrontal cortex** — implicated indirectly via the literature on stress-induced shift from goal-directed to habitual control (Dias-Ferreira et al., 2009; Soares et al., 2012; Otto et al., 2013); medial PFC volume loss under chronic stress promotes habits.
- **Hippocampus** — mentioned as the proposed substrate for the successor representation (Stachenfeld et al., 2017), an example of policy-dependent state inference outside the active inference framework, supporting the broader claim that state inference is conditioned on habitual policies.

---

### Mechanistic insight

The paper does not meet the full bar for mechanistic insight as defined here. It proposes a detailed algorithm — the active inference MDP — and formalises how habits, policy precision, likelihood precision, and affect jointly create attractor states that produce delusion-like inference. However, it does not provide original neural data (recordings, imaging, lesion, pharmacology) directly testing the model's specific variables against measured neural activity. The mechanistic claims about dopamine encoding policy precision and striatal D2R involvement are supported by citations to other empirical work, not by data collected in this paper.

**Computational level**: the brain solves a problem of inference under uncertainty about social intentions, simultaneously maintaining a model of its own action tendencies (policies/habits) — these two components interact to generate self-consistent beliefs.

**Algorithmic level**: variational free-energy minimisation via belief propagation; posterior beliefs about states are weighted sums over policies, creating the critical conditional dependency between policy priors and state posteriors; habits accumulate Dirichlet counts regardless of outcome valence, making them progressively outcome-independent.

**Implementational level**: policy precision γ is hypothesised to be encoded by striatal dopamine (D2 receptors, indirect pathway); no new neural data are presented to support this link.

---

### Limitations & open questions

- The task omits hierarchical/sequential inference across trials (each trial begins anew), so the model cannot capture trial-to-trial belief updating as studied in most empirical paradigms; the authors argue the same dynamics should arise in hierarchical extensions.
- The global likelihood precision decrease modelled here (a = 0.6–0.75) may be clinically extreme; more selective or domain-specific precision reductions are not modelled.
- The affective model assumes a simple coupling of trust/distrust decisions to arousal; richer bidirectional mood–belief dynamics (e.g., beliefs changing mood) are left to future work.
- The model does not address why delusions resist "second-factor" correction from memory or reasoning systems (cf. two-factor theories of delusions).
- Jaspers's category of "ununderstandable" delusions — those involving abrupt, experience-near alterations in the structure of semantic meaning — is acknowledged as outside the model's scope.
- The model does not capture referential ideas or delusions with weak affective themes.
- The paper calls for longitudinal experimental designs to test the predicted conditional dependencies between inference about states, affects, policies, and delusion scores.
- Whether D2R antagonists reduce delusions specifically via policy precision (as the model predicts) rather than via aberrant salience (Kapur, 2003) remains an empirical question; the two accounts make different predictions about which evidence (dominant vs. non-dominant policy) is most affected by antipsychotics.

---

### Connections & keywords

**Key citations**:
- Adams et al. (2013) — computational anatomy of psychosis (predictive coding account)
- Fletcher & Frith (2009) — Bayesian approach to positive symptoms of schizophrenia
- Friston et al. (2017a) — active inference: a process theory
- Behrens et al. (2008) — associative learning of social value (task basis)
- Diaconescu et al. (2014) — hierarchical Bayesian learning of others' intentions (task basis)
- FitzGerald et al. (2015) — dopamine, reward learning, and active inference
- Schmack et al. (2021) — striatal dopamine mediates hallucination-like perception in mice
- Adams et al. (2020) — striatal D2/3 receptor availability and variability in action selection (PET)
- Howes & Kapur (2009) — dopamine hypothesis of schizophrenia version III
- Kapur (2003) — aberrant salience framework
- Hoffman & McGlashan (2001) — parasitic attractors in parallel distributed processing models of schizophrenia
- Stachenfeld et al. (2017) — hippocampus as predictive map (successor representation)
- Reed et al. (2020) — paranoia as deficit in non-social belief updating

**Named models or frameworks**:
- Active inference (free energy principle)
- Markov decision process (MDP) model
- Partially observable MDP (POMDP)
- Variational free energy / expected free energy (G)
- Predictive coding hierarchy
- Successor representation (Dayan, 1993)
- Dirichlet habit learning
- Two-factor theory of delusions (Coltheart & Davies)
- Aberrant salience hypothesis (Kapur)

**Brain regions**:
- Striatum (dorsal / tail of striatum)
- Prefrontal cortex (medial)
- Hippocampus

**Keywords**:
- active inference
- delusions
- attractor dynamics
- policy precision
- likelihood precision
- habitual learning
- Bayesian psychiatry
- computational psychiatry
- dopamine D2 receptors
- paranoia
- schizophrenia
- choice-induced preference change
