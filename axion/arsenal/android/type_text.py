"""
Android text input action.
"""

from axion.devices import AndroidDevice


class TypeTextAction:
    """
    Type text on Android device.
    """

    def execute(
        self,
        text: str,
    ):
        device = AndroidDevice()

        return device.type_text(
            text
        )