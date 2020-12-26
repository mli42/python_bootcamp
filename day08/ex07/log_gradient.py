# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    log_gradient.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/26 17:12:49 by mli               #+#    #+#              #
#    Updated: 2020/12/26 17:59:51 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from log_pred import logistic_predict_


def log_gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Computes a gradient vector from three non-empty numpy.ndarray, with a for-loop.
        The three arrays must have compatible dimensions.
    Args:
      x: has to be an numpy.ndarray, a matrix of dimension m * n.
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be an numpy.ndarray, a vector (n + 1) * 1.
    Returns:
      The gradient as a numpy.ndarray, a vector of dimensions (n + 1) * 1, containing
        the result of the formula for all j.
      None if x, y, or theta are empty numpy.ndarray.
      None if x, y and theta do not have compatible dimensions.
    Raises:
      This function should not raise any Exception.
    """
    if (0 in [x.size, y.size, theta.size] or x.shape[0] != y.shape[0] or
        (x.shape[1] + 1) != theta.shape[0]):
        return None
    res = np.zeros(shape=(theta.shape))
    m, n = x.shape
    y_hat = logistic_predict_(x, theta)
    for i in range(m):
        res[0][0] += (y_hat[i][0] - y[i][0])
        for j in range(n):
            res[j + 1][0] += (y_hat[i][0] - y[i][0]) * (x[i][j])
    res = res / m
    return res


if __name__ == "__main__":
    # Example 1:
    y1 = np.array([1]).reshape(1, 1)
    x1 = np.array([4]).reshape(1, 1)
    theta1 = np.array([[2], [0.5]])

    print(log_gradient(x1, y1, theta1))
    # Output:
    """
    array([[-0.01798621],
           [-0.07194484]])
    """

    # Example 2:
    y2 = np.array([[1], [0], [1], [0], [1]])
    x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
    theta2 = np.array([[2], [0.5]])

    print(log_gradient(x2, y2, theta2))
    # Output:
    """
    array([[0.3715235 ],
           [3.25647547]])
    """

    # Example 3:
    y3 = np.array([[0], [1], [1]])
    x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
    theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])

    print(log_gradient(x3, y3, theta3))
    # Output:
    """
    array([[-0.55711039],
           [-0.90334809],
           [-2.01756886],
           [-2.10071291],
           [-3.27257351]])
    """
