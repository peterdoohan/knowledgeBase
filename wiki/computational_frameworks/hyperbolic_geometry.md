# Hyperbolic Geometry in Neural Representations

## Current understanding

Neurons in rat dorsal CA1 hippocampus represent space according to a 3D hyperbolic geometry whose radius expands proportionally to the logarithm of exploration time. This hyperbolic organization maximizes Fisher information per neuron compared to Euclidean (uniform or log-normal field size) organizations, and the optimal representation size scales logarithmically with neuron count. The finding challenges the default assumption that spatial representation is approximately Euclidean and establishes that the representational geometry of the hippocampal spatial map is negatively curved, not flat. The hyperbolic geometry is not static but expands dynamically with exploration, matching a principled information-theoretic prediction (R ~ log(T)).

## Key evidence

- CA1 population activity is topologically consistent with a 3D hyperbolic geometry, not Euclidean geometry, in both linear track (three animals; radius range 13–15.5) and square box environments (multiple sessions; two-way ANOVA: F = 7,924.61, P < 10⁻⁸; 3D best fit vs. all other dimensions, P < 10⁻⁸) ([Zhang 2022](../../raw/summaries/zhang2022_hyperbolic_geometry_hippocampus.md))

- The radius of the hyperbolic representation grows proportionally to the logarithm of exploration time (r = 0.85, P = 3 × 10⁻⁶ for square box across days), consistent with the information-theoretic prediction that maximal learnable information scales as log(T) ([Zhang 2022](../../raw/summaries/zhang2022_hyperbolic_geometry_hippocampus.md))

- On shorter timescales (seconds), the hyperbolic radius on novel track segments increased with temporal familiarity (r = 0.50, P = 0.0003); place field size correlated positively with first-pass speed (r = 0.35, P = 9 × 10⁻²¹), meaning faster (less familiar) traversal produced larger, less resolved place fields ([Zhang 2022](../../raw/summaries/zhang2022_hyperbolic_geometry_hippocampus.md))

- The exponent of the Bayesian decoding accuracy curve (c) increased significantly over exploration time (r = 0.86, P = 10⁻⁶) and correlated with hyperbolic radius (r = 0.70, P = 0.0007), demonstrating that larger hyperbolic radius supports better spatial localisation ([Zhang 2022](../../raw/summaries/zhang2022_hyperbolic_geometry_hippocampus.md))

- Fisher information analysis showed that exponentially distributed place field sizes (as expected under hyperbolic geometry) provide more positional information than uniform or log-normal distributions (P < 0.001 at all network sizes), and there is an optimal hyperbolic radius for each network size ([Zhang 2022](../../raw/summaries/zhang2022_hyperbolic_geometry_hippocampus.md))

- Extrapolating the optimal-radius curve to the full CA1 neuron count (320,000–490,000 active pyramidal cells, 30–40% active per environment) closely matched experimentally observed radii, indicating the observed geometry is near the information-theoretic optimum ([Zhang 2022](../../raw/summaries/zhang2022_hyperbolic_geometry_hippocampus.md))

- Control analyses confirmed that shuffled spike trains do not produce Betti curves consistent with hyperbolic geometry, and that neither average running speed, active exploration time, nor time outside the environment explains the radius expansion ([Zhang 2022](../../raw/summaries/zhang2022_hyperbolic_geometry_hippocampus.md))

## History of ideas

The prevailing working model at the time of this paper was that CA1 neurons form a distributed code for position with place fields varying in size across the environment but with no strong framework specifying the global geometric organisation of the population code. It was generally intuited — and implicitly assumed — that spatial representation is approximately linear or Euclidean, consistent with everyday perception of distance. The paper directly challenged this default assumption by asking whether a non-Euclidean (hyperbolic) organisation better accounts for the population-level structure of place cell activity. Prior work on other systems (head direction cells, grid cells) had identified specific manifold structures using persistent homology, but CA1 spatial coding had not been subjected to this geometric analysis.

## Open questions

- Whether the same hyperbolic geometry characterizes other hippocampal subfields (CA3, dentate gyrus), ventral hippocampus, or other species including humans
- The precise biological mechanism by which the hierarchical/hyperbolic organisation is instantiated (which plasticity rules, which cell types, what role interneurons play)
- The topological method requires a sufficient number of simultaneously recorded neurons (>~30–50); this limits the analysis to particular recording configurations
- Whether hyperbolic geometry characterises hippocampal representations of non-spatial or abstract relational information
- The relationship between hyperbolic geometry in CA1 and the known dorsal-ventral gradient in place field scale, as well as the grid cell scale hierarchy in entorhinal cortex
- The prediction that the order of spike receipt from different neurons should matter (non-commutativity of hyperbolic addition) requires testing

## Related pages

- [Place cells](place_cells.md)
- [Hippocampus](../brain_regions/hippocampus.md)
- [Hippocampus CA1](../brain_regions/hippocampus_ca1.md)
- [Spatial navigation](spatial_navigation.md)
- [Cognitive map](cognitive_map.md)
- [Grid cells](grid_cells.md)
- [Entorhinal cortex](../brain_regions/medial_entorhinal_cortex.md)
- [Information theory](information_theory.md)
- [Topology](topology.md)
