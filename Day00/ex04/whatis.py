import sys as sys

num_args = len(sys.argv)

if num_args > 2:
    print("AssertionError: more than one argument is provided")

elif num_args == 2:
    try:
        value = int(sys.argv[1])

        if value % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as err:
        print(err)
