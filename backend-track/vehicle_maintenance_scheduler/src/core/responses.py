from rest_framework.response import Response


def success_response(data=None, message="Success", status_code=200, meta=None):
    payload = {
        "success": True,
        "message": message,
        "data": data,
        "errors": None,
    }
    if meta is not None:
        payload["meta"] = meta
    return Response(payload, status=status_code)


def error_response(message="Error", errors=None, status_code=400, data=None):
    return Response(
        {
            "success": False,
            "message": message,
            "data": data,
            "errors": errors,
        },
        status=status_code,
    )
