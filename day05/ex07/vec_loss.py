# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_loss.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/14 16:11:04 by mli               #+#    #+#              #
#    Updated: 2022/08/13 16:07:12 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

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
    if not all([isinstance(obj, np.ndarray) for obj in [y, y_hat]]) or y.size == 0:
        return None
    if y.shape not in [(y.size,), (y.size, 1)] or y.shape != y_hat.shape:
        return None
    x = (y_hat - y)
    j_elem = x.dot(x) / (2 * y.shape[0])
    return np.sum(j_elem)
