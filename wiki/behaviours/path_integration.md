# Path Integration

## Current understanding

Path integration (dead reckoning) is the process by which an animal updates its internal position estimate by integrating self-motion velocity signals over time. The dorsomedial entorhinal cortex (dMEC) is the primary neural substrate for this computation, with grid cells providing a high-capacity spatial representation that enables accurate integration over ecologically relevant distances.

The computational mechanism involves continuous attractor network dynamics, where the stable states of recurrent networks form a manifold parameterized by the position of a triangular lattice population pattern. Velocity inputs from head direction cells drive translation of this pattern, effectively integrating self-motion. The accuracy of this integration depends on network size, neural noise characteristics, and boundary conditions.

## Key evidence

- Grid cells implement a residue number system (modulo code) for position that enables carry-free arithmetic updating, making dMEC the likely locus of path integration ([Fiete 2008](../../raw/summaries/fiete2008_grid_cells_position.md))

- Continuous attractor networks of ~10^4 neurons can accurately integrate velocity with <0.1 cm/m error over 260m trajectories, producing coherent grid responses over 1-10 minutes and 10-100 meters ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- Sub-Poisson spiking statistics (CV < 1) observed in real dMEC recordings extend coherent integration time roughly quadratically compared to Poisson spiking, reaching behaviorally relevant timescales ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- Aperiodic attractor networks can match periodic network performance with carefully tapered feedforward inputs at boundaries, broadening biological plausibility beyond idealized toroidal topologies ([Burak 2009](../../raw/summaries/burak2009_path_integration_grid_cells.md))

- Hippocampal CA1 neurons in mice develop firing fields anchored to a variably positioned task-relevant object (lever), and the directional tuning of these fields on individual trials predicts the animal's homing direction during path-integration-based navigation in darkness. ([Jazi 2023](../../raw/summaries/jazi2023_hippocampal_path_integration_homing.md))

- Near-complete remapping of hippocampal ensembles occurs between random foraging and path-integration-based homing tasks on the same physical arena (map similarity r = 0.02), and further remapping is observed between light and dark trials, and between search and homing epochs within the task. ([Jazi 2023](../../raw/summaries/jazi2023_hippocampal_path_integration_homing.md))

- Approximately 25% of reliably active CA1 pyramidal cells have firing fields anchored to the lever box position, firing in a fixed direction relative to the lever box in a Cardinal (world-centred) reference frame — not a lever-relative or bridge-relative frame. ([Jazi 2023](../../raw/summaries/jazi2023_hippocampal_path_integration_homing.md))

- During dark trials, directional selectivity of lever-box-anchored fields is reduced after longer/more complex search paths, consistent with path integration error accumulation; lever-anchored field directional stability is higher on trials with accurate homing than inaccurate homing. ([Jazi 2023](../../raw/summaries/jazi2023_hippocampal_path_integration_homing.md))

- In ~24% of lever-anchored neurons, the single-trial directional drift of the firing field is significantly positively correlated with homing direction; at the population level this shift is highly significant (P = 4.05 × 10⁻⁸), establishing that hippocampal object-anchored representations predict navigational behavioral outcomes under path integration conditions. ([Jazi 2023](../../raw/summaries/jazi2023_hippocampal_path_integration_homing.md))

## History of ideas

Early models of grid cells proposed two competing mechanisms: continuous attractor networks (recurrent dynamics) and oscillatory interference models (independent neuron computations). Prior to 2009, attractor models were known to integrate velocity poorly, with errors accumulating quickly enough that frequent external position resets would be required. This cast doubt on whether attractor dynamics could underlie grid cell activity and path integration behavior.

The demonstration that continuous attractor networks could achieve accurate integration over behaviorally relevant scales resolved this challenge. The key insight was that previous failures reflected specific architectural choices (inadequate network size, improper velocity coupling, boundary effects) rather than fundamental limitations of the attractor mechanism itself. This reopened the attractor framework as a viable account of grid cell dynamics and path integration.

## Open questions

- How is the required recurrent weight structure (center-surround with direction-dependent shifts) learned developmentally?
- What is the actual topology of dMEC networks (periodic vs aperiodic) and what are the boundary conditions?
- How do velocity input noise and bias affect integration accuracy in natural behavior?
- What additional sensory corrections are required when integration errors accumulate beyond ~10-100 meter ranges?
- How do the proposed readout schemes (place-label vs explicit metric) map onto hippocampal circuitry?

## Related pages

- [Grid cells](grid_cells.md)
- [Place cells](place_cells.md)
- [Spatial navigation](spatial_navigation.md)
- [Grid cells in entorhinal cortex](../brain_regions/medial_entorhinal_cortex.md)
- [Attractor networks](../computational_frameworks/attractor_networks.md)
- [Cognitive map](cognitive_map.md)
