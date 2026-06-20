from numpy import asarray, array
from PIL import Image as img


def ft_load(path: str) -> array:
    """
    ft_load(path: str) -> array

    Loads an image, prints its format and returns its
    pixels content in RGB format. Takes a path to the image
    as an argument. It processes JPG and JPEG images.
    """
    try:
        image = img.open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found with this path: {path}")
    except OSError:
        raise ValueError("Invalid image file or unsupported format.")

    if image.format not in ("JPEG", "JPG"):
        raise ValueError("Only JPG and JPED formats are supported.")

    rgb_img = image.convert("RGB")
    rgb_arr = asarray(rgb_img)
    print("The shape of image is:", rgb_arr.shape)

    return rgb_arr
