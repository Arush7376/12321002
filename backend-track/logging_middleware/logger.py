import logging


def get_logger(name: str) -> logging.Logger:
    """Return a configured application logger without creating ad hoc handlers."""

    return logging.getLogger(name)
