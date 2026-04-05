---
source_file: devuyst2009_calcium_connexin43_hemichannels.md
title: "Ca2+ regulation of connexin 43 hemichannels in C6 glioma and glial cells"
authors: Elke De Vuyst, Nan Wang, Elke Decrock, Marijke De Bock, Mathieu Vinken, Marijke Van Moorhem, Charles Lai, Maxime Culot, Vera Rogiers, Romeo Cecchelli, Christian C. Naus, W. Howard Evans, Luc Leybaert
year: 2009
journal: Cell Calcium
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Intracellular Ca2+ triggers ATP release via Cx43 hemichannels not through direct action on the connexin protein, but through a multi-step signalling cascade involving CaM, CaMK-II, p38 MAPK, phospholipase A2, arachidonic acid, ROS, and NO, with a bell-shaped concentration–response profile reflecting opposing positive and negative feedback at different Ca2+ levels.

---

### Background & motivation

Connexin hemichannels (formed by Cx43) can open in response to various stimuli and serve as a release pathway for small paracrine messengers such as ATP. Earlier work demonstrated that intracellular Ca2+ elevations could trigger hemichannel-related responses, but the intracellular signalling pathway linking Ca2+ to hemichannel opening remained unknown. Understanding this pathway is important for explaining how glial cells respond to physiological stimuli (e.g., glutamate spillover) and for clarifying the regulation of purinergic signalling in brain tissue. This study fills the gap by systematically dissecting the signalling steps between [Ca2+]i elevation and Cx43 hemichannel-mediated ATP release.

---

### Methods

- **Cell lines**: C6 glioma cells stably transfected with Cx43 (C6-Cx43), HeLa-Cx43, C6 wild-type, C6-Panx1-Myc; primary cortical glial cells from neonatal rat brain (95% GFAP-positive astrocytes).
- **Stimuli**: Ca2+ ionophore A23187 (concentration and time–response), CaM agonist CALP1, exogenous arachidonic acid (AA), and glutamate.
- **ATP release measurement**: Bioluminescence plate reader assay in extracellular medium.
- **Ca2+ imaging**: Fura-2-AM ratiometric fluorescence imaging.
- **Hemichannel identification**: Cx43 siRNA knockdown (~50% reduction), Gap 26/27 mimetic peptide blockade (IC50 ~54 µM and ~95 µM respectively), exclusion of Panx1, P2X7 receptor pore, and vesicular release mechanisms (botulinum toxin B, tetanus toxin, bafilomycin A1).
- **Pharmacological dissection**: Inhibitors targeting CaM (W7), CaMK-II (AIP, KN62), p38 MAPK (SB202190), PLA2 (AACOCF3), lipoxygenase (baicalein), cyclo-oxygenase (indomethacin), ROS (N-acetyl-l-cysteine, α-tocopherol, SOD), and NO synthesis (Nω-nitro-l-arginine); P2Y receptors (PPADS, suramin).
- **Membrane potential**: Voltage-sensitive dye DiBAC4(3) to assess depolarisation.
- **Statistics**: Unpaired one-tailed t-test; one-way ANOVA with Bonferroni post-test.

---

### Key findings

- Ca2+-triggered ATP release was strictly Cx43-dependent: absent in C6-WT, C6-Panx1-Myc, and after siRNA knockdown of *gja1*; abolished by Gap 26/27 mimetic peptides.
- Responses showed a bell-shaped concentration–response to [Ca2+]i, peaking at ~500 nM; responses disappeared at higher [Ca2+]i, indicating distinct inhibitory mechanisms at high Ca2+.
- CaM is required: W7 abolished responses; CALP1 (Ca2+-independent CaM activator) alone triggered ATP release (EC50 ~87 µM, S-shaped curve), confirming CaM as an upstream node distinct from the inhibitory pathway active at high [Ca2+]i.
- CaMK-II is downstream of CaM: AIP and KN62 (both 1 µM) strongly inhibited A23187- and CALP1-triggered ATP release.
- p38 MAPK is downstream of CaMK-II but upstream of AA: SB202190 blocked A23187- and CALP1-triggered, but not AA-triggered, ATP release.
- AA signalling cascade is required: AACOCF3 (PLA2 inhibitor), baicalein (lipoxygenase inhibitor), and indomethacin (cyclo-oxygenase inhibitor) all strongly suppressed responses; exogenous AA potentiated and by itself triggered hemichannel responses.
- ROS and NO are downstream effectors: multiple antioxidants and NO synthase inhibition abolished responses across all three triggers.
- AA causes modest membrane depolarisation; cells with open hemichannels showed greater depolarisation, consistent with voltage contributing to channel opening.
- Positive feedback loops amplify responses: P2Y receptor blockade (PPADS, suramin) abolished AA-triggered ATP release; BAPTA-AM blocked AA-induced ATP release, indicating Ca2+ feedback from AA back to the start of the cascade.
- The full pathway was confirmed in primary rat cortical astrocytes stimulated with A23187 or glutamate (100 µM glutamate produced ~360–430 nM peak [Ca2+]i, within the activating range).

---

### Computational framework

Not applicable. This is a pharmacological/cell-biological study with no explicit computational or mathematical framework. The results constrain any future model of astrocytic purinergic signalling by defining the ordered sequence of kinase steps (CaM → CaMK-II → p38 MAPK → cPLA2 → AA → ROS/NO) that gates hemichannel opening, including the existence of competing positive and negative feedback loops producing a non-monotonic Ca2+ dose–response.

---

### Prevailing model of the system under study

The introduction situates the paper against the background that Cx43 hemichannels have low open probability under resting conditions but open in response to membrane depolarisation, low extracellular Ca2+, chemical hypoxia, and ROS. Previous work (including on Cx32) had shown that [Ca2+]i elevations could trigger hemichannel-mediated ATP release, and Ca2+–CaM interactions were known to regulate gap junctional communication. The implicit prevailing assumption challenged by this paper is that Ca2+ might act directly on the Cx43 protein to open hemichannels. The paper was also informed by the published finding that p38 MAPK stimulates hemichannel dye uptake in HeLa-Cx43 cells, but the upstream triggers and integration of this signal were not established.

---

### What this paper contributes

The paper shows definitively that Ca2+ does not act directly on Cx43 to open hemichannels, but instead routes through a multi-step kinase and lipid-signalling cascade: CaM → CaMK-II → p38 MAPK → cPLA2 → AA → (lipoxygenase/cyclo-oxygenase) → ROS → NO → Cx43 S-nitrosylation + membrane depolarisation. This ordered pathway, together with its multiple positive feedback loops, provides a mechanistic explanation for how physiological Ca2+ signals (including glutamate-induced oscillations in glial cells) translate into gliotransmitter ATP release. The bell-shaped concentration–response is now interpretable as the result of two competing mechanisms — CaM-dependent activation and a CaM-independent high-Ca2+ suppression — rather than a simple saturation effect.

---

### Brain regions & systems

This paper is primarily a cellular and molecular study conducted in glioma cell lines and primary cortical glial cells. No specific brain regions are investigated at a systems or circuit level.

- **Cerebral cortex (astrocytes)** — source of primary glial cell cultures used to validate pathway findings; the results are framed as relevant to astrocytic ATP release during neuronal activity (glutamate spillover in vivo).

---

### Mechanistic insight

The paper does not meet the bar for the Mechanistic insight section as defined. It presents a detailed signalling algorithm (the multi-step cascade from [Ca2+]i to hemichannel opening) and provides pharmacological evidence that is consistent with this ordering, but it does not provide neural recording data, imaging data in intact brain tissue, or lesion/pharmacology evidence that specifically discriminates this algorithm from alternatives in a neural context. All experiments are conducted in cell culture.

The pharmacological dissection does establish a plausible algorithmic account of the intracellular pathway, but the paper does not address Marr's implementational level (specific cell types, connectivity, biophysical mechanisms of the ion channel itself) nor does it provide in vivo neural data.

---

### Limitations & open questions

- All mechanistic work is in cell lines (C6 glioma) or primary cortical astrocyte cultures; in vivo relevance remains to be demonstrated.
- siRNA knockdown achieved only ~50% Cx43 protein reduction yet almost fully abolished functional responses, suggesting a non-linear threshold or membrane-trafficking effect that is not fully explained.
- The mechanism by which high [Ca2+]i suppresses responses (the descending limb of the bell curve) is identified as CaM-independent but not further characterised.
- The AA-induced membrane depolarisation observed is small relative to the voltages needed to open hemichannels in patch-clamp; how the combination of depolarisation, ROS, NO, and AA converges to a channel-opening threshold in intact cells is not resolved and the authors flag this for future electrophysiology.
- Whether the cascade operates identically in neurons, or in other brain regions beyond cortex, is not addressed.
- Positive feedback loops (P2Y receptor-mediated Ca2+ re-entry, hemichannel Ca2+ influx) complicate quantitative interpretation of inhibitor effects; thresholds and gain within the loop are not modelled.

---

### Connections & keywords

**Key citations**:
- De Vuyst et al. (2006) EMBO J — original demonstration that Ca2+ triggers Cx32 hemichannel opening
- Kang et al. (2008) J Neurosci — Cx43 hemichannels are permeable to ATP
- Schalper et al. (2008) Mol Biol Cell — p38 MAPK and hemichannel permeability
- Ramachandran et al. (2007) PLoS ONE — ROS and membrane depolarisation open hemichannels
- Contreras et al. (2002) PNAS — metabolic inhibition opens Cx43 hemichannels in astrocytes
- Pearson et al. (2005) Neuron — ATP release via hemichannels regulates retinal progenitor proliferation

**Named models or frameworks**: None explicitly named.

**Brain regions**: Cerebral cortex (primary astrocyte cultures).

**Keywords**: connexin 43 hemichannels, intracellular calcium signalling, ATP release, calmodulin, CaMK-II, p38 MAPK, phospholipase A2, arachidonic acid, reactive oxygen species, nitric oxide, gliotransmission, astrocytes
