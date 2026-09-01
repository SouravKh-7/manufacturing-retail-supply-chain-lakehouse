# Architecture diagrams

| Diagram | State | Question answered |
|---|---|---|
| [System overview](system-overview.md) | Planned | What business flow will the lakehouse support? |
| [Current scaffold](current-scaffold.md) | Implemented | What repository components currently exist? |
| [Medallion flow](medallion-flow.md) | Planned | How will data move from source to Gold? |
| [Quality and publication](quality-flow.md) | Planned | How will rejected data and publication gates work? |
| [Future streaming architecture](future-streaming.md) | Future direction | How could event and CDC ingestion be added later? |

The current scaffold, planned batch-first lakehouse, and future streaming direction are maintained as separate figures.

## Implementation roadmap

1. Define versioned synthetic source contracts and labeled scenarios.
2. Implement reproducible generators and immutable Bronze landing.
3. Add Silver standardization, keys, deduplication, quality, and quarantine.
4. Implement incremental Delta merges, late data, replay, and SCD Type 2.
5. Publish reconciled Gold products.
6. Add orchestration, freshness, failure recovery, and CI evidence.
7. Run controlled Spark experiments only after correctness baselines pass.

The root README distinguishes this target state from the current scaffold.
