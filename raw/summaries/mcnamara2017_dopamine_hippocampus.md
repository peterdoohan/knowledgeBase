---
source_file: mcnamara2017_dopamine_hippocampus.md
paper_id: mcnamara2017_dopamine_hippocampus
title: "Two sources of dopamine for the hippocampus"
authors:
  - "Colin G. McNamara"
  - "David Dupret"
year: 2017
journal: "Trends in Neurosciences"
paper_type: review
contribution_type: theoretical
species:
  - mouse
methods:
  - optogenetics
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - prefrontal_cortex
  - ventral_tegmental_area
frameworks:
  - reinforcement_learning
keywords:
  - dopamine_co_release_from_noradrenergic_terminals
  - locus_coeruleus_hippocampus_dopamine
  - hippocampal_memory_consolidation
  - novelty_dependent_plasticity
  - d1_d5_receptor_dependent_ltp
  - vta_hippocampus_projection
  - optogenetic_circuit_dissection
  - catecholamine_co_transmission
  - spatial_memory_persistence
  - hippocampal_offline_reactivation
  - dual_dopaminergic_pathways
  - neuromodulatory_gating_of_plasticity
  - two
  - sources
  - dopamine
  - hippocampus
---

### One-line summary

Noradrenergic fibres from the locus coeruleus release dopamine in the hippocampus and contribute to novelty-related memory consolidation, constituting a second dopaminergic input alongside the previously established ventral tegmental area projection.

---

### Background & motivation

Dopaminergic signalling in the hippocampus is known to modulate synaptic plasticity and support the encoding of novel experiences into long-term memory. The ventral tegmental area (VTA) was long considered the sole source of this hippocampal dopamine, based on pharmacological manipulation of D1/D5 receptors and rodent behavioural studies. Two 2016 studies (Takeuchi et al. and Kempadoo et al.) challenged this assumption by demonstrating that locus coeruleus (LC) noradrenergic fibres also release dopamine in the hippocampus, raising the question of how these two inputs differ functionally.

---

### Methods

This is a narrative spotlight review synthesising two primary empirical studies:

- **Takeuchi et al. (2016)**: mice performed a spatial reward-location learning task; optogenetic burst activation of LC neurons was applied 30 minutes post-encoding; pharmacological dissection used intra-hippocampal D1/D5 antagonist (SCH23390) and beta-adrenoceptor antagonist (propranolol); optogenetic activation of LC-TH+ fibres in hippocampal slice preparations assessed synaptic plasticity.
- **Kempadoo et al. (2016)**: high-performance liquid chromatography measured catecholamine release from photostimulated LC-TH+ axons in hippocampal slice preparations; optogenetic activation during spatial object recognition and Barnes Maze tasks tested learning effects; receptor dependence assessed with D1/D5 and beta-adrenergic antagonists.
- The authors also reference a prior study (McNamara et al. 2014) showing VTA-TH+ stimulation during learning enhances memory retention and hippocampal reactivation, for comparison.
- Synthesis is narrative; no formal meta-analytic or quantitative inclusion criteria are described.

---

### Key findings

- Burst optogenetic activation of LC neurons 30 minutes after encoding extended spatial memory persistence from 1 hour to 24 hours in mice, mimicking the effect of novelty exposure.
- This memory enhancement by post-encoding LC activation required hippocampal D1/D5 receptors but not beta-adrenoceptors, implying dopamine (not noradrenaline) as the effective transmitter.
- HPLC measurements confirmed that photostimulation of LC-TH+ hippocampal axons released dopamine (at approximately one-tenth the concentration of noradrenaline released from the same terminals, representing a near fourfold increase from baseline).
- LC-TH+ fibres innervate the dorsal hippocampus at approximately 4.5 times the density of VTA-TH+ fibres.
- VTA-TH+ stimulation applied during (not after) learning enhanced memory retention and promoted offline hippocampal reactivation of learning-associated firing patterns; the same protocol failed to enhance memory for earlier events.
- LC-TH+ activation produced temporally broad modulation (retroactive enhancement), consistent with LC's role in regulating alertness; VTA-TH+ activation produced temporally precise, concurrent learning-dependent modulation, consistent with value-based instruction.
- Both VTA and LC catecholaminergic neurons showed sustained firing increases during spatial novelty exposure in the absence of discrete reward.

---

### Computational framework

Not applicable in a strict formal sense. The paper does not employ a computational model or mathematical framework. However, it implicitly frames the two dopaminergic projections in terms of a **reinforcement learning / neuromodulatory gating** perspective: dopamine signals novelty and value to gate hippocampal plasticity. The temporal specificity contrast — LC as a broad, delayed plasticity modulator versus VTA as a precise, concurrent learning signal — maps loosely onto distinctions in RL between general arousal/exploration signals and reward prediction error signals. The results constrain theories of dopaminergic modulation of memory consolidation, particularly models assigning a single source to hippocampal dopamine.

---

### Prevailing model of the system under study

The prevailing model at the time of this paper held that dopaminergic modulation of hippocampal plasticity and novelty-dependent memory consolidation was mediated exclusively by projections from the VTA. This hippocampal-VTA loop model (Lisman and Grace, 2005) proposed that the hippocampus detects novelty and signals the VTA, which in turn releases dopamine back into the hippocampus to gate long-term plasticity. Pharmacological evidence using D1/D5 receptor manipulations was interpreted entirely within this framework, with the sparse VTA dopaminergic innervation of the hippocampus treated as the sole anatomical substrate.

---

### What this paper contributes

This spotlight establishes that the LC is a functionally significant and anatomically dominant source of dopamine in the hippocampus, requiring a revision of the VTA-centric model. Key contributions:

- The LC-VTA duality is now supported by both circuit-level anatomy (fibre density) and direct neurochemical measurement (HPLC).
- The two pathways are functionally dissociable by their temporal relationship to learning: LC modulates plasticity retroactively and broadly (minutes to hours post-encoding), consistent with a general novelty/arousal signal; VTA modulates plasticity concurrently and precisely, consistent with a value-based learning signal.
- Both pathways act through D1/D5 receptors in the hippocampus, suggesting convergent molecular mechanisms despite anatomical and functional differences.
- The paper raises the possibility that VTA fibres may exert targeted effects on specific cell types or synapses, whereas LC fibres produce volume transmission across a wider hippocampal territory.
- Key unresolved question: how LC-TH+ versus VTA-TH+ activation differentially affects hippocampal network dynamics (place cell remapping, offline reactivation, cross-area coordination).

---

### Brain regions & systems

- **Hippocampus (dorsal, CA3-CA1)** — primary site of dopaminergic modulation; locus of synaptic plasticity changes underlying spatial memory encoding and consolidation.
- **Locus coeruleus (LC)** — noradrenergic nucleus newly identified as a source of hippocampal dopamine release; LC-TH+ fibres more densely innervate dorsal hippocampus than VTA fibres.
- **Ventral tegmental area (VTA)** — canonical source of hippocampal dopamine; sparser innervation; associated with value-based, concurrent learning signals and enhancement of hippocampal offline reactivation.
- **Prefrontal cortex** — implicated in cross-area coordination of learning-related replay (referenced via Benchenane et al. 2010 and Peyrache et al. 2009), relevant to the broader network context of VTA-TH+ modulation.

---

### Mechanistic insight

The paper partially meets the bar. It reviews empirical data (optogenetics, pharmacology, HPLC) that specifically support dopamine release from LC noradrenergic terminals as the mechanistic basis for novelty-enhanced hippocampal memory, providing evidence at the algorithmic and implementational levels.

- **Computational**: the brain must selectively strengthen memories for novel, potentially important events. Dopaminergic gating of hippocampal plasticity implements this prioritisation.
- **Algorithmic**: post-encoding LC activation (triggered by novelty or arousal) releases dopamine in the hippocampus, boosting CA3-CA1 synaptic plasticity via D1/D5 receptors. This is dissociable from adrenergic signalling and from VTA input. The VTA pathway operates during encoding to enhance concurrent representations and their offline reactivation.
- **Implementational**: LC-TH+ noradrenergic axons co-release dopamine (at ~10% of noradrenaline concentration) into the dorsal hippocampus. VTA-TH+ dopaminergic fibres provide sparser but potentially more targeted innervation, possibly selective for particular interneurons or synaptic sites.

**Bonus**: the paper explicitly addresses neuromodulator identity (dopamine vs. noradrenaline co-release from the same LC terminals), fibre density differences, and receptor subtype specificity (D1/D5 vs. beta-adrenergic), making the implementational level unusually well-characterised for a spotlight piece. The main gap is that the effect of LC-TH+ activation on hippocampal network dynamics (firing patterns, reactivation) remains unmeasured.

---

### Limitations & open questions

- The effect of LC-TH+ activation on hippocampal firing dynamics (place cell activity, theta oscillations, offline replay) has not been directly measured and compared to VTA-TH+ effects.
- The relative contribution of co-released dopamine versus noradrenaline from LC fibres under naturalistic (non-optogenetic) conditions is unknown.
- Whether VTA-TH+ fibres selectively target specific hippocampal cell types or synapses remains to be determined.
- The possibility that dopamine co-release from LC fibres is an artefact of optogenetic supraphysiological stimulation (rather than a physiological mode of signalling) is not fully ruled out, though the behavioural effects are consistent with a functional role.
- The functional significance of dopamine co-release from LC fibres in the ventral hippocampus and in non-spatial memory tasks is unexplored.
- Whether the two dopaminergic sources act independently or interact (e.g. through receptor competition or mutual modulation) is unresolved.

---

### Connections & keywords

**Key citations**:
- Lisman, J.E. and Grace, A.A. (2005) — hippocampal-VTA loop model
- Takeuchi, T. et al. (2016) — LC optogenetics and spatial memory consolidation
- Kempadoo, K.A. et al. (2016) — HPLC measurement of LC dopamine release; spatial learning
- McNamara, C.G. et al. (2014) — VTA dopaminergic neurons, hippocampal reactivation, spatial memory persistence
- Bethus, I. et al. (2010) — dopamine and hippocampal NMDA-dependent memory persistence
- Benchenane, K. et al. (2010) — hippocampal-prefrontal theta coherence and learning
- Gomperts, S.N. et al. (2015) — VTA neuron coordination with hippocampal reactivation

**Named models or frameworks**:
- Hippocampal-VTA loop (Lisman & Grace, 2005)
- Optogenetic activation of LC-TH+ and VTA-TH+ fibres
- Crossword maze and Barnes Maze spatial learning paradigms
- Spatial object recognition task

**Brain regions**:
- Hippocampus (dorsal, CA3-CA1)
- Locus coeruleus (LC)
- Ventral tegmental area (VTA)
- Prefrontal cortex

**Keywords**:
- dopamine co-release from noradrenergic terminals
- locus coeruleus hippocampus dopamine
- hippocampal memory consolidation
- novelty-dependent plasticity
- D1/D5 receptor-dependent LTP
- VTA-hippocampus projection
- optogenetic circuit dissection
- catecholamine co-transmission
- spatial memory persistence
- hippocampal offline reactivation
- dual dopaminergic pathways
- neuromodulatory gating of plasticity
