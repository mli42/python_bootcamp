# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sigmoid.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/26 15:33:44 by mli               #+#    #+#              #
#    Updated: 2020/12/26 15:47:05 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def sigmoid_(x: np.ndarray) -> np.ndarray:
    """
    Compute the sigmoid of a vector.
    Args:
        x: has to be an numpy.ndarray, a vector
    Returns:
        The sigmoid value as a numpy.ndarray.
        None if x is an empty numpy.ndarray.
    Raises:
        This function should not raise any Exception.
    """
    if x.size == 0:
        return None
    return 1 / (1 + np.exp(-x))

if __name__ == "__main__":
    # Example 1:
    x = np.array(-4)
    print(sigmoid_(x))
    # Output: array([0.01798620996209156])

    # Example 2:
    x = np.array(2)
    print(sigmoid_(x))
    # Output: array([0.8807970779778823])

    # Example 3:
    x = np.array([[-4], [2], [0]])
    print(sigmoid_(x))
    # Output: array([[0.01798620996209156], [0.8807970779778823], [0.5]])
