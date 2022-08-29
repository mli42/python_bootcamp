# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 15:03:43 by mli               #+#    #+#              #
#    Updated: 2022/08/29 14:24:47 by mli              ###   ########.fr        #
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


def simple_predict(x: np.ndarray, theta: np.ndarray) -> np.ndarray:
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
    m, n = x.shape
    y_hat = np.full(shape=(m, 1), fill_value=theta[0][0])
    for i in range(m):
        for j in range(n):
            y_hat[i][0] += x[i][j] * theta[j + 1][0]
    return y_hat
