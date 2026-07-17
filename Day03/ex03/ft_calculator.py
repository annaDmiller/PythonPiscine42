class calculator:
    """Class that contains a vector of numbers with which math operations
    can be done"""
    def __init__(self, vector: list[int | float]):
        """__init__(self, vector: list[int | float])

        Initializes a vector from the list shared as parameter."""
        self.values = vector

    def __add__(self, object: int | float) -> None:
        """__add__(self, object: int | float) -> None

        Adds a scalar value given as parameter to the values from the
        vector saved in calculator."""
        self.values = [x + object for x in self.values]
        print(self.values)

    def __mul__(self, object: int | float) -> None:
        """__mul__(self, object: int | float) -> None

        Multiplies the values of the vector saved in calculator
        with a scalar value given as parameter."""
        self.values = [x * object for x in self.values]
        print(self.values)

    def __sub__(self, object: int | float) -> None:
        """__sub__(self, object: int | float) -> None

        Substracts a scalar value given as parameter from the values
        of the vector saved in calculator."""
        self.values = [x - object for x in self.values]
        print(self.values)

    def __truediv__(self, object: int | float) -> None:
        """__sub__(self, object: int | float) -> None

        Divides values from the vector saved in the calculater with
        a scalar value given as parameter."""
        try:
            self.values = [x / object for x in self.values]
        except ZeroDivisionError:
            print("Can't divide by zero.")
        else:
            print(self.values)
