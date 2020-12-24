# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_spliter.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/24 18:26:00 by mli               #+#    #+#              #
#    Updated: 2020/12/24 23:09:19 by mli              ###   ########.fr        #
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
    Raises:
      This function should not raise any Exception.
    """
    if x.shape[0] != y.shape[0]:
        return None
    m = x.shape[0]
    delim = int(m * proportion)
    concatenated = np.concatenate((x, y), 1)
    np.random.shuffle(concatenated)
    x, y = concatenated[..., :-1], concatenated[..., -1:]
    x_train, x_test, y_train, y_test = x[:delim], x[delim:], y[:delim], y[delim:]
    return (x_train, x_test, y_train, y_test)

if __name__ == "__main__":
    x1 = np.array([1, 42, 300, 10, 59]).reshape(-1, 1)
    y = np.array([0,1,0,1,0]).reshape(-1, 1)

    # Example 1:
    print(data_spliter(x1, y, 0.8))
    # Output:
    #(array([  1,  59,  42, 300]), array([10]), array([0, 0, 0, 1]), array([1]))

    # Example 2:
    print(data_spliter(x1, y, 0.5))
    # Output:
    #(array([59, 10]), array([  1, 300,  42]), array([0, 1]), array([0, 1, 0]))

    x2 = np.array([ [  1,  42],
                    [300,  10],
                    [ 59,   1],
                    [300,  59],
                    [ 10,  42]])

    # Example 3:
    print(data_spliter(x2, y, 0.8))
    # Output:
    """
    (array([[10,  42],
            [300,  59],
            [59,   1],
            [300,  10]]),
    array([[1, 42]]),
    array([0, 1, 0, 1]),
    array([0]))
    """

    # Example 4:
    print(data_spliter(x2, y, 0.5))
    # Output:
    """
    array([[59,  1],
           [10, 42]])
    array([[300,  10],
           [300,  59],
           [ 1,   42]])
    array([0, 0])
    array([1, 1, 0]))
    """
