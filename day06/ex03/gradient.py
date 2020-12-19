# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/16 22:28:08 by mli               #+#    #+#              #
#    Updated: 2020/12/16 22:47:42 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from prediction import predict_

def simple_gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Computes a gradient vector from three non-empty numpy.ndarray.
        The three arrays must have compatible dimensions.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * 1.
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be an numpy.ndarray, a 2 * 1 vector.
    Returns:
      The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
      None if x, y, or theta are empty numpy.ndarray.
      None if x, y and theta do not have compatible dimensions.
    Raises:
      This function should not raise any Exception.
    """
    if (0 in [len(x), len(y), len(theta)] or x.shape != y.shape or
            (x.shape[1] + 1) != theta.shape[0]):
        return None
    res = np.zeros(shape=(theta.shape))
    m = x.shape[0]
    y_hat = predict_(x, theta)
    for i in range(m):
        res[0][0] += (y_hat[i][0] - y[i][0])
        res[1][0] += (y_hat[i][0] - y[i][0]) * (x[i][0])
    res = res / m
    return res

if __name__ == "__main__":
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
    x = x.reshape(len(x), 1)
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])
    y = y.reshape(len(y), 1)

    # Example 0:
    theta1 = np.array([2, 0.7]).reshape(2, 1)
    print(simple_gradient(x, y, theta1))
    # Output: array([21.0342574, 587.36875564])

    # Example 1:
    theta2 = np.array([1, -0.4]).reshape(2, 1)
    print(simple_gradient(x, y, theta2))
    # Output: array([58.86823748, 2229.72297889])
