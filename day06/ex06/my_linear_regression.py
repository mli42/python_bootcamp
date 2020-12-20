# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_linear_regression.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 20:59:43 by mli               #+#    #+#              #
#    Updated: 2020/12/20 22:12:28 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class MyLinearRegression():
    """
    Description:
        My personnal linear regression class to fit like a boss.
    """

    def __init__(self, thetas: np.ndarray, alpha: float = 0.001, max_iter: int = 1000):
        if isinstance(thetas, list):
            thetas = np.asarray(thetas).reshape(len(thetas), 1)
        thetas = thetas.astype("float64")
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    @staticmethod
    def mse_(y: np.ndarray, y_hat: np.ndarray) -> float:
        if y.shape != y_hat.shape:
            return None
        mse_elem = (y_hat - y) ** 2 / (y.shape[0])
        return np.sum(mse_elem)

    @staticmethod
    def cost_elem_(y: np.ndarray, y_hat: np.ndarray) -> np.ndarray:
        """
        Description:
            Calculates all the elements (1/2*M)*(y_pred - y)^2 of the cost function.
        Args:
            y: has to be an numpy.ndarray, a vector.
            y_hat: has to be an numpy.ndarray, a vector.
        Returns:
            J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
            None if there is a dimension matching problem between X, Y or theta.
        Raises:
            This function should not raise any Exception.
        """
        if y.shape != y_hat.shape:
            return None
        res = (y_hat - y) ** 2 / (2 * y.shape[0])
        return res

    @staticmethod
    def cost_(y: np.ndarray, y_hat: np.ndarray) -> float:
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
        if y.shape != y_hat.shape:
            return None
        j_elem = MyLinearRegression.cost_elem_(y, y_hat)
        return np.sum(j_elem)

    @staticmethod
    def add_intercept(x: np.ndarray, axis: int = 1) -> np.ndarray:
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
        ones = np.ones((x.shape[0], 1))
        res = np.concatenate((ones, x), axis=axis)
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
        theta = self.thetas
        intercepted = self.add_intercept(x)
        if intercepted.shape[1] != theta.shape[0]:
            return None
        y_hat = intercepted.dot(theta)
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
        theta = self.thetas
        alpha = self.alpha
        if x.shape != y.shape or theta.shape != (2, 1):
            return None
        for _ in range(self.max_iter):
            new_theta = self.gradient_(x, y)
            theta[0][0] -= alpha * new_theta[0][0]
            theta[1][0] -= alpha * new_theta[1][0]
        self.thetas = theta
