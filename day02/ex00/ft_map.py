# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/17 11:28:57 by mli               #+#    #+#              #
#    Updated: 2020/01/17 11:36:32 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, list_of_inputs):
    res = []
    for element in list_of_inputs:
        res.append(function_to_apply(element))
    return (res)


'''
lst = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
print(list(ft_map(lambda x: x*2 , lst)))

# [10, 14, 44, 194, 108, 124, 154, 46, 146, 122]
'''
