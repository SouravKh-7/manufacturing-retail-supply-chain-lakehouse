# Medallion data flow

**State:** Planned

```mermaid
flowchart TD
    A[Synthetic source batches]
    B[Bronze landing]
    C[Schema and contract checks]
    D[Silver conformed entities]
    E[Quarantine]
    F[Reconciliation and freshness gates]
    G[Gold supply-chain products]
    H[Analytics]

    A --> B
    B --> C
    C -->|Accepted| D
    C -->|Rejected| E
    D --> F
    F --> G
    G --> H
```

