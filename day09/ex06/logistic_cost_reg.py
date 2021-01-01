# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logistic_cost_reg.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/01 18:17:50 by mli               #+#    #+#              #
#    Updated: 2021/01/01 18:40:02 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from l2_reg import l2

def reg_log_cost_(y: np.ndarray, y_hat: np.ndarray, theta: np.ndarray, lambda_: float) -> float:
    """Computes the regularized cost of a logistic regression model from two non-empty numpy.ndarray, without any for loop. The two arrays must have the same dimensions.
    Args:
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      y_hat: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be a numpy.ndarray, a vector of dimension n * 1.
      lambda_: has to be a float.
    Returns:
      The regularized cost as a float.
      None if y, y_hat, or theta is empty numpy.ndarray.
      None if y and y_hat do not share the same dimensions.
    Raises:
      This function should not raise any Exception.
    """
    if y.shape != y_hat.shape:
        return None
    eps: float = 1e-15
    ones = np.ones(y.shape)
    m = y.shape[0]
    res = np.sum(y * np.log(y_hat + eps) + (ones - y) * np.log(ones - y_hat + eps)) / -m
    res += (lambda_ * l2(theta)) / (2 * m)
    return res


if __name__ == "__main__":
    y = np.array([1, 1, 0, 0, 1, 1, 0]).reshape(-1, 1)
    y_hat = np.array([.9, .79, .12, .04, .89, .93, .01]).reshape(-1, 1)
    theta = np.array([1, 2.5, 1.5, -0.9]).reshape(-1, 1)

    # Example :
    print(reg_log_cost_(y, y_hat, theta, .5))
    # Output: 0.43377043716475955

    # Example :
    print(reg_log_cost_(y, y_hat, theta, .05))
    # Output: 0.13452043716475953

    # Example :
    print(reg_log_cost_(y, y_hat, theta, .9))
    # Output: 0.6997704371647596