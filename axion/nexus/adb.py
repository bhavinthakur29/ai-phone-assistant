"""
ADB communication transport.

Nexus responsibility:
- Execute ADB commands
- Return command results
- Handle communication failures
"""

from __future__ import annotations

import subprocess

from dataclasses import dataclass

from axion.vault import settings
from axion.chronicle import get_logger

from axion.nexus.exceptions import ADBError


logger = get_logger(__name__)


@dataclass
class CommandResult:
    """
    Result of an ADB command execution.
    """

    stdout: str
    stderr: str
    return_code: int

    @property
    def success(self) -> bool:
        """
        Whether command completed successfully.
        """
        return self.return_code == 0

    def raise_for_error(self) -> None:
        """
        Raise an exception if command failed.
        """

        if not self.success:
            raise ADBError(
                self.stderr or "Unknown ADB error"
            )


class ADBTransport:
    """
    Low-level ADB communication layer.
    """

    def __init__(
        self,
        adb_path: str | None = None,
    ) -> None:

        self.adb_path = (
            adb_path
            or settings.adb.path
        )


    def execute(
        self,
        args: list[str],
    ) -> CommandResult:
        """
        Execute an ADB command.
        """

        command = [
            self.adb_path,
            *args,
        ]

        logger.info(
            "Executing ADB command: %s",
            command,
        )

        try:

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
            )

        except OSError as exc:

            raise ADBError(
                str(exc)
            ) from exc


        return CommandResult(
            stdout=result.stdout.strip(),
            stderr=result.stderr.strip(),
            return_code=result.returncode,
        )
    