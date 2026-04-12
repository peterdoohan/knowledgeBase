---
source_file: zutshi2022_extrinsic_intrinsic_ca1.md
paper_id: zutshi2022_extrinsic_intrinsic_ca1
title: "Extrinsic control and intrinsic computation in the hippocampal CA1 circuit"
authors:
  - "Ipshita Zutshi"
  - "Manuel Valero"
  - "Antonio Fernández-Ruiz"
  - "György Buzsáki"
year: 2022
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - optogenetics
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - hippocampus
  - ca1
  - place_cells
  - theta_oscillations
  - medial_entorhinal_cortex
  - ca3
  - optogenetics
  - pharmacogenetics
  - cell_assemblies
  - remapping
  - current_source_density
  - local_field_potential
  - intrinsic_computation
  - functional_deafferentation
  - spatial_memory
  - neuronal_silencing
  - extrinsic
  - control
  - intrinsic
  - computation
---

### One-line summary

CA1 place cells and assemblies persist despite combined silencing of medial entorhinal cortex and CA3 inputs, demonstrating substantial intrinsic computation capacity in the CA1 circuit.

### Background & motivation

A fundamental question in circuit neuroscience is whether neuronal spiking reflects local computation or passive inheritance from upstream inputs. In the hippocampal CA1 region, this is particularly relevant because CA1 pyramidal neurons receive sparse recurrent connections and depend heavily on inputs from CA3 and the medial entorhinal cortex (mEC). Prior studies using lesions or inactivation have produced conflicting results about the relative contributions of these inputs to CA1 place cell activity. This study aimed to systematically compare the effects of selective mEC, CA3, and local CA1 silencing on network dynamics and spatial representations.

### Methods

- **Subjects**: 21 male Grik4-Cre mice (expressing Cre in CA3 and DG neurons)
- **Viral manipulations**:
  - mEC silencing: AAV5-mDlx-ChR2-mCherry (optogenetic activation of interneurons) in unilateral or bilateral mEC
  - CA1 silencing: AAV1-CaMKII-stGtACR2 (optogenetic suppression of pyramidal cells) in unilateral CA1
  - CA3 silencing: AAV5-Syn-DIO-PSAM4-GlyR-IRES-GFP (pharmacogenetic silencing) in bilateral CA3
- **Recordings**: 64- or 128-channel silicon probes in dorsal CA1 with optic fibers for stimulation
- **Behavior**: Delayed spatial alternation task on a Figure-8 maze with optogenetic stimulation restricted to the central arm
- **Analysis**: Current source density (CSD) analysis, unit clustering with Kilosort, cell assembly detection (PCA-ICA), place field mapping, theta phase modulation

### Key findings

- **mEC silencing**: Dramatically reduced theta and gamma currents in CA1 (particularly in stratum lacunosum-moleculare) but only moderately affected CA1 pyramidal cell firing rates; unilateral mEC silencing had minimal effect on place field stability, while bilateral mEC silencing caused significant remapping
- **CA3 silencing**: Strongly decreased CA1 firing rates but had minimal effect on theta currents; caused significant place cell remapping and reduced place field stability; effect on spatial map was larger than mEC silencing alone
- **Local CA1 silencing**: Reduced local firing rates without affecting theta currents in other layers; produced significant remapping with supralinear enhancement when combined with mEC silencing
- **Combined manipulations**: Even with combined mEC + CA3 silencing or mEC + CA1 silencing, the fraction of spatially tuned place fields remained intact, and CA1 cell assemblies persisted with stable expression; firing rates and CSD magnitude were dissociable
- **Theta phase effects**: Each input manipulation produced distinct shifts in theta phase preference of CA1 pyramidal cells—mEC silencing slightly advanced phase, CA1 silencing slightly delayed phase, and CA3 silencing caused ~30° shift toward the theta peak
- **Phase precession**: Bilateral mEC and CA3 manipulations reduced the proportion of significantly precessing place fields by 40-50%, but the remaining cells continued to show significant phase precession, suggesting the deafferented CA1 can support some level of phase precession

### Computational framework

The paper employs a **dynamical systems/network oscillation framework** conceptualizing hippocampal theta as an emergent property of interacting neuronal populations. The study distinguishes between:
- **Subthreshold collective activity** (measured by LFP/CSD) reflecting summed synaptic currents
- **Output spiking activity** of individual neurons

The framework treats place fields as emergent properties of sequentially organized neuronal assemblies, with theta oscillations providing the temporal structure for spike timing. The work also engages with attractor network concepts, discussing whether CA1 place fields emerge from inherited patterns (from CA3/mEC) or local computation.

### Prevailing model of the system under study

Prior to this study, the prevailing view held that CA1 neuronal activity largely reflects "inheritance" from upstream inputs rather than local computation. Specifically:
- CA1 place cells were thought to inherit their spatial firing properties primarily from CA3 and/or mEC inputs
- The CA3 contribution was emphasized due to its extensive recurrent collateral system, proposed to support attractor-based pattern completion
- The mEC contribution was viewed as providing spatial information via grid cells and theta rhythmicity
- CA1 was seen as primarily refining place fields rather than generating them independently
- Theta oscillations were thought to be primarily driven by mEC inputs, particularly layer 2 stellate cells

This view was supported by lesion studies showing that CA3 or mEC damage reduced CA1 place cell activity, though results were variable and often partial.

### What this paper contributes

This paper challenges the prevailing model by demonstrating that the CA1 network possesses substantial intrinsic computational capacity:

1. **Input-independent place field maintenance**: Even with combined silencing of both major inputs (mEC and CA3), CA1 continued to generate and maintain place fields at the same fraction as in intact conditions, demonstrating that CA1 can generate spatially tuned activity without requiring continuous external drive.

2. **Dissociation of LFP and spiking**: The study reveals that firing rates and synaptic currents (measured by CSD) are dissociable—mEC silencing dramatically reduced theta currents while only moderately affecting CA1 firing, whereas CA3 silencing strongly reduced firing without affecting theta currents.

3. **Differential input contributions**: The work clarifies that mEC is the main current generator for hippocampal theta oscillations (via direct layer 3-to-CA1 projections, not just indirectly through the trisynaptic loop), while CA3 contributes primarily to firing rate maintenance and spatial map stability.

4. **Local assembly persistence**: CA1 cell assemblies remained stable and continued to express even during functional deafferentation, indicating that the circuit mechanisms for assembly formation and maintenance are largely intrinsic to CA1.

5. **Reconfiguration vs. elimination**: While inputs are not required for place field expression, they do contribute to map stability—perturbations cause remapping (reconfiguration of which cells fire where) rather than elimination of spatial tuning.

### Brain regions & systems

- **CA1 (hippocampus)** — Primary site of recording and manipulation; demonstrates intrinsic capacity for place field generation and assembly expression despite input silencing
- **Medial entorhinal cortex (mEC)** — Major input to CA1; primary generator of theta currents in CA1; optogenetically silenced using Dlx-ChR2 targeting interneurons
- **CA3 (hippocampus)** — Provides strong excitatory drive to CA1; contributes to place map stability and firing rates; pharmacogenetically silenced using PSAM4-GlyR in Grik4-Cre mice
- **Dentate gyrus (DG)** — Indirectly affected by mEC silencing; characterized by prominent theta sinks in molecular layer

### Mechanistic insight

This paper provides strong mechanistic insight by linking specific neural circuit perturbations to both network-level dynamics (LFP/CSD) and single-neuron output (spiking, place fields), though it does not fully satisfy the highest bar for mechanistic insight (explicit algorithm + neural data supporting that specific algorithm over alternatives).

**Computational level**: The brain region (CA1) must generate and maintain spatial representations (place fields) to support navigation and memory. The study demonstrates this can occur with minimal external input, suggesting the problem can be solved through local circuit computation.

**Algorithmic level**: The paper proposes that CA1 place fields emerge from sequentially organized neuronal assemblies, with theta oscillations providing temporal structure. The intrinsic CA1 circuit—with its sparse recurrent excitation and prominent feedforward and feedback inhibition—can generate these sequential dynamics. The study shows that input perturbations reconfigure which assemblies are active (remapping) but does not eliminate the circuit's capacity for assembly expression.

**Implementational level**: The physical implementation involves:
- Sparse recurrent connections between CA1 pyramidal cells
- Strong local inhibition (basket cells, bistratified cells, O-LM cells) creating competitive dynamics
- Theta-frequency modulation providing temporal windows for assembly expression
- Differential contributions from mEC (theta current generation) and CA3 (firing rate support)

The paper does not identify the specific algorithm with sufficient formal precision to fully satisfy the highest mechanistic bar, but it provides substantial evidence constraining the space of possible mechanisms.

### Limitations & open questions

- **Silencing completeness**: The efficacy of silencing could not be identical across all brain regions, meaning some differences in observed effects may reflect technical rather than biological differences
- **Behavioral context**: All experiments were conducted in a relatively simple spatial alternation task; the findings might differ in more complex environments where animals must rely more heavily on external cues
- **Mechanism of intrinsic computation**: While the study demonstrates CA1's capacity for input-independent computation, the specific circuit mechanisms (which local microcircuits generate and sustain assemblies) remain to be identified
- **Reconciliation with prior lesion studies**: The finding that CA1 place fields persist without major inputs appears to conflict with some prior lesion studies; the differences may relate to chronic vs. acute manipulations, lesion completeness, or behavioral task demands
- **Role of other inputs**: The study focused on mEC and CA3 inputs; the contributions of lateral entorhinal cortex, perirhinal cortex, thalamic reuniens, and subcortical neuromodulators remain to be systematically tested
- **Temporal coding**: While spatial firing persisted, phase precession was reduced by 40-50% with mEC and CA3 silencing, suggesting some temporal coding aspects may be more input-dependent

### Connections & keywords

**Key citations**: Mizuseki et al. 2009 (theta windows for computation), Brun et al. 2002 (CA3 lesions), Miao et al. 2015 (entorhinal inactivation), Fernández-Ruiz et al. 2021 (gamma communication), Davoudi and Foster 2019 (CA3 silencing), Schlesiger et al. 2015 (MEC for temporal organization), O'Keefe and Recce 1993 (phase precession), Dragoi and Buzsáki 2006 (theta sequences), Fernández-Ruiz et al. 2017 (theta-gamma coupling)

**Named models or frameworks**: Attractor network models, Pattern completion, Phase precession, Theta-gamma coupling, Cell assemblies, Current source density analysis, Deafferentation paradigm

**Brain regions**: CA1 (hippocampus), CA3 (hippocampus), Medial entorhinal cortex (mEC), Dentate gyrus (DG), Stratum lacunosum-moleculare (sLM), Stratum radiatum, Stratum oriens, Stratum pyramidale

**Keywords**: hippocampus, CA1, place cells, theta oscillations, medial entorhinal cortex, CA3, optogenetics, pharmacogenetics, cell assemblies, remapping, current source density, local field potential, intrinsic computation, functional deafferentation, spatial memory, neuronal silencing
