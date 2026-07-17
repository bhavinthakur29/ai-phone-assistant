"""
Axion runtime context.

Stores transient runtime information.

Context is not configuration.
Context represents the current execution state.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class RuntimeContext:
    """
    Represents the current Axion runtime state.
    """

    session_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    started_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    environment: str = "development"


context = RuntimeContext()