# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loss.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/14 16:11:04 by mli               #+#    #+#              #
#    Updated: 2022/08/29 16:39:43 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


def __check_arrays(arrays: Tuple[np.ndarray]) -> bool:
    return all([
        isinstance(obj, np.ndarray)
        and obj.dtype.kind in 'iuf'
        and len(obj.shape) == 2
        and obj.size != 0
        for obj in arrays])


def loss_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """Computes the half mean squared error of two non-empty numpy.ndarray,
        without any for loop. The two arrays must have the same dimensions.
    Args:
      y: has to be an numpy.ndarray, a vector.
      y_hat: has to be an numpy.ndarray, a vector.
    Returns:
      The half mean squared error of the two vectors as a float.
      None if y or y_hat are empty numpy.ndarray.
      None if y and y_hat does not share the same dimensions.
    Raises:
      This function should not raise any Exceptions.
    """
    if (
        __check_arrays((y, y_hat)) is False
        or y.size != y.shape[0]
        or y.shape != y_hat.shape
    ):
        return None
    j_elem = (y_hat - y) ** 2 / (2 * y.shape[0])
    return np.sum(j_elem)
