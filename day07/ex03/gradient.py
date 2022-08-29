# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 16:23:49 by mli               #+#    #+#              #
#    Updated: 2022/08/29 18:16:43 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from typing import Tuple
from prediction import add_intercept


def __check_arrays(arrays: Tuple[np.ndarray]) -> bool:
    return all([
        isinstance(obj, np.ndarray)
        and obj.dtype.kind in 'iuf'
        and len(obj.shape) == 2
        and obj.size != 0
        for obj in arrays])


def gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
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
    if (
        not __check_arrays((x, y, theta))
        or x.shape[0] != y.shape[0]
        or y.shape[1] != 1
        or theta.shape[1] != 1
        or x.shape[1] + 1 != theta.size
    ):
        return None
    m = x.shape[0]
    x = add_intercept(x)
    nabla_j = x.T.dot(x.dot(theta) - y) / m
    return nabla_j
