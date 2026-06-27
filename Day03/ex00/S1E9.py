from abc import ABC, abstractmethod


class Character(ABC):
    """
    An abstract class "Character" for describing the characters
    of GOT.
    """
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initializes the Character. Takes first_name and is_alive
        (non-mandatory, default=True) as paramters.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """
        "Kills" the character: is_alive attribute is set to False.
        """
        self.is_alive = False


class Stark(Character):
    """
    A member of Stark family character which inherits from Character
    class.
    """
    def __init__(elf, first_name: str, is_alive: bool = True):
        """
        Initializes the Character of Stark family.
        """
        super().__init__(first_name, is_alive)
