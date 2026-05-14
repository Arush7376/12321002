import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings.development")

app = Celery("notification_app_be")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
