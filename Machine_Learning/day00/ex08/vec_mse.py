# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_mse.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 16:41:53 by mli               #+#    #+#              #
#    Updated: 2020/01/20 17:03:53 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def vec_mse(y, y_hat):
    if (np.shape(y) != np.shape(y_hat) or len(y) == 0 or len(y_hat) == 0):
        return (None)
    return (np.dot(y_hat - y, y_hat - y) / len(y))

""" Computes the mean squared error of two non-empty numpy.ndarray,
    without any for loop. The two arrays must have the same dimensions.

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

"""
X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(vec_mse(X, Y))
print(vec_mse(X, X))
"""
