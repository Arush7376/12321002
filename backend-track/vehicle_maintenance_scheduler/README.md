# vehicle_maintenance_scheduler

Django REST Framework service for vehicle maintenance scheduling.

## Setup

```bash
cd backend-track
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python vehicle_maintenance_scheduler/src/manage.py migrate
python vehicle_maintenance_scheduler/src/manage.py runserver 0.0.0.0:8000
```

## API

- Base URL: `http://localhost:8000/api/v1/`
- Health: `GET /api/v1/health/`
- Swagger: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Celery

```bash
cd vehicle_maintenance_scheduler
cd vehicle_maintenance_scheduler/src
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

Prepared for JWT authentication, vehicle CRUD APIs, maintenance scheduler APIs, background jobs, and API permissions.

## Logging

Structured JSON request logs are written to `logs/app.log` by the shared `logging_middleware` package. APIs should obtain loggers through `logging_middleware.logger.get_logger()`.
