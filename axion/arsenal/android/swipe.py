"""
Android swipe action.
"""

from __future__ import annotations

from typing import Any

from axion.devices.android import AndroidDevice


class SwipeAction:
    """
    Execute Android swipe gesture.
    """

    def execute(
        self,
        x1: str,
        y1: str,
        x2: str,
        y2: str,
        duration: str = "300",
    ) -> Any:
        """
        Perform swipe gesture.

        Parameters
        ----------
        x1:
            Starting X coordinate.

        y1:
            Starting Y coordinate.

        x2:
            Ending X coordinate.

        y2:
            Ending Y coordinate.

        duration:
            Swipe duration in milliseconds.
        """

        device = AndroidDevice()

        return device.swipe(
            int(x1),
            int(y1),
            int(x2),
            int(y2),
            int(duration),
        )