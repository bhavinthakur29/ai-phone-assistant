"""
Action registry.

Responsible for storing and retrieving
available Axion actions.

Registry does not execute actions.
"""

from __future__ import annotations

from typing import Callable, Any

from axion.chronicle import get_logger


logger = get_logger(__name__)


class ActionRegistry:
    """
    Stores executable Axion actions.

    The registry only manages registration
    and lookup. Execution is handled by Executor.
    """

    def __init__(self) -> None:
        self._actions: dict[str, Callable[..., Any]] = {}

    def register(
        self,
        name: str,
        action: Callable[..., Any],
    ) -> None:
        """
        Register an action.

        Parameters
        ----------
        name:
            Action identifier.

        action:
            Callable action implementation.
        """

        logger.info(
            "Registering action: %s",
            name,
        )

        self._actions[name] = action


    def get(
        self,
        name: str,
    ) -> Callable[..., Any] | None:
        """
        Retrieve an action.
        """

        return self._actions.get(name)


    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether an action exists.
        """

        return name in self._actions


    def list_actions(self) -> list[str]:
        """
        Return available action names.
        """

        return list(self._actions.keys())