"""
Axion execution engine.

Responsible for executing registered actions.
"""

from __future__ import annotations

from typing import Any

from axion.chronicle import get_logger
from axion.core.registry import ActionRegistry


logger = get_logger(__name__)


class Executor:
    """
    Executes Axion actions through the registry.
    """

    def __init__(
        self,
        registry: ActionRegistry | None = None,
    ) -> None:
        """
        Initialize executor.
        """

        self._registry = registry or ActionRegistry()


    def execute(
        self,
        action_name: str,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Execute a registered action.

        Parameters
        ----------
        action_name:
            Action identifier.

        args:
            Positional arguments.

        kwargs:
            Keyword arguments.
        """

        logger.info(
            "Executing action: %s",
            action_name,
        )

        action_class = self._registry.get(
            action_name
        )

        if action_class is None:
            raise ValueError(
                f"Unknown action: {action_name}"
            )

        action = action_class()

        return action.execute(
            *args,
            **kwargs,
        )