---
source_file: "ferreira2018_supraspinal_locomotion.md"
paper_id: "ferreira2018_supraspinal_locomotion"
title: "Connecting Circuits for Supraspinal Control of Locomotion"
authors: "Manuel J. Ferreira-Pinto, Ludwig Ruder, Paolo Capelli, Silvia Arber"
year: 2018
journal: "Neuron"
paper_type: "review"
contribution_type: "review"
species: ["mouse", "rat"]
methods: ["calcium_imaging", "optogenetics"]
brain_regions: ["infralimbic_cortex", "striatum", "ventral_tegmental_area", "substantia_nigra", "thalamus", "amygdala", "visual_cortex", "periaqueductal_gray"]
keywords: ["connecting", "circuits", "supraspinal", "control", "locomotion"]
key_citations: ["roseberry2016_basal_ganglia_motor"]
---

### One-line summary

This review synthesises recent cell-type-resolved work on the supraspinal circuits that initiate, speed-regulate, and terminate locomotion, proposing that a hierarchically organised chain from forebrain/midbrain context-computing structures through the mesencephalic locomotor region (MLR) to reticulospinal neurons in the caudal brainstem implements the full behavioural range from quiet exploration to high-speed escape.

---

### Background & motivation

Locomotion is controlled by distributed circuits spanning the spinal cord, brainstem, midbrain, and forebrain, but while spinal central pattern generators (CPGs) are fairly well characterised, the mechanisms by which supraspinal structures initiate, tune, and terminate locomotion have remained opaque. Classical approaches (lesions, electrical stimulation, pharmacology) identified key regions — notably the MLR — but could not resolve the cellular identities, connectivity, or functional logic of these circuits. The advent of viral and genetic tools for cell-type-specific manipulation in mice has now made such resolution possible, and this review synthesises the resulting literature to articulate an emerging organisational logic for supraspinal locomotor control.

---

### Methods

This is a narrative review with a selective focus on recent (primarily 2014–2018) cell-type-level optogenetic, chemogenetic, calcium-imaging, and anatomical tracing studies in mice, with supporting material from classical cat/rat electrical stimulation work and invertebrate/lamprey studies for evolutionary context. No formal inclusion criteria or meta-analytic statistics are used.

- Coverage spans spinal circuit diversity, brainstem reticulospinal identity, MLR cellular organisation, basal ganglia locomotor circuits, and forebrain/hypothalamic/amygdalar/collicular influences on context-specific locomotion.
- The review explicitly excludes cerebellum and motor cortex, which are noted as contributors not covered here.
- Synthesis approach: mechanistic narrative organised around the three temporal phases of locomotion (initiation, ongoing regulation, termination) and regulatory categories (exploration, escape, hunting/predation).

---

### Key findings

For **reviews**, the major conclusions drawn across the literature:

**Spinal circuits**
- Spinal interneuron diversity is higher than previously appreciated; speed-dependent V2a submodules in zebrafish (and likely mice) match motor neuron subtypes, and V0d/V0v subpopulations differentially regulate gait transitions with speed.
- Long descending spinal projection neurons (cervical-to-lumbar) are critical for fore-hindlimb coordination at high speeds and receive input from many supraspinal locomotor centers.

**Brainstem (MLR and reticular formation)**
- Glutamatergic (vGlut2) neurons in the MLR are the cellular substrate of the functionally defined locomotion-promoting MLR site; optogenetic activation elicits locomotion with intensity-speed scaling.
- Within the MLR, CnF-vGlut2 neurons mediate high-speed, short-latency, synchronous-gait locomotion consistent with escape, while PPN-vGlut2 neurons are associated with low-speed, longer-latency, alternating-gait exploratory locomotion — though results on PPN-vGlut2 across studies are partially discordant.
- Cholinergic PPN neurons have a modulatory rather than driver role, acting partly via direct modulation of SNc/VTA dopamine neurons.
- GABAergic MLR neurons suppress locomotion via local inhibition of glutamatergic MLR neurons.
- In the caudal brainstem, LPGi-vGlut2 neurons (lateral paragigantocellular nucleus) are a critical relay for high-speed locomotor signals from the MLR to the spinal cord; selective ablation impairs high-speed but not low-speed locomotion.
- Separate caudal brainstem populations (including glycinergic LPGi and Gi neurons, and Chx10+ excitatory rostral medullary/pontine neurons) mediate behavioral arrest, each via distinct downstream pathways.
- In lamprey, reticular formation neurons divide into "start," "maintain," and "stop" cell types with distinct response profiles during MLR stimulation.

**Basal ganglia**
- Striatal D1-SPN and D2-SPN activation exerts opposing effects on glutamatergic MLR neurons (and thus locomotion) via the SNr→PPN pathway.
- Both D1- and D2-SPNs are active during movement initiation and execution; dedicated spatially compact ensembles encoding locomotion vs. other actions exist within the striatum.
- SNc dopamine signals are phasic before movement onset (not just tonic), encode movement vigor rather than locomotion specifically, and promote initiation probability; this signal is disrupted in Parkinson's disease models.

**Context-dependent (forebrain/midbrain) circuits**
- Defensive escape is mediated by dlPAG/dPAG glutamatergic neurons (targeting likely CnF/LPGi); freezing by l/vlPAG glutamatergic neurons (with CeA providing long-range inhibitory gating).
- Intra-PAG GABAergic interneurons act as a switch ensuring flight and freezing are mutually exclusive.
- Predatory hunting suppresses l/vlPAG glutamatergic neurons via GABAergic CeA and LH projections.
- Superior colliculus parvalbumin neurons can bypass the PAG to elicit escape (via parabigeminal nucleus) and freezing (via LPTN) in response to looming visual stimuli.
- VMHdm/c SF1 neurons promote either freezing or escape depending on activation magnitude and shelter availability.

**Key open questions identified**: identity of brainstem relay neurons for low-speed exploration (no single clear population found); precise downstream targets of escape-mediating PAG neurons; how BG-computed vigor is translated into specific speeds; circuit basis of behavioral choice between locomotion and competing actions.

---

### Computational framework

Not applicable in a formal sense. The paper does not employ or propose a computational model with defined variables, equations, or inference procedures.

The review is framed in terms of **circuit-level control logic**: a hierarchical series of input-output transformations in which high-level context signals (emotional valence, internal needs, volitional goals) are computed by forebrain structures and progressively funneled through the PAG and BG into the MLR, which then recruits specific reticulospinal populations that set locomotor speed and gait. This is consistent with a control-theoretic or action-selection framework, in which:
- Forebrain/midbrain structures determine *whether* and *why* to locomote (context selection).
- The MLR determines *how fast* and *what gait* (speed/vigor encoding).
- Reticulospinal and CPG circuits determine *how* (execution).

The closest explicit computational concept referenced is the BG direct/indirect pathway model (Albin/DeLong prokinetic/antikinetic framework), which the review treats as an oversimplification, updating it with evidence that both pathways are co-active and their net effect is ensemble- and target-specific.

---

### Prevailing model of the system under study

Before the reviewed work, the field operated with a region-based model of supraspinal locomotor control derived mainly from electrical stimulation and pharmacological studies in cats and rats:

- The MLR (broadly comprising CnF and PPN) was a functionally defined site that, when electrically stimulated, reliably elicited graded locomotion; it was thought to receive context information from the forebrain and transmit locomotor commands via reticulospinal neurons in the ventromedial medulla to spinal CPGs.
- The CnF was associated with defensive/escape locomotion; the PPN with exploratory locomotion selected by the basal ganglia, but the distinction was blurry and based on gross stimulation patterns.
- The reticular formation was presumed to contain the key MLR→spinal relay neurons, but electrical microstimulation in the medulla produced variable results, and the specific cell types involved were unknown.
- The BG were classically modelled as two parallel pathways (direct: prokinetic; indirect: antikinetic) with tonic SNr inhibition of MLR neurons as the descending gate for movement initiation.
- Dopamine was understood primarily as a tonic modulator of striatal D1/D2 balance (not as a fast, phasic, vigor-encoding signal).

The introduction frames the key gap as: technological limitations preventing identification of specific neuronal populations — meaning all prior conclusions were at the level of brain regions and neurotransmitter classes, not defined cell types with known connectivity.

---

### What this paper contributes

The review establishes that modern cell-type-resolved tools (optogenetics, viral tracing, calcium imaging, genetic intersectional strategies) have fundamentally changed what can be claimed about supraspinal locomotor control:

1. **Cell-type specificity replaces region-based logic**: within any given brain region (MLR, reticular formation, PAG, striatum), intermingled cell types with opposing functions exist. Location alone does not predict function; neurotransmitter identity and connectivity are necessary and sometimes insufficient.

2. **A speed-segregated brainstem hierarchy is now supported**: CnF→LPGi-vGlut2 constitutes a relatively well-characterised circuit for high-speed/escape locomotion. The equivalent circuit for low-speed exploration remains to be identified.

3. **BG locomotor control is more nuanced than the two-pathway model**: both D1- and D2-SPN ensembles contribute to movement initiation; SNr effects on MLR neurons are heterogeneous; dopamine acts as a fast phasic vigor signal, not just a tonic D1/D2 modulator.

4. **Context-specific locomotion (escape, freeze, hunt) maps onto specific cell types in PAG, hypothalamus, CeA, and superior colliculus** with partially resolved downstream connectivity to MLR/brainstem populations.

5. **The emerging principle**: supraspinal locomotor circuits are organised in a hierarchical manner with dedicated neuronal populations at each level encoding specific locomotor attributes (initiation latency, speed, gait, direction, behavioral context), and these populations are embedded in specific input-output matrices that align with behavioral need.

---

### Brain regions & systems

- **Spinal cord (lumbar and cervical CPG circuits)** — executive circuits for rhythm and pattern generation; subject of extensive prior review; context here is as the downstream target of supraspinal commands.
- **Lateral paragigantocellular nucleus (LPGi), caudal medulla** — glutamatergic LPGi-vGlut2 neurons are a critical relay for high-speed locomotor drive from MLR to spinal cord; separate glycinergic LPGi neurons mediate atonia/arrest.
- **Gigantocellular nucleus (Gi) and subdomains (GiA, GiV, Mc), caudal brainstem** — reticulospinal regions with locomotion-stopping populations; Gi-Chx10 excitatory neurons halt locomotion via spinal glycinergic interneurons.
- **Pontine reticular formation** — glycinergic neurons here project ascendingly to the intralaminar thalamus and can halt locomotion via thalamic modulation.
- **Mesencephalic locomotor region (MLR)** — functionally defined midbrain region; CnF-vGlut2 neurons drive high-speed escape locomotion; PPN-vGlut2 neurons associated with low-speed exploration; cholinergic PPN neurons are modulatory; GABAergic MLR neurons are inhibitory.
- **Cuneiform nucleus (CnF)** — key subdivision of MLR for high-speed/defensive locomotion; receives input from PAG and inferior colliculus.
- **Pedunculopontine nucleus (PPN)** — subdivision of MLR associated with voluntary/exploratory locomotion; receives basal ganglia input; also sends ascending projections to BG, thalamus, VTA/SNc, basal forebrain.
- **Periaqueductal gray (PAG)** — midbrain intermediary between forebrain threat/need computation and brainstem locomotor execution; dlPAG mediates escape; l/vlPAG mediates freezing and is suppressed during hunting; intra-PAG GABAergic interneurons act as a flight/freeze switch.
- **Substantia nigra pars reticulata (SNr)** — BG output structure providing tonic GABAergic inhibition of MLR (primarily PPN); locomotion-predictive SNr neurons are disinhibited by D1-SPN activation.
- **Striatum (dorsal)** — BG input structure; D1-SPN ensembles promote locomotion; D2-SPN ensembles suppress it; spatially compact ensembles are action-specific.
- **Substantia nigra pars compacta (SNc)** — dopaminergic input to dorsal striatum; phasic activity before movement onset encodes vigor and promotes initiation probability.
- **Ventral tegmental area (VTA)** — dopaminergic midbrain nucleus; target of PPN cholinergic projections; segregated from SNc in locomotor vs. reward encoding.
- **Dorsomedial/central ventromedial hypothalamus (VMHdm/c, SF1 neurons)** — compute defensive response type (escape vs. freeze) based on threat magnitude and shelter availability.
- **Lateral hypothalamus (LH)** — glutamatergic neurons promote escape; GABAergic neurons promote predatory pursuit and capture; projects to PAG.
- **Central amygdala (CeA)** — GABAergic neurons encode predatory phases (pursuit, capture, consumption) and promote freezing; converges on l/vlPAG.
- **Superior colliculus (SC)** — processes visual threat (looming stimuli); parvalbumin+ neurons drive escape via parabigeminal nucleus and freezing via LPTN, bypassing PAG.
- **Intralaminar thalamic nucleus (LPTN/IL)** — receives ascending inhibitory projections from pontine reticular formation (locomotion arrest) and from SC parvalbumin neurons (freezing).
- **Basal forebrain** — receives ascending projections from PPN-vGlut2 neurons, mediates gain modulation of visual cortex during locomotion.

---

### Mechanistic insight

The paper partially meets the mechanistic bar for certain circuits but not at a review-level synthesis.

For the **CnF→LPGi circuit for high-speed locomotion**, the review assembles evidence that approaches mechanistic completeness:
- **Computational**: the problem is translating a contextual "escape" signal into high-speed synchronous-gait locomotion with short latency.
- **Algorithmic**: CnF-vGlut2 neurons receive threat-related input (from PAG and inferior colliculus), fire with locomotor state and speed, and project to LPGi-vGlut2 neurons, which in turn target intermediate-lamina spinal interneurons (CPG rhythm/pattern circuits) rather than motor neurons directly; a parallel inhibitory LPGi pathway targets motor neurons and mediates atonia.
- **Implementational**: identified at the level of glutamatergic vs. GABAergic/glycinergic cell types with distinct projection targets; specific cell types (Chx10 for halt neurons, vGlut2 for speed neurons) identified via developmental origin. Biophysical mechanisms (channel-level or synaptic plasticity) are not addressed.

The paper does not meet the full bar for the BG→MLR or PAG→brainstem circuits, where the specific algorithms and the neural data directly testing them against alternatives remain incomplete. The review explicitly notes these as open questions.

---

### Limitations & open questions

- The cellular identity of brainstem relay neurons for low-speed exploratory locomotion (PPN-equivalent relay) has not been found; this circuit may be distributed or require finer dissection.
- Discordant results on PPN-vGlut2 neurons across two major studies (Caggiano et al. vs. Josset et al.) are unresolved; subtle targeting differences or unidentified cell-type diversity are offered as possible explanations.
- The precise downstream targets of escape-mediating d/dlPAG neurons in the brainstem remain undescribed.
- Whether l/vlPAG freeze neurons suppressed during predation are the same neurons active during freezing is unresolved.
- How BG-computed vigor (dopamine × striatal ensemble activity) is translated into specific locomotor speeds by downstream brainstem centers is not yet understood.
- The circuit mechanisms for behavioral choice between locomotion and competing movements (grooming, reaching, etc.) are unaddressed.
- Cerebellum and motor cortex are explicitly excluded despite their known contributions.
- Most evidence is from mice; cross-species generalisability, especially to humans, is not fully established.
- The review acknowledges a citation strategy biased toward recent optogenetic/genetic studies, omitting much classical and older literature.

---

### Connections & keywords

**Key citations**:
- Caggiano et al. (2018) Nature — MLR speed/gait subdivision, CnF vs. PPN
- Capelli et al. (2017) Nature — LPGi-vGlut2 speed control circuits
- Roseberry et al. (2016) Cell — BG→MLR cell-type control
- Bouvier et al. (2015) Cell — Chx10 brainstem halt neurons
- Tovote et al. (2016) Nature — PAG midbrain circuits for defensive behavior
- Kiehn (2016) Nat Rev Neurosci — spinal CPG review
- da Silva et al. (2018) Nature — dopamine vigor and initiation
- Howe & Dombeck (2016) Nature — dopaminergic axon calcium imaging
- Han et al. (2017) Cell — CeA predatory hunting circuits
- Li et al. (2018) Neuron — hypothalamic predation/evasion circuits
- Shang et al. (2018) Nat Commun — SC parvalbumin escape/freeze circuits
- Evans et al. (2018) Nature — dPAG escape threshold and looming stimuli
- Ruder et al. (2016) Neuron — long spinal projection neurons
- Juvin et al. (2016) Cell Rep — lamprey reticulospinal start/stop cells
- Shik & Orlovsky (1976) Physiol Rev — original MLR characterisation

**Named models or frameworks**:
- Mesencephalic locomotor region (MLR)
- Central pattern generator (CPG)
- Basal ganglia direct/indirect pathway model (Albin/DeLong)
- Behavioral arrest/halt circuit (Bouvier/Capelli)
- Hierarchical supraspinal locomotor control model (Jordan 1998, updated)

**Brain regions**: spinal cord, LPGi, Gi, GiA, GiV, Mc, pontine reticular formation, CnF, PPN, MLR, PAG (dlPAG, l/vlPAG, dPAG), SNr, SNc, VTA, striatum, dorsal striatum, VMHdm/c, lateral hypothalamus, central amygdala, superior colliculus, intralaminar thalamus (LPTN/IL), basal forebrain

**Keywords**: supraspinal locomotor control, mesencephalic locomotor region, reticulospinal neurons, optogenetics cell-type specificity, locomotor speed regulation, cuneiform nucleus, pedunculopontine nucleus, basal ganglia locomotion, dopamine movement vigor, escape freezing PAG circuits, central pattern generator descending control, predatory hunting circuits
