---
source_file: fiore2015_basal_ganglia_behavior.md
paper_id: fiore2015_basal_ganglia_behavior
title: "Evolutionarily conserved mechanisms for the selection and maintenance of behavioural activity"
authors:
  - "Vincenzo G. Fiore"
  - "Raymond J. Dolan"
  - "Nicholas J. Strausfeld"
  - "Frank Hirth"
year: 2015
journal: "Philosophical Transactions of the Royal Society B"
paper_type: review
contribution_type: theoretical
species:
  - mouse
methods:
  - optogenetics
  - computational_modeling
  - lesion
brain_regions:
  - striatum
  - nucleus_accumbens
  - ventral_tegmental_area
  - substantia_nigra
  - thalamus
frameworks:
  - reinforcement_learning
  - attractor_networks
keywords:
  - action_selection
  - basal_ganglia
  - central_complex
  - attractor_states
  - dimensionality_reduction
  - evolutionary_homology
  - dopamine
  - winner_take_all
  - sensorimotor_integration
  - direct_pathway
  - indirect_pathway
  - ontogenetic_clones
  - evolutionarily
  - conserved
  - mechanisms
  - selection
  - maintenance
  - behavioural
  - activity
key_citations:
  - kravitz2010_basal_ganglia_optogenetic
wiki_pages:
  - wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning
---

### One-line summary

The insect central complex and vertebrate basal ganglia share deep evolutionary homologies in genetic specification, circuit architecture, and computational mechanisms — specifically dimensionality reduction and attractor-state dynamics — that implement action selection and maintenance across taxa separated by more than 540 million years.

---

### Background & motivation

Survival requires animals to select appropriate behaviours in response to external and internal cues, and this capacity is phylogenetically ancient. Arthropods and vertebrates accomplish similar goal-directed and habitual behavioural control despite vast differences in brain size. Prior work by Strausfeld and Hirth (2013) established deep homology between the insect central complex (CX) and the vertebrate basal ganglia (BG) at the levels of embryological origin, orthologous genetic specification, neurochemistry, and behavioural pathology. This paper extends that analysis by identifying shared computational principles — the functional anatomy of circuits and the algorithms they implement — to argue for evolutionarily conserved mechanisms underlying action selection.

---

### Methods

This is a theoretical/comparative review. The synthesis approach includes:

- Comparative neuroanatomy of the insect CX (protocerebral bridge, fan-shaped body, ellipsoid body, noduli, lateral accessory lobes) and the vertebrate BG (striatum, GPe, GPi, STN, SNr, thalamus), drawing on data from Drosophila, cockroach, locust, lamprey, rodent, and primate.
- Review of lineage tracing and clonal analysis studies in both Drosophila (MARCM) and rodents (retroviral/thymidine labelling, Nkx2.1/Dlx1&2 mouse genetics) to establish correspondence in ontogenetic specification.
- Review of physiological, optogenetic, lesion, and connectomics studies to characterise the functional anatomy of CX and BG circuits.
- Application of a common computational vocabulary — dimensionality reduction, attractor states, winner-take-all dynamics, reinforcement learning via dopamine — to account for circuit function in both taxa.
- Literature is synthesised narratively; no meta-analytic statistics are performed.

---

### Key findings

- Both CX and BG derive from neural stem cells of the basal forebrain; in each structure, neuronal identity is specified by birth time and order via combinatorial selector gene programmes, generating ontogenetic clones as conserved cytoarchitectonic modules.
- Both structures are organised into parallel-projecting, partially segregated loops (sensorimotor, associative, and in vertebrates also limbic) that integrate and convey sensorimotor representations.
- In the BG, the corticostriatal input reduction is approximately 10:1, followed by a ~1000:1 reduction between striatum and GPi/SNr output nuclei; analogous dimensionality reduction occurs across the CX PB–FB–EB hierarchy.
- The CX ellipsoid body (EB) is proposed to be computationally homologous to the GPi/SNr gating system: it receives converging spatially organised sensory input, expresses lateral inhibition, and its output drives motor areas via the LAL (functionally analogous to thalamo-motor outputs).
- The Gall neuropil, which connects PB, EB, and LAL, is proposed to play a role comparable to the STN: providing tonic excitatory drive that balances afferent inhibition within the selection circuit.
- Action selection in both systems is described as transitions through attractor states in a nonlinear energy landscape; the direct pathway (D1-MSNs) strengthens attractors and stabilises selections, the indirect pathway (D2-MSNs) creates shallower or oscillatory attractors enabling switching.
- Dopamine modulates the circuit dually: phasic bursts (prediction error signals) alter synaptic weights to encode reinforcement learning, widening and steepening attractors for trained stimuli; tonic dopamine fluctuations transiently alter the gain of the entire loop, shifting the system between a stable maintenance mode and a flexible switching mode.
- Structural mutations affecting FB/EB in Drosophila produce locomotor defects (circling, reduced speed) consistent with impaired alternating motor selections, paralleling BG-related movement disorders.
- The multiplicity of correspondences supports the hypothesis of a common ancestral ground-plan circuit present in the last common ancestor of insects and vertebrates (>540 Ma).

---

### Computational framework

The paper uses a **dynamical systems / attractor network** framework, augmented by **reinforcement learning** (dopaminergic prediction error) and the concept of **dimensionality reduction**.

- **What is being modelled**: the neural computation that selects one behavioural action from competing alternatives and maintains it until conditions change.
- **Key variables**: neural gain within each parallel channel/column; the shape (steepness, width) of attractor basins in the energy landscape; phasic vs. tonic dopamine signals; reference position in sensorimotor space.
- **Core formalism**: re-entrant loops generate nonlinear dynamics describable as energy landscapes with multiple stable points (attractors). A sensory perturbation moves the system from a high-energy state towards the nearest attractor (winner-take-all); direct-pathway gain strengthens attractors (stable selection), indirect-pathway activity flattens them (exploration/switching). Phasic dopamine implements temporal-difference-like prediction error learning by modifying channel-specific gains; tonic dopamine uniformly scales all channel gains, controlling the overall stability vs. flexibility trade-off.
- **Key assumption**: the computational architecture is substrate-independent; the same algorithm is implemented in circuits that share evolutionary origin but differ enormously in physical scale.

---

### Prevailing model of the system under study

The introduction situates the paper against two bodies of prior work. First, the standard vertebrate model of BG function: the direct/indirect/hyperdirect pathway model (Alexander, DeLong & Strick 1986; Redgrave, Prescott & Gurney 1999; Nelson & Kreitzer 2014), in which direct pathway activation facilitates behaviour and indirect pathway activation suppresses it, implementing a selection-via-gating mechanism. Second, the emerging literature on evolutionary conservation of BG across vertebrates (lamprey through primates; Grillner and colleagues) and the prior homology claim by Strausfeld & Hirth (2013) extending this to insects. The paper thus works against a background assumption that BG-like action selection is a vertebrate innovation, and extends the prevailing selection-via-gating model by embedding it in a cross-phylum attractor-state framework that also encompasses the insect CX.

---

### What this paper contributes

The paper advances several claims beyond the prior homology literature:

1. **Computational mechanistic account**: It translates anatomical homology into a shared computational language — dimensionality reduction and attractor-state dynamics — giving a functional explanation, not just a structural one, for why the two circuits are homologous.
2. **EB as a gating node**: It proposes that the insect EB, with its identified layer-specific R-neuron subtypes and lateral inhibition, functions as the CX equivalent of GPi/SNr, and makes testable predictions about input/output layer organisation (directionality hypothesis) that were not previously formalised.
3. **Gall–STN analogy**: It identifies the Gall neuropil as a candidate STN functional homologue, a structural element not previously incorporated into computational accounts of CX function.
4. **Unified dopamine account**: It synthesises phasic/tonic dopamine roles in both taxa within a single attractor-landscape framework, where phasic dopamine reshapes individual attractors (long-term learning) and tonic dopamine modulates global landscape stability (short-term flexibility).
5. **Indirect pathway oscillatory role**: It incorporates recent optogenetic data showing indirect pathway contributions to action initiation and contraversive oscillatory movement, amending the standard direct/indirect model.

---

### Brain regions & systems

- **Insect central complex (CX)**: the primary insect circuit studied; proposed homologue of the vertebrate BG for action selection and maintenance.
  - **Protocerebral bridge (PB)**: encodes spatially organised sensory representations (visual, tactile); input layer of CX.
  - **Fan-shaped body (FB)**: integrates sensorimotor and associative inputs across modules; intermediate processing layer.
  - **Ellipsoid body (EB)**: proposed gating node; R1–R4 ring neurons mediate selection among behavioural alternatives via lateral inhibition and attractor dynamics.
  - **Lateral accessory lobes (LAL)**: output stage; relays CX selections to descending motor channels; functional analogue of thalamo-motor output.
  - **Gall**: satellite neuropil proposed as functional analogue of the STN.
- **Vertebrate basal ganglia (BG)**: primary vertebrate circuit studied.
  - **Striatum** (caudate, putamen, nucleus accumbens): input nucleus; D1- and D2-MSNs implement direct and indirect pathways.
  - **Globus pallidus internal segment (GPi) / substantia nigra pars reticulata (SNr)**: output nuclei; gating via inhibition of thalamus and brainstem motor centres.
  - **Globus pallidus external segment (GPe)**: intermediate node in indirect pathway.
  - **Subthalamic nucleus (STN)**: hyperdirect pathway; provides tonic excitatory drive to GPi/SNr; proposed analogue of the Gall.
  - **Thalamus**: relay from BG output to cortex and brainstem motor regions; functional analogue of the LAL.
- **Dopaminergic systems**: substantia nigra pars compacta (SNc) and VTA in vertebrates; corresponding dopaminergic neurons in insects; modulate both circuits for reinforcement learning and gain control.
- **Optic tectum / superior colliculus** and **mesencephalic locomotor region (MLR)**: brainstem motor targets of subcortical BG loops; no direct CX analogue is specified.

---

### Mechanistic insight

The paper does not fully meet the high bar as defined: it proposes an algorithm (attractor-state selection via gating) and draws on neural data from multiple sources, but it does not present a single study providing neural data that specifically supports the attractor algorithm over alternatives in a controlled comparison. The evidence is integrative and cross-species rather than arising from a single experimental design that links the model's variables (e.g. attractor basin depth, gain parameters) to measured neural activity.

Nonetheless, the paper makes substantive progress toward Marr's three levels:

- **Computational**: the problem is selection and maintenance of adaptive behaviour — choosing one action from competing alternatives and sustaining it until conditions change.
- **Algorithmic**: the solution is dimensionality reduction through spatially organised parallel loops, followed by winner-take-all competition among attractor states; dopaminergic prediction error signals update attractor shapes via gain changes; tonic dopamine modulates global landscape stability.
- **Implementational**: the paper maps algorithm onto specific circuits and cell types — D1-MSNs (direct pathway, stable attractors), D2-MSNs (indirect pathway, oscillatory attractors), STN/Gall (tonic excitation balancing inhibition), dopaminergic nuclei (phasic and tonic modulation). However, the insect side of this mapping remains speculative for several components (EB layer directionality, Gall targets), and the functional claims rest largely on lesion, mutation, and optogenetic data rather than single-unit recordings of attractor dynamics per se.

---

### Limitations & open questions

- The internal wiring of the insect EB — specifically the directionality of connections among R-neuron layers and whether parallel or centre-off gating is realised — is explicitly acknowledged as unknown at the time of writing.
- The specific targets of the Gall in the EB (input vs. output layers) had not been determined.
- The paper relies heavily on the prior homology claim (Strausfeld & Hirth 2013), which is contested in the field; the distinction between deep homology and convergent evolution is acknowledged but the case rests on a weight-of-evidence argument.
- The attractor-state framework is proposed qualitatively; quantitative modelling linking specific parameter values (e.g. gain, attractor depth) to measured neural or behavioural data is not provided in this paper (though cited companion work addresses this for the BG side).
- The extent to which the lamprey-to-primate conservation of BG generalises the functional claims across all vertebrates, and whether the CX-BG homology holds for all insects, is not deeply examined.
- The paper does not address how the CX/BG circuits interact with other brain regions (e.g. hippocampus, mushroom bodies in insects) for episodic or spatial memory, beyond noting the associative loop.
- The hypothesis that a single common ancestor circuit gave rise to both CX and BG implies specific predictions about circuit architecture in intermediate taxa that are not examined here.

---

### Connections & keywords

**Key citations**:
- Strausfeld NJ, Hirth F (2013) Science — deep homology of CX and BG (foundational prior work)
- Alexander, DeLong, Strick (1986) Annu Rev Neurosci — parallel organisation of BG-cortical loops
- Redgrave, Prescott, Gurney (1999) Neuroscience — BG as solution to selection problem
- Gurney, Prescott, Redgrave (2001) Biol Cybern — computational model of BG action selection
- Bar-Gad, Morris, Bergman (2003) Prog Neurobiol — dimensionality reduction in BG
- Seelig & Jayaraman (2015) Nature — neural dynamics for landmark orientation in Drosophila CX
- Kravitz et al. (2010) Nature — optogenetic control of direct/indirect pathways
- Montague, Dayan, Sejnowski (1996); Schultz, Dayan, Montague (1997) — dopamine as prediction error
- Stephenson-Jones et al. (2011) Curr Biol — evolutionary conservation of BG in vertebrates

**Named models or frameworks**:
- Direct/indirect/hyperdirect pathway model (standard BG model)
- Attractor-state / energy landscape framework
- Winner-take-all selection mechanism
- Reinforcement learning (temporal difference / prediction error)
- Dimensionality reduction framework (Bar-Gad et al.)
- Ontogenetic clone hypothesis (Strausfeld & Hirth)

**Brain regions**:
- Central complex (CX): protocerebral bridge, fan-shaped body, ellipsoid body, lateral accessory lobes, Gall
- Basal ganglia: striatum (caudate, putamen, nucleus accumbens), GPi, GPe, SNr, STN
- Thalamus, substantia nigra pars compacta, VTA, optic tectum/superior colliculus, mesencephalic locomotor region

**Keywords**:
- action selection, basal ganglia, central complex, attractor states, dimensionality reduction, evolutionary homology, dopamine, winner-take-all, sensorimotor integration, direct pathway, indirect pathway, ontogenetic clones

### Related wiki pages
- [[wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning|Dopamine reward prediction error and temporal-difference learning]]
