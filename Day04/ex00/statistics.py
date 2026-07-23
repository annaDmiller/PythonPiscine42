def print_error() -> None:
    """print_error() -> None

    Prints an error message into the standard output."""
    print("ERROR")
    return


def mean_of_list(lst: list[int | float]) -> int | float:
    """mean_of_list(lst: list[int | float]) -> int | float

    Calculates the mean of the list of numbers and
    returns it."""
    return sum(num for num in lst) / len(lst)


def median_of_list(lst: list([int | float])) -> [int | float]:
    """median_of_list(lst: list([int | float])) -> [int | float]

    Calculates the median value of the list of numbers and
    returns it."""
    size_list = len(lst)
    if size_list % 2 == 0:
        return (lst[size_list // 2 - 1]
                + lst[size_list // 2]) / 2
    else:
        return lst[size_list // 2]


def var_of_list(lst: list([int | float])) -> [int | float]:
    """var_of_list(lst: list([int | float])) -> [int | float]

    Calculates the variance of the list of numbers and
    returns it."""
    mean = mean_of_list(lst)
    lst_temp = [(num - mean) ** 2 for num in lst]
    return mean_of_list(lst_temp)


def calculate_mean(lst: list([int | float])) -> None:
    """calculate_mean(lst: list([int | float])) -> None

    Calculates the mean of list of numbers and prints the result.
    If the list is None or empty, prints an error."""
    if lst is None or len(lst) == 0:
        return print_error()

    mean = mean_of_list(lst)
    print(f"mean : {mean}")
    return


def calculate_median(lst: list([int | float])) -> None:
    """calculate_median(lst: list([int | float])) -> None

    Calculates the median of list of numbers and prints the result.
    If the list is None or empty, prints an error."""
    if lst is None or len(lst) == 0:
        return print_error()

    median = median_of_list(lst)
    print(f"median : {median}")
    return


def calculate_quartile(lst: list([int | float])) -> None:
    """calculate_quartile(lst: list([int | float])) -> None

    Calculates the quartiles (25% and 75%) of list of
    numbers and prints the result. If the list is None or
    empty, prints an error."""
    if lst is None or len(lst) == 0:
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

    Calculates the standard deviation of list of
    numbers and prints the result. If the list is None
    or empty, prints an error."""
    if lst is None or len(lst) == 0:
        return print_error()

    std = var_of_list(lst) ** 0.5
    print(f"std : {std}")
    return


def calculate_var(lst: list([int | float])) -> None:
    """calculate_var(lst: list([int | float])) -> None

    Calculates the variance of list of numbers and
    prints the result. If the list is None or empty,
    prints an error."""
    if lst is None or len(lst) == 0:
        return print_error()

    var = var_of_list(lst)
    print(f"var : {var}")
    return


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

    actions = {
        "mean": calculate_mean,
        "median": calculate_median,
        "quartile": calculate_quartile,
        "std": calculate_std,
        "var": calculate_var,
    }

    list_args = list(args)
    list_args.sort()
    for action in kwargs.values():
        func = actions.get(action.lower())
        if func:
            func(list_args)

    return
