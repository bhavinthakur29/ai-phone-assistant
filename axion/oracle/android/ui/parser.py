"""
Android UI XML parser.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET

from axion.chronicle import get_logger

from axion.oracle.android.ui.models import UIElement


logger = get_logger(__name__)


class UIParser:
    """
    Parses Android UI hierarchy XML.
    """

    def parse(
        self,
        xml_content: str,
    ) -> list[UIElement]:
        """
        Convert XML hierarchy into UI elements.
        """

        logger.info(
            "Parsing UI XML hierarchy."
        )

        root = ET.fromstring(
            xml_content
        )

        elements = []


        for node in root.iter(
            "node"
        ):

            element = UIElement(
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


            elements.append(
                element
            )


        return elements