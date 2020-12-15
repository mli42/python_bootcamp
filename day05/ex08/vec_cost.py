# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vec_cost.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/14 16:11:04 by mli               #+#    #+#              #
#    Updated: 2020/12/15 23:20:54 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

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
    j_elem = (y_hat - y) ** 2 / (2 * y.shape[0])
    return np.sum(j_elem)

if __name__ == "__main__":
    X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(7, 1)
    Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(7, 1)

    flag = 3
    if flag & 1:
        # Example 1:
        print(cost_(X, Y))
        # Output: 2.142857142857143
    if flag & 2:
        # Example 2:
        print(cost_(X, X))
        # Output: 0.0
