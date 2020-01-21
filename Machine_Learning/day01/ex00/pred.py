# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pred.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/21 15:32:50 by mli               #+#    #+#              #
#    Updated: 2020/01/21 18:26:42 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

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

"""Description:
        Prediction of output using the hypothesis function (linear model).

    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of features + 1, 1).
        X: has to be a numpy.ndarray, a matrix of dimension (number of
    training examples, number of features).

    Returns:
        pred: numpy.ndarray, a vector of dimension (number of the training examples, 1).
        None if X does not match the dimension of theta.

    Raises:
        This function should not raise any Exception.
"""


'''
X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
print(predict_(theta1, X1))

X2 = np.array([[1], [2], [3], [5], [8]])
theta2 = np.array([[2.]])
print(predict_(theta2, X2))

X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta3 = np.array([[0.05], [1.], [1.], [1.]])
print(predict_(theta3, X3))
'''
