# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loss.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/14 16:11:04 by mli               #+#    #+#              #
#    Updated: 2022/08/13 15:05:14 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from prediction import simple_predict as predict


def loss_elem_(y: np.ndarray, y_hat: np.ndarray) -> np.ndarray:
    """
    Description:
        Calculates all the elements (y_pred - y)^2 of the loss function.
    Args:
        y: has to be an numpy.ndarray, a vector.
        y_hat: has to be an numpy.ndarray, a vector.
    Returns:
        J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
        None if there is a dimension matching problem between X, Y or theta.
    Raises:
        This function should not raise any Exception.
    """
    if not all([isinstance(obj, np.ndarray) for obj in [y, y_hat]]) or y.size == 0:
        return None
    if y.shape not in [(y.size,), (y.size, 1)] or y.shape != y_hat.shape:
        return None
    res = (y_hat - y) ** 2
    return res


def loss_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculates the value of loss function.
    Args:
        y: has to be an numpy.ndarray, a vector.
        y_hat: has to be an numpy.ndarray, a vector.
    Returns:
        J_value : has to be a float.
        None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    j_elem = loss_elem_(y, y_hat)
    if j_elem is None:
        return None
    return np.sum(j_elem) / (2 * y.shape[0])
