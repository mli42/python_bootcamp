# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 16:23:49 by mli               #+#    #+#              #
#    Updated: 2020/12/22 16:39:18 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from prediction import add_intercept

def gradient_(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Computes a gradient vector from three non-empty numpy.ndarray,
        without any for-loop. The three arrays must have the compatible dimensions.
    Args:
        x: has to be an numpy.ndarray, a matrix of dimension m * n.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector (n + 1) * 1.
    Returns:
        The gradient as a numpy.ndarray, a vector of dimensions n * 1,
        containg the result of the formula for all j.
        None if x, y, or theta are empty numpy.ndarray.
        None if x, y and theta do not have compatible dimensions.
    Raises:
        This function should not raise any Exception.
    """
    m = x.shape[0]
    x = add_intercept(x)
    nabla_j = x.T.dot(x.dot(theta) - y) / m
    return nabla_j

if __name__ == "__main__":
    X = np.array([
            [-6,  -7,  -9],
            [13,  -2,  14],
            [-7,  14,  -1],
            [-8,  -4,   6],
            [-5,  -9,   6],
            [ 1,  -5,  11],
            [ 9, -11,   8]])
    Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)
    theta = np.array([0, 3, 0.5, -6]).reshape(-1, 1)

    print(gradient_(X, Y, theta))
    """
       [[ -33.71428571]
        [ -37.35714286]
        [ 183.14285714]
        [-393.        ]]
    """

    theta = np.array([0, 0, 0, 0]).reshape(-1, 1)
    print(gradient_(X, Y, theta))
    """
       [[-0.71428571]
        [ 0.85714286]
        [23.28571429]
        [-26.42857143]]
    """
