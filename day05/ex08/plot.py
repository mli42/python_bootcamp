# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/14 21:39:23 by mli               #+#    #+#              #
#    Updated: 2022/08/14 14:41:05 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
from vec_loss import loss_
from prediction import simple_predict as predict_

def plot_with_loss(x: np.ndarray, y: np.ndarray, theta: np.ndarray) -> None:
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
    if (
        not all([isinstance(obj, np.ndarray) for obj in [x, y, theta]])
        or not all([obj.shape in [(obj.size,), (obj.size, 1)] for obj in [x, y, theta]])
        or theta.size != 2
        or x.size != y.size
    ):
        return None
    # Reshape parameters
    params = [x, y, theta]
    for i, elem in enumerate(params):
        params[i] = elem.reshape(-1, 1)

    # Calculate the loss
    y_hat = predict_(x, theta)
    current_loss = loss_(y, y_hat) * 2

    plt.title(f"Cost: {current_loss:6f}")
    plt.plot(x, y, "o", label="data")
    plt.plot(x, y_hat, label="prediction")
    for i, ax in enumerate(x):
        plt.plot([ax, ax], [y[i], y_hat[i]], "r--")
    # plt.legend()
    plt.show()

if __name__ == "__main__":
    x = np.arange(1,6)
    y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])

    flag = 7
    if flag & 1:
        # Example 1:
        theta1 = np.array([18, -1])
        plot_with_loss(x, y, theta1)
    if flag & 2:
        # Example 2:
        theta2 = np.array([14, 0])
        plot_with_loss(x, y, theta2)
    if flag & 4:
        # Example 3:
        theta3 = np.array([12, 0.8])
        plot_with_loss(x, y, theta3)
