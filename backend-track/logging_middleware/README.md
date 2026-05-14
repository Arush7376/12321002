# logging_middleware

Reusable Django middleware for request/response logging.

## Features

- HTTP method and endpoint URL
- Status code
- Response time in milliseconds
- UTC timestamp
- Client IP address
- Exception stack traces
- Structured JSON file logging to `logs/app.log` through Django logging configuration

## Usage

Add the middleware to a Django project:

```python
MIDDLEWARE = [
    "logging_middleware.middleware.RequestResponseLoggingMiddleware",
]
```

Configure a `request_logger` logger in Django settings. Both Django services in this repo already write to `logs/app.log`.

The package exposes `logging_middleware.logger.get_logger()` so APIs use centralized logging configuration instead of direct console logging.
