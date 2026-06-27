from load_csv import load
import matplotlib.pyplot as plt


def to_number(val: str) -> int:
    """
    to_number(val: str) -> int

    Converts a short human-readable form of the number into int.
    Returns an integer value of the number.
    Example of usage: 3.28M => 3280000 or 400k => 400000.
    """
    filtered = str(val).strip().lower()

    if filtered.endswith("k"):
        return float(filtered[:-1]) * 1_000
    if filtered.endswith("m"):
        return float(filtered[:-1]) * 1_000_000
    if filtered.endswith("b"):
        return float(filtered[:-1]) * 1_000_000_000

    return float(filtered)


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

    year = "1900"
    if year not in income.columns or year not in life_expect.columns:
        print(f"No data for this year: {year}")
        return

    year_income = [to_number(val) for val in income[year]]
    year_life = life_expect[year].astype(float)

    plt.scatter(year_income, year_life, label=f"{year}")
    plt.title(f"{year}")

    plt.xlabel("Gross domestic product")
    plt.xscale("log")
    xticks = [300, 1000, 10000]
    xlabels = ["300", "1k", "10k"]
    plt.xticks(xticks, xlabels)

    plt.ylabel("Life expectancy")
    
    plt.show()
    return 


if __name__ == "__main__":
    main()
