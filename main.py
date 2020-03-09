import pandas as pd
import matplotlib.pyplot as plt

def main():
    filename = "time_series_19-covid-Confirmed.csv"
    df = pd.read_csv("../COVID-19/csse_covid_19_data/csse_covid_19_time_series/" + filename)
    df = df.loc[df["Country/Region"] == "Ireland"]
    print(df.head())
    df.plot()
    plt.show()

if __name__ == "__main__":
    main()
