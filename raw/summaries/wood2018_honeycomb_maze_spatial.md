---
source_file: wood2018_honeycomb_maze_spatial.md
title: The honeycomb maze provides a novel test to study hippocampal-dependent spatial navigation
authors: Ruth A. Wood, Marius Bauza, Julija Krupic, Stephen Burton, Andrea Delekate, Dennis Chan, John O'Keefe
year: 2018
journal: Nature
paper_type: empirical
contribution_type: methodological
---

### One-line summary

The honeycomb maze, a novel hexagonal platform navigation task for rats, enables precise control over spatial choices and reveals that hippocampal lesions impair learning by disrupting vector-based computations of goal direction.

### Background & motivation

Existing spatial navigation tests (T maze, radial arm maze, Morris water maze) have limitations: they allow multiple solution strategies (egocentric, cue-based) or lack control over individual choices. The Morris water maze overcomes some limitations but presents challenges for single-cell recording due to swimming behavior and uncontrolled choice points. The honeycomb maze was designed to provide a more controlled environment for studying hippocampal-dependent spatial navigation while enabling simultaneous neural recordings.

### Methods

- **Task design**: 37 hexagonal platforms (11.5 cm sides) arranged in a tessellated honeycomb pattern (145.5 cm diameter). Each platform independently raised/lowered via pneumatic tubes.
- **Navigation paradigm**: Rats navigate from 1 of 8-9 starting platforms to a fixed goal platform by making sequential binary choices between two adjacent raised platforms. The "correct" choice is the platform with the smallest angle to the goal-heading direction.
- **Manipulated variables**: Three geometric factors were systematically varied: (1) angle α (0°–135°): deviation of correct platform from goal direction; (2) angle β (60°, 120°, 180°): separation between the two choice platforms; (3) distance (1–5 platforms): steps to goal from choice point.
- **Subjects**: Male Lister hooded rats (12–16 weeks): 9 unoperated controls, 8 sham hippocampal lesions, 8 sham medial entorhinal lesions, 8 hippocampal ibotenic acid lesions.
- **Analysis**: ANOVAs to assess learning rates and factor effects; multiple regression to quantify contributions of α, β, and distance to performance.

### Key findings

- **Rapid learning**: All control groups (unoperated, sham hippocampal, sham MEC) learned rapidly, reaching >90% accuracy within 28 trials. No significant differences between control groups (F₂,₂₂ < 0.001, P > 0.999), demonstrating task reliability.
- **Three factors govern performance in controls**:
  - **Angle β (platform separation)**: Performance improved with larger separations (180°: 92.8% ± 1.1% vs. 60°: 85.8% ± 1.4%; F₂,₁₆ = 8.850, P = 0.003).
  - **Distance from goal**: Performance decreased with distance (adjacent: 88.4% ± 1.0% vs. 5 platforms away: 71.8% ± 6.1%; F₃,₂₄ = 3.707, P = 0.025).
  - **Angle α (deviation from goal direction)**: Performance decreased as correct platform deviated from goal direction (0°–29°: 86.2% ± 1.3% vs. ≥90°: 61.1% ± 3.1%; F₄,₃₂ = 20.670, P < 0.001). Rats performed better when correct choice was "ahead" (<90°) vs. "behind" (>90°) of goal direction (t₈ = 6.620, P < 0.001).
- **Multiple regression**: Angle α, β, and distance all significantly predicted performance (R² = 0.055, F₃,₃₉₁ = 7.608, P < 0.001), with experience accounting for additional variance.
- **Interaction effects**: Performance on "ahead" vs. "behind" choices varied with distance (F₃,₂₄ = 9.133, P < 0.001) — the angle-to-goal effect decreased at greater distances.
- **Hippocampal lesion effects**:
  - Severe learning impairment compared to sham controls (F₁,₁₄ = 10.240, P = 0.006).
  - Greater sensitivity to all three factors (angle β × lesion: F₂,₂₈ = 6.981, P = 0.003; distance × lesion: F₄,₅₆ = 4.999, P = 0.002; angle α × lesion: F₂.₃,₃₂.₈ = 8.431, P = 0.001).
  - Longer choice latencies (F₁,₁₄ = 11.103, P = 0.005), with larger difference between correct vs. incorrect choice latencies for lesioned rats (uncertainty marker).
  - Performance correlated with lesion size (more damage = worse performance), though not statistically significant possibly due to floor effects.

### Computational framework

The paper proposes a **vector-based navigation schema** grounded in the hippocampal cognitive map framework. The core formalism involves:

- **Goal-direction vector**: A vector (A) representing the direction and distance from the animal's current location to the goal, encoded by the hippocampus.
- **Choice platform vectors**: Vectors (B, C) pointing to each potential choice platform from the current location.
- **Vector projection**: The navigation system computes the inner product (projection) of each choice vector onto the goal-direction vector (Bgd, Cgd), selecting the choice with the larger projection.
- **Decision difficulty**: The discrimination is easier when the angle between choices (β) is larger, producing greater differences in projection magnitudes.

This framework assumes the hippocampus represents location (place cells), goal location, and performs vector computations to determine heading direction. The three factors affecting performance (angle α, angle β, distance) naturally emerge from this vector geometry.

### Prevailing model of the system under study

The prevailing model, established by O'Keefe and Nadel (1978) and supported by decades of electrophysiological work, holds that the hippocampal formation generates a **cognitive map** — an internal representation of space that enables location identification, environmental change detection, and navigation to goals. This map is supported by spatially tuned neurons: place cells (location coding), head direction cells (heading coding), grid cells (distance coding in specific directions), and boundary cells (distance from environmental boundaries). 

The Morris water maze has been the gold standard for testing hippocampal-dependent spatial navigation, building on findings that hippocampal lesions impair place navigation. However, the introduction notes limitations of existing tasks: T maze, radial arm maze, and Barnes maze allow multiple solution strategies (directional-heading, object-heading, not just place learning); the Morris water maze lacks control over choices at each location and presents challenges for single-cell recording due to swimming behavior.

### What this paper contributes

This paper makes both **methodological** and **empirical** contributions:

**Methodological contribution**: The honeycomb maze represents a substantial improvement over existing spatial navigation tests. Unlike the Morris water maze, it:
- Controls the animal's choices at each decision point (binary choices between two platforms)
- Enables assessment of goal-direction knowledge from any location in the maze
- Allows systematic identification of factors influencing performance (angles α, β, and distance)
- Permits concomitant single-cell recording (demonstrated with place cell example)
- Enables flexible schedule design from hippocampal-sensitive (never-repeated trials) to guidance-based (stereotyped sequences)

**Empirical contribution**: The paper establishes that:
1. **Vector computations underlie navigation**: Control rats can identify the better direction even when neither choice aligns with the goal, suggesting the brain performs vector computations (projecting choice vectors onto a goal-direction vector).
2. **Hippocampus is critical for vector-based navigation**: Rats with hippocampal lesions are impaired on all three geometric factors (angles α, β, distance), suggesting the hippocampus either performs or provides necessary inputs for these vector computations.
3. **Alternative locus hypothesis**: The impairment could reflect disrupted hippocampal input to other regions (e.g., parietal cortex) that perform the actual computation, using place cell representations of current location, goal, and choice platforms.
4. **Performance factors quantified**: The relative contributions of angle α, angle β, and distance to performance were statistically quantified, providing a framework for comparing navigation across groups and conditions.

### Brain regions & systems

- **Hippocampus** — primary focus; site of ibotenic acid lesions. Lesions impaired learning and increased sensitivity to all three geometric factors. Role: generates cognitive map supporting vector-based navigation. Preserved tissue in ventral hippocampus in lesioned rats.
- **Medial entorhinal cortex** — sham lesions only (no actual damage); tested as control to rule out non-specific effects of surgery in nearby region. No impairment observed.
- **Caudate nucleus / putamen** — incidental minor damage in some hippocampal lesion rats; not systematically studied.
- **Subiculum** — minor damage to dorsal subiculum in subset of lesioned rats; mentioned as incidental.
- **Medial geniculate nucleus** — minor incidental damage in subset of lesioned rats.
- **Pre- and parasubiculum** — minor incidental damage in subset of lesioned rats.

### Mechanistic insight

This paper does **not** fully meet the high bar for mechanistic insight, but it makes significant progress toward a mechanistic account:

**What the paper provides**:
1. **Behavioral algorithm**: The paper formalizes a vector-based navigation algorithm (Extended Data Fig. 6) where the animal computes projections of choice vectors onto a goal-direction vector to select the optimal path. This provides an algorithmic-level account of the decision process.

2. **Neural necessity**: Hippocampal lesions severely impair task performance, establishing that the hippocampus is necessary for this vector-based navigation. The lesion effects are specific to all three geometric factors (angles α, β, distance), implicating the hippocampus in vector computations.

3. **Place cell evidence**: Extended Data Fig. 1 shows a place cell recorded during maze navigation, demonstrating that place cells fire during task performance and that the maze is compatible with electrophysiological recording.

**Why it does not fully meet the bar**:

The paper does **not** provide neural data that specifically supports the proposed vector algorithm over alternative computational accounts. Specifically:
- No recordings show neurons encoding the goal-direction vector, choice vectors, or their inner products
- No evidence distinguishes vector-based navigation from alternative strategies (e.g., learned stimulus-response associations, place-approach heuristics)
- The lesion data establish necessity but not the specific computational mechanism

**Marr's levels assessment**:
- **Computational**: The paper identifies the problem as vector-based navigation — computing goal directions and comparing choice options via inner products. The "why" is efficient navigation to goals from arbitrary starting positions.
- **Algorithmic**: The vector projection algorithm is proposed: represent current location and goal as vectors, compute projections of choice options onto the goal-direction vector, select the larger projection.
- **Implementational**: Limited evidence. The hippocampus is necessary, and place cells are active during the task, but how the hippocampus implements the vector computation is not established. The paper hypothesizes that place cells encode locations (current, goal, choices) and that vector computations occur in the hippocampus or in downstream regions (e.g., parietal cortex) using hippocampal inputs.

### Limitations & open questions

- **Lesion extent variability**: Hippocampal damage ranged from 48% to 94%, with preserved tissue primarily in ventral hippocampus. This variability may have contributed to the non-significant correlation between lesion size and performance (though floor effects were also suggested).
- **Incidental damage**: Minor damage to caudate/putamen, dorsal subiculum, medial geniculate, and pre/parasubiculum in some lesioned rats complicates pure attribution to hippocampus.
- **No direct neural evidence for vector coding**: The proposed vector-based algorithm is supported by behavioral data and formal modeling but lacks direct neural recordings showing neurons encoding goal-direction vectors or vector projections.
- **Limited comparison to other spatial tasks**: While the paper argues for advantages over the Morris water maze, direct behavioral comparisons between tasks in the same subjects were not conducted.
- **Single species/strain**: Only male Lister hooded rats were tested; generalizability to other strains, sexes, or species is unknown.
- **Open question**: Is the vector computation performed within the hippocampus itself, or does the hippocampus provide spatial representations (place cells) that enable vector computations in other regions (e.g., parietal cortex)?
- **Open question**: What is the role of entorhinal cortex (grid cells, boundary cells) in honeycomb maze performance? Sham MEC lesions did not impair controls, but actual MEC lesions were not tested.
- **Open question**: How do place cell firing patterns on the maze relate to the vector navigation strategy? The single example shows stable place fields, but population coding remains uncharacterized.

### Connections & keywords

**Key citations**:
- Morris RGM (1981, 1982, 1984) — Morris water maze foundational work
- O'Keefe & Nadel (1978) — The Hippocampus as a Cognitive Map
- O'Keefe & Dostrovsky (1971) — discovery of place cells
- Hafting et al. (2005) — discovery of grid cells
- Taube et al. (1990) — head direction cells
- Olton et al. (1978, 1976) — radial arm maze work
- Barnes (1979) — Barnes maze
- Eichenbaum et al. (1990) — hippocampal representation in place learning

**Named models or frameworks**:
- Cognitive map theory (O'Keefe & Nadel)
- Vector-based navigation schema (proposed in this paper)
- Honeycomb maze (novel behavioral paradigm)

**Brain regions**:
- Hippocampus — primary focus; lesion target; cognitive map generator
- Medial entorhinal cortex — sham lesion control region
- Caudate nucleus / putamen — incidental damage
- Subiculum — minor incidental damage
- Parietal cortex — hypothesized locus of vector computation (not tested)

**Keywords**:
spatial navigation, honeycomb maze, hippocampus, place cells, cognitive map, vector navigation, spatial memory, lesion study, rat behavior, goal-directed navigation, Morris water maze alternative, hippocampal-dependent learning, spatial decision-making
