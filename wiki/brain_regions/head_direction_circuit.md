# Head Direction Circuit

## Current understanding

The head direction (HD) circuit, centered in the anterior dorsal nucleus of the thalamus (ADn) and extending to the postsubiculum and other regions, maintains an internal compass-like representation of the animal's heading in the horizontal plane. This circuit implements a ring attractor architecture where neural activity forms a localized "bump" that tracks the animal's head direction through angular velocity integration.

## Key evidence

- The head direction circuit in the anterior dorsal nucleus of thalamus (ADn) implements a ring attractor, with neural activity constrained to a 1-dimensional ring manifold that is isometric with head direction and invariant across waking and REM sleep. Direct visualization of the ring manifold using thousands of simultaneously recorded neurons confirms states flow back to the ring after perturbations. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

- In Drosophila, the ellipsoid body implements a ring attractor for heading direction with physically ring-shaped anatomy and copy-and-offset connectivity confirmed by EM. Turner-Evans et al. (2020) combined electrophysiology and EM to confirm the predicted double-ring connectivity architecture. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

## History of ideas

Ring attractor models for head direction cells were first proposed by Zhang in 1996, providing a computational mechanism for how the brain could maintain a stable heading representation while integrating angular velocity signals. These models predicted specific connectivity patterns (copy-and-offset) that would enable bump movement around the ring. For decades, these remained theoretical predictions due to limitations in population recording capabilities. The direct visualization of the ring manifold in mammalian ADn by Chaudhuri et al. (2019) and the connectomic validation in Drosophila by Turner-Evans et al. (2020) provided rigorous empirical confirmation that had been elusive for over two decades.

## Open questions

- What are the specific cellular mechanisms that maintain the fine-tuned balance between feedback and decay required for line attractor integration?
- How does the brain develop and maintain the continuous weight symmetries required for pattern-forming continuous attractors?
- What is the role of different cell types (interneurons vs. pyramidal cells) in maintaining attractor dynamics?

## Related pages

- [[medial_entorhinal_cortex]]
- [[spatial_navigation]]
- [[attractor_networks]]
- [[grid_cells]]
- [[place_cells]]
