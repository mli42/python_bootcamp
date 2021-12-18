# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/17 11:28:57 by mli               #+#    #+#              #
#    Updated: 2021/12/18 19:42:54 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_reduce(function_to_apply, iterable):
    if not hasattr(iterable, '__iter__') or (len(iterable) == 0) or \
        not callable(function_to_apply):
        return None

    res = iterable[0]
    for element in iterable[1:]:
        res = function_to_apply(res, element)
    return (res)

if __name__ == "__main__":
    # from functools import reduce
    lst = [5, 10, 20, 50, 100]
    fct_sum = lambda x, y: x + y

    print(ft_reduce(fct_sum, lst))
    print(ft_reduce(fct_sum , []))
    print(ft_reduce(fct_sum , None))
    print(ft_reduce(None, lst))
