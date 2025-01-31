import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from repository import get_data, get_weight
from model import portfolio_return, portfolio_standard_dev, portfolio_variance, portfolio_cumulative_returns
from view import to_print, display_chart


def main():
    # https://campus.datacamp.com/courses/introduction-to-portfolio-analysis-in-python/introduction-to-portfolio-analysis?ex=6
    data = get_data()

    # Define weights for the portfolio
    weights = get_weight()

    # Calculate expected portfolio performance
    port_return = portfolio_return(weights, data)

    # Print the portfolio return
    to_print(port_return)
    to_print(portfolio_cumulative_returns(data, weights))

    display_chart(data, weights)

    # Calculate the portfolio variance
    port_variance = portfolio_variance(weights, data)

    # Print the result
    to_print(str(np.round(port_variance, 4) * 100) + '%')

    # https: // campus.datacamp.com / courses / introduction - to - portfolio - analysis - in -python / introduction - to - portfolio - analysis?ex = 10
    # Calculate the standard deviation by taking the square root
    port_standard_dev = portfolio_standard_dev(weights, data)

    # Print the results
    to_print(str(np.round(port_standard_dev, 4) * 100) + '%')


if __name__ == '__main__':
    main()
