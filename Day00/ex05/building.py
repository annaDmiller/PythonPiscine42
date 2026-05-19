import sys as sys

#add ___doc___
#process Ctrl + C exception
#find a better way to write function (?)

def main():
    PUNCT = r"""!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    args = sys.argv[1:]
    size_args = len(args)

    if size_args > 1:
        print("AssertionError: more than one argument is provided")
        exit(1)
    
    if size_args == 0:
        print("What is the next to count?")
        line = sys.stdin.read()
        
    else:
        line = args[0]

    num_upper = 0
    num_lower = 0
    num_punct = 0
    num_spaces = 0
    num_digits = 0
    num_chars = 0

    for char in line:
        num_chars += 1
        if char >= '0' and char <= '9':
            num_digits += 1

        elif char >= 'a' and char <= 'z':
            num_lower += 1
        
        elif char >= 'A' and char <= 'Z':
            num_upper += 1

        elif char == ' ' or char == '\r' or char == '\n':
            num_spaces += 1

        elif char in PUNCT:
            num_punct += 1

    print("The text contains", num_chars, "characters:")
    print(num_upper, "upper letters")
    print(num_lower, "lower letters")
    print(num_punct, "punctuation marks")
    print(num_spaces, "spaces")
    print(num_digits, "digits")

    exit(0)

if __name__ == "__main__":
    main()    