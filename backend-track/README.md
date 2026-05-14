# backend-track

This repository contains my backend evaluation work for the Backend Track. I kept the two problem statements separate because the vehicle scheduling task and notification priority task have different responsibilities, but they share the same basic Django/DRF setup and logging middleware.

## Projects

- `vehicle_maintenance_scheduler`: fetches depot/vehicle data and computes the best maintenance schedule.
- `notification_app_be`: fetches notifications and ranks the top 10 unread items for a priority inbox.
- `logging_middleware`: reusable Django middleware for request logging.
- `docs`: notes about structure and logging.
- `screenshots`: place for output/API screenshots.

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

## Gunicorn Command

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

## Logging

The request middleware writes JSON logs to `logs/app.log` using `RotatingFileHandler`. Each request log includes method, endpoint, status code, response time, timestamp, request ID, client IP, and error details if an exception occurs.

## Implementation Notes

- Vehicle scheduling is solved using 0/1 knapsack dynamic programming.
- Notification priority uses type weight first and timestamp second.
- The code does not hard-code API data; API responses are stored separately for review.
- The Django structure leaves space for auth, websocket notifications, caching, and background jobs if the project is extended.
