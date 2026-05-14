# logging_middleware

Reusable Django middleware for request/response logging.

## Features

- HTTP method and endpoint URL
- Status code
- Response time in milliseconds
- UTC timestamp
- Client IP address
- Exception stack traces
- File logging to `logs/app.log` through Django logging configuration

## Usage

Add the middleware to a Django project:

```python
MIDDLEWARE = [
    "logging_middleware.middleware.RequestResponseLoggingMiddleware",
]
```

Configure a `request_logger` logger in Django settings. The starter services already write to `logs/app.log`.
