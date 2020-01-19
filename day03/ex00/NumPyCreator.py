# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 19:05:40 by mli               #+#    #+#              #
#    Updated: 2020/01/19 22:47:10 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class NumPyCreator:

    @staticmethod
    def from_list(lst):
        return (np.asarray(lst))

    @staticmethod
    def from_tuple(tpl):
        return (np.asarray(tpl))

    @staticmethod
    def from_iterable(itr):
        return (np.fromiter(itr, float))

    @staticmethod
    def from_shape(shape, value=0):
        return (np.full(shape, value))

    @staticmethod
    def random(shape):
        return (np.random.random(shape))

    @staticmethod
    def identity(n):
        return (np.eye(n))
