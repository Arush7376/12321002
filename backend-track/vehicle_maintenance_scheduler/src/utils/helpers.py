import uuid
from datetime import UTC, datetime


def generate_request_id() -> str:
    return str(uuid.uuid4())


def utc_now_iso() -> str:
    return datetime.now(UTC).isoformat()
