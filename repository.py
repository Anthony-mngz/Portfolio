import pandas as pd
import numpy as np


def get_data():
    return pd.read_csv(
        r"input\small_portfolio.csv",
        delimiter=",",
        index_col="date",
        parse_dates=["date"],
    )


def get_weight():
    """"""
    return np.array([0.05, 0.4, 0.3, 0.25])
