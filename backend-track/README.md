# backend-track

Production-grade Django backend starter for Backend Track evaluation work. The repository contains two modular DRF services, centralized structured logging, Docker orchestration, and a reusable request logging middleware package.

## Projects

- `vehicle_maintenance_scheduler`: vehicle CRUD and maintenance scheduler foundation.
- `notification_app_be`: queue-driven notification system foundation.
- `logging_middleware`: reusable Django middleware for structured JSON request logging.
- `docs`: architecture and extension notes.
- `screenshots`: evaluation screenshots and API proof captures.

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
python vehicle_maintenance_scheduler/src/manage.py migrate
python vehicle_maintenance_scheduler/src/manage.py runserver 0.0.0.0:8000
```

Health check: `GET http://localhost:8000/api/v1/health/`

Swagger: `http://localhost:8000/swagger/`

## Celery

```bash
cd vehicle_maintenance_scheduler
celery -A config worker --loglevel=info
```

## Docker

```bash
copy .env.example .env
docker compose up --build
```

## Production Command

```bash
gunicorn config.wsgi:application --chdir vehicle_maintenance_scheduler/src --bind 0.0.0.0:8000 --workers 3
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
- `DJANGO_ENV`

## Root Structure

```text
backend-track/
  logging_middleware/
  vehicle_maintenance_scheduler/
  notification_app_be/
  screenshots/
  docs/
  notification_system_design.md
  Dockerfile
  docker-compose.yml
  requirements.txt
  .env.example
  .gitignore
  README.md
```

## Logging Architecture

All API and middleware logs flow through centralized Python loggers configured in Django settings. Request logs are JSON formatted and written with `RotatingFileHandler` to `logs/app.log`. The request middleware records method, endpoint, status code, response time, timestamp, request ID, client IP, and exception details.

## Architecture Readiness

The services are prepared for JWT auth, scheduler engines, notification queues, websocket notifications, Redis caching, provider clients, and optimization algorithms through dedicated packages under each service's `src/` directory.
