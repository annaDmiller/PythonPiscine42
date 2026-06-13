import sys as sys
from ft_filter import ft_filter


def main():
    """
    Read two arguments - a string and an integer - and prints
    number of words from string that have a length greater
    than an integer number.

    If the number of arguments is different from 2, or if the type
    of any argument is wrong, prints AssertionError.
    """
    args_num = len(sys.argv)

    if args_num != 3:
        sys.exit("AssertionError: the arguments are bad")

    elif not (sys.argv[1] != ""
              and all(ch.isalnum() or ch.isspace() for ch in sys.argv[1])):
        sys.exit("AssertionError: the arguments are bad")

    args = sys.argv[1:]
    try:
        limit = int(args[1])
    except (ValueError, TypeError):
        sys.exit("AssertionError: the arguments are bad")

    print(ft_filter(lambda str: len(str) > limit, args[0].split()))
    return


if __name__ == "__main__":
    main()
