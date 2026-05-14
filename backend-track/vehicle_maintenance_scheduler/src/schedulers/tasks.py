from config.celery import app


@app.task(name="vehicle_maintenance_scheduler.health_ping")
def health_ping():
    return {"status": "ok", "service": "vehicle_maintenance_scheduler"}
