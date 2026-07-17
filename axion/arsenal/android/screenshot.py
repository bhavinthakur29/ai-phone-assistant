"""
Android screenshot action.
"""

from axion.oracle.android.screenshot import (
    AndroidScreenshotOracle,
)


class ScreenshotAction:
    """
    Capture Android screenshot.
    """


    def execute(self):

        oracle = AndroidScreenshotOracle()

        return oracle.capture()