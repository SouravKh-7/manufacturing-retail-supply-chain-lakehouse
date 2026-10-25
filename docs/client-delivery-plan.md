# Client delivery plan

This plan records the client-oriented Databricks project discussed earlier. It extends the current scaffold's roadmap; no cloud deployment, streaming pipeline, benchmark or completed client engagement is claimed.

## Discovery and scope

Confirm business owners, source permissions, source volumes and daily growth, delivery windows, freshness targets, correction policies, retention, data classification and budget. Record each requirement with an owner, acceptance criterion and a reproducible synthetic example.

| Requirement | First demonstrable slice | Later decision |
| --- | --- | --- |
| Multiple source types | Versioned CSV and JSON source contracts with deterministic sample data | SQL extraction and API connectors after access is available |
| Reliable batch reporting | One source -> Bronze -> validated Silver -> reconciled Gold | Additional domains and orchestration dependencies |
| Streaming machine monitoring | Define event ID, equipment ID, event time, arrival time and a file-replay scenario | Choose file micro-batches or a message broker from latency and operational needs |
| Database design | Document facts, dimensions, grains, keys and history | Implement and test the dimensional model |
| Cost control | Establish input size, runtime, correctness and budget measurements | Compare viable compute options under the same workload |
| Support | Define failures, ownership, retries, recovery and evidence | Alerts and support handover after pipeline implementation |

## Delivery gates

1. Approve source contracts, business grain and synthetic data scenarios.
2. Implement one batch source with replay metadata and reconciliation.
3. Add Silver checks and rejected-row quarantine with reasons.
4. Implement one Gold fact and its conformed dimensions.
5. Demonstrate duplicates, late data, corrections and safe reruns.
6. Add streaming only after its freshness target and recovery expectations are agreed.
7. Benchmark representative loads, configure the deployment and record a repeatable demo.
8. Deliver runbooks and a handover checklist.

## Compute and cost decision record

Do not prescribe a cluster size without workload evidence. Record representative data size, file count, concurrency, runtime target, shuffle/spill, memory pressure and total cost per successful run. Compare a small baseline with one alternative while keeping data and correctness checks fixed. Record auto-termination, scheduling, retry limits and spending controls. Any cloud price estimate must use a dated regional quote at deployment time.

## Support evidence

Define how to detect a missing source batch, schema change, failed reconciliation, partial write and checkpoint loss. Each runbook must state diagnosis queries, publication behavior, replay/backfill scope, validation after recovery, owner and escalation path. Test recovery using synthetic failures before calling the platform production-ready.

See [dimensional design](data-model/dimensional-design.md) for star/snowflake diagrams and validation requirements.
