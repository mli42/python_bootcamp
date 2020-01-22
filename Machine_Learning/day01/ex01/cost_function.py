# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cost_function.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/21 22:36:40 by mli               #+#    #+#              #
#    Updated: 2020/01/21 23:29:17 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def mean_zip3f(x, y, f):
    res = float(0)
    for nb1, nb2 in zip(x, y):
        res += f(nb1, nb2)
    return (res / len(y))

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

# BEGIN

def cost_elem_(theta, X, Y):
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

def cost_(theta, X, Y):
    shape_x = np.shape(X)
    shape_y = np.shape(Y)
    shape_th = np.shape(theta)
    if (shape_x[1] != shape_th[0] - 1 or shape_x[0] != shape_y[0]):
        return (None)
    pred = predict_(theta, X)
    f = lambda x, y : (x - y) ** 2
    return (float(mean_zip3f(pred, Y, f)) / 2)


'''
X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
Y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
print(cost_elem_(theta1, X1, Y1))
print(cost_(theta1, X1, Y1))

X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
Y2 = np.array([[19.], [42.], [67.], [93.]])
print(cost_elem_(theta2, X2, Y2))
print(cost_(theta2, X2, Y2))
'''


"""Description: cost_elem_
        Calculates all the elements (0.5 / M) *(y_pred - y)^2 of the cost function.
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
        X: has to be a numpy.ndarray, a matrix of dimension (number of training examples, number of features).
    Returns:
        J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
        None if there is a dimension matching problem between X, Y or theta.
"""

"""Description: cost_
        Calculates the value of cost function.
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
        X: has to be a numpy.ndarray, a vector of dimension (number of training examples, number of features).
    Returns:
        J_value : has to be a float.
        None if X does not match the dimension of theta.
"""
