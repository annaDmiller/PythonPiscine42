from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads two CSV files with the data and displays the projection of
    life expectancy in relation to the gross national product of
    the year 1900 for each country.
    """
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    years = load("life_expectancy_years.csv")
    if data is None or years is None:
        return
    



if __name__ == "__main__":
    main()
