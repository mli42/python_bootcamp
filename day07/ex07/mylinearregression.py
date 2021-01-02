# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mylinearregression.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 20:59:43 by mli               #+#    #+#              #
#    Updated: 2021/01/02 18:22:02 by mli              ###   ########.fr        #
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
            thetas = np.asarray(thetas).reshape(-1, 1)
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
            x: has to be an numpy.ndarray, a matrix of dimension m * n.
        Returns:
            X as a numpy.ndarray, a matrix of dimension m * (n + 1).
            None if x is not a numpy.ndarray.
            None if x is a empty numpy.ndarray.
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(x, np.ndarray) or x.size == 0:
            return None
        ones = np.ones((x.shape[0], 1))
        res = np.concatenate((ones, x), axis=axis)
        return res

    def predict_(self, x: np.ndarray) -> np.ndarray:
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
        theta = self.thetas
        if (x.shape[1] + 1) != theta.shape[0]:
            return None
        intercepted = self.add_intercept(x)
        y_hat = intercepted.dot(theta)
        return y_hat

    def gradient_(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
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
        theta = self.thetas
        if (0 in [x.size, y.size, theta.size] or x.shape[0] != y.shape[0] or
            (x.shape[1] + 1) != theta.shape[0]):
            return None
        m = x.shape[0]
        y_hat = self.predict_(x)
        x = self.add_intercept(x)
        nabla_j = x.T.dot(y_hat - y) / m
        return nabla_j

    def fit_(self, x: np.ndarray, y: np.ndarray) -> None:
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
        theta = self.thetas
        alpha = self.alpha
        if x.shape[0] != y.shape[0] or (x.shape[1] + 1) != theta.shape[0]:
            return None
        for _ in range(self.max_iter):
            new_theta = self.gradient_(x, y)
            theta -= alpha * new_theta
        self.thetas = theta
