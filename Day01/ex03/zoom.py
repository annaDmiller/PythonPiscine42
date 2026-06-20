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

        zoomed_arr = rgb_arr[100:500, 100:500, 0:1]
        print("New shape after slicing:", zoomed_arr.shape)
        print(zoomed_arr)

        plt.imshow(zoomed_arr[:, :, 0])
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
    return


if __name__ == "__main__":
    main()
