# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_model.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/20 18:27:27 by mli               #+#    #+#              #
#    Updated: 2020/12/21 15:26:11 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR

def plot_regression(x: np.ndarray, y: np.ndarray, y_hat: np.ndarray) -> None:
    """ Plots true data + predicted data
    Args:
        x, y, y_hat: numpy.ndarray of size m * 1
    """
    if x.shape != y.shape or y.shape != y_hat.shape:
        return
    plt.xlabel("Quantity of blue pill (in micrograms)")
    plt.ylabel("Space driving score")
    plt.grid()

    plt.plot(x, y_hat, "--X", color="lime", linewidth=2, label="S$_{predict}$(pills)")
    plt.plot(x, y, "o", color="cyan", label="S$_{true}$(pills)")

    plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", ncol=2, frameon=False)
    plt.show()

def plot_cost(x: np.ndarray, y: np.ndarray) -> None:
    plt.xlabel("$θ_1$")
    plt.ylabel("cost function $J(θ_0, θ_1)$")
    plt.grid()

    linear_model = MyLR(np.array([[0], [0]]), max_iter=500)
    thetas_0 = range(85, 95, 2)
    for t0 in thetas_0:
        linear_model.thetas[0][0] = t0

        npoints = 100
        y_cost = [0] * npoints
        thetas1 = np.linspace(-15, -3.8, npoints)
        for i, t1 in enumerate(thetas1):
            linear_model.thetas[1][0] = t1
            y_hat = linear_model.predict_(x)
            y_cost[i] = linear_model.cost_(y, y_hat)
        plt.plot(thetas1, y_cost, label="$J(θ_0=%d, θ_1)$" % t0)

    plt.legend()
    plt.show()

def plot2graphs(x: np.ndarray, y: np.ndarray) -> None:
    linear_model = MyLR(np.array([[89.0], [-8]]), max_iter=500)

    flag = 3
    if flag & 1:
        linear_model.fit_(x, y)
        y_hat = linear_model.predict_(x)
        plot_regression(x, y, y_hat)
    if flag & 2:
        plot_cost(x, y)

if __name__ == "__main__":
    data = pd.read_csv("../resources/are_blue_pills_magics.csv")
    Xpill = np.array(data["Micrograms"]).reshape(-1,1)
    Yscore = np.array(data["Score"]).reshape(-1,1)

    if False:
        linear_model1 = MyLR(np.array([[89.0], [-8]]))
        linear_model2 = MyLR(np.array([[89.0], [-6]]))

        Y_model1 = linear_model1.predict_(Xpill)
        Y_model2 = linear_model2.predict_(Xpill)

        print("model 1") # 57.603042857142825
        print(linear_model1.mse_(Yscore, Y_model1))
        print(mean_squared_error(Yscore, Y_model1))

        print("\nmodel 2") # 232.16344285714285
        print(linear_model2.mse_(Yscore, Y_model2))
        print(mean_squared_error(Yscore, Y_model2))

    plot2graphs(Xpill, Yscore)
