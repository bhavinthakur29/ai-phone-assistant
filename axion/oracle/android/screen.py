"""
Android screen observation.

Responsibilities:
- Read display resolution.
- Read display density.

This module only observes state.
It does not perform actions.
"""

from __future__ import annotations

import re

from axion.chronicle import get_logger
from axion.nexus import ADBTransport


logger = get_logger(__name__)


class AndroidScreenOracle:
    """
    Provides Android display information.
    """


    def __init__(
        self,
        adb: ADBTransport | None = None,
    ) -> None:

        self._adb = adb or ADBTransport()



    def get_resolution(self) -> str:
        """
        Get Android display resolution.
        """

        logger.info(
            "Reading screen resolution."
        )

        result = self._adb.execute(
            [
                "shell",
                "wm",
                "size",
            ]
        )

        result.raise_for_error()

        match = re.search(
            r"(\d+x\d+)",
            result.stdout,
        )

        if not match:
            return "Unknown"

        return match.group(1)



    def get_density(self) -> str:
        """
        Get Android display density.
        """

        logger.info(
            "Reading screen density."
        )

        result = self._adb.execute(
            [
                "shell",
                "wm",
                "density",
            ]
        )

        result.raise_for_error()

        match = re.search(
            r"(\d+)",
            result.stdout,
        )

        if not match:
            return "Unknown"

        return match.group(1)



    def info(self) -> dict[str, str]:
        """
        Return complete display information.
        """

        return {
            "resolution": self.get_resolution(),
            "density": self.get_density(),
        }