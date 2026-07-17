"""
Chronicle

Centralized logging subsystem.

Responsibilities:
- Configure application logging
- Provide reusable loggers
- Write logs to console and file
- Ensure logging is configured only once

No other module should directly configure Python logging.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from axion.vault import paths

MAX_LOG_SIZE = 5 * 1024 * 1024
BACKUP_COUNT = 5

# -----------------------------------------------------------------------------
# Runtime Files
# -----------------------------------------------------------------------------

LOG_DIRECTORY = paths.logs
LOG_FILE = LOG_DIRECTORY / "axion.log"

DEFAULT_LOG_LEVEL = logging.INFO

LOG_FORMAT = (
    "[%(asctime)s] "
    "[%(levelname)s] "
    "[%(name)s] "
    "%(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# -----------------------------------------------------------------------------
# Internal State
# -----------------------------------------------------------------------------

_INITIALIZED = False


# -----------------------------------------------------------------------------
# Initialization
# -----------------------------------------------------------------------------

def _initialize_logging() -> None:
    """
    Configure the global logging system.

    This function is executed only once.
    """
    global _INITIALIZED

    if _INITIALIZED:
        return

    formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt=DATE_FORMAT,
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()

    if root_logger.handlers:
        root_logger.handlers.clear()

    root_logger.setLevel(DEFAULT_LOG_LEVEL)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    _INITIALIZED = True


# -----------------------------------------------------------------------------
# Public API
# -----------------------------------------------------------------------------
class Chronicle:

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        """
        Return a configured logger.

        Parameters
        ----------
        name:
            Usually __name__.

        Returns
        -------
        logging.Logger
        """
        _initialize_logging()

        return logging.getLogger(name)