# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/07 18:36:21 by mli               #+#    #+#              #
#    Updated: 2020/12/08 00:09:11 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Matrix:
    def __init__(self, elements: list = None, shape: tuple = None) -> None:
        if isinstance(elements, list):
            self.data = elements.copy()
            self.shape = (len(elements), len(elements[0]))
        elif isinstance(shape, tuple):
            self.shape = shape
            self.data = [[0] * self.shape[1] for tmp in range(self.shape[0])]

    def __add__(self, other):
        # add : vectors and matrices, can have errors with vectors and matrices.
        if isinstance(other, Matrix) and self.shape != other.shape:
            return
        res = Matrix(shape=(self.shape))
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                res.data[i][j] = self.data[i][j] + other.data[i][j]
        return res

    def __sub__(self, other):
        # sub : vectors and matrices, can have errors with vectors and matrices.
        if isinstance(other, Matrix) and self.shape != other.shape:
            return
        res = Matrix(shape=(self.shape))
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                res.data[i][j] = self.data[i][j] - other.data[i][j]
        return res

    def __truediv__(self, other):
        # div : only scalars.
        if not isinstance(other, (int, float)):
            return
        res = Matrix(shape=(self.shape))
        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                res.data[i][j] = self.data[i][j] / other
        return res

    def __mul__(self, other):
        # mul : scalars, vectors and matrices , can have errors with vectors and matrices.
        # if we perform Matrix * Vector (dot product), return a Vector.
        res = None
        if isinstance(other, (int, float)):
            res = Matrix(shape=(self.shape))
            for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    res.data[i][j] = self.data[i][j] * other
        elif isinstance(other, Matrix):
            common_len = self.shape[1]
            res = Matrix(shape=(self.shape[0], other.shape[1]))
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
        return "(Matrix %s)" %(self.data)
    def __repr__(self) -> str:
        return "(Matrix %s)" %(self.data)

if __name__ == "__main__":
    m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
                 [0.0, 2.0, 4.0, 6.0]])
    m2 = Matrix([[10, 10, 10, 10],
                 [10, 10, 10, 10]])
    m3 = Matrix([[0.0, 1.0],
                 [2.0, 3.0],
                 [4.0, 5.0],
                 [6.0, 7.0]])
    #print(m1 + m2)
    #print(m1 - m2)
    #print(m3 * 2)
    #print(m3 / 2)
    print(m1 * m3)
    #print(Matrix(shape=(5,3)))

    import numpy as np
    np1 = np.array([[0.0, 1.0, 2.0, 3.0],
                    [0.0, 2.0, 4.0, 6.0]])
    np2 = np.array([[0.0, 1.0],
                    [2.0, 3.0],
                    [4.0, 5.0],
                    [6.0, 7.0]])
    print(np1.dot(np2))
