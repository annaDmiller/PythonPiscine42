import sys as sys


def main():
    """Read one input string and print character category counts.

    If more than one argument is provided, print an AssertionError message.
    If no argument is provided, prompt the user and read from standard input.
    """
    PUNCT = r"""!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    size_args = len(sys.argv)

    if size_args > 2:
        print("AssertionError: more than one argument is provided")
        return

    elif size_args == 1:
        print("What is the next to count?")
        try:
            line = sys.stdin.read()
        except KeyboardInterrupt:
            print("An exception occured - input is interrupted")
            return

    else:
        line = sys.argv[1]

    num_upper = sum(ch.isupper() for ch in line)
    num_lower = sum(ch.islower() for ch in line)
    num_punct = sum(ch in PUNCT for ch in line)
    num_spaces = sum(ch in ' \n\r\t\v\f' for ch in line)
    num_digits = sum(ch.isdigit() for ch in line)

    print("The text contains", len(line), "characters:")
    print(num_upper, "upper letters")
    print(num_lower, "lower letters")
    print(num_punct, "punctuation marks")
    print(num_spaces, "spaces")
    print(num_digits, "digits")

    return


if __name__ == "__main__":
    main()
