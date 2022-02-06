# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/19 19:05:40 by mli               #+#    #+#              #
#    Updated: 2022/02/06 15:05:30 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class NumPyCreator:

    @staticmethod
    def __guard_simple_or_nested(array: list or tuple, what: type) -> bool:
        if (not isinstance(array, what)):
            return False
        is_type = [isinstance(obj, what) for obj in array]
        if not any(is_type): # if there aren't any what-type
            return True
        elif not all(is_type): # if there is some, but not all
            return False

        # They are all what-type
        size = None
        for elem in array:
            if size is None:
                size = len(elem)
            elif len(elem) != size:
                return False
        return True

    @staticmethod
    def __guard_shape(shape) -> bool:
        if not (isinstance(shape, tuple) and len(shape) == 2
        and all([(isinstance(obj, int) and obj >= 0) for obj in shape])):
            return False
        return True

    @staticmethod
    def from_list(lst):
        if (not NumPyCreator.__guard_simple_or_nested(lst, list)):
            return None
        return (np.asarray(lst))

    @staticmethod
    def from_tuple(tpl):
        if (not NumPyCreator.__guard_simple_or_nested(tpl, tuple)):
            return None
        return (np.asarray(tpl))

    @staticmethod
    def from_iterable(itr):
        if not hasattr(itr, '__iter__'):
            return None
        return (np.fromiter(itr, int))

    @staticmethod
    def from_shape(shape, value=0):
        if not (NumPyCreator.__guard_shape(shape)):
            return None
        return (np.full(shape, value))

    @staticmethod
    def random(shape):
        if not (NumPyCreator.__guard_shape(shape)):
            return None
        return (np.random.random(shape))

    @staticmethod
    def identity(n):
        if not (isinstance(n, int) and n >= 0):
            return None
        return (np.eye(n))


def main():
    display_repr = lambda x: print(repr(x))
    npc = NumPyCreator()

    display_repr(npc.from_list([[1,2,3],[6,3,4]]))
    # array([[1, 2, 3], [6, 3, 4]])

    display_repr(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
    # array([['1', '2', '3'], ['a', 'b', 'c'], ['6', '4', '7']], dtype='<U21')

    display_repr(npc.from_list(((1,2),(3,4))))
    # None

    display_repr(npc.from_tuple(('a','b','c')))
    # array(['a', 'b', 'c'], dtype='<U1')

    display_repr(npc.from_tuple([[1,2,3],[6,3,4]]))
    # None

    display_repr(npc.from_iterable(range(5)))
    # array([0, 1, 2, 3, 4])

    shape=(3,5)
    display_repr(npc.from_shape(shape))
    # array([[0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0]])

    display_repr(npc.random(shape))
    # with 0 < x < 1
    # array([[x, x, x, x, x],
    #        [x, x, x, x, x],
    #        [x, x, x, x, x]])

    display_repr(npc.identity(4))
    # array([[1., 0., 0., 0.],
    #        [0., 1., 0., 0.],
    #        [0., 0., 1., 0.],
    #        [0., 0., 0., 1.]])

    display_repr(npc.from_list([[],[]]))
    # array([], shape=(2, 0), dtype=float64)

    display_repr(npc.from_list([[1,2,3],[6,3,4],[8,5,6]]))
    # array([[1, 2, 3],
    #        [6, 3, 4],
    #        [8, 5, 6]])

    display_repr(npc.from_shape((0, 0)))
    # array([], shape=(0, 0), dtype=float64)

    print("Expect None * 6")
    display_repr(npc.from_list("toto"))
    display_repr(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
    display_repr(npc.from_tuple(3.2))
    display_repr(npc.from_tuple(((1,5,8),(7,5))))
    display_repr(npc.from_shape((-1, -1)))
    display_repr(npc.identity(-1))
    print("End of None")

if __name__ == "__main__":
    main()
