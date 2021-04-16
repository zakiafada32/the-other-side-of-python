import numpy as np
from PIL import Image
from typing import Literal, Union

White = tuple[Literal[255], Literal[255], Literal[255]]
Black = tuple[Literal[0], Literal[0], Literal[0]]

Color = dict[
    str,
    Union[White, Black],
]


class Canvas:
    """Object where all shapes are going to be drawn"""

    def __init__(self, height: int, width: int, color: Union[White, Black]):
        self.color = color
        self.height = height
        self.width = width

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath: str):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)