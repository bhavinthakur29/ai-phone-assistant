"""
Image perception primitives.

Responsible for:
- Loading images
- Providing image metadata
- Preparing images for analysis

No AI logic here.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from PIL import Image

from axion.chronicle import get_logger


logger = get_logger(__name__)


@dataclass
class ImageFrame:
    """
    Represents an image captured from a device.
    """

    path: str
    width: int
    height: int
    format: str



class ImageLoader:
    """
    Loads images into Axion perception system.
    """


    def load(
        self,
        image_path: str,
    ) -> ImageFrame:
        """
        Load image file.

        Parameters
        ----------
        image_path:
            Image location.

        Returns
        -------
        ImageFrame
        """

        logger.info(
            "Loading image: %s",
            image_path,
        )


        path = Path(image_path)


        if not path.exists():

            raise FileNotFoundError(
                image_path
            )


        image = Image.open(
            path
        )


        frame = ImageFrame(
            path=str(path),
            width=image.width,
            height=image.height,
            format=image.format or "unknown",
        )


        image.close()


        return frame