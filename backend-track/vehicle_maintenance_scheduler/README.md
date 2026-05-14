# vehicle_maintenance_scheduler

This service contains the solution for the vehicle maintenance scheduling problem. It fetches depot and vehicle task data from the evaluation APIs and chooses the task subset that maximizes impact without crossing the mechanic-hour budget.

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

## Scheduling Logic

The scheduler uses the 0/1 knapsack approach:

- `Duration` is treated as the cost.
- `Impact` is treated as the value.
- `MechanicHours` is the capacity.

The implementation is in `src/services/maintenance_scheduler.py`. API responses and output files are stored under `api_responses/` and `vehicle_scheduling/`.

## Logging

Structured JSON request logs are written to `logs/app.log` by the shared `logging_middleware` package. APIs should obtain loggers through `logging_middleware.logger.get_logger()`.
