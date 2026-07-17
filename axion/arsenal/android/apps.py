"""
Android application actions.
"""

from __future__ import annotations

from axion.devices.android import AndroidDevice


class LaunchAppAction:
    """
    Launch Android application.
    """

    def execute(
        self,
        package: str,
    ):

        device = AndroidDevice()

        return device.launch_app(
            package
        )


class CloseAppAction:
    """
    Close Android application.
    """

    def execute(
        self,
        package: str,
    ):

        device = AndroidDevice()

        return device.close_app(
            package
        )


class ListAppsAction:
    """
    List installed Android applications.
    """

    def execute(
        self,
    ):

        device = AndroidDevice()

        return device.list_apps()