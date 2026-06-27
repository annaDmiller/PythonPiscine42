from S1E9 import Character


class Baratheon(Character):
    """
    A member of Baratheon family character which inherits from Character
    class.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        return 


class Lannister(Character):
    """
    A member of Lannister family character which inherits from Character
    class.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    # decorator
    #def create_lannister(self, first_name: str, is_alive: bool = True):
        #return 
