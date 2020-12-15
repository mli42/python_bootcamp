# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    other_costs.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/14 22:59:47 by mli               #+#    #+#              #
#    Updated: 2020/12/15 10:28:49 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# MSE, RMSE, MAE, R2score
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
from vec_cost import cost_

def mse_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculate the MSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
    Returns:
        mse: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    costs = cost_(y, y_hat)
    if costs is None:
        return None
    return costs * 2

def rmse_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculate the RMSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
    Returns:
        rmse: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    cmse = mse_(y, y_hat)
    if cmse is None:
        return None
    return cmse ** 0.5

def mae_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculate the MAE between the predicted output and the real output.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
    Returns:
        mae: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    if y.shape != y_hat.shape:
        return None
    elem = abs(y_hat - y) / y.shape[0]
    return np.sum(elem)

def r2score_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculate the R2score between the predicted output and the output.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
    Returns:
        r2score: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    if y.shape != y_hat.shape:
        return None
    means = (np.sum(y) / y.shape[0])
    dividend = np.sum((y_hat - y) ** 2)
    divisor = np.sum((y - means) ** 2)
    res = 1 - (dividend / divisor)
    return res

if __name__ == "__main__":
    # Example 1:
    x = np.array([0, 15, -9, 7, 12, 3, -21])
    y = np.array([2, 14, -13, 5, 12, 4, -19])

    x = x.reshape(len(x), 1)
    y = y.reshape(len(y), 1)

    tests = dict.fromkeys(["mse", "rmse", "mae", "r2score"])
    for ele in tests:
        tests[ele] = list()

    # Mean squared error
    tests["mse"].append([mse_(x,y), mean_squared_error(x,y)])
    #4.285714285714286

    # Root mean squared error
    ## sklearn implementation not available: take the square root of MSE
    tests["rmse"].append([rmse_(x,y), sqrt(mean_squared_error(x,y))])
    #2.0701966780270626

    # Mean absolute error
    tests["mae"].append([mae_(x,y), mean_absolute_error(x,y)])
    #1.7142857142857142

    # R2-score
    tests["r2score"].append([r2score_(x,y), r2_score(x,y)])
    #0.9681721733858745

    for i, ele in enumerate(tests.items()):
        fct = ele[0]
        if len(ele[1]) == 0:
            continue
        res = ele[1][0]
        if res[0] is None:
            res[0] = 42
        color = "✅" if (res[0] == res[1]) else "🚨"
        print("[%d][%-7s] %s - %f. Expected: %f" %(i, fct, color, res[0], res[1]))
