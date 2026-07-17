"""
Android device abstraction.

Responsibilities:
- Represent an Android device.
- Provide high-level Android operations.
- Delegate communication to Nexus.

This module contains no ADB implementation details.
"""

from __future__ import annotations

from axion.chronicle import get_logger
from axion.nexus import ADBTransport, CommandResult
from pathlib import Path
from datetime import datetime

logger = get_logger(__name__)


class AndroidDevice:
    """
    High-level Android device interface.
    """

    BACK_KEY = 4
    HOME_KEY = 3

    def __init__(
        self,
        transport: ADBTransport | None = None,
    ) -> None:
        """
        Create Android device abstraction.

        Parameters
        ----------
        transport:
            Nexus transport implementation.
        """

        self._transport = transport or ADBTransport()


    # ---------------------------------------------------------
    # Connection
    # ---------------------------------------------------------

    def connect(self) -> CommandResult:
        """
        Check connected Android devices.
        """

        logger.info(
            "Checking Android connection."
        )

        return self._transport.execute(
            ["devices"]
        )


    def disconnect(self) -> None:
        """
        Disconnect device.

        Reserved for future wireless ADB/session handling.
        """

        logger.info(
            "Android device disconnected."
        )


    def is_connected(self) -> bool:
        """
        Check whether an Android device exists.
        """

        result = self.connect()

        if not result.success:
            return False

        return any(
            "\tdevice" in line
            for line in result.stdout.splitlines()[1:]
        )


    # ---------------------------------------------------------
    # Input
    # ---------------------------------------------------------

    def tap(
        self,
        x: int,
        y: int,
    ) -> CommandResult:
        """
        Tap screen coordinate.
        """

        logger.info(
            "Tap: %s,%s",
            x,
            y,
        )

        return self._transport.execute(
            [
                "shell",
                "input",
                "tap",
                str(x),
                str(y),
            ]
        )


    def swipe(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        duration: int = 300,
    ) -> CommandResult:
        """
        Swipe between coordinates.
        """

        logger.info(
            "Swipe: %s,%s -> %s,%s",
            x1,
            y1,
            x2,
            y2,
        )

        return self._transport.execute(
            [
                "shell",
                "input",
                "swipe",
                str(x1),
                str(y1),
                str(x2),
                str(y2),
                str(duration),
            ]
        )


    def type_text(
        self,
        text: str,
    ) -> CommandResult:
        """
        Type text into focused input.
        """

        logger.info(
            "Typing text."
        )

        text = text.replace(
            " ",
            "%s",
        )

        return self._transport.execute(
            [
                "shell",
                "input",
                "text",
                text,
            ]
        )


    def press_back(self) -> CommandResult:
        """
        Press Android back button.
        """

        logger.info(
            "Pressing back."
        )

        return self.keyevent(
            self.BACK_KEY
        )


    def home(self) -> CommandResult:
        """
        Press Android home button.
        """

        logger.info(
            "Pressing home."
        )

        return self.keyevent(
            self.HOME_KEY
        )


    def keyevent(
        self,
        keycode: int,
    ) -> CommandResult:
        """
        Send Android key event.
        """

        return self._transport.execute(
            [
                "shell",
                "input",
                "keyevent",
                str(keycode),
            ]
        )


    # ---------------------------------------------------------
    # Applications
    # ---------------------------------------------------------

    def launch_app(
        self,
        package_name: str,
    ) -> CommandResult:
        """
        Launch Android application.

        Parameters
        ----------
        package_name:
            Android package identifier.
        """

        logger.info(
            "Launching app: %s",
            package_name,
        )

        return self._transport.execute(
            [
                "shell",
                "monkey",
                "-p",
                package_name,
                "1",
            ]
        )


    def close_app(
        self,
        package_name: str,
    ) -> CommandResult:
        """
        Force stop Android application.

        Parameters
        ----------
        package_name:
            Android package identifier.
        """

        logger.info(
            "Closing app: %s",
            package_name,
        )

        return self._transport.execute(
            [
                "shell",
                "am",
                "force-stop",
                package_name,
            ]
        )


    def list_apps(
        self,
    ) -> CommandResult:
        """
        List installed Android applications.
        """

        logger.info(
            "Listing installed apps."
        )

        return self._transport.execute(
            [
                "shell",
                "pm",
                "list",
                "packages",
            ]
        )
    
        # ---------------------------------------------------------
    # Screen Capture
    # ---------------------------------------------------------

    def screenshot(
        self,
        output_dir: str = ".axion/screenshots",
    ) -> CommandResult:
        """
        Capture Android screen.

        Saves screenshot locally.
        """

        logger.info(
            "Capturing screenshot."
        )

        directory = Path(output_dir)

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = (
            datetime.now()
            .strftime(
                "screen_%Y%m%d_%H%M%S.png"
            )
        )

        output = directory / filename


        result = self._transport.execute_raw(
            [
                "exec-out",
                "screencap",
                "-p",
            ],
            output_file=output,
        )


        return result