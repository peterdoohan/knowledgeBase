---
source_file: foster2021_cortico_basal_ganglia.md
paper_id: foster2021_cortico_basal_ganglia
title: "The mouse cortico–basal ganglia–thalamic network"
authors:
  - "Nicholas N. Foster"
  - "Joshua Barry"
  - "Laura Korobkova"
  - "Luis Garcia"
  - "Lei Gao"
  - "Marlene Becerra"
  - "Yasmine Sherafat"
  - "Bo Peng"
  - "Xiangning Li"
  - "Jun-Hyeok Choi"
  - "Lin Gou"
  - "Brian Zingg"
  - "Sana Azam"
  - "Darrick Lo"
  - "Neda Khanjani"
  - "Bin Zhang"
  - "Jim Stanis"
  - "Ian Bowman"
  - "Kaelan Cotter"
  - "Chunru Cao"
  - "Seita Yamashita"
  - "Amanda Tugangui"
  - "Anan Li"
  - "Tao Jiang"
  - "Xueyan Jia"
  - "Zhao Feng"
  - "Sarvia Aquino"
  - "Hyun-Seung Mun"
  - "Muye Zhu"
  - "Anthony Santarelli"
  - "Nora L. Benavidez"
  - "Monica Song"
  - "Gordon Dan"
  - "Marina Fayzullina"
  - "Sarah Ustrell"
  - "Tyler Boesen"
  - "David L. Johnson"
  - "Hanpeng Xu"
  - "Michael S. Bienkowski"
  - "X. William Yang"
  - "Hui Gong"
  - "Michael S. Levine"
  - "Ian Wickersham"
  - "Qingming Luo"
  - "Joel D. Hahn"
  - "Byung Kook Lim"
  - "Li I. Zhang"
  - "Carlos Cepeda"
  - "Houri Hintiryan"
  - "Hong-Wei Dong"
year: 2021
journal: Nature
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - optogenetics
brain_regions:
  - striatum
  - nucleus_accumbens
  - substantia_nigra
  - thalamus
frameworks:
  - reinforcement_learning
keywords:
  - cortico_basal_ganglia_thalamo_cortical_loop
  - basal_ganglia_subnetworks
  - direct_pathway_convergence
  - indirect_pathway_parallelism
  - striatonigral_pathway
  - striatopallidal_pathway
  - mesoscale_connectome
  - closed_circuit_loop
  - corticonigral_projection
  - anterograde_transsynaptic_tracing
  - mouse_brain_atlas
  - community_detection_network_analysis
  - mouse
  - corticobasal
  - gangliathalamic
  - network
key_citations:
  - wang2020_alternating_theta_sequences
---

### One-line summary

A comprehensive mesoscale connectome of the mouse cortico–basal ganglia–thalamic loop reveals six parallel subnetworks with convergent direct (striatonigral) and parallel indirect (striatopallidal) pathways, and demonstrates for the first time that the loop is truly closed-circuit.

---

### Background & motivation

The cortico–basal ganglia–thalamo–cortical loop is a fundamental network motif implicated in cognition, sensorimotor behaviour, and many neurological and neuropsychiatric disorders. The canonical model proposes just three parallel channels (motor, limbic, associative) flowing through the basal ganglia, but this three-channel view cannot account for the diverse functions attributed to the basal ganglia. Building on a prior study that subdivided the mouse dorsal striatum (caudoputamen, CP) into 29 functional domains based on cortical inputs, this paper asks: how do these fine-grained striatal domains map their outputs through every downstream node of the loop, and does the loop actually close in a recurrent fashion?

---

### Methods

- 268 male C57Bl/6 and Ai14 mice; ~700 injections total; 138 mice used specifically for striatal output analysis.
- Anterograde tracers (PHAL, AAV-GFP, AAV-RFP) injected into 36 representative CP domains plus nucleus accumbens subdivisions; outputs tracked through GPe, SNr, thalamus and back to cortex.
- Fluorescence micro-optical sectioning tomography (fMOST) for single-cell-level axonal reconstructions.
- Anterograde transsynaptic AAV tracing (AAV1-Cre) to verify functional synaptic specificity across nodes.
- Channelrhodopsin-2-assisted circuit mapping (CRACM) combined with transsynaptic tracing to test convergence of direct and indirect pathways onto individual SNr neurons electrophysiologically.
- Double co-injection technique (anterograde–retrograde tracer pairs at non-adjacent nodes) to demonstrate whole-loop labelling in a single animal.
- Patch-clamp recordings in acute slice to verify closed-loop thalamocortical-to-corticostriatal excitatory synaptic connections.
- Network analysis: Louvain community detection algorithm applied to grid-quantified axonal terminal field data across multiple gamma values; consensus community structures identified.

---

### Key findings

- The striatonigral (direct) pathway is characterized by convergence: SNr receives inputs from multiple striatal domains per unit area (mean 6.49 ± 2.97 striatal domain inputs per grid box), roughly twice the convergence seen in GPe (mean 3.75 ± 1.79; P < 0.0001). This was confirmed electrophysiologically: all 6 SNr neurons responded to ChR2 stimulation of a second CP domain's axons, while 5 of 6 GPe neurons did not (P = 0.0152); peak current was also significantly greater in SNr (267.5 ± 197.6 pA vs 33.67 ± 24.74 pA; P = 0.0348).
- The striatopallidal (indirect) pathway is predominantly parallel: 36 GPe domains identified, 64% receiving only one or two striatal inputs; 69% spanning a single coronal level.
- 14 SNr domains identified from network analysis of the 36 CP domain projections.
- Direct and indirect pathways originating from the same striatal domain ultimately converge onto the same postsynaptic SNr neurons: 10 of 14 recorded SNr neurons showed inhibitory responses to pallidonigral stimulation when those SNr neurons were pre-labelled via transsynaptic tracing from the same CP domain.
- Six domains each identified in parafascicular (PF) and ventromedial (VM) thalamus, corresponding to associative, trunk/lower-limb, upper-limb, mouth, limbic, and ventral-striatal subregions.
- Six parallel cortico–basal ganglia–thalamic subnetworks delineated: each transduce a specific subset of cortical information through every node of the loop.
- The loop is demonstrably closed-circuit: thalamocortical axons from PF.m synapse onto corticostriatal neurons projecting to CPi.vl.v — 9 of 13 recorded labelled neurons showed monosynaptic excitatory postsynaptic currents (mean 44.89 ± 42.8 pA) in response to optogenetic thalamocortical stimulation.
- A direct corticonigral projection was identified from orofacial motor cortex (MOp-m/i) to SNr.orb, confirmed anatomically with synaptophysin-GFP synaptic bouton labelling and functionally with transsynaptic AAV tracing.

---

### Computational framework

Not applicable in the strict sense — no explicit computational model or formalism is developed. The paper is a large-scale anatomical and circuit-mapping study operating at the connectome level. The implicit framework is that of parallel and convergent information routing: the basal ganglia implements divergent-then-convergent processing, with the indirect pathway acting as a set of parallel channels and the direct pathway integrating (converging) information before routing it through SNr.

The results constrain circuit-level models of basal ganglia function. In particular, the finding that direct and indirect pathways converge onto the same SNr neurons from the same striatal source is directly relevant to formal models of action selection (e.g., actor-critic and Go/No-Go reinforcement learning models) that assume these pathways exert opposing influences on the same output neurons.

---

### Prevailing model of the system under study

The classical model of basal ganglia organisation, dominant since Alexander, DeLong and Strick (1986), proposes three parallel functional channels — motor/sensorimotor, limbic, and associative — flowing through anatomically segregated striatal, pallidal, and nigral territories. A separate pair of pathways within this framework — the direct (striatonigral) and indirect (striatopallidal) pathways — are hypothesised to have opposing effects on basal ganglia output, with the direct pathway disinhibiting thalamus and the indirect pathway inhibiting it. While some efforts had refined the three-channel model by postulating additional subnetworks, a definitive whole-circuit wiring diagram at fine spatial resolution was lacking. Moreover, it had long been hypothesised (but never demonstrated in a single animal) that the network forms a truly closed recurrent loop from cortex back to the same cortical neurons via striatum, nigra, and thalamus.

---

### What this paper contributes

This paper replaces the coarse three-channel model with a six-subnetwork model grounded in fine-grained, multi-synaptic connectional data across every node of the loop. Specifically:

- It establishes that the mouse basal ganglia has at least 14 SNr and 36 GPe domains — far more than the three classical channels — each with distinct striatal inputs.
- It resolves a longstanding ambiguity about direct vs. indirect pathway topography: the indirect pathway is characterised by higher parallelism and specificity, while the direct pathway integrates information from multiple sources into fewer output domains.
- It provides the first single-animal demonstration that the cortico–basal ganglia–thalamic loop is genuinely closed-circuit, with thalamocortical neurons synapsing directly onto corticostriatal neurons in the same subnetwork.
- It identifies a previously uncharacterised direct corticonigral pathway as a third fast route for cortical information to reach SNr (in addition to the well-known direct striatonigral and hyperdirect cortico-STN-SNr pathways).
- It shows that direct and indirect pathways from the same striatal domain converge onto the same SNr neurons, supporting a model where opposing pathway signals are integrated at the SNr level rather than at separate downstream targets.

---

### Brain regions & systems

- Caudoputamen (CP) / dorsal striatum — input node of the loop; 29–33 functional domains used as the starting point for tracing
- Globus pallidus external (GPe) — indirect pathway relay; 36 domains identified; characterised by parallel (low-convergence) striatal inputs
- Substantia nigra pars reticulata (SNr) — direct pathway output nucleus; 14 domains identified; characterised by convergent striatal inputs; also target of pallidonigral and novel corticonigral projections
- Parafascicular thalamic nucleus (PF) — basal ganglia output relay; 6 domains identified; projects back to striatum and cortex
- Ventromedial thalamic nucleus (VM) — second major SNr target; 6 domains with distinct cortical innervation topography
- Primary motor cortex (MOp), particularly orofacial subregion MOp-m/i — cortical node of the oro-brachial subnetwork; origin of novel direct corticonigral projection; site of thalamocortical-to-corticostriatal closed-loop synapse
- Nucleus accumbens (ACBc, ACBsh.m, ACBsh.l) — ventral striatal component; projects to a ventral basal ganglia subnetwork including SNr.dm and PF.vs
- Subthalamic nucleus (STN) — receives collaterals from the corticonigral pathway; not systematically analysed in this paper

---

### Mechanistic insight

This paper partially meets the bar. It presents a detailed wiring diagram (structural algorithm) for how information flows through the cortico–basal ganglia–thalamic loop, and provides anatomical and electrophysiological data that directly support specific circuit connectivity claims. However, it does not directly address the *computation* performed by this circuit — i.e., what problem the basal ganglia is solving — and does not provide neural recording data linking specific computations (e.g., action selection, reward prediction errors) to the structural organisation described.

Mapping onto Marr's levels:

- **Computational**: Not addressed. The paper is agnostic about what the basal ganglia computes. The six-subnetwork structure implies that distinct cognitive/behavioural functions are processed in parallel, but no formal claim about the computation is made.
- **Algorithmic**: Substantially addressed. The paper shows that direct pathway information converges (many striatal inputs to fewer SNr outputs), indirect pathway information is routed in parallel (one-to-one striatal-to-GPe mappings), and these two streams re-converge on the same SNr neurons — consistent with an integration/gating algorithm implemented at the level of SNr. The closed-loop demonstration shows that thalamic output feeds back to the exact corticostriatal neurons that initiated the loop.
- **Implementational**: Partially addressed. Specific cell types are identified (D1- vs D2-Cre lines used to confirm direct/indirect pathway topography), dendritic morphology of SNr projection neurons is characterised (showing capacity for multi-input integration at a coronal level), and layer-specific cortical connectivity of thalamocortical feedback is shown (PF.m axons terminating in layer 4 of MOp-m/i, overlapping with apical dendrites of corticostriatal neurons). The paper does not address neuromodulatory or biophysical mechanisms.

---

### Limitations & open questions

- The analysis focuses on the mouse dorsal striatum and omits major components of the circuit: substantia nigra pars compacta (SNc), internal globus pallidus (GPi/entopeduncular nucleus), subthalamic nucleus (STN), and numerous other thalamic nuclei.
- Ventral striatum (nucleus accumbens) analysis is limited to three injection sites; its full integration into the six-subnetwork model is not completed.
- The six subnetworks are identified at a structural level; their functional significance — what computations or behaviours they mediate — is not directly tested.
- The convergence of direct and indirect pathways onto the same SNr neurons was demonstrated for one pathway pair; the generality across all six subnetworks remains to be confirmed.
- The direct corticonigral pathway was characterised mainly in the oro-brachial subnetwork; its prevalence and role across other subnetworks is unclear.
- The paper does not address dynamic aspects (e.g., how signals are gated or modulated in real-time behaviour), dopaminergic modulation, or plasticity within these circuits.
- The work is in mouse; cross-species generality (particularly to primates, where three-channel models were largely derived) is assumed but not directly demonstrated here.

---

### Connections & keywords

**Key citations**:
- Alexander, DeLong & Strick (1986) — original three-channel parallel organisation model
- Parent & Hazrati (1995) — functional anatomy of the basal ganglia loop
- Hintiryan et al. (2016) — mouse cortico-striatal projectome (basis for the 29 CP domain subdivision)
- Mandelbaum et al. (2019) — distinct cortico-thalamic-striatal circuits through PF
- Lee, Wang & Sabatini (2020) — anatomically segregated basal ganglia pathways allowing parallel behavioral modulation
- Albin, Young & Penney (1989) — functional anatomy of basal ganglia disorders (direct/indirect pathway model)
- Gerfen (1984, 1985) — neostriatal mosaic and striatonigral compartmentalization

**Named models or frameworks**:
- Three-channel model of basal ganglia (Alexander et al. 1986)
- Direct pathway (striatonigral)
- Indirect pathway (striatopallidal)
- Hyperdirect pathway (cortico-STN-SNr)
- Corticonigral pathway (novel, described here)
- Louvain community detection algorithm (network analysis)
- CRACM (channelrhodopsin-2-assisted circuit mapping)
- fMOST (fluorescence micro-optical sectioning tomography)
- SHIELD tissue clearing

**Brain regions**:
- Caudoputamen (CP), dorsal striatum
- Globus pallidus external (GPe)
- Substantia nigra pars reticulata (SNr)
- Parafascicular thalamic nucleus (PF)
- Ventromedial thalamic nucleus (VM)
- Primary motor cortex (MOp), secondary motor cortex (MOs)
- Nucleus accumbens (ACBc, ACBsh)
- Subthalamic nucleus (STN)

**Keywords**:
- cortico-basal ganglia-thalamo-cortical loop
- basal ganglia subnetworks
- direct pathway convergence
- indirect pathway parallelism
- striatonigral pathway
- striatopallidal pathway
- mesoscale connectome
- closed-circuit loop
- corticonigral projection
- anterograde transsynaptic tracing
- mouse brain atlas
- community detection network analysis
