import sys as sys

def main():
    """
    Read two arguments - a string and an integer - and prints number of words from string that have a length greater than an integer number.

    If the number of arguments is different from 2, or if the type of any argument is wrong, prints AssertionError.
    """
    args = sys.argv[1:]
    args_num = len(args)

    if args_num != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    if not(args[0] != "" and all(ch.isalpha() or ch.isspace() for ch in args[0])):
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    try:
        limit = int(args[1])
    except (ValueError, TypeError):
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    sort_limit = lambda str : len(str) > limit
    sorted_list_words = [word for word in args[0].split() if sort_limit(word)]
    print(sorted_list_words)
    return 

if __name__ == "__main__":
    main()    