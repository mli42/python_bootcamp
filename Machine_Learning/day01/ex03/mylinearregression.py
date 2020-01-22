# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mylinearregression.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/22 14:32:22 by mli               #+#    #+#              #
#    Updated: 2020/01/22 14:47:59 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class MyLinearRegression():
"""Description:
        My personnal linear regression class to fit like a boss.
"""
    def __init__(self, theta):
        try:
            self.theta = np.asarray(theta)
            self.th_shape = np.shape(theta)
        except:
            exit(print("Theta is a list or numpy array"))
        if (self.th_shape[1] != 1):
            exit(print("Theta shape wrong"))

    def predict_(self, X):
        theta = self.theta
        shape_x = np.shape(X)
        shape_th = np.shape(theta)
        if (shape_x[1] != shape_th[0] - 1):
            return (None)
        new_X = []
        for i in range(len(X)):
            new_X.append((np.insert(X[i], 0, [1])))
        new_X = np.asarray(new_X)
        return (np.dot(new_X, theta))

    @staticmethod
    def mean_zip3f(x, y, f):
        res = float(0)
        for nb1, nb2 in zip(x, y):
            res += f(nb1, nb2)
        return (res / len(y))

    def cost_elem_(self, X, Y):
        theta = self.theta
        shape_x = np.shape(X)
        shape_y = np.shape(Y)
        shape_th = np.shape(theta)
        if (shape_x[1] != shape_th[0] - 1 or shape_x[0] != shape_y[0]):
            return (None)
        res = []
        pred = predict_(theta, X)
        f = lambda x, y : (x - y) ** 2
        for nb1, nb2 in zip(pred, Y):
            res.append(f(nb1, nb2))
        return (np.asarray(res) / (shape_y[0] * 2))

    def cost_(self, X, Y):
        theta = self.theta
        shape_x = np.shape(X)
        shape_y = np.shape(Y)
        shape_th = np.shape(theta)
        if (shape_x[1] != shape_th[0] - 1 or shape_x[0] != shape_y[0]):
            return (None)
        pred = predict_(theta, X)
        f = lambda x, y : (x - y) ** 2
        return (float(mean_zip3f(pred, Y, f)) / 2)

    @staticmethod
    def vec_linear_mse(x, y, theta):
        res = np.dot(x, theta) - y
        res = np.dot(np.transpose(res), res)
        return (res / len(x))

    @staticmethod
    def vec_gradient(x, y, theta):
        shape_x = np.shape(x)
        shape_y = np.shape(y)
        if (shape_x[0] != shape_y[0] or shape_x[1] != np.shape(theta)[0] or
                len(x) == 0 or len(y) == 0 or len(theta) == 0):
            return (None)
        res = np.dot(x, theta) - y
        res = np.dot(np.transpose(x), res) / len(x)
        return (res)

    def fit_(self, X, Y, alpha, n_cycle):
        theta = self.theta
        shape_x = np.shape(X)
        shape_y = np.shape(Y)
        shape_th = np.shape(theta)
        if (shape_x[1] != shape_th[0] - 1 or shape_x[0] != shape_y[0] or alpha <= 0.0 or n_cycle <= 0):
            return (None)
        new_X = []
        for i in range(len(X)):
            new_X.append((np.insert(X[i], 0, [1])))
        new_X = np.asarray(new_X)
        for i in range(n_cycle):
            theta -= alpha * vec_gradient(new_X, Y, theta)
        return (theta)
