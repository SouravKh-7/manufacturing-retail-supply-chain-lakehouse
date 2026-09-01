# System overview

**State:** Planned

The repository currently contains a scaffold and design contracts. The diagram shows the intended business flow.

```mermaid
flowchart LR
    A[Manufacturing and supplier data]
    B[Warehouse and inventory data]
    C[Retail, sales and return data]
    D[Lakehouse processing]
    E[Trusted supply-chain products]
    F[Operations and analytics]

    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
```

