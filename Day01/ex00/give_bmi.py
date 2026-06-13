def verify_int_or_float(lst: list[int | float]) -> bool:
    """
    verify_int_or_float(lst: list[int | float]) -> bool

    Verify if the values in the given list are integers or floats.
    Return True if all values are integers or floats. Otherwise, returns False.
    """
    for item in lst:
        match item:
            case int():
                continue

            case float():
                continue

            case _:
                return False

    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]

    Returns the list of values of Body Mass index
    calculated based on the given arguments.
    """
    if len(height) != len(weight):
        print("The range of two lists is not the same. Please, review them.")
        return None

    try:
        assert verify_int_or_float(height)
        assert verify_int_or_float(weight)
    except AssertionError:
        print("The values in the arguments can be only int or float.", end="")
        print("Please, review them.")
        return None

    if all(h == 0 for h in height):
        print("The height can't be 0 (division by 0). Please, review.")
        return None

    return list((weight[ind] / (height[ind] * height[ind])
                 for ind in range(len(weight))))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]

    Verifies if the given values of the bmi list are above or below the limit.
    Returns True if the value is above the limit. Otherwise, returns False.
    """
    
