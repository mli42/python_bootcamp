# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mat_vec_prod.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 14:13:53 by mli               #+#    #+#              #
#    Updated: 2020/01/20 14:59:18 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mat_vec_prod(x, y):
    shape_x = np.shape(x)
    shape_y = np.shape(y)
    if (shape_x[1] != shape_y[0] or len(x) == 0 or len(y) == 0):
        return (None)
    res = []
    for k in range(shape_x[0]):
        nb = 0
        for l in range(shape_x[1]):
            nb += x[k][l] * y[l][0]
        res.append(nb)
    return (np.asarray(res).reshape((shape_x[0], shape_y[1])))

    """ Computes the product of two non-empty numpy.ndarray, using a
        for-loop. The two arrays must have compatible dimensions.

    Args:
     x: has to be an numpy.ndarray, a matrix of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension n * 1.

    Returns:
     The product of the matrix and the vector as a vector of dimension m * 1.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share compatibles dimensions.

    Raises:
     This function should not raise any Exception.
    """

'''
W = np.array([[ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])

X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))

print(mat_vec_prod(W, X))
print(mat_vec_prod(W, Y))
'''
