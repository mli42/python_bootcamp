# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 21:56:52 by mli               #+#    #+#              #
#    Updated: 2020/12/15 23:15:58 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

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
    ones = np.ones((x.shape[0], 1))
    res = np.concatenate((ones, x), axis=1)
    return res

def predict_(x: np.ndarray, theta: np.ndarray) -> np.ndarray:
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
    intercepted = add_intercept(x)
    if intercepted.shape[1] != theta.shape[0]:
        return None
    y_hat = intercepted.dot(theta)
    return y_hat

if __name__ == "__main__":
    x = np.arange(1,6).reshape(5, 1)

    # Example 1:
    theta1 = np.array([5, 0])
    print(predict_(x, theta1))
    # Ouput: array([5., 5., 5., 5., 5.])
    # Do you understand why y_hat contains only 5's here?

    # Example 2:
    theta2 = np.array([0, 1])
    print(predict_(x, theta2))
    # Output: array([1., 2., 3., 4., 5.])
    # Do you understand why y_hat == x here?

    # Example 3:
    theta3 = np.array([5, 3])
    print(predict_(x, theta3))
    # Output: array([ 8., 11., 14., 17., 20.])

    # Example 4:
    theta4 = np.array([-3, 1])
    print(predict_(x, theta4))
    # Output: array([-2., -1.,  0.,  1.,  2.])

    # More:
    print(predict_(np.array([[1, 2, 3], [4, 5, 6]]), theta4))
    # Wrong shape
