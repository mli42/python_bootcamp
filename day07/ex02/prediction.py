# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 15:03:43 by mli               #+#    #+#              #
#    Updated: 2020/12/22 15:34:40 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def simple_predict(x: np.ndarray, theta: np.ndarray) -> np.ndarray:
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
    m, n = x.shape
    y_hat = np.zeros((m, 1))
    y_hat[..., 0] = theta[0, 0]
    for i in range(m):
        for j in range(n):
            y_hat[i][0] += x[i][j] * theta[j + 1][0]
    return y_hat

if __name__ == "__main__":
    x = np.arange(1, 13).reshape((4, -1))

    # Example 1:
    theta1 = np.array([5, 0, 0, 0]).reshape(-1, 1)
    print(simple_predict(x, theta1))
    # Ouput: array([5., 5., 5., 5.])

    # Example 2:
    theta2 = np.array([0, 1, 0, 0]).reshape(-1, 1)
    print(simple_predict(x, theta2))
    # Output: array([ 1.,  4.,  7., 10.])

    # Example 3:
    theta3 = np.array([-1.5, 0.6, 2.3, 1.98]).reshape(-1, 1)
    print(simple_predict(x, theta3))
    # Output: array([ 9.64, 24.28, 38.92, 53.56])


    # Example 4:
    theta4 = np.array([-3, 1, 2, 3.5]).reshape(-1, 1)
    print(simple_predict(x, theta4))
    # Output: array([12.5, 32. , 51.5, 71. ])
