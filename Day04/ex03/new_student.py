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
    """"""
    pass
