# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multivariate_linear_model.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 17:43:14 by mli               #+#    #+#              #
#    Updated: 2022/09/12 15:15:37 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mylinearregression import MyLinearRegression as MyLR


def plot_ulr(x: np.ndarray, y: np.ndarray, y_hat: np.ndarray, xlabel: str,
        colors: tuple, lr_model: MyLR):
    plt.xlabel(f"x: {xlabel}")
    plt.ylabel("y: sell price (in keuros)")
    plt.grid()

    plt.plot(x, y, "o", color=colors[0], label="Sell price")
    plt.plot(x, y_hat, "o", color=colors[1], label="Predicted sell price", markersize=3)

    thetas = ", ".join([f"{x:.3f}" for x in lr_model.thetas.flatten()])
    thetas = f"[{thetas}]"
    mse = f"{lr_model.mse_(y, y_hat):.3f}"
    plt.title(f"$\\theta$: {thetas}; MSE: {mse}")
    plt.legend()
    print(f"{xlabel}: {thetas = }; {mse = }")
    plt.show()


def univariate_lr(df: pd.DataFrame, feature: str, colors: tuple,
        alpha: float, max_iter: int = 100_000) -> None:
    theta = np.array([[0], [0]])
    linear_model = MyLR(theta, alpha, max_iter)
    x = df[feature].to_numpy().reshape(-1, 1)
    y = df["Sell_price"].to_numpy().reshape(-1, 1)

    linear_model.fit_(x, y)
    y_hat = linear_model.predict_(x)

    plot_ulr(x, y, y_hat, feature.lower(), colors, linear_model)


def multivariate_lr(df: pd.DataFrame,
        theta: np.ndarray, alpha: float, max_iter: int) -> None:
    linear_model = MyLR(theta, alpha, max_iter)
    predicting_feature = "Sell_price"
    x = np.array(df.drop(predicting_feature, axis=1))
    y = np.array(df[predicting_feature]).reshape(-1, 1)

    linear_model.fit_(x, y)
    y_hat = linear_model.predict_(x)

    config = (
        ("age (in years)", ("darkblue", "dodgerblue")),
        ("thrust power (in 10Km/s)", ("g", "lime")),
        ("distance (in Tmeters)", ("darkviolet", "violet")),
    )
    for i, [xlabel, colors] in enumerate(config):
        plot_ulr(x[..., i], y, y_hat, xlabel, colors, linear_model)

if __name__ == "__main__":
    try:
        df = pd.read_csv("../resources/spacecraft_data.csv")
        if len(df) < 1 or list(df.keys()) != ['Age', 'Thrust_power', 'Terameters', 'Sell_price']:
            raise Exception('File corrupted')
    except Exception as e:
        exit(e)

    print("# 1. Univariate")
    univariate_lr(df, "Age", colors=("darkblue", "dodgerblue"), alpha=1e-2)
    univariate_lr(df, "Thrust_power", colors=("g", "lime"), alpha=1e-4)
    univariate_lr(df, "Terameters", colors=("darkviolet", "violet"), alpha=2e-4)

    print("# 2. Multiveriate")
    multivariate_lr(df, theta=np.zeros((4, 1)), alpha=3e-5, max_iter=100_000)
