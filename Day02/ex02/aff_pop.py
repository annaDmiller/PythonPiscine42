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
    Loads the CSV file with the data and displays life expectancy
    information of France in the graph.
    """
    data = load("population_total.csv")
    if data is None:
        return
    
    countries = ["France", "Russia"]
    if not all(countries[ind] in data.index for ind in range(len(countries))):
        print(f"No data for any of the specified countries: {campus_country} or {country}")
        return

    max_val = 0
    for country in countries:
        info = data.loc[country]
        info = info[(info.index.astype(int) <= 2050)]
        years = info.index.astype(int)
        values = [to_number(val) for val in info.values]
        if max(values) > max_val : max_val = int(max(values))
        plt.plot(years, values, label=country)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xticks(range(years.min(), years.max(), 40))

    plt.ylabel("Population")
    step = 20_000_000
    y_ticks = range(0, max_val + step, step)
    y_labels = [f"{int(t/1_000_000)}M" for t in y_ticks]
    plt.yticks(y_ticks[1:-1], y_labels[1:-1])

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
