# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 18:35:15 by mli               #+#    #+#              #
#    Updated: 2022/08/11 18:13:04 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def simple_predict(x: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
      y_hat as a numpy.ndarray, a vector of dimension m * 1.
      None if x or theta are empty numpy.ndarray.
      None if x or theta dimensions are not appropriate.
    Raises:
      This function should not raise any Exception.
    """
    if not all([isinstance(obj, np.ndarray) for obj in [x, theta]]):
        return None
    if theta.shape not in [(2,), (2, 1)] or x.shape not in [(x.size,), (x.size, 1)]:
        return None
    return theta[0] + theta[1] * x
