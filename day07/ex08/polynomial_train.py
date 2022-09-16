# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_train.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 23:20:23 by mli               #+#    #+#              #
#    Updated: 2022/09/15 18:02:24 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from typing import Dict


def train_model(x: np.ndarray, y: np.ndarray, lr_config: Dict):
    linear_model = MyLR(
        thetas=np.array(lr_config["theta"]),
        alpha=lr_config["alpha"],
        max_iter=int(lr_config["max_iter"])
    )
    linear_model.fit_(x, y)
    return linear_model


def plot_score(linear_model: MyLR, x: np.ndarray, y: np.ndarray, power: int, score_ax: plt.Subplot) -> None:
    y_hat = linear_model.predict_(x)
    current_mse = linear_model.mse_(y, y_hat)

    print(f"POWER: {power}; {current_mse = }")
    print(f"Thetas:\n{linear_model.thetas}")
    score_ax.bar(power, current_mse, label="$%d_{th} cost: %.3f$" %(power, current_mse))


def plot_model(linear_model: MyLR, y: np.ndarray, power: int, model_ax: plt.Subplot) -> None:
    PACE = 0.1
    continuous_x = np.arange(1, 7 + PACE, PACE).reshape(-1, 1)
    x = add_polynomial_features(continuous_x, power)
    y_hat = linear_model.predict_(x)

    model_ax.plot(continuous_x, y_hat, label="$%d_{th} curve$" %power)


def main():
    try:
        df = pd.read_csv("../resources/are_blue_pills_magics.csv")
        if len(df) < 1 or list(df.keys()) != ['Patient', 'Micrograms', 'Score']:
            raise Exception('File corrupted')
    except Exception as e:
        exit(e)
    df = df.drop("Patient", axis=1)
    predicting_feature = "Score"
    x = df.drop(predicting_feature, axis=1).to_numpy()
    y = df[predicting_feature].to_numpy().reshape(-1, 1)

    score_fig, score_ax = plt.subplots()
    score_ax.set_title("MSE in function of polynomial's degree")
    score_ax.set_xlabel("x degree")
    score_ax.set_ylabel("MSE")
    score_ax.grid()

    model_fig, model_ax = plt.subplots()
    model_ax.set_title("Score depending on taken blue pills (Micrograms)")
    model_ax.set_xlabel("Micrograms")
    model_ax.set_ylabel("Score")
    model_ax.grid()

    model_ax.plot(x, y, "o", label="$S_{true}$")

    createConfig = lambda theta, alpha, max_iter: {"theta": theta, "alpha": alpha, "max_iter": max_iter}
    lr_configs = (
        createConfig([[1], [1]], 1e-2, 1e5),
        createConfig([[1], [1], [1]], 1e-3, 1e5),
        createConfig([[1], [1], [1], [1]], 1e-5, 1e6),
        createConfig([[-20],[ 160],[ -80],[ 10],[ -1]], 1e-6, 1e6),
        createConfig([[1140],[ -1850],[ 1110],[ -305],[ 40],[ -2]], 1e-8, 1e6),
        createConfig([[9110],[ -18015],[ 13400],[ -4935],[ 966],[ -96.4],[ 3.86]], 1e-9, 1e6),
    )

    for i, lr_config in enumerate(lr_configs, start=1):
        new_x = add_polynomial_features(x, i)

        print(f"Training #{i} model...")
        linear_model = train_model(new_x, y, lr_config)
        plot_score(linear_model, new_x, y, i, score_ax)
        plot_model(linear_model, y, i, model_ax)

    score_ax.legend()
    model_ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
