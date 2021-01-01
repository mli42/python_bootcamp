# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_cost_reg.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/01 18:17:50 by mli               #+#    #+#              #
#    Updated: 2021/01/01 18:27:25 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from l2_reg import l2


def reg_cost_(y: np.ndarray, y_hat: np.ndarray, theta: np.ndarray, lambda_: float) -> float:
    """Computes the regularized cost of a linear regression model from two non-empty numpy.ndarray, without any for loop.
        The two arrays must have the same dimensions.
    Args:
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      y_hat: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be a numpy.ndarray, a vector of dimension n * 1.
      lambda_: has to be a float.
    Returns:
      The regularized cost as a float.
      None if y, y_hat, or theta are empty numpy.ndarray.
      None if y and y_hat do not share the same dimensions.
    Raises:
      This function should not raise any Exception.
    """
    if y.shape != y_hat.shape:
        return None
    j_elem = np.sum((y_hat - y) ** 2) + lambda_ * l2(theta)
    res =  j_elem / (2 * y.shape[0])
    return res


if __name__ == "__main__":
    y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)
    y_hat = np.array([3, 13, -11.5, 5, 11, 5, -20]).reshape(-1, 1)
    theta = np.array([1, 2.5, 1.5, -0.9]).reshape(-1, 1)

    # Example :
    print(reg_cost_(y, y_hat, theta, .5))
    # Output: 0.8503571428571429

    # Example :
    print(reg_cost_(y, y_hat, theta, .05))
    # Output: 0.5511071428571429

    # Example :
    print(reg_cost_(y, y_hat, theta, .9))
    # Output: 1.116357142857143
