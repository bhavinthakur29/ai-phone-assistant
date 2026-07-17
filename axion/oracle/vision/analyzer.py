"""
Screen analysis engine.

Responsible for extracting
basic visual information.

No AI inference yet.
"""

from __future__ import annotations

from dataclasses import dataclass

from PIL import Image

from axion.chronicle import get_logger
from axion.oracle.vision.image import ImageFrame


logger = get_logger(__name__)


@dataclass
class ScreenState:
    """
    Represents analyzed screen state.
    """

    width: int
    height: int
    brightness: float
    average_color: tuple[int, int, int]



class ScreenAnalyzer:
    """
    Basic visual analyzer.
    """


    def analyze(
        self,
        frame: ImageFrame,
    ) -> ScreenState:
        """
        Analyze image frame.
        """

        logger.info(
            "Analyzing screen image."
        )


        image = Image.open(
            frame.path
        ).convert(
            "RGB"
        )


        pixels = list(
            image.getdata()
        )


        total = len(
            pixels
        )


        avg = tuple(
            sum(
                pixel[i]
                for pixel in pixels
            ) // total

            for i in range(3)
        )


        brightness = (
            sum(avg) / 3
        ) / 255



        image.close()


        return ScreenState(
            width=frame.width,
            height=frame.height,
            brightness=round(
                brightness,
                3,
            ),
            average_color=avg,
        )