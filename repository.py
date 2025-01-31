import pandas as pd
import yfinance as yf


def get_data():
    return pd.read_csv(
        r"input\small_portfolio.csv",
        delimiter=",",
        index_col="date",
        parse_dates=["date"],
    )


def get_weight():
    """"""
    portfolio = {"GE": 0.5, "JPM": 0.2, "MSFT": 0.2, "PG": 0.1}
    return portfolio

"""def get_data():
    return pd.read_csv(
        r"input\small_portfolio.csv",
        delimiter=",",
        index_col="date",
        parse_dates=["date"],
    )"""