# Theta Sweeps

## Current understanding

Hippocampal theta sweeps are sequential activations of place cells within individual theta cycles that encode goal-oriented cognitive vectors independent of movement or head direction. Rather than simply reflecting movement-related dynamics or sampling possible future trajectories, theta sweeps encode abstract cognitive vectors toward goal locations, transcending immediate sensory inputs and motor outputs. The goal-directed nature of theta sweeps is demonstrated by their robust alignment to goal direction even when movement and head directions are dissociated from goal direction. This positions theta sweeps as a neural substrate for flexible online spatial planning within the cognitive map framework, supporting rapid evaluation of potential future trajectories during navigation.

## Key evidence

- Theta sweeps exhibit robust goal-oriented directional bias, with sweep directions significantly more aligned to goal direction than movement or head direction (p = 0.0004 for SD vs GD vs MD; p = 0.0005 for MD vs HD) ([Yu 2025](../../raw/summaries/yu2025_theta_sweeps_goal_direction.md))

- Initial offset directions (IOD) also show significant alignment to goal direction with no modulation by movement or head direction (p = 0.0078 for IOD vs GD vs MD; p = 0.9449 for MD vs HD) ([Yu 2025](../../raw/summaries/yu2025_theta_sweeps_goal_direction.md))

- Goal-modulation strengthens with experience within recording sessions (p = 0.0269 for first vs second half of trials) ([Yu 2025](../../raw/summaries/yu2025_theta_sweeps_goal_direction.md))

- Goal-modulation is stronger before correct compared to incorrect choices even after controlling for distance to goal (p = 0.0136), suggesting behavioral relevance ([Yu 2025](../../raw/summaries/yu2025_theta_sweeps_goal_direction.md))

- In goal-switching sessions, sweeps align more strongly with current than alternative goal (p = 0.0220 for SD; p = 0.0060 for IOD) ([Yu 2025](../../raw/summaries/yu2025_theta_sweeps_goal_direction.md))

- Theta sweep length increases with distance to goal and movement speed, and with theta power ([Yu 2025](../../raw/summaries/yu2025_theta_sweeps_goal_direction.md))

- The continuous attractor network model with goal-directed input successfully reproduces goal-oriented theta sweeps and predicts goal-oriented theta phase precession (toward goal) and procession (away from goal), both confirmed empirically ([Yu 2025](../../raw/summaries/yu2025_theta_sweeps_goal_direction.md))

- Replay events during sharp wave/ripples also show goal-directed bias, supporting that replay reflects composition of theta sweeps rather than direct experience ([Yu 2025](../../raw/summaries/yu2025_theta_sweeps_goal_direction.md))

## History of ideas

Prior to this work, theta sweeps were understood as sequential activations of place cells within theta cycles that sweep forward from the animal's current location. Several models proposed that theta sweeps emerge from intrinsic network dynamics, particularly firing rate adaptation within attractor networks, or from oscillatory interference mechanisms. The field recognized that theta sweeps could sample potential paths ahead of the animal, sometimes alternating to both sides of choice points or the forward direction in open fields, and that sweep length correlated with speed, distance to goals, and learning. However, it remained unresolved whether theta sweeps simply reflect movement-related dynamics or encode more abstract cognitive vectors toward goals. The prevailing view held that theta sweeps might reflect possible future movement trajectories rather than encoding a location-independent "sense of direction" toward goal locations. This paper established that hippocampal theta sweeps encode a goal-oriented cognitive vector that transcends immediate movement and sensory constraints.

## Open questions

- The top-down goal-oriented input to directional cells is hypothesized to originate from retrosplenial cortex or medial prefrontal cortex via thalamus, but this remains to be empirically validated
- Causal manipulations (e.g., phase-specific interventions) are needed to establish necessity and sufficiency of theta sweeps for navigation
- Direct evidence in humans or non-rodent species is limited
- The extent to which goal-directed theta sweeps support non-spatial planning or abstract reasoning remains unexplored
- The hypothesis that replay reflects composition of theta sweeps rather than experience requires further testing with manipulations that dissociate these possibilities
- How the full entorhinal-hippocampal circuit implements goal-directed sweep dynamics remains to be fully characterized

## Related pages

- [Place cells](place_cells.md)
- [Hippocampal replay](hippocampal_replay.md)
- [Forward replay](forward_replay.md)
- [Sharp-wave ripples](sharp_wave_ripples.md)
- [Spatial navigation](spatial_navigation.md)
- [Goal-directed behaviour](goal_directed_behaviour.md)
- [Cognitive map](cognitive_map.md)
- [Continuous attractor networks](../computational_frameworks/attractor_networks.md)
- [Theta oscillations](theta_oscillations.md)
- [Phase precession](phase_precession.md)
