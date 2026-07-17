"""
Android UI intelligence analyzer.
"""

from __future__ import annotations

from axion.chronicle import get_logger

from axion.oracle.android.ui.models import UIElement


logger = get_logger(__name__)


class UIAnalyzer:
    """
    Analyze UI elements for automation.
    """


    def find_clickable(
        self,
        elements: list[UIElement],
    ) -> list[UIElement]:
        """
        Return clickable elements.
        """

        return [
            element
            for element in elements
            if element.clickable
        ]



    def find_text(
        self,
        elements: list[UIElement],
        text: str,
    ) -> UIElement | None:
        """
        Find element by visible text.
        """

        text = text.lower()


        for element in elements:

            if (
                element.text
                and text in element.text.lower()
            ):
                return element


        return None



    def summarize(
        self,
        elements: list[UIElement],
    ) -> dict:
        """
        Create UI summary.
        """

        clickable = [
            e
            for e in elements
            if e.clickable
        ]


        return {

            "total": len(elements),

            "clickable": len(clickable),

            "texts": [
                e.text
                for e in elements
                if e.text
            ],

        }