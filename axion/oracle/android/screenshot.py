"""
Android screenshot oracle.

Provides visual state capture
for AI perception.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from axion.chronicle import get_logger
from axion.nexus import ADBTransport


logger = get_logger(__name__)


class AndroidScreenshotOracle:
    """
    Capture Android device screenshots.
    """


    def __init__(
        self,
        adb: ADBTransport | None = None,
    ) -> None:

        self._adb = adb or ADBTransport()



    def capture(
        self,
        output_dir: str = ".axion/reports",
    ) -> str:
        """
        Capture current Android screen.

        Returns:
            Screenshot path.
        """

        logger.info(
            "Capturing Android screenshot."
        )


        directory = Path(output_dir)

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )


        filename = (
            "screenshot_"
            + datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )
            + ".png"
        )


        path = directory / filename



        result = self._adb.execute_binary(
            [
                "exec-out",
                "screencap",
                "-p",
            ],
            path,
        )


        result.raise_for_error()


        return str(path)