"""
Android UI data models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class UIElement:
    """
    Represents a single Android UI element.
    """

    text: str
    resource_id: str
    class_name: str
    clickable: bool
    bounds: str


    @property
    def center(self) -> tuple[int, int] | None:
        """
        Calculate element center coordinate.
        """

        try:

            value = (
                self.bounds
                .replace("[", "")
                .replace("]", " ")
                .strip()
            )

            parts = value.split()

            x1, y1 = map(
                int,
                parts[0].split(",")
            )

            x2, y2 = map(
                int,
                parts[1].split(",")
            )

            return (
                (x1 + x2) // 2,
                (y1 + y2) // 2,
            )

        except Exception:
            return None