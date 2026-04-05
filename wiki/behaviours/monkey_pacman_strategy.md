# Monkey Pac-Man Strategy

## Current understanding

Macaque monkeys trained to play Pac-Man use compositional strategies and hierarchical decision-making with a "take-the-best" heuristic, achieving over 90% prediction accuracy with a dynamic strategy model. The monkeys demonstrate sophisticated strategic competence without explicit instruction, employing multiple basis strategies that are dynamically combined based on game context. Rather than averaging across strategies, monkeys predominantly use a single dominant strategy at each decision point, simplifying computational demands. They can also assemble basis strategies into higher-level compound strategies (e.g., planned attacks combining energizer collection with ghost chasing), demonstrating compositional cognitive abilities.

## Key evidence

- The dynamic compositional strategy model achieved 90.4% overall prediction accuracy (Monkey O: 90.7%, Monkey P: 90.0%), significantly outperforming static (81.6%), LARL (66.9%), and perceptron (62.4%) models ([Yang 2022](../../raw/summaries/yang2022_monkey_pacman_strategy.md))

- Monkeys adopted a "take-the-best" (TTB) heuristic: the dominant strategy weight (0.907 ± 0.117) was significantly larger than secondary (0.273 ± 0.233) and tertiary (0.087 ± 0.137) strategies ([Yang 2022](../../raw/summaries/yang2022_monkey_pacman_strategy.md))

- In over 90% of time points, the weight difference between first and second strategies exceeded 0.1; in 33% of cases it exceeded 0.9 ([Yang 2022](../../raw/summaries/yang2022_monkey_pacman_strategy.md))

- Strategy usage was context-dependent: local strategy dominated early game (abundant pellets), global strategy became prominent in late game (scarce local pellets), approach strategy activated when ghosts were scared and nearby ([Yang 2022](../../raw/summaries/yang2022_monkey_pacman_strategy.md))

- Monkeys formed compound strategies: planned attack (energizer consumption followed by ghost chasing) and suicide (deliberate death to reset game when pellet distribution was unfavorable) ([Yang 2022](../../raw/summaries/yang2022_monkey_pacman_strategy.md))

- Eye movements validated strategy labels: fixation patterns shifted to match strategy-relevant game elements (ghosts during approach, pellets during local, energizers during energizer strategy) ([Yang 2022](../../raw/summaries/yang2022_monkey_pacman_strategy.md))

- Pupil dilation increased transiently around strategy transitions (p<0.01), consistent with hierarchical decision-making requiring additional cognitive processing at strategy switches ([Yang 2022](../../raw/summaries/yang2022_monkey_pacman_strategy.md))

- Monkeys demonstrated sophisticated understanding of ghost "personalities": more likely to evade aggressive Blinky but could safely follow Clyde when nearby due to Clyde's avoidance behavior at close range ([Yang 2022](../../raw/summaries/yang2022_monkey_pacman_strategy.md))

## History of ideas

Prior to this study, the prevailing understanding of animal decision-making in complex tasks was limited by the availability of sufficiently complex behavioral paradigms. Existing studies typically used simple rule-based tasks where strategies were mutually exclusive and cued explicitly, equated strategies with simple stimulus-response associations, focused on flat decision-making models where actions are computed directly from sensory features, and lacked quantitative frameworks for studying how animals manage multiple strategies dynamically. While animals exhibit complex strategy-like behaviors in nature, quantitative studies were lacking and the level of complexity of existing animal behavioral paradigms was insufficient for studying how animals manage strategies to simplify sophisticated tasks. This study established that non-human primates can employ compositional strategies and hierarchical decision-making to solve complex tasks, challenging the view that strategic decision-making is uniquely human or requires linguistic capacities.

## Open questions

- The particular set of basis strategies was hand-crafted by the researchers; it remains unknown whether monkeys naturally develop these specific strategies or whether alternative decompositions would be equally valid
- The study does not investigate the neural mechanisms underlying strategy selection and transitions; future work combining this paradigm with neural recordings is needed
- Only two monkeys were tested, limiting generalizability to the broader macaque population
- The training period was extensive (hundreds of sessions), raising questions about the scalability of this approach for studying advanced cognition in animals
- The model assumes stable strategy weights within time windows, but the dynamics of how strategy transitions occur in real-time remain poorly understood
- It is unclear whether the take-the-best heuristic reflects a capacity limitation or an optimal computational strategy

## Related pages

- [Hierarchical decision-making](hierarchical_decision_making.md)
- [Compositional strategies](compositional_strategies.md)
- [Take-the-best heuristic](take_the_best_heuristic.md)
- [Strategy switching](strategy_switching.md)
- [Reinforcement learning](../computational_frameworks/reinforcement_learning.md)
- [Complex behavior paradigm](complex_behavior_paradigm.md)
- [Non-human primate cognition](non_human_primate_cognition.md)
- [Eye movements](eye_movements.md)
- [Pupil dilation](pupil_dilation.md)
