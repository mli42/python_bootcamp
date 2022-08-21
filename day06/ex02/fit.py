# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fit.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/19 18:35:43 by mli               #+#    #+#              #
#    Updated: 2022/08/21 22:07:59 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from vec_gradient import simple_gradient as gradient

def fit_(x: np.ndarray, y: np.ndarray, theta: np.ndarray,
         alpha: float, max_iter: int) -> np.ndarray:
    """
    Description:
        Fits the model to the training dataset contained in x and y.
    Args:
        x: a vector of dimension m * 1: (number of training examples, 1).
        y: a vector of dimension m * 1: (number of training examples, 1).
        theta: a vector of dimension 2 * 1.
        alpha: has to be a float, the learning rate
        max_iter: has to be an int, the number of iterations done
    Returns:
        new_theta: numpy.ndarray, a vector of dimension 2 * 1.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exception.
    """
    if (
        not all([
            isinstance(obj, np.ndarray)
            and obj.dtype.kind in 'iuf'
            and obj.shape in [(obj.size,), (obj.size, 1)]
            for obj in (x, y, theta)])
        or not isinstance(alpha, (int, float))
        or not isinstance(max_iter, int)
        or theta.size != 2
        or x.size != y.size
    ):
        return None

    # Reshape parameters
    params = [x, y, theta]
    for i, elem in enumerate(params):
        if len(elem.shape) != 2:
            params[i] = elem.reshape(-1, 1)

    # Linear Gradient Descent
    theta = theta.astype("float64")
    for _ in range(max_iter):
        nabla = gradient(x, y, theta)
        theta -= alpha * nabla
    return theta
