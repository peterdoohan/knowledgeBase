# pyControl

## Current understanding

*No content yet — will be synthesised from Key evidence once sufficient facts are collected.*

## Key evidence

- pyControl achieves sub-millisecond response latencies (556 ± 17 μs under low load, 859 ± 241 μs under high load) with 99.6% of latencies under 2 ms ([Akam 2022](../../raw/summaries/akam2022_pycontrol_behavioral_experiments.md))

- pyControl provides millisecond-level timing accuracy with errors approximately uniformly distributed across the 1 ms clock resolution. Under low load: mean −220 μs, SD 282 μs; under high load: mean −10 μs, SD 353 μs with 99.5% of errors < 1 ms and maximum error 1.9 ms ([Akam 2022](../../raw/summaries/akam2022_pycontrol_behavioral_experiments.md))

- pyControl implements a task definition framework based on extended finite state machines running directly on MicroPython-enabled microcontrollers. Tasks are defined as states, events, state-behaviour functions, and timers with arbitrary MicroPython code within state functions; runs on pyboard microcontroller (Arm Cortex M4, 168 MHz, 192 KB RAM) ([Akam 2022](../../raw/summaries/akam2022_pycontrol_behavioral_experiments.md))

- pyControl supports high-throughput behavioral testing with up to 24 parallel setups confirmed running from a single computer. The GUI is built in PyQt for configuring and running parallel experiments ([Akam 2022](../../raw/summaries/akam2022_pycontrol_behavioral_experiments.md))

- pyControl's implementation of the 5-Choice Serial Reaction Time Task replicates established pharmacological effects of atomoxetine. Atomoxetine (2 mg/kg i.p.) reduced premature responding and increased attentional accuracy (p<0.05, paired t-tests); attention challenges reduced accuracy and increased omissions, impulsivity challenges increased premature responses ([Akam 2022](../../raw/summaries/akam2022_pycontrol_behavioral_experiments.md))

- MicroPython's automatic garbage collection in pyControl can introduce brief pauses that affect digital input processing when multiple edges occur during a single garbage collection episode. Only the last edge is processed when multiple edges arrive on a single digital input during garbage collection; timers that elapse during garbage collection are processed immediately afterwards with correct timestamps ([Akam 2022](../../raw/summaries/akam2022_pycontrol_behavioral_experiments.md))

## History of ideas

## Open questions

## Related pages

- [Extended finite state machine](../computational_frameworks/extended_finite_state_machine.md)
- [High-throughput behavioral testing](high_throughput_behavioral_testing.md)
- [5-Choice Serial Reaction Time Task](../behaviours/five_choice_serial_reaction_time_task.md)
