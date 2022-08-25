# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    minmax.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/21 18:30:08 by mli               #+#    #+#              #
#    Updated: 2022/08/25 13:31:55 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def minmax(x: np.ndarray) -> np.ndarray:
    """Computes the normalized version of a non-empty numpy.ndarray using the min-max standardization.
        Args:
            x: has to be an numpy.ndarray, a vector.
        Returns:
            x' as a numpy.ndarray.
            None if x is a non-empty numpy.ndarray.
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
    x_min = np.min(x)
    x_max = np.max(x)
    x_span = x_max - x_min
    res = (x - x_min) / x_span
    return res.reshape((-1,))
