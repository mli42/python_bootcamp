# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 22:28:37 by mli               #+#    #+#              #
#    Updated: 2022/08/12 19:13:16 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt

def plot(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> None:
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * 1.
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
      This function should not raise any Exceptions.
    """
    if (
        not all([isinstance(obj, np.ndarray) for obj in [x, y, theta]])
        or x.size == 0
        or theta.shape not in [(2,), (2, 1)]
        or x.shape not in [(x.size,), (x.size, 1)]
        or x.shape != y.shape
        ):
        print('Incorrect parameter')
        return None
    h = lambda x: theta[0] + theta[1] * x
    plt.plot(x, y, "o")
    plt.plot(x, h(x))
    plt.show()

if __name__ == "__main__":
    x = np.arange(1,6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

    flag = 7

    if True:
        if flag & 1:
            # Example 1:
            theta1 = np.array([4.5, -0.2])
            plot(x, y, theta1)
        if flag & 2:
            # Example 2:
            theta2 = np.array([-1.5, 2])
            plot(x, y, theta2)
        if flag & 4:
            # Example 3:
            theta3 = np.array([3, 0.3])
            plot(x, y, theta3)
