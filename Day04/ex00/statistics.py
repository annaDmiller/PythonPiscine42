def print_error() -> None:
    """print_error() -> None

    Prints an error message into the standard output."""
    print("ERROR")
    return


def calculate_mean(lst: list([int | float])) -> None:
    """calculate_mean(lst: list([int | float])) -> None

    Calculates the mean of *args values and prints the result.
    If there are no arguments passed, prints an error."""
    if lst == None or len(lst) == 0:
        return print_error()

    mean = sum(num for num in lst) / len(lst)
    print(f"mean : {mean}")
    return


def median_of_list(lst: list([int | float])) -> [int | float]:
    """median_of_list(lst: list([int | float])) -> [int | float]

    Calculates the median value of the list of numbers.
    """
    size_list = len(lst)
    if size_list % 2 == 0:
        return (lst[size_list // 2 - 1]
                       + lst[size_list // 2]) / 2
    else:
        return lst[size_list // 2]


def calculate_median(lst: list([int | float])) -> None:
    """calculate_median(lst: list([int | float])) -> None

    Calculates the meridian of *args values and prints the result.
    If there are no arguments passed, prints an error."""
    if lst == None or len(lst) == 0:
        return print_error()

    median = median_of_list(lst)
    print(f"median : {median}")
    return


def calculate_quartile(lst: list([int | float])) -> None:
    """calculate_quartile(lst: list([int | float])) -> None
    
    Calculates the quartiles (25% and 75%) of *args values
    and prints the result. If there are no arguments passed,
    prints an error."""
    if lst == None or len(lst) == 0:
        return print_error()

    middle_ind = len(lst) // 2
    higher_list = lst[middle_ind:]
    if (len(lst) % 2 == 0):
        lower_list = lst[:middle_ind]
    else:
        lower_list = lst[:middle_ind + 1]

    low_quartile = float(median_of_list(lower_list))
    high_quartile = float(median_of_list(higher_list))
    print(f"quartile : [{low_quartile}, {high_quartile}]")
    return


def calculate_std(lst: list([int | float])) -> None:
    """calculate_std(*args: [int | float]) -> None
    
    Calculates the standard deviation of *args values
    and prints the result. If there are no arguments passed,
    prints an error."""
    if lst == None or len(lst) == 0:
        return print_error()

    mean = sum(num for num in lst) / len(lst)


def calculate_var(lst: list([int | float])) -> None:
    """calculate_var(lst: list([int | float])) -> None
    
    Calculates the variance of *args values and prints the
    result. If there are no arguments passed, prints an
    error."""

    if lst == None or len(lst) == 0:
        return print_error()


def ft_statistics(*args: any, **kwargs: any) -> None:
    """ft_statistics(*args: Any, **kwargs: Any) -> None

    Takes any amount of numbers (*args parameter) and makes
    the Mean, Median, Quartiles, Standard Deviation and 
    Variance according to the request (**kwargs ask). Prints
    the result into the standard output."""
    if len(args) != 0 and not all(type(arg) in (int, float)
                                  for arg in args):
        return print_error()

    if len(kwargs) == 0:
        return

    list_args = list(args)
    list_args.sort()
    for key, action in kwargs.items():
        action = action.lower()
        match action:
            case "mean":
                calculate_mean(list_args)

            case "median":
                calculate_median(list_args)

            case "quartile":
                calculate_quartile(list_args)

            case "std":
                calculate_std(list_args)

            case "var":
                calculate_var(list_args)

            case _:
                continue
    
    return
