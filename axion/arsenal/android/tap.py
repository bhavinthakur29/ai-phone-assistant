"""
Android tap action.
"""

from axion.devices import AndroidDevice


class TapAction:
    """
    Tap screen coordinates.
    """

    def execute(
        self,
        x: int,
        y: int,
    ):
        device = AndroidDevice()

        return device.tap(
            x,
            y,
        )