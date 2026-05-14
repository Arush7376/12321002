from rest_framework.exceptions import APIException


class ApplicationError(APIException):
    status_code = 400
    default_detail = "Application error."
    default_code = "application_error"


class ResourceNotFoundError(ApplicationError):
    status_code = 404
    default_detail = "Requested resource was not found."
    default_code = "resource_not_found"


class ConflictError(ApplicationError):
    status_code = 409
    default_detail = "Resource conflict."
    default_code = "resource_conflict"


class ExternalServiceError(ApplicationError):
    status_code = 502
    default_detail = "External service error."
    default_code = "external_service_error"
