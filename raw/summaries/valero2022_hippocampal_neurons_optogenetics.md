---
source_file: valero2022_hippocampal_neurons_optogenetics.md
title: Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics
authors: Manuel Valero, Ipshita Zutshi, Euisik Yoon, György Buzsáki
year: 2022
journal: Science
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Optogenetic probing of subthreshold membrane dynamics in hippocampal CA1 pyramidal neurons reveals state-dependent shifts between balanced and reciprocal E/I modes, unmasking preexisting place fields in non-place cells.

---

### Background & motivation

Understanding how neurons integrate excitatory and inhibitory inputs requires access to subthreshold membrane dynamics, which has been limited to intracellular recordings. Three competing models of E/I integration have been proposed: (1) tuned excitation with blanket inhibition, (2) balanced network where I tracks E changes, and (3) reciprocal network where I decreases with Vm depolarization. The authors developed a method to probe subthreshold dynamics using optogenetic depolarizing pulses in freely moving mice, allowing simultaneous recording from hundreds of neurons.

---

### Methods

- **Subjects**: CamKIIa-Cre::Ai32 mice (n=4)
- **Recording**: Custom micro-LED (mLED) probes with four shanks, three mLEDs per shank; recorded 822 CA1 pyramidal neurons
- **Optogenetic stimulation**: 20-ms light pulses at 0.02-0.1 mW, with randomly variable 20-40 ms offsets (~0.3-0.6 s intervals)
- **Behavioral paradigms**: 
  - Home cage recordings (SPW-Rs)
  - Linear track running with interleaved baseline and stimulation blocks
- **Intracellular validation**: Head-fixed waking mice and anesthetized rats (5 cells each) for Vm manipulation during SPW-Rs
- **Analysis**: Rate gain calculations, spatial decoding, independent component analysis (ICA) for assemblies, Bayesian decoding for replay sequences

---

### Key findings

- **SPW-Rs show balanced network mode**: During sharp-wave ripples, optogenetic depolarization produced decreased firing rate responses (negative gain), consistent with the balanced network model where increased inhibition tracks excitation. This was confirmed by intracellular recordings showing Vm-dependent response decreases.

- **Theta and place fields show reciprocal mode**: During theta oscillations and within place fields, optogenetic depolarization increased firing rate responses (positive gain), consistent with the reciprocal network model where inhibition weakens with depolarization. In-field gain was several-fold higher than out-of-field gain and increased with light intensity.

- **Unmasking preexisting place fields**: 69.3% (289/417) of non-place cells revealed place fields under optogenetic stimulation. These unmasked fields showed "ghost fields" - correlations between sparse baseline spikes and light-induced place field locations. Unmasked place fields had similar features to real place fields (stability, spatial information) and improved spatial decoding accuracy.

- **Assembly organization revealed**: Neuronal assemblies active during SPW-Rs in the home cage predicted spatial overlap and sequences of place fields during track running. This relationship was revealed for non-place cells only when unmasked place fields were included, suggesting preconfigured attractor assemblies.

- **Improved replay decoding**: Including unmasked place fields from non-place cells significantly increased the fraction of SPW-R events with significant virtual track trajectories during replay.

---

### Computational framework

The paper employs three computational models of E/I integration:

1. **Tuned excitation / blanket inhibition**: Inhibition is constant and high; excitatory tuning determines responses. Both Vm and firing rate decrease at more depolarized holding potentials (negative gain).

2. **Balanced network**: Inhibition tracks excitation changes (I ∝ E). Results in decreasing response gain with depolarization (negative gain), matching observations during SPW-Rs.

3. **Reciprocal network**: Inhibition decreases as Vm depolarizes (anti-correlated E/I). Results in increasing response gain with depolarization (positive gain), matching observations during theta and place fields.

The framework treats these as distinct modes of neuronal operation that can shift depending on brain state, with the reciprocal mode favoring signal amplification (pattern completion) and the balanced mode favoring decorrelation and gain control.

---

### Prevailing model of the system under study

The prevailing model of place cell formation assumes spatially uniform inhibition (blanket inhibition) across the hippocampal CA1 population, with place fields emerging from spatially tuned excitatory inputs. According to this view, non-place cells lack sufficient excitatory drive to overcome this uniform inhibition. Place cells were thought to be a specialized subset of CA1 pyramidal neurons with distinct connectivity or intrinsic properties. The relationship between SPW-R activity and place cell sequences was established, but the extent to which non-place cells participate in spatial coding and assembly organization remained unclear.

---

### What this paper contributes

This paper fundamentally challenges the uniform inhibition model by demonstrating that:

1. **Place fields emerge through localized disinhibition**, not just spatially tuned excitation. The reciprocal E/I mode during theta and place fields shows reduced inhibition within fields, allowing high-excitability neurons to express place fields when combined with external cues.

2. **Most CA1 pyramidal neurons are preconfigured place cells**. The unmasking of place fields in 69% of "non-place cells" indicates that the proportion of place cells in CA1 is far higher than previously estimated. These are not "new" place fields but preexisting subthreshold maps revealed by depolarization.

3. **Preconfigured attractor assemblies underlie spatial coding**. SPW-R cofiring in the home cage predicts spatial relationships between place fields, including unmasked fields of non-place cells. This suggests that spatial maps are scaffolded by preexisting assembly organization rather than being purely experience-dependent.

4. **Brain state-dependent E/I modes regulate network function**. The paper establishes that hippocampal CA1 operates in distinct computational modes: balanced mode during SPW-Rs (gain control, decorrelation) and reciprocal mode during theta/place fields (amplification, pattern completion).

---

### Brain regions & systems

- **Hippocampal CA1**: Primary region of study. Site of pyramidal neuron recordings and optogenetic stimulation. Exhibits state-dependent shifts between balanced and reciprocal E/I modes.

- **Hippocampal CA3**: Implied as source of excitatory inputs to CA1 during SPW-Rs and place field activation, though not directly recorded.

- **Entorhinal cortex**: Implied source of spatial and temporal inputs to CA1, referenced in context of place cell formation.

- **Subcortical modulatory systems**: Referenced as potential controllers of brain state-dependent shifts between E/I modes (e.g., neuromodulators affecting interneuron-pyramidal cell timing relationships).

---

### Mechanistic insight

The paper provides strong mechanistic insight by linking computational models to neural data:

**Computational level**: The brain solves the problem of encoding spatial information while maintaining network stability. This requires balancing pattern separation (during SPW-Rs) and pattern completion (during theta/place fields).

**Algorithmic level**: The algorithm involves state-dependent switching between two E/I integration modes:
- **Balanced mode**: Inhibition tracks excitation (I ∝ E), producing negative gain. This implements gain control and decorrelation during SPW-Rs.
- **Reciprocal mode**: Inhibition anti-correlates with excitation (I decreases as E increases), producing positive gain. This implements amplification and pattern completion during place field traversal.

**Implementational level**: The implementation involves:
- **Micro-LED probes** for simultaneous stimulation and recording from hundreds of CA1 neurons
- **State-dependent disinhibition** within place fields, evidenced by position-dependent interneuron firing and decreased inhibition of place cells
- **Preconfigured assembly organization** revealed through SPW-R cofiring patterns that predict spatial relationships
- **Theta-phase modulation** of excitability, with highest gain at the trough of theta cycles

The paper meets the high bar for mechanistic insight by providing both formal models (three E/I integration modes) and neural data (optogenetic responses, intracellular recordings, assembly analysis) that specifically support the reciprocal model for place fields and the balanced model for SPW-Rs.

---

### Limitations & open questions

- **Causal demonstration of behavioral consequences**: The paper demonstrates that unmasked place fields improve spatial decoding and replay sequences, but does not establish whether manipulating E/I balance causally affects behavior or learning.

- **Source of inhibition modulation**: While the paper shows decreased inhibition within place fields, the specific sources and mechanisms (e.g., which interneuron subtypes, neuromodulatory control) are not fully characterized.

- **Developmental origins of preconfigured assemblies**: The SPW-R cofiring that predicts spatial relationships suggests preconfigured organization, but how these assemblies form during development versus through experience is not addressed.

- **Generalization to other brain regions**: The findings are specific to hippocampal CA1; whether similar E/I mode switching occurs in other cortical or subcortical regions remains to be determined.

- **Long-term stability of unmasked place fields**: The paper demonstrates acute unmasking of place fields, but whether these fields persist without continued optogenetic stimulation or represent stable representational changes is unclear.

---

### Connections & keywords

**Key citations:**
- Grienberger et al. 2017 (Nat. Neurosci.) — tuned excitation/blanket inhibition model
- O'Keefe & Nadel 1978 — hippocampus as cognitive map
- Bittner et al. 2015 (Nat. Neurosci.) — synaptic potentiation mechanisms in place cells
- Wilson & McNaughton 1993, 1994 — place cell ensemble coding and reactivation
- Grosmark & Buzsáki 2016 (Science) — SPW-R and memory consolidation
- Dragoi & Tonegawa 2011 (Nature) — preconfigured hippocampal assembly sequences

**Named models or frameworks:**
- Tuned excitation / blanket inhibition model
- Balanced network model
- Reciprocal network model
- Hippocampal cognitive map framework
- Attractor network model of place cells
- Pattern separation and pattern completion framework

**Brain regions:**
- Hippocampal CA1 (primary)
- Hippocampal CA3 (implied)
- Entorhinal cortex (implied)

**Keywords:**
- optogenetics
- sharp-wave ripples (SPW-Rs)
- place cells
- subthreshold dynamics
- excitation-inhibition balance
- theta oscillations
- neuronal assemblies
- hippocampus
- memory replay
- attractor networks
