# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_train.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 23:20:23 by mli               #+#    #+#              #
#    Updated: 2020/12/23 23:51:41 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR

def compare_polynomials(x: np.ndarray, y: np.ndarray, i: int) -> None:
    theta = [2.5] * (x.shape[1] + 1)
    alpha = 1e-8
    max_iter = int(1e+6)

    linear_model = MyLR(theta, alpha, max_iter)

    linear_model.fit_(x, y)
    y_hat = linear_model.predict_(x)
    this_cost = linear_model.cost_(y, y_hat)

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
        if i == 5:
            break

    # Really long...
    """
        x:
    cost:
        775.052944158059
    theta:
    [[2.84125035]
    [3.59086108]]

        x ** 2:
    cost:
        706.7481504704375
    theta:
    [[2.64617435]
    [2.5089702 ]
    [0.7592692 ]]

        x ** 3:
    cost:
        545.921156358857
    theta:
    [[ 2.68308089]
    [ 2.79528699]
    [ 2.68942942]
    [-0.355095  ]]

        x ** 4:
    cost:
        470.82920350290914
    theta:
    [[ 2.59177766]
    [ 2.54099006]
    [ 2.22641474]
    [ 1.07002996]
    [-0.22255799]]

        x ** 5:
    cost:
        408.50749922874644
    theta:
    [[ 2.61465462]
    [ 2.62654902]
    [ 2.51714341]
    [ 1.807409  ]
    [-0.6292243 ]
    [ 0.04538613]]
    """

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
