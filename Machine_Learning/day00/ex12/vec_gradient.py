# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_gradient.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 19:07:02 by mli               #+#    #+#              #
#    Updated: 2020/01/20 19:14:20 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def vec_linear_mse(x, y, theta):
    res = np.dot(x, theta) - y
    res = np.dot(np.transpose(res), res)
    return (res / len(x))

def vec_gradient(x, y, theta):
    shape_x = np.shape(x)
    shape_y = np.shape(y)
    if (shape_x[0] != shape_y[0] or shape_x[1] != np.shape(theta)[0] or
            len(x) == 0 or len(y) == 0 or len(theta) == 0):
        return (None)
    res = np.dot(x, theta) - y
    res = np.dot(np.transpose(x), res) / len(x)
    return (res)

""" Computes a gradient vector from three non-empty numpy.ndarray,
    without any for-loop. The three arrays must have the compatible dimensions.

    Args:
     x: has to be an numpy.ndarray, a matrice of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension m * 1.
     theta: has to be an numpy.ndarray, a vector n * 1.

    Returns:
     The gradient as a numpy.ndarray, a vector of dimensions n * 1, containg
the result of the formula for all j.
     None if x, y, or theta are empty numpy.ndarray.
     None if x, y and theta do not have compatible dimensions.

    Raises:
     This function should not raise any Exception.
"""

'''
X = np.array([[ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]])

Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,0.5,-6])
print(vec_gradient(X, Y, Z))

W = np.array([0,0,0])
print(vec_gradient(X, Y, W))

print(vec_gradient(X, X.dot(Z), Z))
'''
