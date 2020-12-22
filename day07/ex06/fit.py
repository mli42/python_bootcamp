# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fit.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 18:35:43 by mli               #+#    #+#              #
#    Updated: 2020/12/22 16:53:10 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from gradient import gradient_
from prediction import predict_

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
    if x.shape[0] != y.shape[0] or (x.shape[1] + 1) != theta.shape[0]:
        return None
    for _ in range(max_iter):
        new_theta = gradient_(x, y, theta)
        theta -= alpha * new_theta
    return theta

if __name__ == "__main__":
    x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
    y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
    theta = np.array([[42.], [1.], [1.], [1.]])

    # Example 0:
    theta2 = fit_(x, y, theta,  alpha = 0.0005, max_iter=42000)
    print(theta2)
    # Output: array([[41.99..],[0.97..], [0.77..], [-1.20..]])

    # Example 1:
    print(predict_(x, theta2))
    # Output: array([[19.5992..], [-2.8003..], [-25.1999..], [-47.5996..]])