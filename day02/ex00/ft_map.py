# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/17 11:28:57 by mli               #+#    #+#              #
#    Updated: 2021/12/18 18:37:56 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, iterable):
    def get_map_generator():
        for element in iterable:
            yield (function_to_apply(element))

    if not hasattr(iterable, '__iter__') or \
        not callable(function_to_apply):
        return None
    return get_map_generator()


if __name__ == "__main__":
    iter_var = range(10) # [0, 1, 2, ..., 9]
    print(ft_map(lambda x: x*2 , iter_var))
    # [0, 2, 4, ..., 18]

    print(ft_map(lambda x: x*2 , 5))
    # None

    print(ft_map("Not function" , iter_var))
    # None
