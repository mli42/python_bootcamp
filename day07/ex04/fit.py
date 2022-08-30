# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fit.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 18:35:43 by mli               #+#    #+#              #
#    Updated: 2022/08/30 15:55:45 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from typing import Tuple
from gradient import gradient as gradient_
from prediction import predict_


def __check_arrays(arrays: Tuple[np.ndarray]) -> bool:
    return all([
        isinstance(obj, np.ndarray)
        and obj.dtype.kind in 'iuf'
        and len(obj.shape) == 2
        and obj.size != 0
        for obj in arrays])


def fit_(x: np.ndarray, y: np.ndarray, theta: np.ndarray,
         alpha: float, max_iter: int) -> np.ndarray:
    """
    Description:
        Fits the model to the training dataset contained in x and y.
    Args:
        x: a matrix of dimension m * n: (number of training examples, number of features).
        y: a vector of dimension m * 1: (number of training examples, 1).
        theta: a vector of dimension (n + 1) * 1: (number of features + 1, 1).
        alpha: has to be a float, the learning rate
        max_iter: has to be an int, the number of iterations done during the gradient descent
    Returns:
        new_theta: numpy.ndarray, a vector of dimension (number of features + 1, 1).
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exception.
    """
    if (
        not __check_arrays((x, y, theta))
        or not isinstance(alpha, (int, float))
        or not isinstance(max_iter, int)
        or x.shape[0] != y.shape[0]
        or y.shape[1] != 1
        or theta.shape[1] != 1
        or x.shape[1] + 1 != theta.size
    ):
        return None
    theta = theta.astype("float64")
    for _ in range(max_iter):
        nabla = gradient_(x, y, theta)
        theta -= alpha * nabla
    return theta
