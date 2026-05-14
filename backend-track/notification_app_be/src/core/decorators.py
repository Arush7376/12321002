from functools import wraps

from asgiref.sync import sync_to_async


def async_safe(func):
    """Run a synchronous callable safely from async code paths."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        return await sync_to_async(func, thread_sensitive=True)(*args, **kwargs)

    return wrapper
