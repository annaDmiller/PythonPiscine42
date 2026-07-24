def callLimit(limit: int):
    """callLimit(limit: int)

    Takes as argument a call limit of another function
    and blocks its execution above the limit."""
    count = 0

    def callLimiter(function):
        """callLimiter(function)

        Takes a function as an argument to run it."""

        def limit_function(*args: any, **kwargs: any):
            """limit_function(*args: any, **kwargs: any)

            Runs the function."""
            nonlocal count
            nonlocal limit

            if (count >= limit):
                print(f"Error: {function} call too many times")
            else:
                function(*args, **kwargs)
                count += 1

            return

        return limit_function

    return callLimiter
