from S1E9 import Character


class Baratheon(Character):
    """A member of Baratheon family character which inherits from Character
    class."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes a member of Baratheon family."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """Returns the a human-readable string for end users of the
        Baratheon class."""
        return f'(\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'

    def __repr__(self) -> str:
        """Returns the technical string representation of the object."""
        return 'Vector: ' + self.__str__()


class Lannister(Character):
    """A member of Lannister family character which inherits from Character
    class."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes a member of Lannister family."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Returns the a human-readable string for end users of the
        Lannister class."""
        return f'(\'{self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'

    def __repr__(self) -> str:
        """Returns the technical string representation of the object."""
        return 'Vector: ' + self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Creates a member of Lannister family in a chain."""
        return cls(first_name, is_alive)
