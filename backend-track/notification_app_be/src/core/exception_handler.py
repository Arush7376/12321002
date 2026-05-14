from rest_framework import status
from rest_framework.views import exception_handler

from logging_middleware.logger import get_logger
from core.responses import error_response


logger = get_logger(__name__)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        detail = response.data.get("detail", response.data)
        return error_response(
            message=str(detail) if isinstance(detail, str) else "Request validation failed.",
            errors=response.data,
            status_code=response.status_code,
        )

    logger.exception("Unhandled exception", exc_info=exc)
    return error_response(
        message="Internal server error.",
        errors={"detail": "An unexpected error occurred."},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
