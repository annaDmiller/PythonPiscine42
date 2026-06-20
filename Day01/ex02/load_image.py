from numpy import asarray, array
from PIL import Image as img
from PIL import UnidentifiedImageError


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
        raise FileNotFoundError(f"File not found: {path}") from None
    except PermissionError:
        raise PermissionError(f"No access to the file: {path}") from None
    except IsADirectoryError:
        raise IsADirectoryError(f"This is a directory: {path}") from None
    except UnidentifiedImageError:
        raise UnidentifiedImageError("Incorrect format of image.") from None
    except OSError:
        raise OSError("OS error occured. Try once more later.") from None

    if image.format not in ("JPEG", "JPG"):
        raise ValueError("Only JPG and JPED formats are supported.")

    rgb_img = image.convert("RGB")
    rgb_arr = asarray(rgb_img)
    print("The shape of image is:", rgb_arr.shape)

    return rgb_arr
