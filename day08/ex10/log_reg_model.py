# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    log_reg_model.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/26 23:45:53 by mli               #+#    #+#              #
#    Updated: 2020/12/28 18:07:46 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import pandas as pd
from data_spliter import data_spliter
from my_logistic_regression import MyLogisticRegression as MyLR

def ofa(x: np.ndarray, y: np.ndarray, zipcode: float, x_test: np.ndarray, theta) -> np.ndarray:
    """ One For All
    Args:
        x (np.ndarray): shape(m * n)
        y (np.ndarray): shape(m * 1)
        zipcode (float): the one zipcode against the all
        theta: init value for theta
    Returns:
        np.ndarray: shape(m_2 * 1),
            percentage for each citizen of belonging to $zipcode planet
        None: if shapes doesn't match
    """
    if x.shape[0] != y.shape[0] or y.shape[1] != 1:
        return None
    y = (y[...] == zipcode)
    alpha = 3e-4
    max_iter = int(3e+5)
    lr_model = MyLR(theta, alpha, max_iter)
    lr_model.fit_(x, y)
    y_test_hat = lr_model.predict_(x_test)
    #print(lr_model.theta)
    return y_test_hat

def main():
    y_data = pd.read_csv("../resources/solar_system_census_planets.csv", index_col=0)
    x_data = pd.read_csv("../resources/solar_system_census.csv", index_col=0)
    y = np.array(y_data)
    x = np.array(x_data)

    zipcodes = [0, 1, 2, 3]
    thetas = ([[ 4.90348242], [-0.02999681], [-0.03250215], [ 2.40047782]],
              [[ 1.28802845], [-0.06179008], [ 0.01894334], [ 8.00000601]],
              [[-4.75798975], [-0.00574743], [ 0.09731946], [-4.55362614]],
              [[-2.20593027], [ 0.08724529], [-0.09877385], [-8.59898021]])

    x_train, x_test, y_train, y_test = data_spliter(x, y, 0.7)
    #print(x_train, x_test, y_train, y_test)

    ys_hat = [ofa(x_train, y_train, zipcode, x_test, theta)
              for zipcode, theta in zip(zipcodes, thetas)]
    ys_hat = np.concatenate(ys_hat, axis=1)

    """
    y_best = np.zeros(y_test.shape)
    for i in range(y_best.shape[0]):
        ith_hat = ys_hat[i]
        best_zipcode = np.where(ith_hat == np.amax(ith_hat))[0][0]
        y_best[i] = best_zipcode
    """
    y_best = np.argmax(ys_hat, axis=1).reshape(-1, 1)

    compare = np.concatenate((y_test, y_best), axis=1)
    compare = pd.DataFrame(compare.astype("int64"))
    print(compare)

    # Checking if prediction is right
    unique, counts = np.unique(y_best == y_test, return_counts=True)
    print(dict(zip(unique, counts)))

if __name__ == "__main__":
    main()
