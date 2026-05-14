# Notification System Design

## Architecture Diagram

```text
Client
  |
  v
Django REST API
  |
  +--> PostgreSQL for durable notification records
  |
  +--> Redis queue
          |
          v
       Celery worker
          |
          +--> Email/SMS provider
          +--> WebSocket push layer
```

## Queue-Based Notification Flow

The API accepts notification requests and persists them with an initial status. A Celery task is pushed to Redis. Workers consume the task, call the required provider adapter, and update the delivery status. This keeps the HTTP request fast and moves slow provider calls to the background.

## Retry Mechanism

Retries should use exponential backoff. Each notification should carry an idempotency key so the same notification is not delivered twice if a worker crashes after sending but before updating the database. Failed items after the retry limit can be moved to a dead-letter queue for manual review.

## Scaling Strategy

Django API instances can scale horizontally behind a load balancer. Celery workers can be scaled based on queue depth. Redis should be monitored for memory usage and latency. For high traffic, queues can be split by notification type or priority.

## WebSocket Notifications

For websocket notifications, authenticated clients can subscribe to a user-specific channel. When a notification is created or delivered, the backend can publish an event to that channel. If websocket delivery fails, the client can still fetch unread notifications through the REST API.

## Security

JWT authentication can protect user APIs. Provider credentials should stay in environment variables or a secrets manager. Rate limiting is required for public endpoints. Request logs should not store sensitive tokens or full provider secrets.

## Deployment

The project can be deployed with Docker on Render, Railway, or AWS. The release flow should run tests, apply migrations, and then start Gunicorn and Celery workers. Rollback should keep the previous image available.

## Monitoring

Useful metrics include request error rate, request latency, Celery queue depth, retry count, provider error rate, and notification delivery time. Application logs are structured JSON so they can be shipped to a log platform later.

## Stage 6: Priority Inbox

The priority inbox ranks unread notifications using a two-part score:

1. Notification type weight: `Placement` > `Result` > `Event`
2. Recency: newer notifications rank higher within the same type

The implementation uses a bounded min-heap of size `n` to maintain the current top notifications efficiently as new notifications arrive. For each incoming notification, compute `(type_weight, timestamp)` and compare it with the lowest-ranked item in the heap. If the new item is better, evict the heap root and insert the new notification.

This keeps memory bounded to `O(n)` and updates each incoming notification in `O(log n)`, which is efficient for a continuously arriving stream where only the top 10 must be displayed.
