# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multivariate_linear_model.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 17:43:14 by mli               #+#    #+#              #
#    Updated: 2020/12/22 22:08:27 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mylinearregression import MyLinearRegression as MyLR

def plot_ulr(x: np.ndarray, y: np.ndarray, y_hat: np.ndarray, feature: str,
             colors: tuple, new_theta: np.ndarray, lr_model: MyLR):
    plt.xlabel(f"x: {feature}")
    plt.ylabel("y: sell price (in keuros)")
    plt.grid()

    plt.plot(x, y, "o", color=colors[0], label="Sell price")
    plt.plot(x, y_hat, "o", color=colors[1], label="Predicted sell price", markersize=3)

    thstr = ["%.3f" %x for x in new_theta.flatten()]
    thstr = ", ".join(thstr)
    plt.title("$\\theta: (%s); mse: %.3f$" %
            (thstr, lr_model.mse_(y, y_hat)))
    plt.legend()
    plt.show()

def univariate_lr(data: pd.DataFrame, feature: str, colors: tuple,
      theta: list = [0, 0], alpha: float = 0.001, max_iter: int = 1000) -> None:
    linear_model = MyLR(theta, alpha, max_iter)
    x = np.array(data[feature]).reshape(-1, 1)
    y = np.array(data["Sell_price"]).reshape(-1, 1)
    linear_model.fit_(x, y)
    y_hat = linear_model.predict_(x)
    new_theta = linear_model.thetas

    plot_ulr(x, y, y_hat, feature.lower(), colors, new_theta, linear_model)

def multivariate_lr(data: pd.DataFrame,
                    theta: np.ndarray, alpha: float, max_iter: int) -> None:
    linear_model = MyLR(theta, alpha, max_iter)
    predicting_feature = "Sell_price"
    x = np.array(data.drop(predicting_feature, axis=1))
    y = np.array(data[predicting_feature]).reshape(-1, 1)

    linear_model.fit_(x, y)
    y_hat = linear_model.predict_(x)
    new_theta = linear_model.thetas
    #print("new theta:", new_theta, sep='\n')
    #print("MyLR.mse_(y, y_hat):", linear_model.mse_(y, y_hat))

    #Age, Thrust_power, Terameters
    plot_ulr(x[..., 0], y, y_hat, "age",
             ("darkblue", "dodgerblue"), new_theta, linear_model)
    plot_ulr(x[..., 1], y, y_hat, "thrust power",
             ("g", "lime"), new_theta, linear_model)
    plot_ulr(x[..., 2], y, y_hat, "terameters",
             ("darkviolet", "violet"), new_theta, linear_model)

if __name__ == "__main__":
    data = pd.read_csv("../resources/spacecraft_data.csv")

    # 1. Univariate
    univariate_lr(data, "Age", colors=("darkblue", "dodgerblue"), theta=[650, -15], alpha=0.01)
    univariate_lr(data, "Thrust_power", colors=("g", "lime"), theta=[20, 5], alpha=0.0001)
    univariate_lr(data, "Terameters", colors=("darkviolet", "violet"), theta=[750, -3], alpha=0.0002)

    # 2. Multiveriate
    multivariate_lr(data, theta=[385.67, -24.3617, 5.6672, -2.668],
                    alpha=1e-6, max_iter=100000)

    if False:
        X = np.array(data['Age']).reshape(-1, 1)
        Y = np.array(data['Sell_price']).reshape(-1, 1)
        myLR_age = MyLR([[1000.0], [-1.0]], alpha=2.5e-5, max_iter=100000)
        myLR_age.fit_(X, Y)
        RMSE_age = myLR_age.mse_(X, Y)
        print(RMSE_age)  # 57636.77729...
