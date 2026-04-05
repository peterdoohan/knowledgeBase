---
source_file: kravitz2010_basal_ganglia_optogenetic.md
title: "Regulation of parkinsonian motor behaviours by optogenetic control of basal ganglia circuitry"
authors: Alexxai V. Kravitz, Benjamin S. Freeze, Philip R. L. Parker, Kenneth Kay, Myo T. Thwin, Karl Deisseroth, Anatol C. Kreitzer
year: 2010
journal: Nature
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Selective optogenetic activation of direct- and indirect-pathway striatal neurons produces opposing motor effects in mice — direct-pathway activation increases locomotion and rescues parkinsonian deficits, while indirect-pathway activation induces a parkinsonian-like state.

---

### Background & motivation

The basal ganglia direct and indirect pathways have long been proposed to exert opposing influences on motor function: the direct pathway facilitates movement and the indirect pathway suppresses it (the classical Albin/DeLong model). However, this hypothesis had never been directly tested in behaving animals, because no prior technique allowed pathway-specific manipulation in vivo. Newer anatomical and functional data had begun to question the strict dichotomy, making an empirical test particularly timely. This paper fills the gap by using cell-type-specific optogenetics to causally test whether selectively driving each pathway produces the motor effects the classical model predicts.

---

### Methods

- **Subjects**: BAC transgenic mice expressing Cre recombinase under D1 (direct pathway) or D2 (indirect pathway) receptor regulatory elements.
- **Viral targeting**: Cre-dependent AAV1 encoding a double-floxed inverted ChR2–YFP fusion (DIO construct) injected into dorsomedial striatum, restricting ChR2 expression to direct- (D1-ChR2) or indirect-pathway (D2-ChR2) medium spiny neurons (MSNs).
- **Expression validation**: Immunostaining for MSN marker DARPP-32, interneuron markers (ChAT, PV, NPY), and axonal projection targets confirmed >90% specificity to MSNs and correct pathway anatomy; <5% interneuron co-labelling.
- **Electrophysiology**: In vitro whole-cell patch-clamp confirmed ChR2 did not alter MSN passive or active properties; in vivo optrode recordings (silicon probe + integrated optical fibre) confirmed light-evoked firing in striatum and appropriate downstream effects in SNr under anaesthesia.
- **Behavioural testing**: Bilateral fibre-optic illumination (473 nm, 1 mW per tip, 30-s average on/60-s off) in awake, freely moving mice; behaviour tracked with video (ETHOVISION). Measures: time ambulatory, freezing, fine movement, ambulation bout frequency/duration/velocity, gait (DigiGait treadmill system).
- **Parkinson's disease model**: Bilateral 6-OHDA injection into dorsomedial striatum in D1-ChR2 mice; motor behaviour assessed pre- and post-lesion, with and without direct-pathway optical activation.
- **Controls**: Cre-dependent YFP-only (no ChR2) mice confirmed illumination alone had no behavioural effect.

---

### Key findings

- **Indirect-pathway activation** (D2-ChR2, bilateral) produced a parkinsonian motor state: increased freezing frequency and duration, decreased ambulation frequency and duration, decreased ambulation velocity, and decreased fine-movement velocity (all P < 0.05).
- **Direct-pathway activation** (D1-ChR2, bilateral) had the opposite effect: decreased freezing, increased locomotor initiations, increased ambulatory bout duration, and more vigorous fine movements (all P < 0.05).
- **Unilateral stimulation**: direct-pathway activation produced contraversive rotations; indirect-pathway activation produced ipsiversive rotations — consistent with classical model predictions and mimicking dopamine-depletion-induced rotation.
- **Circuit-level validation**: Direct-pathway activation inhibited SNr neurons (8.6 ± 3.0% of baseline firing rate, n = 8); indirect-pathway activation excited SNr neurons (162 ± 19% of baseline, n = 4), consistent with the classical model.
- **Gait was unaffected** by direct or indirect pathway activation (no significant change in stride length, stance width, stride frequency, etc.), indicating the pathways regulate the pattern of locomotion rather than locomotor coordination per se.
- **6-OHDA rescue**: Direct-pathway activation in mice with near-total dopamine depletion of dorsomedial striatum (TH intensity reduced to 4 ± 12% of control) completely restored motor behaviour to pre-lesion levels — bradykinesia, freezing frequency/duration, and locomotor initiation were all rescued (P < 0.05 for all measures).

---

### Computational framework

Not applicable. The paper does not employ a formal computational framework. The results bear directly on reinforcement learning and action-selection models of basal ganglia function (e.g., actor-critic models with opponent direct/indirect pathway contributions), and constrain the direction of causal influence each pathway exerts on motor output. They are most immediately relevant to the classical "rate model" of basal ganglia function (Albin/DeLong), which the data largely support.

---

### Prevailing model of the system under study

The classical model of basal ganglia function (Albin et al., 1989; DeLong, 1990; Alexander & Crutcher, 1990) holds that the striatum gives rise to two parallel output pathways: the direct pathway (striatonigral, expressing D1 receptors) disinhibits the thalamus and facilitates movement; the indirect pathway (striatopallidal, expressing D2 receptors) ultimately inhibits the thalamus and suppresses movement. Dopamine, acting on D1 receptors, reinforces direct-pathway activity, while acting on D2 receptors it inhibits indirect-pathway activity — so dopamine loss in Parkinson's disease was predicted to tip the balance toward indirect-pathway overactivation and motor suppression. As the authors note, this model had never been directly tested with cell-type-specific manipulations in behaving animals; prior pharmacological and lesion approaches lacked the specificity to isolate each pathway independently. More recent anatomical work (noted by the authors as refs 8–10) had begun to question strict pathway segregation and the cleanness of the opposition.

---

### What this paper contributes

The results provide the first direct causal evidence that the direct and indirect pathways have opposing, pathway-specific effects on motor behaviour that match the classical model's predictions. The paper establishes: (1) indirect-pathway activation alone is sufficient to produce a full parkinsonian motor syndrome (bradykinesia, freezing, reduced locomotor initiation); (2) direct-pathway activation alone promotes locomotion and reduces freezing; (3) enhancing direct-pathway activity can fully rescue a constellation of motor deficits in a dopamine-depletion model of Parkinson's disease. This last finding was unexpected and identifies direct-pathway augmentation as a potential therapeutic strategy — complementary to, and potentially more specific than, existing approaches (deep-brain stimulation, subthalamic lesions) that target the indirect pathway. The work also resolves the long-standing empirical gap by demonstrating that strict pathway-level separation is sufficient to bidirectionally control motor state, providing the strongest causal support yet for the classical model.

---

### Brain regions & systems

- **Dorsomedial striatum** — site of ChR2 viral injection and optical stimulation; primary locus of pathway-specific manipulation; proposed to be involved in earlier stages of motor planning.
- **Globus pallidus (GP)** — canonical projection target of indirect-pathway MSNs (D2-Cre axons confirmed to project here); part of the indirect-pathway circuit.
- **Substantia nigra pars reticulata (SNr)** — main basal ganglia output nucleus; electrophysiologically recorded during striatal stimulation to confirm circuit-level effects (inhibited by direct-pathway activation, excited by indirect-pathway activation).
- **Entopeduncular nucleus** — canonical projection target of direct-pathway MSNs; confirmed by anatomical tracing of D1-Cre ChR2–YFP fibres.
- **Substantia nigra pars compacta (SNc)** — confirmed to be free of ChR2–YFP-labelled afferent fibres (ruling out inadvertent dopaminergic neuron activation).

---

### Mechanistic insight

This paper meets both criteria for the high bar.

**Phenomenon**: Bidirectional regulation of motor behaviour (locomotion, freezing, bradykinesia) by basal ganglia circuitry, and the motor deficits of Parkinson's disease.

**Computational level**: The brain is selecting and initiating motor actions from a repertoire. The basal ganglia are proposed to gate action — facilitating selected actions and suppressing competing ones.

**Algorithmic level**: Two parallel striatal output streams (direct and indirect) with opposing effects on downstream basal ganglia nuclei implement the gating computation. Direct-pathway activity disinhibits motor programs by suppressing SNr output; indirect-pathway activity reinforces motor suppression by exciting SNr output. The paper demonstrates this opposition is causal and pathway-specific: selectively driving either stream is sufficient to shift the animal's motor state continuously and reversibly.

**Implementational level**: The paper provides detailed implementation-level specificity — the relevant cell types are D1-receptor-expressing and D2-receptor-expressing medium spiny neurons; their downstream connectivity (D1-MSNs → SNr/entopeduncular nucleus; D2-MSNs → GP) is anatomically confirmed; SNr neuron firing is shown to be modulated in the predicted direction by each pathway. The 6-OHDA rescue experiment further shows that dopamine loss's motor consequences can be bypassed by directly augmenting D1-MSN activity, linking the neuromodulatory system (dopamine) to pathway-level activity changes.

**Bonus**: The paper explicitly identifies cell types (D1-MSNs and D2-MSNs), connectivity targets, a key neuromodulator (dopamine), and the specific basal ganglia output nucleus (SNr) as the site where pathway-level signals converge to regulate downstream motor circuits.

---

### Limitations & open questions

- The study targeted dorsomedial striatum specifically; whether the same bidirectional logic applies across other striatal subregions (e.g., dorsolateral, ventral striatum) remains to be established.
- Optical stimulation parameters (constant illumination, 1 mW, ~30-s trains) may not replicate natural activity patterns of MSNs (which fire at low rates and in sparse, context-dependent bursts); whether phasic or naturalistic stimulation patterns yield the same results is unclear.
- Anaesthetised in vivo recordings of MSN firing rates (~0.03–0.06 Hz baseline) were about tenfold lower than in awake animals, complicating precise quantification of stimulation efficacy in the behaving state.
- The 6-OHDA model involves near-complete dopamine depletion in one striatal subregion; generalisability to more graded dopamine loss, or to models of Parkinson's disease with broader dopamine-system pathology, requires future study.
- The authors note that a comprehensive sensorimotor battery is needed to fully characterise the role of each pathway; non-motor aspects of basal ganglia function (e.g., reward learning, habit formation) were not assessed.
- No data are presented on the long-term stability of direct-pathway stimulation as a rescue strategy, nor on potential adverse effects of sustained pathway activation.

---

### Connections & keywords

**Key citations**:
- Albin, Young & Penney (1989) — original formulation of the classical model of basal ganglia disorders
- DeLong (1990) — primate model of movement disorders, basis of rate model
- Alexander & Crutcher (1990) — functional architecture of basal ganglia circuits
- Boyden et al. (2005) — original channelrhodopsin-2 optogenetics paper
- Gong et al. (2007) — BAC transgenic Cre mouse lines used here
- Kreitzer & Malenka (2007) — prior work on endocannabinoid-mediated rescue of motor deficits in Parkinson's disease models

**Named models or frameworks**:
- Classical (Albin/DeLong) rate model of basal ganglia function
- Cre-dependent DIO (double-floxed inverted open reading frame) viral strategy
- 6-OHDA mouse model of Parkinson's disease

**Brain regions**:
- Dorsomedial striatum
- Globus pallidus
- Substantia nigra pars reticulata (SNr)
- Entopeduncular nucleus
- Substantia nigra pars compacta (SNc)

**Keywords**:
- optogenetics, channelrhodopsin-2
- basal ganglia direct pathway, basal ganglia indirect pathway
- medium spiny neurons, D1-MSN, D2-MSN
- striatum, dorsomedial striatum
- Parkinson's disease, 6-OHDA model
- bradykinesia, freezing, locomotor initiation
- cell-type-specific circuit manipulation
- deep-brain stimulation (therapeutic comparison)
