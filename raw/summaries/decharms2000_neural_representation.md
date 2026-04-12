---
source_file: "decharms2000_neural_representation.md"
paper_id: "decharms2000_neural_representation"
title: "Neural Representation and the Cortical Code"
authors: "R. Christopher deCharms, Anthony Zador"
year: 2000
journal: "Annual Review of Neuroscience"
paper_type: "review"
contribution_type: "review"
methods: ["lesion"]
brain_regions: ["prefrontal_cortex", "visual_cortex", "primary_auditory_cortex"]
keywords: ["neural", "representation", "cortical", "code"]
---

### One-line summary

Neural representation in the cerebral cortex requires both content (the information a signal carries about inputs) and function (the effect that signal has on cognition and behaviour), and cortical coding may operate through rate coding, temporal coding, and/or coordinated population coding.

---

### Background & motivation

Understanding how the brain encodes information is a central problem in neuroscience: neurons generate spike trains, but the rules by which these trains carry meaningful signals remain disputed. A large literature existed on single cortical areas and individual sensory modalities, but no synthesis of general coding principles across the cortex had been attempted. This review fills that gap by integrating work on single-neuron firing rates, temporal spike patterns, population-level independent coding, and coordinated (synchrony-based) coding, and by explicitly linking neural signals to cognition and behaviour.

---

### Methods

This is a narrative review covering the theoretical and empirical literature on cortical coding as of 2000. Scope and approach:

- Covers coding mechanisms across multiple primary cortical areas: primary visual cortex (V1), primary auditory cortex (AI), primary somatosensory cortex (SI), extrastriate cortex (MT, IT), and prefrontal/motor cortex.
- Reviews both single-neuron approaches (tuning curves, stimulus reconstruction via reverse correlation) and population approaches (population vector, synchrony/oscillation studies).
- Includes reanalysis of firing-rate distribution data from V1, AI, SI, and IT from previously published datasets (new analysis presented in the paper).
- Discusses binocular rivalry, microstimulation, and cortical lesion/stimulation experiments as tools for linking neural signals to perception and behaviour.
- No formal inclusion/exclusion criteria are stated; the synthesis is narrative and selective.

---

### Key findings

- Neural representation is defined by two properties: **content** (the information the signal carries about inputs) and **function** (the causal effect on behaviour or cognition). Neither alone is sufficient.
- The distinction between **rate coding** and **temporal coding** is a matter of timescale rather than category: as bin size decreases, rate measurement converges on spike-timing measurement.
- MT neurons can encode information about time-varying stimuli at rates ~20 times higher using spike timing than using mean rate alone (from Buracas et al 1998).
- Cortical neurons in V1, AI, and SI show broadly similar spatiotemporal feature selectivity structures when scaled by perceptual discriminative capacity; feature-extraction timescales are largely overlapping (~25–150 ms).
- Populations on the order of ~100,000 primary cortical neurons are activated by any individual suprathreshold stimulus component.
- In primary auditory cortex, neurons can show **stimulus-frequency-specific changes in synchrony** in the absence of changes in mean firing rate, suggesting coordinated coding can operate independently of rate modulation (deCharms & Merzenich 1996).
- Cortical neurons fire highly irregular spike trains; recent evidence suggests this irregularity arises from temporally coordinated (synchronous) input barrages rather than from intrinsic spike-generating mechanisms.
- Single-neuron signals in area MT correlate with individual perceptual decisions in visual motion discrimination tasks (Britten et al 1992, 1996).
- Cortical microstimulation can causally substitute for tactile percepts in discrimination tasks (Romo et al 1998), establishing a causal link between neural and mental representations.
- Binocular rivalry data (Logothetis and colleagues) show that firing rates in higher visual areas (especially IT cortex) track the animal's subjective percept rather than the physical stimulus, and that rivalry is a competition between neural representations rather than between eyes.

---

### Computational framework

The paper does not develop a single novel computational framework; rather, it reviews and contrasts several:

**Rate coding**: The mean firing rate of a neuron encodes stimulus features. The neuron is modelled as a noisy integrator whose output is proportional to a stimulus parameter. Decoding is spike counting over a time window.

**Temporal coding**: Spike-timing precision beyond mean rate carries additional information. Key assumption: the relevant timescale for decoding is shorter than a typical interspike interval.

**Independent population coding**: Each neuron votes independently for a feature value; the population vector (Georgopoulos) aggregates these independent signals. Assumes no meaningful inter-neuronal correlation beyond what is implied by shared tuning.

**Coordinated population coding**: Information is carried in the relationships (e.g. synchrony, correlated firing) among multiple neurons, not derivable from individual cells considered separately. Key claim: coordinated inputs explain the irregularity of cortical spike trains.

The paper proposes a formal definition of representation as a signal that is statistically related to both the input and output of an information transformation — a three-way relational structure — but notes that no widely accepted statistical measure for this exists at the time of writing.

---

### Prevailing model of the system under study

The dominant model at the time was that cortical representation is primarily a function of single-neuron mean firing rates (rate coding). Each neuron has a tuning curve that specifies its preferred stimulus, and the population represents a stimulus by the pattern of firing rates across many independently operating cells. Population vector decoding (motor cortex) exemplified how independent neuronal votes could reconstruct a high-dimensional variable. The temporal structure of spike trains beyond mean rate was considered a secondary and contentious issue. The cerebral cortex was also typically studied in isolation from behaviour, or with only indirect behavioural validation.

---

### What this paper contributes

The review makes several clarifying and synthesising contributions:

1. It provides a unified conceptual framework — representation requires both content and function — that cuts across sensory, motor, and cognitive domains and links neurophysiology to perception and behaviour.
2. It argues that rate coding vs temporal coding is not a categorical distinction but a timescale choice, dissolving a spurious debate.
3. It synthesises cross-cortical evidence that primary cortical areas share broadly similar spatiotemporal coding properties, suggesting common principles rather than area-specific mechanisms.
4. It brings coordinated coding (synchrony) into the mainstream discussion and presents novel evidence that synchrony changes can occur independently of rate changes in auditory cortex.
5. It draws an explicit bridge between neural representations and subjective mental representations through parallel measurement of content and function, using binocular rivalry and microstimulation data as concrete examples of this link.

The review identifies the key unresolved question: whether information is primarily in pooled independent signals or substantially in inter-neuronal coordination, and acknowledges that no canonical statistical framework for measuring three-way (input-neuron-output) representation existed at the time.

---

### Brain regions & systems

- **Primary visual cortex (V1)** — used as the canonical example for rate and temporal coding, tuning curves, and reverse correlation; also implicated in mental imagery activation (Kosslyn et al 1995).
- **Extrastriate visual cortex, area MT** — central example for linking single-neuron signals to individual perceptual decisions (motion discrimination); also for temporal coding of stimulus temporal structure.
- **Inferotemporal cortex (IT)** — reviewed for binocular rivalry data showing firing tracks subjective percept; also for complex object representation.
- **Primary auditory cortex (AI)** — key site for coordinated coding evidence (synchrony without rate change; deCharms & Merzenich 1996); reverse correlation methods applied here.
- **Primary somatosensory cortex (SI, area 3b)** — used for cross-cortical comparison of spatiotemporal feature selectivity and for linking neural signals to tactile perceptual performance (Mountcastle).
- **Primary motor cortex** — reviewed for population vector model of movement direction coding (Georgopoulos).
- **Prefrontal and frontal cortex** — reviewed for evidence of coordinated coding (synfire chains, synchrony changes correlated with behaviour: Vaadia et al 1995, Riehle et al 1997).

---

### Mechanistic insight

The paper partially meets the bar. It presents an algorithmic proposal (coordinated population coding, specifically synchrony-based coding) and cites neural data bearing on it (auditory cortex synchrony changes without rate changes; dual whole-cell recordings showing synchronous input barrages; optical imaging showing comodulated activity). However, as the authors themselves acknowledge, the auditory synchrony data lack a direct link to behavioural function in awake animals, and attempts to replicate the rate-control experiment in behaving animals produced confounded results. The paper therefore does not cleanly satisfy the second criterion (neural data specifically supporting the coordinated coding algorithm over alternatives).

At the level of content-function linkage in MT, the paper does meet the bar for a different, narrower claim:

- **Computational**: the brain must transform sensory inputs into perceptual decisions.
- **Algorithmic**: single MT neurons carry independent signals whose content (motion direction tuning) tracks the animal's perceptual report on individual trials.
- **Implementational**: the paper does not address cell types, connectivity, or biophysical mechanisms.

Overall: the mechanistic insight is strongest for rate-based single-neuron coding linked to perceptual decisions (MT), but the more novel coordinated coding proposal is supported by neural data that fall short of direct behavioural validation in awake subjects.

---

### Limitations & open questions

- The key unresolved question left open: is information in cortical populations primarily carried by independent signals or by inter-neuronal coordination, and how should we measure this?
- No widely accepted three-way statistical measure of representation (linking input, neural signal, and output simultaneously) existed at time of writing.
- Evidence for coordinated coding without rate changes (auditory cortex) was obtained only in anesthetized animals; replication in awake behaving animals was not achieved.
- The review does not address sub-cortical contributions to representation, plasticity mechanisms in depth, or development.
- The question of what subjective experience is for — its functional necessity and adaptive value — is raised but left unanswered.
- The relationship between independent and coordinated coding is acknowledged as often ambiguous in practice, with no clear criterion for distinguishing them in data from awake animals.

---

### Connections & keywords

**Key citations**:
- Georgopoulos et al 1986 (population vector, motor cortex)
- Britten et al 1992, 1996 (MT neurons and perceptual decisions)
- deCharms & Merzenich 1996 (coordinated coding in auditory cortex)
- Logothetis and colleagues (binocular rivalry series)
- Buracas et al 1998 (temporal coding in MT)
- Romo et al 1998 (microstimulation and tactile percepts)
- Stevens & Zador 1998 (synchronous input barrages and spike irregularity)
- Lampl et al 1999 (synchronous membrane potential fluctuations)
- Arieli et al 1996 (ongoing activity and cortical variability)
- Softky & Koch 1993 (irregular firing conundrum)
- Shadlen & Newsome 1994, 1998 (balanced excitation-inhibition; independent coding)
- Singer & Gray 1995 (gamma oscillations and binding)

**Named models or frameworks**:
- Rate-coding hypothesis (Adrian 1928)
- Temporal-coding hypothesis
- Population vector model (Georgopoulos)
- Independent population coding
- Coordinated population coding
- Synfire chains (Abeles 1991)
- Reverse correlation / spike-triggered average
- Stimulus reconstruction / decoding framework

**Brain regions**:
- Primary visual cortex (V1)
- Middle temporal area (MT)
- Inferotemporal cortex (IT)
- Primary auditory cortex (AI)
- Primary somatosensory cortex (SI, area 3b)
- Primary motor cortex
- Prefrontal cortex

**Keywords**:
- neural representation
- cortical code
- rate coding
- temporal coding
- population coding
- coordinated coding
- neural synchrony
- reverse correlation
- spike irregularity
- content and function of representation
- binocular rivalry
- perceptual decision making
