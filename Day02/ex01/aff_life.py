from load_csv import load
from pandas import DataFrame as Dataset
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """
    Loads the CSV file with the data and displays life expectancy
    information of France in the graph.
    """
    data = load("life_expectancy_years.csv")
    if data is None:
        return 

    campus_country = "France"
    if campus_country not in data.index:
        print(f"No data for the specified country: {campus_country}")
        return
    
    country_data = data.loc[campus_country]
    years = country_data.index.astype(int)
    values = country_data.values.astype(float)

    plt.plot(years, values, label=campus_country)
    plt.title(f"{campus_country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(range(years.min(), years.max() + 1, 40))
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()