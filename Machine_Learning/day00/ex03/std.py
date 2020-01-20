# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    std.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/20 12:14:10 by mli               #+#    #+#              #
#    Updated: 2020/01/20 13:31:44 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from math import sqrt

def mean_f(x, f=None):
    width = len(x)
    if (width == 0):
        return (None)
    res = float(0)
    for nb in x:
        res += f(nb) if f != None else nb
    return (res / width)

def variance(x):
    mu = mean_f(x)
    f = (lambda x : (x - mu) ** 2)
    return (mean_f(x, f) if (mu != None) else mu)

def std(x):
    var = variance(x)
    return (sqrt(var) if (var != None) else var)

'''
print("First Test")
X = np.array([0, 15, -9, 7, 12, 3, -21])
print(std(X))
print(np.std(X))

print("\nSecond Test")
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(std(Y))
print(np.std(Y))
'''
