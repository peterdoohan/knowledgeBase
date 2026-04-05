---
source_file: lee2019_dopamine_movement_selectivity.md
title: Reward prediction error does not explain movement selectivity in DMS-projecting dopamine neurons
authors: Rachel S Lee, Marcelo G Mattar, Nathan F Parker, Ilana B Witten, Nathaniel D Daw
year: 2019
journal: eLife
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Movement-related signals in dopamine neurons projecting to dorsomedial striatum (DMS) are genuinely distinct from reward prediction error signals: the value component reflects chosen (not contralateral) action value and cannot account for the neurons' contralateral choice selectivity.

---

### Background & motivation

Midbrain dopamine (DA) neurons are classically understood to encode reward prediction errors (RPEs), but recent recordings — including a prior study by the same group (Parker et al., 2016) — showed that DA neurons projecting to the dorsomedial striatum (DMS) are also selectively active during contralateral choices. This creates a puzzle: are these movement-related signals genuinely encoding motor direction, or might they be explained by a more sophisticated RPE — specifically, an action-specific RPE tuned to the value of the contralateral movement? Resolving this would clarify whether dopamine has a direct role in movement encoding beyond its established role in reward learning.

---

### Methods

- **Subjects**: 17 male TH-IRES-Cre mice expressing GCaMP6f in dopamine neurons; recordings from DMS-projecting neurons via fiber photometry.
- **Recording sites**: VTA/SN::DMS terminals (n = 12 recording sites) and VTA/SN::DMS cell bodies via retrograde labeling (n = 7 recording sites).
- **Task**: Probabilistic reversal learning — mice chose between two levers with reward probabilities of 70% and 10%, with the high-probability lever swapping on an unsignalled pseudorandom schedule.
- **Behavioral modeling**: Trial-by-trial Q-learning mixed-effects model fit to each mouse's choices using Hamiltonian Monte Carlo (Stan/PyStan); free parameters: learning rate (α), inverse temperature (β), stay bonus.
- **Value proxies**: (1) Previous trial outcome (rewarded vs. not, restricted to stay trials) as a theory-neutral proxy; (2) Q-value difference (chosen minus unchosen) from the fitted model.
- **Key analysis**: Linear mixed-effects regression of GCaMP6f signal (time-locked to lever presentation and lever press) onto action (contra vs. ipsi), value difference, their interaction, and intercept. Compared two reference frames: contralateral value (contra minus ipsi Q-values) vs. chosen value (chosen minus unchosen Q-values).
- **Control analyses**: Signals time-locked to nose poke; multi-event kernel regression (nose poke, lever presentation, lever press simultaneously); within-animal hemisphere comparison; lever-press latency as a vigor covariate.

---

### Key findings

- DMS-projecting DA neurons show significant modulation by both contralateral movement direction and action value, confirming that two distinct signals coexist.
- The value signal follows a **chosen value** reference frame: GCaMP6f is higher for rewarded (or high Q-value) trials regardless of whether the choice was contralateral or ipsilateral. The direction of value modulation does not flip between contra and ipsi trials.
- A **contralateral value** model predicts that value modulation should reverse sign between contra and ipsi trials. This prediction was not supported — a significant interaction emerged only when the regression was cast in terms of contralateral value (supporting the chosen value model by exclusion).
- After lever press, the **contralateral/ipsilateral selectivity reversed** sign (consistent with the mouse reversing physical head direction back to the reward port), while value modulation did not reverse — further dissociating the two signals.
- Results were consistent across recording from terminals and cell bodies, ruling out terminal-level introduction of the movement signal (e.g., via cholinergic interneurons).
- Lever-press latency (as a proxy for movement vigor or motivation) did not significantly predict GCaMP6f, nor did it eliminate the contralateral action effect.
- Counterbalanced hemisphere recordings confirmed that the contralateral selectivity reverses within-animal, ruling out side biases.

---

### Computational framework

The paper uses a **reinforcement learning / temporal difference (TD) RPE** framework as its primary lens.

The central question is whether DMS DA signals encode a standard RPE for the chosen state value, or an action-specific RPE for the contralateral action value. Two competing models are formalised:

1. **Contralateral value model**: DA neurons track the TD RPE for the value of the contralateral action specifically (analogous to action-specific critics in actor-critic architectures, or advantage learning). This would predict that value modulation flips sign across contra vs. ipsi choice trials.

2. **Chosen value model**: DA neurons track a standard critic RPE for the value of whichever action was chosen (the current state value, conditioned on the choice made). This is the classic mesolimbic RPE formulation. This would predict consistent value modulation sign regardless of which action was chosen.

The paper does not develop a new computational model — it uses the Q-learning fit purely to estimate trial-by-trial value, not to make novel theoretical claims about DA computation. The framework constrains what the observed signals can mean: because movement direction encoding survives after partialling out chosen value, something beyond RPE is present in DMS DA signals.

---

### Prevailing model of the system under study

The introduction presents two partially competing frameworks that were both active in the field prior to this paper:

1. **Classic RPE account**: DA neurons primarily encode RPE — the difference between received and predicted reward — which drives corticostriatal plasticity and enables reward-based learning. In this framework, DA influences movement only indirectly: by shaping which movements are reinforced (via learning) or via tonic effects on response vigour. Phasic DA activity at the time of actions reflects anticipatory components of the TD error (value signals at predictive cues), not movement per se.

2. **Direct movement encoding**: A growing set of studies (including Parker et al., 2016 from the same labs) had reported that subsets of DA neurons, particularly those projecting to dorsal striatum, show phasic responses correlated with movement onset, choice direction, or locomotion. These observations were difficult to reconcile with the pure RPE account but had not been definitively separated from a possible action-specific RPE explanation.

The specific resolution the paper tests — that contralateral choice selectivity could be an action-specific RPE rather than direct movement encoding — was an open possibility that prior work had not cleanly ruled out.

---

### What this paper contributes

Prior to this paper, the movement-related signals in DMS-projecting DA neurons (Parker et al., 2016) were ambiguous: they could have reflected direct encoding of contralateral movement direction, or could have been reinterpreted as an action-specific RPE (value predictions tied to contralateral choices). This paper definitively rules out the action-specific RPE account for these signals. The key contribution is to show that:

1. The value component of DMS DA signals tracks *chosen* action value — not contralateral action value — making a value-based explanation of the lateralised selectivity impossible within any standard RPE framework.
2. The movement-directional component is therefore a genuinely independent signal, not reducible to RPE in any obvious formulation.
3. The two signals have distinct temporal dynamics and distinct reference frames (contralateral vs. ipsilateral for movement; chosen vs. unchosen for value), and coexist in the same population-level signal.

The paper thus establishes that DMS-projecting DA neurons multiplex at minimum two functionally distinct signals — RPE for chosen value and a direct movement direction signal — and calls for an extended computational account that incorporates both.

---

### Brain regions & systems

- **VTA/SNc (ventral tegmental area / substantia nigra pars compacta)**: Source of recorded dopamine neurons; fibers placed here for cell-body recordings of retrogradely labelled DMS-projecting cells.
- **Dorsomedial striatum (DMS)**: Primary target of the recorded DA projection; site of terminal recordings. The DMS has been implicated in goal-directed behaviour and action selection. Movement-direction selectivity is specifically associated with this projection.
- **Ventral striatum / nucleus accumbens (NAcc)**: Mentioned as comparison site (DA projections here show classic RPE signals without strong movement selectivity); contralateral recording site in the same animals but data not analysed in this paper.
- **Basal ganglia direct/indirect pathways**: Discussed as the putative downstream mechanism by which lateralised DA signals could selectively modulate contralateral movements, via differential effects on medium spiny neurons.

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight.

It presents an algorithm (competing formalisations of RPE — contralateral value vs. chosen value) and provides neural data (GCaMP6f photometry) that specifically supports one algorithm over the other.

**Computational level**: The brain must solve the problem of credit assignment — determining which actions and states produced reward — and must also regulate movement initiation. These may be partially separable computational problems.

**Algorithmic level**: DMS-projecting DA neurons implement two distinct computations simultaneously: (a) a standard chosen-value TD signal (anticipatory RPE for overall state value, conditioned on the choice made), consistent with a 'critic' in actor-critic frameworks; and (b) a contralateral movement-direction signal that tracks which way the animal is moving rather than the value of that movement. The critical evidence is that decomposing GCaMP6f signals by both choice direction and value shows consistent (not reversed) value modulation across contra and ipsi trials — ruling out the contralateral value algorithm — while the directional modulation reverses following lever press in tandem with the animal's physical reversal of movement direction.

**Implementational level**: The paper provides partial implementational grounding. The signal is present at both terminals and cell bodies, ruling out terminal-level insertion of the movement signal (e.g., via striatal cholinergic interneurons or glutamatergic inputs). The movement-direction signal likely enters at the level of midbrain DA cell bodies, consistent with anatomical inputs to VTA/SNc from motor and premotor circuits. The downstream mechanism — differential modulation of direct vs. indirect pathway medium spiny neurons in DMS — is discussed but not directly tested. A limitation is that fiber photometry provides only population-level data, leaving open whether individual DA neurons multiplex both signals or whether they are segregated across distinct cell subpopulations.

---

### Limitations & open questions

- **Population vs. single-unit resolution**: Fiber photometry captures bulk fluorescence; it is not possible to determine whether individual DA neurons carry both the RPE and movement signals simultaneously, or whether they are segregated across distinct neuronal subpopulations. Single-unit or two-photon imaging is needed.
- **Movement monitoring**: The inference that post-lever-press signal reversal reflects change in head/movement direction is plausible but not directly confirmed — head tracking was not available.
- **Causal role**: The study is correlational. Whether the contralateral DA signal *causes* movement initiation or only correlates with it cannot be established from photometry alone.
- **Motor vigor / motivation**: Lever-press latency was controlled for but is an imperfect proxy. Finer-grained movement kinematics could help further dissociate motivation from direction signals.
- **Generality**: The findings are specific to DMS-projecting DA neurons in a two-choice reversal learning task. Whether the same dissociation holds in other DA projection pathways (e.g., DLS, NAcc) or in tasks with more complex action spaces is unresolved.
- **Plasticity implications**: If both RPE and movement signals coexist in the same DA signal at DMS synapses, how do recipient medium spiny neurons parse them for learning versus action-initiation purposes? This remains an open mechanistic question.
- **Action-specific RPEs elsewhere**: Although the DMS signal does not reflect contralateral value RPE, the possibility of action-specific RPEs in other brain regions or projection targets is not ruled out and remains a productive question.

---

### Connections & keywords

**Key citations**:
- Parker et al. (2016) — original report of contralateral choice selectivity in VTA/SN::DMS DA neurons (Nature Neuroscience)
- Schultz, Dayan & Montague (1997) — foundational RPE account of DA
- Montague, Dayan & Sejnowski (1996) — mesolimbic DA as predictive Hebbian learning / TD RPE
- Gershman, Pesaran & Daw (2009) — human neuroimaging evidence for effector-specific (lateralised) value signals
- Syed et al. (2016) — 'go/no-go' DA movement selectivity in NAcc
- da Silva et al. (2018) — DA activity gates and invigorates movement initiation
- Howe & Dombeck (2016) — rapid DA signals during locomotion
- Niv et al. (2007) — tonic DA, opportunity costs, and response vigour
- Berke (2018) — review of dopamine function and movement
- Collins & Frank (2014) — opponent actor learning (OpAL) model of DA in striatum

**Named models or frameworks**:
- Q-learning mixed-effects model (trial-by-trial RL model of behaviour)
- Actor-critic framework (Barto et al., 1983)
- Advantage learning (Baird, 1994)
- Temporal difference (TD) RPE
- Contralateral value model vs. chosen value model (competing hypotheses introduced and tested here)

**Brain regions**:
- VTA/SNc (ventral tegmental area / substantia nigra pars compacta)
- Dorsomedial striatum (DMS)
- Nucleus accumbens (NAcc / ventral striatum)
- Basal ganglia direct and indirect pathways

**Keywords**:
- dopamine reward prediction error
- movement selectivity dopamine
- dorsomedial striatum
- fiber photometry GCaMP6f
- action-specific RPE
- chosen value vs contralateral value
- Q-learning mixed-effects model
- probabilistic reversal learning
- DA projection heterogeneity
- contralateral choice selectivity
- actor-critic basal ganglia
- VTA dopamine terminals
