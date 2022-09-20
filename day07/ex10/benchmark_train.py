# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    benchmark_train.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/20 11:33:07 by mli               #+#    #+#              #
#    Updated: 2022/09/20 17:50:36 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import numpy as np
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
from data_spliter import data_spliter
from typing import Dict


def main():
    try:
        df = pd.read_csv("../resources/space_avocado.csv")
        df.drop('Unnamed: 0', axis=1, inplace=True)
        if len(df) < 1 or list(df.keys()) != ['weight', 'prod_distance', 'time_delivery', 'target']:
            raise Exception('File corrupted')
    except Exception as e:
        exit(e)
    Y_LABEL = "target"
    X_LABEL = df.columns.difference([Y_LABEL]).tolist()
    x = df.drop(Y_LABEL, axis=1).to_numpy()
    y = df[Y_LABEL].to_numpy().reshape(-1, 1)

    RANGE = range(1, 5)
    for power_weight in RANGE:
        for power_dist in RANGE:
            for power_time in RANGE:
                print(f"### Training: {power_weight = } {power_dist = } {power_time = }")
                new_x = np.concatenate(
                    [add_polynomial_features(x[:, i].reshape(-1, 1), power)
                        for i, power in enumerate((power_weight, power_dist, power_time))],
                    axis=1
                )

                x_train, x_test, y_train, y_test = data_spliter(new_x, y, 0.8)

                mylr = MyLR(
                    thetas=np.ones((new_x.shape[1] + 1, 1)),
                    alpha=3e-7,
                    max_iter=int(1e4)
                )

                mylr.fit_(x_train, y_train)

                print(mylr.thetas)
                return



if __name__ == "__main__":
    main()
