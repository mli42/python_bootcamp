# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    log_pred.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/26 15:52:52 by mli               #+#    #+#              #
#    Updated: 2020/12/26 17:56:37 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

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

def sigmoid_(x: np.ndarray) -> np.ndarray:
    """
    Compute the sigmoid of a vector.
    Args:
        x: has to be an numpy.ndarray, a vector
    Returns:
        The sigmoid value as a numpy.ndarray.
        None if x is an empty numpy.ndarray.
    Raises:
        This function should not raise any Exception.
    """
    if x.size == 0:
        return None
    return 1 / (1 + np.exp(-x))

def logistic_predict_(x: np.ndarray, theta: np.ndarray) -> np.ndarray:
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * n.
      theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
    Returns:
      y_hat as a numpy.ndarray, a vector of dimension m * 1.
      None if x or theta are empty numpy.ndarray.
      None if x or theta dimensions are not appropriate.
    Raises:
      This function should not raise any Exception.
    """
    if (x.shape[1] + 1) != theta.shape[0]:
        return None
    x = add_intercept(x)
    y_hat = sigmoid_(x.dot(theta))
    return y_hat

if __name__ == "__main__":
    # Example 1
    x = np.array([4]).reshape(1, 1)
    theta = np.array([[2], [0.5]])
    print(logistic_predict_(x, theta))
    # Output: array([[0.98201379]])

    # Example 1
    x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
    theta2 = np.array([[2], [0.5]])
    print(logistic_predict_(x2, theta2))
    # Output:
    """
    array([[0.98201379],
           [0.99624161],
           [0.97340301],
           [0.99875204],
           [0.90720705]])
    """

    # Example 3
    x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
    theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
    print(logistic_predict_(x3, theta3))
    # Output:
    """
    array([[0.03916572],
           [0.00045262],
           [0.2890505 ]])
    """
