# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_train.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 23:20:23 by mli               #+#    #+#              #
#    Updated: 2020/12/24 23:14:22 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter

def compare_polynomials(x: np.ndarray, y: np.ndarray, i: int) -> None:
    theta = [2.5] * (x.shape[1] + 1)
    alpha = 1e-8
    max_iter = int(1e+6)
    linear_model = MyLR(theta, alpha, max_iter)

    x_train, x_test, y_train, y_test = data_spliter(x, y, 0.6)

    linear_model.fit_(x_train, y_train)
    y_hat = linear_model.predict_(x_test)
    this_cost = linear_model.cost_(y_test, y_hat)

    print(i, this_cost)
    print(linear_model.thetas)
    plt.bar(i, this_cost, label="$%d_{th} cost: %.3f$" %(i, this_cost))

def main():
    data = pd.read_csv("../resources/are_blue_pills_magics.csv")
    data = data.drop("Patient", axis=1)
    predicting_feature = "Score"
    x = np.array(data.drop(predicting_feature, axis=1))
    y = np.array(data[predicting_feature]).reshape(-1, 1)

    plt.title("cost in function of polynomial's degree")
    plt.xlabel("x degree")
    plt.ylabel("cost")
    plt.grid()

    for i in range(1, 11):
        new_x = add_polynomial_features(x, i)
        compare_polynomials(new_x, y, i)
        if i == 4:
            break

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
