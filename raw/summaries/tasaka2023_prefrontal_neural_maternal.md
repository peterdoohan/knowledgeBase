---
source_file: "tasaka2023_prefrontal_neural_maternal.md"
paper_id: "tasaka2023_prefrontal_neural_maternal"
title: "A Prefrontal Neural Circuit for Maternal Behavioural Learning in Mice"
authors: "Gen-ichi Tasaka, Mitsue Hagihara, Satsuki Irie, Haruna Kobayashi, Kengo Inada, Miho Kihara, Takaya Abe, Kazunari Miyamichi"
year: 2023
journal: "bioRxiv"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
methods: ["calcium_imaging", "optogenetics"]
brain_regions: ["orbitofrontal_cortex", "prelimbic_cortex", "striatum", "ventral_striatum", "ventral_tegmental_area", "thalamus", "mediodorsal_thalamus", "amygdala"]
keywords: ["prefrontal", "neural", "circuit", "maternal", "behavioural", "learning", "mice"]
---

### One-line summary

The orbitofrontal cortex (OFC) contains innately sculpted representations of pup retrieval that are shaped by submedius thalamic input and facilitate ventral tegmental area dopamine neurons to enable efficient maternal behavioural learning.

---

### Background & motivation

Maternal behaviours are crucial for infant survival and can be learned through co-housing with experienced mothers, yet the neural circuit mechanisms underlying this learning remain poorly understood. While prevalent models assume the frontal cortex integrates infant-related sensory signals and controls decision-making, these ideas had not been functionally tested. This study addresses the gap by examining the detailed input/output organization of the orbitofrontal cortex (OFC) in maternal behaviour learning.

---

### Methods

- **Subjects**: Virgin female mice (_Rbp4-Cre_, _Tnnt1-Cre_, _DAT-Cre_ crossed with _Ai162_) at 2–5 months of age
- **Behavioural paradigm**: Alloparental learning through co-housing virgin females with lactating mothers and pups; stages included naïve virgin (NV), co-housed virgin day 1 (CV1), day 2 (CV2), lactating mother (LM), and weaned mother (WM)
- **Calcium imaging**: Chronic microendoscopic Ca2+ imaging (Inscopix nVista) of OFC layer 5 pyramidal neurons (OFC[Rbp4]) and SMT/MD Tnnt1 neurons during freely behaving pup retrieval
- **Viral tracing**: Rabies virus-based retrograde monosynaptic tracing from OFC[Rbp4] neurons; anterograde tracing from SMT and MD using AAV5_CAG-FLEx-TC[b]
- **Manipulations**: Chemogenetic inhibition (hM4Di) of SMT[→OFC] and MD[→OFC] projections; optogenetic inhibition (stGtACR2) of OFC during VTA fiber photometry
- **Analysis**: MIN1PIPE for cell extraction, custom MATLAB scripts for responsive cell identification, AMaSiNe for brain-wide anatomical annotation

---

### Key findings

- **OFC[Rbp4] neurons are necessary for efficient maternal learning**: Ablation of ~30% of OFC[Rbp4] neurons significantly delayed pup retrieval learning, with prolonged latency and reduced number of retrieved pups.

- **Innate and stable representation of pup retrieval**: OFC[Rbp4] neurons showed robust elevated and suppressed responses time-locked to anticipatory, interaction, retrieval onset, and completion phases. These representations were already present in naïve virgin mice (never exposed to pups) and remained stable across all maternality stages (NV → CV1 → CV2 → LM → WM), with individual cells showing comparable activity patterns across days.

- **Selective tuning to social over non-social rewards**: 98 neurons showed elevated responses to pup retrieval vs. 30 to sucrose water. Only 14% of pup retrieval-responsive neurons overlapped with pup odor responses, demonstrating mostly non-overlapping representations of pup retrieval and sensory cues.

- **SMT as a prominent presynaptic partner**: Rabies tracing revealed that SMT (submedius thalamus) and MD (mediodorsal thalamus) provide major thalamic inputs to OFC[Rbp4] neurons. 83% of SMT input cells were Tnnt1-positive. SMT[Tnnt1] neurons projected selectively to ventral/lateral OFC, while MD[Tnnt1] neurons projected more broadly to medial/lateral OFC, AI, PL, amygdala, and ventral striatum.

- **SMT functionally shapes OFC representations**: SMT[Tnnt1] neurons showed similar pup retrieval-locked representations as OFC[Rbp4] neurons. Chemogenetic silencing of SMT[→OFC] projections significantly attenuated elevated responses in OFC[Rbp4] neurons (except interaction responses), whereas MD[→OFC] silencing had minimal effects.

- **OFC facilitates VTA[DA] neurons during early learning**: Optogenetic silencing of OFC significantly reduced pup retrieval-locked Ca2+ activity of VTA dopamine neurons at CV1 and CV2 stages, but not at LM stage. OFC silencing also acutely reduced pup retrieval number specifically at CV1. VTA[DA] response magnitude was inversely correlated with behavioural performance.

---

### Computational framework

The study employs a circuit-level dynamical systems approach to understanding maternal behaviour learning. The core computational framework involves:

1. **Neural population coding**: OFC[Rbp4] neurons encode pup retrieval through distributed population activity, with distinct subpopulations showing elevated or suppressed responses to specific behavioural categories (anticipatory, interaction, onset, completion). Activity heat maps reveal that peak response times tile the entire pup retrieval sequence.

2. **Innate, learning-invariant representations**: Unlike flexible value-coding frameworks typically associated with OFC, the representations of pup retrieval are innately sculpted and stable across learning stages. This suggests an abstract, identity-based coding scheme for behaviourally relevant social objects ("pups") rather than learned value representations.

3. **Hierarchical circuit architecture**: The SMT→OFC→VTA circuit implements a hierarchical control structure where thalamic inputs shape cortical representations, which in turn modulate dopaminergic motivation centers. This represents a top-down cognitive control of motivation through innate cortical representations.

4. **Prediction error signaling**: VTA[DA] neurons show time-locked activity after pup interaction, consistent with a social reward prediction error signal. The OFC's facilitation of VTA[DA] activity during early learning stages suggests the OFC may contribute to computing or conveying prediction errors to guide learning.

---

### Prevailing model of the system under study

The paper establishes several prevailing models that it builds upon or challenges:

1. **Prefrontal cortex as flexible, experience-dependent modulator of social behaviour**: The dominant view in the field holds that the prefrontal cortex (PFC) modulates social behaviours based on flexible coding shaped by prior experiences or learning. This model suggests that PFC representations are plastic and adapt to social context. The authors cite Kingsbury et al. (2020), Zhou et al. (2017), and Padilla-Coreano et al. (2022) as supporting this flexible coding view.

2. **OFC as value-based decision-maker**: The prevailing model of OFC function emphasizes its role in value-based decision-making and reversal learning by representing and updating subjective values. This framework, developed through studies using artificial learning paradigms with mono-modality sensory cues, suggests that OFC representations are dynamic and value-dependent. The authors cite Wallis (2011), Stalnaker et al. (2015), and Izquierdo (2017) as representative of this view.

3. **Subcortical circuits as primary organizers of maternal behaviour**: Previous research has primarily focused on subcortical structures (medial preoptic area, VTA, PVN) as the core neural substrates for maternal behaviour. The frontal cortex was assumed to be an integrator of sensory signals and controller of decision-making, but this role had not been functionally tested. The authors cite Dulac et al. (2014), Wu et al. (2014), Kohl et al. (2018), and Fang et al. (2018) as establishing these subcortical circuit models.

4. **Maternal behaviour representations are experience-dependent**: The prevailing assumption was that efficient maternal behaviour acquisition requires experience-dependent formation of neural representations in higher cognitive areas. The authors contrast their findings with this assumption, showing instead that representations are largely innate.

---

### What this paper contributes

This paper provides several key contributions that refine, challenge, or extend the prevailing models:

1. **Discovery of innate, learning-invariant representations in OFC**: The paper challenges the prevailing view of OFC as a flexible, experience-dependent encoder by demonstrating that OFC[Rbp4] neurons contain stable, innately-tuned representations of pup retrieval that are largely unaffected by learning. These representations are present in naïve virgins (never exposed to pups) and remain consistent across all maternality stages (NV → CV1 → CV2 → LM → WM). Individual cells show comparable activity patterns across days, indicating that learning does not reshape these representations. This finding suggests that for ethologically critical social behaviours, the OFC may implement an abstract, identity-based coding scheme rather than flexible value coding.

2. **Identification of SMT as a key thalamic input shaping cortical representations**: The paper identifies the submedius thalamus (SMT) as a prominent presynaptic partner of OFC[Rbp4] neurons that functionally contributes to pup retrieval representations. Through rabies tracing, the authors provide a quantitative brain-wide presynaptic landscape of OFC[Rbp4] neurons, revealing that SMT provides major thalamic input. They generated novel _Tnnt1-Cre_ mice to selectively target SMT[Tnnt1] neurons, demonstrating that silencing SMT[→OFC] projections attenuates OFC[Rbp4] elevated responses to pup retrieval. This establishes SMT as a functionally important thalamic node for social behaviour representations and provides new genetic access tools for future studies.

3. **Functional linking of OFC to VTA dopamine system during learning**: The paper reveals a functional circuit through which OFC facilitates VTA[DA] neuron activity specifically during early stages of maternal learning (CV1 and CV2), but not after learning is complete (LM). Optogenetic silencing of OFC reduces pup retrieval-locked VTA[DA] activities and impairs behavioural performance at CV1. This demonstrates that the OFC provides top-down cognitive control over motivation centers to enable efficient learning of maternal behaviours. The inverse correlation between VTA[DA] response magnitude and behavioural performance suggests that OFC may contribute to computing or conveying social reward prediction errors during learning.

4. **Selective social tuning of OFC representations**: The paper demonstrates that OFC[Rbp4] neurons are preferentially tuned to social (pup retrieval) over non-social (sucrose water) rewards, with 3x more neurons responding to pup retrieval than to sucrose. Importantly, pup retrieval representations are largely distinct from pup odor representations (only 14% overlap), indicating that OFC encodes the abstract identity of the behavioural object ("pups") rather than fragmented sensory cues. This suggests the OFC utilizes distinct neural coding schemes for behaviourally relevant social objects.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC)** — locus of innate pup retrieval representations; layer 5 pyramidal neurons (OFC[Rbp4]) show elevated and suppressed responses to anticipatory, interaction, onset, and completion phases of pup retrieval; necessary for efficient maternal learning
- **Submedius thalamus (SMT)** — prominent presynaptic partner of OFC[Rbp4] neurons; source of thalamocortical input shaping pup retrieval representations in OFC; SMT[Tnnt1] neurons project selectively to ventral/lateral OFC and show similar retrieval-locked activity patterns
- **Mediodorsal thalamus (MD)** — secondary thalamic input to OFC; MD[Tnnt1] neurons project to medial/lateral OFC, agranular insular cortex, prelimbic cortex, amygdala, and ventral striatum; shows retrieval-locked activity but less functional contribution to OFC representations than SMT
- **Ventral tegmental area (VTA)** — target of OFC projections; VTA dopamine neurons (VTA[DA]) show pup retrieval-locked activity that is facilitated by OFC specifically during early learning stages (CV1, CV2) but not after learning completion (LM)
- **Paraventricular hypothalamic nucleus (PVN)** — source of oxytocin neuron activation that can facilitate maternal behaviours in naïve virgins; pharmacogenetic activation of PVN oxytocin neurons induces pup retrieval and associated OFC neural responses without co-housing
- **Prelimbic cortex (PL)** — receives MD[Tnnt1] projections; part of broader frontal network potentially involved in maternal behaviour (not directly tested)
- **Agranular insular cortex (AI)** — receives MD[Tnnt1] projections; part of broader cortical network

---

### Mechanistic insight

This paper partially meets the bar for mechanistic insight. The paper provides clear evidence for a circuit mechanism (SMT→OFC→VTA) that supports maternal behavioural learning, with neural data specifically supporting the role of the SMT→OFC connection in shaping cortical representations. However, the paper does not formalize a specific algorithm for how information is transformed through this circuit.

**Computational level**: The brain needs to learn maternal behaviours efficiently to ensure infant survival. The problem involves recognizing pups, planning retrieval actions, and updating motivational states based on experience. The OFC provides an abstract, identity-based representation of the pup as a social object that can guide decision-making and motivation.

**Algorithmic level**: The circuit implements a hierarchical processing architecture where thalamic inputs (SMT, MD) provide sensorimotor signals to the OFC, which then modulates dopaminergic motivation centers (VTA). The OFC contains distributed population codes for different phases of pup retrieval (anticipatory, interaction, onset, completion), with distinct neurons showing elevated or suppressed responses. However, the specific representations and transformations are not formalized as a computational algorithm.

**Implementational level**: The circuit is implemented through specific anatomical connections: SMT[Tnnt1] neurons provide thalamocortical input to ventral/lateral OFC; OFC[Rbp4] layer 5 pyramidal neurons encode pup retrieval; OFC projects directly to VTA[DA] neurons. The OFC representations are largely innate and stable across learning, while the functional coupling to VTA changes with learning stage (stronger during early learning, weaker after learning completion).

The paper does not meet the full bar for mechanistic insight because it does not formalize a specific algorithm or computational model that explains how information is transformed through the SMT→OFC→VTA circuit. The findings are descriptive rather than providing a formal mechanistic account of how the circuit computations enable maternal learning.

---

### Limitations & open questions

- The study focused specifically on OFC but did not analyze whether other frontal cortical regions (e.g., mPFC) might have similar functions in parallel with the OFC-SMT network
- Whether distinct OFC[Rbp4] populations can be associated with specific axonal projection targets or gene expression patterns remains unclear; projection-defined or transcriptional-type-specific neurons may encode unique information
- The disparity in behavioural paradigms (pup retrieval in freely moving animals vs. head-fixed odor exposure) may impact sensitivity and character of neural responses; some anticipatory/interaction responses may reflect motor planning disrupted by head-fixation
- The study did not identify which specific behavioural category-locked OFC activities are required for VTA[DA] facilitation; it remains unclear whether OFC activities are acutely required for trial-based learning of pup retrieval
- The functional heterogeneity of VTA[DA] neurons and the specific dopamine subcircuits involved require further investigation; multiple synaptic pathways beyond direct OFC→VTA projections may be significant
- The mechanism by which OFC loses influence on VTA[DA] activities at the LM stage (after learning completion) remains unknown; maternal plasticity in the OFC-to-VTA circuit requires future investigation

---

### Connections & keywords

**Key citations**:
- Dulac et al. (2014) — neural control of maternal and paternal behaviors
- Carcea et al. (2021) — oxytocin neurons enable social transmission of maternal behaviour
- Fang et al. (2018) — hypothalamic-midbrain pathway for maternal behaviors
- Xie et al. (2022) — dopaminergic reward prediction error shapes maternal behavior
- Wu et al. (2014) — galanin neurons in MPOA govern parental behaviour
- Kohl et al. (2018) — functional circuit architecture underlying parental behaviour

**Named models or frameworks**:
- Microendoscopic Ca2+ imaging in freely behaving animals
- Rabies virus-based retrograde monosynaptic tracing
- Alloparental behaviour learning paradigm (co-housing)
- Fiber photometry with optogenetic manipulation
- Projection-specific chemogenetics (hM4Di)

**Brain regions**:
- Orbitofrontal cortex (OFC)
- Submedius thalamus (SMT)
- Mediodorsal thalamus (MD)
- Ventral tegmental area (VTA)
- Paraventricular hypothalamic nucleus (PVN)
- Prelimbic cortex (PL)
- Agranular insular cortex (AI)

**Keywords**:
maternal behaviour, orbitofrontal cortex, submedius thalamus, thalamocortical circuit, ventral tegmental area, dopamine, calcium imaging, microendoscopy, pup retrieval, alloparental learning, social behaviour, innate representation, top-down control, oxytocin, Tnnt1
