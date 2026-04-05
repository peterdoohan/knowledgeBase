# Compositionality

## Current understanding

Compositionality is the ability to build complex representations by recombining simpler components. In the context of cognitive maps, compositionality allows the brain to construct flexible spatial representations that can adapt to new environments by combining precomputed object representations rather than learning each environment from scratch.

---

## Key evidence

- The medial entorhinal cortex encodes compositional predictive maps through Predictive Object Representations (PORs)—compact, translation- and rotation-invariant matrices representing objects as perturbations to open space. Using the Woodbury matrix identity, compositional predictive maps are computed by adding low-rank POR correction terms to baseline open-space map; complexity scales with object size (O³) rather than environment size (S³) ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- The compositional framework enables efficient planning via simple matrix-vector multiplication, performing comparably to complete ground-truth planners (relative path length 1.09 with updates) and substantially outperforming successor representation models ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

- The learning algorithm for refining combined PORs operates in object-space rather than state-space, making it computationally tractable compared to temporal-difference learning of successor representations ([Piray 2025](../../raw/summaries/piray2025_compositional_cognitive_map.md))

---

## History of ideas

The concept of compositionality in cognitive maps addresses a fundamental tension between flexibility and efficiency in spatial representation. Successor Representation (SR) models proposed by Stachenfeld et al. (2017) offered predictive maps but required recomputing entire maps when environments change, predicting global remapping inconsistent with empirical data. The Tolman-Eichenbaum Machine (TEM) by Whittington et al. (2020) captured relational structure but learned compositionality implicitly through backpropagation. Piray & Daw (2025) introduced Predictive Object Representations (PORs) as a principled framework that reconciles compositionality with efficient planning, providing a unified account of object vector cells and grid cells while predicting local remapping consistent with empirical observations.

---

## Open questions

- How does the brain learn and update PORs for novel objects encountered during navigation?
- What are the circuit mechanisms implementing the projection of PORs onto grid cell basis functions?
- How does the compositional framework extend to dynamically changing environments with moving or occluded objects?

---

## Related pages

- [[medial_entorhinal_cortex]]
- [[grid_cells]]
- [[successor_representation]]
- [[model_based_rl]]
- [[cognitive_map]]
