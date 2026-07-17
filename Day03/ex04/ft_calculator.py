class calculator:
    """A calculator that allows to do calculations of 2 vectors:

    -dot product

    -addition

    -substraction"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dotproduct(V1: list[float], V2: list[float]) -> None

        Calculates the dot product of two vectors."""
        temp = [a * b for a, b in zip(V1, V2)]
        res = sum(x for x in temp)
        print(f"Dot product is : {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add_vec(V1: list[float], V2: list[float]) -> None

        Calculates the result of addition of two vectors."""
        res = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """sous_vec(V1: list[float], V2: list[float]) -> None

        Calculates the result of substraction of two vectors."""
        res = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is : {res}")
