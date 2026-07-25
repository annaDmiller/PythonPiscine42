import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate_id() -> str

    Generates an Id for the studen. The Id contains 15 ascii
    lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A class that represents a student in the system.
    Contains attributes:

    -name

    -surname

    -active flag (default=True)

    -login (non initializable): 1 letter of Name + surname

    -id (non initializable): 15 random letters"""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(default="", init=False)
    id: str = field(default="", init=False)

    def __post_init__(self):
        """__post_init__(self)

        Adds custom logic of login and id calculation and assignment
        on init."""
        self.login = self.name[0] + self.surname
        self.id = generate_id()
