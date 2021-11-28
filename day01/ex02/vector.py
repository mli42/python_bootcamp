# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 17:45:09 by mli               #+#    #+#              #
#    Updated: 2021/11/28 22:16:34 by mli              ###   ########.fr        #
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
        return (f"Vector({self.values})")

    def get_value(self, index: int) -> float or int:
        if self.shape[0] < index and self.shape[1] < index:
            raise ValueError("index out of bound")
        if isinstance(self.values[index], float):
            return self.values[index]
        return self.values[index][0]

    def __add__(self, other):
        if not (isinstance(other, Vector) and (other.shape == self.shape)):
            raise ValueError("Addition only between vectors of same shape")
        res = []
        if self.shape == (1, 1):
            res.append(self.get_value(0) + other.get_value(0))
        elif self.shape[0] > 1:
            for a, b in zip(self.values, other.values):
                res.append([a[0] + b[0]])
        else: # self.shape[1] > 1
            for a, b in zip(self.values, other.values):
                res.append(a + b)
        return (res)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not (isinstance(other, Vector) and (other.shape == self.shape)):
            raise ValueError("Subtraction only between vectors of same shape")
        res = []
        if self.shape == (1, 1):
            res.append(self.get_value(0) - other.get_value(0))
        elif self.shape[0] > 1:
            for a, b in zip(self.values, other.values):
                res.append([a[0] - b[0]])
        else: # self.shape[1] > 1
            for a, b in zip(self.values, other.values):
                res.append(a - b)
        return (res)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        if not isinstance(other, (float, int)):
            raise ValueError("Truediv only with float/int")
        if float(other) == 0.0:
            raise ValueError("Cannot div by 0")
        res = []
        if self.shape == (1, 1):
            res.append(self.get_value(0) / other)
        elif self.shape[0] > 1:
            for a in self.values:
                res.append([a[0] / other])
        else: # self.shape[1] > 1
            for a in self.values:
                res.append(a / other)
        return (res)

    def __rtruediv__(self, other):
        raise ValueError('A scalar cannot be divided by a Vector.')

    def __mul__(self, other):
        if not isinstance(other, (float, int)):
            raise ValueError("Multiplication only with float/int")
        res = []
        if self.shape == (1, 1):
            res.append(self.get_value(0) * other)
        elif self.shape[0] > 1:
            for a in self.values:
                res.append([a[0] * other])
        else: # self.shape[1] > 1
            for a in self.values:
                res.append(a * other)
        return (res)

    def __rmul__(self, other):
        return self.__mul__(other)

    def dot(self, other) -> float or int:
        if not (isinstance(other, Vector) and \
            (self.shape == other.shape or self.shape == other.shape[::-1])):
            raise ValueError("Vector.dot take a vector of same dimension")
        res = 0
        length = len(self.values)
        for i in range(length):
            res += self.get_value(i) * other.get_value(i)
        return res

    def T(self):
        res = []
        for x in self.values:
            if isinstance(x, float):
                res.append([x])
            else:
                res.append(x[0])
        return Vector(res)

'''
Following are differences (repr vs str):
Repr’s goal is to be unambiguous and str’s is to be readable.

str() is used for creating output for end user
(a representation that is useful for printing the object).

While repr() is mainly used for debugging and development.
(a representation that has all information about the abject)
'''
