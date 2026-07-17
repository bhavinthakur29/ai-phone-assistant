"""
Android home action.
"""

from axion.arsenal import Action
from axion.devices import AndroidDevice


class HomeAction(Action):
    """
    Press Android home button.
    """

    def execute(
        self,
        **kwargs,
    ):
        device = AndroidDevice()

        return device.home()