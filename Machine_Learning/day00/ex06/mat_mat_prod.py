# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mat_mat_prod.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 15:12:21 by mli               #+#    #+#              #
#    Updated: 2020/01/20 16:06:27 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mat_mat_prod(x, y):
    shape_x = np.shape(x)
    shape_y = np.shape(y)
    if (shape_x[1] != shape_y[0] or len(x) == 0 or len(y) == 0):
        return (None)
    res = []
    for j in range(shape_y[1]):
        res.append([])
        for k in range(shape_x[0]):
            nb = 0
            for l in range(shape_x[1]):
                nb += x[k][l] * y[l][j]
            res[j].append(nb)
    return (np.transpose(np.asarray(res).reshape((shape_x[0], shape_y[1]))))

    """Computes the product of two non-empty numpy.ndarray, using a
for-loop. The two arrays must have compatible dimensions.
    Args:
     x: has to be an numpy.ndarray, a matrix of dimension m * n.
     y: has to be an numpy.ndarray, a vector of dimension n * p.
    Returns:
     The product of the matrices as a matrix of dimension m * p.
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

Z = np.array([[ -6, -1, -8, 7, -8],
    [ 7, 4, 0, -10, -10],
    [ 7, -13, 2, 2, -11],
    [ 3, 14, 7, 7, -4],
    [ -1, -3, -8, -4, -14],
    [ 9, -14, 9, 12, -7],
    [ -9, -4, -10, -3, 6]])

print(mat_mat_prod(W, Z))
print(mat_mat_prod(Z, W))
'''
