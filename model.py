import numpy as np


def portfolio_return(weights, data):
    """
     Calculate expected portfolio performance

     args : weights (array[float]), poids des positions
            data (Dataframe), contient les données journalières des titres

     return : retourne la performance du portefeuille
     """
    returns = data.pct_change()
    mean_daily_returns = returns.mean()
    return np.sum(mean_daily_returns * weights)


def portfolio_variance(weights, data):
    """
    Calculate the portfolio variance

    args : weights (array[float]), poids des positions
            data (Dataframe), contient les données journalières des titres

    return : retourne la variance du portefeuille
    """
    returns = data.pct_change()
    cov_matrix = (returns.cov()) * 250
    return np.dot(weights.T, np.dot(cov_matrix, weights))


def portfolio_standard_dev(weights, data):
    """
    Calculate the standard deviation by taking the square root

     args : weights (array[float]), poids des positions
            data (Dataframe), contient les données journalières des titres

     return : retourne l'écart type' du portefeuille
     """
    returns = data.pct_change()
    cov_matrix = (returns.cov()) * 250
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))


def portfolio_cumulative_returns(returns):
    daily_cum_ret = (1 + returns).cumprod()
    return daily_cum_ret