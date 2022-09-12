# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_model.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/22 22:47:23 by mli               #+#    #+#              #
#    Updated: 2022/09/12 16:01:17 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def add_polynomial_features(x: np.ndarray, power: int) -> np.ndarray:
    """Add polynomial features to vector x by raising its values up to the power given in argument.
    Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        power: has to be an int, the power up to which the components of vector x are going to be raised.
    Returns:
        The matrix of polynomial features as a numpy.ndarray, of dimension m * n,
        containing the polynomial feature values for all training examples.
        None if x is an empty numpy.ndarray.
    Raises:
        This function should not raise any Exception.
    """
    if not (
        isinstance(x, np.ndarray)
        and x.dtype.kind in 'iuf'
        and x.shape == (x.size, 1)
        and isinstance(power, int)
        and power >= 1
    ):
        return None
    res = x
    for i in range(2, power + 1):
        raised = x ** i
        res = np.concatenate((res, raised), axis=1)
    return res
