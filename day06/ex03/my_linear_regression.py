# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_linear_regression.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 20:59:43 by mli               #+#    #+#              #
#    Updated: 2022/08/24 13:51:51 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from typing import Tuple


class MyLinearRegression():
    """
    Description:
        My personnal linear regression class to fit like a boss.
    """

    def __check_arrays(self, arrays: Tuple[np.ndarray]) -> bool:
        return all([
            isinstance(obj, np.ndarray)
            and obj.dtype.kind in 'iuf'
            and obj.shape == (obj.size, 1)
            and obj.size != 0
            for obj in arrays])


    def __init__(self, thetas: np.ndarray, alpha: float = 0.001, max_iter: int = 1000):
        if (
            not self.__check_arrays((thetas,))
            or not isinstance(alpha, (int, float))
            or not isinstance(max_iter, int)
            or thetas.size != 2
        ):
            raise ValueError('Wrong argument')

        thetas = thetas.reshape(-1, 1).astype("float64")
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas


    def loss_elem_(self, y: np.ndarray, y_hat: np.ndarray) -> float:
        if (
            not self.__check_arrays((y, y_hat))
            or y.shape != y_hat.shape
        ):
            return None
        j_elem = (y_hat - y) ** 2 / (2 * y.shape[0])
        return j_elem


    def loss_(self, y: np.ndarray, y_hat: np.ndarray) -> float:
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
        j_elem = self.loss_elem_(y, y_hat)
        if j_elem is None:
            return None
        return np.sum(j_elem)


    def mse_(self, y: np.ndarray, y_hat: np.ndarray) -> float:
        """ Computes the MSE of two non-empty numpy.ndarray.
            The two arrays must have the same dimensions.
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
            not self.__check_arrays((y, y_hat))
            or y.shape != y_hat.shape
        ):
            return None
        j_elem = (y_hat - y) ** 2
        return np.sum(j_elem) / y.shape[0]


    @staticmethod
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
        if not isinstance(x, np.ndarray) or x.size == 0:
            return None
        if len(x.shape) == 1:
            x = x.reshape(-1, 1)
        ones = np.ones((x.shape[0], 1))
        res = np.concatenate((ones, x), axis=1)
        return res


    def predict_(self, x: np.ndarray) -> np.ndarray:
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
        if (
            not self.__check_arrays((x, self.thetas))
            or x.shape[1] + 1 != self.thetas.shape[0]
        ):
            return None
        x = self.add_intercept(x)
        y_hat = x.dot(self.thetas)
        return y_hat


    def gradient_(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """Computes a gradient vector from three non-empty numpy.ndarray, without any for loop.
            The three arrays must have compatible dimensions.
        Args:
            x: has to be a numpy.ndarray, a matrix of dimension m * 1.
            y: has to be a numpy.ndarray, a vector of dimension m * 1.
            theta: has to be a numpy.ndarray, a 2 * 1 vector.
        Returns:
            The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
            None if x, y, or theta is an empty numpy.ndarray.
            None if x, y and theta do not have compatible dimensions.
        Raises:
            This function should not raise any Exception.
        """
        if (
            not self.__check_arrays((x, y, self.thetas))
            or self.thetas.size != 2
            or x.size != y.size
        ):
            return None
        m = x.shape[0]
        x = self.add_intercept(x)
        nabla_j = x.T.dot(x.dot(self.thetas) - y) / m
        return nabla_j


    def fit_(self, x: np.ndarray, y: np.ndarray) -> None:
        """
        Description:
            Fits the model to the training dataset contained in x and y.
        Args:
            x: a vector of dimension m * 1: (number of training examples, 1).
            y: a vector of dimension m * 1: (number of training examples, 1).
            theta: a vector of dimension 2 * 1.
            alpha: has to be a float, the learning rate
            max_iter: has to be an int, the number of iterations done
        Returns:
            new_theta: numpy.ndarray, a vector of dimension 2 * 1.
            None if there is a matching dimension problem.
        Raises:
            This function should not raise any Exception.
        """
        if (
            not self.__check_arrays((x, y, self.thetas))
            or self.thetas.size != 2
            or x.size != y.size
        ):
            return None
        for _ in range(self.max_iter):
            nabla = self.gradient_(x, y)
            self.thetas -= self.alpha * nabla
