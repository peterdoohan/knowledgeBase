---
source_file: leblond2003_locomotion_spinal.md
title: "Treadmill Locomotion in the Intact and Spinal Mouse"
authors: Hugues Leblond, Marion L'Espérance, Didier Orsal, Serge Rossignol
year: 2003
journal: The Journal of Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Adult mice can spontaneously re-express coordinated hindlimb locomotion on a treadmill within 14 days of complete thoracic spinal cord transection, without pharmacological treatment, demonstrating that the mouse lumbar spinal cord contains a functional central pattern generator for locomotion.

---

### Background & motivation

The ability of the spinal cord to generate locomotor movements after complete thoracic transection is well established in cats but not in adult rats, which require pharmacological or cellular interventions to recover hindlimb locomotion. Mice are increasingly used in spinal cord injury research because of their well-characterised genetics, yet detailed kinematic and EMG baselines for normal mouse locomotion were lacking. It was also unknown whether adult mice, like cats but unlike adult rats, could express spontaneous spinal locomotion after a complete lesion. Establishing these baselines and determining the locomotor capacity of the spinal mouse were necessary prerequisites for evaluating experimental therapies in this species.

---

### Methods

- **Subject population**: 23 adult mice (CD1, BALB/c, C57BL/6 strains; 25–30 g); 10 intact mice for baseline characterisation and 13 CD1 mice for spinalization experiments (11 trained, 2 untrained).
- **Surgical procedure**: Complete spinal cord transection at the T8 level under isoflurane anaesthesia; one mouse received a second transection at the same site to rule out axonal regrowth.
- **Treadmill locomotion**: Mice walked on a motor-driven treadmill belt (0.07–0.2 m/sec); spinal mice were supported at the tail and, initially, hindquarters.
- **Kinematics**: Side-view video (30 fps, de-interlaced to 60 fields/sec) with reflective markers at iliac crest, femoral head, knee (corrected by triangulation), ankle, and metatarsophalangeal joint; custom software extracted joint angles and stick diagrams.
- **EMG**: Chronic microwire electrodes implanted in vastus lateralis (VL) and tibialis anterior (TA) of both hindlimbs in one mouse; signals differentially amplified (100 Hz–3 kHz) and digitised at 1 kHz, synchronised with video.
- **Interlimb coupling**: Gait diagrams and coupling phases calculated for homologous, homolateral, and diagonal limb pairs; circular statistics used for phase comparisons.
- **Statistics**: Student's t-test for intact vs. spinal comparisons; circular statistics (Zar, 1996) for phase values.

---

### Key findings

- Intact mice walked reliably on the treadmill across strains; mean step cycle duration ranged from ~253 ms (CD1) to ~403 ms (C57BL/6) at 0.15 m/sec, with stance duration varying with speed and swing duration (~100–180 ms) remaining relatively invariant.
- Homologous limb coupling was ~0.5 (strict out-of-phase alternation) for both girdles; homolateral forelimb–hindlimb coupling ranged 0.25–0.45 and was speed-dependent.
- Joint angular excursions (hip ~16°, knee ~34°, ankle ~28°) and the Philippson step-cycle subphases (F, E1, E2, E3) were clearly present and consistent across speeds.
- Chronic EMG implants (~0.30 g) did not impair locomotion, enabling future within-animal before/after spinalization comparisons.
- After complete T8 transection, 10 of 13 spinal mice re-expressed hindlimb locomotion within 14 days without pharmacological treatment; 2 untrained mice also recovered, and 2 mice never recovered.
- Recovery followed a stereotyped sequence: no movement for days 1–5; occasional flexions from day 6; intralimb kinematics resembling intact mice restored by ~day 12; proper out-of-phase hindlimb alternation (phase ~0.46 ± 0.09, not significantly different from intact) by day 14.
- Mean step cycle duration of spinal mice (700 ± 64 ms) was significantly longer than intact mice (500 ± 94 ms; p < 0.0005), driven by prolonged stance rather than swing.
- A second spinalization at the same level did not disrupt or reverse locomotor recovery, ruling out axonal regrowth as the cause.
- Homolateral forelimb–hindlimb coupling was permanently lost after complete transection; visual observation alone was insufficient to detect this loss.

---

### Computational framework

Not applicable. The paper is purely empirical with no explicit computational framework. The results constrain central pattern generator (CPG) models of spinal locomotion: specifically, they provide in vivo evidence that the lumbar spinal CPG in adult mice is intrinsically capable of generating rhythmic, coordinated hindlimb stepping without supraspinal input or pharmacological drive. The finding that intralimb coordination recovers before interlimb alternation suggests a hierarchical organisation within the spinal locomotor network, with limb-specific rhythm generators becoming functional before their coupling circuits.

---

### Prevailing model of the system under study

Based on the introduction, the prevailing understanding at the time was that the lumbosacral spinal cord of many species (most thoroughly studied in the cat) contains a central pattern generator capable of producing hindlimb locomotion after complete spinal transection. However, adult rats were known to be unable to recover sustained hindlimb locomotion without pharmacological or cellular interventions, suggesting species differences in CPG autonomy. Neonatal in vitro preparations of the mouse spinal cord had demonstrated rhythmic motor output, but whether the adult mouse could express spinal locomotion in vivo was unknown. The field also lacked quantitative kinematic and EMG baselines for normal mouse locomotion, and behavioural assessments (such as open-field scoring analogous to the BBB scale) were considered potentially unreliable for detecting true locomotor patterns vs. isolated reflex movements.

---

### What this paper contributes

The paper establishes that the adult mouse lumbar spinal cord contains a CPG that can generate coordinated hindlimb stepping in vivo after complete supraspinal disconnection, bridging the gap between neonatal in vitro mouse data and in vivo adult spinal locomotion. It demonstrates that mice are more cat-like than rat-like in their ability to recover spinal locomotion spontaneously, a finding with direct implications for interpreting locomotor recovery scores in transgenic mouse models of spinal cord injury. The study also provides the first detailed kinematic and EMG baselines for normal mouse treadmill locomotion, showing that conventional cat/rat equipment can be adapted for mice. Finally, it demonstrates that intralimb coordination recovers before interlimb alternation in the mouse, a temporal dissociation that was not observed in the cat, suggesting subtly different CPG organisation or recovery dynamics across species.

---

### Brain regions & systems

- **Lumbosacral spinal cord** — proposed locus of the central pattern generator responsible for generating hindlimb locomotor rhythm; shown to be sufficient for coordinated stepping after complete thoracic transection.
- **Thoracic spinal cord (T8)** — site of complete transection; paper demonstrates that circuits caudal to T8 are sufficient for locomotor recovery.
- Supraspinal structures are implicitly referenced as the source of descending drive that is removed by spinalization; no direct measurements of brain regions were made.

---

### Mechanistic insight

The paper comes close to but does not fully meet the bar. It provides strong in vivo evidence that the spinal CPG can operate autonomously (the double-transection control is a particularly clean manipulation), and it describes the temporal sequence of recovery (intralimb before interlimb coordination). However, it does not formalise an explicit algorithm for how the CPG generates locomotion, and it provides no neural recordings (unit activity, interneuron identification, pharmacological dissection) that would link a specific computational mechanism to the observed locomotor pattern. The EMG recordings from one animal document muscle activation timing but do not resolve the underlying spinal circuitry.

- **Computational level**: The spinal cord solves the problem of generating rhythmic, coordinated hindlimb stepping in the absence of supraspinal input.
- **Algorithmic level**: Not addressed — the paper does not identify the specific representations or processes within the CPG.
- **Implementational level**: Not addressed — specific cell types, interneurons, or neuromodulatory systems are not investigated.

---

### Limitations & open questions

- Kinematic recordings were made at the limit of temporal resolution (swing phase ~100 ms, ~6 video fields); higher-speed cameras would be needed for faster gait analysis.
- Knee angle required triangulation correction due to skin slippage, introducing potential measurement error.
- Only one mouse was implanted for EMG, limiting the generalisability of the electrophysiological characterisation.
- Tail support was provided throughout spinal locomotion testing, meaning the degree of active weight support cannot be independently assessed; a mechanical device measuring weight support was unavailable.
- 2 of 13 spinal mice never recovered locomotion and one recovered much later (29 days); the sources of this variability are not explained.
- The paper does not address which spinal interneurons or neuromodulatory systems underlie the observed CPG activity in the mouse.
- Whether recovery in the absence of training (2 untrained mice) reflects the same CPG mechanism as in trained mice is not explored.
- The dissociation between apparent open-field locomotion and true treadmill locomotion is noted but not systematically quantified.

---

### Connections & keywords

**Key citations**:
- Barbeau and Rossignol (1987) — cat spinal locomotion recovery baseline
- Bélanger et al. (1996) — detailed cat treadmill kinematics before and after spinalization
- Bonnot et al. (1998) — neonatal mouse spinal cord CPG in vitro
- Basso et al. (1995) — BBB locomotor rating scale in rats
- Grillner (1981) — review of spinal locomotor control across species
- Broton et al. (1996) — kinematic analysis in spinal rats; limitations of open-field observation

**Named models or frameworks**:
- Central pattern generator (CPG) — spinal network generating rhythmic locomotor output
- Philippson (1905) step-cycle subphases (F, E1, E2, E3)
- Hildebrand (1976) gait analysis / duty cycle
- BBB scale (Basso–Beattie–Bresnahan) — mentioned as a comparator for open-field locomotor scoring

**Brain regions**:
- Lumbosacral spinal cord
- Thoracic spinal cord (T8 transection site)

**Keywords**: spinal cord transection, central pattern generator, hindlimb locomotion, treadmill kinematics, electromyography, interlimb coordination, spinal mouse, locomotor recovery, step cycle, gait analysis, spinal cord injury, mouse model
