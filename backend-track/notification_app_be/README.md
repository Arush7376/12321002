# notification_app_be

Django REST Framework service for queue-based notification delivery.

## Setup

```bash
cd backend-track
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python notification_app_be/manage.py migrate
python notification_app_be/manage.py runserver 0.0.0.0:8001
```

## API

- Base URL: `http://localhost:8001/api/v1/`
- Health: `GET /api/v1/health/`
- Swagger: `http://localhost:8001/swagger/`
- ReDoc: `http://localhost:8001/redoc/`

## Celery

```bash
cd notification_app_be
celery -A src.config worker --loglevel=info
```

## Structure

```text
src/
  apps/
  core/
  api/
  services/
  repositories/
  middlewares/
  validators/
  serializers/
  permissions/
  schedulers/
  utils/
  config/
  tests/
```

## Future Modules

Prepared for notification queues, email/SMS provider adapters, websocket notifications, retry policies, and delivery status tracking.
