import matplotlib.pyplot as plt
import numpy as np


def ft_invert(arr: np.array) -> np.array:
    """
    ft_invert(arr: np.array) -> np.array

    Inverts the color of the image received and then
    displays the resulting image. Returns an array with
    inverted color values of pixels.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Argument must be a NumPy array.")

    if arr.ndim not in (2, 3):
        raise ValueError("Input must be a 2D or 3D image array.")

    if arr.ndim == 3 and arr.shape[2] not in (1, 3):
        raise ValueError("3D image must have 1 or 3 channels.")

    if not np.issubdtype(arr.dtype, np.integer):
        raise TypeError("Image array must contain int pixel values.")

    res_arr = 255 - arr

    plt.imshow(res_arr)
    plt.show()
    return res_arr


def ft_red(arr: np.array) -> np.array:
    """
    ft_red(arr: np.array) -> np.array

    Colors the image received into red and then
    displays the resulting image. Returns an array with
    changed values of pixels.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Argument must be a NumPy array.")

    if arr.ndim not in (2, 3):
        raise ValueError("Input must be a 2D or 3D image array.")

    if arr.ndim == 3 and arr.shape[2] not in (1, 3):
        raise ValueError("3D image must have 1 or 3 channels.")

    if not np.issubdtype(arr.dtype, np.integer):
        raise TypeError("Image array must contain int pixel values.")

    if arr.ndim == 3 and arr.shape[2] == 3:
        res_arr = np.copy(arr)
        for j in range(len(res_arr)):
            for i in range(len(res_arr[0])):
                res_arr[j][i][1] = 0
                res_arr[j][i][2] = 0
    else:
        gray = np.mean(arr, axis=-1)
        res_arr = np.stack([gray, np.zeros_like(gray), np.zeros_like(gray)],
                           axis=-1)

    plt.imshow(res_arr)
    plt.show()
    return res_arr


def ft_green(arr: np.array) -> np.array:
    """
    ft_green(arr: np.array) -> np.array

    Colors the image received into green and then
    displays the resulting image. Returns an array with
    changed values of pixels.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Argument must be a NumPy array.")

    if arr.ndim not in (2, 3):
        raise ValueError("Input must be a 2D or 3D image array.")

    if arr.ndim == 3 and arr.shape[2] not in (1, 3):
        raise ValueError("3D image must have 1 or 3 channels.")

    if not np.issubdtype(arr.dtype, np.integer):
        raise TypeError("Image array must contain int pixel values.")

    if arr.ndim == 3 and arr.shape[2] == 3:
        res_arr = np.copy(arr)
        for j in range(len(res_arr)):
            for i in range(len(res_arr[0])):
                res_arr[j][i][0] = 0
                res_arr[j][i][2] = 0
    else:
        gray = np.mean(arr, axis=-1)
        res_arr = np.stack([np.zeros_like(gray), gray, np.zeros_like(gray)],
                           axis=-1)

    plt.imshow(res_arr)
    plt.show()
    return res_arr


def ft_blue(arr: np.array) -> np.array:
    """
    ft_blue(arr: np.array) -> np.array

    Colors the image received into blue and then
    displays the resulting image. Returns an array with
    changed values of pixels.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Argument must be a NumPy array.")

    if arr.ndim not in (2, 3):
        raise ValueError("Input must be a 2D or 3D image array.")

    if arr.ndim == 3 and arr.shape[2] not in (1, 3):
        raise ValueError("3D image must have 1 or 3 channels.")

    if not np.issubdtype(arr.dtype, np.integer):
        raise TypeError("Image array must contain int pixel values.")

    if arr.ndim == 3 and arr.shape[2] == 3:
        res_arr = np.copy(arr)
        for j in range(len(res_arr)):
            for i in range(len(res_arr[0])):
                res_arr[j][i][0] = 0
                res_arr[j][i][1] = 0
    else:
        gray = np.mean(arr, axis=-1)
        res_arr = np.stack([np.zeros_like(gray), np.zeros_like(gray), gray],
                           axis=-1)

    plt.imshow(res_arr)
    plt.show()
    return res_arr


def ft_grey(arr: np.array) -> np.array:
    """
    ft_grey(arr: np.array) -> np.array

    Colors the image received into grey and then
    displays the resulting image. Returns an array with
    changed values of pixels.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Argument must be a NumPy array.")

    if arr.ndim not in (2, 3):
        raise ValueError("Input must be a 2D or 3D image array.")

    if arr.ndim == 3 and arr.shape[2] not in (1, 3):
        raise ValueError("3D image must have 1 or 3 channels.")

    if not np.issubdtype(arr.dtype, np.integer):
        raise TypeError("Image array must contain int pixel values.")

    res_arr = np.mean(arr, axis=-1)

    plt.imshow(res_arr, cmap="gray")
    plt.show()
    return res_arr
