# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TinyStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/11 14:51:00 by mli               #+#    #+#              #
#    Updated: 2022/08/11 16:34:58 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class TinyStatistician:

    def __guard(funct):
        def inner(array, *args, **kwargs):
            # Is a numpy array with kind of integer/unsigned/floating
            if isinstance(array, np.ndarray) and array.dtype.kind in 'iuf':
                array = array.flatten().tolist()
            if not isinstance(array, list) or len(array) < 1 or \
                not all([isinstance(obj, (int, float)) for obj in array]):
                return None
            if funct.__name__ == 'percentile' and \
                (len(args) != 1 or not isinstance(args[0], int)):
                return None
            return_value = funct(array, *args, **kwargs)
            return return_value
        return inner

    @staticmethod
    @__guard
    def mean(x: list) -> float:
        return sum(x) / len(x)

    @staticmethod
    @__guard
    def percentile(x: list, percentile: int) -> float:
        x = sorted(x)
        m = len(x) - 1
        index: float = m * percentile / 100

        if index.is_integer():
            return x[int(index)]
        floored, ceiled = int(index), int(index) + 1
        return x[floored] * (ceiled - index) + x[ceiled] * (index - floored)

    @staticmethod
    @__guard
    def median(x: list) -> float:
        return TinyStatistician.percentile(x, 50)

    @staticmethod
    @__guard
    def quartile(x: list) -> float:
        return [TinyStatistician.percentile(x, percentile) for percentile in (25, 75)]

    @staticmethod
    @__guard
    def var(x: list) -> float:
        res = 0
        m = len(x) - 1
        mean = TinyStatistician.mean(x)

        for elem in x:
            res += (elem - mean) ** 2
        return res / m

    @staticmethod
    @__guard
    def std(x: list) -> float:
        return TinyStatistician.var(x) ** 0.5
