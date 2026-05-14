from config.celery import app


@app.task(name="notification_app_be.health_ping")
def health_ping():
    return {"status": "ok", "service": "notification_app_be"}
