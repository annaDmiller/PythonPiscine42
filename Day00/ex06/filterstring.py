import sys as sys

def check_limit(limit):
    return lambda str : len(str) > limit

def main():
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

    list_words = args[0].split()
    sort_limit = check_limit(limit)
    sorted_list_words = [word for word in list_words if sort_limit(word)]
    print(sorted_list_words)

if __name__ == "__main__":
    main()    