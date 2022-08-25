# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    z_score.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/21 18:30:08 by mli               #+#    #+#              #
#    Updated: 2022/08/25 13:15:32 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


def zscore(x: np.ndarray) -> np.ndarray:
    """Computes the normalized version of a non-empty numpy.ndarray using the z-score standardization.
    Args:
        x: has to be an numpy.ndarray, a vector.
    Returns:
        x' as a numpy.ndarray.
        None if x is an empty numpy.ndarray.
    Raises:
        This function shouldn't raise any Exception.
    """
    if not (
        isinstance(x, np.ndarray)
        and x.dtype.kind in 'iuf'
        and x.shape in [(x.size, ), (x.size, 1)]
        and x.size != 0
    ):
        return None
    mean = np.sum(x) / x.size
    std = (sum([(x_elem - mean) ** 2 for x_elem in x]) / x.size) ** .5
    res = (x - mean) / std
    return res
