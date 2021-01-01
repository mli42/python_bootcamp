# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    l2_reg.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/30 23:15:51 by mli               #+#    #+#              #
#    Updated: 2021/01/01 18:04:10 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


def iterative_l2(theta: np.ndarray) -> float:
    # Computes the L2 regularization of a numpy.ndarray, with a for-loop.
    res = float(0)
    for i in range(1, theta.size):
        res += theta[i][0] ** 2
    return res


def l2(theta: np.ndarray) -> float:
    """Computes the L2 regularization of a non-empty numpy.ndarray, without any for-loop.
    Args:
      theta: has to be a numpy.ndarray, a vector of dimension n * 1.
    Returns:
      The L2 regularization as a float.
      None if theta in an empty numpy.ndarray.
    Raises:
      This function should not raise any Exception.
    """
    if theta.size == 0:
        return None
    theta_prime = theta.flatten()[1:, ...].astype("float64")
    return theta_prime.dot(theta_prime)

if __name__ == "__main__":
    x = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)

    print(iterative_l2(x))
    print(l2(x))
    # Output: 911.0

    y = np.array([3, 0.5, -6]).reshape(-1 ,1)
    print(iterative_l2(y))
    print(l2(y))
    # Output: 36.25
