# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 17:45:09 by mli               #+#    #+#              #
#    Updated: 2020/01/16 22:58:49 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# magic methods

class Vector:
    def __init__(self, a=None, b=0):
        if (isinstance(a, (list, int, range, tuple)) == False or isinstance(b, int) == False):
            exit(print("Error of use. Give a list, a tuple, a range, or (one/two) integers"))

        value = []
        if (isinstance(a, list)):
            for nb in a:
                if (isinstance(nb, (int, float)) == False):
                    exit(print("List should contains only floats or int"))
                value.append(float(nb))
        elif (isinstance(a, int)):
            if (a > b):
                a, b = b, a
            for nb in range(a, b):
                value.append(float(nb))
        elif (isinstance(a, (tuple, range))):
            if (isinstance(a, tuple)):
                a = range(a[0], a[-1])
            for nb in a:
                value.append(float(nb))
        value.sort()
        self.value = value
        self.size = len(value)

    def __repr__(self):
        return ("Value : %s | Size : %d" %(str(self.value), self.size))

    def __str__(self):
        if (isinstance(self.value, (int, float))):
            return ("Value : %s | Size : %d" %(str(self.value), self.size))
        if (isinstance(self.value, list)):
            return ("Value : %s | Size : %d" %(str(self.value)[1 : -1], self.size))

    def __add__(self, other):
        if (isinstance(other, (int, float)) and isinstance(self.value, (int, float))):
            return (self.value + other)
        elif (isinstance(other, list) and isinstance(self.value, list) and (len(other) == self.size)):
            res = []
            for i in range(0, self.size - 1):
                res.append(self.value[i] + other[i])
            return (res)
        elif (isinstance(other, Vector) and isinstance(self.value, list) and (other.size == self.size)):
            res = []
            for i in range(0, self.size - 1):
                res.append(self.value[i] + other.value[i])
            return (res)
        else:
            exit(print("Error, format not good"))

#print(Vector([0.0, 1.0, 5.0, 3.0]).value)
#print(Vector(3).value)
#print(Vector((10, 15)).value)
#print(Vector(range(20, 25)).value)

vect = Vector(range(20, 25))

vect1 = Vector(range(20, 25))

print(repr(vect))
print(str(vect))

print(vect + vect1)
print(vect + [2, 3, 1, 5, 6])



'''
Following are differences (repr vs str):
Repr’s goal is to be unambiguous and str’s is to be readable.

str() is used for creating output for end user
(a representation that is useful for printing the object).

While repr() is mainly used for debugging and development.
(a representation that has all information about the abject)
'''


