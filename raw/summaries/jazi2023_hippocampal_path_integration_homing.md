---
source_file: jazi2023_hippocampal_path_integration_homing.md
paper_id: jazi2023_hippocampal_path_integration_homing
title: "Hippocampal firing fields anchored to a moving object predict homing direction during path-integration-based behavior"
authors:
  - "Maryam Najafian Jazi"
  - "Adrian Tymorek"
  - "Ting-Yun Yen"
  - "Felix Jose Kavarayil"
  - "Moritz Stingl"
  - "Sherman Richard Chau"
  - "Benay Baskurt"
  - "Celia García Vilela"
  - "Kevin Allen"
year: 2023
journal: "Nature Communications"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
tasks:
  - foraging_task
methods:
  - electrophysiology
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - retrosplenial_cortex
frameworks:
  - reinforcement_learning
keywords:
  - path_integration
  - homing_behaviour
  - hippocampal_place_cells
  - object_anchored_firing_fields
  - lever_anchored_cells
  - allocentric_reference_frame
  - hippocampal_remapping
  - task_dependent_spatial_coding
  - directional_trial_drift
  - ca1_pyramidal_cells
  - navigation
  - self_motion_cues
  - hippocampal
  - firing
  - fields
  - anchored
  - moving
  - object
  - predict
  - homing
---

### One-line summary

Hippocampal CA1 neurons in mice develop firing fields anchored to a variably positioned task-relevant object (lever), and the directional tuning of these fields on individual trials predicts the animal's homing direction during path-integration-based navigation in darkness.

---

### Background & motivation

Path integration (PI) — the process of using self-motion cues to track position and plan a return trajectory — depends on hippocampal and parahippocampal circuits, yet the specific firing patterns that hippocampal neurons adopt during active PI-based homing had not been characterised. Most prior work studied place cells during random foraging rather than goal-directed homing, leaving open whether PI-relevant navigational demands reshape hippocampal representations and whether cell activity in those conditions predicts behavioural accuracy. Existing homing paradigms (e.g., the food-carrying task) also yield too few trials per session to statistically link single-trial neural activity to homing outcomes. This paper fills both gaps by introducing a high-throughput automated paradigm and recording CA1 neurons during it.

---

### Methods

- **Task (AutoPI):** Male C57BL/6 mice (n = 13 behavioural, n = 9 electrophysiological; 3–6 months old) learned to leave a home base, navigate to a randomly repositioned lever on a circular arena (diameter 80 cm), press it, and return for a food reward. Sessions alternated between light and dark trials. Mice performed ~75 trials/hour (up to 150/day).
- **Behavioural measures:** Homing error at the arena periphery; search and homing path length, duration, speed, and complexity. Correlation of search path length/duration with homing error used to verify PI.
- **Electrophysiology:** Silicon probe recordings (Buzsaki32, NeuroNexus) targeting dorsal CA1; 438 putative pyramidal cells identified via spike autocorrelation and waveform clustering (Kilosort2 + Phy). Recordings during 30-min random foraging, rest, and ~90–120 min AutoPI task.
- **Neural analyses:** 2D firing rate maps; trial matrices of firing rate as a function of y-axis coordinate or distance/direction from the lever box; three directional reference frames (Cardinal, Bridge, Lever); lever-box-anchored field classification by three criteria (peak within 10 cm, peak rate > 7.5 Hz, map stability > 0.4); circular–circular correlation between single-trial firing direction drift and homing direction.
- **Controls:** Arena rotation between trials (prevents odor re-use); airflow above arena (n = 6 mice, tests olfactory guidance); white noise throughout (masks auditory cues).

---

### Key findings

- Homing error in darkness was significantly above chance but significantly below chance-level (median 18.15° vs. 90° chance), and correlated positively with search path length and duration, confirming path integration.
- Near-complete remapping of hippocampal ensembles occurred between random foraging and the AutoPI task on the same physical arena (map similarity r = 0.02, not significant, vs. r = 0.66 within random foraging).
- Further remapping was observed between light and dark trials, and between search and homing epochs within the task.
- ~25% of reliably active pyramidal cells had firing fields anchored to the lever box position, firing in a fixed direction relative to the lever box in a Cardinal (world-centred) reference frame — not a lever-relative or bridge-relative frame.
- During dark trials, directional selectivity of lever-box-anchored fields was reduced after longer/more complex search paths (trial matrix correlation lower for long vs. short search paths; peak rate lower; results consistent with path integration error accumulation).
- Lever-anchored field directional stability was higher on trials with accurate homing (lower homing error) than inaccurate homing (mean vector length and trial matrix correlation both significantly larger for accurate trials, P < 0.05 and P = 0.0078 respectively).
- In 24.1% of lever-anchored neurons (26.9% total), the single-trial directional drift of the firing field was significantly positively correlated with homing direction (clockwise drift → clockwise homing rotation); at the population level this shift was highly significant (P = 4.05 × 10⁻⁸).
- The relationship held even when lever position was restricted to near-arena-center trials, ruling out lever position as a confound.

---

### Computational framework

**Reinforcement learning / path integration.** The paper implicitly uses a path integration model in which a neural integrator accumulates noisy self-motion signals (linear and angular) during the search phase, building an estimate of allocentric position and heading relative to the starting point. Key variables: estimated heading direction (updated via angular PI), estimated position (via linear PI), accumulated error (grows with path length/duration). The framework predicts that (i) longer search paths produce larger homing errors, and (ii) neural representations tied to directional estimates around the lever box should degrade after longer paths. Both predictions are confirmed. The directional lever-box-anchored cells are interpreted as encoding heading direction in a cardinal reference frame, with their trial-to-trial variability reflecting drift in the angular PI process after the lever is encountered.

---

### Prevailing model of the system under study

The hippocampus is classically understood as supporting a world-centred cognitive map via place cells that fire at fixed locations regardless of task demands. Prior to this paper, it was debated whether hippocampal representations during PI-based homing would reflect a single world-centred reference frame (as in standard random foraging) or would incorporate additional task-relevant reference frames. The single prior study of hippocampal/parahippocampal activity during homing (Valerio & Taube, head-direction cells in thalamus) showed that HD cell drift predicts homing error, but hippocampal place cell activity during active homing was largely uncharacterised. A subset of studies had shown that some hippocampal cells can adopt goal/object-centred reference frames during navigation toward variably located goals, but whether this would hold during PI-based homing (without landmarks) and whether such cells would predict homing outcomes was unknown.

---

### What this paper contributes

This paper establishes that hippocampal CA1 place cells undergo context-dependent remapping when a PI-based homing demand is imposed — even when the physical environment is unchanged — and that a substantial fraction (~25%) adopt an object-centred reference frame anchored to the task-relevant lever. Crucially, the directional component of these fields is expressed in a Cardinal (allocentric) frame, not a lever-intrinsic frame, showing that hippocampal object-anchored representations are tied to the world-directional system (likely via head-direction inputs from MEC). Most importantly, the paper provides the first direct evidence that trial-by-trial variation in hippocampal firing direction around a task-relevant object predicts the animal's subsequent homing direction, linking a specific hippocampal representation to a navigational behavioural outcome under PI conditions. This advances the prevailing model from "hippocampus is needed for homing" (lesion level) to "a specific sub-population of hippocampal cells encodes the directional information used to plan the homing trajectory."

---

### Brain regions & systems

- **Hippocampus (CA1)** — primary recording site; locus of lever-box-anchored firing fields and task-induced remapping; proposed contributor to homing direction computation via cardinal-frame directional coding around task-relevant objects.
- **Medial entorhinal cortex (MEC)** — discussed as likely source of directional inputs (head-direction cells, object-vector cells, border cells) to CA1; not recorded in this study.
- **Parietal cortex / retrosplenial cortex** — mentioned in introduction as regions whose lesions impair H-PI; not studied here.
- **Thalamic head-direction system** — cited as precedent (Valerio & Taube) where HD cell drift predicts homing error; not recorded here.

---

### Mechanistic insight

The paper meets criterion 1 (a specific algorithm: angular path integration updating directional firing fields around a task-relevant object) and partially meets criterion 2 (neural data from CA1 recordings that support this algorithm). The evidence is correlational rather than causal, and no alternative algorithms are formally excluded, but the link between single-trial firing direction drift and homing direction is a strong behavioural-neural coupling.

- **Computational level:** The problem being solved is estimating the home-base direction after an extended outward search using only self-motion cues. The brain must track its own rotational trajectory (angular PI) to maintain an allocentric heading estimate at the moment of committing to a return path.
- **Algorithmic level:** CA1 neurons fire in a cardinal-frame directional zone around the lever box, with peak firing direction varying trial-to-trial. This trial drift encodes (or reflects) accumulated angular PI error. The direction of peak activity at the lever box serves as a read-out of the animal's internal estimate of its orientation, which maps onto homing direction.
- **Implementational level:** Not addressed. The paper discusses MEC (object-vector cells, border cells, HD cells) as plausible upstream sources of the directional signal, but no recordings from MEC or from identified cell types (e.g., interneurons, pyramidal subtypes) were made. Physical implementation remains uncharacterised.

**Bonus:** No specific cell types, neuromodulators, or biophysical mechanisms are studied.

---

### Limitations & open questions

- **Causality absent:** The correlation between lever-anchored field direction and homing direction does not prove that these cells drive homing. Optogenetic or chemogenetic manipulation of lever-anchored cell activity during the task would be needed.
- **Regression slope < 1:** Trial drift in neural firing direction is systematically smaller than the change in homing direction, meaning the neural signal is not a perfect read-out; additional factors must influence homing.
- **MEC recordings absent:** The circuit mechanism upstream of the lever-anchored fields is speculative. Whether MEC object-vector cells, HD cells, or border cells provide the critical input is unknown.
- **Single sex:** Only male mice used; generalisability to females is untested.
- **Head-direction system not recorded:** It is unclear how the lever-anchored fields relate quantitatively to HD cell activity in the same animals.
- **Dark trials only partially involve pure PI:** The paper controls for odour and sound but cannot exclude all non-PI cues.
- **Population coding not explored:** Only single-cell correlations to homing are reported; whether a population vector or ensemble pattern would better predict homing is not examined.
- **Developmental and disease relevance:** The paper notes PI is impaired early in Alzheimer's disease; whether AutoPI-task lever-anchored cells are selectively disrupted in relevant models is a future question.

---

### Connections & keywords

**Key citations:**
- Valerio & Taube (thalamic HD cell drift predicts homing error — prior study of neural activity during H-PI)
- McNaughton et al. 2006 (path integration and the neural basis of the cognitive map; Nat. Rev. Neurosci.)
- Maaswinkel, Jarrard & Whishaw 1999 (hippocampal lesions impair H-PI)
- Rolls & O'Mara / Gothard et al. 1996 (hippocampal cells firing relative to a moveable goal)
- Deshmukh & Knierim; Høydal et al. (landmark-vector cells / object-vector cells in hippocampus and MEC)
- Allen et al. 2014 (GluA1 KO, impaired grid cell periodicity and path integration)

**Named models or frameworks:**
- AutoPI task (Automated Path Integration task — novel paradigm introduced in this paper)
- Path integration (H-PI, homing-based path integration)
- Cardinal / Bridge / Lever reference frames (directional reference frame analysis)
- Lever-box-anchored firing field (novel cell class defined in this paper)

**Brain regions:**
- Hippocampus (CA1)
- Medial entorhinal cortex (MEC)
- Retrosplenial cortex
- Parietal cortex
- Anterior thalamus (head-direction system)

**Keywords:**
- path integration
- homing behaviour
- hippocampal place cells
- object-anchored firing fields
- lever-anchored cells
- allocentric reference frame
- hippocampal remapping
- task-dependent spatial coding
- directional trial drift
- CA1 pyramidal cells
- navigation
- self-motion cues
