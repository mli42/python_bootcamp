# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    log_loss.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/26 16:25:18 by mli               #+#    #+#              #
#    Updated: 2020/12/26 17:57:43 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from log_pred import logistic_predict_

def log_loss_(y: np.ndarray, y_hat: np.ndarray, eps: float = 1e-15) -> float:
    """
    Computes the logistic loss value.
    Args:
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        y_hat: has to be an numpy.ndarray, a vector of dimension m * 1.
        eps: has to be a float, epsilon (default=1e-15)
    Returns:
        The logistic loss value as a float.
        None on any error.
    Raises:
        This function should not raise any Exception.
    """
    if y.shape != y_hat.shape:
        return None
    res = 0
    m = y.shape[0]
    for i in range(m):
        res += y[i][0] * np.log(y_hat[i][0]) + (1 - y[i][0]) * np.log(1 - y_hat[i][0])
    res /= -m
    return res

if __name__ == "__main__":
    # Example 1:
    y1 = np.array([1]).reshape(1, 1)
    x1 = np.array([4]).reshape(1, 1)
    theta1 = np.array([[2], [0.5]])
    y_hat1 = logistic_predict_(x1, theta1)
    print(log_loss_(y1, y_hat1))
    # Output: 0.01814992791780973

    # Example 2:
    y2 = np.array([[1], [0], [1], [0], [1]])
    x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
    theta2 = np.array([[2], [0.5]])
    y_hat2 = logistic_predict_(x2, theta2)
    print(log_loss_(y2, y_hat2))
    # Output: 2.4825011602474483

    # Example 3:
    y3 = np.array([[0], [1], [1]])
    x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
    theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
    y_hat3 = logistic_predict_(x3, theta3)
    print(log_loss_(y3, y_hat3))
    # Output: 2.9938533108607053
