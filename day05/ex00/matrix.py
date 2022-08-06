# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/07 18:36:21 by mli               #+#    #+#              #
#    Updated: 2022/08/06 18:43:02 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from copy import deepcopy
from typing import List, Tuple

class Matrix:

    @staticmethod
    def __check_shape(shape: Tuple) -> bool:
        """ Check if given parameter is a shape
        Args:
            shape (Tuple): should be (x, y)
        Returns:
            bool: True if is a shape, False otherwise
        """
        if not isinstance(shape, tuple) or len(shape) != 2:
            return False
        return all([isinstance(obj, int) for obj in shape])


    @staticmethod
    def __check_data_shape(data: List) -> Tuple or None:
        """ Check if given parameter has a correct data shape (x, y)
        Args:
            shape (Tuple): should be (x, y)
        Returns:
            Tuple: shape if the format is good
            None otherwise
        """
        rows, cols = 0, 0
        if not isinstance(data, list) or not all([isinstance(obj, list) for obj in data]):
            return None
        for i, row in enumerate(data):
            if not all([isinstance(obj, (int, float)) for obj in row]):
                return None
            if i == 0:
                cols = len(row)
            elif cols != len(row):
                return None
            rows += 1
        return (rows, cols)


    def __init__(self, param: List or Tuple[float, float]) -> None:
        """ Initialize the Matrix
        Args:
            param (List or Tuple):
                - List => elements of the matrix
                - Tuple => shape of the matrix, filled with zeros
        """
        self.constructor = type(self)
        potential_shape = self.__check_data_shape(param)
        if potential_shape is not None:
            self.data = deepcopy(param)
            self.shape = potential_shape
        elif self.__check_shape(param):
            self.shape = param
            self.data = [[0] * self.shape[1] for _ in range(self.shape[0])]
        else:
            raise ValueError("Incorrect initialization of Matrix")


    def T(self):
        transposed = self.constructor(self.shape[::-1])
        for j, rows in enumerate(self.data):
            for i, data in enumerate(rows):
                transposed.data[i][j] = data
        return transposed


    def __add__(self, other):
        # add : vectors and matrices, can have errors with vectors and matrices.
        if isinstance(other, Matrix) and self.shape != other.shape:
            return
        res = self.constructor(self.shape)
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                res.data[i][j] = self.data[i][j] + other.data[i][j]
        return res

    def __sub__(self, other):
        # sub : vectors and matrices, can have errors with vectors and matrices.
        if isinstance(other, Matrix) and self.shape != other.shape:
            return
        res = self.constructor(self.shape)
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                res.data[i][j] = self.data[i][j] - other.data[i][j]
        return res

    def __truediv__(self, other):
        # div : only scalars.
        if not isinstance(other, (int, float)):
            return
        res = self.constructor(self.shape)
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                res.data[i][j] = self.data[i][j] / other
        return res

    def __mul__(self, other):
        # mul : scalars, vectors and matrices , can have errors with vectors and matrices.
        # if we perform Matrix * Vector (dot product), return a Vector.
        res = None
        if isinstance(other, (int, float)):
            res = self.constructor(self.shape)
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    res.data[i][j] = self.data[i][j] * other
        elif isinstance(other, Matrix):
            common_len = self.shape[1]
            res = self.constructor((self.shape[0], other.shape[1]))
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    res.data[i][j] = sum([self.data[i][k] * other.data[k][j] for k in range(common_len)])
        return res

    def __radd__(self, other):
        return Matrix.__add__(self, other)
    def __rsub__(self, other):
        return Matrix.__sub__(self, other)
    def __rmul__(self, other):
        return Matrix.__mul__(self, other)
    def __rtruediv__(self, other):
        return Matrix.__truediv__(self, other)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"{self.constructor.__name__}({self.data})"


class Vector(Matrix):

    def __init__(self, param: List or Tuple[float, float]) -> None:
        """ Initialize the Vector
        Args:
            param (List or Tuple):
                - List => elements of the vector
                - Tuple => shape of the vector, filled with zeros
        """
        super().__init__(param)
        if self.shape[0] != 1 and self.shape[1] != 1:
            raise ValueError('Vector has incorrect shape')
