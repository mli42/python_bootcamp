# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 18:35:43 by mli               #+#    #+#              #
#    Updated: 2020/12/19 21:17:47 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from prediction import add_intercept

def gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Computes a gradient vector from three non-empty numpy.ndarray, without any for loop.
        The three arrays must have compatible dimensions.
    Args:
        x: has to be a numpy.ndarray, a matrix of dimension m * 1.
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        theta: has to be a numpy.ndarray, a 2 * 1 vector.
    Returns:
        The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
        None if x, y, or theta is an empty numpy.ndarray.
        None if x, y and theta do not have compatible dimensions.
    Raises:
        This function should not raise any Exception.
    """
    m = x.shape[0]
    x = add_intercept(x)
    nabla_j = x.T.dot(x.dot(theta) - y) / m
    return nabla_j

if __name__ == "__main__":
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])

    x = x.reshape(len(x), 1)
    y = y.reshape(len(y), 1)

    # Example 0:
    theta1 = np.array([2, 0.7]).reshape(2, 1)
    print(gradient(x, y, theta1))
    # Output: array([21.0342574, 587.36875564])

    # Example 1:
    theta2 = np.array([1, -0.4]).reshape(2, 1)
    print(gradient(x, y, theta2))
    # Output: array([58.86823748, 2229.72297889])
