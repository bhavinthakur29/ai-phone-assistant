"""
Android UI hierarchy analyzer.

Oracle responsibility:
- Dump Android UI hierarchy
- Parse XML
- Provide UI element models
- Search UI elements
"""

from __future__ import annotations

import xml.etree.ElementTree as ET

from dataclasses import dataclass

from axion.chronicle import get_logger
from axion.nexus.adb import ADBTransport


logger = get_logger(__name__)


@dataclass
class UIElement:
    """
    Represents Android UI element.
    """

    text: str
    resource_id: str
    class_name: str
    clickable: bool
    bounds: str


    @property
    def center(self) -> tuple[int, int] | None:
        """
        Calculate center coordinate.
        """

        try:

            values = (
                self.bounds
                .replace("[", "")
                .replace("]", " ")
                .split()
            )

            x1, y1 = map(
                int,
                values[0].split(",")
            )

            x2, y2 = map(
                int,
                values[1].split(",")
            )

            return (
                (x1 + x2) // 2,
                (y1 + y2) // 2,
            )


        except Exception:

            return None



class UIParser:
    """
    Convert XML hierarchy into objects.
    """


    def parse(
        self,
        xml_data: str,
    ) -> list[UIElement]:

        logger.info(
            "Parsing UI hierarchy."
        )


        elements = []


        root = ET.fromstring(
            xml_data
        )


        for node in root.iter(
            "node"
        ):

            elements.append(

                UIElement(

                    text=node.attrib.get(
                        "text",
                        ""
                    ),

                    resource_id=node.attrib.get(
                        "resource-id",
                        ""
                    ),

                    class_name=node.attrib.get(
                        "class",
                        ""
                    ),

                    clickable=node.attrib.get(
                        "clickable",
                        "false"
                    ) == "true",

                    bounds=node.attrib.get(
                        "bounds",
                        ""
                    ),

                )

            )


        return elements



class UIAnalyzer:
    """
    Analyze UI elements.
    """


    def find_text(
        self,
        elements: list[UIElement],
        text: str,
    ) -> UIElement | None:
        """
        Find element by text.
        """

        text = text.lower()


        for element in elements:

            if (
                element.text
                and text in element.text.lower()
            ):
                return element


        return None



    def clickable_elements(
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



    def summarize(
        self,
        elements: list[UIElement],
    ) -> dict:
        """
        Create UI summary.
        """

        return {

            "total_elements": len(elements),

            "clickable_elements": len(
                self.clickable_elements(
                    elements
                )
            ),

            "visible_text": [
                element.text
                for element in elements
                if element.text
            ],

        }



class AndroidUI:
    """
    Android UI provider.
    """


    def __init__(
        self,
        adb: ADBTransport | None = None,
    ):

        self.adb = (
            adb
            or ADBTransport()
        )

        self.parser = UIParser()



    def dump(
        self,
    ) -> list[UIElement]:
        """
        Capture current UI hierarchy.
        """

        logger.info(
            "Dumping Android UI hierarchy."
        )


        self.adb.execute(
            [
                "shell",
                "uiautomator",
                "dump",
                "/sdcard/window.xml",
            ]
        ).raise_for_error()


        result = self.adb.execute(
            [
                "shell",
                "cat",
                "/sdcard/window.xml",
            ]
        )


        result.raise_for_error()


        return self.parser.parse(
            result.stdout
        )