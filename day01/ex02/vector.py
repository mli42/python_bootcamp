# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/15 17:45:09 by mli               #+#    #+#              #
#    Updated: 2020/01/15 18:37:48 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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


#print(Vector([0.0, 1.0, 5.0, 3.0]).value)
#print(Vector(3).value)
#print(Vector((10, 15)).value)
#print(Vector(range(20, 25)).value)
