import uuid


REQUEST_ID_HEADER = "HTTP_X_REQUEST_ID"


def get_or_create_request_id(request) -> str:
    request_id = request.META.get(REQUEST_ID_HEADER)
    if request_id:
        return request_id
    return str(uuid.uuid4())


def get_client_ip(request) -> str:
    forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR", "")
