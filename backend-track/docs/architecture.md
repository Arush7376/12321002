# Backend Track Architecture

## Service Boundaries

- `vehicle_maintenance_scheduler`: owns vehicle and maintenance scheduling workflows.
- `notification_app_be`: owns notification queueing, provider delivery, and future websocket fan-out.
- `logging_middleware`: shared request logging package used by both services.

## Clean Architecture Layers

- `api`: DRF routing and versioned presentation layer.
- `serializers`: request/response validation and transformation.
- `services`: use-case orchestration.
- `repositories`: persistence adapters and query boundaries.
- `clients`: external API/provider clients.
- `core`: cross-cutting primitives such as responses, exceptions, pagination, and decorators.
- `middleware`: project-specific middleware extension point.

## Extension Points

The repository is prepared for JWT auth, scheduler engines, notification queues, websocket notifications, Redis caching, provider integrations, and optimization algorithms.
