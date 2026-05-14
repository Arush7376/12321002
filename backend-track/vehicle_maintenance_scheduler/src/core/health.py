from django.db import connections
from django.db.utils import OperationalError
from django.utils import timezone
from rest_framework.views import APIView

from src.core.responses import success_response


class HealthCheckView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        database_status = "ok"
        try:
            connections["default"].cursor()
        except OperationalError:
            database_status = "unavailable"

        return success_response(
            data={
                "service": "vehicle_maintenance_scheduler",
                "status": "ok",
                "database": database_status,
                "timestamp": timezone.now().isoformat(),
            },
            message="Service is healthy.",
        )
