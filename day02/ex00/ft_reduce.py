# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/17 11:28:57 by mli               #+#    #+#              #
#    Updated: 2020/01/17 11:44:11 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_reduce(function_to_apply, list_of_inputs):
    res = list_of_inputs[0]
    for element in list_of_inputs[1 : ]:
        res = function_to_apply(res, element)
    return (res)

'''
#from functools import reduce
lst = [5, 8, 10, 20, 50, 100]
print (ft_reduce((lambda x, y: x + y), lst))
#Output = 193
'''
