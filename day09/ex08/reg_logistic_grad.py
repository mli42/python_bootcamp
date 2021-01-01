# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reg_logistic_grad.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/01 20:44:43 by mli               #+#    #+#              #
#    Updated: 2021/01/01 21:30:36 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from my_logistic_regression import MyLogisticRegression as MyLR


def reg_logistic_grad(x: np.ndarray, y: np.ndarray, theta: np.ndarray, lambda_: float) -> np.ndarray:
    if (0 in [x.size, y.size, theta.size] or x.shape[0] != y.shape[0] or
        (x.shape[1] + 1) != theta.shape[0]):
        return None
    res = np.zeros(shape=(theta.shape))
    m, n = x.shape
    mylr = MyLR(theta)
    y_hat = mylr.predict_(x)
    for i in range(m):
        y_diff = y_hat[i][0] - y[i][0]
        res[0][0] += y_diff
        for j in range(n):
            res[j + 1][0] += (y_diff * x[i][j]) + (lambda_ * theta[j + 1][0]) / m
    res = res / m
    return res

def vec_reg_logistic_grad(x: np.ndarray, y: np.ndarray, theta: np.ndarray, lambda_: float) -> np.ndarray:
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
    if (0 in [x.size, y.size, theta.size] or x.shape[0] != y.shape[0] or
        (x.shape[1] + 1) != theta.shape[0]):
        return None
    mylr = MyLR(theta)
    m = x.shape[0]
    y_hat = mylr.predict_(x)
    x = mylr.add_intercept(x)
    theta_prime = np.concatenate((np.array([[0]]), theta[1:, ...]), axis=0)
    nabla_j = (x.T.dot(y_hat - y) + lambda_ * theta_prime) / m
    return nabla_j


if __name__ == "__main__":
    def test(x: np.ndarray, y: np.ndarray, theta: np.ndarray, lambda_: float) -> None:
        print("ite: ", lambda_, "\n", reg_logistic_grad(x, y, theta, lambda_))
        print("vec: ", lambda_, "\n", vec_reg_logistic_grad(x, y, theta, lambda_))
        print("_______________________________________________________________")

    x = np.array([[0, 2, 3, 4],
                  [2, 4, 5, 5],
                  [1, 3, 2, 7]])
    y = np.array([[0], [1], [1]])
    theta = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])

    # Example 1:
    test(x, y, theta, 1)
    """
        array([[-0.55711039],
               [-1.40334809],
               [-1.91756886],
               [-2.56737958],
               [-3.03924017]])
    """

    # Example 2:
    test(x, y, theta, 0.5)
    """
        array([[-0.55711039],
               [-1.15334809],
               [-1.96756886],
               [-2.33404624],
               [-3.15590684]])
    """

    # Example 3:
    test(x, y, theta, 0.0)
    """
        array([[-0.55711039],
               [-0.90334809],
               [-2.01756886],
               [-2.10071291],
               [-3.27257351]])
    """
