# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fit.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 18:35:43 by mli               #+#    #+#              #
#    Updated: 2020/12/19 20:49:41 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from gradient import gradient
from prediction import predict_

def fit_(x: np.ndarray, y: np.ndarray, theta: np.ndarray,
         alpha: float, max_iter: int) -> np.ndarray:
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
    if x.shape != y.shape or theta.shape != (2, 1):
        return None
    theta = theta.astype("float64")
    while max_iter > 0:
        new_theta = gradient(x, y, theta)
        theta[0][0] -= alpha * new_theta[0][0]
        theta[1][0] -= alpha * new_theta[1][0]
        max_iter -= 1
    return theta

if __name__ == "__main__":
    x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
    y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
    theta= np.array([1, 1])

    x = x.reshape(len(x), 1)
    y = y.reshape(len(y), 1)
    theta = theta.reshape(len(theta), 1)

    # Example 0:
    theta1 = fit_(x, y, theta, alpha=5e-8, max_iter=1500000)
    print(theta1)
    # Output:
    """
    array([[1.40709365],
           [1.1150909]])
    """
    # Example 1:
    print(predict_(x, theta1))
    # Output:
    """
    array([[15.3408728],
           [25.38243697],
           [36.59126492],
           [55.95130097],
           [65.53471499]])
    """
