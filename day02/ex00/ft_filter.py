# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/17 11:28:57 by mli               #+#    #+#              #
#    Updated: 2020/01/17 11:32:34 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function_to_apply, list_of_inputs):
    res = []
    for element in list_of_inputs:
        if (function_to_apply(element) == True):
            res.append(element)
    return (res)

'''
seq = [0, 1, 2, 3, 5, 8, 13]
print(ft_filter(lambda x: x % 2, seq))
print(ft_filter(lambda x: x % 2 == 0, seq))
'''
