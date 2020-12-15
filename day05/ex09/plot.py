# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/14 21:39:23 by mli               #+#    #+#              #
#    Updated: 2020/12/14 22:24:02 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
from vec_cost import cost_
from prediction import simple_predict as predict_

def plot_with_cost(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> None:
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * 1.
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
      This function should not raise any Exception.
    """
    y_hat = predict_(x, theta)
    costs = cost_(y, y_hat)
    plt.title("Cost: %f" %costs)
    plt.plot(x, y, "o", label="data")
    plt.plot(x, y_hat, label="prediction")
    for i, ax in enumerate(x):
        plt.plot(list(ax) * 2, [y[i], y_hat[i]], "r--")
    #plt.legend()
    plt.show()

if __name__ == "__main__":
    x = np.arange(1,6).reshape(5, 1)
    y = np.array([11.52434424, 10.62589482, 13.14755699,
                  18.60682298, 14.14329568]).reshape(5, 1)

    flag = 7
    if flag & 1:
        # Example 1:
        theta1 = np.array([18, -1]).reshape(2, 1)
        plot_with_cost(x, y, theta1)
    if flag & 2:
        # Example 2:
        theta2 = np.array([14, 0]).reshape(2, 1)
        plot_with_cost(x, y, theta2)
    if flag & 4:
        # Example 3:
        theta3 = np.array([12, 0.8]).reshape(2, 1)
        plot_with_cost(x, y, theta3)
