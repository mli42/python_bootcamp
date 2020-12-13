# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 21:35:03 by mli               #+#    #+#              #
#    Updated: 2020/12/13 21:54:03 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def add_intercept(x: np.ndarray) -> np.ndarray:
    """Adds a column of 1's to the non-empty numpy.ndarray x.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * 1.
    Returns:
      X as a numpy.ndarray, a vector of dimension m * 2.
      None if x is not a numpy.ndarray.
      None if x is a empty numpy.ndarray.
    Raises:
      This function should not raise any Exception.
    """
    shape = (x.shape[0], 1)
    ones = np.full(shape, 1)
    res = np.concatenate((ones, x), axis=1)
    return res

if __name__ == "__main__":
    # Example 1:
    x = np.arange(1, 6, dtype=float).reshape((5, 1))
    print(add_intercept(x))
    # Output:
    """
    array([[1., 1.],
           [1., 2.],
           [1., 3.],
           [1., 4.],
           [1., 5.]])
    """
    # Example 2:
    y = np.arange(1, 10, dtype=float).reshape((3, 3))
    print(add_intercept(y))
    # Output:
    """
    array([[1., 1., 2., 3.],
           [1., 4., 5., 6.],
           [1., 7., 8., 9.]])
    """
