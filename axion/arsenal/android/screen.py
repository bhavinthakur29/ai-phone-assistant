"""
Android screen information action.
"""

from __future__ import annotations

from axion.chronicle import get_logger
from axion.oracle.android.screen import AndroidScreenOracle


logger = get_logger(__name__)


class ScreenAction:
    """
    Action for retrieving Android screen information.
    """


    def execute(
        self,
    ):

        logger.info(
            "Executing screen information action."
        )

        oracle = AndroidScreenOracle()

        return oracle.info()