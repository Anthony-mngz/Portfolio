import pandas as pd
import yfinance as yf


portfolio = {"GE": 0.5, "JPM": 0.2, "MSFT": 0.2, "PG": 0.1}
field_to_keep = "Close"
begin_date = "2015-01-02"
end_date = "2018-03-27"

def get_data():
    tickers = list(portfolio.keys())
    data = yf.download(tickers, start=begin_date, end=end_date)
    return data[field_to_keep]


def get_weight()-> np.array:
    """"""
    return np.array(list(portfolio.value())

"""def get_data():
    return pd.read_csv(
        r"input\small_portfolio.csv",
        delimiter=",",
        index_col="date",
        parse_dates=["date"],
    )"""
