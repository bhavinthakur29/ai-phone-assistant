"""
Axion command dispatcher.

Responsible for translating user input
into executable actions.

Dispatcher does not contain business logic.
"""

from __future__ import annotations

import shlex
from typing import Any

from axion.chronicle import get_logger
from axion.core.executor import Executor


logger = get_logger(__name__)


class Dispatcher:
    """
    Routes commands to the execution engine.
    """

    def __init__(
        self,
        executor: Executor,
    ) -> None:
        """
        Initialize dispatcher.

        Parameters
        ----------
        executor:
            Axion execution engine.
        """

        self._executor = executor


    def dispatch(
        self,
        command: str,
    ) -> Any:
        """
        Parse and execute command.

        Example:

            android.home

            android.tap 500 500
        """

        logger.info(
            "Dispatching command: %s",
            command,
        )

        parts = shlex.split(command)

        if not parts:
            return None


        action_name = parts[0]

        args = parts[1:]


        return self._executor.execute(
            action_name,
            *args,
        )