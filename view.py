import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def display_chart(data, weights):
    returns = data.pct_change()
    returns['Portfolio'] = returns.dot(weights)

    # Calculate cumulative returns
    daily_cum_ret = (1 + returns).cumprod()

    # Plot the portfolio cumulative returns only
    fig, ax = plt.subplots()
    ax.plot(daily_cum_ret.index, daily_cum_ret["Portfolio"], color='purple', label="portfolio")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    plt.legend()
    plt.show()

def to_print(info):
    return print(info)
