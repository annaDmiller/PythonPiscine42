import numpy as np


def normalize_index(ind: int, size: int) -> int:
    """
    normalize_index(ind: int, size: int) -> int

    Takes a value of index and transforms it into a positive value of index.
    """
    return (ind if ind >= 0 else (size + ind))


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice_me(family: list, start: int, end: int) -> list

    Takes a 2D array, prints its shape and returns a truncated
    array based on start and end arguments. Start index is included,
    end index is excluded.
    """
    if type(start) is not int or type(end) is not int:
        raise TypeError("Start and End arguments must be integers.")

    if not isinstance(family, list):
        raise TypeError("2D array argument must be of list type.")

    if len(family) == 0:
        raise ValueError("2D array can't be empty.")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("2D array must contain lists only.")

    if not all(len(row) == len(family[0]) for row in family):
        raise AssertionError("Rows of 2D must be of the same length.")

    np_arr = np.array(family)
    n_rows = np_arr.shape[0]
    start_ind = normalize_index(start, n_rows)
    end_ind = normalize_index(end, n_rows)

    if start_ind < 0 or start_ind >= n_rows or end_ind < 0 or end_ind > n_rows:
        raise IndexError("Start and/or End values are out of range of 2D arr.")

    if end_ind < start_ind:
        raise ValueError("End index can't be less than Start index.")

    print("My shape is :", np_arr.shape)
    new_arr = np_arr[start_ind:end_ind]
    print("My new shape is :", new_arr.shape)

    return new_arr.tolist()
