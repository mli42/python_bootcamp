# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 14:04:18 by mli               #+#    #+#              #
#    Updated: 2020/01/13 15:19:53 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

reversed_str = str()
argc = len(sys.argv)

for i in range(1, argc):
    arg = sys.argv[argc - i]
    reversed_str += arg[::-1]
    if (i != argc - 1):
        reversed_str += " "
print (str(reversed_str).swapcase())
