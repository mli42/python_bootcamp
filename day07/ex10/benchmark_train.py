# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    benchmark_train.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/20 11:33:07 by mli               #+#    #+#              #
#    Updated: 2022/09/20 11:55:38 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import pandas as pd
import numpy as np
from polynomial_model import add_polynomial_features
from mylinearregression import MyLinearRegression as MyLR
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
    x = df.drop(Y_LABEL, axis=1).to_numpy()
    y = df[Y_LABEL].to_numpy().reshape(-1, 1)


if __name__ == "__main__":
    main()
