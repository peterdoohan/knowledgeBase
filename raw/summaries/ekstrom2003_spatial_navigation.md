---
source_file: ekstrom2003_spatial_navigation.md
paper_id: ekstrom2003_spatial_navigation
title: "Cellular networks underlying human spatial navigation"
authors:
  - "Arne D. Ekstrom"
  - "Michael J. Kahana"
  - "Jeremy B. Caplan"
  - "Tony A. Fields"
  - "Eve A. Isham"
  - "Ehren L. Newman"
  - "Itzhak Fried"
year: 2003
journal: Nature
paper_type: empirical
contribution_type: empirical
species:
  - human
tasks:
  - virtual_navigation
methods:
  - electrophysiology
  - fmri
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - amygdala
keywords:
  - place_cells
  - human_hippocampus
  - spatial_navigation
  - virtual_reality
  - single_unit_recording
  - parahippocampal_region
  - view_responsive_cells
  - goal_responsive_cells
  - spatial_remapping
  - medial_temporal_lobe
  - allocentric_coding
  - intracranial_electrophysiology
  - cellular
  - networks
  - underlying
  - human
  - spatial
  - navigation
---

### One-line summary

Single-unit recordings in epilepsy patients navigating a virtual town reveal a dissociation between human hippocampal place cells (responding to spatial location) and parahippocampal view cells (responding to visual landmarks), with goal-responsive and conjunctive cells distributed broadly across frontal and temporal lobes.

---

### Background & motivation

Rodent place cells — hippocampal neurons that fire when an animal occupies a specific location — are a canonical example of a neural correlate of complex behaviour. Human neuroimaging consistently implicates the hippocampus and parahippocampal region in spatial navigation, but these regions also respond selectively to visual stimuli, leaving open whether human navigation relies on place coding analogous to that in rodents or on a distinct, visually driven mechanism. The paper fills this gap by using direct single-neuron recordings in humans during active virtual navigation, a method that could not be achieved with fMRI alone.

---

### Methods

- **Subjects**: 7 patients with pharmacologically intractable epilepsy undergoing invasive electrode monitoring for surgical planning (6 right-handed; epileptic foci in temporal and frontal lobes).
- **Task**: "Taxi driver" virtual town navigation game — subjects explored a town, picked up passengers appearing at random locations, and delivered them to one of three fixed labelled shops. Seven deliveries per shop per session.
- **Recordings**: 317 neurons recorded from depth electrodes with 40-µm platinum-iridium microwires; regions included hippocampus (n=67), parahippocampal region (n=54), amygdala (n=111), and frontal lobes (n=85). Signals bandpass-filtered 0.6–6 kHz; spikes isolated by inter-spike-interval distributions and waveform parameters.
- **Design control**: Subjects viewed shop front images before navigation to dissociate navigation-specific responses from pure object perception.
- **Analysis**: Three-way ANOVA (place 7×7 grid × view [5 levels] × goal [4 levels]) for each cell; place fields identified by spike-shuffling threshold (>95th percentile of shuffled firing rates); direction-dependence of place fields tested with t-test on firing-rate differences across opposing traversal directions.

---

### Key findings

- 42% of cells (117/279) responded significantly to at least one spatial factor (place, view, or goal).
- 26% responded to place, 12% to view, 21% to goal; 16% showed interaction effects only.
- Only 2% of cells responded to shop images viewed before navigation (below Type I error rate), ruling out pure visual object responses as an explanation for navigation-related activity.
- 11% of all cells (31/279) were bona fide place-selective (responding to place but not to view or place×view interaction); 24% of hippocampal cells met this criterion — significantly higher than in amygdala, parahippocampal region, or frontal lobes (χ²(3)=11.3, P<0.01).
- Place fields showed a mean 74% increase in firing rate over background; mean of 1.7 non-contiguous fields per cell.
- Place responses were non-directional: the distribution of firing-rate differences across opposing traversal directions was centred on zero and normal (t(32)=0.32, P=0.70).
- 26% of place-responsive cells (8/31) had place×goal interaction effects, firing in different locations depending on navigational goal.
- 88% of view cells (29/33) responded preferentially to a single object; location-independent view cells were clustered in the parahippocampal region (7/10 view cells there; χ²(3)=11.3, P<0.01).
- 21% of cells were goal-responsive, distributed across all recorded regions (not significantly clustered).
- 15% of goal-responsive cells also showed view×goal interaction effects (predominantly for shops, not passengers).
- Hippocampus vs. parahippocampal region dissociation for place vs. view was significant: χ²(1)=10.5, P<0.005.

---

### Computational framework

Not applicable in a formal sense. The paper is empirical and does not implement or fit a computational model. The findings are interpreted within a two-system framework of human spatial navigation (Burgess, Maguire & O'Keefe, 2002) in which the parahippocampal region constructs coarse allocentric representations from visual landmarks, and the hippocampus integrates these with context to form flexible, map-like representations. This framework is narrative rather than mathematical. The results could constrain cognitive map models (Tolman 1948; O'Keefe & Nadel 1978) and grid-cell/place-cell network models of navigation.

---

### Prevailing model of the system under study

Prior to this paper, rodent electrophysiology had firmly established that hippocampal pyramidal cells ("place cells") fire selectively at specific locations in an environment, providing an allocentric map. This had never been directly verified in single-unit recordings from humans. Human neuroimaging showed that the hippocampus and parahippocampal region are both active during navigation, but also that parahippocampal cortex responds strongly to visual scenes and landmarks (Epstein & Kanwisher 1998; Epstein et al. 2003). Primate single-unit work had suggested that the hippocampus might encode spatial *views* rather than locations per se (Georges-François, Rolls & Robertson 1999). The prevailing uncertainty was therefore whether human navigation is place-coded (as in rodents), view-coded (as in non-human primates), or driven primarily by visual recognition processes in the parahippocampal region.

---

### What this paper contributes

The paper provides the first direct single-unit evidence that human hippocampal neurons include bona fide place cells — cells that respond to location independently of view and of navigational goal — establishing that rodent-like place coding has a human homologue. Concurrently, it demonstrates that location-independent view-responsive cells are preferentially localised to the parahippocampal region, consistent with fMRI findings but now resolved at the cellular level. This double dissociation — hippocampus for place, parahippocampal region for view — supports a complementary-systems model of navigation. The additional discovery of goal-responsive and conjunctive (place×goal, view×goal) cells across the medial temporal and frontal lobes extends the picture beyond pure spatial coding to include goal-directed and contextual representations that could support flexible, task-driven navigation.

---

### Brain regions & systems

- **Hippocampus** — primary locus of place-selective cells (24% of recorded hippocampal neurons); also hosts goal-modulated place cells suggesting context-dependent spatial remapping.
- **Parahippocampal region** (including pre/parasubiculum, entorhinal, perirhinal, and parahippocampal cortices) — primary locus of location-independent view-responsive cells; proposed to extract coarse allocentric representations from visual landmarks.
- **Amygdala** — recorded from extensively (111 cells); shows spatial, view, and goal responses but no significant clustering of any cell type; some view×goal conjunctive cells observed.
- **Frontal lobes** (anterior cingulate, orbital frontal cortex, supplementary motor cortex) — substantial proportion of goal-responsive cells; also hosts place, view, and conjunctive cells, suggesting a role in representing navigational goals and planning.

---

### Mechanistic insight

The paper meets both criteria for the mechanistic insight bar: it identifies a candidate algorithm (place coding via spatially selective firing) and provides neural data (single-unit recordings during navigation) that specifically support it over alternative accounts (view-based coding, pure object perception). However, the implementational level is not directly addressed — no data are provided on specific cell types (e.g., pyramidal vs. interneuron beyond the firing-rate exclusion criterion), connectivity, neuromodulators, or biophysical mechanisms.

- **Computational**: The problem being solved is spatial self-localisation and navigation — computing "where am I?" and "how do I reach my goal?" in an allocentric reference frame.
- **Algorithmic**: The hippocampus represents location via cells with circumscribed, non-directional place fields that can be modulated by current navigational goal (contextual remapping). The parahippocampal region represents what is visible (landmark identity), independent of location, providing a view-based spatial index. Goal information is encoded throughout the medial temporal and frontal lobes, including conjunctive place×goal and view×goal representations.
- **Implementational**: Not directly addressed. The paper identifies anatomical clustering of cell types across regions but does not characterise circuit-level mechanisms, synaptic inputs, or the specific cell classes underlying place or view coding.

---

### Limitations & open questions

- Small patient sample (n=7); epilepsy and electrode placement may introduce biases in the cell populations sampled.
- The virtual town paradigm uses keyboard-based navigation without vestibular or proprioceptive cues, which may affect place field properties compared with real-world navigation.
- The study cannot adequately address bearing (head-direction) responses due to the experimental design; it is not possible to disambiguate place from heading within the virtual environment.
- It remains unclear whether the human place cells reported here are truly homologous to rodent place cells at the algorithmic and implementational levels, or whether they represent a functionally analogous but mechanistically distinct computation.
- The dissociation between hippocampal and parahippocampal function is anatomically coarse; the parahippocampal region as defined includes multiple subregions (entorhinal, perirhinal, parahippocampal cortex proper) whose individual contributions are not resolved.
- The directionality and stability of place fields across sessions or across different town configurations were not tested.
- Goal-related responses were not significantly clustered in any specific region, leaving the network architecture for goal representation unresolved.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Dostrovsky (1971) — original rat hippocampal place cell discovery
- Muller, Kubie & Ranck (1987) — spatial firing patterns of hippocampal cells
- Wilson & McNaughton (1993) — hippocampal ensemble coding for space
- Maguire et al. (1998) — human navigation network (fMRI)
- Epstein & Kanwisher (1998) — parahippocampal place area (PPA)
- Georges-François, Rolls & Robertson (1999) — spatial view cells in primate hippocampus
- Burgess, Maguire & O'Keefe (2002) — human hippocampus and spatial/episodic memory model
- O'Keefe & Nadel (1978) — The Hippocampus as a Cognitive Map

**Named models or frameworks**:
- Taxi driver virtual navigation paradigm
- Cognitive map theory (Tolman 1948; O'Keefe & Nadel 1978)
- Two-system navigation model (Burgess, Maguire & O'Keefe 2002)

**Brain regions**:
- Hippocampus
- Parahippocampal region (entorhinal, perirhinal, parahippocampal cortex, pre/parasubiculum)
- Amygdala
- Anterior cingulate cortex
- Orbital frontal cortex
- Supplementary motor cortex

**Keywords**: place cells, human hippocampus, spatial navigation, virtual reality, single-unit recording, parahippocampal region, view-responsive cells, goal-responsive cells, spatial remapping, medial temporal lobe, allocentric coding, intracranial electrophysiology
