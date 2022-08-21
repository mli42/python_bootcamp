# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/16 22:28:08 by mli               #+#    #+#              #
#    Updated: 2022/08/21 21:59:51 by mli              ###   ########.fr        #
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
    if not isinstance(x, np.ndarray) or x.dtype.kind not in 'iuf' or x.size == 0:
        return None
    if len(x.shape) == 1:
        x = x.reshape(-1, 1)
    ones = np.ones((x.shape[0], 1))
    res = np.concatenate((ones, x), axis=1)
    return res


def predict_(x: np.ndarray, theta: np.ndarray) -> np.ndarray:
    if not all([isinstance(obj, np.ndarray) and obj.dtype.kind in 'iuf' for obj in [x, theta]]) or x.size == 0:
        return None
    if theta.shape not in [(2,), (2, 1)] or x.shape not in [(x.size,), (x.size, 1)]:
        return None
    x = add_intercept(x)
    y_hat = x.dot(theta)
    return y_hat


def simple_gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Computes a gradient vector from three non-empty numpy.ndarray.
        The three arrays must have compatible dimensions.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * 1.
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be an numpy.ndarray, a 2 * 1 vector.
    Returns:
      The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
      None if x, y, or theta are empty numpy.ndarray.
      None if x, y and theta do not have compatible dimensions.
    Raises:
      This function should not raise any Exception.
    """
    if (
        not all([
            isinstance(obj, np.ndarray)
            and obj.dtype.kind in 'iuf'
            and obj.shape in [(obj.size,), (obj.size, 1)]
            for obj in (x, y, theta)])
        or theta.size != 2
        or x.size != y.size
    ):
        return None
    # Reshape parameters
    params = [x, y, theta]
    for i, elem in enumerate(params):
        params[i] = elem.reshape(-1, 1)

    # Gradient algorithm
    m = x.shape[0]
    res = np.zeros(theta.shape)
    y_hat = predict_(x, theta)
    for i in range(m):
        res[0][0] += (y_hat[i][0] - y[i][0])
        res[1][0] += (y_hat[i][0] - y[i][0]) * (x[i][0])
    res = res / m
    return res
