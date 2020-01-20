# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mean.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 11:38:26 by mli               #+#    #+#              #
#    Updated: 2020/01/20 11:46:23 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mean(x):
    width = len(x)
    if (width == 0):
        return (None)
    res = float(0)
    for nb in x:
        res += nb
    return (res / width)


    """Computes the mean of a non-empty numpy.ndarray, using a for-loop.
    Args:
     x: has to be an numpy.ndarray, a vector.

    Returns:
     The mean as a float.
     None if x is an empty numpy.ndarray.

    Raises:
     This function should not raise any Exception.
    """

'''
X = np.array([0, 15, -9, 7, 12, 3, -21])
print(mean(X))
print(mean(X ** 2))
'''
