def square(x: int | float) -> int | float:
    """square(x: int | float) -> int | float

    Calculates a square of argument and returns it."""
    return x * x


def pow(x: int | float) -> int | float:
    """pow(x: int | float) -> int | float

    Calculates the exponentiation of argument by itself
    and returns it."""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer(x: int | float, function) -> object

    Takes as argument a number and a function. Returns
    an object that when called returns the result of the
    arguments calculation."""
    count = 0

    def inner() -> float:
        """inner() -> float

        Returns the result of the arguments calculation."""
        nonlocal x
        nonlocal count

        x = function(x)
        count += 1
        return x

    return inner
