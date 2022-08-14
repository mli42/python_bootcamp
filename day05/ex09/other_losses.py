# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    other_losses.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/14 22:59:47 by mli               #+#    #+#              #
#    Updated: 2022/08/14 15:34:44 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from math import sqrt


def __guard(y: np.ndarray, y_hat: np.ndarray) -> bool:
    """ Check y and y_hat type and shape
    Args:
        y (np.ndarray): should be a (m * 1) vector
        y_hat (np.ndarray): should be a (m * 1) vector
    Returns:
        bool: True if it is all good, False otherwise
    """
    if (
        not all([isinstance(obj, np.ndarray) for obj in [y, y_hat]]) or y.size == 0
        or not all([obj.shape in [(obj.size,), (obj.size, 1)] for obj in [y, y_hat]])
        or y.shape != y_hat.shape
    ):
        return False
    return True


def mse_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculate the MSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
    Returns:
        mse: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    if __guard(y, y_hat) is False:
        return None
    j_elem = (y_hat - y) ** 2 / y.shape[0]
    return np.sum(j_elem)


def rmse_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculate the RMSE between the predicted output and the real output.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
    Returns:
        rmse: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    res = mse_(y, y_hat)
    if res is None:
        return None
    return res ** 0.5


def mae_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculate the MAE between the predicted output and the real output.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
    Returns:
        mae: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    if __guard(y, y_hat) is False:
        return None
    elem = abs(y_hat - y)
    return np.sum(elem) / y.shape[0]


def r2score_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculate the R2score between the predicted output and the output.
    Args:
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be a numpy.ndarray, a vector of dimension m * 1.
    Returns:
        r2score: has to be a float.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exceptions.
    """
    if __guard(y, y_hat) is False:
        return None
    y_mean = np.sum(y) / y.shape[0]
    dividend = np.sum((y_hat - y) ** 2)
    divisor = np.sum((y - y_mean) ** 2)
    res = 1 - (dividend / divisor)
    return res
