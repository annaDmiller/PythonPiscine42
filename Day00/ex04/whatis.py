import sys as sys

args = sys.argv[1:]
num_args = len(args)

if num_args > 1:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)

if num_args == 0:
    print("")
    sys.exit(0)

i = 0
while i < len(args[0]):
    char = args[0][i]
    if char < '0' or char > '9':
        if char == '-' and i == 0:
            i += 1
            continue
        print("AssertionError: argument is not an integer")
        sys.exit(1)

    i += 1

number = int(args[0])
if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
