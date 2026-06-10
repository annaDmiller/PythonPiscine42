import sys as sys


def main():
    """
    Takes a string as an argument and encodes it into Morse Code.

    The program supports spaces and alphanumeric characters only.

    If the number of arguments is different from 1, or the type of
    any argument is wrong, prints AssertionError.
    """

    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. ",
                    "0": "----- "}

    args = sys.argv[1:]
    size_args = len(args)

    if size_args != 1 or not (args[0] != ""
                              and all(ch == ' ' or ch.isalnum()
                                      for ch in args[0])):
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    print("".join(NESTED_MORSE[ch] for ch in args[0].upper()).rstrip())
    return


if __name__ == "__main__":
    main()
