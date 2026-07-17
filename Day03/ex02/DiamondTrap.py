from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A king that inherits from 2 families: Baratheon and Lannister."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """__init__(self, first_name: str, is_alive: bool = True)
        
        Initializes the King. Takes first_name and is_alive
        (non-mandatory, default=True) as paramters."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes_color: str):
        """set_eyes(self, eyes_color: str)
        
        Set the eyes color with the string value given as parameter."""
        self.eyes = eyes_color

    def set_hairs(self, hairs_color: str):
        """set_hairs(self, hairs_color: str)
        
        Set the hairs color with the string value given as parameter."""
        self.hairs = hairs_color

    def get_eyes(self) -> str:
        """get_eyes(self) -> str
        
        Returns a string with value of the eyes color."""
        return self.eyes

    def get_hairs(self) -> str:
        """get_hairs(self) -> str
        
        Returns a string with value of the hairs color."""
        return self.hairs
