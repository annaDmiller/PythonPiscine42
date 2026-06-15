def verify_int_or_float(lst: list[int | float]) -> bool:
    """
    verify_int_or_float(lst: list[int | float]) -> bool

    Verifies if the values in the given list are integers or floats.
    Returns True if all values are integers or floats. Otherwise, returns False.
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

def check_negative_zero(lst: list[int | float]) -> bool:
    """
    check_negative(lst: list[int | float]) -> bool

    Verifies if the values in the given list are negative or zero.
    Returns True if all values are positive. Otherwise, returns False.
    """
    return all(int(lst[ind]) <= 0 for ind in range(len(lst)))


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]

    Returns the list of values of Body Mass index
    calculated based on the given arguments.
    """
    if height is None or weight is None:
        print("At least 1 of the argument is None. Please, review.")
        return None

    if len(height) != len(weight):
        print("The range of two lists is not the same. Please, review them.")
        return None

    try:
        assert verify_int_or_float(height)
        assert verify_int_or_float(weight)
    except AssertionError:
        print("The values in the arguments can be only int or float.", end="")
        print(" Please, review them.")
        return None
    
    try:
        assert check_negative_zero(height)
        assert check_negative_zero(weight)
    except AssertionError:
        print("Height/weight values must be positive. Please, review them.")
        return None

    try:
        return list((weight[ind] / (height[ind] * height[ind])
                 for ind in range(len(weight))))
    except ZeroDivisionError:
        print("The height can't be 0 (division by 0). Please, review.")
        return None



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(bmi: list[int | float], limit: int) -> list[bool]

    Verifies if the given values of the bmi list are above or below the limit.
    Returns True if the value is above the limit. Otherwise, returns False.
    """
    if bmi is None or limit is None:
        print("At least 1 of the argument is None. Please, review.")
        return None
    
    try:
        assert verify_int_or_float(bmi)
        int_limit = int(limit)
    except AssertionError:
        print("The values of the bmi can be only int or float.", end="")
        print("Please, review them.")
        return None
    except (TypeError, ValueError):
        print("Limit value is incorrect. Please, review it.")
        return None
    
    try:
        assert check_negative_zero(bmi)
    except AssertionError:
        print("The values of bmi must be positive. Please, review them.")
        return None
    else:
        return list(bmi[ind] > int_limit for ind in range(len(bmi)))
