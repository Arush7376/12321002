# Logging Architecture

The shared `logging_middleware` package centralizes request logging for all Django services.

## Output

Logs are written to `logs/app.log` using `RotatingFileHandler` and structured JSON formatting.

## Request Fields

- `request_id`
- `method`
- `endpoint`
- `status_code`
- `response_time_ms`
- `timestamp`
- `client_ip`
- `error`

## Usage

Application code should use `logging_middleware.logger.get_logger()` and avoid ad hoc console logging.
