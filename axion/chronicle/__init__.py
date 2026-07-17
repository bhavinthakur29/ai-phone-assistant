"""
Chronicle

Centralized logging subsystem for Axion.

Public API:
    from axion.chronicle import get_logger
"""

from .chronicle import get_logger

__all__ = ["get_logger"]