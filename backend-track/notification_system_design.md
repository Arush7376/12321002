# Notification System Design

## Architecture Diagram

Placeholder for high-level system diagram covering API, PostgreSQL, Redis, Celery workers, notification providers, and websocket gateway.

## Queue-Based Notification Flow

Placeholder for producer, queue, worker, provider adapter, status persistence, and callback flow.

## Retry Mechanism

Placeholder for exponential backoff, dead-letter queues, idempotency keys, provider-specific retry policies, and poison message handling.

## Scaling Strategy

Placeholder for horizontal Django scaling, Celery worker autoscaling, Redis sizing, queue partitioning, read replicas, and provider throughput limits.

## WebSocket Notifications

Placeholder for channel subscription model, authentication, fan-out, presence, and fallback polling.

## Security

Placeholder for JWT authentication, API permissions, secrets management, provider credential rotation, rate limits, and audit logging.

## Deployment

Placeholder for AWS, Render, Railway, Docker, CI/CD, migrations, static files, and release rollback strategy.

## Monitoring

Placeholder for structured logs, metrics, traces, Celery queue depth, retry rate, provider error rate, alerting, and dashboards.

## Stage 6: Priority Inbox

The priority inbox ranks unread notifications using a two-part score:

1. Notification type weight: `Placement` > `Result` > `Event`
2. Recency: newer notifications rank higher within the same type

The implementation uses a bounded min-heap of size `n` to maintain the current top notifications efficiently as new notifications arrive. For each incoming notification, compute `(type_weight, timestamp)` and compare it with the lowest-ranked item in the heap. If the new item is better, evict the heap root and insert the new notification.

This keeps memory bounded to `O(n)` and updates each incoming notification in `O(log n)`, which is efficient for a continuously arriving stream where only the top 10 must be displayed.
