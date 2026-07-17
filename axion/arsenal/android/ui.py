"""
Android UI action.
"""

from __future__ import annotations

from axion.chronicle import get_logger
from axion.oracle.android.ui import AndroidUI


logger = get_logger(__name__)


class UIAction:
    """
    Dump Android UI hierarchy.
    """


    def execute(
        self,
    ):

        logger.info(
            "Executing UI dump action."
        )


        ui = AndroidUI()

        elements = ui.dump()


        return [
            {
                "text": item.text,
                "resource_id": item.resource_id,
                "class": item.class_name,
                "clickable": item.clickable,
                "bounds": item.bounds,
            }
            for item in elements
        ]