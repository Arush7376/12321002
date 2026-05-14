from django.urls import path

from core.health import HealthCheckView


app_name = "api_v1"

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
]
