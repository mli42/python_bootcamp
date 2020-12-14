# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cost.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/14 16:11:04 by mli               #+#    #+#              #
#    Updated: 2020/12/14 18:55:32 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from prediction import simple_predict as predict

def cost_elem_(y: np.ndarray, y_hat: np.ndarray) -> np.ndarray:
    """
    Description:
        Calculates all the elements (1/2*M)*(y_pred - y)^2 of the cost function.
    Args:
        y: has to be an numpy.ndarray, a vector.
        y_hat: has to be an numpy.ndarray, a vector.
    Returns:
        J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
        None if there is a dimension matching problem between X, Y or theta.
    Raises:
        This function should not raise any Exception.
    """
    if y.shape != y_hat.shape:
        return None
    res = (y_hat - y) ** 2 / (2 * y.shape[0])
    return res

def cost_(y: np.ndarray, y_hat: np.ndarray) -> float:
    """
    Description:
        Calculates the value of cost function.
    Args:
        y: has to be an numpy.ndarray, a vector.
        y_hat: has to be an numpy.ndarray, a vector.
    Returns:
        J_value : has to be a float.
        None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    j_elem = cost_elem_(y, y_hat)
    if j_elem is None:
        return None
    return sum(j_elem)[0]

if __name__ == "__main__":
    x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    y_hat1 = predict(x1, theta1)
    y1 = np.array([[2.], [7.], [12.], [17.], [22.]])

    x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
    theta2 = np.array([[0.05], [1.], [1.], [1.]])
    y_hat2 = predict(x2, theta2)
    y2 = np.array([[19.], [42.], [67.], [93.]])

    x3 = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(7, 1)
    theta3 = np.array([[0.], [1.]])
    y_hat3 = predict(x3, theta3)
    y3 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(7, 1)

    if True:
        flag = 63
        if flag & 1:
            print("# Example 1:")
            print(cost_elem_(y1, y_hat1))
            # Output: array([[0.], [0.1], [0.4], [0.9], [1.6]])
        if flag & 2:
            print("# Example 2:")
            print(cost_(y1, y_hat1))
            # Output: 3.0
        if flag & 4:
            print("# Example 3:")
            print(cost_elem_(y2, y_hat2))
            # Output: array([[1.3203125], [0.7503125], [0.0153125], [2.1528125]])
        if flag & 8:
            print("# Example 4:")
            print(cost_(y2, y_hat2))
            # Output: 4.238750000000004
        if flag & 16:
            print("# Example 5:")
            print(cost_(y3, y_hat3))
            # Output: 2.142857142857143
        if flag & 32:
            print("# Example 6:")
            print(cost_(y3, y3))
            # Output: 0.0
