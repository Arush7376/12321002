# notification_app_be

Django REST Framework service for queue-based notification delivery.

## Setup

```bash
cd backend-track
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python notification_app_be/src/manage.py migrate
python notification_app_be/src/manage.py runserver 0.0.0.0:8001
```

## API

- Base URL: `http://localhost:8001/api/v1/`
- Health: `GET /api/v1/health/`
- Swagger: `http://localhost:8001/swagger/`
- ReDoc: `http://localhost:8001/redoc/`

## Celery

```bash
cd notification_app_be
cd notification_app_be/src
celery -A config worker --loglevel=info
```

## Structure

```text
src/
  apps/
  core/
  api/
  services/
  repositories/
  middleware/
  validators/
  serializers/
  permissions/
  clients/
  schedulers/
  utils/
  config/
  tests/
```

## Future Modules

Prepared for notification queues, email/SMS provider adapters, websocket notifications, retry policies, and delivery status tracking.

## Logging

Structured JSON request logs are written to `logs/app.log` by the shared `logging_middleware` package. APIs should obtain loggers through `logging_middleware.logger.get_logger()`.

## Stage 6 Priority Inbox

The priority inbox implementation lives in `src/services/priority_inbox.py`. It ranks notifications by `Placement > Result > Event`, then by newest timestamp within the same type. Fetched API responses and computed top-10 output are stored in `priority_inbox/`.
