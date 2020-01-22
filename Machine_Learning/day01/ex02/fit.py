# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fit.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/21 23:34:26 by mli               #+#    #+#              #
#    Updated: 2020/01/22 14:22:26 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def vec_linear_mse(x, y, theta):
    res = np.dot(x, theta) - y
    res = np.dot(np.transpose(res), res)
    return (res / len(x))

def vec_gradient(x, y, theta):
    shape_x = np.shape(x)
    shape_y = np.shape(y)
    if (shape_x[0] != shape_y[0] or shape_x[1] != np.shape(theta)[0] or
            len(x) == 0 or len(y) == 0 or len(theta) == 0):
        return (None)
    res = np.dot(x, theta) - y
    res = np.dot(np.transpose(x), res) / len(x)
    return (res)

# BEGIN

def fit_(theta, X, Y, alpha, n_cycle):
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

"""Description:
        Performs a fit of Y(output) with respect to X.
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
        X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
        Y: has to be a numpy.ndarray, a vector of dimension (number of training examples, 1).
        alpha : un float positif
        n_cycle : un integer positif
    Returns:
        new_theta: numpy.ndarray, a vector of dimension (number of the features +1,1).
        None if there is a matching dimension problem.


        Les delta arrondis signifie que l’on prend la dérivée partielle
        le terme signifie que tu multiplies -alpha par la dérivée partielle suivant theta_j de la fonction J
"""

"""
def predict_(theta, X):
    shape_x = np.shape(X)
    shape_th = np.shape(theta)
    if (shape_x[1] != shape_th[0] - 1):
        return (None)
    new_X = []
    for i in range(len(X)):
        new_X.append((np.insert(X[i], 0, [1])))
    new_X = np.asarray(new_X)
    return (np.dot(new_X, theta))

X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
Y1 = np.array([[2.], [6.], [10.], [14.], [18.]])
theta1 = np.array([[1.], [1.]])
n_theta = (fit_(theta1, X1, Y1, alpha = 0.01, n_cycle=2000))
print(n_theta)
print(predict_(n_theta, X1))

X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
Y2 = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta2 = np.array([[42.], [1.], [1.], [1.]])
n_theta = fit_(theta2, X2, Y2, alpha = 0.0005, n_cycle=42000)
print(n_theta)
print(predict_(n_theta, X2))
"""
