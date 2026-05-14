import logging
import time
from datetime import UTC, datetime


logger = logging.getLogger("request_logger")


class RequestResponseLoggingMiddleware:
    """Log request and response metadata in a reusable Django middleware."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()
        timestamp = datetime.now(UTC).isoformat()
        client_ip = self._get_client_ip(request)

        try:
            response = self.get_response(request)
        except Exception as exc:
            duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
            logger.exception(
                "request_error method=%s path=%s status_code=%s duration_ms=%s timestamp=%s client_ip=%s error=%s",
                request.method,
                request.get_full_path(),
                500,
                duration_ms,
                timestamp,
                client_ip,
                exc,
            )
            raise

        duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
        logger.info(
            "request_completed method=%s path=%s status_code=%s duration_ms=%s timestamp=%s client_ip=%s",
            request.method,
            request.get_full_path(),
            response.status_code,
            duration_ms,
            timestamp,
            client_ip,
        )
        return response

    @staticmethod
    def _get_client_ip(request):
        forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if forwarded_for:
            return forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR", "")
