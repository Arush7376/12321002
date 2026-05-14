import time
from datetime import UTC, datetime

from logging_middleware.logger import get_logger
from logging_middleware.utils import get_client_ip, get_or_create_request_id


logger = get_logger("request_logger")


class RequestResponseLoggingMiddleware:
    """Log request and response metadata in a reusable Django middleware."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()
        timestamp = datetime.now(UTC).isoformat()
        client_ip = get_client_ip(request)
        request_id = get_or_create_request_id(request)

        try:
            response = self.get_response(request)
        except Exception as exc:
            duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
            logger.error(
                "request_error",
                extra={
                    "request_id": request_id,
                    "method": request.method,
                    "endpoint": request.get_full_path(),
                    "status_code": 500,
                    "response_time_ms": duration_ms,
                    "timestamp": timestamp,
                    "client_ip": client_ip,
                    "error": str(exc),
                },
                exc_info=True,
            )
            raise

        duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
        response["X-Request-ID"] = request_id
        logger.info(
            "request_completed",
            extra={
                "request_id": request_id,
                "method": request.method,
                "endpoint": request.get_full_path(),
                "status_code": response.status_code,
                "response_time_ms": duration_ms,
                "timestamp": timestamp,
                "client_ip": client_ip,
                "error": None,
            },
        )
        return response
