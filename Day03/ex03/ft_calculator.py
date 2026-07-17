class calculator:
    """Class that contains a vector of numbers with which math operations
    can be done"""
    def __init__(self, vector: list[int | float]):
        """__init__(self, vector: list[int | float])
        
        Initializes a vector from the list shared as parameter."""
        if not isinstance(vector, list):
            raise TypeError("The calculator takes only the vector of numbers.")
        if not all(type(x) in (int, float) for x in vector):
            raise TypeError("Values of the vector must be int or float")
        self.values = vector

    def __add__(self, object: int | float) -> None:
        """__add__(self, object: int | float) -> None
        
        Adds a scalar value given as parameter to the values from the
        vector saved in calculator."""
        if type(object) not in (int, float):
            raise TypeError("The addition can be done only with int/float" +
                            " number.")
        self.values = [x + object for x in self.values]
        print(self.values)

    def __mul__(self, object: int | float) -> None:
        """__mul__(self, object: int | float) -> None
        
        Multiplies the values of the vector saved in calculator
        with a scalar value given as parameter."""
        if type(object) not in (int, float):
            raise TypeError("The multiplication can be done only with" +
                            " int/float number.")
        self.values = [x * object for x in self.values]
        print(self.values)

    def __sub__(self, object: int | float) -> None:
        """__sub__(self, object: int | float) -> None
        
        Substracts a scalar value given as parameter from the values
        of the vector saved in calculator."""
        if type(object) not in (int, float):
            raise TypeError("The substraction can be done only with " +
                            "int/float number.")
        self.values = [x - object for x in self.values]
        print(self.values)

    def __truediv__(self, object: int | float) -> None:
        """__sub__(self, object: int | float) -> None
        
        Divides values from the vector saved in the calculater with
        a scalar value given as parameter."""
        if type(object) not in (int, float):
            raise TypeError("The division can be done only with int/float " +
                            "number.")
        self.values = [x / object for x in self.values]
        print(self.values)
