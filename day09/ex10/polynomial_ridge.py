# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_ridge.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/02 22:41:50 by mli               #+#    #+#              #
#    Updated: 2021/01/02 23:54:18 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mylinearregression import MyLinearRegression as MyLR
from ridge import MyRidge as MyRR
from polynomial_model_extended import add_polynomial_features
from data_spliter import data_spliter


def compare_models(x: np.ndarray, y: np.ndarray, lambda_: float) -> None:
    theta = [0.5] * (x.shape[1] + 1)
    alpha = 1e-15
    max_iter = int(3e+5)
    linear_model = MyRR(theta, alpha, max_iter)

    x_train, x_test, y_train, y_test = data_spliter(x, y, 0.6)

    linear_model.fit_(x_train, y_train)
    y_hat = linear_model.predict_(x_test)
    this_mse = linear_model.mse_(y_test, y_hat)

    print("lambda: %.1f | mse: %.3e" %(lambda_, this_mse))
    print("theta:\n", linear_model.thetas)
    plt.bar(lambda_, this_mse, width=3e-2, label="$%.1f_{\\lambda}$ mse: %.2e" %(lambda_, this_mse))

def main():
    #Age,Thrust_power,Terameters,Sell_price
    data = pd.read_csv("../resources/spacecraft_data.csv")
    predicting_feature = "Sell_price"

    x = np.array(data.drop(predicting_feature, axis=1))
    y = np.array(data[predicting_feature]).reshape(-1, 1)
    new_x = add_polynomial_features(x, 3)

    plt.title("Cost in function of $\\lambda$ value")
    plt.xlabel("$\\lambda$ value")
    plt.ylabel("Mean Squared Error (MSE)")
    plt.grid()

    for lambda_ in np.arange(0, 1, 0.1):
        compare_models(new_x, y, lambda_)
        #if lambda_ >= 0.7:
        #    break

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
