"""
Android back action.
"""

from axion.devices import AndroidDevice


class BackAction:
    """
    Press Android back button.
    """

    def execute(self):
        device = AndroidDevice()

        return device.press_back()