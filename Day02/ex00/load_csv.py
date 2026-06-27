import pandas as pd
from pandas import DataFrame as Dataset


def load(path: str) -> Dataset:
    """
    load(path: str) -> Dataset

    Takes a path to the file where the data stores,
    writes the dimensions of the DataFrame and returns it.
    If the path is bad or any other errors occur, it returns
    None.
    """
    try:
        table = pd.read_csv(path, index_col=0, header=0)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except PermissionError:
        print(f"No access to read the file: {path}")
        return None
    except IsADirectoryError:
        print(f"This is a directory: {path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"The file {path} is empty. Can't process it.")
        return None
    except OSError:
        print("OS error occured. Try once more later.")
        return None
    except Exception:
        print("Unknown eror has occurred. Try once more later.")
        return None

    print(f"Loading dataset of dimensions {table.shape}")

    return (table)
