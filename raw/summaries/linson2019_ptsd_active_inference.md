---
source_file: linson2019_ptsd_active_inference.md
paper_id: linson2019_ptsd_active_inference
title: "Reframing PTSD for computational psychiatry with the active inference framework"
authors:
  - "Adam Linson"
  - "Karl Friston"
year: 2019
journal: "Cognitive Neuropsychiatry"
paper_type: review
contribution_type: theoretical
tasks:
  - foraging_task
methods:
  - dynamic_causal_modelling
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - thalamus
  - amygdala
frameworks:
  - active_inference
  - bayesian_inference
keywords:
  - active_inference
  - free_energy_minimisation
  - ptsd_pathophysiology
  - precision_weighted_prediction_errors
  - epistemic_foraging
  - sensory_attenuation
  - threat_prior
  - fight_flight_freeze
  - auditory_masking_energetic_and_informational
  - fear_generalisation_fear_extinction
  - computational_psychiatry
  - hierarchical_generative_model
  - reframing
  - ptsd
  - computational
  - psychiatry
  - active
  - inference
  - framework
---

### One-line summary

PTSD is reframed as a maladaptive entrenchment of threat-response priors under the active inference framework, in which a failure of epistemic foraging (exploratory sensing) prevents belief updating and traps the organism in a self-maintaining fight/flight/freeze state.

---

### Background & motivation

PTSD is heterogeneous, and existing models tend to be discipline-bound — focusing exclusively on neurobiology or behavioural psychology without integration. Computational psychiatry has achieved traction in explaining schizophrenia and autism via Bayesian pathophysiology accounts, but equivalent treatment of PTSD is underdeveloped. This paper aims to provide a first-principles active inference account that unifies neurobiology, cognitive science, and evolutionary considerations of PTSD, thereby creating a theoretical foundation for subsequent in silico modelling work.

---

### Methods

This is a theoretical review paper synthesising empirical and computational work across multiple domains.

- Scope of literature: neurobiology and psychology of stress and PTSD; auditory cognition (cocktail party effect, auditory masking, acoustic startle); computational psychiatry of schizophrenia and autism; evolutionary biophysics and metabolic constraints on sensing.
- Synthesis method: narrative integration using active inference (free energy minimisation) as the unifying formal framework.
- An "explanatory stack" of four levels is constructed: (i) embodied-embedded body/environment dynamics, (ii) neurobiological substrate, (iii) hierarchical Bayesian generative model, and (iv) psychophysical/phenomenological level.
- No new empirical data are collected; existing studies are interpreted and contextualised within the framework.

---

### Key findings

- PTSD can be characterised as a pathologically strong threat prior that biases model competition toward threat detection, drastically lowering the evidence threshold required to classify a stimulus as dangerous.
- Crucially, the threat prior also suppresses epistemic foraging (active scene resampling), preventing the organism from obtaining the contradictory sensory evidence that would revise or extinguish the prior — a self-maintaining pathological attractor.
- This double deficit (strong threat prior + impaired scene resampling) explains the full phenomenology: hyperarousal, hypervigilance, flashbacks, re-experiencing, and impaired reality testing.
- "Safety learning" and "fear extinction" are recast as repairing inference by extending the counterfactual space to include non-threat hidden causes.
- Type 1 trauma (acute, high-energy event) maps onto energetic auditory masking and fight/flight policy selection; Type 2 trauma (chronic threat) maps onto informational masking and freeze/hypervigilance policy selection.
- Physiologically, the mechanism involves stress-induced Ca2+/cAMP signalling in the PFC that opens K+ channels, hyperpolarises cells, and weakens long-range connectivity — decoupling exteroceptive inference from higher cortical comprehension and locking the system into limbic/amygdala-driven responses.
- The absent gamma-frequency synchrony under stress corresponds to impaired neuronal message passing, consistent with a "underfitting" scenario: sparse environmental samples are dominated by strong top-down priors.
- The account integrates contextual processing models of PTSD (Liberzon & Abelson, 2016) with the Bayesian formalisms, offering explanatory power beyond neural circuit descriptions.

---

### Computational framework

**Active inference / free energy minimisation (Friston, 2009, 2010)**

- Core formalisation: agents minimise variational free energy (an upper bound on sensory surprise) through a combination of perceptual inference (updating internal beliefs to match sensory input) and active inference (acting on the world to make sensory input conform to predictions).
- Key variables: prior beliefs over hidden world states and policies; precision (the inverse variance) weighting prediction errors; expected free energy guiding policy selection; metabolic cost as an implicit constraint on action and sensing.
- In the PTSD account, the generative model is hierarchical. At the top, an evolutionarily selected "survival prior" underwrites fight/flight/freeze policies. At lower levels, exteroceptive prediction errors from auditory and visual streams update beliefs about environmental states. Precision control — implemented via neuromodulation and postsynaptic gain — determines how strongly ascending prediction errors influence belief revision.
- Under PTSD, the precision afforded to exteroceptive prediction errors is pathologically attenuated (sensory attenuation), not intrinsically but because the dominant policy (fight/flight) mandates metabolic reallocation away from exploratory sensing.
- Reward is recast as minimising expected free energy; proprioceptive inference implements action; interoception/exteroception are modelled as separate inference streams, each with their own precision-weighting.

---

### Prevailing model of the system under study

The dominant pre-existing framework for PTSD emphasised a classical information-processing scheme: sensory input is neurally computed, and PTSD results from impaired top-down executive control (PFC) over bottom-up sensory/limbic signals. Within this framework, impaired "reality testing" was understood as a failure of PFC-mediated cognitive control over amygdala-driven fear responses, and symptoms such as generalised conditioned fear were explained in terms of associative learning gone wrong (e.g., overgeneralisation of conditioned fear). Contextual processing models (Liberzon & Abelson, 2016) added the idea that hippocampus-PFC-thalamus-amygdala circuitry is impaired in contextual gating of fear. The paper positions all of these accounts as valid but incomplete because they treat the brain as a passive input-output processor rather than an active, self-organising, embodied agent — and because they underestimate the metabolic and evolutionary constraints on sensorimotor inference.

---

### What this paper contributes

The active inference reframing offers the following specific advances:

1. Unification: diverse clinical, cognitive, and neurobiological findings on PTSD are brought into a single principled framework rather than remaining as parallel, discipline-specific accounts.
2. Mechanism: impaired "reality testing" is not merely PFC-executive failure but specifically a failure of epistemic foraging — the biased sampling of the world that is mandated by the dominant threat policy, making the disorder self-maintaining.
3. Causal account: the paper explains why the pathology persists: once the threat prior is dominant, it blocks the very sensory evidence that would disconfirm it. This is more causally explicit than "impaired extinction" or "overgeneralised fear conditioning."
4. Evolutionary grounding: PTSD is an emergent phenotype from normally adaptive survival priors, not a post-hoc symptom cluster — providing a framework for thinking about individual differences in vulnerability.
5. Therapeutic implications: safety learning and fear extinction are reinterpreted as epistemic repairs (expanding counterfactual inference space), pointing toward interventions that restore exploratory sensing rather than simply extinguishing fear associations.
6. Auditory specificity: the paper provides a novel account of why auditory stimuli are particularly relevant to PTSD — grounded in evolutionary biophysics (auditory pathway speed, azimuthal precision, energetic salience) rather than purely clinical observation.

---

### Brain regions & systems

- **Prefrontal cortex (PFC)** — locus of precision control over ascending prediction errors and long-range connectivity; stress-induced Ca2+/cAMP signalling hyperpolarises PFC cells, weakening effective connectivity and decoupling exteroceptive comprehension from limbic responses; role in epistemic foraging and reality testing.
- **Amygdala** — hub of threat-prior activation and amygdala-modulated fight/flight/freeze policy selection; responds to sparse sensory information; inhibits PFC-modulated scene sampling subsystem; role in associative learning of threat-linked stimuli.
- **Hippocampus** — implicated in contextual processing; hippocampal-prefrontal pathway (Godsil et al., 2013) mediates scene recognition and exteroceptive inference; functional decoupling between hippocampus and PFC is proposed as a substrate of PTSD impairment.
- **Hypothalamus-pituitary-adrenal (HPA) axis** — neuroendocrine system whose dysregulation (hyperarousal with hypocortisolaemia) is explained by the self-maintaining threat state preventing the glucocorticoid "brake" from operating.
- **Limbic system / sympathetic nervous system** — receives redirected metabolic resources under fight/flight policy; includes locomotor circuits activated during motor preparation.
- **Auditory cortex and frontal-temporal pathway** — the auditory processing hierarchy (stimulus detection through comprehension) is invoked throughout; long-range propagation to higher cortical areas is required for threat disconfirmation; this propagation is impaired under stress.
- **Thalamus** — mentioned as part of the context-processing circuitry (hippocampus-PFC-thalamus-amygdala) impaired in PTSD.

---

### Mechanistic insight

The paper does not present original empirical data and therefore does not itself meet the two-criterion bar. It synthesises existing evidence rather than providing new neural recordings, imaging, or pharmacological data directly testing the active inference algorithm.

The paper proposes a specific algorithm (active inference with precision-weighted prediction errors, hierarchical policy selection, and epistemic foraging as the key restorative process) and cites supporting empirical evidence (e.g., stress-induced PFC hyperpolarisation via Ca2+/cAMP/K+ channels — Arnsten, 2009, 2015; resting-state effective connectivity impairment in PTSD — Nicholson et al., 2017; gamma oscillation impairment — Fries, 2005; auditory startle in PTSD — Shalev et al., 2000), but the mapping is cross-study synthesis rather than within-study algorithmic validation. The subsequent paper (Linson, Parr & Friston, in review at time of publication) is described as providing electrophysiological and psychophysical tests of the specific model variables.

---

### Limitations & open questions

- The paper explicitly characterises itself as a theoretical reframing and foundation for future empirical work; no new data are presented, so the specific active inference formalisation of PTSD has not yet been directly validated.
- The "fight or flight" abstraction is acknowledged to oversimplify threat response repertoires (e.g., fright/tonic immobility is excluded; the serial ordering of flight > fight is noted but not modelled).
- Individual differences in PTSD vulnerability and recovery are discussed conceptually but not formalised.
- The mechanisms by which an original trauma experience creates or potentiates a strong threat prior in the first place are not fully specified (the developmental/learning origins of the prior are left to future work).
- The relationship between PTSD and psychosis (comorbidity, overlapping mechanisms) is flagged as significant but not resolved — the framework places both on a continuum of precision/inference dysfunction, but does not differentiate them formally.
- How to translate the account into tractable clinical interventions (beyond the broad suggestion of restoring epistemic foraging) is not worked out in this paper.
- The framework assumes a Markov Decision Process generative model structure, which is an approximation that may not capture the full richness of trauma phenomenology (e.g., temporal dynamics of intrusive memories).

---

### Connections & keywords

**Key citations:**
- Friston (2009, 2010) — free energy principle and active inference
- Feldman & Friston (2010) — attention, uncertainty, and free energy; precision control of sensory signals
- Brown, Friston & Bestmann (2011) — active inference, attention, and motor preparation
- Arnsten (2009, 2015) — stress-induced PFC impairment via Ca2+/cAMP signalling
- Liberzon & Abelson (2016) — contextual processing model of PTSD
- Nicholson et al. (2017) — dynamic causal modelling of effective connectivity in PTSD
- Peters, McEwen & Friston (2017) — uncertainty, stress, and free energy
- Linson, Clark, Ramamoorthy & Friston (2018) — active inference for embodied ecological cognition
- Wilkinson, Dodgson & Meares (2017) — predictive processing and psychological trauma typology
- LeDoux (2012) — evolutionary account of emotion and neural circuits
- Shalev et al. (2000) — auditory startle response in PTSD

**Named models or frameworks:**
- Active inference / free energy minimisation (Friston)
- Predictive coding / hierarchical predictive processing
- Bayesian brain / hierarchical Bayesian generative model
- Global Neuronal Workspace Theory (referenced as related account, Vugt et al., 2018)
- Markov Decision Process scheme for active inference (mentioned as basis of subsequent paper)
- "Explanatory stack" (four-level explanatory architecture: embodied-embedded / neurobiological / hierarchical Bayesian / psychophysical)

**Brain regions:**
- Prefrontal cortex (PFC)
- Amygdala
- Hippocampus (hippocampal-prefrontal pathway)
- Hypothalamus-pituitary-adrenal (HPA) axis
- Thalamus
- Auditory cortex / frontal-temporal cortex

**Keywords:**
- active inference
- free energy minimisation
- PTSD pathophysiology
- precision-weighted prediction errors
- epistemic foraging
- sensory attenuation
- threat prior
- fight-flight-freeze
- auditory masking (energetic and informational)
- fear generalisation / fear extinction
- computational psychiatry
- hierarchical generative model
