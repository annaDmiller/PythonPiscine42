from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads two CSV files with the data and displays the projection of
    life expectancy in relation to the gross national product of
    the year 1900 for each country.
    """
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expect = load("life_expectancy_years.csv")
    if income is None or life_expect is None:
        return

    year_income = income["1900"].astype(int)
    year_life = life_expect["1900"].astype(float)

    plt.scatter(year_income, year_life, label="1900")
    plt.title("1900")

    plt.xlabel("Gross domestic product")
    plt.xscale("log")
    xticks = [300, 1000, 10000]
    xlabels = ["300", "1k", "10k"]
    plt.xticks(xticks, xlabels)

    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
