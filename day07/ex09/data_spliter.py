# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_spliter.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/24 18:26:00 by mli               #+#    #+#              #
#    Updated: 2022/09/16 16:43:27 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def data_spliter(x: np.ndarray, y: np.ndarray, proportion: float) -> tuple:
    """Shuffles and splits the dataset (given by x and y) into a training and a
    test set, while respecting the given proportion of examples to be kept in the traning set.
    Args:
        x: has to be an numpy.ndarray, a matrix of dimension m * n.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        proportion: has to be a float, the proportion of the dataset that will
        be assigned to the training set.
    Returns:
        (x_train, x_test, y_train, y_test) as a tuple of numpy.ndarray
        None if x or y is an empty numpy.ndarray.
        None if x and y do not share compatible dimensions.
        None if x, y or proportion is not of expected type.
    Raises:
        This function should not raise any Exception.
    """
    if (
        not all([
            isinstance(obj, np.ndarray)
            and obj.dtype.kind in 'iuf'
            and len(obj.shape) == 2
            and obj.size != 0
            for obj in (x, y)])
        or x.shape[0] != y.shape[0]
        or y.shape[1] != 1
        or not isinstance(proportion, float)
        or not (proportion > 0 and proportion < 1)
    ):
        return None
    delim = int(x.shape[0] * proportion)
    concatenated = np.concatenate((x, y), 1)

    np.random.shuffle(concatenated)
    x, y = concatenated[..., :-1], concatenated[..., -1:]
    x_train, x_test, y_train, y_test = x[:delim], x[delim:], y[:delim], y[delim:]
    return (x_train, x_test, y_train, y_test)
