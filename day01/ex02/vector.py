# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 17:45:09 by mli               #+#    #+#              #
#    Updated: 2021/11/28 17:59:04 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# magic methods
from copy import deepcopy

class Vector:
    @staticmethod
    def check_shape_1_x(arr: list) -> bool:
        return all([isinstance(obj, float) for obj in arr])

    @staticmethod
    def check_shape_x_1(arr: list) -> bool:
        return all([isinstance(obj, list) and \
            len(obj) == 1 and isinstance(obj[0], float) \
            for obj in arr])

    def __init__(self, a):
        if isinstance(a, (list, int, range)) == False:
            raise ValueError("Vector inits with either list[float] / list[list[float]] / int / range")

        values = []
        shape = ()
        if (isinstance(a, list)):
            if self.check_shape_1_x(a):
                values = deepcopy(a)
                shape = (1, len(a))
            elif self.check_shape_x_1(a):
                values = deepcopy(a)
                shape = (len(a), 1)
            else:
                raise ValueError("Vector list shape incorrect")
        elif isinstance(a, (int, range)):
            # size & range constructor
            src_range = range(0, a) if isinstance(a, int) else a
            values = [[float(nb)] for nb in src_range]
            shape = (len(src_range), 1)
        else:
            raise Exception("Unexpected error")
        self.values = values
        self.shape = shape

    def __repr__(self) -> str:
        return (f"Values: {self.values} | Shape: {self.shape}")

    def __str__(self) -> str:
        return (str(self.values))

    def get_1x1_value(self) -> int:
        if self.shape != (1, 1):
            return 0
        if isinstance(self.values[0], float):
            return self.values[0]
        return self.values[0][0]

    def __add__(self, other):
        if not (isinstance(other, Vector) and (other.shape == self.shape)):
            raise ValueError("Addition only between vectors of same shape")
        res = []
        if self.shape == (1, 1):
            res.append(self.get_1x1_value() + other.get_1x1_value())
        elif self.shape[0] > 1:
            for a, b in zip(self.values, other.values):
                res.append([a[0] + b[0]])
        else: # self.shape[1] > 1
            for a, b in zip(self.values, other.values):
                res.append(a + b)
        return (res)

    def __radd__(self, other):
        return self.__add__(other)

'''
Following are differences (repr vs str):
Repr’s goal is to be unambiguous and str’s is to be readable.

str() is used for creating output for end user
(a representation that is useful for printing the object).

While repr() is mainly used for debugging and development.
(a representation that has all information about the abject)
'''
