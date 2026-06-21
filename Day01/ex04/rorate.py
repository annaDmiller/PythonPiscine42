from load_image import ft_load
import matplotlib.pyplot as plt
from numpy import array


def ft_transpose_array(src_arr: array) -> array:
    """
    ft_transpose_array(src_arr: array) -> array

    Gets an array as a parameter and transposes it.
    Returns a new ransposed array.
    """
    if src_arr.ndim == 2:
        height, width = src_arr.shape
    elif src_arr.ndim == 3:
        if src_arr.shape[2] != 1:
            raise ValueError("3D array must have (H, W, 1) shape.")
        height, width = src_arr.shape[0], src_arr.shape[1]
    else:
        raise ValueError("Array must be 2D or 3D.")

    if height != width:
        raise ValueError(f"Array is not square. Shape is: {src_arr.shape}")

    res = [[src_arr[j][i] for j in range(len(src_arr))]
           for i in range(len(src_arr[0]))]
    return array(res)


def main():
    """
    Loads an image, cuts a square part of it and transposes it.
    """
    image_path = "animal.jpeg"
    try:
        rgb_arr = ft_load(image_path)
        print(rgb_arr)

        square = rgb_arr[100:500, 500:900, 0:1]
        print("\nSquare part of the image:")
        print(square)

        rotated_arr = ft_transpose_array(square[:, :, 0])
        print("\nNew shape after Transpose:", rotated_arr.shape)
        print(rotated_arr)

        plt.imshow(rotated_arr, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
    return


if __name__ == "__main__":
    main()
