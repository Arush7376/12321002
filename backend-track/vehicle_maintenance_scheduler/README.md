# vehicle_maintenance_scheduler

Django REST Framework service for vehicle maintenance scheduling.

## Setup

```bash
cd backend-track
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python vehicle_maintenance_scheduler/manage.py migrate
python vehicle_maintenance_scheduler/manage.py runserver 0.0.0.0:8000
```

## API

- Base URL: `http://localhost:8000/api/v1/`
- Health: `GET /api/v1/health/`
- Swagger: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Celery

```bash
cd vehicle_maintenance_scheduler
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

Prepared for JWT authentication, vehicle CRUD APIs, maintenance scheduler APIs, background jobs, and API permissions.
