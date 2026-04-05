---
source_file: murphy-royal2020_stress_astrocyte_lactate_ltp.md
title: Stress gates an astrocytic energy reservoir to impair synaptic plasticity
authors: Ciaran Murphy-Royal, April D. Johnston, Andrew K. J. Boyce, Blanca Diaz-Castro, Adam Institoris, Govind Peringod, Oliver Zhang, Randy F. Stout, David C. Spray, Roger J. Thompson, Baljit S. Khakh, Jaideep S. Bains, Grant R. Gordon
year: 2020
journal: Nature Communications
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Acute stress impairs long-term potentiation by reducing astrocyte gap junction coupling and restricting lactate shuttling through astrocytic networks, creating an energy deficit at synapses.

### Background & motivation

Astrocytes support synaptic transmission and plasticity through metabolic coupling via gap junction networks that shuttle energy substrates. While stress is known to impair memory and synaptic plasticity (LTP), the cellular mechanisms linking stress hormones to synaptic dysfunction remain unclear. Astrocytes express high levels of glucocorticoid receptors, making them potential targets for stress-induced changes. This study investigates whether stress-induced alterations in astrocyte metabolic networks contribute to impaired synaptic plasticity.

### Methods

- **Animal model**: Adult C57BL6J mice (P25-70), both sexes, subjected to 20-min swim stress followed by 90-min recovery
- **RNA sequencing**: Astrocyte-specific transcriptome analysis using Aldh1l1-cre/ERT2 x Ribotag mice (n=4 per group)
- **Morphology analysis**: Single astrocyte filling with FITC-dextran, Sholl analysis of territory size and ramification index
- **Calcium imaging**: GCaMP6s expression under Aldh1l1 promoter, machine learning-based analysis of microdomain calcium events using SVM-RBF classifier
- **Gap junction coupling**: Real-time dye flux assay with Alexa-488 hydrazide, time constant (tau) measurement of intercellular dye transfer
- **Western blot**: Connexin 30 and 43 protein expression in whole-cell lysates and membrane fractions
- **Electrophysiology**: 
  - Astrocyte-fEPSP (a-fEPSP) recording through patched astrocytes
  - Classical field EPSP recordings for validation
  - Theta burst stimulation (TBS) for LTP induction
- **Lactate measurements**: Enzymatic biosensors for extracellular L-lactate quantification
- **Pharmacological manipulations**: Carbenoxolone (gap junction blocker), D-lactate (competitive inhibitor), L-lactate rescue, AR-C155858 and 4-CIN (MCT inhibitors), corticosterone, RU486 (GR antagonist), metyrapone (CORT synthesis inhibitor)
- **Genetic manipulation**: Dominant-negative connexin 43 (dnCx43) expressed via AAV2/5 under GfaABC1D promoter

### Key findings

- Acute stress altered 117 genes in the astrocyte translatome, including decreased sox-9 (regulator of connexin 30) and modifications in Wnt/β-catenin signaling pathway
- Stressed mice showed astrocyte hypertrophy: increased territorial domain (2646 ± 75 µm² vs 2385 ± 113 µm²) and increased ramification index (10.6 ± 1.3 vs 7.7 ± 1.3)
- Microdomain calcium events showed prolonged half-width in stressed astrocytes (4.5 ± 0.06 s vs 3.85 ± 0.6 s, P < 0.0001), with machine learning classifier achieving 72% accuracy in distinguishing naive from stressed traces
- Connexin 30 protein expression decreased after stress (79.7 ± 5.1% of naive, P = 0.02), while connexin 43 showed no significant change (90.1 ± 5.7%, P = 0.2)
- Functional gap junction coupling was impaired: tau increased from 254.5 ± 21.9 s to 430.4 ± 43 s (P = 0.0009), indicating slower dye transfer between astrocytes
- Corticosterone (CORT) was necessary and sufficient for decreased coupling: metyrapone (CORT synthesis inhibitor) blocked stress effects, and exogenous CORT (100 nM) mimicked stress effects; RU486 (GR antagonist) blocked CORT effects
- Stress slowed shuttling of fluorescent glucose analog 2-NBDG through astrocyte networks (tau = 356.7 ± 39.9 s vs 228.6 ± 36.9 s, P = 0.007)
- Gap junction blockade with carbenoxolone (CBX) prevented LTP (98.2 ± 15% vs 132 ± 4% in naive, P = 0.025)
- Intracellular D-lactate in astrocytes blocked LTP (104 ± 8% vs 132 ± 3.5%, P = 0.008), demonstrating that disrupting astrocyte-to-neuron lactate shuttling impairs plasticity
- Dominant-negative connexin 43 (dnCx43) expression blocked LTP (104.3 ± 2.7% vs naive), and this was rescued by L-lactate patch-filling (137.2 ± 9.1%, P = 0.006)
- After theta burst stimulation, extracellular L-lactate decreased in stressed mice (81 ± 6% of baseline, P = 0.027) but not in naive mice (114 ± 9%), indicating failure to replenish lactate during sustained activity
- Stress impaired neocortical LTP (109 ± 3% vs 132 ± 4%, P < 0.001), which was rescued by L-lactate patch-filling in astrocytes (126 ± 5%, P = 0.02)
- The rescue by L-lactate was blocked by MCT inhibitors AR-C155858 and 4-CIN, indicating neuronal lactate uptake is required for the rescue effect
- Findings were replicated in hippocampus CA1: stress reduced gap junction coupling (tau = 254 ± 15 s vs 168 ± 8 s, P < 0.001) and impaired LTP (116 ± 2.5% vs 142 ± 8.3%), which was rescued by L-lactate (159 ± 8.7%, P = 0.004)

### Computational framework

Not applicable. This is an empirical study investigating the mechanisms by which stress impairs synaptic plasticity through astrocyte metabolic networks. The findings could constrain models of astrocyte-neuron metabolic coupling and the role of gap junction networks in synaptic energy homeostasis.

### Prevailing model of the system under study

Prior to this study, the field understood that: (1) astrocytes provide metabolic support to neurons via the astrocyte-neuron lactate shuttle, which is essential for LTP and memory formation; (2) astrocytes are coupled into syncytial networks via gap junctions (primarily connexin 30 and 43), allowing diffusion of metabolic substrates between cells; (3) acute stress impairs LTP and memory through glucocorticoid receptor activation in neurons; (4) astrocytes express high levels of glucocorticoid receptors and show structural and molecular changes in stress-related disorders. However, the specific mechanism linking stress hormones to astrocyte function and synaptic plasticity was unknown.

### What this paper contributes

This paper establishes that acute stress impairs synaptic plasticity by disrupting astrocyte metabolic networks rather than through direct neuronal mechanisms. The key advances are:

1. **Identifies astrocytes as primary targets of stress hormones**: Glucocorticoids (corticosterone) act on astrocytic glucocorticoid receptors to reduce gap junction coupling, independent of neuronal effects.

2. **Reveals the mechanism**: Stress reduces connexin 30 expression and functional gap junction coupling between astrocytes, impairing the shuttling of energy substrates (glucose and lactate) through the astrocytic network.

3. **Demonstrates functional consequences**: Isolated astrocytes cannot meet the energy demands of synaptic plasticity. Stress impairs activity-dependent lactate release, creating an energy deficit that prevents LTP.

4. **Provides causal rescue**: Direct delivery of L-lactate to astrocytes rescues stress-impaired LTP, but only if neuronal lactate uptake via monocarboxylate transporters is intact. This confirms the astrocyte-neuron lactate shuttle as the critical pathway.

5. **Generalizes across brain regions**: The mechanism is conserved in both neocortex and hippocampus, suggesting broad relevance for stress-induced cognitive impairment.

### Brain regions & systems

- **Neocortex (somatosensory cortex)**: Primary site for RNAseq, morphological analysis, calcium imaging, gap junction coupling, and LTP experiments. Astrocytes show hypertrophy, altered calcium signaling, and reduced coupling after stress. LTP is impaired and rescued by L-lactate delivery.
- **Hippocampus (CA1 region, ventral)**: Replication of key findings. Stress reduces gap junction coupling (tau = 168s → 254s) and impairs LTP (142% → 116% baseline), which is rescued by L-lactate delivery to astrocytes (159% baseline).
- **Astrocyte syncytial networks**: The functional unit underlying metabolic support. Gap junction coupling (connexin 30 and 43) enables shuttling of glucose and lactate between astrocytes, creating a distributed energy reservoir for synapses.
- **Tripartite synapse**: The functional synaptic unit comprising presynaptic terminal, postsynaptic neuron, and perisynaptic astrocyte processes. Activity-dependent lactate release from astrocytes is required for LTP at these synapses.

### Mechanistic insight

This paper provides strong mechanistic insight that meets both criteria: (1) it formalizes an algorithmic process (the astrocyte syncytium as a metabolic network distributing energy), and (2) it provides extensive neural data supporting this mechanism over alternatives.

**Computational level**: The brain must solve the problem of matching highly localized, transient energy demands at synapses undergoing plasticity with distributed energy stores. The solution uses astrocyte networks as an "energy grid" that pools metabolic resources and distributes them on demand to active synaptic "sinks." This architecture reduces the burden on individual cells and increases reliability of energy supply during high-demand events like LTP induction.

**Algorithmic level**: The implementation involves:
- Glucose uptake and glycogenolysis in astrocytes providing substrate for lactate production
- Gap junction coupling (connexin 30 and 43) enabling diffusion of glucose and lactate through the astrocytic network
- Activity-dependent lactate release via monocarboxylate transporters (MCT4 on astrocytes, MCT1/MCT2 on neurons)
- Neuronal lactate uptake fueling ATP production required for NMDA receptor function and LTP maintenance

**Implementational level**: The mechanism is realized through:
- **Connexin 30**: Reduced expression following stress (79.7% of naive), regulated by sox-9 transcription factor
- **Connexin 43**: Target of dominant-negative manipulation; required for network coupling but not directly changed in expression by stress
- **Glucocorticoid receptors**: Mediate stress effects; corticosterone both necessary and sufficient for reduced coupling
- **Monocarboxylate transporters**: MCT4 on astrocytes releases lactate; MCT1/2 on neurons mediate uptake
- **Mitochondria**: Implicated in calcium microdomain changes; possibly impaired positioning/function in stress

The paper demonstrates that stress disrupts the algorithmic level (gap junction coupling) without necessarily changing the implementational level (connexin expression) dramatically, suggesting that functional changes may arise from post-translational modifications or morphological changes affecting channel function.

### Limitations & open questions

- **Mechanism of connexin 30 reduction**: While sox-9 downregulation was identified, the complete signaling cascade from glucocorticoid receptor activation to reduced connexin 30 expression is not fully mapped
- **Morphological vs. molecular mechanisms**: The relative contribution of astrocyte hypertrophy (physical uncoupling) versus connexin expression changes to reduced functional coupling remains unresolved
- **Mitochondrial involvement**: While calcium microdomain changes suggest mitochondrial dysfunction, direct evidence for stress-induced changes in mitochondrial positioning or function in astrocytes is lacking
- **Regional specificity**: The mechanism was demonstrated in neocortex and hippocampus, but whether other brain regions show similar or divergent responses to stress is unknown
- **Chronic stress effects**: Only acute stress (single 20-min swim) was investigated; whether chronic stress produces similar or distinct effects on astrocyte networks is unknown
- **Behavioral correlates**: While LTP impairments were demonstrated, direct behavioral tests of memory following astrocyte-specific manipulations were not performed
- **Hemichannel contribution**: The possibility that stress increases hemichannel activity (as suggested by prior work) while decreasing gap junction coupling was not directly tested
- **Therapeutic potential**: While L-lactate rescue was demonstrated, the translational feasibility of targeting astrocyte metabolic networks for stress-related disorders remains unexplored

### Connections & keywords

**Key citations:**
- Rouach et al. (2008) - foundational work on astrocyte metabolic networks sustaining hippocampal synaptic transmission
- Pannasch et al. (2011, 2014) - connexin 30/43 roles in synaptic plasticity and morphology
- Suzuki et al. (2011) - astrocyte-neuron lactate transport required for long-term memory formation
- Kaouane et al. (2012) - glucocorticoids induce PTSD-like memory impairments
- Henneberger et al. (2010) - astrocyte D-serine release required for LTP

**Named models or frameworks:**
- Astrocyte-neuron lactate shuttle (ANLS) hypothesis
- Tripartite synapse concept
- Astrocyte syncytial network / metabolic coupling model
- Theta burst stimulation (TBS) protocol for LTP induction
- Astrocyte-fEPSP (a-fEPSP) recording technique

**Brain regions:**
- Somatosensory cortex (neocortex) - primary site for RNAseq, imaging, and electrophysiology
- Hippocampus CA1 (ventral) - replication of gap junction coupling and LTP findings
- Dorsal hippocampus - viral injection site for dnCx43 experiments

**Keywords:**
- Astrocyte gap junction coupling
- Connexin 30 (Cx30) and Connexin 43 (Cx43)
- Glucocorticoid receptor signaling
- Corticosterone (CORT)
- L-lactate and monocarboxylate transporters (MCT1, MCT2, MCT4)
- Long-term potentiation (LTP)
- Synaptic plasticity
- Acute stress
- Astrocyte-neuron lactate shuttle
- Energy metabolism
- Dominant-negative connexin 43 (dnCx43)
- RNA sequencing (RNAseq)
- Two-photon microscopy
- Patch-clamp electrophysiology
- Tripartite synapse
