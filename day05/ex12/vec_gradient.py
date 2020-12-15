# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_gradient.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/15 10:32:22 by mli               #+#    #+#              #
#    Updated: 2020/12/15 11:43:45 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from tools import add_intercept

def vec_gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Computes a gradient vector from three non-empty numpy.ndarray,
        without any for-loop. The three arrays must have the compatible dimensions.
    Args:
      x: has to be an numpy.ndarray, a matrice of dimension (m, n).
      y: has to be an numpy.ndarray, a vector of dimension (m, 1).
      theta: has to be an numpy.ndarray, a vector of dimension (n, 1).
    Returns:
      The gradient as a numpy.ndarray, a vector of dimensions (n, 1), containing
        the result of the formula for all j.
      None if x, y, or theta are empty numpy.ndarray.
      None if x, y and theta do not have compatible dimensions.
    Raises:
      This function should not raise any Exception.
    """
    if (0 in [len(x), len(y), len(theta)] or y.shape[1] != theta.shape[1] or
            x.shape[0] != y.shape[0] or x.shape[1] != theta.shape[0]):
        return None
    res = (x.T / len(y)).dot(x.dot(theta) - y)
    return res

if __name__ == "__main__":
    X = np.array([
            [-6,  -7,  -9],
            [13,  -2,  14],
            [-7,  14,  -1],
            [-8,  -4,   6],
            [-5,  -9,   6],
            [ 1,  -5,  11],
            [ 9, -11,   8]])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])
    Y = Y.reshape(len(Y), 1)

    theta = np.array([3, 0.5, -6])
    theta = theta.reshape(len(theta), 1)

    print(vec_gradient(X, Y, theta))
    # array([ -37.35714286, 183.14285714, -393.])

    theta = np.array([0, 0, 0])
    theta = theta.reshape(len(theta), 1)

    print(vec_gradient(X, Y, theta))
    # array([  0.85714286, 23.28571429, -26.42857143])

    theta1 = np.array([0, 0, 0, 0])
    theta1 = theta1.reshape(len(theta1), 1)

    print(vec_gradient(X, add_intercept(X).dot(theta1), theta))
    # array([0., 0., 0.])
