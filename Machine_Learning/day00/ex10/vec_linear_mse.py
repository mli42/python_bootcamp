# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_linear_mse.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 17:57:26 by mli               #+#    #+#              #
#    Updated: 2020/01/20 18:05:53 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def vec_linear_mse(x, y, theta):
    shape_x = np.shape(x)
    shape_y = np.shape(y)
    if (shape_x[0] != shape_y[0] or shape_x[1] != np.shape(theta)[0] or
            len(x) == 0 or len(y) == 0 or len(theta) == 0):
        return (None)
    res = np.dot(x, theta) - y
    res = np.dot(np.transpose(res), res)
    return (res / len(x))


""" Computes the mean squared error of three non-empty numpy.ndarray,
    without any for-loop. The three arrays must have compatible dimensions.

    Args:
     y: has to be an numpy.ndarray, a vector of dimension m * 1.
     x: has to be an numpy.ndarray, a matrix of dimesion m * n.
     theta: has to be an numpy.ndarray, a vector of dimension n * 1.

    Returns:
     The mean squared error as a float.
     None if y, x, or theta are empty numpy.ndarray.
     None if y, x or theta does not share compatibles dimensions.
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
print(vec_linear_mse(X, Y, Z))

W = np.array([0,0,0])
print(vec_linear_mse(X, Y, W))
"""
