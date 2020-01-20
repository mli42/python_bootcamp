# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_mse.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 17:13:40 by mli               #+#    #+#              #
#    Updated: 2020/01/20 17:56:38 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mean_zip3f(x, y, f):
    res = float(0)
    for nb1, nb2 in zip(x, y):
        res += f(nb1, nb2)
    return (res / len(y))

def linear_mse(x, y, theta):
    shape_x = np.shape(x)
    shape_y = np.shape(y)
    if (shape_x[0] != shape_y[0] or shape_x[1] != np.shape(theta)[0] or
            len(x) == 0 or len(y) == 0):
        return (None)
    f = lambda x, y : (np.dot(theta, x) - y) ** 2
    return (mean_zip3f(x, y, f))


""" Computes the mean squared error of three non-empty numpy.ndarray,
    using a for-loop. The three arrays must have compatible dimensions.

    Args:
     y: has to be an numpy.ndarray, a vector of dimension m * 1.
     x: has to be an numpy.ndarray, a matrix of dimesion m * n.
     theta: has to be an numpy.ndarray, a vector of dimension n * 1.

    Returns:
     The mean squared error as a float.
     None if y, x, or theta are empty numpy.ndarray.
     None if y, x or theta does not share compatibles dimensions.

    Raises:
     This function should not raise any Exception.
"""

"""
X = np.array([[ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]])

Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,0.5,-6])

print(linear_mse(X, Y, Z))

W = np.array([0,0,0])
print(linear_mse(X, Y, W))
"""
