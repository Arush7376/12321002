# backend-track

Production-grade Django backend starter for Backend Track evaluation work. The repository contains two modular DRF services and a reusable request logging middleware package.

## Projects

- `vehicle_maintenance_scheduler`: vehicle CRUD and maintenance scheduler foundation.
- `notification_app_be`: queue-driven notification system foundation.
- `logging_middleware`: reusable Django middleware for structured request logging.

## Setup

```bash
cd backend-track
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Update `.env` with PostgreSQL, Redis, and Django secrets.

## Run Locally

```bash
python vehicle_maintenance_scheduler/manage.py migrate
python vehicle_maintenance_scheduler/manage.py runserver 0.0.0.0:8000
```

Health check: `GET http://localhost:8000/api/v1/health/`

Swagger: `http://localhost:8000/swagger/`

## Celery

```bash
cd vehicle_maintenance_scheduler
celery -A src.config worker --loglevel=info
```

## Docker

```bash
copy .env.example .env
docker compose up --build
```

## Production Command

```bash
gunicorn vehicle_maintenance_scheduler.src.config.wsgi:application --chdir vehicle_maintenance_scheduler --bind 0.0.0.0:8000 --workers 3
```

## Environment Variables

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CORS_ALLOWED_ORIGINS`
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`
- `REDIS_URL`
- `CELERY_BROKER_URL`, `CELERY_RESULT_BACKEND`
- `LOG_LEVEL`

## Root Structure

```text
backend-track/
  logging_middleware/
  vehicle_maintenance_scheduler/
  notification_app_be/
  notification_system_design.md
  Dockerfile
  docker-compose.yml
  requirements.txt
  .env.example
  .gitignore
  README.md
```
