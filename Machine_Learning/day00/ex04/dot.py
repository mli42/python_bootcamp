# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dot.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 13:35:45 by mli               #+#    #+#              #
#    Updated: 2020/01/20 14:12:06 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def sum_no_f(x):
    if (len(x) == 0):
        return (None)
    res = float(0)
    for nb in x:
        res += nb
    return (res)

def dot(x, y):
    if (np.shape(x) != np.shape(y) or len(x) == 0 or len(y) == 0):
        return (None)
    return (sum_no_f(x * y))


""" Computes the dot product of two non-empty numpy.ndarray, using a
    for-loop. The two arrays must have the same dimensions.

    Args:
     x: has to be an numpy.ndarray, a vector.
     y: has to be an numpy.ndarray, a vector.

    Returns:
     The dot product of the two vectors as a float.
     None if x or y are empty numpy.ndarray.
     None if x and y does not share the same dimensions.

    Raises:
     This function should not raise any Exception.
"""

'''
X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

print(dot(X, Y))
print(dot(X, X))
print(dot(Y, Y))
'''
