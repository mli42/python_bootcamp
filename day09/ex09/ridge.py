# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ridge.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/01 22:31:15 by mli               #+#    #+#              #
#    Updated: 2021/01/02 18:36:03 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from mylinearregression import MyLinearRegression as MyLR


class MyRidge(MyLR):
    """
    Description:
        My personnal ridge regression class
    """

    def __init__(self,  thetas, alpha=0.001, max_iter=1000, lambda_=0.5):
        super().__init__(thetas, alpha, max_iter)
        self.lambda_ = lambda_

    def get_theta_prime(self) -> np.ndarray:
        theta_prime = np.concatenate((np.array([[0]]), self.thetas[1:, ...]), axis=0)
        return theta_prime

    def l2(self) -> float:
        """Computes the L2 regularization of a non-empty numpy.ndarray.
        Args:
            theta: has to be a numpy.ndarray, a vector of dimension n * 1.
        Returns:
            The L2 regularization as a float.
            None if theta in an empty numpy.ndarray.
        Raises:
            This function should not raise any Exception.
        """
        theta = self.thetas
        if theta.size == 0:
            return None
        theta_prime = theta.flatten()[1:, ...].astype("float64")
        return theta_prime.dot(theta_prime)

    def cost_(self, y: np.ndarray, y_hat: np.ndarray) -> float:
        """Computes the regularized cost of a linear regression model from two non-empty numpy.ndarray, without any for loop.
            The two arrays must have the same dimensions.
        Args:
            y: has to be an numpy.ndarray, a vector of dimension m * 1.
            y_hat: has to be an numpy.ndarray, a vector of dimension m * 1.
            theta: has to be a numpy.ndarray, a vector of dimension n * 1.
            lambda_: has to be a float.
        Returns:
            The regularized cost as a float.
            None if y, y_hat, or theta are empty numpy.ndarray.
            None if y and y_hat do not share the same dimensions.
        Raises:
            This function should not raise any Exception.
        """
        if y.shape != y_hat.shape:
            return None
        j_elem = np.sum((y_hat - y) ** 2) + self.lambda_ * self.l2()
        res =  j_elem / (2 * y.shape[0])
        return res

    def gradient_(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """Computes the regularized linear gradient of three non-empty numpy.ndarray, without any for-loop. The three arrays must have compatible dimensions.
        Args:
            x: has to be a numpy.ndarray, a matrix of dimesion m * n.
            y: has to be a numpy.ndarray, a vector of dimension m * 1.
            theta: has to be a numpy.ndarray, a vector of dimension n * 1.
            lambda_: has to be a float.
        Returns:
            A numpy.ndarray, a vector of dimension n * 1, containing the results of the formula for all j.
            None if y, x, or theta are empty numpy.ndarray.
            None if y, x or theta does not share compatibles dimensions.
        Raises:
            This function should not raise any Exception.
        """
        nabla_j = super().gradient_(x, y)
        if nabla_j is not None:
            m = x.shape[0]
            nabla_j += (self.lambda_ * self.get_theta_prime()) / m
        return nabla_j

    # Does not need to reimplement fit because it uses gradient_()

if __name__ == "__main__":
    a = MyRidge([1, 2, 3, 4])
    print(a.thetas)
    print(a.lambda_)
    print(a.get_theta_prime())
