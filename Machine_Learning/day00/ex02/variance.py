# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    variance.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 11:50:04 by mli               #+#    #+#              #
#    Updated: 2020/01/20 12:12:37 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mean_f(x, f=None):
    width = len(x)
    if (width == 0):
        return (None)
    res = float(0)
    for nb in x:
        res += f(nb) if f != None else nb
    return (res / width)

def variance(x):
    mu = mean_f(x)
    f = (lambda x : (x - mu) ** 2)
    return (mean_f(x, f))

    """Computes the variance of a non-empty numpy.ndarray, using a for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.
    Returns:
     The variance as a float.
     None if x is an empty numpy.ndarray.
    Raises:
     This function should not raise any Exception.
    """

'''
X = np.array([0, 15, -9, 7, 12, 3, -21])
print(variance(X))
print(np.var(X))

print(variance(X/2))
print(np.var(X/2))
'''
