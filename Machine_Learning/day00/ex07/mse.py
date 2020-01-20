# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mse.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 16:09:28 by mli               #+#    #+#              #
#    Updated: 2020/01/20 16:36:05 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mean_zipf(x, y, f):
    res = float(0)
    for nb1, nb2 in zip(x, y):
        res += f(nb1, nb2)
    return (res / len(x))

def mse(y, y_hat):
    shape_y = np.shape(y)
    shape_y_hat = np.shape(y_hat)
    if (shape_y != shape_y_hat or len(y) == 0 or len(y_hat) == 0):
        return (None)
    f = lambda x, y : (y - x) ** 2
    return (mean_zipf(y, y_hat, f))


""" Computes the mean squared error of two non-empty numpy.ndarray, using
    a for-loop. The two arrays must have the same dimensions.

    Args:
     y: has to be an numpy.ndarray, a vector.
     y_hat: has to be an numpy.ndarray, a vector.

    Returns:
     The mean squared error of the two vectors as a float.
     None if y or y_hat are empty numpy.ndarray.
     None if y and y_hat does not share the same dimensions.

    Raises:
     This function should not raise any Exception.
"""


'''
X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

print(mse(X, Y))
print(mse(X, X))
'''
