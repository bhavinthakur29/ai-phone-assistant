"""
Axion runtime bootstrap.
"""

from axion.core.registry import ActionRegistry

from axion.arsenal.android.home import HomeAction
from axion.arsenal.android.back import BackAction
from axion.arsenal.android.tap import TapAction
from axion.arsenal.android.type_text import TypeTextAction
from axion.arsenal.android.swipe import SwipeAction
from axion.arsenal.android.apps import (
    LaunchAppAction,
    CloseAppAction,
    ListAppsAction,
)


def create_registry() -> ActionRegistry:
    """
    Create default action registry.
    """

    registry = ActionRegistry()

    registry.register(
        "android.home",
        HomeAction,
    )

    registry.register(
        "android.back",
        BackAction,
    )

    registry.register(
        "android.tap",
        TapAction,
    )

    registry.register(
        "android.type",
        TypeTextAction,
    )

    registry.register(
        "android.swipe",
        SwipeAction,
    )

    registry.register(
        "android.launch",
        LaunchAppAction,
    )

    registry.register(
        "android.close",
        CloseAppAction,
    )

    registry.register(
        "android.apps",
        ListAppsAction,
    )

    return registry