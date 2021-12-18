# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/17 11:28:57 by mli               #+#    #+#              #
#    Updated: 2021/12/18 19:25:06 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function_to_apply, iterable):
    def get_filter_generator():
        for element in iterable:
            if (function_to_apply(element) == True):
                yield (element)

    if not hasattr(iterable, '__iter__') or \
        not callable(function_to_apply):
        return None
    return get_filter_generator()


if __name__ == "__main__":
    fct = lambda x: (x % 2 == 0)
    iter_var = range(10) # [0, 1, 2, ..., 9]

    print(ft_filter(fct, iter_var))
    print(*ft_filter(fct, iter_var))
    # [0, 2, 4, ..., 8]

    print(ft_filter(fct, 5))
    # None

    print(ft_filter("Not function" , iter_var))
    # None
