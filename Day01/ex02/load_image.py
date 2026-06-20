from numpy import asarray
import numpy as array
from PIL import Image as img


def ft_load(path: str) -> array:
    """
    ft_load(path: str) -> array

    Loads an image, prints its format and returns its
    pixels content in RGB format. Takes a path to the image
    as an argument. It processes JPG and JPEG images.
    """
    image = img.open(path)
    rgb_arr = asarray(image)
    print("The shape of image is:", rgb_arr.shape)

    return rgb_arr
