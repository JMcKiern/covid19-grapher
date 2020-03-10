import pandas as pd
import matplotlib.pyplot as plt


def plot(df: pd.DataFrame, ax: plt.axes, country_name: str, x: str="Date", y: str="Confirmed Cases"):
    df = df.loc[df["Country/Region"] == country_name]
    df.plot(x=x, y=y, label=country_name, ax=ax)

def add_days_since_first_case(df: pd.DataFrame, number_of_cases: int):
    df_wc = df.loc[df["Confirmed Cases"] > number_of_cases]
    df_wc = df_wc.groupby("Country/Region", as_index=False)["Date"].min()
    df = df.merge(df_wc[["Date", "Country/Region"]], on="Country/Region")
    df = df.rename(columns={"Date_x": "Date", "Date_y": "Date of case " + str(number_of_cases)})
    df["Days since case " + str(number_of_cases)] = (df["Date"] - df["Date of case " + str(number_of_cases)]).dt.days
    return df

def get_clean_df(filename: str, number_of_cases: int):
    df = pd.read_csv("../COVID-19/csse_covid_19_data/csse_covid_19_time_series/" + filename)
    df = df.melt(var_name="Date", value_name="Confirmed Cases", id_vars=["Province/State", "Country/Region", "Lat", "Long"])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.groupby(["Date", "Country/Region"], as_index=False).sum()
    df = add_days_since_first_case(df, number_of_cases)
    # TODO: Add % change
    return df

def main():
    filename = "time_series_19-covid-Confirmed.csv"
    number_of_cases = 10
    df = get_clean_df(filename, number_of_cases)
    fig, ax = plt.subplots()
    x = "Days since case " + str(number_of_cases)
    plot(df, ax, "Australia", x=x)
    plot(df, ax, "New Zealand", x=x)
    # plot(df, ax, "Italy", x=x)
    plot(df, ax, "France", x=x)
    # plot(df, ax, "Mainland China", x=x)
    plot(df, ax, "Ireland", x=x)
    plot(df, ax, "UK", x=x)
    # plot(df, ax, "South Korea", x=x)
    plot(df, ax, "Japan", x=x)
    # plot(df, ax, "United States", x=x)
    # plot(df, ax, "Cambodia", x=x)
    # plot(df, ax, "Thailand", x=x)
    # plot(df, ax, "India", x=x)
    plot(df, ax, "Taiwan", x=x)
    plot(df, ax, "Singapore", x=x)
    ax.set_xlim(left=0)

    plt.show()

if __name__ == "__main__":
    main()
