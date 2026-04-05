# Kilosort

## Current understanding

Kilosort is a GPU-accelerated spike sorting framework that uses template matching and graph-based clustering to extract single-unit activity from extracellular electrophysiology recordings. The algorithm handles the key challenges of probe drift (non-stationary waveforms) and spike collisions (overlapping electrical fields from nearby neurons).

## Key evidence

- Kilosort4 outperforms all tested competitors across drift conditions using a novel graph-based clustering algorithm; correctly identified most units across all six drift conditions with no-drift case 526/600 ground-truth units vs next best at ~320-460; step-drift condition recovered 43 units vs 25-27 for Kilosort 2.5/3 ([Pachitariu 2023](../../raw/summaries/pachitariu2023_kilosort_spike_sorting.md))

- The graph-based clustering algorithm uses bipartite modularity optimization with nearest-neighbor graphs constructed via FAISS search; nearest-neighbor graph constructed with brute-force FAISS search over subsampled landmark set; bipartite graph enables parallel GPU optimization of modularity cost function; initialized with K-means++ (200 clusters) ([Pachitariu 2023](../../raw/summaries/pachitariu2023_kilosort_spike_sorting.md))

- Hierarchical merging tree with refractory-period criteria enables automated splitting and merging decisions without human curation; dendrogram constructed by sweeping resolution parameter γ; splits/merges decided by bimodality of spike projections and refractoriness of cross-correlogram; global merges applied across probe sections using waveform cross-correlation ([Pachitariu 2023](../../raw/summaries/pachitariu2023_kilosort_spike_sorting.md))

- Realistic simulation framework using waveform banks from high-drift recordings enables benchmarking across drift conditions; 600 ground-truth single units + 600 multi-units added with realistic ISIs and amplitudes; waveform bank of 597 units from 11 high-drift IBL recordings captures realistic waveform shape changes across depths ([Pachitariu 2023](../../raw/summaries/pachitariu2023_kilosort_spike_sorting.md))

- Kilosort4 runs in ~25 minutes per 45-minute recording on an RTX 3090, scaling to large recording durations via bipartite graph formulation and landmark subsampling ([Pachitariu 2023](../../raw/summaries/pachitariu2023_kilosort_spike_sorting.md))

## History of ideas

## Open questions

## Related pages
- [Neuropixels](neuropixels.md)
- [Spike sorting](spike_sorting.md)
- [Single unit recording](single_unit_recording.md)
