# Future streaming architecture

**State:** Future direction

This diagram is separate from the planned batch-first lakehouse and the current scaffold.

```mermaid
flowchart TD
    A[Operational events and CDC]
    B[Streaming ingestion]
    C[Bronze Delta tables]
    D[Streaming quality and deduplication]
    E[Silver conformed state]
    F[Gold operational products]
    G[Near-real-time consumers]
    H[Checkpoints and monitoring]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    H --> B
    H --> D
```

