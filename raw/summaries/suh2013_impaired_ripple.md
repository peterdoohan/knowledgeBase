---
source_file: "suh2013_impaired_ripple.md"
paper_id: "suh2013_impaired_ripple"
title: "Impaired Hippocampal Ripple-Associated Replay in a Mouse Model of Schizophrenia"
authors: "Junghyup Suh, David J. Foster, Heydar Davoudi, Matthew A. Wilson, Susumu Tonegawa"
year: 2013
journal: "Neuron"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
tasks: ["linear_track"]
methods: ["electrophysiology", "tetrode_recording"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "medial_entorhinal_cortex"]
keywords: ["impaired", "hippocampal", "ripple", "associated", "replay", "mouse", "model", "schizophrenia"]
---

### One-line summary

Calcineurin knockout mice, a model of schizophrenia, show normal place cell firing during exploration but exhibit 2.5-fold increased sharp-wave ripple abundance and completely abolished sequential replay of place cell sequences during rest.

---

### Background & motivation

Cognitive symptoms of schizophrenia are thought to result from impairments in neural circuit information processing. The calcineurin knockout mouse model exhibits behavioral and cognitive abnormalities recapitulating schizophrenia symptoms, including deficits in working memory and latent inhibition. The forebrain-specific knockout of calcineurin (a synaptic plasticity-mediating phosphatase) causes a shift in synaptic plasticity toward potentiation (reduced LTD, enhanced LTP). This study aimed to investigate how this molecular dysfunction translates to disrupted information processing in hippocampal circuits.

---

### Methods

- **Subjects**: 7 calcineurin knockout (KO) mice and 5 littermate control (CT) mice
- **Recording**: High-density extracellular electrophysiology using 6 independently adjustable tetrodes targeted to dorsal CA1 hippocampus
- **Behavior**: Recordings during RUN epochs (40-60 min on 76×10 cm linear track) bracketed by SLEEP epochs (30-60 min awake rest in sleep box)
- **Analysis**:
  - SWR detection: 100-240 Hz filtered EEG, events >5 SD above mean, >3 ms duration
  - Place field analysis: spatial information, coherence, sparsity, directionality
  - Replay analysis: cross-correlograms of spike pairs during SWRs, correlation between place field distance and temporal spike separation
  - Decimation controls to match spike rates and SWR abundance between groups

---

### Key findings

- **SWR abundance**: 2.5-fold increase in SWR events during awake rest in KO mice (F(1,10) = 31.7, p < 0.001)
- **EEG power**: Significant increase in ripple band power (100-240 Hz) during immobility; no change in gamma (25-80 Hz) or theta (4-12 Hz) power
- **Place fields during RUN**: Normal place cell properties in KO: field size, in-field firing rate, directionality, sparsity, spatial information, and spatial coherence (all NS)
- **Unit activity during SWRs**: 
  - Double the spike rate per SWR in KO (2.56 vs 1.11 spikes/SWR, p < 0.05)
  - Six-fold increase in SWR spikes per second during rest (0.62 vs 0.10 spikes/s, p < 0.0005)
  - Greater participation in SWR events (54.5% vs 35.4% of SWRs, p < 0.001)
- **Burst properties**: Faster burst firing in KO (interspike interval: 4.99 ms vs 5.70 ms, p < 10^-6); increased amplitude attenuation within bursts
- **Replay abolished**: 
  - In CT: significant positive correlation between place field distance and temporal spike separation during SWRs (r = 0.21, p < 0.01)
  - In KO: correlation completely abolished (r = -0.007, NS)
  - "Close" vs "far" cell pairs showed strong difference in CT (p < 0.01) but no difference in KO (NS)
  - Decimation controls confirmed that neither increased spike rate nor increased SWR abundance alone explained the replay deficit

---

### Computational framework

Not applicable. This is an empirical study recording neural activity in behaving animals. However, the results are discussed in the context of synaptic plasticity mechanisms (BCM theory, LTP/LTD balance) and their role in shaping temporal sequences of place cell activity. The findings suggest that excessive/unbalanced potentiation disrupts the precise temporal organization required for replay, supporting models in which synaptic plasticity during running sculpts the sequences that can be subsequently reactivated during rest.

---

### Prevailing model of the system under study

Before this study, the prevailing understanding was that:
1. Sharp-wave ripples (SWRs) during awake rest are associated with sequential reactivation of place cells ("replay") that reflects previous behavioral experience
2. SWR-associated replay is important for memory consolidation, spatial working memory, and planning future behaviors
3. Calcineurin knockout mice exhibit schizophrenia-like behavioral phenotypes and altered synaptic plasticity (shift toward potentiation)
4. The hippocampus is implicated in schizophrenia, with evidence of dysfunction in patients

The gap this paper addressed was whether and how the molecular/cellular changes in calcineurin KO translate to circuit-level information processing deficits in the hippocampus, specifically during SWR-associated replay.

---

### What this paper contributes

This paper establishes that the calcineurin KO mouse model of schizophrenia exhibits a selective disruption in hippocampal information processing during rest periods:

1. **Circuit hyperexcitability**: The 2.5-fold increase in SWR abundance and 6-fold increase in SWR-associated spiking demonstrate elevated excitability in hippocampal circuits during rest, despite normal single-unit responses during active exploration.

2. **Abolished replay**: The complete loss of the normal relationship between place field distance and temporal spike separation during SWRs indicates that sequential reactivation of place cells is fundamentally disrupted. This is not merely a consequence of increased activity (decimation controls confirmed this).

3. **Selective deficit**: The dissociation between normal place fields during RUN and abolished replay during SWRs suggests that complex aspects of place cell activity (temporal sequences during rest) are more critical for memory function than basic place field properties.

4. **Mechanistic insight**: The results suggest that excessive/unbalanced synaptic potentiation (due to calcineurin loss) disrupts the precise temporal organization of spike sequences, providing a link between molecular dysfunction and circuit-level information processing deficits.

---

### Brain regions & systems

- **Hippocampus (CA1)**: Primary recording site. Shows 2.5-fold increase in SWR abundance and 6-fold increase in SWR-associated spiking. Normal place fields during exploration but abolished sequential replay during rest.
- **Hippocampus (CA3)**: Implicated as the source of SWRs and place cell sequences; discussed in context of synaptic plasticity mechanisms that sculpt sequences.
- **Medial entorhinal cortex**: Mentioned in discussion as a region whose layer III projection to CA1 was previously shown to be important for spatial working memory without affecting basic place field properties.
- **Default mode network (DMN)**: Discussed as including hippocampal formation; proposed to be overactive in schizophrenia; calcineurin KO results provide evidence for DMN dysfunction in an animal model.

---

### Mechanistic insight

This paper provides strong mechanistic insight by combining algorithmic and implementational evidence:

**Computational level**: The brain must solve the problem of consolidating spatial memories and supporting working memory through reactivation of previous experiences during rest periods.

**Algorithmic level**: Sequential reactivation (replay) of place cells during SWRs serves as the algorithm for memory consolidation and working memory. The key algorithmic feature is that temporal spike separation during SWRs correlates with spatial distance between place fields (distant place cells fire further apart in time). This temporal structure allows the sequence to encode spatial trajectories.

**Implementational level**: 
- The calcineurin KO demonstrates that normal synaptic plasticity (balanced LTP/LTD) is required for proper replay structure. The shift toward excessive potentiation in KO disrupts the temporal organization of replay.
- The mechanism involves NMDA-receptor dependent plasticity (discussed in context of SWR abundance changes after LTP induction in slice studies).
- The specific biophysical implementation involves calcineurin (a phosphatase) regulating synaptic strength; loss of this regulation leads to hyperexcitability and disorganized replay.

This paper meets the mechanistic insight bar because it links a specific molecular manipulation (calcineurin KO) to a specific circuit-level computation (replay) and provides evidence for how altered synaptic plasticity disrupts the temporal structure of neural sequences.

---

### Limitations & open questions

- **Behavioral correlation**: The study demonstrates impaired replay but does not directly test whether the specific replay deficits cause the working memory impairments previously shown in these mice. The link between replay and behavior is inferred from prior literature.
- **Sleep vs. awake rest**: The study focused on awake rest periods; SWR-associated replay during sleep was not specifically analyzed, though the mechanisms may differ.
- **Directionality of replay**: The study did not distinguish between forward and reverse replay, which may have different functional roles (e.g., consolidation vs. planning).
- **Causality of calcineurin**: While the KO shows deficits, whether restoring calcineurin function would rescue replay was not tested.
- **Generalization to other schizophrenia models**: Whether similar replay deficits exist in other genetic or environmental models of schizophrenia was not addressed.
- **Clinical translation**: Whether patients with schizophrenia show similar hippocampal replay deficits has not been directly tested (invasive recordings would be required).

---

### Connections & keywords

**Key citations**:
- Zeng et al., 2001 (original calcineurin KO characterization)
- Miyakawa et al., 2003 (behavioral phenotypes of calcineurin KO)
- Foster and Wilson, 2006 (awake replay in rats)
- Karlsson and Frank, 2009 (awake replay of remote experiences)
- Jadhav et al., 2012 (SWRs support spatial working memory)
- Buzsáki, 1989 (two-stage model of memory formation)

**Named models or frameworks**:
- BCM theory of synaptic plasticity
- Two-stage model of memory trace formation (Buzsáki)
- Default mode network (DMN) framework
- Sharp-wave ripple (SWR) replay model

**Brain regions**:
- Hippocampus CA1
- Hippocampus CA3
- Medial entorhinal cortex (layer III)
- Default mode network (hippocampal formation, posterior cingulate, retrosplenial cortex, prefrontal cortex)

**Keywords**:
sharp-wave ripples, hippocampal replay, place cells, calcineurin, synaptic plasticity, schizophrenia mouse model, working memory, default mode network, awake rest, sequence reactivation, LTP/LTD balance, NMDA receptors, memory consolidation
