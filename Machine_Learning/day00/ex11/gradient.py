# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 18:09:50 by mli               #+#    #+#              #
#    Updated: 2020/01/20 19:06:13 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mean_zip3fact(x, y, f):
    res = []
    for n in range(np.shape(x)[1]):
        nb = 0
        for nb1, nb2, m in zip(x, y, range(np.shape(x)[0])):
            nb += f(nb1, nb2, x[m][n])
        res.append(nb)
    return (np.asarray(res) / len(x))

def gradient(x, y, theta):
    shape_x = np.shape(x)
    shape_y = np.shape(y)
    if (shape_x[0] != shape_y[0] or shape_x[1] != np.shape(theta)[0] or
            len(x) == 0 or len(y) == 0 or len(theta) == 0):
        return (None)
    f = lambda x, y, z: (np.dot(theta, x) - y) * z
    return (mean_zip3fact(x, y, f))


""" Computes a gradient vector from three non-empty numpy.ndarray, using
    a for-loop. The two arrays must have the compatible dimensions.

    Args:
     x: has to be an numpy.ndarray, a matrice of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension m * 1.
     theta: has to be an numpy.ndarray, a vector n * 1.

    Returns:
     The gradient as a numpy.ndarray, a vector of dimensions n * 1.
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

print(gradient(X, Y, Z))

W = np.array([0,0,0])
print(gradient(X, Y, W))
print(gradient(X, X.dot(Z), Z))
'''
