# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_model.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/20 18:27:27 by mli               #+#    #+#              #
#    Updated: 2022/08/24 16:30:29 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.metrics import mean_squared_error
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
    plt.xlabel(r"$\theta_1$")
    plt.ylabel("cost function J$(\\theta_0, \\theta_1)$")
    plt.grid()

    npoints = 100
    thetas_0 = np.linspace(80, 100, 6)
    thetas_1 = np.linspace(-15, -4, npoints)
    linear_model = MyLR(np.array([[0], [0]]))
    for t0 in thetas_0:
        linear_model.thetas[0][0] = t0

        y_cost = [0] * npoints
        for i, t1 in enumerate(thetas_1):
            linear_model.thetas[1][0] = t1
            y_hat = linear_model.predict_(x)
            y_cost[i] = linear_model.mse_(y, y_hat)
        plt.plot(thetas_1, y_cost, label=f"J$(\\theta_0={t0}, \\theta_1)$")

    plt.ylim([10, 150])
    plt.legend()
    plt.show()


def plotting(x: np.ndarray, y: np.ndarray, flag: int = 3) -> None:
    if flag & 1:
        linear_model = MyLR(np.array([[.0], [.0]]), alpha=0.01, max_iter=10_000)

        np.set_printoptions(linewidth=np.inf)
        print(f'Before training: {linear_model.thetas = }')
        linear_model.fit_(x, y)
        print(f'After training: {linear_model.thetas = }')
        y_hat = linear_model.predict_(x)
        plot_regression(x, y, y_hat)
    if flag & 2:
        plot_cost(x, y)


if __name__ == "__main__":
    try:
        df = pd.read_csv("../resources/are_blue_pills_magics.csv")
        if list(df.keys()) != ["Patient", "Micrograms", "Score"] or len(df) < 1:
            raise Exception('File corrupted')
    except Exception as e:
        exit(e)

    Xpill = df["Micrograms"].to_numpy().reshape(-1,1)
    Yscore = df["Score"].to_numpy().reshape(-1,1)

    linear_model1 = MyLR(np.array([[89.0], [-8]]))
    linear_model2 = MyLR(np.array([[89.0], [-6]]))

    Y_model1 = linear_model1.predict_(Xpill)
    Y_model2 = linear_model2.predict_(Xpill)

    print("model 1") # 57.603042857142825
    print(linear_model1.mse_(Yscore, Y_model1))
    # print(mean_squared_error(Yscore, Y_model1))

    print("\nmodel 2") # 232.16344285714285
    print(linear_model2.mse_(Yscore, Y_model2))
    # print(mean_squared_error(Yscore, Y_model2))

    plotting(Xpill, Yscore)
