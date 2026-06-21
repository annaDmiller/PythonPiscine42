from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """
    Loads an image "animal.jpeg", prints information about it,
    and displays it after zooming.
    """
    image_path = "animal.jpeg"
    try:
        rgb_arr = ft_load(image_path)
        print(rgb_arr)

        zoomed_arr = rgb_arr[100:500, 500:900, 0:1]
        print("New shape after slicing:", zoomed_arr.shape, end="")
        print(f" or ({zoomed_arr.shape[0]}, {zoomed_arr.shape[1]})")
        print(zoomed_arr)

        plt.imshow(zoomed_arr[:, :, 0], cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
    return


if __name__ == "__main__":
    main()
