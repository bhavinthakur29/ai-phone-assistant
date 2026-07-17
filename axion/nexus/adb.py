"""
ADB communication transport.

Nexus responsibility:
- Execute ADB commands
- Return command results
- Handle communication failures
- Handle binary output streams
"""

from __future__ import annotations

import subprocess

from dataclasses import dataclass
from pathlib import Path

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
    raw: bytes | None = None


    @property
    def success(self) -> bool:
        """
        Whether command completed successfully.
        """

        return self.return_code == 0


    def raise_for_error(self) -> None:
        """
        Raise exception if command failed.
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
        Execute text based ADB command.
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
            )


        except OSError as exc:

            raise ADBError(
                str(exc)
            ) from exc



        return CommandResult(
            stdout=result.stdout.decode(
                "utf-8",
                errors="ignore",
            ),

            stderr=result.stderr.decode(
                "utf-8",
                errors="ignore",
            ),

            return_code=result.returncode,
        )



    def execute_binary(
        self,
        args: list[str],
        output_file: Path,
    ) -> CommandResult:
        """
        Execute ADB command producing binary output.

        Used for:
        - screenshots
        - files
        - media
        """

        command = [
            self.adb_path,
            *args,
        ]


        logger.info(
            "Executing binary ADB command: %s",
            command,
        )


        try:

            result = subprocess.run(
                command,
                capture_output=True,
            )


        except OSError as exc:

            raise ADBError(
                str(exc)
            ) from exc



        if result.returncode == 0:

            output_file.write_bytes(
                result.stdout
            )


        return CommandResult(
            stdout=(
                str(output_file)
                if result.returncode == 0
                else ""
            ),

            stderr=result.stderr.decode(
                "utf-8",
                errors="ignore",
            ).strip(),

            return_code=result.returncode,

            raw=result.stdout,
        )