import numpy as np


def is_valid_number_list(lst: list[int | float]) -> bool:
    """
    is_valid_number_list(lst: list[int | float]) -> bool

    Verifies if the values in the given list are integers or floats.
    Returns True if all values are integers or floats.
    Otherwise, returns False.
    """
    return (isinstance(lst, list)
            and all(type(x) in (int, float) for x in lst))


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]

    Returns the list of values of Body Mass index
    calculated based on the given arguments.
    """
    if (not is_valid_number_list(height) or not is_valid_number_list(weight)):
        raise TypeError("Height and weight must be lists of int or float.")

    if len(height) != len(weight):
        raise ValueError("Height and weight must have the same length.")

    h_nparr = np.array(height, dtype=float)
    w_nparr = np.array(weight, dtype=float)

    if np.any(h_nparr <= 0) or np.any(w_nparr <= 0):
        raise ValueError("Height and weight values must be positive.")

    bmi_nparr = w_nparr / (h_nparr ** 2)
    return bmi_nparr.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]

    Verifies if the given values of the bmi list are above or below the limit.
    Returns True if the value is above the limit. Otherwise, returns False.
    """
    if not is_valid_number_list(bmi):
        raise TypeError("BMI must be a list of int or float.")

    if type(limit) is not int:
        raise TypeError("Limit must be an int value.")

    bmi_nparr = np.array(bmi, dtype=float)

    if np.any(bmi_nparr <= 0):
        raise ValueError("BMI values can't be negative or zero.")

    return (bmi_nparr > limit).tolist()
