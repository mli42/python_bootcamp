# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 15:37:28 by mli               #+#    #+#              #
#    Updated: 2022/08/29 16:22:33 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from typing import Tuple


def __check_arrays(arrays: Tuple[np.ndarray]) -> bool:
    return all([
        isinstance(obj, np.ndarray)
        and obj.dtype.kind in 'iuf'
        and len(obj.shape) == 2
        and obj.size != 0
        for obj in arrays])


def add_intercept(x: np.ndarray) -> np.ndarray:
    """Adds a column of 1's to the non-empty numpy.ndarray x.
    Args:
        x: has to be an numpy.ndarray, a matrix of dimension m * n.
    Returns:
        X as a numpy.ndarray, a matrix of dimension m * (n + 1).
        None if x is not a numpy.ndarray.
        None if x is a empty numpy.ndarray.
    Raises:
        This function should not raise any Exception.
    """
    if __check_arrays((x, )) is False:
        return None
    ones = np.ones((x.shape[0], 1))
    res = np.concatenate((ones, x), axis=1)
    return res


def predict_(x: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Computes the prediction vector y_hat from two non-empty numpy.ndarray.
    Args:
      x: has to be an numpy.ndarray, a matrix of dimension m * n.
      theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
    Returns:
      y_hat as a numpy.ndarray, a vector of dimension m * 1.
      None if x or theta are empty numpy.ndarray.
      None if x or theta dimensions are not appropriate.
    Raises:
      This function should not raise any Exception.
    """
    if (
        __check_arrays((x, theta)) is False
        or theta.size != theta.shape[0]
        or x.shape[1] + 1 != theta.size
    ):
        return None
    x = add_intercept(x)
    y_hat = x.dot(theta)
    return y_hat
