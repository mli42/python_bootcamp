# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 14:04:18 by mli               #+#    #+#              #
#    Updated: 2020/11/11 16:40:21 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Reverses the order of a string and the case of its words.
"""

import sys

res = []
for arg in sys.argv[:0:-1]:
    res.append(arg[::-1])
if len(res) != 0:
    print(" ".join(res).swapcase())
