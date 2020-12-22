# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_model.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 22:47:23 by mli               #+#    #+#              #
#    Updated: 2020/12/22 23:07:35 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def add_polynomial_features(x: np.ndarray, power: int) -> np.ndarray:
    """Add polynomial features to vector x by raising its values up to the power given in argument.
    Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        power: has to be an int, the power up to which the components of vector x are going to be raised.
    Returns:
        The matrix of polynomial features as a numpy.ndarray, of dimension m * n,
        containing the polynomial feature values for all training examples.
        None if x is an empty numpy.ndarray.
    Raises:
        This function should not raise any Exception.
    """
    res = x
    for i in range(2, power + 1):
        raised = x ** i
        res = np.concatenate((res, raised), axis=1)
    return res

if __name__ == "__main__":
    x = np.arange(1,6).reshape(-1, 1)

    # Example 1:
    print(add_polynomial_features(x, 3))
    # Output:
    """
    array([[1,   1,   1],
           [2,   4,   8],
           [3,   9,  27],
           [4,  16,  64],
           [5,  25, 125]])
    """

    # Example 2:
    print(add_polynomial_features(x, 6))
    # Output:
    """
    array([[    1,     1,     1,     1,     1,     1],
           [    2,     4,     8,    16,    32,    64],
           [    3,     9,    27,    81,   243,   729],
           [    4,    16,    64,   256,  1024,  4096],
           [    5,    25,   125,   625,  3125, 15625]])
    """
