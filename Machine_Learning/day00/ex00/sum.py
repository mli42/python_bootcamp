# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sum.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 10:56:44 by mli               #+#    #+#              #
#    Updated: 2020/01/20 11:37:22 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def sum_(x, f):
    if (len(x) == 0 or isinstance(f(1), (int, float)) == False):
        return (None)
    res = float(0)
    for nb in x:
        res += f(nb)
    return (res)

""" Computes the sum of a non-empty numpy.ndarray onto wich a function is
    applied element-wise, using a for-loop.

    Args:
     x: has to be an numpy.ndarray, a vector.
     f: has to be a function, a function to apply element-wise to the vector.

    Returns:
     The sum as a float.
     None if x is an empty numpy.ndarray or if f is not a valid function.

    Raises:
     This function should not raise any Exception.
"""
#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(sum_(X, lambda x: x))
#print(sum_(X, lambda x: x**2))
